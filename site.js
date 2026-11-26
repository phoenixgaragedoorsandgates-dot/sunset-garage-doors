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

  // Reviews carousel
  var track = document.querySelector(".carousel");
  if (!track) return;
  function step() { var c = track.querySelector(".review"); return c ? c.getBoundingClientRect().width + 16 : 300; }
  function go(dir) {
    var max = track.scrollWidth - track.clientWidth - 4;
    if (dir > 0 && track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: "smooth" });
    else if (dir < 0 && track.scrollLeft <= 4) track.scrollTo({ left: max, behavior: "smooth" });
    else track.scrollBy({ left: dir * step(), behavior: "smooth" });
  }
  var paused = false, t;
  function pause() { paused = true; clearTimeout(t); t = setTimeout(function () { paused = false; }, 12000); }
  document.querySelectorAll(".carousel-btn").forEach(function (b) {
    b.addEventListener("click", function () { go(+b.dataset.dir); pause(); });
  });
  ["mouseenter", "touchstart", "focusin"].forEach(function (ev) { track.addEventListener(ev, pause, { passive: true }); });
  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    setInterval(function () { if (!paused && !document.hidden) go(1); }, 6000);
  }
})();
