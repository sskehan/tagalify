from dsl import *

# Review Exercises, Parts III and IV (book pages 220-221), with the Answer key (pages 226-227).
# Every Tagalog item is copied as printed, accents included. Items whose answer the book
# does not print are shown as "Your turn" prompts only.

TRY = "Try it yourself first, then check."

PRON = [
    "Ang kapatíd ko ay marúnong. ______ ay nag-áaral na mabúti.",
    "Ang mga batà ay kumákain. ______ ay nagúgutom.",
    "Maráming pera si Ramon. Iyón ay ibinigáy ng ______ amá.",
    "Halíka, Helen. Sumama ______ sa amin.",
    "Kúnin ______ ang aklát sa mesa.",
    "______ lahát ay ináanyayáhan niya.",
    "Mayróon ba kayong pagkáin para sa ______?",
    "Hindi isináma si Peter sa sine. Umíiyak ______.",
    "Isáng aráw, ______ ay nagpasyál sa Luneta.",
    "Nákita ______ ang maráming bapór sa dágat.",
    "Kúnin ______ ang inyóng aklát.",
    "Isáma ninyó ako kung púpunta ______ sa Baguio.",
    "Ang báhay ______ ay nasa Pandácan.",
    "Nákita ______ na ba ang Tagaytáy?",
    "______ ay mga tunay na kaibigan.",
    "Sila ay magbábakasyon sa ______ baháy.",
    "Gabí na nang ______ ay umalis.",
    "Huwág ______ magágalit sa akin.",
    "Nalúlungkot ba ______?",
    "Marámi ______ bang kaibígan sa Maynila?",
    "Magsalitâ ______ ng Tagalog sa áting kláse.",
]

PRON_ANS = ["siya", "sila", "kanyang", "ka", "mo", "kaming", "amin; akin; kanila", "siya", "kami; sila",
            "namin; nila", "mo; ninyo", "kayo", "ko; namin", "mo", "sila; kayo; kami", "aming; ating; inyong",
            "(any nominative pronoun)", "kang; kayong", "kayo; sila", "ka", "ka; kayo"]

MISSING = [
    "Ang papél at plúma ay gámit sa ______.",
    "Sina Tom at Mary ay ______.",
    "Ang ______ ay para sa mga nagúgutom.",
    "Ang ______ ay mabangó at magandá.",
    "Si Mang Tomas ay nagtátanim. Siya ay ______.",
    "Si Gng. Cruz ay nagtúturo. Siya ay ______.",
    "Tayo ay umíinom ng ______ kapag naúuhaw.",
    "Maráming nábabasa sa mga ______.",
    "Ang bátang ______ ay nakatútuwâ.",
    "Ang bátang ______ ay nakagágalit.",
]

MISSING_ANS = ["pagsúlat", "magkaibígan; magkapatíd; etc.", "pagkáin", "bulaklák", "magsasaká", "gurò", "túbig",
               "páhayagan; aklát; mágasin", "mabaít; magandá", "masamâ"]

ADJ = [
    "Si John ay bása nang bása. Siya ay maraming nálalaman. Nasásagot niya ang lahát ng tinátanong ng gurò. Si John ay ______.",
    "Ang dálaga ay laging naglílinis ng kanilang baháy. Siya ang naglúlutò ng pagkáin. Siya ang naglálabá ng mga damít. Ang dalága ay ______.",
    "Ayaw niyáng magtrabáho. Gusto niya ay matúlog lamang. Siya ay hindî tumútulong sa kanyáng iná. Kung may gágawin sa báhay siya ay umáalis. Bumabalik lamang siyá kung kákain. Siya ay ______.",
    "Hindi niya mákita ang kanyang kaúsap. Ang lahát ay madilím. Ang mga bulaklák ay waláng kúlay para sa kanyá. Siya ay ______.",
    "Mahírap si Peter. Walâ siyáng pagkain. Walâ siyáng damít. Walâ siyáng mga magúlang. Si Peter ay ______.",
]

ADJ_ANS = ["marúnong", "masípag", "tamád", "bulág", "kaáwa-awà"]

QUEST = [
    "Pumunta ba kayo sa palengke kahapon?",
    "Nagsasalita na ba kayo ng Tagalog?",
    "Umiinom ka ba ng kape sa umaga? (in the morning)",
    "Aalis na ba kayo? Hindi pa ako aalis.",
    "Sumulat ba kayo sa inyong kaibigan sa Amerika?",
]

TRANS = [
    ("I bought a big house in Quezon City.", "Bumili ako ng isang malaking bahay sa Quezon City."),
    ("We read (or are reading) in the class.", "Bumabasa kami sa klase."),
    ("We shall go to your house tomorrow.", "Pupunta kami sa inyong bahay bukas."),
    ("Peter's clothes are clean.", "Malinis ang mga damit ni Peter."),
    ("My dress is not clean.", "Hindi malinis ang aking baro."),
]

ARTS = [
    "______ bisita ______ bagong kasal ay mga kaibigan at kamag-anak ______ kanilang bayan.",
    "Kami ang sumakay ______ kotse, kasama ______ katulong at ______ anak ko.",
    "______ bahay ______ aming kaibigan ay nasa Nueva Ecija.",
    "Umalis kami ______ Maynila nang ika – 10:00 ______ umaga.",
    "Maraming pagkain ______ mahabang mesa.",
    "Maganda ______ asawa ______ aking kaibigan.",
]

ARTS_ANS = [
    "Ang mga bisíta ng bágong kasál ay mga kaibígan at kamag-ának sa kanilang báyan.",
    "Kami ay sumakay sa kotse, kasáma ang katúlong at ang anak ko.",
    "Ang bahay ng aming kaibígan ay nasa Nueva Ecija.",
    "Umalís kami sa Maynila nang ika-10:00 ng umaga.",
    "Maraming pagkáin sa mahábang mesa.",
    "Magandá ang asawa ng aking kaibígan.",
]


def rows(items):
    return [[f"{n}.", t] for n, t in enumerate(items, 1)]


def answers(items):
    return [TRY] + [f"{n}. {t}" for n, t in enumerate(items, 1)]


def pron_q(n):
    return f"Part III A {n}. Fill in the pronoun: \"{PRON[n - 1]}\""


LESSON = {
    "id": "r2",
    "label": "R2",
    "title": "Review: Parts III and IV – pronouns, describing words and ang, ng, sa",
    "summary": "The book's review exercises Parts III and IV: filling in pronouns, missing words and describing words, answering ba questions, translating sentences, and choosing ang, ng or sa",
    "minutes": 35,
    "goals": [
        "Choose the right pronoun form for each place in a sentence",
        "Fill in missing nouns and describing words from the clues",
        "Answer yes/no questions with ba in complete sentences",
        "Translate short sentences about buying, reading, going and being clean",
        "Fill in ang, ng and sa (and their plural forms)",
    ],
    "sections": [
        S("About this review",
          P("This lesson covers **Part III** and **Part IV** of the book's Review Exercises. Each section is one lettered exercise, with the book's instruction and items exactly as printed, followed by the book's answer where the Answer key gives one."),
          BOX("tip", "How to use this lesson", items=[
              "Cover the answer, fill in each blank yourself, then open **The book's answer**.",
              "When the book gives several answers separated by semicolons, any of them is correct.",
              "Each section ends with a **Revise** line telling you which lesson teaches that point."])),

        S("Part III A. Fill in the pronouns",
          P("The book's instruction: **Fill in the blanks with the correct pronouns:**"),
          TABLE(["", "Sentence"], rows(PRON), title="Part III A (page 220)"),
          BOX("tip", "The book's answer", items=answers(PRON_ANS)),
          BOX("rule", "How to choose", items=[
              "Before **ay**, or as the subject, use a subject pronoun: **siya**, **sila**, **kami**, **kayo** (Lesson 6).",
              "**Ka** follows the predicate; **ikáw** starts a sentence (Lesson 6): **Sumama ka sa amin.**",
              "The doer of an -in- verb takes the possessive form: **Kúnin mo ang aklát** (Lessons 8 and 15).",
              "Before a noun, a possessive pronoun takes a ligature: **ng kanyang amá**, **sa aming baháy** (Lesson 8)."]),
          BOX("warn", "Book spellings", items=[
              "Item 13 prints **báhay** and item 16 prints **baháy**.",
              "Item 17's answer is printed as *(any nominative pronoun)*: any subject pronoun such as siya, sila or kami fits."]),
          P("*Revise: Lesson 6 (personal pronouns) and Lesson 8 (possessive pronouns).*")),

        S("Part III B. The missing words",
          P("The book's instruction: **What are the missing words in the following sentences?**"),
          TABLE(["", "Sentence"], rows(MISSING), title="Part III B (page 220)"),
          BOX("tip", "The book's answer", items=answers(MISSING_ANS))),

        S("Part III C. The right describing word",
          P("The book's instruction: **Fill in with the appropriate adjective.** Each short passage describes a person; the last line needs one adjective that sums them up."),
          TABLE(["", "Passage"], rows(ADJ), title="Part III C (pages 220-221)"),
          BOX("tip", "The book's answer", items=answers(ADJ_ANS)),
          BOX("warn", "Book spellings", items=[
              "Passage 2 prints both **dálaga** and **dalága**.",
              "Passage 2 prints **baháy**; passage 3 prints **báhay**.",
              "Passage 4 prints **kanyang** and **kanyá**; passage 3 prints **kanyáng**."])),

        S("Part III D. Five examples",
          P("The book's instruction: **Write five examples for each of the following categories.** The categories are **mga hayop**, **mga pagkain**, **mga gawain** and **mga hanapbuhay**."),
          BOX("tip", "Your turn", items=[
              "Write five Tagalog words for each category, numbered 1 to 5.",
              "The book gives no single answer for this exercise."])),

        S("Part IV A. Answer in complete sentences",
          P("The book's instruction: **Answer the following questions in complete sentences.**"),
          TABLE(["", "Question"], rows(QUEST), title="Part IV A (page 221)"),
          BOX("tip", "Your turn", items=[
              "Answer each question about yourself with **Oo** or **Hindi**, in a complete sentence.",
              "The Answer key prints no answer for this exercise."]),
          BOX("warn", "Book slip", t="Item 4 prints a reply after the question: **Aalis na ba kayo? Hindi pa ako aalis.** It is shown as printed."),
          P("*Revise: Lesson 10 (the question word ba).*"),
          VOC("words", "Word from this page")),

        S("Part IV B. Translate into Tagalog",
          P("The book's instruction: **Translate the following sentences into Tagalog.**"),
          TABLE(["", "English"], rows([e for e, _ in TRANS]), title="Part IV B (page 221)"),
          BOX("tip", "The book's answer", items=answers([t for _, t in TRANS])),
          BOX("warn", "Book spelling", t="These answers are printed without accent marks."),
          P("*Revise: Lesson 14 (-um- and mag- verb forms).*")),

        S("Part IV C. Ang, ng or sa",
          P("The book's instruction: **Fill in the blanks with ang, ng, sa or their plural forms.** **Ang** marks the main character, **ng** links an owner or the other characters, and **sa** marks the place."),
          TABLE(["", "Sentence"], rows(ARTS), title="Part IV C (page 221)"),
          BOX("tip", "The book's answer", items=answers(ARTS_ANS)),
          BOX("warn", "Book slips", items=[
              "In item 2 the question prints **Kami ang sumakay**, but the answer prints **Kami ay sumakay**. Item 2 is not used in the exercises.",
              "The answers add accent marks that the questions do not have (bisíta, kaibígan, mahábang…), and item 4 prints **Umalis** in the question and **Umalís** in the answer."]),
          BOX("remember", "Remember", items=[
              "Subject or before ay: **siya**, **sila**, **kami**, **kayo**; after the predicate: **ka**.",
              "Doer of an -in- verb: **mo**, **ninyo**, **namin**.",
              "Possessive pronoun before a noun: **kanyang**, **aming**, **inyong**.",
              "**Ang** for the main character, **ng** for the owner, **sa** for the place: **Ang bahay ng aming kaibígan ay nasa Nueva Ecija.**"]),
          P("*Revise: Lesson 16 (the articles ang and ng) and Lesson 26 (the preposition sa).*")),
    ],
    "vocab": [
        V("sa-umaga-r2", "sa umaga", "in the morning", pos="phrase", group="words",
          note="Printed in Part IV A: Umiinom ka ba ng kape sa umaga? (in the morning)"),
    ],
    "exercises": [
        # Part III A
        CH(pron_q(1), ["siya", "niya", "kanya"], "siya", "Before ay the subject pronoun is needed: Siya ay nag-áaral (Lesson 6)."),
        CH(pron_q(2), ["sila", "nila", "kanila"], "sila", "Before ay the subject pronoun is needed: Sila ay nagúgutom."),
        CH(pron_q(3), ["kanyang", "kanya", "siya"], "kanyang",
           "Before the noun amá the possessive pronoun needs the ligature -ng: ng kanyang amá (Lesson 8)."),
        CH(pron_q(4), ["ka", "mo", "ikaw"], "ka", "Helen is the one who goes along. After the verb, you is ka; ikáw starts a sentence (Lesson 6)."),
        CH(pron_q(5), ["mo", "ka", "ikaw"], "mo", "Kúnin is an -in- verb, so the doer takes the possessive form mo (Lesson 15)."),
        CH(pron_q(12), ["kayo", "ninyo", "inyo"], "kayo", "The book's answer is kayo: you (plural) are the ones going."),
        CH(pron_q(14), ["mo", "ka", "ikaw"], "mo", "The book's answer is mo, the possessive form, as with Kúnin mo."),
        CH(pron_q(18), ["kang (or kayong)", "mo", "niya"], "kang (or kayong)",
           "The book's answer is kang or kayong: ka or kayo + the ligature -ng, as in Huwág kang umalís (Lesson 37)."),
        CH(pron_q(21), ["ka (or kayo)", "mo", "ninyo"], "ka (or kayo)",
           "The book's answer is ka or kayo: the one who speaks is the subject."),
        # Part III B
        CH("Part III B 1. \"Ang papél at plúma ay gámit sa ______.\"", ["pagsúlat", "túbig", "bulaklák"], "pagsúlat",
           "The book's answer is pagsúlat."),
        CH("Part III B 3. \"Ang ______ ay para sa mga nagúgutom.\"", ["pagkáin", "gurò", "páhayagan"], "pagkáin",
           "The book's answer is pagkáin (food, Lesson 4)."),
        CH("Part III B 4. \"Ang ______ ay mabangó at magandá.\"", ["bulaklák", "túbig", "magsasaká"], "bulaklák",
           "The book's answer is bulaklák."),
        CH("Part III B 5. \"Si Mang Tomas ay nagtátanim. Siya ay ______.\"", ["magsasaká", "gurò", "bulaklák"], "magsasaká",
           "The book's answer is magsasaká (farmer, Lesson 15)."),
        CH("Part III B 6. \"Si Gng. Cruz ay nagtúturo. Siya ay ______.\"", ["gurò", "magsasaká", "túbig"], "gurò",
           "The book's answer is gurò (teacher, Lesson 7)."),
        CH("Part III B 7. \"Tayo ay umíinom ng ______ kapag naúuhaw.\"", ["túbig", "aklát", "bulaklák"], "túbig",
           "The book's answer is túbig (water, Lesson 4)."),
        # Part III C
        CH("Part III C 1. Si John ay bása nang bása… Nasásagot niya ang lahát ng tinátanong ng gurò. Si John ay ______.",
           ["marúnong", "tamád", "bulág"], "marúnong", "The book's answer is marúnong (Lesson 4: intelligent; learned)."),
        CH("Part III C 2. Ang dálaga ay laging naglílinis… Siya ang naglúlutò… Siya ang naglálabá… Ang dalága ay ______.",
           ["masípag", "tamád", "bulág"], "masípag", "The book's answer is masípag (industrious, Lesson 6)."),
        CH("Part III C 3. Ayaw niyáng magtrabáho. Gusto niya ay matúlog lamang… Siya ay ______.",
           ["tamád", "masípag", "marúnong"], "tamád", "The book's answer is tamád (lazy, Lesson 7)."),
        CH("Part III C 4. Hindi niya mákita ang kanyang kaúsap. Ang lahát ay madilím… Siya ay ______.",
           ["bulág", "masípag", "tamád"], "bulág", "The book's answer is bulág (blind, Lesson 19)."),
        CH("Part III C 5. Mahírap si Peter. Walâ siyáng pagkain. Walâ siyáng damít… Si Peter ay ______.",
           ["kaáwa-awà", "marúnong", "masípag"], "kaáwa-awà", "The book's answer is kaáwa-awà."),
        # Part IV B
        BU(TRANS[0][0], TRANS[0][1]),
        BU(TRANS[1][0], TRANS[1][1]),
        BU(TRANS[2][0], TRANS[2][1]),
        BU(TRANS[3][0], TRANS[3][1], explain="Malinis comes first, then ang mga damit, then ni Peter (the owner)."),
        BU(TRANS[4][0], TRANS[4][1], explain="Hindi goes before malinis."),
        # Part IV C (item 2 left out: question and answer differ)
        CH("Part IV C 1. \"" + ARTS[0] + "\"", ["Ang mga / ng / sa", "Ng mga / ang / ng", "Sa / ang / ang"], "Ang mga / ng / sa",
           "Book's answer: " + ARTS_ANS[0]),
        CH("Part IV C 3. \"" + ARTS[2] + "\"", ["Ang / ng", "Ng / ang", "Sa / sa"], "Ang / ng",
           "Book's answer: " + ARTS_ANS[2]),
        CH("Part IV C 4. \"" + ARTS[3] + "\"", ["sa / ng", "ang / sa", "ng / ang"], "sa / ng",
           "Book's answer: " + ARTS_ANS[3]),
        CH("Part IV C 5. \"" + ARTS[4] + "\"", ["sa", "si", "ni"], "sa",
           "Book's answer: " + ARTS_ANS[4] + " Si and ni are only for names."),
        CH("Part IV C 6. \"" + ARTS[5] + "\"", ["ang / ng", "ng / ang", "sa / sa"], "ang / ng",
           "Book's answer: " + ARTS_ANS[5]),
    ],
    "recap": [
        "Subject pronouns (siya, sila, kami, kayo) stand before ay; ka follows the predicate.",
        "The doer of an -in- verb is in the possessive form: Kúnin mo ang aklát.",
        "A possessive pronoun before a noun takes a ligature: ng kanyang amá.",
        "Describing a person: marúnong, masípag, tamád, bulág, kaáwa-awà.",
        "Ang (main character), ng (owner), sa (place): Maganda ang asawa ng aking kaibígan.",
    ],
}
