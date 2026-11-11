'use strict';
/* Tagalify views. Needs core.js loaded first. */

let tab = 'home';
let stack = [];
let wordsMode = 'dict';
let query = '';
const root = document.getElementById('view');
const add = (...kids) => root.append(...kids.flat(Infinity).filter((k) => k != null && k !== false));

/* ---------- navigation ---------- */
function push(v) { stack.push(v); history.pushState({ n: stack.length }, ''); render(); }
function replace(v) { stack[stack.length - 1] = v; render(); }
function back() { if (stack.length) history.back(); }
window.addEventListener('popstate', () => {
  if (document.getElementById('sheet')) { closeSheet(); return; }
  if (stack.length) { stack.pop(); render(); }
});

function setTab(t) { tab = t; stack = []; render(); }

function applySettings() {
  const s = db.settings;
  const dark = s.theme === 'dark' || (s.theme === 'auto' && matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  document.documentElement.style.fontSize = (s.size * 100) + '%';
}

function render(keepScroll) {
  const y = window.scrollY;
  root.replaceChildren();
  const top = stack[stack.length - 1];
  document.body.classList.toggle('full', !!top);
  document.querySelectorAll('#nav button').forEach((b) => b.classList.toggle('active', b.dataset.tab === tab));
  if (top) VIEWS[top.name](top); else TABS[tab]();
  window.scrollTo(0, keepScroll ? y : 0);
}

/* ---------- small components ---------- */
function ring(p, size, text) {
  const r = 18, c = 2 * Math.PI * r, d = Math.max(0, Math.min(1, p));
  const s = h('span', { class: 'ring', style: `width:${size || 46}px;height:${size || 46}px` });
  s.innerHTML = `<svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="${r}" class="rb"/><circle cx="22" cy="22" r="${r}" class="rf" stroke-dasharray="${(c * d).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 22 22)"/></svg>`;
  s.append(h('i', {}, text != null ? text : Math.round(d * 100) + '%'));
  return s;
}
const bar = (p, cls) => h('div', { class: 'meter ' + (cls || '') }, h('i', { style: 'width:' + Math.round(Math.max(0, Math.min(1, p)) * 100) + '%' }));
const stat = (label, value) => h('div', { class: 'stat' }, h('b', {}, String(value)), h('span', {}, label));
const starsEl = (n) => h('span', { class: 'stars', 'aria-label': n + ' of 3 stars' }, [0, 1, 2].map((i) => h('span', { class: i < n ? 'on' : '' }, '★')));
function topbar(title, sub, extra) {
  return h('div', { class: 'topbar' },
    h('button', { class: 'back', 'aria-label': 'Back', onclick: back }, '‹'),
    h('div', { class: 'tt' }, h('b', {}, title), sub ? h('small', {}, sub) : null),
    extra || null);
}
const pct = (x) => Math.round(x * 100) + '%';

/* ---------- HOME ---------- */
function currentLesson() {
  return orderedLessons().find((L) => lessonStats(L.id).pct < 0.999) || null;
}
function nextStep(L) {
  const st = lessonStats(L.id), s = lstate(L.id);
  if (st.read < 1) return { t: s.read.length ? 'Keep reading' : 'Start reading', go: () => push({ name: 'reader', id: L.id, i: Math.min(s.pos || 0, L.sections.length - 1) }) };
  if (st.learned < 1) return { t: 'Learn the words', go: () => push({ name: 'learn', id: L.id }) };
  if (st.practice < 1) return { t: 'Practise', go: () => push({ name: 'practice', id: L.id }) };
  return { t: 'Open lesson', go: () => push({ name: 'hub', id: L.id }) };
}
function viewHome() {
  const cur = currentLesson();
  const due = dueKeys().length;
  const ov = overall();
  add(
    h('section', { class: 'hero' },
      h('img', { class: 'hero-logo', src: 'logo.png', alt: 'Tagalify logo', width: 84, height: 84 }),
      h('div', {},
        h('h1', {}, h('span', { class: 'b1' }, 'Tagal'), h('span', { class: 'b2' }, 'ify')),
        h('p', {}, 'Learn Tagalog step by step, from the very first rule to real conversation.'))),
    cur ? (() => {
      const st = lessonStats(cur.id), ns = nextStep(cur);
      return h('div', { class: 'card cont' },
        h('div', { class: 'cont-top' }, ring(st.pct, 56),
          h('div', {}, h('small', {}, 'Continue'), h('b', {}, (cur.label === 'Intro' || isNaN(+cur.label) ? '' : 'Lesson ' + cur.label + ': ') + cur.title))),
        bar(st.pct),
        h('button', { class: 'btn block', onclick: ns.go }, ns.t + ' ›'));
    })() : h('div', { class: 'card' }, h('b', {}, 'You have finished every lesson so far.'), h('p', {}, 'Keep your reviews going. New lessons can be added any time.')),
    due ? h('div', { class: 'card due' }, h('div', {}, h('b', {}, due + (due === 1 ? ' word' : ' words') + ' to review'), h('small', {}, 'A few minutes now keeps them in your memory')),
      h('button', { class: 'btn', onclick: () => push({ name: 'review' }) }, 'Review')) : null,
    h('div', { class: 'card' },
      h('div', { class: 'row between' }, h('b', {}, 'Course progress'), h('b', {}, pct(ov))),
      bar(ov, 'big'),
      h('div', { class: 'stats' },
        stat('day streak', streak()),
        stat('words learned', Object.keys(db.cards).filter((k) => words.has(k)).length),
        stat('lessons done', orderedLessons().filter((L) => lessonStats(L.id).pct >= 0.999).length))),
    h('div', { class: 'card hint' }, h('b', {}, 'Tip'), h('p', {}, 'Coloured words are tappable. Tap any one to hear it.')));
}

/* ---------- COURSE ---------- */
function viewCourse() {
  add(h('h2', { class: 'pagetitle' }, 'Course'));
  course.units.forEach((u) => {
    add(h('h3', { class: 'unit' }, u.title));
    u.lessons.forEach((id) => {
      const L = lessons.get(id);
      if (!L) return;
      const st = lessonStats(id);
      const numeric = !isNaN(+L.label);
      add(h('button', { class: 'lrow', onclick: () => push({ name: 'hub', id }) },
        ring(st.pct, 48, numeric ? L.label : '★'),
        h('span', { class: 'lr-t' }, h('b', {}, L.title), h('small', {}, L.summary),
          h('small', { class: 'lr-m' }, L.minutes + ' min · ' + L.vocab.length + ' words')),
        starsEl(st.stars)));
    });
  });
  add(h('p', { class: 'foot' }, 'More lessons will be added here. Your progress is kept.'));
}

/* ---------- LESSON HUB ---------- */
function viewHub(v) {
  const L = lessons.get(v.id), st = lessonStats(v.id), s = lstate(v.id);
  const numeric = !isNaN(+L.label);
  const step = (n, title, sub, p, go, label) => h('button', { class: 'step', onclick: go },
    h('span', { class: 'sn' }, n), h('span', { class: 'st' }, h('b', {}, title), h('small', {}, sub), bar(p)),
    h('span', { class: 'go' }, label));
  add(topbar(numeric ? 'Lesson ' + L.label : L.title, numeric ? L.title : L.summary),
    h('div', { class: 'card' },
      h('div', { class: 'row between' }, h('span', {}, L.minutes + ' min · ' + L.vocab.length + ' words'), starsEl(st.stars)),
      h('div', { class: 'row between' }, h('b', {}, 'Lesson progress'), h('b', {}, pct(st.pct))),
      bar(st.pct, 'big')),
    h('h3', { class: 'unit' }, 'By the end you can'),
    h('ul', { class: 'goals' }, L.goals.map((g) => h('li', {}, g))),
    h('h3', { class: 'unit' }, 'Your three steps'),
    step(1, 'Read the lesson', st.readN + ' of ' + L.sections.length + ' pages read', st.read,
      () => push({ name: 'reader', id: L.id, i: st.read >= 1 ? 0 : Math.min(s.pos || 0, L.sections.length - 1) }), st.read >= 1 ? 'Again' : st.readN ? 'Continue' : 'Start'),
    step(2, 'Learn the words', st.learnedN + ' of ' + st.total + ' words learned', st.learned,
      () => push({ name: 'learn', id: L.id }), st.learned >= 1 ? 'Done' : 'Learn'),
    step(3, 'Practise', s.best ? 'Best score ' + s.best + '%' : 'Exercises with instant feedback', st.practice,
      () => push({ name: 'practice', id: L.id }), s.best ? 'Again' : 'Start'),
    h('h3', { class: 'unit' }, 'Words in this lesson'),
    h('div', { class: 'vlist' }, L.vocab.map((w) => vocabRow(w))),
    h('h3', { class: 'unit' }, 'Quick recap'),
    h('div', { class: 'box remember' }, h('ul', {}, L.recap.map((r) => h('li', {}, r)))));
}

/* ---------- READER ---------- */
function viewReader(v) {
  const L = lessons.get(v.id), s = lstate(v.id), sec = L.sections[v.i];
  const n = L.sections.length;
  if (!s.read.includes(v.i)) s.read.push(v.i);
  s.pos = v.i;
  save();
  const last = v.i === n - 1;
  add(topbar(L.title, 'Page ' + (v.i + 1) + ' of ' + n),
    bar((v.i + 1) / n, 'thin'),
    h('article', { class: 'page' },
      h('h2', {}, sec.title),
      sec.blocks.map((b) => renderBlock(b, L)),
      last ? h('div', { class: 'box remember' }, h('div', { class: 'box-t' }, h('span', { class: 'ic' }, '\u{1F3AF}'), 'Lesson recap'), h('ul', {}, L.recap.map((r) => h('li', {}, r)))) : null),
    h('div', { class: 'pager' },
      h('button', { class: 'btn ghost', disabled: v.i === 0, onclick: () => { v.i--; render(); } }, '‹ Previous'),
      last ? h('button', { class: 'btn', onclick: back }, 'Finish reading')
        : h('button', { class: 'btn', onclick: () => { v.i++; render(); } }, 'Next ›')));
}

/* ---------- LEARN WORDS ---------- */
function viewLearn(v) {
  const L = lessons.get(v.id);
  if (!v.list) {
    v.list = L.vocab.filter((w) => !db.cards[w.key]).slice(0, db.settings.newPerDay);
    v.i = 0;
  }
  if (!v.list.length) {
    add(topbar('Learn words', L.title),
      h('div', { class: 'card center' }, h('div', { class: 'big' }, '\u{1F389}'), h('b', {}, 'You have learned every word in this lesson.'),
        h('button', { class: 'btn block', onclick: back }, 'Back to lesson')));
    return;
  }
  if (v.i >= v.list.length) {
    const left = L.vocab.filter((w) => !db.cards[w.key]).length;
    add(topbar('Learn words', L.title),
      h('div', { class: 'card center' }, h('div', { class: 'big' }, '✅'), h('b', {}, v.list.length + ' new words added to your reviews'),
        left ? h('p', {}, left + ' more words are waiting in this lesson.') : h('p', {}, 'That is every word in this lesson.'),
        left ? h('button', { class: 'btn block', onclick: () => { v.list = null; render(); } }, 'Learn ' + Math.min(left, db.settings.newPerDay) + ' more') : null,
        h('button', { class: 'btn ' + (left ? 'ghost' : '') + ' block', onclick: back }, 'Back to lesson')));
    return;
  }
  const w = v.list[v.i];
  add(topbar('Learn words', L.title + ' · ' + (v.i + 1) + '/' + v.list.length), bar(v.i / v.list.length, 'thin'),
    h('div', { class: 'wordcard' },
      h('div', { class: 'wc-tl' }, w.tl),
      db.settings.sound && w.say ? h('div', { class: 'wc-say' }, w.say) : null,
      h('div', { class: 'wc-en' }, w.en),
      h('span', { class: 'tag' }, w.pos),
      w.note ? h('div', { class: 'box tip' }, h('p', {}, rich(w.note))) : null,
      h('div', { class: 'row center' },
        h('button', { class: 'btn', onclick: () => say(w.tl) }, '\u{1F50A} Hear it'),
        h('button', { class: 'btn ghost', onclick: () => say(w.tl, true) }, '\u{1F40C} Slowly'))),
    h('div', { class: 'pager' },
      h('button', { class: 'btn ghost', disabled: v.i === 0, onclick: () => { v.i--; render(); } }, '‹ Back'),
      h('button', { class: 'btn', onclick: () => {
        if (!db.cards[w.key]) { db.cards[w.key] = newCard(); logToday().new++; }
        logToday().act++;
        save(); v.i++; render();
      } }, 'Got it ›')));
  setTimeout(() => { if (stack[stack.length - 1] === v && v.list[v.i] === w) say(w.tl); }, 250);
}

/* ---------- PRACTICE ---------- */
function startPractice(L) {
  const items = shuffle(L.exercises.map((e, idx) => ({ e, idx, first: null, again: false })));
  return { queue: items, total: items.length, i: 0, ok: 0, finished: false };
}
function viewPractice(v) {
  const L = lessons.get(v.id);
  if (!v.p) v.p = startPractice(L);
  const p = v.p;
  if (p.i >= p.queue.length) { practiceDone(v, L); return; }
  const it = p.queue[p.i];
  const finish = (correct) => {
    if (it.first === null) { it.first = correct; if (correct) p.ok++; }
    if (!correct && !it.again) { it.again = true; p.queue.push({ ...it, first: it.first, again: true }); }
  };
  const next = () => { p.i++; render(); };
  const body = h('div', { class: 'ex-area' });
  add(topbar('Practise', L.title + ' · ' + Math.min(p.i + 1, p.queue.length) + '/' + p.queue.length), bar(p.i / p.queue.length, 'thin'), body);
  EX[it.e.type](body, it.e, finish, next);
}
function feedback(body, ok, explain, next, label) {
  body.append(h('div', { class: 'fb ' + (ok ? 'good' : 'bad') },
    h('b', {}, ok ? 'Correct!' : 'Not quite.'), explain ? h('p', {}, rich(explain)) : null),
  h('button', { class: 'btn block', onclick: next }, label || 'Continue ›'));
}
const EX = {
  choice(body, e, finish, next) {
    body.append(h('div', { class: 'q' }, e.q, e.tl ? speakBtn(e.tl) : null));
    const opts = h('div', { class: 'opts' });
    body.append(opts);
    let done = false;
    shuffle(e.options).forEach((o) => {
      const b = h('button', { class: 'opt', onclick: () => {
        if (done) return; done = true;
        const ok = o === e.answer;
        finish(ok);
        b.classList.add(ok ? 'right' : 'wrong');
        if (!ok) [...opts.children].forEach((x) => { if (x.textContent === e.answer) x.classList.add('right'); });
        [...opts.children].forEach((x) => { x.disabled = true; });
        feedback(body, ok, e.explain, next);
      } }, o);
      opts.append(b);
    });
  },
  listen(body, e, finish, next) {
    body.append(h('div', { class: 'q' }, 'Listen, then choose the meaning.'),
      h('div', { class: 'row center' },
        h('button', { class: 'btn big', onclick: () => say(e.tl) }, '\u{1F50A} Play'),
        h('button', { class: 'btn ghost', onclick: () => say(e.tl, true) }, '\u{1F40C} Slowly')));
    const opts = h('div', { class: 'opts' });
    body.append(opts);
    let done = false;
    shuffle(e.options).forEach((o) => {
      const b = h('button', { class: 'opt', onclick: () => {
        if (done) return; done = true;
        const ok = o === e.answer;
        finish(ok);
        b.classList.add(ok ? 'right' : 'wrong');
        if (!ok) [...opts.children].forEach((x) => { if (x.textContent === e.answer) x.classList.add('right'); });
        [...opts.children].forEach((x) => { x.disabled = true; });
        feedback(body, ok, (e.explain ? e.explain + ' ' : '') + 'You heard: ' + e.tl, next);
      } }, o);
      opts.append(b);
    });
    setTimeout(() => say(e.tl), 300);
  },
  build(body, e, finish, next) {
    body.append(h('div', { class: 'q' }, 'Build this in Tagalog:', h('div', { class: 'qen' }, e.en)));
    const tiles = shuffle(e.tokens.concat(e.extra || []).map((t, i) => ({ t, id: i })));
    const placed = [];
    const ans = h('div', { class: 'answer' });
    const pool = h('div', { class: 'pool' });
    const check = h('button', { class: 'btn block', disabled: true }, 'Check');
    let locked = false;
    const draw = () => {
      ans.replaceChildren(...(placed.length ? placed.map((x) => h('button', { class: 'tile', onclick: () => { if (locked) return; placed.splice(placed.indexOf(x), 1); draw(); } }, x.t))
        : [h('span', { class: 'ph' }, 'Tap the words in order')]));
      pool.replaceChildren(...tiles.map((x) => h('button', { class: 'tile', disabled: placed.includes(x) || locked, onclick: () => { placed.push(x); draw(); } }, x.t)));
      check.disabled = !placed.length || locked;
    };
    check.onclick = () => {
      locked = true; draw();
      const ok = placed.map((x) => x.t).join(' ') === e.tokens.join(' ');
      finish(ok);
      ans.classList.add(ok ? 'right' : 'wrong');
      check.remove();
      feedback(body, ok, (ok ? '' : 'Correct answer: ') + '**' + e.tl + '** ' + (e.explain || ''), next);
      say(e.tl);
    };
    body.append(ans, pool, check);
    draw();
  },
  match(body, e, finish, next) {
    body.append(h('div', { class: 'q' }, e.q));
    const L = e.pairs.map((p, i) => ({ t: p[0], i }));
    const R = shuffle(e.pairs.map((p, i) => ({ t: p[1], i })));
    let selL = null, mistakes = 0, left = e.pairs.length;
    const colL = h('div', { class: 'mcol' }), colR = h('div', { class: 'mcol' });
    const bl = L.map((x) => h('button', { class: 'opt m', onclick: () => {
      if (x.done) return; selL = x; bl.forEach((b, k) => b.classList.toggle('sel', L[k] === x));
    } }, x.t));
    const br = R.map((x) => h('button', { class: 'opt m', onclick: (ev) => {
      if (!selL || x.done) return;
      const btn = ev.currentTarget;
      if (selL.i === x.i) {
        x.done = true; selL.done = true;
        btn.classList.add('right'); bl[L.indexOf(selL)].classList.remove('sel'); bl[L.indexOf(selL)].classList.add('right');
        btn.disabled = true; bl[L.indexOf(selL)].disabled = true;
        selL = null; left--;
        if (!left) { finish(mistakes === 0); feedback(body, mistakes === 0, mistakes ? 'You made ' + mistakes + ' mistake' + (mistakes > 1 ? 's' : '') + ' on the way.' : 'All matched on the first go.', next); }
      } else {
        mistakes++; btn.classList.add('wrong'); setTimeout(() => btn.classList.remove('wrong'), 450);
      }
    } }, x.t));
    bl.forEach((b) => colL.append(b)); br.forEach((b) => colR.append(b));
    body.append(h('div', { class: 'mgrid' }, colL, colR));
  },
};
function practiceDone(v, L) {
  const p = v.p, s = lstate(v.id);
  const score = Math.round(p.ok / p.total * 100);
  if (!p.saved) {
    p.saved = true;
    s.best = Math.max(s.best || 0, score);
    logToday().act++;
    save();
  }
  const stars = score >= 90 ? 3 : score >= 70 ? 2 : 1;
  add(topbar('Practice complete', L.title),
    h('div', { class: 'card center' },
      starsEl(stars), h('div', { class: 'score' }, score + '%'),
      h('p', {}, p.ok + ' of ' + p.total + ' right on the first try.'),
      h('p', {}, score >= 90 ? 'Excellent. You know this lesson well.' : score >= 70 ? 'Good work. Reading the pages again will lift it further.' : 'Keep going. Read the lesson again, then try once more.'),
      h('button', { class: 'btn block', onclick: () => { v.p = null; render(); } }, 'Try again'),
      h('button', { class: 'btn ghost block', onclick: back }, 'Back to lesson')));
}

/* ---------- REVIEW ---------- */
function viewReview(v) {
  if (!v.list) { v.list = shuffle(dueKeys()).slice(0, 30); v.i = 0; v.total = v.list.length; v.show = false; v.dir = {}; v.n = 0; }
  if (v.i >= v.list.length) {
    add(topbar('Review', ''), h('div', { class: 'card center' }, h('div', { class: 'big' }, v.total ? '\u{1F31F}' : '✅'),
      h('b', {}, v.total ? 'Review done' : 'Nothing to review right now'),
      h('p', {}, v.total ? v.n + ' answers today. See you tomorrow.' : 'Learn some words in a lesson and they will show up here.'),
      h('button', { class: 'btn block', onclick: back }, 'Done')));
    return;
  }
  const key = v.list[v.i], w = words.get(key), c = db.cards[key];
  let d = db.settings.direction;
  if (d === 'mixed') d = v.dir[key] || (v.dir[key] = Math.random() < 0.5 ? 'te' : 'et');
  const front = d === 'te' ? w.tl : w.en;
  add(topbar('Review', (v.i + 1) + ' of ' + v.list.length), bar(v.i / v.list.length, 'thin'),
    h('div', { class: 'wordcard' },
      h('small', { class: 'cap' }, d === 'te' ? 'What does this mean?' : 'How do you say this in Tagalog?'),
      h('div', { class: d === 'te' ? 'wc-tl' : 'wc-en big' }, front),
      d === 'te' ? h('button', { class: 'btn ghost', onclick: () => say(w.tl) }, '\u{1F50A} Hear it') : null,
      v.show ? h('div', { class: 'reveal' },
        d === 'te' ? h('div', { class: 'wc-en' }, w.en) : h('div', { class: 'wc-tl' }, w.tl),
        db.settings.sound && w.say ? h('div', { class: 'wc-say' }, w.say) : null,
        w.note ? h('div', { class: 'box tip' }, h('p', {}, rich(w.note))) : null) : null),
    v.show ? h('div', { class: 'rates' }, [['Again', 0], ['Hard', 1], ['Good', 2], ['Easy', 3]].map(([lab, q]) =>
      h('button', { class: 'rate r' + q, onclick: () => {
        rate(c, q); logToday().reviews++; logToday().act++; v.n++;
        if (q === 0) v.list.push(key);
        v.i++; v.show = false; save(); render();
      } }, h('b', {}, lab), h('small', {}, previewInt(c, q)))))
      : h('div', { class: 'pager' }, h('button', { class: 'btn block', onclick: () => { v.show = true; render(); if (d === 'et') say(w.tl); } }, 'Show answer')));
  if (d === 'te') setTimeout(() => { if (stack[stack.length - 1] === v && v.list[v.i] === key && !v.show) say(w.tl); }, 250);
}

/* ---------- WORDS ---------- */
function dictRows(list) {
  const q = query.trim().toLowerCase();
  list.replaceChildren();
  let n = 0;
  orderedLessons().forEach((L) => {
    const ws = L.vocab.filter((w) => !q || fold(w.tl).includes(fold(q)) || w.en.toLowerCase().includes(q));
    if (!ws.length) return;
    n += ws.length;
    list.append(h('h3', { class: 'unit' }, (isNaN(+L.label) ? '' : 'Lesson ' + L.label + ': ') + L.title));
    ws.forEach((w) => list.append(h('div', { class: 'vrow', onclick: () => openWord(w.key) },
      h('span', { class: 'dot' + (db.cards[w.key] ? ' on' : ''), title: db.cards[w.key] ? 'Learned' : 'Not learned yet' }),
      h('div', { class: 'vmain' }, h('b', {}, w.tl), db.settings.sound && w.say ? h('span', { class: 'vsay' }, w.say) : null),
      h('div', { class: 'ven' }, w.en), speakBtn(w.tl))));
  });
  if (!n) list.append(h('p', { class: 'foot' }, 'No words match.'));
}
/* ---------- BOOK VOCABULARY LISTS (pages 208-218) ---------- */
let gloss = null, glossDir = 'tl', glossLetter = 'A', glossQ = '';
async function loadGloss() {
  if (gloss) return gloss;
  try { gloss = await (await fetch('data/glossary.json', { cache: 'no-cache' })).json(); } catch (e) { gloss = null; }
  return gloss;
}
let appIndex = null;
function appWordFor(w) {
  if (!appIndex) { appIndex = new Map(); words.forEach((v) => { const k = fold(v.tl); const cur = appIndex.get(k); if (!cur || (words.get(cur).lesson === 'a07' && v.lesson !== 'a07')) appIndex.set(k, v.key); }); }
  return appIndex.get(fold(w));
}
function viewBookList() {
  const box = h('div', {});
  add(h('p', { class: 'foot' }, 'The Vocabulary Lists at the back of the book (pages 208 to 218), exactly as printed. Accent marks appear only where the book prints them. A green dot means the word is also taught in a lesson: tap the row to open it.'),
    h('div', { class: 'seg small' },
      h('button', { class: glossDir === 'tl' ? 'on' : '', onclick: () => { glossDir = 'tl'; glossLetter = 'A'; render(); } }, 'Tagalog → English'),
      h('button', { class: glossDir === 'en' ? 'on' : '', onclick: () => { glossDir = 'en'; glossLetter = 'A'; render(); } }, 'English → Tagalog')),
    gloss && gloss.abbrev ? h('details', { class: 'howto' }, h('summary', {}, 'Abbreviations used in the list'),
      h('div', {}, gloss.abbrev.map((a) => h('div', {}, h('b', {}, a.a), ' ' + a.m)))) : null,
    h('input', { type: 'search', class: 'search', placeholder: 'Search the book list', value: glossQ, 'aria-label': 'Search the book list',
      oninput: (e) => { glossQ = e.target.value; draw(); } }),
    box);
  const draw = () => {
    box.replaceChildren();
    if (!gloss) { box.append(h('p', { class: 'foot' }, 'Loading…')); return; }
    const list = gloss[glossDir] || [];
    const q = fold(glossQ.trim());
    let rows;
    if (q) rows = list.filter((e) => fold(e.w).includes(q) || fold(e.d).includes(q)).slice(0, 300);
    else {
      const letters = [...new Set(list.map((e) => (fold(e.w)[0] || '').toUpperCase()))].filter((c) => /[A-Z]/.test(c));
      if (!letters.includes(glossLetter)) glossLetter = letters[0];
      box.append(h('div', { class: 'letters' }, letters.map((c) => h('button', { class: c === glossLetter ? 'on' : '', onclick: () => { glossLetter = c; draw(); } }, c))));
      rows = list.filter((e) => (fold(e.w)[0] || '').toUpperCase() === glossLetter);
    }
    rows.forEach((e) => {
      const key = glossDir === 'tl' ? appWordFor(e.w) : null;
      const taught = key && words.get(key).lesson !== 'a07';
      box.append(h('div', { class: 'grow' + (key ? ' link' : ''), onclick: key ? () => openWord(key) : null },
        taught ? h('span', { class: 'dot on', title: 'Also taught in a lesson' }) : h('span', { class: 'dot' }),
        h('div', { class: 'gmain' }, h('b', {}, e.w), ' ', rich(e.d),
          e.note ? h('small', { class: 'gnote' }, ' (' + e.note + ')') : null),
        h('small', { class: 'gpg' }, 'p' + e.p),
        glossDir === 'tl' ? speakBtn(e.w) : null));
    });
    if (!rows.length) box.append(h('p', { class: 'foot' }, 'Nothing matches.'));
    else if (q && rows.length === 300) box.append(h('p', { class: 'foot' }, 'Showing the first 300 matches.'));
  };
  draw();
  if (!gloss) loadGloss().then(() => { if (box.isConnected) draw(); });
}
function viewWords() {
  add(h('h2', { class: 'pagetitle' }, 'Words'),
    h('div', { class: 'seg' },
      h('button', { class: wordsMode === 'dict' ? 'on' : '', onclick: () => { wordsMode = 'dict'; render(); } }, 'Dictionary'),
      h('button', { class: wordsMode === 'book' ? 'on' : '', onclick: () => { wordsMode = 'book'; render(); } }, 'Book list'),
      h('button', { class: wordsMode === 'cheat' ? 'on' : '', onclick: () => { wordsMode = 'cheat'; render(); } }, 'Cheat sheet')));
  if (wordsMode === 'book') { viewBookList(); return; }
  if (wordsMode === 'dict') {
    const list = h('div', {});
    const inp = h('input', { type: 'search', class: 'search', placeholder: 'Search Tagalog or English', value: query, 'aria-label': 'Search words',
      oninput: (e) => { query = e.target.value; dictRows(list); } });
    add(inp, list);
    dictRows(list);
  } else if (ref) {
    add(h('p', { class: 'para' }, ref.intro));
    ref.sections.forEach((s) => add(h('section', { class: 'refsec' }, h('h3', { class: 'unit' }, s.title), s.blocks.map((b) => renderBlock(b, null)))));
    add(h('h3', { class: 'unit' }, 'Colour key'), legendBlock());
  }
}

/* ---------- PROGRESS ---------- */
function viewProgress() {
  const ov = overall();
  const learned = Object.keys(db.cards).filter((k) => words.has(k)).length;
  const reviews = Object.values(db.log).reduce((a, d) => a + (d.reviews || 0), 0);
  add(h('h2', { class: 'pagetitle' }, 'Progress'),
    h('div', { class: 'card center' }, ring(ov, 110), h('b', {}, 'of the course complete'),
      h('small', {}, orderedLessons().filter((L) => lessonStats(L.id).pct >= 0.999).length + ' of ' + orderedLessons().length + ' lessons finished')),
    h('div', { class: 'card' }, h('div', { class: 'stats four' },
      stat('day streak', streak()), stat('words learned', learned + '/' + words.size), stat('reviews done', reviews), stat('due now', dueKeys().length))),
    h('h3', { class: 'unit' }, 'Lesson by lesson'));
  orderedLessons().forEach((L) => {
    const st = lessonStats(L.id);
    add(h('button', { class: 'card prog', onclick: () => push({ name: 'hub', id: L.id }) },
      h('div', { class: 'row between' }, h('b', {}, (isNaN(+L.label) ? '' : L.label + '. ') + L.title), starsEl(st.stars)),
      h('div', { class: 'pbars' },
        h('div', {}, h('small', {}, 'Read ' + pct(st.read)), bar(st.read, 'read')),
        h('div', {}, h('small', {}, 'Words ' + st.learnedN + '/' + st.total), bar(st.learned, 'words')),
        h('div', {}, h('small', {}, 'Practice ' + (lstate(L.id).best || 0) + '%'), bar(st.practice, 'prac')))));
  });
  add(h('p', { class: 'foot' }, 'Lesson score = 40% reading, 30% words learned, 30% practice. Reach 70% in practice to fill that bar. Stars: 70% = 2, 90% = 3.'));
}

/* ---------- MORE / SETTINGS ---------- */
function opt(label, sel, options, onchange) {
  return h('label', { class: 'setrow' }, h('span', {}, label),
    h('select', { onchange: (e) => onchange(e.target.value) }, options.map(([v, t]) => h('option', { value: v, selected: String(v) === String(sel) }, t))));
}
function viewMore() {
  const s = db.settings;
  add(h('h2', { class: 'pagetitle' }, 'More'),
    h('div', { class: 'card' },
      opt('New words per session', s.newPerDay, [[5, '5'], [10, '10'], [15, '15'], [20, '20']], (v) => { s.newPerDay = +v; save(); }),
      opt('Review direction', s.direction, [['mixed', 'Mixed'], ['te', 'Tagalog to English'], ['et', 'English to Tagalog']], (v) => { s.direction = v; save(); }),
      opt('Theme', s.theme, [['auto', 'Match phone'], ['light', 'Light'], ['dark', 'Dark']], (v) => { s.theme = v; save(); applySettings(); }),
      opt('Text size', s.size, [[0.9, 'Small'], [1, 'Normal'], [1.15, 'Large'], [1.3, 'Extra large']], (v) => { s.size = +v; save(); applySettings(); }),
      h('label', { class: 'setrow' }, h('span', {}, 'Show sound guide (ka-PE)'),
        h('input', { type: 'checkbox', checked: s.sound, onchange: (e) => { s.sound = e.target.checked; save(); } }))),
    syncCard(),
    voiceCard(),
    h('div', { class: 'card' },
      h('b', {}, '\u{1F399} Recording studio'),
      h('p', {}, 'Record a native speaker saying each word and sentence. Tagalify plays your recordings first, so the app speaks with a real voice.'),
      h('p', { class: 'fine' }, dbxConnected() ? 'Recordings are backed up to Dropbox automatically.' : 'Recordings are kept on this phone. Connect Dropbox above to back them up.'),
      h('button', { class: 'btn block', onclick: () => push({ name: 'studio' }) }, '\u{1F399} Open recording studio')),
    h('div', { class: 'card' },
      h('b', {}, 'Backup file'),
      h('p', {}, 'You can also save your progress as a file, or load one. Recordings are not included in this file.'),
      h('div', { class: 'row' },
        h('button', { class: 'btn ghost', onclick: exportBackup }, 'Back up'),
        h('label', { class: 'btn ghost filebtn' }, 'Restore', h('input', { type: 'file', accept: 'application/json', onchange: importBackup }))),
      h('button', { class: 'btn danger block', onclick: resetAll }, 'Reset all progress')),
    h('div', { class: 'card about' },
      h('div', { class: 'about-top' }, h('img', { src: 'logo.png', alt: '', width: 64, height: 64 }), h('div', {}, h('b', {}, 'Tagalify v' + APP_VERSION), h('small', {}, 'Your Tagalog study guide'))),
      h('p', {}, 'Lessons follow Paraluman S. Aspillera’s Basic Tagalog (Introduction, Lessons 1 to 44, the Appendices, the Vocabulary Lists and the Review Exercises, to page 229). Tagalog words, accent marks and meanings match the textbook.'),
      h('p', {}, 'Works offline once opened.')));
}
function download(name, blob) {
  const a = h('a', { href: URL.createObjectURL(blob), download: name });
  document.body.append(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
function exportBackup() {
  download('tagalify-backup.json', new Blob([JSON.stringify(db)], { type: 'application/json' }));
}
function importBackup(e) {
  const f = e.target.files[0];
  if (!f) return;
  f.text().then((t) => {
    const d = JSON.parse(t);
    if (!d || typeof d !== 'object' || !d.cards) throw new Error('bad');
    localStorage.setItem(KEY, JSON.stringify(d));
    db = loadDb(); save(); applySettings(); render(); toast('Progress restored');
  }).catch(() => toast('That file is not a Tagalify backup'));
}
function resetAll() {
  if (!confirm('Erase all your progress on this phone? Recordings are kept.')) return;
  localStorage.removeItem(KEY);
  db = loadDb(); applySettings(); render(); toast('Progress reset');
}

/* ---------- RECORDING STUDIO ---------- */
const CRC = (() => { const t = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
function crc32(b) { let c = 0xFFFFFFFF; for (let i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 255] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; }
function makeZip(files) {
  const enc = new TextEncoder(), parts = [], central = [];
  let off = 0;
  const now = new Date();
  const time = (now.getHours() << 11) | (now.getMinutes() << 5) | (now.getSeconds() >> 1);
  const date = ((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate();
  files.forEach((f) => {
    const name = enc.encode(f.name), crc = crc32(f.data), size = f.data.length;
    const lh = new DataView(new ArrayBuffer(30));
    lh.setUint32(0, 0x04034b50, true); lh.setUint16(4, 20, true); lh.setUint16(6, 0x0800, true); lh.setUint16(8, 0, true);
    lh.setUint16(10, time, true); lh.setUint16(12, date, true); lh.setUint32(14, crc, true); lh.setUint32(18, size, true); lh.setUint32(22, size, true);
    lh.setUint16(26, name.length, true); lh.setUint16(28, 0, true);
    parts.push(lh.buffer, name, f.data);
    const ch = new DataView(new ArrayBuffer(46));
    ch.setUint32(0, 0x02014b50, true); ch.setUint16(4, 20, true); ch.setUint16(6, 20, true); ch.setUint16(8, 0x0800, true); ch.setUint16(10, 0, true);
    ch.setUint16(12, time, true); ch.setUint16(14, date, true); ch.setUint32(16, crc, true); ch.setUint32(20, size, true); ch.setUint32(24, size, true);
    ch.setUint16(28, name.length, true); ch.setUint32(42, off, true);
    central.push(ch.buffer, name);
    off += 30 + name.length + size;
  });
  const csize = central.reduce((a, p) => a + (p.byteLength != null ? p.byteLength : p.length), 0);
  const end = new DataView(new ArrayBuffer(22));
  end.setUint32(0, 0x06054b50, true); end.setUint16(8, files.length, true); end.setUint16(10, files.length, true);
  end.setUint32(12, csize, true); end.setUint32(16, off, true);
  return new Blob([...parts, ...central, end.buffer], { type: 'application/zip' });
}
let recorder = null;
/* ---------- microphone choice (external mics such as RØDE Wireless PRO) ---------- */
function micGet(k, d) { try { const x = localStorage.getItem('tg.' + k); return x == null ? d : x; } catch (e) { return d; } }
function micSet(k, x) { try { localStorage.setItem('tg.' + k, x); } catch (e) {} }
function micConstraints(id) {
  const raw = micGet('micRaw', '0') === '1';
  const a = { echoCancellation: !raw, noiseSuppression: !raw, autoGainControl: !raw };
  if (id) a.deviceId = { exact: id };
  return { audio: a };
}
async function micStream() {
  const id = micGet('mic', '');
  try { return await navigator.mediaDevices.getUserMedia(micConstraints(id)); }
  catch (e) {
    if (id && (e.name === 'OverconstrainedError' || e.name === 'NotFoundError' || e.name === 'NotReadableError')) {
      toast('Chosen microphone not found, using the phone mic');
      return await navigator.mediaDevices.getUserMedia(micConstraints(''));
    }
    throw e;
  }
}
async function micList() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) return [];
  let ds = await navigator.mediaDevices.enumerateDevices();
  if (ds.some((d) => d.kind === 'audioinput' && !d.label)) {
    // labels only appear after permission: ask once, then list again
    try { const st = await navigator.mediaDevices.getUserMedia({ audio: true }); st.getTracks().forEach((t) => t.stop()); ds = await navigator.mediaDevices.enumerateDevices(); } catch (e) {}
  }
  return ds.filter((d) => d.kind === 'audioinput' && d.deviceId !== 'communications');
}
let micMeter = null;
function micMeterStop() { if (micMeter) { cancelAnimationFrame(micMeter.raf); micMeter.stream.getTracks().forEach((t) => t.stop()); try { micMeter.ctx.close(); } catch (e) {} micMeter = null; } }
async function micMeterStart(bar, label) {
  micMeterStop();
  let stream;
  try { stream = await micStream(); } catch (e) { toast('Microphone permission is needed'); return false; }
  const ctx = new (window.AudioContext || window.webkitAudioContext)();
  const an = ctx.createAnalyser(); an.fftSize = 1024;
  ctx.createMediaStreamSource(stream).connect(an);
  const buf = new Float32Array(an.fftSize);
  const tr = stream.getAudioTracks()[0];
  if (label) label.textContent = 'Listening on: ' + ((tr && tr.label) || 'microphone');
  micMeter = { stream, ctx, raf: 0 };
  const tick = () => {
    an.getFloatTimeDomainData(buf);
    let pk = 0; for (let i = 0; i < buf.length; i++) pk = Math.max(pk, Math.abs(buf[i]));
    bar.style.width = Math.min(100, Math.round(Math.sqrt(pk) * 100)) + '%';
    bar.className = 'lvl' + (pk > 0.9 ? ' hot' : pk > 0.02 ? ' ok' : '');
    if (!bar.isConnected) { micMeterStop(); return; }
    micMeter.raf = requestAnimationFrame(tick);
  };
  tick();
  return true;
}
function micCard() {
  const sel = h('select', { 'aria-label': 'Microphone', onchange: (e) => { micSet('mic', e.target.value); if (micMeter) testBtn.onclick(true); } },
    h('option', { value: '' }, 'Phone default'));
  const fill = async () => {
    const ms = await micList(), cur = micGet('mic', '');
    sel.replaceChildren(h('option', { value: '' }, 'Phone default'),
      ...ms.map((d, i) => h('option', { value: d.deviceId, selected: d.deviceId === cur }, d.label || 'Microphone ' + (i + 1))));
    if (cur && !ms.some((d) => d.deviceId === cur)) sel.value = '';
  };
  const bar = h('i', { class: 'lvl' }), who = h('small', { class: 'muted' }, 'Tap Test, then speak. The bar should move.');
  const testBtn = h('button', { class: 'btn ghost block' }, '🎙️ Test microphone');
  testBtn.onclick = async (restart) => {
    if (micMeter && restart !== true) { micMeterStop(); testBtn.textContent = '🎙️ Test microphone'; bar.style.width = '0'; return; }
    if (await micMeterStart(bar, who)) { testBtn.textContent = '■ Stop test'; fill(); }
  };
  if (navigator.mediaDevices && navigator.mediaDevices.addEventListener) {
    navigator.mediaDevices.ondevicechange = () => { if (sel.isConnected) fill(); };
  }
  fill();
  const raw = h('input', { type: 'checkbox', checked: micGet('micRaw', '0') === '1', onchange: (e) => { micSet('micRaw', e.target.checked ? '1' : '0'); if (micMeter) testBtn.onclick(true); } });
  return h('div', { class: 'card', id: 'miccard' },
    h('b', {}, '🎙️ Microphone'),
    h('label', { class: 'setrow' }, h('span', {}, 'Record with'), sel),
    h('label', { class: 'setrow' }, h('span', {}, 'External mic: turn off phone noise filters'), raw),
    h('div', { class: 'meter' }, bar), who, testBtn,
    h('details', { class: 'howto' }, h('summary', {}, 'Using a wireless or USB mic (e.g. RØDE Wireless PRO)'),
      h('ol', {},
        h('li', {}, 'Plug the receiver into the phone’s USB-C port and switch the transmitter on ', h('b', {}, 'before'), ' opening this page.'),
        h('li', {}, 'Tap ', h('b', {}, 'Test microphone'), ' and allow the microphone if asked. The list then shows every mic the phone can see.'),
        h('li', {}, 'Pick the RØDE (it may be called ', h('b', {}, 'USB audio'), ' or ', h('b', {}, 'USB headset'), ') under Record with, and speak into the transmitter. The bar should move.'),
        h('li', {}, 'Tick the noise filter box for a cleaner, more natural sound from a good external mic.'),
        h('li', {}, 'If the RØDE is not in the list: unplug and plug the receiver back in, then close Tagalify completely and open it again. In the RØDE app, make sure the receiver output is set to USB / digital, not 3.5 mm.'))));
}
async function startRec(text, done) {
  if (!navigator.mediaDevices || !window.MediaRecorder) { toast('Recording is not supported on this device'); return false; }
  micMeterStop();
  let stream;
  try { stream = await micStream(); } catch (e) { toast('Microphone permission is needed'); return false; }
  const mime = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4', 'audio/ogg'].find((m) => MediaRecorder.isTypeSupported(m));
  const mr = new MediaRecorder(stream, mime ? { mimeType: mime } : {});
  const chunks = [];
  mr.ondataavailable = (e) => { if (e.data.size) chunks.push(e.data); };
  mr.onstop = async () => {
    stream.getTracks().forEach((t) => t.stop());
    const blob = new Blob(chunks, { type: mr.mimeType || 'audio/webm' });
    await recPut(slug(text), { blob, type: blob.type, text, ts: Date.now() });
    onRecordingChanged(slug(text), false);
    recorder = null; done();
  };
  mr.start();
  recorder = mr;
  return true;
}
function studioItems(L) {
  const sents = [], en = new Map();
  L.sections.forEach((s) => s.blocks.forEach((b) => { if (b.type === 'examples') b.items.forEach((i) => { if (!sents.includes(i.tl)) { sents.push(i.tl); en.set(i.tl, i.en); } }); }));
  const ws = [];
  L.vocab.forEach((v) => { if (!ws.includes(v.tl)) { ws.push(v.tl); en.set(v.tl, v.en); } });
  return { ws, sents, en };
}
function viewStudio(v) {
  if (!v.have) { v.have = new Set(); recKeys().then((ks) => { ks.forEach((k) => v.have.add(k)); if (stack[stack.length - 1] === v) render(true); }); }
  if (v.lid == null) v.lid = course.lessons[0].id;
  const L = lessons.get(v.lid), it = studioItems(L);
  const row = (text) => {
    const key = slug(text);
    const el = h('div', { class: 'srow' });
    const draw = () => {
      const has = v.have.has(key), isRec = v.recording === key;
      el.replaceChildren(...[
        h('span', { class: 'dot' + (has ? ' on' : '') }),
        h('span', { class: 'stxt' }, h('b', {}, text), it.en.get(text) ? h('small', { class: 'sen' }, it.en.get(text)) : null),
        has ? h('button', { class: 'ib', 'aria-label': 'Play recording', onclick: () => say(text) }, '▶') : null,
        h('button', { class: 'ib rec' + (isRec ? ' live' : ''), 'aria-label': isRec ? 'Stop recording' : 'Record ' + text, onclick: async () => {
          if (isRec) { recorder && recorder.stop(); return; }
          if (recorder) return;
          const ok = await startRec(text, () => { v.have.add(key); v.recording = null; toast('Saved'); render(true); });
          if (ok) { v.recording = key; draw(); }
        } }, isRec ? '■' : '●'),
        has ? h('button', { class: 'ib', 'aria-label': 'Delete recording', onclick: async () => { await recDel(key); onRecordingChanged(key, true); v.have.delete(key); render(true); } }, '✕') : null].filter(Boolean));
    };
    draw();
    return el;
  };
  const total = it.ws.length + it.sents.length;
  const done = [...it.ws, ...it.sents].filter((t) => v.have.has(slug(t))).length;
  add(topbar('Recording studio', done + ' of ' + total + ' recorded in this lesson', h('img', { class: 'tb-logo', src: 'icon-192.png', alt: '', width: 34, height: 34 })),
    h('div', { class: 'card' },
      h('p', {}, 'Tap the red dot, say the word clearly, tap the square to stop. Your voice replaces the phone’s computer voice everywhere in the app. When you are happy, tap Export and put the files in the audio folder of the app on GitHub.'),
      h('label', { class: 'setrow' }, h('span', {}, 'Lesson'),
        h('select', { onchange: (e) => { v.lid = e.target.value; render(); } },
          course.lessons.map((m) => h('option', { value: m.id, selected: m.id === v.lid }, (isNaN(+m.label) ? '' : m.label + '. ') + m.title)))),
      h('button', { class: 'btn block', onclick: exportAudio }, '⬇ Export all recordings (zip)')),
    v.mic || (v.mic = micCard()),
    h('h3', { class: 'unit' }, 'Words'), h('div', { class: 'card tight' }, it.ws.map(row)),
    it.sents.length ? [h('h3', { class: 'unit' }, 'Sentences'), h('div', { class: 'card tight' }, it.sents.map(row))] : null);
}
async function exportAudio() {
  const keys = await recKeys();
  if (!keys.length) { toast('Nothing recorded yet'); return; }
  const files = [], man = { ...manifest }, enc = new TextEncoder();
  for (const k of keys) {
    const r = await recGet(k);
    if (!r || !r.blob) continue;
    const ext = /mp4|aac/.test(r.type) ? 'm4a' : /ogg/.test(r.type) ? 'ogg' : 'webm';
    const path = 'audio/' + k + '.' + ext;
    files.push({ name: path, data: new Uint8Array(await r.blob.arrayBuffer()) });
    man[k] = path;
  }
  files.push({ name: 'audio/manifest.json', data: enc.encode(JSON.stringify(man, null, 1)) });
  download('tagalify-audio.zip', makeZip(files));
  toast('Exported ' + (files.length - 1) + ' recordings');
}

/* ---------- computer voice ---------- */
function voiceCard() {
  const s = db.settings;
  const fil = filVoices();
  const cur = pickVoice();
  const good = cur && isFil(cur);
  return h('div', { class: 'card', id: 'voicecard' },
    h('b', {}, '\u{1F5E3}\uFE0F Computer voice'),
    h('div', { class: 'syncstate ' + (good ? 'good' : 'bad') },
      h('b', {}, good ? '\u2705 Filipino voice: ' + cur.name : '\u26A0\uFE0F No Filipino voice found on this phone'),
      h('small', {}, good ? 'Used for any word that has no recording yet.' : 'Words without a recording are read by an English voice, which sounds wrong. Install the Filipino voice using the steps below.')),
    fil.length > 1 ? opt('Voice', s.voice || cur.voiceURI, fil.map((x) => [x.voiceURI, x.name]), (x) => { s.voice = x; save(); }) : null,
    opt('Speaking speed', s.rate, [[0.7, 'Slow'], [0.9, 'Normal'], [1.05, 'Fast']], (x) => { s.rate = +x; save(); }),
    h('button', { class: 'btn ghost block', onclick: () => tts('Magandáng umága pô. Kumustá kayó?') }, '\u{1F50A} Test the voice'),
    h('details', { class: 'howto' }, h('summary', {}, 'How to install the Filipino voice'),
      h('ol', {},
        h('li', {}, 'Open the Play Store and install or update ', h('b', {}, 'Speech Recognition & Synthesis from Google'), ' (also called Speech Services by Google).'),
        h('li', {}, 'Open your phone ', h('b', {}, 'Settings'), ' and search for ', h('b', {}, 'Text-to-speech'), '. On a Samsung it is under General management (or Accessibility).'),
        h('li', {}, 'Set ', h('b', {}, 'Preferred engine'), ' to ', h('b', {}, 'Speech Services by Google'), '.'),
        h('li', {}, 'Tap the gear next to it, then ', h('b', {}, 'Install voice data'), ' and choose ', h('b', {}, 'Filipino (Philippines)'), '. Download it and pick a voice.'),
        h('li', {}, 'Close Tagalify completely and open it again. This card should now show a Filipino voice.')),
      h('p', { class: 'fine' }, 'The computer voice is only a stand-in. Recordings from your native speaker always play first and sound best.')));
}

/* ---------- registry ---------- */
const TABS = { home: viewHome, course: viewCourse, words: viewWords, progress: viewProgress, more: viewMore };
const VIEWS = { hub: viewHub, reader: viewReader, learn: viewLearn, practice: viewPractice, review: viewReview, studio: viewStudio };

async function init() {
  applySettings();
  document.querySelectorAll('#nav button').forEach((b) => b.addEventListener('click', () => setTab(b.dataset.tab)));
  try {
    await loadData();
  } catch (e) {
    add(h('div', { class: 'card' }, h('b', {}, 'Could not load the lessons.'), h('p', {}, 'Open the app once with a connection, then it works offline.')));
    return;
  }
  const justConnected = await dbxHandleRedirect();
  if (justConnected) tab = 'more';
  render();
  if (dbxConnected()) scheduleSync(justConnected ? 300 : 1500);
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').then(() => navigator.serviceWorker.ready).then((reg) => {
      const urls = Object.values(manifest).filter((u) => typeof u === 'string');
      if (reg.active && urls.length) reg.active.postMessage({ type: 'cache', urls });
    }).catch(() => {});
  }
  if ('speechSynthesis' in window) {
    speechSynthesis.getVoices();
    speechSynthesis.onvoiceschanged = () => { const c = document.getElementById('voicecard'); if (c) c.replaceWith(voiceCard()); };
  }
}
init();
