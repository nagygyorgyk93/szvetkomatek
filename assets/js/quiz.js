/* Szvetkó matek — mini-kvíz motor (v2).
   Kétféle kártya:
   1) EGYSZERŰ (visszafelé kompatibilis): <div class="kviz" data-answer="1" data-jo="…" data-nem="…">
        <p class="kviz-cim">🎯 Gyors kérdés</p><p>Kérdés…</p>
        <div class="opciok"><button>…</button>…</div><p class="visszajelzes"></p></div>
   2) VÁLTOZATOS: a .kviz több <div class="valtozat" data-answer=".." data-jo=".." data-nem="..">
        elemet tartalmaz (mindegyikben <p class="k">Kérdés</p> + .opciok). Mód:
        data-mod="veletlen" (alap): betöltéskor/„🎲 Másik kérdés” gombra véletlen változat;
        data-mod="lanc": helyes válasz után a „Következő kérdés →” gombbal a következő.
   data-answer: a helyes opció 0-alapú indexe. A visszajelzés (data-jo/data-nem) SIMA szöveg
   (a KaTeX csak betöltéskor fut, dinamikus szövegre nem). */
(function(){
  'use strict';
  function wire(scope, vj){
    var gombok = scope.querySelectorAll('.opciok button');
    gombok.forEach(function(b, i){
      b.addEventListener('click', function(){
        if(scope.dataset.kesz === '1') return;
        var helyes = parseInt(scope.getAttribute('data-answer'), 10);
        var jo  = scope.getAttribute('data-jo')  || '✔ Helyes!';
        var nem = scope.getAttribute('data-nem') || '✘ Nem talált — gondold át újra!';
        gombok.forEach(function(x){ x.classList.remove('helyes','rossz'); });
        if(i === helyes){
          b.classList.add('helyes'); scope.dataset.kesz = '1';
          if(vj){ vj.textContent = jo; vj.className = 'visszajelzes jo'; }
          gombok.forEach(function(x){ x.disabled = true; });
          scope.dispatchEvent(new CustomEvent('kviz-helyes', {bubbles:true}));
        } else {
          b.classList.add('rossz');
          if(vj){ vj.textContent = nem; vj.className = 'visszajelzes nem'; }
        }
      });
    });
  }
  document.querySelectorAll('.kviz').forEach(function(k){
    var vj = k.querySelector('.visszajelzes');
    var valt = Array.prototype.slice.call(k.children).filter(function(el){
      return el.classList && el.classList.contains('valtozat');
    });
    if(valt.length === 0){ wire(k, vj); return; }   // egyszerű mód

    valt.forEach(function(v){ wire(v, vj); });
    var aktiv = -1;
    function mutat(idx){
      valt.forEach(function(v, i){ v.hidden = (i !== idx); });
      var g = valt[idx].querySelectorAll('.opciok button');
      g.forEach(function(x){ x.disabled = false; x.classList.remove('helyes','rossz'); });
      valt[idx].dataset.kesz = '';
      if(vj){ vj.textContent = ''; vj.className = 'visszajelzes'; }
      aktiv = idx;
    }
    var mod = k.getAttribute('data-mod') || 'veletlen';
    if(mod === 'lanc'){
      mutat(0);
      var kov = document.createElement('button');
      kov.type = 'button'; kov.className = 'ujra'; kov.textContent = 'Következő kérdés →'; kov.hidden = true;
      k.addEventListener('kviz-helyes', function(){ if(aktiv < valt.length - 1) kov.hidden = false; });
      kov.addEventListener('click', function(){ if(aktiv < valt.length - 1){ mutat(aktiv + 1); kov.hidden = true; } });
      k.appendChild(kov);
    } else {
      mutat(Math.floor(Math.random() * valt.length));
      if(valt.length > 1){
        var masik = document.createElement('button');
        masik.type = 'button'; masik.className = 'ujra'; masik.textContent = '🎲 Másik kérdés';
        masik.addEventListener('click', function(){
          var i; do { i = Math.floor(Math.random() * valt.length); } while(i === aktiv && valt.length > 1);
          mutat(i);
        });
        k.appendChild(masik);
      }
    }
  });
})();
