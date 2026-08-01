/* Szvetkó matek — KÜLDETÉSNAPLÓ (haladáskövetés)
   ------------------------------------------------------------------
   A kadét haladása a böngésző localStorage-ában él (nincs szerver, nincs
   adatgyűjtés). Ez a szkript minden oldalon fut (az ui.js tölti be), és
   JS-ből injektálja a felületet — a HTML-oldalakat nem kell módosítani:
     · fejléc-chip (rang + XP)                → minden oldal
     · „Egység teljesítve” gomb + auto-jelölés → tananyag / összefoglaló / terepküldetés
     · „megoldva” pipa a feladatkártyákon      → feladatgyűjtemények
     · kvíz-találat rögzítése                  → a quiz.js `kviz-helyes` eseményéből
     · haladás-gyűrű a kártyákon               → index-oldalak
   A jutalom-pillanatokat a `szvetko-jutalom` esemény jelzi (effekt.js figyeli).
   Nyilvános API: window.Naplo (a kuldetesnaplo.html használja). */
(function () {
  'use strict';

  var ROOT   = document.documentElement.getAttribute('data-root') || '.';
  var KULCS  = 'szvetko-naplo-v1';
  var PONT   = { oldal: 10, kviz: 5, feladat: 2, projekt: 30 };
  var RANGOK = [
    { tol: 0,    nev: 'Újonc',       jel: '🔰' },
    { tol: 150,  nev: 'Kadét',       jel: '🎖️' },
    { tol: 420,  nev: 'Ügynök',      jel: '🛡️' },
    { tol: 800,  nev: 'Elit ügynök', jel: '⚡' },
    { tol: 1300, nev: 'Bosszúálló',  jel: '🦸' },
    { tol: 1850, nev: 'Legenda',     jel: '🏆' }
  ];

  /* ---------- tároló ---------- */
  function ures() { return { v: 1, oldalak: {}, projektek: {}, feladatok: {}, kvizek: {}, beall: { effekt: 1 } }; }
  var A = ures();
  try {
    var nyers = localStorage.getItem(KULCS);
    if (nyers) {
      var b = JSON.parse(nyers);
      if (b && typeof b === 'object') {
        A = b;
        ['oldalak', 'projektek', 'feladatok', 'kvizek'].forEach(function (k) { A[k] = A[k] || {}; });
        A.beall = A.beall || { effekt: 1 };
      }
    }
  } catch (e) { /* privát mód / letiltott tároló → memóriában marad */ }

  function ment() { try { localStorage.setItem(KULCS, JSON.stringify(A)); } catch (e) {} }
  function db(o) { return Object.keys(o || {}).length; }
  function xp() {
    return db(A.oldalak) * PONT.oldal + db(A.projektek) * PONT.projekt +
           db(A.feladatok) * PONT.feladat + db(A.kvizek) * PONT.kviz;
  }
  function rang(p) {
    var i = 0;
    for (var j = 0; j < RANGOK.length; j++) if (p >= RANGOK[j].tol) i = j;
    return { i: i, r: RANGOK[i], kov: RANGOK[i + 1] || null };
  }

  /* ---------- oldal-azonosító (a webhely gyökeréhez képest) ---------- */
  var MELY = ROOT === '.' ? 0 : ROOT.split('/').length;
  function oldalKulcs() {
    var r = location.pathname.split('/').filter(Boolean).map(decodeURIComponent);
    if (!r.length || !/\.html?$/i.test(r[r.length - 1])) r.push('index.html');
    return r.slice(Math.max(0, r.length - 1 - MELY)).join('/');
  }
  var OK = oldalKulcs();
  var BAZIS = location.pathname.slice(0, location.pathname.length - encodeURI(OK).length);
  function linkKulcs(a) {
    try {
      var p = new URL(a.getAttribute('href'), location.href).pathname;
      if (p.indexOf(BAZIS) !== 0) return null;
      var k = decodeURIComponent(p.slice(BAZIS.length));
      return /\.html?$/i.test(k) ? k : (k.replace(/\/?$/, '/') + 'index.html');
    } catch (e) { return null; }
  }

  /* ---------- jutalom ---------- */
  var SZAVAK = ['BANG!', 'POW!', 'BOOM!', 'ZAP!', 'WHAM!'];
  function jutalom(elem, pont, szoveg) {
    var elozo = rang(xp() - pont).i, most = rang(xp()).i;
    document.dispatchEvent(new CustomEvent('szvetko-jutalom', {
      detail: {
        elem: elem, xp: pont,
        szo: szoveg || SZAVAK[Math.floor(Math.random() * SZAVAK.length)],
        rangUj: most > elozo ? RANGOK[most] : null
      }
    }));
    chipFrissit();
  }

  /* ---------- fejléc-chip ---------- */
  var chip = null;
  function chipFrissit() {
    if (!chip) return;
    var p = xp(), r = rang(p);
    chip.innerHTML = '<span class="jel">' + r.r.jel + '</span><b>' + r.r.nev + '</b>' +
                     '<span class="xp">' + p + ' XP</span>';
    chip.setAttribute('title', r.kov ? ('Következő rang: ' + r.kov.nev + ' (' + (r.kov.tol - p) + ' XP múlva)')
                                     : 'Elérted a legmagasabb rangot!');
    chip.classList.remove('lobban'); void chip.offsetWidth; chip.classList.add('lobban');
  }
  function chipBe() {
    var fej = document.querySelector('.fejlec-bel');
    if (!fej || document.querySelector('.naplo-chip')) return;
    chip = document.createElement('a');
    chip.className = 'naplo-chip';
    chip.href = ROOT + '/kuldetesnaplo.html';
    chip.setAttribute('aria-label', 'Küldetésnapló');
    var kereso = fej.querySelector('.kereso-mini');
    if (kereso) fej.insertBefore(chip, kereso); else fej.appendChild(chip);
    chipFrissit();
  }

  /* ---------- 1) teljesíthető oldalak (tananyag / összefoglaló / terepküldetés) ---------- */
  function oldalGomb() {
    var nev = OK.split('/').pop();
    var projekt = nev === 'terepkuldetes.html';
    if (!(projekt || nev === 'osszefoglalo.html' || nev.indexOf('tananyag-') === 0)) return;
    var tar = projekt ? A.projektek : A.oldalak;
    var tartalom = document.querySelector('.tartalom') || document.querySelector('main');
    if (!tartalom) return;

    var sav = document.createElement('div');
    sav.className = 'egyseg-kesz';
    var gomb = document.createElement('button');
    gomb.type = 'button'; gomb.className = 'kesz-gomb';
    var cimke = document.createElement('span');
    cimke.className = 'kesz-cimke';
    sav.appendChild(gomb); sav.appendChild(cimke);

    var lapozo = tartalom.querySelector('.lapozo') || document.querySelector('.lapozo');
    if (lapozo && lapozo.parentNode) lapozo.parentNode.insertBefore(sav, lapozo);
    else tartalom.appendChild(sav);

    function rajzol() {
      var kesz = !!tar[OK];
      gomb.classList.toggle('kesz', kesz);
      gomb.textContent = kesz ? '✅ Teljesítve' : (projekt ? '🎯 Küldetés teljesítve' : '✅ Egység teljesítve');
      cimke.textContent = kesz ? ('+' + (projekt ? PONT.projekt : PONT.oldal) + ' XP a naplódban')
                               : 'Ha végeztél, jelöld be — vagy görgesd végig a lapot.';
    }
    function jelol(auto) {
      if (tar[OK]) return;
      tar[OK] = Date.now(); ment(); rajzol();
      jutalom(gomb, projekt ? PONT.projekt : PONT.oldal, projekt ? 'MISSION COMPLETE!' : (auto ? 'CLEAR!' : 'BANG!'));
    }
    gomb.addEventListener('click', function () {
      if (tar[OK]) { delete tar[OK]; ment(); rajzol(); chipFrissit(); }
      else jelol(false);
    });
    rajzol();

    /* automatikus jelölés a lap aljához érve */
    if (!tar[OK]) {
      var fig = function () {
        var h = document.documentElement;
        var arany = (h.scrollTop + h.clientHeight) / h.scrollHeight;
        if (arany > 0.9) { jelol(true); window.removeEventListener('scroll', fig); }
      };
      window.addEventListener('scroll', fig, { passive: true });
      setTimeout(fig, 1200);   /* rövid lapnál nincs mit görgetni */
    }
  }

  /* ---------- 2) feladatkártyák pipája ---------- */
  function feladatPipak() {
    var kartyak = document.querySelectorAll('article.feladat[id]');
    if (!kartyak.length) return;
    kartyak.forEach(function (k) {
      var azon = OK + '#' + k.id;
      var cimke = document.createElement('label');
      cimke.className = 'fel-pipa';
      cimke.title = 'Megoldottam';
      var be = document.createElement('input');
      be.type = 'checkbox'; be.checked = !!A.feladatok[azon];
      var sz = document.createElement('span'); sz.textContent = 'megoldva';
      cimke.appendChild(be); cimke.appendChild(sz);
      be.addEventListener('change', function () {
        if (be.checked) { A.feladatok[azon] = Date.now(); ment(); jutalom(cimke, PONT.feladat); }
        else { delete A.feladatok[azon]; ment(); chipFrissit(); }
        k.classList.toggle('megoldva', be.checked);
      });
      k.classList.toggle('megoldva', be.checked);
      var fejsor = k.querySelector('.fejsor');
      if (fejsor) fejsor.appendChild(cimke); else k.appendChild(cimke);
    });
  }

  /* ---------- 3) kvízek ---------- */
  function kvizek() {
    var lista = document.querySelectorAll('.kviz');
    if (!lista.length) return;
    document.addEventListener('kviz-helyes', function (ev) {
      /* több változatos kvíznél az esemény a .valtozat elemről jön → a befoglaló .kviz kell */
      var el = ev.target.closest ? ev.target.closest('.kviz') : ev.target, i = -1;
      for (var j = 0; j < lista.length; j++) if (lista[j] === el) { i = j; break; }
      if (i < 0) return;
      var azon = OK + '#kviz-' + i;
      if (A.kvizek[azon]) return;
      A.kvizek[azon] = Date.now(); ment();
      jutalom(el, PONT.kviz);
    });
  }

  /* ---------- 4) haladás-gyűrűk az index-kártyákon ---------- */
  function gyuruSVG(szazalek) {
    var s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    s.setAttribute('class', 'gyuru'); s.setAttribute('viewBox', '0 0 36 36');
    s.innerHTML = '<circle class="hatso" cx="18" cy="18" r="15.5"></circle>' +
                  '<circle class="elso" cx="18" cy="18" r="15.5" ' +
                  'stroke-dasharray="' + (szazalek * 0.974) + ' 999"></circle>' +
                  '<text x="18" y="22">' + szazalek + '%</text>';
    return s;
  }
  function teljesitheto(t) {
    return t.db.oldal * PONT.oldal + t.db.projekt * PONT.projekt +
           t.db.kviz * PONT.kviz + t.db.feladat * PONT.feladat;
  }
  function elert(t) {
    var p = 0, i;
    for (i = 0; i < t.oldalak.length; i++) {
      var o = t.oldalak[i];
      if (o.t === 'projekt') { if (A.projektek[o.u]) p += PONT.projekt; }
      else if (A.oldalak[o.u]) p += PONT.oldal;
    }
    var elotag = t.url.replace(/index\.html$/, '');
    for (var k in A.feladatok) if (k.indexOf(elotag) === 0) p += PONT.feladat;
    for (var k2 in A.kvizek) if (k2.indexOf(elotag) === 0) p += PONT.kviz;
    return p;
  }
  function terkepBetolt(kesz) {
    if (window.__naploTerkep) { kesz(window.__naploTerkep); return; }
    if (!window.fetch) { kesz(null); return; }
    fetch(ROOT + '/assets/naplo-terkep.json')
      .then(function (v) { return v.json(); })
      .then(function (d) { window.__naploTerkep = d; kesz(d); })
      .catch(function () { kesz(null); });   /* file:// alatt nem működik — nem baj */
  }
  function gyuruk() {
    var kartyak = document.querySelectorAll('a.kartya');
    if (!kartyak.length) return;
    terkepBetolt(function (T) {
      if (!T) return;
      kartyak.forEach(function (a) {
        var k = linkKulcs(a);
        if (!k) return;
        var ossz = 0, meg = 0, talalt = false;
        for (var tag in T.tagozatok) {
          var tg = T.tagozatok[tag];
          if (k === tg.url) {                      /* tagozat-kártya a főhadiszálláson */
            tg.temakorok.forEach(function (t) { ossz += teljesitheto(t); meg += elert(t); });
            talalt = ossz > 0;
          }
          tg.temakorok.forEach(function (t) {      /* témakör-kártya a tagozat-indexen */
            if (k === t.url) { ossz = teljesitheto(t); meg = elert(t); talalt = ossz > 0; }
          });
        }
        if (!talalt) return;
        var sz = Math.round(meg / ossz * 100);
        a.classList.add('gyuruvel');
        a.appendChild(gyuruSVG(sz));
        if (sz === 100) a.classList.add('teljes');
      });
    });
  }

  /* ---------- nyilvános API (a küldetésnapló-oldalnak) ---------- */
  window.Naplo = {
    ROOT: ROOT, PONT: PONT, RANGOK: RANGOK,
    allapot: function () { return A; },
    kulcs: function () { return OK; },
    xp: xp, rang: rang, db: db,
    teljesitheto: teljesitheto, elert: elert, terkep: terkepBetolt,
    ment: ment,
    torol: function () { A = ures(); ment(); },
    kod: function () {                                   /* napló-kód: tömör, másolható */
      try { return btoa(unescape(encodeURIComponent(JSON.stringify(A)))).replace(/=+$/, ''); }
      catch (e) { return ''; }
    },
    kodBe: function (s) {
      try {
        var t = s.replace(/\s+/g, ''); while (t.length % 4) t += '=';
        var o = JSON.parse(decodeURIComponent(escape(atob(t))));
        if (!o || typeof o !== 'object' || !o.oldalak) return false;
        A = o; ['oldalak','projektek','feladatok','kvizek'].forEach(function (k) { A[k] = A[k] || {}; });
        A.beall = A.beall || { effekt: 1 };
        ment(); return true;
      } catch (e) { return false; }
    },
    effektBe: function () { return A.beall.effekt !== 0; },
    effektAllit: function (be) { A.beall.effekt = be ? 1 : 0; ment(); }
  };

  /* ---------- indulás ---------- */
  function indul() {
    chipBe(); oldalGomb(); feladatPipak(); kvizek(); gyuruk();
    document.dispatchEvent(new CustomEvent('naplo-kesz'));
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', indul);
  else indul();
})();
