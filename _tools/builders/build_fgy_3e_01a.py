# -*- coding: utf-8 -*-
"""3e/01 — A altema feladatgyujtemeny: terelemek, merolegesseg, poliederek, alaplap."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (Rational as R, sqrt, simplify, N, atan, acos, deg, pi, symbols,
                   solve, Eq, Matrix)
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

a, x = symbols('a x', positive=True)

# --- kocka és téglatest átlók, szögek
chk("A7-lap", sqrt(6**2 + 6**2), 6*sqrt(2))
chk("A7-test", sqrt((6*sqrt(2))**2 + 6**2), 6*sqrt(3))
chk("A8", sqrt(6**2 + 8**2 + 24**2), 26)
chk("A9", deg(atan(1/sqrt(2))), deg(atan(sqrt(2)/2)))
chk("A9-fok", N(deg(atan(sqrt(2)/2))), 35.26438968, 1e-6)
chk("K4", N(deg(atan(R(12, 5)))), 67.38013505, 1e-6)
chk("K5", N(deg(atan(sqrt(2)))), 54.73561032, 1e-6)
chk("K6", N(deg(atan(R(2, 3)))), 33.69006753, 1e-6)
chk("K7", 10*sqrt(3)/2, 5*sqrt(3))
# --- kockabeli élpárok
chk("N1-osszes", R(12*11, 2), 66)
chk("N1-parhuzamos", 3*R(4*3, 2), 18)
chk("N1-metszo", 8*3, 24)
chk("N1-kitero", 66 - 18 - 24, 24)
# --- lapátlók szöge (szabályos háromszög)
chk("N3", deg(acos(R(1, 2))), 60)
# --- csúcs/él/lap
for n_, cs, el, la in [(4, 8, 12, 6), (6, 12, 18, 8), (3, 6, 9, 5)]:
    chk(f"hasab{n_}", [2*n_, 3*n_, n_+2], [cs, el, la])
    chk(f"euler-hasab{n_}", 2*n_ - 3*n_ + (n_+2), 2)
for n_, cs, el, la in [(4, 5, 8, 5), (6, 7, 12, 7), (3, 4, 6, 4)]:
    chk(f"gula{n_}", [n_+1, 2*n_, n_+1], [cs, el, la])
    chk(f"euler-gula{n_}", (n_+1) - 2*n_ + (n_+1), 2)
chk("K10", solve(Eq(3*x, 21), x)[0], 7)
chk("oktaeder", [6, 12, 8], [6, 12, 8])
# --- síkidomok
chk("A16-m", 8*sqrt(3)/2, 4*sqrt(3))
chk("A16-T", 8**2*sqrt(3)/4, 16*sqrt(3))
chk("A17-atlo", sqrt(5**2 + 5**2), 5*sqrt(2))
chk("A17-teglalap", sqrt(6**2 + 8**2), 10)
chk("A18", R((12 + 8)*5, 2), 50)
chk("A19-T", R(16*12, 2), 96)
chk("A19-oldal", sqrt(8**2 + 6**2), 10)
chk("A20-T", 6*(6**2*sqrt(3)/4), 54*sqrt(3))
chk("A20-rho", 6*sqrt(3)/2, 3*sqrt(3))
chk("A21-30", [R(12, 2), 12*sqrt(3)/2], [6, 6*sqrt(3)])
chk("A21-45", 7*sqrt(2), sqrt(7**2 + 7**2))
chk("A22", solve(Eq(x**2*sqrt(3)/4, 25*sqrt(3)), x)[0], 10)
chk("K11", solve(Eq(3*x**2*sqrt(3)/2, 96*sqrt(3)), x)[0], 8)
chk("K12-m", sqrt(5**2 - 4**2), 3)
chk("K12-T", R((14 + 6)*3, 2), 30)
chk("K13-a", solve(Eq(x*sqrt(3)/2, 6*sqrt(3)), x)[0], 12)
chk("K13-T", 12**2*sqrt(3)/4, 36*sqrt(3))
chk("K14-atlo", 2*sqrt(13**2 - 12**2), 10)
chk("K14-T", R(24*10, 2), 120)
chk("N4", (pi*(a*sqrt(3)/2)**2) / (pi*a**2), R(3, 4))
chk("J", sqrt(2)*a/2, a*sqrt(2)/2)
# --- kockabeli kölcsönös helyzetek (vektorosan)
KOCKA = dict(A=(0,0,0), B=(1,0,0), C=(1,1,0), D=(0,1,0),
             A1=(0,0,1), B1=(1,0,1), C1=(1,1,1), D1=(0,1,1))
def helyzet(e1, e2):
    u = Matrix(KOCKA[e1[1]]) - Matrix(KOCKA[e1[0]])
    v = Matrix(KOCKA[e2[1]]) - Matrix(KOCKA[e2[0]])
    w = Matrix(KOCKA[e2[0]]) - Matrix(KOCKA[e1[0]])
    if u.cross(v).norm() == 0:
        return "parhuzamos"
    return "metszo" if Matrix([[*u], [*v], [*w]]).det() == 0 else "kitero"
for par, vart in [((("A","B"),("C1","D1")), "parhuzamos"),
                  ((("A","B"),("C","C1")), "kitero"),
                  ((("B","C"),("A1","D1")), "parhuzamos"),
                  ((("A","B"),("A","D")), "metszo"),
                  ((("A","B"),("D","D1")), "kitero"),
                  ((("A","B"),("B1","C1")), "kitero"),
                  ((("A","B"),("A1","D1")), "kitero")]:
    g = helyzet(*par)
    if g != vart:
        E.append((str(par), g, vart))
# az AB-vel kitérő élek száma
ELEK = [("A","B"),("B","C"),("C","D"),("D","A"),("A1","B1"),("B1","C1"),("C1","D1"),
        ("D1","A1"),("A","A1"),("B","B1"),("C","C1"),("D","D1")]
kit = [e for e in ELEK if e != ("A","B") and helyzet(("A","B"), e) == "kitero"]
chk("A2-kitero-db", len(kit), 4)
assert not E, E
print("sympy önteszt: OK")

K = "$ABCDA_1B_1C_1D_1$"

# ============================== ALAP ==============================
ALAP = [
 # --- A1: térelemek (alap 1–5)
 (f"Az ábrázolt kocka csúcsai {K} (az $A_1$ az $A$ fölött, a $B_1$ a $B$ fölött, és így "
  "tovább). Igaz vagy hamis?",
  ["Az $AB$ és a $C_1D_1$ él párhuzamos.",
   "Az $AB$ és a $CC_1$ él metsző.",
   "Az $AA_1$ él merőleges az $ABCD$ lapra.",
   "A $BC$ és az $A_1D_1$ él kitérő.",
   "Az $ABCD$ és az $A_1B_1C_1D_1$ lap párhuzamos."],
  ["igaz", "hamis (kitérő)", "igaz", "hamis (párhuzamos)", "igaz"], True),

 (f"Sorold fel az {K} kocka összes olyan élét, amely az $AB$ éllel <b>kitérő</b>! "
  "Hány ilyen él van?",
  None,
  "$CC_1$, $DD_1$, $A_1D_1$, $B_1C_1$ — összesen $4$ él."),

 ("Hány sík fektethető át a következő alakzatokon?",
  ["két metsző egyenesen", "két párhuzamos, nem egybeeső egyenesen",
   "egy egyenesen", "három, egy egyenesre eső ponton", "két kitérő egyenesen"],
  ["pontosan egy", "pontosan egy", "végtelen sok", "végtelen sok", "egy sem"], True),

 ("Melyik adat határoz meg <b>egyértelműen</b> egy síkot? Döntsd el mindegyikről!",
  ["három pont", "három, nem egy egyenesre eső pont",
   "egy egyenes és egy rá nem illeszkedő pont", "két kitérő egyenes"],
  ["nem (ha egy egyenesre esnek, végtelen sok sík megy át rajtuk)", "igen",
   "igen", "nem (nincs ilyen sík)"], True),

 ("Nézz körül a teremben! Nevezz meg egy-egy példát a következőkre. (Több jó válasz is van.)",
  ["két párhuzamos sík", "két metsző sík és a metszésvonaluk",
   "két kitérő egyenes", "egy síkot döfő egyenes"],
  ["a padló és a mennyezet; vagy két szemközti fal",
   "a fal és a padló — a metszésvonaluk a szegélyléc vonala",
   "az ajtófélfa függőleges éle és a padló egy vele nem egy síkban lévő éle",
   "a lámpa felfüggesztő rúdja döfi a mennyezet síkját"]),

 # --- A2: merőlegesség és szögek (alap 6–10)
 (f"Az {K} kockában mely élek merőlegesek az $ABCD$ alaplapra? És mely lapok merőlegesek rá?",
  None,
  "Élek: $AA_1$, $BB_1$, $CC_1$, $DD_1$. Lapok: mind a négy oldallap "
  "($ABB_1A_1$, $BCC_1B_1$, $CDD_1C_1$, $DAA_1D_1$)."),

 ("Egy kocka éle $6$ cm. Számítsd ki",
  ["a lapátlóját", "a testátlóját"],
  ["$6\\sqrt2\\approx 8{,}49$ cm", "$6\\sqrt3\\approx 10{,}39$ cm"], True),

 ("Egy téglatest élei $6$ cm, $8$ cm és $24$ cm. Mekkora a testátlója?", None,
  "$D=\\sqrt{6^2+8^2+24^2}=\\sqrt{676}=26$ cm."),

 ("Egy $3$ m hosszú létrát a falnak támasztunk; a talajjal $60^\\circ$-os szöget zár be. "
  "Milyen magasan éri a falat, és milyen messze van a talpa a faltól?", None,
  "Magasság: $3\\sin 60^\\circ=\\frac{3\\sqrt3}{2}\\approx 2{,}60$ m; távolság: "
  "$3\\cos 60^\\circ=1{,}5$ m."),

 ("Egy $8$ cm élű kocka középpontja mekkora távolságra van",
  ["az egyik lapjától", "az egyik csúcsától"],
  ["$4$ cm", "$4\\sqrt3\\approx 6{,}93$ cm (a testátló fele)"], True),

 # --- A3: poliéderek (alap 11–15)
 ("Hány csúcsa, éle és lapja van a következő testeknek?",
  ["négyzetes hasáb", "szabályos hatoldalú hasáb", "négyoldalú gúla", "hatoldalú gúla"],
  ["$8$ csúcs, $12$ él, $6$ lap", "$12$ csúcs, $18$ él, $8$ lap",
   "$5$ csúcs, $8$ él, $5$ lap", "$7$ csúcs, $12$ él, $7$ lap"], True),

 ("Egy hasáb alaplapja $n$ oldalú sokszög. Fejezd ki $n$-nel a csúcsok, az élek és a "
  "lapok számát!", None,
  "Csúcs: $2n$, él: $3n$, lap: $n+2$."),

 ("Melyik test <b>poliéder</b>? Válaszd ki!",
  ["kocka", "henger", "gúla", "gömb", "csonkagúla"],
  ["igen", "nem (a palástja görbült, a két alaplapja kör)", "igen",
   "nem (a felülete végig görbült)", "igen"], True),

 ("Nevezd meg az öt szabályos poliédert, és add meg, milyen sokszög a lapjuk!", None,
  "Tetraéder (szabályos háromszög), kocka (négyzet), oktaéder (szabályos háromszög), "
  "dodekaéder (szabályos ötszög), ikozaéder (szabályos háromszög)."),

 ("Konvex-e a test? Indokold röviden!",
  ["kocka", "L alakú épülettömb (L alaplapú hasáb)", "szabályos négyoldalú gúla"],
  ["igen", "nem — a két szár végpontját összekötő szakasz kilép a testből", "igen"], True),

 # --- A4: az alaplap (alap 16–22)
 ("Egy egyenlő oldalú háromszög oldala $8$ cm. Számítsd ki",
  ["a magasságát", "a területét"],
  ["$4\\sqrt3\\approx 6{,}93$ cm", "$16\\sqrt3\\approx 27{,}71$ cm²"], True),

 ("Számítsd ki!",
  ["Egy négyzet oldala $5$ cm — mekkora az átlója és a területe?",
   "Egy téglalap oldalai $6$ cm és $8$ cm — mekkora az átlója és a területe?"],
  ["átló $5\\sqrt2\\approx 7{,}07$ cm, terület $25$ cm²",
   "átló $10$ cm, terület $48$ cm²"]),

 ("Egy trapéz párhuzamos oldalai $12$ cm és $8$ cm, magassága $5$ cm. Mekkora a területe?",
  None, "$T=\\frac{(12+8)\\cdot 5}{2}=50$ cm²."),

 ("Egy rombusz átlói $16$ cm és $12$ cm. Mekkora",
  ["a területe", "az oldala"],
  ["$96$ cm²", "$10$ cm (a fél átlókból: $\\sqrt{8^2+6^2}$)"], True),

 ("Egy szabályos hatszög oldala $6$ cm. Számítsd ki",
  ["a területét", "az apotémáját (a beírt kör sugarát)"],
  ["$54\\sqrt3\\approx 93{,}53$ cm²", "$3\\sqrt3\\approx 5{,}20$ cm"], True),

 ("Számítsd ki a hiányzó adatokat!",
  ["Egy derékszögű háromszög átfogója $12$ cm, egyik szöge $30^\\circ$. Mekkorák a befogói?",
   "Egy derékszögű háromszög mindkét befogója $7$ cm. Mekkora az átfogója?"],
  ["$6$ cm és $6\\sqrt3\\approx 10{,}39$ cm",
   "$7\\sqrt2\\approx 9{,}90$ cm"]),

 ("Egy egyenlő oldalú háromszög területe $25\\sqrt3$ cm². Mekkora az oldala?", None,
  "$a=10$ cm."),
]

# ============================== KÖZÉP ==============================
KOZEP = [
 # --- A1 (közép 1–3)
 (f"Az {K} kockában hányféle <b>kölcsönös helyzetben</b> lehet két él? Számold meg azt is, hány "
  "élpár <b>metsző</b>, hány <b>párhuzamos</b> és hány <b>kitérő</b>! (A kockának $12$ éle van.)",
  None,
  "Háromféle helyzet lehetséges: metsző, párhuzamos, kitérő. Összesen $\\binom{12}{2}=66$ élpár. Párhuzamos: $3$ irány, mindegyikben $4$ él, "
  "azaz $3\\cdot\\binom{4}{2}=18$ pár. Metsző: minden csúcsban $3$ él fut össze, "
  "$8\\cdot\\binom{3}{2}=24$ pár. Kitérő: $66-18-24=24$ pár."),

 ("Legyen $a$, $b$ és $c$ három <b>páronként különböző</b> egyenes a térben. Igaz vagy "
  "hamis? Indokold!",
  ["Ha $a\\parallel b$ és $b\\parallel c$, akkor $a\\parallel c$.",
   "Ha $a\\perp b$ és $b\\perp c$, akkor $a\\perp c$.",
   "Ha két egyenesnek nincs közös pontja, akkor párhuzamosak."],
  ["igaz", "hamis — a térben $a$ és $c$ lehet párhuzamos, kitérő, sőt tetszőleges szögben metsző is",
   "hamis — kitérők is lehetnek"]),

 ("Adott két kitérő egyenes, $e$ és $f$. Hány olyan sík van, amely tartalmazza az $e$-t "
  "és párhuzamos az $f$-fel?", None,
  "Pontosan egy."),

 # --- A2 (közép 4–7)
 ("Egy téglatest alaplapjának élei $3$ cm és $4$ cm, a magassága $12$ cm. Mekkora szöget "
  "zár be a testátló az alaplappal?", None,
  "$\\varphi\\approx 67{,}38^\\circ$."),

 ("Mekkora szöget zár be a kocka testátlója az egyik <b>élével</b>? (Mutasd meg, hogy "
  "mindegy, melyik élt választjuk!)", None,
  "$\\approx 54{,}74^\\circ$ — a testátló mindhárom élirányra ugyanúgy áll, mert "
  "$\\cos\\varphi=\\frac{a}{a\\sqrt3}=\\frac{1}{\\sqrt3}$."),

 ("Egy $2$ m magas oszlop árnyéka $3$ m hosszú. Mekkora szöget zárnak be a napsugarak a "
  "vízszintes talajjal?", None,
  "$\\approx 33{,}69^\\circ$."),

 ("Két sík $60^\\circ$-os szöget zár be. Az egyik síkban felveszünk egy pontot, amely a "
  "metszésvonaltól $10$ cm-re van. Milyen messze van ez a pont a másik síktól?", None,
  "$5\\sqrt3\\approx 8{,}66$ cm."),

 # --- A3 (közép 8–10)
 ("Egy gúla alaplapja $n$ oldalú sokszög. Fejezd ki $n$-nel a csúcsok, az élek és a lapok "
  "számát! Ellenőrizd a négyoldalú gúlán!", None,
  "Csúcs: $n+1$, él: $2n$, lap: $n+1$. Négyoldalú gúlára: $5$, $8$, $5$."),

 ("Egy hasábnak $21$ éle van. Hány oldalú az alaplapja, és hány lapja van a testnek?",
  None, "$3n=21$, tehát $n=7$: hétoldalú hasáb, $9$ lapja van."),

 ("Egy szabályos oktaédernek hány csúcsa, éle és lapja van? Hány lap találkozik egy "
  "csúcsában?", None,
  "$6$ csúcs, $12$ él, $8$ lap; egy csúcsban $4$ lap találkozik."),

 # --- A4 (közép 11–14)
 ("Egy szabályos hatszög területe $96\\sqrt3$ cm². Mekkora az oldala?", None,
  "$a=8$ cm."),

 ("Egy egyenlő szárú trapéz párhuzamos oldalai $14$ cm és $6$ cm, a szárai $5$ cm-esek. "
  "Mekkora a magassága és a területe?", None,
  "A szár vetülete $\\frac{14-6}{2}=4$ cm, ezért $H=\\sqrt{5^2-4^2}=3$ cm és $T=30$ cm²."),

 ("Egy egyenlő oldalú háromszög magassága $6\\sqrt3$ cm. Mekkora az oldala és a területe?",
  None, "$a=12$ cm, $T=36\\sqrt3\\approx 62{,}35$ cm²."),

 ("Egy rombusz oldala $13$ cm, egyik átlója $24$ cm. Mekkora a másik átlója és a területe?",
  None, "A másik átló $10$ cm, a terület $120$ cm²."),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 ("Adott két kitérő egyenes, $e$ és $f$. Mutasd meg, hogy van olyan <b>síkpár</b>, "
  "amelynek egyik síkja az $e$-t, másik síkja az $f$-et tartalmazza, és a két sík "
  "párhuzamos!", None,
  "Az $e$ egy pontján át húzzuk meg az $f$-fel párhuzamos $f'$ egyenest: az $e$ és az "
  "$f'$ két metsző egyenes, tehát meghatároznak egy $S$ síkot. Az $f$ nem fekszik "
  "$S$-ben, mert akkor $e$ és $f$ egy síkba esne, vagyis nem lennének kitérők — így "
  "$f\\parallel S$. Ugyanígy az $f$ egy pontján át kapjuk az $e$-vel párhuzamos "
  "egyenest és vele az $S'$ síkot. Az $S$ és az $S'$ ugyanannak a két iránynak a "
  "síkja, ezért párhuzamosak."),

 (f"Az {K} kockában mekkora szöget zár be az $AB_1$ és a $B_1C$ lapátló?", None,
  "$60^\\circ$ — az $AB_1C$ háromszög mindhárom oldala lapátló, tehát egyenlő oldalú."),

 ("Egy szabályos hatszög beírt és köréírt körének területe hogyan aránylik egymáshoz?",
  None, "$3:4$."),

 ("Egy szabályos négyoldalú hasáb alapéle $a$, magassága $H$. Fejezd ki $a$-val és $H$-mel "
  "a testátló $D$ hosszát! Számítsd ki $a=5$ cm és $H=12$ cm esetén, majd fordítva: "
  "mekkora $H$, ha $a=6$ cm és $D=11$ cm?", None,
  "$D=\\sqrt{2a^2+H^2}$; behelyettesítve $\\sqrt{50+144}=\\sqrt{194}\\approx 13{,}93$ cm. "
  "Visszafelé: $\\sqrt{72+H^2}=11$, ahonnan $H^2=49$, tehát $H=7$ cm."),
]

JOKER = ("Egy $a$ élű kocka <b>lapközéppontjai</b> egy szabályos oktaéder csúcsai. "
         "Mekkora ennek az oktaédernek az éle?",
         "Két szomszédos lapközéppontot összekötő szakasz olyan derékszögű háromszög "
         "átfogója, amelynek mindkét befogója $\\frac{a}{2}$, ezért az oktaéder éle "
         "$\\sqrt{\\left(\\frac a2\\right)^2+\\left(\\frac a2\\right)^2}="
         "\\frac{a\\sqrt2}{2}\\approx 0{,}71a$.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="01-poliederek", fajl="feladatok-terelemek.html",
           cim="Térelemek és poliéderek", temakor="Poliéderek",
           alcim="Pont, egyenes és sík a térben, merőlegesség és szögek, a poliéderek "
                 "fogalma, valamint az alaplapok területe. A szögeket két tizedesjegyre "
                 "kerekítve add meg. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-alaplap.html", prevc="Az alaplap",
           nxt="tananyag-hasab.html", nxtc="A hasáb")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
