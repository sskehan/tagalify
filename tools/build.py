import importlib, json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "tagalify", "data"))
sys.path.insert(0, HERE)

ALIAS = {"verb": "pred", "adj": "pred", "adv": "pred", "num": "noun", "expr": "other"}
ROLES = {"marker", "noun", "pred", "pron", "link", "ay", "poss", "part", "other"}
POS = {"noun", "verb", "adj", "adv", "pron", "marker", "link", "part", "phrase", "expr", "num", "other"}
errors, warns = [], []


def role(r):
    return ALIAS.get(r, r)


INLINE = re.compile(r"\[\[([^\]|]+)(?:\|([a-z]+))?\]\]")


def fix_text(s, where):
    def sub(m):
        t, r = m.group(1), m.group(2)
        if r is None:
            return m.group(0)
        r2 = role(r)
        if r2 not in ROLES:
            errors.append(f"{where}: bad inline role {r!r} in {m.group(0)}")
        return f"[[{t}|{r2}]]"
    return INLINE.sub(sub, s)


def walk(o, where):
    if isinstance(o, str):
        return fix_text(o, where)
    if isinstance(o, list):
        return [walk(x, where) for x in o]
    if isinstance(o, dict):
        d = {}
        for k, v in o.items():
            if k == "r":
                d[k] = role(v)
                if d[k] not in ROLES:
                    errors.append(f"{where}: bad chip role {v!r}")
            else:
                d[k] = walk(v, where)
        return d
    return o


def fix_blocks(blocks, where):
    for b in blocks:
        if b["type"] == "examples":
            for it in b["items"]:
                for p in it["parts"]:
                    if len(p) != 3:
                        errors.append(f"{where}: bad part {p}")
                        continue
                    p[2] = role(p[2])
                    if p[2] not in ROLES:
                        errors.append(f"{where}: bad part role {p}")


def norm(s):
    return re.sub(r"[.,?!]", "", s).lower().split()


def validate(L):
    i = L["id"]
    for k in ("id", "label", "title", "summary", "minutes", "goals", "sections", "vocab", "exercises", "recap"):
        if k not in L:
            errors.append(f"{i}: missing {k}")
    groups = {v["group"] for v in L["vocab"]}
    for v in L["vocab"]:
        if v["pos"] not in POS:
            errors.append(f"{i}: vocab {v['id']} bad pos {v['pos']}")
    for s in L["sections"]:
        for b in s["blocks"]:
            if b["type"] == "vocab" and b["group"] not in groups:
                errors.append(f"{i}: vocab block group {b['group']} missing")
    for n, e in enumerate(L["exercises"]):
        w = f"{i} ex{n + 1}"
        t = e["type"]
        if t in ("choice", "listen"):
            if e["answer"] not in e["options"]:
                errors.append(f"{w}: answer not in options: {e['answer']!r}")
            if len(set(e["options"])) != len(e["options"]):
                errors.append(f"{w}: duplicate options")
        elif t == "build":
            if [x for x in e["tokens"]] != norm(e["tl"]) and e["tokens"] != norm(e["tl"]):
                warns.append(f"{w}: custom tokens {e['tokens']}")
            if "".join(e["tokens"]).replace(" ", "") != "".join(norm(e["tl"])) and not e.get("tokens"):
                errors.append(f"{w}: tokens mismatch")
        elif t == "match":
            if len(e["pairs"]) < 2:
                errors.append(f"{w}: <2 pairs")
            left = [p[0] for p in e["pairs"]]
            right = [p[1] for p in e["pairs"]]
            if len(set(left)) != len(left) or len(set(right)) != len(right):
                errors.append(f"{w}: duplicate pair side")
        else:
            errors.append(f"{w}: unknown type {t}")


def main():
    os.makedirs(os.path.join(OUT, "lessons"), exist_ok=True)
    lessons = []
    for f in sorted(glob.glob(os.path.join(HERE, "c[0-9][0-9]_*.py"))):
        name = os.path.basename(f)[:-3]
        if name == "c10_reference":
            continue
        mod = importlib.import_module(name)
        lessons.append(mod.LESSON)
    seen = {}
    for L in lessons:
        fix_blocks([b for s in L["sections"] for b in s["blocks"]], L["id"])
        L2 = walk(L, L["id"])
        validate(L2)
        for v in L2["vocab"]:
            if v["id"] in seen:
                errors.append(f"duplicate vocab id {v['id']} in {L['id']} and {seen[v['id']]}")
            seen[v["id"]] = L["id"]
        with open(os.path.join(OUT, "lessons", L["id"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(L2, fh, ensure_ascii=False, indent=1)
        L["_out"] = L2
    # duplicate tl+en across lessons (info only)
    tlseen = {}
    for L in lessons:
        for v in L["_out"]["vocab"]:
            k = v["tl"].lower()
            if k in tlseen and tlseen[k][1] == v["en"]:
                warns.append(f"same word+meaning {k!r} in {tlseen[k][0]} and {L['id']}")
            tlseen[k] = (L["id"], v["en"])

    units = [
        {"id": "start", "title": "Start here", "lessons": ["primer", "background"]},
        {"id": "basics", "title": "Sounds and greetings", "lessons": ["l01", "l02", "l03"]},
        {"id": "sentences", "title": "Building sentences", "lessons": ["l04", "l05", "l06"]},
        {"id": "connect", "title": "Joining and owning", "lessons": ["l07", "l08"]},
        {"id": "questions", "title": "Asking and comparing", "lessons": ["l09", "l10", "l11"]},
        {"id": "having", "title": "Having and counting", "lessons": ["l12", "l13"]},
        {"id": "verbs1", "title": "Action words (verbs)", "lessons": ["l14", "l15", "l16"]},
        {"id": "verbs2", "title": "Wanting, able, becoming, having", "lessons": ["l17", "l18", "l19", "l20"]},
        {"id": "express", "title": "Thoughts, feelings and requests", "lessons": ["l21", "l22", "l23", "l24", "l25"]},
        {"id": "where-when", "title": "Where, for whom and when", "lessons": ["l26", "l27", "l28", "l29", "l30"]},
        {"id": "making-words", "title": "Nouns, more verbs and adverbs", "lessons": ["l31", "l32", "l33", "l34"]},
        {"id": "joining-ideas", "title": "Joining ideas and agreeing", "lessons": ["l35", "l36", "l37", "l38", "l39"]},
        {"id": "word-building", "title": "Building words, and colours", "lessons": ["l40", "l41", "l42", "l43", "l44"]},
        {"id": "appendices", "title": "Appendices: food, idioms and conversation", "lessons": ["a01", "a02", "a03", "a04", "a05", "a06", "a07"]},
        {"id": "review", "title": "Review exercises", "lessons": ["r1", "r2", "r3", "r4"]},
    ]
    by = {L["id"]: L for L in lessons}
    for u in units:
        miss = [lid for lid in u["lessons"] if lid not in by]
        for lid in miss:
            warns.append(f"unit lesson {lid} missing (skipped)")
        u["lessons"] = [lid for lid in u["lessons"] if lid in by]
    units = [u for u in units if u["lessons"]]
    index = {"app": "Tagalify", "version": "2.01", "units": [], "lessons": []}
    for u in units:
        index["units"].append({"id": u["id"], "title": u["title"], "lessons": u["lessons"]})
    for L in lessons:
        o = L["_out"]
        index["lessons"].append({"id": o["id"], "label": o["label"], "title": o["title"], "summary": o["summary"],
                                 "minutes": o["minutes"], "file": f"data/lessons/{o['id']}.json",
                                 "words": len(o["vocab"]), "exercises": len(o["exercises"])})
    with open(os.path.join(OUT, "course.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)

    ref = importlib.import_module("c10_reference").REFERENCE
    ref = walk(ref, "reference")
    with open(os.path.join(OUT, "reference.json"), "w", encoding="utf-8") as fh:
        json.dump(ref, fh, ensure_ascii=False, indent=1)

    for w in warns:
        print("warn:", w)
    for e in errors:
        print("ERROR:", e)
    tot_w = sum(len(L["_out"]["vocab"]) for L in lessons)
    tot_e = sum(len(L["_out"]["exercises"]) for L in lessons)
    print(f"{len(lessons)} lessons, {tot_w} words, {tot_e} exercises, {len(errors)} errors")
    sys.exit(1 if errors else 0)


main()
