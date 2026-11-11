from dsl import *

# Review Exercises, Parts VII and VIII (book pages 224-226) with the Answer key (pages 228-229).
# Everything Tagalog is copied as printed, including the book's misprints, which are pointed out in notes.

TRY = "Try it yourself first, then check your answers here."


def items(rows):
    return [[a, b] for a, b in rows]


LESSON = {
    "id": "r4",
    "label": "R4",
    "title": "Review: Parts VII and VIII – particles, comparisons, can and should, causatives and passives",
    "summary": "The book's review exercises on word order with ba and other particles, comparing and intensifying adjectives, can/should sentences, magpa- and pa- + -in verbs, plural adjectives, verbs and adjectives used as nouns, and passive sentences, with the book's answers",
    "minutes": 35,
    "goals": [
        "Put ba, raw, rin, pô, na and pa in the right place",
        "Say good, very good, how good and most industrious",
        "Compare people and things: more than, as … as, of the same height",
        "Say what someone can, should or needs to do",
        "Understand magpa- and pa- + -in sentences, plural adjectives, and ang + verb or adjective",
        "Translate passive sentences into English",
    ],
    "sections": [
        S("About this review",
          P("This lesson is the book's own **review exercises, Parts VII and VIII**. Every item is copied exactly as the book prints it. After each exercise you will find **the book's answer** from its answer key (the book gives no answer for the two *create sentences* exercises)."),
          BOX("tip", "How to use this review", items=[
              "Say or write your own answer first. Then compare it with the book's answer.",
              "Each exercise names the lesson to **revise** if you find it hard.",
              "The exercises at the end of this lesson are built from the book's answers."])),

        # ---------------- PART VII ----------------
        S("Part VII A. Put the words in order",
          P("**Book's instruction:** Arrange the words and particles in the following sentences, and replace with correct ones."),
          TABLE(["", "As printed"], items([
              ("1.", "marumi ang bata ang raw ba"), ("2.", "siya ay bata ba pa"), ("3.", "siya ay kumain rin ay ba po"),
              ("4.", "nakaalis nab a siya"), ("5.", "nakapag-aral hindi siya pa"),
              ("6.", "bakit siya hindi makatatakbo nang mabilis"), ("7.", "ba ito ang aklat mo")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. Marumi raw ba ang bata?",
              "2. Siya ba ay bata pa?",
              "3. Siya rin pô ba ay kumain?",
              "4. Nakaalis na ba siya?",
              "5. Hindi pa siya nakapag-aral.",
              "6. Bakit hindi siya makatakbo ng mabilis?",
              "7. Ito ba ang aklat mo?"]),
          PAT("Particles follow the first word",
              [("item 1", [("Marumi", "pred"), ("raw", "part"), ("ba", "part"), ("ang", "marker"), ("bata", "noun")]),
               ("item 4", [("Nakaalis", "pred"), ("na", "part"), ("ba", "part"), ("siya", "pron")])],
              note="The book's answers to items 1 and 4."),
          P("As Lesson 10 showed, little words such as **na, pa, rin, raw** and **pô** come after the question word or the predicate and push **ba** further back. **Raw** means *they say*; **rin** means *too, also*; **pa** means *still, yet*; **na** means *already*."),
          BOX("warn", "Book slips", items=[
              "Item 4 prints **nab a**: a misprint for **na ba**.",
              "Items 1 and 3 have an extra word (a second **ang**, a second **ay**) that the answer drops.",
              "Item 6: the answer also changes **makatatakbo** to **makatakbo** and **nang** to **ng**.",
              "Item 3 prints **po**; the answer prints **pô**."]),
          BOX("remember", "Revise", t="Revise: Lesson 10 (The question word ba).")),

        S("Part VII B. Good, very good, most industrious",
          P("**Book's instruction:** Give the Tagalog equivalent of the following words and phrases."),
          TABLE(["", "English"], items([
              ("1.", "good"), ("2.", "very good"), ("3.", "how good"),
              ("4.", "industrious"), ("5.", "very industrious"), ("6.", "most industrious")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. good - **mabuti**",
              "2. very good - **napakabuti**",
              "3. how good - **kay buti** or **mabuting-mabuti**",
              "4. industrious - **masipag**",
              "5. very industrious - **napakasipag** or **masipag na masipag**",
              "6. most industrious - **pinakamasipag**."]),
          TABLE(["", "mabuti (good)", "masipag (industrious)"],
                [["very", "napakabuti", "napakasipag · masipag na masipag"],
                 ["how", "kay buti · mabuting-mabuti", ""],
                 ["most", "", "pinakamasipag"]],
                title="The book's answer as a table",
                note="napaka- = very; pinaka- = most; an adjective doubled with a ligature (masipag na masipag) is also very."),
          BOX("warn", "Book spellings", items=[
              "Lesson 11 writes **nápaka-** with an accent; this answer key prints **napaka-**.",
              "Lesson 41 writes **kaybúti** (how good!) as one word; this answer key prints **kay buti**.",
              "Lesson 11 gives a doubled adjective (magandáng-magandá) as *very*; here the book gives **mabuting-mabuti** for *how good*."]),
          VOC("degree", "New from this exercise"),
          BOX("remember", "Revise", t="Revise: Lesson 11 (Making comparisons).")),

        S("Part VII C. Comparisons",
          P("**Book's instruction:** Translate these sentences into Tagalog."),
          TABLE(["", "English"], items([
              ("1.", "Peter is brighter than John."), ("2.", "John is taller than his brother."),
              ("3.", "My house is as beautiful as his."), ("4.", "His child is small."),
              ("5.", "His child is smaller than my child."), ("6.", "His child is of the same height as mine."),
              ("7.", "His dog is not as bad as his neighbor's."), ("8.", "John and Peter are brothers."),
              ("9.", "Jack and his friend are of the same color."), ("10.", "My sister is more beautiful than I.")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. Lalong marunong si Peter kaysa kay John.",
              "2. Lalong mataas si John kaysa sa kanyang kapatid na lalaki.",
              "3. Ang aking bahay ay kasingganda ng kaniyang bahay.",
              "4. Maliit ang kanyang anak.",
              "5. Lalong maliit ang kanyang anak kaysa sa anak ko.",
              "6. Magkasintaas ang anak niya at ang anak ko.",
              "7. Ang kanyang aso ay hindi kasinsama ng aso ng kapitbahay niya.",
              "8. Magkapatid sina John at Peter.",
              "9. Si Jack at ang kanyang kaibigan ay magkasingkulay.",
              "10. Lalong maganda ang aking kapatid kaysa sa akin."]),
          PAT("More than: lalong + adjective + kaysa",
              [("item 1", [("Lalong", "other"), ("marunong", "pred"), ("si", "marker"), ("Peter", "noun"), ("kaysa", "other"), ("kay", "marker"), ("John", "noun")]),
               ("item 5", [("Lalong", "other"), ("maliit", "pred"), ("ang", "marker"), ("kanyang", "poss"), ("anak", "noun"), ("kaysa", "other"), ("sa", "marker"), ("anak", "noun"), ("ko", "poss")])],
              note="Kaysa kay before a person's name; kaysa sa before other nouns (Lesson 11)."),
          BOX("english", "Which word for which idea?", items=[
              "*more … than*: **lalong** + adjective + **kaysa kay / kaysa sa** (items 1, 2, 5, 10).",
              "*as … as*: **kasing-** / **kasin-** + root (kasingganda, kasinsama) (items 3, 7).",
              "*of the same …* for two people together: **magkasin-** / **magkasing-** (magkasintaas, magkasingkulay) (items 6, 9).",
              "*brothers*: **magkapatid** (item 8)."]),
          BOX("warn", "Book spellings", t="Item 3 prints **kaniyang**; the other answers print **kanyang**. Lesson 11 writes lalóng, káysa and kasíng- with accents; this answer key prints them without."),
          BOX("remember", "Revise", t="Revise: Lesson 11 (Making comparisons).")),

        S("Part VII D. Create sentences",
          P("**Book's instruction:** Create sentences using the following words."),
          BOX("tip", "Your turn", items=[
              "1. **magandá**", "2. **kay gandá**", "3. **magandáng-magandá**", "4. **nápakagandá**",
              "5. **pinakamagandá**", "6. **magkasintaás**", "7. **hindî kasinggúlang**", "8. **hindî kasimbaít**",
              "Make one sentence with each. The book gives no single answer for this exercise."]),
          BOX("remember", "Revise", t="Revise: Lesson 11 (Making comparisons).")),

        S("Part VII E. Can, should, need",
          P("**Book's instruction:** Translate the following into Tagalog."),
          TABLE(["", "English"], items([
              ("1.", "Don't eat now."), ("2.", "He cannot ride a horse."), ("3.", "Can you swim?"), ("4.", "Yes, I can swim."),
              ("5.", "You should study Tagalog everyday."), ("6.", "Why don't you eat your supper?"),
              ("7.", "Do you know his name?"), ("8.", "What do you need?")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. Huwag kang kumain ngayon.",
              "2. Hindi siya marunong sumakay sa kabayo.",
              "3. Marunong ka bang lumangoy?",
              "4. Oo, marunong akong lumangoy.",
              "5. Kailangan mong mag-aral ng Tagalog araw-araw.",
              "6. Bakit hindi ka kumain ng iyong hapunan?",
              "7. Alam mo ba ang kanyang pangalan?",
              "8. Ano ang kailangan mo?"]),
          BOX("english", "Notice", items=[
              "Here *can swim* and *cannot ride* are said with **marunong** followed by the verb in the infinitive: **marunong akong lumangoy**, **marunong sumakay**.",
              "Item 5 uses **Kailangan mong** (*you need to*) for *you should*.",
              "**Huwag kang** + infinitive = *don't* (Lesson 37).",
              "**Ba** goes after **ka** and **mo**: *Marunong ka bang…?*, *Alam mo ba…?* (Lesson 10)."]),
          BOX("remember", "Revise", t="Revise: Lesson 17 (Pseudo verbs) and Lesson 37 (huwág).")),

        # ---------------- PART VIII ----------------
        S("Part VIII A. Create sentences with pa- + -in and magpa-",
          P("**Book's instruction:** Create sentences from the following root words using the prefixes on the left. Afterwards, give the English translation of your sentences."),
          BOX("tip", "Your turn", items=[
              "1. **lambót** using **pa-in**", "2. **kain** using **magpa-**",
              "3. **upo** using **pa_in**", "4. **inom** using **magpa-**",
              "The book gives no single answer for this exercise. Look at Part VIII B for model sentences."]),
          P("Remember from Lesson 36: **magpa-** and **pa- + -in** verbs are about having something done: someone gives an order to have something done to another. **Magpa-** is active; **pa- + -in** is passive."),
          BOX("warn", "Book slip", t="Item 3 prints **pa_in** (an underscore): it means **pa-in**, as in item 1."),
          BOX("remember", "Revise", t="Revise: Lesson 36 (Magpa- and pa- + -in verb forms).")),

        S("Part VIII B. Made to do it: into English",
          P("**Book's instruction:** Translate the following sentences into English."),
          TABLE(["", "Tagalog"], items([
              ("1.", "Huwág mong sirain ang papel."), ("2.", "Pinasulat ko siya ng liham."),
              ("3.", "Siya'y pinaalis ng kanyang ama."), ("4.", "Ang kanyang tákot ay nagpatakbó kay Juan."),
              ("5.", "Pinabasa niya ako ng pahayagan.")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. Don't tear the paper.",
              "2. I made him/her write a letter.",
              "3. His father made him/her leave.",
              "4. His fear made Juan run.",
              "5. He/She made me read the newspaper."]),
          EXS([("Pinasulat ko siya ng liham.", "I made him/her write a letter.",
                [("Pinasulat", "made … write", "pred"), ("ko", "I (doer)", "poss"), ("siya", "him/her", "pron"), ("ng", "a", "marker"), ("liham", "letter", "noun")]),
               ("Pinabasa niya ako ng pahayagan.", "He/She made me read the newspaper.",
                [("Pinabasa", "made … read", "pred"), ("niya", "he/she (doer)", "poss"), ("ako", "me", "pron"), ("ng", "the", "marker"), ("pahayagan", "newspaper", "noun")])],
              title="Pa- + -in: made someone do it"),
          BOX("remember", "Revise", t="Revise: Lesson 36 (Magpa- and pa- + -in verb forms) and Lesson 37 (huwág).")),

        S("Part VIII C. Plural adjectives two ways",
          P("**Book's instruction:** Give the plural form of the following adjectives in two ways."),
          TABLE(["Adjective"], [["**magandá**"], ["**mabuti**"]]),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. **magaganda**; **mga maganda**",
              "2. **mabubuti**; **mga mabuti**"]),
          P("Way 1 is the one from Lesson 4: repeat the first syllable of the root (ma**ga**ganda, ma**bu**buti). Way 2 puts **mga** in front of the adjective."),
          BOX("warn", "Book spellings", t="The exercise prints **magandá**; the answer prints magaganda and mga maganda without accents. Lesson 4 writes **magagandá**."),
          BOX("remember", "Revise", t="Revise: Lesson 4 (Plurals: mga and plural adjectives).")),

        S("Part VIII D. Ang + adjective or verb: into English",
          P("**Book's instruction:** Translate the following phrases into English."),
          TABLE(["", "Tagalog"], items([
              ("1.", "ang mabaít"), ("2.", "ang mabaít na tao"), ("3.", "and bumábasa"),
              ("4.", "ang binábasa"), ("5.", "ang patakbó"), ("6.", "ang maglabá")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. the good one",
              "2. the good man",
              "3. the one reading",
              "4. the thing being read",
              "5. the manner of running or the running of (something such as a contest)",
              "6. the washing of clothes"]),
          P("As in Lesson 31, putting **ang** in front of an adjective or a verb turns it into a noun: **ang mabaít** is *the good one*. Compare item 3, an active verb (*the one reading*), with item 4, a passive -in verb (*the thing being read*)."),
          BOX("warn", "Book slip", t="Item 3 prints **and bumábasa**: a misprint for **ang bumábasa**."),
          VOC("nouns", "New from this exercise"),
          BOX("remember", "Revise", t="Revise: Lesson 31 (Forming nouns).")),

        S("Part VIII E. Passive sentences: into English",
          P("**Book's instruction:** Translate the following sentences into English using the passive voice of verbs."),
          TABLE(["", "Tagalog"], items([
              ("1.", "Kanyáng iniligtás ako."), ("2.", "Siya'y pinalo ng kaibigan niya."), ("3.", "Hindî niya ako sinulátan."),
              ("4.", "Ako'y kanyang binigyán ng aklát niya."), ("5.", "Ang iyong ibinigay ay akin na."),
              ("6.", "Ang sa kanyá ay hindi magagámit ng ibá.")])),
          BOX("tip", "The book's answer", items=[
              TRY,
              "1. I was saved by him.",
              "2. He was hit by his friend.",
              "3. He had not written to me.",
              "4. His/her book was given to me by him.",
              "5. What you have given me is mine already.",
              "6. What is his/hers cannot be used by another."]),
          BOX("english", "Passive in English", items=[
              "In items 1 to 4 the one who receives the action is the subject (**ako**, **siya**), and the doer is in the possessive form (**kanyáng**, **ng kaibigan niya**, **niya**, **kanyang**).",
              "Item 3: the book's English (*He had not written to me*) is not in the passive voice."]),
          BOX("remember", "Revise", t="Revise: Lesson 15 (-in- verb forms), Lesson 32 (I- verb forms) and Lesson 33 (-An verb forms).")),
    ],
    "vocab": [
        V("napakabuti-r4", "napakabuti", "very good", pos="adj", group="degree"),
        V("kay-buti-r4", "kay buti", "how good", pos="adj", group="degree",
          note="The book also gives mabuting-mabuti. Lesson 41 writes kaybúti (how good!)."),
        V("mabuting-mabuti-r4", "mabuting-mabuti", "how good", pos="adj", group="degree",
          note="The book also gives kay buti."),
        V("ang-mabait-r4", "ang mabaít", "the good one", pos="phrase", group="nouns"),
        V("ang-mabait-na-tao-r4", "ang mabaít na tao", "the good man", pos="phrase", group="nouns"),
        V("ang-binabasa-r4", "ang binábasa", "the thing being read", pos="phrase", group="nouns"),
        V("ang-patakbo-r4", "ang patakbó", "the manner of running or the running of (something such as a contest)", pos="phrase", group="nouns"),
        V("ang-maglaba-r4", "ang maglabá", "the washing of clothes", pos="phrase", group="nouns"),
    ],
    "exercises": [
        # Part VII A
        BU("Put in order: marumi ang bata ang raw ba", "Marumi raw ba ang bata?", extra=["ang"],
           explain="Raw and ba follow the first word; the second ang is not needed."),
        BU("Put in order: siya ay bata ba pa", "Siya ba ay bata pa?"),
        BU("Put in order: siya ay kumain rin ay ba po", "Siya rin pô ba ay kumain?", extra=["ay"],
           explain="Rin, pô and ba follow siya; only one ay is needed."),
        BU("Put in order: nakaalis nab a siya", "Nakaalis na ba siya?", explain="The book's nab a is a misprint for na ba."),
        BU("Put in order: nakapag-aral hindi siya pa", "Hindi pa siya nakapag-aral."),
        BU("Put in order: ba ito ang aklat mo", "Ito ba ang aklat mo?"),
        # Part VII B
        MA("Match the English to the book's Tagalog.",
           [("good", "mabuti"), ("very good", "napakabuti"), ("industrious", "masipag"), ("most industrious", "pinakamasipag")]),
        CH("\"How good\" in the book's answer?", ["kay buti", "pinakamasipag", "napakasipag"], "kay buti",
           "The book also gives mabuting-mabuti. Pinakamasipag = most industrious; napakasipag = very industrious."),
        # Part VII C
        BU("Peter is brighter than John.", "Lalong marunong si Peter kaysa kay John."),
        BU("John is taller than his brother.", "Lalong mataas si John kaysa sa kanyang kapatid na lalaki."),
        BU("My house is as beautiful as his.", "Ang aking bahay ay kasingganda ng kaniyang bahay."),
        BU("His child is of the same height as mine.", "Magkasintaas ang anak niya at ang anak ko."),
        BU("John and Peter are brothers.", "Magkapatid sina John at Peter."),
        BU("My sister is more beautiful than I.", "Lalong maganda ang aking kapatid kaysa sa akin."),
        # Part VII E
        BU("Don't eat now.", "Huwag kang kumain ngayon."),
        BU("Can you swim?", "Marunong ka bang lumangoy?"),
        BU("Yes, I can swim.", "Oo, marunong akong lumangoy."),
        BU("Do you know his name?", "Alam mo ba ang kanyang pangalan?"),
        BU("What do you need?", "Ano ang kailangan mo?"),
        # Part VIII B
        LI("Huwág mong sirain ang papel.", ["Don't tear the paper.", "I made him/her write a letter.", "His fear made Juan run."],
           "Don't tear the paper.", "Huwág mong + verb = don't."),
        LI("Pinasulat ko siya ng liham.", ["I made him/her write a letter.", "He/She made me read the newspaper.", "His father made him/her leave."],
           "I made him/her write a letter.", "Pa- + -in: made someone do it. Ko = I (the doer)."),
        LI("Siya'y pinaalis ng kanyang ama.", ["His father made him/her leave.", "His fear made Juan run.", "Don't tear the paper."],
           "His father made him/her leave.", "Pinaalis = made to leave."),
        LI("Pinabasa niya ako ng pahayagan.", ["He/She made me read the newspaper.", "I made him/her write a letter.", "His father made him/her leave."],
           "He/She made me read the newspaper.", "Pinabasa = made to read; niya = he/she (the doer)."),
        # Part VIII C
        CH("The book's two plural forms of mabuti?", ["mabubuti; mga mabuti", "magaganda; mga maganda", "napakabuti; kay buti"],
           "mabubuti; mga mabuti", "Magaganda; mga maganda are the plurals of maganda. Napakabuti and kay buti mean very good and how good."),
        # Part VIII D
        MA("Match the phrase to the book's English.",
           [("ang mabaít", "the good one"), ("ang mabaít na tao", "the good man"), ("ang binábasa", "the thing being read"), ("ang maglabá", "the washing of clothes")]),
        LI("ang patakbó", ["the manner of running or the running of (something such as a contest)", "the one reading", "the washing of clothes"],
           "the manner of running or the running of (something such as a contest)", "Ang maglabá = the washing of clothes."),
        # Part VIII E
        LI("Kanyáng iniligtás ako.", ["I was saved by him.", "He was hit by his friend.", "He had not written to me."],
           "I was saved by him.", "Iniligtás = was saved; kanyáng = by him."),
        LI("Siya'y pinalo ng kaibigan niya.", ["He was hit by his friend.", "I was saved by him.", "What you have given me is mine already."],
           "He was hit by his friend.", "Pinalo = was hit."),
        LI("Ang iyong ibinigay ay akin na.", ["What you have given me is mine already.", "What is his/hers cannot be used by another.", "His/her book was given to me by him."],
           "What you have given me is mine already.", "Ang iyong ibinigay = what you have given."),
    ],
    "recap": [
        "Particles follow the first word and push ba back: Marumi raw ba ang bata? Nakaalis na ba siya?",
        "mabuti, napakabuti, kay buti / mabuting-mabuti; masipag, napakasipag / masipag na masipag, pinakamasipag.",
        "More than: Lalong marunong si Peter kaysa kay John. As … as: kasingganda. Same height: magkasintaas.",
        "Can: marunong + -ng + infinitive (Marunong ka bang lumangoy?). Need/should: Kailangan mong mag-aral.",
        "Made someone do it: Pinasulat ko siya ng liham. Plurals: magaganda / mga maganda. Ang + verb or adjective = a noun.",
    ],
}
