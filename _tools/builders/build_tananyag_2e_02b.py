# -*- coding: utf-8 -*-
"""2e/02 — B altema: a masodfoku fuggveny (B1) es vizsgalata (B2). Mentor: Küklopsz."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
         temakor="Másodfokú egyenletek és függvények")
FGY = "feladatok-masodfoku-fuggveny.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, solve, simplify, expand, im, re as _re
x = symbols('x')
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
chk("B1-kanonikus", expand((x-3)**2-4), x**2-6*x+5)
chk("B1-u", -R(-6, 2), 3);                chk("B1-v", -R(36-20, 4), -4)
chk("B2-zerus", sorted(solve(x**2-2*x-3, x)), [-1, 3])
chk("B2-csucs", 1-2-3, -4)
chk("B2-zerus2", sorted(solve(-x**2+4*x-3, x)), [1, 3])
chk("B2-csucs2", -4+8-3, 1)
chk("B2-terulet", solve(20-4*x, x), [5])         # T = -2x^2+20x, csúcs x=5
chk("B2-tmax", -2*25+20*5, 50)
assert not E, E
print("sympy önteszt: OK")

# ===================================================================== B1

SVG_A = svg_fuggvenyek(
    [(lambda t: t**2, "#047857", "y = x²", [(-2.1, 2.1)]),
     (lambda t: 2*t**2, "#3b82f6", "y = 2x²", [(-1.5, 1.5)]),
     (lambda t: 0.5*t**2, "#8b5cf6", "y = ½x²", [(-2.5, 2.5)]),
     (lambda t: -t**2, "#ef4444", "y = −x²", [(-2.1, 2.1)])],
    xr=(-2.7, 2.7), yr=(-4.3, 4.3), w=380, h=270,
    leiras="Az y=x², y=2x², y=½x² és y=−x² parabolák: a főegyüttható a nyílásirányt "
           "és a karcsúságot szabja meg")

SVG_POZ = svg_fuggvenyek(
    [(lambda t: t**2-4, "#047857", "D &gt; 0", [(-2.6, 2.6)]),
     (lambda t: t**2, "#3b82f6", "D = 0", [(-2.3, 2.3)]),
     (lambda t: t**2+2, "#8b5cf6", "D &lt; 0", [(-2.1, 2.1)])],
    xr=(-3.0, 3.0), yr=(-4.4, 4.4), w=360, h=260,
    leiras="Felfelé nyíló parabola: két, egy vagy nulla metszéspont az x-tengellyel")

SVG_NEG = svg_fuggvenyek(
    [(lambda t: -t**2+4, "#047857", "D &gt; 0", [(-2.6, 2.6)]),
     (lambda t: -t**2, "#3b82f6", "D = 0", [(-2.3, 2.3)]),
     (lambda t: -t**2-2, "#8b5cf6", "D &lt; 0", [(-2.1, 2.1)])],
    xr=(-3.0, 3.0), yr=(-4.4, 4.4), w=360, h=260,
    leiras="Lefelé nyíló parabola: ugyanaz a három eset, tükrözve")

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Küklopsz:</b> Az optikai sugaram nem egyenesen halad, ha közeg téríti el — '
         'hanem <b>parabola</b> mentén. Ugyanígy repül a kilőtt lövedék, esik a labda, '
         'és így terjed Dr. Baljós energiahulláma is. Aki ismeri ezt a görbét, egyetlen '
         'pillantással megmondja, hol a legmagasabb pont, hol éri a földet, és hogy '
         'egyáltalán eléri-e. Ezért kezdünk a <b>képpel</b>, nem a képlettel.'),
   'Az előző egységekben azt kérdeztük: <b>hol nulla</b> a kifejezés. Most azt nézzük, '
   'hogyan viselkedik <b>mindenütt</b> — és kiderül, hogy a két kérdés ugyanannak '
   'a görbének két különböző olvasata.',
 ]),

 ("Az alapfüggvény és a főegyüttható", [
   doboz("definicio", "Másodfokú függvény",
         '<p><b>Másodfokú függvénynek</b> nevezzük az $f:\\mathbb{R}\\to\\mathbb{R}$,</p>'
         '$$f(x)=ax^{2}+bx+c,\\qquad a\\neq 0$$'
         '<p>alakú valós függvényt. A grafikonja <b>parabola</b>. Az $a=1$, $b=c=0$ eset '
         'az $y=x^{2}$ <b>alapfüggvény</b>, amelyet az I. témakörben már vizsgáltunk '
         '(<a href="../01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-hatvanyfuggveny.html'
         '#tetel-paros-kitevo">→ hatványfüggvény</a>).</p>',
         hid="def-masodfoku-fuggveny"),
   abra(SVG_A, "A főegyüttható két dolgot szab meg: az <b>előjele</b> a nyílásirányt, "
                "az <b>abszolút értéke</b> a görbe karcsúságát."),
   doboz("tetel", "Mit csinál az $a$?",
         '<p><b>Előjel:</b> ha $a&gt;0$, a parabola <b>felfelé</b> nyílik (konvex), és '
         'van <b>minimuma</b>; ha $a&lt;0$, <b>lefelé</b> nyílik (konkáv), és van '
         '<b>maximuma</b>.</p>'
         '<p><b>Nagyság:</b> minél nagyobb $\\lvert a\\rvert$, annál <b>karcsúbb</b> '
         '(meredekebb) a parabola; minél kisebb, annál <b>szélesebb</b>.</p>',
         hid="tetel-foegyutthato"),
 ]),

 ("Az általános alak és a kanonikus alak", [
   'Az $y=ax^{2}+bx+c$ alakból a zérushelyeket könnyű megkapni, a <b>csúcspontot</b> '
   'viszont nem. Ezért átírjuk teljes négyzetes — más néven <b>kanonikus</b> — alakra: '
   'abból a csúcs egyből leolvasható.',
   doboz("tetel", "Kanonikus alak és a csúcspont",
         '<p>Minden másodfokú függvény felírható</p>'
         '$$f(x)=a\\left(x-u\\right)^{2}+v$$'
         '<p>alakban, ahol a <b>csúcspont</b> $C(u;v)$, és</p>'
         '$$u=-\\frac{b}{2a},\\qquad v=f(u)=-\\frac{D}{4a}.$$'
         '<p>A parabola az $x=u$ egyenesre <b>tengelyesen szimmetrikus</b> — ez a '
         '<b>szimmetriatengelye</b>.</p>',
         hid="tetel-kanonikus",
         lenyilo=("Miért?",
                  '<p>Emeljük ki $a$-t, majd egészítsük ki teljes négyzetté:</p>'
                  '$$ax^{2}+bx+c=a\\left(x^{2}+\\frac{b}{a}x\\right)+c'
                  '=a\\left(x+\\frac{b}{2a}\\right)^{2}-\\frac{b^{2}}{4a}+c.$$'
                  '<p>Az utolsó két tag összevonva $-\\dfrac{b^{2}-4ac}{4a}=-\\dfrac{D}{4a}$ — '
                  'ugyanaz a teljes négyzetté alakítás, mint a megoldóképletnél.</p>')),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Írd kanonikus alakba, és add meg a csúcspontot: $y=x^{2}-6x+5$.</p>',
         hid="pelda-kanonikus",
         lenyilo=("Megoldás",
                  '<p><b>Képlettel:</b> $u=-\\dfrac{-6}{2}=3$, és $D=36-20=16$, tehát '
                  '$v=-\\dfrac{16}{4}=-4$. A csúcspont $C(3;-4)$.</p>'
                  '<p><b>Teljes négyzetté alakítással:</b> '
                  '$x^{2}-6x+5=(x-3)^{2}-9+5=(x-3)^{2}-4$ — ugyanaz.</p>')),
   kviz('Hol van az $y=x^{2}+8x+7$ függvény csúcspontjának $x$-koordinátája?',
        ['$x=-4$', '$x=4$', '$x=-8$'], 0,
        jo="✔ u = −b/(2a) = −8/2 = −4.",
        nem="✘ A képlet u = −b/(2a) = −8/(2·1) = −4."),
 ]),

 ("A hat eset", [
   'A parabola és az $x$-tengely kölcsönös helyzetét két adat dönti el: az $a$ '
   '<b>előjele</b> (merre nyílik) és a $D$ <b>előjele</b> (hány metszéspont van). '
   'Két lehetőség szorozva hárommal — ez a <b>hat eset</b>.',
   abra(SVG_POZ, "$a&gt;0$: felfelé nyíló parabola. $D&gt;0$ → két zérushely · "
                 "$D=0$ → egy (érinti a tengelyt) · $D&lt;0$ → egy sem (végig a tengely fölött)."),
   abra(SVG_NEG, "$a&lt;0$: lefelé nyíló parabola — ugyanaz a három eset, tükrözve."),
   doboz("tetel", "A hat eset összefoglalva",
         '<div class="tblwrap"><table>'
         '<tr><th></th><th>$D&gt;0$</th><th>$D=0$</th><th>$D&lt;0$</th></tr>'
         '<tr><td><b>$a&gt;0$</b></td><td>két zérushely; a csúcs a tengely <b>alatt</b></td>'
         '<td>egy (kettős) zérushely; a csúcs <b>a tengelyen</b></td>'
         '<td>nincs zérushely; a görbe <b>végig a tengely fölött</b></td></tr>'
         '<tr><td><b>$a&lt;0$</b></td><td>két zérushely; a csúcs a tengely <b>fölött</b></td>'
         '<td>egy (kettős) zérushely; a csúcs <b>a tengelyen</b></td>'
         '<td>nincs zérushely; a görbe <b>végig a tengely alatt</b></td></tr>'
         '</table></div>'
         '<p>Vagyis a diszkrimináns nem elvont szám: azt mondja meg, <b>hányszor metszi</b> '
         'a parabola az $x$-tengelyt. A komplex gyökök épp azt jelentik, hogy '
         '<b>egyszer sem</b>.</p>',
         hid="tetel-hat-eset"),
   kviz('Az $y=-x^{2}+2x-5$ parabola hol helyezkedik el az $x$-tengelyhez képest?',
        ['Végig a tengely alatt.', 'Két pontban metszi.', 'Érinti a tengelyt.'], 0,
        jo="✔ a = −1 < 0 (lefelé nyílik) és D = 4 − 20 = −16 < 0 → nincs metszéspont.",
        nem="✘ Számold ki D-t: 4 − 20 = −16 < 0, és a < 0 → a parabola végig a tengely alatt van."),
   gyakorolj(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Küklopsz:</b> A kép megvan. Most tegyük rendszerbe: van egy fix szempontsor, '
         'amit minden másodfokú függvényen végig kell futtatni. Ha ezt a listát fejből '
         'tudod, a dolgozat legnagyobb pontszámú feladatát rutinból megcsinálod.',
         outro=True),
 ]),
]

# ===================================================================== B2

SVG_VIZSG = svg_fuggvenyek(
    [(lambda t: t**2-2*t-3, "#047857", "y = x² − 2x − 3", [(-2.3, 4.3)])],
    xr=(-3.0, 5.0), yr=(-4.8, 5.2), w=400, h=290,
    leiras="Az y = x² − 2x − 3 parabola a zérushelyekkel, a csúcsponttal és "
           "az y-tengelymetszettel",
    pontok=[(-1, 0, "(−1; 0)", "#ef4444", -46, -8), (3, 0, "(3; 0)", "#ef4444", 6, -8),
            (1, -4, "C(1; −4)", "#047857", 8, 16), (0, -3, "(0; −3)", "#8b5cf6", -52, 14)])

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Küklopsz:</b> A csapatnak protokoll kell, nem ötletelés. A függvényvizsgálat '
         'is protokoll: ugyanaz a néhány kérdés, mindig ugyanabban a sorrendben. '
         'Ha végigmész rajta, a végén ott a teljes kép — és a grafikon már csak '
         'a jegyzőkönyv. Dr. Baljós energiagörbéit is így mérjük be.'),
 ]),

 ("A vizsgálat protokollja", [
   doboz("definicio", "Mit kérdezünk meg?",
         '<ol class="reszfeladatok">'
         '<li><b>Nyílásirány:</b> az $a$ előjele — konvex (felfelé) vagy konkáv (lefelé)?</li>'
         '<li><b>Zérushelyek:</b> az $ax^{2}+bx+c=0$ egyenlet megoldásai — itt metszi '
         'a görbe az $x$-tengelyt.</li>'
         '<li><b>$y$-tengelymetszet:</b> $f(0)=c$.</li>'
         '<li><b>Csúcspont:</b> $C(u;v)$, ahol $u=-\\dfrac{b}{2a}$ és $v=f(u)$.</li>'
         '<li><b>Szélsőérték:</b> $a&gt;0$ esetén <b>minimum</b>, $a&lt;0$ esetén '
         '<b>maximum</b>; az értéke $v$.</li>'
         '<li><b>Értékkészlet:</b> $a&gt;0$ esetén $[v,+\\infty)$, $a&lt;0$ esetén '
         '$(-\\infty,v]$.</li>'
         '</ol>'
         '<p>Az értelmezési tartomány mindig a teljes $\\mathbb{R}$ — ezt nem kell keresni.</p>',
         hid="def-vizsgalat-protokoll"),
   doboz("erdekesseg", "Miért ilyen sorrendben?",
         '<p>Mert minden lépés a következőt készíti elő. A nyílásirányból már tudod, '
         'minimum vagy maximum lesz-e; a csúcspontból jön a szélsőérték; a szélsőértékből '
         'az értékkészlet. Ha a sorrendet betartod, <b>nem kell gondolkodni</b> — csak '
         'számolni.</p>'),
 ]),

 ("Teljes kidolgozott vizsgálat", [
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Vizsgáld meg és ábrázold: $y=x^{2}-2x-3$.</p>',
         hid="pelda-teljes-vizsgalat",
         lenyilo=("Megoldás — lépésről lépésre",
                  '<p><b>1. Nyílásirány:</b> $a=1&gt;0$ → felfelé nyílik, <b>konvex</b>, '
                  'minimuma lesz.</p>'
                  '<p><b>2. Zérushelyek:</b> $D=4+12=16$, '
                  '$x_{1,2}=\\dfrac{2\\pm 4}{2}$ → $x_{1}=-1$, $x_{2}=3$.</p>'
                  '<p><b>3. $y$-tengelymetszet:</b> $f(0)=-3$.</p>'
                  '<p><b>4. Csúcspont:</b> $u=-\\dfrac{-2}{2}=1$, '
                  '$v=f(1)=1-2-3=-4$ → $C(1;-4)$.</p>'
                  '<p><b>5. Szélsőérték:</b> minimum, értéke $-4$ (az $x=1$ helyen).</p>'
                  '<p><b>6. Értékkészlet:</b> $[-4,+\\infty)$.</p>')),
   abra(SVG_VIZSG, "A grafikonhoz elég három adat: a <b>két zérushely</b>, a "
                   "<b>csúcspont</b> és az <b>$y$-tengelymetszet</b>. A parabola "
                   "szimmetrikus az $x=1$ egyenesre."),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Három visszatérő hiba:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>A csúcs $y$-koordinátáját „megsaccolni".</b> Nem a két zérushely '
         'átlagának képe, hanem $f(u)$ — <b>be kell helyettesíteni</b>. (Az $u$ viszont '
         'valóban a két zérushely átlaga, ha vannak.)</li>'
         '<li><b>Az értékkészletet $\\mathbb{R}$-nek írni.</b> Az az <b>értelmezési '
         'tartomány</b>. Az értékkészlet a csúcstól indul.</li>'
         '<li><b>A minimum és a minimumhely összekeverése.</b> A minimum <b>értéke</b> '
         '$v=-4$; a minimum<b>hely</b> $x=1$.</li>'
         '</ol>'),
   kviz('Mi az $y=x^{2}-6x+8$ függvény értékkészlete?',
        ['$[-1,+\\infty)$', '$\\mathbb{R}$', '$[8,+\\infty)$'], 0,
        jo="✔ u = 3, v = 9 − 18 + 8 = −1, és a > 0 → [−1, +∞).",
        nem="✘ Számold ki a csúcsot: u = 3, v = f(3) = −1. Mivel a > 0, az értékkészlet [−1, +∞)."),
 ]),

 ("Ha a parabola lefelé nyílik", [
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Vizsgáld meg: $y=-x^{2}+4x-3$.</p>',
         hid="pelda-konkav",
         lenyilo=("Megoldás",
                  '<p><b>1.</b> $a=-1&lt;0$ → lefelé nyílik, <b>konkáv</b>, maximuma lesz.</p>'
                  '<p><b>2.</b> $D=16-12=4$, $x_{1,2}=\\dfrac{-4\\pm 2}{-2}$ → '
                  '$x_{1}=1$, $x_{2}=3$.</p>'
                  '<p><b>3.</b> $f(0)=-3$.</p>'
                  '<p><b>4.</b> $u=-\\dfrac{4}{-2}=2$, $v=f(2)=-4+8-3=1$ → $C(2;1)$.</p>'
                  '<p><b>5.</b> <b>Maximum</b>, értéke $1$.</p>'
                  '<p><b>6.</b> Értékkészlet: $(-\\infty,1]$.</p>')),
 ]),

 ("Szélsőérték-feladatok", [
   'A másodfokú függvény leggyakoribb valós alkalmazása: valamit <b>maximalizálni</b> '
   'vagy <b>minimalizálni</b> kell. A recept: írd fel a keresett mennyiséget egyetlen '
   'változó másodfokú függvényeként, majd keresd meg a csúcspontot.',
   doboz("pelda", "Vészterem-szimuláció — a kerítés",
         '<p>A kampusz fala mellé téglalap alakú edzőterületet kerítenek be. A fal felőli '
         'oldalra nem kell kerítés, a másik három oldalra összesen $20$ méter kerítés áll '
         'rendelkezésre. Mekkora a lehető legnagyobb bekeríthető terület?</p>',
         hid="pelda-szelsoertek",
         lenyilo=("Megoldás",
                  '<p>Legyen a fallal <b>párhuzamos</b> oldal $y$, a rá merőleges kettő '
                  'pedig $x$-$x$. Ekkor $2x+y=20$, tehát $y=20-2x$.</p>'
                  '<p>A terület:</p>'
                  '$$T(x)=x\\left(20-2x\\right)=-2x^{2}+20x.$$'
                  '<p>Ez másodfokú függvény $a=-2&lt;0$ főegyütthatóval → van <b>maximuma</b> '
                  'a csúcspontban: $u=-\\dfrac{20}{-4}=5$, és $T(5)=-50+100=50$.</p>'
                  '<p><b>Válasz:</b> a merőleges oldalak $5$ m-esek, a fallal párhuzamos '
                  '$10$ m, a legnagyobb terület $50\\ \\text{m}^{2}$.</p>')),
   kviz('Egy $T(x)=-x^{2}+12x$ területfüggvény hol veszi fel a maximumát?',
        ['$x=6$-nál, az értéke $36$.', '$x=12$-nél, az értéke $0$.',
         '$x=-6$-nál, az értéke $36$.'], 0,
        jo="✔ u = −12/(−2) = 6, és T(6) = −36 + 72 = 36.",
        nem="✘ A csúcs u = −b/(2a) = −12/(−2) = 6, ahol T(6) = 36."),
   gyakorolj(FGY + "#alap-6", "A 6–11", FGY + "#kozep-5", "K 5–10"),
   brief('<b>Küklopsz:</b> Eddig azt kérdeztük, <b>hol nulla</b> a függvény. A következő '
         'lépés: hol <b>pozitív</b> és hol <b>negatív</b>? Ez már nem egy pont, hanem '
         'egy egész <b>tartomány</b> — és pontosan ilyen a védőpajzs hatósugara is. '
         'Jöjjenek a másodfokú egyenlőtlenségek.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-masodfoku-fuggveny.html",
     cim="A másodfokú függvény és grafikonja", cim_tiszta="A másodfokú függvény és grafikonja",
     alcim="A parabola és a főegyüttható szerepe, a kanonikus alak és a csúcspont, "
           "valamint a parabola és az $x$-tengely hat lehetséges kölcsönös helyzete.",
     chip="Az M-Faktor · 5/8", szakaszok=B1,
     elozo=(FGY.replace("fuggveny", "egyenletek"), "Feladatok — másodfokú egyenletek"),
     kovetkezo=("tananyag-fuggvenyvizsgalat.html", "A másodfokú függvény vizsgálata")),
 lap(**T, fajl="tananyag-fuggvenyvizsgalat.html",
     cim="A másodfokú függvény vizsgálata", cim_tiszta="A másodfokú függvény vizsgálata",
     alcim="A vizsgálat rögzített szempontsora, teljes kidolgozott példák konvex és "
           "konkáv esetre, valamint szélsőérték-feladatok valós helyzetekben.",
     chip="Az M-Faktor · 6/8", szakaszok=B2,
     elozo=("tananyag-masodfoku-fuggveny.html", "A másodfokú függvény és grafikonja"),
     kovetkezo=(FGY, "Feladatok — másodfokú függvény")),
]
for u in KI:
    print("✓", os.path.basename(u))
