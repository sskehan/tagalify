from dsl import *

# Conversational Tagalog, part 1 (book pages 200-203).
# Lines: (speaker or None for the narrator, Tagalog as printed, English as printed, parts)


def conv(lines):
    out = []
    for who, tl, en, parts in lines:
        out.append((tl, f"{who}: {en}" if who else en, parts))
    return out


MEET1 = [
    (None, "Dumating si Peter Smith galing sa Hong Kong. Sinalubong siya ni Linda Reyes, tagapamahala ng mga benta ng kanilang kompanya.",
     "Peter Smith arrived from Hong Kong. He was met by Linda Reyes, sales director of their company.", []),
    ("LINDA", "Maligayang pagdating, Ginoong Smith.", "Welcome, Mr. Smith.", []),
    ("PETER", "Salamat, kumusta ka Martin?", "Thank you. How are you, Linda?", []),
    ("LINDA", "Mabuti po naman. Kayo? Kumusta ang inyong biyahe?", "I am fine. And you? How was your trip?", []),
    ("PETER", "Mabuti naman. Maayos ang lahat.", "It was all right. Everything was fine.", []),
    ("LINDA", "May reserbasyon kayo sa Manila Peninsula. Narito na ang sundo ninyo na magdadala sa inyo sa otel. Magkita po tayo mamaya doon sa otel para sa pulong.",
     "You have a reservation at the Manila Peninsula. Here's the person who will drive you to the hotel. I'll see you later at the hotel for the meeting.", []),
    ("PETER", "Maraming salamat.", "Thank you.", []),
]

MEET2 = [
    (None, "Pinulong ni Peter Smith ang mga kawani ng kanilang kompanya sa otel.",
     "Peter Smith met the personnel of the company in the hotel.", []),
    ("LINDA", "Ikinararangal kong ipakilala sa inyo ang ating pangulo, Si Ginoong Peter Smith.",
     "I have the honor to introduce to you our president, Mr. Peter Smith.", []),
    ("PETER", "Maraming salamat, Martin. Magandang umaga sa inyong lahat. Natutuwa ako sa muli nating pagkikita sa simula ng bagong taong ito. Binabati ko rin kayong lahat sa inyong magandang benta noong nakaraang taon.",
     "Thank you very much, Linda. Good morning to you all. I am happy to see you again at the start of this new year. I also congratulate you for the good sales last year.", []),
    ("LINDA", "Maraming salamat po. Talaga pong nagsikap ang lahat para maabot at malagpasan ang ating kota. Ginoong Smith, bago po tayo mag-umpisa ng miting, maari po bang ipakilala ko ang mga bago nating direktor?",
     "Thank you very much, sir. Everybody really tried hard to reach and go beyond our quota. Mr. Smith, before we start the meeting, may I introduce our new directors?", []),
    ("PETER", "Sige, ipagpatuloy mo.", "By all means, continue.", []),
    ("LINDA", "Ginoong Smith, si Ricardo Sandoval ang ating Katulong na Direktor sa Pagbebenta.",
     "Mr. Smith, this is Ricardo Sandoval, Assistant Director for Sales.", []),
    ("PETER", "Ikinagagalak kitang makilala, Ricardo.", "I am pleased to meet you, Ricardo.", []),
    ("RICARDO", "Maraming salamat po.", "Thank you, sir.", []),
    ("LINDA", "At ito po naman si Binibining Delia Orosa, ang bago nating Direktor sa Pananaliksik.",
     "And this is Miss Delia Orosa, our new Director for Research.", []),
    ("PETER", "Ikinalulugod kong mapabilang ka sa ating pangkat, Delia.", "I am happy to have you in our group, Delia.", []),
    ("DELIA", "Salamat po.", "Thank you, sir.",
     [("Salamat", "thank you", "pred"), ("po", "(respect)", "part")]),
]

DIRECTIONS = [
    (None, "Bagong dating ang mag-inang Aling Ana at Sally sa Quezon City. Galing sila sa lalawigan at bumaba sila sa estasyon ng bus sa Cubao. Pupunta sila sa Makati upang dalawin ang kapatid ni Aling Ana. Nagtanong sila sa isang lalaking dumaraan.",
     "Aling Ana and her daughter Sally had just arrived in Quezon City. They came from the province and got down at the bus station in Cubao. They are going to Makati to visit Aling Ana's sister. They asked a man who was passing by.", []),
    ("ALING ANA", "Mawalang-galang na po. Saan ba ang sakayan patungong Makati?", "Excuse me, sir. Where can we get a ride to Makati?", []),
    ("LALAKI", "Dumiretso kayo riyan, tumawid sa Edsa at sumakay sa bus na may karatulang Ayala.",
     "Go straight ahead, cross Edsa and board the bus with the signboard Ayala.", []),
    ("ALING ANA", "Tanghali na kami. Marahil mas mabilis ang taksi.", "We're already late. Perhaps a taxi will be faster.", []),
    ("SALLY", "Nay, bakit hindi natin subukan ang MRT?", "Mother, why don't we try the MRT?", []),
    ("LALAKI", "Mas mabilis ang MRT. Madali kayong makararating sa Makati. Ang estasyon ng MRT Cubao ay nasa Farmers' Plaza. Bumili kayo ng tiket para sa Buendia Station. Pagdating ninyo roon, marami na kayong masasakyang jeepney o FX.",
     "MRT is faster. You will reach Makati easily. The Cubao MRT station is in Farmers' Plaza. Buy a ticket for Buendia Station. When you get there, you can take a jeepney or FX.", []),
    ("ALING ANA", "Maraming salamat po sa inyong tulong.", "Thank you for your assistance, sir.", []),
    ("LALAKI", "Walang anuman po.", "You're welcome, madam.", []),
    ("ALING ANA", "Ibang-iba na ang Maynila ngayon. May MRT at FX na. Sa ating probinsiya ay marami pa ring karetela at traysikel.",
     "Manila is very different now. They already have the MRT and FX. In the province, we still have a lot of carriages and tricycles.", []),
]

BANK = [
    (None, "Kagagaling lamang ni Nestor sa Saudi Arabia. Kailangan niyang magpapalit ng dolyar. Nagpasama siya kay Juan sa bangko.",
     "Nestor has just arrived from Saudi Arabia. He needs to change his dollars into pesos.", []),
    ("NESTOR", "Magandang umaga. Maari bang magpapalit ng limang daang dolyar sa piso? Magkano ang palitan ngayon?",
     "Good morning. May I have my $500 changed into peso? What is the current exchange rate?", []),
    ("TELLER", "Kuwarenta y nuwebe po sa dolyar. Pakipunan po ninyo ang aplikasyon na ito.",
     "Forty-nine pesos to a dollar. Please fill up this application form.", []),
    ("NESTOR", "Salamat. Kung nais kong maglagak sa inyong bangko, magkano ang paunang deposito?",
     "Thank you. If I wish to deposit in your bank, how much is the initial deposit?", []),
    ("TELLER", "Sampung libong piso po ang unang deposito.", "The initial deposit is P10,000, sir.", []),
    ("NESTOR", "Ano naman ang mga kailangan para magbukas ng account?", "What are needed to open an account?", []),
    ("TELLER", "Kailangan ng dalawang ID tulad ng lisensiya ng drayber, pasaporte o SSS.",
     "Two IDs are needed like a driver's license, passport or SSS.", []),
    ("NESTOR", "Kailangan rin ba ng litrato?", "Is a photo needed?", []),
    ("TELLER", "Opo, puwede po kahit ano ang sukat.", "Yes, sir. Any size will do.", []),
    ("NESTOR", "Maraming salamat. Babalik na lamang ako sa ibang araw.", "Thank you, I'll come back some other day.", []),
]

CLUB = [
    (None, "Ang pulong ng samahan ni Tessie ay tuwing ikalawang Martes ng buwan. Ito ay ginaganap sa isang restoran sa Malate. Ang layunin ng kanilang samahan ay tumulong sa mga maralitang kababaihan at kabataan sa Barangay 83 ng Sta. Ana. Noong Martes na iyon, pagkatapos ang pag-awit ng Pambansang Awit at ang panalanging pambungad, tinawag ng kalihim ang mga pangalan ng dumalo sa miting.",
     "Tessie's club meets every second Tuesday of the month. It is held in a restaurant in Malate. The purpose of their club is to help the poor women and children of Barangay 83 of Sta. Ana. That particular Tuesday, after the singing of the National Anthem and the opening prayer, the secretary called the names of those who attended the meeting.", []),
    ("TESSIE", "Magandang hapon sa inyong lahat. Kalihim Elsa, ilang kasapi ang dumalo sa pulong na ito?",
     "Good afternoon, everyone. Secretary Elsa, how many members are present in this meeting?", []),
    ("ELSA", "May labinlimang kasapi ang naririto ngayon maliban kina Mary at Kris.",
     "There are 15 members present now excluding Mary and Kris.", []),
    ("TESSIE", "Basahin natin ngayon ang mga tala ng nakaraang miting.", "Let's now read the minutes of the past meeting.", []),
    ("TESSIE", "Salamat, Kalihim Elsa. Tatalakayin naman natin ang ating pangkabuhayang proyekto sa Tondo. May ulat ang tagapangulo ng lupon, si Pacita.",
     "Thank you, Secretary Elsa. We will now discuss our livelihood project in Tondo. Pacita, the chairperson of the committee will report.", []),
    ("PACITA", "Sa ika-8 ng Pebrero, gaganapin ang ating proyekto na magtuturo sa mga kababaihan ng barangay ng iba't ibang paggawa ng longganisa.",
     "On February 8, we will conduct our project to teach the women of the barangay the different ways of making sausages.", []),
    ("TESSIE", "Salamat, Pacita. At tungkol naman sa mga bata, ano ang ulat mo, Carol?",
     "Thank you, Pacita, Regarding the children, what is your report, Carol?", []),
    ("CAROL", "Sa ika-16 ng Marso, dadalhin natin ang mga bata sa Museo Pambata sa Roxas Boulevard kung saan matututo sila ng maraming kaalaman tungkol sa kanilang paligid. Pagkatapos ay ipapasyal sila sa Rizal Park.",
     "On March 16, we will take the children to the Children's Museum on Roxas Blvd where they will learn a lot about their surroundings. Then we are taking them to Rizal Park.", []),
    ("TESSIE", "Paano ang pagkain ng mga bata?", "What about the children's food?", []),
    ("CAROL", "Isang kompanya ng gatas ang umako sa kanilang pagkain pati na ng kanilang transportasyon.",
     "A milk company will take care of their food as well as their transportation.", []),
    ("TESSIE", "Binabati ko kayo, Pacita at Carol sa inyong magandang pamumuno. May iba pa bang bagay tayong tatalakayin? Kung wala na, tinatapos ko na ang miting na ito. Maraming salamat sa inyong pagdalo.",
     "Congratulations, Pacita and Carol for your fine leadership. Are there other matters to discuss? If none, the meeting is adjourned. Thank you very much for coming.", []),
]

MARKET1 = [
    (None, "Si Ginang Jones at ang kusinera niyang si Ada ay nagpunta sa palengke. Magkakaroon ng munting salu-salo si Ginang Jones para sa mag-asawang Thomas na galing sa Bangkok. Nais ni Ginang Jones na bumili ng mga sariwang prutas at gulay sa palengke. Pumunta sila sa puwesto ng mga prutas kung saan nakakita sila ng mga mangga, saging, dalandan, papaya, tsiko at lansones.",
     "Mrs. Jones and her cook Ada went to the market. Mrs. Jones will have a small party for the Thomas couple who arrived from Bangkok. Mrs. Jones wants to buy fresh fruits and vegetables in the market. They went to the fruit stand first where they saw mangoes, bananas, oranges, papaya, chico and lanzones.", []),
    ("GNG. JONES", "Magkano ang mangga?", "How much are the mangoes?",
     [("Magkano", "how much", "pred"), ("ang", "the", "marker"), ("mangga", "mangoes", "noun")]),
    ("MALE VENDOR", "Sisenta po ang isang kilo.", "Sixty pesos per kilo.", []),
    ("ADA", "Saan ba galing ang mga iyan?", "Where do they come from?", []),
    ("MALE VENDOR", "Sa Pangasinan. Matatamis ang mga mangga na galing doon.", "From Pangasinan. Mangoes from that place are very sweet.", []),
    ("GNG. JONES", "Bigyan mo ako ng dalawang kilo. Gusto ko rin ng saging na lacatan at isang piña.",
     "Give me two kilos. I also like lacatan and pineapple.", []),
    ("ADA", "Bibili rin po ba kayo ng pakwan, madam?", "Are you also buying watermelon, madam?", []),
    ("GNG. JONES", "Oo, gustong-gusto ni Ginoong Jones ang pakwan.", "Yes, Mr. Jones likes watermelon very much.", []),
    ("MALE VENDOR", "Narito na lahat ng inyong pinamili.", "Here are all the things you have bought.", []),
    ("GNG. JONES", "Salamat. Pakikuwenta lahat.", "Thank you. Please add up everything.", []),
]

MARKET2 = [
    (None, "Pagkatapos sa prutasan, nagtungo naman sila sa gulayan.", "From the fruitstand, they went to the vegetable section. (The book misprints \"sa sa gulayan\" here.)", []),
    ("GNG. JONES", "Bumili tayo ng letsugas, kamatis at sibuyas para sa salad.", "Let's buy lettuce, tomatoes and onions for the salad.", []),
    ("ADA", "Nais ba ninyong gumawa ako ng lumpiang sariwa?", "Do you want me to prepare fresh vegetable spring roll?", []),
    ("GNG. JONES", "Oo, gusto ko iyon. Sarapan mo ang salsa.", "Yes, I like that. Make the sauce delicious.", []),
    ("ADA", "Bibili ako ng petsay, karot, repolyo, abitsuelas at patatas. Hahaluan ko rin ng singkamas ang lumpia.",
     "I will buy Chinese cabbage, carrot, cabbage, beans and potatoes. I'll also mix turnips in the spring roll.", []),
    ("GNG. JONES", "Sige, ikaw ang bahala. Pihadong magugustuhan ng ating mga panauhin ang lumpiang Pilipino.",
     "Okay, it's up to you. For sure, our visitors will like Filipino spring roll.", []),
]

MARKET3 = [
    (None, "Mula sa palengke, nagtungo si Ginang Jones at si Ada sa supermarket na malapit sa kanilang bahay sa Makati. Di kalakihan ang pamilihan pero maraming mga paninda, lokal man o galing sa ibang bansa. Pumunta si Ginang Jones at si Ada sa karnihan. Bumili sila ng lomo, giniling na karneng-baboy, lengua at manok. Nagtungo rin sila sa isdaan.",
     "From the market, Mrs. Jones and Ada went to the supermarket near their house. The supermarket is not very big but it sells a lot of goods, both local and imported. Mrs. Jones and Ada went to the meat section where they bought sirloin, ground pork, ox tongue and chicken. They also went to the fish section.", []),
    ("GNG. JONES", "Maganda at sariwa ang mga lapu-lapu dito. Pumili ka ng ilang piraso. Pumili ka na rin ng kaunting halaan at sugpo. Ayan, palagay ko nabili na natin ang lahat ng kailangan. Umuwi na tayo.",
     "The grouper here is good and fresh. Choose a few pieces. Also choose some clams and prawns. There, I guess we have all that we need. Let's go home.", []),
]


LESSON = {
    "id": "a05",
    "label": "A5",
    "title": "Conversations: meeting people, directions, the bank, a meeting, the market",
    "summary": "Five real-life conversations with the book's translations: welcoming a visitor and making introductions, asking directions, changing money at a bank, running a club meeting, and shopping at the market and supermarket",
    "minutes": 35,
    "goals": [
        "Follow a welcome and a round of introductions at work",
        "Ask for directions and understand the answer",
        "Change money and ask about opening a bank account",
        "Follow the order of a club meeting",
        "Buy fruit, vegetables, meat and fish at the market",
    ],
    "sections": [
        S("How these conversations work",
          P("This appendix gives several everyday **conversations**. Each Tagalog line is followed by the book's **English translation**, with the speaker's name in front. A **Vocabulary List** and some **cultural notes** explain words that were not used in the earlier lessons."),
          BOX("tip", "How to study them", items=[
              "Read the English first so you know what is happening, then read the Tagalog line by line.",
              "Tap **Listen** and repeat each line out loud, as if you were that speaker.",
              "The translations are natural English, not word for word, so a Tagalog line and its English may not match word by word.",
              "The narrator's lines (with no speaker) set the scene."]),
          BOX("culture", "Names and titles", items=[
              "**Ginoong** = Mr. (Ginoong Smith), **Ginang / Gng.** = Mrs. (Ginang Jones), **Binibining** = Miss (Binibining Delia Orosa). These match the English translations.",
              "**Aling** is used before an older woman's name (Aling Ana). The notes in the next lesson explain it."])),

        S("Meeting someone and making introductions",
          P("**Pagtatagpô at Pagpapakilala** (*Meeting Someone and Making Introductions*). Linda welcomes her company's president, Peter Smith, at the start of his visit."),
          EXS(conv(MEET1), title="Part 1: the arrival"),
          EXS(conv(MEET2), title="Part 2: meeting the staff"),
          BOX("warn", "A slip in the book", t="In two of Peter's lines the Tagalog says **Martin**, but the English says **Linda** (the person he is talking to). The lines are shown here exactly as printed."),
          BOX("tip", "Polite phrases to borrow", items=[
              "**Maligayang pagdating** = Welcome",
              "**Ikinagagalak kitang makilala** = I am pleased to meet you",
              "**Sige, ipagpatuloy mo.** = By all means, continue."]),
          P("The book's Vocabulary List also gives **pangulo** = president, which you met in Lesson 26."),
          VOC("meet", "Vocabulary List")),

        S("Asking directions",
          P("**Pagtatanong Ng Direksiyón** (*Asking Directions*). Aling Ana and her daughter Sally have arrived in Quezon City from the province and need to get to Makati."),
          EXS(conv(DIRECTIONS), title="Asking Directions"),
          BOX("culture", "Getting around Metro Manila", items=[
              "**MRT** = Metro Rail Transit.",
              "**FX** = an air-conditioned vehicle that can accommodate nine passengers. FX fare is more expensive than a jeepney's.",
              "**EDSA** = Epifanio de los Santos Avenue, a major thoroughfare crossing several cities in Metro Manila."]),
          BOX("tip", "Near and far", items=[
              "**malapit** = near → **malapít-lapít** = nearer; a bit near",
              "**malayò** = far → **malayó-layô** = farther; a bit far"]),
          P("The book's list also gives **lalawigan** = province, which you met in Lesson 30."),
          VOC("dir", "Vocabulary List and Notes")),

        S("At the bank",
          P("**Sa Bangko** (*At the Bank*). Nestor has come home from Saudi Arabia and changes his dollars."),
          EXS(conv(BANK), title="At the Bank"),
          BOX("english", "About the translation", t="The book's English for the opening leaves out the last Tagalog sentence, **Nagpasama siya kay Juan sa bangko.**"),
          VOC("bank", "Vocabulary List")),

        S("In a meeting",
          P("**Sa Isang Pulong** (*In a Meeting*). Tessie chairs her club's monthly meeting. The book gives no vocabulary list for this conversation."),
          EXS(conv(CLUB), title="In a Meeting"),
          BOX("tip", "Meeting words from the translation", items=[
              "**Kalihim Elsa** = Secretary Elsa",
              "**Magandang hapon sa inyong lahat.** = Good afternoon, everyone.",
              "**Maraming salamat sa inyong pagdalo.** = Thank you very much for coming."]),
          VOC("club", "Phrases from the conversation")),

        S("At the market and in a store",
          P("**Sa Palengke at Tindahan** (*At the Market and in a Store*). Mrs. Jones and her cook Ada shop for a small party."),
          EXS(conv(MARKET1), title="At the fruit stand"),
          EXS(conv(MARKET2), title="At the vegetable section"),
          EXS(conv(MARKET3), title="At the supermarket"),
          BOX("tip", "Shopping phrases", items=[
              "**Magkano ang mangga?** = How much are the mangoes?",
              "**Bigyan mo ako ng dalawang kilo.** = Give me two kilos.",
              "**Pakikuwenta lahat.** = Please add up everything.",
              "**Sige, ikaw ang bahala.** = Okay, it's up to you."]),
          VOC("market", "Phrases from the conversation"),
          BOX("remember", "Remember", items=[
              "Welcome: **Maligayang pagdating.** Pleased to meet you: **Ikinagagalak kitang makilala.**",
              "Excuse me: **Mawalang-galang na po.** You're welcome: **Walang anuman po.**",
              "Bank: **maglagak** (to deposit), **magpalit ng pera** (to change currency), **pakipunán** (please fill up).",
              "Market: **Magkano…?** **Bigyan mo ako ng…** **Pakikuwenta lahat.**"])),
    ],
    "vocab": [
        # meeting
        V("sundo-a05", "sundô", "somebody who fetches", say="sun-doQ", pos="noun", group="meet"),
        V("pagbebenta-a05", "pagbebenta", "sales", pos="noun", group="meet"),
        V("pagpapakilala-a05", "pagpapakilala", "introduce", pos="noun", group="meet", note="The conversation title Pagtatagpô at Pagpapakilala = Meeting Someone and Making Introductions."),
        V("pananaliksik-a05", "pananaliksík", "research", say="pa-na-na-lik-SIK", pos="noun", group="meet"),
        V("pangkat-a05", "pangkát", "group", say="pang-KAT", pos="noun", group="meet"),
        V("paliparan-a05", "páliparan", "airport", say="PA-li-pa-ran", pos="noun", group="meet"),
        V("pulong-a05", "pulong", "meeting", pos="noun", group="meet"),
        V("magsikap-a05", "magsikap", "to work hard", pos="verb", group="meet"),
        V("ipagpatuloy-a05", "ipagpatuloy", "continue", pos="verb", group="meet", note="Sige, ipagpatuloy mo. = By all means, continue."),
        V("maligayang-pagdating-a05", "Maligayang pagdating", "Welcome", pos="phrase", group="meet", note="Maligayang pagdating, Ginoong Smith. = Welcome, Mr. Smith."),
        V("ikinagagalak-kitang-makilala-a05", "Ikinagagalak kitang makilala", "I am pleased to meet you", pos="phrase", group="meet", note="Appendix A4 prints Ikínagagalák kong mákilala kayó."),
        # directions
        V("bumaba-a05", "bumabâ", "to go down", say="bu-ma-baQ", pos="verb", group="dir"),
        V("diretso-a05", "dirétso", "straight ahead", say="di-RET-so", pos="adv", group="dir"),
        V("dumalaw-a05", "dumalaw", "to visit", pos="verb", group="dir", note="Lesson 21 prints dumálaw (visited)."),
        V("malapit-a05", "malapit", "near", pos="adj", group="dir", note="Lesson 2 prints malápit."),
        V("malapit-lapit-a05", "malapít-lapít", "nearer; a bit near", say="ma-la-PIT la-PIT", pos="adj", group="dir"),
        V("malayo-a05", "malayò", "far", say="ma-LA-yoQ", pos="adj", group="dir"),
        V("malayo-layo-a05", "malayó-layô", "farther; a bit far", say="ma-la-YO la-yoQ", pos="adj", group="dir"),
        V("tumawid-a05", "tumawíd", "to cross", say="tu-ma-WID", pos="verb", group="dir"),
        V("mrt-a05", "MRT", "Metro Rail Transit", pos="noun", group="dir"),
        V("mawalang-galang-na-po-a05", "Mawalang-galang na po.", "Excuse me, sir.", pos="phrase", group="dir", note="Lesson 3 prints Mawaláng-gálang pô."),
        V("walang-anuman-po-a05", "Walang anuman po.", "You're welcome, madam.", pos="phrase", group="dir"),
        # bank
        V("lisensiya-a05", "lisensiya", "license", pos="noun", group="bank"),
        V("litrato-a05", "litrato", "photo", pos="noun", group="bank"),
        V("magbukas-a05", "magbukas", "to open", pos="verb", group="bank", note="Lesson 33 prints magbukás."),
        V("maglagak-a05", "maglagak", "to deposit", pos="verb", group="bank"),
        V("magpalit-ng-pera-a05", "magpalit ng pera", "to change currency", pos="phrase", group="bank"),
        V("pakipunan-a05", "pakipunán", "please fill up", say="pa-ki-pu-NAN", pos="verb", group="bank"),
        V("sukat-a05", "sukat", "size", pos="noun", group="bank"),
        # club meeting
        V("kalihim-a05", "kalihim", "secretary", pos="noun", group="club", note="From Kalihim Elsa = Secretary Elsa."),
        V("magandang-hapon-lahat-a05", "Magandang hapon sa inyong lahat.", "Good afternoon, everyone.", pos="phrase", group="club"),
        V("salamat-pagdalo-a05", "Maraming salamat sa inyong pagdalo.", "Thank you very much for coming.", pos="phrase", group="club"),
        # market
        V("magkano-ang-mangga-a05", "Magkano ang mangga?", "How much are the mangoes?", pos="phrase", group="market"),
        V("bigyan-dalawang-kilo-a05", "Bigyan mo ako ng dalawang kilo.", "Give me two kilos.", pos="phrase", group="market"),
        V("pakikuwenta-lahat-a05", "Pakikuwenta lahat.", "Please add up everything.", pos="phrase", group="market"),
        V("ikaw-ang-bahala-a05", "Sige, ikaw ang bahala.", "Okay, it's up to you.", pos="phrase", group="market"),
        V("umuwi-na-tayo-a05", "Umuwi na tayo.", "Let's go home.", pos="phrase", group="market", note="Appendix A4 prints Umuwî na táyo."),
    ],
    "exercises": [
        CH("Linda greets Peter with \"Maligayang pagdating, Ginoong Smith.\" What does she say?", ["Welcome, Mr. Smith.", "Thank you, Mr. Smith.", "Good morning, Mr. Smith."], "Welcome, Mr. Smith.", "Maligayang pagdating = Welcome."),
        CH("What is a sundô?", ["somebody who fetches", "a reservation", "a meeting"], "somebody who fetches", "Narito na ang sundo ninyo = Here's the person who will drive you."),
        CH("How does Peter say \"I am pleased to meet you, Ricardo\"?", ["Ikinagagalak kitang makilala, Ricardo.", "Ikinalulugod kong mapabilang ka sa ating pangkat, Ricardo.", "Sige, ipagpatuloy mo, Ricardo."], "Ikinagagalak kitang makilala, Ricardo.", "The second option is what he says to Delia: I am happy to have you in our group."),
        CH("Which word means \"group\"?", ["pangkát", "pulong", "pagbebenta"], "pangkát", "pulong = meeting; pagbebenta = sales."),
        CH("How does Aling Ana politely start her question to the stranger?", ["Mawalang-galang na po.", "Walang anuman po.", "Maraming salamat po."], "Mawalang-galang na po.", "Excuse me, sir."),
        CH("What does \"malayó-layô\" mean?", ["farther; a bit far", "nearer; a bit near", "far"], "farther; a bit far", "malayò = far; malapít-lapít = nearer; a bit near."),
        CH("What is an FX?", ["an air-conditioned vehicle that can accommodate nine passengers", "the Metro Rail Transit", "a major avenue in Metro Manila"], "an air-conditioned vehicle that can accommodate nine passengers", "Its fare is more expensive than a jeepney's."),
        CH("Which word means \"to deposit\"?", ["maglagak", "magbukas", "magpalit ng pera"], "maglagak", "magbukas = to open; magpalit ng pera = to change currency."),
        CH("The teller says \"Pakipunan po ninyo ang aplikasyon na ito.\" What should Nestor do?", ["Fill up the application form", "Show a photo", "Come back another day"], "Fill up the application form", "pakipunán = please fill up."),
        CH("\"Kailangan rin ba ng litrato?\" What is Nestor asking?", ["Is a photo needed?", "Is a license needed?", "What size is needed?"], "Is a photo needed?", "litrato = photo."),
        CH("In the meeting, who is \"Kalihim Elsa\"?", ["Secretary Elsa", "the chairperson", "a new member"], "Secretary Elsa", "The secretary called the names of those who attended."),
        CH("Mrs. Jones says \"Pakikuwenta lahat.\" What does she want?", ["Please add up everything.", "Give me two kilos.", "Choose a few pieces."], "Please add up everything.", "She is ready to pay."),
        LI("Walang anuman po.", ["You're welcome, madam.", "Thank you, sir.", "Excuse me, sir."], "You're welcome, madam.", "The man's reply to Aling Ana's thanks."),
        LI("Sige, ipagpatuloy mo.", ["By all means, continue.", "Thank you very much.", "Everything was fine."], "By all means, continue.", "ipagpatuloy = continue."),
        LI("Magkano ang mangga?", ["How much are the mangoes?", "Where do they come from?", "Give me two kilos."], "How much are the mangoes?", "Magkano = how much."),
        LI("Sige, ikaw ang bahala.", ["Okay, it's up to you.", "Yes, I like that.", "Let's go home."], "Okay, it's up to you.", "Mrs. Jones lets Ada decide."),
        BU("Thank you.", "Maraming salamat."),
        BU("Is a photo needed?", "Kailangan rin ba ng litrato?"),
        BU("Mother, why don't we try the MRT?", "Nay, bakit hindi natin subukan ang MRT?"),
        BU("Give me two kilos.", "Bigyan mo ako ng dalawang kilo."),
        BU("What about the children's food?", "Paano ang pagkain ng mga bata?"),
        MA("Match the word to its meaning (Asking Directions).", [("bumabâ", "to go down"), ("tumawíd", "to cross"), ("dumalaw", "to visit"), ("malapit", "near")]),
        MA("Match the word to its meaning (At the Bank).", [("lisensiya", "license"), ("sukat", "size"), ("magbukas", "to open"), ("maglagak", "to deposit")]),
        MA("Match the word to its meaning (Introductions).", [("pagbebenta", "sales"), ("pananaliksík", "research"), ("páliparan", "airport"), ("magsikap", "to work hard")]),
    ],
    "recap": [
        "Meeting people: Maligayang pagdating (welcome); Ikinagagalak kitang makilala (I am pleased to meet you).",
        "Directions: Mawalang-galang na po (excuse me); tumawíd (to cross); malapit / malayò (near / far).",
        "Bank: maglagak (to deposit), magbukas (to open), magpalit ng pera (to change currency), pakipunán (please fill up).",
        "Meeting: Kalihim (secretary); Maraming salamat sa inyong pagdalo (thank you very much for coming).",
        "Market: Magkano ang…? Bigyan mo ako ng… Pakikuwenta lahat.",
    ],
}
