# -*- coding: utf-8 -*-
"""4e/02 — A blokk: az elemi fuggvenyek (A1), ertelmezesi tartomany, zerushely, elojel (A2),
paritas, periodicitas, monotonitas (A3). Mentor: Nagol (Ved Vilmos kommental).
Kuldetes: Az Aszimptota-fal Attorese. Specifikacio: projektek/4e/munkafajlok/narrativa_02-fuggvenyek.md
Osszetett es inverz fuggveny NINCS (felhasznaloi dontes); periodicitasbol feladat nincs; monotonitas csak grafikonrol."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="4e", mappa="02-fuggvenyek", temakor="Függvények")
KUL = "Az Aszimptota-fal Áttörése"
FT = "feladatok-tulajdonsagok.html"
E101 = "../../1e/01-logika-halmazok-fuggvenyek/"
E202 = "../../2e/02-masodfoku-egyenletek-es-fuggvenyek/"
E203 = "../../2e/03-exponencialis-es-logaritmus-fuggveny/"
E204 = "../../2e/04-trigonometrikus-fuggvenyek/"
KEK, BORO, ZOLD, PIROS, LILA, SOT = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#7c3aed", "#0f172a"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FT}#nehez-{tol}">Zsoldos-lista I., nehéz {tol}–{ig}</a>.</p>')


# ---------------------------------------------------------------- önteszt
from sympy import (symbols, solve, solveset, S, Interval, Union, oo, sqrt, log, simplify, sin, cos,
                   Rational as R, reduce_inequalities, And)
E = []


def chk(nev, kapott, vart):
    if not (kapott == vart or (hasattr(kapott, "equals") and kapott.equals(vart))):
        E.append((nev, kapott, vart))


x = symbols("x", real=True)
# A2 — értelmezési tartomány
chk("A2-pelda-1", solveset(x + 3 >= 0, x, S.Reals) - {2}, Union(Interval(-3, 2, False, True), Interval.open(2, oo)))
chk("A2-pelda-2", solveset(x**2 - 4*x > 0, x, S.Reals), Union(Interval.open(-oo, 0), Interval.open(4, oo)))
chk("A2-kviz-1", solve(x - 5, x), [5])
chk("A2-zerus", [r for r in solve(x**2 - 9, x) if (r - 3) != 0], [-3])
chk("A2-elojel", solveset((x + 1)*(x - 3)/(x - 1) > 0, x, S.Reals), Union(Interval.open(-1, 1), Interval.open(3, oo)))
chk("A2-kviz-3", solveset((x - 2)**2*(x + 1) < 0, x, S.Reals), Interval.open(-oo, -1))
# A3 — paritás
f1, f2, f3, f4 = x**4 - 3*x**2, x**3 + 2*x, x**2 + x, x*sin(x)
chk("A3-paros", simplify(f1.subs(x, -x) - f1), 0)
chk("A3-paratlan", simplify(f2.subs(x, -x) + f2), 0)
chk("A3-egyik-sem", [simplify(f3.subs(x, -x) - f3) == 0, simplify(f3.subs(x, -x) + f3) == 0], [False, False])
chk("A3-xsinx", simplify(f4.subs(x, -x) - f4), 0)
chk("A3-kviz-1", [((-1)**2 - 2*(-1)) , (1**2 - 2*1)], [3, -1])      # g(x)=x²−2x: g(−1)=3, g(1)=−1 → nem páros
chk("A3-x3p1", [simplify((x**3 + 1).subs(x, -x) + (x**3 + 1)) == 0], [False])
# A3 — grafikonelemzés (töröttvonal)
PT = [(-3, -2), (-1, 2), (2, -1), (4, 3)]


def tv(t):
    for (a, b), (c, d) in zip(PT, PT[1:]):
        if a <= t <= c:
            return b + (d - b) * (t - a) / (c - a)
    raise ValueError


chk("A3-zerusok", [tv(-2), tv(1), tv(2.5)], [0, 0, 0])
chk("A3-ertekkeszlet", (min(p[1] for p in PT), max(p[1] for p in PT)), (-2, 3))
# A1 — névjegyek
chk("A1-log", [math.log2(1), math.log2(8)], [0, 3])
chk("A1-exp", [2**0, 2**3], [1, 8])
assert not E, E
print("önteszt: OK")


# ---------------------------------------------------------------- ábrák
def svg_szamegyenes(savok, pontok, xr=(-5, 6), w=360, h=92, leiras="Számegyenes"):
    """savok = [(lo, hi, szin, y_eltolas, felirat)], pontok = [(x, "teli"|"ures", szin)]."""
    bal, jobb = 18, 18
    X = lambda t: bal + (t - xr[0]) / (xr[1] - xr[0]) * (w - bal - jobb)
    y0 = h - 26
    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}">',
          '  <defs><marker id="nyilsz" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" markerHeight="6" '
          'orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker></defs>',
          f'  <line x1="{X(xr[0]):.1f}" y1="{y0}" x2="{X(xr[1]):.1f}" y2="{y0}" stroke="#0f172a" '
          'stroke-width="1.4" marker-end="url(#nyilsz)"/>']
    for t in range(int(xr[0]) + 1, int(xr[1])):
        ki.append(f'  <line x1="{X(t):.1f}" y1="{y0 - 4}" x2="{X(t):.1f}" y2="{y0 + 4}" stroke="#0f172a"/>')
        ki.append(f'  <text x="{X(t):.1f}" y="{y0 + 17}" font-size="10" fill="#475569" text-anchor="middle">{t}</text>')
    for lo, hi, szin, dy, felirat in savok:
        a, b = X(max(lo, xr[0])), X(min(hi, xr[1] - 0.3))
        ki.append(f'  <line x1="{a:.1f}" y1="{y0 - dy}" x2="{b:.1f}" y2="{y0 - dy}" stroke="{szin}" '
                  'stroke-width="5" stroke-linecap="round" opacity=".85"/>')
        if felirat:
            ki.append(f'  <text x="{b + 4:.1f}" y="{y0 - dy + 4}" font-size="10" fill="{szin}">{felirat}</text>')
    for t, tipus, szin in pontok:
        kit = "#ffffff" if tipus == "ures" else szin
        ki.append(f'  <circle cx="{X(t):.1f}" cy="{y0}" r="4.2" fill="{kit}" stroke="{szin}" stroke-width="1.8"/>')
    ki.append('</svg>')
    return "\n".join(ki)


SVG_HATVANY = svg_fuggvenyek(
    [(lambda t: t**2, KEK, "y = x²", [(-2.1, 2.1)]), (lambda t: t**3, PIROS, "y = x³", [(-1.7, 1.7)]),
     (lambda t: math.sqrt(t), ZOLD, "y = √x", [(0, 3.3)])],
    xr=(-2.6, 3.4), yr=(-3, 4.2), w=380, h=260,
    leiras="Az y = x², y = x³ és y = √x grafikonja: a négyzetfüggvény parabola, a köbfüggvény negatív x-re az x "
           "tengely alatt halad, a gyökfüggvény csak a nemnegatív számokon van értelmezve")
SVG_RECIPROK = svg_fuggvenyek(
    [(lambda t: 1 / t, LILA, "y = 1/x", [(-3.2, -0.22), (0.22, 3.2)])],
    xr=(-3.4, 3.4), yr=(-3.6, 3.6), w=340, h=250,
    leiras="Az y = 1/x hiperbola két ága; a 0-ban nincs értelmezve")
SVG_EXPLOG = svg_fuggvenyek(
    [(lambda t: 2**t, KEK, "y = 2ˣ", [(-3, 2.2)]), (lambda t: 0.5**t, BORO, "y = (1/2)ˣ", [(-2.2, 3)]),
     (lambda t: math.log2(t), ZOLD, "y = log₂ x", [(0.06, 4.2)])],
    xr=(-3.2, 4.4), yr=(-3, 4.6), w=390, h=270,
    pontok=[(0, 1, "(0; 1)", SOT, 6, -8), (1, 0, "(1; 0)", SOT, 4, 14)],
    leiras="Az y = 2ˣ, az y = (1/2)ˣ és az y = log₂ x grafikonja; az exponenciális görbék a (0; 1), "
           "a logaritmusgörbe az (1; 0) ponton megy át")
SVG_TRIG = svg_fuggvenyek(
    [(lambda t: math.sin(t), KEK, "y = sin x", [(-6.3, 6.3)]), (lambda t: math.cos(t), PIROS, "y = cos x", [(-6.3, 6.3)])],
    xr=(-6.6, 6.8), yr=(-1.8, 2.2), w=420, h=190, egyseg=("1", "1"),
    leiras="A szinusz- és a koszinuszfüggvény grafikonja két periódusnyi hosszon; értékük −1 és 1 között van")
SVG_KITALALOS = svg_fuggvenyek(
    [(lambda t: 3**t, KEK, "A", [(-3, 1.3)]), (lambda t: t**3 - 1, PIROS, "B", [(-1.3, 1.7)]),
     (lambda t: math.log(t, 3), ZOLD, "C", [(0.05, 4.2)])],
    xr=(-3.2, 4.4), yr=(-3, 4.4), w=380, h=260,
    leiras="Három grafikon A, B, C betűvel: az A a (0; 1) ponton megy át és balra a 0-hoz simul, a B az "
           "(1; 0) és a (0; −1) ponton, a C az (1; 0) ponton megy át és csak pozitív x-re létezik")

SVG_METSZET = svg_szamegyenes(
    [(-3, 5.7, KEK, 22, ""), (-4.7, 1.8, PIROS, 36, ""), (2.2, 5.7, PIROS, 36, ""),
     (-3, 1.8, ZOLD, 10, ""), (2.2, 5.7, ZOLD, 10, "")],
    [(-3, "teli", ZOLD), (2, "ures", ZOLD)], xr=(-5, 6), h=96,
    leiras="Számegyenes: kék sáv x ≥ −3, piros sáv x ≠ 2, zöld sáv a kettő közös része: [−3; 2) és (2; ∞)")
SVG_TORT_ELOJEL = svg_fuggvenyek(
    [(lambda t: (t + 1) * (t - 3) / (t - 1), KEK, "y = (x+1)(x−3)/(x−1)", [(-3.2, 0.93), (1.07, 5.2)]),
    ],
    xr=(-3.4, 5.4), yr=(-5, 5), w=380, h=260,
    pontok=[(-1, 0, "−1", ZOLD, -14, -8), (3, 0, "3", ZOLD, 4, -8)],
    leiras="Az y = (x+1)(x−3)/(x−1) grafikonja: zérushelyek −1 és 3, az 1-ben nincs értelmezve; a görbe a "
           "−1 < x < 1 és az x > 3 helyeken az x tengely fölött, máshol alatta van")
SVG_PAROS = svg_fuggvenyek(
    [(lambda t: t**4 - 3 * t**2, KEK, "y = x⁴ − 3x²", [(-1.95, 1.95)]),
     (lambda t: t**3 + 2 * t, PIROS, "y = x³ + 2x", [(-1.3, 1.3)])],
    xr=(-2.4, 2.4), yr=(-3.2, 3.6), w=360, h=260,
    leiras="Egy páros függvény (az y tengelyre szimmetrikus) és egy páratlan függvény (az origóra szimmetrikus) grafikonja")
SVG_ELEMZES = svg_fuggvenyek(
    [(tv, SOT, "f", [(-3, 4)])], xr=(-3.6, 4.6), yr=(-2.8, 3.8), w=380, h=260, jelmagyarazat=False,
    pontok=[(-3, -2, "", SOT), (4, 3, "", SOT)],
    leiras="Az f függvény grafikonja a [−3; 4] intervallumon: a (−3; −2), (−1; 2), (2; −1), (4; 3) pontokat "
           "összekötő töröttvonal")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Az I.V.H. személyazonosság-ellenőrzést tart. Minden függvénynek fel kell mutatnia a '
         '<b>névjegyét</b>: hol van értelmezve, milyen értékeket vesz fel, és hogyan néz ki a grafikonja. '
         '<b>Véd Vilmos:</b> Ismerem mindet, tavaly együtt buliztunk. <b>Nagol:</b> Akkor mondd meg, hol nincs '
         'értelmezve a logaritmus. <b>Véd Vilmos:</b> … a hétvégén? Ebben a fejezetben egyébként egy falba '
         'fogok ütközni, amit soha nem érek el. Az aszimptotáról van szó — de előbb ismerkedjünk.'),
 ]),

 ("Emlékeztető: mi a függvény?", [
   r'<p class="lead">A <b>függvény</b> egy halmaz minden eleméhez pontosan egy értéket rendel. Az a halmaz, '
   r'amelynek elemeihez hozzárendelünk, az <b>értelmezési tartomány</b> ($D_f$); a felvett értékek halmaza az '
   r'<b>értékkészlet</b> ($R_f$). A <b>grafikon</b> az $\big(x;\,f(x)\big)$ pontok összessége.</p>'
   r'<p>Ha bármelyik bizonytalan, itt az elsős anyag: '
   '<a href="' + E101 + 'tananyag-fuggveny-fogalma.html">a függvény fogalma</a> · '
   '<a href="' + E101 + 'tananyag-fuggvenytulajdonsagok.html">a függvények tulajdonságai</a>.</p>',
   doboz("definicio", "Az elemi függvények",
         r'<p><b>Elemi függvénynek</b> nevezzük az alapfüggvényeket — a konstans, a hatvány- és a '
         r'gyökfüggvények, az exponenciális és a logaritmusfüggvény, a trigonometrikus függvények —, '
         r'valamint mindazokat, amelyek ezekből a négy alapművelettel és egymásba helyettesítéssel (pl. '
         r'$\sqrt{x+4}$, $\lg(x^2-4x)$, $x\sin x$) véges sok lépésben felépíthetők.</p>',
         hid="def-elemi"),
 ]),

 ("Hatványfüggvények és a gyökfüggvény", [
   r'<p class="lead">Az $y=x^n$ ($n$ pozitív egész) függvény grafikonja a kitevő paritásán múlik. <b>Páros</b> '
   r'$n$-re a grafikon az $y$ tengelyre szimmetrikus, és sosem megy az $x$ tengely alá; <b>páratlan</b> $n$-re '
   r'az origóra szimmetrikus, és negatív $x$-re az $x$ tengely alatt halad.</p>',
   abra(SVG_HATVANY, 'A négyzet-, a köb- és a négyzetgyökfüggvény.'),
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>függvény</th><th>$D_f$</th><th>$R_f$</th><th>zérushely</th></tr>'
   r'<tr><td>$y=x^2$ (páros kitevő)</td><td>$\mathbb R$</td><td>$[0;\,\infty)$</td><td>$0$</td></tr>'
   r'<tr><td>$y=x^3$ (páratlan kitevő)</td><td>$\mathbb R$</td><td>$\mathbb R$</td><td>$0$</td></tr>'
   r'<tr><td>$y=\sqrt x$</td><td>$[0;\,\infty)$</td><td>$[0;\,\infty)$</td><td>$0$</td></tr>'
   r'<tr><td>$y=\dfrac1x$</td><td>$\mathbb R\setminus\{0\}$</td><td>$\mathbb R\setminus\{0\}$</td><td>nincs</td></tr>'
   r'</table></div>',
   abra(SVG_RECIPROK, 'Az $y=\\frac1x$ grafikonja két ágból áll; a $0$-ban nincs értelmezve.'),
   kviz(r'Melyik állítás igaz az $y=x^3$ függvény grafikonjára?',
        [r'negatív $x$-re a görbe az $x$ tengely alatt halad',
         r'ugyanolyan alakú, mint az $y=x^2$ parabola, csak meredekebb',
         r'az $y$ tengelyre szimmetrikus',
         r'negatív $x$-re nincs értelmezve'], 0,
        jo="✔ Páratlan kitevőnél a negatív szám köbe negatív: (−2)³ = −8. A grafikon az origóra szimmetrikus.",
        nem="✘ A páratlan kitevő megtartja az előjelet: (−2)³ = −8, míg (−2)² = 4. Az x³ grafikonja "
            "ezért a negatív oldalon lefelé megy, és az origóra szimmetrikus."),
 ]),

 ("Az exponenciális és a logaritmusfüggvény", [
   r'<p class="lead">Az $y=a^x$ ($a\gt0$, $a\ne1$) <b>exponenciális függvény</b> minden valós számra '
   r'értelmezve van, és csak pozitív értékeket vesz fel. Ha $a\gt1$, növekvő; ha $0\lt a\lt1$, csökkenő. '
   r'Mindegyik grafikon átmegy a $(0;\,1)$ ponton, mert $a^0=1$.</p>'
   r'<p>Az $y=\log_a x$ <b>logaritmusfüggvény</b> csak <b>pozitív</b> számokra értelmezett, értékkészlete '
   r'viszont a teljes $\mathbb R$. Grafikonja átmegy az $(1;\,0)$ ponton, mert $\log_a1=0$. Részletesen: '
   '<a href="' + E203 + 'tananyag-exponencialis-fuggveny.html">az exponenciális függvény</a> (2e).</p>',
   abra(SVG_EXPLOG, 'Az exponenciális görbék a $(0;\\,1)$ ponton mennek át, a logaritmusgörbe az $(1;\\,0)$ ponton.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „$\log_2 0=0$, hiszen a nulla logaritmusa nulla”, és a $\log_2(-8)$-ra is '
         r'kiszámol valamit.</p>'
         r'<p><b>A logaritmus csak pozitív számra értelmes.</b> Nincs olyan kitevő, amelyre $2$-t emelve $0$-t '
         r'vagy negatív számot kapnánk, ezért $\log_2 0$ és $\log_2(-8)$ nem létezik. A $0$-hoz közeledve a '
         r'logaritmus a $-\infty$ felé zuhan — ez lesz az első aszimptotánk.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Exponenciálisan nő a kamatos kamatozású betét és egy baktériumtenyészet, exponenciálisan '
         r'fogy a radioaktív anyag. A logaritmus pedig ott van a földrengések Richter-skáláján (egy egység '
         r'tízszeres kitérés) és a decibel-skálán (10 dB tízszeres hangintenzitás).</p>'),
 ]),

 ("A trigonometrikus függvények", [
   r'<p class="lead">A $\sin x$ és a $\cos x$ minden valós számra értelmezett, értékkészletük $[-1;\,1]$, '
   r'és $2\pi$ hosszanként ismétlődnek. A $\operatorname{tg} x=\dfrac{\sin x}{\cos x}$ ott nincs értelmezve, '
   r'ahol $\cos x=0$, vagyis az $x=\dfrac\pi2+k\pi$ $(k\in\mathbb Z)$ helyeken; értékkészlete $\mathbb R$, és $\pi$ '
   r'hosszanként ismétlődik. Részletesen: '
   '<a href="' + E204 + 'tananyag-trig-fuggvenyek-grafikonja.html">a trigonometrikus függvények grafikonja</a> (2e).</p>',
   abra(SVG_TRIG, 'A szinusz és a koszinusz: hullám $-1$ és $1$ között.'),
 ]),

 ("Melyik képlet melyik grafikon?", [
   r'<p class="lead">A grafikonról a képletet jellegzetes pontok és viselkedés alapján azonosítjuk: hol '
   r'metszi a tengelyeket, hol nincs értelmezve, merre halad a két széle.</p>',
   abra(SVG_KITALALOS, 'Három grafikon — melyik melyik képlethez tartozik?'),
   doboz("pelda", "I.V.H. Akták — grafikon és képlet",
         r'<p>Párosítsuk a grafikonokat az $y=3^x$, az $y=x^3-1$ és az $y=\log_3 x$ képlettel!</p>'
         r'<ul><li><b>A:</b> átmegy a $(0;1)$ ponton, balra a $0$-hoz simul, jobbra meredeken nő → $y=3^x$.</li>'
         r'<li><b>B:</b> minden valós számra értelmezett, a $(0;-1)$ és az $(1;0)$ ponton megy át → $y=x^3-1$.</li>'
         r'<li><b>C:</b> csak pozitív $x$-re létezik, és az $(1;0)$ ponton megy át → $y=\log_3 x$.</li></ul>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „egy pont nem elég — a B és a C is átmegy az $(1;0)$-n. Ilyenkor '
         r'a második pont vagy az értelmezési tartomány dönt.”</p>', hid="pelda-grafikon-keplet"),
   kviz(r'Egy grafikon átmegy az $(1;\,0)$ ponton. Melyik következtetés helyes?',
        [r'ebből egyedül még nem dönthető el, hogy $\log_a x$ vagy más függvény',
         r'biztosan logaritmusfüggvény, mert $\log_a 1=0$',
         r'biztosan exponenciális függvény',
         r'biztosan az $y=x-1$ egyenes'], 0,
        jo="✔ Sok függvény átmegy ezen a ponton (log, x³ − 1, x − 1, …). Kell egy második pont vagy a "
           "viselkedés, például hogy negatív x-re is létezik-e a görbe.",
        nem="✘ Egyetlen közös pont nem azonosít: az (1; 0)-n a logaritmus, az x³ − 1 és az x − 1 is átmegy. "
            "Nézz meg még egy pontot vagy az értelmezési tartományt."),
   GY(FT + "#alap-1", "A 1–4", FT + "#kozep-1", "K 1–2"),
   brief('<b>Nagol:</b> A névjegy első sora mindig az, <b>hol él</b> a függvény. A logaritmusnál láttuk, hogy '
         'ez nem mindig a teljes számegyenes. A következő leckében megtanuljuk kiszámolni is. '
         '<b>Véd Vilmos:</b> És ha a képletben egyszerre van tört, gyök és logaritmus? <b>Nagol:</b> Akkor '
         'mindhárom feltételnek teljesülnie kell.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Beírtam a számológépbe, hogy $\\sqrt{-4}$, és azt írta ki: ERROR. 🌮 '
         '<i>Burek-matek:</i> „szerintem $-2$, mert $(-2)^2=4$.” <b>Nagol:</b> Nem. A négyzetgyök nemnegatív '
         'számot ad, és negatív számra nincs értelmezve — a képletnek ott <b>nincs értelme</b>. Ma '
         'megtanuljuk előre megmondani, hol van értelme, hol nulla és hol pozitív egy függvény.'),
 ]),

 ("Mikor nincs értelme a képletnek?", [
   r'<p class="lead">Ha egy függvényt csak képlettel adunk meg, az <b>értelmezési tartománya</b> azoknak a '
   r'valós számoknak a halmaza, amelyekre a képlet kiszámolható. Iskolai függvényeknél három dologra '
   r'kell figyelni.</p>',
   doboz("tetel", "Az értelmezési tartomány három tiltása",
         r'<ul><li><b>Tört:</b> a nevező nem lehet $0$.</li>'
         r'<li><b>Páros gyök</b> ($\sqrt{\ }$, $\sqrt[4]{\ }$, …): a gyökjel alatti kifejezés nem lehet negatív ($\ge0$).</li>'
         r'<li><b>Logaritmus:</b> a logaritmus argumentuma (a $\log$ utáni kifejezés) csak pozitív lehet ($\gt0$).</li></ul>'
         r'<p>A polinomok, az exponenciális függvény, a $\sin$ és a $\cos$ minden valós számra értelmezett; a '
         r'$\operatorname{tg}x=\frac{\sin x}{\cos x}$ tört, ezért ott $\cos x\ne0$.</p>',
         hid="tetel-ert-tartomany"),
   kviz(r'Mi az $f(x)=\dfrac{3}{x-5}$ függvény értelmezési tartománya?',
        [r'$\mathbb R\setminus\{5\}$', r'$\mathbb R\setminus\{0\}$', r'$\mathbb R\setminus\{3\}$', r'$x\gt5$'], 0,
        jo="✔ A nevező x − 5, ez x = 5-nél nulla — csak ezt a számot kell kivenni.",
        nem="✘ Nem a számlálót és nem magát az x-et kell vizsgálni, hanem a nevezőt: x − 5 = 0 pontosan "
            "x = 5-nél. Minden más szám megengedett, a negatívak is."),
 ]),

 ("Több feltétel egyszerre", [
   r'<p class="lead">Ha a képletben több „veszélyes” rész van, <b>mindegyik</b> feltételnek egyszerre '
   r'teljesülnie kell: az értelmezési tartomány a feltételek <b>közös része</b> (metszete). Másodfokú '
   r'feltételnél a másodfokú egyenlőtlenség kell ('
   '<a href="' + E202 + 'tananyag-masodfoku-egyenlotlensegek.html">ismétlés, 2e</a>).</p>',
   doboz("pelda", "I.V.H. Akták — két feltétel metszete",
         r'<p>Határozzuk meg az $f(x)=\dfrac{\sqrt{x+3}}{x-2}$ függvény értelmezési tartományát!</p>'
         r'<ul><li>a gyök alatt: $x+3\ge0$, vagyis $x\ge-3$;</li>'
         r'<li>a nevező: $x-2\ne0$, vagyis $x\ne2$.</li></ul>'
         r'<p>A kettő együtt: $D_f=[-3;\,2)\cup(2;\,\infty)$.</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a $-3$ benne van (a gyök alatt lehet $0$), a $2$ nincs.”</p>',
         hid="pelda-ert-tartomany"),
   abra(SVG_METSZET, 'Kék: $x\\ge-3$; piros: $x\\ne2$; zöld: a közös rész. A $-3$ teli '
        'pont (benne van), a $2$ üres pont (kimarad).'),
   r'<p>Másodfokú feltétel: az $f(x)=\lg(x^2-4x)$ függvénynél $x^2-4x\gt0$, azaz $x(x-4)\gt0$. A parabola '
   r'felfelé nyílik, zérushelyei $0$ és $4$, tehát $D_f=(-\infty;\,0)\cup(4;\,\infty)$.</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos az $f(x)=\dfrac{\sqrt{x+3}}{x-2}$ függvénynél csak a nevezőt nézi, és '
         r'$D_f=\mathbb R\setminus\{2\}$-t ír — a $-10$-et is beírná.</p>'
         r'<p><b>Minden feltételnek teljesülnie kell.</b> A $-10$-re a nevező rendben van, de a gyök alatt '
         r'$-7$ állna. A feltételeket nem „vagy”, hanem „és” kapcsolja össze.</p>'),
   NEHEZ(1, 2, "értelmezési tartomány több feltétellel, tört a gyök alatt"),
 ]),

 ("Zérushelyek", [
   r'<p class="lead">A függvény <b>zérushelye</b> az az $x$, amelyre $f(x)=0$ — ott metszi a grafikon az '
   r'$x$ tengelyt. Zérushely <b>csak az értelmezési tartományban</b> lehet.</p>'
   r'<p>Törtnél: a tört akkor $0$, ha a <b>számlálója</b> $0$, a nevezője pedig nem. Például '
   r'$f(x)=\dfrac{x^2-9}{x-3}$ esetén a számláló $x=3$-ban és $x=-3$-ban nulla, de a $3$ nincs benne '
   r'$D_f$-ben — ezért az egyetlen zérushely $x=-3$.</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a $\dfrac{x^2-9}{x-3}$ zérushelyeinek a $3$-at és a $-3$-at adja meg — a $3$-at is, pedig '
         r'ott a nevező $0$.</p>'
         r'<p><b>Előbb az értelmezési tartomány, aztán a zérushely.</b> Ahol a nevező $0$, ott a függvény nincs '
         r'értelmezve, tehát zérushelye sem lehet.</p>'),
   kviz(r'Mik a $g(x)=\dfrac{x^2-4x}{x-4}$ függvény zérushelyei?',
        [r'csak $x=0$', r'$x=0$ és $x=4$', r'csak $x=4$', r'nincs zérushelye'], 0,
        jo="✔ A számláló x(x − 4), ez 0-ban és 4-ben nulla. A 4 viszont kiesik az értelmezési "
           "tartományból, így csak a 0 marad.",
        nem="✘ A számláló x(x − 4), de a 4-nél a nevező is nulla — ott a függvény nincs értelmezve. "
            "Zérushely csak a 0."),
 ]),

 ("Az előjel — előjeltáblázat", [
   r'<p class="lead">A függvény <b>pozitív</b>, ahol a grafikon a tengely fölött, és <b>negatív</b>, ahol '
   r'alatta van. Szorzatnál és törtnél az előjelet tényezőnként vizsgáljuk: a tényezők zérushelyei '
   r'szakaszokra bontják a számegyenest, és minden szakaszon összeszorozzuk az előjeleket.</p>',
   doboz("pelda", "I.V.H. Akták — egy tört előjele",
         r'<p>Vizsgáljuk meg az $f(x)=\dfrac{(x+1)(x-3)}{x-1}$ függvény előjelét! Kritikus pontok: $-1$, $1$, $3$.</p>'
         r'<div class="tblwrap"><table class="tt-table">'
         r'<tr><th></th><th>$x\lt-1$</th><th>$-1\lt x\lt1$</th><th>$1\lt x\lt3$</th><th>$x\gt3$</th></tr>'
         r'<tr><td>$x+1$</td><td>$-$</td><td>$+$</td><td>$+$</td><td>$+$</td></tr>'
         r'<tr><td>$x-3$</td><td>$-$</td><td>$-$</td><td>$-$</td><td>$+$</td></tr>'
         r'<tr><td>$x-1$</td><td>$-$</td><td>$-$</td><td>$+$</td><td>$+$</td></tr>'
         r'<tr><th>$f(x)$</th><td>$-$</td><td>$+$</td><td>$-$</td><td>$+$</td></tr></table></div>'
         r'<p>Tehát $f(x)\gt0$, ha $-1\lt x\lt1$ vagy $x\gt3$; $f(x)\lt0$, ha $x\lt-1$ vagy $1\lt x\lt3$; '
         r'zérushelyek: $-1$ és $3$; az $1$-ben nincs értelmezve.</p>', hid="pelda-elojeltabla"),
   abra(SVG_TORT_ELOJEL, 'A grafikon pontosan ott van a tengely fölött, ahol a táblázat „+” jelet ad.'),
   kviz(r'Hol negatív a $h(x)=(x-2)^2(x+1)$ függvény?',
        [r'ha $x\lt-1$', r'ha $-1\lt x\lt2$', r'ha $x\lt-1$ vagy $x\gt2$', r'ha $x\gt2$'], 0,
        jo="✔ A négyzet sosem negatív, így az előjelet egyedül az x + 1 dönti el: negatív, ha x < −1. "
           "A 2-ben a függvény 0, de ott nem vált előjelet.",
        nem="✘ Az (x − 2)² tényező négyzet: a 2 két oldalán is pozitív, ott nincs előjelváltás. Az előjel "
            "csak az x + 1-en múlik: h(x) < 0 pontosan akkor, ha x < −1."),
   GY(FT + "#alap-5", "A 5–12", FT + "#kozep-3", "K 3–6"),
   brief('<b>Nagol:</b> Tudjuk, hol él a függvény, hol nulla és hol pozitív. Most azt nézzük meg, hogyan '
         '<b>viselkedik</b>: tükrös-e, ismétlődik-e, emelkedik vagy süllyed. <b>Véd Vilmos:</b> Én '
         'mindenképp emelkedő vagyok.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Belenéztem a tükörbe, és a tükörképem mást csinált, mint én. <b>Nagol:</b> '
         'A páros függvény tükörképe önmaga. A tiéd nem páros — és az sem biztos, hogy páratlan. Ma a '
         'függvények <b>viselkedését</b> nézzük: szimmetriát, ismétlődést és azt, hol nő és hol csökken.'),
 ]),

 ("Páros és páratlan függvény", [
   r'<p class="lead">A paritás a grafikon <b>szimmetriáját</b> írja le. Feltétele, hogy az értelmezési '
   r'tartomány szimmetrikus legyen a $0$-ra: ha $x$ benne van, $-x$ is.</p>',
   doboz("definicio", "Páros és páratlan függvény",
         r'<ul><li>$f$ <b>páros</b>, ha minden $x\in D_f$ esetén $-x\in D_f$ és $f(-x)=f(x)$ — a grafikon az $y$ tengelyre szimmetrikus;</li>'
         r'<li>$f$ <b>páratlan</b>, ha minden $x\in D_f$ esetén $-x\in D_f$ és $f(-x)=-f(x)$ — a grafikon az origóra szimmetrikus.</li></ul>'
         r'<p>Egy függvény lehet <b>egyik sem</b>.</p>', hid="def-paros-paratlan"),
   doboz("pelda", "I.V.H. Akták — paritásvizsgálat",
         r'<p>Helyettesítsünk $x$ helyére $-x$-et, és hasonlítsuk össze az eredményt $f(x)$-szel!</p>'
         r'<ul><li>$f(x)=x^4-3x^2$: $f(-x)=(-x)^4-3(-x)^2=x^4-3x^2=f(x)$ → <b>páros</b>.</li>'
         r'<li>$g(x)=x^3+2x$: $g(-x)=-x^3-2x=-(x^3+2x)=-g(x)$ → <b>páratlan</b>.</li>'
         r'<li>$h(x)=x^2+x$: $h(-x)=x^2-x$, ez sem $h(x)$, sem $-h(x)$ (pl. $h(1)=2$, $h(-1)=0$) → <b>egyik sem</b>.</li>'
         r'<li>$k(x)=x\sin x$: a szinusz páratlan, $\sin(-x)=-\sin x$, így $k(-x)=(-x)(-\sin x)=x\sin x$ → <b>páros</b> '
         r'(páratlan · páratlan = páros).</li></ul>',
         hid="pelda-paritas"),
   abra(SVG_PAROS, 'A kék görbe az $y$ tengelyre, a piros az origóra szimmetrikus.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „az $x^3+1$ páratlan, mert páratlan a kitevő”, és „ami nem páros, az '
         r'páratlan”.</p>'
         r'<p><b>Mindig számolj: $f(-x)=?$</b> Itt $(-x)^3+1=-x^3+1$, ami sem $x^3+1$, sem $-(x^3+1)$ — tehát '
         r'<b>egyik sem</b>. A konstans tag elrontja a páratlanságot.</p>'),
   kviz(r'A $g(x)=x^2-2x$ függvényre $g(-1)=3$ és $g(1)=-1$. Mit mond ez a paritásáról?',
        [r'nem páros, mert egy konkrét $x$-re $g(-x)\ne g(x)$',
         r'páratlan, mert az egyik érték pozitív, a másik negatív',
         r'páros, mert két pontban vizsgáltuk',
         r'semmit, a paritást csak grafikonról lehet eldönteni'], 0,
        jo="✔ Egyetlen ellenpélda elég a cáfolathoz: g(−1) ≠ g(1). Páratlan sem, mert g(−1) ≠ −g(1) (3 ≠ 1). "
           "Igazolni viszont csak az általános f(−x) számolással lehet.",
        nem="✘ Ellenpéldával cáfolni lehet: g(−1) = 3 ≠ g(1) = −1, tehát nem páros. Páratlan csak akkor lehetne, ha "
            "g(−1) = −g(1) = 1 volna, de 3-at kaptunk — így egyik sem."),
 ]),

 ("Periodikus függvények", [
   r'<p class="lead">Egy függvény <b>periodikus</b>, ha a grafikonja egy szakasz ismétlődéséből áll.</p>',
   doboz("definicio", "Periodikus függvény",
         r'<p>Az $f$ függvény periodikus, ha van olyan $p\gt0$ szám, hogy minden $x\in D_f$ esetén $x+p\in D_f$ és '
         r'$f(x+p)=f(x)$. A legkisebb ilyen $p$ (ha van) az <b>alapperiódus</b>.</p>', hid="def-periodikus"),
   r'<p>Példák: a $\sin x$ és a $\cos x$ alapperiódusa $2\pi$, a $\operatorname{tg}x$-é $\pi$. A nem konstans '
   r'polinomok, az exponenciális és a logaritmusfüggvény <b>nem</b> periodikusak.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Periodikus a hangrezgés (a hangmagasság a periódus hosszán múlik), a nappalok hossza az év során, '
         r'a szívritmus EKG-görbéje és a váltakozó áram feszültsége.</p>'),
 ]),

 ("Monotonitás és korlátosság — a grafikonról", [
   r'<p class="lead">A grafikonról leolvasható, hol <b>nő</b> és hol <b>csökken</b> a függvény, és van-e '
   r'legnagyobb vagy legkisebb értéke. Pontos kiszámolásukhoz a deriválás kell — ez a következő témakör '
   r'(A függvény deriváltja) eszköze.</p>',
   doboz("definicio", "Monoton függvény",
         r'<p>Az $f$ egy intervallumon <b>szigorúan növekvő</b>, ha ott bármely $x_1\lt x_2$ esetén '
         r'$f(x_1)\lt f(x_2)$, és <b>szigorúan csökkenő</b>, ha $f(x_1)\gt f(x_2)$. Az $f$ <b>korlátos</b>, ha '
         r'értékei két rögzített szám közé esnek.</p>', hid="def-monoton-fv"),
   r'<p>Az $y=x^2$ a $(-\infty;\,0]$ intervallumon csökken, a $[0;\,\infty)$ intervallumon nő, legkisebb értéke $0$; '
   r'a $\sin x$ korlátos ($-1\le\sin x\le1$), az $y=x^3$ nem korlátos.</p>',
 ]),

 ("Egy grafikon — minden tulajdonság", [
   r'<p class="lead">Egy grafikonról a függvény teljes „névjegye” leolvasható. Ez a típus a felmérőkön is '
   r'visszatér.</p>',
   abra(SVG_ELEMZES, 'Az $f$ függvény grafikonja a $[-3;\\,4]$ intervallumon (a töröttvonal végpontjai a görbe részei).'),
   doboz("pelda", "I.V.H. Akták — grafikonelemzés",
         r'<ul><li><b>Értelmezési tartomány:</b> $D_f=[-3;\,4]$; <b>értékkészlet:</b> $R_f=[-2;\,3]$.</li>'
         r'<li><b>Zérushelyek:</b> $-2$, $1$ és $2{,}5$.</li>'
         r'<li><b>Előjel:</b> $f(x)\gt0$ a $(-2;\,1)$ és a $(2{,}5;\,4]$ intervallumon, $f(x)\lt0$ a $[-3;\,-2)$ és az $(1;\,2{,}5)$ intervallumon.</li>'
         r'<li><b>Monotonitás:</b> nő a $[-3;\,-1]$ és a $[2;\,4]$, csökken a $[-1;\,2]$ intervallumon.</li>'
         r'<li><b>Legnagyobb érték:</b> $3$ (az $x=4$ helyen); <b>legkisebb:</b> $-2$ (az $x=-3$ helyen).</li>'
         r'<li><b>Paritás:</b> egyik sem — már az értelmezési tartomány sem szimmetrikus.</li></ul>',
         hid="pelda-grafikonelemzes"),
   kviz(r'Honnan olvasod le a grafikonról a függvény értékkészletét?',
        [r'az $y$ tengelyről: mely magasságokat éri el a görbe',
         r'az $x$ tengelyről: meddig tart a görbe balra és jobbra',
         r'a zérushelyekből',
         r'a görbe két végpontjának $x$ koordinátájából'], 0,
        jo="✔ Az értékkészlet a felvett függvényértékek halmaza — ezek a pontok magasságai, vagyis "
           "függőleges irányban kell nézni.",
        nem="✘ Az x tengely mentén az értelmezési tartományt látod. Az értékkészlet a felvett "
            "értékek (magasságok) halmaza, ezt az y tengelyre vetítve olvasod le."),
   GY(FT + "#alap-13", "A 13–16", FT + "#kozep-7", "K 7–8"),
   brief('<b>Nagol:</b> Eddig azt néztük, mennyi a függvény egy pontban. Most jön a fejezet igazi kérdése: '
         '<b>mihez közelít</b> a függvény, ha $x$ egy pont felé fut — akkor is, ha abban a pontban nincs '
         'értelmezve. <b>Véd Vilmos:</b> Ha nincs értelmezve, akkor ott nincs semmi. <b>Nagol:</b> Majd meglátjuk.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-elemi-fuggvenyek.html",
     cim="Az elemi függvények",
     cim_tiszta="Az elemi függvények",
     alcim="Ismerős arcok: hatvány- és gyökfüggvények, az exponenciális és a logaritmusfüggvény, a "
           "trigonometrikus függvények — értelmezési tartomány, értékkészlet és grafikon.",
     chip=KUL + " · 1/7", szakaszok=A1,
     elozo=("index.html", "Függvények — témakör"),
     kovetkezo=("tananyag-ertelmezesi-tartomany.html", "Értelmezési tartomány, zérushely, előjel")),
 lap(**T, fajl="tananyag-ertelmezesi-tartomany.html",
     cim="Értelmezési tartomány, zérushely, előjel",
     alcim="Hol van értelme a képletnek? A három tiltás, több feltétel metszete, a zérushelyek és az "
           "előjeltáblázat.",
     chip=KUL + " · 2/7", szakaszok=A2,
     elozo=("tananyag-elemi-fuggvenyek.html", "Az elemi függvények"),
     kovetkezo=("tananyag-fuggvenytulajdonsagok.html", "Paritás, periodicitás, monotonitás")),
 lap(**T, fajl="tananyag-fuggvenytulajdonsagok.html",
     cim="Paritás, periodicitás, monotonitás",
     alcim="Páros és páratlan függvény, periodikus függvények, és egy grafikon teljes elemzése: "
           "értékkészlet, zérushely, előjel, monotonitás.",
     chip=KUL + " · 3/7", szakaszok=A3,
     elozo=("tananyag-ertelmezesi-tartomany.html", "Értelmezési tartomány, zérushely, előjel"),
     kovetkezo=("tananyag-fuggveny-hatarerteke.html", "A függvény határértéke")),
]
for u in KI:
    print("✓", os.path.basename(u))
