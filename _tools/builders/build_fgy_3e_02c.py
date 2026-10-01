# -*- coding: utf-8 -*-
"""3e/02 — C altema feladatgyujtemeny: a gomb es az osszetett testek."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, sqrt, pi, simplify, N, symbols, solve, Eq
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        ok = abs(float(N(g)) - float(w)) < tol
    elif isinstance(w, (list, tuple)):
        ok = list(g) == list(w)
    else:
        kul = simplify(g - w)
        ok = (kul == 0) or abs(float(N(kul))) < 1e-9
    if not ok:
        E.append((n, g, w))

x, Rg = symbols('x R', positive=True)
F_g = lambda RR: 4*RR**2*pi
V_g = lambda RR: R(4, 3)*RR**3*pi
V_h = lambda rr, HH: rr**2*pi*HH
V_k = lambda rr, HH: rr**2*pi*HH/3
M_h = lambda rr, HH: 2*rr*pi*HH

# --- C1 (alap 1–6, közép 1–3)
chk("a1", R(18, 2), 9)
chk("a4", 7**2*pi, 49*pi)
chk("k2", R(26, 2), 13)
chk("n-metszet", sqrt(15**2 - 9**2), 12)
# --- C2 (alap 7–16, közép 4–11)
chk("a7-F", F_g(6), 144*pi);            chk("a7-V", V_g(6), 288*pi)
chk("a8-F", F_g(3), 36*pi);             chk("a8-V", V_g(3), 36*pi)
chk("a9-F", F_g(5), 100*pi);            chk("a9-V", V_g(5), R(500, 3)*pi)
chk("a10", V_g(R(12, 2)), 288*pi)
chk("a11", solve(Eq(F_g(x), 64*pi), x)[0], 4)
chk("a12", solve(Eq(F_g(x), 196*pi), x)[0], 7)
chk("a13", solve(Eq(V_g(x), 36*pi), x)[0], 3)
chk("a14", solve(Eq(V_g(x), 972*pi), x)[0], 9)
chk("a15-F", F_g(11), 484*pi);          chk("a15-kozelites", N(F_g(11), 9), 1520.53084, 1e-4)
chk("a16-V", V_g(10), R(4000, 3)*pi);   chk("a16-liter", N(V_g(10)/1000, 9), 4.18879020, 1e-7)
chk("k4-F", F_g(2*Rg)/F_g(Rg), 4);      chk("k4-V", V_g(2*Rg)/V_g(Rg), 8)
chk("k5-F", F_g(2)/F_g(3), R(4, 9));    chk("k5-V", V_g(2)/V_g(3), R(8, 27))
chk("k6", solve(Eq(F_g(x*Rg), 4*F_g(Rg)), x)[0], 2)
chk("k7", solve(Eq(V_g(x*Rg), 8*V_g(Rg)), x)[0], 2)
chk("k8", V_g(Rg)/V_h(Rg, 2*Rg), R(2, 3))
chk("k9-h", V_h(6, 12), 432*pi);        chk("k9-g", V_g(6), 288*pi)
chk("k9-arany", V_g(6)/V_h(6, 12), R(2, 3))
chk("k10-V", V_g(3), 36*pi);            chk("k10-m", N(V_g(3)*R(785, 100), 9), 887.814084, 1e-5)
chk("k11", solve(Eq(F_g(x), V_g(x)), x)[0], 3)
# --- C3 (alap 17–22, közép 12–17)
chk("a17", V_h(3, 4) + V_g(3)/2, 54*pi)
chk("a18", V_h(4, 10) - V_h(3, 10), 70*pi)
chk("a19", V_k(3, 4) + V_h(3, 6), 66*pi)
chk("a20", M_h(5, 12) + F_g(5)/2, 170*pi)
chk("a21", V_h(6, 10) - V_h(2, 10), 320*pi)
chk("a22", V_h(2, 10) + V_k(2, 3), 44*pi)
chk("k12", V_h(6, 10) + V_g(6)/2, 504*pi)
chk("k13", M_h(6, 10) + F_g(6)/2, 192*pi)
chk("k14-V", V_h(6, 10) - V_h(5, 10), 110*pi)
chk("k14-F", 2*(6**2 - 5**2)*pi + M_h(6, 10) + M_h(5, 10), 242*pi)
chk("k15-H", sqrt(10**2 - 6**2), 8)
chk("k15-V", V_k(6, 8) + V_h(1, 8), 104*pi)
chk("k16-g", V_g(3), 36*pi);            chk("k16-h", V_h(2, 4), 16*pi)
chk("k17-V", V_g(3), 36*pi)
chk("k17-szazalek", N((216 - V_g(3))/216*100, 9), 47.6401225, 1e-6)
# --- nehéz
chk("n1", (2*Rg)**3/V_g(Rg), 6/pi)
chk("n2", solve(Eq(V_h(5, x), V_g(3)), x)[0], R(144, 100))
chk("n3-F", N((F_g(25)/F_g(20) - 1)*100, 9), 56.25, 1e-7)
chk("n3-V", N((V_g(25)/V_g(20) - 1)*100, 9), 95.3125, 1e-7)
chk("n4-V", V_g(4), R(256, 3)*pi)
chk("n4-liter", N(V_g(4)*1000, 9), 268082.573, 1e-2)
chk("joker", F_g(Rg)/(2*Rg**2*pi + M_h(Rg, 2*Rg)), R(2, 3))
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- C1: a gömb (alap 1–6)
 ("Egy gömb átmérője $18$ cm. Mekkora a sugara?", None,
  "A sugár az átmérő fele: $R=9$ cm. (A képletekbe mindig a <b>sugár</b> megy.)"),

 ("Egy gömb sugara $10$ cm. Milyen helyzetben van a gömbfelülethez képest az a sík, "
  "amely a középponttól", ["$6$ cm-re", "$10$ cm-re", "$12$ cm-re van?"],
  ['metszi: a metszet kör',
   'érinti: egy közös pont',
   'elkerüli: nincs közös pont'], True),

 ("Mit nevezünk a gömb <b>főkörének</b>, és mekkora a sugara?", None,
  'A középponton átmenő sík és a gömbfelület metszete; sugara $R$.'),

 ("Egy gömb sugara $7$ cm. Milyen síkidomot kapunk, ha a <b>középponton átmenő</b> síkkal "
  "metsszük el, és mekkora ennek a területe?", None,
  '$7$ cm sugarú körlap; területe $49\\pi$ cm².'),

 ("Hány közös pontja van egy gömbfelületnek és az <b>érintősíkjának</b>, és milyen "
  "szöget zár be a sík az érintési pontba húzott sugárral?", None,
  "Pontosan <b>egy</b> közös pontjuk van, és az érintősík <b>merőleges</b> az érintési "
  "pontba húzott sugárra ($90^\\circ$)."),

 ("Igaz vagy hamis?", 
  ["A gömbfelület minden pontja ugyanolyan messze van a középponttól.",
   "A gömb (test) minden pontja ugyanolyan messze van a középponttól.",
   "A gömbfelületnek van olyan síkmetszete, amely nem kör."],
  ['igaz',
   'hamis',
   'igaz'], True),

 # --- C2: felszín és térfogat (alap 7–16)
 ("Egy gömb sugara $6$ cm. Számítsd ki a felszínét és a térfogatát!", None,
  "$F=4R^2\\pi=144\\pi\\ \\text{cm}^2$, "
  "$V=\\frac{4R^3\\pi}{3}=\\frac{864\\pi}{3}=288\\pi\\ \\text{cm}^3$."),

 ("Egy gömb sugara $3$ cm. Mekkora a felszíne és a térfogata?", None,
  '$F=36\\pi$ cm²; $V=36\\pi$ cm³.'),

 ("Egy gömb sugara $5$ cm. Mekkora a felszíne és a térfogata?", None,
  "$F=100\\pi\\ \\text{cm}^2$, $V=\\frac{4\\cdot125\\pi}{3}="
  "\\frac{500\\pi}{3}\\ \\text{cm}^3$."),

 ("Egy gömb <b>átmérője</b> $12$ cm. Mekkora a térfogata?", None,
  "Előbb a sugár: $R=6$ cm. Ezután $V=\\frac{4\\cdot216\\pi}{3}=288\\pi\\ \\text{cm}^3$."),

 ("Egy gömb felszíne $64\\pi\\ \\text{cm}^2$. Mekkora a sugara?", None,
  '$R=4$ cm.'),

 ("Egy gömb felszíne $196\\pi\\ \\text{cm}^2$. Mekkora a sugara?", None,
  '$R=7$ cm.'),

 ("Egy gömb térfogata $36\\pi\\ \\text{cm}^3$. Mekkora a sugara?", None,
  '$R=3$ cm.'),

 ("Egy gömb térfogata $972\\pi\\ \\text{cm}^3$. Mekkora a sugara?", None,
  '$R=9$ cm.'),

 ("Egy focilabda átmérője $22$ cm. Mekkora a felszíne? (Két tizedesre kerekítve.)", None,
  '$F=484\\pi\\approx1520{,}53$ cm².'),

 ("Egy gömb alakú tartály sugara $10$ cm. Hány <b>liter</b> fér bele? (Két tizedesre "
  "kerekítve.)", None,
  "$V=\\frac{4000\\pi}{3}\\approx4188{,}79\\ \\text{cm}^3$, ami körülbelül "
  "$4{,}19$ liter."),

 # --- C3: összetett és üreges testek (alap 17–22)
 ("Egy hengeres tartály ($r=3$ cm, $H=4$ cm) tetején <b>félgömb</b> van, amelynek a "
  "sugara a hengerével egyenlő. Mekkora a test térfogata?", None,
  '$V=54\\pi$ cm³.'),

 ("Egy $10$ cm hosszú cső külső sugara $4$ cm, belső sugara $3$ cm. Mekkora az anyag "
  "térfogata?", None,
  "$V=16\\pi\\cdot10-9\\pi\\cdot10=160\\pi-90\\pi=70\\pi\\ \\text{cm}^3$."),

 ("Egy hengerre ($r=3$ cm, $H=6$ cm) kúp alakú tetőt teszünk ($r=3$ cm, $H=4$ cm). "
  "Mekkora a keletkező test térfogata?", None,
  '$V=66\\pi$ cm³.'),

 ("Egy hengeres oszlop ($r=5$ cm, $H=12$ cm) tetején félgömb van, amelynek a sugara a "
  "hengerével egyenlő. Mekkora a <b>külső</b> felülete, ha az alsó körlapot nem "
  "számítjuk?", None,
  '$F=170\\pi$ cm².'),

 ("Egy $6$ cm sugarú, $10$ cm magas hengerből kifúrunk egy $2$ cm sugarú, végig "
  "átmenő hengeres lyukat. Mekkora a megmaradó test térfogata?", None,
  "$V=36\\pi\\cdot10-4\\pi\\cdot10=360\\pi-40\\pi=320\\pi\\ \\text{cm}^3$."),

 ("Egy gyertya hengeres törzsből ($r=2$ cm, $H=10$ cm) és a tetején egy kúpból "
  "($r=2$ cm, $H=3$ cm) áll. Mekkora a térfogata?", None,
  "$V=4\\pi\\cdot10+\\frac{4\\pi\\cdot3}{3}=40\\pi+4\\pi=44\\pi\\ \\text{cm}^3$."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- C1 (közép 1–3)
 ("Egy gömb sugara $15$ cm. Milyen távolságra lehet a középponttól egy sík, ha",
  ["érinti a gömbfelületet", "metszi", "elkerüli"],
  ["$d=15$ cm (pontosan a sugárral egyenlő)", "$0\\le d&lt;15$ cm (a $d=0$ eset a főkör)",
   "$d&gt;15$ cm"], True),

 ("Egy gömb <b>átmérője</b> $26$ cm, egy sík a középponttól $13$ cm-re halad. Milyen "
  "helyzetben van a sík és a gömbfelület?", None,
  'Érinti; egy közös pontjuk van.'),

 ("Egy sík érinti a gömbfelületet. Mit tudunk mondani az érintési pontba húzott "
  "sugárról, és mi ennek a síkbeli megfelelője?", None,
  "Az érintősík <b>merőleges</b> az érintési pontba húzott sugárra. A síkbeli "
  "megfelelője: a kör érintője merőleges az érintési pontba húzott sugárra."),

 # --- C2 (közép 4–11)
 ("Egy gömb sugarát <b>megduplázzuk</b>. Hányszorosára nő a felszíne és a térfogata?", None,
  'A felszíne a négyszeresére, a térfogata a nyolcszorosára nő.'),

 ("Két gömb sugarának aránya $2:3$. Hogyan aránylik a felszínük és a térfogatuk?", None,
  "A felszínek aránya $2^2:3^2=4:9$, a térfogatoké $2^3:3^3=8:27$."),

 ("Egy gömb felszíne a <b>négyszeresére</b> nő. Hányszorosára nő a sugara?", None,
  'A sugár a kétszeresére nő.'),

 ("Egy gömb térfogata a <b>nyolcszorosára</b> nő. Hányszorosára nő a felszíne?", None,
  'A felszín a négyszeresére nő.'),

 ("Egy gömb és a köré írt henger térfogatának aránya — vezesd le általánosan!", None,
  "A köré írt henger alapköre a főkör ($r=R$), a magassága az átmérő ($H=2R$), ezért "
  "$V_{\\text{henger}}=R^2\\pi\\cdot2R=2R^3\\pi$. A gömbé "
  "$\\frac{4R^3\\pi}{3}$, tehát az arány "
  "$\\frac{4R^3\\pi/3}{2R^3\\pi}=\\frac23$ — ez Arkhimédész $2:3$ aránya."),

 ("Egy gömb sugara $6$ cm. Mekkora a köré írt henger térfogata, és mekkora a gömbé?", None,
  '$V_{\\text{henger}}=432\\pi$ cm³; $V_{\\text{gömb}}=288\\pi$ cm³.'),

 ("Mekkora egy $3$ cm sugarú acélgolyó tömege, ha az acél sűrűsége "
  "$7{,}85\\ \\text{g/cm}^3$? (Két tizedesre kerekítve.)", None,
  '$m\\approx887{,}81$ g.'),

 ("Egy gömb felszínének és térfogatának a <b>számértéke</b> megegyezik. Mekkora a "
  "sugara?", None,
  '$R=3$.'),

 # --- C3 (közép 12–17)
 ("Egy víztorony tartálya hengerből ($r=6$ m, $H=10$ m) és a rá épített, azonos sugarú "
  "félgömb tetőből áll. Mekkora a teljes térfogata?", None,
  '$V=504\\pi$ m³.'),

 ("Egy víztorony tartálya hengerből ($r=6$ m, $H=10$ m) és azonos sugarú félgömb tetőből "
  "áll. Mekkora a <b>külső</b> felülete, ha az alsó körlapot nem festik?", None,
  '$F=192\\pi$ m².'),

 ("Egy mindkét végén nyitott cső hossza $10$ cm, külső sugara $6$ cm, belső sugara "
  "$5$ cm. Mekkora", ["az anyag térfogata", "a teljes felszíne"],
  ['$V=110\\pi$ cm³',
   '$F=242\\pi$ cm²'], True),

 ("Egy tömör dísztárgy kúp alakú részből (alapkör sugara $6$ cm, alkotója $10$ cm) és "
  "egy hozzáillesztett hengeres nyélből ($r=1$ cm, $H=8$ cm) áll. Mekkora a két rész "
  "térfogatának <b>összege</b>?", None,
  '$V=104\\pi$ cm³.'),

 ("Melyikbe fér több: egy $3$ m sugarú <b>gömb</b> alakú tartályba, vagy egy $2$ m "
  "sugarú, $4$ m magas <b>hengeres</b> tartályba?", None,
  'A gömbbe: $36\\pi$ m³, szemben a henger $16\\pi$ m³-ével.'),

 ("Egy $6$ cm élű fakockából kiesztergáljuk a lehető legnagyobb gömböt. Hány "
  "<b>százalék</b> a hulladék? (Két tizedesre kerekítve.)", None,
  '$47{,}64\\,\\%$.'),
]

# ============================== NEHÉZ SZINT ==============================
NEHEZ = [
 ("Egy gömb <b>köré</b> írunk egy kockát (a kocka lapjai érintik a gömböt). Hogyan "
  "aránylik a kocka és a gömb térfogata? (A számértéket két tizedesre kerekítve "
  "add meg!)", None,
  '$V_{\\text{kocka}}:V_{\\text{gömb}}=\\dfrac6\\pi\\approx1{,}91$.'),

 ("Egy $5$ cm sugarú hengeres pohárban víz van. Beleteszünk egy $3$ cm sugarú gömböt, "
  "amely teljesen elmerül. Hány centimétert emelkedik a vízszint?", None,
  '$1{,}44$ cm-rel.'),

 ("Egy gömb alakú léggömb sugara $20$ cm-ről $25$ cm-re nő. Hány <b>százalékkal</b> nő "
  "a felszíne és a térfogata? (Két tizedesre kerekítve.)", None,
  'A felszín $56{,}25\\,\\%$-kal, a térfogat $95{,}31\\,\\%$-kal nő.'),

 ("Egy víztorony gömb alakú tartályának <b>átmérője</b> $8$ m. Hány liter víz fér "
  "bele? (Egészre kerekítve.)", None,
  '$268\\,083$ liter.'),
]

JOKER = ("Arkhimédész szerint a gömb és a köré írt henger térfogatának aránya $2:3$. "
         "Igazold, hogy a <b>felszínükre</b> is ugyanez az arány igaz!",
         "A köré írt henger alapköre a gömb főköre ($r=R$), a magassága az átmérő "
         "($H=2R$).</p>"
         "<p>$$F_{\\text{henger}}=2R^2\\pi+2R\\pi\\cdot2R=2R^2\\pi+4R^2\\pi=6R^2\\pi,"
         "\\qquad F_{\\text{gömb}}=4R^2\\pi.$$</p>"
         "<p>Az arány tehát $\\frac{4R^2\\pi}{6R^2\\pi}=\\frac23$ — ugyanaz, mint a "
         "térfogatoknál.</p>"
         "<p>Ez a kettős egybeesés tette a tételt Arkhimédész kedvencévé: a "
         "hagyomány szerint ezért vésette a hengerbe írt gömböt a sírkövére. Sőt, "
         "még többről van szó: a gömb <b>felszíne</b> pontosan egyenlő a köré írt henger "
         "<b>palástjával</b> ($4R^2\\pi$) — mintha a gömbfelületet rá lehetne teríteni "
         "a hengerre.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="02-forgastestek", fajl="feladatok-gomb.html",
           cim="A gömb és az összetett testek", temakor="Forgástestek",
           alcim="A gömbfelület és a sík kölcsönös helyzete, a gömb felszíne és "
                 "térfogata, valamint az összetett és üreges testek. A végeredmény "
                 "pontos alakban áll ($\\pi$-vel); közelítést csak ott adunk, ahol a "
                 "feladat kéri. A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-osszetett-testek.html", prevc="Összetett és üreges testek",
           nxt="osszefoglalo.html", nxtc="Összefoglaló")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
