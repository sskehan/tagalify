'use strict';
// Bump VERSION whenever app code (index.html, core.js, app.js, style.css) changes so phones pick it up.
const VERSION = 'tagalify-v2.01';
const SHELL = ['./', 'index.html', 'style.css', 'core.js', 'sync.js', 'app.js', 'manifest.webmanifest',
  'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'apple-touch-icon.png', 'logo.png',
  'data/course.json', 'data/reference.json', 'data/glossary.json', 'audio/manifest.json'];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(VERSION);
    await cache.addAll(SHELL);
    try {
      const idx = await (await fetch('data/course.json', { cache: 'no-cache' })).json();
      await Promise.all(idx.lessons.map((l) => cache.add(l.file).catch(() => {})));
    } catch (e) { /* lesson files get cached on first use instead */ }
    self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('message', (event) => {
  const msg = event.data || {};
  if (msg.type === 'cache' && Array.isArray(msg.urls)) {
    event.waitUntil((async () => {
      const cache = await caches.open(VERSION);
      await Promise.all(msg.urls.map((u) => cache.add(u).catch(() => {})));
    })());
  }
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  const isAudio = url.pathname.includes('/audio/') && !url.pathname.endsWith('manifest.json');
  event.respondWith((async () => {
    const cache = await caches.open(VERSION);
    if (isAudio) {
      const hit = await cache.match(req, { ignoreSearch: true });
      if (hit) return hit;
    }
    try {
      // no-cache: always ask GitHub whether the file changed (avoids the 10-minute browser cache delay)
      const fresh = await fetch(req.mode === 'navigate' ? req.url : req, { cache: 'no-cache' });
      if (fresh && fresh.status === 200) cache.put(req, fresh.clone());
      return fresh;
    } catch (e) {
      const hit = await cache.match(req, { ignoreSearch: true });
      if (hit) return hit;
      if (req.mode === 'navigate') {
        const shell = await cache.match('index.html');
        if (shell) return shell;
      }
      throw e;
    }
  })());
});
