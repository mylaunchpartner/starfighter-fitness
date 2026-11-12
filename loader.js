/* GHL loader: keeps the page in sync with this repo.
   The GHL snippet wraps a static copy of embed.html (or data-file) in <div id="sf-fit-root" data-v="N">.
   If version.json here has a different v, the latest embed.html replaces it. */
(function () {
  var s = document.currentScript;
  if (!s) return;
  var root = document.getElementById(s.getAttribute("data-root"));
  if (!root || root.getAttribute("data-sf-loader") === "1") return;
  root.setAttribute("data-sf-loader", "1");
  var base = s.src.replace(/[^\/]*(\?.*)?$/, "");
  var file = s.getAttribute("data-file") || "embed.html";
  var key = s.getAttribute("data-vkey") || "v";
  var bucket = Math.floor(Date.now() / 300000); /* re-check every 5 minutes */
  fetch(base + "version.json?b=" + bucket, { cache: "no-store" })
    .then(function (r) { return r.json(); })
    .then(function (j) {
      var v = j[key];
      if (v === undefined || String(v) === root.getAttribute("data-v")) return;
      return fetch(base + file + "?v=" + v).then(function (r) { return r.text(); }).then(function (html) {
        root.innerHTML = html;
        root.setAttribute("data-v", String(v));
        var olds = root.querySelectorAll("script");
        for (var i = 0; i < olds.length; i++) {
          var o = olds[i], n = document.createElement("script");
          for (var k = 0; k < o.attributes.length; k++) n.setAttribute(o.attributes[k].name, o.attributes[k].value);
          n.text = o.text;
          o.parentNode.replaceChild(n, o);
        }
      });
    })
    .catch(function () {});
})();
