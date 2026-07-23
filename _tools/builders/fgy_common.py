# -*- coding: utf-8 -*-
"""Közös HTML-építő a topic-1 feladatgyűjteményekhez (Szvetkó matek) — v2.
Feladat = (intro, subs, ans[, rovid]) :
  intro : str (felvezető mondat)
  subs  : list[str] részfeladatok (egymás alá; rovid=True → egymás mellé, tágas) VAGY None
  ans   : str (egy bekezdés) VAGY list[str] (részfeladatonként, egymás alá)
  rovid : bool (rövid részfeladatok egymás mellé)
"""
import re, os, glob
DEST=glob.glob("/sessions/*/mnt/Claude/web/1e/01-logika-halmazok-fuggvenyek")[0]
def w(t): return re.sub(r'\$([^$]*)\$', r'<span class="math inline">\\(\1\\)</span>', t)

def _subs(subs, rovid):
    if not subs: return ''
    cls = 'reszfeladatok rovid' if rovid else 'reszfeladatok'
    return f'<ol class="{cls}">' + ''.join(f'<li>{w(s)}</li>' for s in subs) + '</ol>'

def _ans(ans):
    if isinstance(ans,(list,tuple)):
        return '<div class="bel"><ol class="reszfeladatok">' + ''.join(f'<li>{w(a)}</li>' for a in ans) + '</ol></div>'
    return f'<div class="bel"><p>{w(ans)}</p></div>'

def _one(prefix, i, chip, it):
    intro, subs, ans = it[0], it[1], it[2]
    rovid = it[3] if len(it) > 3 else False
    lvl = f' {chip}' if chip else ''
    szam = '★' if prefix == 'joker' else f'{i}.'
    idattr = 'joker' if prefix == 'joker' else f'{prefix}-{i}'
    return f'''    <article class="feladat{lvl}" id="{idattr}">
      <p><span class="szam">{szam}</span> {w(intro)}</p>{_subs(subs, rovid)}
      <details class="vegeredmeny"><summary>Végeredmény</summary>
        {_ans(ans)}
      </details>
    </article>'''

def cards(items, prefix, chip):
    return "\n".join(_one(prefix, i, chip, it) for i, it in enumerate(items, 1))

def gyt_cards(items, prefix="gyt"):
    return "\n".join(_one(prefix, i, None, it) for i, it in enumerate(items, 1))

def joker_card(intro, ans, subs=None):
    return _one('joker', 1, 'joker', (intro, subs, ans))

def page(fname, altema_cim, tananyag_link, sections_html, prev, prevc, nxt, nxtc):
    alcim="Három szint: haladj sorban, vagy ugorj a szintedre. A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!"
    html=f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{altema_cim} — feladatok | 1e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="1e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">√</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főoldal</a> ›
  <a href="../index.html"><span class="tagozat-jel">1e</span></a> ›
  <a href="index.html">Logika, halmazok, függvények</a> ›
  <span class="itt">{altema_cim} — feladatok</span>
</nav>
<div class="hero">
  <h1>{altema_cim} — feladatgyűjtemény</h1>
  <p class="alcim">{w(alcim)}</p>
  <div class="meta-sor">
    <span class="chip alap">Alap</span><span class="chip kozep">Közép</span>
    <span class="chip nehez">Nehéz</span><span class="chip joker">Joker</span>
  </div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
{sections_html}
    <div class="gyakorolj">
      <span class="ikon">📖</span>
      <p>Elakadtál? Nézd át a <a href="{tananyag_link}">tananyagot</a> vagy a <a href="osszefoglalo.html">tömör összefoglalót</a>.</p>
    </div>
    <div class="lapozo">
      <a class="elozo" href="{prev}"><span class="irany">← Előző</span><span class="hova">{prevc}</span></a>
      <a class="kov" href="{nxt}"><span class="irany">Következő →</span><span class="hova">{nxtc}</span></a>
    </div>
  </div>
  <nav class="toc" id="toc" aria-label="Tartalomjegyzék"></nav>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {{delimiters:[
    {{left:'\\\\(', right:'\\\\)', display:false}},
    {{left:'\\\\[', right:'\\\\]', display:true}}
  ]}});
</script>
<script src="../../assets/js/ui.js"></script>
<script src="../../assets/js/quiz.js"></script>
</body>
</html>
'''
    open(os.path.join(DEST,fname),"w",encoding="utf-8").write(html)
    return fname
