# -*- coding: utf-8 -*-
"""3e/04 — A blokk feladatgyujtemeny: vektorok a sikban es a terben (koordinatak).
Horgony-terv: narrativa_04-vektorok.md · feladat-terkep: terkep_fgy_04-vektorok.md.
Forras-szamok: 4_Vektorok/4.0 Feladatok_Vektorok.pdf, 16. Vektorok_feladatok_ellenorzore.pdf."""
import sys, os, math
from itertools import permutations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from abra_common import svg_vektorok_sik, TINTA, HALVANY

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Matrix, sqrt, cos, pi, Rational as Q, symbols, solve, simplify, N, atan
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


# hatszög O origóval: OA=u, OB=v, OC=v-u, OD=-u, OE=-v, OF=u-v
u, v = V(1, 0), V(Q(1, 2), sqrt(3)/2)
H = dict(A=u, B=v, C=v - u, D=-u, E=-v, F=u - v, O=V(0, 0))
vek = lambda p, q: H[q] - H[p]
BC = vek("B", "C")
chk("a1-egyenlo", [vek("A", "O"), vek("O", "D"), vek("F", "E")], [BC] * 3)
chk("a1-ellentett", [vek("C", "B"), vek("O", "A"), vek("D", "O"), vek("E", "F")], [-BC] * 4)
chk("a1-parh", [vek("A", "D"), vek("D", "A")], [2 * BC, -2 * BC])
# paralelogramma ABCD: A=0, B=a, D=b, C=a+b
a2, b2 = V(3, 1), V(1, 2)
A_, B_, D_, C_ = V(0, 0), a2, b2, a2 + b2
chk("a2", [C_ - A_, D_ - B_, A_ - C_, B_ - D_], [a2 + b2, b2 - a2, -a2 - b2, a2 - b2])
M_ = (B_ + C_) / 2
chk("a3", [M_ - A_, M_ - D_], [a2 + b2 / 2, a2 - b2 / 2])
chk("a4", [2*(a2 - 3*b2) + 3*(b2 + a2), 4*(a2 + b2) - 2*(2*a2 - b2), Q(1, 2)*(4*a2 - 2*b2) - (a2 - b2)],
    [5*a2 - 3*b2, 6*b2, a2])
chk("a5", [3 + 4, 4 - 3, sqrt(9 + 16)], [7, 1, 5])
chk("a7", [8*cos(pi/3), 8*cos(5*pi/6), 8*cos(pi/2)], [4, -4*sqrt(3), 0])
chk("a7-kerek", 8*cos(5*pi/6), -6.93, 0.005); chk("a7-72", 8*cos(72*pi/180), 2.47, 0.005)
chk("a11", [V(3, -1, 5) - V(1, 0, -2), V(1, 0, -2) - V(3, -1, 5)], [V(2, -1, 7), V(-2, 1, -7)])
a, b, c, d = V(-3, 2, 4), V(-2, 1, -2), V(3, -4, 5), V(8, -5, 7)
chk("a12", [2*a - 4*c + 6*d, c + 3*b - 7*a], [V(30, -10, 30), V(18, -15, -29)])
p, q = V(4, -3, 1), V(5, -2, -3)
chk("a13", [p.norm(), (p + q).norm(), (p - q).norm()], [sqrt(26), sqrt(110), 3*sqrt(2)])
chk("a13-k0", sqrt(26), 5.10, 0.005); chk("a13-k1", (p + q).norm(), 10.49, 0.005); chk("a13-k2", (p - q).norm(), 4.24, 0.005)
chk("a14", [(V(3, -1, 5) - V(1, 0, -2)).norm(), (V(-4, 1, 4) - V(2, 3, 1)).norm()], [3*sqrt(6), 7])
chk("a14-k", 3*sqrt(6), 7.35, 0.005)
chk("a15", V(1, -2, 3) + V(6, 4, 4) - V(3, 2, 1), V(4, 0, 6))
chk("a16", (V(-7, 2, 8) + V(6, 4, 5)) / 2, V(Q(-1, 2), 3, Q(13, 2)))
chk("a17", [V(-3, 6, -12), V(Q(1, 2), -1, 2)], [-3 * V(1, -2, 4), Q(1, 2) * V(1, -2, 4)])
assert not (Q(2, 1) == Q(-4, -2) == Q(6, 4)), "a17: (2;-4;6) nem parhuzamos"
e = V(6, -2, 3)
chk("a18", [e.norm(), e / e.norm()], [7, V(Q(6, 7), Q(-2, 7), Q(3, 7))])
# közép
chk("k1", [H["D"], H["E"], H["F"], vek("C", "E"), vek("D", "F")], [-u, -v, u - v, u - 2*v, 2*u - v])
CA, CB = V(2, 5), V(6, 1)
chk("k2", [(CA + CB) / 2, CB - CA, Q(2, 3) * (CA + CB) / 2], [(CA + CB) / 2, CB - CA, (CA + CB) / 3])
chk("k3", [sqrt(25 + 9), sqrt(100 + 9)], [sqrt(34), sqrt(109)])
chk("k3-k1", sqrt(34), 5.83, 0.005); chk("k3-k2", sqrt(109), 10.44, 0.005); chk("k3-k3", sqrt(61), 7.81, 0.005)
chk("k4", sqrt(12**2 + 5**2), 13); chk("k4-szog", atan(Q(5, 12)) * 180 / pi, 22.6, 0.05)
t = symbols("t")
chk("k6", sorted(solve(1 + 4 + t**2 - (5*t**2 + 4), t)), [Q(-1, 2), Q(1, 2)])
S = V(Q(1, 2), 1, -1)
chk("k7", [2*S - V(1, 0, -2), 2*S - V(3, -1, 5)], [V(0, 2, 0), V(-2, 3, -7)])
chk("k8", [2*V(1, 4, 1) - V(5, -2, 3), 2*V(7, 1, 4) - V(5, -2, 3)], [V(-3, 10, -1), V(9, 4, 5)])
chk("k9", 2*V(6, 4, 5) - V(-7, 2, 8), V(19, 6, 2))
chk("k10", V(2, -1, 4) + (V(2, 2, 10) - V(2, -1, 4)) / 3, V(2, 0, 6))
A, B, C = V(1, 0, -1), V(1, -1, 3), V(-7, 2, 1)
chk("k11", [(B - A).norm(), (C - B).norm(), (C - A).norm()], [sqrt(17), sqrt(77), 6*sqrt(2)])
chk("k11-k", (B - A).norm() + (C - B).norm() + (C - A).norm(), 21.38, 0.005)
A, B, C = V(3, 1, 2), V(5, 3, 3), V(4, -1, 4)
chk("k12", [(B - A).norm(), (C - A).norm(), (C - B).norm()**2], [3, 3, 18])
assert 77 < 17 + 72
# nehéz
K, Ah, Bh = V(2, -3, 5), V(1, -3, 6), V(1, -2, 5)
ka, kb = Ah - K, Bh - K
chk("n1-szabalyos", [ka.norm(), kb.norm(), ka.dot(kb)], [sqrt(2), sqrt(2), 1])
chk("n1", [K + kb - ka, K - ka, K - kb, K + ka - kb], [V(2, -2, 4), V(3, -3, 4), V(3, -4, 5), V(2, -4, 6)])
A, B, C = V(1, 2, 0), V(4, 3, 1), V(2, -1, 3)
chk("n3", [B + C - A, A + C - B, A + B - C], [V(5, 0, 4), V(-1, -2, 2), V(3, 6, -2)])
chk("n4", sorted(solve((3 - 1)**2 + (t - 2)**2 + (-1 - 3)**2 - (V(5, 0, 1) - V(1, 2, 3)).norm()**2, t)), [0, 4])
chk("n4-szab", [(V(5, 0, 1) - V(3, 4, -1)).norm(), (V(3, 4, -1) - V(1, 2, 3)).norm(), (V(5, 0, 1) - V(3, 0, -1)).norm()], [2*sqrt(6), 2*sqrt(6), 2*sqrt(2)])
# joker
UG = set()
for perm in set(permutations((2, 1, 0))):
    for s1 in (1, -1):
        for s2 in (1, -1):
            m = list(perm)
            nz = [i for i, x in enumerate(m) if x]
            m[nz[0]] *= s1
            m[nz[1]] *= s2
            UG.add(tuple(m))
chk("jok-db", len(UG), 24)
assert {sum(x*x for x in m) for m in UG} == {5}
assert (1, 1, 1) not in UG
assert all(sum(m) % 2 == 1 for m in UG)
assert tuple(map(sum, zip((0, -2, -1), (0, 1, 2), (1, 2, 0)))) == (1, 1, 1)
assert all(x in UG for x in ((0, -2, -1), (0, 1, 2), (1, 2, 0)))
assert not E, E
print("sympy önteszt: OK")

# ============================== ÁBRA ==============================
_H = [(2 * math.cos(k * math.pi / 3), 2 * math.sin(k * math.pi / 3)) for k in range(6)]
SVG_HATSZOG = svg_vektorok_sik(
    [], szakaszok=[(_H[i], _H[(i + 1) % 6], TINTA, None) for i in range(6)]
                  + [((0, 0), _H[i], HALVANY, "4 3") for i in range(6)],
    pontok=list(zip(_H + [(0, 0)], "ABCDEFO", [14, 10, -10, -14, -10, 10, 0],
                    [5, -7, -7, 5, 19, 19, -9])),
    xr=(-2.5, 2.5), yr=(-2.15, 2.15), egyseg=48, racs=False,
    leiras="Szabályos ABCDEF hatszög, középpontja O")


def abra(svg):
    return f'<div class="svgwrap">{svg}</div>'


def vv(s):
    return "$" + s + "$"


# ============================== ALAPSZINT ==============================
ALAP = [
 # --- A1: vektorok a síkban (alap 1–8)
 (r"Az $ABCDEF$ szabályos hatszög középpontja $O$. Tekintsük azokat a vektorokat, amelyeknek "
  r"kezdő- és végpontja is az $A$, $B$, $C$, $D$, $E$, $F$, $O$ pontok valamelyike. Ezek közül "
  r"keresd meg" + abra(SVG_HATSZOG),
  [r"az összes olyat, amelyik <b>egyenlő</b> a $\overrightarrow{BC}$ vektorral;",
   r"a $\overrightarrow{BC}$ összes <b>ellentett</b> vektorát;",
   r"azokat, amelyek <b>párhuzamosak</b> a $\overrightarrow{BC}$-vel, de <b>nem egyenlő hosszúak</b> vele!"],
  [r"$\overrightarrow{AO}$, $\overrightarrow{OD}$, $\overrightarrow{FE}$ (mindhárom párhuzamos, "
   r"egyenlő hosszú és azonos irányítású)",
   r"$\overrightarrow{CB}$, $\overrightarrow{OA}$, $\overrightarrow{DO}$, $\overrightarrow{EF}$",
   r"$\overrightarrow{AD}$ és $\overrightarrow{DA}$ (kétszer olyan hosszúak; "
   r"$\overrightarrow{AD}=2\overrightarrow{BC}$)"]),

 (r"Az $ABCD$ paralelogrammában $\overrightarrow{AB}=\vec a$ és $\overrightarrow{AD}=\vec b$. "
  r"Fejezd ki $\vec a$ és $\vec b$ segítségével a következő vektorokat!",
  [r"$\overrightarrow{AC}$", r"$\overrightarrow{BD}$", r"$\overrightarrow{CA}$", r"$\overrightarrow{DB}$"],
  [r"$\vec a+\vec b$", r"$\vec b-\vec a$", r"$-\vec a-\vec b$", r"$\vec a-\vec b$"], True),

 (r"Az $ABCD$ paralelogrammában $\overrightarrow{AB}=\vec a$, $\overrightarrow{AD}=\vec b$, és "
  r"$M$ a $BC$ oldal felezőpontja. Fejezd ki $\vec a$ és $\vec b$ segítségével!",
  [r"$\overrightarrow{AM}$", r"$\overrightarrow{DM}$"],
  [r"$\overrightarrow{AM}=\overrightarrow{AB}+\overrightarrow{BM}=\vec a+\tfrac12\vec b$",
   r"$\overrightarrow{DM}=\overrightarrow{DC}+\overrightarrow{CM}=\vec a-\tfrac12\vec b$"], True),

 (r"Egyszerűsítsd a kifejezéseket!",
  [r"$2(\vec a-3\vec b)+3(\vec b+\vec a)$", r"$4(\vec a+\vec b)-2(2\vec a-\vec b)$",
   r"$\tfrac12(4\vec a-2\vec b)-(\vec a-\vec b)$"],
  [r"$5\vec a-3\vec b$", r"$6\vec b$", r"$\vec a$"], True),

 (r"Az $\vec a$ intenzitása $3$, a $\vec b$ intenzitása $4$. Mekkora $|\vec a+\vec b|$, ha a két "
  r"vektor szöge",
  [r"$0^\circ$;", r"$180^\circ$;", r"$90^\circ$?"],
  [r"$7$ (azonos irányításúak: a hosszak összeadódnak)",
   r"$1$ (ellentétes irányításúak: a hosszak kivonódnak)",
   r"$5$ (az összeg egy $3\times4$-es téglalap átlója: $\sqrt{9+16}=5$)"], True),

 (r"Az $ABC$ szabályos háromszögben mekkora a következő vektorpárok szöge? Vigyázz: két "
  r"vektor szögét közös kezdőpontba tolva mérjük!",
  [r"$\overrightarrow{AB}$ és $\overrightarrow{AC}$", r"$\overrightarrow{AB}$ és $\overrightarrow{BC}$",
   r"$\overrightarrow{AB}$ és $\overrightarrow{CA}$", r"$\overrightarrow{AB}$ és $\overrightarrow{BA}$"],
  [r"$60^\circ$", r"$120^\circ$ (a szög a $B$ csúcsnál lévő külső szöggel egyenlő: $180^\circ-60^\circ$)",
   r"$120^\circ$ ($\overrightarrow{CA}=-\overrightarrow{AC}$, ezért $180^\circ-60^\circ$)",
   r"$180^\circ$ (ellentett vektorok)"], True),

 (r"A $\vec b$ vektor intenzitása $8$. Számítsd ki a $\vec b$ skaláris vetületét egy $\vec a$ "
  r"vektorra, ha a két vektor szöge",
  [r"$60^\circ$;", r"$150^\circ$;", r"$90^\circ$;", r"$72^\circ$ (számológéppel, két tizedesre)!"],
  [r"$8\cos60^\circ=4$", r"$8\cos150^\circ=-4\sqrt3\approx-6{,}93$", r"$0$",
   r"$8\cos72^\circ\approx2{,}47$"], True),

 (r"Döntsd el, igaz-e az állítás, és indokold!",
  [r"Ha két nem nullvektor párhuzamos, akkor az egyik a másik számszorosa.",
   r"$|-2\vec a|=-2|\vec a|$ bármely $\vec a$ vektorra.",
   r"Bármely két vektorra $|\vec a+\vec b|\le|\vec a|+|\vec b|$.",
   r"Két ellentett vektor összege a nullvektor."],
  [r"igaz: ha $\vec b\parallel\vec a$, akkor $\vec b=\lambda\vec a$, ahol $|\lambda|=\frac{|\vec b|}{|\vec a|}$, "
   r"és $\lambda$ azonos irányításnál pozitív, ellentétesnél negatív",
   r"hamis: ha $\vec a\ne\vec 0$, a jobb oldal negatív, az intenzitás pedig nem lehet az; "
   r"helyesen $|-2\vec a|=2|\vec a|$",
   r"igaz: ez a háromszög-egyenlőtlenség (egyenlőség csak azonos irányításnál, vagy ha "
   r"valamelyik vektor nullvektor)",
   r"igaz: $\vec a+(-\vec a)=\vec 0$"]),

 # --- A2: koordináták (alap 9–18)
 (r"Hol helyezkedik el a pont? Add meg a legszűkebb helyet: a koordinátatengelyt, ha "
  r"tengelyen van, különben a koordinátasíkot!",
  [r"$A(0;3;0)$", r"$B(2;0;-1)$", r"$C(0;0;5)$", r"$D(4;-2;0)$"],
  [r"az $y$ tengelyen", r"az $xz$ síkban", r"a $z$ tengelyen", r"az $xy$ síkban"], True),

 (r"Írd fel a vektort a másik alakban!",
  [r"$2\vec i-3\vec j+\vec k$", r"$4\vec j-\vec k$", r"$(-1;0;5)$", r"$(0;0;-3)$"],
  [r"$(2;-3;1)$", r"$(0;4;-1)$", r"$-\vec i+5\vec k$", r"$-3\vec k$"], True),

 (r"Adott az $A(1;0;-2)$ és a $B(3;-1;5)$ pont. Add meg a vektorok koordinátáit!",
  [r"$\overrightarrow{AB}$", r"$\overrightarrow{BA}$"],
  [r"$(2;-1;7)$", r"$(-2;1;-7)$"], True),

 (r"Legyen $\vec a=(-3;2;4)$, $\vec b=(-2;1;-2)$, $\vec c=(3;-4;5)$ és $\vec d=(8;-5;7)$. "
  r"Számítsd ki!",
  [r"$2\vec a-4\vec c+6\vec d$", r"$\vec c+3\vec b-7\vec a$"],
  [r"$(30;-10;30)$", r"$(18;-15;-29)$"], True),

 (r"Adottak az $\vec a=(4;-3;1)$ és a $\vec b=(5;-2;-3)$ vektorok. Számítsd ki!",
  [r"$|\vec a|$", r"$|\vec a+\vec b|$", r"$|\vec a-\vec b|$"],
  [r"$\sqrt{16+9+1}=\sqrt{26}\approx5{,}10$",
   r"$\vec a+\vec b=(9;-5;-2)$, intenzitása $\sqrt{110}\approx10{,}49$",
   r"$\vec a-\vec b=(-1;-1;4)$, intenzitása $\sqrt{18}=3\sqrt2\approx4{,}24$"]),

 (r"Mekkora a két pont távolsága?",
  [r"$A(1;0;-2)$ és $B(3;-1;5)$", r"$P(2;3;1)$ és $Q(-4;1;4)$"],
  [r"$\overrightarrow{AB}=(2;-1;7)$, $|\overrightarrow{AB}|=\sqrt{54}=3\sqrt6\approx7{,}35$",
   r"$\overrightarrow{PQ}=(-6;-2;3)$, $|\overrightarrow{PQ}|=\sqrt{49}=7$"]),

 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(1;-2;3)$, $B(3;2;1)$ és "
  r"$C(6;4;4)$. Határozd meg a $D$ csúcs koordinátáit!", None,
  r"$\overrightarrow{AD}=\overrightarrow{BC}$, ezért (koordinátánként, a helyvektorokkal számolva) "
  r"$D=A+C-B$: $D(4;0;6)$."),

 (r"Határozd meg az $A(-7;2;8)$ és a $B(6;4;5)$ pont által meghatározott szakasz "
  r"felezőpontjának koordinátáit!", None,
  r"$F=\tfrac12(A+B)$: $F(-0{,}5;\ 3;\ 6{,}5)$."),

 (r"Melyik vektor párhuzamos az $\vec a=(1;-2;4)$ vektorral? Ha párhuzamos, add meg azt a "
  r"$\lambda$ számot is, amelyre az adott vektor $\lambda\vec a$!",
  [r"$\vec b=(-3;6;-12)$", r"$\vec c=(2;-4;6)$", r"$\vec d=\left(\tfrac12;-1;2\right)$"],
  [r"párhuzamos, $\lambda=-3$", r"nem párhuzamos (az arányok $2$, $2$, de $\tfrac64\ne2$)",
   r"párhuzamos, $\lambda=\tfrac12$"]),

 (r"Adott az $\vec a=(6;-2;3)$ vektor. Határozd meg",
  [r"az $\vec a$ intenzitását;", r"az $\vec a$-val azonos irányítású egységvektort;",
   r"az $\vec a$-val ellentétes irányítású egységvektort!"],
  [r"$|\vec a|=\sqrt{36+4+9}=7$", r"$\vec a_0=\left(\frac{6}{7};-\frac{2}{7};\frac{3}{7}\right)$",
   r"$-\vec a_0=\left(-\frac{6}{7};\frac{2}{7};-\frac{3}{7}\right)$"]),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- A1 (közép 1–5)
 (r"Az $ABCDEF$ szabályos hatszög középpontja $O$, és $\overrightarrow{OA}=\vec a$, "
  r"$\overrightarrow{OB}=\vec b$. Fejezd ki $\vec a$ és $\vec b$ segítségével!" + abra(SVG_HATSZOG),
  [r"$\overrightarrow{OD}$", r"$\overrightarrow{OE}$", r"$\overrightarrow{OF}$",
   r"$\overrightarrow{CE}$", r"$\overrightarrow{DF}$"],
  [r"$-\vec a$", r"$-\vec b$", r"$\vec a-\vec b$ (mert $\overrightarrow{OF}=\overrightarrow{BA}$)",
   r"$\overrightarrow{OE}-\overrightarrow{OC}=-\vec b-(\vec b-\vec a)=\vec a-2\vec b$",
   r"$\overrightarrow{OF}-\overrightarrow{OD}=(\vec a-\vec b)+\vec a=2\vec a-\vec b$"]),

 (r"Az $ABC$ háromszögben $\overrightarrow{CA}=\vec a$ és $\overrightarrow{CB}=\vec b$. Az $F$ pont az "
  r"$AB$ oldal felezőpontja, $S$ a háromszög súlypontja. Fejezd ki $\vec a$ és $\vec b$ "
  r"segítségével! <i>(A súlypont a súlyvonalat a csúcstól számítva $2:1$ arányban osztja.)</i>",
  [r"$\overrightarrow{AB}$", r"$\overrightarrow{CF}$", r"$\overrightarrow{CS}$"],
  [r"$\vec b-\vec a$", r"$\overrightarrow{CA}+\tfrac12\overrightarrow{AB}=\tfrac12(\vec a+\vec b)$",
   r"$\tfrac23\overrightarrow{CF}=\tfrac13(\vec a+\vec b)$"], True),

 (r"Az $\vec a$ és a $\vec b$ merőleges egymásra, $|\vec a|=5$ és $|\vec b|=3$. Számítsd ki!",
  [r"$|\vec a-\vec b|$", r"$|2\vec a+\vec b|$", r"$|\vec a-2\vec b|$"],
  [r"$\sqrt{25+9}=\sqrt{34}\approx5{,}83$ (téglalap átlója)",
   r"$2\vec a$ intenzitása $10$, és ez is merőleges $\vec b$-re: $\sqrt{100+9}=\sqrt{109}\approx10{,}44$",
   r"$-2\vec b$ intenzitása $6$, és merőleges $\vec a$-ra: $\sqrt{25+36}=\sqrt{61}\approx7{,}81$"]),

 (r"Egy motorcsónak a vízhez képest $12$ km/h sebességgel halad kelet felé, a folyó pedig "
  r"$5$ km/h sebességgel sodorja dél felé. Mekkora a csónak parthoz viszonyított sebessége, "
  r"és hány fokkal tér el a keleti iránytól?", None,
  r"A két sebességvektor merőleges, az eredő intenzitása $\sqrt{12^2+5^2}=13$ km/h. Az eltérés "
  r"szögére $\operatorname{tg}\alpha=\frac{5}{12}$, így $\alpha\approx22{,}6^\circ$ (kelettől dél felé)."),

 (r"Maxi szerint az $ABC$ szabályos háromszögben, ahol az oldal hossza $a$, az "
  r"$\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}$ vektor intenzitása $3a$, "
  r"„hiszen három $a$ hosszú vektort adtunk össze”. Mit rontott el? Mennyi a helyes válasz?", None,
  r"A vektorok összegének intenzitása nem a hosszak összege. A háromszög-szabállyal "
  r"$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$, és "
  r"$\overrightarrow{AC}+\overrightarrow{CA}=\vec 0$: az összeg a nullvektor, intenzitása $0$."),

 # --- A2 (közép 6–12)
 (r"Határozd meg a $t$ valós számot úgy, hogy az $\vec a=(1;2;t)$ és a "
  r"$\vec b=\left(t\sqrt5;0;2\right)$ vektor intenzitása egyenlő legyen!", None,
  r"$1+4+t^2=5t^2+4$, azaz $4t^2=1$, tehát $t=\frac12$ vagy $t=-\frac12$."),

 (r"Adott az $A(1;0;-2)$ és a $B(3;-1;5)$ pont, valamint az $S\left(\tfrac12;1;-1\right)$ pont. "
  r"Határozd meg a $C$ és a $D$ pont koordinátáit úgy, hogy az $ABCD$ négyszög olyan "
  r"paralelogramma legyen, amelynek középpontja $S$!", None,
  r"A paralelogramma átlói felezik egymást: $S$ az $AC$ és a $BD$ felezőpontja. Koordinátánként "
  r"(helyvektorokkal) számolva "
  r"$C=2S-A$: $C(0;2;0)$, $D=2S-B$: $D(-2;3;-7)$."),

 (r"Az $ABC$ háromszög egyik csúcsa $A(5;-2;3)$. Az $AB$ oldal felezőpontja $F(1;4;1)$, az $AC$ "
  r"oldal felezőpontja $G(7;1;4)$. Határozd meg a másik két csúcs koordinátáit!", None,
  r"$B=2F-A$: $B(-3;10;-1)$, és $C=2G-A$: $C(9;4;5)$."),

 (r"Határozd meg az $A(-7;2;8)$ pont $B(6;4;5)$ pontra vonatkozó tükörképének koordinátáit!", None,
  r"A tükörkép $A'$, és $B$ az $AA'$ szakasz felezőpontja: $A'=2B-A$, azaz $A'(19;6;2)$."),

 (r"Határozd meg az $A(2;-1;4)$ és a $B(2;2;10)$ pont által meghatározott szakasz $A$-hoz "
  r"közelebbi harmadolópontját!", None,
  r"$H=A+\tfrac13\overrightarrow{AB}=(2;-1;4)+\tfrac13(0;3;6)$, tehát $H(2;0;6)$."),

 (r"Adott az $A(1;0;-1)$, $B(1;-1;3)$, $C(-7;2;1)$ csúcsú háromszög.",
  [r"Számítsd ki a kerületét!", r"Hegyesszögű, derékszögű vagy tompaszögű a háromszög? Indokold!"],
  [r"$AB=\sqrt{17}$, $BC=\sqrt{77}$, $AC=\sqrt{72}=6\sqrt2$; a kerület "
   r"$\sqrt{17}+\sqrt{77}+6\sqrt2\approx21{,}38$",
   r"hegyesszögű: a leghosszabb oldal négyzete $77$, és $77\lt 17+72=89$, így a vele szemközti szög is "
   r"hegyesszög"]),

 (r"Az $A(3;1;2)$, $B(5;3;3)$, $C(4;-1;4)$ pontok egy háromszög csúcsai. Döntsd el és indokold!",
  [r"Egyenlő szárú-e a háromszög?", r"Derékszögű-e a háromszög?"],
  [r"igen: $AB=\sqrt{4+4+1}=3$ és $AC=\sqrt{1+4+4}=3$",
   r"igen: $BC^2=1+16+1=18=AB^2+AC^2$, így Pitagorasz tételének megfordítása szerint az "
   r"$A$-nál derékszög van"]),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Az $ABCDEF$ szabályos hatszög középpontja $K(2;-3;5)$, két szomszédos csúcsa $A(1;-3;6)$ és "
  r"$B(1;-2;5)$. Határozd meg a hatszög másik négy csúcsának koordinátáit!", None,
  r"$\overrightarrow{KA}=(-1;0;1)$, $\overrightarrow{KB}=(-1;1;0)$. A szabályos hatszögben "
  r"$\overrightarrow{KC}=\overrightarrow{KB}-\overrightarrow{KA}$, $\overrightarrow{KD}=-\overrightarrow{KA}$, "
  r"$\overrightarrow{KE}=-\overrightarrow{KB}$, $\overrightarrow{KF}=\overrightarrow{KA}-\overrightarrow{KB}$. "
  r"Így $C(2;-2;4)$, $D(3;-3;4)$, $E(3;-4;5)$, $F(2;-4;6)$."),

 (r"Bizonyítsd be vektorokkal, hogy a háromszög két oldalának felezőpontját összekötő "
  r"szakasz (középvonal) párhuzamos a harmadik oldallal, és hossza annak fele!", None,
  r"Legyen $F$ a $CA$, $G$ a $CB$ oldal felezőpontja. Ekkor $\overrightarrow{CF}=\tfrac12\overrightarrow{CA}$ "
  r"és $\overrightarrow{CG}=\tfrac12\overrightarrow{CB}$, így "
  r"$\overrightarrow{FG}=\overrightarrow{CG}-\overrightarrow{CF}=\tfrac12\left(\overrightarrow{CB}-"
  r"\overrightarrow{CA}\right)=\tfrac12\overrightarrow{AB}$. Egy vektor fele párhuzamos vele, és "
  r"intenzitása fele akkora — ez az állítás."),

 (r"Az $A(1;2;0)$, $B(4;3;1)$ és $C(2;-1;3)$ pont egy paralelogramma három csúcsa, de nem "
  r"tudjuk, milyen sorrendben. Határozd meg a negyedik csúcs összes lehetséges helyzetét!", None,
  r"$\overrightarrow{AB}=(3;1;1)$ és $\overrightarrow{AC}=(1;-3;3)$ nem párhuzamosak, tehát a pontok nem "
  r"esnek egy egyenesre. Mindhárom pont lehet a negyedik csúccsal szemközti csúcs. $D_1=B+C-A=(5;0;4)$ (az $A$-val "
  r"szemközti), $D_2=A+C-B=(-1;-2;2)$ (a $B$-vel szemközti), $D_3=A+B-C=(3;6;-2)$ (a $C$-vel "
  r"szemközti) — három paralelogramma van."),

 (r"Adott az $A(1;2;3)$, a $B(3;t;-1)$ és a $C(5;0;1)$ pont. Határozd meg a $t$ értékét úgy, hogy "
  r"$AB=AC$ legyen! Melyik esetben lesz az $ABC$ háromszög szabályos?", None,
  r"$AC^2=16+4+4=24$ és $AB^2=4+(t-2)^2+16$, így $(t-2)^2=4$: $t=4$ vagy $t=0$. "
  r"$t=4$ esetén $B(3;4;-1)$ és $BC^2=4+16+4=24$: a háromszög <b>szabályos</b> (oldala $2\sqrt6$). "
  r"$t=0$ esetén $BC^2=4+0+4=8$: csak egyenlő szárú."),
]

JOKER = (r"Tér-eb egy háromdimenziós sakktáblán ugrál, a sakkbeli lóhoz hasonlóan: egy ugrással "
         r"az egyik koordinátája $2$-vel, egy másik $1$-gyel változik (növekszik vagy csökken), a "
         r"harmadik változatlan. Egy ugrás tehát egy vektor, például $(2;-1;0)$ vagy $(0;1;-2)$.",
         [r"$24$ ugrásvektor van: $3$-féleképpen választható a $2$-vel változó koordináta, $2$-féleképpen "
          r"az $1$-gyel változó, és mindkettő előjele $2$-féle ($3\cdot2\cdot2\cdot2=24$)",
          r"mindegyik intenzitása $\sqrt{4+1+0}=\sqrt5$",
          r"$3$ ugrás. Egy ugrás a koordináták összegét páratlan számmal ($\pm1$ vagy $\pm3$) változtatja, "
          r"az $(1;1;1)$-ben pedig az összeg $3$, páratlan: páros számú ugrással nem érhető el, egyetlen "
          r"ugrással sem, mert $(1;1;1)$ nem ugrásvektor. Három elég: $(0;-2;-1)+(0;1;2)+(1;2;0)=(1;1;1)$"],
         [r"Hány különböző ugrásvektor van?", r"Mekkora az intenzitásuk?",
          r"Legalább hány ugrással jut el az origóból az $(1;1;1)$ pontba? Indokold!"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (18, 12, 4), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="04-vektorok", fajl="feladatok-vektorok.html",
           cim="Vektorok", temakor="Vektorok",
           alcim="Vektorok a síkban és a térben: műveletek, szög és vetület, koordináták, "
                 "intenzitás és távolság. A végeredmény minden feladatnál lenyitható — előbb "
                 "számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-koordinatak-terben.html", prevc="Vektorok a térben",
           nxt="feladatok-szorzatok.html", nxtc="A két szorzat — feladatok")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
