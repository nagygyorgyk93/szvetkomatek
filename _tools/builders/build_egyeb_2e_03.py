# -*- coding: utf-8 -*-
"""2e/03 — osszefoglalo (F4), terepkuldetes (F5p), Vészterem (F6h), temakor-index (F5)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, GYOKER
from fgy_common import cards, oldal, w

T = dict(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
         temakor="Exponenciális és logaritmusfüggvény")

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, log, N, solve, simplify, sqrt
x, t = symbols('x t', real=True)
def S(e): return sorted(solve(e, x))
def TT(e): return sorted(solve(e, t))
E = []
def chk(n, g, w_, tol=None):
    if tol is not None:
        if abs(float(g) - w_) > tol:
            E.append((n, float(g), w_))
    elif (g != w_) if isinstance(w_, (list, tuple)) else (simplify(g - w_) != 0):
        E.append((n, g, w_))
P = [
 # --- terepküldetés I
 ("TI1", 5*3**4, 405),
 ("TI2", S(3**x - 243), [5]), ("TI2e", 5*3**5, 1215),
 ("TI3", 80*R(1, 2)**3, 10),
 ("TI4", TT(t**2 - 12*t + 27), [3, 9]),
 ("TI4a", S(3**x - 3), [1]), ("TI4b", S(3**x - 9), [2]),
 # --- terepküldetés II
 ("TII1", N(log(500, 2)), 8.96578428466, 1e-9),
 ("TII2", N(9*log(10, 2)), 29.8973528540, 1e-9),
 ("TII3", S(x - 40), [40]), ("TII3e", R(1, 2)**5, R(1, 32)),
 ("TII4", sorted(solve(2*x**2 + x - 10, x)), [R(-5, 2), 2]),
 ("TII4e", (2*2 - 1)*(2 + 1), 9),
 # --- terepküldetés III
 ("TIII1", S(x - 10), [10]), ("TIII1e", 2**10, 1024),
 ("TIII2", S(2*x - 1 - 3), [2]),
 ("TIII3", S(x - 2 - 5), [7]),
 ("TIII4", S(4*x - 2 - (x + 7)), [3]), ("TIII4et", S(4*x - 2), [R(1, 2)]),
 # --- Vészterem
 ("DA1a", R(3)**-2, R(1, 9)), ("DA1b", R(2, 5)**0, 1), ("DA1c", R(49)**R(1, 2), 7),
 ("DA3a", S(x - 5), [5]), ("DA3b", S(2*x - 4), [2]), ("DA3c", S(x + 5), [-5]),
 ("DA4", 2**4*(4 - 1), 48), ("DA4x", S(x - 4), [4]),
 ("DA5a", S(x - 6), [6]), ("DA5b", S(x - 3), [3]),
 ("DA6a", log(128, 2), 7), ("DA6b", log(R(1, 25), 5), -2), ("DA6c", log(3, 9), R(1, 2)),
 ("DA7a", log(400, 10) - log(4, 10), 2), ("DA7b", log(4, 6) + log(54, 6), 3),
 ("DA8", S(3*x - 9), [3]),
 ("DA9", S(x + 5 - 9), [4]),
 ("DK1", TT(t**2 - 9*t + 8), [1, 8]),
 ("DK2", S(x**2 - x - 6), [-2, 3]),
 ("DK3", log(8, 4), R(3, 2)),
 ("DK4", S(x**2 - 16), [-4, 4]),
 ("DK5", S(3*x - 1 - 8), [3]),
 ("DK6", N(log(R(3, 2))/log(R(106, 100))), 6.958515633, 1e-8),
 ("DN1", TT(t**2 - 6*t - 27), [-3, 9]), ("DN1x", S(3**x - 9), [2]),
 ("DN2", S(x - 1 - 9), [10]),
 ("DN3", TT(t**2 - 3*t + 2), [1, 2]),
]
for it in P:
    chk(*it)
assert not E, E
print("sympy önteszt: OK —", len(P), "assert")

# ==================================================================== F4

OSSZ = [
 ("Az exponenciális függvény", [
  '<p>$f(x)=a^{x}$, ahol $a&gt;0$ és $a\\neq 1$ '
  '(<a href="tananyag-exponencialis-fuggveny.html#def-exponencialis">→</a>). '
  '<b>ÉT:</b> $\\mathbb{R}$ · <b>ÉK:</b> $(0;+\\infty)$ — az érték '
  '<b>sosem nulla és sosem negatív</b> · áthalad a $(0;1)$ ponton · aszimptota az '
  '$x$-tengely · nullahelye <b>nincs</b>.</p>',
  '<p><b>Monotonitás:</b> $a&gt;1$ → szigorúan <b>növekvő</b>; $0&lt;a&lt;1$ → szigorúan '
  '<b>csökkenő</b>. Mindkettő kölcsönösen egyértelmű — erre épül minden egyenlet '
  '(<a href="tananyag-exponencialis-fuggveny.html#tetel-monotonitas">→</a>).</p>',
  '<p><b>Transzformációk:</b> $y=a^{x}+c$ függőleges eltolás (az aszimptota is mozdul, '
  '$y=c$) · $y=a^{x-b}$ vízszintes eltolás <b>jobbra</b> · $y=a^{-x}$ tükrözés az '
  '$y$-tengelyre · $y=-a^{x}$ tükrözés az $x$-tengelyre '
  '(<a href="tananyag-exponencialis-fuggveny.html#tetel-transzformaciok">→</a>).</p>',
 ]),
 ("Exponenciális egyenletek", [
  '<p><b>Alapelv:</b> $a^{u}=a^{v}\\iff u=v$ — hozd <b>közös alapra</b> a két oldalt, '
  'majd hagyd el az alapot '
  '(<a href="tananyag-exponencialis-egyenletek.html#tetel-alapelv">→</a>).</p>',
  '<p><b>Kiemelés:</b> $a^{x+k}=a^{x}\\cdot a^{k}$, tehát $a^{x}$ minden tagból kiemelhető. '
  '⚠️ $2^{x+2}\\neq 2^{x}+4$ — a kitevőben álló összeg <b>szorzattá</b> bomlik '
  '(<a href="tananyag-exponencialis-egyenletek.html#tetel-kiemeles">→</a>).</p>',
  '<p><b>Másodfokúra visszavezethető:</b> ha $a^{2x}$ és $a^{x}$ is szerepel, legyen '
  '$t=a^{x}$, ahol <b>$t&gt;0$</b>. Ekkor $a^{2x}=t^{2}$, és másodfokú egyenlet marad. '
  '⚠️ A $t$-t <b>vissza kell helyettesíteni</b>, a nem pozitív gyököt pedig <b>eldobni</b> '
  '(<a href="tananyag-exponencialis-egyenletek.html#tetel-helyettesites">→</a>).</p>',
 ]),
 ("Exponenciális egyenlőtlenségek", [
  '<p>Közös alapra hozás után az alap dönt:</p>'
  '<div class="tblwrap"><table>'
  '<tr><th>Alap</th><th>Monotonitás</th><th>$a^{u}&lt;a^{v}$ ⟹</th></tr>'
  '<tr><td>$a&gt;1$</td><td>növekvő</td><td>$u&lt;v$ — a jel <b>marad</b></td></tr>'
  '<tr><td>$0&lt;a&lt;1$</td><td>csökkenő</td><td>$u&gt;v$ — a jel <b>MEGFORDUL</b></td></tr>'
  '</table></div>'
  '<p>(<a href="tananyag-exponencialis-egyenlotlensegek.html#tetel-jelfordulas">→</a>) '
  '⚠️ A $\\pm\\infty$ mellett <b>mindig nyitott</b> zárójel áll.</p>',
 ]),
 ("A logaritmus fogalma és azonosságai", [
  '<p><b>Definíció:</b> $\\log_{a}b=c\\iff a^{c}=b$, ahol $a&gt;0$, $a\\neq 1$ és '
  '<b>$b&gt;0$</b> (<a href="tananyag-logaritmus-fogalma.html#def-logaritmus">→</a>). '
  'Negatív szám és a nulla logaritmusa <b>nem létezik</b>.</p>',
  '<p><b>Alapösszefüggések:</b> $\\log_{a}1=0$ · $\\log_{a}a=1$ · $\\log_{a}a^{k}=k$ · '
  '$a^{\\log_{a}b}=b$ '
  '(<a href="tananyag-logaritmus-fogalma.html#tetel-alaposszefuggesek">→</a>). '
  'Jelölés: $\\lg b=\\log_{10}b$ és $\\ln b=\\log_{e}b$.</p>',
  '<p><b>Azonosságok</b> ($u,v&gt;0$):</p>'
  '$$\\log_{a}(uv)=\\log_{a}u+\\log_{a}v,\\qquad'
  '\\log_{a}\\frac{u}{v}=\\log_{a}u-\\log_{a}v,\\qquad'
  '\\log_{a}u^{k}=k\\log_{a}u.$$'
  '<p>⚠️ $\\log_{a}(u+v)\\neq\\log_{a}u+\\log_{a}v$ — a logaritmusnak az '
  '<b>összeadásról nincs mondanivalója</b> '
  '(<a href="tananyag-logaritmus-azonossagai.html#tetel-azonossagok">→</a>).</p>',
 ]),
 ("Áttérés más alapra és alkalmazások", [
  '<p>$$\\log_{a}b=\\frac{\\log_{c}b}{\\log_{c}a}=\\frac{\\lg b}{\\lg a}$$'
  '<p>Felül az <b>argumentum</b>, alul az <b>alap</b> — és <b>osztás</b>, nem kivonás '
  '(<a href="tananyag-attetes-mas-alapra.html#tetel-attetes">→</a>). '
  'Ellenőrzés fejben: $\\log_{2}7$ a $2$ és a $3$ között van, mert $4&lt;7&lt;8$.</p>',
  '<p><b>Logaritmikus skálák:</b> $\\mathrm{pH}=-\\lg[\\mathrm{H}^{+}]$ · Richter · '
  'decibel ($L=10\\lg\\frac{I}{I_{0}}$) — minden egység <b>tízszeres</b> különbség '
  '(<a href="tananyag-attetes-mas-alapra.html#pelda-alkalmazas">→</a>).</p>',
  '<p><b>Növekedési feladat:</b> a modell $q^{n}=k$ alakú, a megoldás '
  '$n=\\log_{q}k=\\dfrac{\\lg k}{\\lg q}$. Kamat: $1{,}05^{n}=2$; felezés: '
  '$\\left(\\tfrac12\\right)^{t/T}=r$.</p>',
 ]),
 ("A logaritmusfüggvény, egyenletek és egyenlőtlenségek", [
  '<p><b>$f(x)=\\log_{a}x$ az $y=a^{x}$ inverze</b>, a grafikonjuk az $y=x$ egyenesre '
  'tükrös (<a href="tananyag-inverz-es-logaritmusfuggveny.html#tetel-inverz-grafikon">→</a>). '
  '<b>ÉT:</b> $(0;+\\infty)$ · <b>ÉK:</b> $\\mathbb{R}$ · nullahely $x=1$ · aszimptota az '
  '$y$-tengely · $a&gt;1$ → növekvő, $0&lt;a&lt;1$ → csökkenő.</p>',
  '<p><b>Egyenlet — a munkamenet:</b> ① ÉT (minden argumentum pozitív, több feltétel esetén '
  'a <b>metszetük</b>) → ② azonosságokkal <b>összevonás</b> → ③ '
  '$\\log_{a}u=\\log_{a}v\\iff u=v$, illetve $\\log_{a}u=c\\iff u=a^{c}$ → ④ '
  '<b>összevetés az ÉT-vel</b> '
  '(<a href="tananyag-logaritmusos-egyenletek.html#tetel-log-egyenlet-menete">→</a>).</p>',
  '<p><b>Egyenlőtlenség:</b> ugyanez, de az alap szerint <b>fordulhat a jel</b>, és a '
  'végeredmény mindig az ÉT és a kapott halmaz <b>metszete</b> '
  '(<a href="tananyag-logaritmusos-egyenletek.html#tetel-log-egyenlotlenseg">→</a>).</p>',
  doboz("csapda", "Amire a dolgozaton a legtöbben ráfutnak",
        '<p>1) <b>Jelfordulás</b>: mielőtt elhagyod az alapot, kérdezd meg, nagyobb-e '
        '$1$-nél. &nbsp; 2) $a^{x+k}=a^{x}\\cdot a^{k}$, <b>nem</b> $a^{x}+a^{k}$. &nbsp; '
        '3) A helyettesítésnél $t&gt;0$ — a negatív gyököt <b>eldobod</b>, és a $t$-ből '
        '<b>vissza kell számolni</b> $x$-et. &nbsp; 4) Logaritmusnál <b>mindig ÉT-tel kezdj</b>; '
        'nem az $x$ előjelét nézed, hanem az <b>argumentum értékét</b>. &nbsp; '
        '5) $\\lg(u+v)\\neq\\lg u+\\lg v$. &nbsp; 6) Áttérésnél <b>osztás</b>, felül az '
        'argumentum. &nbsp; 7) A végtelen mellett <b>nyitott</b> zárójel; az ÉT és a megoldás '
        'között <b>metszet</b> van, nem unió.</p>'),
  '<div class="gyakorolj"><span class="ikon">🎯</span><p>Élesben: a '
  '<a href="feladatok-logaritmusfuggveny.html#gyak-dolgozat">gyakorló dolgozattal</a> mérd fel '
  'magad, majd indulj <a href="terepkuldetes.html">A Vírusgörbe terepküldetésre</a>!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Taktikai memóriakártya",
    cim_tiszta="Taktikai memóriakártya", itt="Taktikai memóriakártya",
    alcim="Az Evolúciós Ugrás minden képlete, protokollja és tipikus csapdája egy helyen — "
          "ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip="Az Evolúciós Ugrás · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-logaritmusfuggveny.html", "Feladatok — logaritmusfüggvény"),
    kovetkezo=("terepkuldetes.html", "A Vírusgörbe terepküldetés"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> Kadét, ez már nem szimuláció. Dr. Baljós vírusa kijutott a '
         'laborból, és <b>exponenciálisan</b> terjed. Három dolgot kell tudnom, méghozzá '
         'gyorsan: milyen ütemben nő a fertőzés, <b>mennyi időnk van</b> a kritikus '
         'küszöbig, és meddig tart ki a karanténpajzs. Az első kérdésre az exponenciális '
         'függvény felel, a másodikra a <b>logaritmus</b>, a harmadikra az '
         'egyenlőtlenségek. Indulhatsz.'),
   '<p class="lead">Ez a küldetés a teljes témakört használja: exponenciális függvényt és '
   'egyenletet, helyettesítést, logaritmus-azonosságokat, áttérést más alapra, valamint '
   'exponenciális és logaritmusos egyenlőtlenséget. Dolgozz füzetben, és a végén add le a '
   'jelentést. <b>A megoldások nincsenek fent</b> — ezt a bevetést a tanárod értékeli.</p>',
 ]),
 ("Fázis I — A terjedés modellezése", [
   doboz("pelda", "I. fázis: a növekedési görbe",
         '<p>A fertőzött sejtek száma óránként a <b>háromszorosára</b> nő, és $5$ sejtből '
         'indul: $N(t)=5\\cdot 3^{t}$.</p>'
         '<ol class="reszfeladatok">'
         '<li>Hány fertőzött sejt lesz <b>4 óra</b> múlva?</li>'
         '<li>Mikor éri el a telep az <b>1215</b> sejtet?</li>'
         '<li>Az ellenszérum hatóanyaga $6$ óránként feleződik: '
         '$M(t)=80\\cdot\\left(\\tfrac12\\right)^{t/6}$ mg. Mennyi marad belőle '
         '<b>18 óra</b> után?</li>'
         '<li>A vírus két kritikus időpontban mutálódik; ezeket a '
         '$9^{t}-12\\cdot 3^{t}+27=0$ egyenlet adja meg. Mikor?</li>'
         '</ol>'),
 ]),
 ("Fázis II — A visszaszámlálás", [
   doboz("pelda", "II. fázis: mennyi időnk van?",
         '<ol class="reszfeladatok">'
         '<li>Egy másik törzs óránként <b>duplázódik</b>, egyetlen sejtből. Hány óra alatt '
         'éri el az <b>500</b> sejtet? (Számológéppel, négy tizedesre.)</li>'
         '<li>És hány óra alatt az <b>egymilliárdot</b> ($10^{9}$)? Használd ki, hogy '
         '$\\log_{2}10^{9}=9\\log_{2}10$.</li>'
         '<li>Egy izotóp felezési ideje $8$ nap. Hány nap alatt csökken a mennyisége az '
         '<b>egy harminckettedére</b>?</li>'
         '<li>A karanténkód: $\\log_{3}(2x-1)+\\log_{3}(x+1)=2$. Mennyi $x$? '
         '(Az értelmezési tartománnyal kezdj!)</li>'
         '</ol>'),
 ]),
 ("Fázis III — A karantén határai", [
   doboz("pelda", "III. fázis: meddig tart ki a pajzs?",
         '<ol class="reszfeladatok">'
         '<li>A helyzet <b>kritikus</b>, ha a sejtszám eléri az $1024$-et, azaz '
         '$2^{t}\\ge 1024$. Mettől kritikus?</li>'
         '<li>A pajzs addig működik, amíg $3^{2t-1}&lt;27$. Meddig?</li>'
         '<li>Az ellenszérum akkor még hatásos, ha '
         '$\\left(\\tfrac12\\right)^{t-2}&gt;\\tfrac{1}{32}$. Hány óráig?</li>'
         '<li>A zárókód: $\\log_{0,5}(4x-2)\\ge\\log_{0,5}(x+7)$. Add meg a megoldást '
         'intervallummal — és <b>ne feledd az értelmezési tartományt</b>!</li>'
         '</ol>'),
   '<div class="gyakorolj"><span class="ikon">📋</span><p><b>Jelentés:</b> a füzetedben '
   'minden fázisnál legyen ott a <b>modell</b> (a felírt egyenlet vagy egyenlőtlenség), '
   'a levezetés és a <b>mértékegységgel</b> ellátott válasz. A logaritmusos feladatoknál '
   'az értelmezési tartomány is része a megoldásnak.</p></div>',
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="A Vírusgörbe", cim_tiszta="A Vírusgörbe",
    itt="A Vírusgörbe terepküldetés",
    alcim="Háromfázisú járványügyi bevetés — növekedési modell, visszaszámlálás "
          "logaritmussal és a karantén határainak kiszámítása.",
    chip="Az Evolúciós Ugrás · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Taktikai memóriakártya"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h

DR_A = [
 ("Számold ki!",
  ["$3^{-2}$", "$\\left(\\tfrac25\\right)^{0}$", "$49^{0,5}$"],
  ["$\\dfrac19$", "$1$", "$7$"], True),
 ("Ábrázold, és add meg az aszimptotát!",
  ["$y=2^{x}-1$", "$y=\\left(\\tfrac13\\right)^{x+1}$"],
  ["$1$-gyel lejjebb; aszimptota: $y=-1$; nullahely: $x=0$.",
   "$1$-gyel balra; aszimptota az $x$-tengely; a $(0;\\tfrac13)$ ponton át."], True),
 ("Oldd meg!", ["$3^{x}=243$", "$5^{2x}=625$", "$\\left(\\tfrac12\\right)^{x}=32$"],
  ["$x=5$", "$x=2$", "$x=-5$"], True),
 ("Oldd meg kiemeléssel! $2^{x+2}-2^{x}=48$", None,
  "$2^{x}(4-1)=48$, azaz $3\\cdot 2^{x}=48$ és $2^{x}=16$: $x=4$."),
 ("Oldd meg!", ["$2^{x}\\le 64$", "$\\left(\\tfrac13\\right)^{x}&gt;\\tfrac{1}{27}$"],
  ["$x\\in(-\\infty;6]$", "A jel fordul: $x&lt;3$, azaz $x\\in(-\\infty;3)$"], True),
 ("Számold ki!", ["$\\log_{2}128$", "$\\log_{5}\\tfrac{1}{25}$", "$\\log_{9}3$"],
  ["$7$", "$-2$", "$\\dfrac12$"], True),
 ("Vond össze, majd számold ki!",
  ["$\\lg 400-\\lg 4$", "$\\log_{6}4+\\log_{6}54$"],
  ["$\\lg 100=2$", "$\\log_{6}216=3$"], True),
 ("Add meg az értelmezési tartományt! $y=\\log_{2}(3x-9)$", None,
  "$3x-9&gt;0$, tehát $x\\in(3;+\\infty)$."),
 ("Oldd meg! $\\log_{3}(x+5)=2$", None,
  "ÉT: $x&gt;-5$; $x+5=9$, tehát $x=4$."),
]

DR_K = [
 ("Oldd meg helyettesítéssel! $4^{x}-9\\cdot 2^{x}+8=0$", None,
  "$t=2^{x}$: $t^{2}-9t+8=0$, innen $t_{1}=1$, $t_{2}=8$, tehát $x_{1}=0$ és $x_{2}=3$."),
 ("Oldd meg! $2^{x^{2}-x-6}=1$", None,
  "$x^{2}-x-6=0$, innen $x_{1}=-2$ és $x_{2}=3$."),
 ("Számold ki! $\\log_{4}8$", None,
  "Közös alap a $2$: $\\dfrac{\\log_{2}8}{\\log_{2}4}=\\dfrac32$."),
 ("Oldd meg! $\\lg(x+3)+\\lg(x-3)=\\lg 7$", None,
  "ÉT: $x&gt;3$. Innen $x^{2}-9=7$, azaz $x=\\pm 4$ — az ÉT miatt csak $x=4$."),
 ("Oldd meg! $\\log_{2}(3x-1)&lt;3$", None,
  "ÉT: $x&gt;\\tfrac13$; $3x-1&lt;8$, tehát $x&lt;3$. A metszet: "
  "$x\\in\\left(\\tfrac13;3\\right)$."),
 ("Egy befektetés évi $6\\%$-kal gyarapszik. Hány év alatt lesz a másfélszerese?", None,
  "$1{,}06^{n}=1{,}5$, tehát $n=\\dfrac{\\lg 1{,}5}{\\lg 1{,}06}\\approx 6{,}96$ — "
  "a <b>7. év</b> folyamán."),
]

DR_N = [
 ("Oldd meg! $9^{x}-2\\cdot 3^{x+1}-27=0$", None,
  "$3^{x+1}=3\\cdot 3^{x}$, tehát $t^{2}-6t-27=0$: $t_{1}=9$, $t_{2}=-3$. "
  "A negatív kiesik, marad $3^{x}=9$, azaz $x=2$."),
 ("Oldd meg! $\\log_{\\frac13}(x-1)\\ge -2$", None,
  "ÉT: $x&gt;1$. Az alap kisebb $1$-nél, a jel fordul: "
  "$x-1\\le\\left(\\tfrac13\\right)^{-2}=9$, tehát $x\\le 10$. A metszet: $x\\in(1;10]$."),
 ("Oldd meg! $\\lg^{2}x-3\\lg x+2=0$", None,
  "ÉT: $x&gt;0$. A $t=\\lg x$ helyettesítéssel $t^{2}-3t+2=0$: $t_{1}=1$, $t_{2}=2$, "
  "tehát $x_{1}=10$ és $x_{2}=100$."),
]

dr_brief = ('<div class="brief"><p>🕹️ <b>SZVETI:</b> <b>Vészterem</b> — Az Evolúciós Ugrás '
            'modul. A szimuláció a <b>teljes témakört</b> lefedi: exponenciális függvény és '
            'egyenletek, helyettesítés, egyenlőtlenségek, a logaritmus fogalma és azonosságai, '
            'áttérés más alapra, logaritmusfüggvény és logaritmusos egyenletek. Haladj a '
            'fokozatokon: zöld → sárga → piros. A végeredményt lenyithatod, de előbb küzdd '
            'le magad!</p></div>')

dr_body = ('    ' + dr_brief + '\n'
           '    <h2 id="alap">🟢 Alapfokozat</h2>\n' + cards(DR_A, "alap", "alap") +
           '\n    <h2 id="kozep">🟡 Középfokozat</h2>\n' + cards(DR_K, "kozep", "kozep") +
           '\n    <h2 id="nehez">🔴 Nehéz fokozat</h2>\n' + cards(DR_N, "nehez", "nehez"))

oldal(**T, fajl="feladatok-hazi.html", cim="Vészterem",
      h1="🕹️ Vészterem — házi feladatgyűjtemény", itt="Vészterem — házi",
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
    # a kártyacím is átmegy a matek-konverzión (pl. „Az $i$ hatványai")
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = [
 kartya("tananyag-exponencialis-fuggveny.html", "Az exponenciális függvény",
        "A fogalom, a két alapeset ($a&gt;1$ és $0&lt;a&lt;1$), tulajdonságok, eltolás és tükrözés"),
 kartya("tananyag-exponencialis-egyenletek.html", "Exponenciális egyenletek",
        "Közös alapra hozás, kiemelés és a $t=a^{x}$ helyettesítés"),
 kartya("tananyag-exponencialis-egyenlotlensegek.html", "Exponenciális egyenlőtlenségek",
        "A monotonitásból következő jelfordulás és az intervallumos írásmód"),
 kartya("tananyag-logaritmus-fogalma.html", "A logaritmus fogalma",
        "A hatványozás második fordítottja, a négy alapösszefüggés, $\\lg$ és $\\ln$"),
 kartya("tananyag-logaritmus-azonossagai.html", "A logaritmus azonosságai",
        "Szorzat, hányados és hatvány logaritmusa — bontás és összevonás"),
 kartya("tananyag-attetes-mas-alapra.html", "Áttérés más alapra és alkalmazások",
        "Az áttérési képlet, számológép-használat, logaritmikus skálák"),
 kartya("tananyag-inverz-es-logaritmusfuggveny.html", "Az inverz és a logaritmusfüggvény",
        "Tükrözés az $y=x$ egyenesre, a logaritmusgörbe tulajdonságai és eltolásai"),
 kartya("tananyag-logaritmusos-egyenletek.html", "Logaritmusos egyenletek és egyenlőtlenségek",
        "Az értelmezési tartomány mint első lépés, összevonás, jelfordulás, hamis gyökök"),
 kartya("feladatok-exponencialis.html", "🏋️ Exponenciális függvény — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker, a végén <b>gyakorló ellenőrzővel</b>"),
 kartya("feladatok-logaritmus.html", "🏋️ A logaritmus — feladatok",
        "Alap · Közép · Nehéz + Joker — definíció, azonosságok, áttérés, skálák"),
 kartya("feladatok-logaritmusfuggveny.html", "🏋️ A logaritmusfüggvény — feladatok",
        "Alap · Közép · Nehéz + Joker, a végén <b>gyakorló dolgozattal</b>"),
 kartya("feladatok-hazi.html", "🕹️ Vészterem — házi feladatok",
        "A teljes témakört lefedő házi feladatsor, óraszám-arányosan"),
 kartya("terepkuldetes.html", "🎯 A Vírusgörbe terepküldetés",
        "Háromfázisú járványügyi bevetés — a teljes témakör egyben"),
 kartya("osszefoglalo.html", "📇 Taktikai memóriakártya",
        "Minden képlet, protokoll és tipikus csapda egy helyen — dolgozat előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exponenciális és logaritmusfüggvény | 2e | Szvetkó matek</title>
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
  <span class="itt">Exponenciális és logaritmusfüggvény</span>
</nav>
<div class="hero">
  <h1>Exponenciális és logaritmusfüggvény</h1>
  <p class="alcim">A robbanásszerű növekedés függvényétől a logaritmuson át az inverz
  függvényig — modellezés, visszaszámlálás, egyenletek és egyenlőtlenségek.</p>
  <div class="meta-sor"><span class="chip ora">21 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧬 <b>Szektor 03 — Az Evolúciós Ugrás (A Vírusgörbe).</b> Kiképző:
  <b>Dr. Bestia</b> (Dr. Bestia). Dr. Baljós vírusa nem lineárisan és nem másodfokon terjed, hanem
  <b>megkétszereződik</b> minden lépésben — ezt a növekedést a másodfokú függvény már nem
  írja le. Dr. Bestia a laborból vezeti a bevetést: előbb megtanuljuk <b>modellezni</b> a
  terjedést, aztán megfordítjuk a kérdést, és a <b>logaritmussal</b> számoljuk ki, mennyi
  időnk maradt.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🧬 Az exponenciális függvény — Dr. Bestia</h3>
    <div class="racs">
''' + "\n".join(K[0:3]) + '''
    </div>

    <h3>🔬 A logaritmus — Dr. Bestia</h3>
    <div class="racs">
''' + "\n".join(K[3:6]) + '''
    </div>

    <h3>🪞 A logaritmusfüggvény — Dr. Bestia</h3>
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
    A Vírusgörbe terepküldetés. A Vészterem házi bármikor jöhet.</p>
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
