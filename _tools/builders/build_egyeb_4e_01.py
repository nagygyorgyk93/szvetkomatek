# -*- coding: utf-8 -*-
"""4e/01 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p), I.V.H. Kihallgato Terem (F6h) es a temakor-index (F5).
Kuldetes: A Vegtelenbe es... Ne Tovabb! Mentor: Ved Vilmos (Nagol javit).
Az adatok ujak: sem a felmerokben, sem a tananyag peldaiban, sem a Zsoldos-listaban nem szerepelnek."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, abra, brief, svg_fuggvenyek, GYOKER
from fgy_common import cards, oldal, w
from sympy import (Rational as Q, symbols, limit, oo, exp, latex, sympify, S, E as EE, Pow, log, nsimplify,
                   solve, Eq, simplify)
from sympy.parsing.sympy_parser import parse_expr
import sympy

T = dict(tagozat="4e", mappa="01-sorozatok-hatarerteke", temakor="Sorozatok határértéke")
KUL = "A Végtelenbe és… Ne Tovább!"
ZOLD, KEK, PIROS = "#047857", "#3b82f6", "#ef4444"
A = "tananyag-hatarertek-fogalma.html"
B1 = "tananyag-racionalis-tortek.html"
B2 = "tananyag-gyokos-kifejezesek.html"
B3 = "tananyag-az-e-szam.html"
C = "tananyag-vegtelen-mertani-sor.html"
FGY = "feladatok-hatarertek.html"

n = symbols("n", positive=True, integer=True)
LD = {"n": n, "Rational": Q, "sqrt": sympy.sqrt}


def TX(s):
    t = latex(parse_expr(s, local_dict=LD, evaluate=False), order="none")
    t = re.sub(r"(?<![\d.}])1 \\frac", r"\\frac", t)
    t = t.replace(r"\frac", r"\dfrac")                       # kiemelt tört a feladatsorban …
    return re.sub(r"\^\{\\dfrac", r"^{\\frac", t)               # … de a kitevőben kicsi marad


def _zar(e, t):
    return r"\left(" + t + r"\right)" if parse_expr(e, local_dict=LD, evaluate=False).is_Add else t


def LIM(s):
    return limit(sympify(s, locals=LD), n, oo)


def V(v):
    if v == oo:
        return r"+\infty"
    if v == -oo:
        return r"-\infty"
    if isinstance(v, Pow) and v.base == EE or v.func == exp:
        k = v.exp if isinstance(v, Pow) else v.args[0]
        return "e^{%s}" % latex(k)
    return latex(v)


def LIMS(intro, exprs):
    return (intro, [r"$\lim\limits_{n\to\infty}" + _zar(e, TX(e)) + "$" for e in exprs],
            ["$" + V(LIM(e)) + "$" for e in exprs])


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


def ms(b1, q):
    return Q(b1) / (1 - Q(q))


# ==================================================================== F4 — Csalópapír
OSSZ = [
 ("📇 A határérték", [
  r'<p class="lead">Az $(a_n)$ sorozat határértéke az $A$ szám, ha a tagok tetszőlegesen megközelítik '
  r'$A$-t: akármilyen keskeny $A\pm\varepsilon$ sávot adunk meg, valahányadik tagtól kezdve '
  r'<b>minden</b> tag a sávba esik. Jele: $\lim\limits_{n\to\infty}a_n=A$.</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Fogalom</th><th>Jelentés / szabály</th><th>Megjegyzés</th></tr>'
  r'<tr><td>konvergens (' + h(A, "def-konvergens") + r')</td><td>van véges határértéke</td>'
  r'<td>a határérték egyértelmű; néhány tagból csak <b>sejteni</b> lehet</td></tr>'
  r'<tr><td>divergens</td><td>nincs véges határértéke</td>'
  r'<td>tarthat $+\infty$-hez vagy $-\infty$-hez, vagy oszcillálhat, mint $(-1)^n$</td></tr>'
  r'<tr><td>nevezetes határértékek (' + h(A, "tetel-nevezetes") + r')</td>'
  r'<td>$\dfrac{c}{n^k}\to0$ és $n^k\to+\infty$, ha $k\gt0$</td>'
  r'<td>$q^n\to0$, ha $\lvert q\rvert\lt1$ · $q^n=1$, ha $q=1$ · $q^n\to+\infty$, ha $q\gt1$ · '
  r'divergens, ha $q\le-1$</td></tr>'
  r'<tr><td>műveletek (' + h(A, "tetel-muveletek") + r')</td>'
  r'<td>konvergens sorozatok összegének, különbségének, szorzatának és hányadosának határértéke a '
  r'határértékek összege, különbsége, szorzata, hányadosa</td>'
  r'<td>hányadosnál a nevező határértéke nem lehet $0$</td></tr>'
  r'<tr><td>határozatlan alakok</td><td>$\dfrac{\infty}{\infty}$, $\infty-\infty$, $1^\infty$</td>'
  r'<td>ezekből <b>semmi nem következik</b> — előbb át kell alakítani</td></tr>'
  r'</table></div>',
 ]),

 ("📐 Törtek: kiemelés és a fokszám-szabály", [
  r'<p class="lead">$\dfrac{\infty}{\infty}$ alaknál a számlálóból és a nevezőből is a <b>nevező '
  r'legmagasabb fokú</b> $n$-hatványát emeljük ki, és egyszerűsítünk ' + h(B1, "pelda-kiemeles") + r'. '
  r'Az eredmény mindig a fokszám-szabály ' + h(B1, "tetel-fokszam") + r':</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>számláló: $p$-edfokú, főegyüttható $a$ · nevező: $r$-edfokú, főegyüttható $b$</th>'
  r'<th>a határérték</th></tr>'
  r'<tr><td>$p\lt r$ — a nevező „győz”</td><td>$0$</td></tr>'
  r'<tr><td>$p=r$ — döntetlen</td><td>$\dfrac ab$</td></tr>'
  r'<tr><td>$p\gt r$ — a számláló „győz”</td><td>$+\infty$ vagy $-\infty$, az $\dfrac ab$ előjele szerint</td></tr>'
  r'</table></div>'
  r'<p><b>Gyökös kifejezés</b> ' + h(B2, "tetel-gyok-kiemeles") + r'. A gyökjel alól $n^2$-et emelünk ki, és '
  r'$\sqrt{n^2}=n$, mert $n\gt0$. Így $\sqrt{an^2+bn+c}$ ($a\gt0$) nagy $n$-re úgy viselkedik, mint '
  r'$\sqrt a\cdot n$ — a főegyütthatóból is gyököt vonunk.</p>'
  r'<p><b>Két tört különbsége</b> ($\infty-\infty$) ' + h(B1, "pelda-kulonbseg") + r'. Előbb közös '
  r'nevezőre hozunk és összevonunk, csak utána jöhet a fokszám-szabály.</p>',
 ]),

 ("🔢 Az $e$ szám", [
  r'<p class="lead">$e=\lim\limits_{n\to\infty}\left(1+\dfrac1n\right)^n\approx2{,}718$ '
  r'' + h(B3, "def-e") + r', és általában ' + h(B3, "tetel-e-altalanos") + r'</p>'
  r'$$\lim_{n\to\infty}\left(1+\frac kn\right)^{mn}=e^{km}.$$'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Első lépés: mihez tart az alap?</th><th>Mit csinálunk?</th></tr>'
  r'<tr><td>$1$-hez, és a kitevő $+\infty$-hez ($1^\infty$)</td>'
  r'<td>$\left(1+\frac{k}{\dots}\right)$ alakra hozzuk: a törtes alapot $1+\dfrac{\text{szám}}{\text{nevező}}$ '
  r'alakba írjuk ' + h(B3, "pelda-e-hanyados") + r', az eltolt nevezőt a kitevőben kiegyenlítjük '
  r'' + h(B3, "pelda-e-eltolt") + r'</td></tr>'
  r'<tr><td>egy $1$-nél nagyobb számhoz, a kitevő $+\infty$-hez</td><td>a határérték $+\infty$</td></tr>'
  r'<tr><td>egy $0$ és $1$ közötti számhoz, a kitevő $+\infty$-hez</td><td>a határérték $0$</td></tr>'
  r'<tr><td>a kitevőnek is véges a határértéke (és az alapé pozitív)</td><td>nem határozatlan alak: behelyettesítjük a két '
  r'határértéket ' + h(B3, "pelda-nem-e") + r'</td></tr>'
  r'</table></div>',
 ]),

 ("♾️ A végtelen mértani sor", [
  r'<p class="lead">A $b_1+b_1q+b_1q^2+\dots$ végtelen mértani sor összege a részletösszegek '
  r'határértéke, $S=\lim\limits_{n\to\infty}S_n$ ' + h(C, "tetel-vegtelen-mertani-sor") + r'.</p>'
  r'$$S=\frac{b_1}{1-q},\qquad\text{ha }\lvert q\rvert\lt1 .$$'
  r'<p>Ha $\lvert q\rvert\ge1$ (és $b_1\ne0$), a sornak <b>nincs</b> összege — a képletet ilyenkor nem '
  r'szabad használni. A feltételt <b>mindig</b> ellenőrizzük, mielőtt behelyettesítünk.</p>'
  r'<p><b>Szakaszos tizedes tört</b> ' + h(C, "pelda-szakaszos") + r'. A szakaszok egy végtelen '
  r'mértani sor tagjai: egyjegyű szakasznál $q=\frac1{10}$, kétjegyűnél $q=\frac1{100}$. Vegyes szakaszos '
  r'törtnél a nem ismétlődő részt külön adjuk hozzá.</p>'
  r'<p><b>Szöveges feladatnál</b> az első tagot és a hányadost keressük meg: „minden lépés az előző '
  r'$\frac23$-a” → $q=\frac23$. Ha a mozgás oda-vissza történik (pattogó labda), az első utat külön '
  r'számoljuk, a többit kétszer.</p>',
 ]),

 ("⚠️ Véd Vilmos csapdái — amin a legtöbben elcsúsznak", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A nyolc leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>Határozatlan alak eredményként:</b> ✗ „$\frac\infty\infty=1$”, ✗ „$\infty-\infty=0$”, '
  r'✗ „$1^\infty=1$” — ezek nem számok, hanem jelzések, hogy át kell alakítani.</li>'
  r'<li><b>Rossz főtag:</b> a főtag a <b>legmagasabb fokú</b> tag, nem az elsőnek leírt: '
  r'$\dfrac{3-2n^2}{n^2+5}\to-2$.</li>'
  r'<li><b>Elveszett előjel:</b> ha $p\gt r$, az előjelet a főegyütthatók döntik el: '
  r'$\dfrac{n^2+1}{3-n}\to-\infty$.</li>'
  r'<li><b>Gyökvonás a főegyütthatóból:</b> $\sqrt{9n^2+1}$ úgy viselkedik, mint $3n$, nem mint $9n$.</li>'
  r'<li><b>Mindenre $e$:</b> először nézd meg, mihez tart az alap! '
  r'$\left(\frac{2n+1}{n}\right)^n\to+\infty$, mert az alap $2$-höz tart.</li>'
  r'<li><b>A kitevő előjele:</b> $\left(1-\frac2n\right)^{n}\to e^{-2}$ — a $k$ itt $-2$.</li>'
  r'<li><b>Mértani sor feltétel nélkül:</b> $\lvert q\rvert\ge1$ esetén nincs összeg, bármit ad is a '
  r'képlet.</li>'
  r'<li><b>A $q^n$ negatív $q$-val:</b> ha $q\le-1$, a sorozat nem $+\infty$-hez tart, hanem '
  r'oszcillál: divergens.</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A + r'">a sorozat határértéke</a> · '
  r'<a href="' + B1 + r'">kiemelés — törtek határértéke</a> · '
  r'<a href="' + B2 + r'">gyökös kifejezések</a> · '
  r'<a href="' + B3 + r'">az $e$ szám</a> · '
  r'<a href="' + C + r'">a végtelen mértani sor</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FGY + r'">Zsoldos-lista</a> (Zöldfülű · X-Force · Maximális '
  r'erőbedobás · joker) és az <a href="feladatok-hazi.html">I.V.H. Kihallgató Terem</a> házi feladatsora.</p>'
  r'<p><b>Ismétlés:</b> a sorozat fogalma, a monotonitás és a mértani sorozat első $n$ tagjának összegképlete a tavalyi '
  r'<a href="../../3e/06-indukcio-sorozatok/osszefoglalo.html">Taktikai memóriakártyán</a> van. '
  r'A témakört <a href="terepkuldetes.html">' + KUL + r'</a> küldetés zárja.</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon",
    cim_tiszta="Csalópapír", itt="Csalópapír",
    alcim="A határérték, a kiemelés, az $e$ szám és a végtelen mértani sor egy lapon — ismétléshez, az "
          "ellenőrző előtti átfutáshoz, nyomtatáshoz. (Véd Vilmos szerint ez csalás. Nagol szerint tanulás.)",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=OSSZ,
    elozo=("feladatok-hazi.html", "I.V.H. Kihallgató Terem"),
    kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p — terepküldetés (önteszt)
E = []


def ck(nev, g, wv):
    jo = g == wv or (not isinstance(g, list) and simplify(sympify(g) - sympify(wv)) == 0)
    if not jo:
        E.append((nev, g, wv))


a = lambda m: Q(6 * m - 1, 2 * m + 3)
for m, wv in zip(range(1, 6), [1, Q(11, 7), Q(17, 9), Q(23, 11), Q(29, 13)]):
    ck(f"I-a{m}", a(m), wv)
ck("I-a100", round(float(a(100)), 3), Q(2951, 1000)); ck("I-a1000", round(float(a(1000)), 3), Q(2995, 1000))
ck("I-lim", LIM("(6*n-1)/(2*n+3)"), 3)
ck("I-elteres", simplify(3 - sympify("(6*n-1)/(2*n+3)", locals=LD) - 10 / (2 * n + 3)), 0)
ck("I-kuszob", next(m for m in range(1, 5000) if abs(a(m) - 3) < Q(1, 100)), 499)
ck("II-T1", LIM("(5*n**2-3*n+4)/(10*n**2+7)"), Q(1, 2))
ck("II-T2", LIM("sqrt(64*n**2+5*n)/(4*n-9)"), 2)
ck("II-T3", LIM("(1+5/n)**(3*n)"), exp(15))
ck("II-T1-1000", round(float(Q(5 * 10**6 - 3000 + 4, 10**7 + 7)), 4), Q(4997, 10000))
ck("III-S", ms(12, Q(5, 6)), 72)
ck("III-tagok", [12 * Q(5, 6) ** k for k in range(5)], [12, 10, Q(25, 3), Q(125, 18), Q(625, 108)])
ck("III-kuszob", next(m for m in range(1, 100) if 72 * (1 - Q(5, 6) ** m) > 70), 20)
ck("III-S19", round(float(72 * (1 - Q(5, 6) ** 19)), 2), Q(6975, 100))
ck("III-S20", round(float(72 * (1 - Q(5, 6) ** 20)), 2), Q(7012, 100))
ck("III-qmax", solve(Eq(12 / (1 - symbols("x")), 70), symbols("x"))[0], Q(29, 35))
ck("III-q3", float(Q(29, 35)) // 0.001 / 1000, 0.828)
ck("IV-1", LIM("(2*n**2+3)/(n+1)-(2*n**2-5)/(n+4)"), 6)
ck("IV-2", LIM("(1+2*n/(n+3))**n"), oo)
ck("IV-2alap", LIM("1+2*n/(n+3)"), 3)
ck("IV-3", [3 * (-2) ** k for k in range(4)], [3, -6, 12, -24])
ck("IV-3reszlet", [sum(3 * (-2) ** k for k in range(j)) for j in range(1, 5)], [3, -3, 9, -15])
ck("IV-4", LIM("(4*n**3+n)/(7-2*n**3)"), -2)
assert not E, E
print("F5p önteszt: OK")

SVG_SZENZOR = svg_fuggvenyek(
    [(lambda u: 3, PIROS, "y = 3", [(0, 12.5)])],
    xr=(0, 12.6), yr=(0, 3.6), w=380, h=230, tengely=("n", "aₙ"),
    leiras="A szenzor első tizenkét mérése és a 3-as szint",
    pontok=[(m, float(a(m)), "", ZOLD) for m in range(1, 13)])

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Jó hírem van: az I.V.H. nem nulláz le mindenkit. Csak azt, aki nem tudja '
         'kiszámolni a végtelent. Én kismotorral próbáltam, a szenzor megőrült, az időszerver kijelzői '
         'végtelen sokáig pörögnek, és a fékutam is gyanús. 🌮 <i>Burek-matek:</i> „ami végtelen sokáig '
         'tart, az végtelen nagy is.” <b>Nagol:</b> Hibás, és ezt most te fogod bebizonyítani. Négy fázis: '
         'a szenzor, a kijelzők, a fékút — és végül Vilmos jegyzőkönyve, tele hibás „levezetéssel”.'),
   r'<p>Minden lépésnél írd le, melyik módszert használtad (kiemelés, gyök alól kiemelés, az $e$-s '
   r'összefüggés, végtelen mértani sor). Számológép használható: a nem egész eredményeket a kért '
   r'pontossággal kerekítsd, és jelöld a kerekítést. A választ fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, '
   r'mint máshol a számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><b>Amire szükséged lesz:</b> a határérték fogalma, a kiemelés és a fokszám-szabály, a gyökös '
   r'törtek, az $\left(1+\frac kn\right)^{mn}\to e^{km}$ összefüggés és a végtelen mértani sor.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — A szenzor", [
   r'<p>A kismotor szenzora az $n$-edik mérésnél $a_n=\dfrac{6n-1}{2n+3}$ ezer fordulat/perc fordulatszámot mutat. '
   r'Nagol szerint a szenzor egy jól meghatározott szinthez közelít — Vilmos szerint „csak úgy '
   r'nő”.</p>',
   abra(SVG_SZENZOR, 'Az első tizenkét mérés és az $y=3$ szint.'),
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki az első öt mérést, tört alakban és két tizedesjegyre kerekítve is!</li>'
   r'<li>Számítsd ki $a_{100}$ és $a_{1000}$ értékét három tizedesjegyre! Mit sejtesz a határértékről?</li>'
   r'<li>Igazold a sejtésedet kiemeléssel!</li>'
   r'<li>Mutasd meg, hogy $3-a_n=\dfrac{10}{2n+3}$! Mit árul el ez arról, hogy a pontok alulról vagy '
   r'felülről közelítenek a $3$-hoz?</li>'
   r'<li>Hányadik méréstől kezdve tér el minden mérés $0{,}01$-nál kevesebbel a határértéktől?</li>'
   r'</ol>',
 ]),

 ("II. fázis — Az időszerver kijelzői", [
   r'<p>Az időszerver három kijelzője végtelen sokáig pörög. Az újraindításhoz a határértékeikre van '
   r'szükség:</p>'
   r'$$T_1=\frac{5n^2-3n+4}{10n^2+7},\qquad T_2=\frac{\sqrt{64n^2+5n}}{4n-9},\qquad '
   r'T_3=\left(1+\frac5n\right)^{3n}.$$'
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki mindhárom kijelző határértékét! Nevezd meg, melyik módszert használtad!</li>'
   r'<li>Számítsd ki a $T_1$ kijelző $n=1000$-hez tartozó értékét négy tizedesjegyre! Mennyivel tér el '
   r'a határértéktől?</li>'
   r'<li>Vilmos szerint $T_3$ határértéke $1$, „mert $1+\frac5n\to1$, és $1$ bármely hatványa $1$”. '
   r'Mi a hiba a gondolatmenetében?</li>'
   r'</ol>',
 ]),

 ("III. fázis — A fékút", [
   r'<p>Vilmos fékez. Az első másodpercben még $12$ métert tesz meg, és minden további másodpercben az '
   r'előző másodperc útjának $\frac56$-át. A fékezés kezdetekor $70$ méterre előtte egy szakadék széle van.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Mennyit tesz meg az első öt másodperc mindegyikében (tört alakban és két tizedesjegyre kerekítve)? '
   r'Milyen sorozatot alkotnak ezek az utak?</li>'
   r'<li>Mekkora a teljes fékút, ha a fékezés (elméletben) végtelen sokáig tart?</li>'
   r'<li>Megáll-e Vilmos a szakadék előtt? Ha nem, hányadik másodpercben lépi át a $70$ métert? '
   r'<i>(Elég próbálgatással megkeresni, számológéppel.)</i></li>'
   r'<li>Nagol szerint erősebben kellene fékezni. Legfeljebb mekkora lehet a hányados (az első '
   r'másodperc $12$ métere mellett), hogy a teljes fékút legfeljebb $70$ méter legyen? Add meg tört '
   r'alakban és három tizedesjegyre lefelé kerekítve is!</li>'
   r'<li>Vilmos „fékezés” helyett gyorsít: minden másodpercben az előző út $\frac65$-át teszi meg. '
   r'Van-e ilyenkor véges teljes útja? Indokold meg!</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Véd Vilmos jegyzőkönyve", [
   r'<p>Vilmos leadta az I.V.H.-nak a saját „megoldásait”. Mindegyik hibás. Keresd meg a hibát, és add '
   r'meg a helyes eredményt; ha nincs véges határérték vagy összeg, indokold meg!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>$\lim\limits_{n\to\infty}\left(\dfrac{2n^2+3}{n+1}-\dfrac{2n^2-5}{n+4}\right)=\infty-\infty=0$.</li>'
   r'<li>$\lim\limits_{n\to\infty}\left(1+\dfrac{2n}{n+3}\right)^{n}=e^{2}$, „mert ez $1^\infty$ alakú, és '
   r'a törtben $2$ áll”.</li>'
   r'<li>$3-6+12-24+\dots=\dfrac{3}{1-(-2)}=1$.</li>'
   r'<li>$\lim\limits_{n\to\infty}\dfrac{4n^3+n}{7-2n^3}=2$, „mert a főegyütthatók hányadosa $4:2$”.</li>'
   r'<li>Mi a közös a négy hibában? Fogalmazd meg két-három mondatban, mit kell <b>ellenőrizni</b>, '
   r'mielőtt egy szabályt vagy képletet alkalmazunk!</li>'
   r'</ol>',
   brief('<b>Nagol:</b> A szenzor be van mérve, a kijelzők újraindultak, és tudjuk, hol állna meg '
         'a motor — ha jobban fékezne. Vilmos jegyzőkönyve pedig megmutatta, hogy a végtelennel nem lehet '
         'úgy bánni, mint egy számmal. A számításaidat a tanárod ellenőrzi; a kulcs nem kerül a hálózatra. '
         '<b>Véd Vilmos:</b> Szóval megúsztuk? <b>Nagol:</b> Ezt a fejezetet igen.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: a szenzor, az időszerver kijelzői, a fékút és Véd Vilmos hibás jegyzőkönyve. "
          "Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Csalópapír"),
    kovetkezo=("index.html", "A Negyedik Fal"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — I.V.H. Kihallgató Terem
HE = []
for nev, g, wv in [("h1-tagok", [Q(4 * m + 2, m + 1) for m in range(1, 6)], [3, Q(10, 3), Q(7, 2), Q(18, 5), Q(11, 3)]),
                   ("h1-lim", LIM("(4*n+2)/(n+1)"), 4),
                   ("h5-tagok", [24 * Q(5, 8) ** k for k in range(1, 4)], [15, Q(75, 8), Q(375, 64)]),
                   ("h5-S", ms(24, Q(5, 8)), 64),
                   ("k3a", ms(Q(45, 100), Q(1, 100)), Q(5, 11)),
                   ("k3b", Q(1, 10) + ms(Q(2, 100), Q(1, 10)), Q(11, 90))]:
    if simplify(sympify(g) - sympify(wv)) != 0 if not isinstance(g, list) else g != wv:
        HE.append((nev, g, wv))
assert not HE, HE

HA = [
 (r"Írd fel az $a_n=\dfrac{4n+2}{n+1}$ sorozat első öt tagját, és sejtsd meg a határértékét! A sejtésedet "
  r"igazold kiemeléssel!", None,
  r"$3;\ \frac{10}{3};\ \frac{7}{2};\ \frac{18}{5};\ \frac{11}{3}$ — a határérték: $" + V(LIM("(4*n+2)/(n+1)")) + "$"),
 LIMS("Számítsd ki a határértékeket!", ["(9*n**2-4*n)/(3*n**2+5)", "(7*n+2)/(n**3+1)", "(4-n**3)/(2*n**2+n)"]),
 ("Mihez tart a sorozat? Ha nincs határértéke, indokold meg!",
  [r"$a_n=\left(\dfrac57\right)^n$", r"$a_n=2+\dfrac{7}{n^2}$", r"$a_n=\left(-\dfrac65\right)^n$"],
  ["$0$", "$2$", r"nincs határértéke, divergens: $q=-\frac65\le-1$, a tagok előjele váltakozik, az "
                 r"abszolút értékük nő"]),
 LIMS("Számítsd ki a határértékeket! Használd az $\\left(1+\\frac kn\\right)^{mn}\\to e^{km}$ összefüggést.",
      ["(1+1/n)**(5*n)", "(1+3/n)**(2*n)"]),
 (r"Az I.V.H. szondája az első órában $24$ km-t repül, és minden további órában az előző órai útjának "
  r"$\frac58$-át teszi meg.",
  ["Mennyit repül a második, a harmadik és a negyedik órában?",
   "Mekkora utat tesz meg összesen, ha végtelen sokáig repül?"],
  [r"$15$ km, $\frac{75}{8}=9{,}375$ km és $\frac{375}{64}\approx5{,}86$ km",
   r"$\frac{24}{1-\frac58}=" + latex(ms(24, Q(5, 8))) + "$ km"]),
]
HK = [
 LIMS("Számítsd ki a határértékeket!", ["(6*n+1)/sqrt(4*n**2+n)", "sqrt(81*n**2-5)/(2-3*n)"]),
 LIMS("Számítsd ki a határértékeket!", ["(1-2/n)**(5*n)", "(1+6/n)**(n/4)"]),
 ("Végtelen mértani sorok és szakaszos tizedes törtek.",
  [r"Írd fel közönséges törtként: $0{,}\dot4\dot5$!", r"Írd fel közönséges törtként: $0{,}1\dot2$!",
   r"Van-e összege a $10-\frac{25}{2}+\frac{125}{8}-\dots$ végtelen mértani sornak?"],
  [r"$\frac{45}{99}=" + latex(ms(Q(45, 100), Q(1, 100))) + "$",
   r"$\frac{1}{10}+\frac{2}{90}=" + latex(Q(1, 10) + ms(Q(2, 100), Q(1, 10))) + "$",
   r"nincs, mert $q=-\frac54$, és $\lvert q\rvert\ge1$"]),
]
HN = [
 LIMS("Számítsd ki a határértékeket!", ["(n**2+4)/(n+2)-(n**2-2)/(n+3)", "3*n**2/(3*n+1)-(n**2+1)/(n+2)"]),
 LIMS("Számítsd ki a határértékeket! Ha kell, írd az alapot $1+\\frac{\\dots}{\\dots}$ alakba, és a kitevőt "
      "igazítsd a tört nevezőjéhez.",
      ["((n+5)/(n+1))**(3*n)", "(1+2/(3*n+1))**(n+5)"]),
]
assert [V(LIM(e)) for e in ["(n**2+4)/(n+2)-(n**2-2)/(n+3)", "3*n**2/(3*n+1)-(n**2+1)/(n+2)",
                            "((n+5)/(n+1))**(3*n)", "(1+2/(3*n+1))**(n+5)"]] == \
       ["1", r"\frac{5}{3}", "e^{12}", r"e^{\frac{2}{3}}"]
print("F6h önteszt: OK")

body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(HA, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(HK, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(HN, "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem",
      h1="I.V.H. Kihallgató Terem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a sorozatok határértékéből — házi feladatnak és a témazáró ellenőrző "
            "előtti bemelegítésnek. Az I.V.H. minden választ ellenőriz: a végeredmény minden feladatnál "
            "lenyitható, de csak a számolás után nézd meg!",
      sections_html="\n".join(body),
      prev=FGY, prevc="Zsoldos-lista", nxt="osszefoglalo.html", nxtc="Csalópapír")
print("✓ feladatok-hazi.html | Alap", len(HA), "Közép", len(HK), "Nehéz", len(HN))


# ==================================================================== F5 — témakör-index
def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = {
 "A": kartya(A, "A sorozat határértéke", "Közelítés, sáv-kép, konvergens és divergens sorozat, nevezetes határértékek, műveletek"),
 "B1": kartya(B1, "Kiemelés — törtek határértéke", "A fokszám-szabály három esete, szorzatok és hatványok a törtben"),
 "B2": kartya(B2, "Gyökös kifejezések határértéke", "Kiemelés a gyökjel alól: $\\sqrt{n^2}=n$, és a gyökös törtek"),
 "B3": kartya(B3, "Az e szám", "Az $1^\\infty$ alak, a kamatos kamat határa, $\\left(1+\\frac kn\\right)^{mn}\\to e^{km}$ — és amikor nem $e$ a válasz"),
 "C": kartya(C, "A végtelen mértani sor", "Végtelen sok tag összege, a $\\lvert q\\rvert\\lt1$ feltétel, szakaszos tizedes törtek"),
 "fgy": kartya(FGY, "🏋️ Zsoldos-lista",
               "Határérték-feladatok három szinten: Zöldfülű · X-Force · Maximális erőbedobás — 54 feladat és egy joker"),
 "hazi": kartya("feladatok-hazi.html", "🕹️ I.V.H. Kihallgató Terem — házi feladatok",
                "Rövid, vegyes gyakorlósor az ellenőrző előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL,
              "Négyfázisú záróküldetés — a szenzor, az időszerver kijelzői, a fékút és Véd Vilmos hibás jegyzőkönyve"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír",
                "A határérték, a kiemelés, az $e$ szám és a végtelen mértani sor egy lapon — ellenőrző előtti átfutáshoz"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(K[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sorozatok határértéke | 4e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="4e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">&#8730;</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">4e</span></a> ›
  <span class="itt">Sorozatok határértéke</span>
</nav>
<div class="hero">
  <h1>Sorozatok határértéke</h1>
  <p class="alcim">Mihez közelít egy sorozat, ha végtelen sokáig folytatjuk? A határérték fogalma, a
  kiemelés és a gyökös törtek, az <i>e</i> szám, végül a végtelen mértani sor — végtelen sok tag véges összege.</p>
  <div class="meta-sor"><span class="chip ora">11 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🏍️ <b>01 — A Végtelenbe és… Ne Tovább!</b> Mentor: <b>Véd Vilmos</b> (és
  <b>Nagol</b>, aki kijavítja). Igen, te ott, a képernyő másik oldalán. Az I.V.H. le akarja nullázni az
  évfolyamot, és az első kérdése az, hogy ki tudod-e számolni a végtelent. Én kismotorral próbáltam —
  nem jött össze. Nagol szerint papírral és kiemeléssel kell. Kezdd az első lappal; a Csalópapírt pedig
  senki nem veszi el tőled.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🏍️ A határérték — Véd Vilmos</h3>
''' + racs("A") + '''
    <h3>📐 Kiemelés és az <i>e</i> szám — Véd Vilmos és Nagol</h3>
''' + racs("B1", "B2", "B3") + '''
    <h3>♾️ A végtelen mértani sor — Nagol</h3>
''' + racs("C") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("fgy", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> az öt tananyag-egység sorban, közben a Zsoldos-lista
    megfelelő szintjei, a végén az I.V.H. Kihallgató Terem — ezekre épül a témazáró ellenőrző. A
    Csalópapír az ismétlést szolgálja, a témakört pedig <i>A Végtelenbe és… Ne Tovább!</i> záróküldetés zárja.</p>
  </div>
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
  renderMathInElement(document.body, {delimiters:[
    {left:'\\\\(', right:'\\\\)', display:false},
    {left:'\\\\[', right:'\\\\]', display:true}
  ]});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
