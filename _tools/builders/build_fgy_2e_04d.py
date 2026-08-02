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
  ["szinusztétel (ASA/AAS)", "koszinusztétel (SAS)", "koszinusztétel (SSS)"], True),
 ("Oldd meg a háromszöget! $\\alpha=50^\\circ$, $\\beta=60^\\circ$, $a=10$. " + KER,
  None, "$\\gamma=70^\\circ$; $b=\\dfrac{10\\sin 60^\\circ}{\\sin 50^\\circ}"
        "\\approx 11{,}31$; $c=\\dfrac{10\\sin 70^\\circ}{\\sin 50^\\circ}\\approx 12{,}27$."),
 ("Számítsd ki a harmadik oldalt! $b=9$, $c=12$, $\\alpha=40^\\circ$. " + KER, None,
  "$a^{2}=81+144-2\\cdot 9\\cdot 12\\cdot\\cos 40^\\circ\\approx 59{,}534$, tehát "
  "$a\\approx 7{,}72$."),
 ("Számítsd ki a legnagyobb szöget! $a=5$, $b=6$, $c=7$.", None,
  "A legnagyobb szög a $c=7$ oldallal szemközti: "
  "$\\cos\\gamma=\\dfrac{25+36-49}{2\\cdot 5\\cdot 6}=\\dfrac{12}{60}=0{,}2$, "
  "tehát $\\gamma\\approx 78{,}46^\\circ$."),
 ("Mekkora a háromszög területe? $a=10$, $b=14$, $\\gamma=40^\\circ$.", None,
  "$T=\\tfrac12\\cdot 10\\cdot 14\\cdot\\sin 40^\\circ\\approx 45{,}00$."),
 ("Mekkora a háromszög területe? $a=7$, $b=9$, $\\gamma=120^\\circ$.", None,
  "$T=\\tfrac12\\cdot 7\\cdot 9\\cdot\\sin 120^\\circ=31{,}5\\cdot 0{,}86603"
  "\\approx 27{,}28$."),
 ("Igaz-e, hogy létezik ilyen háromszög? Indokold!",
  ["$a=3$, $b=4$, $c=10$", "$a=6$, $b=7$, $c=9$"],
  ["<b>Nem</b> — $3+4=7&lt;10$, sérül a háromszög-egyenlőtlenség.",
   "<b>Igen</b> — bármely két oldal összege nagyobb a harmadiknál."], True),
 ("Egy háromszögben $\\alpha=30^\\circ$, $\\beta=45^\\circ$. Mekkora $\\gamma$? "
  "Melyik a leghosszabb oldal?", None,
  "$\\gamma=105^\\circ$; a leghosszabb oldal a $c$, mert a legnagyobb szöggel van szemközt."),
 ("Egy derékszögű háromszögben $\\gamma=90^\\circ$. Mit ad a koszinusztétel?", None,
  "$c^{2}=a^{2}+b^{2}-2ab\\cos 90^\\circ=a^{2}+b^{2}$ — épp a <b>Pitagorasz-tétel</b>."),
 ("Egy szabályos háromszög oldala $6$. Mekkora a területe?", None,
  "$T=\\tfrac12\\cdot 6\\cdot 6\\cdot\\sin 60^\\circ=18\\cdot\\tfrac{\\sqrt3}{2}"
  "=9\\sqrt3\\approx 15{,}59$."),
 ("Egy háromszög két oldala $8$ és $5$, a közbezárt szög $90^\\circ$. Mekkora a "
  "területe és a harmadik oldala?", None,
  "$T=\\tfrac12\\cdot 8\\cdot 5\\cdot 1=20$; a harmadik oldal "
  "$\\sqrt{64+25}=\\sqrt{89}\\approx 9{,}43$."),
 ("Mekkora a háromszög köré írt körének sugara, ha $a=12$ és $\\alpha=35^\\circ$? "
  "(Használd a $2R=\\tfrac{a}{\\sin\\alpha}$ alakot.)", None,
  "$R=\\dfrac{12}{2\\sin 35^\\circ}\\approx 10{,}46$."),
 ("Egy háromszögben $a=9$, $\\alpha=40^\\circ$, $\\beta=75^\\circ$. Melyik oldal a "
  "leghosszabb? Számold ki!", None,
  "$\\gamma=65^\\circ$, tehát a legnagyobb szög $\\beta$: a $b$ oldal a leghosszabb. "
  "$b=\\dfrac{9\\sin 75^\\circ}{\\sin 40^\\circ}\\approx 13{,}53$."),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Oldd meg a háromszöget! $\\alpha=35^\\circ$, $\\beta=80^\\circ$, $a=20$. " + KER,
  None, "$\\gamma=65^\\circ$; $b\\approx 34{,}34$; $c\\approx 31{,}60$."),
 ("Oldd meg a háromszöget! $b=15$, $c=8$, $\\alpha=105^\\circ$. " + KER, None,
  "$a^{2}=225+64-2\\cdot 15\\cdot 8\\cdot\\cos 105^\\circ\\approx 351{,}116$, tehát "
  "$a\\approx 18{,}74$. A <b>kisebbik</b> oldal szöge: "
  "$\\sin\\gamma=\\dfrac{8\\sin 105^\\circ}{18{,}74}$, $\\gamma\\approx 24{,}36^\\circ$, "
  "és $\\beta\\approx 50{,}64^\\circ$."),
 ("Oldd meg a háromszöget! $a=8$, $b=11$, $c=15$. " + KER, None,
  "A legnagyobb oldal a $c$: $\\cos\\gamma=\\dfrac{64+121-225}{2\\cdot 8\\cdot 11}"
  "=-\\dfrac{40}{176}\\approx -0{,}22727$, tehát $\\gamma\\approx 103{,}14^\\circ$ "
  "(<b>tompaszög</b>). Innen $\\alpha\\approx 31{,}29^\\circ$ és "
  "$\\beta\\approx 45{,}57^\\circ$ (összegük $180^\\circ$ ✔)."),
 ("Egy háromszögben $a=7$, $b=10$ és $\\alpha=40^\\circ$. Hány megoldás van? "
  "Számold ki $\\beta$-t!", None,
  "$\\sin\\beta=\\dfrac{10\\sin 40^\\circ}{7}\\approx 0{,}91820$, tehát "
  "$\\beta\\approx 66{,}67^\\circ$ <b>vagy</b> $\\beta\\approx 113{,}33^\\circ$ — "
  "mindkettő ad érvényes háromszöget, mert $\\alpha$ hegyesszög és $a&lt;b$. "
  "Ez a <b>kétértelmű (SSA) eset</b>."),
 ("Egy torony tövéhez nem tudunk odajutni. Az $A$ pontból a csúcsot $28^\\circ$-os, "
  "$60$ méterrel közelebbről, a $B$ pontból $43^\\circ$-os emelkedési szögben látjuk. "
  "Milyen magas a torony?", None,
  "Az $ABT$ háromszögben a $B$-nél lévő belső szög $180^\\circ-43^\\circ=137^\\circ$, "
  "tehát $\\angle ATB=15^\\circ$. Szinusztétellel "
  "$BT=\\dfrac{60\\sin 28^\\circ}{\\sin 15^\\circ}\\approx 108{,}83$ m, végül "
  "$h=BT\\sin 43^\\circ\\approx 74{,}22$ m."),
 ("Egy hajó a kikötőből $25$ km-t halad, majd $110^\\circ$-kal elfordul, és további "
  "$35$ km-t tesz meg. Milyen messze van a kikötőtől?", None,
  "A háromszög belső szöge $180^\\circ-110^\\circ=70^\\circ$: "
  "$d^{2}=625+1225-2\\cdot 25\\cdot 35\\cdot\\cos 70^\\circ\\approx 1251{,}47$, "
  "tehát $d\\approx 35{,}38$ km."),
 ("Egy paralelogramma oldalai $9$ és $6$, a bezárt szög $50^\\circ$. Mekkora a "
  "területe?", None,
  "A paralelogramma két egybevágó háromszögből áll: "
  "$T=2\\cdot\\tfrac12\\cdot 9\\cdot 6\\cdot\\sin 50^\\circ=54\\sin 50^\\circ"
  "\\approx 41{,}37$."),
 ("Egy háromszög oldalai $13$, $14$, $15$. Mekkora a területe? "
  "(Számold ki előbb az egyik szöget!)", None,
  "$\\cos\\gamma=\\dfrac{169+196-225}{2\\cdot 13\\cdot 14}=\\dfrac{140}{364}"
  "\\approx 0{,}38462$, tehát $\\gamma\\approx 67{,}38^\\circ$ és "
  "$T=\\tfrac12\\cdot 13\\cdot 14\\cdot\\sin\\gamma\\approx 84{,}00$. "
  "(Héron-képlettel pontosan $84$.)"),
 ("Egy háromszögben $\\alpha=60^\\circ$, $b=8$, $c=5$. Mekkora az $a$ oldal és a "
  "terület?", None,
  "$a^{2}=64+25-2\\cdot 8\\cdot 5\\cdot 0{,}5=49$, tehát $a=7$ (egész!). "
  "$T=\\tfrac12\\cdot 8\\cdot 5\\cdot\\sin 60^\\circ=20\\cdot\\tfrac{\\sqrt3}{2}"
  "=10\\sqrt3\\approx 17{,}32$."),
 ("Egy rombusz oldala $10$, hegyesszöge $65^\\circ$. Mekkorák az átlói?", None,
  "A rövidebb átló a hegyesszöggel szemközt: "
  "$d_{1}^{2}=100+100-200\\cos 65^\\circ\\approx 115{,}47$, $d_{1}\\approx 10{,}75$. "
  "A hosszabb a tompaszöggel ($115^\\circ$) szemközt: "
  "$d_{2}^{2}=200-200\\cos 115^\\circ\\approx 284{,}52$, $d_{2}\\approx 16{,}87$."),
 ("Egy háromszög két szöge $\\alpha=45^\\circ$ és $\\gamma=60^\\circ$, a köré írt "
  "körének sugara $R=10$. Mekkora az $a$ oldal?", None,
  "$a=2R\\sin\\alpha=20\\cdot\\tfrac{\\sqrt2}{2}=10\\sqrt2\\approx 14{,}14$."),
 ("Két megfigyelő $500$ méterre áll egymástól, és ugyanazt a léggömböt látja: az egyik "
  "$40^\\circ$-os, a másik $55^\\circ$-os emelkedési szögben (a léggömb köztük van). "
  "Milyen magasan van a léggömb?", None,
  "A háromszög harmadik szöge $180^\\circ-40^\\circ-55^\\circ=85^\\circ$. Az egyik "
  "ferde távolság $\\dfrac{500\\sin 55^\\circ}{\\sin 85^\\circ}\\approx 411{,}17$ m, "
  "a magasság ebből $411{,}17\\cdot\\sin 40^\\circ\\approx 264{,}29$ m."),
 ("Egy háromszögben $a=12$, $b=9$, $\\gamma=35^\\circ$. Számold ki a $c$ oldalt, majd "
  "ellenőrizd a szinusztétellel, hogy $\\alpha+\\beta+\\gamma=180^\\circ$!", None,
  "$c^{2}=144+81-2\\cdot 12\\cdot 9\\cdot\\cos 35^\\circ\\approx 48{,}09$, tehát "
  "$c\\approx 6{,}93$. A legkisebb oldal a $c$, ezért $\\gamma$ a legkisebb szög ✔ "
  "$\\sin\\beta=\\dfrac{9\\sin 35^\\circ}{6{,}93}$ → $\\beta\\approx 48{,}18^\\circ$, "
  "$\\alpha\\approx 96{,}82^\\circ$; az összeg $180^\\circ$ ✔"),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Igazold a koszinusztétellel, hogy ha $a^{2}=b^{2}+c^{2}$, akkor a háromszög "
  "derékszögű!", None,
  "$a^{2}=b^{2}+c^{2}-2bc\\cos\\alpha$, és ha $a^{2}=b^{2}+c^{2}$, akkor "
  "$2bc\\cos\\alpha=0$. Mivel $b,c\\neq 0$, csak $\\cos\\alpha=0$ lehet, azaz "
  "$\\alpha=90^\\circ$ ✔ (Ez a Pitagorasz-tétel megfordítása.)"),
 ("Egy háromszög oldalai $2$, $3$ és $4$. Tompaszögű-e? Indokold számolással!", None,
  "A legnagyobb oldallal szemközti szög: "
  "$\\cos\\gamma=\\dfrac{4+9-16}{2\\cdot 2\\cdot 3}=-\\dfrac{3}{12}=-0{,}25$. "
  "A koszinusz <b>negatív</b>, tehát $\\gamma\\approx 104{,}48^\\circ$ — a háromszög "
  "<b>tompaszögű</b>."),
 ("Egy háromszögben $\\alpha=30^\\circ$, $a=5$, $b=8$. Van-e ilyen háromszög? "
  "Hány darab?", None,
  "$\\sin\\beta=\\dfrac{8\\sin 30^\\circ}{5}=0{,}8$, tehát $\\beta\\approx 53{,}13^\\circ$ "
  "vagy $\\beta\\approx 126{,}87^\\circ$. Mindkettőnél $\\alpha+\\beta&lt;180^\\circ$, "
  "tehát <b>két</b> különböző háromszög létezik."),
 ("Egy szabályos hatszög oldala $4$. Mekkora a leghosszabb átlója és a területe?", None,
  "A szabályos hatszög hat szabályos háromszögből áll, ezért a leghosszabb átló "
  "$2\\cdot 4=8$. A terület "
  "$6\\cdot\\tfrac12\\cdot 4\\cdot 4\\cdot\\sin 60^\\circ=24\\sqrt3\\approx 41{,}57$."),
 ("Egy háromszög területe $30$, két oldala $8$ és $10$. Mekkora a közbezárt szög?", None,
  "$30=\\tfrac12\\cdot 8\\cdot 10\\cdot\\sin\\gamma$, tehát $\\sin\\gamma=0{,}75$: "
  "$\\gamma\\approx 48{,}59^\\circ$ <b>vagy</b> $\\gamma\\approx 131{,}41^\\circ$ — "
  "két különböző háromszög adja ugyanazt a területet."),
 ("Egy telek háromszög alakú: két oldala $40$ m és $55$ m, a közbezárt szög "
  "$78^\\circ$. Mekkora a harmadik oldal és a telek területe?", None,
  "$c^{2}=1600+3025-2\\cdot 40\\cdot 55\\cdot\\cos 78^\\circ\\approx 3710{,}0$, tehát "
  "$c\\approx 60{,}91$ m. $T=\\tfrac12\\cdot 40\\cdot 55\\cdot\\sin 78^\\circ"
  "\\approx 1076{,}0\\ \\text{m}^{2}$."),
]

JOKER = ("Egy paralelogramma oldalai $8$ és $5$, a hegyesszöge $60^\\circ$. "
         "Mekkorák az átlói, és mit mondhatunk az átlók négyzetösszegéről?",
         "A <b>rövidebb</b> átló a $60^\\circ$-os szöggel szemközt: "
         "$d_{1}^{2}=64+25-2\\cdot 8\\cdot 5\\cos 60^\\circ=89-40=49$, tehát $d_{1}=7$. "
         "A <b>hosszabb</b> a $120^\\circ$-os szöggel szemközt: "
         "$d_{2}^{2}=89-80\\cos 120^\\circ=89+40=129$, tehát "
         "$d_{2}=\\sqrt{129}\\approx 11{,}36$. "
         "Figyeld meg: $d_{1}^{2}+d_{2}^{2}=49+129=178=2(64+25)$ — az átlók "
         "négyzetösszege mindig az oldalak négyzetösszegének a <b>kétszerese</b> "
         "(paralelogramma-azonosság), mert a két koszinuszos tag ellentétes előjellel "
         "kiesik.")

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
