# -*- coding: utf-8 -*-
"""3e/02 — B altema feladatgyujtemeny: a kup, a sikmetszetek es a csonkakup."""
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

x, r_, H_ = symbols('x r H', positive=True)
S = lambda rr, HH: sqrt(rr**2 + HH**2)
M_k = lambda rr, ss: rr*pi*ss
F_k = lambda rr, ss: rr**2*pi + rr*pi*ss
V_k = lambda rr, HH: rr**2*pi*HH/3
V_h = lambda rr, HH: rr**2*pi*HH
S_cs = lambda RR, rr, HH: sqrt(HH**2 + (RR - rr)**2)
M_cs = lambda RR, rr, ss: (RR + rr)*pi*ss
V_cs = lambda RR, rr, HH: HH*pi/3*(RR**2 + RR*rr + rr**2)

# --- B1 (alap 1–6, közép 1–3)
chk("a1", S(5, 12), 13)
chk("a2", sqrt(15**2 - 9**2), 12)
chk("a3", sqrt(17**2 - 8**2), 15)
chk("a4-s", 2*5, 10);                    chk("a4-H", sqrt(10**2 - 5**2), 5*sqrt(3))
chk("a5-fi", 360*R(6, 10), 216)
chk("k1", [R(16, 2), 17, sqrt(17**2 - 8**2)], [8, 17, 15])
chk("k2-r", 12*R(120, 360), 4)
chk("k3-r", solve(Eq(x*sqrt(3), 6*sqrt(3)), x)[0], 6)
# --- B2 (alap 7–16, közép 4–11)
chk("a7-M", M_k(6, 10), 60*pi);          chk("a7-F", F_k(6, 10), 96*pi)
chk("a8-s", S(5, 12), 13);               chk("a8-F", F_k(5, 13), 90*pi)
chk("a8-V", V_k(5, 12), 100*pi)
chk("a9", V_k(3, 4), 12*pi)
chk("a10", V_k(9, 12), 324*pi)
chk("a11-H", sqrt(10**2 - 6**2), 8);     chk("a11-V", V_k(6, 8), 96*pi)
chk("a12", F_k(3, 6), 27*pi)
chk("a13", solve(Eq(M_k(5, x), 65*pi), x)[0], 13)
chk("a14", solve(Eq(V_k(6, x), 96*pi), x)[0], 8)
chk("a15", solve(Eq(V_k(x, 12), 100*pi), x)[0], 5)
chk("a16", N(V_k(2, R(15, 10)), 9), 6.28318531, 1e-6)
chk("k4-s", solve(Eq(F_k(6, x), 96*pi), x)[0], 10)
chk("k4-H", sqrt(10**2 - 6**2), 8)
chk("k5-r", solve(Eq(F_k(x, 5), 24*pi), x)[0], 3)
chk("k6-a", solve(Eq(x**2*sqrt(3)/4, 9*sqrt(3)), x)[0], 6)
chk("k6-V", V_k(3, 3*sqrt(3)), 9*sqrt(3)*pi)
chk("k7", V_k(r_, 3)/V_k(r_, 5), R(3, 5))
chk("k8-r", solve(Eq(V_k(x, 3*x), 27*pi), x)[0], 3)
chk("k9", V_h(4, 9) - V_k(4, 9), 96*pi)
chk("k10-r", sqrt(25**2 - 24**2), 7)
chk("k10-F", F_k(7, 25), 224*pi);        chk("k10-V", V_k(7, 24), 392*pi)
chk("k11-M", M_k(9, 15), 135*pi);        chk("k11-H", sqrt(15**2 - 9**2), 12)
# --- B3 (alap 17–21, közép 12–15)
chk("a17", 2*6*10, 120)
chk("a18-T", 5*12, 60);                  chk("a18-K", 2*5 + 2*13, 36)
chk("a19", [R(8, 2), R(8, 2)**2*pi], [4, 16*pi])
chk("a20", 7**2*pi, 49*pi)
chk("a21", [9*R(1, 3), (9*R(1, 3))**2*pi], [3, 9*pi])
chk("k12-H", solve(Eq(7*x, 84), x)[0], 12)
chk("k12-V", V_k(7, 12), 196*pi)
chk("k13-r", solve(Eq((2*x)**2, 64), x)[0], 4)
chk("k13-V", V_h(4, 8), 128*pi)
chk("k14-k", R(3, 12), R(1, 4))
chk("k14-tav", 16 - 16*R(1, 4), 12)
chk("k15-r", solve(Eq(2*x + 20, 32), x)[0], 6)
chk("k15-V", V_k(6, sqrt(10**2 - 6**2)), 96*pi)
# --- B4 (alap 22–28, közép 16–21)
chk("a22", S_cs(8, 5, 4), 5)
chk("a23", solve(Eq(S_cs(10, 4, x), 10), x)[0], 8)
chk("a24", M_cs(6, 3, 5), 45*pi)
chk("a25", 6**2*pi + 3**2*pi + 45*pi, 90*pi)
chk("a26", V_cs(6, 3, 4), 84*pi)
chk("a27", V_cs(5, 2, 6), 78*pi)
chk("a28-V", V_cs(10, 7, 12), 876*pi)
chk("a28-liter", N(V_cs(10, 7, 12)/1000, 9), 2.75203516, 1e-6)
chk("k16-s", S_cs(9, 4, 12), 13)
chk("k16-M", M_cs(9, 4, 13), 169*pi)
chk("k16-F", 81*pi + 16*pi + 169*pi, 266*pi)
chk("k17-H", solve(Eq(V_cs(5, 3, x), 196*pi), x)[0], 12)
chk("k18-r", solve(Eq(S_cs(10, x, 12), 13), x)[0], 5)
chk("k19", solve(Eq((x)*pi*5, 45*pi), x)[0], 9)
chk("k20-kis", V_k(4, 6), 32*pi);        chk("k20-teljes", V_k(8, 12), 256*pi)
chk("k20-cs", V_k(8, 12) - V_k(4, 6), 224*pi)
chk("k20-keplet", V_cs(8, 4, 6), 224*pi)
chk("k21-V", V_cs(15, 12, 25), 4575*pi)
chk("k21-liter", N(V_cs(15, 12, 25)/1000, 9), 14.3727864, 1e-6)
# --- nehéz
chk("n1-r", solve(Eq(F_k(x, 10), 144*pi), x)[0], 8)
chk("n1-V", V_k(8, 6), 128*pi)
chk("n2", V_k(r_/2, H_/2)/(V_k(r_, H_) - V_k(r_/2, H_/2)), R(1, 7))
chk("n3", 6*R(6, 6 - 2), 9)
chk("n4", V_k(r_, r_*sqrt(3))/V_h(r_, 2*r_), sqrt(3)/6)
chk("n5-V", V_k(6, 6), 72*pi)
chk("joker-r", 20*R(90, 360), 5)
chk("joker-H", sqrt(20**2 - 5**2), 5*sqrt(15))
chk("joker-V", V_k(5, 5*sqrt(15)), R(125, 3)*sqrt(15)*pi)
chk("joker-kozelites", N(V_k(5, 5*sqrt(15)), 9), 506.972335, 1e-5)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- B1: a kúp elemei (alap 1–6)
 ("Egy kúp alapkörének sugara $5$ cm, magassága $12$ cm. Mekkora az alkotója?", None,
  "$s=\\sqrt{r^2+H^2}=\\sqrt{25+144}=\\sqrt{169}=13$ cm."),

 ("Egy kúp alapkörének sugara $9$ cm, alkotója $15$ cm. Mekkora a magassága?", None,
  "$H=\\sqrt{s^2-r^2}=\\sqrt{225-81}=\\sqrt{144}=12$ cm."),

 ("Egy kúp magassága $8$ cm, alkotója $17$ cm. Mekkora az alapkörének sugara?", None,
  "$r=\\sqrt{s^2-H^2}=\\sqrt{289-64}=\\sqrt{225}=15$ cm."),

 ("Egy <b>egyenlő oldalú</b> kúp alapkörének sugara $5$ cm. Mekkora", 
  ["az alkotója", "a magassága"],
  ["$s=2r=10$ cm", "$H=\\sqrt{100-25}=5\\sqrt3\\approx8{,}66$ cm"], True),

 ("Egy kúp alkotója $10$ cm, alapkörének sugara $6$ cm. Mekkora a hálójában a körcikk "
  "sugara és középponti szöge?", None,
  "A körcikk sugara az <b>alkotó</b>: $10$ cm. A középponti szög "
  "$\\varphi=360^\\circ\\cdot\\frac rs=360^\\circ\\cdot\\frac{6}{10}=216^\\circ$."),

 ("A kúp három adata közül ($r$, $H$, $s$) melyik a leghosszabb, és miért?", None,
  "Az <b>alkotó</b> ($s$), mert a jellemző derékszögű háromszögben az <b>átfogó</b>: "
  "$s^2=r^2+H^2$, ezért $s>r$ és $s>H$ is teljesül."),

 # --- B2: felszín és térfogat (alap 7–16)
 ("Egy kúp alapkörének sugara $6$ cm, alkotója $10$ cm. Mekkora a palástja és a "
  "felszíne?", None,
  "$M=r\\pi s=60\\pi\\ \\text{cm}^2$, $F=r^2\\pi+M=36\\pi+60\\pi=96\\pi\\ \\text{cm}^2$."),

 ("Egy kúp alapkörének sugara $5$ cm, magassága $12$ cm. Számítsd ki",
  ["az alkotóját", "a felszínét", "a térfogatát"],
  ["$s=13$ cm", "$F=25\\pi+65\\pi=90\\pi\\ \\text{cm}^2$",
   "$V=\\frac{25\\pi\\cdot12}{3}=100\\pi\\ \\text{cm}^3$"], True),

 ("Mekkora annak a kúpnak a térfogata, amelynek az alapköre $3$ cm sugarú, a magassága "
  "pedig $4$ cm?", None,
  "$V=\\frac{9\\pi\\cdot4}{3}=12\\pi\\ \\text{cm}^3$."),

 ("Egy kúp alapkörének sugara $9$ cm, magassága $12$ cm. Mekkora a térfogata?", None,
  "$V=\\frac{81\\pi\\cdot12}{3}=324\\pi\\ \\text{cm}^3$."),

 ("Egy kúp alapkörének sugara $6$ cm, alkotója $10$ cm. Mekkora a <b>térfogata</b>?", None,
  "Előbb a magasság: $H=\\sqrt{100-36}=8$ cm. Ezután "
  "$V=\\frac{36\\pi\\cdot8}{3}=96\\pi\\ \\text{cm}^3$."),

 ("Egy egyenlő oldalú kúp alapkörének sugara $3$ cm. Mekkora a felszíne?", None,
  "Itt $s=2r=6$ cm, ezért $F=r\\pi(r+s)=3\\pi\\cdot9=27\\pi\\ \\text{cm}^2$."),

 ("Egy kúp palástja $65\\pi\\ \\text{cm}^2$, alapkörének sugara $5$ cm. Mekkora az "
  "alkotója?", None,
  "$M=r\\pi s$, tehát $5\\pi s=65\\pi$, ahonnan $s=13$ cm."),

 ("Egy kúp térfogata $96\\pi\\ \\text{cm}^3$, alapkörének sugara $6$ cm. Mekkora a "
  "magassága?", None,
  "$\\frac{36\\pi H}{3}=96\\pi$, tehát $12H=96$ és $H=8$ cm."),

 ("Egy kúp térfogata $100\\pi\\ \\text{cm}^3$, magassága $12$ cm. Mekkora az alapkörének "
  "sugara?", None,
  "$\\frac{r^2\\pi\\cdot12}{3}=100\\pi$, azaz $4r^2=100$, tehát $r=5$ cm."),

 ("Egy kúp alakú homokkupac alapkörének sugara $2$ m, magassága $1{,}5$ m. Hány "
  "köbméter homok van benne? (Két tizedesre kerekítve.)", None,
  "$V=\\frac{4\\pi\\cdot1{,}5}{3}=2\\pi\\approx6{,}28\\ \\text{m}^3$."),

 # --- B3: síkmetszetek (alap 17–21)
 ("Egy henger alapkörének sugara $6$ cm, magassága $10$ cm. Mekkora a "
  "<b>tengelymetszetének</b> a területe?", None,
  "A tengelymetszet téglalap, oldalai $2r=12$ cm és $H=10$ cm, ezért "
  "$T=120\\ \\text{cm}^2$."),

 ("Egy kúp alapkörének sugara $5$ cm, magassága $12$ cm. Mekkora a tengelymetszetének",
  ["a területe", "a kerülete"],
  ["$T=\\frac{2r\\cdot H}{2}=\\frac{10\\cdot12}{2}=60\\ \\text{cm}^2$",
   "$s=13$ cm, ezért $K=2r+2s=10+26=36$ cm"], True),

 ("Egy kúp alapkörének sugara $8$ cm. A <b>csúcstól</b> mérve a magasság felénél elmetsszük "
  "az alaplappal párhuzamos síkkal. Mekkora a metszetkör sugara és "
  "területe?", None,
  "A hasonlóság aránya $k=\\frac12$, ezért a metszetkör sugara $4$ cm, a területe "
  "pedig $16\\pi\\ \\text{cm}^2$."),

 ("Egy henger alapkörének sugara $7$ cm. Mekkora az alaplappal párhuzamos "
  "síkmetszetének a területe?", None,
  "A henger párhuzamos metszete az alapkörrel <b>egybevágó</b>, ezért a területe "
  "$49\\pi\\ \\text{cm}^2$ — bárhol is metszünk."),

 ("Egy kúp alapkörének sugara $9$ cm, magassága $12$ cm. A <b>csúcstól</b> mérve a magasság "
  "harmadánál metsszük el az alaplappal párhuzamosan. Mekkora a metszetkör "
  "sugara és területe?", None,
  "$k=\\frac13$, ezért a sugár $9\\cdot\\frac13=3$ cm, a terület pedig "
  "$9\\pi\\ \\text{cm}^2$. (A $12$ cm-es magasság ehhez nem is kell.)"),

 # --- B4: csonkakúp (alap 22–28)
 ("Egy csonkakúp alapkörének sugara $R=8$ cm, fedőköréé $r=5$ cm, magassága $H=4$ cm. "
  "Mekkora az alkotója?", None,
  "$s=\\sqrt{H^2+(R-r)^2}=\\sqrt{16+9}=5$ cm."),

 ("Egy csonkakúp alapkörének sugara $R=10$ cm, fedőköréé $r=4$ cm, az alkotója $10$ cm. "
  "Mekkora a magassága?", None,
  "$s^2=H^2+(R-r)^2$, tehát $100=H^2+36$, ahonnan $H=8$ cm."),

 ("Egy csonkakúp alapkörének sugara $R=6$ cm, fedőköréé $r=3$ cm, az alkotója $5$ cm. "
  "Mekkora a palástja?", None,
  "$M=(R+r)\\pi s=9\\pi\\cdot5=45\\pi\\ \\text{cm}^2$."),

 ("Egy csonkakúp alapkörének sugara $R=6$ cm, fedőköréé $r=3$ cm, az alkotója $5$ cm. "
  "Mekkora a <b>felszíne</b>?", None,
  "$F=R^2\\pi+r^2\\pi+M=36\\pi+9\\pi+45\\pi=90\\pi\\ \\text{cm}^2$."),

 ("Egy csonkakúp alapkörének sugara $R=6$ cm, fedőköréé $r=3$ cm, a magassága $H=4$ cm. "
  "Mekkora a térfogata?", None,
  "$V=\\frac{H\\pi}{3}\\left(R^2+Rr+r^2\\right)=\\frac{4\\pi}{3}(36+18+9)="
  "\\frac{4\\pi}{3}\\cdot63=84\\pi\\ \\text{cm}^3$."),

 ("Egy csonkakúp alapkörének sugara $R=5$ cm, fedőköréé $r=2$ cm, a magassága $H=6$ cm. "
  "Mekkora a térfogata?", None,
  "$V=\\frac{6\\pi}{3}(25+10+4)=2\\pi\\cdot39=78\\pi\\ \\text{cm}^3$."),

 ("Egy virágcserép csonkakúp alakú: a felső körének sugara $10$ cm, az aljáé $7$ cm, a "
  "magassága $12$ cm. Hány <b>liter</b> föld fér bele? (Két tizedesre kerekítve.)", None,
  "$V=\\frac{12\\pi}{3}(100+70+49)=4\\pi\\cdot219=876\\pi\\approx2752{,}04\\ "
  "\\text{cm}^3$, ami körülbelül $2{,}75$ liter. (A térfogatképlet a két sugárban "
  "<b>szimmetrikus</b>, ezért mindegy, melyiket nevezzük $R$-nek — a cserép felfelé "
  "szélesedik.)"),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- B1 (közép 1–3)
 ("Egy kúp tengelymetszete olyan egyenlő szárú háromszög, amelynek az alapja $16$ cm, a "
  "szára $17$ cm. Mekkora a kúp alapkörének sugara, az alkotója és a magassága?", None,
  "A tengelymetszet alapja az átmérő: $2r=16$, tehát $r=8$ cm. A szár az alkotó: "
  "$s=17$ cm. Innen $H=\\sqrt{289-64}=15$ cm."),

 ("Egy kúp hálójában a körcikk középponti szöge $120^\\circ$, a sugara $12$ cm. Mekkora "
  "a kúp alapkörének sugara?", None,
  "$\\varphi=360^\\circ\\cdot\\frac rs$, tehát $120=360\\cdot\\frac{r}{12}$, ahonnan "
  "$r=4$ cm. (A körcikk sugara az alkotó: $s=12$ cm.)"),

 ("Egy egyenlő oldalú kúp magassága $6\\sqrt3$ cm. Mekkora az alapkörének sugara és az "
  "alkotója?", None,
  "Egyenlő oldalú kúpnál $H=r\\sqrt3$, tehát $r\\sqrt3=6\\sqrt3$, ahonnan $r=6$ cm és "
  "$s=2r=12$ cm."),

 # --- B2 (közép 4–11)
 ("Egy kúp felszíne $96\\pi\\ \\text{cm}^2$, alapkörének sugara $6$ cm. Mekkora az "
  "alkotója és a magassága?", None,
  "$F=r\\pi(r+s)$, tehát $6\\pi(6+s)=96\\pi$, ahonnan $6+s=16$ és $s=10$ cm. Innen "
  "$H=\\sqrt{100-36}=8$ cm."),

 ("Egy kúp felszíne $24\\pi\\ \\text{cm}^2$, az alkotója $5$ cm. Mekkora az alapkörének "
  "sugara?", None,
  "$r^2\\pi+5r\\pi=24\\pi$, azaz $r^2+5r-24=0$. A megoldóképlet szerint "
  "$r=\\frac{-5+\\sqrt{25+96}}{2}=\\frac{-5+11}{2}=3$ cm (a negatív gyök nem sugár)."),

 ("Egy kúp tengelymetszete <b>szabályos</b> háromszög, amelynek a területe "
  "$9\\sqrt3\\ \\text{cm}^2$. Mekkora a kúp térfogata?", None,
  "A szabályos háromszög területe $\\frac{a^2\\sqrt3}{4}=9\\sqrt3$, tehát $a^2=36$ és "
  "$a=6$ cm. Ez az átmérő, ezért $r=3$ cm, az alkotó $s=6$ cm, a magasság "
  "$H=3\\sqrt3$ cm. Így $V=\\frac{9\\pi\\cdot3\\sqrt3}{3}=9\\sqrt3\\,\\pi\\ "
  "\\text{cm}^3$."),

 ("Két kúp alapköre egybevágó, a magasságuk aránya $3:5$. Hogyan aránylik a térfogatuk?", None,
  "A térfogat a magassággal egyenesen arányos, ezért a térfogatok aránya is $3:5$."),

 ("Egy kúp magassága az alapkör sugarának <b>háromszorosa</b>, a térfogata "
  "$27\\pi\\ \\text{cm}^3$. Mekkora a sugara?", None,
  "$\\frac{r^2\\pi\\cdot3r}{3}=r^3\\pi=27\\pi$, tehát $r=3$ cm (és $H=9$ cm)."),

 ("Egy kúp és egy henger alapköre és magassága is megegyezik: $r=4$ cm, $H=9$ cm. "
  "Mennyivel nagyobb a henger térfogata?", None,
  "$V_{\\text{henger}}=16\\pi\\cdot9=144\\pi$, $V_{\\text{kúp}}=\\frac{144\\pi}{3}"
  "=48\\pi$. A különbség $96\\pi\\ \\text{cm}^3$ — vagyis a henger térfogata a "
  "kúpénak a <b>háromszorosa</b>."),

 ("Egy kúp alkotója $25$ cm, magassága $24$ cm. Mekkora a felszíne és a térfogata?", None,
  "$r=\\sqrt{625-576}=7$ cm. Innen $F=49\\pi+7\\cdot25\\pi=224\\pi\\ \\text{cm}^2$ és "
  "$V=\\frac{49\\pi\\cdot24}{3}=392\\pi\\ \\text{cm}^3$."),

 ("Egy kúp alakú papírtölcsér alkotója $15$ cm, alapkörének sugara $9$ cm. Hány "
  "négyzetcentiméter papír kell hozzá (a tölcsér felül nyitott), és milyen mély?", None,
  "Csak a palást kell: $M=r\\pi s=9\\pi\\cdot15=135\\pi\\ \\text{cm}^2$. A mélysége a "
  "magasság: $H=\\sqrt{225-81}=12$ cm."),

 # --- B3 (közép 12–15)
 ("Egy kúp tengelymetszetének területe $84\\ \\text{cm}^2$, az alapkör sugara $7$ cm. "
  "Mekkora a magassága és a térfogata?", None,
  "A tengelymetszet területe $\\frac{2r\\cdot H}{2}=r\\,H$, tehát $7H=84$ és "
  "$H=12$ cm. Innen $V=\\frac{49\\pi\\cdot12}{3}=196\\pi\\ \\text{cm}^3$."),

 ("Egy henger tengelymetszete <b>négyzet</b>, amelynek a területe $64\\ \\text{cm}^2$. "
  "Mekkora a henger térfogata?", None,
  "A négyzet oldala $8$ cm; ez egyszerre az átmérő és a magasság, tehát $r=4$ cm és "
  "$H=8$ cm (egyenlő oldalú henger). Így $V=16\\pi\\cdot8=128\\pi\\ \\text{cm}^3$."),

 ("Egy kúp alapkörének sugara $12$ cm, magassága $16$ cm. Milyen messze kell az "
  "<b>alaplaptól</b> elmetszeni az alaplappal párhuzamos síkkal, hogy a metszetkör "
  "sugara $3$ cm legyen?", None,
  "A hasonlóság aránya $k=\\frac{3}{12}=\\frac14$, tehát a metszősík a <b>csúcstól</b> "
  "$16\\cdot\\frac14=4$ cm-re van. Az alaplaptól mérve ez $16-4=12$ cm."),

 ("Egy kúp tengelymetszetének kerülete $32$ cm, az alkotója $10$ cm. Mekkora a "
  "térfogata?", None,
  "A kerület $2r+2s=32$, tehát $2r+20=32$ és $r=6$ cm. Innen $H=\\sqrt{100-36}=8$ cm, "
  "és $V=\\frac{36\\pi\\cdot8}{3}=96\\pi\\ \\text{cm}^3$."),

 # --- B4 (közép 16–21)
 ("Egy csonkakúp alapkörének sugara $R=9$ cm, fedőköréé $r=4$ cm, a magassága $H=12$ cm. "
  "Számítsd ki",
  ["az alkotóját", "a palástját", "a felszínét"],
  ["$s=\\sqrt{144+25}=13$ cm", "$M=(9+4)\\pi\\cdot13=169\\pi\\ \\text{cm}^2$",
   "$F=81\\pi+16\\pi+169\\pi=266\\pi\\ \\text{cm}^2$"], True),

 ("Egy csonkakúp alapkörének sugara $R=5$ cm, fedőköréé $r=3$ cm, a térfogata "
  "$196\\pi\\ \\text{cm}^3$. Mekkora a magassága?", None,
  "$\\frac{H\\pi}{3}(25+15+9)=\\frac{49H\\pi}{3}=196\\pi$, tehát "
  "$H=\\frac{196\\cdot3}{49}=12$ cm."),

 ("Egy csonkakúp alkotója $13$ cm, magassága $12$ cm, a nagyobbik sugara $10$ cm. "
  "Mekkora a kisebbik sugara?", None,
  "$s^2=H^2+(R-r)^2$, tehát $169=144+(10-r)^2$, ahonnan $(10-r)^2=25$ és $10-r=5$, "
  "azaz $r=5$ cm."),

 ("Egy csonkakúp palástja $45\\pi\\ \\text{cm}^2$, az alkotója $5$ cm. Mekkora a két "
  "sugár <b>összege</b>?", None,
  "$M=(R+r)\\pi s$, tehát $(R+r)\\cdot5\\pi=45\\pi$, ahonnan $R+r=9$ cm. (A két sugár "
  "külön-külön ebből még nem határozható meg.)"),

 ("Egy $12$ cm magas kúp alapkörének sugara $8$ cm. A magasság <b>felénél</b> "
  "elmetsszük az alaplappal párhuzamosan, és a felső darabot elhagyjuk. Mekkora a "
  "megmaradó csonkakúp térfogata? Ellenőrizd a csonkakúp képletével is!", None,
  "<b>Kivonással:</b> a teljes kúp $V=\\frac{64\\pi\\cdot12}{3}=256\\pi$; a levágott "
  "kis kúp sugara $4$ cm, magassága $6$ cm, tehát $\\frac{16\\pi\\cdot6}{3}=32\\pi$. "
  "A csonkakúp $256\\pi-32\\pi=224\\pi\\ \\text{cm}^3$.<br>"
  "<b>Képlettel:</b> $\\frac{6\\pi}{3}(64+32+16)=2\\pi\\cdot112=224\\pi\\ \\text{cm}^3$ "
  "— a két út ugyanazt adja."),

 ("Egy vödör csonkakúp alakú: a felső körének sugara $15$ cm, az aljáé $12$ cm, a "
  "magassága $25$ cm. Hány liter fér bele? (Két tizedesre kerekítve.)", None,
  "$V=\\frac{25\\pi}{3}(225+180+144)=\\frac{25\\pi}{3}\\cdot549=4575\\pi\\approx"
  "14372{,}79\\ \\text{cm}^3$, ami körülbelül $14{,}37$ liter."),
]

# ============================== NEHÉZ SZINT ==============================
NEHEZ = [
 ("Egy kúp felszíne $144\\pi\\ \\text{cm}^2$, az alkotója $10$ cm. Mekkora a "
  "térfogata?", None,
  "$r^2\\pi+10r\\pi=144\\pi$, azaz $r^2+10r-144=0$. Innen "
  "$r=\\frac{-10+\\sqrt{100+576}}{2}=\\frac{-10+26}{2}=8$ cm. A magasság "
  "$H=\\sqrt{100-64}=6$ cm, tehát $V=\\frac{64\\pi\\cdot6}{3}=128\\pi\\ "
  "\\text{cm}^3$."),

 ("Egy kúpot a magassága <b>felénél</b> elmetszünk az alaplappal párhuzamosan. Hogyan "
  "aránylik a keletkező kis kúp térfogata a csonkakúpéhoz?", None,
  "A hasonlóság aránya $k=\\frac12$, ezért a kis kúp térfogata a teljesnek "
  "$\\left(\\frac12\\right)^3=\\frac18$ része. A csonkakúpra így $\\frac78$ marad, "
  "tehát az arány $\\frac18:\\frac78=\\mathbf{1:7}$."),

 ("Egy csonkakúp sugarai $6$ cm és $2$ cm, magassága $6$ cm. Mekkora annak a kúpnak a "
  "magassága, amelyből a csonkolással keletkezett?", None,
  "A levágott kis kúp és a teljes kúp hasonlóak, a sugarak aránya "
  "$\\frac26=\\frac13$. Ha a teljes kúp magassága $x$, akkor a kis kúpé "
  "$\\frac x3$, és a különbségük a csonkakúp magassága: $x-\\frac x3=6$, ahonnan "
  "$\\frac{2x}{3}=6$ és $x=9$ cm."),

 ("Egy egyenlő oldalú kúp és egy egyenlő oldalú henger alapköre azonos, $r$ sugarú. "
  "Hogyan aránylik a térfogatuk?", None,
  "A kúpnál $H=r\\sqrt3$, tehát $V_{\\text{kúp}}=\\frac{r^2\\pi\\cdot r\\sqrt3}{3}="
  "\\frac{r^3\\pi\\sqrt3}{3}$. A hengernél $H=2r$, tehát "
  "$V_{\\text{henger}}=2r^3\\pi$. Az arány "
  "$\\frac{\\sqrt3}{3}:2=\\sqrt3:6\\approx1:3{,}46$."),

 ("Egy kúp tengelymetszete olyan egyenlő szárú háromszög, amelynek a <b>szárszöge</b> "
  "$90^\\circ$. Mekkora a magassága a sugarához képest, és mekkora a térfogata, ha "
  "$r=6$ cm?", None,
  "A szárszög $90^\\circ$, ezért az alapon fekvő szögek $45^\\circ$-osak, tehát a "
  "magasság és a sugár által alkotott háromszög egyenlő szárú: $H=r$. Így "
  "$H=6$ cm és $V=\\frac{36\\pi\\cdot6}{3}=72\\pi\\ \\text{cm}^3$."),
]

JOKER = ("Egy $20$ cm sugarú körlapból kivágunk egy <b>negyedkörcikket</b>, és <b>abból</b> "
         "hajlítunk tölcsért. Mekkora a tölcsér térfogata? (Adj pontos alakot és "
         "közelítést is!)",
         "A körcikk sugara lesz az <b>alkotó</b>: $s=20$ cm, a középponti szöge "
         "$\\varphi=90^\\circ$.<br>"
         "A $\\varphi=360^\\circ\\cdot\\frac rs$ összefüggésből "
         "$90=360\\cdot\\frac{r}{20}$, tehát $r=5$ cm.<br>"
         "A magasság $H=\\sqrt{400-25}=\\sqrt{375}=5\\sqrt{15}\\approx19{,}36$ cm, "
         "ezért</p>"
         "<p>$$V=\\frac{25\\pi\\cdot5\\sqrt{15}}{3}=\\frac{125\\sqrt{15}}{3}\\pi"
         "\\approx506{,}97\\ \\text{cm}^3.$$</p>"
         "<p>Érdemes megfigyelni, hogy a tölcsér <b>keskeny és mély</b> lett: minél "
         "kisebb a kivágott cikk, annál hegyesebb a tölcsér.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="02-forgastestek", fajl="feladatok-kup.html",
           cim="A kúp és a csonkakúp", temakor="Forgástestek",
           alcim="A kúp elemei, felszíne és térfogata, a henger és a kúp síkmetszetei, "
                 "valamint a csonkakúp. A végeredmény pontos alakban áll ($\\pi$-vel); "
                 "közelítést csak ott adunk, ahol a feladat kéri. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-csonkakup.html", prevc="A csonkakúp",
           nxt="tananyag-gomb.html", nxtc="A gömbfelület és a gömb")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
