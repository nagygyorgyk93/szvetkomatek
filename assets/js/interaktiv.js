/* Szvetkó matek — interaktív ábrák (közös modul).
 *
 * A `tananyag_common.svg_interaktiv()` által generált `.interaktiv` blokkokat kelti életre.
 * A statikus SVG maga az első képkocka (JS nélkül is értelmes); ez a szkript csak a
 * `.iv-*` osztályú elemek attribútumait frissíti a csúszka mozgatásakor.
 *
 * Módok (data-mod):
 *   szelo  — rögzített P(x0; f(x0)), a csúszka Δx-et állítja: Q pont, szelő, Δy/Δx
 *   erinto — a csúszka x0-t mozgatja: érintő, f'(x0) előjele (és ha data-f2="1", f''(x0) előjele)
 *   sereg  — a polinom egy F primitív függvény, a csúszka a C-t állítja: F+C görbéje, érintő az x0-ban
 *            (a meredekség nem függ C-től)
 *   osszeg — a polinom az f, a data-ab="a,b" intervallumon n téglalapos alsó és felső közelítő összeg;
 *            data-pontos = a pontos terület szövege
 *   pascal — Pascal-háromszög (tananyag_common.svg_pascal): a csúszka az n-edik sort (.iv-psor[data-n])
 *            emeli ki; kijelző: (a + b)^n kifejtése és a sorösszeg 2^n (2026-09-26)
 *   szimulacio — érme- és kockaszimulátor (abra_stat.svg_szimulacio, 2026-09-29): „+1 … +1000 dobás” gombok,
 *            a relatív gyakoriság vonaldiagramja és a klasszikus valószínűség szaggatott vonala; data-sor = a
 *            beégetett kezdő sorozat (a statikus kép), innen folytatja
 *   adatlabor  — leíró statisztika (abra_stat.svg_adatlabor, 2026-09-29): adatsor-választó + szövegmező, élő
 *            mutatók (a kvartilis az alsó és a felső fél mediánja; 1/n-es szórásnégyzet — ugyanúgy, mint a
 *            Python-oldali abra_stat.mutatok), pont- és dobozdiagram
 *   homotecia — a meglévő háromszög képe: k előjele, |k|, hossz- és területarány
 *   exponencialis — az aˣ alapgrafikonja, külön 0 < a < 1 és a > 1 tartománnyal
 *   sorozat — aₙ = 2 + 1/n, nyílt ε-sáv és látható tagszám; a sávhatár egész számokkal ellenőrizve
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
    var s = Math.abs(r - Math.round(r)) < 1e-9 ? String(Math.round(r)) : r.toFixed(2).replace(/0+$/, "");
    return s.replace(".", ",").replace("-", "−");
  }

  var FELSO = "⁰¹²³⁴⁵⁶⁷⁸⁹";
  function felso(n) {
    return String(n).split("").map(function (c) { return FELSO.charAt(+c); }).join("");
  }
  function binom(n, k) {
    var r = 1;
    for (var i = 1; i <= k; i++) r = r * (n - k + i) / i;
    return Math.round(r);
  }
  function kifejtes(n) {                     // (a + b)^n — ugyanaz, mint a tananyag_common.pascal_kifejtes()
    var tagok = [];
    for (var k = 0; k <= n; k++) {
      var c = binom(n, k), ea = n - k, eb = k, t = (c === 1 && (ea || eb)) ? "" : String(c);
      if (ea) t += "a" + (ea > 1 ? felso(ea) : "");
      if (eb) t += "b" + (eb > 1 ? felso(eb) : "");
      tagok.push(t);
    }
    return tagok.join(" + ");
  }
  function pascal(doboz) {
    var csuszka = doboz.querySelector("input[type=range]");
    var kiir = doboz.querySelector(".iv-ertek");
    var kijelzo = doboz.querySelector(".iv-kijelzo");
    var sorok = doboz.querySelectorAll(".iv-psor");
    if (!csuszka || !sorok.length) return;
    function frissit() {
      var n = Math.round(parseFloat(csuszka.value));
      for (var i = 0; i < sorok.length; i++) {
        var ki = parseInt(sorok[i].getAttribute("data-n"), 10) === n;
        var kor = sorok[i].querySelectorAll("circle"), szam = sorok[i].querySelectorAll("text");
        for (var j = 0; j < kor.length; j++) {
          kor[j].setAttribute("fill", ki ? "#2563eb" : "#ffffff");
          kor[j].setAttribute("stroke", ki ? "#1d4ed8" : "#94a3b8");
        }
        for (var t = 1; t < szam.length; t++) szam[t].setAttribute("fill", ki ? "#ffffff" : "#0f172a");
      }
      kiir.textContent = String(n);
      kijelzo.textContent = "n = " + n + ":  (a + b)" + felso(n) + " = " + kifejtes(n) + ";  a sor összege "
        + Math.pow(2, n) + " = 2" + felso(n) + ".";
    }
    csuszka.addEventListener("input", frissit);
    frissit();
    return true;
  }


  // ------------------------------------------------------------ közös segédek a statisztikai módokhoz
  var SVGNS = "http://www.w3.org/2000/svg";
  function ezres(n) {                          // 10000 → "10 000" (nem törő szóköz)
    return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }
  function tized(v, j) { return v.toFixed(j).replace(".", ",").replace("-", "−"); }
  function elem(nev, attr) {
    var e = document.createElementNS(SVGNS, nev);
    for (var k in attr) if (Object.prototype.hasOwnProperty.call(attr, k)) e.setAttribute(k, attr[k]);
    return e;
  }
  function urit(g) { while (g && g.firstChild) g.removeChild(g.firstChild); }

  // ------------------------------------------------------------ szimulátor (2026-09-29)
  function szepMax(n) {
    var h = 10;
    for (;;) {
      if (h >= n) return h;
      if (2 * h >= n) return 2 * h;
      if (5 * h >= n) return 5 * h;
      h *= 10;
    }
  }
  function szimulacio(doboz) {
    var gorbe = doboz.querySelector(".iv-szim-gorbe"), cel = doboz.querySelector(".iv-szim-cel");
    var celCimke = doboz.querySelector(".iv-szim-cel-cimke"), xt = doboz.querySelectorAll(".iv-szim-xt");
    var valaszto = doboz.querySelector(".iv-szim-tipus"), kijelzo = doboz.querySelector(".iv-kijelzo");
    var gombok = doboz.querySelectorAll("button[data-db]"), ujra = doboz.querySelector(".iv-szim-ujra");
    if (!gorbe || !cel || !valaszto || !kijelzo) return;
    var W = parseFloat(doboz.getAttribute("data-w")), H = parseFloat(doboz.getAttribute("data-h"));
    var B = 44, J = 14, F = 12, L = 30, px = W - B - J, py = H - F - L, MAXN = 100000;
    var TIP = {
      erme: { p: 0.5, jel: "1/2", siker: "fej", nev: "Érmedobás" },
      kocka: { p: 1 / 6, jel: "1/6", siker: "hatos", nev: "Kockadobás" }
    };
    var tipus = "erme", n = 0, k = 0, rel = [];
    function Y(v) { return F + (1 - v) * py; }
    function dob(db) {
      var p = TIP[tipus].p;
      for (var i = 0; i < db && n < MAXN; i++) { n++; if (Math.random() < p) k++; rel.push(k / n); }
    }
    function rajzol() {
      var t = TIP[tipus], max = szepMax(Math.max(n, 10)), m = Math.min(n, 400), d = [];
      for (var i = 0; i < m; i++) {
        var idx = Math.floor((i + 1) * n / m) - 1;
        d.push((i ? "L" : "M") + (B + (idx + 1) / max * px).toFixed(1) + "," + Y(rel[idx]).toFixed(1));
      }
      gorbe.setAttribute("d", d.join(" "));
      cel.setAttribute("y1", Y(t.p).toFixed(1));
      cel.setAttribute("y2", Y(t.p).toFixed(1));
      if (celCimke) { celCimke.setAttribute("y", (Y(t.p) - 4).toFixed(1)); celCimke.textContent = t.jel; }
      for (var j = 0; j < xt.length; j++) xt[j].textContent = ezres(max * j / (xt.length - 1));
      kijelzo.textContent = n === 0 ? t.nev + ": még nincs dobás. Nyomd meg a gombokat!"
        : t.nev + ": " + ezres(n) + " dobás, ebből " + ezres(k) + " " + t.siker + " — a relatív gyakoriság "
          + ezres(k) + "/" + ezres(n) + " ≈ " + tized(k / n, 3) + ". A klasszikus valószínűség " + t.jel + " ≈ "
          + tized(t.p, 3) + "." + (n >= MAXN ? " (Elértük a " + ezres(MAXN) + " dobást — kezdd újra!)" : "");
    }
    function nullaz() { n = 0; k = 0; rel = []; }
    var sor = doboz.getAttribute("data-sor") || "";
    for (var i = 0; i < sor.length; i++) { n++; if (sor.charAt(i) === "1") k++; rel.push(k / n); }
    valaszto.value = "erme";
    valaszto.addEventListener("change", function () { tipus = valaszto.value in TIP ? valaszto.value : "erme"; nullaz(); rajzol(); });
    for (var g = 0; g < gombok.length; g++) {
      gombok[g].addEventListener("click", function () { dob(parseInt(this.getAttribute("data-db"), 10) || 1); rajzol(); });
    }
    if (ujra) ujra.addEventListener("click", function () { nullaz(); rajzol(); });
    rajzol();
    return true;
  }

  // ------------------------------------------------------------ adatlabor (2026-09-29)
  function median(s) { var n = s.length, f = Math.floor(n / 2); return n % 2 ? s[f] : (s[f - 1] + s[f]) / 2; }
  function mutatok(a) {                        // = abra_stat.mutatok (Python)
    var s = a.slice().sort(function (x, y) { return x - y; }), n = s.length, h = Math.floor(n / 2);
    var ossz = 0, i;
    for (i = 0; i < n; i++) ossz += s[i];
    var atl = ossz / n, also = s.slice(0, h), felso = n % 2 ? s.slice(h + 1) : s.slice(h);
    var aae = 0, vr = 0, gy = {}, maxgy = 0;
    for (i = 0; i < n; i++) {
      aae += Math.abs(s[i] - atl); vr += (s[i] - atl) * (s[i] - atl);
      var kk = String(s[i]); gy[kk] = (gy[kk] || 0) + 1; if (gy[kk] > maxgy) maxgy = gy[kk];
    }
    var mod = [];
    if (maxgy > 1) for (var kulcs in gy) if (gy[kulcs] === maxgy) mod.push(parseFloat(kulcs));
    mod.sort(function (x, y) { return x - y; });
    return { n: n, s: s, atlag: atl, median: median(s), q1: also.length ? median(also) : s[0],
      q3: felso.length ? median(felso) : s[n - 1], min: s[0], max: s[n - 1], aae: aae / n, vr: vr / n,
      sz: Math.sqrt(vr / n), mod: mod, modgy: maxgy };
  }
  function szamsor(szoveg) {
    var ki = [], rossz = 0, reszek = String(szoveg || "").replace(/−/g, "-").split(/[\s;]+/);
    for (var i = 0; i < reszek.length; i++) {
      var t = reszek[i].replace(/^,+|,+$/g, "");
      if (!t) continue;
      if (/^-?\d+([.,]\d+)?$/.test(t)) ki.push(parseFloat(t.replace(",", "."))); else rossz++;
    }
    return { adat: ki, rossz: rossz };
  }
  function tengelyX(lo, hi) {
    if (hi - lo < 1e-9) { lo -= 1; hi += 1; }
    var nyers = (hi - lo) / 6, mag = Math.pow(10, Math.floor(Math.log(nyers) / Math.LN10)), lep = 10 * mag;
    var szorzok = [1, 2, 5, 10];
    for (var i = 0; i < szorzok.length; i++) if (szorzok[i] * mag >= nyers) { lep = szorzok[i] * mag; break; }
    return [Math.floor(lo / lep) * lep, Math.ceil(hi / lep) * lep, lep];
  }
  function adatlabor(doboz) {
    var valaszto = doboz.querySelector(".iv-al-valaszt"), mezo = doboz.querySelector(".iv-al-adat");
    var kijelzo = doboz.querySelector(".iv-kijelzo"), cim = doboz.querySelector(".iv-tabla caption");
    var pontok = doboz.querySelector(".iv-al-pontok"), tengely = doboz.querySelector(".iv-al-tengely");
    if (!valaszto || !mezo || !pontok || !tengely) return;
    var W = parseFloat(doboz.getAttribute("data-w")), BAL2 = 20, JOBB2 = 20, px2 = W - BAL2 - JOBB2, CY = 96;
    var ALAP = "Kék pontok: az adatok · doboz: Q₁–Q₃, benne a medián · piros szaggatott vonal: az átlag.";
    function cella(k, v) { var c = doboz.querySelector('td[data-m="' + k + '"]'); if (c) c.textContent = v; }
    function vonal(sel, x1, y1, x2, y2) {
      var e = doboz.querySelector(sel);
      if (!e) return;
      e.setAttribute("x1", x1.toFixed(1)); e.setAttribute("y1", y1); e.setAttribute("x2", x2.toFixed(1)); e.setAttribute("y2", y2);
      e.setAttribute("visibility", "visible");
    }
    function frissit() {
      var p = szamsor(mezo.value), a = p.adat;
      if (!a.length) {
        urit(pontok); urit(tengely);
        var rejt = [".iv-al-bajusz1", ".iv-al-bajusz2", ".iv-al-min", ".iv-al-max", ".iv-al-doboz", ".iv-al-me", ".iv-al-atl"];
        for (var r = 0; r < rejt.length; r++) { var e = doboz.querySelector(rejt[r]); if (e) e.setAttribute("visibility", "hidden"); }
        var tdk = doboz.querySelectorAll("td[data-m]");
        for (var q = 0; q < tdk.length; q++) tdk[q].textContent = "—";
        kijelzo.textContent = "Írj be legalább egy számot!";
        return;
      }
      var m = mutatok(a), t = tengelyX(m.min, m.max), lo = t[0], hi = t[1], lep = t[2];
      function X(v) { return BAL2 + (v - lo) / (hi - lo) * px2; }
      urit(pontok); urit(tengely);
      var db = {}, maxst = 0, i;
      for (i = 0; i < m.s.length; i++) { var kk = String(m.s[i]); db[kk] = (db[kk] || 0) + 1; if (db[kk] > maxst) maxst = db[kk]; }
      var koz = Math.min(8, 52 / maxst), hanyadik = {};
      for (i = 0; i < m.s.length; i++) {
        var kl = String(m.s[i]), j = hanyadik[kl] || 0; hanyadik[kl] = j + 1;
        pontok.appendChild(elem("circle", { cx: X(m.s[i]).toFixed(1), cy: (66 - j * koz).toFixed(1), r: 4,
          fill: "#1d4ed8", "fill-opacity": ".7" }));
      }
      for (var v = lo; v <= hi + 1e-9; v += lep) {
        tengely.appendChild(elem("line", { x1: X(v).toFixed(1), y1: 118, x2: X(v).toFixed(1), y2: 122, stroke: "#0f172a" }));
        var tx = elem("text", { x: X(v).toFixed(1), y: 136, "font-size": "10.5", fill: "#475569", "text-anchor": "middle" });
        tx.textContent = fmt(v); tengely.appendChild(tx);
      }
      vonal(".iv-al-bajusz1", X(m.min), CY, X(m.q1), CY);
      vonal(".iv-al-bajusz2", X(m.q3), CY, X(m.max), CY);
      vonal(".iv-al-min", X(m.min), CY - 7, X(m.min), CY + 7);
      vonal(".iv-al-max", X(m.max), CY - 7, X(m.max), CY + 7);
      vonal(".iv-al-me", X(m.median), CY - 11, X(m.median), CY + 11);
      vonal(".iv-al-atl", X(m.atlag), CY - 15, X(m.atlag), CY + 15);
      var dz = doboz.querySelector(".iv-al-doboz");
      if (dz) {
        dz.setAttribute("x", X(m.q1).toFixed(1)); dz.setAttribute("width", (X(m.q3) - X(m.q1)).toFixed(1));
        dz.setAttribute("visibility", "visible");
      }
      cella("n", String(m.n)); cella("atlag", fmt(m.atlag)); cella("median", fmt(m.median));
      cella("modusz", m.mod.length ? m.mod.map(fmt).join("; ") + " (" + m.modgy + "-szer)" : "nincs (minden érték egyszer fordul elő)");
      cella("terjedelem", fmt(m.max - m.min)); cella("q1", fmt(m.q1)); cella("q3", fmt(m.q3));
      cella("iqr", fmt(m.q3 - m.q1)); cella("aae", fmt(m.aae)); cella("var", fmt(m.vr)); cella("sz", fmt(m.sz));
      kijelzo.textContent = p.rossz ? ALAP + " (" + p.rossz + " nem szám jellegű részt kihagytam.)" : ALAP;
    }
    function betolt() {
      var o = valaszto.options[valaszto.selectedIndex];
      var e = (o && o.getAttribute("data-ertekek")) || "";
      if (cim && o) cim.textContent = o.textContent;
      if (e) mezo.value = e.split(",").map(function (s) { return fmt(parseFloat(s)); }).join("; ");
      else if (valaszto.value === "sajat") { mezo.value = ""; mezo.focus(); }
      frissit();
    }
    valaszto.addEventListener("change", betolt);
    mezo.addEventListener("input", function () {
      if (valaszto.value !== "sajat") { valaszto.value = "sajat"; if (cim) cim.textContent = "saját adatok"; }
      frissit();
    });
    frissit();
    return true;
  }

  // ------------------------------------------------------------ az I1 első három szemléltetése
  function pontosFmt(v) {                    // a negyedes arány négyzete is pontosan kiírható
    return v.toFixed(4).replace(/\.?0+$/, "").replace(".", ",").replace("-", "−");
  }
  function visszaallit(doboz, alap) {
    var gomb = doboz.querySelector(".iv-alaphelyzet");
    if (gomb) gomb.addEventListener("click", alap);
  }
  function homotecia(doboz) {
    var arany = doboz.querySelector(".iv-homo-arany"), oldal = doboz.querySelector(".iv-homo-oldal");
    var svg = doboz.querySelector("svg"), eredeti = doboz.querySelector(".iv-homo-eredeti");
    var kep = doboz.querySelector(".iv-homo-kep"), O = doboz.querySelector(".iv-homo-O");
    var A1 = doboz.querySelector(".iv-homo-A1-pont"), cim = doboz.querySelector(".iv-homo-A1");
    var Acim = doboz.querySelector(".iv-homo-A"), kiir = doboz.querySelector(".iv-homo-ertek");
    var kijelzo = doboz.querySelector(".iv-kijelzo");
    if (!(arany && oldal && svg && eredeti && kep && O && A1 && cim && Acim && kiir && kijelzo)) return;
    var ox = Number(O.getAttribute("cx")), oy = Number(O.getAttribute("cy"));
    var pontok = eredeti.getAttribute("points").trim().split(/\s+/).map(szamok);
    function frissit() {
      var meret = Number(arany.value), k = meret * Number(oldal.value);
      var kepPontok = pontok.map(function (p) { return [ox + k * (p[0] - ox), oy + k * (p[1] - oy)]; });
      kep.setAttribute("points", kepPontok.map(function (p) { return p[0].toFixed(2) + "," + p[1].toFixed(2); }).join(" "));
      A1.setAttribute("cx", kepPontok[0][0].toFixed(2)); A1.setAttribute("cy", kepPontok[0][1].toFixed(2));
      cim.setAttribute("x", (kepPontok[0][0] + 7).toFixed(2)); cim.setAttribute("y", (kepPontok[0][1] - 9).toFixed(2));
      cim.textContent = k === 1 ? "A = A₁" : "A₁";
      Acim.setAttribute("visibility", k === 1 ? "hidden" : "visible");
      kiir.textContent = pontosFmt(meret);
      arany.setAttribute("aria-valuetext", "Az arány nagysága: " + pontosFmt(meret));
      var hely = k > 0 ? "azonos" : "ellenkező";
      kijelzo.textContent = "A homotécia aránya " + pontosFmt(k) + ". A képpontok a középpontból induló " + hely
        + " félegyenesre kerülnek. A megfelelő oldalak és a kerületek aránya " + pontosFmt(meret)
        + ", a területek aránya " + pontosFmt(k * k) + "."
        + (k === 1 ? " Minden pont a helyén marad: a két háromszög egybeesik." : (k === -1 ? " Középpontos tükrözés; a méret megmarad." : ""));
      svg.setAttribute("aria-label", "Az O középpontú, k = " + pontosFmt(k) + " arányú homotécia: F és F₁");
    }
    arany.addEventListener("input", frissit); oldal.addEventListener("change", frissit);
    visszaallit(doboz, function () { oldal.value = "1"; arany.value = arany.defaultValue; frissit(); });
    frissit(); return true;
  }
  function exponencialis(doboz) {
    var alap = doboz.querySelector(".iv-exp-alap"), tipus = doboz.querySelector(".iv-exp-tipus");
    var gorbe = doboz.querySelector(".iv-exp-gorbe"), cim = doboz.querySelector(".iv-exp-cimke");
    var kiir = doboz.querySelector(".iv-exp-ertek"), kijelzo = doboz.querySelector(".iv-kijelzo");
    var svg = doboz.querySelector("svg");
    if (!(alap && tipus && gorbe && cim && kiir && kijelzo && svg)) return;
    var xr = szamok(doboz.getAttribute("data-xr")), yr = szamok(doboz.getAttribute("data-yr"));
    var w = Number(doboz.getAttribute("data-w")), h = Number(doboz.getAttribute("data-h"));
    function X(x) { return BAL + (x - xr[0]) / (xr[1] - xr[0]) * (w - BAL - JOBB); }
    function Y(y) { return FENT + (yr[1] - y) / (yr[1] - yr[0]) * (h - FENT - LENT); }
    function frissit() {
      var a = Number(alap.value) / 100, lo = xr[0], hi = xr[1], d = [];
      var felsoX = Math.log(yr[1]) / Math.log(a);
      if (a > 1) hi = Math.min(hi, felsoX); else lo = Math.max(lo, felsoX);
      for (var i = 0; i <= 160; i++) {
        var x = lo + (hi - lo) * i / 160;
        d.push((i ? "L" : "M") + X(x).toFixed(2) + "," + Y(Math.pow(a, x)).toFixed(2));
      }
      gorbe.setAttribute("d", d.join(" ")); gorbe.setAttribute("stroke", a > 1 ? "#047857" : "#dc2626");
      cim.textContent = "y = " + (a < 1 ? "(" + pontosFmt(a) + ")" : pontosFmt(a)) + "ˣ";
      kiir.textContent = pontosFmt(a); alap.setAttribute("aria-valuetext", "Az exponenciális függvény alapja: " + pontosFmt(a));
      kijelzo.textContent = "Az alap " + pontosFmt(a) + ": a függvény szigorúan " + (a > 1 ? "növekvő" : "csökkenő")
        + ". Az értéke −1-nél közelítőleg " + pontosFmt(1 / a) + "; 0-nál 1; 1-nél " + pontosFmt(a) + ".";
      svg.setAttribute("aria-label", "Az y = aˣ exponenciális függvény alapgrafikonja, a = " + pontosFmt(a));
    }
    function tartomany() {
      var no = tipus.value === "no";
      alap.min = no ? "101" : "10"; alap.max = no ? "500" : "99";
      alap.value = no ? "200" : "50";
      frissit();
    }
    alap.addEventListener("input", frissit); tipus.addEventListener("change", tartomany);
    visszaallit(doboz, function () { tipus.value = "no"; tartomany(); });
    frissit(); return true;
  }
  function sorozat(doboz) {
    var szelesseg = doboz.querySelector(".iv-sor-szelesseg"), tagszam = doboz.querySelector(".iv-sor-tagszam");
    var sav = doboz.querySelector(".iv-sor-sav"), also = doboz.querySelector(".iv-sor-also"), felso = doboz.querySelector(".iv-sor-felso");
    var pontok = doboz.querySelector(".iv-sor-pontok"), racs = doboz.querySelector(".iv-sor-racs"), tengely = doboz.querySelector(".iv-sor-tengely");
    var kiEps = doboz.querySelector(".iv-sor-eps"), kiDb = doboz.querySelector(".iv-sor-db"), kijelzo = doboz.querySelector(".iv-kijelzo");
    var svg = doboz.querySelector("svg");
    if (!(szelesseg && tagszam && sav && also && felso && pontok && racs && tengely && kiEps && kiDb && kijelzo && svg)) return;
    var w = Number(doboz.getAttribute("data-w")), h = Number(doboz.getAttribute("data-h"));
    var yr = szamok(doboz.getAttribute("data-yr")), px = w - BAL - JOBB, py = h - FENT - LENT;
    function Y(y) { return FENT + (yr[1] - y) / (yr[1] - yr[0]) * py; }
    function frissit() {
      var szazad = Number(szelesseg.value), eps = szazad / 100, db = Number(tagszam.value);
      var elso = Math.floor(100 / szazad) + 1, belul = 0, hataron = 0, kivul = 0;
      function X(n) { return BAL + n / (db + 1) * px; }
      sav.setAttribute("y", Y(2 + eps).toFixed(2)); sav.setAttribute("height", (Y(2 - eps) - Y(2 + eps)).toFixed(2));
      also.setAttribute("y1", Y(2 - eps).toFixed(2)); also.setAttribute("y2", Y(2 - eps).toFixed(2));
      felso.setAttribute("y1", Y(2 + eps).toFixed(2)); felso.setAttribute("y2", Y(2 + eps).toFixed(2));
      urit(pontok); urit(racs); urit(tengely);
      for (var n = 1; n <= db; n++) {
        // 1/n < ε pontosan akkor, ha n · ε_század > 100: a határ nem kerekítési döntés.
        var hely = n * szazad > 100 ? "belul" : (n * szazad === 100 ? "hatar" : "kivul");
        if (hely === "belul") belul++; else if (hely === "hatar") hataron++; else kivul++;
        pontok.appendChild(elem("circle", { "data-n": n, "data-hely": hely,
          cx: X(n).toFixed(2), cy: Y(2 + 1 / n).toFixed(2), r: db > 35 ? "2.5" : "4",
          fill: hely === "hatar" ? "#ffffff" : (hely === "belul" ? "#047857" : "#dc2626"),
          stroke: hely === "hatar" ? "#b45309" : "none", "stroke-width": "2" }));
      }
      for (var y = 1; y <= 3; y++) racs.appendChild(elem("line", {x1: BAL, y1: Y(y), x2: w - JOBB, y2: Y(y), stroke: "#cbd5e1", "stroke-width": ".6"}));
      var lepes = Math.ceil(db / 6);
      for (var t = lepes; t <= db; t += lepes) {
        racs.appendChild(elem("line", {x1: X(t), y1: FENT, x2: X(t), y2: Y(0), stroke: "#cbd5e1", "stroke-width": ".6"}));
        var cim = elem("text", {x: X(t), y: Y(0) + 14, "font-size": "11", fill: "#475569", "text-anchor": "middle"});
        cim.textContent = String(t); tengely.appendChild(cim);
      }
      kiEps.textContent = pontosFmt(eps); kiDb.textContent = String(db);
      szelesseg.setAttribute("aria-valuetext", "A sáv félszélessége: " + pontosFmt(eps));
      kijelzo.textContent = "A sáv félszélessége " + pontosFmt(eps) + ": a nyílt sáv " + pontosFmt(2 - eps) + " és " + pontosFmt(2 + eps)
        + " között van. A " + elso + ". tagtól kezdve minden további tag benne van. Az első " + db + " tagból "
        + belul + " belül, " + (kivul + hataron) + " kívül van; " + (hataron ? "a " + (100 / szazad) + ". tag a határra esik, ezért kívül marad." : "határra eső tag nincs.")
        + (!belul ? " Növeld a látható tagok számát: a sávba eső tagok még nem látszanak." : "");
      svg.setAttribute("aria-label", "Az aₙ = 2 + 1/n sorozat első " + db + " tagja, a 2 körüli nyílt sáv félszélessége " + pontosFmt(eps));
    }
    szelesseg.addEventListener("input", frissit); tagszam.addEventListener("input", frissit);
    visszaallit(doboz, function () { szelesseg.value = szelesseg.defaultValue; tagszam.value = tagszam.defaultValue; frissit(); });
    frissit(); return true;
  }

  function indit(doboz) {
    var mod = doboz.getAttribute("data-mod");
    if (mod === "pascal") return pascal(doboz);
    if (mod === "szimulacio") return szimulacio(doboz);
    if (mod === "adatlabor") return adatlabor(doboz);
    if (mod === "homotecia") return homotecia(doboz);
    if (mod === "exponencialis") return exponencialis(doboz);
    if (mod === "sorozat") return sorozat(doboz);
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
    var gorbe = doboz.querySelector(".iv-gorbe");
    var also = doboz.querySelector(".iv-also"), felso = doboz.querySelector(".iv-felso");
    var ab = szamok(doboz.getAttribute("data-ab"));
    var pontos = doboz.getAttribute("data-pontos") || "";
    if (!csuszka) return;
    if (mod === "osszeg" ? !(also && felso) : !(egyenes && pP)) return;

    function ut(C) {                          // F + C görbéje; a rajzterületből kilógó részeknél megszakad
      var d = [], le = true, n = 160;
      for (var i = 0; i <= n; i++) {
        var xx = xr[0] + (xr[1] - xr[0]) * i / n, yy = ertek(a, xx) + C;
        if (yy >= yr[0] - 0.5 && yy <= yr[1] + 0.5) {
          d.push((le ? "M" : "L") + X(xx).toFixed(1) + "," + Y(yy).toFixed(1)); le = false;
        } else le = true;
      }
      return d.join(" ");
    }
    function teglak(n) {                      // alsó és felső téglalapok (szakaszonként monoton f)
      var lo = [], hi = [], sl = 0, sh = 0, dx = (ab[1] - ab[0]) / n;
      for (var i = 0; i < n; i++) {
        var xl = ab[0] + i * dx, xq = xl + dx, fl = ertek(a, xl), fr = ertek(a, xq);
        var m = Math.min(fl, fr), M = Math.max(fl, fr);
        sl += m * dx; sh += M * dx;
        lo.push("M" + X(xl).toFixed(1) + "," + Y(0).toFixed(1) + " V" + Y(m).toFixed(1) + " H" + X(xq).toFixed(1)
          + " V" + Y(0).toFixed(1) + " Z");
        hi.push("M" + X(xl).toFixed(1) + "," + Y(0).toFixed(1) + " V" + Y(M).toFixed(1) + " H" + X(xq).toFixed(1)
          + " V" + Y(0).toFixed(1) + " Z");
      }
      return [lo.join(" "), hi.join(" "), sl, sh];
    }

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
      if (mod === "sereg") {
        var m = ertek(d1, x0fix), y = ertek(a, x0fix) + v;
        if (gorbe) gorbe.setAttribute("d", ut(v));
        vonal(x0fix, y, m, ZOLD);
        pont(pP, x0fix, y);
        kiir.textContent = fmt(v);
        kijelzo.textContent = "C = " + fmt(v) + ":  az x₀ = " + fmt(x0fix) + " helyen az érintő meredeksége "
          + fmt(m) + " — minden C-re ugyanannyi, mert (F + C)′ = F′ = f.";
        return;
      }
      if (mod === "osszeg") {
        var n = Math.max(1, Math.round(v)), r = teglak(n);
        also.setAttribute("d", r[0]); felso.setAttribute("d", r[1]);
        kiir.textContent = String(n);
        kijelzo.textContent = "n = " + n + ":  alsó összeg ≈ " + fmt(r[2]) + ",  felső összeg ≈ " + fmt(r[3])
          + ";  a pontos terület: " + pontos + ".";
        return;
      }
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
    return true;
  }

  function mind() {
    var dobozok = document.querySelectorAll(".interaktiv[data-mod]");
    for (var i = 0; i < dobozok.length; i++) {
      if (indit(dobozok[i])) dobozok[i].classList.add("iv-kesz");
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mind);
  else mind();
})();
