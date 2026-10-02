# -*- coding: utf-8 -*-
"""2e/04 — D altema feladatgyujtemeny: szinusz- es koszinusztetel, haromszog megoldasa,
terulet es alkalmazasok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, pi, sqrt, sin, cos, tan, asin, acos, rad, deg, N
E = []
def chk(n, g, w, tol=6e-3):
    if abs(float(g) - w) > tol:
        E.append((n, float(g), w))
def asa(sz, o, m, h):
    return o*sin(rad(m))/sin(rad(sz)), o*sin(rad(h))/sin(rad(sz))
def sas(u, v, g):
    w = sqrt(u**2 + v**2 - 2*u*v*cos(rad(g)))
    return w, deg(asin(min(u, v)*sin(rad(g))/w))
a1 = asa(50, 10, 60, 70); chk("A1b", a1[0], 11.30516); chk("A1c", a1[1], 12.26682)
a2 = sas(9, 12, 40);      chk("A2a", a2[0], 7.715854); chk("A2sz", a2[1], 48.570)
chk("A3", deg(acos(R(5**2 + 6**2 - 7**2, 2*5*6))), 78.463)
chk("A4T", R(1, 2)*10*14*sin(rad(40)), 44.99513)
chk("A5T", R(1, 2)*7*9*sin(rad(120)), 27.27980)
k1 = asa(35, 20, 80, 65); chk("K1b", k1[0], 34.33920); chk("K1c", k1[1], 31.60199)
k2 = sas(15, 8, 105);     chk("K2a", k2[0], 18.73810); chk("K2sz", k2[1], 24.355)
chk("K3a", deg(acos(R(8**2 + 11**2 - 15**2, 2*8*11))), 103.14)
chk("K3b", deg(acos(R(11**2 + 15**2 - 8**2, 2*11*15))), 31.290)
chk("K3c", deg(acos(R(8**2 + 15**2 - 11**2, 2*8*15))), 45.573)
chk("K4R", 12/(2*sin(rad(35))), 10.46068)
chk("K5", deg(asin(10*sin(rad(40))/7)), 66.674)
BT = 60*sin(rad(28))/sin(rad(15))
chk("K6BT", BT, 108.8339); chk("K6h", BT*sin(rad(43)), 74.22456)
chk("K7", sqrt(25**2 + 35**2 - 2*25*35*cos(rad(70))), 35.37605)
chk("N1", 9*6*sin(rad(50)), 41.36640)
chk("N2", sqrt(21*8*7*6), 84.0)
chk("N3", deg(acos(R(2**2 + 3**2 - 4**2, 2*2*3))), 104.48)
chk("J", sqrt(8**2 + 5**2 - 2*8*5*cos(rad(120))), 11.35782)
assert not E, E
print("sympy önteszt: OK")

KER = ("A szögfüggvények értékeit öt tizedesre, a hosszakat két tizedesre kerekítsd!")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Írd fel a szinusztételt és a koszinusztételt fejből!", None,
  "Szinusztétel: $\\dfrac{a}{\\sin\\alpha}=\\dfrac{b}{\\sin\\beta}="
  "\\dfrac{c}{\\sin\\gamma}=2R$. &nbsp; Koszinusztétel: "
  "$a^{2}=b^{2}+c^{2}-2bc\\cos\\alpha$."),
 ("Melyik tételt használnád? (Csak a tétel nevét add meg!)",
  ["$\\alpha=40^\\circ$, $\\beta=70^\\circ$, $a=8$",
   "$b=5$, $c=7$, $\\alpha=50^\\circ$", "$a=4$, $b=6$, $c=9$"],
  ['szinusztétel',
   'koszinusztétel',
   'koszinusztétel'], True),
 ("Oldd meg a háromszöget! $\\alpha=50^\\circ$, $\\beta=60^\\circ$, $a=10$. " + KER,
  None, '$\\gamma=70^\\circ$; $b\\approx11{,}31$; $c\\approx12{,}27$.'),
 ("Számítsd ki a harmadik oldalt! $b=9$, $c=12$, $\\alpha=40^\\circ$. " + KER, None,
  '$a\\approx7{,}72$.'),
 ("Számítsd ki a legnagyobb szöget! $a=5$, $b=6$, $c=7$.", None,
  '$\\gamma\\approx78{,}46^\\circ$.'),
 ("Mekkora a háromszög területe? $a=10$, $b=14$, $\\gamma=40^\\circ$.", None,
  '$T\\approx45{,}00$.'),
 ("Mekkora a háromszög területe? $a=7$, $b=9$, $\\gamma=120^\\circ$.", None,
  '$T=\\dfrac{63\\sqrt3}{4}\\approx27{,}28$.'),
 ("Igaz-e, hogy létezik ilyen háromszög? Indokold!",
  ["$a=3$, $b=4$, $c=10$", "$a=6$, $b=7$, $c=9$"],
  ["<b>Nem</b> — $3+4=7&lt;10$, sérül a háromszög-egyenlőtlenség.",
   "<b>Igen</b> — bármely két oldal összege nagyobb a harmadiknál."], True),
 ("Egy háromszögben $\\alpha=30^\\circ$, $\\beta=45^\\circ$. Mekkora $\\gamma$? "
  "Melyik a leghosszabb oldal?", None,
  '$\\gamma=105^\\circ$; a leghosszabb oldal $c$.'),
 ("Egy derékszögű háromszögben $\\gamma=90^\\circ$. Mit ad a koszinusztétel?", None,
  '$c^2=a^2+b^2$ (Pitagorasz-tétel).'),
 ("Egy szabályos háromszög oldala $6$. Mekkora a területe?", None,
  '$T=9\\sqrt3\\approx15{,}59$.'),
 ("Egy háromszög két oldala $8$ és $5$, a közbezárt szög $90^\\circ$. Mekkora a "
  "területe és a harmadik oldala?", None,
  '$T=20$; a harmadik oldal $\\sqrt{89}\\approx9{,}43$.'),
 ("Mekkora a háromszög köré írt körének sugara, ha $a=12$ és $\\alpha=35^\\circ$? "
  "(Használd a $2R=\\tfrac{a}{\\sin\\alpha}$ alakot.)", None,
  '$R\\approx10{,}46$.'),
 ("Egy háromszögben $a=9$, $\\alpha=40^\\circ$, $\\beta=75^\\circ$. Melyik oldal a "
  "leghosszabb? Számold ki!", None,
  'A $b$ oldal a leghosszabb; $b\\approx13{,}52$.'),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Oldd meg a háromszöget! $\\alpha=35^\\circ$, $\\beta=80^\\circ$, $a=20$. " + KER,
  None, "$\\gamma=65^\\circ$; $b\\approx 34{,}34$; $c\\approx 31{,}60$."),
 ("Oldd meg a háromszöget! $b=15$, $c=8$, $\\alpha=105^\\circ$. " + KER, None,
  '$a\\approx18{,}74$; $\\beta\\approx50{,}64^\\circ$; $\\gamma\\approx24{,}36^\\circ$.'),
 ("Oldd meg a háromszöget! $a=8$, $b=11$, $c=15$. " + KER, None,
  '$\\alpha\\approx31{,}29^\\circ$; $\\beta\\approx45{,}57^\\circ$; $\\gamma\\approx103{,}14^\\circ$.'),
 ("Egy háromszögben $a=7$, $b=10$ és $\\alpha=40^\\circ$. Hány megoldás van? "
  "Számold ki $\\beta$-t!", None,
  'Két megoldás: $\\beta\\approx66{,}67^\\circ$ vagy $\\beta\\approx113{,}33^\\circ$.'),
 ('Egy torony tövéhez nem tudunk odajutni. Az $A$ és $B$ megfigyelőpont a torony talpával egy vízszintes egyenesen, a torony ugyanazon oldalán van; $B$ $60$ méterrel közelebb áll hozzá. A csúcsot $A$-ból $28^\\circ$-os, $B$-ből $43^\\circ$-os emelkedési szögben látjuk. Milyen magas a torony?', None,
  '$h\\approx74{,}22$ m.'),
 ('Egy hajó a kikötőből $25$ km-t halad, majd az eredeti haladási irányához képest $110^\\circ$-kal elfordul, és további $35$ km-t tesz meg. Milyen messze van a kikötőtől?', None,
  '$d\\approx35{,}38$ km.'),
 ("Egy paralelogramma oldalai $9$ és $6$, a bezárt szög $50^\\circ$. Mekkora a "
  "területe?", None,
  '$T\\approx41{,}37$.'),
 ("Egy háromszög oldalai $13$, $14$, $15$. Mekkora a területe? "
  "(Számold ki előbb az egyik szöget!)", None,
  'A $15$-ös oldallal szemközti szög $\\gamma\\approx67{,}38^\\circ$; $T=84$.'),
 ("Egy háromszögben $\\alpha=60^\\circ$, $b=8$, $c=5$. Mekkora az $a$ oldal és a "
  "terület?", None,
  '$a=7$; $T=10\\sqrt3\\approx17{,}32$.'),
 ("Egy rombusz oldala $10$, hegyesszöge $65^\\circ$. Mekkorák az átlói?", None,
  'A rövidebb átló $\\approx10{,}75$, a hosszabb $\\approx16{,}87$.'),
 ("Egy háromszög két szöge $\\alpha=45^\\circ$ és $\\gamma=60^\\circ$, a köré írt "
  "körének sugara $R=10$. Mekkora az $a$ oldal?", None,
  '$a=10\\sqrt2\\approx14{,}14$.'),
 ('Két megfigyelő $500$ méterre áll egymástól, azonos vízszintes síkon. Ugyanazt a léggömböt látják: az egyik $40^\\circ$-os, a másik $55^\\circ$-os emelkedési szögben. A léggömb a megfigyelőkön átmenő függőleges síkban van, és függőleges vetülete a két megfigyelő közé esik. Milyen magasan van a léggömb?', None,
  '$h\\approx264{,}28$ m.'),
 ("Egy háromszögben $a=12$, $b=9$, $\\gamma=35^\\circ$. Számold ki a $c$ oldalt, majd "
  "ellenőrizd a szinusztétellel, hogy $\\alpha+\\beta+\\gamma=180^\\circ$!", None,
  '$c\\approx6{,}93$; a szinusztétellel $\\beta\\approx48{,}13^\\circ$, az oldalak alapján $\\alpha\\approx96{,}87^\\circ$; az összeg $180^\\circ$.'),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Igazold a koszinusztétellel, hogy ha $a^{2}=b^{2}+c^{2}$, akkor a háromszög "
  "derékszögű!", None,
  'A koszinusztételből $2bc\\cos\\alpha=b^2+c^2-a^2=0$. Mivel $b,c>0$, $\\cos\\alpha=0$, tehát $\\alpha=90^\\circ$.'),
 ("Egy háromszög oldalai $2$, $3$ és $4$. Tompaszögű-e? Indokold számolással!", None,
  'Igen: $4^2>2^2+3^2$, tehát a legnagyobb szög tompa.'),
 ("Egy háromszögben $\\alpha=30^\\circ$, $a=5$, $b=8$. Van-e ilyen háromszög? "
  "Hány darab?", None,
  'Igen, két különböző háromszög.'),
 ("Egy szabályos hatszög oldala $4$. Mekkora a leghosszabb átlója és a területe?", None,
  'A leghosszabb átló $8$; $T=24\\sqrt3\\approx41{,}57$.'),
 ("Egy háromszög területe $30$, két oldala $8$ és $10$. Mekkora a közbezárt szög?", None,
  '$\\gamma\\approx48{,}59^\\circ$ vagy $\\gamma\\approx131{,}41^\\circ$.'),
 ("Egy telek háromszög alakú: két oldala $40$ m és $55$ m, a közbezárt szög "
  "$78^\\circ$. Mekkora a harmadik oldal és a telek területe?", None,
  '$c\\approx60{,}91$ m; $T\\approx1075{,}96\\ \\text{m}^2$.'),
]

JOKER = ("Egy paralelogramma oldalai $8$ és $5$, a hegyesszöge $60^\\circ$. "
         "Mekkorák az átlói, és mit mondhatunk az átlók négyzetösszegéről?",
         '$d_1=7$, $d_2=\\sqrt{129}\\approx11{,}36$; $d_1^2+d_2^2=178=2(8^2+5^2)$, általában is az oldalak négyzetösszegének kétszerese.')

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
           fajl="feladatok-haromszogek.html", cim="Háromszögek",
           temakor="Trigonometrikus függvények",
           alcim="Szinusz- és koszinusztétel, a négy alapeset, terület, valamint "
                 "magasság- és távolságmérés a gyakorlatban. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-haromszog-megoldasa.html", prevc="Háromszög megoldása és alkalmazások",
           nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
