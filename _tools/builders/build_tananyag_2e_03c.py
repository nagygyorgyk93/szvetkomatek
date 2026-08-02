# -*- coding: utf-8 -*-
"""2e/03 — C altema: az inverz fuggveny es a logaritmusfuggveny (C1), logaritmusos
egyenletek es egyenlotlensegek (C2). Mentor: Beast."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
         temakor="Exponenciális és logaritmusfüggvény")
FGY = "feladatok-logaritmusfuggveny.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, log, solve, simplify, Interval, oo
x = symbols('x', real=True)
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
chk("C1-1", log(1, 2), 0);              chk("C1-2", log(2, 2), 1)
chk("C1-3", log(4, 2), 2);              chk("C1-4", log(R(1, 2), 2), -1)
chk("C2-1", solve(x - 3 - 8, x), [11])          # log2(x-3)=3
chk("C2-2", solve(2*x + 1 - 25, x), [12])       # log5(2x+1)=2
chk("C2-3", solve(x**2 - 4*x - 5, x), [-1, 5])  # log(x^2-4x)=log5 -> x^2-4x-5=0
chk("C2-3et", (-1)**2 - 4*(-1), 5)              # az x=-1 az ÉT-be BELEFÉR
chk("C2-4", solve(3*x - 2 - (x + 6), x), [4])   # log(3x-2)=log(x+6)
chk("C2-5", solve(x - 1 - 16, x), [17])         # log2(x-1)<4 -> x-1<16
chk("C2-6", solve(2*x - 6 - 9, x), [R(15, 2)])  # log3(2x-6)>2 -> 2x-6>9
chk("C2-7", solve(x**2 - 3*x - 4, x), [-1, 4])
chk("C2-8", solve(4*x + 1 - (x + 7), x), [2])   # log_{0,5}(4x+1) >= log_{0,5}(x+7)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_INV = svg_fuggvenyek(
    [(lambda u: 2**u, "#047857", "y = 2ˣ", [(-3.6, 2.3)]),
     (lambda u: math.log(u, 2) if u > 0 else None, "#3b82f6", "y = log₂x", [(0.04, 5.2)]),
     (lambda u: u, "#94a3b8", "y = x", [(-3.6, 5.2)])],
    xr=(-3.6, 5.2), yr=(-3.6, 5.2), w=390, h=330,
    leiras="Az exponenciális és a logaritmusfüggvény grafikonja egymás tükörképe "
           "az y egyenlő x egyenesre",
    pontok=[(0, 1, "(0; 1)", "#047857", 8, -6), (1, 0, "(1; 0)", "#3b82f6", 8, 16)])

SVG_LOG = svg_fuggvenyek(
    [(lambda u: math.log(u, 2) if u > 0 else None, "#047857", "y = log₂x", [(0.04, 5.4)]),
     (lambda u: math.log(u, 0.5) if u > 0 else None, "#ef4444", "y = log₀,₅x", [(0.04, 5.4)])],
    xr=(-0.8, 5.4), yr=(-3.4, 3.4), w=380, h=250,
    leiras="A logaritmusfüggvény növekvő és csökkenő esete",
    pontok=[(1, 0, "(1; 0)", "#8b5cf6", 6, 16)])

# ===================================================================== C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Beast:</b> Két függvényünk van, amelyek ugyanarról a jelenségről beszélnek, '
         'csak ellenkező irányból. Az egyik azt mondja meg, <i>mennyi lesz $x$ óra múlva</i>, '
         'a másik azt, <i>hány óra kell hozzá</i>. Az ilyen párokat a matematika '
         '<b>inverz</b> függvényeknek nevezi — és a grafikonjuk mindig ugyanabban '
         'a tükörben néz egymásra.'),
 ]),

 ("Az inverz függvény", [
   doboz("definicio", "Inverz függvény",
         '<p>Ha az $f$ függvény <b>kölcsönösen egyértelmű</b> (azaz különböző '
         '$x$-ekhez különböző értékeket rendel), akkor létezik az <b>inverze</b>, '
         'jelben $f^{-1}$, amely minden függvényértékhez visszaadja az eredeti '
         '$x$-et:</p>'
         '$$f(x)=y\\iff f^{-1}(y)=x.$$'
         '<p>Az inverz <b>értelmezési tartománya</b> az eredeti függvény '
         '<b>értékkészlete</b>, és fordítva.</p>',
         hid="def-inverz"),
   doboz("tetel", "A grafikonok kapcsolata",
         '<p>Az $f$ és az $f^{-1}$ grafikonja <b>egymás tükörképe az $y=x$ egyenesre</b>.</p>'
         '<p>Miért? Mert ha az $f$ grafikonján rajta van a $(p;q)$ pont, akkor az '
         'inverzén a $(q;p)$ pont van rajta — a két koordináta cserél helyet. '
         'Az $y=x$ egyenesre való tükrözés pedig épp ezt csinálja.</p>',
         hid="tetel-inverz-grafikon"),
   doboz("csapda", "Sinister vírus-kódja",
         '<p>Az $f^{-1}$ jelölés <b>nem</b> reciprokot jelent!</p>'
         '<p>✘ $f^{-1}(x)=\\dfrac{1}{f(x)}$ &nbsp;&nbsp;&nbsp; '
         '✔ $f^{-1}$ = az a függvény, amely „visszacsinálja” az $f$-et</p>'
         '<p>Nem minden függvénynek van inverze: az $y=x^{2}$ például a $2$-höz és '
         'a $-2$-höz is $4$-et rendel, tehát a $4$-ből nem lehet egyértelműen '
         'visszatalálni. Ezért kell a kölcsönös egyértelműség.</p>'),
 ]),

 ("A logaritmusfüggvény", [
   'Az exponenciális függvény szigorúan monoton, tehát <b>kölcsönösen egyértelmű</b> — '
   'így van inverze. Ez az inverz a <b>logaritmusfüggvény</b>.',
   doboz("definicio", "Logaritmusfüggvény",
         '<p>Legyen $a&gt;0$ és $a\\neq 1$. A</p>'
         '$$f:(0;+\\infty)\\to\\mathbb{R},\\qquad f(x)=\\log_{a}x$$'
         '<p>függvényt <b>logaritmusfüggvénynek</b> nevezzük. Ez az $y=a^{x}$ '
         'exponenciális függvény <b>inverze</b>.</p>',
         hid="def-logaritmusfuggveny"),
   abra(SVG_INV, "Az $y=2^{x}$ és az $y=\\log_{2}x$ grafikonja tükörképe egymásnak "
                 "az $y=x$ egyenesre. Az egyik a $(0;1)$, a másik az $(1;0)$ ponton "
                 "halad át — a koordináták cserélnek helyet."),
   abra(SVG_LOG, "Ha $a&gt;1$, a logaritmusfüggvény <b>növekvő</b>; ha $0&lt;a&lt;1$, "
                 "<b>csökkenő</b>. Mindkettő átmegy az $(1;0)$ ponton, mert "
                 "$\\log_{a}1=0$ minden alapra."),
   doboz("tetel", "A logaritmusfüggvény tulajdonságai",
         '<div class="tblwrap"><table>'
         '<tr><th>Tulajdonság</th><th>$a&gt;1$</th><th>$0&lt;a&lt;1$</th></tr>'
         '<tr><td>Értelmezési tartomány</td><td colspan="2">$(0;+\\infty)$ — '
         '<b>csak pozitív számokra</b></td></tr>'
         '<tr><td>Értékkészlet</td><td colspan="2">$\\mathbb{R}$ — minden valós értéket felvesz</td></tr>'
         '<tr><td>Nullahely</td><td colspan="2">$x=1$, mert $\\log_{a}1=0$</td></tr>'
         '<tr><td>Monotonitás</td><td>szigorúan növekvő</td><td>szigorúan csökkenő</td></tr>'
         '<tr><td>Aszimptota</td><td colspan="2">az $y$-tengely ($x=0$)</td></tr>'
         '<tr><td>Metszés az $y$-tengellyel</td><td colspan="2">nincs (a $0$ nincs az ÉT-ben)</td></tr>'
         '</table></div>'
         '<p>Vedd észre: minden sor az exponenciális függvény megfelelő sorának a '
         '<b>tükörképe</b> — az ÉT és az ÉK helyet cserélt, a vízszintes aszimptotából '
         'függőleges lett.</p>',
         hid="tetel-logf-tulajdonsagok"),
   kviz('Mi az $f(x)=\\log_{3}x$ függvény értelmezési tartománya?',
        ['$(0;+\\infty)$', '$\\mathbb{R}$', '$[0;+\\infty)$'], 0,
        jo="✔ Csak pozitív szám logaritmusa létezik — a 0 sem tartozik bele.",
        nem="✘ Logaritmusa csak POZITÍV számnak van, tehát x > 0."),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Add meg az értelmezési tartományt, és ábrázold: '
         '<b>a)</b> $y=\\log_{2}(x-3)$; <b>b)</b> $y=\\log_{2}x+1$.</p>',
         hid="pelda-logf-eltolas",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> A logaritmus argumentuma pozitív kell legyen: $x-3&gt;0$, '
                  'tehát az ÉT: $x&gt;3$, azaz $(3;+\\infty)$. A grafikon az '
                  '$y=\\log_{2}x$ görbe <b>3 egységgel jobbra</b> tolva; az aszimptota '
                  'is átvándorol az $x=3$ egyenesre. Nullahely: $x-3=1$, azaz $x=4$.</p>'
                  '<p><b>b)</b> Itt az argumentum maga az $x$, tehát az ÉT változatlanul '
                  '$x&gt;0$. A grafikon <b>1 egységgel feljebb</b> tolva; az aszimptota '
                  'marad az $y$-tengely. Nullahely: $\\log_{2}x=-1$, azaz $x=\\tfrac12$.</p>')),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
 ]),
]

# ===================================================================== C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Beast:</b> Utolsó szakasz. A logaritmusos egyenletnél van egy lépés, amit '
         '<b>soha nem hagyhatsz ki</b>: az <b>értelmezési tartomány</b>. Nem azért, mert '
         'a tanár kéri — hanem mert a megoldás közben olyan gyök is előbukkanhat, amelyre '
         'az eredeti egyenletnek semmi értelme. Az ÉT a szűrő, ami ezeket kifogja. '
         'Kezdd vele, ne a végén told hozzá.'),
 ]),

 ("Az értelmezési tartomány — az első lépés", [
   doboz("tetel", "A munkamenet",
         '<p><b>1.</b> Írd fel az <b>értelmezési tartományt</b>: minden logaritmus '
         'argumentuma legyen pozitív. Több logaritmus esetén a feltételek '
         '<b>metszete</b> az ÉT.</p>'
         '<p><b>2.</b> Az azonosságokkal <b>vond össze</b> a logaritmusokat, hogy mindkét '
         'oldalon egyetlen logaritmus (vagy egy szám) maradjon.</p>'
         '<p><b>3.</b> Hagyd el a logaritmust — a függvény kölcsönösen egyértelmű:</p>'
         '$$\\log_{a}u=\\log_{a}v\\iff u=v,\\qquad \\log_{a}u=c\\iff u=a^{c}.$$'
         '<p><b>4.</b> Oldd meg a kapott egyenletet, és <b>vesd össze az ÉT-vel</b>: '
         'ami kilóg belőle, azt eldobod.</p>',
         hid="tetel-log-egyenlet-menete"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $\\log_{2}(x-3)=3$; <b>b)</b> $\\log_{5}(2x+1)=2$; '
         '<b>c)</b> $\\lg(3x-2)=\\lg(x+6)$.</p>',
         hid="pelda-log-egyenletek",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> ÉT: $x-3&gt;0$, azaz $x&gt;3$. A definíció szerint '
                  '$x-3=2^{3}=8$, tehát $x=11$. Ez nagyobb $3$-nál, '
                  'így $\\boxed{x=11}$.</p>'
                  '<p><b>b)</b> ÉT: $2x+1&gt;0$, azaz $x&gt;-\\tfrac12$. Innen '
                  '$2x+1=5^{2}=25$, tehát $2x=24$ és $\\boxed{x=12}$ — az ÉT-ben van.</p>'
                  '<p><b>c)</b> ÉT: $3x-2&gt;0$ <b>és</b> $x+6&gt;0$, azaz $x&gt;\\tfrac23$ '
                  'és $x&gt;-6$ — a metszet $x&gt;\\tfrac23$. A logaritmust elhagyva '
                  '$3x-2=x+6$, tehát $2x=8$ és $\\boxed{x=4}$.</p>')),
   doboz("csapda", "Sinister vírus-kódja",
         '<p><b>A hamis gyök.</b> Oldd meg gondolatban: $\\lg(x^{2}-4x)=\\lg 5$. '
         'A logaritmust elhagyva $x^{2}-4x-5=0$, ahonnan $x_{1}=5$ és $x_{2}=-1$. '
         'A $-1$ elsőre gyanús — pedig <b>jó megoldás</b>: az argumentum értéke '
         '$(-1)^{2}-4\\cdot(-1)=5&gt;0$.</p>'
         '<p>Tanulság: <b>nem az $x$ előjelét kell nézni, hanem az argumentum '
         'értékét</b>. Mindig helyettesíts vissza az ÉT-feltételbe, ne találgass.</p>'),
   kviz('Mi a $\\log_{3}(x+2)=2$ egyenlet megoldása?',
        ['$x=7$', '$x=9$', '$x=4$'], 0,
        jo="✔ x + 2 = 3² = 9, tehát x = 7 (és 7 + 2 > 0, az ÉT rendben).",
        nem="✘ A definíció szerint x + 2 = 3² = 9, ahonnan x = 7."),
 ]),

 ("Logaritmusos egyenlőtlenségek", [
   'Itt a két korábbi szempont <b>találkozik</b>: kell az értelmezési tartomány (mint az '
   'egyenleteknél), és figyelni kell a <b>jelfordulásra</b> (mint az exponenciális '
   'egyenlőtlenségeknél). A végeredmény mindig a kettő <b>metszete</b>.',
   doboz("tetel", "Logaritmusos egyenlőtlenség",
         '<p>Tegyük fel, hogy az egyenlőtlenség $\\log_{a}u&lt;\\log_{a}v$ alakú '
         '(az ÉT: $u&gt;0$ és $v&gt;0$).</p>'
         '<ul>'
         '<li>Ha <b>$a&gt;1$</b> (növekvő): $u&lt;v$ — a <b>jel marad</b>.</li>'
         '<li>Ha <b>$0&lt;a&lt;1$</b> (csökkenő): $u&gt;v$ — a <b>jel megfordul</b>.</li>'
         '</ul>'
         '<p>A megoldás a kapott egyenlőtlenség megoldáshalmazának és az '
         '<b>értelmezési tartománynak a metszete</b>.</p>',
         hid="tetel-log-egyenlotlenseg"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $\\log_{2}(x-1)&lt;4$; <b>b)</b> $\\log_{3}(2x-6)&gt;2$; '
         '<b>c)</b> $\\log_{0,5}(4x+1)\\ge\\log_{0,5}(x+7)$.</p>',
         hid="pelda-log-egyenlotlensegek",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> ÉT: $x-1&gt;0$, azaz $x&gt;1$. Az alap $2&gt;1$, a jel '
                  'marad: $x-1&lt;2^{4}=16$, tehát $x&lt;17$. A metszet: '
                  '$\\boxed{x\\in(1;17)}$.</p>'
                  '<p><b>b)</b> ÉT: $2x-6&gt;0$, azaz $x&gt;3$. Az alap $3&gt;1$: '
                  '$2x-6&gt;3^{2}=9$, tehát $2x&gt;15$ és $x&gt;\\tfrac{15}{2}$. '
                  'Ez szigorúbb az ÉT-nél, tehát $\\boxed{x\\in\\left(\\tfrac{15}{2};+\\infty\\right)}$.</p>'
                  '<p><b>c)</b> ÉT: $4x+1&gt;0$ és $x+7&gt;0$, azaz $x&gt;-\\tfrac14$ '
                  '(ez a szigorúbb). Az alap $0&lt;0{,}5&lt;1$, ezért a jel '
                  '<b>megfordul</b>: $4x+1\\le x+7$, tehát $3x\\le 6$ és $x\\le 2$. '
                  'A metszet: $\\boxed{x\\in\\left(-\\tfrac14;2\\right]}$.</p>')),
   doboz("csapda", "Sinister vírus-kódja",
         '<p>A három leggyakoribb hiba:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>Az ÉT kihagyása.</b> A c) feladatban ÉT nélkül $x\\le 2$ jönne ki — '
         'de a $-5$ például nem megoldás, mert ott $4x+1$ negatív.</li>'
         '<li><b>A jelfordulás elfelejtése.</b> Nézd meg az alapot, mielőtt elhagyod '
         'a logaritmust.</li>'
         '<li><b>Uniót írni metszet helyett.</b> Az ÉT és a kapott halmaz között '
         '<b>metszet</b> van: mindkét feltételnek egyszerre kell teljesülnie.</li>'
         '</ol>'),
   kviz('A $\\log_{0,2}(x+1)&gt;\\log_{0,2}(2x-3)$ megoldásánál mi történik a jellel?',
        ['Megfordul, mert az alap kisebb 1-nél.',
         'Marad, mert mindkét oldalon logaritmus áll.',
         'Megfordul, mert az argumentumok pozitívak.'], 0,
        jo="✔ A 0,2 alapú logaritmusfüggvény csökkenő, ezért a reláció megfordul.",
        nem="✘ Az alap dönt: 0 < 0,2 < 1 → a függvény csökkenő → a jel megfordul."),
   gyakorolj(FGY + "#alap-7", "A 7–14", FGY + "#kozep-4", "K 4–12"),
   brief('<b>Beast:</b> Küldetés teljesítve, kadétok. Az <b>Evolúciós Ugrás</b> megvan: '
         'tudjuk modellezni a robbanásszerű növekedést, és — ami fontosabb — tudunk '
         '<b>visszafelé</b> is számolni. Ez az anyag a <b>3. dolgozat</b> teljes '
         'terjedelme; a gyűjtemény végén találsz hozzá felkészítő sávot. '
         'Nézd át a taktikai memóriakártyát, aztán jöhet a terepküldetés.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-inverz-es-logaritmusfuggveny.html",
     cim="Az inverz függvény és a logaritmusfüggvény",
     cim_tiszta="Az inverz függvény és a logaritmusfüggvény",
     alcim="Az inverz fogalma és a tükrözés az $y=x$ egyenesre, a logaritmusfüggvény "
           "grafikonja, tulajdonságai és eltolásai.",
     chip="Az Evolúciós Ugrás · 7/8", szakaszok=C1,
     elozo=("feladatok-logaritmus.html", "Feladatok — logaritmus"),
     kovetkezo=("tananyag-logaritmusos-egyenletek.html",
                "Logaritmusos egyenletek és egyenlőtlenségek")),
 lap(**T, fajl="tananyag-logaritmusos-egyenletek.html",
     cim="Logaritmusos egyenletek és egyenlőtlenségek",
     cim_tiszta="Logaritmusos egyenletek és egyenlőtlenségek",
     alcim="Az értelmezési tartomány mint első lépés, az összevonás, a jelfordulás "
           "és a hamis gyökök kiszűrése.",
     chip="Az Evolúciós Ugrás · 8/8", szakaszok=C2,
     elozo=("tananyag-inverz-es-logaritmusfuggveny.html",
            "Az inverz függvény és a logaritmusfüggvény"),
     kovetkezo=(FGY, "Feladatok — logaritmusfüggvény")),
]
for u in KI:
    print("✓", os.path.basename(u))
