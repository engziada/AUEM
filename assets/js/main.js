// AUEM — navigation, announcement bar and gallery lightbox.
// Content comes from content/*.json at build time; this file only adds behaviour.

document.addEventListener("DOMContentLoaded", function () {
  /* ---------------- mobile navigation ---------------- */
  var toggle = document.querySelector(".nav-toggle");
  function syncNavAria() {
    if (toggle) {
      var isOpen = document.body.classList.contains("nav-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    }
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      setTimeout(syncNavAria, 10);
    });
  }

  document.querySelectorAll(".nav-link").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("nav-open");
      syncNavAria();
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
      document.body.classList.remove("nav-open");
      syncNavAria();
    }
  });

  /* ---------------- announcement bar ---------------- */
  (function announcements() {
    var bar = document.getElementById("announce-bar");
    if (!bar) return;

    var KEY = "auem.announce.dismissed";
    var all = Array.prototype.slice.call(bar.querySelectorAll(".announce-msg"));
    if (!all.length) {
      bar.remove();
      return;
    }

    function loadDismissed() {
      try {
        var raw = JSON.parse(window.localStorage.getItem(KEY) || "[]");
        return Object.prototype.toString.call(raw) === "[object Array]" ? raw : [];
      } catch (e) {
        return [];
      }
    }

    function saveDismissed(list) {
      try {
        window.localStorage.setItem(KEY, JSON.stringify(list.slice(-40)));
      } catch (e) {
        /* private mode: dismissal just won't persist */
      }
    }

    var dismissed = loadDismissed();
    var live = all.filter(function (msg) {
      return dismissed.indexOf(msg.getAttribute("data-announce-id")) === -1;
    });
    if (!live.length) {
      bar.remove();
      return;
    }

    var index = 0;
    var timer = null;
    var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function show(i) {
      index = (i + live.length) % live.length;
      live.forEach(function (msg, n) {
        msg.classList.toggle("is-active", n === index);
      });
    }

    function stop() {
      if (timer) {
        window.clearInterval(timer);
        timer = null;
      }
    }

    function start() {
      if (live.length < 2 || reduced) return;
      stop();
      timer = window.setInterval(function () {
        show(index + 1);
      }, 8000);
    }

    var close = bar.querySelector(".announce-close");
    if (close) {
      close.addEventListener("click", function () {
        var current = live[index];
        var id = current ? current.getAttribute("data-announce-id") : null;
        if (id) {
          dismissed.push(id);
          saveDismissed(dismissed);
        }
        if (current) current.remove();
        live = live.filter(function (m) { return m !== current; });
        if (!live.length) {
          bar.remove();
          return;
        }
        show(Math.min(index, live.length - 1));
      });
    }

    bar.addEventListener("mouseenter", stop);
    bar.addEventListener("mouseleave", start);
    bar.addEventListener("focusin", stop);
    bar.addEventListener("focusout", start);

    bar.hidden = false;
    show(0);
    start();
  })();

  /* ---------------- gallery lightbox ---------------- */
  (function lightbox() {
    var items = Array.prototype.slice.call(document.querySelectorAll(".gallery-item"));
    if (!items.length) return;

    var box = document.createElement("div");
    box.className = "lightbox";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.innerHTML =
      '<button class="lightbox-close" type="button" aria-label="close">×</button>' +
      '<button class="lightbox-nav prev" type="button" aria-label="previous">‹</button>' +
      '<figure class="lightbox-figure"><img alt=""><figcaption class="lightbox-cap"></figcaption>' +
      '<span class="lightbox-count"></span></figure>' +
      '<button class="lightbox-nav next" type="button" aria-label="next">›</button>';
    document.body.appendChild(box);

    var img = box.querySelector("img");
    var cap = box.querySelector(".lightbox-cap");
    var count = box.querySelector(".lightbox-count");
    var close = box.querySelector(".lightbox-close");
    var prev = box.querySelector(".lightbox-nav.prev");
    var next = box.querySelector(".lightbox-nav.next");
    var current = -1;
    var lastFocus = null;

    function open(i) {
      current = (i + items.length) % items.length;
      var item = items[current];
      img.src = item.getAttribute("data-full") || "";
      img.alt = item.getAttribute("data-caption") || "";
      cap.textContent = item.getAttribute("data-caption") || "";
      cap.hidden = !cap.textContent;
      count.textContent = items.length > 1 ? current + 1 + " / " + items.length : "";
      box.classList.add("open");
      document.body.style.overflow = "hidden";
      close.focus();
    }

    function shut() {
      box.classList.remove("open");
      document.body.style.overflow = "";
      img.removeAttribute("src");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    items.forEach(function (item, i) {
      item.addEventListener("click", function () {
        lastFocus = item;
        open(i);
      });
    });

    close.addEventListener("click", shut);
    prev.addEventListener("click", function () { open(current - 1); });
    next.addEventListener("click", function () { open(current + 1); });

    box.addEventListener("click", function (e) {
      if (e.target === box) shut();
    });

    document.addEventListener("keydown", function (e) {
      if (!box.classList.contains("open")) return;
      if (e.key === "Escape") shut();
      else if (e.key === "ArrowRight") open(current + 1);
      else if (e.key === "ArrowLeft") open(current - 1);
    });
  })();
});
