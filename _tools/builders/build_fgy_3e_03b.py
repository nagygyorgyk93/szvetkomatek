# -*- coding: utf-8 -*-
"""3e/03 — B blokk feladatgyujtemeny: a determinans (B1) es a Cramer-szabaly (B2).
Horgony-terv: narrativa_03-linearis-rendszerek.md. A determinans itt allhat onallo
szamolokartyakent (gyakorlas); felmerore nem kerul onalloan. M2: nincs parameteres rendszer."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as Q, Matrix, symbols, solve, expand, linsolve, FiniteSet, EmptySet
from itertools import permutations
x, y, z, X = symbols('x y z X')
E = []


def chk(n, g, w):
    if g != w:
        E.append((n, g, w))


def det(m):
    return Matrix(m).det()


def cramer(A, b):
    A, b = Matrix(A), Matrix(b)
    ki = [A.det()]
    for j in range(A.shape[1]):
        M = A.copy()
        M[:, j] = b
        ki.append(M.det())
    return tuple(ki)


def megold(A, b):
    return tuple(Matrix(A).LUsolve(Matrix(b)))


# --- B1 alap
chk("a1-a", det([[2, 3], [-1, 5]]), 13)
chk("a1-b", det([[7, -3], [10, -9]]), -33)
chk("a2-a", det([[4, -2], [6, -3]]), 0)
chk("a2-arany", (Q(6, 4), Q(-3, -2)), (Q(3, 2), Q(3, 2)))
chk("a2-b", det([[-1, 5], [2, -3]]), -7)
chk("a3", det([[2, 3, -1], [0, 1, 4], [5, 1, 3]]), 63)
chk("a4", det([[4, 1, 5], [-3, 2, 4], [1, 3, -5]]), -154)
chk("a5", det([[2, 0, 0], [5, 3, 0], [1, 4, -1]]), -6)
chk("a6", det([[1, 0, 2], [3, 0, -1], [4, 5, 6]]), 35)
chk("a6-kifejtes", 5*(-1)**(3+2)*det([[1, 2], [3, -1]]), 35)
chk("a7-a", det([[1, 2, 3], [0, 0, 0], [4, 5, 6]]), 0)
chk("a7-b", det([[2, -1, 4], [2, -1, 4], [3, 7, 1]]), 0)
chk("a7-c", det([[1, 3, -2], [5, 0, 1], [2, 6, -4]]), 0)
chk("a7-d", det([[1, 0, 0], [0, 2, 0], [0, 0, 3]]), 6)
a_, b_, c_, d_, e_, f_, g_, h_, i_ = symbols('a b c d e f g h i')
M0 = Matrix([[a_, b_, c_], [d_, e_, f_], [g_, h_, i_]])
chk("a8-a", expand(Matrix([M0.row(1), M0.row(0), M0.row(2)]).det() + M0.det()), 0)
chk("a8-b", expand(Matrix([M0.row(1), M0.row(2), M0.row(0)]).det() - M0.det()), 0)
chk("a8-c", expand(Matrix([M0.row(0), M0.row(1), M0.row(0) + M0.row(1)]).det()), 0)
# --- B2 alap
chk("a9", cramer([[3, 2], [5, -1]], [7, 3]), (-13, -13, -26))
chk("a9-m", megold([[3, 2], [5, -1]], [7, 3]), (1, 2))
chk("a10", cramer([[4, -3], [2, 5]], [1, -19]), (26, -52, -78))
chk("a10-m", megold([[4, -3], [2, 5]], [1, -19]), (-2, -3))
chk("a12", cramer([[1, 1, 1], [2, 1, 3], [-1, 5, -2]], [6, 13, 3]), (-5, -5, -10, -15))
chk("a12-m", megold([[1, 1, 1], [2, 1, 3], [-1, 5, -2]], [6, 13, 3]), (1, 2, 3))
chk("a13", cramer([[1, 2, 3], [2, -1, 1], [3, 1, -2]], [3, 6, 3]), (30, 60, -30, 30))
chk("a13-m", megold([[1, 2, 3], [2, -1, 1], [3, 1, -2]], [3, 6, 3]), (2, -1, 1))
chk("a14-a", det([[1, 2, -1], [2, 4, -2], [1, -1, 1]]), 0)
chk("a14-b", det([[1, 2, -1], [2, 1, -2], [1, -1, 1]]), -6)
chk("a15", cramer([[2, 1, -1], [1, -1, 2], [3, 2, 1]], [0, 9, 7]), (-10, -20, 10, -30))
chk("a15-m", megold([[2, 1, -1], [1, -1, 2], [3, 2, 1]], [0, 9, 7]), (2, -1, 3))
# --- B1 közép
chk("k1-a", det([[2, 1, 1], [-5, 1, 4], [12, 3, -4]]), -31)
chk("k1-b", det([[2, 1, 3], [5, 3, 2], [1, 4, 3]]), 40)
chk("k2", det([[3, 4, -5], [8, 7, -2], [2, -1, 8]]), 0)
chk("k2-sor", tuple(2*Matrix([[3, 4, -5]]) + Matrix([[2, -1, 8]])), (8, 7, -2))
chk("k3", sorted(solve(det([[X - 2, 3, 1], [1, 5, X - 2], [2, 1, -3]]), X)), [-7, 2])
chk("k4", expand(det([[x - y, -2], [x*y, x - y]])), x**2 + y**2)
# --- B2 közép
chk("k5", cramer([[2, 3, -1], [3, -2, 2], [4, 1, -3]], [1, -1, -11]), (48, -48, 96, 144))
chk("k5-m", megold([[2, 3, -1], [3, -2, 2], [4, 1, -3]], [1, -1, -11]), (-1, 2, 3))
chk("k6", cramer([[2, 1, 1], [4, -3, 1], [6, 2, -1]], [2, 7, -1]), (38, 19, -38, 76))
chk("k6-m", megold([[2, 1, 1], [4, -3, 1], [6, 2, -1]], [2, 7, -1]), (Q(1, 2), -1, 2))
chk("k7", cramer([[1, 1, 1], [2, -1, 1], [1, 2, -1]], [2, 5, -3]), (7, 7, -7, 14))
chk("k7-m", megold([[1, 1, 1], [2, -1, 1], [1, 2, -1]], [2, 5, -3]), (1, -1, 2))
chk("k8-D", det([[1, 1, 2], [2, -1, 1], [4, 1, 5]]), 0)
chk("k8-a", linsolve([x + y + 2*z - 3, 2*x - y + z - 3, 4*x + y + 5*z - 9], [x, y, z]),
    FiniteSet((2 - z, 1 - z, z)))
chk("k8-b", linsolve([x + y + 2*z - 3, 2*x - y + z - 3, 4*x + y + 5*z - 8], [x, y, z]), EmptySet)
chk("k8-b-lepes", (2*3 + 3) - 8, 1)
chk("k9", cramer([[6, 5], [1, -2]], [6, Q(-7, 10)]), (-17, Q(-17, 2), Q(-51, 5)))
chk("k9-m", megold([[6, 5], [1, -2]], [6, Q(-7, 10)]), (Q(1, 2), Q(3, 5)))
chk("k10", cramer([[3, -2], [-1, 4]], [4, 2]), (10, 20, 10))
chk("k10-m", megold([[3, -2], [-1, 4]], [4, 2]), (2, 1))
chk("k11", (Q(24, -12), Q(0, -12), Q(-36, -12)), (-2, 0, 3))
# --- nehéz
chk("n1", cramer([[3, 2, 1], [2, 1, 2], [1, 3, 2]], [330, 320, 400]), (-11, -440, -660, -990))
chk("n1-m", megold([[3, 2, 1], [2, 1, 2], [1, 3, 2]], [330, 320, 400]), (40, 60, 90))
chk("n2", sorted(solve(det([[-1, 4, X + 1], [2, -1, X - 3], [1, X, -1]]), X)), [-2, Q(2, 3)])
chk("n3-D", det([[1, 2, -1], [2, 1, 1], [4, 5, -1]]), 0)
chk("n3", linsolve([x + 2*y - z - 1, 2*x + y + z - 5, 4*x + 5*y - z - 7], [x, y, z]),
    FiniteSet((3 - z, z - 1, z)))
chk("n3-xy", (3 - 2, 2 - 1, 2), (1, 1, 2))
chk("n3-c", linsolve([x + 2*y - z - 1, 2*x + y + z - 5, 4*x + 5*y - z - 8], [x, y, z]), EmptySet)
ertek = [p[0]*p[3] - p[1]*p[2] for p in permutations([1, 2, 3, 4])]
chk("n4", (max(ertek), min(ertek)), (10, -10))
# --- joker: Maxi 4x4-es „Sarrus"-a egy permutációs mátrixon
J = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
le = sum(J[0, k % 4]*J[1, (k+1) % 4]*J[2, (k+2) % 4]*J[3, (k+3) % 4] for k in range(4))
fel = sum(J[0, k % 4]*J[1, (k-1) % 4]*J[2, (k-2) % 4]*J[3, (k-3) % 4] for k in range(4))
chk("joker-maxi", (le, fel), (0, 0))
chk("joker-valodi", J.det(), -1)
assert not E, E
print("sympy önteszt: OK")


# ============================== SEGÉDEK ==============================
def dm(*sorok):
    """Determináns KaTeX-ben: dm("2&3", "-1&5")."""
    return "\\begin{vmatrix}" + "\\\\".join(sorok) + "\\end{vmatrix}"


def rs(*sorok):
    return "$$\\begin{aligned}" + "\\\\".join(sorok) + "\\end{aligned}$$"


# ============================== ALAPSZINT ==============================
ALAP = [
 # --- B1: a determináns (alap 1–8)
 ("Számítsd ki a determinánst!",
  [f"${dm('2&3', '-1&5')}$", f"${dm('7&-3', '10&-9')}$"],
  ["$13$", "$-33$"], True),

 ("Számítsd ki a determinánst!",
  [f"${dm('4&-2', '6&-3')}$", f"${dm('-1&5', '2&-3')}$",
   "Miért jött ki az a) részben $0$?"],
  ["$0$", "$-7$", "mert a második sor az első $\\frac{3}{2}$-szerese: a két sor arányos"]),

 (f"Számítsd ki a determinánst a Sarrus-szabállyal! $${dm('2&3&-1', '0&1&4', '5&1&3')}$$", None,
  "$63$"),

 (f"Számítsd ki a determinánst a Sarrus-szabállyal! $${dm('4&1&5', '-3&2&4', '1&3&-5')}$$", None,
  "$-154$"),

 (f"Melyik sora szerint érdemes kifejteni ezt a determinánst? Számítsd ki! "
  f"$${dm('2&0&0', '5&3&0', '1&4&-1')}$$", None,
  "Az első sora szerint, mert abban két nulla áll. Az értéke $-6$."),

 (f"Melyik oszlopa szerint érdemes kifejteni ezt a determinánst? Számítsd ki! "
  f"$${dm('1&0&2', '3&0&-1', '4&5&6')}$$", None,
  "A második oszlopa szerint, mert abban csak egy elem nem nulla. Az értéke $35$."),

 ("Döntsd el számolás nélkül, mely determinánsok értéke $0$! Válaszodat indokold!",
  [f"${dm('1&2&3', '0&0&0', '4&5&6')}$", f"${dm('2&-1&4', '2&-1&4', '3&7&1')}$",
   f"${dm('1&3&-2', '5&0&1', '2&6&-4')}$", f"${dm('1&0&0', '0&2&0', '0&0&3')}$"],
  ["$0$, mert van csupa nulla sora",
   "$0$, mert két sora egyenlő",
   "$0$, mert a harmadik sora az első kétszerese",
   "nem $0$: a Sarrus-szabállyal csak a főátló szorzata marad, $1\\cdot2\\cdot3=6$"], True),

 (f"Tudjuk, hogy $${dm('a&b&c', 'd&e&f', 'g&h&i')}=7.$$ Mennyi a determináns értéke, ha",
  ["felcseréljük az első két sorát?",
   "előbb az első és a második, majd a második és a harmadik sorát cseréljük fel?",
   "a harmadik sora helyére az első két sor összegét írjuk?"],
  ["$-7$, mert egy sorcsere előjelet vált",
   "$7$, mert két sorcsere kétszer vált előjelet",
   "$0$, mert a harmadik sor az első kettő összege lesz"]),

 # --- B2: a Cramer-szabály (alap 9–16)
 ("Oldd meg a Cramer-szabállyal!" + rs(r"3x+2y&=7", r"5x-y&=3"), None,
  "$D=-13$, $D_x=-13$, $D_y=-26$, tehát $(x;y)=(1;2)$."),

 ("Oldd meg a Cramer-szabállyal!" + rs(r"4x-3y&=1", r"2x+5y&=-19"), None,
  "$D=26$, $D_x=-52$, $D_y=-78$, tehát $(x;y)=(-2;-3)$."),

 ("Írd fel, de ne számítsd ki a $D$, a $D_y$ és a $D_z$ determinánst az alábbi rendszerhez!" +
  rs(r"2x-y+4z&=5", r"x+3z&=-2", r"-3x+2y-z&=7"), None,
  f"$D={dm('2&-1&4', '1&0&3', '-3&2&-1')}$, "
  f"$D_y={dm('2&5&4', '1&-2&3', '-3&7&-1')}$, "
  f"$D_z={dm('2&-1&5', '1&0&-2', '-3&2&7')}$. "
  "A második egyenletből hiányzó $y$ együtthatója $0$."),

 ("Oldd meg a Cramer-szabállyal!" + rs(r"x+y+z&=6", r"2x+y+3z&=13", r"-x+5y-2z&=3"), None,
  "$D=-5$, $D_x=-5$, $D_y=-10$, $D_z=-15$, tehát $(x;y;z)=(1;2;3)$."),

 ("Oldd meg a Cramer-szabállyal!" + rs(r"x+2y+3z&=3", r"2x-y+z&=6", r"3x+y-2z&=3"), None,
  "$D=30$, $D_x=60$, $D_y=-30$, $D_z=30$, tehát $(x;y;z)=(2;-1;1)$."),

 ("Számítsd ki a fő determinánst, és döntsd el, alkalmazható-e a Cramer-szabály!",
  [rs(r"x+2y-z&=3", r"2x+4y-2z&=5", r"x-y+z&=1"),
   rs(r"x+2y-z&=3", r"2x+y-2z&=5", r"x-y+z&=1")],
  ["$D=0$ (az első két sor arányos), tehát nem alkalmazható",
   "$D=-6\\ne0$, tehát alkalmazható"], True),

 ("Ebből a rendszerből csak a $z$ értékére vagyunk kíváncsiak. Melyik két determinánst kell "
  "kiszámítanod? Számítsd ki a $z$-t!" + rs(r"2x+y-z&=0", r"x-y+2z&=9", r"3x+2y+z&=7"), None,
  "Elég a $D$ és a $D_z$: $D=-10$, $D_z=-30$, tehát $z=3$."),

 ("Maxi egy rendszer megoldásakor ezt írta: „$D=0$ és $D_x=0$, tehát "
  "$x=\\frac{D_x}{D}=\\frac{0}{0}=1$.” Mi a hiba? Mit tudunk ilyenkor a rendszer megoldásairól?",
  None,
  "Nullával nem osztunk, a $\\frac{0}{0}$ nem szám. Ha $D=0$, a Cramer-szabály nem "
  "alkalmazható. A rendszer ilyenkor határozatlan vagy ellentmondásos, és hogy melyik, azt a "
  "Gauss-eljárás dönti el."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- B1 (közép 1–4)
 ("Számítsd ki a determinánsokat kétféleképpen: a Sarrus-szabállyal és kifejtéssel is!",
  [f"${dm('2&1&1', '-5&1&4', '12&3&-4')}$", f"${dm('2&1&3', '5&3&2', '1&4&3')}$"],
  ["$-31$", "$40$"], True),

 (f"Tekintsd a következő determinánst: $${dm('3&4&-5', '8&7&-2', '2&-1&8')}$$",
  ["Számítsd ki!",
   "Milyen összefüggés van a sorai között, amely megmagyarázza az eredményt? "
   "(Ötlet: vesd össze a második sort az első kétszeresével.)"],
  ["$0$",
   "a második sor az első sor kétszeresének és a harmadik sornak az összege"]),

 (f"Oldd meg az egyenletet! $${dm('x-2&3&1', '1&5&x-2', '2&1&-3')}=0$$", None,
  "$x=-7$ vagy $x=2$"),

 (f"Számítsd ki, és vond össze a kapott kifejezést! Mikor lehet az értéke $0$, ha $x$ és $y$ "
  f"valós számok? "
  f"$${dm('x-y&-2', 'xy&x-y')}$$", None,
  "$x^2+y^2$. Ez csak akkor $0$, ha $x=0$ és $y=0$, mert két négyzet összege, és egyik tag sem negatív."),

 # --- B2 (közép 5–11)
 ("Rendezd a rendszert, majd oldd meg a Cramer-szabállyal!" + rs(r"2x+3y&=z+1", r"3x+2z&=2y-1", r"4x+y&=3z-11"), None,
  "Rendezve $2x+3y-z=1$, $3x-2y+2z=-1$, $4x+y-3z=-11$; $D=48$, $D_x=-48$, $D_y=96$, $D_z=144$, tehát $(x;y;z)=(-1;2;3)$."),

 ("Oldd meg a Cramer-szabállyal!" + rs(r"2x+y+z&=2", r"4x-3y+z&=7", r"6x+2y-z&=-1"), None,
  "$D=38$, $D_x=19$, $D_y=-38$, $D_z=76$, tehát $(x;y;z)=\\left(\\frac{1}{2};\\ -1;\\ 2\\right)$."),

 ("Oldd meg a rendszert a Gauss-eljárással és a Cramer-szabállyal is! Melyik volt számodra "
  "kevesebb munka, és miért?" + rs(r"x+y+z&=2", r"2x-y+z&=5", r"x+2y-z&=-3"), None,
  "$(x;y;z)=(1;-1;2)$; a Cramer-szabályhoz $D=7$, $D_x=7$, $D_y=-7$, $D_z=14$. Itt jellemzően a "
  "Gauss-eljárás a rövidebb: az első egyenletben minden együttható $1$, így két lépésben "
  "lépcsős alakot kapunk, a Cramer-szabályhoz viszont négy harmadrendű determináns kell."),

 ("Mindkét rendszer fő determinánsa $0$. Döntsd el a Gauss-eljárással, melyik határozatlan "
  "és melyik ellentmondásos! A határozatlannál add meg a megoldásokat a $z=t$ jelöléssel.",
  [rs(r"x+y+2z&=3", r"2x-y+z&=3", r"4x+y+5z&=9"),
   rs(r"x+y+2z&=3", r"2x-y+z&=3", r"4x+y+5z&=8")],
  ["határozatlan (a harmadik egyenlet $2S_1+S_2$): $(x;y;z)=(2-t;\\ 1-t;\\ t)$",
   "ellentmondásos: $S_3-2S_1-S_2$ után $0=-1$"], True),

 ("Oldd meg a Cramer-szabállyal!" + rs(r"6x+5y&=6", r"x-2y&=-\frac{7}{10}"), None,
  "$D=-17$, $D_x=-\\frac{17}{2}$, $D_y=-\\frac{51}{5}$, tehát "
  "$(x;y)=\\left(\\frac{1}{2};\\ \\frac{3}{5}\\right)$."),

 ("Rendezd a rendszert, majd oldd meg a Cramer-szabállyal!" + rs(r"3x&=2y+4", r"4y-2&=x"), None,
  "Rendezve $3x-2y=4$ és $-x+4y=2$; $D=10$, $D_x=20$, $D_y=10$, tehát $(x;y)=(2;1)$."),

 ("Egy háromismeretlenes rendszerről ezt tudjuk: $D=-12$, $D_x=24$, $D_y=0$, $D_z=-36$.",
  ["Add meg a rendszer megoldását!",
   "Mit mondhatsz, ha egy másik rendszernél $D=0$?"],
  ["$(x;y;z)=(-2;0;3)$",
   "a Cramer-szabály nem alkalmazható; a rendszer határozatlan vagy ellentmondásos, és ezt a "
   "Gauss-eljárással kell eldönteni"]),
]

# ============================== NEHÉZ SZINT ==============================
NEHEZ = [
 ("Egy pékségben három vásárló fizetett. Az első $3$ kifliért, $2$ pogácsáért és $1$ perecért "
  "$330$ dinárt, a második $2$ kifliért, $1$ pogácsáért és $2$ perecért $320$ dinárt, a harmadik "
  "$1$ kifliért, $3$ pogácsáért és $2$ perecért $400$ dinárt fizetett. Mennyibe kerül egy perec? "
  "Használd a Cramer-szabályt, és csak azokat a determinánsokat számítsd ki, amelyekre "
  "valóban szükség van!", None,
  "Ha $x$ a kifli, $y$ a pogácsa, $z$ a perec ára, elég a $D$ és a $D_z$: $D=-11$, "
  "$D_z=-990$, tehát egy perec $90$ dinár."),

 (f"Oldd meg az egyenletet! $${dm('-1&4&x+1', '2&-1&x-3', '1&x&-1')}=0$$", None,
  "$x=-2$ vagy $x=\\frac{2}{3}$"),

 ("Tekintsd a következő rendszert:" + rs(r"x+2y-z&=1", r"2x+y+z&=5", r"4x+5y-z&=7"),
  ["Próbáld megoldani a Cramer-szabállyal! Mit tapasztalsz?",
   "Hány megoldása van a rendszernek? Ha végtelen sok, add meg őket a $z=t$ jelöléssel!",
   "A megoldások közül melyikben lesz $x=y$?",
   "Mire kellene kicserélni a harmadik egyenlet jobb oldalán álló $7$-et, hogy a rendszernek "
   "ne legyen megoldása?"],
  ["$D=0$ (a harmadik sor az első kétszeresének és a második sornak az összege), tehát a "
   "Cramer-szabály nem alkalmazható",
   "végtelen sok: $(x;y;z)=(3-t;\\ t-1;\\ t)$",
   "$3-t=t-1$, tehát $t=2$: $(x;y;z)=(1;1;2)$",
   "bármely $7$-től különböző számra, például $8$-ra: ekkor $S_3-2S_1-S_2$ után $0=1$"]),

 ("Egy másodrendű determináns négy eleme az $1$, a $2$, a $3$ és a $4$, mindegyik "
  "pontosan egyszer. Mekkora a determináns lehető legnagyobb és lehető legkisebb értéke? Indokold!",
  None,
  "A legnagyobb érték $10$, például $\\begin{vmatrix}4&1\\\\2&3\\end{vmatrix}=4\\cdot3-1\\cdot2=10$: a "
  "főátlóba a két legnagyobb, a mellékátlóba a két legkisebb szám kerül. A legkisebb érték "
  "$-10$, a két sor felcserélésével."),
]

JOKER = (f"Maxi szerint a Sarrus-szabály $4\\times4$-es determinánsra is működik: mellé írja az "
         f"első három oszlopot, és négy lefelé haladó átló szorzatát összeadja, négy fölfelé "
         f"haladóét kivonja. Mutasd meg egy olyan $4\\times4$-es determinánson, amelyet "
         f"kifejtéssel könnyen ki tudsz számolni, hogy Maxi szabálya rossz eredményt ad! "
         f"(Ötlet: a kifejtés $4\\times4$-es determinánsra is ugyanúgy működik, mint $3\\times3$-asra, "
         f"csak az aldeterminánsok harmadrendűek. Próbálkozz sok nullát tartalmazó determinánssal!)",
         f"Egy jó ellenpélda: $${dm('1&0&0&0', '0&0&1&0', '0&1&0&0', '0&0&0&1')}$$ "
         f"Az első sor szerint kifejtve az értéke $1\\cdot{dm('0&1&0', '1&0&0', '0&0&1')}=-1$. "
         f"Maxi nyolc átlója közül mindegyikben van nulla, ezért nála $0$ jön ki. A hiba oka: a "
         f"$4\\times4$-es determináns $24$ tagból áll, az átlók viszont csak $8$-at adnak.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]
assert (len(ALAP), len(KOZEP)) == (16, 11), (len(ALAP), len(KOZEP))

ut = oldal(tagozat="3e", mappa="03-linearis-rendszerek", fajl="feladatok-determinans.html",
           cim="A determináns és a Cramer-szabály", temakor="Lineáris egyenletrendszerek",
           alcim="Másod- és harmadrendű determináns, Sarrus-szabály, kifejtés, a determináns "
                 "tulajdonságai, a Cramer-szabály és a korlátja. A végeredmény minden feladatnál "
                 "lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="feladatok-rendszerek.html", prevc="Egyenletrendszerek — feladatok",
           nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
