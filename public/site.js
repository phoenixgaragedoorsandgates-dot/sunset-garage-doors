(function () {
  document.querySelectorAll(".yr").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Land exactly on #section links. Photos and fonts above the section can
  // finish loading while (or after) the page scrolls and push it down, so we
  // keep re-aligning for a moment until the layout settles.
  function headerOffset() { var h = document.querySelector(".site-header"); return (h ? h.offsetHeight : 0) + 12; }
  function settleOn(id, smooth) {
    var el = document.getElementById(id);
    if (!el) return;
    var until = performance.now() + 4000, userMoved = false;
    // Skip the section's empty top padding: land on its label/heading instead.
    var anchor = el.querySelector(".label, h1, h2") || el;
    var extra = anchor === el ? 0 : (window.innerWidth < 760 ? 0 : 20);
    function y() { return anchor.getBoundingClientRect().top + window.pageYOffset - headerOffset() - extra; }
    function stop() { userMoved = true; }
    window.addEventListener("wheel", stop, { once: true, passive: true });
    window.addEventListener("touchstart", stop, { once: true, passive: true });
    if (smooth) {
      // Our own glide (iPhone's built-in smooth scroll stops a few pixels off,
      // which forced a visible correction). The target is re-measured every
      // frame, so anything that loads mid-glide is absorbed without a jump.
      var start = window.pageYOffset, t0 = performance.now();
      var dur = Math.min(900, Math.max(350, Math.abs(y() - start) * 0.25));
      (function glide(now) {
        if (userMoved) return;
        var k = Math.min((now - t0) / dur, 1);
        var e = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
        window.scrollTo(0, start + (y() - start) * e);
        if (k < 1) requestAnimationFrame(glide);
      })(t0);
      return;
    }
    // Page opened with #section in the address: jump, then follow late layout shifts.
    window.scrollTo(0, y());
    var lastT = y();
    (function follow() {
      if (userMoved || performance.now() > until) return;
      var t = y();
      if (Math.abs(t - lastT) > 2) { lastT = t; window.scrollTo(0, t); }
      requestAnimationFrame(follow);
    })();
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href*='#']");
    if (!a) return;
    var url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash) return;
    var id = decodeURIComponent(url.hash.slice(1));
    if (!document.getElementById(id)) return;
    e.preventDefault();
    history.pushState(null, "", url.hash);
    settleOn(id, true);
  });
  if (location.hash) {
    var startId = decodeURIComponent(location.hash.slice(1));
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    settleOn(startId, false);
    window.addEventListener("load", function () { settleOn(startId, false); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { settleOn(startId, false); });
  }

  // Analytics: count taps on call and text buttons
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href^='tel:'], a[href^='sms:']");
    if (!a || typeof window.gtag !== "function") return;
    var where = a.closest(".mobile-bar") ? "mobile_bar" : a.closest(".site-header, .mnav") ? "header"
      : a.closest(".site-footer") ? "footer" : a.closest(".hero") ? "hero" : "page";
    window.gtag("event", a.href.indexOf("tel:") === 0 ? "call_click" : "text_click", {
      link_location: where, page_path: location.pathname
    });
  }, true);

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

  // Carousels: we move the strip ourselves with a CSS transform (no native
  // scrolling), so fast flicks on iPhone can't leave it blank. Content is
  // repeated 3x and the position wraps, so it loops forever both ways.
  function loopCarousel(el, loopWidth, speed) {
    var offset = 0, vel = 0, last = null, hover = false, holdUntil = 0;
    var down = false, dragging = false, startX = 0, startY = 0, lastX = 0, lastT = 0, anim = null;
    function mod(a, n) { return ((a % n) + n) % n; }
    function render() {
      var w = loopWidth();
      if (w > 0) el.style.setProperty("--x", (-(w + mod(offset, w))).toFixed(2) + "px");
    }
    function tick(now) {
      if (last === null) last = now;
      var dt = Math.min(now - last, 64) / 1000;
      last = now;
      if (anim) {
        var t = Math.min((now - anim.t0) / anim.dur, 1), e2 = 1 - Math.pow(1 - t, 3);
        offset = anim.from + (anim.to - anim.from) * e2;
        if (t >= 1) anim = null;
      } else if (!dragging) {
        if (Math.abs(vel) > 5) {
          offset += vel * dt;
          vel *= Math.pow(0.04, dt); // smooth slow-down
        } else {
          vel = 0;
          if (!reduce && !hover && now > holdUntil) offset += speed * dt;
        }
      }
      render();
      requestAnimationFrame(tick);
    }
    el.addEventListener("pointerdown", function (e) {
      if (e.button !== undefined && e.button !== 0) return;
      down = true; dragging = false; anim = null;
      startX = lastX = e.clientX; startY = e.clientY; lastT = performance.now();
    });
    window.addEventListener("pointermove", function (e) {
      if (!down) return;
      var dx = e.clientX - startX, dy = e.clientY - startY;
      if (!dragging) {
        if (Math.abs(dx) < 6 || Math.abs(dx) < Math.abs(dy)) return;
        dragging = true; vel = 0;
        el.classList.add("dragging");
      }
      var now = performance.now(), mx = e.clientX - lastX;
      offset -= mx;
      var dtm = Math.max(now - lastT, 1);
      vel = vel * 0.6 + (-mx / dtm * 1000) * 0.4;
      lastX = e.clientX; lastT = now;
    });
    function end() {
      if (!down) return;
      down = false;
      if (dragging) {
        dragging = false; el.classList.remove("dragging");
        if (performance.now() - lastT > 80) vel = 0;
        vel = Math.max(-6000, Math.min(6000, vel));
      }
      holdUntil = performance.now() + 2500;
    }
    window.addEventListener("pointerup", end);
    window.addEventListener("pointercancel", end);
    el.addEventListener("mouseenter", function () { hover = true; });
    el.addEventListener("mouseleave", function () { hover = false; });
    el.addEventListener("dragstart", function (e) { e.preventDefault(); });
    el.addEventListener("wheel", function (e) {
      if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) { e.preventDefault(); offset += e.deltaX; vel = 0; holdUntil = performance.now() + 2500; }
    }, { passive: false });
    window.addEventListener("resize", render);
    render();
    requestAnimationFrame(tick);
    return {
      step: function (px) {
        vel = 0; holdUntil = performance.now() + 4000;
        var from = anim ? anim.to : offset;
        anim = { from: offset, to: from + px, t0: performance.now(), dur: 450 };
      }
    };
  }

  // Brand logos (3 identical tracks in the HTML)
  var marquee = document.querySelector(".marquee");
  if (marquee) {
    var mTrack = marquee.querySelector(".marquee-track");
    loopCarousel(marquee, function () { return mTrack.offsetWidth + 16; }, 60);
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
  var n = originals.length;
  var reviews = loopCarousel(track, function () {
    return track.children[n].offsetLeft - track.children[0].offsetLeft;
  }, 50);
  function cardStep() { var c = track.querySelector(".review"); return c ? c.getBoundingClientRect().width + 16 : 300; }
  document.querySelectorAll(".carousel-btn").forEach(function (b) {
    b.addEventListener("click", function () { reviews.step((+b.dataset.dir) * cardStep()); });
  });
})();
