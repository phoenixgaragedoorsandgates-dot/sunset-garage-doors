(function () {
  document.querySelectorAll(".yr").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Mobile menu
  var btn = document.querySelector(".menu-btn");
  var mnav = document.getElementById("mnav");
  if (btn && mnav) {
    btn.addEventListener("click", function () {
      var open = mnav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    mnav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { mnav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); }
    });
  }

  // Reviews carousel: slow continuous scroll, pauses on hover/touch, arrows jump one card
  var track = document.querySelector(".carousel");
  if (!track) return;
  var originals = Array.prototype.slice.call(track.children);
  originals.forEach(function (c) {
    var clone = c.cloneNode(true);
    clone.setAttribute("aria-hidden", "true");
    track.appendChild(clone);
  });
  function loopWidth() { return track.scrollWidth / 2; }
  function cardStep() { var c = track.querySelector(".review"); return c ? c.getBoundingClientRect().width + 16 : 300; }
  var pos = 0, hover = false, holdUntil = 0, last = null;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var SPEED = 40; // pixels per second

  function tick(now) {
    if (last === null) last = now;
    var dt = Math.min(now - last, 100) / 1000;
    last = now;
    if (!hover && now > holdUntil && !reduce) {
      pos += SPEED * dt;
      var w = loopWidth();
      if (pos >= w) pos -= w;
      track.scrollLeft = pos;
    } else {
      pos = track.scrollLeft;
    }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);

  function jump(dir) {
    var w = loopWidth();
    var target = track.scrollLeft + dir * cardStep();
    if (target < 0) { track.scrollLeft += w; target += w; }
    if (target >= w) { track.scrollLeft -= w; target -= w; }
    holdUntil = performance.now() + 4000;
    track.scrollTo({ left: target, behavior: "smooth" });
  }
  document.querySelectorAll(".carousel-btn").forEach(function (b) {
    b.addEventListener("click", function () { jump(+b.dataset.dir); });
  });
  track.addEventListener("mouseenter", function () { hover = true; });
  track.addEventListener("mouseleave", function () { hover = false; });
  track.addEventListener("touchstart", function () { holdUntil = performance.now() + 5000; }, { passive: true });
  track.addEventListener("focusin", function () { hover = true; });
  track.addEventListener("focusout", function () { hover = false; });
})();
