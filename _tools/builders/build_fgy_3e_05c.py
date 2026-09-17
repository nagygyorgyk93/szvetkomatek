# -*- coding: utf-8 -*-
"""3e/05 — 3. feladatgyujtemeny: a kor (C1-C2).
Horgony-terv: narrativa_05-analitikus-geometria.md · feladat-terkep: terkep_fgy_05-analitikus-geometria.md.
Forras-szamok: 6. Feladatok - Analitikus geometria - II. resz.pdf (1-16).
Forrashibak: 9a (az egyik metszespont (6;-3)), 10. (x+2y+1=0). Felmero-utkozes miatt: 2a uj kozeppont, 5. helyett 7."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Matrix, sqrt, Rational as Q, symbols, solve, simplify, N, Abs, expand, Poly
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(a, b) for a, b in zip(g, w))
    if hasattr(g, "shape"):
        return g.shape == w.shape and all(simplify(a - b) == 0 for a, b in zip(g, w))
    return simplify(g - w) == 0


def chk(n, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((n, g, w))


x, y, t, k, m, c, q = symbols("x y t k m c q", real=True)


def kp(expr):
    """altalanos alakbol kozeppont es r^2"""
    e = expand(expr)
    d, ee, f = e.coeff(x, 1).subs(y, 0), e.coeff(y, 1).subs(x, 0), e.subs({x: 0, y: 0})
    p0, q0 = -d / 2, -ee / 2
    return (p0, q0, p0**2 + q0**2 - f)


def metsz(kor, l):
    s = solve([kor, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s], key=lambda u: (float(N(u[0])), float(N(u[1]))))


def pe(l, p):
    l = expand(l)
    return Abs(l.subs({x: p[0], y: p[1]})) / sqrt(l.coeff(x)**2 + l.coeff(y)**2)


# --- alap
chk("a1", [kp((x - 5)**2 + (y + 2)**2 - 20), kp((x + 4)**2 + y**2 - 121), kp(x**2 + y**2 - Q(9, 4)),
           kp(x**2 + (y - 7)**2 - 25), kp(x**2 + y**2 - Q(25, 4))],
    [(5, -2, 20), (-4, 0, 121), (0, 0, Q(9, 4)), (0, 7, 25), (0, 0, Q(25, 4))])
chk("a3", [kp((x - 7)*(x - 3) + (y + 4)*(y - 2)), kp((x + 3)*(x - 3) + (y - 2)*(y + 6)), kp((x + 5)*(x - 3) + (y - 7)*(y + 1))],
    [(5, -1, 13), (0, -2, 25), (-1, 3, 32)])   # Thalesz: (x-x1)(x-x2)+(y-y1)(y-y2)=0
chk("a4", [kp(x**2 + y**2 - 10*x + 2*y + 22), kp(x**2 + y**2 - 2*x - 8*y - 8), kp(x**2 + y**2 + 6*y + 7),
           kp(x**2 + y**2 - 3*x + 2*y + 2), kp(x**2 + y**2 - 6*x - y + 3)],
    [(5, -1, 4), (1, 4, 25), (0, -3, 2), (Q(3, 2), -1, Q(5, 4)), (3, Q(1, 2), Q(25, 4))])
K5 = lambda u, v: (u - 1)**2 + (v + 2)**2
chk("a5", [K5(4, 2), K5(6, 1), K5(-1, 0)], [25, 34, 8])
chk("a6", (1 + 2)**2 + (5 - 1)**2, 25)
chk("a7", [kp(x**2 + y**2 - 4*x + 6*y + 4), kp(x**2 + y**2 + 2*x - 4*y + 10), kp(x**2 + y**2 - 8*x)],
    [(2, -3, 9), (-1, 2, -5), (4, 0, 16)])
chk("a8", [(4 - 2)**2 + (6 - 3)**2, (6 - 2)**2 + (7 - 3)**2], [13, 32])
K9 = x**2 + y**2 - 2*x + 6*y - 15
chk("a9", [metsz(K9, x - 2*y - 12), metsz(K9, x - 2*y + 6), metsz(K9, 3*x - 4*y + 10)],
    [[(-2, -7), (6, -3)], [], [(-2, 1)]])
assert pe(x - 2*y + 6, (1, -3)) > 5
chk("a9d", pe(3*x - 4*y + 10, (1, -3)), 5)
chk("a10", metsz(x**2 + y**2 - 6*x + 4*y + 8, x + 2*y + 1), [(1, -1), (5, -3)])
chk("a11", metsz(x**2 + y**2 - 4*x + 2*y - 15, 2*x + y - 3), [(0, 3), (4, -5)])
chk("a12", [metsz(x**2 + y**2 - 25, -3*x + 4*y - 25), metsz((x - 2)**2 + (y + 1)**2 - 13, 2*x + 3*y - 14)],
    [[(-3, 4)], [(4, 2)]])
chk("a13", [pe(x - 2*y, (-1, 2)), pe(2*x - y + 14, (-1, 2)), pe(x + y + 8, (-1, 2)), sqrt(20)],
    [sqrt(5), 2*sqrt(5), 9*sqrt(2)/2, 2*sqrt(5)])
chk("a13k1", 9*sqrt(2)/2, 6.36, .005); chk("a13k2", 2*sqrt(5), 4.47, .005)
chk("a14", metsz((x - 1)**2 + (y + 1)**2 - 25, y - 2), [(-3, 2), (5, 2)])
# --- közép
chk("k1", sorted(solve((4 + t)**2 + (-1 + 3*t)**2 - 25, t)), [-1, Q(4, 5)])
chk("k2", solve((-3 + 2*k)**2 + (4 - k)**2 - 5, k), [2])
Cm = solve([2*x + y - 3, x + 4*y + 2], [x, y])
chk("k3", [Cm[x], Cm[y], (-2 - Cm[x])**2 + (1 - Cm[y])**2], [2, -1, 20])
a0 = solve((6 - x)**2 + 4 - (x**2 + 16), x)
chk("k4", [a0, a0[0]**2 + 16], [[2], 20])
K15 = x**2 + y**2 + 4*x - 2*y - 5
M15 = metsz(K15, 3*x + y + 5)
chk("k5", [M15, sqrt((M15[0][0] - M15[1][0])**2 + (M15[0][1] - M15[1][1])**2)], [[(-3, 4), (-1, -2)], 2*sqrt(10)])
chk("k5k", 2*sqrt(10), 6.32, .005)
chk("k6", [pe(x + y - 2, (0, 0)), 2*sqrt(9 - 2)], [sqrt(2), 2*sqrt(7)]); chk("k6k", 2*sqrt(7), 5.29, .005)
chk("k6m", len(metsz(x**2 + y**2 - 9, x + y - 2)), 2)
chk("k7", [(1 + 2)**2 + 4**2, metsz((x + 2)**2 + y**2 - 25, 3*x + 4*y - 19)], [25, [(1, 4)]])
chk("k8", [(4 + 1)**2 + (4 - 2)**2, (3 + 1)**2 + (5 - 2)**2, metsz((x + 1)**2 + (y - 2)**2 - 25, 4*x + 3*y - 27)],
    [29, 25, [(3, 5)]])
chk("k9", metsz(x**2 + y**2 - 4*x + 6*y + 8, x - 2*y - 5), [(Q(-1, 5), Q(-13, 5)), (3, -1)])
chk("k9h", sqrt((3 + Q(1, 5))**2 + (-1 + Q(13, 5))**2), 8*sqrt(5)/5); chk("k9k", 8*sqrt(5)/5, 3.58, .005)
K10 = x**2 + y**2 - 6*x - 4*y - 12
M10 = metsz(K10, x - y + 4)
chk("k10", [kp(K10), M10, sqrt((M10[1][0] - M10[0][0])**2 + (M10[1][1] - M10[0][1])**2), pe(x - y + 4, (3, 2))],
    [(3, 2, 25), [(-2, 2), (3, 7)], 5*sqrt(2), 5*sqrt(2)/2])
chk("k10k1", 5*sqrt(2), 7.07, .005); chk("k10k2", 5*sqrt(2)/2, 3.54, .005)


def erinto_param(kor, l, par):
    """a behelyettesites utan D=0"""
    yl = solve(l, y)[0]
    pol = Poly(expand(kor.subs(y, yl)), x)
    A2, B2, C2 = pol.all_coeffs()
    return sorted(solve(B2**2 - 4*A2*C2, par), key=lambda u: float(N(u))), (A2, B2, C2)


# --- nehéz
sol, egyh = erinto_param((x - 1)**2 + (y - 1)**2 - 4, 2*x + y + m, m)
chk("n1", [sol, egyh], [[-3 - 2*sqrt(5), -3 + 2*sqrt(5)], (5, 4*m + 2, m**2 + 2*m - 2)])
chk("n1k1", -3 + 2*sqrt(5), 1.47, .005); chk("n1k2", -3 - 2*sqrt(5), -7.47, .005)
chk("n1d", [pe(2*x + y - 3 + 2*sqrt(5), (1, 1)), pe(2*x + y - 3 - 2*sqrt(5), (1, 1))], [2, 2])
chk("n2", [erinto_param(x**2 + y**2 - 5*x - 7*y + 6, x + y + c, c)[0],
           erinto_param(x**2 + y**2 - 8*x + 2*y + 12, 2*x - y - m, m)[0]], [[-11, -1], [4, 14]])
chk("n3", sorted(solve(Abs(5 - 2*q + 1) / sqrt(5) - sqrt(20), q)), [-2, 8])
# 15c,d: K: C(-2;1), r^2=10; e: 3x+y+5=0
chk("n4k", kp(K15), (-2, 1, 10))
chk("n4", [erinto_param(K15, y + 3*x - c, c)[0], erinto_param(K15, y - x/3 - c, c)[0]],
    [[-15, 5], [Q(-5, 3), 5]])
K16 = x**2 + y**2 - 4*x + 6*y + 8
chk("n5", [kp(K16), erinto_param(K16, y - x/2 - c, c)[0], erinto_param(K16, y + 2*x - c, c)[0]],
    [(2, -3, 5), [Q(-13, 2), Q(-3, 2)], [-4, 6]])
# joker: legkozelebbi pont
Ck = Matrix([6, 8]); d0 = sqrt(Ck.dot(Ck))
pk = Ck * (d0 - 7) / d0
chk("jok", [d0 - 7, pk, (pk[0] - 6)**2 + (pk[1] - 8)**2], [3, Matrix([Q(9, 5), Q(12, 5)]), 49])
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- C1: a kör egyenlete (alap 1–8)
 (r"Add meg a kör középpontját és sugarát!",
  [r"$(x-5)^2+(y+2)^2=20$", r"$(x+4)^2+y^2=121$", r"$x^2+y^2=\tfrac94$", r"$x^2+(y-7)^2=25$", r"$4x^2+4y^2=25$"],
  [r"$C(5;-2)$, $r=2\sqrt5$", r"$C(-4;0)$, $r=11$", r"$C(0;0)$, $r=\tfrac32$", r"$C(0;7)$, $r=5$",
   r"$C(0;0)$, $r=\tfrac52$"], True),

 (r"Írd fel a kör egyenletét, ha adott a $C$ középpontja és az $r$ sugara!",
  [r"$C(-4;1)$, $r=2$", r"$C\left(0;-\tfrac12\right)$, $r=3\sqrt2$", r"$C(-5;0)$, $r=\tfrac73$", r"$C(0;0)$, $r=\sqrt{10}$"],
  [r"$(x+4)^2+(y-1)^2=4$", r"$x^2+\left(y+\tfrac12\right)^2=18$", r"$(x+5)^2+y^2=\tfrac{49}{9}$", r"$x^2+y^2=10$"], True),

 (r"Írd fel annak a körnek az egyenletét, amelynek egyik átmérője az $AB$ szakasz!",
  [r"$A(7;-4)$, $B(3;2)$", r"$A(-3;2)$, $B(3;-6)$", r"$A(-5;7)$, $B(3;-1)$"],
  [r"$(x-5)^2+(y+1)^2=13$", r"$x^2+(y+2)^2=25$", r"$(x+1)^2+(y-3)^2=32$"]),

 (r"Határozd meg a kör középpontját és sugarát, majd írd fel az egyenletét $(x-p)^2+(y-q)^2=r^2$ alakban!",
  [r"$x^2+y^2-10x+2y+22=0$", r"$x^2+y^2-2x-8y-8=0$", r"$x^2+y^2+6y+7=0$", r"$x^2+y^2-3x+2y+2=0$",
   r"$x^2+y^2-6x-y+3=0$"],
  [r"$C(5;-1)$, $r=2$; $(x-5)^2+(y+1)^2=4$", r"$C(1;4)$, $r=5$; $(x-1)^2+(y-4)^2=25$",
   r"$C(0;-3)$, $r=\sqrt2$; $x^2+(y+3)^2=2$", r"$C\left(\tfrac32;-1\right)$, $r=\tfrac{\sqrt5}{2}$; "
   r"$\left(x-\tfrac32\right)^2+(y+1)^2=\tfrac54$", r"$C\left(3;\tfrac12\right)$, $r=\tfrac52$; "
   r"$(x-3)^2+\left(y-\tfrac12\right)^2=\tfrac{25}{4}$"]),

 (r"Adott a $(x-1)^2+(y+2)^2=25$ kör. A körön, a körön kívül vagy a körön belül van a pont?",
  [r"$P(4;2)$", r"$Q(6;1)$", r"$R(-1;0)$"],
  [r"a körön ($25=25$)", r"kívül ($34\gt25$)", r"belül ($8\lt25$)"], True),

 (r"Írd fel annak a körnek az egyenletét, amelynek középpontja $C(-2;1)$, és átmegy az $A(1;5)$ ponton!", None,
  r"$r=CA=5$; $(x+2)^2+(y-1)^2=25$"),

 (r"Kör egyenlete-e? Ha igen, add meg a középpontot és a sugarat!",
  [r"$x^2+y^2-4x+6y+4=0$", r"$x^2+y^2+2x-4y+10=0$", r"$x^2+2y^2-4x=0$", r"$x^2+y^2-8x=0$"],
  [r"igen: $C(2;-3)$, $r=3$", r"nem: teljes négyzetté alakítva a jobb oldalon $-5$ állna, a sugár négyzete nem lehet negatív",
   r"nem: $x^2$ és $y^2$ együtthatója különböző", r"igen: $C(4;0)$, $r=4$"]),

 (r"Egy kerti öntöző a $(2;3)$ pontban áll (egy egység $1$ méter), és $5$ méter sugarú körben locsol.",
  [r"Írd fel a locsolt terület határának egyenletét!", r"Eléri-e a víz a $(4;6)$ pontban lévő rózsát?",
   r"Eléri-e a víz a $(6;7)$ pontban lévő bokrot?"],
  [r"$(x-2)^2+(y-3)^2=25$", r"igen ($13\lt25$)", r"nem ($32\gt25$)"]),

 # --- C2: a kör és az egyenes (alap 9–14)
 (r"Határozd meg a $K\colon x^2+y^2-2x+6y-15=0$ kör és az $l$ egyenes kölcsönös helyzetét! Ha van közös "
  r"pontjuk, add meg.",
  [r"$l\colon x-2y-12=0$", r"$l\colon x-2y+6=0$", r"$l\colon 3x-4y+10=0$"],
  [r"szelő: $(6;-3)$ és $(-2;-7)$", r"nincs közös pontjuk", r"érintő: $(-2;1)$"]),

 (r"Határozd meg a $K\colon x^2+y^2-6x+4y+8=0$ kör és az $l\colon x+2y+1=0$ egyenes metszéspontjait!", None,
  r"$(1;-1)$ és $(5;-3)$"),

 (r"Határozd meg a $K\colon x^2+y^2-4x+2y-15=0$ kör és az $l\colon 2x+y-3=0$ egyenes metszéspontjait!", None,
  r"$(0;3)$ és $(4;-5)$"),

 (r"Írd fel a kör érintőjének egyenletét a megadott pontjában! Előbb ellenőrizd, hogy a pont a körön van!",
  [r"$x^2+y^2=25$, $P(-3;4)$", r"$(x-2)^2+(y+1)^2=13$, $P(4;2)$"],
  [r"$-3x+4y=25$, azaz $3x-4y+25=0$", r"$2x+3y-14=0$"]),

 (r"Adott a $(x+1)^2+(y-2)^2=20$ kör. Hasonlítsd össze a középpont és az egyenes $d$ távolságát a sugárral, "
  r"és döntsd el, hány közös pontja van a körnek és az egyenesnek!",
  [r"$x-2y=0$", r"$2x-y+14=0$", r"$x+y+8=0$"],
  [r"$d=\sqrt5\lt2\sqrt5$: szelő, $2$ közös pont", r"$d=2\sqrt5=r$: érintő, $1$ közös pont",
   r"$d=\tfrac{9\sqrt2}{2}\approx6{,}36\gt r\approx4{,}47$: nincs közös pont"]),

 (r"Milyen hosszú húrt metsz ki a $(x-1)^2+(y+1)^2=25$ körből az $y=2$ egyenes?", None,
  r"a metszéspontok $(-3;2)$ és $(5;2)$, a húr hossza $8$"),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- C1 (közép 1–4)
 (r"Határozd meg a $t$ valós paramétert úgy, hogy a $(x+t)^2+(y+3t)^2=25$ kör átmenjen az $A(4;-1)$ ponton!",
  None, r"$t=-1$ vagy $t=\tfrac45$"),

 (r"Határozd meg a $k$ valós paramétert úgy, hogy a $(x+2k)^2+(y-k)^2=5$ kör átmenjen az $S(-3;4)$ ponton!",
  None, r"$k=2$"),

 (r"Egy kör középpontja a $2x+y-3=0$ és az $x+4y+2=0$ egyenes metszéspontja, és a kör átmegy az "
  r"$M(-2;1)$ ponton. Írd fel a kör egyenletét!", None, r"$C(2;-1)$; $(x-2)^2+(y+1)^2=20$"),

 (r"Egy kör középpontja az $x$-tengelyen van, és a kör átmegy az $A(6;2)$ és a $B(0;4)$ ponton. "
  r"Írd fel a kör egyenletét!", None, r"$C(2;0)$; $(x-2)^2+y^2=20$"),

 # --- C2 (közép 5–10)
 (r"Adott a $K\colon x^2+y^2+4x-2y-5=0$ kör és az $e\colon 3x+y+5=0$ egyenes.",
  [r"Határozd meg a metszéspontjaikat!", r"Milyen hosszú húrt metsz ki a kör az egyenesből?"],
  [r"$A(-3;4)$ és $B(-1;-2)$", r"$AB=2\sqrt{10}\approx6{,}32$"]),

 (r"Egy mobiltorony a $(0;0)$ pontban áll, a jele $3$ km sugarú körön belül fogható (egy egység $1$ km). Egy "
  r"egyenes országút az $x+y-2=0$ egyenes mentén halad. Milyen hosszú útszakaszon van térerő?", None,
  r"a középpont és az út távolsága $\sqrt2\lt3$, a húr hossza $2\sqrt7\approx5{,}29$ km"),

 (r"Írd fel a $(x+2)^2+y^2=25$ kör érintőjének egyenletét a $P(1;4)$ pontban!", None, r"$3x+4y-19=0$"),

 (r"Maxi a $(x+1)^2+(y-2)^2=25$ kör érintőjét akarta felírni a $Q(4;4)$ pontban. Ellenőrizd előbb, van-e "
  r"értelme a feladatnak! Utána írd fel az érintőt a kör $P(3;5)$ pontjában!", None,
  r"$Q$ nincs a körön ($25+4=29\ne25$), ezért nem lehet a kör érintési pontja; a $P(3;5)$ pontbeli "
  r"érintő $4x+3y-27=0$"),

 (r"Adott a $K\colon x^2+y^2-4x+6y+8=0$ kör és az $l\colon x-2y-5=0$ egyenes.",
  [r"Határozd meg a metszéspontjaikat!", r"Milyen hosszú húrt metsz ki a kör az egyenesből?"],
  [r"$(3;-1)$ és $\left(-\tfrac15;-\tfrac{13}{5}\right)$", r"$\tfrac{8\sqrt5}{5}\approx3{,}58$"]),

 (r"Adott a $K\colon x^2+y^2-6x-4y-12=0$ kör és az $e\colon x-y+4=0$ egyenes.",
  [r"Határozd meg a kör középpontját és sugarát!", r"Határozd meg a metszéspontokat és a húr hosszát!",
   r"Mutasd meg a középpont és az egyenes távolságával is, hogy az egyenes szelő!"],
  [r"$C(3;2)$, $r=5$", r"$(-2;2)$ és $(3;7)$, a húr $5\sqrt2\approx7{,}07$",
   r"$d=\tfrac{5\sqrt2}{2}\approx3{,}54\lt5$"]),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Határozd meg az $m$ valós paramétert úgy, hogy a $2x+y+m=0$ egyenes érintse a $(x-1)^2+(y-1)^2=4$ kört!",
  [r"Fejezd ki az egyenesből $y$-t, helyettesítsd a kör egyenletébe, és rendezd az $x$-re másodfokú egyenletet!",
   r"Mikor van az egyenletnek pontosan egy megoldása? Határozd meg $m$-et!",
   r"Írd fel az érintők egyenletét! Ellenőrizd a középpont és az egyenes távolságával is!"],
  [r"$5x^2+(4m+2)x+m^2+2m-2=0$", r"$D=0$: $m^2+6m-11=0$, $m=-3\pm2\sqrt5$ ($\approx1{,}47$ vagy $\approx-7{,}47$)",
   r"$2x+y-3+2\sqrt5=0$ és $2x+y-3-2\sqrt5=0$; mindkettőre $d=2=r$"]),

 (r"Határozd meg az ismeretlen együtthatót úgy, hogy az $l$ egyenes érintse a $K$ kört!",
  [r"$l\colon x+y+c=0$, $K\colon x^2+y^2-5x-7y+6=0$", r"$l\colon 2x-y-m=0$, $K\colon x^2+y^2-8x+2y+12=0$"],
  [r"$c=-1$ vagy $c=-11$", r"$m=4$ vagy $m=14$"]),

 (r"Határozd meg a $q$ paramétert úgy, hogy a $(x-5)^2+(y-q)^2=20$ kör érintse az $x-2y+1=0$ egyenest!", None,
  r"$q=-2$ vagy $q=8$"),

 (r"Adott a $K\colon x^2+y^2+4x-2y-5=0$ kör és az $e\colon 3x+y+5=0$ egyenes.",
  [r"Határozd meg a kör középpontját és sugarát!", r"Írd fel a körnek az $e$-vel párhuzamos érintőit!",
   r"Írd fel a körnek az $e$-re merőleges érintőit!"],
  [r"$C(-2;1)$, $r=\sqrt{10}$", r"$y=-3x+5$ és $y=-3x-15$", r"$y=\tfrac13x+5$ és $y=\tfrac13x-\tfrac53$"]),

 (r"Adott a $K\colon x^2+y^2-4x+6y+8=0$ kör és az $l\colon x-2y-5=0$ egyenes.",
  [r"Írd fel a körnek az $l$-lel párhuzamos érintőit!", r"Írd fel a körnek az $l$-re merőleges érintőit!"],
  [r"$y=\tfrac12x-\tfrac32$ és $y=\tfrac12x-\tfrac{13}{2}$", r"$y=-2x+6$ és $y=-2x-4$"]),
]

JOKER = (r"A $(x-6)^2+(y-8)^2=49$ kör pontjai közül melyik van a legközelebb az origóhoz? Milyen messze van? "
         r"<i>(Tipp: rajzold le, és gondold végig, merre kell elindulni a középpontból.)</i>",
         r"A legközelebbi pont a középpontot az origóval összekötő szakaszon van: $|OC|=10$, a távolság "
         r"$10-7=3$, a pont $\left(\tfrac95;\tfrac{12}{5}\right)$.")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (14, 10, 5), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="05-analitikus-geometria", fajl="feladatok-kor.html",
           cim="A kör", temakor="Síkbeli analitikus geometria",
           alcim="A kör egyenlete, a kör és az egyenes kölcsönös helyzete, húr és érintő. Számológép "
                 "használható: a szögeket egy, minden más közelítő értéket két tizedesre kerekíts. A "
                 "végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-kor-es-egyenes.html", prevc="A kör és az egyenes",
           nxt="tananyag-ellipszis.html", nxtc="Az ellipszis")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
