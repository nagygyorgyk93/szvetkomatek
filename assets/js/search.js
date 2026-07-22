/* Szvetkó matek — kliensoldali kereső (search.html).
   Az assets/search-index.json-t a _tools/build_search_index.py állítja elő;
   minden tartalmi változás után újra kell futtatni (F5 integrációs lépés). */
(function(){
  'use strict';
  var mezo = document.getElementById('q');
  var lista = document.getElementById('talalatok');
  var osszegzo = document.getElementById('osszegzo');
  if(!mezo || !lista) return;

  function norm(s){
    return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
  }

  var index = [];
  fetch('assets/search-index.json')
    .then(function(r){return r.json();})
    .then(function(d){
      index = d.map(function(o){
        return {o:o, ncim:norm(o.cim), nfej:norm((o.fejezetek||[]).join(' ')), nszoveg:norm(o.szoveg)};
      });
      var q = new URLSearchParams(location.search).get('q');
      if(q){mezo.value = q; keres(q);}
    })
    .catch(function(){ if(osszegzo) osszegzo.textContent = 'A keresőindex nem tölthető be.'; });

  function kiemel(szoveg, nszoveg, nq){
    var p = nszoveg.indexOf(nq);
    if(p < 0) return szoveg.slice(0,160) + '…';
    var eleje = Math.max(0, p-70);
    var resz = szoveg.slice(eleje, p) + '<mark>' + szoveg.slice(p, p+nq.length) + '</mark>' +
               szoveg.slice(p+nq.length, p+nq.length+90);
    return (eleje>0?'…':'') + resz + '…';
  }

  function keres(q){
    var nq = norm(q.trim());
    lista.innerHTML = '';
    if(nq.length < 2){ if(osszegzo) osszegzo.textContent = 'Írj be legalább 2 karaktert.'; return; }
    var talalatok = [];
    index.forEach(function(e){
      var pont = 0;
      if(e.ncim.indexOf(nq) >= 0) pont += 5;
      if(e.nfej.indexOf(nq) >= 0) pont += 3;
      if(e.nszoveg.indexOf(nq) >= 0) pont += 1;
      if(pont > 0) talalatok.push({e:e, pont:pont});
    });
    talalatok.sort(function(a,b){return b.pont - a.pont;});
    if(osszegzo) osszegzo.textContent = talalatok.length ?
      (talalatok.length + ' találat erre: „' + q + '”') : ('Nincs találat erre: „' + q + '”.');
    talalatok.slice(0,50).forEach(function(t){
      var o = t.e.o;
      var div = document.createElement('div');
      div.className = 'talalat';
      div.innerHTML =
        '<div class="hol">' + (o.tagozat ? '<span class="tagozat-jel">'+o.tagozat+'</span>' : '') +
          (o.tema || '') + '</div>' +
        '<h3><a href="' + o.url + '">' + o.cim + '</a></h3>' +
        '<p>' + kiemel(o.szoveg, t.e.nszoveg, nq) + '</p>';
      lista.appendChild(div);
    });
  }

  document.getElementById('kereso-form').addEventListener('submit', function(ev){
    ev.preventDefault();
    var q = mezo.value;
    history.replaceState(null, '', 'search.html?q=' + encodeURIComponent(q));
    keres(q);
  });
})();
