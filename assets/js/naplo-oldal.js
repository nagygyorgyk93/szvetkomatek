/* Szvetkó matek — a Küldetésnapló oldal kirajzolása (csak a kuldetesnaplo.html-en fut). */
(function () {
  'use strict';

  function indul() {
    var N = window.Naplo;
    if (!N) return;
    var A = N.allapot(), P = N.PONT;

    /* --- rang + összesített sáv --- */
    var p = N.xp(), r = N.rang(p);
    document.getElementById('rang-jel').textContent = r.r.jel;
    document.getElementById('rang-nev').textContent = r.r.nev;
    document.getElementById('rang-xp').textContent = p + ' XP';
    var alatta = document.getElementById('rang-alatta');
    if (r.kov) {
      var szak = r.kov.tol - RANG_ELOZO(r), benne = p - RANG_ELOZO(r);
      alatta.textContent = 'Következő rang: ' + r.kov.nev + ' — még ' + (r.kov.tol - p) + ' XP';
      setTimeout(function () {
        document.getElementById('rang-sav').style.width = Math.min(100, benne / szak * 100) + '%';
      }, 60);
    } else {
      alatta.textContent = 'Elérted a legmagasabb rangot. Tiszteletünk, kadét!';
      setTimeout(function () { document.getElementById('rang-sav').style.width = '100%'; }, 60);
    }
    function RANG_ELOZO(x) { return x.r.tol; }

    /* --- számlálók --- */
    document.getElementById('sz-oldal').textContent    = N.db(A.oldalak);
    document.getElementById('sz-kviz').textContent     = N.db(A.kvizek);
    document.getElementById('sz-feladat').textContent  = N.db(A.feladatok);
    document.getElementById('sz-projekt').textContent  = N.db(A.projektek);

    /* --- témakörönkénti haladás --- */
    N.terkep(function (T) {
      var hova = document.getElementById('naplo-lista');
      if (!T) {
        hova.innerHTML = '<p class="halvany">A részletes haladás csak a webhelyről betöltve látszik ' +
                         '(helyi fájlból megnyitva a böngésző nem engedi beolvasni a térképet).</p>';
        return;
      }
      var html = '';
      for (var tag in T.tagozatok) {
        var tg = T.tagozatok[tag];
        if (!tg.temakorok.length) continue;
        var tOssz = 0, tMeg = 0;
        tg.temakorok.forEach(function (t) { tOssz += N.teljesitheto(t); tMeg += N.elert(t); });
        html += '<h2>' + tg.cim + ' <span class="pill">' +
                Math.round(tMeg / (tOssz || 1) * 100) + '%</span></h2>';
        tg.temakorok.forEach(function (t) {
          var ossz = N.teljesitheto(t), meg = N.elert(t);
          var sz = Math.round(meg / (ossz || 1) * 100);
          /* részletek */
          var elotag = t.url.replace(/index\.html$/, ''), fDb = 0, kDb = 0, oDb = 0, pDb = 0, k;
          for (k in A.feladatok) if (k.indexOf(elotag) === 0) fDb++;
          for (k in A.kvizek)    if (k.indexOf(elotag) === 0) kDb++;
          t.oldalak.forEach(function (o) {
            if (o.t === 'projekt') { if (A.projektek[o.u]) pDb++; }
            else if (A.oldalak[o.u]) oDb++;
          });
          html += '<div class="naplo-sor' + (sz === 100 ? ' teljes' : '') + '">' +
                    '<h3><a href="' + t.url + '">' + t.cim + '</a> ' +
                      '<span class="pill">' + sz + '%</span></h3>' +
                    '<div class="sav-kulso"><div class="sav-belso" style="width:' + sz + '%"></div></div>' +
                    '<div class="reszek">' +
                      '<span>📗 tananyag: <b>' + oDb + '</b>/' + t.db.oldal + '</span>' +
                      '<span>🎯 kvíz: <b>' + kDb + '</b>/' + t.db.kviz + '</span>' +
                      '<span>✏️ feladat: <b>' + fDb + '</b>/' + t.db.feladat + '</span>' +
                      (t.db.projekt ? '<span>🛰️ terepküldetés: <b>' + pDb + '</b>/' + t.db.projekt + '</span>' : '') +
                    '</div></div>';
        });
      }
      hova.innerHTML = html || '<p class="halvany">Még nincs feldolgozott témakör.</p>';
    });

    /* --- eszközök --- */
    var uzenet = document.getElementById('naplo-uzenet');
    function szol(s) { uzenet.textContent = s; setTimeout(function () { uzenet.textContent = ''; }, 4000); }

    var mezo = document.getElementById('naplo-kod');
    document.getElementById('kod-keszit').addEventListener('click', function () {
      mezo.value = N.kod(); mezo.select(); szol('Kész — másold ki (Ctrl+C), és illeszd be a másik eszközön.');
    });
    document.getElementById('kod-betolt').addEventListener('click', function () {
      if (!mezo.value.trim()) { szol('Előbb illeszd be a kódot a mezőbe.'); return; }
      if (N.kodBe(mezo.value)) location.reload();
      else szol('Ez a kód nem érvényes — ellenőrizd, hogy a teljes szöveget bemásoltad-e.');
    });
    document.getElementById('naplo-torles').addEventListener('click', function () {
      if (confirm('Biztosan törlöd a teljes küldetésnaplót? Ez nem vonható vissza.')) {
        N.torol(); location.reload();
      }
    });
    var kapcsolo = document.getElementById('effekt-kapcs');
    kapcsolo.checked = N.effektBe();
    kapcsolo.addEventListener('change', function () {
      N.effektAllit(kapcsolo.checked);
      szol(kapcsolo.checked ? 'Látványelemek bekapcsolva.' : 'Látványelemek kikapcsolva.');
    });
  }

  if (window.Naplo) indul();
  else document.addEventListener('naplo-kesz', indul);
})();
