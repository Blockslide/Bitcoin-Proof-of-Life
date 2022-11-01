//--------------------------------------------------------------------------
// You can find dozens of practical, detailed, and working examples of
// service worker usage on https://github.com/mozilla/serviceworker-cookbook
//--------------------------------------------------------------------------

// Cache name
var CACHE_NAME = 'cache-version-1';

// Files
var REQUIRED_FILES = [
  'index.html',
  '/bitcoin-proof-of-life',
  'https://cdn.jsdelivr.net/npm/bootstrap-dark-5@1.1.3/dist/css/bootstrap-dark.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/PullToRefresh/0.1.1/ptr.min.css',
  'https://cdn.jsdelivr.net/npm/easyqrcodejs@4.4.10/dist/easy.qrcode.min.js',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js',
  'https://cdn.jsdelivr.net/npm/luxon@2.3.0/build/global/luxon.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/PullToRefresh/0.1.1/ptr.min.js'
];

self.addEventListener('install', function (event) {
  // Perform install step:  loading each required file into cache
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        // Add all offline dependencies to the cache
        return cache.addAll(REQUIRED_FILES);
      })
      .then(function () {
        return self.skipWaiting();
      })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        // Cache hit - return the response from the cached version
        if (response) {
          return response;
        }
        // Not in cache - return the result from the live server
        // `fetch` is essentially a "fallback"
        return fetch(event.request);
      }
      )
  );
});

self.addEventListener('activate', function (event) {
  // Calling claim() to force a "controllerchange" event on navigator.serviceWorker
  event.waitUntil(self.clients.claim());
});
