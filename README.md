# Tagalify v2.00

A complete, offline study guide for learning Tagalog, built for native English speakers starting from zero. It installs on Android as an app (a Progressive Web App) and works without a connection after the first visit.

## What's inside

| Unit | Lessons |
|---|---|
| Start here | How Tagalog sentences work · Tagalog and the Filipino people |
| Sounds and greetings | 1. The Tagalog alphabet · 2. Syllables and stress · 3. Greetings and common expressions |
| Building sentences | 4. The articles si and ang · 5. Sentence formation · 6. Personal and demonstrative pronouns |
| Joining and owning | 7. Words that link and describe · 8. Words that show possession |
| Asking and comparing | 9. Asking questions · 10. The question word ba · 11. Making comparisons |
| Having and counting | 12. Using may and mayroón · 13. Numbers |
| Action words (verbs) | 14. -Um- and mag- verb forms · 15. -In- verb forms · 16. The articles ang and ng |
| Wanting, able, becoming, having | 17. Pseudo verbs: dápat, gustó and others · 18. Ma- and Maka- verb forms · 19. Magíng: to be or to become · 20. Magkaroón: to have |
| Thoughts, feelings and requests | 21. Expressing thoughts and actions · 22. Expressing emotions · 23. Who, which and that · 24. Saying please · 25. Saán and násaán: where |
| Where, for whom and when | 26. The preposition sa · 27. Para sa and para kay: for and to · 28. Telling time · 29. The word when in Tagalog · 30. Verb roots |
| Nouns, more verbs and adverbs | 31. Forming nouns · 32. I- verb forms · 33. -An verb forms · 34. Adverbs |
| Joining ideas and agreeing | 35. Conjunctions and interjections · 36. Magpa- and pa- + -in verb forms · 37. Expressing Disagreement, Agreement or Doubt · 38. Forming nouns from verbs · 39. Forming participles using naka- |
| Building words, and colours | 40. Noun affixes · 41. Formation of adjectives · 42. Plural forms of verbs · 43. Contractions · 44. Colors |
| Appendices: food, idioms and conversation | A1. Foods · A2. Cooking terms · A3. Tagalog idioms · A4. Everyday Tagalog expressions · A5. Conversations: meeting people, directions, the bank, a meeting, the market · A6. Conversations: the mall, mealtime, visiting the sick, school, a vacation · A7. Book vocabulary list: more words |
| Review exercises | R1. Review: Parts I and II – sentences, passives and possessives · R2. Review: Parts III and IV – pronouns, describing words and ang, ng, sa · R3. Review: Parts V and VI – verbs, saan/nasaan, time and ma-/maka- · R4. Review: Parts VII and VIII – particles, comparisons, can and should, causatives and passives |

57 lessons, 3239 words, 1552 exercises, plus a one-page cheat sheet and the book's two Vocabulary Lists (Words › Book list).

Every Tagalog word is written with the textbook's accent marks (kapé, báhay, punò, punô), and every meaning matches the textbook. The sound guide uses CAPITALS for the stressed syllable and **Q** for the glottal catch, the same notation as Lesson 2 of the book.

Each lesson has three steps, and each step has its own progress bar:

1. **Read**: illustrated pages with colour-coded grammar. Every coloured word can be tapped to hear it.
2. **Learn the words**: flashcards that add each word to your spaced-repetition reviews.
3. **Practise**: multiple choice, listening, sentence building and matching. Wrong answers come back at the end, and you earn stars for your first-try score.

Lesson progress = 40% reading + 30% words learned + 30% practice (70% or more fills the practice bar).

### The colour key

| Colour | Role | Examples |
|---|---|---|
| Blue | Marker (the book calls si and ang articles) | ang, si, sa, ni, ng |
| Green | Noun | bahay, aso, Ana |
| Orange | Predicate (action or description) | malaki, kumakain |
| Purple | Pronoun | ako, ikaw, siya, ito |
| Pink | Linker (the book calls them ligatures) | -ng, -g, na |
| Teal | ay | ay |
| Gold | Owner word | ko, aking, niya |
| Indigo | Polite word | pô, hô, opô |

## Put it on GitHub (free hosting)

1. Create a new repository on GitHub, for example `tagalify`.
2. Upload **everything in this folder** (keep the folder structure: `data/`, `audio/`, `tools/` and the files at the top level).
3. In the repository, open **Settings → Pages**. Under *Build and deployment*, choose **Deploy from a branch**, pick `main` and `/ (root)`, then **Save**.
4. After a minute your app is live at `https://<your-username>.github.io/tagalify/`.
5. On your Android phone, open that link in Chrome, tap the **⋮** menu and choose **Add to Home screen** (or **Install app**).

When you upload a newer version later, open `sw.js` and change `VERSION` (for example to `tagalify-v1.02`) so phones download the update.

## Dropbox backup (set up once)

Tagalify backs up your progress and all recordings to **Dropbox › Apps › Tagalify**, the same way as your other apps.

1. Go to dropbox.com/developers/apps and choose **Create app**.
2. Choose **Scoped access**, then **App folder**, and name it **Tagalify**.
3. On the **Permissions** tab, tick `files.metadata.read`, `files.metadata.write`, `files.content.read` and `files.content.write`, then **Submit**.
4. On the **Settings** tab, under **OAuth 2 › Redirect URIs**, add your app's address exactly, for example `https://sskehan.github.io/tagalify/` (with the slash at the end), and tap **Add**.
5. Under **OAuth 2 › Allow public clients (Implicit Grant & PKCE)**, choose **Allow**.
6. The App key (`klrgsofuelkzwbl`) is built into the app from v1.03.
7. In Tagalify open **More › Dropbox backup** and tap **Connect Dropbox**. Sign in and tap **Allow**.

From then on it backs up a few seconds after any change and when you leave the app (on Wi-Fi only, unless you turn that off). On a new phone, install Tagalify, connect Dropbox, and your progress and recordings come back by themselves.

To build the key into the app (so you never type it), put it in `sync.js` on the line `const DBX_KEY_BUILTIN = '';`.

## Computer voice with a Filipino accent

Words without a recording are read by your phone's built-in voice. Install Google's Filipino voice so it sounds right: Play Store › update **Speech Recognition & Synthesis from Google**; phone Settings › search **Text-to-speech** › Preferred engine **Speech Services by Google** › gear › **Install voice data** › **Filipino (Philippines)**. Then close and reopen Tagalify. **More › Computer voice** shows which voice is used and has a test button.

## Recording a native speaker

Tagalify plays sound in this order: your own recordings → audio files in the `audio/` folder → the phone's built-in Filipino voice.

1. In the app, open **More → Open recording studio**.
2. Choose a lesson, tap the red dot, say the word, tap the square to stop. A green dot means it's recorded. Play it back and re-record if needed.
3. Tap **Export all recordings (zip)**.
4. Unzip it and upload the contents of its `audio/` folder into the `audio/` folder on GitHub (replace `manifest.json`).

Now everyone who uses your app hears the real voice. With Dropbox connected, every recording is also backed up to Dropbox › Apps › Tagalify › recordings as soon as it is made, so you don't have to export to keep them safe.

## Adding future lessons

The lessons are written as small Python files in `tools/` (`c02_l01.py` and so on) and turned into the JSON the app reads by `tools/build.py`.

The easiest route is to upload the next chapters to Claude together with this folder and ask it to add them as Lesson 9, 10 and onward, in the same style. It will:

1. Write a new file such as `tools/c11_l09.py`, following the same layout (sections, examples, vocabulary, exercises, recap).
2. Add the lesson id to a unit in the `units` list inside `tools/build.py` (or add a new unit).
3. Run `python3 tools/build.py`. It checks every exercise and word and writes `data/course.json` and `data/lessons/l09.json`.
4. Add any new rules to `tools/c10_reference.py` for the cheat sheet.
5. Bump `VERSION` in `sw.js` and the version in `core.js` (`APP_VERSION`) and `build.py`.

Then upload the changed files to GitHub. Your progress on the phone is kept.

## Your data

Progress and recordings are stored on the phone, and copied to your own Dropbox if you connect it. Nothing is sent anywhere else. You can also save a backup file of your progress from **More › Backup file**.

## Version history

**2.00 – final release**
- Covers the whole of Aspillera's Basic Tagalog up to page 229: Introduction, Lessons 1-44, the Appendices, the Vocabulary Lists and the Review Exercises. The Reading Materials (pages 230-239) are not included (noted in More › About).
- Final audit: Lessons 1-8 and the Introduction independently re-checked against the page images (the later lessons were checked as they were built). Fixed: two greeting translations in Lesson 3, the meaning of marúnong, a practice sentence and a practice table in Lessons 4 and 7 that were not in the book, two quiz options in Lesson 7, and two Lesson 18 listening quizzes that relied on stress the computer voice cannot show.
- Whole-app checks: no duplicate words, every quiz answer among its options, no repeated options, cross-references between lessons verified.

**1.14**
- Course › Review exercises (book pages 218-229): R1-R4 cover the book's eight Review Parts with every item and the book's answer key. Questions with a printed answer are marked practice (113 exercises); open-ended tasks are "Your turn" prompts; each exercise points to the lesson to revise. Book slips kept as printed with notes. All checked against the page images.

**1.13** (includes everything in 1.12)
- Words › Book list: the book's two Vocabulary Lists (pages 208-218), Tagalog→English (875 entries) and English→Tagalog (956 entries), exactly as printed, searchable and browsable by letter, with the abbreviations key. A green dot marks words also taught in a lesson (tap to open).
- A7 "Book vocabulary list: more words": the 493 list words not taught in any lesson, as flashcards with match practice.

**1.12**
- New part of the course: Appendices (book pages 189-207) - A1 Foods, A2 Cooking terms, A3 Tagalog idioms, A4 Everyday Tagalog expressions, A5-A6 Conversational Tagalog (ten conversations line by line with the book's English). About 440 new words, all checked against the page images.

**1.11**
- Vocabulary sweep of the Introduction and Lessons 1 to 39: every Tagalog word or phrase the book gives a meaning for is now in that lesson's word list (about 940 new words, shown at the end of each lesson under "More words from this lesson"). Every new word, accent mark and meaning checked against the page images by separate checkers.
- Fixed the accents of magkaíbígan in Lesson 34 to match the book.
- New versions now show up on the phone as soon as they are on GitHub (no more 10-minute wait).

**1.10**
- Recording studio: choose which microphone to record with (for example a RØDE Wireless PRO or other USB-C mic), a live level meter to test it, and an option to turn off the phone's noise filters for external mics. Falls back to the phone mic if the chosen one is unplugged.

**1.09**
- Added Lessons 40 to 44 (book pages 171-188), the last lessons in the book: noun affixes, formation of adjectives, plural forms of verbs, contractions, and colours.
- From this version every Tagalog word or phrase the book gives a meaning for is in the lesson's word list.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.08**
- Added Lessons 35 to 39 (book pages 152-170): conjunctions and interjections, magpa- and pa- + -in verbs, expressing disagreement/agreement/doubt, forming nouns from verbs, and participles with naka-.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.07**
- Added Lessons 31 to 34 (book pages 132-151): forming nouns, i- verb forms, -an verb forms, and adverbs.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.06**
- Added Lessons 26 to 30 (book pages 115-131): the preposition sa, para sa and para kay, telling time, the word "when", and verb roots.
- Recording studio now shows the English meaning under each Tagalog word and sentence.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.05**
- Added Lessons 21 to 25 (book pages 101-115): expressing thoughts and actions, expressing emotions, who/which/that, saying please (paki-/maki-), and saán/násaán.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.04**
- Added Lessons 9 to 20 from the book (pages 52 to 100): asking questions, ba, comparisons, may and mayroón, numbers, -um-/mag- verbs, -in- verbs, ang and ng, pseudo verbs, ma-/maka- verbs, magíng and magkaroón.
- Every Tagalog word, accent mark and meaning checked against the page images by a separate checker.

**1.03**
- Dropbox App key built in, so connecting is one tap.

**1.02**
- Dropbox backup of progress and recordings, automatic on Wi-Fi, with restore on a new phone.
- Computer voice settings: shows whether a Filipino voice is installed, lets you choose the voice and speed, with a test button and install steps.

**1.01**
- New Tagalify app icon on the home screen, splash screen, home page, word cards, recording studio and About.
- Every Tagalog word, accent mark and English meaning checked against the textbook pages and corrected to match. Words that were not in the textbook were removed or replaced with textbook words, and the example sentences now use the book's names (Ruth, Peter, Helen, Tom, Mary).
- The sound guide now follows the book (Q for the glottal catch), with stress shown only where the book marks it.
- Lessons 3 to 8 were rebuilt to follow the book section by section, including all of Lesson 7's ligature sequences and exceptions and Lesson 8's tables.
- Fixes: a stray "null" on the home page, italics in lesson text, the phone's back button now closes a word card, search ignores accent marks, and reading progress stays correct after lesson updates.

**1.00**
- First release: Introduction and Lessons 1 to 8.

## Credits

The lessons follow the order and topics of Paraluman S. Aspillera's *Basic Tagalog* (Introduction and Lessons 1 to 8). The explanations, examples and exercises are rewritten for beginners who speak English.
