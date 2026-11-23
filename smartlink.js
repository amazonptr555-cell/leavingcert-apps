// Sends each visitor to the right store for this app and their device.
// Each app page sets window.LC_APP_ID before loading this file.
(function () {
  var app = (window.LC_APPS || {})[window.LC_APP_ID] || {};
  var ua = navigator.userAgent || "";
  var isIOS = /iPhone|iPad|iPod/i.test(ua) ||
    (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1); // iPadOS reports as a Mac
  var isAndroid = /Android/i.test(ua);

  if (isIOS && app.ios) { window.location.replace(app.ios); return; }
  if (isAndroid && app.android) { window.location.replace(app.android); return; }

  document.documentElement.className = isAndroid ? "android" : (isIOS ? "ios" : "desktop");
  document.addEventListener("DOMContentLoaded", function () {
    setButton("ios", app.ios, "App Store: coming soon");
    setButton("android", app.android, "Android: coming soon");
  });

  function setButton(id, url, comingSoon) {
    var a = document.getElementById(id);
    if (!a) return;
    if (url) { a.href = url; }
    else { a.textContent = comingSoon; a.removeAttribute("href"); a.className += " off"; }
  }
})();
