# -*- coding: utf-8 -*-
"""2e/02 — C altema: masodfoku egyenlotlensegek (C1) es a masodfoku-linearis rendszer (C2).
Mentor: Küklopsz."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
         temakor="Másodfokú egyenletek és függvények")
FGY = "feladatok-egyenlotlensegek-es-rendszerek.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, solve, simplify, Eq, im, re as _re
x, y, t = symbols('x y t')
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
chk("C1-1", sorted(solve(x**2-5*x+6, x)), [2, 3])
chk("C1-2", sorted(solve(x**2-4*x+4, x)), [2])
chk("C1-3", 1-4, -3)                                     # x^2+x+1 diszkriminánsa
chk("C1-4", sorted(solve(x**2-3*x+2, x)), [1, 2])
chk("C1-5", sorted(solve(2*x**2-7*x+3, x)), [R(1,2), 3])
chk("C2-1", sorted(solve(x**2-3*x+2, x)), [1, 2])
chk("C2-2", sorted(solve(t**2-7*t+12, t)), [3, 4])
chk("C2-3", sorted(solve(y**2+2*y-3, y)), [-3, 1])
chk("C2-4", sorted(solve(x**2-2*x+1, x)), [1])
chk("C2-5", 4-20, -16)                                   # x^2-2x+5 diszkriminánsa
assert not E, E
print("sympy önteszt: OK")

SVG_EGYENL = svg_fuggvenyek(
    [(lambda u: u**2-5*u+6, "#047857", "y = x² − 5x + 6", [(0.2, 4.8)])],
    xr=(-0.6, 5.4), yr=(-1.6, 4.4), w=380, h=250,
    leiras="Az y = x² − 5x + 6 parabola: a 2 és a 3 között a tengely alatt, azon kívül fölötte",
    pontok=[(2, 0, "2", "#ef4444", -4, -8), (3, 0, "3", "#ef4444", 4, -8)])

SVG_RENDSZER = svg_fuggvenyek(
    [(lambda u: u**2-2*u, "#047857", "y = x² − 2x", [(-1.3, 3.3)]),
     (lambda u: u-2, "#3b82f6", "y = x − 2", [(-1.5, 4.0)])],
    xr=(-1.8, 4.2), yr=(-3.4, 4.2), w=380, h=270,
    leiras="Az y = x² − 2x parabola és az y = x − 2 egyenes két metszéspontja",
    pontok=[(1, -1, "(1; −1)", "#8b5cf6", -50, 16), (2, 0, "(2; 0)", "#8b5cf6", 8, -8)])

# ===================================================================== C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Küklopsz:</b> A védőpajzs nem egyetlen pontban működik, hanem egy egész '
         '<b>tartományon</b>. A „hol nulla?” kérdésre egy vagy két szám a válasz — '
         'a „hol pozitív?” kérdésre viszont intervallumok. És itt jön a jó hír: '
         'ha megvan a parabola képe, az egyenlőtlenséget <b>le lehet olvasni</b>. '
         'Nem kell új módszer, csak az, amit a <a href="tananyag-masodfoku-fuggveny.html">másodfokú függvényről</a> és a <a href="tananyag-fuggvenyvizsgalat.html">vizsgálatáról</a> megtanultál.'),
 ]),

 ("Mit jelent a megoldás?", [
   'A másodfokú egyenlőtlenség — például $x^{2}-5x+6&gt;0$ — azt kérdezi: <b>mely '
   '$x$ értékekre</b> pozitív a bal oldal? Ez pontosan azt jelenti: hol van a parabola '
   'az $x$-tengely <b>fölött</b>.',
   abra(SVG_EGYENL, "Az $y=x^{2}-5x+6$ parabola zérushelyei $2$ és $3$. A két gyök "
                    "<b>között</b> a görbe a tengely alatt van (negatív), azon kívül fölötte "
                    "(pozitív)."),
   doboz("tetel", "A megoldás menete",
         '<p><b>1.</b> Rendezd az egyenlőtlenséget nullára (a jobb oldalon $0$ álljon).</p>'
         '<p><b>2.</b> Oldd meg a hozzá tartozó <b>egyenletet</b> — keresd meg a zérushelyeket (az egyenlet gyökei egyben a függvény zérushelyei).</p>'
         '<p><b>3.</b> Nézd meg az $a$ előjelét (merre nyílik a parabola), és a képről '
         '<b>olvasd le</b> a megoldást.</p>'
         '<p>Ha $a&gt;0$ és két zérushely van ($x_{1}&lt;x_{2}$):</p>'
         '<ul>'
         '<li>a kifejezés <b>negatív</b> a gyökök <b>között</b>: $x\\in(x_{1};x_{2})$;</li>'
         '<li><b>pozitív</b> a gyökökön <b>kívül</b>: '
         '$x\\in(-\\infty;x_{1})\\cup(x_{2};+\\infty)$.</li>'
         '</ul>'
         '<p>Ha $a&lt;0$, a két eset <b>felcserélődik</b>.</p>',
         hid="tetel-egyenlotlenseg-menete"),
 ]),

 ("A hiányzó két eset: $D=0$ és $D&lt;0$", [
   doboz("tetel", "Amikor nincs két gyök",
         '<p><b>$D=0$</b> (egy kettős gyök, $x_{0}$): $a&gt;0$ esetén a kifejezés '
         '<b>mindenütt nemnegatív</b>, és csak $x_{0}$-ban nulla. Tehát '
         '$ax^{2}+bx+c&gt;0$ megoldása $\\mathbb{R}\\setminus\\{x_{0}\\}$, míg '
         '$ax^{2}+bx+c&lt;0$-nak <b>nincs</b> megoldása.</p>'
         '<p><b>$D&lt;0$</b> (nincs valós gyök): a parabola <b>végig</b> a tengely egyik '
         'oldalán van. Ha $a&gt;0$, a kifejezés minden $x$-re pozitív; ha $a&lt;0$, '
         'minden $x$-re negatív.</p>',
         hid="tetel-egyenlotlenseg-D"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $x^{2}-5x+6&gt;0$; <b>b)</b> $x^{2}-5x+6\\le 0$; '
         '<b>c)</b> $x^{2}-4x+4&gt;0$; <b>d)</b> $x^{2}+x+1&gt;0$.</p>',
         hid="pelda-egyenlotlensegek",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> A zérushelyek $2$ és $3$, $a&gt;0$ → a gyökökön kívül pozitív:</p>'
                  '$$x\\in(-\\infty;2)\\cup(3;+\\infty).$$'
                  '<p><b>b)</b> Ugyanaz a parabola, most a nem pozitív rész kell — a gyökök '
                  'között, <b>zárt</b> végpontokkal (az egyenlőség is megengedett):</p>'
                  '$$x\\in[2;3].$$'
                  '<p><b>c)</b> $D=16-16=0$, a kettős gyök $x=2$. A kifejezés '
                  '$(x-2)^{2}$, ami mindenütt nemnegatív, és csak $2$-ben nulla:</p>'
                  '$$x\\in\\mathbb{R}\\setminus\\{2\\}.$$'
                  '<p><b>d)</b> $D=1-4=-3&lt;0$ és $a=1&gt;0$ → a parabola végig a tengely '
                  'fölött van, tehát az egyenlőtlenség <b>minden valós $x$-re</b> teljesül: '
                  '$x\\in\\mathbb{R}$.</p>')),
   kviz('Mi az $x^{2}-9&lt;0$ egyenlőtlenség megoldása?',
        ['$x\\in(-3;3)$', '$x\\in(-\\infty;-3)\\cup(3;+\\infty)$', '$x\\in\\mathbb{R}$'], 0,
        jo="✔ A zérushelyek −3 és 3; a>0, tehát a kifejezés a gyökök között negatív.",
        nem="✘ a > 0 esetén a parabola a két gyök KÖZÖTT van a tengely alatt: (−3; 3)."),
 ]),

 ("Negatív főegyüttható és a szigorú végpontok", [
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $-x^{2}+3x-2\\ge 0$; <b>b)</b> $2x^{2}-7x+3&lt;0$.</p>',
         hid="pelda-negativ-fo",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> Két út van. Vagy $-1$-gyel szorzunk — ilyenkor a reláció '
                  '<b>megfordul</b>: $x^{2}-3x+2\\le 0$, aminek a gyökei $1$ és $2$, tehát '
                  '$x\\in[1;2]$. Vagy meghagyjuk: $a=-1&lt;0$, a parabola lefelé nyílik, '
                  'így a gyökök <b>között</b> (és a gyökökben) van a tengely fölött vagy rajta — ugyanaz jön ki.</p>'
                  '<p><b>b)</b> $D=49-24=25$, a gyökök $\\tfrac12$ és $3$. Mivel $a=2&gt;0$ '
                  'és negatív értéket keresünk, a gyökök közötti <b>nyílt</b> intervallum '
                  'a megoldás: $x\\in\\left(\\tfrac12;3\\right)$.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Három klasszikus hiba:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>Negatív számmal szorozni a relációjel megfordítása nélkül.</b> '
         'A $-x^{2}+3x-2\\ge 0$-ból $x^{2}-3x+2\\le 0$ lesz — a <b>relációjel</b> átfordul.</li>'
         '<li><b>Zárt zárójel a végtelennél.</b> A $+\\infty$ és a $-\\infty$ nem szám, '
         'nem lehet „elérni” — mellettük <b>mindig nyitott</b> zárójel áll: '
         '$(3;+\\infty)$, sosem $(3;+\\infty]$.</li>'
         '<li><b>Az uniót metszetnek írni.</b> Ha a megoldás két különálló darabból áll, '
         'azok <b>uniója</b> ($\\cup$) a válasz, nem a metszetük — az utóbbi üres lenne.</li>'
         '</ol>'),
   kviz('Melyik a helyes megoldás: $-x^{2}+4&gt;0$?',
        ['$x\\in(-2;2)$', '$x\\in(-\\infty;-2)\\cup(2;+\\infty)$', 'Nincs megoldás.'], 0,
        jo="✔ a < 0, a parabola lefelé nyílik → a gyökök között van a tengely fölött.",
        nem="✘ Szorozz −1-gyel (a jel fordul): x² − 4 < 0, azaz x ∈ (−2; 2)."),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–5, 11"),
   brief('<b>Küklopsz:</b> Utolsó bevetés a szektorban. Eddig egyetlen görbét néztünk. '
         'Most kettőt teszünk egymásra — egy parabolát és egy egyenest —, és megkeressük, '
         '<b>hol találkoznak</b>. Ez a bemérés utolsó lépése.',
         outro=True),
 ]),
]

# ===================================================================== C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Küklopsz:</b> Két feltétel, két egyenlet. Az egyik <b>lineáris</b>, a másik '
         '<b>másodfokú</b>. Tavaly két egyenes metszéspontját kerested — most egy '
         'egyenes és egy parabola találkozási pontjait. A módszer ugyanaz, mint akkor: '
         '<b>behelyettesítés</b>. A különbség csak annyi, hogy a végén másodfokú '
         'egyenletet kapsz — és így akár <b>két</b> megoldás is lehet.'),
 ]),

 ("A behelyettesítés módszere", [
   doboz("tetel", "Az eljárás",
         '<p>Egy másodfokú és egy lineáris egyenletből álló rendszer megoldása:</p>'
         '<p><b>1.</b> A <b>lineáris</b> egyenletből fejezd ki az egyik ismeretlent '
         '(azt, amelyiket könnyebb).</p>'
         '<p><b>2.</b> Helyettesítsd be a másodfokú egyenletbe — így egyismeretlenes '
         'másodfokú egyenletet kapsz.</p>'
         '<p><b>3.</b> Oldd meg, majd <b>minden</b> gyökhöz számold ki a másik ismeretlent is.</p>'
         '<p><b>4.</b> A megoldás <b>számpárokból</b> áll — annyiból, ahány gyököt a másodfokú '
         'egyenlet adott: $(x_{1};y_{1})$, $(x_{2};y_{2})$.</p>',
         hid="tetel-rendszer-menete"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg a rendszert: $y=x^{2}-2x$ &nbsp;és&nbsp; $y=x-2$.</p>',
         hid="pelda-rendszer",
         lenyilo=("Megoldás",
                  '<p>Mindkét egyenlet $y$-ra van rendezve, ezért egyenlővé tehetjük őket:</p>'
                  '$$x^{2}-2x=x-2\\ \\Rightarrow\\ x^{2}-3x+2=0.$$'
                  '<p>Innen $D=9-8=1$, tehát $x_{1}=1$ és $x_{2}=2$.</p>'
                  '<p>Visszahelyettesítve a <b>lineáris</b> egyenletbe: '
                  '$y_{1}=1-2=-1$ és $y_{2}=2-2=0$.</p>'
                  '<p><b>Megoldás:</b> $(1;-1)$ és $(2;0)$.</p>')),
   abra(SVG_RENDSZER, "A rendszer megoldásai a két görbe <b>metszéspontjai</b>. "
                      "Az algebrai számolás és a kép ugyanazt mondja."),
 ]),

 ("Hány megoldás lehet?", [
   'A behelyettesítés után másodfokú egyenletet kapunk — és annak a diszkriminánsa '
   'dönti el a megoldások számát. Geometriailag: hányszor metszi az egyenes a parabolát?',
   doboz("tetel", "Három eset",
         '<p>(A „parabola” helyett bármilyen másodfokú görbe állhat — kör, hiperbola —, '
         'feltéve, hogy a behelyettesítés után valóban másodfokú egyenletet kapunk.)</p>'
         '<p><b>$D&gt;0$:</b> az egyenes <b>két pontban</b> metszi a görbét → '
         'két megoldáspár.</p>'
         '<p><b>$D=0$:</b> az egyenes <b>érinti</b> a parabolát → egy (kettős) megoldás.</p>'
         '<p><b>$D&lt;0$:</b> nincs közös pontjuk → a rendszernek <b>nincs valós megoldása</b>.</p>',
         hid="tetel-rendszer-esetek"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Hány közös pontja van az $y=x^{2}$ parabolának <b>a)</b> az $y=2x-1$, '
         '<b>b)</b> az $y=2x-5$ egyenessel?</p>',
         hid="pelda-metszespontok",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $x^{2}=2x-1\\Rightarrow x^{2}-2x+1=0$, $D=4-4=0$ → '
                  '<b>egy</b> közös pont ($x=1$, $y=1$): az egyenes <b>érinti</b> a parabolát.</p>'
                  '<p><b>b)</b> $x^{2}=2x-5\\Rightarrow x^{2}-2x+5=0$, $D=4-20=-16&lt;0$ → '
                  '<b>nincs</b> valós közös pont; az egyenes elhalad a parabola mellett.</p>')),
   kviz('Hány valós megoldása van az $y=x^{2}+1$, $y=x$ rendszernek?',
        ['Egy sem.', 'Egy.', 'Kettő.'], 0,
        jo="✔ x² + 1 = x → x² − x + 1 = 0, ahol D = 1 − 4 = −3 < 0.",
        nem="✘ x² − x + 1 = 0 diszkriminánsa −3 < 0, tehát nincs valós metszéspont."),
 ]),

 ("Ha összeg és szorzat van megadva", [
   'Van egy különösen elegáns eset, ahol a Viète-képletek jönnek segítségül: ha a két '
   'ismeretlen <b>összegét</b> és <b>szorzatát</b> ismerjük.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: $x+y=7$ &nbsp;és&nbsp; $x\\cdot y=12$.</p>',
         hid="pelda-osszeg-szorzat",
         lenyilo=("Megoldás",
                  '<p>Ha két szám összege $S$, szorzata $P$, akkor a két szám a '
                  '$t^{2}-St+P=0$ egyenlet gyöke — ez a Viète-képletek megfordítása. '
                  'Valós számpár csak akkor van, ha ennek a diszkriminánsa nemnegatív: '
                  '$S^{2}-4P\\ge 0$. Itt $S=7$, $P=12$, és '
                  '$49-48=1&gt;0$:</p>'
                  '$$t^{2}-7t+12=0.$$'
                  '<p>Innen $D=49-48=1$, tehát $t_{1}=4$ és $t_{2}=3$.</p>'
                  '<p><b>Megoldás:</b> $(3;4)$ és $(4;3)$ — a rendszer szimmetrikus, ezért '
                  'a két szám <b>felcserélhető</b>.</p>')),
   doboz("pelda", "Vészterem-szimuláció — amikor a másodfokú egyenletben mindkét ismeretlen szerepel",
         '<p>Oldd meg: $x-y=2$ &nbsp;és&nbsp; $x^{2}+y^{2}=10$.</p>',
         hid="pelda-vegyes-rendszer",
         lenyilo=("Megoldás",
                  '<p>A lineáris egyenletből $x=y+2$. Behelyettesítve:</p>'
                  '$$(y+2)^{2}+y^{2}=10\\ \\Rightarrow\\ 2y^{2}+4y-6=0\\ \\Rightarrow\\ '
                  'y^{2}+2y-3=0.$$'
                  '<p>Innen $y_{1}=1$ és $y_{2}=-3$, tehát $x_{1}=3$ és $x_{2}=-1$.</p>'
                  '<p><b>Megoldás:</b> $(3;1)$ és $(-1;-3)$. '
                  '<b>Ellenőrzés:</b> $(3;1)$: $3-1=2$ ✔ és $9+1=10$ ✔; $(-1;-3)$: $-1-(-3)=2$ ✔ és $1+9=10$ ✔</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A leggyakoribb hiba: <b>megállni $x$-nél</b>. A rendszer megoldása nem szám, '
         'hanem <b>számpár</b> — minden $x$-hez ki kell számolni a hozzá tartozó $y$-t. '
         'És vigyázz: a visszahelyettesítést a <b>lineáris</b> egyenletbe végezd, '
         'mert az mindig egyetlen értéket ad. Ha a másodfokúba helyettesítesz vissza — például '
         'az $x^{2}+y^{2}=10$-be —, két érték is jöhet, és közülük csak az egyik illik a párba.</p>'),
   kviz('Az $x+y=5$, $xy=6$ rendszer megoldásai:',
        ['$(2;3)$ és $(3;2)$', 'Csak $(2;3)$', '$(1;6)$ és $(6;1)$'], 0,
        jo="✔ A t² − 5t + 6 = 0 egyenlet gyökei 2 és 3; a rendszer szimmetrikus.",
        nem="✘ Írd fel a t² − 5t + 6 = 0 egyenletet: gyökei 2 és 3, tehát mindkét sorrend megoldás."),
   gyakorolj(FGY + "#alap-7", "A 7–12", FGY + "#kozep-6", "K 6–10"),
   brief('<b>Dr. Bestia:</b> Kadétok, jó munka — a Parabola-csapást elhárítottuk. De miközben '
         'ti a röppályákkal foglalkoztatok, én a laborban mértem valamit, és nem tetszik: '
         'Dr. Baljós vírusa nem másodfokon terjed többé. <b>Megduplázódik</b> minden '
         'lépésben. Az ilyen növekedést a másodfokú függvény már nem írja le — sokkal '
         'gyorsabb annál. A következő küldetés az <b>Evolúciós Ugrás</b>, és a fegyverünk '
         'az exponenciális függvény lesz.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-masodfoku-egyenlotlensegek.html",
     cim="Másodfokú egyenlőtlenségek", cim_tiszta="Másodfokú egyenlőtlenségek",
     alcim="A megoldás leolvasása a parabola képéről, a három diszkrimináns-eset, "
           "a negatív főegyüttható kezelése és az intervallumos írásmód.",
     chip="Az M-Faktor · 7/8", szakaszok=C1,
     elozo=("feladatok-masodfoku-fuggveny.html", "Feladatok — másodfokú függvény"),
     kovetkezo=("tananyag-masodfoku-linearis-rendszer.html",
                "Másodfokú és lineáris egyenletből álló rendszer")),
 lap(**T, fajl="tananyag-masodfoku-linearis-rendszer.html",
     cim="Másodfokú és lineáris egyenletből álló rendszer",
     cim_tiszta="Másodfokú és lineáris egyenletből álló rendszer",
     alcim="A behelyettesítés módszere, a metszéspontok száma a diszkrimináns alapján, "
           "valamint az összeg–szorzat típusú rendszerek Viète-képletekkel.",
     chip="Az M-Faktor · 8/8", szakaszok=C2,
     elozo=("tananyag-masodfoku-egyenlotlensegek.html", "Másodfokú egyenlőtlenségek"),
     kovetkezo=(FGY, "Feladatok — egyenlőtlenségek és rendszerek")),
]
for u in KI:
    print("✓", os.path.basename(u))
