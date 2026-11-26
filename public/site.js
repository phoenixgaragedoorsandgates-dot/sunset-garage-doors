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

  // Continuous auto-scroll that people can also swipe/drag. Loops seamlessly.
  function autoScroll(el, loopWidth, speed) {
    var pos = el.scrollLeft, hover = false, holdUntil = 0, last = null, touching = false;
    function wrap() {
      var w = loopWidth();
      if (w <= 0) return;
      if (el.scrollLeft >= w) el.scrollLeft -= w;
      else if (el.scrollLeft <= 0 && (touching || performance.now() < holdUntil)) el.scrollLeft += w;
    }
    function tick(now) {
      if (last === null) last = now;
      var dt = Math.min(now - last, 100) / 1000;
      last = now;
      if (!reduce && !hover && !touching && now > holdUntil) {
        pos += speed * dt;
        var w = loopWidth();
        if (w > 0 && pos >= w) pos -= w;
        el.scrollLeft = pos;
      } else {
        pos = el.scrollLeft;
      }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    el.addEventListener("scroll", wrap, { passive: true });
    el.addEventListener("mouseenter", function () { hover = true; });
    el.addEventListener("mouseleave", function () { hover = false; });
    el.addEventListener("touchstart", function () { touching = true; }, { passive: true });
    el.addEventListener("touchend", function () { touching = false; holdUntil = performance.now() + 2500; }, { passive: true });
    el.addEventListener("wheel", function () { holdUntil = performance.now() + 2500; }, { passive: true });
    // Drag with a mouse on desktop
    var dragging = false, startX = 0, startLeft = 0;
    el.addEventListener("mousedown", function (e) { dragging = true; startX = e.pageX; startLeft = el.scrollLeft; el.classList.add("dragging"); e.preventDefault(); });
    window.addEventListener("mousemove", function (e) { if (dragging) { el.scrollLeft = startLeft - (e.pageX - startX); } });
    window.addEventListener("mouseup", function () { if (dragging) { dragging = false; el.classList.remove("dragging"); holdUntil = performance.now() + 1500; } });
    return { hold: function (ms) { holdUntil = performance.now() + ms; } };
  }

  // Brand logos
  var marquee = document.querySelector(".marquee");
  if (marquee) {
    var firstTrack = marquee.querySelector(".marquee-track");
    autoScroll(marquee, function () { return firstTrack.offsetWidth + 16; }, 35);
  }

  // Reviews carousel
  var track = document.querySelector(".carousel");
  if (!track) return;
  Array.prototype.slice.call(track.children).forEach(function (c) {
    var clone = c.cloneNode(true);
    clone.setAttribute("aria-hidden", "true");
    track.appendChild(clone);
  });
  var reviews = autoScroll(track, function () { return track.scrollWidth / 2; }, 40);
  function cardStep() { var c = track.querySelector(".review"); return c ? c.getBoundingClientRect().width + 16 : 300; }
  document.querySelectorAll(".carousel-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var w = track.scrollWidth / 2, dir = +b.dataset.dir;
      var target = track.scrollLeft + dir * cardStep();
      if (target < 0) { track.scrollLeft += w; target += w; }
      if (target >= w) { track.scrollLeft -= w; target -= w; }
      reviews.hold(4000);
      track.scrollTo({ left: target, behavior: "smooth" });
    });
  });
})();
