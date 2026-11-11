from dsl import *

# Everyday Tagalog Expressions (book pages 196-199).
# Each entry: (vocab id stem, Tagalog as printed, English as printed, glossed parts or [])
# The heading and sections I-II are printed on page 196, right after the last idiom.

LOC = [
    ("puwedeng-magtanong", "Puwédeng magtanóng?", "May I ask something?", []),
    ("saan-restawran", "Saán akó makakakíta ng isáng magalíng na réstawran?", "Where can I find a good restaurant?", []),
    ("saan-simbahan", "Saán akó makakakíta ng simbáhang Protestánte?", "Where can I find a Protestant church?", []),
    ("saan-doktor", "Saán may doktór?", "Where can I find a doctor?", []),
    ("pangalan-kalsada", "Anó ang pangálan ng kalsádang itó?", "What is the name of this street?", []),
    ("saan-nakatira-cruz", "Saán nakatirá si Ginoóng Cruz?", "Where does Mr. Cruz live?", []),
    ("para-po", "Pára po (sa kánto)!", "[Please] stop (at the corner)!", []),
    ("kanan-kaliwa", "Kánan/Kaliwâ.", "Turn right/left.",
     [("Kánan", "right", "pred"), ("Kaliwâ", "left", "pred")]),
    ("diretso-lang", "Dirétso lang.", "Straight ahead.", []),
    ("tumitigil-bus", "Tumítigil ba ang bus dito?", "Does a bus stop here?", []),
    ("gaano-katagal-bus", "Gaáno katagal ang datíng ng (súsunod na) bus?", "How long before the (next) bus comes?", []),
    ("saan-paparoon", "Saán páparoón ang bus na itó?", "Where is this bus going?", []),
    ("anong-oras-dating", "Anóng oras ang datíng nitóng bus sa Maynilà?", "What time does this bus arrive in Manila?", []),
    ("paano-pumunta", "Paáno pumuntá sa Ortigas Avenue mulâ ditó?", "How do I get to Ortigas Avenue from here?", []),
    ("ngalan-baryo", "Anó ang ngálan ng báryong itó?", "What is the name of this barrio?", []),
    ("puwede-inumin", "Puwéde bang inumín ang túbig na itó?", "Is this water safe to drink?", []),
    ("saan-makakabili-pagkain", "Saán makákabilí ng pagkain?", "Where can we buy food?", []),
    ("pakituro-daan", "Pakiturò sa ákin ang daán.", "Please show me the way.", []),
    ("mag-taksi", "Mag-táksi táyo.", "Let us take a taxi.", []),
    ("maghintay-rito", "Maghintáy ka rito.", "Wait here.", []),
]

KIDS = [
    ("halika", "Halíka.", "Come here.", []),
    ("maghugas", "Maghúgas ka ng kamáy at mukhâ.", "Wash your hands and face.", []),
    ("isuot-sapatos", "Isuót mo ang iyóng sapatos at damít.", "Put on your shoes and clothes.", []),
    ("maupo-magpahinga", "Maupó ka at magpahingá.", "Sit down and rest.", []),
    ("matulog", "Matúlog ka na.", "Go to sleep", []),
    ("kunin-laruan", "Kúnin mo ang iyóng laruán.", "Pick up your toy.", []),
    ("iligpit-laruan", "Iligpít mo ang iyóng mga laruán.", "Put away your toys.", []),
    ("huwag-umiyak", "Huwág kang umiyák.", "Do not cry.", []),
    ("huwag-mag-away", "Huwág kayóng mag-away.", "Don't quarrel.", []),
    ("lumabas-maglaro", "Lumabás kayó at maglarô.", "Go out and play.", []),
    ("huwag-gisingin", "Huwág mong gisíngin ang sanggól.", "Do not wake up the baby.", []),
    ("magpakabait", "Magpakábaít ka.", "Be a good boy (or girl).", []),
]

TIME = [
    ("anong-oras-na", "Anóng oras na?", "What time is it?", []),
    ("ngayon-linggo", "Ngayón ay Linggó.", "Today is Sunday.",
     [("Ngayón", "today", "noun"), ("ay", "is", "ay"), ("Linggó", "Sunday", "noun")]),
    ("bukas-lunes", "Búkas ay Lúnes.", "Tomorrow is Monday.",
     [("Búkas", "tomorrow", "noun"), ("ay", "is", "ay"), ("Lúnes", "Monday", "noun")]),
    ("sabado-kahapon", "Sábado kahápon.", "Yesterday was Saturday.",
     [("Sábado", "Saturday", "pred"), ("kahápon", "yesterday", "noun")]),
    ("mahal-na-araw", "Ngayón ay Mahál na Áraw.", "It is now Holy Week.", []),
    ("buwang-ito-enero", "Ang buwáng ito ay Enéro.", "This month is January.", []),
    ("petsa-abril", "Ang pétsa ay ika-20 (or a bente) ng Abríl.", "The date is April 20.", []),
    ("taon-2007", "Ang taón ay dalawáng libo at pitó.", "The year is 2007.", []),
]

SPEAK = [
    ("nag-aaral-magsalita", "Nag-áaral akóng magsalitâ ng Tagálog.", "I am learning to speak Tagalog.", []),
    ("nagsasalita-kaunti", "Nagsásalitâ akó ng káunti lámang.", "I speak only little Tagalog.", []),
    ("kausapin-mo-ako", "Kausápin mo akó sa Tagálog.", "Please talk to me in Tagalog.", []),
    ("paano-sinasabi", "Paáno sinásabi sa Tagálog ang ... ?", "How do you say ... in Tagalog?", []),
    ("iwasto-pagbigkas", "Iwastô mo ang áking pagbigkás.", "Please correct my pronunciation.", []),
    ("nag-aaral-wika", "Nag-áaral kamí ng inyóng wikà.", "We are studying your language.", []),
    ("nagsasalita-ka-ba", "Nagsásalitâ ka ba ng Tagálog?", "Do you speak Tagalog?", []),
    ("hindi-maintindihan", "Hindî ko maintindihán.", "I do not understand.", []),
    ("paki-ulit", "Paki-úlit nga.", "Please repeat.", []),
    ("anong-sinabi", "Anóng sinabi mo?", "What did you say?", []),
]

INTRO = [
    ("pangalan-ko", "Ang pangalan ko ay Jonathan.", "My name is Jonathan.", []),
    ("ano-pangalan-mo", "Anó ang pangalan mo?", "What is your name?", []),
    ("sino-ka", "Síno ka/kayó?", "Who are you?", []),
    ("saan-ka-nakatira", "Saán ka nakatirá?", "Where do you live?", []),
    ("ito-kaibigan", "Itó ang kaibígan kong si Paolo.", "This is my friend Paolo.", []),
    ("ikinagagalak", "Ikínagagalák kong mákilala kayó.", "I am pleased to meet you.", []),
    ("dumalaw-kayo", "Dumálaw kayó sa ámin.", "Please come and visit us.", []),
    ("kaibigan-ni-jolina", "Kaibígan akó ni Jolina.", "I am Jolina's friend.", []),
    ("sino-kasama", "Síno ang mga kasáma mo?", "Who are your companions?", []),
    ("ikaw-ba-kaibigan", "Ikáw ba ang kaibígan ng kapatíd kong babáe?", "Are you my sister's friend?", []),
    ("kilala-ba-kita", "Kilalá ba kitá?", "Do I know you?", []),
    ("kilala-kita", "Kilalá kitá.", "I know you.", []),
    ("hindi-kita-kilala", "Hindí kitá kilalá.", "I do not know you.", []),
]

DRESS = [
    ("isusuot", "Anó ang iyóng isúsuót?", "What will you wear?", []),
    ("ewan-ko", "Ewan ko. Walá akóng bágong damít.", "I do not know. I don't have a new dress.", []),
    ("luma-na", "Lumá na iyán.", "That is an old one.", []),
    ("wala-maisuot", "Walá akóng máisuót.", "I have nothing to wear.", []),
    ("isusuot-barong", "Isúsuót ko ang áking Bárong Tagálog.", "I will wear my Barong Tagalog.", []),
    ("gusto-barong", "Gustó ko ang Bárong Tagálog.", "I like the Barong Tagalog.", []),
    ("malamig-isuot", "Itó ay malamíg isuót.", "It is cool.", []),
    ("mainit-amerikana", "Maínit ang amérikana.", "A coat is warm.",
     [("Maínit", "warm", "pred"), ("ang", "the", "marker"), ("amérikana", "coat", "noun")]),
]

PARTY = [
    ("handa-na", "Handâ na ang pagkain. Kumáin na táyo.", "The food is ready. Let's eat.", []),
    ("kumain-mabuti", "Kumáin kayóng mabúti.", "Eat well.", []),
    ("gusto-kanin", "Gustó mo pa ng kánin?", "Do you like more rice?", []),
    ("kumuha-pa", "Kumúha pa kayó.", "Please get some more.", []),
    ("huwag-mahiya", "Húwag kayóng mahiyâ.", "Don't be shy.", []),
    ("busog-na", "Salámat. Busóg na akó.", "Thank you. I am already full.", []),
]

BYE = [
    ("gabi-na", "Gabí na. Umuwî na táyo.", "It is late (at night). Let's go home.", []),
    ("salamat-pagparito", "Salámat sa inyóng pagparíto.", "Thank you for coming.", []),
    ("nasiyahan", "Nasiyahán kamí sa inyóng handâ.", "We enjoyed the party.", []),
    ("pumarito-uli", "Pumaríto kayó ulî.", "Please come again.", []),
    ("babalik-kami", "Babalík kamí.", "We will return.",
     [("Babalík", "will return", "pred"), ("kamí", "we", "pron")]),
    ("paalam-salamat", "Paalám. Maraming salámat.", "Goodbye. Thank you very much.", []),
    ("hanggang-sa-muli", "Paalám, hanggáng sa mulî.", "Goodbye, until next time.", []),
]

MARKET = [
    ("sariwa-karne", "Sariwà ba ang karne?", "Is the meat fresh?", []),
    ("magkano-ito", "Magkano ito?", "How much is this?",
     [("Magkano", "how much", "pred"), ("ito", "this", "pron")]),
    ("kilo-baboy", "Magkano ang isáng kílo ng baboy?", "How much is a kilo of pork?", []),
    ("kilo-baka", "Bigyán mo akó ng isáng kílo ng baka.", "Give me one kilo of beef.", []),
    ("ang-mahal", "Ang mahál namán nitó.", "This is expensive.", []),
    ("meron-pa-iba", "Méron pa ba kayóng ibá?", "Do you have other things?", []),
    ("gawa-pilipinas", "Gawâ ba itó sa Pilipínas?", "Is this made in the Philippines?", []),
    ("subenir", "Saán akó makakabilí ng mga subenir?", "Where can I buy souvenirs?", []),
    ("magandang-presyo", "Magandáng presyo.", "The price is fair.", []),
    ("hindi-tama-sukli", "Hindî táma ang suklî.", "This is not the correct change.", []),
    ("pakibalot", "Pakibalot ngâ ninyó itó.", "Please wrap this item.", []),
]

KITCHEN = [
    ("mainit-pugon", "Maínit ang pugón.", "The stove is hot.",
     [("Maínit", "hot", "pred"), ("ang", "the", "marker"), ("pugón", "stove", "noun")]),
    ("puno-kaserola", "Punô ang kaseróla.", "The pot is full.",
     [("Punô", "full", "pred"), ("ang", "the", "marker"), ("kaseróla", "pot", "noun")]),
    ("matalas-kutsilyo", "Matálas ang kutsílyo.", "The knife is sharp.",
     [("Matálas", "sharp", "pred"), ("ang", "the", "marker"), ("kutsílyo", "knife", "noun")]),
    ("walang-laman", "Waláng lamán ang páminggalan.", "The pantry is empty.", []),
    ("malilinis-pinggan", "Malilínis ang mga pinggán.", "The dishes are clean.",
     [("Malilínis", "clean", "pred"), ("ang", "the", "marker"), ("mga", "(plural)", "marker"), ("pinggán", "dishes", "noun")]),
    ("marumi-sahig", "Marumí ang sahíg.", "The floor is dirty.",
     [("Marumí", "dirty", "pred"), ("ang", "the", "marker"), ("sahíg", "floor", "noun")]),
    ("lutuin-natin", "Lutúin nátin ang pagkain.", "Let us cook the food.", []),
    ("hugasan-gulay", "Hugásan nang mabúti ang mga gúlay.", "Wash the vegetables thoroughly.", []),
    ("iayos-kabinet", "Iayos mo ang mga kábinet.", "Keep the cabinets in order.", []),
]

DINING = [
    ("oras-na-kumain", "Oras na para kumáin.", "It is time to eat.", []),
    ("ano-ang-ulam", "Anó ang ulam?", "What's for breakfast (or lunch or dinner)?", []),
    ("magpasalamat", "Magpasalamat tayó [sa áting pagkain].", "Let us say our graces.", []),
    ("gusto-karne", "Gustó mo ng karné?", "Will you have meat?", []),
    ("pakiabot-kanin", "Pakiabót ng kánin.", "Please pass the rice.", []),
    ("meron-tsa", "Méron bang tsa?", "Do you have tea?", []),
    ("gusto-pa-tsa", "Gustó ko pa ng tsa.", "I would like more tea.",
     [("Gustó", "like", "pred"), ("ko", "I", "pron"), ("pa", "more", "part"), ("ng", "(marker)", "marker"), ("tsa", "tea", "noun")]),
    ("pakidala-tinapay", "Pakidalá ng tinápay.", "Please bring the bread.", []),
    ("tapos-kumain", "Tapós na kamíng kumáin.", "We are through eating.", []),
    ("basong-tubig", "Isáng básong túbig ngâ.", "A glass of water please.", []),
    ("pakiligpit-mesa", "Pakiligpít ang mésa.", "Please clear the table.", []),
    ("ang-sarap", "Ang saráp ng pagkain!", "That was a good meal!", []),
]

LIVING = [
    ("tuloy-kayo", "Tulóy kayó. Maupô kayó.", "Please come in and sit down.", []),
    ("natutuwa-pagparito", "Natútuwâ kamí sa pagparito ninyó.", "We are happy that you came.", []),
    ("upuang-komportable", "Ang úpúang itó ay komportable.", "This chair is comfortable.", []),
    ("makinig-tugtog", "Ibig ba ninyóng makiníg ng tugtóg?", "Do you wish to listen to some music?", []),
    ("magbasa-diyaryo", "Ibig ba ninyóng magbasá ng diyaryo?", "Would you like to read the newspaper?", []),
    ("malamig-na-tubig", "Ibig ba ninyó ng malamíg na túbig?", "Would you like some cold water?", []),
    ("gaano-katagal-nakatira", "Gáano katagál na kayóng nakatirá rito?", "How long have you been living here?", []),
    ("nasisiyahan-tumira", "Nasísiyahán kamíng tumirá rito.", "We enjoy living here.", []),
    ("mga-tao-dito", "Ang mga tao dito ay mabubuti at matutulungin.", "The people here are friendly and helpful.", []),
]

NOTES = {
    "halika": "Lesson 34 prints halika.",
    "pangalan-kalsada": "This page prints pangálan; the introductions on page 197 print pangalan.",
    "gaano-katagal-bus": "The living-room list prints Gáano katagál.",
    "huwag-umiyak": "The party list prints Húwag.",
    "huwag-mahiya": "A very common expression of hosts when they offer food to their guests and want to make them feel more welcome. The children's list prints Huwág.",
    "busog-na": "The book also gives: Húwag na. Salámat.",
    "mainit-amerikana": "Amérikana refers to the formal coat and tie introduced by the Americans.",
    "magandang-presyo": "The book also gives: Sulit ang presyo.",
    "oras-na-kumain": "The book also gives: Kaínan na.",
    "ano-ang-ulam": "Ulam (viand) goes with rice every meal time.",
    "sariwa-karne": "The dining-room list prints karné.",
    "gusto-karne": "The market list prints karne.",
    "magpasalamat": "Other lines print táyo.",
    "petsa-abril": "Printed exactly as in the book: ika-20 (or a bente).",
    "hindi-kita-kilala": "Page 197 prints Hindî (Hindî ko maintindihán).",
    "paalam-salamat": "Lesson 3 prints Maráming salámat.",
}


def ex(rows):
    return [(tl, en, parts) for _, tl, en, parts in rows]


SKIP = {"anong-oras-na"}  # already in Lesson 28 with the same spelling and meaning


def voc(rows, group):
    return [V(k + "-a04", tl, en, pos="phrase", group=group, note=NOTES.get(k)) for k, tl, en, _ in rows if k not in SKIP]


LESSON = {
    "id": "a04",
    "label": "A4",
    "title": "Everyday Tagalog expressions",
    "summary": "Ready-made phrases for directions, children, time, speaking Tagalog, introductions, dressing up, parties, goodbyes, the market, kitchen, dining room and living room",
    "minutes": 35,
    "goals": [
        "Ask for places and directions, and get around by bus or taxi",
        "Give simple instructions to children",
        "Say the day, month, date and year",
        "Tell people you are learning Tagalog and ask for help",
        "Introduce yourself and others",
        "Use polite phrases as a guest or host: at a party, at meals, in the living room and when saying goodbye",
        "Shop at the market and talk about the kitchen",
    ],
    "sections": [
        S("About these expressions",
          P("Lesson 3 gave you the first everyday expressions: greetings such as *Good day*, *How are you* and *Excuse me*, and the respect word **pô**. This appendix adds more ready-made phrases, grouped by **place or situation** (the market, the kitchen…), plus **instructions for children**. They are the kind of phrases you need when you talk with native Tagalog speakers."),
          BOX("tip", "How to use this lesson", items=[
              "Learn each phrase as a whole, like a block. You do not need to take every word apart.",
              "Tap **Listen** on the examples and say them out loud.",
              "Notice the respect word **pô / po** (Lesson 3) and the request words starting with **paki-** (Lesson 24), such as **Pakiturò** (please show) and **Paki-úlit** (please repeat).",
              "Commands with **Huwág** (*do not*) come from Lesson 37."])),

        S("I. Locations and directions",
          P("Phrases for finding places, asking for directions and taking a bus or taxi. **Saán** (*where*) starts many of them."),
          EXS(ex(LOC), title="Locations and directions"),
          BOX("culture", "Stopping a ride", t="**Pára po!** is what you call out to make a jeepney or bus stop. Add **sa kánto** to say *at the corner*."),
          BOX("warn", "Book spellings", items=[
              "This page prints **pangálan** (name); page 197 prints **pangalan**.",
              "This page prints **Gaáno katagal**; page 199 prints **Gáano katagál**."]),
          VOC("loc", "Locations and directions")),

        S("II. Instructions for children",
          P("Short commands for children. Several begin with **Huwág** (*do not*), followed by **kang**, **kayóng** or **mong** (ka, kayó, mo + the ligature -ng from Lesson 7)."),
          EXS(ex(KIDS), title="Instructions for children"),
          BOX("tip", "Do not…", items=[
              "**Huwág kang umiyák.** Do not cry.",
              "**Huwág kayóng mag-away.** Don't quarrel.",
              "**Huwág mong gisíngin ang sanggól.** Do not wake up the baby."]),
          VOC("kids", "Instructions for children")),

        S("III. Time",
          P("Saying the time, day, month, date and year. The book writes the date as **ika-20 (or a bente)** and the year 2007 as **dalawáng libo at pitó**."),
          EXS(ex(TIME), title="Time"),
          VOC("time", "Time")),

        S("IV. Speaking in Tagalog",
          P("Useful phrases while you are learning: tell people you are learning, ask them to repeat or to correct you."),
          EXS(ex(SPEAK), title="Speaking in Tagalog"),
          BOX("tip", "Asking for a word", t="**Paáno sinásabi sa Tagálog ang ... ?** Put the English word in the gap: *How do you say ... in Tagalog?*"),
          VOC("speak", "Speaking in Tagalog")),

        S("V. Making introductions",
          P("Giving your name, asking someone's name and introducing a friend."),
          EXS(ex(INTRO), title="Making introductions"),
          BOX("warn", "Book spellings", t="Page 198 prints **Hindí kitá kilalá** with an acute accent on hindí; page 197 prints **Hindî ko maintindihán**."),
          VOC("intro", "Making introductions")),

        S("VI. Dressing up",
          P("Talking about what to wear."),
          EXS(ex(DRESS), title="Dressing up"),
          BOX("culture", "Barong Tagalog and amérikana", t="**Amérikana** refers to the formal coat and tie introduced by the Americans. A coat is warm (**Maínit ang amérikana**), while the Barong Tagalog is cool to wear (**Itó ay malamíg isuót**)."),
          VOC("dress", "Dressing up")),

        S("VII. At a party",
          P("Phrases a host and a guest use when food is served."),
          EXS(ex(PARTY) + [("Húwag na. Salámat.", "Thank you. I am already full. (the book's other way to say it)", [])], title="At a party"),
          BOX("culture", "Don't be shy", t="**Húwag kayóng mahiyâ.** is a very common expression of hosts when they offer food to their guests. It helps the guests feel more welcome in their homes."),
          VOC("party", "At a party")),

        S("VIII. Goodbyes",
          P("Leaving a party and thanking the hosts."),
          EXS(ex(BYE), title="Goodbyes"),
          VOC("bye", "Goodbyes")),

        S("IX. In the market",
          P("Asking prices and buying at the market. **Magkano** means *how much*."),
          EXS(ex(MARKET) + [("Sulit ang presyo.", "The price is fair. (the book's other way to say it)", [])], title="In the market"),
          BOX("warn", "Book spellings", t="The market list prints **karne** (meat); the dining-room list prints **karné**."),
          VOC("market", "In the market")),

        S("X. In the kitchen",
          P("Describing things in the kitchen and giving kitchen jobs. Most describing sentences use the pattern **describing word + ang + thing**:"),
          PAT("describing word + ang + thing",
              [("hot stove", [("Maínit", "pred"), ("ang", "marker"), ("pugón", "noun")]),
               ("sharp knife", [("Matálas", "pred"), ("ang", "marker"), ("kutsílyo", "noun")])],
              note="The stove is hot. · The knife is sharp."),
          EXS(ex(KITCHEN), title="In the kitchen"),
          VOC("kitchen", "In the kitchen")),

        S("XI. In the dining room",
          P("Phrases for mealtime. Look for the **paki-** request words from Lesson 24: **Pakiabót** (please pass), **Pakidalá** (please bring), **Pakiligpít** (please clear)."),
          EXS(ex(DINING) + [("Kaínan na.", "It is time to eat. (the book's other way to say it)", [])], title="In the dining room"),
          BOX("culture", "Ulam", t="**Ulam** (viand) is the dish that goes with rice at every meal. So **Anó ang ulam?** is how you ask what's for breakfast, lunch or dinner."),
          VOC("dining", "In the dining room")),

        S("XII. In the living room",
          P("Welcoming visitors and chatting with them."),
          EXS(ex(LIVING), title="In the living room"),
          BOX("remember", "Remember", items=[
              "Locations: **Saán…?** (where), **Pára po!** (stop), **Kánan/Kaliwâ** (turn right/left).",
              "Children: **Huwág kang / kayóng / mong…** (do not…).",
              "Learning: **Hindî ko maintindihán.** **Paki-úlit nga.**",
              "Market: **Magkano ito?** **Ang mahál namán nitó.**",
              "Polite requests with **paki-**: Pakiabót, Pakidalá, Pakiligpít, Pakibalot.",
              "Host phrases: **Tulóy kayó. Maupô kayó.** **Húwag kayóng mahiyâ.**"]),
          VOC("living", "In the living room")),
    ],
    "vocab": (voc(LOC, "loc") + voc(KIDS, "kids") + voc(TIME, "time") + voc(SPEAK, "speak") + voc(INTRO, "intro")
              + voc(DRESS, "dress")
              + [V("amerikana-a04", "amérikana", "a coat (the formal coat and tie introduced by the Americans)", say="a-ME-ri-ka-na", pos="noun", group="dress")]
              + voc(PARTY, "party")
              + [V("huwag-na-salamat-a04", "Húwag na. Salámat.", "Thank you. I am already full.", pos="phrase", group="party", note="The book's other way to say Salámat. Busóg na akó.")]
              + voc(BYE, "bye") + voc(MARKET, "market")
              + [V("sulit-ang-presyo-a04", "Sulit ang presyo.", "The price is fair.", pos="phrase", group="market", note="The book's other way to say Magandáng presyo.")]
              + voc(KITCHEN, "kitchen") + voc(DINING, "dining")
              + [V("kainan-na-a04", "Kaínan na.", "It is time to eat.", pos="phrase", group="dining", note="The book's other way to say Oras na para kumáin."),
                 V("ulam-a04", "ulam", "viand (goes with rice every meal time)", pos="noun", group="dining")]
              + voc(LIVING, "living")),
    "exercises": [
        CH("How do you ask \"May I ask something?\"", ["Puwédeng magtanóng?", "Paki-úlit nga.", "Saán may doktór?"], "Puwédeng magtanóng?", "Paki-úlit nga = Please repeat."),
        CH("You want the jeepney to stop at the corner. What do you call out?", ["Pára po (sa kánto)!", "Dirétso lang.", "Maghintáy ka rito."], "Pára po (sa kánto)!", "Dirétso lang = Straight ahead; Maghintáy ka rito = Wait here."),
        CH("What does \"Kánan/Kaliwâ\" mean?", ["Turn right/left.", "Straight ahead.", "Please show me the way."], "Turn right/left.", "Kánan = right, Kaliwâ = left."),
        CH("Which phrase tells a child \"Do not cry\"?", ["Huwág kang umiyák.", "Huwág kayóng mag-away.", "Matúlog ka na."], "Huwág kang umiyák.", "Huwág kayóng mag-away = Don't quarrel; Matúlog ka na = Go to sleep."),
        CH("\"Búkas ay Lúnes.\" What does it mean?", ["Tomorrow is Monday.", "Today is Sunday.", "Yesterday was Saturday."], "Tomorrow is Monday.", "Ngayón ay Linggó = Today is Sunday."),
        CH("How do you say \"I do not understand\"?", ["Hindî ko maintindihán.", "Hindí kitá kilalá.", "Ewan ko."], "Hindî ko maintindihán.", "Hindí kitá kilalá = I do not know you."),
        CH("What does \"Ikínagagalák kong mákilala kayó\" mean?", ["I am pleased to meet you.", "Please come and visit us.", "Who are your companions?"], "I am pleased to meet you.", "A polite phrase when you are introduced."),
        CH("What is \"amérikana\"?", ["The formal coat and tie introduced by the Americans", "The Barong Tagalog", "A new dress"], "The formal coat and tie introduced by the Americans", "Maínit ang amérikana = A coat is warm."),
        CH("A host says \"Húwag kayóng mahiyâ.\" What do they mean?", ["Don't be shy.", "Please get some more.", "Eat well."], "Don't be shy.", "A very common expression when hosts offer food to their guests."),
        CH("Which is another way the book gives to say \"Thank you. I am already full\"?", ["Húwag na. Salámat.", "Kumúha pa kayó.", "Gustó mo pa ng kánin?"], "Húwag na. Salámat.", "Salámat. Busóg na akó. is the first way."),
        CH("At the market, how do you say \"This is expensive\"?", ["Ang mahál namán nitó.", "Magandáng presyo.", "Magkano ito?"], "Ang mahál namán nitó.", "Magandáng presyo = The price is fair."),
        CH("\"Hindî táma ang suklî.\" What does it mean?", ["This is not the correct change.", "Please wrap this item.", "Do you have other things?"], "This is not the correct change.", "Suklî is the change you get back."),
        CH("What is \"ulam\"?", ["The viand that goes with rice every meal time", "The rice itself", "Tea"], "The viand that goes with rice every meal time", "Anó ang ulam? = What's for breakfast (or lunch or dinner)?"),
        CH("Which phrase welcomes visitors into the living room?", ["Tulóy kayó. Maupô kayó.", "Gabí na. Umuwî na táyo.", "Babalík kamí."], "Tulóy kayó. Maupô kayó.", "Please come in and sit down."),
        LI("Saán may doktór?", ["Where can I find a doctor?", "Where can I find a Protestant church?", "Where does Mr. Cruz live?"], "Where can I find a doctor?", "Saán = where."),
        LI("Paki-úlit nga.", ["Please repeat.", "Please talk to me in Tagalog.", "What did you say?"], "Please repeat.", "Anóng sinabi mo? = What did you say?"),
        LI("Paalám, hanggáng sa mulî.", ["Goodbye, until next time.", "Please come again.", "Thank you for coming."], "Goodbye, until next time.", "Pumaríto kayó ulî = Please come again."),
        LI("Punô ang kaseróla.", ["The pot is full.", "The stove is hot.", "The pantry is empty."], "The pot is full.", "Punô = full; kaseróla = pot."),
        LI("Pakiabót ng kánin.", ["Please pass the rice.", "Please bring the bread.", "Please clear the table."], "Please pass the rice.", "Pakidalá ng tinápay = Please bring the bread."),
        BU("How much is this?", "Magkano ito?"),
        BU("The knife is sharp.", "Matálas ang kutsílyo."),
        BU("Do you speak Tagalog?", "Nagsásalitâ ka ba ng Tagálog?"),
        BU("What is your name?", "Anó ang pangalan mo?"),
        BU("I would like more tea.", "Gustó ko pa ng tsa."),
        MA("Match the time phrase to its meaning.", [("Anóng oras na?", "What time is it?"), ("Ngayón ay Linggó.", "Today is Sunday."), ("Sábado kahápon.", "Yesterday was Saturday."), ("Ngayón ay Mahál na Áraw.", "It is now Holy Week.")]),
        MA("Match the kitchen sentence to its meaning.", [("Maínit ang pugón.", "The stove is hot."), ("Marumí ang sahíg.", "The floor is dirty."), ("Malilínis ang mga pinggán.", "The dishes are clean."), ("Waláng lamán ang páminggalan.", "The pantry is empty.")]),
        MA("Match the introduction to its meaning.", [("Kilalá kitá.", "I know you."), ("Kilalá ba kitá?", "Do I know you?"), ("Saán ka nakatirá?", "Where do you live?"), ("Síno ka/kayó?", "Who are you?")]),
    ],
    "recap": [
        "Directions: Puwédeng magtanóng? Saán…? Pára po (sa kánto)! Kánan/Kaliwâ. Dirétso lang.",
        "Children: Halíka. Huwág kang umiyák. Matúlog ka na. Magpakábaít ka.",
        "Learning Tagalog: Hindî ko maintindihán. Paki-úlit nga. Paáno sinásabi sa Tagálog ang ... ?",
        "Introductions: Ang pangalan ko ay… Ikínagagalák kong mákilala kayó.",
        "Guest and host: Tulóy kayó. Kumáin na táyo. Húwag kayóng mahiyâ. Salámat. Busóg na akó.",
        "Market and table: Magkano ito? Pakiabót ng kánin. Ang saráp ng pagkain!",
    ],
}
