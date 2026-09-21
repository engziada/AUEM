// Close mobile nav when a link is clicked; mark current year.
document.addEventListener("DOMContentLoaded", function () {
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
});
