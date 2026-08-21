# -*- coding: utf-8 -*-
"""3e/02 — A altema feladatgyujtemeny: forgastestek es a henger.
Jeloles-kanon: r sugar, H testmagassag, s alkoto, B alap, M palast."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (Rational as R, sqrt, pi, simplify, N, symbols, solve, Eq, cbrt)
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

r, x, H = symbols('r x H', positive=True)
B_ = lambda rr: rr**2*pi
M_ = lambda rr, HH: 2*rr*pi*HH
F_ = lambda rr, HH: 2*rr**2*pi + 2*rr*pi*HH
V_ = lambda rr, HH: rr**2*pi*HH

# --- A1: forgatás
chk("a2", [5, 9], [5, 9])
chk("a4-s", sqrt(6**2 + 8**2), 10)
chk("k1-a", V_(6, 4), 144*pi);          chk("k1-b", V_(4, 6), 96*pi)
chk("k1-arany", V_(6, 4)/V_(4, 6), R(3, 2))
chk("k2-a", B_(4)*3/3, 16*pi);          chk("k2-b", B_(3)*4/3, 12*pi)
# --- A2: a henger elemei
chk("a5", 2*7*pi, 14*pi)
chk("a7", 2*6, 12);                     chk("a8", R(14, 2), 7)
chk("a9", [R(8, 2), 5], [4, 5])
chk("k3-r", solve(Eq(2*x*pi, 12*pi), x)[0], 6)
chk("k4-r", solve(Eq(2*x*(2*x), 100), x)[0], 5)
chk("k5-r", solve(Eq(2*(2*x + 5), 30), x)[0], 5)
# --- A3: felszín és térfogat
chk("a10-F", F_(4, 9), 104*pi);         chk("a10-V", V_(4, 9), 144*pi)
chk("a11-M", M_(6, 10), 120*pi);        chk("a11-F", F_(6, 10), 192*pi)
chk("a11-V", V_(6, 10), 360*pi)
chk("a12", V_(3, 5), 45*pi)
chk("a13-F", F_(4, 8), 96*pi);          chk("a13-V", V_(4, 8), 128*pi)
chk("a14", solve(Eq(V_(7, x), 245*pi), x)[0], 5)
chk("a15", solve(Eq(V_(x, 4), 100*pi), x)[0], 5)
chk("a16", solve(Eq(F_(4, x), 112*pi), x)[0], 10)
chk("a17", N(V_(4, 10), 9), 502.654825, 1e-5)
chk("a18", N(V_(2, 5), 9), 62.8318531, 1e-6)
chk("a19", B_(3) + M_(3, 8), 57*pi)
chk("a20", N(M_(1, 4), 9), 25.1327412, 1e-6)
chk("k6", solve(Eq(F_(x, 8), 96*pi), x)[0], 4)
chk("k7", solve(Eq(V_(x, 2*x), 128*pi), x)[0], 4)
chk("k8-r", solve(Eq(F_(x, 3*x), 32*pi), x)[0], 2)
chk("k9", V_(r, 2)/V_(r, 3), R(2, 3))
chk("k10", V_(2, H)/V_(3, H), R(4, 9))
chk("k11-r", solve(Eq(2*x*6, 48), x)[0], 4)
chk("k11-V", V_(4, 6), 96*pi)
chk("k12-r", solve(Eq(2*x**2*pi, 110*pi - 60*pi), x)[0], 5)
chk("k12-H", solve(Eq(M_(5, x), 60*pi), x)[0], 6)
chk("k13-V", V_(R(6, 10), 2), R(72, 100)*pi)
chk("k13-liter", N(V_(R(6, 10), 2)*1000, 9), 2261.94671, 1e-4)
chk("k14", V_(x/2, 4*H)/V_(x, H), 1)
# --- nehéz
chk("n1-r", solve(Eq(F_(x, 2*x), 54*pi), x)[0], 3)
chk("n1-V", V_(3, 6), 54*pi)
chk("n2-a", N(V_(10/pi, 30), 9), 954.929659, 1e-5)
chk("n2-b", N(V_(15/pi, 20), 9), 1432.39449, 1e-4)
chk("n3", B_(5)*3, 75*pi)
chk("n4", solve(Eq(V_(x, x), F_(x, x)), x)[0], 4)
# --- joker: adott V mellett a legkisebb felszín H = 2r-nél
chk("joker-eo", F_(x, 2*x), 6*x**2*pi)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- A1: forgástestek (alap 1–4)
 ("Milyen forgástest keletkezik, ha megforgatjuk",
  ["a téglalapot az egyik oldala körül",
   "a derékszögű háromszöget az egyik befogója körül",
   "a félkört az átmérője körül",
   "a derékszögű trapézt a párhuzamos oldalakra merőleges szára körül"],
  ["henger", "kúp", "gömb", "csonkakúp"], True),

 ("Egy $5\\times9$-es téglalapot megforgatunk a $9$ egység hosszú oldala körül. "
  "Mekkora a keletkező henger alapkörének sugara és a magassága?", None,
  "A tengellyel párhuzamos oldal lesz a magasság, a rá merőleges a sugár: $r=5$ és "
  "$H=9$."),

 ("Milyen síkidom a henger", ["tengelymetszete", "tengelyre merőleges metszete"],
  ["téglalap ($2r$ széles, $H$ magas)", "az alapkörrel egybevágó kör"], True),

 ("Egy derékszögű háromszög befogói $6$ cm és $8$ cm. Megforgatjuk a $6$ cm-es befogója "
  "körül. Milyen test keletkezik, és mekkora a sugara, a magassága és az alkotója?", None,
  "Kúp keletkezik: a tengely a $6$ cm-es befogó, ezért $H=6$ cm és $r=8$ cm. Az alkotó "
  "az átfogó: $s=\\sqrt{36+64}=10$ cm."),

 # --- A2: a henger elemei (alap 5–9)
 ("Egy henger alapkörének sugara $7$ cm, magassága $10$ cm. Mekkora a hálójában szereplő "
  "téglalap két oldala?", None,
  "Az egyik oldal az alapkör kerülete, $2r\\pi=14\\pi$ cm, a másik a magasság, $10$ cm."),

 ("Egy henger alapkörének átmérője $10$ cm, magassága $4$ cm. Mekkora az alkotója?", None,
  "Egyenes hengernél az alkotó megegyezik a magassággal: $s=H=4$ cm. (Az átmérő itt "
  "fölösleges adat.)"),

 ("Egy egyenlő oldalú henger alapkörének sugara $6$ cm. Mekkora a magassága?", None,
  "A tengelymetszet négyzet, ezért $H=2r=12$ cm."),

 ("Egy egyenlő oldalú henger magassága $14$ cm. Mekkora az alapkörének sugara?", None,
  "$H=2r$, ezért $r=7$ cm."),

 ("Egy henger tengelymetszete $8\\ \\text{cm}\\times5\\ \\text{cm}$-es téglalap. "
  "Mekkora a sugara és a magassága?", None,
  "A tengelymetszet egyik oldala az <b>átmérő</b>: $2r=8$, tehát $r=4$ cm; a másik a "
  "magasság: $H=5$ cm."),

 # --- A3: felszín és térfogat (alap 10–20)
 ("Egy henger alapkörének sugara $4$ cm, magassága $9$ cm. Számítsd ki a felszínét és a "
  "térfogatát!", None,
  "$F=2r\\pi(r+H)=8\\pi\\cdot13=104\\pi\\ \\text{cm}^2$, "
  "$V=r^2\\pi H=16\\pi\\cdot9=144\\pi\\ \\text{cm}^3$."),

 ("Egy henger alapkörének sugara $6$ cm, magassága $10$ cm. Mekkora", 
  ["a palástja", "a felszíne", "a térfogata"],
  ["$M=2r\\pi H=120\\pi\\ \\text{cm}^2$", "$F=72\\pi+120\\pi=192\\pi\\ \\text{cm}^2$",
   "$V=36\\pi\\cdot10=360\\pi\\ \\text{cm}^3$"], True),

 ("Mekkora annak a hengernek a térfogata, amelynek az alapköre $3$ cm sugarú, a "
  "magassága pedig $5$ cm?", None,
  "$V=9\\pi\\cdot5=45\\pi\\ \\text{cm}^3$."),

 ("Egy egyenlő oldalú henger alapkörének sugara $4$ cm. Mekkora a felszíne és a "
  "térfogata?", None,
  "Itt $H=2r=8$ cm, ezért $F=2\\cdot16\\pi+2\\cdot4\\pi\\cdot8=96\\pi\\ \\text{cm}^2$ "
  "és $V=16\\pi\\cdot8=128\\pi\\ \\text{cm}^3$."),

 ("Egy henger térfogata $245\\pi\\ \\text{cm}^3$, alapkörének sugara $7$ cm. Mekkora a "
  "magassága?", None,
  "$49\\pi\\cdot H=245\\pi$, ahonnan $H=5$ cm."),

 ("Egy henger térfogata $100\\pi\\ \\text{cm}^3$, magassága $4$ cm. Mekkora az "
  "alapkörének sugara?", None,
  "$r^2\\pi\\cdot4=100\\pi$, tehát $r^2=25$ és $r=5$ cm."),

 ("Egy henger felszíne $112\\pi\\ \\text{cm}^2$, alapkörének sugara $4$ cm. Mekkora a "
  "magassága?", None,
  "$32\\pi+8\\pi H=112\\pi$, ahonnan $8H=80$, tehát $H=10$ cm."),

 ("Egy hengeres pohár alapkörének sugara $4$ cm, magassága $10$ cm. Hány <b>deciliter</b> "
  "fér bele? (A választ két tizedesre kerekítve add meg!)", None,
  "$V=16\\pi\\cdot10=160\\pi\\approx502{,}65\\ \\text{cm}^3$. Mivel "
  "$1\\ \\text{dl}=100\\ \\text{cm}^3$, ez körülbelül $5{,}03$ deciliter."),

 ("Egy hengeres tartály alapkörének sugara $2$ m, magassága $5$ m. Hány köbméter, és "
  "hány <b>liter</b> víz fér bele? (Két tizedesre kerekítve.)", None,
  "$V=4\\pi\\cdot5=20\\pi\\approx62{,}83\\ \\text{m}^3$. Mivel "
  "$1\\ \\text{m}^3=1000$ liter, ez körülbelül $62\\,832$ liter."),

 ("Egy <b>fedél nélküli</b> hengeres tartály alapkörének sugara $3$ dm, magassága "
  "$8$ dm. Hány négyzetdeciméter lemezre van szükség a gyártásához?", None,
  "Csak <b>egy</b> alapkör kell: $F=r^2\\pi+2r\\pi H=9\\pi+48\\pi="
  "57\\pi\\ \\text{dm}^2$."),

 ("Egy hengeres oszlop alapkörének sugara $1$ m, magassága $4$ m. Hány négyzetméter a "
  "<b>palástja</b>? (Két tizedesre kerekítve.)", None,
  "$M=2r\\pi H=8\\pi\\approx25{,}13\\ \\text{m}^2$."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- A1 (közép 1–2)
 ("Egy $4\\times6$-os téglalapot megforgatunk előbb a $4$, majd a $6$ egység hosszú "
  "oldala körül. Melyik henger térfogata nagyobb, és hányszorosa a másikénak?", None,
  "A $4$-es oldal körül $r=6$ és $H=4$, tehát $V_1=36\\pi\\cdot4=144\\pi$; a $6$-os "
  "oldal körül $r=4$ és $H=6$, tehát $V_2=16\\pi\\cdot6=96\\pi$. Az első a nagyobb, "
  "és $\\frac{144\\pi}{96\\pi}=\\frac32$-szerese a másodiknak."),

 ("Egy derékszögű háromszög befogói $3$ cm és $4$ cm. Mekkora a keletkező kúp "
  "térfogata, ha megforgatjuk", ["a $3$ cm-es befogó körül", "a $4$ cm-es befogó körül"],
  ["$r=4$, $H=3$, tehát $V=\\frac{16\\pi\\cdot3}{3}=16\\pi\\ \\text{cm}^3$",
   "$r=3$, $H=4$, tehát $V=\\frac{9\\pi\\cdot4}{3}=12\\pi\\ \\text{cm}^3$"], True),

 # --- A2 (közép 3–5)
 ("Egy henger palástja kiterítve olyan téglalap, amelynek az egyik oldala "
  "$12\\pi$ cm, a másik $7$ cm. Mekkora a henger sugara és magassága?", None,
  "A $12\\pi$ az alapkör kerülete: $2r\\pi=12\\pi$, tehát $r=6$ cm. A magasság a másik "
  "oldal: $H=7$ cm."),

 ("Egy egyenlő oldalú henger tengelymetszetének területe $100\\ \\text{cm}^2$. Mekkora "
  "az alapkörének sugara?", None,
  "A tengelymetszet négyzet, oldala $2r$, ezért $(2r)^2=100$, tehát $2r=10$ és "
  "$r=5$ cm."),

 ("Egy henger tengelymetszetének kerülete $30$ cm, a magassága $5$ cm. Mekkora az "
  "alapkörének sugara?", None,
  "A tengelymetszet téglalap: $2(2r+H)=30$, tehát $2r+5=15$, ahonnan $r=5$ cm."),

 # --- A3 (közép 6–14)
 ("Egy henger felszíne $96\\pi\\ \\text{cm}^2$, magassága $8$ cm. Mekkora az alapkörének "
  "sugara?", None,
  "$2r^2\\pi+16r\\pi=96\\pi$, azaz $r^2+8r-48=0$. A megoldóképlet szerint "
  "$r=\\frac{-8+\\sqrt{64+192}}{2}=\\frac{-8+16}{2}=4$ cm (a negatív gyök nem "
  "sugár)."),

 ("Egy henger térfogata $128\\pi\\ \\text{cm}^3$, a magassága az alapkör sugarának "
  "<b>kétszerese</b>. Mekkora a sugár?", None,
  "$r^2\\pi\\cdot2r=128\\pi$, tehát $r^3=64$ és $r=4$ cm."),

 ("Egy henger magassága az alapkör sugarának <b>háromszorosa</b>, a felszíne "
  "$32\\pi\\ \\text{cm}^2$. Mekkora a sugara és a magassága?", None,
  "$2r^2\\pi+2r\\pi\\cdot3r=8r^2\\pi=32\\pi$, tehát $r^2=4$, azaz $r=2$ cm és "
  "$H=6$ cm."),

 ("Két henger alapköre egyenlő, a magasságuk aránya $2:3$. Hogyan aránylik a "
  "térfogatuk?", None,
  "A térfogat a magassággal <b>egyenesen arányos</b> (a $r^2\\pi$ tényező közös), ezért "
  "a térfogatok aránya is $2:3$."),

 ("Két henger magassága egyenlő, az alapköreik sugarának aránya $2:3$. Hogyan aránylik "
  "a térfogatuk?", None,
  "A sugár <b>négyzetesen</b> szerepel, ezért a térfogatok aránya "
  "$2^2:3^2=4:9$."),

 ("Egy henger tengelymetszetének területe $48\\ \\text{cm}^2$, a magassága $6$ cm. "
  "Mekkora a térfogata?", None,
  "A tengelymetszet téglalap: $2r\\cdot6=48$, tehát $r=4$ cm. Innen "
  "$V=16\\pi\\cdot6=96\\pi\\ \\text{cm}^3$."),

 ("Egy henger palástja $60\\pi\\ \\text{cm}^2$, a felszíne $110\\pi\\ \\text{cm}^2$. "
  "Mekkora a sugara és a magassága?", None,
  "A két alapkör területe $110\\pi-60\\pi=50\\pi$, tehát $2r^2\\pi=50\\pi$, ahonnan "
  "$r=5$ cm. A palástból $2\\cdot5\\pi\\cdot H=60\\pi$, tehát $H=6$ cm."),

 ("Egy hengeres víztartály belső <b>átmérője</b> $1{,}2$ m, magassága $2$ m. Hány liter "
  "víz fér bele? (Egészre kerekítve.)", None,
  "A sugár $r=0{,}6$ m, ezért $V=0{,}36\\pi\\cdot2=0{,}72\\pi\\approx2{,}26\\ "
  "\\text{m}^3$, ami körülbelül $2262$ liter."),

 ("Egy henger alapkörének sugarát a <b>felére</b> csökkentjük, a magasságát pedig a "
  "<b>négyszeresére</b> növeljük. Hogyan változik a térfogata?", None,
  "$\\left(\\frac r2\\right)^2\\pi\\cdot4H=\\frac{r^2}{4}\\pi\\cdot4H=r^2\\pi H$ — a "
  "térfogat <b>nem változik</b>. A sugár negyedelő hatását épp kiegyenlíti a magasság "
  "négyszerezése."),
]

# ============================== NEHÉZ SZINT ==============================
NEHEZ = [
 ("Egy henger felszíne $54\\pi\\ \\text{cm}^2$, és a magassága megegyezik az alapkör "
  "<b>átmérőjével</b>. Mekkora a térfogata?", None,
  "A feltétel szerint $H=2r$, tehát egyenlő oldalú hengerről van szó: "
  "$F=6r^2\\pi=54\\pi$, ahonnan $r=3$ cm és $H=6$ cm. Így "
  "$V=9\\pi\\cdot6=54\\pi\\ \\text{cm}^3$."),

 ("Egy $20\\ \\text{cm}\\times30\\ \\text{cm}$-es téglalapból hengerpalástot hajtunk "
  "össze — ez kétféleképpen lehetséges. Melyik esetben nagyobb a keletkező henger "
  "térfogata, és mennyivel? (Két tizedesre kerekítve.)", None,
  "Ha a $20$ cm-es oldal lesz a kerület: $2r\\pi=20$, tehát $r=\\frac{10}{\\pi}$ és "
  "$H=30$, ezért $V_1=\\frac{100}{\\pi^2}\\pi\\cdot30=\\frac{3000}{\\pi}\\approx"
  "954{,}93\\ \\text{cm}^3$. Ha a $30$ cm-es: $r=\\frac{15}{\\pi}$, $H=20$, ezért "
  "$V_2=\\frac{4500}{\\pi}\\approx1432{,}39\\ \\text{cm}^3$. A <b>szélesebb, "
  "alacsonyabb</b> henger a nagyobb, mégpedig $\\frac{1500}{\\pi}\\approx477{,}46\\ "
  "\\text{cm}^3$-rel."),

 ("Egy $5$ cm sugarú hengeres pohárban a víz $8$ cm magasan áll. Beleteszünk egy testet, "
  "amitől a vízszint $3$ cm-t emelkedik. Mekkora a test térfogata?", None,
  "A kiszorított víz térfogata egy $5$ cm sugarú, $3$ cm magas henger térfogata: "
  "$V=25\\pi\\cdot3=75\\pi\\ \\text{cm}^3$. (A kezdeti $8$ cm fölösleges adat — csak "
  "azt biztosítja, hogy a test elmerüljön.)"),

 ("Egy henger magassága megegyezik az alapkör <b>sugarával</b>, és a felszínének "
  "és a térfogatának a <b>számértéke</b> egyenlő. Mekkora a sugár?", None,
  "Ha $H=r$, akkor $F=2r^2\\pi+2r^2\\pi=4r^2\\pi$ és $V=r^3\\pi$. A számértékek "
  "egyenlőségéből $r^3\\pi=4r^2\\pi$, tehát $r=4$. (A „számérték” megszorítás azért "
  "kell, mert a két mennyiség mértékegysége különböző — az egyenlőség csak a "
  "számokra vonatkozik.)"),
]

JOKER = ("Egy hengeres konzervdoboz térfogata adott. A gyártó a lehető <b>legkevesebb</b> "
         "lemezt akarja felhasználni. Milyen kapcsolat legyen a magasság és a sugár "
         "között? (Elég a sejtésed megfogalmazni és néhány konkrét adattal "
         "alátámasztani.)",
         "A legkedvezőbb az <b>egyenlő oldalú</b> henger, vagyis amikor $H=2r$ — a "
         "doboz pontosan olyan magas, mint amilyen széles.<br>"
         "Próbáld ki $V=54\\pi$ mellett: $r=1$-nél $H=54$ és $F=110\\pi$; $r=3$-nál "
         "$H=6$ és $F=54\\pi$; $r=5$-nél $H=2{,}16$ és $F\\approx71{,}6\\pi$. A "
         "középső, $H=2r$ eset adja a legkisebb felszínt.<br>"
         "A valóságban a dobozok mégis magasabbak ennél: a fedél és az alj vastagabb "
         "lemezből készül, a hengerpalást pedig olcsóbb — a gyártó ezért nem a "
         "geometriai, hanem a <b>költség</b>-optimumot keresi.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="3e", mappa="02-forgastestek", fajl="feladatok-henger.html",
           cim="Feladatok — a henger", temakor="Forgástestek",
           alcim="Forgástestek felismerése, a henger elemei, hálója, felszíne és "
                 "térfogata. A végeredmény pontos alakban áll ($\\pi$-vel); "
                 "közelítést csak ott adunk, ahol a feladat kéri. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-henger-felszin-terfogat.html",
           prevc="A henger felszíne és térfogata",
           nxt="tananyag-kup.html", nxtc="A kúp és elemei")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
