/* Szvetkó matek — közös UI: progress, TOC, nyomtatás, mini-kereső.
   Minden oldal <html data-root="..."> attribútummal adja meg a gyökérhez
   vezető relatív utat ('.', '..' vagy '../..'). */
(function(){
  'use strict';
  var ROOT = document.documentElement.getAttribute('data-root') || '.';

  /* Scroll-progress sáv */
  var bar = document.getElementById('progress');
  if(bar){
    var upd = function(){
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max>0 ? (h.scrollTop/max*100) : 0) + '%';
    };
    document.addEventListener('scroll', upd, {passive:true});
    upd();
  }

  /* TOC felépítése a h2/h3 címekből (ha van #toc) */
  var toc = document.getElementById('toc');
  if(toc){
    var cimek = document.querySelectorAll('.tartalom h2[id], .tartalom h3[id]');
    if(cimek.length){
      var frag = document.createDocumentFragment();
      var cim = document.createElement('div');
      cim.className='toc-cim'; cim.textContent='Tartalom';
      frag.appendChild(cim);
      cimek.forEach(function(el){
        var a = document.createElement('a');
        a.href = '#'+el.id;
        a.textContent = el.textContent.replace(/[¶#]\s*$/,'');
        if(el.tagName==='H3') a.className='h3';
        frag.appendChild(a);
      });
      toc.appendChild(frag);
      /* aktív szakasz jelölése */
      var linkek = toc.querySelectorAll('a');
      var obs = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(e.isIntersecting){
            linkek.forEach(function(l){l.classList.toggle('aktiv', l.hash==='#'+e.target.id);});
          }
        });
      }, {rootMargin:'-20% 0px -70% 0px'});
      cimek.forEach(function(el){obs.observe(el);});
    }
  }

  /* Nyomtatás előtt minden lenyílót kinyitunk, utána visszazárjuk */
  var nyitottak = [];
  window.addEventListener('beforeprint', function(){
    nyitottak = [];
    document.querySelectorAll('details:not([open])').forEach(function(d){
      nyitottak.push(d); d.setAttribute('open','');
    });
  });
  window.addEventListener('afterprint', function(){
    nyitottak.forEach(function(d){d.removeAttribute('open');});
    nyitottak = [];
  });

  /* Üdvözlő videó: néma automata lejátszás + „Hang be” (egyszer, hanggal).
     A böngészők a hangos automata indítást tiltják, ezért a hang mindig
     felhasználói kattintásra szólal meg; utána visszaáll a néma ismétlésre. */
  document.querySelectorAll('.hang-gomb').forEach(function(gomb){
    var v = document.getElementById(gomb.getAttribute('data-video'));
    if(!v){ gomb.hidden = true; return; }
    var lassit = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    /* Csökkentett mozgás esetén sem tiltjuk le a lejátszást (a köszöntés elmaradna),
       csak nem ismételjük. */
    if(lassit) v.loop = false;
    v.muted = true; v.defaultMuted = true;   /* a néma automata indítás feltétele */
    nemaInditas();

    function nemaInditas(){
      var p = v.play();
      if(p && p.catch) p.catch(function(){
        /* a böngésző blokkolta (energiatakarékos mód, beállítás, iOS): az első
           felhasználói mozdulatra újrapróbáljuk */
        var esem = ['pointerdown','keydown','touchstart','scroll'];
        var ujra = function(){
          esem.forEach(function(e){ window.removeEventListener(e, ujra, true); });
          v.muted = true;
          var q = v.play(); if(q && q.catch) q.catch(function(){});
        };
        esem.forEach(function(e){ window.addEventListener(e, ujra, {capture:true, passive:true}); });
      });
    }

    /* Átlátszóság-teszt: a videó sarka átlátszó-e? Ha a böngésző nem tudja a VP9-alfát
       (pl. Safari), a keret `nincs-alfa` osztályt kap → CSS-ből screen-keverés. */
    v.addEventListener('loadeddata', function proba(){
      v.removeEventListener('loadeddata', proba);
      try{
        var c = document.createElement('canvas'); c.width = 8; c.height = 8;
        var cx = c.getContext('2d');
        cx.clearRect(0, 0, 8, 8);
        cx.drawImage(v, 0, 0, 8, 8);
        if(cx.getImageData(0, 0, 1, 1).data[3] > 250 && v.parentNode)
          v.parentNode.classList.add('nincs-alfa');
      }catch(e){ /* ha bármi gond van, marad az alapértelmezett megjelenés */ }
    });

    var eredetiSzoveg = gomb.textContent;
    gomb.addEventListener('click', function(){
      v.muted = false; v.loop = false; v.currentTime = 0;
      gomb.disabled = true; gomb.textContent = '🔊 Szól…';
      var p2 = v.play();
      if(p2 && p2.catch) p2.catch(function(){ vissza(); });
    });
    function vissza(){
      v.muted = true;
      if(!lassit) v.loop = true;
      gomb.disabled = false; gomb.textContent = eredetiSzoveg;
      var p3 = v.play(); if(p3 && p3.catch) p3.catch(function(){});
    }
    v.addEventListener('ended', function(){ if(!v.loop) vissza(); });
  });

  /* „Vissza a tetejére” rakéta — hosszú lapokon, 600 px görgetés után */
  (function(){
    if(document.body.scrollHeight < 2200) return;
    var g = document.createElement('button');
    g.type = 'button'; g.className = 'tetejere'; g.title = 'Vissza a tetejére';
    g.setAttribute('aria-label','Vissza a lap tetejére');
    g.textContent = '🚀';
    document.body.appendChild(g);
    g.addEventListener('click', function(){
      var lassit = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({top:0, behavior: lassit ? 'auto' : 'smooth'});
      g.classList.add('kilo');
      setTimeout(function(){ g.classList.remove('kilo'); }, 700);
    });
    var lat = function(){ g.classList.toggle('mutat', document.documentElement.scrollTop > 600); };
    document.addEventListener('scroll', lat, {passive:true}); lat();
  })();

  /* „/” → ugrás a keresőbe (ha épp nem beviteli mezőben vagyunk) */
  document.addEventListener('keydown', function(ev){
    if(ev.key !== '/' || ev.ctrlKey || ev.altKey || ev.metaKey) return;
    var a = document.activeElement;
    if(a && /^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName)) return;
    if(a && a.isContentEditable) return;
    var mezo = document.querySelector('.kereso-mini input, .kereso-nagy input');
    if(mezo){ ev.preventDefault(); mezo.focus(); mezo.select(); }
    else { ev.preventDefault(); window.location.href = ROOT + '/search.html'; }
  });

  /* Küldetésnapló + mikro-animációk betöltése (így nem kell minden oldal
     <head>-jébe felvenni őket) */
  ['naplo.js', 'effekt.js'].forEach(function(f){
    var s = document.createElement('script');
    s.src = ROOT + '/assets/js/' + f; s.defer = true;
    document.body.appendChild(s);
  });

  /* Fejléc mini-kereső → search.html?q=... */
  var form = document.querySelector('.kereso-mini');
  if(form){
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var q = form.querySelector('input').value.trim();
      window.location.href = ROOT + '/search.html' + (q ? '?q='+encodeURIComponent(q) : '');
    });
  }
})();
