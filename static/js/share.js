/* Zero-tracking share helpers: copy-link + native share sheet only.
   No network calls, no storage, no analytics. */
(function () {
  "use strict";

  // Native share (mobile) — shown only when the browser supports it.
  var nativeBtns = document.querySelectorAll(".sl-share-btn.native");
  if (navigator.share) {
    nativeBtns.forEach(function (btn) {
      btn.classList.add("supported");
      btn.addEventListener("click", function () {
        navigator.share({
          title: btn.getAttribute("data-share-title") || document.title,
          url: btn.getAttribute("data-share-url") || location.href
        }).catch(function () {});
      });
    });
  }

  // Copy link — for Instagram / TikTok / anything without a web share intent.
  var copyBtns = document.querySelectorAll(".sl-share-btn.copy");
  copyBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var url = btn.getAttribute("data-copy-url") || location.href;
      function done() {
        var label = btn.querySelector("span.sl-copy-ok");
        if (!label) {
          label = document.createElement("span");
          label.className = "sl-copy-ok";
          label.textContent = "Link copied";
          btn.appendChild(label);
        }
        btn.classList.add("copied");
        setTimeout(function () {
          btn.classList.remove("copied");
          if (label && label.parentNode) label.parentNode.removeChild(label);
        }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done, function () { fallbackCopy(url); done(); });
      } else {
        fallbackCopy(url);
        done();
      }
    });
  });

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta);
  }
})();
