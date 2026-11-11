'use strict';
/* Tagalify core: storage, data, audio (recordings > files > speech), rich text and lesson blocks. */

const APP_VERSION = '1.13';
const KEY = 'tagalify.v1';
const DEFAULTS = { newPerDay: 10, direction: 'mixed', sound: true, theme: 'auto', size: 1, voice: '', rate: 0.9 };

let db = loadDb();
let course = null;
const lessons = new Map();   // id -> lesson json
const words = new Map();     // key -> word
let ref = null;
let manifest = {};

/* ---------- storage ---------- */
function loadDb() {
  try {
    const d = JSON.parse(localStorage.getItem(KEY));
    if (d && typeof d === 'object') {
      return { cards: d.cards || {}, log: d.log || {}, lessons: d.lessons || {}, settings: { ...DEFAULTS, ...(d.settings || {}) }, savedAt: d.savedAt || 0 };
    }
  } catch (e) { /* start fresh */ }
  return { cards: {}, log: {}, lessons: {}, settings: { ...DEFAULTS }, savedAt: 0 };
}
function save(quiet) {
  if (!quiet) db.savedAt = Date.now();
  try { localStorage.setItem(KEY, JSON.stringify(db)); }
  catch (e) { toast('Could not save progress on this device'); }
  if (!quiet && typeof onSaved === 'function') onSaved();
}
const day = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 864e5);
function logToday() {
  const d = day();
  return db.log[d] || (db.log[d] = { new: 0, reviews: 0, act: 0 });
}
function lstate(id) {
  return db.lessons[id] || (db.lessons[id] = { read: [], pos: 0, best: 0, done: false });
}
function streak() {
  let d = day();
  if (!db.log[d]) d -= 1;
  let n = 0;
  while (db.log[d]) { n++; d--; }
  return n;
}

/* ---------- helpers ---------- */
function h(tag, attrs, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v == null || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'value') el.value = v;
    else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
    else if (v === true) el.setAttribute(k, '');
    else el.setAttribute(k, v);
  }
  for (const kid of kids.flat()) {
    if (kid == null || kid === false) continue;
    el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
  }
  return el;
}
let toastTimer;
function toast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2400);
}
function shuffle(a) {
  a = a.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
function slug(t) {
  return String(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9']+/g, '-').replace(/^-+|-+$/g, '').replace(/'/g, '');
}

/* ---------- data ---------- */
async function loadData() {
  course = await (await fetch('data/course.json', { cache: 'no-cache' })).json();
  await Promise.all(course.lessons.map(async (m) => {
    const L = await (await fetch(m.file, { cache: 'no-cache' })).json();
    L.vocab.forEach((v) => { v.key = L.id + ':' + v.id; v.lesson = L.id; words.set(v.key, v); });
    lessons.set(L.id, L);
  }));
  try { ref = await (await fetch('data/reference.json', { cache: 'no-cache' })).json(); } catch (e) { ref = null; }
  try { manifest = await (await fetch('audio/manifest.json', { cache: 'no-cache' })).json(); } catch (e) { manifest = {}; }
}
const fold = (t) => String(t).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
const lname = (L) => (isNaN(+L.label) ? L.title : 'Lesson ' + L.label);
const orderedLessons = () => course.lessons.map((m) => lessons.get(m.id)).filter(Boolean);

/* ---------- progress ---------- */
function lessonStats(id) {
  const L = lessons.get(id);
  const s = lstate(id);
  const readN = s.read.filter((i) => i < L.sections.length).length;
  const read = L.sections.length ? Math.min(1, readN / L.sections.length) : 1;
  const learnedN = L.vocab.filter((v) => db.cards[v.key]).length;
  const learned = L.vocab.length ? learnedN / L.vocab.length : 1;
  const practice = Math.min(1, (s.best || 0) / 70);
  const pct = 0.4 * read + 0.3 * learned + 0.3 * practice;
  const stars = s.best >= 90 ? 3 : s.best >= 70 ? 2 : s.best > 0 ? 1 : 0;
  return { read, readN, learned, learnedN, practice, pct, stars, total: L.vocab.length };
}
function overall() {
  const ls = orderedLessons();
  if (!ls.length) return 0;
  return ls.reduce((a, L) => a + lessonStats(L.id).pct, 0) / ls.length;
}

/* ---------- spaced repetition ---------- */
function newCard() { return { ease: 2.5, int: 0, reps: 0, lapses: 0, due: day() }; }
function rate(c, q) {
  if (q === 0) { c.reps = 0; c.lapses++; c.int = 0; c.ease = Math.max(1.3, c.ease - 0.2); c.due = day(); return c; }
  c.reps++;
  if (q === 1) { c.int = Math.max(1, Math.round((c.int || 1) * 1.2)); c.ease = Math.max(1.3, c.ease - 0.1); }
  else if (q === 2) { c.int = c.reps === 1 ? 1 : c.reps === 2 ? 3 : Math.round(c.int * c.ease); }
  else { c.int = c.reps === 1 ? 3 : Math.round(Math.max(c.int, 1) * c.ease * 1.3); c.ease += 0.1; }
  c.due = day() + c.int;
  return c;
}
function previewInt(c, q) {
  const t = JSON.parse(JSON.stringify(c));
  rate(t, q);
  return q === 0 ? 'soon' : t.int === 1 ? '1 day' : t.int + ' days';
}
const dueKeys = () => Object.keys(db.cards).filter((k) => words.has(k) && db.cards[k].due <= day());

/* ---------- audio ---------- */
let idb = null;
function openIdb() {
  if (idb) return idb;
  idb = new Promise((res, rej) => {
    try {
      const r = indexedDB.open('tagalify', 1);
      r.onupgradeneeded = () => r.result.createObjectStore('rec');
      r.onsuccess = () => res(r.result);
      r.onerror = () => rej(r.error);
    } catch (e) { rej(e); }
  });
  return idb;
}
async function idbOp(mode, fn) {
  const d = await openIdb();
  return new Promise((res, rej) => {
    const tx = d.transaction('rec', mode);
    const req = fn(tx.objectStore('rec'));
    tx.oncomplete = () => res(req && req.result);
    tx.onerror = () => rej(tx.error);
  });
}
const recGet = (k) => idbOp('readonly', (s) => s.get(k)).catch(() => null);
const recPut = (k, v) => idbOp('readwrite', (s) => s.put(v, k));
const recDel = (k) => idbOp('readwrite', (s) => s.delete(k));
const recKeys = () => idbOp('readonly', (s) => s.getAllKeys()).catch(() => []);

let curAudio = null;
function stopAudio() {
  if (curAudio) { try { curAudio.pause(); } catch (e) { /* ignore */ } curAudio = null; }
  if ('speechSynthesis' in window) speechSynthesis.cancel();
}
function playUrl(url, rateX) {
  return new Promise((res) => {
    const a = new Audio(url);
    a.playbackRate = rateX || 1;
    curAudio = a;
    a.onended = () => res(true);
    a.onerror = () => res(false);
    a.play().catch(() => res(false));
  });
}
const isFil = (v) => /^(fil|tl)/i.test(v.lang);
function filVoices() {
  if (!('speechSynthesis' in window)) return [];
  return speechSynthesis.getVoices().filter(isFil);
}
function pickVoice() {
  if (!('speechSynthesis' in window)) return null;
  const vs = speechSynthesis.getVoices();
  const chosen = db.settings.voice && vs.find((v) => v.voiceURI === db.settings.voice);
  return chosen || vs.find((v) => /^fil/i.test(v.lang)) || vs.find((v) => /^tl/i.test(v.lang)) || null;
}
function tts(text, slow) {
  return new Promise((res) => {
    if (!('speechSynthesis' in window)) { toast('No speech voice on this device'); res(false); return; }
    const u = new SpeechSynthesisUtterance(text);
    const v = pickVoice();
    if (v) { u.voice = v; u.lang = v.lang; } else u.lang = 'fil-PH';
    u.rate = slow ? Math.max(0.4, (db.settings.rate || 0.9) - 0.3) : (db.settings.rate || 0.9);
    u.onend = () => res(true);
    u.onerror = () => res(false);
    speechSynthesis.speak(u);
  });
}
async function say(text, slow) {
  stopAudio();
  const clean = String(text).trim();
  if (!clean) return false;
  const key = slug(clean);
  const rec = await recGet(key);
  if (rec && rec.blob) {
    const url = URL.createObjectURL(rec.blob);
    const ok = await playUrl(url, slow ? 0.7 : 1);
    URL.revokeObjectURL(url);
    if (ok) return true;
  }
  if (manifest[key]) {
    const ok = await playUrl(manifest[key], slow ? 0.7 : 1);
    if (ok) return true;
  }
  return tts(clean, slow);
}

/* ---------- rich text ---------- */
const ROLE_INFO = {
  marker: ['Marker', 'Article or marker before a noun: ang, si, sa, ni, ng, mga'],
  noun: ['Noun', 'A person, place or thing'],
  pred: ['Predicate', 'What is said about the subject: an action or description'],
  pron: ['Pronoun', 'I, you, he, we, this, that'],
  link: ['Linker', 'Ligature joining two words: -ng, -g, na'],
  ay: ['Ay', 'Joins a subject to its predicate when the subject comes first'],
  poss: ['Owner word', 'My, your, his, whose it is'],
  part: ['Polite word', 'Shows respect or answers: pô, hô, opô, oo'],
  other: ['Other', 'Everything else: at (and), expressions'],
};
function roleOf(r) { return ROLE_INFO[r] ? r : 'other'; }
function wordSpan(text, role, extra) {
  const r = roleOf(role);
  return h('span', {
    class: 'w ' + r + (extra ? ' ' + extra : ''), role: 'button', tabindex: '0',
    onclick: () => say(text.replace(/^-+/, '')),
  }, text);
}
function rich(s) {
  const frag = document.createDocumentFragment();
  const re = /\*\*(.+?)\*\*|\[\[([^\]|]+)(?:\|([a-z]+))?\]\]|\*([^*\s][^*]*?)\*/g;
  let last = 0, m;
  s = String(s);
  while ((m = re.exec(s))) {
    if (m.index > last) frag.append(s.slice(last, m.index));
    if (m[1] !== undefined) frag.append(h('b', {}, m[1]));
    else if (m[4] !== undefined) frag.append(h('i', {}, m[4]));
    else frag.append(wordSpan(m[2], m[3] || 'other'));
    last = re.lastIndex;
  }
  if (last < s.length) frag.append(s.slice(last));
  return frag;
}
const speakBtn = (text, cls) => h('button', { class: 'spk ' + (cls || ''), 'aria-label': 'Hear ' + text, onclick: (e) => { e.stopPropagation(); say(text); } }, '\u{1F50A}');

/* ---------- lesson blocks ---------- */
const BOX_ICON = { rule: '\u{1F4D0}', tip: '\u{1F4A1}', warn: '⚠️', remember: '\u{1F4CC}', culture: '\u{1F30F}', english: '\u{1F1EC}\u{1F1E7}' };

function renderBlock(b, L) {
  switch (b.type) {
    case 'p': return h('p', { class: 'para' }, rich(b.t));
    case 'h': return h('h3', { class: 'sub' }, rich(b.t));
    case 'box': {
      return h('div', { class: 'box ' + b.kind },
        h('div', { class: 'box-t' }, h('span', { class: 'ic' }, BOX_ICON[b.kind] || ''), b.title),
        b.items ? h('ul', {}, b.items.map((i) => h('li', {}, rich(i)))) : null,
        b.t ? h('p', {}, rich(b.t)) : null);
    }
    case 'pattern': {
      return h('div', { class: 'pattern' },
        b.title ? h('div', { class: 'pt' }, b.title) : null,
        b.rows.map((r) => h('div', { class: 'prow' },
          h('span', { class: 'plab' }, r.label),
          h('span', { class: 'chips' }, r.chips.map((c) => wordSpan(c.t, c.r, 'chip'))))),
        b.note ? h('div', { class: 'pnote' }, rich(b.note)) : null);
    }
    case 'table': {
      return h('div', { class: 'tblbox' },
        b.title ? h('div', { class: 'pt' }, b.title) : null,
        h('div', { class: 'tablewrap' }, h('table', {},
          h('thead', {}, h('tr', {}, b.head.map((x) => h('th', {}, x)))),
          h('tbody', {}, b.rows.map((r) => h('tr', {}, r.map((c) => h('td', {}, rich(c)))))))),
        b.note ? h('div', { class: 'pnote' }, rich(b.note)) : null);
    }
    case 'examples': {
      return h('div', { class: 'exs' },
        b.title ? h('div', { class: 'pt' }, b.title) : null,
        b.items.map((it) => h('div', { class: 'ex' },
          h('div', { class: 'ex-top' },
            it.parts && it.parts.length
              ? h('div', { class: 'ex-parts' }, it.parts.map((p) => h('span', { class: 'part' },
                wordSpan(p[0], p[2]), h('small', {}, p[1]))))
              : h('div', { class: 'ex-tl', onclick: () => say(it.tl) }, it.tl),
            speakBtn(it.tl)),
          h('div', { class: 'ex-en' }, it.en))));
    }
    case 'vocab': {
      const list = L ? L.vocab.filter((v) => v.group === b.group) : [];
      return h('div', { class: 'vlist' },
        b.title ? h('div', { class: 'pt' }, b.title) : null,
        list.map((v) => vocabRow(v)));
    }
    case 'legend': return legendBlock();
    default: return null;
  }
}
function vocabRow(v) {
  return h('div', { class: 'vrow', onclick: () => openWord(v.key) },
    h('div', { class: 'vmain' },
      h('b', {}, v.tl),
      db.settings.sound && v.say ? h('span', { class: 'vsay' }, v.say) : null),
    h('div', { class: 'ven' }, v.en),
    speakBtn(v.tl));
}
function legendBlock() {
  return h('div', { class: 'legend' }, Object.entries(ROLE_INFO).map(([r, [n, d]]) =>
    h('div', { class: 'lg' }, h('span', { class: 'w chip ' + r }, n), h('span', { class: 'lgd' }, d))));
}

/* ---------- word sheet ---------- */
function openWord(key) {
  const v = words.get(key);
  if (!v) return;
  closeSheet();
  history.pushState({ sheet: 1 }, '');
  const card = db.cards[key];
  const L = lessons.get(v.lesson);
  const sheet = h('div', { class: 'sheet-bg', id: 'sheet', onclick: (e) => { if (e.target.id === 'sheet') history.back(); } },
    h('div', { class: 'sheet' },
      h('div', { class: 'grab' }),
      h('img', { class: 'sheet-logo', src: 'icon-192.png', alt: '', width: 36, height: 36 }),
      h('div', { class: 'sw-tl' }, v.tl),
      db.settings.sound && v.say ? h('div', { class: 'sw-say' }, 'Say it: ' + v.say) : null,
      h('div', { class: 'sw-en' }, v.en),
      h('div', { class: 'sw-meta' }, h('span', { class: 'tag' }, v.pos), h('span', { class: 'tag' }, lname(L))),
      v.note ? h('div', { class: 'box tip' }, h('p', {}, rich(v.note))) : null,
      h('div', { class: 'row' },
        h('button', { class: 'btn', onclick: () => say(v.tl) }, '\u{1F50A} Hear it'),
        h('button', { class: 'btn ghost', onclick: () => say(v.tl, true) }, '\u{1F40C} Slowly')),
      h('div', { class: 'sw-st' }, card ? 'In your review deck. Next review ' + (card.due <= day() ? 'today' : 'in ' + (card.due - day()) + ' day(s)') + '.' : 'Not learned yet. Learn it in the Words step of ' + lname(L) + '.'),
      h('button', { class: 'btn ghost block', onclick: () => history.back() }, 'Close')));
  document.body.append(sheet);
}
function closeSheet() { const s = document.getElementById('sheet'); if (s) s.remove(); }
