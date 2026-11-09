# Tagalify v1.00

A complete, offline study guide for learning Tagalog, built for native English speakers starting from zero. It installs on Android as an app (a Progressive Web App) and works without a connection after the first visit.

## What's inside

| Unit | Lessons |
|---|---|
| Start here | How Tagalog sentences work (beginner primer) · Tagalog and the Filipino people |
| Sounds and greetings | 1. The alphabet · 2. Syllables and stress · 3. Greetings and common expressions |
| Building sentences | 4. Si, sina, ang, ang mga · 5. Sentence formation · 6. Pronouns, this and that |
| Joining and owning | 7. Linkers -ng, -g, na · 8. Possession |

10 lessons, 256 words, 202 exercises, plus a one-page cheat sheet.

Each lesson has three steps, and each step has its own progress bar:

1. **Read**: illustrated pages with colour-coded grammar. Every coloured word can be tapped to hear it.
2. **Learn the words**: flashcards that add each word to your spaced-repetition reviews.
3. **Practise**: multiple choice, listening, sentence building and matching. Wrong answers come back at the end, and you earn stars for your first-try score.

Lesson progress = 40% reading + 30% words learned + 30% practice (70% or more fills the practice bar).

### The colour key

| Colour | Role | Examples |
|---|---|---|
| Blue | Marker | ang, si, sa, ni, ng |
| Green | Noun | bahay, aso, Ana |
| Orange | Predicate (action or description) | malaki, kumakain |
| Purple | Pronoun | ako, ikaw, siya, ito |
| Pink | Linker | -ng, -g, na |
| Teal | ay | ay |
| Gold | Owner word | ko, aking, niya |
| Indigo | Polite word | po, ho, opo |

## Put it on GitHub (free hosting)

1. Create a new repository on GitHub, for example `tagalify`.
2. Upload **everything in this folder** (keep the folder structure: `data/`, `audio/`, `tools/` and the files at the top level).
3. In the repository, open **Settings → Pages**. Under *Build and deployment*, choose **Deploy from a branch**, pick `main` and `/ (root)`, then **Save**.
4. After a minute your app is live at `https://<your-username>.github.io/tagalify/`.
5. On your Android phone, open that link in Chrome, tap the **⋮** menu and choose **Add to Home screen** (or **Install app**).

When you upload a newer version later, open `sw.js` and change `VERSION` (for example to `tagalify-v1.01`) so phones download the update.

## Recording a native speaker

Tagalify plays sound in this order: your own recordings → audio files in the `audio/` folder → the phone's built-in Filipino voice.

1. In the app, open **More → Open recording studio**.
2. Choose a lesson, tap the red dot, say the word, tap the square to stop. A green dot means it's recorded. Play it back and re-record if needed.
3. Tap **Export all recordings (zip)**.
4. Unzip it and upload the contents of its `audio/` folder into the `audio/` folder on GitHub (replace `manifest.json`).

Now everyone who uses your app hears the real voice.

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

Progress is stored on the phone only (no account, nothing is sent anywhere). Use **More → Back up** before changing phones, and **Restore** on the new one. Recordings are stored separately on the phone; export them to keep them.

## Credits

The lessons follow the order and topics of Paraluman S. Aspillera's *Basic Tagalog* (Introduction and Lessons 1 to 8). The explanations, examples and exercises are rewritten for beginners who speak English.
