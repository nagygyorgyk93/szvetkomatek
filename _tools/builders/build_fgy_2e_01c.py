# -*- coding: utf-8 -*-
"""2e/01 — „C" altéma feladatgyűjtemény: komplex számok.
+ gyakorló DOLGOZAT (a TELJES témakörre: hatvány + gyök + komplex)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (symbols, I, Rational as R, simplify, expand, sqrt, root, Integer,
                   Abs, re as Re, im as Im, conjugate, solve, Eq)
a, x, y = symbols('a x y', positive=True)
xr, yr = symbols('xr yr', real=True)
n = symbols('n', integer=True, nonnegative=True)
E = []
def ell(nev, kif, vart):
    if simplify(kif - vart) != 0:
        E.append((nev, simplify(kif), vart))

P = [  # (név, kifejezés, várt)
 ("A3a", Abs(3+4*I), 5), ("A3b", Abs(5-12*I), 13), ("A3c", Abs(8+6*I), 10),
 ("A3f", Abs(1+I), sqrt(2)),
 ("A7a", expand((3+2*I)+(5-7*I)), 8-5*I), ("A7b", expand((-4+I)+(6+3*I)), 2+4*I),
 ("A7c", expand((7-2*I)-(3+5*I)), 4-7*I), ("A7d", expand((1-I)-(-2-4*I)), 3+3*I),
 ("A8a", expand((2+3*I)*(1+4*I)), -10+11*I), ("A8b", expand((3-I)*(2+5*I)), 11+13*I),
 ("A8c", expand((1+I)*(1-I)), 2), ("A8d", expand((2-3*I)**2), -5-12*I),
 ("A9a", expand(I*(3+2*I)), -2+3*I), ("A9b", expand((2*I)**2), -4),
 ("A9c", expand((3*I)*(4*I)), -12), ("A9d", expand(-I*(5-I)), -1-5*I),
 ("A10a", simplify(1/I), -I), ("A10b", simplify(2/(1+I)), 1-I),
 ("A10c", simplify(5/(2-I)), 2+I), ("A10d", simplify((1+I)/(1-I)), I),
 ("A11a", expand((2-5*I)+conjugate(2-5*I)), 4),
 ("A11b", expand((2-5*I)-conjugate(2-5*I)), -10*I),
 ("A11c", expand((2-5*I)*conjugate(2-5*I)), 29), ("A11d", Abs(2-5*I)**2, 29),
 ("A12a", expand((1+2*I)+(1-2*I)), 2), ("A12b", expand((3+I)*(3-I)), 10),
 ("A12c", simplify(4/(2*I)), -2*I), ("A12d", expand((1-I)**2), -2*I),
 ("A13b", expand(I**7), -I), ("A13c", expand(I**10), -1), ("A13d", expand(I**13), I),
 ("A13f", expand(I**31), -I), ("A14a", expand(I**50), -1), ("A14b", expand(I**101), I),
 ("A14c", expand(I**2024), 1), ("A14d", expand(I**2027), -I),
 ("A15a", expand(I**3+I**5), 0), ("A15b", expand(2*I**6-3*I**8), -5),
 ("A15c", expand(I**9+I**11), 0), ("A15d", expand(3*I**12+2*I**14), 1),
 ("A16a", simplify(1/I), -I), ("A16b", simplify((6-4*I)/2), 3-2*I),
 ("A16c", simplify(2/(1+I)), 1-I), ("A16d", simplify(2*I/(1-I)), -1+I),
 ("A17a", expand((5-2*I)-3*I), 5-5*I), ("A17b", simplify((3+7*I+1)/2), 2+R(7,2)*I),
 ("K1a", expand((2+3*I)+(1-5*I)), 3-2*I), ("K1a|", Abs(3-2*I), sqrt(13)),
 ("K1b", expand((4-I)-(2+3*I)), 2-4*I), ("K1b|", Abs(2-4*I), 2*sqrt(5)),
 ("K1c", expand(3*I*(2-I)), 3+6*I), ("K1c|", Abs(3+6*I), 3*sqrt(5)),
 ("K3a", Abs(3-4*I)+Abs(5+12*I), 18), ("K3b", Abs(1+I)*Abs(1-I), 2),
 ("K3c", Abs(2*I)-Abs(Integer(-3)), -1), ("K3d", Abs((3+4*I)*(1-I)), 5*sqrt(2)),
 ("K5a", expand((2+3*I)*(4-I)-(1-2*I)**2), 14+14*I),
 ("K5b", expand((5-2*I)*(2+I)+(2-3*I)**2), 7-11*I),
 ("K5c", expand((3+I)*(2+3*I)-(1-I)**2), 3+13*I),
 ("K6a", simplify((2+I)/(2-I)), R(3,5)+R(4,5)*I),
 ("K6b", simplify((3+2*I)/(1+I)), R(5,2)-R(1,2)*I),
 ("K6c", simplify((5-10*I)/(3+4*I)), -1-2*I),
 ("K7a", expand((2+3*I)+(-2-4*I)), -I),
 ("K7b", expand((2+3*I)-2*(-2-4*I)+(-1+I)), 5+12*I),
 ("K7c", expand((2+3*I)*(-2-4*I)), 8-14*I),
 ("K7d", simplify((2+3*I)/(-1+I)), R(1,2)-R(5,2)*I),
 ("K8a", expand((1+I)**2), 2*I), ("K8b", expand((1+I)**3), -2+2*I),
 ("K8c", expand((1+I)**4), -4), ("K8d", simplify(1/(1+I)), R(1,2)-R(1,2)*I),
 ("K9a", simplify((1+I)/(1-I)+(1-I)/(1+I)), 0),
 ("K9b", simplify(2/(1+I)-2/(1-I)), -2*I),
 ("K9c", simplify(((1+I)/sqrt(2))**2), I),
 ("K10a", expand(I**25+I**50+I**75+I**100), 0),
 ("K10b", expand(2*I**15-3*I**22+I**33), 3-I),
 ("K10c", expand(I**2026+I**2027), -1-I),
 ("K11a", simplify(10/(3+I)), 3-I), ("K11b", simplify(5*I/(1-2*I)), -2+I),
 ("K11c", simplify(13/(2+3*I)), 2-3*I),
 ("K13a", expand((3-I)**2), 8-6*I), ("K13b", expand((3-I)*conjugate(3-I)), 10),
 ("K13c", expand((3-I)+conjugate(3-I)), 6),
 ("K13d", simplify((3-I)/conjugate(3-I)), R(4,5)-R(3,5)*I),
 ("K14a", expand((1+I)**8), 16), ("K14b", expand((1-I)**6), 8*I),
 ("K14c", simplify((1+I)**4/(1-I)**2), -2*I),
 ("N1", simplify((1+2*I)**2/(1-I)**10), R(-1,8)-R(3,32)*I),
 ("N2", expand((1+I)**4+(1-I)**4), -8),
 ("N3", expand((1+I)**2*((1+I)**2-(1+I)+1)), -2),
 ("N4", simplify((1+I)/(1-I)+I**24+I**33+I**49), 1+3*I),
 ("N6", simplify(((1-I)/(1+I))**2027), I),
 # gyakorló
 ("GY1", R(49,4)**R(1,2)-1+R(9,2)+R(1,2), R(15,2)),
 ("GY2", Integer(125)**R(2,3)+Integer(36)**R(-1,2), R(151,6)),
 ("GY3a", 4/(5-sqrt(21)), 5+sqrt(21)), ("GY3b", 14/sqrt(7), 2*sqrt(7)),
 ("GY4", root(x**2*sqrt(x**4), 4), x),
 ("GY5", root(x**12*y**-8*symbols('z', positive=True)**16, 4),
  x**3*symbols('z', positive=True)**4/y**2),
 ("GY6", simplify((2**(n+2)+2**(n+1))/2**n), 6),
 ("GY9b", expand((3+4*I)+(1-I)), 4+3*I), ("GY9c", expand((3+4*I)*(1-I)), 7+I),
 ("GY9d", simplify((3+4*I)/(1-I)), R(-1,2)+R(7,2)*I), ("GY9e", Abs(3+4*I), 5),
 ("GY9f", expand(conjugate(1-I)-(3+4*I)), -2-3*I),
 ("GY10", expand(3*I**9-2*I**14+I**27), 2+2*I),
 ("GYH1", R(1,3)**-3-R(-1,2)**-4+R(-3)**-1, R(32,3)),
 ("GYH2a", 6/(sqrt(3)+sqrt(2)), 6*(sqrt(3)-sqrt(2))),
 ("GYH2b", 9/root(3,3), 3*root(9,3)),
 ("GYH3", root(a**4,3)*sqrt(a)/root(a,6), root(a**5,3)),
 ("GYH4", simplify(10/(1+3*I)), 1-3*I),
 ("GYH5b", Abs(2-3*I), sqrt(13)), ("GYH5c", expand((2-3*I)*conjugate(2-3*I)), 13),
 ("GYH5d", expand((2-3*I)**2), -5-12*I),
 ("GYH6", expand(I**2026-2*I**2027+3*I**2028), 2+2*I),
]
for nev, k, v in P:
    ell(nev, k, v)
# egyenletek z és konjugáltja
for nev, egy, vart in [("K12a", Eq((xr+yr*I)+2*conjugate(xr+yr*I), 9-3*I), 3+3*I),
                       ("K12b", Eq(3*(xr+yr*I)-conjugate(xr+yr*I), 4+8*I), 2+2*I),
                       ("K12c", Eq(2*(xr+yr*I)+3*conjugate(xr+yr*I), 15-I), 3+I),
                       ("N5", Eq((2+I)*(xr+yr*I)+2*conjugate(xr+yr*I)-3, 4+6*I), 6+17*I)]:
    s = solve([Eq(Re(egy.lhs-egy.rhs), 0), Eq(Im(egy.lhs-egy.rhs), 0)], [xr, yr], dict=True)[0]
    got = s[xr] + s[yr]*I
    if simplify(got - vart) != 0:
        E.append((nev, got, vart))
assert not E, E[:5]
print("sympy önteszt: OK")

# ============================== FELADATOK ==============================

ALAP = [
 ("Add meg a komplex szám valós és képzetes részét!",
  ["$z=3+5i$", "$z=-2+7i$", "$z=4-i$", "$z=6i$", "$z=-9$", "$z=\\dfrac{1}{2}-\\dfrac{3}{4}i$"],
  ["$\\operatorname{Re}=3$, $\\operatorname{Im}=5$", "$\\operatorname{Re}=-2$, $\\operatorname{Im}=7$",
   "$\\operatorname{Re}=4$, $\\operatorname{Im}=-1$", "$\\operatorname{Re}=0$, $\\operatorname{Im}=6$",
   "$\\operatorname{Re}=-9$, $\\operatorname{Im}=0$",
   "$\\operatorname{Re}=\\dfrac{1}{2}$, $\\operatorname{Im}=-\\dfrac{3}{4}$"], False),

 ("Add meg a konjugált komplex párt!",
  ["$2+5i$", "$-3-4i$", "$7i$", "$-6$", "$1-i$", "$-\\dfrac{1}{2}+2i$"],
  ["$2-5i$", "$-3+4i$", "$-7i$", "$-6$", "$1+i$", "$-\\dfrac{1}{2}-2i$"], True),

 ("Számítsd ki a moduluszt!",
  ["$|3+4i|$", "$|5-12i|$", "$|8+6i|$", "$|-i|$", "$|-7|$", "$|1+i|$"],
  ["$5$", "$13$", "$10$", "$1$", "$7$", "$\\sqrt{2}$"], True),

 ("Oldd meg a komplex számok halmazán!",
  ["$x^{2}=-1$", "$x^{2}=-25$", "$x^{2}=-4$", "$3x^{2}+27=0$"],
  ["$x_{1,2}=\\pm i$", "$x_{1,2}=\\pm 5i$", "$x_{1,2}=\\pm 2i$", "$x_{1,2}=\\pm 3i$"], True),

 ("Hol helyezkedik el a szám a Gauss-síkon?",
  ["$z=4$", "$z=-2i$", "$z=-3+2i$", "$z=1-4i$"],
  ["A valós tengelyen, a $(4;0)$ pontban.", "A képzetes tengelyen, a $(0;-2)$ pontban.",
   "A második síknegyedben, a $(-3;2)$ pontban.",
   "A negyedik síknegyedben, az $(1;-4)$ pontban."], False),

 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["Minden valós szám komplex szám is.", "$\\operatorname{Im}(3-5i)=-5i$",
   "A modulusz mindig nemnegatív valós szám.", "$\\overline{\\overline{z}}=z$",
   "$i^{2}=1$", "A $z=4i$ szám valós része $4$."],
  ["Igaz.", "Hamis, helyesen $-5$ (az $i$ nélkül).", "Igaz.", "Igaz.",
   "Hamis, $i^{2}=-1$.", "Hamis, a valós rész $0$."], False),

 ("Végezd el az összeadást, illetve a kivonást!",
  ["$(3+2i)+(5-7i)$", "$(-4+i)+(6+3i)$", "$(7-2i)-(3+5i)$", "$(1-i)-(-2-4i)$"],
  ["$8-5i$", "$2+4i$", "$4-7i$", "$3+3i$"], True),

 ("Végezd el a szorzást!",
  ["$(2+3i)(1+4i)$", "$(3-i)(2+5i)$", "$(1+i)(1-i)$", "$(2-3i)^{2}$"],
  ["$-10+11i$", "$11+13i$", "$2$", "$-5-12i$"], True),

 ("Számítsd ki!",
  ["$i\\cdot(3+2i)$", "$(2i)^{2}$", "$(3i)(4i)$", "$-i(5-i)$"],
  ["$-2+3i$", "$-4$", "$-12$", "$-1-5i$"], True),

 ("Végezd el az osztást!",
  ["$\\dfrac{1}{i}$", "$\\dfrac{2}{1+i}$", "$\\dfrac{5}{2-i}$", "$\\dfrac{1+i}{1-i}$"],
  ["$-i$", "$1-i$", "$2+i$", "$i$"], True),

 ("Legyen $z=2-5i$. Számítsd ki!",
  ["$z+\\overline{z}$", "$z-\\overline{z}$", "$z\\cdot\\overline{z}$", "$|z|^{2}$"],
  ["$4$", "$-10i$", "$29$", "$29$"], True),

 ("Számítsd ki!",
  ["$(1+2i)+(1-2i)$", "$(3+i)(3-i)$", "$\\dfrac{4}{2i}$", "$(1-i)^{2}$"],
  ["$2$", "$10$", "$-2i$", "$-2i$"], True),

 ("Számítsd ki a képzetes egység hatványait!",
  ["$i^{4}$", "$i^{7}$", "$i^{10}$", "$i^{13}$", "$i^{20}$", "$i^{31}$"],
  ["$1$", "$-i$", "$-1$", "$i$", "$1$", "$-i$"], True),

 ("Számítsd ki! (Oszd a kitevőt $4$-gyel, és nézd a maradékot.)",
  ["$i^{50}$", "$i^{101}$", "$i^{2024}$", "$i^{2027}$"],
  ["$-1$", "$i$", "$1$", "$-i$"], True),

 ("Végezd el a műveleteket!",
  ["$i^{3}+i^{5}$", "$2i^{6}-3i^{8}$", "$i^{9}+i^{11}$", "$3i^{12}+2i^{14}$"],
  ["$0$", "$-5$", "$0$", "$1$"], True),

 ("Oldd meg a komplex számok halmazán!",
  ["$iz=1$", "$2z=6-4i$", "$(1+i)z=2$", "$(1-i)z=2i$"],
  ["$z=-i$", "$z=3-2i$", "$z=1-i$", "$z=-1+i$"], True),

 ("Oldd meg a komplex számok halmazán!",
  ["$z+3i=5-2i$", "$2z-1=3+7i$", "$\\overline{z}=4-6i$"],
  ["$z=5-5i$", "$z=2+\\dfrac{7}{2}i$", "$z=4+6i$"], True),

 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["$i^{4k}=1$ minden $k\\in\\mathbb{N}$ esetén", "$i^{2}=i\\cdot i=-1$",
   "$\\dfrac{1}{i}=i$", "$(2i)^{2}=2i^{2}=-2$"],
  ["Igaz.", "Igaz.", "Hamis, helyesen $-i$.",
   "Hamis: a $2$-t is négyzetre kell emelni, $(2i)^{2}=-4$."], False),
]

KOZEP = [
 ("Végezd el a műveletet, majd add meg $z$ valós részét, képzetes részét, konjugáltját és moduluszát!",
  ["$z=(2+3i)+(1-5i)$", "$z=(4-i)-(2+3i)$", "$z=3i(2-i)$"],
  ["$z=3-2i$; $\\operatorname{Re}=3$, $\\operatorname{Im}=-2$, $\\overline{z}=3+2i$, $|z|=\\sqrt{13}$",
   "$z=2-4i$; $\\operatorname{Re}=2$, $\\operatorname{Im}=-4$, $\\overline{z}=2+4i$, $|z|=2\\sqrt{5}$",
   "$z=3+6i$; $\\operatorname{Re}=3$, $\\operatorname{Im}=6$, $\\overline{z}=3-6i$, $|z|=3\\sqrt{5}$"], False),

 ("Oldd meg a komplex számok halmazán!",
  ["$x^{2}+16=0$", "$2x^{2}+50=0$", "$x^{2}+\\dfrac{1}{4}=0$", "$5x^{2}+45=0$"],
  ["$x_{1,2}=\\pm 4i$", "$x_{1,2}=\\pm 5i$", "$x_{1,2}=\\pm\\dfrac{1}{2}i$", "$x_{1,2}=\\pm 3i$"], True),

 ("Számítsd ki!",
  ["$|3-4i|+|5+12i|$", "$|1+i|\\cdot|1-i|$", "$|2i|-|-3|$", "$\\left|(3+4i)(1-i)\\right|$"],
  ["$18$", "$2$", "$-1$", "$5\\sqrt{2}$"], True),

 ("Igaz-e minden $z\\in\\mathbb{C}$ esetén? Indokolj!",
  ["$z+\\overline{z}$ mindig valós szám.", "$z\\cdot\\overline{z}$ mindig nemnegatív valós szám.",
   "$z-\\overline{z}$ mindig valós szám.", "$|z|=|\\overline{z}|$"],
  ["Igaz, $z+\\overline{z}=2\\operatorname{Re}(z)$.", "Igaz, $z\\overline{z}=|z|^{2}$.",
   "Hamis: $z-\\overline{z}=2\\operatorname{Im}(z)\\cdot i$, ami tisztán képzetes.",
   "Igaz, a tükrözés nem változtatja a hosszt."], False),

 ("Végezd el a műveleteket!",
  ["$(2+3i)(4-i)-(1-2i)^{2}$", "$(5-2i)(2+i)+(2-3i)^{2}$", "$(3+i)(2+3i)-(1-i)^{2}$"],
  ["$14+14i$", "$7-11i$", "$3+13i$"], False),

 ("Végezd el az osztást! (Bővíts a nevező konjugáltjával.)",
  ["$\\dfrac{2+i}{2-i}$", "$\\dfrac{3+2i}{1+i}$", "$\\dfrac{5-10i}{3+4i}$"],
  ["$\\dfrac{3+4i}{5}$", "$\\dfrac{5-i}{2}$", "$-1-2i$"], False),

 ("Legyen $z_{1}=2+3i$, $z_{2}=-2-4i$ és $z_{3}=-1+i$. Számítsd ki!",
  ["$z_{1}+z_{2}$", "$z_{1}-2z_{2}+z_{3}$", "$z_{1}\\cdot z_{2}$", "$\\dfrac{z_{1}}{z_{3}}$"],
  ["$-i$", "$5+12i$", "$8-14i$", "$\\dfrac{1-5i}{2}$"], True),

 ("Legyen $z=1+i$. Számítsd ki!",
  ["$z^{2}$", "$z^{3}$", "$z^{4}$", "$\\dfrac{1}{z}$"],
  ["$2i$", "$-2+2i$", "$-4$", "$\\dfrac{1-i}{2}$"], True),

 ("Számítsd ki a pontos értéket!",
  ["$\\dfrac{1+i}{1-i}+\\dfrac{1-i}{1+i}$", "$\\dfrac{2}{1+i}-\\dfrac{2}{1-i}$",
   "$\\left(\\dfrac{1+i}{\\sqrt{2}}\\right)^{2}$"],
  ["$0$", "$-2i$", "$i$"], True),

 ("Számítsd ki!",
  ["$i^{25}+i^{50}+i^{75}+i^{100}$", "$2i^{15}-3i^{22}+i^{33}$", "$i^{2026}+i^{2027}$"],
  ["$0$", "$3-i$", "$-1-i$"], True),

 ("Oldd meg a komplex számok halmazán!",
  ["$(3+i)z=10$", "$(1-2i)z=5i$", "$(2+3i)z=13$"],
  ["$z=3-i$", "$z=-2+i$", "$z=2-3i$"], True),

 ("Oldd meg! (Írd fel $z=x+yi$ alakban, és bontsd két valós egyenletre.)",
  ["$z+2\\overline{z}=9-3i$", "$3z-\\overline{z}=4+8i$", "$2z+3\\overline{z}=15-i$"],
  ["$z=3+3i$", "$z=2+2i$", "$z=3+i$"], True),

 ("Legyen $z=3-i$. Számítsd ki!",
  ["$z^{2}$", "$z\\cdot\\overline{z}$", "$z+\\overline{z}$", "$\\dfrac{z}{\\overline{z}}$"],
  ["$8-6i$", "$10$", "$6$", "$\\dfrac{4-3i}{5}$"], True),

 ("Számítsd ki! (Használd az $(1\\pm i)^{2}$ értékét.)",
  ["$(1+i)^{8}$", "$(1-i)^{6}$", "$\\dfrac{(1+i)^{4}}{(1-i)^{2}}$"],
  ["$16$", "$8i$", "$-2i$"], True),
]

NEHEZ = [
 ("Számítsd ki! $z=\\dfrac{(1+2i)^{2}}{(1-i)^{10}}$", None, "$z=\\dfrac{-4-3i}{32}$"),
 ("Számítsd ki! $(1+i)^{4}+(1-i)^{4}$", None, "$-8$"),
 ("Legyen $z=1+i$. Számítsd ki $z^{2}\\left(z^{2}-z+1\\right)$ értékét!", None, "$-2$"),
 ("Számítsd ki! $\\dfrac{1+i}{1-i}+i^{24}+i^{33}+i^{49}$", None, "$1+3i$"),
 ("Oldd meg a komplex számok halmazán! $(2+i)z+2\\overline{z}-3=4+6i$", None, "$z=6+17i$"),
 ("Számítsd ki! $\\left(\\dfrac{1-i}{1+i}\\right)^{2027}$", None, "$i$"),
]

JOKER = ("<b>Sinister vírus-kódja.</b> A rendszer ezzel a „bizonyítással” próbálja igazolni, "
         "hogy $-1=1$: $$-1=i^{2}=\\sqrt{-1}\\cdot\\sqrt{-1}\\ \\overset{?}{=}\\ "
         "\\sqrt{(-1)\\cdot(-1)}=\\sqrt{1}=1$$ "
         "Melyik lépés hibás, és miért?",
         "A harmadik lépés: a $\\sqrt{a}\\cdot\\sqrt{b}=\\sqrt{ab}$ azonosság csak $a,b\\ge 0$ "
         "esetén érvényes.")

GYD_ORAI = [
 ("Számítsd ki a számkifejezés pontos értékét! "
  "$\\left(\\dfrac{49}{4}\\right)^{\\frac{1}{2}}-\\left(\\dfrac{5}{2}\\right)^{0}"
  "+\\dfrac{3^{2}}{2}-\\dfrac{(-1)^{3}}{2}$", None, "$\\dfrac{15}{2}$"),
 ("Számítsd ki! $125^{\\frac{2}{3}}+36^{-\\frac{1}{2}}$", None, "$\\dfrac{151}{6}$"),
 ("Gyöktelenítsd és rendezd!",
  ["$\\dfrac{4}{5-\\sqrt{21}}$", "$\\dfrac{14}{\\sqrt{7}}$"],
  ["$5+\\sqrt{21}$", "$2\\sqrt{7}$"], True),
 ("Egyszerűsítsd! $(x&gt;0)$  $\\sqrt[4]{x^{2}\\sqrt{x^{4}}}$", None, "$x$"),
 ("Egyszerűsítsd! $(x,y,z&gt;0)$  $\\sqrt[4]{x^{12}y^{-8}z^{16}}$", None,
  "$\\dfrac{x^{3}z^{4}}{y^{2}}$"),
 ("Hozd egyszerűbb alakra! $(n\\in\\mathbb{N})$  $\\dfrac{2^{n+2}+2^{n+1}}{2^{n}}$", None, "$6$"),
 ("Döntsd el, hogy a hatványfüggvény grafikonja az $y$-tengelyre tükrös (páros) vagy "
  "az origóra szimmetrikus (páratlan)!",
  ["$y=x^{6}$", "$y=x^{-3}$", "$y=x^{5}$", "$y=x^{-4}$"],
  ["Páros.", "Páratlan.", "Páratlan.", "Páros."], True),
 ("Oldd meg a komplex számok halmazán!",
  ["$x^{2}=-64$", "$4x^{2}+36=0$"], ["$x_{1,2}=\\pm 8i$", "$x_{1,2}=\\pm 3i$"], True),
 ("Adottak a $z_{1}=3+4i$ és $z_{2}=1-i$ komplex számok.",
  ["Ábrázold őket a Gauss-síkon!", "$z_{1}+z_{2}$", "$z_{1}\\cdot z_{2}$",
   "$\\dfrac{z_{1}}{z_{2}}$", "$|z_{1}|$", "$\\overline{z_{2}}-z_{1}$"],
  ["A $(3;4)$ és az $(1;-1)$ pont.", "$4+3i$", "$7+i$", "$\\dfrac{-1+7i}{2}$", "$5$",
   "$-2-3i$"], False),
 ("Számítsd ki! $3i^{9}-2i^{14}+i^{27}$", None, "$2+2i$"),
]

GYD_OTTHON = [
 ("Számítsd ki! "
  "$\\left(\\dfrac{1}{3}\\right)^{-3}-\\left(-\\dfrac{1}{2}\\right)^{-4}+(-3)^{-1}$",
  None, "$\\dfrac{32}{3}$"),
 ("Gyöktelenítsd!",
  ["$\\dfrac{6}{\\sqrt{3}+\\sqrt{2}}$", "$\\dfrac{9}{\\sqrt[3]{3}}$"],
  ["$6\\left(\\sqrt{3}-\\sqrt{2}\\right)$", "$3\\sqrt[3]{9}$"], True),
 ("Egyszerűsítsd! $(a&gt;0)$  "
  "$\\dfrac{\\sqrt[3]{a^{4}}\\cdot\\sqrt{a}}{\\sqrt[6]{a}}$", None, "$\\sqrt[3]{a^{5}}$"),
 ("Oldd meg a komplex számok halmazán! $(1+3i)z=10$", None, "$z=1-3i$"),
 ("Legyen $z=2-3i$. Számítsd ki!",
  ["$\\overline{z}$", "$|z|$", "$z\\cdot\\overline{z}$", "$z^{2}$"],
  ["$2+3i$", "$\\sqrt{13}$", "$13$", "$-5-12i$"], True),
 ("Számítsd ki! $i^{2026}-2i^{2027}+3i^{2028}$", None, "$2+2i$"),
]

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
 '    <h2 id="gyak-dolgozat">📝 Gyakorló dolgozat — a teljes témakör</h2>\n    ' + DISZKLEMER +
 '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYD_ORAI, "gyd") +
 '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYD_OTTHON, "gydh"),
]

ut = oldal(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
           fajl="feladatok-komplex-szamok.html", cim="Komplex számok",
           temakor="Hatványozás, gyökvonás, komplex számok",
           alcim="Algebrai alak, Gauss-sík, konjugált és modulusz, a négy alapművelet, az $i$ "
                 "hatványai és egyenletek $\\mathbb{C}$-ben — a végén gyakorló dolgozat a "
                 "TELJES témakörre. A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-i-hatvanyai-es-egyenletek.html", prevc="Az $i$ hatványai és egyenletek",
           nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYD_ORAI), "+", len(GYD_OTTHON))
