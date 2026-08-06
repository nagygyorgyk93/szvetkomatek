# -*- coding: utf-8 -*-
"""2e/03 — A altema: az exponencialis fuggveny (A1), exponencialis egyenletek (A2)
es egyenlotlensegek (A3). Mentor: Dr. Bestia."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
         temakor="Exponenciális és logaritmusfüggvény")
FGY = "feladatok-exponencialis.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, solve, simplify, nsimplify
x, t = symbols('x t', real=True)
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
chk("A1-alap", R(2)**0, 1)
chk("A1-neg", R(2)**-3, R(1, 8))
chk("A1-tukor", R(1, 2)**3, R(2)**-3)
chk("A2-1", solve(3*x - 12, x), [4])                 # 2^{3x}=2^{12}
chk("A2-2", sorted(solve(x**2 - 5*x + 6, x)), [2, 3])
chk("A2-3", solve(2*x + 1 - 5, x), [2])              # 9^{...}: 2x+1=5
chk("A2-kiem", 2**5 + 2**3, 40);   chk("A2-kiem2", solve(2**x - 8, x), [3])
chk("A2-kiem3", 3**6 - 3**4, 648); chk("A2-kiem4", solve(3**x - 81, x), [4])
chk("A2-msf", sorted(solve(t**2 - 6*t + 8, t)), [2, 4])
chk("A2-msf2", sorted(solve(t**2 - 4*t + 3, t)), [1, 3])
chk("A2-msf3", sorted(solve(t**2 + 3*t - 4, t)), [-4, 1])
chk("A3-1", solve(2*x - 1 - 3, x), [2])              # 2^{2x-1}<2^3
chk("A3-2", solve(3*x + 2 - 5, x), [1])
chk("A3-3", solve(x - 4, x), [4])                    # (1/2)^x >= (1/2)^4
chk("A3-4", solve(2*x + 3 + 1, x), [-2])
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_NO = svg_fuggvenyek(
    [(lambda u: 2**u, "#047857", "y = 2ˣ", [(-3.4, 2.3)]),
     (lambda u: 3**u, "#3b82f6", "y = 3ˣ", [(-3.4, 1.6)]),
     (lambda u: 1.5**u, "#8b5cf6", "y = 1,5ˣ", [(-3.4, 3.4)])],
    xr=(-3.4, 3.4), yr=(-1.2, 5.0), w=380, h=260,
    leiras="Növekvő exponenciális függvények: minél nagyobb az alap, annál meredekebb a görbe",
    pontok=[(0, 1, "(0; 1)", "#ef4444", 8, 16)])

SVG_CS = svg_fuggvenyek(
    [(lambda u: 2**u, "#047857", "y = 2ˣ", [(-3.4, 2.3)]),
     (lambda u: 0.5**u, "#ef4444", "y = (½)ˣ", [(-2.3, 3.4)])],
    xr=(-3.4, 3.4), yr=(-1.2, 5.0), w=380, h=260,
    leiras="Az y = 2 az x-edik és az y = fél az x-edik függvény grafikonja "
           "egymás tükörképe az y-tengelyre",
    pontok=[(0, 1, "(0; 1)", "#8b5cf6", 8, 16)])

SVG_ELT = svg_fuggvenyek(
    [(lambda u: 2**u, "#94a3b8", "y = 2ˣ", [(-3.4, 2.3)]),
     (lambda u: 2**u - 3, "#047857", "y = 2ˣ − 3", [(-3.4, 2.9)]),
     (lambda u: 2**(u - 2), "#3b82f6", "y = 2ˣ⁻²", [(-3.4, 4.3)])],
    xr=(-3.4, 4.3), yr=(-3.6, 5.0), w=380, h=280,
    leiras="Az alapgörbe függőleges és vízszintes eltolása")

# ===================================================================== A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> Kadétok, a laborban rossz hírt kaptam. Dr. Baljós vírusa nem '
         'lineárisan és nem is másodfokon terjed: minden órában <b>megkétszereződik</b> '
         'a fertőzött sejtek száma. Egy óra múlva 2, kettő múlva 4, tíz óra múlva már '
         'több mint ezer. Ez az <b>exponenciális növekedés</b> — a természet '
         'leggyorsabb hétköznapi mechanizmusa. Ha meg akarjuk állítani, előbb le kell '
         'írnunk. Kezdjük a görbével.'),
   'Eddig a hatványozásnál az <b>alap</b> volt a változó ($x^{2}$, $x^{3}$ — '
   '<a href="../01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-hatvanyfuggveny.html">'
   'hatványfüggvény</a>). Most cserét hajtunk végre: az alap lesz <b>rögzített</b>, '
   'és a <b>kitevő</b> válik változóvá. Ez az egyetlen csere gyökeresen más '
   'viselkedésű függvényt ad.',
 ]),

 ("Az exponenciális függvény fogalma", [
   doboz("definicio", "Exponenciális függvény",
         '<p><b>Exponenciális függvénynek</b> nevezzük az $f:\\mathbb{R}\\to\\mathbb{R}^{+}$,</p>'
         '$$f(x)=a^{x},\\qquad a&gt;0,\\ a\\neq 1$$'
         '<p>alakú valós függvényt. Az $a$ szám a függvény <b>alapja</b>.</p>',
         hid="def-exponencialis"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Miért kell a két kikötés?</p>'
         '<ul>'
         '<li><b>$a&gt;0$:</b> ha az alap negatív lenne, a hatvány sok $x$-re nem lenne '
         'értelmezhető a valós számok között — például $(-4)^{1/2}=\\sqrt{-4}$ nem valós szám. '
         'A függvény „lyukas” lenne.</li>'
         '<li><b>$a\\neq 1$:</b> az $1^{x}$ minden $x$-re $1$ — ez a konstans függvény, '
         'nem mond semmit a kitevőről.</li>'
         '</ul>'
         '<p>Az $a=0$ eset szintén kiesik: $0^{x}$ negatív kitevőre nullával való '
         'osztás lenne.</p>'),
   'A <b>kitevő bármely valós szám</b> lehet — nemcsak egész. Hogy ennek van értelme, '
   'azt épp az I. témakörben alapoztuk meg: a '
   '<a href="../01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-gyoktelenites-es-racionalis-kitevo.html">'
   'racionális kitevőjű hatvány</a> a gyökvonással definiálható, az irracionális kitevő pedig '
   'ezekből közelítéssel adódik.',
   kviz('Melyik NEM exponenciális függvény?',
        ['$f(x)=x^{3}$', '$f(x)=3^{x}$', '$f(x)=\\left(\\tfrac13\\right)^{x}$'], 0,
        jo="✔ Az x³-ben a KITEVŐ állandó és az ALAP változik — ez hatványfüggvény.",
        nem="✘ Nézd meg, hol van az x: exponenciálisnál a KITEVŐBEN, hatványfüggvénynél az ALAPBAN."),
 ]),

 ("A két alapeset: növekvő és csökkenő", [
   'Az egész témakör legfontosabb megkülönböztetése az, hogy az alap <b>nagyobb</b> vagy '
   '<b>kisebb</b> $1$-nél. Ez dönti el, hogy a függvény nő vagy csökken — és később ez '
   'fogja eldönteni az egyenlőtlenségek irányát is.',
   abra(SVG_NO, "$a&gt;1$ esetén a függvény <b>növekvő</b>. Minél nagyobb az alap, "
                "annál meredekebben emelkedik — de mindegyik görbe átmegy a $(0;1)$ ponton."),
   abra(SVG_CS, "$0&lt;a&lt;1$ esetén a függvény <b>csökkenő</b>. Az $y=\\left(\\tfrac12\\right)^{x}$ "
                "az $y=2^{x}$ tükörképe az $y$-tengelyre, hiszen "
                "$\\left(\\tfrac12\\right)^{x}=2^{-x}$."),
   doboz("tetel", "Monotonitás",
         '<p>Az $f(x)=a^{x}$ függvény</p>'
         '<ul>'
         '<li><b>szigorúan növekvő</b>, ha $a&gt;1$;</li>'
         '<li><b>szigorúan csökkenő</b>, ha $0&lt;a&lt;1$.</li>'
         '</ul>'
         '<p>Mindkét esetben <b>kölcsönösen egyértelmű</b> (injektív): különböző kitevőkhöz '
         'különböző értékek tartoznak. Ez az a tulajdonság, amire az összes exponenciális '
         'egyenlet megoldása épül.</p>',
         hid="tetel-monotonitas"),
   doboz("erdekesseg", "Miért ilyen gyors?",
         '<p>Ha egy papírlapot elméletben $42$-szer félbehajtanál, a vastagsága '
         '$0{,}1\\ \\text{mm}\\cdot 2^{42}$ lenne — nagyjából <b>440 000 km</b>, több mint '
         'a Föld–Hold távolság. Ez ugyanaz a $2^{x}$, amit a grafikonon látsz: a bal oldalon '
         'szinte rátapad a tengelyre, a jobb oldalon pedig elszalad.</p>'),
 ]),

 ("Tulajdonságok", [
   doboz("tetel", "Az $f(x)=a^{x}$ függvény tulajdonságai",
         '<div class="tblwrap"><table>'
         '<tr><th>Tulajdonság</th><th>$a&gt;1$</th><th>$0&lt;a&lt;1$</th></tr>'
         '<tr><td>Értelmezési tartomány</td><td colspan="2">$\\mathbb{R}$ — minden valós szám</td></tr>'
         '<tr><td>Értékkészlet</td><td colspan="2">$(0;+\\infty)$ — <b>mindig pozitív</b></td></tr>'
         '<tr><td>Nullahely</td><td colspan="2">nincs (a görbe sosem éri el a tengelyt)</td></tr>'
         '<tr><td>Metszés az $y$-tengellyel</td><td colspan="2">$(0;1)$, mert $a^{0}=1$</td></tr>'
         '<tr><td>Monotonitás</td><td>szigorúan növekvő</td><td>szigorúan csökkenő</td></tr>'
         '<tr><td>Aszimptota</td><td colspan="2">az $x$-tengely ($y=0$)</td></tr>'
         '</table></div>',
         hid="tetel-tulajdonsagok"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Az exponenciális függvény értéke SOHA nem nulla és soha nem negatív.</b> '
         'A görbe tetszőlegesen közel kerül az $x$-tengelyhez, de nem éri el. Ezért:</p>'
         '<ul>'
         '<li>a $2^{x}=0$ egyenletnek <b>nincs</b> megoldása;</li>'
         '<li>a $3^{x}=-5$ egyenletnek <b>nincs</b> megoldása;</li>'
         '<li>a $2^{x}&gt;0$ egyenlőtlenség <b>minden</b> valós $x$-re teljesül.</li>'
         '</ul>'
         '<p>Ez a későbbi helyettesítéses feladatoknál kulcsfontosságú lesz: ha $t=a^{x}$, '
         'akkor <b>$t&gt;0$</b>, és a negatív $t$-gyököket el kell dobni.</p>'),
   kviz('Mennyi az $f(x)=5^{x}$ függvény értékkészlete?',
        ['$(0;+\\infty)$', '$\\mathbb{R}$', '$[0;+\\infty)$'], 0,
        jo="✔ Minden pozitív értéket felvesz, de a nullát soha.",
        nem="✘ A görbe végig a tengely FÖLÖTT halad, és a nullát sem éri el: (0; +∞)."),
 ]),

 ("Eltolás és tükrözés", [
   'A grafikon rajzolásához nem kell értéktáblázat: elég az alapgörbe, és rá a már ismert '
   '<b>transzformációk</b>.',
   abra(SVG_ELT, "Az $y=2^{x}-3$ három egységgel <b>lefelé</b> tolt görbe (az aszimptota "
                 "is levándorol az $y=-3$ egyenesre), az $y=2^{x-2}$ pedig két egységgel "
                 "<b>jobbra</b> tolt (az aszimptota marad az $x$-tengely)."),
   doboz("tetel", "A négy alapmozgás",
         '<div class="tblwrap"><table>'
         '<tr><th>Alak</th><th>Mit csinál?</th><th>Aszimptota</th></tr>'
         '<tr><td>$y=a^{x}+c$</td><td>$c$ egységgel <b>fel</b> (ha $c&gt;0$)</td><td>$y=c$</td></tr>'
         '<tr><td>$y=a^{x-b}$</td><td>$b$ egységgel <b>jobbra</b> (ha $b&gt;0$)</td><td>$y=0$</td></tr>'
         '<tr><td>$y=a^{-x}$</td><td>tükrözés az <b>$y$-tengelyre</b></td><td>$y=0$</td></tr>'
         '<tr><td>$y=-a^{x}$</td><td>tükrözés az <b>$x$-tengelyre</b></td><td>$y=0$</td></tr>'
         '</table></div>'
         '<p>Figyelj a <b>vízszintes</b> eltolás előjelére: az $y=2^{x-2}$ <b>jobbra</b> tol, '
         'nem balra — a kitevőben a $-2$ „késlelteti” a függvényt.</p>',
         hid="tetel-transzformaciok"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Ábrázold és jellemezd: <b>a)</b> $y=3^{x}-1$; '
         '<b>b)</b> $y=\\left(\\tfrac12\\right)^{x+2}$.</p>',
         hid="pelda-transzformacio",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> Az $y=3^{x}$ görbét $1$-gyel lefelé toljuk. Az aszimptota '
                  '$y=-1$, az értékkészlet $(-1;+\\infty)$. Most már <b>van</b> nullahelye: '
                  '$3^{x}=1$, tehát $x=0$ — a görbe az origón megy át.</p>'
                  '<p><b>b)</b> Az $y=\\left(\\tfrac12\\right)^{x}$ csökkenő görbét '
                  '$2$-vel <b>balra</b> toljuk. Az aszimptota marad az $x$-tengely, '
                  'az értékkészlet $(0;+\\infty)$, és a görbe a $(0;\\tfrac14)$ ponton halad át, '
                  'mert $\\left(\\tfrac12\\right)^{2}=\\tfrac14$.</p>')),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
 ]),
]

# ===================================================================== A2

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> A görbét ismerjük — most jön a kérdés, amiért az egészet '
         'csináljuk: <b>mikor</b> éri el a fertőzés a kritikus szintet? Ez egy egyenlet, '
         'amelyben az ismeretlen a <b>kitevőben</b> ül. Jó hír: nem kell új gépezet. '
         'Egyetlen ötlet elég — ha a két oldalt <b>ugyanarra az alapra</b> hozzuk, '
         'a kitevők egyenlővé tehetők.'),
 ]),

 ("Az alapelv", [
   doboz("tetel", "Az exponenciális egyenlet alaptétele",
         '<p>Ha $a&gt;0$ és $a\\neq 1$, akkor</p>'
         '$$a^{u}=a^{v}\\iff u=v.$$'
         '<p>Miért? Mert az $a^{x}$ függvény <b>kölcsönösen egyértelmű</b>: '
         'két különböző kitevőhöz sosem tartozik ugyanaz az érték. Ezért ha a két '
         'hatvány egyenlő, a kitevőknek is egyenlőnek kell lenniük.</p>'
         '<p>A megoldás menete tehát: <b>hozd közös alapra</b> a két oldalt, majd '
         '<b>hagyd el az alapot</b>, és oldd meg a maradék — általában elsőfokú vagy '
         'másodfokú — egyenletet.</p>',
         hid="tetel-alapelv"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $8^{x}=4096$; <b>b)</b> $9^{x+1}=27^{2x-1}$; '
         '<b>c)</b> $2^{x^{2}-5x}=\\tfrac{1}{64}$.</p>',
         hid="pelda-kozos-alap",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $8=2^{3}$ és $4096=2^{12}$, tehát $2^{3x}=2^{12}$, '
                  'innen $3x=12$, azaz $\\boxed{x=4}$.</p>'
                  '<p><b>b)</b> Közös alap a $3$: $\\left(3^{2}\\right)^{x+1}=\\left(3^{3}\\right)^{2x-1}$, '
                  'azaz $3^{2x+2}=3^{6x-3}$. Innen $2x+2=6x-3$, tehát $4x=5$, '
                  '$\\boxed{x=\\tfrac54}$.</p>'
                  '<p><b>c)</b> $\\tfrac{1}{64}=2^{-6}$, tehát $x^{2}-5x=-6$, azaz '
                  '$x^{2}-5x+6=0$. A gyökök $\\boxed{x_{1}=2}$ és $\\boxed{x_{2}=3}$.</p>')),
   kviz('Mi a megoldása a $5^{2x}=125$ egyenletnek?',
        ['$x=\\tfrac32$', '$x=3$', '$x=25$'], 0,
        jo="✔ 125 = 5³, tehát 2x = 3.",
        nem="✘ Írd 125-öt 5-hatványként: 125 = 5³, így 2x = 3."),
 ]),

 ("Kiemelés — amikor több hatvány szerepel", [
   'Gyakori típus, hogy ugyanannak az alapnak <b>több, egymáshoz közeli kitevőjű</b> '
   'hatványa szerepel. Ilyenkor a hatványozás azonossága segít:',
   doboz("tetel", "A kulcsazonosság",
         '$$a^{x+k}=a^{x}\\cdot a^{k}$$'
         '<p>Vagyis a „$+k$” a kitevőben egy <b>állandó szorzót</b> jelent. Ezért az '
         '$a^{x}$ minden tagból <b>kiemelhető</b>, és utána már egyszerű egyenlet marad.</p>',
         hid="tetel-kiemeles"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $2^{x+2}+2^{x}=40$; <b>b)</b> $3^{x+2}-3^{x}=648$.</p>',
         hid="pelda-kiemeles",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $2^{x}\\cdot 2^{2}+2^{x}=40$, azaz $2^{x}(4+1)=40$, '
                  'tehát $5\\cdot 2^{x}=40$ és $2^{x}=8$. Innen $\\boxed{x=3}$.</p>'
                  '<p><b>b)</b> $3^{x}\\left(3^{2}-1\\right)=648$, azaz $8\\cdot 3^{x}=648$, '
                  'tehát $3^{x}=81$ és $\\boxed{x=4}$.</p>'
                  '<p><b>Ellenőrzés:</b> $2^{5}+2^{3}=32+8=40$ ✔ és $3^{6}-3^{4}=729-81=648$ ✔</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A $2^{x+2}$ <b>nem</b> $2^{x}+2^{2}$! A kitevőben álló összeg '
         '<b>szorzattá</b> bomlik, nem összeggé:</p>'
         '<p>✘ $2^{x+2}=2^{x}+4$ &nbsp;&nbsp;&nbsp; ✔ $2^{x+2}=2^{x}\\cdot 4$</p>'
         '<p>Próbáld ki $x=1$-gyel: $2^{3}=8$, míg $2^{1}+4=6$ — nem ugyanaz.</p>'),
   kviz('Mivel egyenlő $5^{x+1}$?',
        ['$5\\cdot 5^{x}$', '$5^{x}+5$', '$25^{x}$'], 0,
        jo="✔ A kitevőben álló összeg szorzattá bomlik.",
        nem="✘ aˣ⁺ᵏ = aˣ · aᵏ — tehát 5ˣ⁺¹ = 5ˣ · 5."),
 ]),

 ("Másodfokúra visszavezethető exponenciális egyenlet", [
   'Ez a témakör legszebb típusa — és pontosan ugyanaz a gondolat, mint a '
   '<a href="../02-masodfoku-egyenletek-es-fuggvenyek/tananyag-bikvadratikus.html">'
   'bikvadratikus egyenletnél</a>: egy ügyes <b>helyettesítéssel</b> visszavezetjük '
   'a feladatot olyanra, amit már tudunk.',
   doboz("tetel", "A helyettesítés módszere",
         '<p>Ha az egyenletben $a^{2x}$ (vagy $a^{x}$ négyzete) és $a^{x}$ is szerepel, '
         'vezess be új ismeretlent:</p>'
         '$$t=a^{x},\\qquad \\textbf{ahol } t&gt;0.$$'
         '<p>Ekkor $a^{2x}=\\left(a^{x}\\right)^{2}=t^{2}$, és az egyenlet '
         '<b>másodfokúvá</b> válik. A $t$-re kapott gyököket <b>vissza kell '
         'helyettesíteni</b>, és a nem pozitívakat el kell dobni.</p>',
         hid="tetel-helyettesites"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Két hiba les rád:</b></p>'
         '<ol class="reszfeladatok">'
         '<li><b>Megállni $t$-nél.</b> A $t$ nem a válasz! A feladat $x$-et kérdezi — '
         'a $t$-ből még vissza kell számolni.</li>'
         '<li><b>A negatív $t$-gyököt megtartani.</b> Mivel $t=a^{x}$ mindig '
         '<b>pozitív</b>, a $t\\le 0$ gyök nem ad megoldást — ilyenkor nem hibáztál, '
         'egyszerűen kevesebb megoldás van.</li>'
         '</ol>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $4^{x}-6\\cdot 2^{x}+8=0$; '
         '<b>b)</b> $9^{x}-4\\cdot 3^{x}+3=0$; <b>c)</b> $4^{x}+3\\cdot 2^{x}-4=0$.</p>',
         hid="pelda-masodfoku",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $4^{x}=\\left(2^{x}\\right)^{2}$, legyen $t=2^{x}&gt;0$: '
                  '$t^{2}-6t+8=0$, ahonnan $t_{1}=2$, $t_{2}=4$. Visszahelyettesítve '
                  '$2^{x}=2$ és $2^{x}=4$, tehát $\\boxed{x_{1}=1}$, $\\boxed{x_{2}=2}$.</p>'
                  '<p><b>b)</b> $t=3^{x}&gt;0$: $t^{2}-4t+3=0$, innen $t_{1}=1$, $t_{2}=3$, '
                  'azaz $3^{x}=1$ és $3^{x}=3$: $\\boxed{x_{1}=0}$, $\\boxed{x_{2}=1}$.</p>'
                  '<p><b>c)</b> $t=2^{x}&gt;0$: $t^{2}+3t-4=0$, a gyökök $t_{1}=1$ és '
                  '$t_{2}=-4$. A $-4$ <b>nem lehet</b> $2^{x}$ értéke, ezért elhagyjuk. '
                  'Marad $2^{x}=1$, tehát $\\boxed{x=0}$ — egyetlen megoldás.</p>')),
   kviz('A $t=3^{x}$ helyettesítés után $t_{1}=9$ és $t_{2}=-1$ adódott. Mi a megoldás?',
        ['$x=2$', '$x=2$ és $x=-1$', '$x=9$ és $x=-1$'], 0,
        jo="✔ A −1 nem lehet 3ˣ, marad 3ˣ = 9, azaz x = 2.",
        nem="✘ A t = 3ˣ mindig pozitív, tehát a −1 kiesik; a 9-ből x = 2."),
   gyakorolj(FGY + "#alap-7", "A 7–14", FGY + "#kozep-4", "K 4–10"),
 ]),
]

# ===================================================================== A3

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> Az egyenlet arra felel, <b>mikor pontosan</b> — de a valóságban '
         'sokkal fontosabb, hogy <b>meddig</b> maradunk biztonságban. Ez már '
         'egyenlőtlenség. És itt van a témakör egyetlen igazi buktatója: ha az alap '
         '<b>kisebb $1$-nél</b>, a reláció jele <b>megfordul</b>. Ne tanuld be — értsd meg. '
         'A grafikon megmutatja, miért.'),
 ]),

 ("Az alapelv és a jelfordulás", [
   'A gondolat ugyanaz, mint az egyenleteknél: közös alapra hozunk, majd elhagyjuk az '
   'alapot. A különbség, hogy most a <b>monotonitásra</b> is figyelnünk kell.',
   doboz("tetel", "Exponenciális egyenlőtlenség",
         '<p>Tegyük fel, hogy az egyenlőtlenség $a^{u}&lt;a^{v}$ alakú.</p>'
         '<ul>'
         '<li>Ha <b>$a&gt;1$</b> (a függvény <b>növekvő</b>): a nagyobb kitevőhöz nagyobb '
         'érték tartozik, ezért $u&lt;v$ — a <b>reláció iránya megmarad</b>.</li>'
         '<li>Ha <b>$0&lt;a&lt;1$</b> (a függvény <b>csökkenő</b>): a nagyobb kitevőhöz '
         '<b>kisebb</b> érték tartozik, ezért $u&gt;v$ — a <b>reláció MEGFORDUL</b>.</li>'
         '</ul>',
         hid="tetel-jelfordulas"),
   abra(SVG_CS, "A csökkenő görbén jobbra haladva a függvényérték <b>csökken</b>. "
                "Ezért ha $\\left(\\tfrac12\\right)^{u}&lt;\\left(\\tfrac12\\right)^{v}$, "
                "akkor $u$-nak <b>nagyobbnak</b> kell lennie $v$-nél — ez a jelfordulás oka."),
   doboz("erdekesseg", "Ismerős?",
         '<p>Ugyanez a szabály, amit már ismersz: negatív számmal osztva vagy szorozva az '
         'egyenlőtlenséget, a jel megfordul. Mindkét esetben ugyanaz az ok — egy '
         '<b>csökkenő</b> művelet sorrendet cserél.</p>'),
 ]),

 ("Megoldott feladatok", [
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $2^{2x-1}&lt;8$; <b>b)</b> $\\left(\\tfrac12\\right)^{x}\\ge\\tfrac{1}{16}$; '
         '<b>c)</b> $\\left(\\tfrac13\\right)^{2x+3}&gt;3$.</p>',
         hid="pelda-egyenlotlensegek",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $8=2^{3}$, az alap $2&gt;1$, a jel <b>marad</b>: '
                  '$2x-1&lt;3$, tehát $2x&lt;4$ és $\\boxed{x&lt;2}$, azaz '
                  '$x\\in(-\\infty;2)$.</p>'
                  '<p><b>b)</b> $\\tfrac{1}{16}=\\left(\\tfrac12\\right)^{4}$, az alap '
                  '$0&lt;\\tfrac12&lt;1$, a jel <b>fordul</b>: $x\\le 4$, azaz '
                  '$\\boxed{x\\in(-\\infty;4]}$.</p>'
                  '<p><b>c)</b> $3=\\left(\\tfrac13\\right)^{-1}$, az alap kisebb $1$-nél, '
                  'a jel <b>fordul</b>: $2x+3&lt;-1$, tehát $2x&lt;-4$ és '
                  '$\\boxed{x&lt;-2}$, azaz $x\\in(-\\infty;-2)$.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Három hiba, amit a dolgozatokon a legtöbbször látni:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>A jelfordulás elfelejtése.</b> Mielőtt elhagyod az alapot, mindig kérdezd '
         'meg: <i>nagyobb ez az alap $1$-nél?</i> Írd is oda a lap szélére.</li>'
         '<li><b>Rossz irányba fordítani.</b> A jel csak akkor fordul, ha '
         '$0&lt;a&lt;1$ — az $a&gt;1$ eset változatlan.</li>'
         '<li><b>Zárt zárójel a végtelennél.</b> A $\\pm\\infty$ mellett '
         '<b>mindig nyitott</b> zárójel áll: $(-\\infty;2)$, sosem $(-\\infty;2]$ '
         'a végtelen oldalán.</li>'
         '</ol>'),
   kviz('Mi a megoldása a $\\left(\\tfrac14\\right)^{x}&gt;\\tfrac{1}{64}$ egyenlőtlenségnek?',
        ['$x&lt;3$', '$x&gt;3$', '$x&gt;\\tfrac{1}{64}$'], 0,
        jo="✔ Az alap ¼ < 1, ezért a jel megfordul: x < 3.",
        nem="✘ 1/64 = (¼)³, és az alap kisebb 1-nél — a reláció megfordul: x < 3."),
   gyakorolj(FGY + "#alap-15", "A 15–20", FGY + "#kozep-11", "K 11–14"),
   brief('<b>Dr. Bestia:</b> Kiváló. Az exponenciális blokk kész — ez a <b>3. ellenőrző</b> '
         'anyaga. A gyűjtemény végén találsz egy külön felkészítő sávot hozzá. '
         'Utána viszont megfordítjuk a kérdést: eddig azt kérdeztük, <i>mennyi lesz '
         '$x$ óra múlva</i>. A következő küldetésben azt: <b>hány óra kell hozzá?</b> '
         'Ehhez új eszköz kell — a <b>logaritmus</b>.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-exponencialis-fuggveny.html",
     cim="Az exponenciális függvény", cim_tiszta="Az exponenciális függvény",
     alcim="A fogalom és a két alapeset ($a&gt;1$ és $0&lt;a&lt;1$), a függvény "
           "tulajdonságai, valamint a grafikon eltolása és tükrözése.",
     chip="Az Evolúciós Ugrás · 1/8", szakaszok=A1,
     elozo=("index.html", "Exponenciális és logaritmusfüggvény"),
     kovetkezo=("tananyag-exponencialis-egyenletek.html", "Exponenciális egyenletek")),
 lap(**T, fajl="tananyag-exponencialis-egyenletek.html",
     cim="Exponenciális egyenletek", cim_tiszta="Exponenciális egyenletek",
     alcim="Közös alapra hozás, kiemelés, valamint a helyettesítéssel másodfokúra "
           "visszavezethető egyenletek.",
     chip="Az Evolúciós Ugrás · 2/8", szakaszok=A2,
     elozo=("tananyag-exponencialis-fuggveny.html", "Az exponenciális függvény"),
     kovetkezo=("tananyag-exponencialis-egyenlotlensegek.html",
                "Exponenciális egyenlőtlenségek")),
 lap(**T, fajl="tananyag-exponencialis-egyenlotlensegek.html",
     cim="Exponenciális egyenlőtlenségek", cim_tiszta="Exponenciális egyenlőtlenségek",
     alcim="A monotonitásból következő jelfordulás, a megoldás intervallumos alakja "
           "és a tipikus hibák.",
     chip="Az Evolúciós Ugrás · 3/8", szakaszok=A3,
     elozo=("tananyag-exponencialis-egyenletek.html", "Exponenciális egyenletek"),
     kovetkezo=(FGY, "Feladatok — exponenciális függvény")),
]
for u in KI:
    print("✓", os.path.basename(u))
