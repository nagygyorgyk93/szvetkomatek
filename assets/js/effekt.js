/* Szvetkó matek — MIKRO-ANIMÁCIÓK
   ------------------------------------------------------------------
   Két réteg:
   1) Jutalom-pillanatok: képregényes pukkanás (BANG!/POW!…) + lebegő „+XP”
      + rangemelés-villanás — a naplo.js `szvetko-jutalom` eseményére.
   2) Halk háttérzaj: kártyák/dobozok beúszása görgetéskor, apró szikra az
      interaktív elemek kattintására, a hibás kvízválasz megrázása.
   Kikapcsolható a Küldetésnaplóban; `prefers-reduced-motion` esetén magától alszik. */
(function () {
  'use strict';

  /* A rendszer „mozgás csökkentése” beállítását CSAK alapértelmezésnek vesszük:
     a Küldetésnapló kapcsolója felülírja (ha a kadét bekapcsolva hagyja, látja az
     effekteket). A `html.effekt-be` osztály jelzi a CSS-nek, hogy a mozgáscsökkentő
     médiablokk ne fojtsa el az animációkat. */
  function enged() { return !window.Naplo || window.Naplo.effektBe(); }
  function jelzes() { document.documentElement.classList.toggle('effekt-be', enged()); }
  jelzes();
  document.addEventListener('naplo-kesz', jelzes);

  /* ---------- réteg a látványelemeknek ---------- */
  var reteg = null;
  function retegElo() {
    if (!reteg) {
      reteg = document.createElement('div');
      reteg.className = 'effekt-reteg';
      document.body.appendChild(reteg);
    }
    return reteg;
  }
  function kozep(el) {
    if (!el || !el.getBoundingClientRect) return { x: innerWidth / 2, y: innerHeight / 2 };
    var r = el.getBoundingClientRect();
    if (!r.width && !r.height) return { x: innerWidth / 2, y: innerHeight / 2 };
    return { x: r.left + r.width / 2, y: r.top + Math.min(r.height / 2, 90) };
  }
  function elhelyez(e, p, ms) {
    e.style.left = p.x + 'px'; e.style.top = p.y + 'px';
    retegElo().appendChild(e);
    setTimeout(function () { if (e.parentNode) e.parentNode.removeChild(e); }, ms);
  }

  /* ---------- 1) jutalom ---------- */
  document.addEventListener('szvetko-jutalom', function (ev) {
    if (!enged()) return;
    var d = ev.detail || {}, p = kozep(d.elem);

    if (d.szo) {                                  /* képregényes pukkanás */
      var b = document.createElement('div');
      b.className = 'pukkanas';
      b.style.setProperty('--dol', (Math.random() * 16 - 8).toFixed(1) + 'deg');
      b.textContent = d.szo;
      elhelyez(b, p, 900);
    }
    if (d.xp) {                                   /* lebegő pontszám */
      var x = document.createElement('div');
      x.className = 'xp-lebego';
      x.textContent = '+' + d.xp + ' XP';
      elhelyez(x, { x: p.x, y: p.y - 26 }, 1100);
    }
    if (d.rangUj) {                               /* előléptetés */
      var r = document.createElement('div');
      r.className = 'rang-szalag';
      r.innerHTML = '<span class="jel">' + d.rangUj.jel + '</span>' +
                    '<span><b>ELŐLÉPTETÉS</b><br>' + d.rangUj.nev + '</span>';
      retegElo().appendChild(r);
      setTimeout(function () { if (r.parentNode) r.parentNode.removeChild(r); }, 2600);
    }
  });

  /* ---------- 2) apró szikra az interaktív elemekre ---------- */
  document.addEventListener('click', function (ev) {
    if (!enged()) return;
    var el = ev.target.closest('a.kartya, .sav, .kviz .opciok button, .kesz-gomb, .btn-marvel, ' +
                               'details>summary, .kereso-mini button, .kviz .ujra, .naplo-chip');
    if (!el) return;
    var sz = document.createElement('span');
    sz.className = 'szikra';
    elhelyez(sz, { x: ev.clientX, y: ev.clientY }, 620);
  }, true);

  /* ---------- 3) hibás kvízválasz: rövid rázás ---------- */
  document.addEventListener('click', function (ev) {
    if (!enged()) return;
    var b = ev.target.closest('.kviz .opciok button');
    if (!b) return;
    setTimeout(function () {
      if (b.classList.contains('rossz')) {
        b.classList.remove('razas'); void b.offsetWidth; b.classList.add('razas');
      }
    }, 30);
  });

  /* ---------- 4) beúszás görgetéskor ---------- */
  function beuszas() {
    if (!enged() || !window.IntersectionObserver) return;
    var cel = document.querySelectorAll('.kartya, .doboz, .feladat, .kviz, .brief, .talalat, .naplo-sor');
    if (!cel.length || cel.length > 400) return;      /* nagyon hosszú lapon kihagyjuk */
    document.documentElement.classList.add('anim-be');
    var fig = new IntersectionObserver(function (be) {
      be.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('lathato'); fig.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    cel.forEach(function (e) { fig.observe(e); });
    /* biztonsági háló: 3 mp múlva minden látszik (ha bármi félrecsúszna) */
    setTimeout(function () { cel.forEach(function (e) { e.classList.add('lathato'); }); }, 3000);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', beuszas);
  else beuszas();
})();
