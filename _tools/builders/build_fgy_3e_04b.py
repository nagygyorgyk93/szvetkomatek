# -*- coding: utf-8 -*-
"""3e/04 — B + C blokk feladatgyujtemeny: skalaris szorzat, vektorialis szorzat, alkalmazasok.
Horgony-terv: narrativa_04-vektorok.md · feladat-terkep: terkep_fgy_04-vektorok.md.
Ero/munka: csak alap-21 es alap-22 (felhasznaloi dontes). M2: nincs vegyes szorzat."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Matrix, sqrt, cos, sin, acos, pi, Rational as Q, symbols, solve, simplify, N
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(x, y) for x, y in zip(g, w))
    if hasattr(g, "shape"):
        return g.shape == w.shape and all(simplify(x - y) == 0 for x, y in zip(g, w))
    return simplify(g - w) == 0


def chk(n, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((n, g, w))


def V(*k):
    return Matrix(k)


def fok(x, y):
    return acos(x.dot(y) / (x.norm() * y.norm())) * 180 / pi


t, k, x_ = symbols("t k x")
I, J, K_ = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
O3 = V(0, 0, 0)
# B1 alap
chk("a1", [20*cos(pi/3), 20*cos(pi/2), 20*cos(2*pi/3), 20*cos(pi)], [10, 0, -10, -20])
chk("a2", [4*cos(pi/3), 4*cos(2*pi/3)], [2, -2])
chk("a3", [V(1, 2, 5).dot(V(-1, 3, -7)), V(0, 2, 3).dot(V(-2, 1, 3)), V(2, 3, 4).dot(V(5, 7, -1))],
    [-30, 11, 27])
chk("a4", [V(2, -1, 3).dot(V(1, 4, 1)), V(3, 0, -2).dot(V(2, 5, 3)), V(1, 1, 1).dot(V(-2, 0, 1))],
    [1, 0, -1])
chk("a5", solve(V(1, -1, 2).dot(V(5, -1, x_)), x_), [-3])
chk("a6", [fok(V(8, 2, 2), V(4, -4, 0)), fok(V(-1, 1, 0), V(-1, 2, -2))], [60, 45])
chk("a6-c", fok(V(1, 2, 3), V(5, 4, -7)), 103.0, 0.05); chk("a6-c-sk", V(1, 2, 3).dot(V(5, 4, -7)), -8)
chk("a7", [12*cos(2*pi/3), 2*9 + 12*cos(2*pi/3)], [-6, 12])
# B2 alap
chk("a9", [6*sin(pi/4), 6*sin(pi/2), 6*sin(0)], [3*sqrt(2), 6, 0]); chk("a9-k", 3*sqrt(2), 4.24, 0.005)
p = V(1, 2, 1).cross(V(2, 3, -2))
chk("a10", [p, p.norm(), V(-2, 7, -8).cross(V(1, 7, -9))], [V(-7, 4, -1), sqrt(66), V(-7, -26, -21)])
chk("a10-k", sqrt(66), 8.12, 0.005)
chk("a10-b-h", V(-7, -26, -21).norm(), 34.15, 0.005)
chk("k17-sz", [(V(-2, 3, -4) - V(-3, 3, -4)).cross(V(-1, -2, 2) - V(-3, 3, -4)), (V(-1, -2, 2) - V(-2, 3, -4)).norm(), (V(-1, -2, 2) - V(-3, 3, -4)).norm()], [V(0, -6, -5), sqrt(62), sqrt(65)])
chk("a11", [I.cross(K_), (2*I).cross(3*J), (I + J).cross(K_)], [-J, 6*K_, V(1, -1, 0)])
ab = V(2, -1, 4)
chk("a12", [-ab, 3*ab, -2*ab], [V(-2, 1, -4), V(6, -3, 12), V(-4, 2, -8)])
p = V(-1, -4, 3).cross(V(-2, 3, 6))
chk("a13", [p, p.norm()], [V(-33, 0, -11), 11*sqrt(10)]); chk("a13-k", 11*sqrt(10), 34.79, 0.005)
A, B, C = V(5, -3, -4), V(5, 7, -9), V(3, -7, 2)
p = (B - A).cross(C - A)
chk("a14", [B - A, C - A, p, p.norm() / 2], [V(0, 10, -5), V(-2, -4, 6), V(40, 10, 20), 5*sqrt(21)])
chk("a14-k", 5*sqrt(21), 22.91, 0.005)
n = V(1, 0, 2).cross(V(0, 1, -1))
chk("a15", [n, n.dot(V(1, 0, 2)), n.dot(V(0, 1, -1))], [V(-2, 1, 1), 0, 0])
chk("a16", [V(2, -4, 6).cross(V(-1, 2, -3)), V(2, -4, 6).cross(V(1, 2, 3))], [O3, V(-24, 0, 8)])
# C1 alap
Ep, F, G = V(2, 3, 4), V(-2, 3, 1), V(3, -4, 2)
chk("a17", [(F - Ep).norm(), (G - F).norm(), (G - Ep).norm()], [5, 5*sqrt(3), 3*sqrt(6)])
chk("a17-k", 5 + 5*sqrt(3) + 3*sqrt(6), 21.01, 0.005); chk("a17-szog", fok(F - Ep, G - Ep), 86.9, 0.05)
chk("a17-sk", (F - Ep).dot(G - Ep), 2)
A, B, C = V(1, 0, 1), V(3, 1, 3), V(0, 2, 1)
chk("a18", [(B - A).dot(C - A), (B - A).norm(), (C - A).norm(), (B - A).cross(C - A).norm() / 2],
    [0, 3, sqrt(5), 3*sqrt(5)/2]); chk("a18-k", 3*sqrt(5)/2, 3.35, 0.005)
A, B, C, D = V(1, 1, 0), V(3, 2, 2), V(4, 0, 2), V(2, -1, 0)
chk("a19", [B - A, C - D, (B - A).dot(D - A), (B - A).norm(), (D - A).norm(), (B - A).cross(D - A).norm()],
    [V(2, 1, 2), V(2, 1, 2), 0, 3, sqrt(5), 3*sqrt(5)]); chk("a19-k", 3*sqrt(5), 6.71, 0.005)
a, b, c = V(-2, 3, 6), V(6, -2, 3), V(3, 6, -2)
chk("a20", [a.dot(b), b.dot(c), a.dot(c), a.norm(), b.norm(), c.norm()], [0, 0, 0, 7, 7, 7])
R = V(3, -2, 4) + V(1, 5, -1) + V(-2, 1, 1)
chk("a21", [R, R.norm()], [V(2, 4, 4), 6])
chk("a22", V(2, 3, 1).dot(V(5, 0, -2)), 8)
chk("a21-szog", acos(Q(2, 6)) * 180 / pi, 70.5, 0.05)
chk("k6-nemnegyzet", (V(1, -4, 4) - V(1, -2, 3)).dot(V(3, -1, 3) - V(1, -2, 3)), -2)
chk("a19-nemparh", V(2, 1, 2).cross(V(1, -2, 0)) != O3, True)
# B1 közép
chk("k1", [sqrt(9 + 16 + 2*(-6)), 3*9 + 6*(-6) - 2*(-6) - 4*16], [sqrt(13), -61]); chk("k1-k", sqrt(13), 3.61, 0.005)
chk("k2", sorted(solve(V(t, t + 1, 1).dot(V(t, 2, -5)), t)), [-3, 1])
chk("k3", sorted(solve((V(1, 2, 3) + k*V(k, 1, -1)).dot(V(-1, 0, 1)), k)), [-2, 1])
chk("k4", solve(V(-1, -4, x_).dot(V(2, 1, -2)), x_), [-3])
chk("k5", fok(V(1, 7, 2) - V(1, 3, 2), V(1, 5, 4) - V(1, 3, 2)), 45)
A, B, C = V(1, 0, -1), V(1, -1, 3), V(-7, 2, 1)
chk("k5-b", fok(A - B, C - B), 72.3, 0.05); chk("k5-b-sk", (A - B).dot(C - B), 11)
A, B, C = V(1, -2, 3), V(1, -4, 4), V(3, -3, 4)
D = A + C - B
chk("k6", [D, (C - A).dot(D - B), (B - A).norm(), (D - A).norm()], [V(3, -1, 3), 0, sqrt(5), sqrt(5)])
# B2 közép
chk("k7", [2*12, 5*12], [24, 60])
a, b = V(3, 0, 0), V(0, 4, 0)                     # általános ellenőrzés merőleges példával
chk("k7-gen", [((a + b).cross(a - b)).norm(), ((3*a - b).cross(a - 2*b)).norm()], [24, 60])
a, b = V(2, 1, -1), V(1, -1, 2)
chk("k8", [a.cross(b), (2*a + b).cross(b), (2*a - b).cross(2*a + b)],
    [V(1, -5, -3), V(2, -10, -6), V(4, -20, -12)])
A, B, C = V(2, -3, 4), V(5, 3, -4), V(6, -7, 2)
p = (B - A).cross(C - A)
chk("k9", [p, p.norm() / 2, (C - A).norm()], [V(-44, -26, -36), sqrt(977), 6])
chk("k9-T", sqrt(977), 31.26, 0.005); chk("k9-m", sqrt(977)/3, 10.42, 0.005)
chk("k9-C", fok(A - C, B - C), 62.9, 0.05)
A, B, D = V(2, 1, 0), V(3, 3, 1), V(1, 2, 2)
p = (B - A).cross(D - A)
chk("k10", [B + D - A, p, p.norm()], [V(2, 4, 3), V(3, -3, 3), 3*sqrt(3)]); chk("k10-k", 3*sqrt(3), 5.20, 0.005)
p = V(1, 2, 2).cross(V(2, 1, -2))
chk("k11", [p, p.norm(), p / 9], [V(-6, 6, -3), 9, V(Q(-2, 3), Q(2, 3), Q(-1, 3))])
A, B, C = V(1, 2, 3), V(3, 5, 4), V(7, 11, 6)
chk("k12", [(B - A).cross(C - A), C - A], [O3, 3*(B - A)])
chk("k12-t", (B - A).cross(V(7, t, 6) - A), V(11 - t, 0, 2*t - 22)); chk("k12-t2", solve(11 - t, t), [11])
# C1 közép
K, L, M = V(2, -3, -4), V(1, 3, -4), V(6, -5, -2)
p = (L - K).cross(M - K)
chk("k13", [p, p.norm() / 2, (M - L).norm()], [V(12, 2, -22), sqrt(158), sqrt(93)])
chk("k13-T", sqrt(158), 12.57, 0.005); chk("k13-m", 2*sqrt(158)/sqrt(93), 2.61, 0.005)
chk("k13-L", fok(K - L, M - L), 25.4, 0.05)
A, B, C = V(2, 1, -2), V(4, 0, -1), V(4, 3, 2)
D = A + C - B
chk("k14", [D, C - A, D - B, fok(C - A, D - B), (B - A).cross(D - A).norm()],
    [V(2, 4, 1), V(2, 2, 4), V(-2, 4, 2), 60, 6*sqrt(3)]); chk("k14-k", 6*sqrt(3), 10.39, 0.005)
A, C = V(1, 2, 0), V(0, 4, 2)
chk("k15-t", solve((V(3, t, 1) - A).dot(C - A), t), [2])
p = (V(3, 2, 1) - A).cross(C - A)
chk("k15", [p, p.norm() / 2], [V(-2, -5, 4), 3*sqrt(5)/2])
a, b, c = V(-8, 2, 4), V(2, -4, 8), V(-4, 8, -2)
chk("k16", [a.norm(), b.norm(), c.norm(), a.dot(b)], [2*sqrt(21)] * 3 + [8])
A, B, C = V(-3, 3, -4), V(-2, 3, -4), V(1, -7, 8)
G = (A + C) / 2
chk("k17", G, V(-1, -2, 2)); chk("k17-T", (B - A).cross(G - A).norm() / 2, 3.91, 0.005)
chk("k17-K", (B - A).norm() + (G - B).norm() + (G - A).norm(), 16.94, 0.005)
P, Q_, R_ = V(1, 2, -1), V(3, 1, 1), V(0, 4, 2)
chk("k18", [(Q_ - P).dot(R_ - Q_), (P - Q_).dot(R_ - Q_), (P - Q_).norm(), (R_ - Q_).norm()],
    [-7, 7, 3, sqrt(19)])
chk("k18-rossz", fok(Q_ - P, R_ - Q_), 122.4, 0.05); chk("k18-jo", fok(P - Q_, R_ - Q_), 57.6, 0.05)
# nehéz
chk("n1", [4 + 9 + 2*3, 4 + 9 - 2*3, 4 - 9], [19, 7, -5])
chk("n1-szog", acos(-5 / sqrt(133)) * 180 / pi, 115.7, 0.05)
a, b = V(6, 2, -3), V(-3, 6, -2)
p = a.cross(b)
chk("n3", [a.dot(b), a.norm(), b.norm(), p, p / 7], [0, 7, 7, V(14, 21, 42), V(2, 3, 6)])
chk("n4", sorted(solve(5*t**2 + 4 - 49, t)), [-3, 3])
chk("n4-kereszt", (V(0, 2, 0) - V(1, 0, 0)).cross(V(0, 0, t) - V(1, 0, 0)), V(2*t, t, 2))
# joker
chk("jok", [I.cross(I.cross(J)), (I.cross(I)).cross(J)], [-J, O3])
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- B1: skaláris szorzat (alap 1–8)
 (r"Az $\vec a$ intenzitása $4$, a $\vec b$ intenzitása $5$. Mennyi az $\vec a\cdot\vec b$ skaláris "
  r"szorzat, ha a két vektor szöge",
  [r"$60^\circ$;", r"$90^\circ$;", r"$120^\circ$;", r"$180^\circ$?"],
  [r"$4\cdot5\cdot\tfrac12=10$", r"$0$", r"$-10$", r"$-20$"], True),

 (r"Az $ABC$ szabályos háromszög oldala $2$ egység. Számítsd ki!",
  [r"$\overrightarrow{AB}\cdot\overrightarrow{AC}$", r"$\overrightarrow{AB}\cdot\overrightarrow{BC}$"],
  [r"a szög $60^\circ$: $2\cdot2\cdot\tfrac12=2$",
   r"a szög $120^\circ$ (közös kezdőpontba tolva!): $2\cdot2\cdot\left(-\tfrac12\right)=-2$"], True),

 (r"Számítsd ki az $\vec a$ és a $\vec b$ vektor skaláris szorzatát!",
  [r"$\vec a=(1;2;5)$, $\vec b=(-1;3;-7)$", r"$\vec a=(0;2;3)$, $\vec b=(-2;1;3)$",
   r"$\vec a=2\vec i+3\vec j+4\vec k$, $\vec b=5\vec i+7\vec j-\vec k$"],
  [r"$-1+6-35=-30$", r"$0+2+9=11$", r"$10+21-4=27$"]),

 (r"A skaláris szorzat előjele alapján döntsd el, hegyesszöget, derékszöget vagy tompaszöget "
  r"zár-e be a két vektor!",
  [r"$(2;-1;3)$ és $(1;4;1)$", r"$(3;0;-2)$ és $(2;5;3)$", r"$(1;1;1)$ és $(-2;0;1)$"],
  [r"a szorzat $1>0$, és a vektorok nem párhuzamosak: hegyesszöget", r"a szorzat $0$: derékszöget",
   r"a szorzat $-1\lt 0$, és a vektorok nem párhuzamosak: tompaszöget"]),

 (r"Adott az $\vec a=(1;-1;2)$ vektor. Határozd meg a $\vec b=(5;-1;z)$ vektor harmadik "
  r"koordinátáját úgy, hogy $\vec b$ merőleges legyen $\vec a$-ra!", None,
  r"$\vec a\cdot\vec b=5+1+2z=0$, tehát $z=-3$."),

 (r"Mekkora szöget zár be a két vektor? A nem nevezetes szöget számológéppel, egy tizedesre "
  r"kerekítve add meg!",
  [r"$\vec a=(8;2;2)$ és $\vec b=(4;-4;0)$", r"$\vec a=-\vec i+\vec j$ és $\vec b=-\vec i+2\vec j-2\vec k$",
   r"$\vec a=(1;2;3)$ és $\vec b=(5;4;-7)$"],
  [r"$\cos\varphi=\frac{24}{\sqrt{72}\cdot\sqrt{32}}=\frac12$, tehát $\varphi=60^\circ$",
   r"$\cos\varphi=\frac{3}{\sqrt2\cdot3}=\frac{\sqrt2}{2}$, tehát $\varphi=45^\circ$",
   r"$\vec a\cdot\vec b=-8$, $\cos\varphi=\frac{-8}{\sqrt{14}\cdot\sqrt{90}}\approx-0{,}2254$, "
   r"tehát $\varphi\approx103{,}0^\circ$"]),

 (r"Az $\vec a$ intenzitása $3$, a $\vec b$ intenzitása $4$, a szögük $120^\circ$. Számítsd ki!",
  [r"$\vec a\cdot\vec b$", r"$\vec a\cdot(2\vec a+\vec b)$"],
  [r"$3\cdot4\cdot\left(-\tfrac12\right)=-6$",
   r"$2\,\vec a\cdot\vec a+\vec a\cdot\vec b=2\cdot9-6=12$"], True),

 (r"Döntsd el, igaz-e az állítás, és indokold!",
  [r"$\vec a\cdot\vec b=\vec b\cdot\vec a$ bármely két vektorra.",
   r"Két vektor skaláris szorzata egy vektor.",
   r"Ha $\vec a\cdot\vec b=0$, akkor $\vec a$ vagy $\vec b$ a nullvektor.",
   r"$\vec a\cdot\vec a\ge0$ bármely vektorra."],
  [r"igaz: a skaláris szorzat kommutatív",
   r"hamis: a skaláris szorzat szám",
   r"hamis: két merőleges, nem nullvektor szorzata is $0$",
   r"igaz: $\vec a\cdot\vec a=|\vec a|^2$"]),

 # --- B2: vektoriális szorzat (alap 9–16)
 (r"Az $\vec a$ intenzitása $2$, a $\vec b$ intenzitása $3$. Mekkora $|\vec a\times\vec b|$, ha a két "
  r"vektor szöge",
  [r"$45^\circ$;", r"$90^\circ$;", r"$0^\circ$?"],
  [r"$6\sin45^\circ=3\sqrt2\approx4{,}24$", r"$6$", r"$0$ (párhuzamos vektorok)"], True),

 (r"Határozd meg az $\vec a\times\vec b$ vektort és az intenzitását!",
  [r"$\vec a=\vec i+2\vec j+\vec k$, $\vec b=2\vec i+3\vec j-2\vec k$",
   r"$\vec a=(-2;7;-8)$, $\vec b=(1;7;-9)$"],
  [r"$(-7;4;-1)$, intenzitása $\sqrt{66}\approx8{,}12$",
   r"$(-7;-26;-21)$, intenzitása $\sqrt{1166}\approx34{,}15$"]),

 (r"Számítsd ki a vektoriális szorzatokat!",
  [r"$\vec i\times\vec k$", r"$(2\vec i)\times(3\vec j)$", r"$(\vec i+\vec j)\times\vec k$"],
  [r"$-\vec j$", r"$6\vec k$", r"$\vec i\times\vec k+\vec j\times\vec k=-\vec j+\vec i=(1;-1;0)$"], True),

 (r"Tudjuk, hogy $\vec a\times\vec b=(2;-1;4)$. Mivel egyenlő",
  [r"$\vec b\times\vec a$;", r"$(3\vec a)\times\vec b$;", r"$\vec a\times(-2\vec b)$;", r"$\vec a\times\vec a$?"],
  [r"$(-2;1;-4)$", r"$(6;-3;12)$", r"$(-4;2;-8)$", r"$\vec 0=(0;0;0)$"], True),

 (r"Számítsd ki az $\vec a=(-1;-4;3)$ és a $\vec b=(-2;3;6)$ vektor által kifeszített "
  r"paralelogramma területét!", None,
  r"$\vec a\times\vec b=(-33;0;-11)$, így $T=\sqrt{1089+121}=\sqrt{1210}=11\sqrt{10}\approx34{,}79$."),

 (r"Számítsd ki az $A(5;-3;-4)$, $B(5;7;-9)$, $C(3;-7;2)$ csúcsú háromszög területét!", None,
  r"$\overrightarrow{AB}=(0;10;-5)$, $\overrightarrow{AC}=(-2;-4;6)$, "
  r"$\overrightarrow{AB}\times\overrightarrow{AC}=(40;10;20)$, intenzitása $\sqrt{2100}=10\sqrt{21}$, "
  r"így $T=5\sqrt{21}\approx22{,}91$."),

 (r"Adj meg egy olyan nem nulla vektort, amely merőleges az $\vec a=(1;0;2)$ és a $\vec b=(0;1;-1)$ vektorra "
  r"is, majd a skaláris szorzattal ellenőrizd!", None,
  r"$\vec n=\vec a\times\vec b=(-2;1;1)$. Ellenőrzés: $\vec n\cdot\vec a=-2+0+2=0$ és "
  r"$\vec n\cdot\vec b=0+1-1=0$. (Bármely nem nulla számszorosa is jó.)"),

 (r"A vektoriális szorzattal döntsd el, párhuzamos-e az $\vec a=(2;-4;6)$ vektorral",
  [r"a $\vec b=(-1;2;-3)$;", r"a $\vec c=(1;2;3)$!"],
  [r"$\vec a\times\vec b=(0;0;0)$: párhuzamos", r"$\vec a\times\vec c=(-24;0;8)\ne\vec 0$: nem párhuzamos"]),

 # --- C1: alkalmazások (alap 17–22)
 (r"Számítsd ki a háromszög megadott szögét!",
  [r"$A(1;3;2)$, $B(1;7;2)$, $C(1;5;4)$ — az $A$ csúcsnál lévő szöget",
   r"$A(1;0;-1)$, $B(1;-1;3)$, $C(-7;2;1)$ — a $B$ csúcsnál lévő szöget"],
  [r"$\overrightarrow{AB}=(0;4;0)$, $\overrightarrow{AC}=(0;2;2)$, $\cos\alpha=\frac{8}{4\cdot2\sqrt2}=\frac{\sqrt2}{2}$, "
   r"$\alpha=45^\circ$",
   r"$\overrightarrow{BA}=(0;1;-4)$, $\overrightarrow{BC}=(-8;3;-2)$, szorzatuk $11$, "
   r"$\cos\beta=\frac{11}{\sqrt{17}\cdot\sqrt{77}}\approx0{,}3040$, $\beta\approx72{,}3^\circ$"]),

 (r"Az $A(1;0;1)$, $B(3;1;3)$, $C(0;2;1)$ pontok egy háromszög csúcsai.",
  [r"Mutasd meg, hogy a háromszög derékszögű!", r"Számítsd ki a területét!"],
  [r"$\overrightarrow{AB}=(2;1;2)$, $\overrightarrow{AC}=(-1;2;0)$, szorzatuk $-2+2+0=0$: az $A$-nál derékszög van",
   r"a befogók $3$ és $\sqrt5$, így $T=\frac{3\sqrt5}{2}\approx3{,}35$"]),

 (r"Adott négy pont: $A(1;1;0)$, $B(3;2;2)$, $C(4;0;2)$, $D(2;-1;0)$.",
  [r"Mutasd meg, hogy $ABCD$ paralelogramma!", r"Téglalap-e? Négyzet-e?", r"Mekkora a területe?"],
  [r"$\overrightarrow{AB}=\overrightarrow{DC}=(2;1;2)$, és $\overrightarrow{AB}\nparallel\overrightarrow{AD}=(1;-2;0)$, tehát a pontok nincsenek egy egyenesen",
   r"$\overrightarrow{AD}=(1;-2;0)$ és $\overrightarrow{AB}\cdot\overrightarrow{AD}=0$: téglalap; "
   r"$AB=3\ne AD=\sqrt5$: nem négyzet",
   r"$T=AB\cdot AD=3\sqrt5\approx6{,}71$"]),

 (r"Döntsd el, hogy az $\vec a=(-8;2;4)$, $\vec b=(2;-4;8)$ és $\vec c=(-4;8;-2)$ vektorok egy kockát "
  r"feszítenek-e ki! Válaszodat indokold!", None,
  r"Nem. Mindhárom intenzitása $2\sqrt{21}$, de nem merőlegesek páronként: például "
  r"$\vec a\cdot\vec b=-16-8+32=8\ne0$."),

 (r"Egy testre három erő hat: $\vec F_1=(3;-2;4)$ N, $\vec F_2=(1;5;-1)$ N és $\vec F_3=(-2;1;1)$ N.",
  [r"Határozd meg az eredő erőt és a nagyságát!", r"Mekkora szöget zár be az eredő erő az $x$ tengely pozitív felével?"],
  [r"$\vec F=\vec F_1+\vec F_2+\vec F_3=(2;4;4)$ N, nagysága $\sqrt{4+16+16}=6$ N",
   r"$\cos\varphi=\frac{\vec F\cdot\vec i}{|\vec F|}=\frac{2}{6}=\frac13$, $\varphi\approx70{,}5^\circ$"]),

 (r"Egy állandó $\vec F=(2;3;1)$ N erő hat egy testre, miközben a test elmozdulása "
  r"$\vec s=(5;0;-2)$ m. Mennyi munkát végez az erő?", None,
  r"$W=\vec F\cdot\vec s=10+0-2=8$ J."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- B1 (közép 1–6)
 (r"Az $\vec a$ intenzitása $3$, a $\vec b$ intenzitása $4$, a szögük $120^\circ$. Számítsd ki!",
  [r"$|\vec a+\vec b|$", r"$(3\vec a-2\vec b)\cdot(\vec a+2\vec b)$"],
  [r"$|\vec a+\vec b|^2=\vec a\cdot\vec a+2\,\vec a\cdot\vec b+\vec b\cdot\vec b=9-12+16=13$, "
   r"tehát $|\vec a+\vec b|=\sqrt{13}\approx3{,}61$",
   r"$3\cdot9+6\,\vec a\cdot\vec b-2\,\vec a\cdot\vec b-4\cdot16=27-24-64=-61$"]),

 (r"Határozd meg a $t$ valós számot úgy, hogy az $\vec a=(t;t+1;1)$ és a $\vec b=(t;2;-5)$ vektor "
  r"merőleges legyen!", None,
  r"$t^2+2t+2-5=0$, azaz $t^2+2t-3=0$, tehát $t=1$ vagy $t=-3$."),

 (r"Adottak az $\vec a=(1;2;3)$, $\vec b=(k;1;-1)$ és $\vec c=(-1;0;1)$ vektorok. Határozd meg a $k$ "
  r"valós számot úgy, hogy az $\vec a+k\vec b$ vektor merőleges legyen $\vec c$-re!", None,
  r"$\vec a+k\vec b=(1+k^2;\ 2+k;\ 3-k)$, és ennek $\vec c$-vel vett szorzata $-1-k^2+3-k=0$, azaz "
  r"$k^2+k-2=0$: $k=1$ vagy $k=-2$."),

 (r"Milyen $x$ értékekre zár be az $\vec a=(-1;-4;x)$ és a $\vec b=(2;1;-2)$ vektor hegyesszöget?", None,
  r"A két vektor semmilyen $x$-re nem párhuzamos (az első két koordináta aránya $-1:2\ne-4:1$), így "
  r"pontosan akkor zárnak be hegyesszöget, ha a skaláris szorzatuk pozitív: $-2-4-2x>0$, "
  r"tehát $x\lt -3$."),

 (r"Adott az $EFG$ háromszög: $E(2;3;4)$, $F(-2;3;1)$, $G(3;-4;2)$. Számítsd ki",
  [r"a háromszög kerületét;", r"az $E$ csúcsnál lévő szögét!"],
  [r"$EF=5$, $FG=5\sqrt3$, $EG=3\sqrt6$; $K\approx21{,}01$",
   r"$\overrightarrow{EF}\cdot\overrightarrow{EG}=2$, $\cos\varepsilon=\frac{2}{5\cdot3\sqrt6}\approx0{,}0544$, "
   r"$\varepsilon\approx86{,}9^\circ$"]),

 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(1;-2;3)$, $B(1;-4;4)$, $C(3;-3;4)$.",
  [r"Határozd meg a $D$ csúcsot!", r"Mekkora szöget zárnak be az átlók?", r"Milyen különleges paralelogramma ez?"],
  [r"$D=A+C-B=(3;-1;3)$",
   r"$\overrightarrow{AC}=(2;-1;1)$, $\overrightarrow{BD}=(2;3;-1)$, szorzatuk $0$: az átlók merőlegesek, $90^\circ$",
   r"rombusz, de nem négyzet: $AB=AD=\sqrt5$, viszont $\overrightarrow{AB}\cdot\overrightarrow{AD}=-2\ne0$"]),

 # --- B2 (közép 7–12)
 (r"Az $\vec a$ és a $\vec b$ merőleges, $|\vec a|=3$ és $|\vec b|=4$. Számítsd ki!",
  [r"$|(\vec a+\vec b)\times(\vec a-\vec b)|$", r"$|(3\vec a-\vec b)\times(\vec a-2\vec b)|$"],
  [r"$(\vec a+\vec b)\times(\vec a-\vec b)=-\vec a\times\vec b+\vec b\times\vec a=-2\,\vec a\times\vec b$, "
   r"és $|\vec a\times\vec b|=12$, így az eredmény $24$",
   r"$-6\,\vec a\times\vec b-\vec b\times\vec a=-5\,\vec a\times\vec b$, így az eredmény $60$"]),

 (r"Legyen $\vec a=(2;1;-1)$ és $\vec b=(1;-1;2)$. Számítsd ki! (A b) és a c) részt a tulajdonságokkal "
  r"egyszerűsítsd, mielőtt számolsz!)",
  [r"$\vec a\times\vec b$", r"$(2\vec a+\vec b)\times\vec b$", r"$(2\vec a-\vec b)\times(2\vec a+\vec b)$"],
  [r"$(1;-5;-3)$", r"$2\,\vec a\times\vec b=(2;-10;-6)$", r"$4\,\vec a\times\vec b=(4;-20;-12)$"]),

 (r"Az $A(2;-3;4)$, $B(5;3;-4)$, $C(6;-7;2)$ pontok egy háromszög csúcsai. Számítsd ki",
  [r"a háromszög területét;", r"a $B$ csúcsból induló magasságot;", r"a $C$ csúcsnál lévő szöget!"],
  [r"$\overrightarrow{AB}\times\overrightarrow{AC}=(-44;-26;-36)$, $T=\frac{\sqrt{3908}}{2}=\sqrt{977}\approx31{,}26$",
   r"$AC=6$, $m_b=\frac{2T}{AC}\approx10{,}42$",
   r"$\overrightarrow{CA}\cdot\overrightarrow{CB}=32$, $\cos\gamma=\frac{32}{6\sqrt{137}}$, $\gamma\approx62{,}9^\circ$"]),

 (r"Az $ABCD$ paralelogramma (a csúcsok betűrendben követik egymást) három csúcsa $A(2;1;0)$, $B(3;3;1)$ és $D(1;2;2)$. Határozd meg a $C$ "
  r"csúcsot és a paralelogramma területét!", None,
  r"$C=B+D-A=(2;4;3)$. $\overrightarrow{AB}\times\overrightarrow{AD}=(1;2;1)\times(-1;1;2)=(3;-3;3)$, "
  r"így $T=3\sqrt3\approx5{,}20$."),

 (r"Határozd meg azokat az egységvektorokat, amelyek merőlegesek az $\vec a=(1;2;2)$ és a "
  r"$\vec b=(2;1;-2)$ vektorra is!", None,
  r"$\vec a\times\vec b=(-6;6;-3)$, intenzitása $9$. A két egységvektor: "
  r"$\left(-\frac{2}{3};\frac{2}{3};-\frac{1}{3}\right)$ és $\left(\frac{2}{3};-\frac{2}{3};\frac{1}{3}\right)$."),

 (r"Adott az $A(1;2;3)$, a $B(3;5;4)$ és a $C(7;t;6)$ pont. A vektoriális szorzattal határozd meg "
  r"$t$-t úgy, hogy a három pont egy egyenesre essen!", None,
  r"$\overrightarrow{AB}=(2;3;1)$, $\overrightarrow{AC}=(6;t-2;3)$, "
  r"$\overrightarrow{AB}\times\overrightarrow{AC}=(11-t;\ 0;\ 2t-22)$. Ez pontosan $t=11$ esetén a "
  r"nullvektor: ekkor $\overrightarrow{AC}=3\overrightarrow{AB}$, a pontok egy egyenesre esnek "
  r"(és nem alkotnak háromszöget)."),

 # --- C1 (közép 13–18)
 (r"A $K(2;-3;-4)$, $L(1;3;-4)$, $M(6;-5;-2)$ pontok egy háromszög csúcsai. Számítsd ki",
  [r"a háromszög területét;", r"a $K$ csúcsból induló magasságot;", r"az $L$ csúcsnál lévő szöget!"],
  [r"$\overrightarrow{KL}\times\overrightarrow{KM}=(12;2;-22)$, $T=\sqrt{158}\approx12{,}57$",
   r"$LM=\sqrt{93}$, $m_k=\frac{2T}{LM}\approx2{,}61$",
   r"$\overrightarrow{LK}\cdot\overrightarrow{LM}=53$, $\cos\lambda=\frac{53}{\sqrt{37}\cdot\sqrt{93}}$, "
   r"$\lambda\approx25{,}4^\circ$"]),

 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(2;1;-2)$, $B(4;0;-1)$, $C(4;3;2)$. "
  r"Határozd meg",
  [r"a $D$ csúcsot;", r"az átlók hajlásszögét;", r"a paralelogramma területét!"],
  [r"$D=A+C-B=(2;4;1)$",
   r"$\overrightarrow{AC}=(2;2;4)$, $\overrightarrow{BD}=(-2;4;2)$, $\cos\varphi=\frac{12}{24}=\frac12$, $\varphi=60^\circ$",
   r"$\overrightarrow{AB}\times\overrightarrow{AD}=(-6;-6;6)$, $T=6\sqrt3\approx10{,}39$"]),

 (r"Adott az $A(1;2;0)$, a $B(3;t;1)$ és a $C(0;4;2)$ pont.",
  [r"Határozd meg $t$-t úgy, hogy az $ABC$ háromszögben az $A$-nál derékszög legyen!",
   r"Ekkor mekkora a háromszög területe?"],
  [r"$\overrightarrow{AB}\cdot\overrightarrow{AC}=(2;t-2;1)\cdot(-1;2;2)=2t-4=0$, tehát $t=2$",
   r"$\overrightarrow{AB}\times\overrightarrow{AC}=(-2;-5;4)$, $T=\frac{\sqrt{45}}{2}=\frac{3\sqrt5}{2}\approx3{,}35$"]),

 (r"Döntsd el, hogy az $\vec a=(-2;3;6)$, $\vec b=(6;-2;3)$ és $\vec c=(3;6;-2)$ vektorok egy kockát "
  r"feszítenek-e ki! Válaszodat indokold!", None,
  r"Igen: páronként merőlegesek ($\vec a\cdot\vec b=\vec b\cdot\vec c=\vec a\cdot\vec c=0$), és "
  r"mindhárom intenzitása $7$."),

 (r"Legyen $A(-3;3;-4)$, $B(-2;3;-4)$, $C(1;-7;8)$, és $G$ az $AC$ szakasz felezőpontja. Számítsd ki "
  r"az $ABG$ háromszög területét és kerületét!", None,
  r"$G(-1;-2;2)$. $\overrightarrow{AB}=(1;0;0)$, $\overrightarrow{AG}=(2;-5;6)$, "
  r"$\overrightarrow{AB}\times\overrightarrow{AG}=(0;-6;-5)$, $T=\frac{\sqrt{61}}{2}\approx3{,}91$. "
  r"$AB=1$, $BG=\sqrt{62}$, $AG=\sqrt{65}$, $K\approx16{,}94$."),

 (r"Maxi a $P(1;2;-1)$, $Q(3;1;1)$, $R(0;4;2)$ háromszög $Q$ csúcsnál lévő szögét számolta: "
  r"$\overrightarrow{PQ}\cdot\overrightarrow{QR}=-7$, $\cos\varphi=\frac{-7}{3\sqrt{19}}$, "
  r"$\varphi\approx122{,}4^\circ$. Mit rontott el? Mennyi a helyes szög?", None,
  r"A $\overrightarrow{PQ}$ a $Q$ csúcsba <b>befelé</b> mutat, így Maxi a mellékszöget kapta. A "
  r"$Q$-ból induló vektorok kellenek: $\overrightarrow{QP}\cdot\overrightarrow{QR}=7$, "
  r"$\cos\varphi=\frac{7}{3\sqrt{19}}\approx0{,}5353$, $\varphi\approx57{,}6^\circ$ "
  r"($=180^\circ-122{,}4^\circ$)."),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Az $\vec a$ intenzitása $2$, a $\vec b$ intenzitása $3$, szögük $60^\circ$. Mekkora szöget zár be "
  r"az $\vec a+\vec b$ és az $\vec a-\vec b$ vektor?", None,
  r"$\vec a\cdot\vec b=3$. $(\vec a+\vec b)\cdot(\vec a-\vec b)=4-9=-5$, $|\vec a+\vec b|=\sqrt{4+6+9}=\sqrt{19}$, "
  r"$|\vec a-\vec b|=\sqrt{4-6+9}=\sqrt7$. $\cos\varphi=\frac{-5}{\sqrt{133}}\approx-0{,}4336$, "
  r"$\varphi\approx115{,}7^\circ$."),

 (r"Bizonyítsd be a skaláris szorzattal, hogy a rombusz átlói merőlegesek egymásra!", None,
  r"Legyen $\overrightarrow{AB}=\vec a$, $\overrightarrow{AD}=\vec b$, rombuszban $|\vec a|=|\vec b|$. "
  r"Az átlók: $\overrightarrow{AC}=\vec a+\vec b$ és $\overrightarrow{DB}=\vec a-\vec b$. "
  r"$(\vec a+\vec b)\cdot(\vec a-\vec b)=|\vec a|^2-|\vec b|^2=0$, tehát az átlók merőlegesek."),

 (r"Egy kockát kifeszítő három vektor közül kettő $\vec a=(6;2;-3)$ és $\vec b=(-3;6;-2)$. "
  r"Határozd meg a harmadik vektort!", None,
  r"$\vec a\cdot\vec b=0$ és $|\vec a|=|\vec b|=7$. A harmadik vektor merőleges mindkettőre, és "
  r"intenzitása $7$: $\vec a\times\vec b=(14;21;42)$, intenzitása $49$, ezért "
  r"$\vec c_1=\frac{7}{49}(14;21;42)=(2;3;6)$ vagy $\vec c_2=(-2;-3;-6)$."),

 (r"Az $A(1;0;0)$, $B(0;2;0)$ és $C(0;0;t)$ csúcsú háromszög területe $\frac72$. Határozd meg $t$-t!", None,
  r"$\overrightarrow{AB}\times\overrightarrow{AC}=(-1;2;0)\times(-1;0;t)=(2t;t;2)$, "
  r"$T=\frac12\sqrt{5t^2+4}=\frac72$, így $5t^2=45$: $t=3$ vagy $t=-3$."),
]

JOKER = (r"1843. október 16-án William Rowan Hamilton ír matematikus belevéste a dublini Broome-híd "
         r"kövébe a felfedezését, amelyből később a vektoriális szorzat is kinőtt. Hamilton "
         r"szorzásánál a tényezők sorrendje már számított. Nézzük, a vektoriális szorzatnál mi "
         r"történik a zárójelekkel!",
         [r"$\vec i\times(\vec i\times\vec j)=\vec i\times\vec k=-\vec j$",
          r"$(\vec i\times\vec i)\times\vec j=\vec 0\times\vec j=\vec 0$",
          r"a két eredmény különböző, tehát a vektoriális szorzat <b>nem asszociatív</b>: a "
          r"zárójelek helye számít (az alap-12-ben láttad: nem is kommutatív, "
          r"$\vec b\times\vec a=-\vec a\times\vec b$)"],
         [r"Számítsd ki: $\vec i\times(\vec i\times\vec j)$.", r"Számítsd ki: $(\vec i\times\vec i)\times\vec j$.",
          r"Mit mutat a két eredmény?"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (22, 18, 4), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="04-vektorok", fajl="feladatok-szorzatok.html",
           cim="A két szorzat", temakor="Vektorok",
           alcim="A skaláris és a vektoriális szorzat: szög, merőlegesség, terület, párhuzamosság — "
                 "és néhány alkalmazás. A végeredmény minden feladatnál lenyitható — előbb számolj, "
                 "csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="feladatok-vektorok.html", prevc="Vektorok — feladatok",
           nxt="osszefoglalo.html", nxtc="Összefoglaló")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
