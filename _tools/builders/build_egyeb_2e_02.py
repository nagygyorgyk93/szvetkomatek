# -*- coding: utf-8 -*-
"""2e/02 — osszefoglalo (F4), terepkuldetes (F5p), Danger Room (F6h), temakor-index (F5)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, GYOKER
from fgy_common import cards, oldal, w

T = dict(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
         temakor="Másodfokú egyenletek és függvények")

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, solve, simplify, expand, Eq, sqrt, im, re as _re, I
x, y, t, k, m, c = symbols('x y t k m c')
def S(e): return sorted(solve(e, x), key=lambda z: (im(z), _re(z)))
def csucs(a, b, cc): return (R(-b, 2*a), a*R(-b, 2*a)**2 + b*R(-b, 2*a) + cc)
E = []
def chk(n, g, w_):
    if (g != w_) if isinstance(w_, (list, tuple)) else (simplify(g - w_) != 0):
        E.append((n, g, w_))
P = [
 # terepküldetés
 ("TI1", sorted(solve(-5*t**2+30*t-40, t)), [2, 4]),
 ("TI2", sorted(solve(-5*t**2+30*t, t)), [0, 6]),
 ("TI3", sorted(solve(-5*t**2+20*t+25, t)), [-1, 5]),
 ("TI4k", solve(Eq(2*k-10, 0), k), [5]), ("TI4c", 3*5-33, -18),
 ("TI4x", S(x**2-18), [-3*sqrt(2), 3*sqrt(2)]),
 ("TII1", csucs(-5, 30, 0), (3, 45)),
 ("TII2", csucs(-2, 16, -24), (4, 8)),
 ("TII3", sorted(solve(x**2-8*x+12, x)), [2, 6]),
 ("TII4", csucs(-2, 36, 0), (9, 162)),
 ("TIII1", sorted(solve(x**2-10*x+21, x)), [3, 7]),
 ("TIII3", sorted(solve(x**2-7*x+10, x)), [2, 5]),
 ("TIII4", sorted(solve(t**2-20*t+96, t)), [8, 12]),
 ("TIII5", solve(Eq(4+4*c, 0), c), [-1]),
 # Danger Room
 ("DA1a", S(x**2-64), [-8, 8]), ("DA1b", S(x**2+9*x), [-9, 0]),
 ("DA1c", S(x**2-8*x+15), [3, 5]),
 ("DA2a", S(2*x**2-7*x+3), [R(1,2), 3]), ("DA2b", S((x-2)*(x+3)-6), [-4, 3]),
 ("DA4a", expand((x-4)*(x-5)), x**2-9*x+20), ("DA4b", expand((x+5)*(x-3)), x**2+2*x-15),
 ("DA5", 64-2*15, 34),
 ("DA6", csucs(1, -2, -8), (1, -9)), ("DA6b", S(x**2-2*x-8), [-2, 4]),
 ("DA8b", sorted(solve(x**2-7*x+10, x)), [2, 5]),
 ("DA9", S(x**2-2*x-3), [-1, 3]),
 ("DK1", S(x**4-13*x**2+36), [-3, -2, 2, 3]),
 ("DK3", S(-x**2+4*x-3), [1, 3]), ("DK3b", csucs(-1, 4, -3), (2, 1)),
 ("DK4", R(5, 4), R(5,4)),
 ("DK5", sorted(solve(x**2-6*x+8, x)), [2, 4]),
 ("DK6", sorted(solve(t**2-9*t+20, t)), [4, 5]),
 ("DN1", csucs(-2, 30, 0), (R(15,2), R(225,2))),
 ("DN2", solve(Eq(9-3*(m+1)+m, 0), m), [3]),
 ("DN3", S(x**4+5*x**2-36), [-3*I, -2, 2, 3*I]),
]
for n, g, w_ in P:
    chk(n, g, w_)
assert not E, E[:4]
print("sympy önteszt: OK")

# ==================================================================== F4

OSSZ = [
 ("A másodfokú egyenlet", [
  '<p><b>Alak:</b> $ax^{2}+bx+c=0$, ahol $a\\neq 0$ '
  '(<a href="tananyag-masodfoku-egyenlet.html#def-masodfoku-egyenlet">→ tananyag</a>).</p>',
  '<p><b>Hiányos esetek</b> — ne használj megoldóképletet! '
  '$ax^{2}+bx=0\\Rightarrow x(ax+b)=0$ (<b>kiemelés</b>) · '
  '$ax^{2}+c=0\\Rightarrow x^{2}=-\\frac{c}{a}$ (<b>gyökvonás</b>, $\\pm$ jellel!) '
  '(<a href="tananyag-masodfoku-egyenlet.html#tetel-hianyos">→</a>).</p>',
  '<p><b>Megoldóképlet:</b> $x_{1,2}=\\dfrac{-b\\pm\\sqrt{b^{2}-4ac}}{2a}$ '
  '(<a href="tananyag-masodfoku-egyenlet.html#tetel-megoldokeplet">→</a>). '
  'Nem rendezett egyenletnél <b>előbb bonts és rendezz nullára</b> — a „szorzat = 0” '
  'szabály csak nulla jobb oldal mellett működik.</p>',
 ]),
 ("A diszkrimináns", [
  '<p>$D=b^{2}-4ac$ '
  '(<a href="tananyag-diszkriminans.html#def-diszkriminans">→</a>). '
  '<b>$D&gt;0$:</b> két különböző valós gyök · <b>$D=0$:</b> egy kettős gyök, '
  '$x=-\\frac{b}{2a}$ · <b>$D&lt;0$:</b> két <b>konjugált komplex</b> gyök '
  '(<a href="tananyag-diszkriminans.html#tetel-megoldasok-termeszete">→</a>).</p>',
  '<p><b>Paraméteres feladat receptje:</b> írd fel $D$-t a paraméterrel, majd oldd meg a '
  '$D&gt;0$, $D=0$, $D&lt;0$ egyenlőtlenségeket. ⚠️ Ha a paraméter a <b>főegyütthatóban</b> '
  'áll, külön vizsgáld az „ekkor nem másodfokú” esetet '
  '(<a href="tananyag-diszkriminans.html#pelda-parameteres">→</a>).</p>',
 ]),
 ("Viète-képletek és szorzattá alakítás", [
  '<p>$x_{1}+x_{2}=-\\dfrac{b}{a}$ &nbsp;és&nbsp; $x_{1}x_{2}=\\dfrac{c}{a}$ '
  '(<a href="tananyag-viete-es-szorzatta-alakitas.html#tetel-viete">→</a>). '
  'A képletek a <b>komplex</b> gyökökre is érvényesek.</p>',
  '<p><b>Szimmetrikus kifejezések</b> gyökök nélkül: '
  '$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}=\\dfrac{x_{1}+x_{2}}{x_{1}x_{2}}$ · '
  '$x_{1}^{2}+x_{2}^{2}=\\left(x_{1}+x_{2}\\right)^{2}-2x_{1}x_{2}$ · '
  '$\\left(x_{1}-x_{2}\\right)^{2}=\\left(x_{1}+x_{2}\\right)^{2}-4x_{1}x_{2}$ '
  '(<a href="tananyag-viete-es-szorzatta-alakitas.html#tetel-szimmetrikus">→</a>).</p>',
  '<p><b>Egyenlet a gyökeiből:</b> $x^{2}-\\left(x_{1}+x_{2}\\right)x+x_{1}x_{2}=0$. '
  '<b>Szorzattá alakítás:</b> $ax^{2}+bx+c=a\\left(x-x_{1}\\right)\\left(x-x_{2}\\right)$ — '
  '⚠️ az $a$-t <b>ne hagyd le</b>! '
  '(<a href="tananyag-viete-es-szorzatta-alakitas.html#tetel-szorzatta-alakitas">→</a>)</p>',
 ]),
 ("Bikvadratikus egyenletek", [
  '<p>$ax^{4}+bx^{2}+c=0$ → a $t=x^{2}$ helyettesítéssel másodfokú lesz '
  '(<a href="tananyag-bikvadratikus.html#tetel-bikvadratikus">→</a>). '
  '⚠️ <b>Vissza kell helyettesíteni</b>: minden $t$-hez $x=\\pm\\sqrt{t}$ tartozik. '
  'Negatív $t$ esetén a gyökök <b>komplexek</b>; a valós számok halmazán ezeket elvetjük.</p>',
 ]),
 ("A másodfokú függvény", [
  '<p><b>Nyílásirány:</b> $a&gt;0$ → felfelé (konvex, <b>minimum</b>); $a&lt;0$ → lefelé '
  '(konkáv, <b>maximum</b>). Nagyobb $\\lvert a\\rvert$ → karcsúbb parabola '
  '(<a href="tananyag-masodfoku-fuggveny.html#tetel-foegyutthato">→</a>).</p>',
  '<p><b>Csúcspont:</b> $C(u;v)$, ahol $u=-\\dfrac{b}{2a}$ és $v=f(u)=-\\dfrac{D}{4a}$; '
  'kanonikus alak $f(x)=a\\left(x-u\\right)^{2}+v$ '
  '(<a href="tananyag-masodfoku-fuggveny.html#tetel-kanonikus">→</a>).</p>',
  '<p><b>Vizsgálati protokoll:</b> nyílásirány → zérushelyek → $y$-tengelymetszet '
  '($f(0)=c$) → csúcspont → szélsőérték → értékkészlet '
  '($a&gt;0$: $[v;+\\infty)$, $a&lt;0$: $(-\\infty;v]$) '
  '(<a href="tananyag-fuggvenyvizsgalat.html#def-vizsgalat-protokoll">→</a>).</p>',
  '<p><b>A hat eset:</b> a $D$ előjele adja meg, hányszor metszi a parabola az '
  '$x$-tengelyt (2 · 1 · 0), az $a$ előjele pedig, hogy melyik oldalon van a csúcs '
  '(<a href="tananyag-masodfoku-fuggveny.html#tetel-hat-eset">→</a>).</p>',
  '<p><b>Szélsőérték-feladat:</b> írd fel a keresett mennyiséget egyetlen változó '
  'másodfokú függvényeként, majd számold ki a csúcspontot '
  '(<a href="tananyag-fuggvenyvizsgalat.html#pelda-szelsoertek">→</a>).</p>',
 ]),
 ("Egyenlőtlenségek és rendszerek", [
  '<p><b>Egyenlőtlenség:</b> rendezz nullára → oldd meg az <b>egyenletet</b> → '
  'olvasd le a parabola képéről. $a&gt;0$ és két gyök esetén: a kifejezés a gyökök '
  '<b>között negatív</b>, azokon <b>kívül pozitív</b>; $a&lt;0$-nál fordítva '
  '(<a href="tananyag-masodfoku-egyenlotlensegek.html#tetel-egyenlotlenseg-menete">→</a>).</p>',
  '<p><b>$D=0$:</b> $a&gt;0$ mellett a kifejezés mindenütt nemnegatív → a szigorú '
  'egyenlőtlenség megoldása $\\mathbb{R}\\setminus\\{x_{0}\\}$. <b>$D&lt;0$:</b> a parabola '
  'végig a tengely egyik oldalán van → vagy <b>minden</b> valós szám megoldás, vagy '
  '<b>egy sem</b> (<a href="tananyag-masodfoku-egyenlotlensegek.html#tetel-egyenlotlenseg-D">→</a>).</p>',
  '<p><b>Rendszer:</b> a <b>lineáris</b> egyenletből fejezd ki az egyik ismeretlent, '
  'helyettesítsd be, oldd meg a keletkező másodfokú egyenletet, majd <b>minden</b> gyökhöz '
  'számold ki a másik ismeretlent. A megoldás <b>számpár</b> '
  '(<a href="tananyag-masodfoku-linearis-rendszer.html#tetel-rendszer-menete">→</a>).</p>',
  '<p><b>Metszéspontok száma:</b> $D&gt;0$ két pont · $D=0$ <b>érintés</b> · $D&lt;0$ '
  'nincs közös pont. <b>Összeg–szorzat rendszer:</b> ha $x+y=s$ és $xy=p$, akkor $x$ és $y$ '
  'a $t^{2}-st+p=0$ egyenlet gyökei '
  '(<a href="tananyag-masodfoku-linearis-rendszer.html#pelda-osszeg-szorzat">→</a>).</p>',
  doboz("csapda", "Amire a dolgozaton a legtöbben ráfutnak",
        '<p>1) $x^{2}=5x$-ből <b>ne ossz</b> $x$-szel — elveszik az $x=0$. &nbsp; '
        '2) A szorzattá bontásból <b>ne hagyd le</b> a főegyütthatót. &nbsp; '
        '3) $u=-\\frac{b}{2a}$ — ha $b$ negatív, $-b$ <b>pozitív</b>. &nbsp; '
        '4) A bikvadratikusnál <b>helyettesíts vissza</b>, és ne feledd a $\\pm$-t. &nbsp; '
        '5) Negatív számmal szorozva az egyenlőtlenség <b>iránya megfordul</b>. &nbsp; '
        '6) A végtelen mellett <b>mindig nyitott</b> zárójel áll.</p>'),
  '<div class="gyakorolj"><span class="ikon">🎯</span><p>Élesben: a '
  '<a href="feladatok-masodfoku-fuggveny.html#gyak-dolgozat">gyakorló dolgozattal</a> mérd fel '
  'magad, majd indulj <a href="terepkuldetes.html">A Parabola-csapás terepküldetésre</a>!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Taktikai memóriakártya",
    cim_tiszta="Taktikai memóriakártya", itt="Taktikai memóriakártya",
    alcim="Az X-Faktor minden képlete, protokollja és tipikus csapdája egy helyen — "
          "ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip="Az X-Faktor · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-egyenlotlensegek-es-rendszerek.html", "Feladatok — egyenlőtlenségek és rendszerek"),
    kovetkezo=("terepkuldetes.html", "A Parabola-csapás terepküldetés"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Cyclops:</b> Kadét, éles helyzet. Sinister a Genosha fölötti pályáról '
         '<b>ballisztikus</b> töltetekkel lő — a röppálya parabola, és ha ki tudod számolni, '
         'meg tudod előzni. Három feladatod van: bemérni a röppályát, megtalálni a '
         'legmagasabb pontot, és megállapítani, meddig ér a pajzsunk. Wolverine már a '
         'terepen van; a te dolgod a <b>matematika</b>.'),
   '<p class="lead">Ez a küldetés a teljes témakört használja: másodfokú egyenletet, '
   'diszkriminánst, Viète-képleteket, függvényvizsgálatot, egyenlőtlenséget és rendszert. '
   'Dolgozz füzetben, és a végén add le a jelentést. <b>A megoldások nincsenek fent</b> — '
   'ezt a bevetést a tanárod értékeli.</p>',
 ]),
 ("Fázis I — A röppálya bemérése", [
   doboz("pelda", "I. fázis: ballisztika",
         '<p>Sinister lövedékének magassága $t$ másodperc múlva '
         '$h(t)=-5t^{2}+30t$ méter.</p>'
         '<ol class="reszfeladatok">'
         '<li>Mikor van a lövedék <b>$40$ méter</b> magasan? (Két időpont is van!)</li>'
         '<li>Mikor ér földet?</li>'
         '<li>A védőágyúnk lövedéke egy $25$ méteres toronyból indul: '
         '$g(t)=-5t^{2}+20t+25$. Mikor ér földet? (Az egyik gyök nem lehet megoldás — '
         'indokold meg, miért!)</li>'
         '<li>Az elfogórakéta vezérlőkódja az $x^{2}-\\left(2k-10\\right)x+3k-33=0$ '
         'egyenlet, ahol $k$ valós paraméter. A rendszer akkor stabil, ha a két gyök '
         '<b>ellentett</b> szám. Mennyi $k$, és mik a gyökök?</li>'
         '</ol>'),
 ]),
 ("Fázis II — A csúcspont", [
   doboz("pelda", "II. fázis: a legmagasabb pont",
         '<ol class="reszfeladatok">'
         '<li>Milyen magasan és mikor jár Sinister lövedéke a pálya <b>legmagasabb</b> '
         'pontján? ($h(t)=-5t^{2}+30t$)</li>'
         '<li>Az energiapajzs teljesítménye $P(x)=-2x^{2}+16x-24$ (egység), ahol $x$ a '
         'betáplált energia. Mekkora a <b>maximális</b> teljesítmény, és milyen $x$ mellett?</li>'
         '<li>Milyen $x$ értékekre <b>pozitív</b> a pajzs teljesítménye? '
         '(Írd fel intervallummal!)</li>'
         '<li>A bázis fala mellé téglalap alakú védőzónát kerítenek. A fal felőli oldalra '
         'nem kell kerítés, a másik háromra összesen $36$ méter áll rendelkezésre. '
         'Mekkora a <b>legnagyobb</b> bekeríthető terület?</li>'
         '</ol>'),
 ]),
 ("Fázis III — A pajzs hatósugara", [
   doboz("pelda", "III. fázis: a védelmi zóna",
         '<ol class="reszfeladatok">'
         '<li>A pajzs ott véd, ahol $x^{2}-10x+21\\le 0$. Add meg a védett zónát '
         'intervallummal!</li>'
         '<li>Hol <b>nem</b> véd a pajzs? (Ugyanaz a kifejezés, fordított relációval.)</li>'
         '<li>A becsapódás helyét a röppálya és a terepszint metszéspontja adja: '
         '$y=x^{2}-6x+8$ és $y=x-2$. Hol csapódik be a lövedék?</li>'
         '<li>Két energiacella össztöltése $20$ egység, a szorzatuk $96$. '
         'Mennyi külön-külön? (Viète!)</li>'
         '<li>A lézerkerítés az $y=2x+c$ egyenes. Milyen $c$ esetén <b>érinti</b> — '
         'tehát pontosan egy pontban éri — az $y=x^{2}$ pályát?</li>'
         '</ol>'),
   doboz("erdekesseg", "Jelentés a Főhadiszállásnak",
         '<p>Zárásként foglald össze <b>egyetlen táblázatban</b>: a becsapódás időpontját, '
         'a röppálya legmagasabb pontját, a pajzs maximális teljesítményét és a védett zóna '
         'határait. Írj mellé <b>2–3 mondatot</b> arról, hol használtad a diszkriminánst és '
         'hol a Viète-képleteket — Cyclops a gondolatmenetre is kíváncsi.</p>'),
   brief('<b>Beast:</b> Kiváló munka, kadét. A ballisztikát megoldottuk — de miközben ti '
         'a röppályákat számoltátok, a laborban valami sokkal rosszabbat mértem. '
         'Sinister vírusa <b>megduplázódik</b> minden ciklusban. Az ilyen növekedést '
         'a parabola meg sem közelíti. A következő küldetés az <b>Evolúciós Ugrás</b>.',
         outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="A Parabola-csapás terepküldetés",
    cim_tiszta="A Parabola-csapás terepküldetés", itt="A Parabola-csapás terepküldetés",
    alcim="Háromfázisú ballisztikai bevetés: röppálya-bemérés, csúcspont és szélsőérték, "
          "valamint a védelmi zóna határai.",
    chip="Az X-Faktor · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Taktikai memóriakártya"),
    kovetkezo=("index.html", "Vissza a témakörhöz"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h

DR_A = [
 ("Oldd meg a másodfokú egyenletet!",
  ["$x^{2}-64=0$", "$x^{2}+9x=0$", "$x^{2}-8x+15=0$"],
  ["$x_{1,2}=\\pm 8$", "$x_{1}=0$, $x_{2}=-9$", "$3$ és $5$"], True),
 ("Oldd meg!",
  ["$2x^{2}-7x+3=0$", "$(x-2)(x+3)=6$"],
  ["$3$ és $\\dfrac{1}{2}$", "$3$ és $-4$"], True),
 ("Számítsd ki a diszkriminánst, és mondd meg, hány valós megoldás van!",
  ["$x^{2}-2x-3=0$", "$x^{2}+4x+4=0$", "$x^{2}+x+2=0$"],
  ["$D=16$ → két valós.", "$D=0$ → egy kettős.", "$D=-7$ → egy sem (két komplex)."], True),
 ("Bontsd tényezőkre!",
  ["$x^{2}-9x+20$", "$x^{2}+2x-15$"], ["$(x-4)(x-5)$", "$(x+5)(x-3)$"], True),
 ("Az $x^{2}-8x+15=0$ egyenlet megoldása nélkül számítsd ki!",
  ["$x_{1}+x_{2}$", "$x_{1}\\cdot x_{2}$", "$x_{1}^{2}+x_{2}^{2}$"],
  ["$8$", "$15$", "$34$"], True),
 ("Add meg az $y=x^{2}-2x-8$ függvény csúcspontját és zérushelyeit!", None,
  "$C(1;-9)$; zérushelyek $4$ és $-2$."),
 ("Add meg az értékkészletet!",
  ["$y=x^{2}+3$", "$y=-x^{2}+5$"], ["$[3;+\\infty)$", "$(-\\infty;5]$"], True),
 ("Oldd meg az egyenlőtlenséget!",
  ["$x^{2}-25&lt;0$", "$x^{2}-7x+10&gt;0$"],
  ["$x\\in(-5;5)$", "$x\\in(-\\infty;2)\\cup(5;+\\infty)$"], False),
 ("Oldd meg a rendszert! $y=x^{2}$ és $y=2x+3$", None, "$(3;9)$ és $(-1;1)$"),
]

DR_K = [
 ("Oldd meg a bikvadratikus egyenletet! $x^{4}-13x^{2}+36=0$", None, "$\\pm 2$ és $\\pm 3$"),
 ("Milyen $m$ esetén van az $x^{2}-6x+m=0$ egyenletnek két különböző valós megoldása?",
  None, "$m&lt;9$"),
 ("Végezd el a teljes vizsgálatot! $y=-x^{2}+4x-3$", None,
  "Zérushelyek $1$ és $3$; $C(2;1)$; maximum $1$; értékkészlet $(-\\infty;1]$; konkáv."),
 ("A $2x^{2}-10x+8=0$ egyenletre — megoldás nélkül: "
  "$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$", None, "$\\dfrac{5}{4}$"),
 ("Oldd meg! $-x^{2}+6x-8\\ge 0$", None, "$x\\in[2;4]$"),
 ("Oldd meg a rendszert! $x+y=9$ és $x\\cdot y=20$", None, "$(4;5)$ és $(5;4)$"),
]

DR_N = [
 ("A bázis fala mellé téglalap alakú területet kerítenek $30$ méter kerítéssel "
  "(a fal felőli oldalra nem kell kerítés). Mekkora a legnagyobb bekeríthető terület?",
  None, "$112{,}5\\ \\text{m}^{2}$ (a merőleges oldalak $7{,}5$ m-esek)."),
 ("Az $x^{2}-(m+1)x+m=0$ egyenlet egyik gyöke $3$. Mennyi $m$, és mi a másik gyök?",
  None, "$m=3$; a másik gyök $1$."),
 ("Oldd meg a komplex számok halmazán! $x^{4}+5x^{2}-36=0$", None, "$\\pm 2$ és $\\pm 3i$"),
]

dr_brief = ('<div class="brief"><p>🕹️ <b>SZVETI:</b> <b>Veszélyterem</b> — Az X-Faktor modul. '
            'A szimuláció a <b>teljes témakört</b> lefedi: másodfokú egyenletek, diszkrimináns, '
            'Viète, szorzattá alakítás, bikvadratikus, függvényvizsgálat, egyenlőtlenségek és '
            'rendszerek. Haladj a fokozatokon: zöld → sárga → piros. A végeredményt lenyithatod, '
            'de előbb küzdd le magad!</p></div>')

dr_body = ('    ' + dr_brief + '\n'
           '    <h2 id="alap">🟢 Alapfokozat</h2>\n' + cards(DR_A, "alap", "alap") +
           '\n    <h2 id="kozep">🟡 Középfokozat</h2>\n' + cards(DR_K, "kozep", "kozep") +
           '\n    <h2 id="nehez">🔴 Nehéz fokozat</h2>\n' + cards(DR_N, "nehez", "nehez"))

oldal(**T, fajl="feladatok-hazi.html", cim="Danger Room",
      h1="🕹️ Danger Room — házi feladatgyűjtemény", itt="Danger Room — házi",
      alcim="Egyetlen, a teljes témakört lefedő házi feladatsor, óraszám-arányosan. "
            "Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      sections_html=dr_body,
      prev="index.html", prevc="Témakör Főhadiszállása",
      nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5 index

def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + cim + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')

K = [
 kartya("tananyag-masodfoku-egyenlet.html", "A másodfokú egyenlet",
        "Az egyenlet alakja, a három hiányos eset, a megoldóképlet és levezetése, rendezés"),
 kartya("tananyag-diszkriminans.html", "A diszkrimináns",
        "A $D=b^{2}-4ac$ és a megoldások természete, paraméteres feladatok, komplex gyökpárok"),
 kartya("tananyag-viete-es-szorzatta-alakitas.html", "Viète-képletek és szorzattá alakítás",
        "A gyökök összege és szorzata, szimmetrikus kifejezések, a trinom tényezőkre bontása"),
 kartya("tananyag-bikvadratikus.html", "Másodfokúra visszavezethető egyenletek",
        "A $t=x^{2}$ helyettesítés, a visszahelyettesítés buktatói, valós és komplex gyökök"),
 kartya("tananyag-masodfoku-fuggveny.html", "A másodfokú függvény és grafikonja",
        "A főegyüttható szerepe, kanonikus alak és csúcspont, a parabola hat esete"),
 kartya("tananyag-fuggvenyvizsgalat.html", "A másodfokú függvény vizsgálata",
        "A vizsgálat protokollja, teljes kidolgozott példák és szélsőérték-feladatok"),
 kartya("tananyag-masodfoku-egyenlotlensegek.html", "Másodfokú egyenlőtlenségek",
        "Leolvasás a parabola képéről, a három diszkrimináns-eset, intervallumos írásmód"),
 kartya("tananyag-masodfoku-linearis-rendszer.html", "Másodfokú és lineáris rendszer",
        "Behelyettesítés, a metszéspontok száma, összeg–szorzat típusú rendszerek"),
 kartya("feladatok-masodfoku-egyenletek.html", "🏋️ A másodfokú egyenlet — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker, a végén <b>gyakorló ellenőrzővel</b>"),
 kartya("feladatok-masodfoku-fuggveny.html", "🏋️ A másodfokú függvény — feladatok",
        "Alap · Közép · Nehéz + Joker, a végén <b>gyakorló dolgozattal</b>"),
 kartya("feladatok-egyenlotlensegek-es-rendszerek.html", "🏋️ Egyenlőtlenségek és rendszerek",
        "Alap · Közép · Nehéz + Joker — mind a három diszkrimináns-esetre"),
 kartya("feladatok-hazi.html", "🕹️ Danger Room — házi feladatok",
        "A teljes témakört lefedő házi feladatsor, óraszám-arányosan"),
 kartya("terepkuldetes.html", "🎯 A Parabola-csapás terepküldetés",
        "Háromfázisú ballisztikai bevetés — a teljes témakör egyben"),
 kartya("osszefoglalo.html", "📇 Taktikai memóriakártya",
        "Minden képlet, protokoll és tipikus csapda egy helyen — dolgozat előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Másodfokú egyenletek és függvények | 2e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="2e">
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
  <a href="../index.html"><span class="tagozat-jel">2e</span></a> ›
  <span class="itt">Másodfokú egyenletek és függvények</span>
</nav>
<div class="hero">
  <h1>Másodfokú egyenletek és függvények</h1>
  <p class="alcim">A megoldóképlettől a diszkriminánson és a Viète-képleteken át a parabola
  teljes vizsgálatáig — majd az egyenlőtlenségekig és a rendszerekig.</p>
  <div class="meta-sor"><span class="chip ora">22 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧬 <b>Szektor 02 — Az X-Faktor (A Parabola-csapás).</b> Kiképzők:
  <b>Wolverine</b> (egyenletek) és <b>Cyclops</b> (függvények). A fenyegetés többé nem
  lineárisan nő: Sinister <b>másodfokon</b> támad, és a lövedékei parabola mentén repülnek.
  Wolverine szétvágja a problémát — tényezőkre bontja, ami darabolható; Cyclops pedig az
  optikai sugarak röppályáján tanítja meg, hol a csúcspont, meddig ér a pajzs, és hol
  csapódik be a töltet.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>⚔️ A másodfokú egyenlet — Wolverine</h3>
    <div class="racs">
''' + "\n".join(K[0:4]) + '''
    </div>

    <h3>🎯 A másodfokú függvény — Cyclops</h3>
    <div class="racs">
''' + "\n".join(K[4:6]) + '''
    </div>

    <h3>🛡️ Egyenlőtlenségek és rendszerek — Cyclops</h3>
    <div class="racs">
''' + "\n".join(K[6:8]) + '''
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
''' + "\n".join(K[8:12]) + '''
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
''' + K[12] + '''
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
''' + K[13] + '''
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> altémánként előbb a tananyag-egységek sorban,
    utána a hozzá tartozó feladatgyűjtemény; a témakör végén a Taktikai memóriakártya, majd
    A Parabola-csapás terepküldetés. A Danger Room házi bármikor jöhet.</p>
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
