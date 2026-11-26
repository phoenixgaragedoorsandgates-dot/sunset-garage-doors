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

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Continuous auto-scroll that people can also swipe/drag.
  // Content is repeated 3 times; we stay in the middle copy and jump by one
  // copy-width when the user gets near either edge, so it never runs out.
  function autoScroll(el, loopWidth, speed) {
    var hover = false, holdUntil = 0, last = null, touching = false, pos = 0;
    function w() { return loopWidth(); }
    function recenter() {
      var lw = w();
      if (lw <= 0) return;
      if (el.scrollLeft < lw * 0.5) el.scrollLeft += lw;
      else if (el.scrollLeft > lw * 1.5) el.scrollLeft -= lw;
    }
    function start() { el.scrollLeft = w(); pos = el.scrollLeft; }
    function tick(now) {
      if (last === null) last = now;
      var dt = Math.min(now - last, 100) / 1000;
      last = now;
      if (!reduce && !hover && !touching && now > holdUntil) {
        pos += speed * dt;
        el.scrollLeft = pos;
        recenter();
        pos = el.scrollLeft + (pos % 1);
      } else {
        pos = el.scrollLeft;
      }
      requestAnimationFrame(tick);
    }
    if (document.readyState === "complete") start(); else window.addEventListener("load", start);
    start();
    requestAnimationFrame(tick);
    el.addEventListener("scroll", recenter, { passive: true });
    window.addEventListener("resize", recenter);
    el.addEventListener("mouseenter", function () { hover = true; });
    el.addEventListener("mouseleave", function () { hover = false; });
    el.addEventListener("touchstart", function () { touching = true; }, { passive: true });
    el.addEventListener("touchend", function () { touching = false; holdUntil = performance.now() + 2500; }, { passive: true });
    el.addEventListener("wheel", function () { holdUntil = performance.now() + 2500; }, { passive: true });
    var dragging = false, startX = 0, startLeft = 0;
    el.addEventListener("mousedown", function (e) { dragging = true; startX = e.pageX; startLeft = el.scrollLeft; el.classList.add("dragging"); e.preventDefault(); });
    window.addEventListener("mousemove", function (e) {
      if (!dragging) return;
      el.scrollLeft = startLeft - (e.pageX - startX);
      var lw = w(), before = el.scrollLeft; recenter();
      startLeft += el.scrollLeft - before;
    });
    window.addEventListener("mouseup", function () { if (dragging) { dragging = false; el.classList.remove("dragging"); holdUntil = performance.now() + 1500; } });
    return { hold: function (ms) { holdUntil = performance.now() + ms; } };
  }

  // Brand logos (3 identical tracks)
  var marquee = document.querySelector(".marquee");
  if (marquee) {
    var mTrack = marquee.querySelector(".marquee-track");
    autoScroll(marquee, function () { return mTrack.offsetWidth + 16; }, 35);
  }

  // Reviews carousel
  var track = document.querySelector(".carousel");
  if (!track) return;
  var originals = Array.prototype.slice.call(track.children);
  originals.slice().reverse().forEach(function (c) {
    var clone = c.cloneNode(true); clone.setAttribute("aria-hidden", "true");
    track.insertBefore(clone, track.firstChild);
  });
  originals.forEach(function (c) {
    var clone = c.cloneNode(true); clone.setAttribute("aria-hidden", "true");
    track.appendChild(clone);
  });
  var reviews = autoScroll(track, function () { return track.scrollWidth / 3; }, 40);
  function cardStep() { var c = track.querySelector(".review"); return c ? c.getBoundingClientRect().width + 16 : 300; }
  document.querySelectorAll(".carousel-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var target = track.scrollLeft + (+b.dataset.dir) * cardStep();
      reviews.hold(4000);
      track.scrollTo({ left: target, behavior: "smooth" });
    });
  });
})();
