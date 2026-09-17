# -*- coding: utf-8 -*-
"""3e/05 — 2. feladatgyujtemeny: egyenesek (B1-B3).
Horgony-terv: narrativa_05-analitikus-geometria.md · feladat-terkep: terkep_fgy_05-analitikus-geometria.md.
Forras-szamok: Pont, egyenes/5. Feladatok - Analitikus geometria - I. resz.pdf (18-41).
Forrashibak: 28. (a megadott eredmeny nem jon ki -> uj masodik egyenes), 41. (8x-y-3=0)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from abra_common import svg_koordsik, KEK, PIROS, ZOLD

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (Matrix, sqrt, Rational as Q, symbols, solve, simplify, N, Abs, atan, pi, tan,
                   acos, expand, sympify)
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


x, y, a, b, c, m, n = symbols("x y a b c m n", real=True)
P = lambda u, v: Matrix([u, v])
tav = lambda p, q: sqrt((p - q).dot(p - q))


def egy(l1, l2):
    """ket egyenes (kifejezes x,y-ban) metszespontja"""
    s = solve([l1, l2], [x, y], dict=True)
    return P(s[0][x], s[0][y]) if len(s) == 1 else None


def rajta(l, p):
    return simplify(l.subs({x: p[0], y: p[1]})) == 0


def egyenlo_egyenes(l1, l2):
    """ugyanaz az egyenes-e (skalarszoros)"""
    k1 = [l1.coeff(x), l1.coeff(y), l1.subs({x: 0, y: 0})]
    k2 = [l2.coeff(x), l2.coeff(y), l2.subs({x: 0, y: 0})]
    return all(simplify(k1[i] * k2[j] - k1[j] * k2[i]) == 0 for i in range(3) for j in range(3))


def pe(l, p):
    """pont-egyenes tavolsag"""
    return Abs(l.subs({x: p[0], y: p[1]})) / sqrt(l.coeff(x)**2 + l.coeff(y)**2)


def szog(k1, k2):
    k1, k2 = sympify(k1), sympify(k2)
    return atan(Abs((k2 - k1) / (1 + k1 * k2))) * 180 / pi


def chk_egy(nev, l1, l2):
    if not egyenlo_egyenes(expand(l1), expand(l2)):
        E.append((nev, l1, l2))


# --- alap
p18 = 2*x - 5*y + 8
assert [rajta(p18, q) for q in [(1, 2), (-9, -2), (-2, 1), (Q(-3, 2), 1), (-4, 0), (8, 5)]] == \
    [True, True, False, True, True, False]
chk("a2", solve(3*(-1) + b*2 + 11, b), [-4])
chk("a3", solve(a*5 + 4*(-3) - 13, a), [5])
chk("a5", [solve((4*x + 10), x), solve(-5*y + 10, y)], [[Q(-5, 2)], [2]])
chk_egy("a6a", y - (x + 3), x - y + 3); chk_egy("a6b", y - (-x - 4), x + y + 4)
chk_egy("a6c", y - (sqrt(3)*x - 2), sqrt(3)*x - y - 2); chk_egy("a6d", y - (-x + Q(2, 3)), 3*x + 3*y - 2)
chk("a6tan", [tan(pi/4), tan(3*pi/4), tan(pi/3)], [1, -1, sqrt(3)])
chk_egy("a7a", y - 2 - (x - 3), y - (x - 1)); chk_egy("a7b", y + 1 + (x + 4), y - (-x - 5))
chk_egy("a7c", y - 3 - sqrt(3)*(x + 2), y - (sqrt(3)*x + 2*sqrt(3) + 3)); chk_egy("a7d", y + 2 + (x - 5), y - (-x + 3))
for nev, p1, p2, l in [("a8a", (1, 5), (-3, 4), x - 4*y + 19), ("a8b", (-2, -3), (0, 1), 2*x - y + 1),
                       ("a8c", (Q(1, 2), 5), (5, 0), 10*x + 9*y - 50), ("a8d", (-3, 1), (-2, -4), 5*x + y + 14)]:
    if not (rajta(l, p1) and rajta(l, p2)):
        E.append((nev, l))
chk_egy("a9a", 4*x - 5*y - 10, y - (Q(4, 5)*x - 2)); chk_egy("a9a2", 4*x - 5*y - 10, x/Q(5, 2) + y/(-2) - 1)
chk_egy("a9b", 3*x + 6*y - 21, y - (-x/2 + Q(7, 2))); chk_egy("a9b2", 3*x + 6*y - 21, x/7 + y/Q(7, 2) - 1)
chk("a10", [egy(2*x + 3*y - 6, x - 2*y + 4), egy(2*x + 3*y - 6, y), egy(x - 2*y + 4, y)], [P(0, 2), P(3, 0), P(-4, 0)])
chk("a11", [egy(x + 2*y - 2, 3*x - y - 13), egy(x - 3*y + 17, 3*x + 7*y - 29), egy(4*x + 3*y + 5, 2*x + y + 2)],
    [P(4, -1), P(-2, 5), P(Q(-1, 2), -1)])
assert egyenlo_egyenes(2*x - y + 3, 4*x - 2*y + 6)
assert egy(3*x + y - 2, 6*x + 2*y + 5) is None and not egyenlo_egyenes(3*x + y - 2, 6*x + 2*y + 5)
chk("a12", [egy(x + 2*y - 4, 3*x - y - 5), egy(y + x - 4, y - 2*x + 5)], [P(2, 1), P(3, 1)])
assert egy(y - 2*x - 1, 4*x - 2*y + 3) is None      # parhuzamos (k=2)
chk("a13", [3 * Q(-1, 3), 1 * (-2)], [-1, -2])      # 3x-y+2 (k=3) es x+3y-1 (k=-1/3): meroleges; 1 es -2: egyik sem
for nev, p0, l in [("a14a", (4, -3), 2*x - 3*y - 17), ("a14b", (-4, 3), 2*x - 5*y + 23), ("a14c", (-2, 1), x - 4*y + 6)]:
    assert rajta(l, p0), nev
assert rajta(3*x + 5*y - 1, (-3, 2)) and 5*3 + (-3)*5 == 0
assert rajta(3*x + 2*y, (2, -3)) and 2*3 + (-3)*2 == 0
assert rajta(7*x + y + 9, (-2, 5)) and 1*7 + (-7)*1 == 0
chk("a16", [szog(3, Q(1, 2)), szog(Q(-1, 4), Q(3, 5))], [45, 45])
F1, F2 = (P(1, -2) + P(3, -4)) / 2, (P(-7, 1) + P(3, 5)) / 2
assert rajta(x - y - 5, F1) and rajta(5*x + 2*y + 4, F2)
assert (P(3, -4) - P(1, -2)).dot(P(1, 1)) == 0 and (P(3, 5) - P(-7, 1)).dot(P(2, -5)) == 0
chk("a18", [szog(3, 1), szog(sqrt(3), 1/sqrt(3))], [atan(Q(1, 2))*180/pi, 30])
chk("a18k", szog(3, 1), 26.6, .05)
chk("a19", [pe(12*x - 5*y - 27, (4, -1)), pe(3*x - 4*y + 15, (3, 2)), pe(x - 2*y + 7, (-1, -2)), pe(2*x - 3*y, (7, -4))],
    [2, Q(16, 5), 2*sqrt(5), 2*sqrt(13)])
chk("a19k", [2*sqrt(5), 2*sqrt(13)], [sqrt(20), sqrt(52)]); chk("a19k1", 2*sqrt(5), 4.47, .005); chk("a19k2", 2*sqrt(13), 7.21, .005)
chk("a20", [pe(5*x - 12*y + 26, egy(5*x - 12*y - 13, y)), pe(3*x + y + 17, (0, 3))], [3, 2*sqrt(10)])
chk("a20k", 2*sqrt(10), 6.32, .005)
chk("a21", [pe(3*x + 4*y - 20, (0, 0)), pe(x - y + 2, (0, 0))], [4, sqrt(2)]); chk("a21k", sqrt(2), 1.41, .005)
chk("a22", pe(3*x - 4*y + 10, (1, 2)), 1)
chk("a23", [pe(3*x - 4*y, (1, -3)), Abs(4*(-3) - 3*1) / 2], [3, Q(15, 2)])
chk("a24", [pe(3*x - y + 1, (1, 2)), pe(3*x + y + 1, (1, 2))], [2/sqrt(10), 6/sqrt(10)])
chk("a24k", 2/sqrt(10), 0.63, .005); chk("a24m", 6/sqrt(10), 1.90, .005)
# --- közép
assert rajta(2*x - y + 1, (-1, -1)) and rajta(2*x - y + 1, (2, 5))
M28 = egy(2*x - y - 4, x + y - 5)
chk("k2", M28, P(3, 2)); assert rajta(3*x + y - 11, M28) and rajta(3*x + y - 11, (4, -1))
M27 = egy(3*x - 5*y - 11, 4*x + y - 7)
chk("k3", M27, P(2, -1)); assert rajta(y - 2*x + 5, M27) and rajta(y - 2*x + 5, (4, 3))
chk("k4", [solve(3*x - 12, x), solve(2*y - 12, y), Q(4*6, 2)], [[4], [6], 12])
chk("k5", 80*12 + 200, 1160)
chk_egy("k6", 3*x - 2*y + 6, x/(-2) + y/3 - 1)
M33 = egy(y + 2*x - 11, y + x - 8)
assert rajta(5*x + 3*y - 30, M33)
M34 = egy(4*x - 3*y - 8, x + 2*y - 13)
chk("k8", M34, P(5, 4)); assert rajta(x - 3*y + 7, M34) and Q(1, 3) * (-3) == -1
M35 = egy(x + 3*y - 3, x - 2*y - 2)
assert rajta(2*x + y - 5, M35) and (-2) * Q(1, 2) == -1
A, B, C = P(-1, -4), P(5, 6), P(-3, 2)
for l, p1, p2 in [(4*x - y, A, (B + C) / 2), (x - y + 1, B, (A + C) / 2), (x + 5*y - 7, C, (A + B) / 2)]:
    assert rajta(l, p1) and rajta(l, p2)
assert rajta(2*x + y + 6, A) and (C - B).dot(P(1, -2)) == 0      # h_a: iranyvektora (1;-2) meroleges BC-re
chk("k11", [solve(-a/2 - Q(1, 2), a), solve((-a/2) * Q(1, 2) + 1, a)], [[-1], [4]])
chk("k12", egy(y - 2*x - 1, x + 2*y - 12), P(2, 5)); assert 2 * Q(-1, 2) == -1
A, B, C = P(4, 6), P(-4, 0), P(-1, 4)
for l, p1, p2 in [(3*x - 4*y + 12, A, B), (2*x - 5*y + 22, A, C), (4*x - 3*y + 16, B, C), (x + y - 3, C, (A + B) / 2)]:
    assert rajta(l, p1) and rajta(l, p2)
assert rajta(4*x + 3*y - 8, C) and (B - A)[0] * 3 - (B - A)[1] * 4 == 0   # normalvektor (4;3) || AB
assert rajta(3*x - 4*y + 19, C)
chk("k13", [tav(A, B), pe(3*x - 4*y + 12, C), tav(A, B) * pe(3*x - 4*y + 12, C) / 2], [10, Q(7, 5), 7])
A, B, C = P(-5, -4), P(9, -2), P(4, 8)
for l, p1, p2 in [(x - 7*y - 23, A, B), (4*x - 3*y + 8, A, C), (2*x + y - 16, B, C), (11*x - 2*y - 28, C, (A + B) / 2)]:
    assert rajta(l, p1) and rajta(l, p2)
assert rajta(x - 2*y - 3, A) and (C - B).dot(P(2, 1)) == 0
detABC = (B - A)[0]*(C - A)[1] - (B - A)[1]*(C - A)[0]
chk("k14", Abs(detABC) / 2, 75)
chk("k15", [egy(x - 3*y + 14, 7*x + 2*y + 6), egy(7*x + 2*y + 6, 8*x - y - 3), egy(x - 3*y + 14, 8*x - y - 3)],
    [P(-2, 4), P(0, -3), P(1, 5)])
chk("k15T", Abs((P(0, -3) - P(-2, 4))[0]*(P(1, 5) - P(-2, 4))[1] - (P(0, -3) - P(-2, 4))[1]*(P(1, 5) - P(-2, 4))[0]) / 2, Q(23, 2))
V1, V2, V3 = egy(3*x - 2*y - 19, 2*x + y + 6), egy(2*x + y + 6, x - 3*y + 10), egy(x - 3*y + 10, 3*x - 2*y - 19)
chk("k16", [V1, V2, V3], [P(1, -8), P(-4, 2), P(11, 7)])
chk("k16T", Abs((V2 - V1)[0]*(V3 - V1)[1] - (V2 - V1)[1]*(V3 - V1)[0]) / 2, Q(175, 2))
chk("k17", sorted(solve(Abs(c) / 5 - 2, c)), [-10, 10])
chk("k18", [pe(x - y + 1, (4, 1)), egy(x - y + 1, x + y - 5)], [2*sqrt(2), P(2, 3)])
assert rajta(x + y - 5, (4, 1)); chk("k18k", 2*sqrt(2), 2.83, .005)
# --- nehéz
A, B, C = P(-5, -4), P(9, -2), P(4, 8)
AB, AC = B - A, C - A
chk("n1", [tav(A, B), tav(B, (A + C) / 2), pe(x - 7*y - 23, C), acos(AB.dot(AC) / (AB.norm() * AC.norm())) * 180 / pi],
    [10*sqrt(2), sqrt(425)/2, 15*sqrt(2)/2, 45])
chk("n1k", [sqrt(425)/2, 5*sqrt(17)/2], [5*sqrt(17)/2, sqrt(425)/2])
chk("n1k1", 10*sqrt(2), 14.14, .005); chk("n1k2", 5*sqrt(17)/2, 10.31, .005); chk("n1k3", 15*sqrt(2)/2, 10.61, .005)
A, B, C = P(-2, -1), P(4, 1), P(5, 4)
D_ = A + C - B
assert rajta(x + 5*y - 9, B) and rajta(x + 5*y - 9, D_)
chk("n2", [D_, Abs((B - A)[0]*(D_ - A)[1] - (B - A)[1]*(D_ - A)[0]), (A + C) / 2], [P(-1, 2), 16, P(Q(3, 2), Q(3, 2))])
A, C = P(1, 1), P(5, 3)
O = (A + C) / 2; h = (C - A) / 2; r = P(-h[1], h[0])
chk("n3", [O + r, O - r], [P(2, 4), P(4, 0)])
chk("n3b", [tav(P(1, 1), P(2, 4)), tav(P(2, 4), P(5, 3)), (P(2, 4) - P(1, 1)).dot(P(5, 3) - P(2, 4))], [sqrt(10), sqrt(10), 0])
Mt = egy(x - 2*y + 3, 2*x + y - 9)
chk("n4", [Mt, 2*Mt - P(5, -1)], [P(3, 3), P(1, 7)]); assert rajta(2*x + y - 9, (5, -1))
Bt = P(7, -3)
Pk = egy(y, (y - 5) * (7 - 1) - (-3 - 5) * (x - 1))
chk("n5", [Pk, tav(P(1, 5), Bt), tav(P(1, 5), Pk) + tav(Pk, P(7, 3))], [P(Q(19, 4), 0), 10, 10])
# joker
pts = [(i, (100 - 3*i) // 5) for i in range(1, 34) if (100 - 3*i) % 5 == 0 and (100 - 3*i) > 0]
chk("jok", [len(pts), pts[0], pts[-1]], [6, (5, 17), (30, 2)])
assert not E, E
print("sympy önteszt: OK")

# ============================== ÁBRÁK ==============================
def abra(svg):
    return f'<div class="svgwrap">{svg}</div>'


SVG_GRAFIKON = svg_koordsik(
    xr=(-3, 4), yr=(-3, 6), egyseg=30,
    egyenesek=[((2, -1, 1), KEK, "", {})],
    pontok=[((-1, -1), "A", {"dx": -16, "dy": 4}), ((2, 5), "B", {"dx": 14, "dy": 4})],
    leiras="Egyenes a koordináta-rendszerben, amely átmegy a rácspontokon fekvő A és B ponton")

SVG_ABRAZOLAS = svg_koordsik(
    xr=(-5, 4), yr=(-2, 4), egyseg=32, szamok=False,
    egyenesek=[((2, 3, -6), KEK, "", {}), ((1, -2, 4), PIROS, "", {})],
    pontok=[((3, 0), "", {"szin": KEK}), ((0, 2), "", {"szin": ZOLD}), ((-4, 0), "", {"szin": PIROS})],
    leiras="A 2x + 3y − 6 = 0 egyenes a (3;0) és a (0;2), az x − 2y + 4 = 0 egyenes a (−4;0) és a (0;2) "
           "ponton megy át; a két egyenes a (0;2) pontban metszi egymást")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- B1: az egyenes egyenlete (alap 1–10)
 (r"Illeszkedik-e a pont a $p\colon 2x-5y+8=0$ egyenesre?",
  [r"$A(1;2)$", r"$B(-9;-2)$", r"$C(-2;1)$", r"$D\left(-\tfrac32;1\right)$", r"$E(-4;0)$", r"$F(8;5)$"],
  [r"igen", r"igen", r"nem", r"igen", r"igen", r"nem"], True),

 (r"Határozd meg a $b$ valós paraméter értékét úgy, hogy a $p\colon 3x+by+11=0$ egyenes átmenjen a "
  r"$P(-1;2)$ ponton!", None, r"$b=-4$"),

 (r"Határozd meg az $a$ valós paraméter értékét úgy, hogy a $q\colon ax+4y-13=0$ egyenes átmenjen a "
  r"$Q(5;-3)$ ponton!", None, r"$a=5$"),

 (r"Add meg az egyenes iránytényezőjét! Ha nincs, indokold!",
  [r"$y=3x-1$", r"$x+2y-4=0$", r"$y=5$", r"$x=-2$"],
  [r"$k=3$", r"$k=-\tfrac12$", r"$k=0$", r"nincs: az egyenes függőleges"], True),

 (r"Határozd meg, hol metszi az $e\colon 4x-5y+10=0$ egyenes az $x$-tengelyt és az $y$-tengelyt!", None,
  r"$\left(-\tfrac52;0\right)$ és $(0;2)$"),

 (r"Írd fel annak az egyenesnek az egyenletét, amely a pozitív $x$-tengellyel $\alpha$ szöget zár be, "
  r"és az $y$-tengelyt a $(0;n)$ pontban metszi!",
  [r"$\alpha=45^\circ$, $n=3$", r"$\alpha=135^\circ$, $n=-4$", r"$\alpha=60^\circ$, $n=-2$",
   r"$\alpha=135^\circ$, $n=\tfrac23$"],
  [r"$y=x+3$", r"$y=-x-4$", r"$y=\sqrt3\,x-2$", r"$y=-x+\tfrac23$, azaz $3x+3y-2=0$"], True),

 (r"Írd fel annak az egyenesnek az egyenletét, amely a pozitív $x$-tengellyel $\alpha$ szöget zár be, "
  r"és átmegy az $A$ ponton!",
  [r"$\alpha=45^\circ$, $A(3;2)$", r"$\alpha=135^\circ$, $A(-4;-1)$", r"$\alpha=60^\circ$, $A(-2;3)$",
   r"$\alpha=135^\circ$, $A(5;-2)$"],
  [r"$y=x-1$", r"$y=-x-5$", r"$y=\sqrt3\,x+2\sqrt3+3$", r"$y=-x+3$"], True),

 (r"Írd fel a két ponton átmenő egyenes egyenletét általános alakban!",
  [r"$A(1;5)$, $B(-3;4)$", r"$M(-2;-3)$, $N(0;1)$", r"$P\left(\tfrac12;5\right)$, $Q(5;0)$",
   r"$C(-3;1)$, $D(-2;-4)$"],
  [r"$x-4y+19=0$", r"$2x-y+1=0$", r"$10x+9y-50=0$", r"$5x+y+14=0$"], True),

 (r"Írd fel az egyenes egyenletét explicit és tengelymetszetes alakban!",
  [r"$4x-5y-10=0$", r"$3x+6y-21=0$"],
  [r"$y=\tfrac45x-2$ és $\dfrac{x}{\frac52}+\dfrac{y}{-2}=1$",
   r"$y=-\tfrac12x+\tfrac72$ és $\dfrac{x}{7}+\dfrac{y}{\frac72}=1$"]),

 (r"Ábrázold egy koordináta-rendszerben a $2x+3y-6=0$ és az $x-2y+4=0$ egyenest a tengelymetszeteik "
  r"segítségével! Hol metszi egymást a két egyenes?", None,
  [r"$2x+3y-6=0$ (kék): $(3;0)$ és $(0;2)$; $x-2y+4=0$ (piros): $(-4;0)$ és $(0;2)$",
   r"a metszéspont $(0;2)$ — mindkét egyenes ott metszi az $y$-tengelyt",
   r"az ábra (egy rácsköz egy egység):" + abra(SVG_ABRAZOLAS)]),

 # --- B2: két egyenes (alap 11–18)
 (r"Határozd meg a két egyenes metszéspontját!",
  [r"$x+2y-2=0$, $3x-y-13=0$", r"$x-3y+17=0$, $3x+7y-29=0$", r"$4x+3y+5=0$, $2x+y+2=0$"],
  [r"$(4;-1)$", r"$(-2;5)$", r"$\left(-\tfrac12;-1\right)$"], True),

 (r"Határozd meg a két egyenes kölcsönös helyzetét! Ha metszik egymást, add meg a metszéspontot is.",
  [r"$2x-y+3=0$ és $4x-2y+6=0$", r"$3x+y-2=0$ és $6x+2y+5=0$", r"$x+2y-4=0$ és $3x-y-5=0$",
   r"$y=-x+4$ és $y=2x-5$"],
  [r"egybeesnek", r"párhuzamosak (nincs közös pontjuk)", r"metszők, $M(2;1)$", r"metszők, $M(3;1)$"]),

 (r"Párhuzamos, merőleges vagy egyik sem?",
  [r"$y=2x+1$ és $4x-2y+3=0$", r"$3x-y+2=0$ és $x+3y-1=0$", r"$y=x$ és $y=-2x+1$"],
  [r"párhuzamos ($k_1=k_2=2$)", r"merőleges ($k_1k_2=3\cdot\left(-\tfrac13\right)=-1$)",
   r"egyik sem ($k_1=1$, $k_2=-2$)"]),

 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy a $P$ ponton és párhuzamos az $e$ egyenessel!",
  [r"$P(4;-3)$, $e\colon 2x-3y+6=0$", r"$P(-4;3)$, $e\colon 2x-5y-4=0$", r"$P(-2;1)$, $e\colon x-4y-11=0$"],
  [r"$2x-3y-17=0$", r"$2x-5y+23=0$", r"$x-4y+6=0$"]),

 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy az $M$ ponton és merőleges az $l$ egyenesre!",
  [r"$M(-3;2)$, $l\colon 5x-3y-6=0$", r"$M(2;-3)$, $l\colon 2x-3y+5=0$", r"$M(-2;5)$, $l\colon x-7y+14=0$"],
  [r"$3x+5y-1=0$", r"$3x+2y=0$", r"$7x+y+9=0$"]),

 (r"Mekkora szöget zár be a két egyenes?",
  [r"$3x-y+2=0$ és $x-2y+2=0$", r"$x+4y-4=0$ és $3x-5y-12=0$", r"$x+3=0$ és $y-2=0$"],
  [r"$45^\circ$", r"$45^\circ$", r"$90^\circ$"], True),

 (r"Írd fel az $AB$ szakasz felezőmerőlegesének egyenletét!",
  [r"$A(1;-2)$, $B(3;-4)$", r"$A(-7;1)$, $B(3;5)$"],
  [r"$x-y-5=0$", r"$5x+2y+4=0$"], True),

 (r"Mekkora szöget zár be a két egyenes? Számológéppel dolgozz, és egy tizedesre kerekíts!",
  [r"$y=3x$ és $y=x$", r"$y=2x-1$ és $x+2y=0$", r"$y=\sqrt3\,x$ és $y=\tfrac{1}{\sqrt3}\,x$"],
  [r"$\operatorname{tg}\varphi=\tfrac12$, $\varphi\approx26{,}6^\circ$", r"$90^\circ$", r"$30^\circ$"]),

 # --- B3: pont és egyenes távolsága (alap 19–24)
 (r"Számítsd ki az $M$ pont távolságát az $l$ egyenestől!",
  [r"$M(4;-1)$, $l\colon 12x-5y-27=0$", r"$M(3;2)$, $l\colon 3x-4y+15=0$",
   r"$M(-1;-2)$, $l\colon y=\tfrac12x+\tfrac72$", r"$M(7;-4)$, $l\colon y=\tfrac23x$"],
  [r"$d=2$", r"$d=\tfrac{16}{5}$", r"$d=2\sqrt5\approx4{,}47$", r"$d=2\sqrt{13}\approx7{,}21$"]),

 (r"Számítsd ki a két párhuzamos egyenes távolságát!",
  [r"$5x-12y+26=0$ és $5x-12y-13=0$", r"$y=-3x-17$ és $y=-3x+3$"],
  [r"$d=3$", r"$d=2\sqrt{10}\approx6{,}32$"], True),

 (r"Milyen messze van az egyenes az origótól?",
  [r"$3x+4y-20=0$", r"$x-y+2=0$"],
  [r"$4$", r"$\sqrt2\approx1{,}41$"], True),

 (r"Egy mozgásérzékelő a $P(1;2)$ pontban van (egy egység $1$ méter), és $2$ méteren belül jelez. "
  r"Egy robotporszívó a $3x-4y+10=0$ egyenes mentén halad. Jelez-e az érzékelő?", None,
  r"igen: a pálya távolsága az érzékelőtől $d=1$ m, és $1\lt2$"),

 (r"Adott az $A(0;0)$, $B(4;3)$, $C(1;-3)$ csúcsú háromszög.",
  [r"Írd fel az $AB$ oldalegyenes egyenletét!", r"Számítsd ki a $C$ csúcshoz tartozó $m_c$ magasság hosszát!",
   r"Számítsd ki a háromszög területét az $AB$ oldalból és az $m_c$ magasságból!"],
  [r"$3x-4y=0$", r"$m_c=3$", r"$AB=5$, $T=\frac{5\cdot3}{2}=7{,}5$"]),

 (r"Maxi a $P(1;2)$ pont távolságát számolta ki az $y=3x+1$ egyenestől. Így írt: $a=3$, $b=1$, $c=1$, "
  r"tehát $d=\dfrac{|3\cdot1+1\cdot2+1|}{\sqrt{10}}=\dfrac{6}{\sqrt{10}}\approx1{,}90$. Hol a hiba? Mennyi a "
  r"helyes távolság?", None,
  r"Az együtthatókat csak általános alakból lehet leolvasni: $3x-y+1=0$, tehát $b=-1$. A helyes távolság "
  r"$d=\dfrac{2}{\sqrt{10}}\approx0{,}63$."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- B1 (közép 1–6)
 (r"Az ábrán látható egyenes két rácsponton, $A$-n és $B$-n megy át. Olvasd le a pontok koordinátáit, "
  r"és írd fel az egyenes egyenletét explicit alakban!" + abra(SVG_GRAFIKON), None,
  r"$A(-1;-1)$, $B(2;5)$, az egyenes $y=2x+1$"),

 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy az $M(4;-1)$ ponton és a $2x-y-4=0$ és "
  r"az $x+y-5=0$ egyenes metszéspontján!", None, r"a metszéspont $(3;2)$, az egyenes $3x+y-11=0$"),

 (r"Írd fel explicit alakban annak az egyenesnek az egyenletét, amely átmegy a $P(4;3)$ ponton és a "
  r"$3x-5y-11=0$ és a $4x+y-7=0$ egyenes metszéspontján!", None, r"a metszéspont $(2;-1)$, az egyenes $y=2x-5$"),

 (r"Mekkora területű háromszöget zár közre a $3x+2y-12=0$ egyenes a két koordinátatengellyel?", None,
  r"a tengelymetszetek $(4;0)$ és $(0;6)$, a terület $T=12$"),

 (r"Egy taxi alapdíja $200$ dinár, és minden megtett kilométer $80$ dinárba kerül.",
  [r"Írd fel egy egyenes egyenleteként, hogyan függ a fizetendő összeg ($y$) a megtett úttól ($x$ km)!",
   r"Mennyit fizetünk egy $12$ km-es útért?", r"Mit jelent az iránytényező és az $n$ a feladatban?"],
  [r"$y=80x+200$", r"$1160$ dinárt", r"$k=80$: ennyivel nő az ár kilométerenként; $n=200$: az alapdíj"]),

 (r"Maxi a $3x-2y+6=0$ egyenes tengelymetszetes alakját így írta fel: $\dfrac x2+\dfrac y3=1$. "
  r"Hol a hiba? Mi a helyes alak?", None,
  r"$3x-2y=-6$, ezt $-6$-tal kell osztani: $\dfrac{x}{-2}+\dfrac{y}{3}=1$ (az $x$-tengelyt a $(-2;0)$ "
  r"pontban metszi)."),

 # --- B2 (közép 7–12)
 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy az $y=-2x+11$ és az $y=-x+8$ egyenes "
  r"metszéspontján, és párhuzamos az $5x+3y-2=0$ egyenessel!", None,
  r"a metszéspont $(3;5)$, az egyenes $5x+3y-30=0$"),

 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy a $4x-3y-8=0$ és az $x+2y-13=0$ egyenes "
  r"metszéspontján, és merőleges az $y=-3x+8$ egyenesre!", None,
  r"a metszéspont $(5;4)$, az egyenes $x-3y+7=0$"),

 (r"Az $l_1\colon x+3y-3=0$ és az $l_2\colon x-2y-2=0$ egyenes metszéspontján át merőlegest állítunk az "
  r"$l_2$ egyenesre. Írd fel ennek az egyenesnek az egyenletét!", None,
  r"a metszéspont $\left(\tfrac{12}{5};\tfrac15\right)$, az egyenes $2x+y-5=0$"),

 (r"Az $ABC$ háromszög csúcsai $A(-1;-4)$, $B(5;6)$ és $C(-3;2)$.",
  [r"Írd fel a három súlyvonal egyenesének egyenletét!", r"Írd fel az $A$ csúcshoz tartozó "
   r"magasságvonal egyenletét!"],
  [r"$t_a\colon 4x-y=0$, $t_b\colon x-y+1=0$, $t_c\colon x+5y-7=0$", r"$m_a\colon 2x+y+6=0$"]),

 (r"Adott az $ax+2y-3=0$ és a $3x-6y+1=0$ egyenes. Határozd meg $a$ értékét úgy, hogy a két egyenes",
  [r"párhuzamos legyen;", r"merőleges legyen!"],
  [r"$a=-1$", r"$a=4$"], True),

 (r"Határozd meg az $y=2x+1$ és az $x+2y-12=0$ egyenes metszéspontját! Milyen szöget zár be a két "
  r"egyenes?", None, r"$M(2;5)$; merőlegesek ($k_1k_2=2\cdot\left(-\tfrac12\right)=-1$), a szög $90^\circ$"),

 # --- B3 (közép 13–18)
 (r"Az $ABC$ háromszög csúcsai $A(4;6)$, $B(-4;0)$ és $C(-1;4)$. Határozd meg",
  [r"az oldalegyenesek egyenletét;", r"a $C$ csúcshoz tartozó magasságvonal egyenletét;",
   r"az $AB$ oldal hosszát és az $m_c$ magasság hosszát;", r"a háromszög területét!"],
  [r"$AB\colon 3x-4y+12=0$, $AC\colon 2x-5y+22=0$, $BC\colon 4x-3y+16=0$",
   r"$4x+3y-8=0$", r"$AB=10$, $m_c=\tfrac75$", r"$T=7$"]),

 (r"Az $ABC$ háromszög csúcsai $A(-5;-4)$, $B(9;-2)$ és $C(4;8)$. Határozd meg",
  [r"a háromszög területét;", r"az oldalegyenesek egyenletét;",
   r"a $C$ csúcshoz tartozó súlyvonal egyenesének egyenletét;", r"az $A$ csúcshoz tartozó magasságvonal "
   r"egyenletét!"],
  [r"$T=75$", r"$AB\colon x-7y-23=0$, $AC\colon 4x-3y+8=0$, $BC\colon 2x+y-16=0$",
   r"$11x-2y-28=0$", r"$x-2y-3=0$"]),

 (r"Egy háromszög oldalai az $x-3y+14=0$, a $7x+2y+6=0$ és a $8x-y-3=0$ egyenesre illeszkednek. "
  r"Határozd meg a csúcsokat és a háromszög területét!", None,
  r"$(-2;4)$, $(0;-3)$, $(1;5)$; $T=11{,}5$"),

 (r"Egy háromszög oldalai a $3x-2y-19=0$, a $2x+y+6=0$ és az $x-3y+10=0$ egyenesre illeszkednek. "
  r"Határozd meg a csúcsokat és a területet!", None, r"$(1;-8)$, $(-4;2)$, $(11;7)$; $T=87{,}5$"),

 (r"Határozd meg a $c$ értékét úgy, hogy a $3x+4y+c=0$ egyenes $2$ egységnyire legyen az origótól!", None,
  r"$c=10$ vagy $c=-10$"),

 (r"Egy kút a $P(4;1)$ pontban van, a vízvezeték az $x-y+1=0$ egyenes mentén halad (egy egység "
  r"$1$ méter). A kutat a lehető legrövidebb csővel kötik be a vezetékbe.",
  [r"Milyen hosszú a cső?", r"Hol csatlakozik a cső a vezetékhez?"],
  [r"$2\sqrt2\approx2{,}83$ m", r"$M(2;3)$"], True),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Folytassuk a közép 14. feladat háromszögével: $A(-5;-4)$, $B(9;-2)$ és $C(4;8)$. Határozd meg",
  [r"az $AB$ oldal hosszát;", r"a $B$ csúcshoz tartozó $t_b$ súlyvonal hosszát;",
   r"a $C$ csúcshoz tartozó $m_c$ magasság hosszát;",
   r"a $BAC\sphericalangle$ nagyságát! <i>(Tipp: számold ki az $AB$ és az $AC$ egyenes szögét, és gondold "
   r"meg, hogy a háromszög $A$-nál lévő szöge hegyes-e.)</i>"],
  [r"$AB=10\sqrt2\approx14{,}14$", r"$t_b=\dfrac{\sqrt{425}}{2}=\dfrac{5\sqrt{17}}{2}\approx10{,}31$",
   r"$m_c=\dfrac{15\sqrt2}{2}\approx10{,}61$", r"$45^\circ$"]),

 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(-2;-1)$, $B(4;1)$ és $C(5;4)$.",
  [r"Határozd meg a $D$ csúcsot!", r"Számítsd ki a paralelogramma területét!",
   r"Határozd meg az átlók $M$ metszéspontját, és írd fel a $BD$ átló egyenesének egyenletét!"],
  [r"$D(-1;2)$", r"$T=16$", r"$M\left(\tfrac32;\tfrac32\right)$, $BD\colon x+5y-9=0$"]),

 (r"Az $ABCD$ négyzet két szemközti csúcsa $A(1;1)$ és $C(5;3)$. Határozd meg a másik két csúcsot! "
  r"<i>(A négyzet átlói egyenlő hosszúak, merőlegesek, és felezik egymást.)</i>", None,
  r"$B(2;4)$ és $D(4;0)$ (vagy fordított betűzéssel)"),

 (r"Határozd meg a $P(5;-1)$ pont tükörképét az $e\colon x-2y+3=0$ egyenesre!",
  [r"Írd fel a $P$-n átmenő, $e$-re merőleges egyenes egyenletét!",
   r"Határozd meg a talppontot, vagyis a merőleges és az $e$ metszéspontját!",
   r"Határozd meg a $P'$ tükörképet!"],
  [r"$2x+y-9=0$", r"$M(3;3)$", r"$P'(1;7)$"]),

 (r"Két ház az $A(1;5)$ és a $B(7;3)$ pontban áll, a folyópart az $x$-tengely (egy egység $100$ méter). "
  r"A parton egy $P$ szivattyút építenek, és onnan mindkét házhoz egyenes csövet vezetnek. Hová kerüljön a "
  r"szivattyú, hogy a két cső együttes hossza a lehető legkisebb legyen? Mekkora ez a hossz? "
  r"<i>(Tükrözd a $B$ pontot a partra!)</i>", None,
  r"$P\left(\tfrac{19}{4};0\right)$, a csövek együttes hossza $10$ egység, azaz $1000$ m"),
]

JOKER = (r"Egy bolt $3$ és $5$ talléros kuponokat árul. Pontosan $100$ tallér értékben szeretnél kuponokat venni "
         r"úgy, hogy mindkét fajtából legalább egyet vásárolsz. Ha $x$ darab $3$ tallérost és $y$ darab $5$ "
         r"tallérost veszel, akkor $3x+5y=100$.",
         [r"az egyenes első síknegyedbe eső rácspontjait keressük", r"$6$ lehetőség: $(5;17)$, $(10;14)$, "
          r"$(15;11)$, $(20;8)$, $(25;5)$, $(30;2)$"],
         [r"Mit jelent a feladat az egyenes pontjainak nyelvén?",
          r"Hányféleképpen vásárolhatsz? Sorold fel a lehetőségeket!"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (24, 18, 5), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="05-analitikus-geometria", fajl="feladatok-egyenesek.html",
           cim="Egyenesek", temakor="Síkbeli analitikus geometria",
           alcim="Az egyenes egyenletei, két egyenes helyzete és szöge, pont és egyenes távolsága. "
                 "Számológép használható: a szögeket egy, minden más közelítő értéket két tizedesre "
                 "kerekíts. A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-pont-es-egyenes-tavolsaga.html", prevc="Pont és egyenes távolsága",
           nxt="tananyag-kor-egyenlete.html", nxtc="A kör egyenlete")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
