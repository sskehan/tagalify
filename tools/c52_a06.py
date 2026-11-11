from dsl import *

# Conversational Tagalog, part 2 (book pages 203-207).
# Lines: (speaker or None for the narrator, Tagalog as printed, English as printed, parts)


def conv(lines):
    out = []
    for who, tl, en, parts in lines:
        out.append((tl, f"{who}: {en}" if who else en, parts))
    return out


MALL = [
    (None, "Isa sa mga libangan ng mga Pilipino sa lungsod ay ang pagtungo sa mall tuwing Sabado at Linggo. Isang Sabado, ang mag-asawang Fidel at Dolor at ang kanilang mga anak na sina Boyet at Helen, ay nagpunta sa isang mall sa Quezon City.",
     "One of the recreational activities of Filipinos in the city is going to the mall on weekends. One Saturday, the couple Fidel and Dolor and their children, Boyet and Helen, went to a mall in Quezon City.", []),
    ("DOLOR", "Tumingin-tingin muna tayo sa mga tindahan bago manood ng sine.", "Let's take a look around at the stores first before we watch a movie.", []),
    ("HELEN", "Pumunta tayo sa tindahan ng mga plaka. May bagong labas ngayon ang bandang Hale.", "Let's go to the record store. The band Hale has a new release.", []),
    ("BOYET", "Sa tindahan ng mga kompyuter ang gusto ko. May mga bagong labas na mga laro.", "I like to go to computer stores. There are new games.", []),
    ("DOLOR", "Pumunta rin tayo sa loob ng department store. Bagsak-presyo sila sa maraming bagay. Baka makabili ako ng sapatos.",
     "Let's go inside the department store. They have slashed prices on many items. I might be able to buy a pair of shoes.", []),
    ("FIDEL", "Ay naku, lumalaki ang gastos!", "My! It's getting more expensive!", []),
    ("HELEN", "Daddy, tignan mo. Napakaraming kainan dito. Parang masarap lahat.", "Look Daddy, there are many restaurants here. They all seem good.", []),
    ("FIDEL", "Oo nga, pero mahal lamang ng kaunti.", "Yes, it's true, but it's a bit more expensive.", []),
    ("DOLOR", "Fidel, bakit hindi ka bumili ng bagong pantalon? Luma na ang damit pampasok mo sa opisina.",
     "Fidel, why don't you buy a new pair of pants? Your office clothes are already worn-out.", []),
    ("FIDEL", "Tignan natin.", "Let's see.", []),
    ("BOYET", "Daddy, Mommy, may palabas pala ang mga artista dito. Manood tayo.", "Daddy, Mommy, there's a show by artists here. Let's have a look.", []),
    ("DOLOR", "Baka tayo gabihin.", "It might be late by then.", []),
    ("BOYET", "Sandali lamang po. Wala namang pasok bukas.", "It won't take long. Anyway, there are no classes tomorrow.", []),
    ("DOLOR", "Siya, siya, sige na nga.", "All right, all right, let's go.", []),
]

BREAKFAST = [
    (None, "Magkasabay nag-agahan ang pamilyang Aquino nang umagang iyon. Gaya ng dati, naghanda ng sinangag na kain si Aling Betty para sa pamilya. Nagprito rin siya ng tuyo at nagbati ng itlog.",
     "The Aquino family had breakfast together that morning. As usual, Aling Betty prepared fried rice for her family. She also fried dried fish and scrambled eggs.", []),
    ("ALING BETTY", "Kumain kayo habang mainit pa ang sinangag.", "You better eat now while the fried rice is still hot.", []),
    ("MANG JOSE", "Magdasal muna tayo bago kumain.", "Let's pray first before eating.", []),
    ("DAUGHTER", "Nanay, paki-abot po ang binating itlog at kanin.", "Mother, please pass the scrambled eggs and rice.", []),
    ("SON", "Gusto ko rin po ng binating itlog.", "I also like scrambled eggs.", []),
    ("MANG JOSE", "Pakilagyan nga ng mainit na tubig ang tasa ko.", "Could you please pour hot water into my cup?", []),
    ("ALING BETTY", "Mga bata, inumin ninyo ang inyong tsokolate.", "Children, drink your chocolate.", []),
    ("CHILDREN", "Opô, inay.", "Yes, mother.", []),
    ("ALING BETTY", "Kumain kayo nang mabuti para hindi magutom sa eskuwela.", "Eat well, so you won't get hungry in school.", []),
]

LUNCH = [
    ("LORENZO", "Ano ang pananghalian, Manang?", "What's for lunch, Manang?", []),
    ("MAID", "Nagluto ako ng paksiw na bangus at ginisang monggo.", "I cooked milkfish in vinegar and sauteed mung beans.", []),
    ("LORENZO", "May kahalo bang bunga ng ampalaya?", "Does it have bittermelon fruit?", []),
    ("MAID", "Oo, isinama ko na pati dahon.", "Yes, I also included the leaves.", []),
    ("LORENZO", "Naku, masarap ang kain ko ngayon.", "My, I shall have a good meal today.", []),
    ("MAID", "May minatamis din na saba.", "There is also sweetened saba.", []),
]

SUPPER = [
    (None, "Gabi na nang dumating si Mang Ignacio sa kanilang bahay.", "It was already late in the evening when Mang Ignacio arrived home.", []),
    ("MANG IGNACIO", "Masyado akong natrapik sa EDSA kaya ako ginabi.", "I was caught in a traffic along EDSA, that's why I'm late.", []),
    ("ALING MAYA", "Siya, kumain ka na. Baka gutom na gutom ka na. Iinit ko lang ang ulam. Kumain na ang mga bata. Nag-aaral sila sa kanilang kuwarto.",
     "Well, you better eat now. I will reheat your food. The children had already eaten. They are studying in their room.", []),
    ("MANG IGNACIO", "Salamat. Masarap ang ulam. Gusto ko ng ginataang tilapia.", "Thank you. The viand is delicious. I like tilapia in coconut milk.", []),
]

VISIT = [
    (None, "Dumalaw si Aling Lourdes sa kaibigang maysakit. May dala siyang isang dosenang dalandan.", "Lourdes visited her sick friend. She brought a dozen oranges.", []),
    ("LOURDES", "Tao po.", "(The book gives no translation here; see the notes below.)", []),
    ("PEDRO", "Aba! Si Aling Lourdes pala. Pasok kayo.", "Oh! It's Aling Lourdes. Please come in.", []),
    ("LOURDES", "Kamusta ang asawa mo?", "How is your wife?", []),
    ("PEDRO", "Mabuti-buti po ngayon. Pasok kayo. Narito siya.", "She's getting better now. Please come in. She is here.", []),
    ("LOURDES", "Maria, kumusta ka na? Ano ba ang lagay mo ngayon?", "Maria, how are you? What is your condition now? How are you feeling now?", []),
    ("MARIA", "Masakit ang aking dibdib at may lagnat ako sa hapon.", "My chest is painful and I have fever in the afternoon.", []),
    ("LOURDES", "Maganda na ang kulay mo ngayon kaysa noong huli kitang dinalaw. May dala akong dalandan para sa iyo.",
     "Your color is better now than the last time I visited you. I brought some oranges for you.", []),
    ("MARIA", "Naku, salamat, Lourdes. Nag-abala ka pa.", "Thank you, Lourdes. You shouldn't have bothered.", []),
    ("LOURDES", "Mabuti'y patingin ka na sa doctor habang maaga nang gumaling ka.", "It's better for you to see a doctor this early so you can recover faster.", []),
    ("MARIA", "Oo nga. Dadalhin ako ng aking anak sa PGH (or Philippine General Hospital) bukas. Wala raw bayad doon.",
     "Yes, that's true. My son will take me to PGH tomorrow. They say it's free there.", []),
    ("LOURDES", "Siya, hindi na ako magtatagal para makapahinga ka na. At saka na ako paparito ulit.",
     "Well, I will not stay long so you can have some rest. I will visit you again.", []),
    ("MARIA", "Maraming salamat sa pagdalaw mo.", "Thank you for visiting.", []),
    ("LOURDES", "Adios.", "Goodbye.", []),
]

SCHOOL = [
    (None, "Tapos na ang bakasyon sa tag-araw ng mga estudiyante. Muling pumasok sa kanilang paaralan sina Antonio at Roberta. May nakilala silang bagong lipat mula sa ibang paaralan at nagpakilala sila.",
     "The students' summer vacation had ended. Antonio and Roberta went back to school. They met a transferee from another school and they introduced themselves.", []),
    ("ANTONIO", "Ang pangalan ko ay Antonio.", "My name is Antonio.",
     [("Ang", "the", "marker"), ("pangalan", "name", "noun"), ("ko", "my", "poss"), ("ay", "is", "ay"), ("Antonio", "Antonio", "noun")]),
    ("ROBERTA", "Ang pangalan ko naman ay Robert.", "And my name is Roberta.", []),
    ("RICKY", "Ako si Ricky. Galing ako sa Bulacan.", "I am Ricky. I came from Bulacan.", []),
    ("ANTONIO", "Bakit ka lumipat dito sa Maynila?", "Why did you transfer to Manila?", []),
    ("RICKY", "Mas malapit ang trabaho ng ama ko dito kaysa sa Bulacan kaya lumipat na rin ang buong pamilya namin dito.",
     "My father's work is nearer here than to Bulacan so the whole family decided to move here.", []),
    ("ROBERTA", "Ano ba ang taon at seksiyon mo?", "What is your year and section?", []),
    ("RICKY", "Pangalawang taon, seksiyon 2.", "Second year, section 2.", []),
    ("ANTONIO", "Magkaseksiyon pala tayo sa pangalawang taon. Halika, sumama ka sa amin. Tumunog na ang kampana.",
     "It seems we belong to the same section in the second year. Come, join us. The bell has rung.", []),
    ("RICKY", "Salamat.", "Thank you.", []),
    ("ROBERTA", "Maraming nag-aaral dito. May pang-umaga at may panghapon na mga seksiyon. Mahusay rin ang mga guro rito.",
     "There are many students here. There are morning and afternoon sections. The teachers here are also good.", []),
    ("RICKY", "Nasaan ang aklatan?", "Where is the library?", []),
    ("ANTONIO", "Nasa ikatlong palapag. Ipapasyal ka namin mamaya sa buong eskuwelahan, sa aklatan, sa gym at palaruan sa likod ng gusali.",
     "On the third floor. We will tour you later around the school, to the library, gym and playground behind the building.", []),
    ("ROBERTA", "May kantina rin banda roon. Doon tayo manananghalian.", "There's a canteen over there. We will have lunch there.", []),
    ("RICKY", "May dala akong baon.", "I brought my own lunch.", []),
    ("ANTONIO", "Hindi bale. Dalhin mo, doon ka na kumain sa kantina.", "It doesn't matter. Bring your lunch with you and eat it in the canteen.", []),
    ("RICKY", "Salamat. Maraming salamat. Sana maging magkakaibigan tayo.", "Thank you. Thank you very much. I hope we would be friends.", []),
    ("ROBERTA", "Siyempre naman.", "Of course.", []),
]

VACATION = [
    (None, "Ang mag-anak na Santos ay pumunta sa isang bakasyunan sa Batangas. Malapit ang bakasyunan sa dagat at maraming mga punong niyog sa paligid.",
     "The Santos family went to a resort in Batangas. The resort is near the sea and has many coconut trees all around.", []),
    ("SON", "Lumangoy tayo sa dagat mamaya.", "Let's swim in the sea later.", []),
    ("MOTHER", "Teka, hindi pa tayo nakakapag-ayos ng mga gamit natin. Pumunta muna tayo sa kubo na inilaan sa atin.",
     "Wait. We have not fixed our things yet. Let's go first to the nipa hut reserved for us.", []),
    ("DAUGHTER", "Inay, tignan mo. May bangka sa aplaya. Puwede tayong mamangka.", "Mother, look. There's a boat on the beach. We can go boating.", []),
    ("FATHER", "Makikipag-ayos tayo sa katiwala tungkol sa pamamangka. Kailangang mag-ingat tayo. Kung minsan lumalakas ang alon sa lugar na ito.",
     "We will make an arrangement with the caretaker regarding the use of the boat. We have to be careful. Sometimes the waves in this place can be very strong.", []),
    ("MOTHER", "Ibaba na ninyo ang mga gamit mula sa kotse. Iyong mga kaldero, mga plato, kalan, ihawan, kubyertos at ang lalagyan ng yelo.",
     "Unload the things from the car. The pans, plates, stove, griller, the silverware and the ice container.", []),
    ("FATHER", "Narito ang lahat. Ano ba ang iluluto natin ngayon?", "Everything is here. What are we going to cook now?", []),
    ("MOTHER", "Ihawin mo na ang dalag na nabili natin sa daan. At ilaga mo na ang mga alimango. Nagluto na ako ng adobong manok at gulay sa bahay kaninang umaga.",
     "Grill the mudfish that we bought along the road. Boil the crabs, too. I already cooked chicken adobo and vegetables at home.", []),
    ("FATHER", "Hoy, mga bata. Tulungan ninyo ako rito. Pagkapananghalian ay maglalakad tayo sa aplaya. Makapamumulot kayo ng kabibe.",
     "Hey children. Give me a hand. After lunch, we'll walk along the beach. You can pick up shells.", []),
    ("CHILDREN", "Tayo na, bilisan natin para makalangoy tayo kaagad.", "Come on, hurry so we can swim at once.", []),
]


LESSON = {
    "id": "a06",
    "label": "A6",
    "title": "Conversations: the mall, mealtime, visiting the sick, school, a vacation",
    "summary": "Five more conversations with the book's translations: a family day at the mall, breakfast, lunch and supper at home, visiting a sick friend, the first day back at school, and a family beach trip",
    "minutes": 35,
    "goals": [
        "Follow a family conversation at the mall",
        "Talk at the table at breakfast, lunch and supper",
        "Visit a sick friend politely, starting with Tao pô",
        "Introduce yourself to new classmates",
        "Follow a family planning a day at the beach",
        "Use aling, mang, manang, manong and ate correctly",
    ],
    "sections": [
        S("At the mall",
          P("**Sa Mall** (*At the Mall*). Going to the mall on weekends is one of the recreational activities of Filipinos in the city. Fidel, Dolor and their children Boyet and Helen spend a Saturday at a mall in Quezon City."),
          EXS(conv(MALL), title="At the Mall"),
          BOX("culture", "Notes: the mall", items=[
              "It is never enough to translate *mall* as **tindahan** (*store*). Malls in the Philippines are multistory shopping centers offering everything from food and entertainment to books and clothes.",
              "The English word **mall** has been part of Filipino speech, probably since the early 1990s.",
              "It is also used almost like *department store*, although a department store may also be found inside a mall."]),
          VOC("mall", "Words and phrases")),

        S("At mealtime",
          P("**Sa Oras ng Pagkain** (*At Mealtime*) has three short scenes: **almusal** (breakfast), **tanghalian** (lunch) and **hapunan** (supper)."),
          EXS(conv(BREAKFAST), title="A. Almusal (Breakfast)"),
          EXS(conv(LUNCH), title="B. Tanghalian (Lunch)"),
          EXS(conv(SUPPER), title="C. Hapunan (Supper)"),
          BOX("culture", "Vocabulary List and Notes", items=[
              "**almusál** = breakfast, also **agahan**.",
              "**siya** = a colloquial term for *all right* or *okay* (Siya, kumain ka na = Well, you better eat now). Do not confuse it with the pronoun **siyá**.",
              "**ulam** = viand; the dish of meat or vegetables that goes with rice in every meal.",
              "**manang** (for females) or **manong** (for males) = names used to address an older maid or any elderly person who serves in a household or sells commodities.",
              "**ate** (pronounced **a-te**) is frequently used to address a younger maid."]),
          VOC("meal", "Vocabulary List and Notes")),

        S("Visiting an ill person",
          P("**Pagdalaw Sa Maysakít** (*Visiting an Ill Person*). Aling Lourdes visits her sick friend Maria and brings a dozen oranges."),
          EXS(conv(VISIT), title="Visiting an Ill Person"),
          BOX("culture", "Notes", items=[
              "**Tao pô** = a set expression used to announce that a person is outside somebody's house, especially if there is no doorbell.",
              "**aling** (for females) or **mang** (for males) = placed before the names of unrelated older persons. Even people of the same age, especially older people themselves, call each other this way (Aling Lourdes, Mang Ignacio)."]),
          BOX("warn", "Book spellings", t="In this conversation the book prints both **Kamusta** and **kumusta** (how are you)."),
          VOC("visit", "Notes and phrases")),

        S("At school",
          P("**Sa Páaralán** (*At School*). Summer vacation is over. Antonio and Roberta meet Ricky, a transferee from another school."),
          EXS(conv(SCHOOL), title="At School"),
          BOX("warn", "A slip in the book", t="Roberta's line prints **Robert** in the Tagalog, but the English says **Roberta**. It is shown here exactly as printed."),
          VOC("school", "Phrases from the conversation")),

        S("Let's go on a vacation",
          P("**Magbakasyón Táyo** (*Let's Go on a Vacation*). The Santos family goes to a beach resort in Batangas."),
          EXS(conv(VACATION), title="Let's Go on a Vacation"),
          VOC("vac", "Phrases from the conversation"),
          BOX("remember", "Remember", items=[
              "**Tao pô** announces you at someone's door; **Pasok kayo** = Please come in.",
              "**aling / mang** go before the names of older people; **manang / manong** address an older maid or vendor; **ate** a younger maid.",
              "**siya** (no accent) = all right, okay; **siyá** = he, she.",
              "Meals: **almusál / agahan** (breakfast), **tanghalian** (lunch), **hapunan** (supper); **ulam** goes with rice.",
              "Handy replies: **Tignan natin** (Let's see), **Hindi bale** (It doesn't matter), **Siyempre naman** (Of course)."])),
    ],
    "vocab": [
        # mall
        V("tindahan-a06", "tindahan", "store", pos="noun", group="mall", note="Lesson 1 prints tindáhan."),
        V("mall-a06", "mall", "mall (a multistory shopping center)", pos="noun", group="mall"),
        V("tignan-natin-a06", "Tignan natin.", "Let's see.", pos="phrase", group="mall"),
        V("baka-tayo-gabihin-a06", "Baka tayo gabihin.", "It might be late by then.", pos="phrase", group="mall"),
        V("siya-siya-sige-a06", "Siya, siya, sige na nga.", "All right, all right, let's go.", pos="phrase", group="mall"),
        # meals
        V("almusal-a06", "almusál", "breakfast", say="al-mu-SAL", pos="noun", group="meal", note="Also agahan (in Appendix A2)."),
        V("tanghalian-a06", "tanghalian", "lunch", pos="noun", group="meal"),
        V("hapunan-a06", "hapunan", "supper", pos="noun", group="meal", note="Lesson 42 prints hapúnan."),
        V("siya-okay-a06", "siya", "all right; okay (colloquial)", pos="part", group="meal", note="Do not confuse with the pronoun siyá."),
        V("ulam-a06", "ulam", "viand; dish of meat or vegetables that goes with rice in every meal", pos="noun", group="meal"),
        V("manang-a06", "manang", "name used to address an older maid or any elderly person who serves in a household or sells commodities (for females)", pos="noun", group="meal"),
        V("manong-a06", "manong", "name used to address an older maid or any elderly person who serves in a household or sells commodities (for males)", pos="noun", group="meal"),
        V("ate-a06", "ate", "used to address a younger maid", say="a-te", pos="noun", group="meal", note="The book says it is pronounced a-te."),
        # visit
        V("tao-po-a06", "Tao pô", "a set expression used to announce the presence of a person outside of somebody's house, especially if there is no doorbell", pos="phrase", group="visit"),
        V("aling-a06", "aling", "name used to address unrelated older persons (for females), placed before the name", pos="noun", group="visit"),
        V("mang-a06", "mang", "name used to address unrelated older persons (for males), placed before the name", pos="noun", group="visit"),
        V("pasok-kayo-a06", "Pasok kayo.", "Please come in.", pos="phrase", group="visit"),
        V("nag-abala-ka-pa-a06", "Nag-abala ka pa.", "You shouldn't have bothered.", pos="phrase", group="visit"),
        V("maraming-salamat-pagdalaw-a06", "Maraming salamat sa pagdalaw mo.", "Thank you for visiting.", pos="phrase", group="visit"),
        V("adios-a06", "Adios.", "Goodbye.", pos="phrase", group="visit"),
        # school
        V("nasaan-aklatan-a06", "Nasaan ang aklatan?", "Where is the library?", pos="phrase", group="school"),
        V("may-dala-akong-baon-a06", "May dala akong baon.", "I brought my own lunch.", pos="phrase", group="school"),
        V("hindi-bale-a06", "Hindi bale.", "It doesn't matter.", pos="phrase", group="school"),
        V("siyempre-naman-a06", "Siyempre naman.", "Of course.", pos="phrase", group="school"),
        # vacation
        V("lumangoy-tayo-a06", "Lumangoy tayo sa dagat mamaya.", "Let's swim in the sea later.", pos="phrase", group="vac"),
        V("narito-ang-lahat-a06", "Narito ang lahat.", "Everything is here.", pos="phrase", group="vac"),
        V("tulungan-ninyo-ako-a06", "Tulungan ninyo ako rito.", "Give me a hand.", pos="phrase", group="vac"),
    ],
    "exercises": [
        CH("According to the book's note, is \"tindahan\" (store) a good translation of mall?", ["No: malls are multistory shopping centers offering everything", "Yes: they mean exactly the same", "No: a mall is a market (palengke)"], "No: malls are multistory shopping centers offering everything", "It is never sufficient to translate mall as tindahan."),
        CH("Fidel says \"Tignan natin.\" What does he mean?", ["Let's see.", "Let's go.", "Let's eat."], "Let's see.", "His answer when Dolor suggests new pants."),
        CH("Which word is another word for almusál (breakfast)?", ["agahan", "tanghalian", "hapunan"], "agahan", "tanghalian = lunch; hapunan = supper."),
        CH("What is \"ulam\"?", ["the dish of meat or vegetables that goes with rice in every meal", "fried rice", "a sweet dessert"], "the dish of meat or vegetables that goes with rice in every meal", "Masarap ang ulam = The viand is delicious."),
        CH("Aling Maya says \"Siya, kumain ka na.\" What does siya mean here?", ["all right / okay (well)", "he or she", "already"], "all right / okay (well)", "Do not confuse colloquial siya with the pronoun siyá."),
        CH("Whom do you call \"manong\"?", ["an older man who serves in a household or sells commodities", "a younger maid", "your own father"], "an older man who serves in a household or sells commodities", "Manang is for females; ate is used for a younger maid."),
        CH("When do you say \"Tao pô\"?", ["To announce that you are outside somebody's house", "To say goodbye", "To thank a host"], "To announce that you are outside somebody's house", "Especially if there is no doorbell."),
        CH("Where does \"aling\" or \"mang\" go?", ["Before the name of an older person", "After the name", "At the end of the sentence"], "Before the name of an older person", "Aling Lourdes, Mang Ignacio."),
        CH("Maria says \"Nag-abala ka pa.\" What does she mean?", ["You shouldn't have bothered.", "You are very late.", "Please come in."], "You shouldn't have bothered.", "She says it when Lourdes brings oranges."),
        CH("Antonio says \"Hindi bale.\" What does it mean?", ["It doesn't matter.", "Of course.", "Thank you."], "It doesn't matter.", "Ricky has brought his own lunch."),
        LI("Siyempre naman.", ["Of course.", "Let's see.", "It doesn't matter."], "Of course.", "Roberta's answer to Ricky."),
        LI("Nasaan ang aklatan?", ["Where is the library?", "Where is the canteen?", "Where is the playground?"], "Where is the library?", "aklatan = library."),
        LI("Opô, inay.", ["Yes, mother.", "Thank you, mother.", "Good morning, mother."], "Yes, mother.", "The children's polite answer."),
        LI("Adios.", ["Goodbye.", "Thank you.", "Welcome."], "Goodbye.", "Lourdes's last word."),
        BU("Let's see.", "Tignan natin."),
        BU("My name is Antonio.", "Ang pangalan ko ay Antonio."),
        BU("Where is the library?", "Nasaan ang aklatan?"),
        BU("I brought my own lunch.", "May dala akong baon."),
        BU("Let's swim in the sea later.", "Lumangoy tayo sa dagat mamaya."),
        BU("Thank you for visiting.", "Maraming salamat sa pagdalaw mo."),
        MA("Match the meal word to its meaning.", [("almusál", "breakfast"), ("tanghalian", "lunch"), ("hapunan", "supper"), ("ulam", "viand")]),
        MA("Match the line to its meaning.", [("Pasok kayo.", "Please come in."), ("Baka tayo gabihin.", "It might be late by then."), ("Narito ang lahat.", "Everything is here."), ("Tulungan ninyo ako rito.", "Give me a hand.")]),
        MA("Match the word to whom it is used for.", [("aling", "an older woman (before her name)"), ("mang", "an older man (before his name)"), ("manang", "an older maid or woman vendor"), ("ate", "a younger maid")]),
    ],
    "recap": [
        "A mall is more than a tindahan (store): it is a multistory shopping center.",
        "Meals: almusál or agahan (breakfast), tanghalian (lunch), hapunan (supper); ulam is the dish eaten with rice.",
        "Siya (no accent) = all right, okay; siyá = he, she.",
        "Tao pô announces you at the door; aling / mang go before older people's names; manang / manong and ate address household helpers and vendors.",
        "Handy replies: Tignan natin (Let's see), Hindi bale (It doesn't matter), Siyempre naman (Of course), Adios (Goodbye).",
    ],
}
