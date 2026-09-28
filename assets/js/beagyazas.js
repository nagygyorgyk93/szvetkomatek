/* Szvetkó matek — külső média (YouTube-videó, GeoGebra-szimuláció) kattintásra.
   A <figure class="media"> blokkokat a _tools/media.py írja a lapokba a
   _tools/media/*.json katalógusból — kézzel nem kell (és nem is szabad) szerkeszteni.

   Adatvédelem + sebesség: a lap betöltésekor SEMMI nem megy harmadik félhez; az
   iframe csak akkor jön létre, ha a kadét rákattint. JS nélkül a blokk sima link
   a forrásra (új lapon nyílik). A YouTube a youtube-nocookie.com tartományról jön.
   Az ui.js tölti be, ha a lapon van .media — az oldalakhoz nem kell <script>. */
(function(){
  'use strict';
  if (window.__szvMedia) return;
  window.__szvMedia = true;

  var GGB_KAPCSOLOK = 'border/888888/sfsb/true/szb/true/smb/false/stb/false/stbh/false/' +
                      'ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false';

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

  function indit(fig){
    var keret = fig.querySelector('.media-keret');
    if (!keret || keret.querySelector('iframe')) return false;
    var szel = Math.max(280, Math.round(keret.clientWidth || 640));
    var mag = Math.max(200, Math.round(keret.clientHeight || szel * 9 / 16));
    var src = forras(fig, szel, mag);
    if (!src) return false;
    var ifr = document.createElement('iframe');
    ifr.src = src;
    ifr.title = fig.getAttribute('data-cim') || 'beágyazott tartalom';
    ifr.setAttribute('allow', 'autoplay; encrypted-media; fullscreen; picture-in-picture');
    ifr.setAttribute('allowfullscreen', '');
    ifr.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    keret.innerHTML = '';
    keret.appendChild(ifr);
    fig.classList.add('media-fut');
    try { ifr.focus(); } catch (e) {}
    return true;
  }

  document.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('.media-indito') : null;
    if (!a) return;
    // Ctrl/Cmd/Shift/középső gomb: hagyjuk a böngészőt új lapon megnyitni
    if (ev.button !== 0 || ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.altKey) return;
    var fig = a.closest('figure.media');
    if (fig && indit(fig)) ev.preventDefault();
  });
})();
