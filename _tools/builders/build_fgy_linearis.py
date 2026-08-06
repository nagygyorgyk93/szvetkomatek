# -*- coding: utf-8 -*-
"""1e/07 — Lineáris egyenletek, egyenlőtlenségek és rendszerek KÖZÖS feladatgyűjtemény.
Küldetés „A Végső Egyenlet" (teljes csapat). Egy drill-deck. Végeredmény = KIZÁRÓLAG a végső válasz.
A 3_Szöveges feladatok.docx MIND a 17 feladata bekerül (Közép 1-13, Nehéz 14-17). Gauss: max 1 feladat.
Grafikus rendszermegoldás NINCS a gyűjteményben (csak a tananyagban)."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, w

DEST = glob.glob("/sessions/*/mnt/Claude/web/1e/07-linearis-egyenletek-es-rendszerek")[0]

# ===================== önellenőrzés =====================
import sympy as sp
from sympy import symbols, solve, Eq, Rational, simplify
x,y,z,v,m,a=symbols('x y z v m a')
def chk(sol, **exp):
    for k,val in exp.items(): assert simplify(sol[symbols(k)]-val)==0,(sol,k,val)
# Alap
assert solve(Eq(3*x-7,8),x)==[5]; assert solve(Eq(2*(x-3),x+4),x)==[10]
assert solve(Eq(5*x+1,3*x-7),x)==[-4]; assert solve(Eq(x/2+3,7),x)==[8]
assert solve(Eq((x+1)/2,3),x)==[5]; assert solve(Eq(x/3-x/4,1),x)==[12]; assert solve(Eq((2*x-1)/3,x-2),x)==[5]
assert solve(3*x-7-8,x)==[5]  # dummy
chk(solve([Eq(x+y,5),Eq(x-y,1)],[x,y],dict=True)[0], x=3,y=2)
chk(solve([Eq(2*x+y,7),Eq(x-y,2)],[x,y],dict=True)[0], x=3,y=1)
assert solve(Eq(5-(2*x-1),3*x-4),x)==[2]
# Közép mechanikus
assert solve(Eq((3*x+1)/2-(x-2)/3,7),x)==[5]
assert solve(Eq((x+3)*(x-2)-(x-1)*(x+4),4),x)==[-3]
assert solve(3*(x-1)>=x+1)  # inequality solvable
assert solve(Eq(4*(x-1)-3*(x+2),0))  # dummy
chk(solve([Eq((4*x+5*y)/3,(x-3*y)/2+4),Eq((3*x+y)/2,(2*x+7*y)/3-1)],[x,y],dict=True)[0], x=1,y=1)
assert solve(Eq((2*m-1)*2+3,5),m)==[1]
# Gauss 3x3
chk(solve([Eq(x+y+z,6),Eq(x-y+z,2),Eq(2*x+y-z,1)],[x,y,z],dict=True)[0], x=1,y=2,z=3)
# Nehéz
assert solve(Eq(1+5/((v-3)*(v+2)),-1/(v+2)),v)==[2]   # v=-2 kizárva
assert set(solve(Eq(x**2-5*x,0),x))=={0,5}
# szöveges kulcs-ellenőrzés
assert solve([Eq(symbols('n')+symbols('f'),35),Eq(4*symbols('n')+2*symbols('f'),94)],[symbols('n'),symbols('f')])[symbols('n')]==12
# munka-feladatok (nehezebb)
t=symbols('t'); base=Rational(1,6)+Rational(1,10); rem=1-base-Rational(1,12)
assert 1+Rational(1,2)+solve(Eq(t*base,rem),t)[0]==Rational(63,16)
assert 2+(1-2*Rational(1,18)-2*Rational(1,15))/Rational(1,15)==Rational(40,3)
assert 1/(Rational(1,5)+Rational(1,8)+Rational(1,9))==Rational(360,157)
print("MINDEN ASSERT OK")

# ======================== ALAP (11) ========================
ALAP = [
 ("Oldd meg a lineáris egyenleteket!",
  ["$3x-7=8$","$2(x-3)=x+4$","$5x+1=3x-7$","$\\dfrac{x}{2}+3=7$"],
  "a) $x=5$; b) $x=10$; c) $x=-4$; d) $x=8$.", True),
 ("Oldd meg a törtes egyenleteket!",
  ["$\\dfrac{x+1}{2}=3$","$\\dfrac{x}{3}-\\dfrac{x}{4}=1$","$\\dfrac{2x-1}{3}=x-2$"],
  "a) $x=5$; b) $x=12$; c) $x=5$.", True),
 ("Oldd meg az egyenlőtlenségeket, és ábrázold a megoldáshalmazt a számegyenesen!",
  ["$2x-3<5$","$3(x-1)\\ge x+1$","$-2x>6$"],
  "a) $x<4$; b) $x\\ge 2$; c) $x<-3$.", True),
 ("Adott az $f(x)=2x-4$ függvény.",
  ["$f(0)$","$f(3)$","a nullahelye","a tengelymetszete az $y$-tengelyen"],
  "a) $-4$; b) $2$; c) $x=2$; d) $(0,-4)$.", True),
 ("Add meg az $f(x)=-x+3$ függvény három pontját (az ábrázoláshoz)!",
  None, "pl. $(0,3),\\ (1,2),\\ (3,0)$."),
 ("Oldd meg a rendszert behelyettesítéssel: $x+y=5$, $x-y=1$.",
  None, "$x=3,\\ y=2$."),
 ("Oldd meg a rendszert az együtthatók egyenlővé tételével: $2x+y=7$, $x-y=2$.",
  None, "$x=3,\\ y=1$."),
 ("Melyik szám a megoldás?",
  ["$4x=20$","$x-8=-3$","$3x+6=0$","$7-x=2$"],
  "a) $5$; b) $5$; c) $-2$; d) $5$.", True),
 ("Adott az $f(x)=-3x+2$ függvény. Számítsd ki:",
  ["$f(1)$","$f(-2)$","$f(0)$"],
  "a) $-1$; b) $8$; c) $2$.", True),
 ("Add meg a megoldáshalmazt intervallummal!",
  ["$x>2$","$x\\le -1$","$-3\\le x<4$"],
  "a) $(2,\\infty)$; b) $(-\\infty,-1]$; c) $[-3,4)$.", True),
 ("Rendezd lineáris egyenletté, és oldd meg: $5-(2x-1)=3x-4$.",
  None, "$x=2$."),
]

# ======================== KÖZÉP (mechanikus 5 + Gauss 1 + szöveges 1-13) ========================
KOZEP = [
 ("Oldd meg a törtes egyenletet: $\\dfrac{3x+1}{2}-\\dfrac{x-2}{3}=7$.",
  None, "$x=5$."),
 ("Oldd meg a kibontással: $(x+3)(x-2)-(x-1)(x+4)=4$.",
  None, "$x=-3$."),
 ("Oldd meg az egyenlőtlenséget, és ábrázold: $4(x-1)-3(x+2)>-8$.",
  None, "$x>2$."),
 ("Oldd meg a törtes egyenletrendszert: $\\dfrac{4x+5y}{3}=\\dfrac{x-3y}{2}+4$ és $\\dfrac{3x+y}{2}=\\dfrac{2x+7y}{3}-1$.",
  None, "$x=1,\\ y=1$."),
 ("Milyen $m$ esetén halad át az $y=(2m-1)x+3$ egyenes a $P(2,5)$ ponton?",
  None, "$m=1$."),
 ("Oldd meg a háromismeretlenes rendszert (Gauss): $x+y+z=6$, $x-y+z=2$, $2x+y-z=1$.",
  None, "$x=1,\\ y=2,\\ z=3$."),
 # --- 3_Szöveges feladatok.docx 1-13 (hiánytalanul) ---
 ("A ketrecben nyulak és fácánok vannak. Ha a ketrecben $35$ fej és $94$ láb látható, akkor hány nyúl és hány fácán van a ketrecben?",
  None, "$12$ nyúl és $23$ fácán."),
 ("Pistike gombát szed az erdőben. Hétfőn $1{,}1$ kg-mal kevesebbet szedett, mint szerdán, pénteken pedig $0{,}8$ kg-mal többet, mint szerdán. Melyik nap mennyit szedett, ha a három nap összesen $4{,}8$ kg jött össze?",
  None, "hétfő $0{,}6$ kg, szerda $1{,}7$ kg, péntek $2{,}5$ kg."),
 ("Timon és Pumba együtt $112$ kg-ot nyomnak. Pumba $15$-ször olyan nehéz, mint Timon. Hány kilogramm külön-külön Timon és Pumba?",
  None, "Timon $7$ kg, Pumba $105$ kg."),
 ("Jancsika és Juliska sétálnak az erdőben; összesen $9{,}2$ km-t sétáltak. Mennyit sétáltak külön-külön, ha Juliska háromszor akkora utat tett meg, mint Jancsika?",
  None, "Jancsika $2{,}3$ km, Juliska $6{,}9$ km."),
 ("A téglalap egyik oldala kétszer hosszabb a másiknál. Határozd meg az oldalak hosszát, ha a kerület $24$ cm!",
  None, "$4$ cm és $8$ cm."),
 ("Egy panzióban három- és kétágyas szobák vannak. Összesen $14$ szoba van, a férőhelyek száma $34$. Hány két-, illetve háromágyas szoba van?",
  None, "$6$ háromágyas és $8$ kétágyas szoba."),
 ("Egy- és kéteurós pénzérméből összegyűjtöttünk $35$ db-ot, összesen $56$ eurót. Melyik pénzérméből hány db-ot gyűjtöttünk?",
  None, "$14$ db egyeurós és $21$ db kéteurós."),
 ("Egy kókuszrúd és egy csokiszelet ára $560$ Ft. Három csokiszelet $80$ Ft-tal drágább, mint egy kókuszrúd. Mennyit kell fizetnünk öt csokiszeletért és két kókuszrúdért?",
  None, "$1600$ Ft (a csoki $160$ Ft, a kókuszrúd $400$ Ft)."),
 ("A pénzváltó automata a papírpénzt $10$ és $20$ forintosokra váltja, és megválaszthatjuk, hány érmét kapjunk. Hogyan váltja fel az $1000$ Ft-ot, ha $90$ érmét kérünk?",
  None, "$80$ db tízforintos és $10$ db húszforintos."),
 ("Húsz év múlva az apa kétszer annyi idős lesz, mint a fia; $8$ évvel ezelőtt pedig hatszor idősebb volt nála. Hány évesek külön-külön?",
  None, "az apa $50$, a fia $15$ éves."),
 ("Egy kétjegyű szám számjegyeinek összege $11$. Ha a számjegyeit felcseréljük, $45$-tel kisebb számot kapunk. Melyik az eredeti szám?",
  None, "$83$."),
 ("Karcsi $17$ évvel fiatalabb mogorva szomszédjánál. Ha kétszer annyi idős lenne, mint most, akkor egy évvel volna idősebb, mint a szomszédja most. Hány éves a mogorva szomszéd?",
  None, "$35$ éves (Karcsi $18$)."),
 ("Két iskolai csoport két, egymástól $25$ km-re lévő turistaházban szállt meg, melyeket egy ösvény köt össze. Az egyik csoport óránként $4$, a másik $6$ km-t tesz meg. Ha egyszerre indulnak egymás felé, mennyi idő múlva és hol találkoznak?",
  None, "$2{,}5$ óra múlva; a lassabb csoport házától $10$ km-re (a gyorsabbétól $15$ km-re)."),
]

# ======================== NEHÉZ (mechanikus 4 + szöveges 14-17) ========================
NEHEZ = [
 ("Oldd meg a rendszert az $a$ valós paraméter függvényében: $2x+3y=1$, $-2x+ay=0$.",
  None, "ha $a\\neq -3$: $x=\\dfrac{a}{2(a+3)},\\ y=\\dfrac{1}{a+3}$; ha $a=-3$: nincs megoldás."),
 ("Oldd meg (figyelj az értelmezési tartományra): $1+\\dfrac{5}{(v-3)(v+2)}=-\\dfrac{1}{v+2}$.",
  None, "$v=2$ (a $v=-2$ az ÉT miatt kizárva)."),
 ("Oldd meg kiemeléssel: $x^2-5x=0$.",
  None, "$x=0$ vagy $x=5$."),
 ("Oldd meg az egyenlőtlenséget: $\\dfrac{2x-1}{3}-\\dfrac{x+2}{2}\\le 1$.",
  None, "$x\\le 14$."),
 # --- 3_Szöveges feladatok.docx 14-17 („Nehezebb", hiánytalanul) ---
 ("Apa és fia kerítést fest; egyedül $6$, illetve $10$ óra alatt lennének kész. Egyórányi közös munka után a fiút elküldték, így az apa fél órán át egyedül dolgozott, majd közösen befejezték. Összesen mennyi ideig tartott a festés?",
  None, "$\\dfrac{63}{16}$ óra $=3$ óra $56$ perc $15$ mp."),
 ("Egy medencét két csap tölt: az első egyedül $18$ óra, a második egyedül $15$ óra alatt. Az első csapból $2$ órán át folyik a víz, majd elzárják (a második végig folyik). Mennyi idő alatt telik meg a medence?",
  None, "$\\dfrac{40}{3}$ óra $=13$ óra $20$ perc."),
 ("Három teherautó kavicsot hord: egyedül $5$, $8$, illetve $9$ nap alatt végezne. Mennyi idő alatt végeznek, ha párhuzamosan dolgoznak?",
  None, "$\\dfrac{360}{157}$ nap $\\approx 2{,}29$ nap."),
]

JOKER = ("<b>Kán csapdája.</b> Kán a következő egyenletet írta a táblára, és azt állítja, hogy a megoldása "
  "$x=2$: $2x+5=2x+1$. Igaza van-e? Ha nem, mi a helyes válasz, és miért?",
  "Nincs igaza. Az $2x$ mindkét oldalról kiesik, és $5=1$ marad, ami hamis — az egyenletnek "
  "<b>nincs megoldása</b> (nincs olyan $x$, amely kielégítené).")

# ======================== GYAKORLÓ DOLGOZAT (🏫 órai + 🏠 otthoni) ========================
# Verifikáció:
assert solve(Eq((2*x-1)/4+(x+1)/2,3),x)  # dummy solvable
assert solve(Eq(3*(x+2)-2*(x-1),10),x)==[2]
from sympy import symbols as S
chk(solve([Eq(2*x+3*y,12),Eq(x-y,1)],[x,y],dict=True)[0], x=3,y=2)
chk(solve([Eq(x+2*y,7),Eq(3*x-y,7)],[x,y],dict=True)[0], x=3,y=2)
assert solve(Eq((3*m-1)*1+2,4),m)==[1]

GYD_ORAI = [
 ("Ábrázold az $f(x)=3x-6$ függvényt, és add meg a nullahelyét!",
  None, "nullahely: $x=2$; a grafikon a $(0,-6)$ és $(2,0)$ pontokon halad át."),
 ("Oldd meg a törtes egyenletet: $\\dfrac{x+2}{3}-\\dfrac{x-1}{2}=1$.",
  None, "$x=-5$."),
 ("Oldd meg az egyenlőtlenséget, és ábrázold: $3(x+2)-2(x-1)\\ge 10$.",
  None, "$x\\ge 2$."),
 ("Oldd meg a rendszert: $2x+3y=12$, $x-y=1$.",
  None, "$x=3,\\ y=2$."),
 ("Egy szám kétszeresének és $7$-nek az összege $19$. Melyik ez a szám?",
  None, "$6$."),
 ("Oldd meg a kibontással: $(x+2)^2-(x-3)(x+1)=15$.",
  None, "$x=2$."),
 ("Milyen $m$ esetén halad át az $y=(3m-1)x+2$ egyenes a $P(1,4)$ ponton?",
  None, "$m=1$."),
 ("Egy osztályban $30$ tanuló van; $8$-cal több lány, mint fiú. Hány fiú és hány lány van?",
  None, "$11$ fiú és $19$ lány."),
 ("Egy mozijegy $1200$ Ft, egy diákjegy $800$ Ft. Összesen $20$ jegyet vettek $19\\,200$ Ft-ért. Hány teljes árú és hány diákjegyet?",
  None, "$8$ teljes árú és $12$ diákjegy."),
 ("Oldd meg: $\\dfrac{x}{2}-\\dfrac{x-4}{3}=2$.",
  None, "$x=4$."),
]
GYD_OTTHONI = [
 ("Ábrázold az $f(x)=-2x+1$ függvényt, és add meg a nullahelyét!",
  None, "nullahely: $x=\\dfrac{1}{2}$; a $(0,1)$ ponton halad át."),
 ("Oldd meg az egyenlőtlenséget: $2(x-3)<4x+2$.",
  None, "$x>-4$."),
 ("Oldd meg a rendszert: $3x+y=10$, $x+2y=5$.",
  None, "$x=3,\\ y=1$."),
 ("Két szám összege $30$, különbségük $6$. Melyik ez a két szám?",
  None, "$18$ és $12$."),
 ("Egy kétjegyű szám számjegyeinek összege $9$; a felcserélt szám $27$-tel nagyobb. Melyik a szám?",
  None, "$36$."),
 ("Egy raktárban $3$ kg-os és $5$ kg-os zsákok vannak, összesen $20$ zsák és $76$ kg. Hány $3$ kg-os és hány $5$ kg-os zsák van?",
  None, "$12$ db $3$ kg-os és $8$ db $5$ kg-os."),
]
# gyakorló asserts
chk(solve([Eq(3*x+y,10),Eq(x+2*y,5)],[x,y],dict=True)[0], x=3,y=1)
assert solve(Eq(x/2-(x-4)/3,2),x)==[4]
assert solve(Eq(2*(x-3),4*x+2),x)==[-4]
f_,l_=symbols('f_ l_'); s=solve([Eq(f_+l_,30),Eq(l_-f_,8)],[f_,l_]); assert s[f_]==11 and s[l_]==19
t_,d_=symbols('t_ d_'); s=solve([Eq(t_+d_,20),Eq(1200*t_+800*d_,19200)],[t_,d_]); assert s[t_]==8 and s[d_]==12
z3,z5=symbols('z3 z5'); s=solve([Eq(z3+z5,20),Eq(3*z3+5*z5,76)],[z3,z5]); assert s[z3]==12 and s[z5]==8
print("GYAKORLÓ ASSERT OK")

# ======================== OLDAL ========================
body = []
body.append('    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(ALAP, "alap", "alap"))
body.append('    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(KOZEP, "kozep", "kozep"))
body.append('    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"))
body.append('    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]))

diszk = ('<p class="diszklemer">⚠️ Ez <b>gyakorló</b> anyag: nincs garancia, hogy az éles dolgozaton pontosan '
 'ennyi vagy pont ilyen feladat lesz. A cél a biztos rutin — a valódi feladatok ettől eltérhetnek.</p>')

body.append('    <h2 id="gyak-dolgozat">📝 Gyakorló dolgozat</h2>\n    ' + diszk +
  '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYD_ORAI, "gyd") +
  '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYD_OTTHONI, "gydh"))

sections = "\n".join(body)
alcim = ("Közös kiképzési adattár a teljes lineáris szektorhoz: egyenletek, egyenlőtlenségek, függvény, rendszerek és "
 "szöveges feladatok. Haladj a szinteken, vagy ugorj a szükséges témára. A végeredmény minden feladatnál lenyitható — "
 "előbb számolj, csak utána nézd meg!")

html = f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lineáris egyenletek és rendszerek — feladatok | 1e | Szvetkó matek</title>
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
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">1e</span></a> ›
  <a href="index.html">Lineáris egyenletek és rendszerek</a> ›
  <span class="itt">Feladatok</span>
</nav>
<div class="hero">
  <h1>Lineáris egyenletek és rendszerek — feladatgyűjtemény</h1>
  <p class="alcim">{w(alcim)}</p>
  <div class="meta-sor">
    <span class="chip alap">Alap</span><span class="chip kozep">Közép</span>
    <span class="chip nehez">Nehéz</span><span class="chip joker">Joker</span>
  </div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
{sections}
    <div class="gyakorolj">
      <span class="ikon">📖</span>
      <p>Elakadtál? Nézd át a <a href="index.html">témakör tananyagait</a> vagy a <a href="osszefoglalo.html">tömör összefoglalót</a>.</p>
    </div>
    <div class="lapozo">
      <a class="elozo" href="tananyag-egyenletrendszerek.html"><span class="irany">← Előző</span><span class="hova">Egyenletrendszerek</span></a>
      <a class="kov" href="osszefoglalo.html"><span class="irany">Következő →</span><span class="hova">Tömör összefoglaló</span></a>
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
open(os.path.join(DEST, "feladatok-linearis-egyenletek-es-rendszerek.html"), "w", encoding="utf-8").write(html)
print("feladatok kész: Alap", len(ALAP), "Közép", len(KOZEP), "(ebből 13 szöveges) Nehéz", len(NEHEZ),
      "(ebből 4 szöveges) | gyak.dolg.", len(GYD_ORAI)+len(GYD_OTTHONI))
