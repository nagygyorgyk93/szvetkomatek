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
