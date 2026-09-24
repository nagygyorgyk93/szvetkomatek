/* Szvetkó matek — interaktív ábrák (közös modul).
 *
 * A `tananyag_common.svg_interaktiv()` által generált `.interaktiv` blokkokat kelti életre.
 * A statikus SVG maga az első képkocka (JS nélkül is értelmes); ez a szkript csak a
 * `.iv-*` osztályú elemek attribútumait frissíti a csúszka mozgatásakor.
 *
 * Módok (data-mod):
 *   szelo  — rögzített P(x0; f(x0)), a csúszka Δx-et állítja: Q pont, szelő, Δy/Δx
 *   erinto — a csúszka x0-t mozgatja: érintő, f'(x0) előjele (és ha data-f2="1", f''(x0) előjele)
 * A függvény polinom: data-poly="a0,a1,a2,…" (a0 + a1·x + a2·x² + …) — nincs eval.
 * Koordináták: data-xr="x0,x1", data-yr="y0,y1", data-w, data-h (a svg_fuggvenyek() margóival).
 */
(function () {
  "use strict";
  if (window.__szvetkoInteraktiv) return;
  window.__szvetkoInteraktiv = true;

  var BAL = 26, JOBB = 12, FENT = 14, LENT = 22;
  var ZOLD = "#047857", PIROS = "#dc2626", SZURKE = "#64748b";

  function szamok(s) {
    return String(s || "").split(",").map(function (t) { return parseFloat(t); });
  }
  function ertek(a, x) {                     // Horner
    var v = 0;
    for (var i = a.length - 1; i >= 0; i--) v = v * x + a[i];
    return v;
  }
  function derival(a) {
    var d = [];
    for (var i = 1; i < a.length; i++) d.push(i * a[i]);
    return d.length ? d : [0];
  }
  function fmt(v) {                          // magyar tizedesvessző, U+2212 mínusz
    if (!isFinite(v)) return "—";
    var r = Math.round(v * 100) / 100;
    if (Math.abs(r) < 0.005) r = 0;
    var s = Math.abs(r - Math.round(r)) < 1e-9 ? String(Math.round(r)) : r.toFixed(2);
    return s.replace(".", ",").replace("-", "−");
  }

  function indit(doboz) {
    var mod = doboz.getAttribute("data-mod");
    var a = szamok(doboz.getAttribute("data-poly"));
    var d1 = derival(a), d2 = derival(d1);
    var xr = szamok(doboz.getAttribute("data-xr")), yr = szamok(doboz.getAttribute("data-yr"));
    var w = parseFloat(doboz.getAttribute("data-w")), h = parseFloat(doboz.getAttribute("data-h"));
    var x0fix = parseFloat(doboz.getAttribute("data-x0"));
    var f2 = doboz.getAttribute("data-f2") === "1";
    var px = w - BAL - JOBB, py = h - FENT - LENT;
    function X(x) { return BAL + (x - xr[0]) / (xr[1] - xr[0]) * px; }
    function Y(y) { return FENT + (yr[1] - y) / (yr[1] - yr[0]) * py; }

    var csuszka = doboz.querySelector("input[type=range]");
    var kiir = doboz.querySelector(".iv-ertek");
    var kijelzo = doboz.querySelector(".iv-kijelzo");
    var egyenes = doboz.querySelector(".iv-egyenes");
    var pP = doboz.querySelector(".iv-P"), pQ = doboz.querySelector(".iv-Q");
    var lQ = doboz.querySelector(".iv-Q-cimke");
    if (!csuszka || !egyenes || !pP) return;

    function vonal(xa, ya, m, szin) {        // egyenes (xa;ya)-n át, m meredekséggel, a teljes szélességben
      egyenes.setAttribute("x1", X(xr[0]).toFixed(1));
      egyenes.setAttribute("y1", Y(ya + m * (xr[0] - xa)).toFixed(1));
      egyenes.setAttribute("x2", X(xr[1]).toFixed(1));
      egyenes.setAttribute("y2", Y(ya + m * (xr[1] - xa)).toFixed(1));
      if (szin) egyenes.setAttribute("stroke", szin);
    }
    function pont(el, x, y) {
      el.setAttribute("cx", X(x).toFixed(1));
      el.setAttribute("cy", Y(y).toFixed(1));
    }

    function frissit() {
      var v = parseFloat(csuszka.value);
      if (mod === "szelo") {
        var yP = ertek(a, x0fix);
        pont(pP, x0fix, yP);
        if (Math.abs(v) < 0.005) {           // Δx = 0: nincs szelő, csak az érintő
          var m0 = ertek(d1, x0fix);
          vonal(x0fix, yP, m0, ZOLD);
          if (pQ) pQ.setAttribute("visibility", "hidden");
          if (lQ) lQ.setAttribute("visibility", "hidden");
          kiir.textContent = "0";
          kijelzo.textContent = "Δx = 0: két pont helyett egy maradt — ez már nem szelő. A szelők meredeksége "
            + "az érintő meredekségéhez tart: f′(" + fmt(x0fix) + ") = " + fmt(m0) + ".";
          return;
        }
        var xQ = x0fix + v, yQ = ertek(a, xQ);
        var m = (yQ - yP) / v;
        vonal(x0fix, yP, m, "#2563eb");
        if (pQ) { pQ.setAttribute("visibility", "visible"); pont(pQ, xQ, yQ); }
        if (lQ) {
          lQ.setAttribute("visibility", "visible");
          lQ.setAttribute("x", (X(xQ) + 7).toFixed(1));
          lQ.setAttribute("y", (Y(yQ) - 7).toFixed(1));
        }
        kiir.textContent = fmt(v);
        kijelzo.textContent = "Δx = " + fmt(v) + ",  Δy = " + fmt(yQ - yP) + ",  a szelő meredeksége Δy/Δx = "
          + fmt(m) + ".";
      } else {                                // erinto
        var y0 = ertek(a, v), m1 = ertek(d1, v), m2 = ertek(d2, v);
        var szin = m1 > 0.01 ? ZOLD : (m1 < -0.01 ? PIROS : SZURKE);
        vonal(v, y0, m1, szin);
        pont(pP, v, y0);
        kiir.textContent = fmt(v);
        var monoton = m1 > 0.01 ? "pozitív → itt a függvény nő" :
          (m1 < -0.01 ? "negatív → itt a függvény csökken" : "0 → vízszintes érintő (stacionárius hely)");
        var szoveg = "x₀ = " + fmt(v) + ":  f′(x₀) = " + fmt(m1) + ", " + monoton + ".";
        if (f2) {
          var gorb = m2 > 0.01 ? "pozitív → konvex (∪), a görbe az érintő fölött van" :
            (m2 < -0.01 ? "negatív → konkáv (∩), a görbe az érintő alatt van" : "0 → itt válthat a görbülés (inflexió?)");
          szoveg += "  f″(x₀) = " + fmt(m2) + ", " + gorb + ".";
        }
        kijelzo.textContent = szoveg;
      }
    }
    csuszka.addEventListener("input", frissit);
    frissit();
  }

  function mind() {
    var dobozok = document.querySelectorAll(".interaktiv[data-mod]");
    for (var i = 0; i < dobozok.length; i++) indit(dobozok[i]);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mind);
  else mind();
})();
