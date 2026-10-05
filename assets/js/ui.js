/* Szvetkó matek — közös UI: progress, TOC, nyomtatás, mini-kereső.
   Minden oldal <html data-root="..."> attribútummal adja meg a gyökérhez
   vezető relatív utat ('.', '..' vagy '../..'). */
(function(){
  'use strict';
  var ROOT = document.documentElement.getAttribute('data-root') || '.';

  /* A képletes gombok és fejlécek neve a MathML szerkezetét is őrizze meg:
     a sima textContent például egy törtet vagy gyököt puszta számnak olvasna. */
  function matekNev(el, csoportAlap){
    var gyerekek = Array.prototype.slice.call(el.children || []);
    var reszek = gyerekek.map(function(c){ return matekNev(c); }), jel = (el.localName || '').toLowerCase();
    var szoveg = (el.textContent || '').trim();
    if(jel === 'mrow'){
      /* A KaTeX a sima (x-4)^2 alapjaként csak a zárójelet adja át.
         A párjától kezdődő egész csoportot tartjuk együtt. */
      var lista = [], nyitott = [], parok = {')':'(',']':'[','}':'{'};
      gyerekek.forEach(function(c){
        var tag = c.localName, t = (c.textContent || '').trim(), alap = c.firstElementChild;
        var zaro = /^(msup|msub|msubsup)$/.test(tag) && alap && alap.localName === 'mo'
          ? (alap.textContent || '').trim() : '';
        if(zaro && nyitott.length && parok[zaro] === nyitott[nyitott.length-1].jel){
          var kezdet = nyitott.pop().hely;
          lista.push(matekNev(c, lista.splice(kezdet).join(' ')+' '+zaro));
        } else {
          if(tag === 'mo' && /^[([{]$/.test(t)) nyitott.push({jel:t,hely:lista.length});
          else if(tag === 'mo' && nyitott.length && parok[t] === nyitott[nyitott.length-1].jel) nyitott.pop();
          lista.push(matekNev(c));
        }
      });
      var csakSzoveg = gyerekek.every(function(c){
        return c.localName === 'mtext' || (c.localName === 'mover' && c.firstElementChild.localName === 'mtext');
      });
      return lista.join(csakSzoveg ? '' : ' ');
    }
    if(csoportAlap) reszek[0] = csoportAlap;
    if(jel === 'annotation' || jel === 'annotation-xml' || jel === 'mphantom') return '';
    if(jel === 'semantics') return reszek[0] || '';
    if(jel === 'mfrac'){
      if(parseFloat(el.getAttribute('linethickness')) === 0){
        var sor = el.parentElement, binom = sor && sor.children.length === 3
          && sor.firstElementChild.textContent === '(' && sor.lastElementChild.textContent === ')';
        return (binom ? 'binomiális együttható' : 'egymás alá írt kifejezések')+
          ': felső ('+reszek[0]+'), alsó ('+reszek[1]+')';
      }
      return 'tört: számláló ('+reszek[0]+'), nevező ('+reszek[1]+')';
    }
    if(jel === 'msqrt') return 'négyzetgyök ('+reszek.join(' ')+')';
    if(jel === 'mroot') return reszek[1]+'-edik gyök ('+reszek[0]+')';
    if(jel === 'msup'){
      var felso = gyerekek[1].textContent.replace(/\s/g, '');
      var also = gyerekek[0].textContent.replace(/[\u2061-\u2064]/g, '').trim();
      if(felso === '∘') return reszek[0]+' fok';
      if(/^′+$/.test(felso)) return reszek[0]+(/^[fg]$/.test(also)
        ? (felso.length === 1 ? ' első deriváltja' : felso.length === 2 ? ' második deriváltja' : ' '+felso.length+'-edik deriváltja')
        : ' '+felso.length+' vessző');
      if(felso === '−1'){
        var arkusz = {sin:'arkuszszinusz',cos:'arkuszkoszinusz',tg:'arkusztangens',ctg:'arkuszkotangens'};
        if(arkusz[also]) return arkusz[also];
        if(/^[fg]$/.test(also) && el.nextElementSibling && el.nextElementSibling.textContent === '(') return reszek[0]+' inverze';
      }
      return 'hatvány: alap ('+reszek[0]+'), kitevő ('+reszek[1]+')';
    }
    if(jel === 'msub') return reszek[0]+' alsó index ('+reszek[1]+')';
    if(jel === 'msubsup') return reszek[0]+' alsó index ('+reszek[1]+'), felső index ('+reszek[2]+')';
    if(jel === 'munder') return reszek[0]+' alsó jel ('+reszek[1]+')';
    if(jel === 'mover'){
      var ekezetek = {'ˊ':'\u0301','´':'\u0301','¨':'\u0308','˝':'\u030b'};
      if(gyerekek[0].localName === 'mtext' && ekezetek[gyerekek[1].textContent])
        return (gyerekek[0].textContent+ekezetek[gyerekek[1].textContent]).normalize('NFC');
      if(/[⃗→]/.test(gyerekek[1].textContent)) return reszek[0]+' vektor';
      return reszek[0]+' felső jel ('+reszek[1]+')';
    }
    if(jel === 'munderover') return reszek[0]+' alsó jel ('+reszek[1]+'), felső jel ('+reszek[2]+')';
    if(jel === 'mtable') return 'mátrix vagy soronkénti kifejezés: '+reszek.join('; ');
    if(jel === 'mtr') return 'sor: '+reszek.join(', ');
    if(jel === 'mo'){
      var jelek = {'+':'plusz','−':'mínusz','=':'egyenlő','≠':'nem egyenlő',
        '<':'kisebb, mint','>':'nagyobb, mint','≤':'kisebb vagy egyenlő, mint',
        '≥':'nagyobb vagy egyenlő, mint','×':'szorzás keresztjellel','⋅':'szorzás pontjellel','/':'per',
        '∪':'unió','∩':'metszet','∈':'eleme','∉':'nem eleme','∅':'üres halmaz',
        '∖':'halmazkülönbség','△':'szimmetrikus különbség','∞':'végtelen',
        '¯':'felső vonás','→':'nyíl','⇒':'esetén következik, hogy','⇔':'akkor és csak akkor',
        '≈':'közelítőleg egyenlő','∧':'és','∨':'vagy','¬':'nem'};
      return jelek[szoveg] || szoveg.replace(/[\u2061-\u2064]/g, ' ');
    }
    return gyerekek.length ? reszek.join(' ') : szoveg;
  }
  function felolvasas(el){
    if(el.nodeType === 3) return el.textContent;
    if(el.nodeType !== 1 || el.getAttribute('aria-hidden') === 'true') return '';
    if(el.classList.contains('katex')){
      var ml = el.querySelector('math');
      return ml ? matekNev(ml) : '';
    }
    return Array.prototype.map.call(el.childNodes, felolvasas).join(' ');
  }
  document.querySelectorAll('.opciok button, th').forEach(function(el){
    if(el.querySelector('.katex') && !el.hasAttribute('aria-label') && !el.hasAttribute('aria-labelledby')){
      var nev = felolvasas(el).replace(/\s+/g, ' ').trim();
      if(nev){
        el.setAttribute('aria-label', nev);
        if(el.tagName === 'TH'){
          /* A táblázatfejléc szöveges alternatívája azoknak a felolvasóknak is
             elérhető, amelyek a fejléc tartalmából, nem az aria-labelből olvasnak. */
          var sz = document.createElement('span'); sz.className = 'felolvasas';
          sz.textContent = nev; el.appendChild(sz);
        }
      }
    }
  });
  /* Az üres sarok vagy elválasztó nem fejléc: a táblázat adatait nem nevezi meg. */
  document.querySelectorAll('th').forEach(function(el){
    if(!el.textContent.trim() && !el.children.length && !el.hasAttribute('aria-label') && !el.hasAttribute('aria-labelledby')){
      var cella = document.createElement('td');
      Array.prototype.forEach.call(el.attributes, function(a){ cella.setAttribute(a.name, a.value); });
      cella.innerHTML = el.innerHTML; el.replaceWith(cella);
    }
  });

  /* Ugrás a főtartalomra, ismétlődő fejléc kihagyásával. */
  function azonosit(el, alap){
    if(el.id) return el.id;
    var id = alap, n = 1;
    while(document.getElementById(id)) id = alap+'-'+n++;
    el.id = id; return id;
  }
  var fo = document.querySelector('main');
  if(fo){
    var ugr = document.createElement('a');
    ugr.className = 'tartalomra'; ugr.href = '#'+azonosit(fo, 'fo-tartalom');
    ugr.textContent = 'Ugrás a főtartalomra';
    document.body.insertBefore(ugr, document.body.firstChild);
    fo.setAttribute('tabindex', '-1');
    ugr.addEventListener('click', function(ev){ ev.preventDefault(); fo.focus(); });
  }
  var hero = document.querySelector('.hero'), focim = hero && hero.querySelector('h1');
  if(focim){
    hero.setAttribute('role', 'region');
    hero.setAttribute('aria-labelledby', azonosit(focim, 'oldalcim'));
  }
  document.querySelectorAll('nav.morzsa').forEach(function(n){ n.setAttribute('aria-label', 'Útvonal'); });

  /* Csak a ténylegesen gördülő doboz kerül a Tab-sorrendbe. A lenyílók és a
     betűkészletek betöltése után, valamint átméretezéskor újramérjük. */
  function gordithetok(){
    document.querySelectorAll('.tblwrap, .katex-display').forEach(function(el){
      var tul = el.clientWidth > 0 && el.scrollWidth > el.clientWidth;
      if(tul && !el.hasAttribute('tabindex')){
        el.setAttribute('tabindex', '0'); el.setAttribute('data-gorditheto', '1');
        el.setAttribute('role', 'group');
        el.setAttribute('aria-label', el.classList.contains('tblwrap') ? 'Gördíthető táblázat' : 'Gördíthető képlet');
      } else if(!tul && el.getAttribute('data-gorditheto') === '1'){
        ['tabindex','data-gorditheto','role','aria-label'].forEach(function(a){ el.removeAttribute(a); });
      }
    });
  }
  gordithetok(); window.addEventListener('resize', gordithetok);
  document.addEventListener('toggle', gordithetok, true);
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(gordithetok);
  if(document.fonts && document.fonts.addEventListener) document.fonts.addEventListener('loadingdone', gordithetok);

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
    var vezerlok = document.createElement('div'); vezerlok.className = 'video-vezerlok';
    gomb.parentNode.insertBefore(vezerlok, gomb); vezerlok.appendChild(gomb);
    var szunet = document.createElement('button');
    szunet.type = 'button'; szunet.className = 'szunet-gomb';
    szunet.setAttribute('aria-controls', v.id); vezerlok.appendChild(szunet);
    function szunetFrissit(){ szunet.textContent = v.paused ? 'Videó folytatása' : 'Videó szüneteltetése'; }
    szunet.addEventListener('click', function(){
      if(v.paused){ var p = v.play(); if(p && p.catch) p.catch(function(){}); }
      else v.pause();
    });
    v.addEventListener('play', szunetFrissit); v.addEventListener('pause', szunetFrissit);
    if(lassit){ v.loop = false; v.autoplay = false; v.pause(); }
    v.muted = true; v.defaultMuted = true;   /* a néma automata indítás feltétele */
    if(!lassit) nemaInditas();
    szunetFrissit();

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
      if(lassit) v.pause();
      else { var p3 = v.play(); if(p3 && p3.catch) p3.catch(function(){}); }
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
      var logo = document.querySelector('.logo');
      if(logo) logo.focus({preventScroll:true});
      g.classList.add('kilo');
      setTimeout(function(){ g.classList.remove('kilo'); }, 700);
    });
    var lat = function(){ g.classList.toggle('mutat', document.documentElement.scrollTop > 600); };
    document.addEventListener('scroll', lat, {passive:true}); lat();
  })();

  /* „/” → ugrás a keresőbe (ha épp nem beviteli mezőben vagyunk) */
  document.addEventListener('keydown', function(ev){
    if(ev.key !== '/' || ev.ctrlKey || ev.altKey || ev.metaKey) return;
    if(window.Naplo && !window.Naplo.gyorskeresoBe()) return;
    var a = document.activeElement;
    if(a && /^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName)) return;
    if(a && a.isContentEditable) return;
    var mezo = Array.prototype.find.call(document.querySelectorAll('.kereso-mini input, .kereso-nagy input'),
      function(el){ return el.getClientRects().length > 0; });
    if(mezo){ ev.preventDefault(); mezo.focus(); mezo.select(); }
    else { ev.preventDefault(); window.location.href = ROOT + '/search.html'; }
  });

  /* Küldetésnapló + mikro-animációk betöltése (így nem kell minden oldal
     <head>-jébe felvenni őket) */
  /* beagyazas.js: csak ha a lapon van külső média (videó / GeoGebra) */
  var szkriptek = ['naplo.js', 'effekt.js'];
  if (document.querySelector('figure.media')) szkriptek.push('beagyazas.js');
  szkriptek.forEach(function(f){
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
