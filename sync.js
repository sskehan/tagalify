'use strict';
/* Tagalify Dropbox backup.
   Saves progress (progress.json) and the native-speaker recordings (recordings/*.webm|m4a|ogg)
   into the app's own folder in Dropbox: Dropbox > Apps > Tagalify.
   Uses Dropbox OAuth with PKCE, so no secret is stored in the app. */

// Paste the Dropbox App key here to build it in. If empty, the key can be typed into More > Dropbox backup.
const DBX_KEY_BUILTIN = 'klrgsofuelkzwbl';

const DBX_STORE = 'tagalify.dropbox';
const DBX_AUTH = 'https://www.dropbox.com/oauth2/authorize';
const DBX_TOKEN = 'https://api.dropboxapi.com/oauth2/token';
const DBX_API = 'https://api.dropboxapi.com/2/';
const DBX_CONTENT = 'https://content.dropboxapi.com/2/';

let dbx = loadDbx();
let syncTimer = null;
let syncing = false;
let syncStatus = '';

function loadDbx() {
  try { const d = JSON.parse(localStorage.getItem(DBX_STORE)); if (d && typeof d === 'object') return { wifiOnly: true, up: {}, del: [], ...d }; } catch (e) { /* fresh */ }
  return { wifiOnly: true, up: {}, del: [] };
}
function saveDbx() { try { localStorage.setItem(DBX_STORE, JSON.stringify(dbx)); } catch (e) { /* ignore */ } }
const dbxKey = () => (DBX_KEY_BUILTIN || dbx.key || '').trim();
const dbxConnected = () => !!dbx.refresh;
const redirectUri = () => location.origin + location.pathname;

function b64url(bytes) {
  let s = '';
  new Uint8Array(bytes).forEach((b) => { s += String.fromCharCode(b); });
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function dbxConnect() {
  if (!dbxKey()) { toast('Add your Dropbox App key first'); return; }
  const verifier = b64url(crypto.getRandomValues(new Uint8Array(48)));
  const challenge = b64url(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier)));
  dbx.verifier = verifier;
  saveDbx();
  location.href = DBX_AUTH + '?' + new URLSearchParams({
    client_id: dbxKey(), response_type: 'code', code_challenge: challenge,
    code_challenge_method: 'S256', redirect_uri: redirectUri(), token_access_type: 'offline',
  });
}

/* Called on start-up. Finishes the connection when Dropbox sends the user back with ?code=… */
async function dbxHandleRedirect() {
  const q = new URLSearchParams(location.search);
  if (!q.has('code') && !q.has('error')) return false;
  history.replaceState(null, '', redirectUri());
  if (q.has('error') || !dbx.verifier) { toast('Dropbox was not connected'); return false; }
  try {
    const r = await fetch(DBX_TOKEN, {
      method: 'POST',
      body: new URLSearchParams({ code: q.get('code'), grant_type: 'authorization_code', client_id: dbxKey(), redirect_uri: redirectUri(), code_verifier: dbx.verifier }),
    });
    if (!r.ok) throw new Error('token ' + r.status);
    const t = await r.json();
    dbx.refresh = t.refresh_token;
    dbx.access = t.access_token;
    dbx.exp = Date.now() + ((t.expires_in || 14400) - 60) * 1000;
    dbx.account = t.account_id || '';
    delete dbx.verifier;
    dbx.firstSync = true;
    saveDbx();
    toast('Dropbox connected');
    return true;
  } catch (e) {
    delete dbx.verifier; saveDbx();
    toast('Could not connect to Dropbox. Check the App key and redirect URI.');
    return false;
  }
}

function dbxDisconnect() {
  const key = dbx.key;
  dbx = { wifiOnly: dbx.wifiOnly, up: {}, del: [], key };
  saveDbx();
  syncStatus = '';
}

async function dbxToken() {
  if (dbx.access && Date.now() < (dbx.exp || 0)) return dbx.access;
  if (!dbx.refresh) throw new Error('not connected');
  const r = await fetch(DBX_TOKEN, { method: 'POST', body: new URLSearchParams({ grant_type: 'refresh_token', refresh_token: dbx.refresh, client_id: dbxKey() }) });
  if (!r.ok) {
    if (r.status === 400 || r.status === 401) { dbx.refresh = null; saveDbx(); throw new Error('Dropbox access was removed. Connect again.'); }
    throw new Error('token ' + r.status);
  }
  const t = await r.json();
  dbx.access = t.access_token;
  dbx.exp = Date.now() + ((t.expires_in || 14400) - 60) * 1000;
  saveDbx();
  return dbx.access;
}

async function dbxRpc(endpoint, args) {
  const r = await fetch(DBX_API + endpoint, { method: 'POST', headers: { Authorization: 'Bearer ' + await dbxToken(), 'Content-Type': 'application/json' }, body: JSON.stringify(args) });
  if (r.status === 409) return null;          // path not found and similar
  if (r.status === 429) throw new Error('Dropbox is busy (rate limited). It will try again later.');
  if (!r.ok) throw new Error(endpoint + ' ' + r.status);
  return r.json();
}
async function dbxUpload(path, body) {
  const r = await fetch(DBX_CONTENT + 'files/upload', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + await dbxToken(), 'Dropbox-API-Arg': JSON.stringify({ path, mode: 'overwrite', mute: true }), 'Content-Type': 'application/octet-stream' },
    body,
  });
  if (r.status === 429) throw new Error('Dropbox is busy (rate limited). It will try again later.');
  if (!r.ok) throw new Error('upload ' + r.status);
  return r.json();
}
async function dbxDownload(path) {
  const r = await fetch(DBX_CONTENT + 'files/download', { method: 'POST', headers: { Authorization: 'Bearer ' + await dbxToken(), 'Dropbox-API-Arg': JSON.stringify({ path }) } });
  if (r.status === 409) return null;
  if (!r.ok) throw new Error('download ' + r.status);
  return r.blob();
}
async function dbxList(path) {
  let res = await dbxRpc('files/list_folder', { path });
  if (!res) return [];
  const out = res.entries.slice();
  while (res.has_more) { res = await dbxRpc('files/list_folder/continue', { cursor: res.cursor }); out.push(...res.entries); }
  return out.filter((e) => e['.tag'] === 'file');
}

function onWifi() {
  const c = navigator.connection;
  if (!c || !c.type) return true;            // not reported by this browser: assume ok
  return c.type === 'wifi' || c.type === 'ethernet';
}
const extOf = (type) => (/mp4|aac/.test(type) ? 'm4a' : /ogg/.test(type) ? 'ogg' : 'webm');
const typeOf = (name) => (/\.m4a$/.test(name) ? 'audio/mp4' : /\.ogg$/.test(name) ? 'audio/ogg' : 'audio/webm');

/* Main backup. manual = started by a button (ignores the Wi-Fi-only setting). */
async function dbxSync(manual) {
  if (!dbxConnected() || syncing) return false;
  if (!navigator.onLine) { syncStatus = 'Offline. Will back up when online.'; refreshSyncCard(); return false; }
  if (!manual && dbx.wifiOnly && !onWifi()) { syncStatus = 'Waiting for Wi-Fi.'; refreshSyncCard(); return false; }
  syncing = true; syncStatus = 'Backing up…'; refreshSyncCard();
  let restored = false, sent = 0, got = 0;
  try {
    // 1. Progress: the newest copy wins.
    const remoteBlob = await dbxDownload('/progress.json');
    let remote = null;
    if (remoteBlob) { try { remote = JSON.parse(await remoteBlob.text()); } catch (e) { remote = null; } }
    const localEmpty = !Object.keys(db.cards).length && !Object.keys(db.lessons).length;
    if (remote && remote.cards && ((remote.savedAt || 0) > (db.savedAt || 0) || (dbx.firstSync && localEmpty))) {
      localStorage.setItem(KEY, JSON.stringify(remote));
      db = loadDb();
      save(true);
      restored = true;
    } else if (!remote || (db.savedAt || 0) > (remote.savedAt || 0)) {
      await dbxUpload('/progress.json', new Blob([JSON.stringify(db)], { type: 'application/json' }));
    }
    // 2. Recordings: deletions first, then upload new ones, then download missing ones.
    for (const key of (dbx.del || []).slice()) {
      for (const ext of ['webm', 'm4a', 'ogg']) await dbxRpc('files/delete_v2', { path: '/recordings/' + key + '.' + ext });
      dbx.del = dbx.del.filter((k) => k !== key);
      delete dbx.up[key];
      saveDbx();
    }
    const remoteFiles = await dbxList('/recordings');
    const remoteKeys = new Set(remoteFiles.map((f) => f.name.replace(/\.[^.]+$/, '')));
    for (const key of await recKeys()) {
      const rec = await recGet(key);
      if (!rec || !rec.blob) continue;
      if (remoteKeys.has(key) && (dbx.up[key] || 0) >= (rec.ts || 0)) continue;
      await dbxUpload('/recordings/' + key + '.' + extOf(rec.type), rec.blob);
      dbx.up[key] = rec.ts || Date.now();
      saveDbx();
      sent++;
    }
    const have = new Set(await recKeys());
    for (const f of remoteFiles) {
      const key = f.name.replace(/\.[^.]+$/, '');
      if (have.has(key) || (dbx.del || []).includes(key)) continue;
      const blob = await dbxDownload(f.path_lower || '/recordings/' + f.name);
      if (!blob) continue;
      const ts = Date.parse(f.server_modified) || Date.now();
      await recPut(key, { blob: new Blob([blob], { type: typeOf(f.name) }), type: typeOf(f.name), text: key, ts });
      dbx.up[key] = ts;
      got++;
    }
    dbx.last = Date.now();
    dbx.firstSync = false;
    dbx.error = '';
    saveDbx();
    syncStatus = '';
    if (manual || restored || got) toast(restored ? 'Progress restored from Dropbox' : got ? got + ' recordings downloaded from Dropbox' : 'Backed up to Dropbox' + (sent ? ' (' + sent + ' recordings)' : ''));
  } catch (e) {
    dbx.error = e.message || 'Backup failed';
    saveDbx();
    syncStatus = '';
    if (manual) toast(dbx.error);
  } finally {
    syncing = false;
  }
  if (restored) { applySettings(); render(true); } else refreshSyncCard();
  return true;
}

function scheduleSync(delay) {
  if (!dbxConnected()) return;
  clearTimeout(syncTimer);
  syncTimer = setTimeout(() => dbxSync(false), delay == null ? 8000 : delay);
}
/* Hooks used by core.js and the recording studio */
function onSaved() { scheduleSync(); }
function onRecordingChanged(key, deleted) {
  if (!dbxConnected()) return;
  if (deleted) { if (!dbx.del.includes(key)) dbx.del.push(key); saveDbx(); }
  scheduleSync(3000);
}

window.addEventListener('online', () => scheduleSync(2000));
document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') scheduleSync(0); });
if (navigator.connection && navigator.connection.addEventListener) navigator.connection.addEventListener('change', () => scheduleSync(3000));

/* ---------- More screen card ---------- */
function syncCardBody() {
  const rows = [];
  if (!dbxConnected()) {
    rows.push(h('p', {}, 'Back up your progress and your native speaker’s recordings to Dropbox, so nothing is lost if you clear the browser or change phones. Files go to ', h('b', {}, 'Dropbox › Apps › Tagalify'), '.'));
    if (!DBX_KEY_BUILTIN) {
      rows.push(h('label', { class: 'setrow' }, h('span', {}, 'Dropbox App key'),
        h('input', { class: 'keyin', type: 'text', value: dbx.key || '', placeholder: 'e.g. abc123xyz', autocapitalize: 'off', spellcheck: 'false',
          onchange: (e) => { dbx.key = e.target.value.trim(); saveDbx(); } })));
    }
    rows.push(h('button', { class: 'btn block', onclick: () => { const i = document.querySelector('.keyin'); if (i) { dbx.key = i.value.trim(); saveDbx(); } dbxConnect(); } }, 'Connect Dropbox'));
  } else {
    const when = dbx.last ? new Date(dbx.last).toLocaleString([], { dateStyle: 'medium', timeStyle: 'short' }) : 'not yet';
    rows.push(h('div', { class: 'syncstate ' + (dbx.error ? 'bad' : 'good') },
      h('b', {}, dbx.error ? '⚠️ ' + dbx.error : '✅ Connected'),
      h('small', {}, syncStatus || 'Last backup: ' + when)));
    rows.push(h('label', { class: 'setrow' }, h('span', {}, 'Back up on Wi-Fi only'),
      h('input', { type: 'checkbox', checked: dbx.wifiOnly, onchange: (e) => { dbx.wifiOnly = e.target.checked; saveDbx(); } })));
    rows.push(h('div', { class: 'row' },
      h('button', { class: 'btn', onclick: () => dbxSync(true) }, 'Back up now'),
      h('button', { class: 'btn ghost', onclick: () => { if (confirm('Disconnect Dropbox on this phone? Your files stay in Dropbox.')) { dbxDisconnect(); refreshSyncCard(); } } }, 'Disconnect')));
    rows.push(h('p', { class: 'fine' }, 'Backs up automatically a few seconds after any change, and when you leave the app. On a new phone, connect Dropbox and your progress and recordings come back.'));
  }
  return rows;
}
function refreshSyncCard() {
  const c = document.getElementById('synccard');
  if (c) c.replaceChildren(h('b', {}, '☁️ Dropbox backup'), ...syncCardBody());
}
function syncCard() {
  return h('div', { class: 'card', id: 'synccard' }, h('b', {}, '☁️ Dropbox backup'), ...syncCardBody());
}
