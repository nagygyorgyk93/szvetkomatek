# -*- coding: utf-8 -*-
"""4e/02 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p), I.V.H. Kihallgato Terem (F6h) es a temakor-index (F5).
Kuldetes: Az Aszimptota-fal Attorese. Mentor: Nagol (Ved Vilmos a falnal).
Az adatok ujak: sem a felmerokben, sem a tananyag peldaiban, sem a ket Zsoldos-listaban nem szerepelnek."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, brief, GYOKER
from fgy_common import cards, oldal, w
import sympy
from sympy import (Rational as Q, symbols, limit, oo, latex, sympify, S, solveset, simplify, fraction, together, solve)

T = dict(tagozat="4e", mappa="02-fuggvenyek", temakor="Függvények")
KUL = "Az Aszimptota-fal Áttörése"
A1, A2, A3 = "tananyag-elemi-fuggvenyek.html", "tananyag-ertelmezesi-tartomany.html", "tananyag-fuggvenytulajdonsagok.html"
B1, B2, B3 = "tananyag-fuggveny-hatarerteke.html", "tananyag-hatarertek-szamolasa.html", "tananyag-hatarertek-vegtelenben.html"
C1 = "tananyag-aszimptotak.html"
FT, FH = "feladatok-tulajdonsagok.html", "feladatok-hatarertek-aszimptota.html"

x = symbols("x", real=True)
Ex = lambda s: sympify(s, locals={"x": x})


def L(s, a, d=None):
    f = Ex(s)
    if a == -oo:
        return limit(f.subs(x, -x), x, oo)
    if a == oo:
        return limit(f, x, oo)
    return limit(f, x, a, d) if d else limit(f, x, a, "+-")


def ASZ(s):
    f = Ex(s); sz, nv = fraction(together(f))
    fu = sorted((r for r in solve(nv, x) if L(s, r, "+") in (oo, -oo)), key=float)
    h = L(s, oo)
    k = L(f"({s})/x", oo)
    return fu, (None if h in (oo, -oo) else h), ((k, L(f"({s})-({k})*x", oo)) if h in (oo, -oo) else None)


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


def par(s):
    f = Ex(s); g = f.subs(x, -x)
    return "páros" if simplify(g - f) == 0 else "páratlan" if simplify(g + f) == 0 else "egyik sem"


# ==================================================================== F4 — Csalópapír
OSSZ = [
 ("📇 Az elemi függvények névjegye", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>függvény</th><th>$D_f$</th><th>$R_f$</th><th>jellegzetesség</th></tr>'
  r'<tr><td>$y=x^n$, $n\ge2$ páros</td><td>$\mathbb R$</td><td>$[0;\,+\infty)$</td><td>az $y$ tengelyre szimmetrikus</td></tr>'
  r'<tr><td>$y=x^n$, $n\ge1$ páratlan</td><td>$\mathbb R$</td><td>$\mathbb R$</td><td>az origóra szimmetrikus</td></tr>'
  r'<tr><td>$y=\sqrt x$</td><td>$[0;\,+\infty)$</td><td>$[0;\,+\infty)$</td><td>csak nemnegatív $x$-re</td></tr>'
  r'<tr><td>$y=\dfrac1x$</td><td>$\mathbb R\setminus\{0\}$</td><td>$\mathbb R\setminus\{0\}$</td><td>két ág, aszimptoták: $x=0$, $y=0$</td></tr>'
  r'<tr><td>$y=a^x$ ($a\gt0$, $a\ne1$)</td><td>$\mathbb R$</td><td>$(0;\,+\infty)$</td><td>átmegy a $(0;\,1)$ ponton</td></tr>'
  r'<tr><td>$y=\log_ax$ ($\ln x=\log_ex$)</td><td>$(0;\,+\infty)$</td><td>$\mathbb R$</td><td>átmegy az $(1;\,0)$ ponton</td></tr>'
  r'<tr><td>$y=\sin x$, $y=\cos x$</td><td>$\mathbb R$</td><td>$[-1;\,1]$</td><td>periódus: $2\pi$</td></tr>'
  r'<tr><td>$y=\operatorname{tg}x$</td><td>$x\ne\frac\pi2+k\pi$, $k\in\mathbb Z$</td><td>$\mathbb R$</td><td>periódus: $\pi$</td></tr>'
  r'</table></div>'
  r'<p>Részletesen: <a href="' + A1 + r'">az elemi függvények</a>.</p>',
 ]),

 ("📐 Értelmezési tartomány, zérushely, előjel", [
  r'<p class="lead"><b>A három tiltás</b> ' + h(A2, "tetel-ert-tartomany") + r': a nevező $\ne0$; páros gyök alatt '
  r'$\ge0$; a logaritmus argumentuma $\gt0$. Több feltétel esetén a feltételek megoldáshalmazainak <b>közös része</b> '
  r'az értelmezési tartomány.</p>'
  r'<p><b>Zérushely:</b> $f(x)=0$ megoldásai, de csak az értelmezési tartományban; törtnél a számláló zérushelyei, '
  r'ahol a nevező nem $0$.</p>'
  r'<p><b>Előjel</b> ' + h(A2, "pelda-elojeltabla") + r': a számláló és a nevező tényezőinek zérushelyei intervallumokra '
  r'bontják a számegyenest; minden intervallumon összeszorozzuk a tényezők előjelét. Páros kitevőjű tényező zérushelyén '
  r'nincs előjelváltás.</p>',
 ]),

 ("🪞 Paritás és periodicitás", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th></th><th>feltétel (minden $x\in D_f$-re)</th><th>a grafikon</th></tr>'
  r'<tr><td>páros ' + h(A3, "def-paros-paratlan") + r'</td><td>$D_f$ szimmetrikus, és $f(-x)=f(x)$</td><td>az $y$ tengelyre szimmetrikus</td></tr>'
  r'<tr><td>páratlan</td><td>$D_f$ szimmetrikus, és $f(-x)=-f(x)$</td><td>az origóra szimmetrikus</td></tr>'
  r'<tr><td>periodikus ' + h(A3, "def-periodikus") + r'</td><td>van $T\gt0$, amelyre $x+T\in D_f$ és $f(x+T)=f(x)$</td><td>egy szakasz ismétlődik</td></tr>'
  r'</table></div>'
  r'<p>Egy konkrét ellenpélda elég a cáfolathoz; igazolni csak az általános $f(-x)$ kiszámolásával lehet. '
  r'A függvény lehet <b>egyik sem</b>. A monotonitást itt grafikonról olvassuk le; kiszámolni a deriválttal fogjuk.</p>',
 ]),

 ("🎯 A határérték", [
  r'<p class="lead">$\lim\limits_{x\to a}f(x)=A$: $f(x)$ akármilyen közel vihető $A$-hoz, ha $x$ elég közel van $a$-hoz '
  r'($x\ne a$) ' + h(B1, "def-fv-hatarertek") + r'. A pontbeli érték nem számít: ha a görbe mindkét oldalról ugyanahhoz az '
  r'<b>üres</b> ponthoz tart, annak magassága a határérték; a <b>teli</b> ponté a függvényérték.</p>'
  r'<p><b>Egyoldali határérték</b> ' + h(B1, "def-egyoldali") + r': $x\to a-0$ (balról), $x\to a+0$ (jobbról). A '
  r'határérték akkor és csak akkor létezik, ha a kettő létezik és egyenlő.</p>'
  r'<p><b>Folytonosság</b> ' + h(B1, "def-folytonos") + r': $\lim\limits_{x\to a}f(x)=f(a)$. Az elemi függvények '
  r'az értelmezési tartományukban folytonosak — ott a határérték <b>behelyettesítéssel</b> kiszámolható.</p>',
 ]),

 ("🧮 Határérték-számítás — mit csinálj?", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>helyzet</th><th>teendő</th></tr>'
  r'<tr><td>egy szám</td><td>kész: ez a határérték</td></tr>'
  r'<tr><td>$\dfrac00$</td><td>szorzattá alakítás, egyszerűsítés, újra behelyettesítés ' + h(B2, "pelda-szorzatta") + r'</td></tr>'
  r'<tr><td>$\dfrac00$ gyökkel</td><td>bővítés a konjugálttal: $(\sqrt u-c)(\sqrt u+c)=u-c^2$ ' + h(B2, "pelda-konjugalt") + r'</td></tr>'
  r'<tr><td>$\dfrac c0$, $c\ne0$</td><td>egyoldali határértékek: $\pm\infty$, az előjelek szerint ' + h(B2, "pelda-c-per-0") + r'</td></tr>'
  r'<tr><td>$\dfrac\infty\infty$ ($x\to\pm\infty$, racionális tört)</td><td>fokszám-szabály; $x\to-\infty$-nél figyelj az előjelre ' + h(B3, "tetel-fokszam-fv") + r'</td></tr>'
  r'</table></div>',
 ]),

 ("🧱 Aszimptoták", [
  r'<p class="lead">Racionális törtnél $p$ a számláló, $r$ a nevező foka.</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>fajta</th><th>hol keresd</th><th>mikor van</th></tr>'
  r'<tr><td>függőleges $x=a$</td><td>racionális törtnél a nevező zérushelyei (egyszerűsítés után); $\log_ax$-nél $x=0$</td>'
  r'<td>ha legalább az egyik egyoldali határérték $\pm\infty$</td></tr>'
  r'<tr><td>vízszintes $y=c$</td><td>$\lim\limits_{x\to\pm\infty}f(x)$</td><td>ha véges ($p\le r$)</td></tr>'
  r'<tr><td>ferde $y=kx+n$</td><td>$k=\lim\limits_{x\to\pm\infty}\dfrac{f(x)}{x}$, $n=\lim\limits_{x\to\pm\infty}\big(f(x)-kx\big)$</td>'
  r'<td>ha egyszerűsítés után $p=r+1$</td></tr>'
  r'</table></div>'
  r'<p>Ha egy helyen a számláló és a nevező is $0$, ott nem biztos, hogy függőleges aszimptota van: egyszerűsíts, és nézd '
  r'meg újra — lehet, hogy csak <b>lyuk</b> van ott ' + h(C1, "pelda-teljes", "(lépésről lépésre)") + r'.</p>',
 ]),

 ("⚠️ Véd Vilmos csapdái — amin a legtöbben elcsúsznak", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A nyolc leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>Csak egy feltétel:</b> $\dfrac{\sqrt{x+3}}{x-2}$-nél a gyök feltétele is kell, nem csak a nevezőé.</li>'
  r'<li><b>Zérushely a nevezőben:</b> ahol a nevező $0$, ott nincs zérushely — a függvény nincs értelmezve.</li>'
  r'<li><b>„Nem páros, tehát páratlan”:</b> lehet egyik sem; mindig számold ki $f(-x)$-et.</li>'
  r'<li><b>Határérték = behelyettesítés:</b> csak folytonos helyen igaz; a lyuknál a függvény nincs értelmezve '
  r'(behelyettesítve $\dfrac00$), a határérték mégis létezik; ha a pontban külön érték van megadva, az eltérhet tőle.</li>'
  r'<li><b>$\dfrac00=1$ vagy $0$:</b> határozatlan alak — alakíts át.</li>'
  r'<li><b>$\dfrac c0=0$:</b> itt egyoldali végtelen határérték jön, az előjel két oldalon eltérhet.</li>'
  r'<li><b>$x\to-\infty$ is $+\infty$:</b> ha $p\gt r$ és $p-r$ páratlan, a $-\infty$-ben ellenkező előjelű a határérték.</li>'
  r'<li><b>Minden nevező-zérushely aszimptota:</b> ha a számláló is $0$, lehet lyuk. És a görbe <b>metszheti</b> a '
  r'vízszintes aszimptotát.</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A1 + r'">elemi függvények</a> · <a href="' + A2 + r'">értelmezési tartomány, '
  r'zérushely, előjel</a> · <a href="' + A3 + r'">paritás, periodicitás</a> · <a href="' + B1 + r'">a határérték</a> · '
  r'<a href="' + B2 + r'">határérték-számítás</a> · <a href="' + B3 + r'">a végtelenben</a> · <a href="' + C1 + r'">aszimptoták</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FT + r'">Zsoldos-lista I.</a> (tulajdonságok) · <a href="' + FH + r'">Zsoldos-lista II.</a> '
  r'(határérték, aszimptoták) · <a href="feladatok-hazi.html">I.V.H. Kihallgató Terem</a> (házi).</p>'
  r'<p><b>Ismétlés:</b> a sorozat határértéke és a fokszám-szabály a '
  r'<a href="../01-sorozatok-hatarerteke/osszefoglalo.html">01-es Csalópapíron</a>. A témakört '
  r'<a href="terepkuldetes.html">' + KUL + r'</a> küldetés zárja.</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon", cim_tiszta="Csalópapír", itt="Csalópapír",
    alcim="Elemi függvények, értelmezési tartomány, paritás, határérték, határérték-számítás és aszimptoták egy lapon — "
          "ismétléshez, az ellenőrző előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló", szakaszok=OSSZ,
    elozo=("feladatok-hazi.html", "I.V.H. Kihallgató Terem"), kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p — terepküldetés (önteszt)
E = []


def ck(nev, g, wv):
    if not (g == wv or (not isinstance(g, (list, tuple)) and simplify(sympify(g) - sympify(wv)) == 0)):
        E.append((nev, g, wv))


SZ = "(x**2-4*x-5)/(x**2-9)"
ck("I-D", sorted(solve(Ex("x**2-9"), x)), [-3, 3])
ck("I-zerus", sorted(solve(Ex("x**2-4*x-5"), x)), [-1, 5])
ck("I-poz", solveset(Ex(SZ) > 0, x, S.Reals),
   sympy.Union(sympy.Interval.open(-oo, -3), sympy.Interval.open(-1, 3), sympy.Interval.open(5, oo)))
ck("I-f0", Ex(SZ).subs(x, 0), Q(5, 9))
ck("I-par", par(SZ), "egyik sem")
K = "(x**2-9)/(x**2-x-6)"
ck("II-3", L(K, 3), Q(6, 5))
ck("II-m2", [L(K, -2, "-"), L(K, -2, "+")], [-oo, oo])
ck("II-inf", [L(K, oo), L(K, -oo)], [1, 1])
ck("II-gyok", L("(sqrt(x+4)-3)/(x-5)", 5), Q(1, 6))
WV = "(x**2+x-1)/(x-2)"
ck("III-asz", ASZ(WV), ([2], None, (1, 3)))
ck("III-102", Ex(WV).subs(x, 102) - (102 + 3), Q(1, 20))
ck("III-alak", simplify(Ex(WV) - (x + 3 + 5 / (x - 2))), 0)
ck("IV-1", L("(x**2-36)/(x-6)", 6), 12)
ck("IV-2", [L("(x**2-1)/(x-1)", 1), ASZ("(x**2-1)/(x-1)")[0]], [2, []])
ck("IV-3", L("(x**3+2)/(x**2+1)", -oo), -oo)
ck("IV-4", [Ex("x**2+x").subs(x, -1), Ex("x**2+x").subs(x, 1), par("x**2+x")], [0, 2, "egyik sem"])
assert not E, E
print("F5p önteszt: OK")

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Az I.V.H. falat húzott az idővonal köré, és Véd Vilmos már harmadszor fut neki. '
         '<b>Véd Vilmos:</b> Negyedszerre áttöröm! 🌮 <i>Burek-matek:</i> „ha elég gyorsan futok, a végtelenben '
         'odaérek.” <b>Nagol:</b> Nem érsz oda — és ezt ki is fogjuk számolni. Négy fázis: az I.V.H. szenzorjele, a fal '
         'határértékei, Vilmos pályája a fal mentén, végül Vilmos jegyzőkönyve, tele hibás megoldással.'),
   r'<p>Minden lépésnél írd le, melyik módszert használtad (értelmezési tartomány, előjeltáblázat, szorzattá '
   r'alakítás, konjugált, egyoldali határérték, aszimptota-képletek). Számológép használható. A választ '
   r'fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, mint máshol a '
   r'számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — Az I.V.H. szenzorjele", [
   r'<p>Az I.V.H. szenzora az $x$ helyen $s(x)=\dfrac{x^2-4x-5}{x^2-9}$ erősségű jelet ad. Ahol a jel negatív, '
   r'ott Vilmos láthatatlan.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Hol van értelmezve a jel? Hol nulla?</li>'
   r'<li>Készíts előjeltáblázatot! Mely $x$ értékekre (intervallumokon) láthatatlan Vilmos?</li>'
   r'<li>Számítsd ki $s(0)$-t, és vázold a jel előjelsávjait az előjeltáblázat alapján! (Hogy az $x=\pm3$ közelében '
   r'mi történik, a II–III. fázis után pontosítod.)</li>'
   r'<li>Páros, páratlan vagy egyik sem az $s$ függvény? Indokold egy $x$, $-x$ értékpárra kiszámolt két függvényértékkel!</li>'
   r'</ol>',
 ]),

 ("II. fázis — A fal határértékei", [
   r'<p>A fal erőterét a $K(x)=\dfrac{x^2-9}{x^2-x-6}$ függvény írja le.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki a $\lim\limits_{x\to3}K(x)$ határértéket! Milyen alakot kapsz behelyettesítéskor, és mit csinálsz vele?</li>'
   r'<li>Számítsd ki az $x\to-2-0$ és az $x\to-2+0$ egyoldali határértéket! Mit jelent ez $K$ grafikonjára az $x=-2$ egyenes két oldalán?</li>'
   r'<li>Mennyi a $K$ határértéke a $+\infty$-ben és a $-\infty$-ben?</li>'
   r'<li>Egy másik szenzor jele $\dfrac{\sqrt{x+4}-3}{x-5}$. Számítsd ki az $x=5$ helyen vett határértékét!</li>'
   r'</ol>',
 ]),

 ("III. fázis — Vilmos pályája a fal mentén", [
   r'<p>Vilmos pályája a $w(x)=\dfrac{x^2+x-1}{x-2}$ függvény grafikonja; a fal most a $w$ ferde aszimptotája.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Határozd meg a $w$ függőleges aszimptotáját!</li>'
   r'<li>Határozd meg a ferde aszimptotáját ($k$ és $n$ kiszámításával)!</li>'
   r'<li>Mutasd meg, hogy $w(x)=x+3+\dfrac{5}{x-2}$! Mekkora a függőleges távolság a pálya és a ferde aszimptota '
   r'között az $x=102$ helyen?</li>'
   r'<li>Metszi-e valaha Vilmos pályája a ferde aszimptotát? Indokold!</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Véd Vilmos jegyzőkönyve", [
   r'<p>Vilmos leadta a saját „megoldásait” az I.V.H.-nak. Az első négy mind hibás. Keresd meg a hibát, és add meg a helyes '
   r'eredményt; ha nincs véges határérték vagy aszimptota, indokold meg!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>$\lim\limits_{x\to6}\dfrac{x^2-36}{x-6}=\dfrac00=0$.</li>'
   r'<li>„Az $\dfrac{x^2-1}{x-1}$ függvénynek az $x=1$ egyenes függőleges aszimptotája, mert ott a nevező $0$.”</li>'
   r'<li>$\lim\limits_{x\to-\infty}\dfrac{x^3+2}{x^2+1}=+\infty$, „mert a számláló foka nagyobb”.</li>'
   r'<li>„Az $f(x)=x^2+x$ páratlan, mert $f(-1)=0$ és $f(1)=2$ különbözik.”</li>'
   r'<li>Mi a közös a négy hibában? Fogalmazd meg két-három mondatban, mit kell <b>ellenőrizni</b>, mielőtt egy '
   r'szabályt alkalmazunk!</li>'
   r'</ol>',
   brief('<b>Nagol:</b> A szenzor bemérve, a fal határértékei kiszámolva, és Vilmos pályájáról is tudjuk, hogy a fal '
         'mellett fut, de soha nem éri el. A számításaidat a tanárod ellenőrzi; a kulcs nem kerül a hálózatra. '
         '<b>Véd Vilmos:</b> Akkor a falat nem is kellett áttörni? <b>Nagol:</b> Megérteni kellett. A következő '
         'fejezetben azt nézzük meg, milyen gyorsan változik minden — egy pillanat alatt.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: az I.V.H. szenzorjele, a fal határértékei, Vilmos pályája a fal mentén és Véd Vilmos hibás "
          "jegyzőkönyve. Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés", szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Csalópapír"), kovetkezo=("index.html", "A Negyedik Fal"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — I.V.H. Kihallgató Terem
HE = []
for nev, g, wv in [
    ("h1", [sorted(solve(Ex("x**2-4*x"), x)), solve(Ex("8-2*x"), x), solve(Ex("x+6"), x)], [[0, 4], [4], [-6]]),
    ("h2a", [sorted(solve(Ex("(x-3)*(x+1)**2"), x)), solveset(Ex("(x-3)*(x+1)**2") > 0, x, S.Reals)], [[-1, 3], sympy.Interval.open(3, oo)]),
    ("h2b", solveset(Ex("(x**2-9)/(x+2)") > 0, x, S.Reals), sympy.Union(sympy.Interval.open(-3, -2), sympy.Interval.open(3, oo))),
    ("h3", [par("x**6-2*x**2"), par("x*Abs(x)"), par("x**2+3*x"), par("3**x+3**(-x)")], ["páros", "páratlan", "egyik sem", "páros"]),
    ("h4", [L("(x**2-5*x+6)/(x-3)", 3), L("(x**2+4*x+3)/(x**2-1)", -1), L("(4*x**2-1)/(2*x**2+x)", oo)], [1, -1, 2]),
    ("h5", [ASZ("(3*x+2)/(x-1)"), ASZ("x/(x**2-4)")], [([1], 3, None), ([-2, 2], 0, None)]),
    ("k1", [L("(sqrt(x+2)-2)/(x-2)", 2), L("(sqrt(9+x)-3)/x", 0)], [Q(1, 4), Q(1, 6)]),
    ("k2", [L("(x+1)/(4-x)", 4, "-"), L("(x+1)/(4-x)", 4, "+")], [oo, -oo]),
    ("k3", [L("(2*x**3-x)/(x**2+5)", -oo), L("(3-x**2)/(x+1)", -oo)], [-oo, oo]),
    ("n1", ASZ("(x**2-3*x+5)/(x-1)"), ([1], None, (1, -2))),
    ("n2", [ASZ("(x**2-4)/(x**2+x-2)"), L("(x**2-4)/(x**2+x-2)", -2), ASZ("(x**3-x)/(x**2-4)")], [([1], 1, None), Q(4, 3), ([-2, 2], None, (1, 0))]),
]:
    if g != wv:
        HE.append((nev, g, wv))
assert not HE, HE
print("F6h önteszt: OK")

HA = [
 ("Határozd meg a függvények értelmezési tartományát!",
  [r"$f(x)=\dfrac{x+2}{x^2-4x}$", r"$g(x)=\sqrt{8-2x}$", r"$h(x)=\ln(x+6)$"],
  [r"$D_f=\mathbb R\setminus\{0;\,4\}$", r"$D_g=(-\infty;\,4]$", r"$D_h=(-6;\,+\infty)$"]),
 ("Határozd meg a függvények zérushelyeit és előjelét!",
  [r"$y=(x-3)(x+1)^2$", r"$y=\dfrac{x^2-9}{x+2}$"],
  [r"zérushelyek: $-1$ és $3$; $y\gt0$, ha $x\gt3$; $y\lt0$, ha $x\lt-1$ vagy $-1\lt x\lt3$",
   r"zérushelyek: $-3$ és $3$; $y\gt0$, ha $-3\lt x\lt-2$ vagy $x\gt3$; $y\lt0$, ha $x\lt-3$ vagy $-2\lt x\lt3$"]),
 ("Döntsd el, hogy a függvény páros, páratlan vagy egyik sem!",
  [r"$f(x)=x^6-2x^2$", r"$g(x)=x\lvert x\rvert$", r"$h(x)=x^2+3x$", r"$k(x)=3^x+3^{-x}$"],
  ["páros", "páratlan", "egyik sem", "páros"]),
 ("Számítsd ki a határértékeket!",
  [r"$\lim\limits_{x\to3}\dfrac{x^2-5x+6}{x-3}$", r"$\lim\limits_{x\to-1}\dfrac{x^2+4x+3}{x^2-1}$",
   r"$\lim\limits_{x\to+\infty}\dfrac{4x^2-1}{2x^2+x}$"],
  ["$1$", "$-1$", "$2$"]),
 ("Határozd meg a függvények aszimptotáit!",
  [r"$f(x)=\dfrac{3x+2}{x-1}$", r"$g(x)=\dfrac{x}{x^2-4}$"],
  [r"függőleges: $x=1$; vízszintes: $y=3$", r"függőleges: $x=-2$ és $x=2$; vízszintes: $y=0$"]),
]
HK = [
 ("Számítsd ki a határértékeket!",
  [r"$\lim\limits_{x\to2}\dfrac{\sqrt{x+2}-2}{x-2}$", r"$\lim\limits_{x\to0}\dfrac{\sqrt{9+x}-3}{x}$"],
  [r"$\frac14$", r"$\frac16$"]),
 (r"Számítsd ki az $\dfrac{x+1}{4-x}$ egyoldali határértékeit az $x=4$ helyen!", None,
  r"$\lim\limits_{x\to4-0}\dfrac{x+1}{4-x}=+\infty$ (a számláló $5$, a nevező balról pozitív), $\lim\limits_{x\to4+0}\dfrac{x+1}{4-x}=-\infty$"),
 ("Számítsd ki a határértékeket! Figyelj az előjelre!",
  [r"$\lim\limits_{x\to-\infty}\dfrac{2x^3-x}{x^2+5}$", r"$\lim\limits_{x\to-\infty}\dfrac{3-x^2}{x+1}$"],
  [r"$-\infty$", r"$+\infty$"]),
]
HN = [
 (r"Határozd meg az $f(x)=\dfrac{x^2-3x+5}{x-1}$ függvény aszimptotáit!", None,
  r"függőleges: $x=1$ (a számláló értéke ott $3\ne0$); ferde: $k=1$, $n=\lim\limits_{x\to+\infty}\dfrac{-2x+5}{x-1}=-2$, tehát $y=x-2$"),
 ("Határozd meg a függvények aszimptotáit! Előbb nézd meg, hol nulla a számláló.",
  [r"$g(x)=\dfrac{x^2-4}{x^2+x-2}$", r"$h(x)=\dfrac{x^3-x}{x^2-4}$"],
  [r"$g(x)=\frac{x-2}{x-1}$, ha $x\ne-2$: függőleges: $x=1$; vízszintes: $y=1$; az $x=-2$ helyen csak lyuk van (a $\left(-2;\,\frac43\right)$ pontban)",
   r"függőleges: $x=-2$ és $x=2$; vízszintes nincs; ferde: $y=x$"]),
]
body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(HA, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(HK, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(HN, "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem", h1="I.V.H. Kihallgató Terem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span><span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a függvényekből — házi feladatnak és a témazáró ellenőrző előtti bemelegítésnek. "
            "Az I.V.H. minden választ ellenőriz: a végeredmény lenyitható, de csak a számolás után nézd meg!",
      sections_html="\n".join(body), ossz_nev="Csalópapírt",
      prev=FH, prevc="Zsoldos-lista II.", nxt="osszefoglalo.html", nxtc="Csalópapír")
print("✓ feladatok-hazi.html | Alap", len(HA), "Közép", len(HK), "Nehéz", len(HN))


# ==================================================================== F5 — témakör-index
def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


KT = {
 "A1": kartya(A1, "Az elemi függvények", "Hatvány-, gyök-, exponenciális, logaritmus- és trigonometrikus függvények névjegye"),
 "A2": kartya(A2, "Értelmezési tartomány, zérushely, előjel", "A három tiltás, több feltétel, zérushelyek és előjeltáblázat"),
 "A3": kartya(A3, "Paritás, periodicitás, monotonitás", "Páros és páratlan függvény, periodicitás, egy grafikon teljes elemzése"),
 "B1": kartya(B1, "A függvény határértéke", "Közelítés, teli és üres pont, egyoldali határérték, folytonosság"),
 "B2": kartya(B2, "Határérték-számítás", "Behelyettesítés, 0/0 szorzattá alakítással és konjugálttal, c/0"),
 "B3": kartya(B3, "Határérték a végtelenben", "Racionális törtfüggvények a $\\pm\\infty$-ben, az előjel, elemi függvények"),
 "C1": kartya(C1, "Aszimptoták", "Függőleges, vízszintes és ferde aszimptota lépésről lépésre"),
 "f1": kartya(FT, "🏋️ Zsoldos-lista I. — Tulajdonságok", "Értelmezési tartomány, zérushely, előjel, paritás, grafikonelemzés — 22 feladat és egy joker"),
 "f2": kartya(FH, "🏋️ Zsoldos-lista II. — Határérték és aszimptoták", "Grafikonról, 0/0, konjugált, egyoldali, végtelenben, aszimptoták — 34 feladat és egy joker"),
 "hazi": kartya("feladatok-hazi.html", "🕹️ I.V.H. Kihallgató Terem — házi feladatok", "Rövid, vegyes gyakorlósor az ellenőrző előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL, "Négyfázisú záróküldetés — a szenzorjel, a fal határértékei, Vilmos pályája és hibás jegyzőkönyve"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír", "Elemi függvények, értelmezési tartomány, határérték és aszimptoták egy lapon"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(KT[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Függvények | 4e | Szvetkó matek</title>
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
  <span class="itt">Függvények</span>
</nav>
<div class="hero">
  <h1>Függvények</h1>
  <p class="alcim">Az elemi függvények névjegye, értelmezési tartomány, zérushely, előjel és paritás — aztán a
  függvény határértéke, a határérték-számítás fogásai és az aszimptoták, amelyekhez a görbe simul.</p>
  <div class="meta-sor"><span class="chip ora">19 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧱 <b>02 — Az Aszimptota-fal Áttörése.</b> Mentor: <b>Nagol</b> (és <b>Véd Vilmos</b>, aki
  folyton nekimegy a falnak). Szia, megint én vagyok, Vilmos. Az I.V.H. falat húzott körénk, és én már háromszor
  nekifutottam. Nagol szerint nem áttörni kell, hanem kiszámolni, hol van — és hogy miért nem érem el soha. Kezdd a
  függvények névjegyével; a falig úgyis eljutunk.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🧩 A függvény tulajdonságai — Nagol</h3>
''' + racs("A1", "A2", "A3") + '''
    <h3>🎯 A határérték — Nagol</h3>
''' + racs("B1", "B2", "B3") + '''
    <h3>🧱 Az aszimptota-fal — Nagol és Véd Vilmos</h3>
''' + racs("C1") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("f1", "f2", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> a hét tananyag-egység sorban, közben a két Zsoldos-lista megfelelő
    szintjei, a végén az I.V.H. Kihallgató Terem — ezekre épül a témazáró ellenőrző. A Csalópapír az ismétlést
    szolgálja, a témakört pedig <i>Az Aszimptota-fal Áttörése</i> záróküldetés zárja.</p>
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
