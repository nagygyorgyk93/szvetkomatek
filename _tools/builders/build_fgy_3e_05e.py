# -*- coding: utf-8 -*-
"""3e/05 — 5. feladatgyujtemeny: a parabola (E1-E2).
Horgony-terv: narrativa_05-analitikus-geometria.md · feladat-terkep: terkep_fgy_05-analitikus-geometria.md.
Forras-szamok: 6. Feladatok - Analitikus geometria - II. resz.pdf (46-58).
Forrashibak: 46c (p>0 konvencio: p=4), 46d (y^2=24x)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import sqrt, Rational as Q, symbols, solve, simplify, N, expand, Poly
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(a, b) for a, b in zip(g, w))
    return simplify(g - w) == 0


def chk(nev, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((nev, g, w))


x, y, n, p = symbols("x y n p", real=True)


def metsz(g, l):
    s = solve([g, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s if r[x].is_real and r[y].is_real],
                  key=lambda u: (float(N(u[0])), float(N(u[1]))))


def rajta(g, pt):
    return simplify(g.subs({x: pt[0], y: pt[1]})) == 0


def aranyos(p1, p2):
    a, b = Poly(expand(p1), x).all_coeffs(), Poly(expand(p2), x).all_coeffs()
    return len(a) == len(b) and all(simplify(a[i] * b[j] - a[j] * b[i]) == 0 for i in range(len(a)) for j in range(len(a)))


def felt(g, k, par, valt):
    e = expand(g.subs(y, k * x + par))
    A2, B2, C2 = Poly(e, x).all_coeffs()
    return e, sorted(solve(B2**2 - 4 * A2 * C2, valt), key=lambda u: float(N(u)))


def yparab(p2):
    """y^2 = 2p x: (p, fokusz x, vezeregyenes)"""
    pp = Q(p2) / 2
    return (abs(pp), pp / 2, -pp / 2)


# --- alap
chk("a1", [yparab(4), yparab(Q(5, 2)), yparab(-8), yparab(24)],
    [(2, 1, -1), (Q(5, 4), Q(5, 8), Q(-5, 8)), (4, -2, 2), (12, 6, -6)])
chk("a2", [Q(9, 1) / 1, Q(64, 2), Q(1, -4), Q(16, -6)], [9, 32, Q(-1, 4), Q(-8, 3)])
chk("a3", [(Q(8, 2) / 2, -Q(8, 2) / 2), (Q(-12, 2) / 2, Q(12, 2) / 2)], [(2, -2), (-3, 3)])
chk("a4", [Q(4, 2), Q(4, 2) / 2], [2, 1])
chk("a5", [b**2 - 6*a for a, b in [(6, 6), (3, -3*sqrt(2)), (2, 4), (0, 0)]], [0, 0, 4, 0])
P48 = y**2 - 4*x
chk("a6", [metsz(P48, x - 2*y + 4), metsz(P48, 2*x - y - 4), metsz(P48, 2*x - y + 1)], [[(4, 4)], [(1, -2), (4, 4)], []])
assert metsz(y**2 - 6*x, x - 2*y + 6) == [(6, 6)]
assert rajta(y**2 - 2*x, (8, -4)) and metsz(y**2 - 2*x, x + 4*y + 8) == [(8, -4)]
chk("a9", [metsz(y**2 - 9*x, y - 3), metsz(y**2 - 9*x, y + 6)], [[(1, 3)], [(4, -6)]])
assert rajta(y**2 - 10*x, (Q(5, 2), -5)) and metsz(y**2 - 10*x, 2*x + 2*y + 5) == [(Q(5, 2), -5)]
# --- közép
chk("k1", [2 * 2 * 3, -2 * 2 * 5], [12, -20])
chk("k2", [solve(80**2 - 2*p*40, p), Q(80, 2)], [[80], 40])
chk("k3", Q(12, 2) / 2, 3)
chk("k4", [metsz(y**2 - 16*x, x - 6), 6 + 4, sqrt((6 - 4)**2 + 96)], [[(6, -4*sqrt(6)), (6, 4*sqrt(6))], 10, 10])
M49 = metsz(P48, 2*x - y - 4)
chk("k5", sqrt((M49[1][0] - M49[0][0])**2 + (M49[1][1] - M49[0][1])**2), 3*sqrt(5)); chk("k5k", 3*sqrt(5), 6.71, .005)
M58 = metsz(y**2 - 18*x, y - 2*x - 2)
chk("k6", M58, [(Q(1, 2), 3), (2, 6)])
assert metsz(y**2 - 18*x, 6*x - 2*y + 3) == [(Q(1, 2), 3)] and metsz(y**2 - 18*x, 3*x - 2*y + 6) == [(2, 6)]
assert rajta(y**2 + 16*x, (-1, -4)) and metsz(y**2 + 16*x, y - 2*x + 2) == [(-1, -4)]
assert solve(2*x - 2, x) == [1]
chk("k8", [solve(10**2 + 2*p*(-5), p), 5 - Q(16, 20)], [[10], Q(21, 5)])
# --- nehéz
e1, s1 = felt(y**2 - 3*x, Q(1, 4), n, n)
chk("n1", s1, [3]); assert aranyos(e1, x**2 + (8*n - 48)*x + 16*n**2)
assert metsz(y**2 - 3*x, x - 4*y + 12) == [(12, 6)]
e2, s2 = felt(y**2 - 12*x, 1, n, n)
chk("n2", s2, [3]); assert aranyos(e2, x**2 + (2*n - 12)*x + n**2) and metsz(y**2 - 12*x, y - x - 3) == [(3, 6)]
e3, s3 = felt(y**2 - 8*x, 2, n, n)
chk("n3", s3, [1]); assert aranyos(e3, 4*x**2 + (4*n - 8)*x + n**2) and metsz(y**2 - 8*x, y - 2*x - 1) == [(Q(1, 2), 2)]
e4, s4 = felt(y**2 - 2*p*x, Q(-3, 2), Q(-3, 2), p)
chk("n4", s4, [0, Q(9, 2)]); assert aranyos(e4, Q(9, 4)*x**2 + (Q(9, 2) - 2*p)*x + Q(9, 4))
assert metsz(y**2 - 9*x, 3*x + 2*y + 3) == [(1, -3)]
# joker
J = metsz(y**2 - 4*x, x**2 - 4*y)
chk("jok", [J, sqrt(16 + 16)], [[(0, 0), (4, 4)], 4*sqrt(2)]); chk("jokk", 4*sqrt(2), 5.66, .005)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- E1: a parabola (alap 1–5)
 (r"Határozd meg a parabola $p$ paraméterét, a fókuszpontját és a vezéregyenesét! Melyik irányba nyílik?",
  [r"$y^2=4x$", r"$y^2=\tfrac52x$", r"$y^2=-8x$", r"$y^2=24x$"],
  [r"$p=2$, $F(1;0)$, $x=-1$; jobbra", r"$p=\tfrac54$, $F\left(\tfrac58;0\right)$, $x=-\tfrac58$; jobbra",
   r"$p=4$, $F(-2;0)$, $x=2$; balra", r"$p=12$, $F(6;0)$, $x=-6$; jobbra"]),

 (r"Írd fel annak az origó csúcspontú, $x$-tengelyű parabolának az egyenletét, amely átmegy a ponton!",
  [r"$A(1;-3)$", r"$B(2;8)$", r"$C(-4;1)$", r"$D(-6;4)$"],
  [r"$y^2=9x$", r"$y^2=32x$", r"$y^2=-\tfrac14x$", r"$y^2=-\tfrac83x$"], True),

 (r"Határozd meg a parabola fókuszpontját és vezéregyenesét!",
  [r"$x^2=8y$", r"$x^2=-12y$"],
  [r"$F(0;2)$, $y=-2$", r"$F(0;-3)$, $y=3$"], True),

 (r"Az $y=\tfrac14x^2$ függvény grafikonja parabola. Írd fel $x^2=2py$ alakban, és add meg a paraméterét, a "
  r"fókuszpontját és a vezéregyenesét!", None, r"$x^2=4y$; $p=2$, $F(0;1)$, $y=-1$"),

 (r"Rajta van-e a pont az $y^2=6x$ parabolán?",
  [r"$(6;6)$", r"$\left(3;-3\sqrt2\right)$", r"$(2;4)$", r"$(0;0)$"],
  [r"igen", r"igen", r"nem ($16\ne12$)", r"igen (ez a csúcspont)"], True),

 # --- E2: a parabola és az egyenes (alap 6–10)
 (r"Határozd meg az $y^2=4x$ parabola és az $l$ egyenes kölcsönös helyzetét! Ha van közös pontjuk, add meg.",
  [r"$l\colon x-2y+4=0$", r"$l\colon 2x-y-4=0$", r"$l\colon 2x-y+1=0$"],
  [r"érintő: $(4;4)$", r"szelő: $(1;-2)$ és $(4;4)$", r"nincs közös pontjuk"]),

 (r"Írd fel az $y^2=6x$ parabola érintőjének egyenletét az $A(6;6)$ pontjában!", None, r"$x-2y+6=0$"),

 (r"Az $y^2=2x$ parabola $A$ pontjának első koordinátája $8$, a második negatív. Írd fel a parabola érintőjét "
  r"$A$-ban!", None, r"$A(8;-4)$, az érintő $x+4y+8=0$"),

 (r"Hány közös pontja van az $y^2=9x$ parabolának és az egyenesnek? Érintő-e az egyenes?",
  [r"$y=3$", r"$y=-6$"],
  [r"egy: $(1;3)$; nem érintő, párhuzamos a parabola tengelyével", r"egy: $(4;-6)$; nem érintő, ez is "
   r"párhuzamos a tengellyel"]),

 (r"Az $y^2=10x$ parabola $M$ pontjának első koordinátája $\tfrac52$, a második negatív. Írd fel a parabola "
  r"érintőjét $M$-ben!", None, r"$M\left(\tfrac52;-5\right)$, az érintő $2x+2y+5=0$"),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- E1 (közép 1–4)
 (r"Írd fel az origó csúcspontú, $x$-tengelyű parabola egyenletét, ha",
  [r"a fókuszpontja $F(3;0)$;", r"a vezéregyenese az $x=5$ egyenes!"],
  [r"$y^2=12x$", r"$y^2=-20x$"], True),

 (r"Egy parabolaantenna tányérjának átmérője $160$ cm, a mélysége $40$ cm. A vevőfejet a fókuszpontba kell "
  r"szerelni. Milyen messze lesz a vevőfej a tányér aljától? <i>(Helyezd a tányér alját az origóba, a tengelyét "
  r"az $x$-tengelyre: a peremnek a $(40;80)$ pont felel meg.)</i>", None,
  r"$y^2=160x$, $F(40;0)$: a vevőfej $40$ cm-re van a tányér aljától"),

 (r"Maxi szerint az $y^2=12x$ parabola fókuszpontja $F(6;0)$, „hiszen $2p=12$, a fókusz pedig $(p;0)$”. Hol a hiba?",
  None, r"a fókusz $\left(\tfrac p2;0\right)$: $p=6$, tehát $F(3;0)$"),

 (r"Az $y^2=16x$ parabola egy pontjának első koordinátája $6$. Milyen messze van ez a pont a fókuszponttól? "
  r"<i>(Használd a parabola definícióját: a fókusztól és a vezéregyenestől mért távolság egyenlő.)</i>", None,
  r"$P\left(6;\pm4\sqrt6\right)$, $F(4;0)$, a távolság $|PF|=6+4=10$"),

 # --- E2 (közép 5–8)
 (r"Milyen hosszú húrt metsz ki az $y^2=4x$ parabola a $2x-y-4=0$ egyenesből?", None,
  r"a metszéspontok $(1;-2)$ és $(4;4)$, a húr $3\sqrt5\approx6{,}71$"),

 (r"Határozd meg az $y^2=18x$ parabola és az $y=2x+2$ egyenes metszéspontjait, majd írd fel a parabola "
  r"érintőit ezekben a pontokban!", None,
  r"$\left(\tfrac12;3\right)$ és $(2;6)$; az érintők $6x-2y+3=0$ és $3x-2y+6=0$"),

 (r"Az $y^2=-16x$ parabola $M$ pontjának első koordinátája $-1$, a második negatív. Írd fel a parabola érintőjét "
  r"$M$-ben, és határozd meg, hol metszi az érintő a koordinátatengelyeket!", None,
  r"$M(-1;-4)$, az érintő $y=2x-2$; tengelymetszetei $(1;0)$ és $(0;-2)$"),

 (r"Egy parabolaív alakú híd fesztávolsága $20$ m, a legmagasabb pontja $5$ m magasan van. Helyezd a "
  r"koordináta-rendszert úgy, hogy a híd csúcsa az origóba kerüljön!",
  [r"Írd fel az ív egyenletét!", r"Milyen magasan van az ív a híd közepétől vízszintesen $4$ m-re?"],
  [r"$x^2=-20y$", r"$y=-0{,}8$, tehát $5-0{,}8=4{,}2$ m magasan"]),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Írd fel az $y^2=3x$ parabola azon érintőjét, amely párhuzamos az $x-4y+8=0$ egyenessel!",
  [r"Mekkora az érintő iránytényezője? Helyettesítsd az $y=kx+n$ egyenest a parabola egyenletébe!",
   r"Határozd meg $n$-et!", r"Írd fel az érintőt, és add meg az érintési pontot!"],
  [r"$k=\tfrac14$; $x^2+(8n-48)x+16n^2=0$", r"$D=0$: $n=3$", r"$x-4y+12=0$, érintési pont $(12;6)$"]),

 (r"Írd fel az $y^2=12x$ parabola azon érintőjét, amely párhuzamos az $x-y+5=0$ egyenessel!",
  [r"Helyettesítsd az $y=x+n$ egyenest a parabola egyenletébe!", r"Határozd meg $n$-et és az érintési pontot!"],
  [r"$x^2+(2n-12)x+n^2=0$", r"$n=3$: az érintő $y=x+3$, érintési pont $(3;6)$"]),

 (r"Írd fel az $y^2=8x$ parabola azon érintőjét, amely merőleges az $x+2y-5=0$ egyenesre!",
  [r"Mekkora az érintő iránytényezője? Helyettesítsd be az $y=kx+n$ egyenest!",
   r"Határozd meg $n$-et és az érintési pontot!"],
  [r"$k=2$; $4x^2+(4n-8)x+n^2=0$", r"$n=1$: az érintő $y=2x+1$, érintési pont $\left(\tfrac12;2\right)$"]),

 (r"Melyik $y^2=2px$ ($p\gt0$) parabolát érinti a $3x+2y+3=0$ egyenes?",
  [r"Fejezd ki $y$-t, és helyettesítsd be a parabola egyenletébe!",
   r"Milyen $p$ esetén van pontosan egy közös pont?", r"Írd fel a parabola egyenletét és az érintési pontot!"],
  [r"$\tfrac94x^2+\left(\tfrac92-2p\right)x+\tfrac94=0$", r"$D=0$: $p=0$ vagy $p=\tfrac92$; a feltétel miatt "
   r"$p=\tfrac92$", r"$y^2=9x$, érintési pont $(1;-3)$"]),
]

JOKER = (r"Az $y^2=4x$ és az $x^2=4y$ parabola két pontban metszi egymást.",
         [r"$F_1(1;0)$ és $F_2(0;1)$ — a két parabola egymás tükörképe az $y=x$ egyenesre",
          r"$(0;0)$ és $(4;4)$", r"$4\sqrt2\approx5{,}66$"],
         [r"Add meg a két parabola fókuszpontját! Mit veszel észre?", r"Határozd meg a metszéspontokat!",
          r"Milyen messze van egymástól a két metszéspont?"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (10, 8, 4), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="05-analitikus-geometria", fajl="feladatok-parabola.html",
           cim="A parabola", temakor="Síkbeli analitikus geometria",
           alcim="A parabola egyenlete, fókuszpontja és vezéregyenese, közös pontja egyenessel, húr és érintő. "
                 "Számológép használható: a szögeket egy, minden más közelítő értéket két tizedesre kerekíts. "
                 "A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-parabola-es-egyenes.html", prevc="A parabola és az egyenes",
           nxt="osszefoglalo.html", nxtc="Összefoglaló")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
