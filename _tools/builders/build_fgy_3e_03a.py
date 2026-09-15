# -*- coding: utf-8 -*-
"""3e/03 — A + C blokk feladatgyujtemeny: ket ismeretlen, Gauss-eljaras, a megoldasok
szama, szoveges feladatok. Horgony-terv: narrativa_03-linearis-rendszerek.md.
M2-korlat: nincs parameteres rendszer, nincs 2x3-as es 3x2-es rendszer."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from tananyag_common import svg_fuggvenyek

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as Q, symbols, linsolve, expand, FiniteSet, EmptySet
x, y, z, t = symbols('x y z t')
E = []


def chk(n, g, w):
    if g != w:
        E.append((n, g, w))


def ls(*eqs, v=(x, y, z)):
    return linsolve([expand(e) for e in eqs], v)


def egy(*eqs, v=(x, y, z)):
    s = ls(*eqs, v=v)
    return tuple(list(s)[0]) if s != EmptySet and len(s) == 1 else s


# --- A1
chk("a1-a", (2*3 - 1, 3 + 3), (5, 6))
chk("a1-b", (2*2 + 1, 2 - 3), (5, -1))
chk("a1-c", (2*1 + 3, 1 - 9), (5, -8))
chk("a2", egy(2*x + y - 16, x - 4*y + 1, v=(x, y)), (7, 2))
chk("a3", egy(3*x - 4*y + 42, 2*x + y - 5, v=(x, y)), (-2, 9))
chk("a4", egy(5*x + 3*y - 19, 5*x - 2*y - 4, v=(x, y)), (2, 3))
chk("a5", egy(x - y + 2, x + y - 4, v=(x, y)), (1, 3))
chk("a6-a", ls(x + y - 3, 2*x + 2*y - 6, v=(x, y)), FiniteSet((3 - y, y)))
chk("a6-b", ls(x + y - 3, x + y - 5, v=(x, y)), EmptySet)
chk("a6-c", egy(x - y - 1, x + y - 3, v=(x, y)), (2, 1))
# --- A2
chk("a8", egy(x + 2*y - z - 3, y + z - 5, 2*z - 6), (2, 2, 3))
chk("a9", egy(x + y + z - 9, x + 2*y + 3*z - 16, x + 3*y + 4*z - 21), (4, 3, 2))
chk("a10", egy(x + y - 5, y + z - 7, x + z - 6), (2, 3, 4))
chk("a11", egy(x + 3*y + 2*z - 11, 2*x + 5*y + 4*z - 20, 3*x + 8*y + 9*z - 37), (1, 2, 2))
chk("a12", egy(2*x + y + z + 9, x - 2*y + z + 11, x + y - 2*z - 4), (-4, 2, -3))
chk("a13", egy(x + 2*y + 3*z - 32, 2*x + y + 3*z - 31, 3*x + 2*y + z - 28), (4, 5, 6))
chk("a14-lepes", expand((2*x + 3*y - z - 4) - 2*(x + 2*y + z - 7)), -y - 3*z + 10)
chk("a14", egy(x + 2*y + z - 7, 2*x + 3*y - z - 4, x - y + 2*z - 7), (2, 1, 3))
# --- A3
chk("a15-c", egy(x + y + z - 4, y - z - 1, 2*z - 6), (-3, 4, 3))
chk("a16", ls(4*x + 8*y + 4*z + 2, 3*x + 6*y + 3*z - 1, x + 2*y + z + 1), EmptySet)
chk("a17", ls(2*x + y - z + 1, -4*x - 2*y + 2*z - 2, x + y + z - 2), FiniteSet((2*z - 3, 5 - 3*z, z)))
chk("a18-a", egy(2*x + y - 5, x - y - 1, v=(x, y)), (2, 1))
chk("a18-b", ls(2*x + y - 5, 2*x + y - 7, v=(x, y)), EmptySet)
chk("a18-c", ls(2*x + y - 5, 4*x + 2*y - 10, v=(x, y)), FiniteSet((Q(5, 2) - y/2, y)))
# --- C1 alap
chk("a19", egy(2*x + 3*y - 480, x + 2*y - 290, v=(x, y)), (90, 100))
chk("a20", egy(x + y - 57, x - y - 13, v=(x, y)), (35, 22))
chk("a21", egy(x + y - 30, 350*x + 250*y - 8400, v=(x, y)), (9, 21))
chk("a22", egy(x - 3*y, x + 12 - 2*(y + 12), v=(x, y)), (36, 12))
chk("a23-a", egy(x + y - 25, 10*x + 20*y - 380, v=(x, y)), (12, 13))
chk("a23-b", egy(2*x + 2*y - 34, x - y - 7, v=(x, y)), (12, 5))
chk("a24", egy(x + y - 11, 10*y + x - (10*x + y) - 27, v=(x, y)), (4, 7))
# --- közép A1
chk("k1", egy(x/2 + y/3 - 4, x/4 - y/6, v=(x, y)), (4, 6))
chk("k2-lin", (expand((x + 4)*(y - 3) - x*y + 22), expand((x - 2)*(y + 2) - x*y)),
    (-3*x + 4*y + 10, 2*x - 2*y - 4))
chk("k2", egy((x + 4)*(y - 3) - x*y + 22, (x - 2)*(y + 2) - x*y, v=(x, y)), (-2, -4))
chk("k3", egy(x - y + 1, 2*x + y - 3, v=(x, y)), (Q(2, 3), Q(5, 3)))
# --- közép A2
chk("k4", egy(x + 2*y - 5*z - 6, 2*x - y - 2*z + 5, 3*x - 3*y + 4*z + 8), (1, 5, 1))
chk("k5", egy(3*x - 5*y + 2*z + 5, 6*x + 2*y - 3*z - 23, 4*x - 3*y - z - 8), (2, 1, -3))
chk("k6", egy(x + 2*y - 7*z - 18, 4*x - 2*y - 3*z - 17, 2*x - 5*y + 8*z + 13), (5, 3, -1))
chk("k7", egy(x - 6*y + 8*z, 2*x + 4*y - 3*z - 26, 3*x - 4*y + 5*z - 18), (8, 4, 2))
chk("k8", egy(2*x - y + 3*z - 20, x + 2*y + 2*z - 7, 3*x + 2*y - z - 1), (3, -2, 4))
chk("k9-lepes", expand((x + 2*y - 3*z + 1) - (x + 2*y + 3*z - 1)), -6*z + 2)
chk("k9", egy(x + 2*y + 3*z - 1, x + 2*y - 3*z + 1, x - 2*y - 6*z + 4), (-1, Q(1, 2), Q(1, 3)))
# --- közép A3
chk("k10-1", expand((2*x - 5*y + 2*z - 3) - 2*(x - 3*y + z - 1)), y - 1)
chk("k10-2", expand((5*x - 9*y + 5*z - 10) - 5*(x - 3*y + z - 1)), 6*y - 5)
chk("k10", ls(x - 3*y + z - 1, 2*x - 5*y + 2*z - 3, 5*x - 9*y + 5*z - 10), EmptySet)
chk("k11-osszeg", expand((x + y - 2*z + 3) + (x - 2*y + z - 2) + (-2*x + y + z - 1)), 0)
chk("k11", ls(x + y - 2*z + 3, x - 2*y + z - 2, -2*x + y + z - 1),
    FiniteSet((z - Q(4, 3), z - Q(5, 3), z)))
chk("k12-osszeg", expand((x + 3*y - 4*z) + (2*x - y + 3*z)), 3*x + 2*y - z)
chk("k12", ls(x + 3*y - 4*z, 2*x - y + 3*z, 3*x + 2*y - z), FiniteSet((-5*z/7, 11*z/7, z)))
chk("k13", ls(x - y - z - 1, x + 3*y + 3*z + 1, x + y + z), FiniteSet((Q(1, 2), -z - Q(1, 2), z)))
# --- közép C1
chk("k14", egy(Q(1, 2)*(x + y) - 60, 3*(x - y) - 60, v=(x, y)), (70, 50))
chk("k15", egy(x + y - 30, Q(20, 100)*x + Q(50, 100)*y - Q(30, 100)*30, v=(x, y)), (20, 10))
chk("k16", egy(x + 5*y - 650, x + 12*y - 1210, v=(x, y)), (250, 80))
chk("k16-b", 250 + 20*80, 1850)
chk("k17", egy(2*x + 3*y + z - 2300, x + 2*y + 2*z - 1900, 3*x + y + z - 2200), (500, 300, 400))
chk("k18", egy(x + y + z - 12, y - x - z, (100*z + 10*y + x) - (100*x + 10*y + z) - 396), (1, 6, 5))
chk("k19", egy(x + y - 12, 5*x + 2*y - 39, v=(x, y)), (5, 7))
# --- nehéz
a, b, c = symbols('a b c')
chk("n1", egy(a + b + c - 2, a - b + c - 6, 4*a + 2*b + c - 3, v=(a, b, c)), (1, -2, 3))
u, v = symbols('u v')
chk("n2", egy(2*u + 3*v - 2, 4*u - 3*v - 1, v=(u, v)), (Q(1, 2), Q(1, 3)))
chk("n3", egy(x + y + z - 500, Q(11, 10)*x + Q(12, 10)*y + z - 540, z - x - y), (100, 150, 250))
chk("n3-szazalek", Q(540 - 500, 500)*100, 8)
chk("n4-S2-S1", expand((2*x - y + z + 1) - (x + y + 2*z + 1)), x - 2*y - z)
chk("n4", ls(x + y + 2*z + 1, 2*x - y + z + 1, x - 2*y - z),
    FiniteSet((-z - Q(2, 3), -z - Q(1, 3), z)))
chk("n4-b", (-(-1) - Q(2, 3), -(-1) - Q(1, 3), -1), (Q(1, 3), Q(2, 3), -1))
chk("n5", egy(x + y + z - 10, 1200*x + 1600*y + 2000*z - 1560*10, x - 2*z), (2, 7, 1))
p = symbols('p')
A_, B_, C_ = 900 + 6*p, 1500 + 3*p, 2700
chk("n6-AB", linsolve([A_ - B_], [p]), FiniteSet((200,)))
chk("n6-BC", linsolve([B_ - C_], [p]), FiniteSet((400,)))
chk("n6-AC", linsolve([A_ - C_], [p]), FiniteSet((300,)))
chk("n6-300", (A_.subs(p, 300), B_.subs(p, 300)), (2700, 2400))
chk("joker", egy(3*x + 2*y + z - 39, 2*x + 3*y + z - 34, x + 2*y + 3*z - 26),
    (Q(37, 4), Q(17, 4), Q(11, 4)))
assert not E, E
print("sympy önteszt: OK")


# ============================== SEGÉDEK ==============================
def rs(*sorok):
    """Egyenletrendszer display-KaTeX-ben, aligned környezetben (a tananyag stílusa)."""
    return "$$\\begin{aligned}" + "\\\\".join(sorok) + "\\end{aligned}$$"


def abra(svg):
    # a duplikált marker-id-t az fgy_common.oldal() szünteti meg (egyedi_id.py)
    return f'<div class="svgwrap">{svg}</div>'


KEK, BORO = "#3b82f6", "#f59e0b"
SVG_A5 = svg_fuggvenyek(
    [(lambda s: s + 2, KEK, "x − y = −2", [(-3, 3)]),
     (lambda s: 4 - s, BORO, "x + y = 4", [(-2.5, 5)])],
    xr=(-3, 5), yr=(-1, 6.5), w=342, h=321,  # 38 px = 1 egység mindkét tengelyen
    leiras="Két metsző egyenes: x − y = −2 és x + y = 4")
SVG_K3 = svg_fuggvenyek(
    [(lambda s: s + 1, KEK, "x − y = −1", [(-2, 2.5)]),
     (lambda s: 3 - 2*s, BORO, "2x + y = 3", [(-1, 2.5)])],
    xr=(-2, 3), yr=(-2, 5), w=258, h=344,  # 44 px = 1 egység mindkét tengelyen
    leiras="Két metsző egyenes: x − y = −1 és 2x + y = 3; a metszéspont nem rácspont")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- A1: két egyenlet, két ismeretlen (alap 1–6)
 ("Melyik számpár megoldása a rendszernek?" + rs(r"2x+y&=5", r"x-3y&=6"),
  ["$(3;-1)$", "$(2;1)$", "$(1;3)$"],
  ["megoldás: $2\\cdot3-1=5$ és $3+3=6$",
   "nem megoldás: az első egyenletet teljesíti, a másodikat nem ($2-3=-1$)",
   "nem megoldás: az első egyenletet teljesíti, a másodikat nem ($1-9=-8$)"], True),

 ("Oldd meg a rendszert behelyettesítéssel!" + rs(r"2x+y&=16", r"x-4y&=-1"), None,
  "$(x;y)=(7;2)$"),

 ("Oldd meg a rendszert az egyenlő együtthatók módszerével!" + rs(r"3x-4y&=-42", r"2x+y&=5"),
  None, "$(x;y)=(-2;9)$"),

 ("Melyik ismeretlent érdemes kiküszöbölni? Oldd meg a rendszert!" +
  rs(r"5x+3y&=19", r"5x-2y&=4"), None,
  "Az $x$-et, mert az együtthatója a két egyenletben egyenlő. A megoldás $(x;y)=(2;3)$."),

 ("Az ábrán az $x-y=-2$ és az $x+y=4$ egyenes látható. Olvasd le az ábráról a rendszer "
  "megoldását, majd ellenőrizd behelyettesítéssel!" + abra(SVG_A5), None,
  "$(x;y)=(1;3)$; ellenőrzés: $1-3=-2$ és $1+3=4$."),

 ("Hány megoldása van a rendszernek? Számolás nélkül, a két egyenes helyzete alapján döntsd el!",
  [rs(r"x+y&=3", r"2x+2y&=6"), rs(r"x+y&=3", r"x+y&=5"), rs(r"x-y&=1", r"x+y&=3")],
  ["végtelen sok: a második egyenlet az első kétszerese, a két egyenes egybeesik",
   "nincs megoldás: a bal oldal azonos, a jobb oldal más, a két egyenes párhuzamos",
   "pontosan egy: a két egyenes se nem párhuzamos, se nem esik egybe, tehát metszik egymást"], True),

 # --- A2: a Gauss-eljárás (alap 7–14)
 ("Maxi a Gauss-eljárás közben az alábbi lépéseket tervezi. Döntsd el mindegyikről, hogy "
  "<b>ekvivalens</b> átalakítás-e, vagyis változatlanul hagyja-e a rendszer megoldáshalmazát!",
  ["felcseréli az első és a második egyenletet",
   "a harmadik egyenletet megszorozza $0$-val",
   "a második egyenletből kivonja az első kétszeresét ($S_2-2S_1$)",
   "az első két egyenletet összeszorozza egymással",
   "a harmadik egyenletet elosztja $-3$-mal"],
  ["ekvivalens",
   "nem ekvivalens: az egyenletből $0=0$ lesz, vagyis elveszítünk egy egyenletet",
   "ekvivalens",
   "nem ekvivalens: a szorzat már nem lineáris egyenlet, és hamis megoldások kerülhetnek be",
   "ekvivalens, mert $-3\\ne0$"]),

 ("A Gauss-eljárás után ez a lépcsős alak maradt. Oldd meg visszahelyettesítéssel!" +
  rs(r"x+2y-z&=3", r"y+z&=5", r"2z&=6"), None,
  "$z=3$, $y=2$, $x=2$, tehát $(x;y;z)=(2;2;3)$."),

 ("Oldd meg a Gauss-eljárással!" + rs(r"x+y+z&=9", r"x+2y+3z&=16", r"x+3y+4z&=21"), None,
  "$(x;y;z)=(4;3;2)$"),

 ("Oldd meg a rendszert! Figyeld meg, hogy mindegyik egyenletből hiányzik egy ismeretlen." +
  rs(r"x+y&=5", r"y+z&=7", r"x+z&=6"), None,
  "$(x;y;z)=(2;3;4)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"x+3y+2z&=11", r"2x+5y+4z&=20", r"3x+8y+9z&=37"), None,
  "$(x;y;z)=(1;2;2)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"2x+y+z&=-9", r"x-2y+z&=-11", r"x+y-2z&=4"), None,
  "$(x;y;z)=(-4;2;-3)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"x+2y+3z&=32", r"2x+y+3z&=31", r"3x+2y+z&=28"), None,
  "$(x;y;z)=(4;5;6)$"),

 ("Maxi a rendszer második egyenletéből kivonta az első kétszeresét, és ezt kapta: "
  "$-y+z=-10$. Hol hibázott? Írd fel a helyes egyenletet, és oldd meg a rendszert!" +
  rs(r"x+2y+z&=7", r"2x+3y-z&=4", r"x-y+2z&=7"), None,
  "A $z$ együtthatójánál: $-1-2\\cdot1=-3$. Helyesen $-y-3z=-10$. "
  "A megoldás $(x;y;z)=(2;1;3)$."),

 # --- A3: hány megoldás van? (alap 15–18)
 ("Egy háromismeretlenes rendszer Gauss-eljárásakor a lépcsős alak felső két sora "
  "$x+y+z=4$ és $y-z=1$ lett. Határozott, határozatlan vagy ellentmondásos a rendszer, "
  "ha a harmadik sor",
  ["$0=0$", "$0=4$", "$2z=6$"],
  ["határozatlan (végtelen sok megoldás)",
   "ellentmondásos (nincs megoldás)",
   "határozott (pontosan egy megoldás)"], True),

 ("Oldd meg a rendszert!" + rs(r"4x+8y+4z&=-2", r"3x+6y+3z&=1", r"x+2y+z&=-1"), None,
  "Nincs megoldás, a rendszer ellentmondásos: például $S_2-3S_3$ után $0=4$ marad."),

 ("Oldd meg a rendszert! Ha végtelen sok megoldása van, add meg őket a $z=t$ jelöléssel." +
  rs(r"2x+y-z&=-1", r"-4x-2y+2z&=2", r"x+y+z&=2"), None,
  "Határozatlan (a második egyenlet az első $(-2)$-szerese): "
  "$(x;y;z)=(2t-3;\\ 5-3t;\\ t)$, ahol $t$ tetszőleges valós szám."),

 ("Írj a $2x+y=5$ egyenlet mellé egy második egyenletet úgy, hogy a kapott rendszernek",
  ["pontosan egy megoldása legyen", "ne legyen megoldása", "végtelen sok megoldása legyen"],
  ["például $x-y=1$, ekkor a megoldás $(2;1)$; minden olyan egyenlet jó, amelynek egyenese "
   "metszi a $2x+y=5$ egyenest",
   "például $2x+y=7$: a bal oldal azonos, a jobb oldal más",
   "például $4x+2y=10$: az eredeti egyenlet kétszerese"]),

 # --- C1: szövegből rendszer (alap 19–24)
 ("Két toll és három füzet együtt $480$ dinárba, egy toll és két füzet $290$ dinárba kerül. "
  "Mennyibe kerül <b>egy toll és egy füzet együtt</b>?", None,
  "Egy toll $90$, egy füzet $100$ dinár, együtt tehát $190$ dinár. "
  "(Rövidebben: a két egyenlet különbsége éppen $x+y=190$.)"),

 ("Két szám összege $57$, a különbségük $13$. Melyik ez a két szám?", None,
  "$35$ és $22$"),

 ("Egy iskolai filmvetítésre $30$ jegyet adtak el, összesen $8400$ dinárért. "
  "A felnőttjegy $350$, a diákjegy $250$ dinárba került. Hány felnőtt- és hány diákjegy kelt el?",
  None, "$9$ felnőttjegy és $21$ diákjegy."),

 ("Egy apa most háromszor annyi idős, mint a fia. $12$ év múlva kétszer annyi idős lesz. "
  "Hány évesek most?", None,
  "Az apa $36$, a fia $12$ éves."),

 ("Írd fel az egyenletrendszert, megoldanod nem kell! Írd le szavakkal is, mit jelölnek "
  "az ismeretlenek.",
  ["Egy perselyben $10$ és $20$ dináros érmék vannak, összesen $25$ darab, $380$ dinár értékben.",
   "Egy téglalap kerülete $34$ cm, és a hosszabb oldala $7$ cm-rel hosszabb a rövidebbnél."],
  ["$x$ a $10$ dinárosok, $y$ a $20$ dinárosok száma: $x+y=25$ és $10x+20y=380$",
   "$a$ a hosszabb, $b$ a rövidebb oldal centiméterben: $2a+2b=34$ és $a=b+7$"]),

 ("Egy kétjegyű szám számjegyeinek összege $11$. Ha a számjegyeit felcseréljük, $27$-tel "
  "nagyobb számot kapunk. Melyik ez a szám?", None,
  "$47$"),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- A1 (közép 1–3)
 ("Oldd meg a rendszert! Előbb szabadulj meg a törtektől." +
  rs(r"\frac{x}{2}+\frac{y}{3}&=4", r"\frac{x}{4}-\frac{y}{6}&=0"), None,
  "$(x;y)=(4;6)$"),

 ("Oldd meg a rendszert! A zárójelek felbontása után lineáris rendszert kapsz." +
  rs(r"(x+4)(y-3)&=xy-22", r"(x-2)(y+2)&=xy"), None,
  "Rendezés után $-3x+4y=-10$ és $x-y=2$; a megoldás $(x;y)=(-2;-4)$."),

 ("Az ábrán az $x-y=-1$ és a $2x+y=3$ egyenes látható." + abra(SVG_K3),
  ["Becsüld meg az ábráról a metszéspontot!", "Számítsd ki a metszéspont pontos koordinátáit!",
   "Miért nem elég ebben az esetben az ábra?"],
  ["körülbelül $(0{,}7;\\ 1{,}7)$",
   "$(x;y)=\\left(\\frac{2}{3};\\ \\frac{5}{3}\\right)$",
   "a metszéspont nem rácspont, ezért az ábráról csak közelítő értéket olvashatunk le"]),

 # --- A2 (közép 4–9)
 ("Oldd meg a Gauss-eljárással!" + rs(r"x+2y-5z&=6", r"2x-y-2z&=-5", r"3x-3y+4z&=-8"), None,
  "$(x;y;z)=(1;5;1)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"3x-5y+2z&=-5", r"6x+2y-3z&=23", r"4x-3y-z&=8"), None,
  "$(x;y;z)=(2;1;-3)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"x+2y-7z&=18", r"4x-2y-3z&=17", r"2x-5y+8z&=-13"), None,
  "$(x;y;z)=(5;3;-1)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"x-6y+8z&=0", r"2x+4y-3z&=26", r"3x-4y+5z&=18"), None,
  "$(x;y;z)=(8;4;2)$"),

 ("Oldd meg a Gauss-eljárással!" + rs(r"2x-y+3z&=20", r"x+2y+2z&=7", r"3x+2y-z&=1"), None,
  "$(x;y;z)=(3;-2;4)$"),

 ("Oldd meg a rendszert! Mielőtt a szokásos lépésekbe kezdenél, nézd meg alaposan az első "
  "két egyenletet." + rs(r"x+2y+3z&=1", r"x+2y-3z&=-1", r"x-2y-6z&=-4"), None,
  "Az első két egyenlet különbségéből egyszerre esik ki az $x$ és az $y$: $6z=2$. "
  "A megoldás $(x;y;z)=\\left(-1;\\ \\frac{1}{2};\\ \\frac{1}{3}\\right)$."),

 # --- A3 (közép 10–13)
 ("Oldd meg a rendszert, és döntsd el, hány megoldása van!" +
  rs(r"x-3y+z&=1", r"2x-5y+2z&=3", r"5x-9y+5z&=10"), None,
  "Nincs megoldás: $S_2-2S_1$ után $y=1$, $S_3-5S_1$ után $6y=5$, és a kettő ellentmond egymásnak."),

 ("Oldd meg a rendszert! Ha végtelen sok megoldása van, add meg őket a $z=t$ jelöléssel." +
  rs(r"x+y-2z&=-3", r"x-2y+z&=2", r"-2x+y+z&=1"), None,
  "Határozatlan (a három egyenlet összege $0=0$): "
  "$(x;y;z)=\\left(t-\\frac{4}{3};\\ t-\\frac{5}{3};\\ t\\right)$."),

 ("Az alábbi rendszerben minden egyenlet jobb oldala $0$." +
  rs(r"x+3y-4z&=0", r"2x-y+3z&=0", r"3x+2y-z&=0"),
  ["Melyik megoldása biztosan van, számolás nélkül?",
   "Van-e más megoldása is? Ha igen, add meg mindet a $z=t$ jelöléssel!"],
  ["a $(0;0;0)$, mert behelyettesítve mindhárom egyenlet $0=0$",
   "igen, végtelen sok, mert a harmadik egyenlet az első kettő összege: "
   "$(x;y;z)=\\left(-\\frac{5t}{7};\\ \\frac{11t}{7};\\ t\\right)$"]),

 ("Oldd meg a rendszert! Melyik ismeretlen értéke egyértelmű, és melyiké nem?" +
  rs(r"x-y-z&=1", r"x+3y+3z&=-1", r"x+y+z&=0"), None,
  "A rendszer határozatlan, de az $x$ egyértelmű: az első és a harmadik egyenlet összegéből "
  "$x=\\frac{1}{2}$. Az $y$ és a $z$ nem egyértelmű: "
  "$(x;y;z)=\\left(\\frac{1}{2};\\ -\\frac{1}{2}-t;\\ t\\right)$."),

 # --- C1 (közép 14–19)
 ("Két autó egymástól $60$ km-re lévő városokból egyszerre indul egymás felé, és fél óra "
  "múlva találkoznak. Ha ugyanabba az irányba indulnának (a gyorsabb hátulról), a gyorsabb "
  "$3$ óra alatt érné utol a lassabbat. Mekkora a két autó sebessége?", None,
  "$70$ km/h és $50$ km/h."),

 ("Hány liter $20\\%$-os és hány liter $50\\%$-os oldatot kell összeöntenünk, hogy $30$ liter "
  "$30\\%$-os oldatot kapjunk?", None,
  "$20$ liter $20\\%$-os és $10$ liter $50\\%$-os oldatot."),

 ("Egy taxi viteldíja alapdíjból és kilométerenként azonos díjból áll. Egy $5$ km-es út "
  "$650$, egy $12$ km-es $1210$ dinárba kerül.",
  ["Mekkora az alapdíj és a kilométerdíj?", "Mennyibe kerül egy $20$ km-es út?"],
  ["az alapdíj $250$ dinár, a kilométerdíj $80$ dinár", "$1850$ dinár"]),

 ("Egy állatkert pénztáránál három család fizetett. Az első $2$ felnőtt-, $3$ diák- és "
  "$1$ nyugdíjasjegyért $2300$ dinárt, a második $1$ felnőtt-, $2$ diák- és $2$ nyugdíjasjegyért "
  "$1900$ dinárt, a harmadik $3$ felnőtt-, $1$ diák- és $1$ nyugdíjasjegyért $2200$ dinárt "
  "fizetett. Mennyibe kerül egy-egy jegy?", None,
  "Felnőttjegy $500$, diákjegy $300$, nyugdíjasjegy $400$ dinár."),

 ("Egy háromjegyű szám számjegyeinek összege $12$. A középső számjegy a két szélső "
  "összegével egyenlő. Ha az első és az utolsó számjegyet felcseréljük, $396$-tal nagyobb "
  "számot kapunk. Melyik ez a szám?", None,
  "$165$"),

 ("Írj szöveges feladatot, amely az $x+y=12$, $5x+2y=39$ rendszerre vezet! Oldd meg a "
  "rendszert, és fogalmazd meg mondatban a választ a saját kérdésedre.", None,
  "A rendszer megoldása $(x;y)=(5;7)$. Egy lehetséges feladat: „Egy perselyben $12$ érme "
  "van, ötdinárosok és kétdinárosok, összesen $39$ dinár értékben. Hány darab van az egyes "
  "fajtákból?” Válasz: $5$ darab ötdináros és $7$ darab kétdináros."),
]

# ============================== NEHÉZ SZINT ==============================
NEHEZ = [
 ("Az $y=ax^2+bx+c$ parabola átmegy az $(1;2)$, a $(-1;6)$ és a $(2;3)$ ponton. "
  "Határozd meg az $a$, $b$ és $c$ együtthatót!", None,
  "$a=1$, $b=-2$, $c=3$, tehát a parabola $y=x^2-2x+3$."),

 ("Oldd meg a rendszert ($x\\ne0$, $y\\ne0$)! Ötlet: legyen $u=\\frac{1}{x}$ és $v=\\frac{1}{y}$." +
  rs(r"\frac{2}{x}+\frac{3}{y}&=2", r"\frac{4}{x}-\frac{3}{y}&=1"), None,
  "$u=\\frac{1}{2}$ és $v=\\frac{1}{3}$, tehát $(x;y)=(2;3)$, ami megfelel a feltételnek."),

 ("Egy kenyér, egy csomag kávé és egy üveg olívaolaj együtt $500$ dinárba került, és az "
  "olaj ára éppen annyi volt, mint a kenyéré és a kávéé együtt. Egy hónap múlva a kenyér "
  "$10\\%$-kal, a kávé $20\\%$-kal drágult, az olaj ára nem változott, így a három együtt "
  "$540$ dinárba került.",
  ["Mennyibe került eredetileg egy-egy termék?",
   "Hány százalékkal drágult a három termék együttes ára?"],
  ["a kenyér $100$, a kávé $150$, az olaj $250$ dinárba (az első és a harmadik feltételből "
   "azonnal adódik, hogy az olaj az $500$ dinár fele)",
   "$8\\%$-kal, mert $\\frac{40}{500}=0{,}08$"]),

 ("Tekintsd a következő rendszert:" +
  rs(r"x+y+2z&=-1", r"2x-y+z&=-1", r"x-2y-z&=0"),
  ["Mutasd meg, hogy végtelen sok megoldása van, és add meg őket a $z=t$ jelöléssel!",
   "A megoldások közül melyikben teljesül, hogy $x+y+z=0$?"],
  ["$S_2-S_1$ éppen a harmadik egyenletet adja, ezért az elhagyható: "
   "$(x;y;z)=\\left(-t-\\frac{2}{3};\\ -t-\\frac{1}{3};\\ t\\right)$",
   "$x+y+z=-t-1=0$, tehát $t=-1$: $(x;y;z)=\\left(\\frac{1}{3};\\ \\frac{2}{3};\\ -1\\right)$"]),

 ("Egy kávépörkölő háromféle kávét kever: kilója rendre $1200$, $1600$ és $2000$ dinár. $10$ kg "
  "keveréket készít, amelynek kilója $1560$ dinár, és a legolcsóbb fajtából kétszer annyit "
  "tesz bele, mint a legdrágábból. Hány kilogramm kell az egyes fajtákból?", None,
  "$2$ kg a $1200$ dinárosból, $7$ kg a $1600$ dinárosból és $1$ kg a $2000$ dinárosból."),

 ("Három mobiltarifa közül lehet választani. Az <b>A</b> havidíja $900$ dinár, és minden "
  "perc $6$ dinár; a <b>B</b> havidíja $1500$ dinár, és minden perc $3$ dinár; a <b>C</b> "
  "havidíja $2700$ dinár, és korlátlanul lehet vele telefonálni. Havi hány perc beszélgetésnél "
  "melyik tarifa a legolcsóbb?", None,
  "Az A és a B $200$ percnél, a B és a C $400$ percnél kerül ugyanannyiba. Ezért $200$ percnél "
  "kevesebb beszélgetésnél az A, $200$ és $400$ perc között a B, $400$ perc fölött a C a "
  "legolcsóbb (a határokon két tarifa egyenlő). Az A és a C $300$ percnél egyenlő, de ott a B "
  "mindkettőnél olcsóbb."),
]

JOKER = ("Kínában mintegy kétezer éve írták a <i>Kilenc fejezet a matematika művészetéről</i> "
         "című könyvet. Ez a feladat is benne van: „$3$ kéve jó, $2$ kéve közepes és $1$ kéve "
         "gyenge rizsből $39$ dou gabona lesz (a dou ókori kínai űrmérték); $2$ jó, $3$ közepes és $1$ gyenge kévéből $34$ "
         "dou; $1$ jó, $2$ közepes és $3$ gyenge kévéből $26$ dou. Mennyi gabonát ad egy-egy "
         "kéve?” A kínai számolók pálcikákkal, egy táblázaton ugyanazokat a lépéseket hajtották "
         "végre, amelyeket mi Gauss-eljárásnak nevezünk. Oldd meg te is!",
         "Egy kéve jó rizs $\\frac{37}{4}=9\\frac{1}{4}$, egy közepes $\\frac{17}{4}=4\\frac{1}{4}$, "
         "egy gyenge $\\frac{11}{4}=2\\frac{3}{4}$ dou gabonát ad.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]
assert (len(ALAP), len(KOZEP)) == (24, 19), (len(ALAP), len(KOZEP))

ut = oldal(tagozat="3e", mappa="03-linearis-rendszerek", fajl="feladatok-rendszerek.html",
           cim="Egyenletrendszerek", temakor="Lineáris egyenletrendszerek",
           alcim="Két és három ismeretlen, a Gauss-eljárás, a megoldások száma és a szöveges "
                 "feladatok. A végeredmény minden feladatnál lenyitható — előbb számolj, csak "
                 "utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-szoveges-feladatok.html", prevc="Szövegből rendszer",
           nxt="feladatok-determinans.html", nxtc="A determináns — feladatok")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
