/* Szvetkó matek — külső média (YouTube-videó, GeoGebra-szimuláció) kattintásra.
   A <figure class="media"> blokkokat a _tools/media.py írja a lapokba a
   _tools/media/*.json katalógusból — kézzel nem kell (és nem is szabad) szerkeszteni.

   Adatvédelem + sebesség: a lap betöltésekor SEMMI nem megy harmadik félhez; az
   iframe csak akkor jön létre, ha a kadét rákattint. Addig a blokk egy alacsony sáv (Q7);
   a kattintás a .media-fut osztállyal nyitja ki a lejátszó méretére. JS nélkül a blokk sima link
   a forrásra (új lapon nyílik). A YouTube a youtube-nocookie.com tartományról jön.
   Az ui.js tölti be, ha a lapon van .media — az oldalakhoz nem kell <script>. */
(function(){
  'use strict';
  if (window.__szvMedia) return;
  window.__szvMedia = true;

  var GGB_KAPCSOLOK = 'border/888888/sfsb/true/szb/true/smb/false/stb/false/stbh/false/' +
                      'ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false';
  var nyitottak = new WeakMap();
  var szokozIndito = null;

  function inditoNev(fig){
    return (fig.getAttribute('data-tipus') === 'youtube' ? 'Videó indítása: ' :
            'GeoGebra-szimuláció betöltése: ') + (fig.getAttribute('data-cim') || 'beágyazott tartalom');
  }

  function forras(fig, szel, mag){
    var tipus = fig.getAttribute('data-tipus');
    var azon = encodeURIComponent(fig.getAttribute('data-azon') || '');
    if (!azon) return null;
    if (tipus === 'youtube'){
      var k = parseInt(fig.getAttribute('data-kezdes') || '0', 10);
      return 'https://www.youtube-nocookie.com/embed/' + azon +
             '?rel=0&autoplay=1&playsinline=1' + (k > 0 ? '&start=' + k : '');
    }
    if (tipus === 'geogebra'){
      // data-meret = az applet eredeti mérete: ezt kérjük, a GeoGebra pedig az egészet a keretbe
      // skálázza. Nélküle a keret méretében rajzol, és telefonon csak az applet egy darabja látszik.
      var m = /^(\d+)x(\d+)$/.exec(fig.getAttribute('data-meret') || '');
      if (m){ szel = m[1]; mag = m[2]; }
      return 'https://www.geogebra.org/material/iframe/id/' + azon +
             '/width/' + szel + '/height/' + mag + '/' + GGB_KAPCSOLOK;
    }
    return null;
  }

  function indit(fig, a){
    var keret = fig.querySelector('.media-keret');
    if (!keret || keret.querySelector('iframe')) return false;
    // Előbb kinyitjuk a sávot (a .media-fut adja a 16:9-et / az applet arányát), csak utána mérünk.
    fig.classList.add('media-fut');
    var szel = Math.max(280, Math.round(keret.clientWidth || 640));
    var mag = Math.max(200, Math.round(keret.clientHeight || szel * 9 / 16));
    var src = forras(fig, szel, mag);
    if (!src){ fig.classList.remove('media-fut'); return false; }
    var ifr = document.createElement('iframe');
    ifr.src = src;
    ifr.title = fig.getAttribute('data-cim') || 'beágyazott tartalom';
    ifr.setAttribute('allow', 'autoplay; encrypted-media; fullscreen; picture-in-picture');
    ifr.setAttribute('allowfullscreen', '');
    ifr.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    // Az eredeti hivatkozást megőrizzük: bezáráskor ugyanide tér vissza a fókusz.
    var vezerlok = document.createElement('div');
    vezerlok.className = 'media-vezerlok';
    var kulso = document.createElement('a');
    kulso.href = a.href; kulso.target = '_blank'; kulso.rel = 'noopener';
    kulso.textContent = fig.getAttribute('data-tipus') === 'youtube' ?
      'Megnyitás a YouTube-on új lapon' : 'Megnyitás a GeoGebrában új lapon';
    kulso.setAttribute('aria-label', kulso.textContent + ': ' + (fig.getAttribute('data-cim') || 'beágyazott tartalom'));
    nyitottak.set(fig, {indito:a, tartalom:a.innerHTML, vezerlok:vezerlok});
    vezerlok.appendChild(a); vezerlok.appendChild(kulso);
    keret.parentNode.insertBefore(vezerlok, keret);
    a.textContent = 'Beágyazás bezárása';
    a.setAttribute('aria-label', 'Beágyazás bezárása: ' + (fig.getAttribute('data-cim') || 'beágyazott tartalom'));
    a.setAttribute('aria-expanded', 'true');
    keret.innerHTML = '';
    keret.appendChild(ifr);
    try { ifr.focus(); } catch (e) {}
    return true;
  }

  function bezar(fig){
    var allapot = nyitottak.get(fig), keret = fig.querySelector('.media-keret');
    if (!allapot || !keret) return false;
    var a = allapot.indito;
    keret.innerHTML = ''; // Az iframe eltávolítása a lejátszást is megszünteti.
    a.innerHTML = allapot.tartalom;
    a.setAttribute('aria-label', inditoNev(fig));
    a.setAttribute('aria-expanded', 'false');
    keret.appendChild(a);
    allapot.vezerlok.remove(); nyitottak.delete(fig);
    fig.classList.remove('media-fut');
    try { a.focus(); } catch (e) {}
    return true;
  }

  document.querySelectorAll('figure.media .media-indito').forEach(function(a){
    var fig = a.closest('figure.media'), keret = fig.querySelector('.media-keret');
    if (!keret || !forras(fig, 640, 360)) return;
    if (!keret.id) keret.id = fig.id + '-keret';
    // JavaScript nélkül ez továbbra is közvetlen forráshivatkozás.
    a.setAttribute('role', 'button');
    a.setAttribute('aria-label', inditoNev(fig));
    a.setAttribute('aria-controls', keret.id);
    a.setAttribute('aria-expanded', 'false');
  });

  document.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('.media-indito') : null;
    if (!a) return;
    // Ctrl/Cmd/Shift/középső gomb: hagyjuk a böngészőt új lapon megnyitni
    if (ev.button !== 0 || ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.altKey) return;
    var fig = a.closest('figure.media');
    if (fig && (nyitottak.has(fig) ? bezar(fig) : indit(fig, a))) ev.preventDefault();
  });

  // A gombként működő link szóközzel is aktiválható; az Enter natív kattintást ad.
  document.addEventListener('keydown', function(ev){
    if (ev.key !== ' ' || ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.altKey) return;
    var a = ev.target.closest ? ev.target.closest('.media-indito[role="button"]') : null;
    if (a){
      ev.preventDefault();
      if (!ev.repeat) szokozIndito = a;
    }
  });
  document.addEventListener('keyup', function(ev){
    if (ev.key !== ' ') return;
    var kezdet = szokozIndito; szokozIndito = null;
    if (ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.altKey) return;
    var a = ev.target.closest ? ev.target.closest('.media-indito[role="button"]') : null;
    if (a && a === kezdet){ ev.preventDefault(); a.click(); }
  });
  document.addEventListener('focusout', function(ev){
    if (ev.target === szokozIndito) szokozIndito = null;
  });
})();
