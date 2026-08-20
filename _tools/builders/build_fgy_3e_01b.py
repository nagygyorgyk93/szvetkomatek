# -*- coding: utf-8 -*-
"""3e/01 — B altema feladatgyujtemeny: a hasab (fogalom, felszin, terfogat, metszetek)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, sqrt, simplify, N, symbols, solve, Eq, tan, rad
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        ok = abs(float(N(g)) - float(w)) < tol
    elif isinstance(w, (list, tuple)):
        ok = list(g) == list(w)
    else:
        # a különbséget SZÁMSZERŰEN nézzük: a sympy Float(0) == 0 nem mindig igaz,
        # és a python-osztásból (a**2*m/3) float kerülhet a szimbolikus kifejezésbe
        kul = simplify(g - w)
        ok = (kul == 0) or abs(float(N(kul))) < 1e-9
    if not ok:
        E.append((n, g, w))

x = symbols('x', positive=True)
def hasab_B(n, a):
    """Szabályos n-szög alapú hasáb alapterülete."""
    return {3: a**2*sqrt(3)/4, 4: a**2, 6: 6*a**2*sqrt(3)/4}[n]

# --- alap
chk("A3", [5*sqrt(2), 5*sqrt(3)], [sqrt(50), sqrt(75)])
chk("A4", sqrt(12**2 + 9**2 + 8**2), 17)
chk("A6", [12, 18, 8], [2*6, 3*6, 6+2])
B7 = hasab_B(4, 5); chk("A7", [B7, 4*5*8, 2*B7 + 160, B7*8], [25, 160, 210, 200])
B8 = hasab_B(3, 6); chk("A8", [B8, 3*6*10], [9*sqrt(3), 180])
chk("A8-F", 2*B8 + 180, 18*sqrt(3) + 180); chk("A8-V", B8*10, 90*sqrt(3))
B9 = hasab_B(6, 4); chk("A9", [2*B9 + 6*4*9, B9*9], [48*sqrt(3) + 216, 216*sqrt(3)])
chk("A10", [2*(5*4 + 5*3 + 4*3), 5*4*3], [94, 60])
chk("A11", [6*7**2, 7**3], [294, 343])
chk("A12", solve(Eq(6**2*x, 720), x)[0], 20)
chk("A13", [solve(Eq(6*x**2, 150), x)[0], 5**3], [5, 125])
chk("A14", [solve(Eq(x**3, 1000), x)[0], 6*10**2], [10, 600])
chk("A15", [R(32, 10)*1000, R(4500, 1000)], [3200, R(9, 2)])
chk("A16-l", R(80*40*50, 1000), 160)
chk("A16-uveg", R(80*40 + 2*80*50 + 2*40*50, 10000), R(152, 100))
chk("A17", 6*sqrt(2)*10, 60*sqrt(2))
chk("A19", sqrt(6**2 + 8**2)*10, 100)
chk("A20", [2*4*7, 4*sqrt(3)*7], [56, 28*sqrt(3)])
# --- közép
chk("K1", [solve(Eq(x*sqrt(3), 12*sqrt(3)), x)[0], 12*sqrt(2)], [12, sqrt(288)])
chk("K2", solve(Eq(sqrt((3*x)**2 + (4*x)**2 + (12*x)**2), 26), x)[0], 2)
chk("K2-elek", [3*2, 4*2, 12*2], [6, 8, 24])
chk("K3", [solve(Eq(2*6**2 + x**2, 9**2), x)[0], 6**2*3], [3, 108])
chk("K4", [solve(Eq(6*x**2, 216), x)[0], 6*sqrt(3)], [6, sqrt(108)])
B5 = hasab_B(3, 8); chk("K5", [2*B5 + 3*8*5, B5*5], [32*sqrt(3) + 120, 80*sqrt(3)])
chk("K6", solve(Eq(2*4**2 + 4*4*x, 192), x)[0], 10)
chk("K7-a", solve(Eq(6*x*10, 360), x)[0], 6)
chk("K7-V", hasab_B(6, 6)*10, 540*sqrt(3))
chk("K8-a", solve(Eq(x**2*sqrt(3)/4, 49*sqrt(3)), x)[0], 14)
chk("K8-V", 49*sqrt(3)*14, 686*sqrt(3))
chk("K9", [R(2, 3)**2, R(2, 3)**3], [R(4, 9), R(8, 27)])
chk("K10", R((R(14,10) + R(26,10))*25, 2)*10, 500)
chk("K11", N(hasab_B(6, R(3, 10))*3, 4), 0.7014, 1e-3)
chk("K12", R(12, 10)*R(8, 10)*R(5, 10)*1000, 480)
chk("K13", 8*sqrt(2)*6, 48*sqrt(2))
chk("K14", [solve(Eq(x*5, 60), x)[0], 12/sqrt(2)], [12, 6*sqrt(2)])
chk("K15", [2*6*8, 6*sqrt(3)*8], [96, 48*sqrt(3)])
chk("K16", 6*sqrt(2)*6, 36*sqrt(2))
# --- nehéz
chk("N1", 6*sqrt(2)*tan(rad(30)), 2*sqrt(6))
chk("N2", solve(Eq(2*(2*x**2 + 3*x**2 + 6*x**2), 88), x)[0], 2)
chk("N2-V", 2*4*6, 48)
chk("N3", solve(Eq(x**2*sqrt(2), 36*sqrt(2)), x)[0], 6)
chk("N4", solve(Eq(hasab_B(6, x)*4, 216*sqrt(3)), x)[0], 6)
chk("N5", [R(2, 3)**2, R(2, 3)**3], [R(4, 9), R(8, 27)])
chk("J-oldal", 6*sqrt(2)/2, 3*sqrt(2))
chk("J-T", 6*((3*sqrt(2))**2*sqrt(3)/4), 27*sqrt(3))
assert not E, E
print("sympy önteszt: OK")

K = "$ABCDA_1B_1C_1D_1$"

# ============================== ALAP ==============================
ALAP = [
 # --- B1: a hasáb (alap 1–6)
 ("Igaz vagy hamis?",
  ["Minden hasábnak két egybevágó, párhuzamos alaplapja van.",
   "Az egyenes hasáb oldallapjai téglalapok.",
   "A szabályos hasáb minden éle egyenlő.",
   "A ferde hasáb magassága rövidebb, mint az oldaléle.",
   "A kocka szabályos négyoldalú hasáb."],
  ["igaz", "igaz", "hamis (csak az alaplapja szabályos sokszög, a magasság tetszőleges)",
   "igaz", "igaz"], True),

 ("Nevezd meg a testet!",
  ["egyenes hasáb, amelynek az alaplapja négyzet",
   "egyenes hasáb, amelynek minden lapja téglalap",
   "hasáb, amelynek az alaplapja paralelogramma",
   "négyzetes hasáb, amelynek minden éle egyenlő"],
  ["négyzetes (szabályos négyoldalú) hasáb", "téglatest", "paralelepipedon", "kocka"], True),

 ("Egy kocka éle $5$ cm. Mekkora a lapátlója és a testátlója?", None,
  "Lapátló $5\\sqrt2\\approx 7{,}07$ cm, testátló $5\\sqrt3\\approx 8{,}66$ cm."),

 ("Egy téglatest élei $12$ cm, $9$ cm és $8$ cm. Mekkora a testátlója?", None,
  "$D=\\sqrt{12^2+9^2+8^2}=\\sqrt{289}=17$ cm."),

 ("Egy egyenes hasáb hálója két szabályos ötszögből és öt egybevágó téglalapból áll. "
  "Milyen test ez, és hány lapja, éle, csúcsa van?", None,
  "Szabályos ötoldalú hasáb: $7$ lapja, $15$ éle és $10$ csúcsa van."),

 ("Hány csúcsa, éle és lapja van a szabályos hatoldalú hasábnak?", None,
  "$12$ csúcs, $18$ él, $8$ lap."),

 # --- B2: felszín és térfogat (alap 7–16)
 ("Egy négyzetes hasáb alapéle $5$ cm, magassága $8$ cm. Számítsd ki",
  ["az alapterületét", "a palástját", "a felszínét", "a térfogatát"],
  ["$25$ cm²", "$160$ cm²", "$210$ cm²", "$200$ cm³"], True),

 ("Egy szabályos háromoldalú hasáb alapéle $6$ cm, magassága $10$ cm. Mekkora a felszíne "
  "és a térfogata?", None,
  "$F=18\\sqrt3+180\\approx 211{,}18$ cm², $V=90\\sqrt3\\approx 155{,}88$ cm³."),

 ("Egy szabályos hatoldalú hasáb alapéle $4$ cm, magassága $9$ cm. Mekkora a felszíne és a "
  "térfogata?", None,
  "$F=48\\sqrt3+216\\approx 299{,}14$ cm², $V=216\\sqrt3\\approx 374{,}12$ cm³."),

 ("Egy téglatest élei $5$ cm, $4$ cm és $3$ cm. Mekkora a felszíne és a térfogata?", None,
  "$F=94$ cm², $V=60$ cm³."),

 ("Egy kocka éle $7$ cm. Mekkora a felszíne és a térfogata?", None,
  "$F=294$ cm², $V=343$ cm³."),

 ("Egy négyzetes hasáb alapéle $6$ cm, térfogata $720$ cm³. Mekkora a magassága?", None,
  "$m=20$ cm."),

 ("Egy kocka felszíne $150$ cm². Mekkora az éle és a térfogata?", None,
  "$a=5$ cm, $V=125$ cm³."),

 ("Egy kocka térfogata $1000$ cm³. Mekkora az éle és a felszíne?", None,
  "$a=10$ cm, $F=600$ cm²."),

 ("Váltsd át!",
  ["$3{,}2\\ \\text{m}^3$ hány liter?", "$4500\\ \\text{cm}^3$ hány $\\text{dm}^3$?"],
  ["$3200$ liter", "$4{,}5\\ \\text{dm}^3$"], True),

 ("Egy akvárium belső méretei $80$ cm $\\times$ $40$ cm $\\times$ $50$ cm (magas).",
  ["Hány liter víz fér bele, ha színültig töltjük?",
   "Hány négyzetméter üveg kell hozzá, ha felül nyitott?"],
  ["$160$ liter", "$1{,}52\\ \\text{m}^2$ (az alja és négy oldala)"]),

 # --- B3: síkmetszetek (alap 17–20)
 ("Egy négyzetes hasáb alapéle $6$ cm, magassága $10$ cm. Mekkora az átlós metszetének a "
  "területe?", None,
  "$T=60\\sqrt2\\approx 84{,}85$ cm²."),

 ("Milyen alakzat a metszet? Egészítsd ki!",
  ["az egyenes hasáb alaplappal párhuzamos metszete",
   "az egyenes hasáb átlós metszete",
   "a ferde hasáb átlós metszete"],
  ["az alaplappal egybevágó sokszög", "téglalap", "paralelogramma"], True),

 ("Egy téglatest alaplapjának élei $6$ cm és $8$ cm, magassága $10$ cm. Mekkora az átlós "
  "metszetének a területe?", None,
  "Az alaplap átlója $10$ cm, ezért $T=10\\cdot 10=100$ cm²."),

 ("Egy szabályos hatoldalú hasáb alapéle $4$ cm, magassága $7$ cm. Mekkora a <b>kétféle</b> "
  "átlós metszetének a területe?", None,
  "A hosszabb átlóval: $T_1=8\\cdot 7=56$ cm²; a rövidebbel: "
  "$T_2=4\\sqrt3\\cdot 7=28\\sqrt3\\approx 48{,}50$ cm²."),
]

# ============================== KÖZÉP ==============================
KOZEP = [
 # --- B1 (közép 1–4)
 ("Egy kocka testátlója $12\\sqrt3$ cm. Mekkora az éle és a lapátlója?", None,
  "$a=12$ cm, a lapátló $12\\sqrt2\\approx 16{,}97$ cm."),

 ("Egy téglatest éleinek aránya $3:4:12$, a testátlója $26$ cm. Mekkorák az élei?", None,
  "$3x$, $4x$, $12x$ jelöléssel $\\sqrt{(3x)^2+(4x)^2+(12x)^2}=\\sqrt{169x^2}=26$, tehát $x=2$: "
  "az élek $6$ cm, $8$ cm és $24$ cm."),

 ("Egy négyzetes hasáb alapéle $6$ cm, testátlója $9$ cm. Mekkora a magassága és a "
  "térfogata?", None,
  "$D^2=2a^2+m^2$, tehát $81=72+m^2$, ahonnan $m=3$ cm és $V=108$ cm³."),

 ("Egy kocka felszíne $216$ cm². Mekkora az éle és a testátlója?", None,
  "$a=6$ cm, a testátló $6\\sqrt3\\approx 10{,}39$ cm."),

 # --- B2 (közép 5–12)
 ("Egy szabályos háromoldalú hasáb alapéle $8$ cm, magassága $5$ cm. Mekkora a felszíne és "
  "a térfogata?", None,
  "$F=32\\sqrt3+120\\approx 175{,}43$ cm², $V=80\\sqrt3\\approx 138{,}56$ cm³."),

 ("Egy négyzetes hasáb alapéle $4$ cm, felszíne $192$ cm². Mekkora a magassága?", None,
  "$2\\cdot 16+16m=192$, ahonnan $m=10$ cm."),

 ("Egy szabályos hatoldalú hasáb palástja $360$ cm², magassága $10$ cm. Mekkora az alapéle "
  "és a térfogata?", None,
  "$6a\\cdot 10=360$, tehát $a=6$ cm; $V=540\\sqrt3\\approx 935{,}31$ cm³."),

 ("Egy szabályos háromoldalú hasáb <b>minden éle egyenlő</b>, az alapterülete "
  "$49\\sqrt3$ cm². Mekkora a térfogata?", None,
  "$\\frac{a^2\\sqrt3}{4}=49\\sqrt3$, tehát $a=14$ cm, és mivel $m=a$: "
  "$V=686\\sqrt3\\approx 1188{,}19$ cm³."),

 ("Két kocka élének aránya $2:3$. Hogyan aránylik a felszínük és a térfogatuk?", None,
  "A felszínek aránya $4:9$, a térfogatoké $8:27$."),

 ("Egy $25$ m hosszú és $10$ m széles medence mélysége az egyik végén $1{,}4$ m, a másikon "
  "$2{,}6$ m, és egyenletesen változik. Hány köbméter víz fér bele színültig?", None,
  "A keresztmetszet trapéz: $\\frac{(1{,}4+2{,}6)\\cdot 25}{2}=50\\ \\text{m}^2$, "
  "ezért $V=50\\cdot 10=500\\ \\text{m}^3$."),

 ("Egy szabályos hatoldalú hasáb alakú betonoszlop alapéle $30$ cm, magassága $3$ m. "
  "Hány köbméter beton kell hozzá? (Kerekíts két tizedesre.)", None,
  "$a=0{,}3$ m, $B=6\\cdot\\frac{0{,}3^2\\sqrt3}{4}\\approx 0{,}2338\\ \\text{m}^2$, "
  "tehát $V\\approx 0{,}70\\ \\text{m}^3$."),

 ("Egy láda belső méretei $1{,}2$ m $\\times$ $0{,}8$ m $\\times$ $0{,}5$ m. Hány liter fér bele?",
  None, "$V=0{,}48\\ \\text{m}^3=480$ liter."),

 # --- B3 (közép 13–16)
 ("Egy négyzetes hasáb alapéle $8$ cm, magassága $6$ cm. Mekkora az átlós metszetének a "
  "területe?", None,
  "$T=8\\sqrt2\\cdot 6=48\\sqrt2\\approx 67{,}88$ cm²."),

 ("Egy négyzetes hasáb átlós metszetének területe $60$ cm², a magassága $5$ cm. Mekkora az "
  "alaplap átlója és az alapéle?", None,
  "Az átló $12$ cm, az alapél $\\frac{12}{\\sqrt2}=6\\sqrt2\\approx 8{,}49$ cm."),

 ("Egy szabályos hatoldalú hasáb alapéle $6$ cm, magassága $8$ cm. Mekkora a kétféle átlós "
  "metszetének területe?", None,
  "$T_1=12\\cdot 8=96$ cm², $T_2=6\\sqrt3\\cdot 8=48\\sqrt3\\approx 83{,}14$ cm²."),

 ("Egy kocka éle $6$ cm. Mekkora az átlós metszetének a területe?", None,
  "$T=6\\sqrt2\\cdot 6=36\\sqrt2\\approx 50{,}91$ cm²."),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 ("Egy négyzetes hasáb alapéle $6$ cm, és a testátlója $30^\\circ$-os szöget zár be az "
  "alaplappal. Mekkora a magassága?", None,
  "$m=6\\sqrt2\\cdot\\operatorname{tg}30^\\circ=2\\sqrt6\\approx 4{,}90$ cm."),

 ("Egy téglatest éleinek aránya $1:2:3$, a felszíne $88$ cm². Mekkorák az élei, és mekkora "
  "a térfogata?", None,
  "$2(2x^2+3x^2+6x^2)=88$, tehát $x=2$: az élek $2$, $4$ és $6$ cm, a térfogat $48$ cm³."),

 ("Egy kocka átlós metszetének területe $36\\sqrt2$ cm². Mekkora az éle?", None,
  "$a^2\\sqrt2=36\\sqrt2$, tehát $a=6$ cm."),

 ("Egy szabályos hatoldalú hasáb térfogata $216\\sqrt3$ cm³, magassága $4$ cm. Mekkora az "
  "alapéle?", None,
  "$\\frac{6a^2\\sqrt3}{4}\\cdot 4=216\\sqrt3$, ahonnan $a=6$ cm."),

 ("Két hasonló hasáb megfelelő éleinek aránya $2:3$. Hogyan aránylik a felszínük és a "
  "térfogatuk? Indokold!", None,
  "A felszínek aránya $4:9$ (a terület a hosszak négyzetével), a térfogatoké $8:27$ "
  "(a köbével)."),
]

JOKER = ("Egy $6$ cm élű kockát elmetszünk azzal a síkkal, amely hat élt a "
         "<b>felezőpontjában</b> döf. Milyen alakzat a metszet, és mekkora a területe?",
         "A metszet <b>szabályos hatszög</b>, oldala két szomszédos élfelezőpont távolsága, "
         "azaz $\\frac{6\\sqrt2}{2}=3\\sqrt2$ cm. Területe "
         "$6\\cdot\\frac{(3\\sqrt2)^2\\sqrt3}{4}=27\\sqrt3\\approx 46{,}77$ cm².")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="01-poliederek", fajl="feladatok-hasab.html",
           cim="A hasáb", temakor="Poliéderek",
           alcim="A hasáb fajtái, átlói, felszíne és térfogata, fordított feladatok, "
                 "mértékegységek és síkmetszetek. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-hasab-sikmetszetek.html", prevc="A hasáb síkmetszetei",
           nxt="tananyag-gula.html", nxtc="A gúla és elemei")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
