# -*- coding: utf-8 -*-
"""3e/01 — C altema feladatgyujtemeny: a gula, a metszetek es a csonkagula."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, sqrt, simplify, N, symbols, solve, Eq
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

def alap_B(n, a):
    return {3: a**2*sqrt(3)/4, 4: a**2, 6: 6*a**2*sqrt(3)/4}[n]
def alap_rho(n, a):
    return {3: a*sqrt(3)/6, 4: R(1, 2)*a, 6: a*sqrt(3)/2}[n]
def alap_R(n, a):
    return {3: a*sqrt(3)/3, 4: a*sqrt(2)/2, 6: a}[n]
def gula_mo(n, a, m):
    return sqrt(m**2 + alap_rho(n, a)**2)
def gula_M(n, a, mo):
    return n*a*mo/2
def gula_V(n, a, m):
    return alap_B(n, a)*m/3

# --- C1
chk("A2-3", [3+1, 2*3, 3+1], [4, 6, 4])
chk("A2-4", [4+1, 2*4, 4+1], [5, 8, 5])
chk("A2-6", [6+1, 2*6, 6+1], [7, 12, 7])
chk("A3-rho", alap_rho(4, 8), 4)
chk("A3-mo", gula_mo(4, 8, 3), 5)
chk("A4-b", sqrt(4**2 + 3**2), 5)
chk("A5", 1 if alap_rho(4, 6) < alap_R(4, 6) else 0, 1)
# --- C2
chk("A6", [alap_B(4, 6), gula_M(4, 6, 5), alap_B(4, 6) + gula_M(4, 6, 5)], [36, 60, 96])
chk("A7", gula_V(4, 6, 4), 48)
chk("A8", [alap_B(3, 6), gula_M(3, 6, 8)], [9*sqrt(3), 72])
chk("A9", [alap_B(6, 4), gula_M(6, 4, 6)], [24*sqrt(3), 72])
chk("A10", R(48*9, 3), 144)
chk("A11", solve(Eq(R(25, 3)*x, 100), x)[0], 12)
chk("A12", 3, 3)
chk("A13", [alap_rho(4, 10), gula_mo(4, 10, 12), gula_M(4, 10, 13),
            alap_B(4, 10) + gula_M(4, 10, 13), gula_V(4, 10, 12)],
     [5, 13, 260, 360, 400])
chk("A14", [alap_B(3, 8), gula_M(3, 8, 10)], [16*sqrt(3), 120])
chk("A15", 6**2*5 + R(6**2*4, 3), 228)
# --- C3
chk("A16", R(1, 2)**2*64, 16)
chk("A17-T", R(1, 3)**2*81, 9)
chk("A17-V", R(1, 3)**3*54, 2)
chk("A18", solve(Eq(x*12, 4), x)[0], R(1, 3))
# --- C4
chk("A21", [8**2, 4**2, 4*(8+4)/2*6], [64, 16, 144])
chk("A21-F", 64 + 16 + 144, 224)
chk("A22-m", sqrt(5**2 - 3**2), 4)
chk("A22-V", R(4, 3)*(144 + 36 + sqrt(144*36)), 336)
chk("A22-F", 144 + 36 + 4*(12+6)/2*5, 360)
chk("A23", solve(Eq(x/3*(25 + 9 + 15), 98), x)[0], 6)
chk("A24", [R((8 + 5)*4, 2), 6*R((8 + 5)*4, 2)], [26, 156])
chk("A25", R(12, 3)*(100 + 256 + sqrt(100*256)), 2064)
chk("A25-liter", R(2064, 1000), 2.064, 1e-9)
# --- KÖZÉP
chk("K1", solve(Eq(gula_mo(4, x, 4), 5), x)[0], 6)
chk("K2", solve(Eq(gula_V(4, 6, x), 60), x)[0], 5)
chk("K3", [gula_mo(4, 16, 6), gula_M(4, 16, 10), alap_B(4, 16) + gula_M(4, 16, 10)],
     [10, 320, 576])
chk("K4", solve(Eq(alap_B(4, x)*9/3, 300), x)[0], 10)
chk("K5-mo", gula_mo(6, 6, sqrt(11)), sqrt(11 + 27))
chk("K6", [alap_B(3, 12), gula_V(3, 12, 5)], [36*sqrt(3), 60*sqrt(3)])
chk("K7", solve(Eq(4*x*13/2, 260), x)[0], 10)
chk("K8", R(1, 2)**3, R(1, 8))
chk("K9-mo", sqrt(12**2 + 5**2), 13)
chk("K10", [R(2, 3)**2, R(2, 3)**3], [R(4, 9), R(8, 27)])
chk("K11", R(1, 2)**3*216, 27)
chk("K12", solve(Eq(x**2*36, 4), x)[0], R(1, 3))
chk("K13", 100 - R(1, 8)*100, R(700, 8))
chk("K14-m", sqrt(13**2 - 5**2), 12)
chk("K15", [4*(14+8)/2*8, 14**2 + 8**2 + 352], [352, 612])
chk("K16-m", sqrt(10**2 - 6**2), 8)
chk("K16-V", R(8, 3)*(400 + 64 + sqrt(400*64)), R(8, 3)*624)
chk("K17", solve(Eq(4*(10 + x)/2*6, 216), x)[0], 8)
chk("K18", R(6, 3)*(49 + 25 + 35), 218)
chk("K19", [9*R(4, 3), 9*4], [12, 36])
chk("K20", [alap_rho(6, 8), gula_mo(6, 8, 8)], [4*sqrt(3), sqrt(64 + 48)])
chk("K21", R(12, 3)*(64 + 16 + 32), 448)
# --- NEHÉZ
chk("N1", solve(Eq(sqrt(x**2 + alap_rho(4, 12)**2), 10), x)[0], 8)
chk("N1-F", alap_B(4, 12) + gula_M(4, 12, 10), 384)
chk("N2", solve(Eq(64*x**3, 512), x)[0], 2)
chk("N3", [alap_B(4, 6), gula_mo(4, 6, 4)], [36, 5])
chk("N4-k", solve(Eq(x**2*144, 36), x)[0], R(1, 2))
chk("N5", solve(Eq(x/3*(100 + 36 + sqrt(100*36)), 392), x)[0], 6)
chk("N6", [R(1, 2)**2, 1 - R(1, 2)**3], [R(1, 4), R(7, 8)])
chk("J-mo", sqrt(6**2 + 6**2), 6*sqrt(2))
chk("J-F", 12**2 + 4*(12*6*sqrt(2))/2, 144 + 144*sqrt(2))
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAP ==============================
ALAP = [
 # --- C1: a gúla elemei (alap 1–5)
 ("Igaz vagy hamis?",
  ["A gúla minden oldallapja háromszög.",
   "A szabályos gúla magasságának talppontja az alaplap középpontja.",
   "A szabályos gúla oldalélei egyenlők.",
   "Az oldallap magassága hosszabb, mint az oldalél.",
   "Minden háromoldalú gúla szabályos tetraéder."],
  ["igaz", "igaz", "igaz", "hamis (fordítva: $h &lt; b$)",
   "hamis (csak az, amelyiknek mind a hat éle egyenlő)"], True),

 ("Hány csúcsa, éle és lapja van?",
  ["háromoldalú gúla", "négyoldalú gúla", "hatoldalú gúla"],
  ["$4$ csúcs, $6$ él, $4$ lap", "$5$ csúcs, $8$ él, $5$ lap",
   "$7$ csúcs, $12$ él, $7$ lap"], True),

 ("Egy szabályos négyoldalú gúla alapéle $8$ cm, a <b>test</b> magassága $3$ cm. Mekkora",
  ["az alaplap apotémája", "az oldallap magassága"],
  ["$4$ cm", "$5$ cm"], True),

 ("Egy szabályos négyoldalú gúla alapéle $6$ cm, az oldallap magassága $4$ cm. Mekkora az "
  "oldaléle?", None,
  "$b=\\sqrt{h^2+\\left(\\frac a2\\right)^2}=\\sqrt{16+9}=5$ cm."),

 ("Melyik hosszabb a szabályos gúlában: az oldalél vagy az oldallap magassága? Indokold!",
  None,
  "Az <b>oldalél</b>. Mindkettő ugyanabból a magasságból indul, de az oldalél az alaplap "
  "csúcsáig fut ($R$), az oldallap magassága csak az él felezőpontjáig ($r$), és "
  "$r &lt; R$."),

 # --- C2: felszín és térfogat (alap 6–15)
 ("Egy szabályos négyoldalú gúla alapéle $6$ cm, az oldallap magassága $5$ cm. Számítsd ki",
  ["az alapterületet", "a palástot", "a felszínt"],
  ["$36$ cm²", "$60$ cm²", "$96$ cm²"], True),

 ("Egy szabályos négyoldalú gúla alapéle $6$ cm, magassága $4$ cm. Mekkora a térfogata?",
  None, "$V=\\frac{36\\cdot 4}{3}=48$ cm³."),

 ("Egy szabályos háromoldalú gúla alapéle $6$ cm, az oldallap magassága $8$ cm. Mekkora a "
  "felszíne?", None,
  "$B=9\\sqrt3$ cm², $M=72$ cm², tehát $F=9\\sqrt3+72\\approx 87{,}59$ cm²."),

 ("Egy szabályos hatoldalú gúla alapéle $4$ cm, az oldallap magassága $6$ cm. Mekkora a "
  "felszíne?", None,
  "$B=24\\sqrt3$ cm², $M=72$ cm², tehát $F=24\\sqrt3+72\\approx 113{,}57$ cm²."),

 ("Egy gúla alapterülete $48$ cm², magassága $9$ cm. Mekkora a térfogata?", None,
  "$V=\\frac{48\\cdot 9}{3}=144$ cm³."),

 ("Egy gúla alapterülete $25$ cm², térfogata $100$ cm³. Mekkora a magassága?", None,
  "$H=\\frac{3V}{B}=\\frac{300}{25}=12$ cm."),

 ("Egy hasáb és egy gúla alapterülete és magassága is egyenlő. Hányszorosa a hasáb "
  "térfogata a gúláénak?", None,
  "Háromszorosa."),

 ("Egy szabályos négyoldalú gúla alapéle $10$ cm, magassága $12$ cm. Számítsd ki",
  ["az alaplap apotémáját", "az oldallap magasságát", "a palástot", "a felszínt",
   "a térfogatot"],
  ["$5$ cm", "$13$ cm", "$260$ cm²", "$360$ cm²", "$400$ cm³"], True),

 ("Egy szabályos háromoldalú gúla alapéle $8$ cm, az oldallap magassága $10$ cm. Mekkora a "
  "palástja és a felszíne?", None,
  "$M=120$ cm², $B=16\\sqrt3$ cm², tehát $F=16\\sqrt3+120\\approx 147{,}71$ cm²."),

 ("Egy torony alsó része $6$ m alapélű, $5$ m magas négyzetes hasáb; a teteje a hasáb "
  "fedőlapjára illeszkedő, $4$ m magas szabályos négyoldalú gúla. Mekkora a torony "
  "térfogata?", None,
  "$V=180+48=228\\ \\text{m}^3$."),

 # --- C3: metszetek (alap 16–19)
 ("Egy gúla alapterülete $64$ cm². Elmetsszük az alaplappal párhuzamos síkkal, "
  "<b>félmagasságban</b>. Mekkora a metszet területe?", None,
  "$T=\\left(\\frac12\\right)^2\\cdot 64=16$ cm²."),

 ("Egy gúla alapterülete $81$ cm², térfogata $54$ cm³. A csúcstól a magasság harmadánál "
  "metsszük el az alaplappal párhuzamosan. Mekkora",
  ["a metszet területe", "a levágott kis gúla térfogata"],
  ["$9$ cm²", "$2$ cm³"], True),

 ("Egy szabályos négyoldalú gúla alapéle $12$ cm. Az alaplappal párhuzamos metszet oldala "
  "$4$ cm. Mekkora a <b>metszet és az alaplap</b> hasonlósági aránya?", None,
  "$k=\\frac{4}{12}=\\frac13$ — a metszet tehát a magasság harmadánál van (a csúcstól mérve)."),

 ("Mi lesz a metszet, ha a szabályos négyoldalú gúlát",
  ["az alaplappal párhuzamos síkkal metsszük",
   "két szemközti oldalélen átmenő síkkal metsszük"],
  ["az alaplaphoz hasonló négyzet", "egyenlő szárú háromszög (tengelymetszet)"], True),

 # --- C4: csonkagúla (alap 20–26)
 ("Egészítsd ki!",
  ["A csonkagúla oldallapjai …", "A csonkagúla alaplapja és fedőlapja …",
   "A csonkagúla magassága …"],
  ["trapézok", "párhuzamos és egymáshoz hasonló sokszög",
   "a két lap síkjának távolsága"], True),

 ("Egy szabályos négyoldalú csonkagúla alapélei $8$ cm és $4$ cm, az oldallap magassága "
  "$6$ cm. Számítsd ki",
  ["az alaplap és a fedőlap területét", "a palástot", "a felszínt"],
  ["$64$ cm² és $16$ cm²", "$144$ cm²", "$224$ cm²"], True),

 ("Egy szabályos négyoldalú csonkagúla alapélei $12$ cm és $6$ cm, az oldallap magassága "
  "$5$ cm. Mekkora",
  ["a test magassága", "a felszíne", "a térfogata"],
  ["$4$ cm", "$360$ cm²", "$336$ cm³"], True),

 ("Egy csonkagúla alaplapja $25$ cm², fedőlapja $9$ cm², térfogata $98$ cm³. Mekkora a "
  "magassága?", None,
  "$\\sqrt{B_1B_2}=15$, ezért $\\frac{H}{3}\\cdot 49=98$, ahonnan $H=6$ cm."),

 ("Mekkora egy szabályos <b>hatoldalú</b> csonkagúla <b>egyetlen</b> oldallapjának a "
  "területe, ha az alapélek $8$ cm és $5$ cm, az oldallap magassága pedig $4$ cm? És mekkora "
  "az egész palást?", None,
  "Egy trapéz területe $\\frac{(8+5)\\cdot 4}{2}=26$ cm², a palást pedig "
  "$6\\cdot 26=156$ cm²."),

 ("Egy virágcserép csonkagúla alakú, lefelé szűkül: az alja $10$ cm oldalú, a felső "
  "pereme $16$ cm oldalú négyzet, a magassága $12$ cm. Hány liter föld fér bele, ha a "
  "peremig töltjük? (Kerekíts egy tizedesre.)", None,
  "$V=\\frac{12}{3}(100+256+160)=2064\\ \\text{cm}^3\\approx 2{,}1$ liter."),

 ("Melyik képlet melyik testé? Párosítsd!",
  ["$V=B\\,H$", "$V=\\frac{B\\,H}{3}$",
   "$V=\\frac{H}{3}\\left(B_1+B_2+\\sqrt{B_1B_2}\\right)$"],
  ["hasáb", "gúla", "csonkagúla"], True),
]

# ============================== KÖZÉP ==============================
KOZEP = [
 # --- C1 (közép 1–4)
 ("Egy szabályos négyoldalú gúla <b>testmagassága</b> $4$ cm, az <b>oldallap</b> magassága "
  "$5$ cm. Mekkora az alapéle?", None,
  "Az apotéma $r=\\sqrt{5^2-4^2}=3$ cm, tehát $a=2r=6$ cm."),

 ("Egy szabályos négyoldalú gúla alapéle $6$ cm, térfogata $60$ cm³. Mekkora a magassága?",
  None, "$H=\\frac{3V}{B}=\\frac{180}{36}=5$ cm."),

 ("Egy szabályos négyoldalú gúla alapéle $16$ cm, magassága $6$ cm. Számítsd ki",
  ["az oldallap magasságát", "a palástot", "a felszínt"],
  ["$10$ cm", "$320$ cm²", "$576$ cm²"], True),

 ("Egy szabályos négyoldalú gúla magassága $9$ cm, térfogata $300$ cm³. Mekkora az alapéle?",
  None, "$B=\\frac{3V}{H}=100$ cm², tehát $a=10$ cm."),

 # --- C2 (közép 5–12)
 ("Egy szabályos hatoldalú gúla alapéle $4$ cm, magassága $2$ cm. Számítsd ki",
  ["az oldallap magasságát", "a felszínét", "a térfogatát"],
  ["$4$ cm (mert $r=2\\sqrt3$)", "$24\\sqrt3+48\\approx 89{,}57$ cm²",
   "$16\\sqrt3\\approx 27{,}71$ cm³"], True),

 ("Egy szabályos háromoldalú gúla alapéle $12$ cm, magassága $5$ cm. Mekkora az "
  "alapterülete és a térfogata?", None,
  "$B=36\\sqrt3\\approx 62{,}35$ cm², $V=60\\sqrt3\\approx 103{,}92$ cm³."),

 ("Egy szabályos négyoldalú gúla palástja $260$ cm², az oldallap magassága $13$ cm. Mekkora "
  "az alapéle?", None,
  "$M=\\frac{4a\\cdot 13}{2}=26a=260$, tehát $a=10$ cm."),

 ("Egy gúlát az alaplappal párhuzamosan, félmagasságban elmetszünk. A levágott kis gúla "
  "térfogata hányadrésze az eredetinek?", None,
  "$\\left(\\frac12\\right)^3=\\frac18$-a."),

 ("Egy szabályos négyoldalú gúla magassága $12$ cm, az alaplap apotémája $5$ cm. Mekkora az "
  "oldallap magassága és az alapél?", None,
  "$h=\\sqrt{144+25}=13$ cm, $a=2r=10$ cm."),

 ("Két hasonló gúla megfelelő éleinek aránya $2:3$. Hogyan aránylik a felszínük és a "
  "térfogatuk?", None,
  "A felszínek aránya $4:9$, a térfogatoké $8:27$."),

 ("Egy gúla térfogata $216$ cm³. Félmagasságban elmetsszük az alaplappal párhuzamosan. "
  "Mekkora a levágott <b>kis gúla</b> térfogata?", None,
  "$\\left(\\frac12\\right)^3\\cdot 216=27$ cm³."),

 ("Egy gúla alapterülete $36$ cm², az alaplappal párhuzamos metszet területe $4$ cm². "
  "Mekkora a <b>metszet és az alaplap</b> hasonlósági aránya?", None,
  "$k^2=\\frac{4}{36}$, tehát $k=\\frac13$."),

 # --- C3 (közép 13–15)
 ("Egy gúla térfogata $100$ cm³. Félmagasságban elmetsszük az alaplappal párhuzamosan. "
  "Mekkora az <b>alsó</b> darab (a csonkagúla) térfogata?", None,
  "A felső kis gúla $\\frac18\\cdot 100=12{,}5$ cm³, tehát az alsó darab "
  "$100-12{,}5=87{,}5$ cm³."),

 ("Egy szabályos négyoldalú gúla oldaléle $13$ cm, az alaplap köréírt sugara $5$ cm. "
  "Mekkora a magassága?", None,
  "$H=\\sqrt{13^2-5^2}=12$ cm."),

 ("Egy szabályos négyoldalú csonkagúla alapélei $14$ cm és $8$ cm, az oldallap magassága "
  "$8$ cm. Mekkora a palástja és a felszíne?", None,
  "$M=4\\cdot\\frac{(14+8)\\cdot 8}{2}=352$ cm², $F=196+64+352=612$ cm²."),

 # --- C4 (közép 16–21)
 ("Egy szabályos négyoldalú csonkagúla alapélei $20$ cm és $8$ cm, az oldallap magassága "
  "$10$ cm. Mekkora a test magassága és a térfogata?", None,
  "$H=\\sqrt{10^2-6^2}=8$ cm; $V=\\frac83(400+64+160)=1664$ cm³."),

 ("Egy szabályos négyoldalú csonkagúla <b>palástja</b> $216$ cm², az alaplapjának éle "
  "$10$ cm, az oldallap magassága $6$ cm. Mekkora a fedőlap éle?", None,
  "$M=4\\cdot\\frac{(10+a_2)\\cdot 6}{2}=12(10+a_2)=216$, ahonnan $a_2=8$ cm."),

 ("Egy csonkagúla alaplapja $49$ cm², fedőlapja $25$ cm², magassága $6$ cm. Mekkora a "
  "térfogata?", None,
  "$\\sqrt{B_1B_2}=35$, ezért $V=\\frac63(49+25+35)=218$ cm³."),

 ("Egy gúla alapterülete $9$ cm², magassága $4$ cm. Mekkora a térfogata? És mekkora annak "
  "a hasábnak a térfogata, amelynek ugyanez az alaplapja és a magassága?", None,
  "A gúláé $V=\\frac{9\\cdot 4}{3}=12$ cm³, a hasábé $9\\cdot 4=36$ cm³ — háromszor annyi."),

 ("Egy szabályos hatoldalú gúla alapéle $8$ cm, magassága $8$ cm. Mekkora az alaplap "
  "apotémája és az oldallap magassága?", None,
  "$r=4\\sqrt3\\approx 6{,}93$ cm, $h=\\sqrt{64+48}=4\\sqrt7\\approx 10{,}58$ cm."),

 ("Egy szabályos négyoldalú csonkagúla alapélei $8$ cm és $4$ cm, a magassága $12$ cm. "
  "Mekkora a térfogata?", None,
  "$V=\\frac{12}{3}(64+16+32)=448$ cm³."),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 ("Egy szabályos négyoldalú gúla alapéle $12$ cm, az oldallap magassága $10$ cm. Mekkora a "
  "test magassága és a felszíne?", None,
  "$H=\\sqrt{10^2-6^2}=8$ cm; $F=144+240=384$ cm²."),

 ("Két hasonló gúla térfogata $512$ cm³ és $64$ cm³. Hogyan aránylanak a megfelelő éleik?",
  None,
  "A térfogatok aránya $8:1$, tehát az élek aránya $\\sqrt[3]{8}:1=2:1$."),

 ("Egy szabályos négyoldalú gúla <b>oldaléleken átmenő</b> tengelymetszete szabályos "
  "háromszög. Az alapél $8$ cm. Mekkora a gúla magassága?", None,
  "A tengelymetszet alapja az alaplap átlója, $8\\sqrt2$; mivel szabályos háromszög, az "
  "oldalél is $8\\sqrt2$. A köréírt sugár $R=4\\sqrt2$, ezért "
  "$H=\\sqrt{128-32}=4\\sqrt6\\approx 9{,}80$ cm."),

 ("Egy gúla alapterülete $144$ cm². Milyen magasságban (a csúcstól mérve, a magasság "
  "hányadánál) kell elmetszeni, hogy a metszet területe $36$ cm² legyen?", None,
  "$k^2\\cdot 144=36$, tehát $k=\\frac12$: a magasság felénél."),

 ("Egy szabályos négyoldalú csonkagúla alapélei $10$ cm és $6$ cm, a térfogata "
  "$392$ cm³. Mekkora a magassága?", None,
  "$\\sqrt{B_1B_2}=\\sqrt{100\\cdot 36}=60$, ezért $\\frac{H}{3}(100+36+60)=392$, "
  "vagyis $\\frac{H}{3}\\cdot 196=392$, ahonnan $H=6$ cm."),

 ("Egy gúlát félmagasságban elmetszünk az alaplappal párhuzamosan. Az eredeti gúla "
  "alapterülete $B$, térfogata $V$. Fejezd ki ezekkel",
  ["a metszet területét", "az alsó darab (csonkagúla) térfogatát"],
  ["$\\frac{B}{4}$", "$\\frac{7V}{8}$"], True),
]

JOKER = ("Egy szabályos négyoldalú gúla oldallapjai $45^\\circ$-os szöget zárnak be az "
         "alaplappal, az alapél $12$ cm. Mekkora a felszíne?",
         "Ha az oldallap hajlásszöge $45^\\circ$, akkor $H=r=6$ cm, tehát "
         "$h=6\\sqrt2$ cm. Így $M=\\frac{48\\cdot 6\\sqrt2}{2}=144\\sqrt2$ és "
         "$F=144+144\\sqrt2\\approx 347{,}65$ cm².")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="01-poliederek", fajl="feladatok-gula.html",
           cim="A gúla és a csonkagúla", temakor="Poliéderek",
           alcim="A gúla elemei és a három derékszögű háromszög, felszín és térfogat, "
                 "az alaplappal párhuzamos metszet, valamint a csonkagúla. "
                 "Ahol az eredmény irracionális, a kulcs a pontos alakot és a két tizedesre "
                 "kerekített közelítést is megadja. A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-csonkagula.html", prevc="A csonkagúla",
           nxt="index.html", nxtc="Poliéderek — témakör")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
