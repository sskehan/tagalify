"""Tiny helpers for writing Tagalify lessons as Python, then exporting JSON."""
import re

ROLES = {"marker", "noun", "pred", "pron", "link", "ay", "poss", "part", "other"}
POS = {"noun", "verb", "adj", "adv", "pron", "marker", "link", "part", "phrase", "expr", "num", "other"}


def P(t):
    return {"type": "p", "t": t}


def H(t):
    return {"type": "h", "t": t}


def BOX(kind, title, items=None, t=None):
    """kind: rule | tip | warn | remember | culture | english"""
    b = {"type": "box", "kind": kind, "title": title}
    if items:
        b["items"] = items
    if t:
        b["t"] = t
    return b


def PAT(title, rows, note=None):
    """rows = [(label, [(text, role), ...]), ...]"""
    b = {"type": "pattern", "title": title,
         "rows": [{"label": lab, "chips": [{"t": t, "r": r} for t, r in chips]} for lab, chips in rows]}
    if note:
        b["note"] = note
    return b


def TABLE(head, rows, title=None, note=None):
    b = {"type": "table", "head": head, "rows": rows}
    if title:
        b["title"] = title
    if note:
        b["note"] = note
    return b


def EXS(items, title=None):
    """items = [(tl, en, [(word, gloss, role), ...]), ...]"""
    out = []
    for tl, en, parts in items:
        out.append({"tl": tl, "en": en, "parts": [list(p) for p in parts]})
    b = {"type": "examples", "items": out}
    if title:
        b["title"] = title
    return b


def VOC(group, title=None):
    b = {"type": "vocab", "group": group}
    if title:
        b["title"] = title
    return b


def LEGEND():
    return {"type": "legend"}


def S(title, *blocks):
    return {"title": title, "blocks": list(blocks)}


def V(id, tl, en, say=None, pos="noun", group="words", note=None):
    d = {"id": id, "tl": tl, "en": en, "pos": pos, "group": group}
    if say:
        d["say"] = say
    if note:
        d["note"] = note
    return d


# ---- exercises ----
def CH(q, options, answer, explain="", tl=None):
    d = {"type": "choice", "q": q, "options": options, "answer": answer, "explain": explain}
    if tl:
        d["tl"] = tl
    return d


def LI(tl, options, answer, explain=""):
    return {"type": "listen", "tl": tl, "options": options, "answer": answer, "explain": explain}


def BU(en, tl, extra=None, explain="", tokens=None):
    if tokens is None:
        tokens = [re.sub(r"[.,?!]", "", w).lower() for w in tl.split()]
    d = {"type": "build", "en": en, "tl": tl, "tokens": tokens, "explain": explain}
    if extra:
        d["extra"] = extra
    return d


def MA(q, pairs):
    return {"type": "match", "q": q, "pairs": [list(p) for p in pairs]}
