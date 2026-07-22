/* Szvetkó matek — mini-kvíz motor.
   Használat:
   <div class="kviz" data-answer="1" data-jo="Pontosan!" data-nem="Nem az — gondold át újra!">
     <p class="kviz-cim">🎯 Gyors kérdés</p>
     <p>Kérdés szövege…</p>
     <div class="opciok">
       <button>A opció</button><button>B opció</button><button>C opció</button>
     </div>
     <p class="visszajelzes" aria-live="polite"></p>
   </div>
   data-answer: a helyes opció 0-alapú indexe. */
(function(){
  'use strict';
  document.querySelectorAll('.kviz').forEach(function(k){
    var helyes = parseInt(k.getAttribute('data-answer'), 10);
    var vj = k.querySelector('.visszajelzes');
    var joSzoveg  = k.getAttribute('data-jo')  || '✔ Helyes!';
    var nemSzoveg = k.getAttribute('data-nem') || '✘ Nem talált — próbáld újra!';
    var gombok = k.querySelectorAll('.opciok button');
    gombok.forEach(function(b, i){
      b.addEventListener('click', function(){
        gombok.forEach(function(x){x.classList.remove('helyes','rossz');});
        if(i === helyes){
          b.classList.add('helyes');
          if(vj){vj.textContent = joSzoveg; vj.className = 'visszajelzes jo';}
          gombok.forEach(function(x){x.disabled = true;});
        }else{
          b.classList.add('rossz');
          if(vj){vj.textContent = nemSzoveg; vj.className = 'visszajelzes nem';}
        }
      });
    });
  });
})();
