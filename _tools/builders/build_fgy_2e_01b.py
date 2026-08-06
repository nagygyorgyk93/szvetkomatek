# -*- coding: utf-8 -*-
"""2e/01 — „B" altéma feladatgyűjtemény: gyökvonás, műveletek, gyöktelenítés,
racionális kitevő. + gyakorló ELLENŐRZŐ (🏫 órai / 🏠 otthoni)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, simplify, sqrt, root, Integer, Abs
a, b, x, y = symbols('a b x y', positive=True)
E = []
def ell(nev, kif, vart):
    if simplify(kif - vart) != 0:
        E.append((nev, simplify(kif), vart))

# Alap
for nev, k, v in [("A1a", sqrt(169), 13), ("A1b", root(64, 3), 4), ("A1d", root(81, 4), 3),
                  ("A1f", sqrt(R(1, 4)), R(1, 2)), ("A2f", root(64, 6), 2),
                  ("A3a", sqrt(36), 6), ("A3c", sqrt(7)**2, 7), ("A3e", root(16, 4), 2),
                  ("A5a", root(a**2, 6), root(a, 3)), ("A5b", root(a**4, 8), sqrt(a)),
                  ("A5c", root(a**6, 9), root(a**2, 3)), ("A5d", root(a**2, 4), sqrt(a)),
                  ("A6a", sqrt(50), 5*sqrt(2)), ("A6b", sqrt(18), 3*sqrt(2)),
                  ("A6c", sqrt(75), 5*sqrt(3)), ("A6d", sqrt(98), 7*sqrt(2)),
                  ("A6e", root(16, 3), 2*root(2, 3)), ("A6f", root(81, 3), 3*root(3, 3)),
                  ("A7a", 2*sqrt(3), sqrt(12)), ("A7b", 5*sqrt(2), sqrt(50)),
                  ("A7c", 3*root(2, 3), root(54, 3)), ("A7d", 2*root(3, 4), root(48, 4)),
                  ("A8a", sqrt(8)+sqrt(18), 5*sqrt(2)), ("A8b", sqrt(27)-sqrt(12), sqrt(3)),
                  ("A8c", 2*sqrt(45)+sqrt(20), 8*sqrt(5)),
                  ("A8d", sqrt(50)-sqrt(32)+sqrt(8), 3*sqrt(2)),
                  ("A9a", sqrt(3)*sqrt(12), 6), ("A9b", sqrt(2)*sqrt(8), 4),
                  ("A9c", root(2, 3)*root(4, 3), 2), ("A9d", sqrt(5)*sqrt(5), 5),
                  ("A10a", (sqrt(7)+sqrt(3))*(sqrt(7)-sqrt(3)), 4),
                  ("A10b", (sqrt(10)-sqrt(6))*(sqrt(10)+sqrt(6)), 4),
                  ("A10c", (sqrt(5)+2)*(sqrt(5)-2), 1),
                  ("A10d", (sqrt(3)+1)**2, 4+2*sqrt(3)),
                  ("A11a", sqrt(sqrt(x)), root(x, 4)), ("A11b", root(sqrt(x), 3), root(x, 6)),
                  ("A11c", sqrt(x**3), x*sqrt(x)), ("A11d", sqrt(16*x**4), 4*x**2),
                  ("A12a", 1/sqrt(5), sqrt(5)/5), ("A12b", 6/sqrt(2), 3*sqrt(2)),
                  ("A12c", 10/sqrt(5), 2*sqrt(5)), ("A12d", 3/sqrt(3), sqrt(3)),
                  ("A13a", 2/root(4, 3), root(2, 3)), ("A13b", 5/root(25, 3), root(5, 3)),
                  ("A13c", 3/root(27, 4), root(3, 4)),
                  ("A14a", 2/(sqrt(5)-sqrt(3)), sqrt(5)+sqrt(3)),
                  ("A14b", 6/(sqrt(7)+1), sqrt(7)-1),
                  ("A14c", 4/(3-sqrt(5)), 3+sqrt(5)),
                  ("A14d", 1/(sqrt(3)+sqrt(2)), sqrt(3)-sqrt(2)),
                  ("A17a", Integer(9)**R(1, 2), 3), ("A17b", Integer(8)**R(1, 3), 2),
                  ("A17c", Integer(16)**R(3, 4), 8), ("A17d", Integer(25)**R(-1, 2), R(1, 5)),
                  ("A17e", Integer(27)**R(2, 3), 9), ("A17f", Integer(64)**R(-1, 3), R(1, 4))]:
    ell(nev, k, v)
# Közép
for nev, k, v in [("K1a", sqrt(a**6*b**4), a**3*b**2), ("K1b", root(a**9*b**6, 3), a**3*b**2),
                  ("K1c", root(16*a**8, 4), 2*a**2), ("K1d", root(32*a**10*b**15, 5), 2*a**2*b**3),
                  ("K3a", root(sqrt(729), 3), 3), ("K3b", sqrt(root(64, 3)), 2),
                  ("K3c", root(sqrt(256), 4), 2),
                  ("K5a", 3*sqrt(32)-2*sqrt(50)+sqrt(72), 8*sqrt(2)),
                  ("K5b", sqrt(48)+2*sqrt(27)-sqrt(75), 5*sqrt(3)),
                  ("K5c", 2*sqrt(63)-sqrt(112)+sqrt(7), 3*sqrt(7)),
                  ("K6a", (2*sqrt(5)+sqrt(3))*(2*sqrt(5)-sqrt(3)), 17),
                  ("K6b", (sqrt(6)-sqrt(2))**2, 8-4*sqrt(3)),
                  ("K6c", (sqrt(7)+sqrt(5))**2-(sqrt(7)-sqrt(5))**2, 4*sqrt(35)),
                  ("K7a", sqrt(a)*root(a, 3), root(a**5, 6)),
                  ("K7b", root(a**2, 3)/root(a, 6), sqrt(a)),
                  ("K7c", sqrt(a*sqrt(a)), root(a**3, 4)),
                  ("K8a", sqrt((3-sqrt(10))**2), sqrt(10)-3),
                  ("K8b", sqrt((2-sqrt(3))**2), 2-sqrt(3)),
                  ("K8c", sqrt((sqrt(5)-3)**2), 3-sqrt(5)),
                  ("K9a", sqrt(50*x**3*y), 5*x*sqrt(2*x*y)),
                  ("K9b", root(54*x**4*y**6, 3), 3*x*y**2*root(2*x, 3)),
                  ("K9c", sqrt(18*x**5/(2*x)), 3*x**2),
                  ("K10a", sqrt(5)/(sqrt(5)-sqrt(2)), (5+sqrt(10))/3),
                  ("K10b", (sqrt(3)+1)/(sqrt(3)-1), 2+sqrt(3)),
                  ("K10c", 2/(sqrt(6)-sqrt(2)), (sqrt(6)+sqrt(2))/2),
                  ("K11a", 1/(sqrt(3)-sqrt(2))+1/(sqrt(3)+sqrt(2)), 2*sqrt(3)),
                  ("K11b", 1/(sqrt(5)+2)-1/(sqrt(5)-2), -4),
                  ("K11c", 3/(sqrt(7)-2)-3/(sqrt(7)+2), 4),
                  ("K12a", Integer(32)**R(2, 5), 4),
                  ("K12b", R(8, 27)**R(-2, 3), R(9, 4)),
                  ("K12c", R(1, 16)**R(-1, 4), 2),
                  ("K12d", R(16, 81)**R(3, 4), R(8, 27)),
                  ("K13a", a**R(1, 2)*a**R(1, 3)*a**R(1, 6), a),
                  ("K13b", a**R(3, 4)*a**R(1, 2)/a**R(1, 4), a),
                  ("K13c", (a**R(2, 3))**R(3, 4), sqrt(a)),
                  ("K14a", Integer(4)**R(1, 2)+Integer(8)**R(2, 3)+Integer(16)**R(3, 4), 14),
                  ("K14b", Integer(9)**R(-1, 2)+Integer(27)**R(-1, 3), R(2, 3)),
                  ("K14c", (Integer(2)**-2)**R(-3, 2), 8)]:
    ell(nev, k, v)
# Nehéz
ell("N1", sqrt(a*root(a*sqrt(a), 3)), root(a**3, 4))
ell("N2", 2/(sqrt(3)+1)+3/(sqrt(3)-1)-4/sqrt(3), (7*sqrt(3)+3)/6)
ell("N3", sqrt(7+4*sqrt(3)), 2+sqrt(3))
ell("N4", root(a, 3)*root(a, 4), root(a**7, 12))
ell("N5", (sqrt(5)+sqrt(3))**2*(8-2*sqrt(15)), 4)
ell("JOK", sqrt((2-5)**2), 3)
# Gyakorló
for nev, k, v in [("GY1", R(1, 2)**-2+R(-1, 2)**2-R(1, 2**2), 4),
                  ("GY2a", 1/sqrt(7), sqrt(7)/7), ("GY2b", 12/sqrt(6), 2*sqrt(6)),
                  ("GY2c", 8/(sqrt(5)-1), 2*(sqrt(5)+1)),
                  ("GY3a", sqrt(a**8*b**6), a**4*b**3),
                  ("GY3b", root(a**3*sqrt(a**2), 4), a),
                  ("GY4", (a**3/b**-2)**2*(a**-1/b**3)**-1, a**7*b**7),
                  ("GY5", sqrt(28)-sqrt(63)+2*sqrt(7), sqrt(7)),
                  ("GY6", Integer(8)**R(2, 3)-Integer(16)**R(1, 4)+Integer(81)**R(-1, 2), R(19, 9)),
                  ("GYH1", R(2, 5)**-2-R(-1, 2)**-2, R(9, 4)),
                  ("GYH2a", 9/sqrt(3), 3*sqrt(3)),
                  ("GYH2b", 5/(sqrt(10)+sqrt(5)), sqrt(10)-sqrt(5)),
                  ("GYH3a", root(27*x**6*y**9, 3), 3*x**2*y**3),
                  ("GYH3b", root(x**4, 6), root(x**2, 3)),
                  ("GYH4", x**R(2, 3)*x**R(1, 2)/x**R(1, 6), x),
                  ("GYH5", (sqrt(11)-sqrt(6))*(sqrt(11)+sqrt(6))+(sqrt(5)-1)**2, 11-2*sqrt(5)),
                  ("GYH6", R(27, 8)**R(-1, 3)+R(1, 16)**R(-3, 4), R(26, 3))]:
    ell(nev, k, v)
assert not E, E[:5]
# rendezések
assert root(4, 3) < root(20, 6) < sqrt(3)
assert sqrt(2) < root(3, 3) < root(5, 4)
assert root(2, 3) < root(5, 6) < root(3, 4)
assert sqrt(2) < root(5, 3) < root(30, 6)
print("sympy önteszt: OK")

# ============================== FELADATOK ==============================

ALAP = [
 ("Számítsd ki a gyökök pontos értékét!",
  ["$\\sqrt{169}$", "$\\sqrt[3]{64}$", "$\\sqrt[3]{-27}$", "$\\sqrt[4]{81}$",
   "$\\sqrt[5]{-1}$", "$\\sqrt{0{,}25}$"],
  ["$13$", "$4$", "$-3$", "$3$", "$-1$", "$0{,}5$"], True),

 ("Számítsd ki, ha létezik a valós számok halmazán!",
  ["$\\sqrt{-16}$", "$\\sqrt[3]{-8}$", "$\\sqrt[4]{-16}$", "$\\sqrt[5]{-32}$",
   "$\\sqrt{0}$", "$\\sqrt[6]{64}$"],
  ["Nem létezik.", "$-2$", "Nem létezik.", "$-2$", "$0$", "$2$"], True),

 ("Add meg a pontos értéket!",
  ["$\\sqrt{(-6)^{2}}$", "$\\sqrt[3]{(-6)^{3}}$", "$\\left(\\sqrt{7}\\right)^{2}$",
   "$\\left(\\sqrt[3]{5}\\right)^{3}$", "$\\sqrt[4]{(-2)^{4}}$", "$\\sqrt[5]{(-2)^{5}}$"],
  ["$6$", "$-6$", "$7$", "$5$", "$2$", "$-2$"], True),

 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["$\\sqrt{a^{2}}=a$ minden valós $a$-ra", "$\\sqrt[3]{a^{3}}=a$ minden valós $a$-ra",
   "$\\sqrt{25}=\\pm 5$", "$\\sqrt{9+16}=\\sqrt{9}+\\sqrt{16}$",
   "$\\sqrt{4\\cdot 9}=\\sqrt{4}\\cdot\\sqrt{9}$",
   "$\\sqrt[4]{-81}$ nincs értelmezve a valós számok halmazán"],
  ["Hamis, helyesen $|a|$.", "Igaz.", "Hamis, helyesen $5$.",
   "Hamis: $5\\neq 7$.", "Igaz.", "Igaz."], False),

 ("Egyszerűsítsd a gyökkitevőt! $(a&gt;0)$",
  ["$\\sqrt[6]{a^{2}}$", "$\\sqrt[8]{a^{4}}$", "$\\sqrt[9]{a^{6}}$", "$\\sqrt[4]{a^{2}}$"],
  ["$\\sqrt[3]{a}$", "$\\sqrt{a}$", "$\\sqrt[3]{a^{2}}$", "$\\sqrt{a}$"], True),

 ("Hozd ki a gyökjel alól a lehető legnagyobb tényezőt!",
  ["$\\sqrt{50}$", "$\\sqrt{18}$", "$\\sqrt{75}$", "$\\sqrt{98}$",
   "$\\sqrt[3]{16}$", "$\\sqrt[3]{81}$"],
  ["$5\\sqrt{2}$", "$3\\sqrt{2}$", "$5\\sqrt{3}$", "$7\\sqrt{2}$",
   "$2\\sqrt[3]{2}$", "$3\\sqrt[3]{3}$"], True),

 ("Vidd be a tényezőt a gyökjel alá!",
  ["$2\\sqrt{3}$", "$5\\sqrt{2}$", "$3\\sqrt[3]{2}$", "$2\\sqrt[4]{3}$"],
  ["$\\sqrt{12}$", "$\\sqrt{50}$", "$\\sqrt[3]{54}$", "$\\sqrt[4]{48}$"], True),

 ("Végezd el a műveleteket!",
  ["$\\sqrt{8}+\\sqrt{18}$", "$\\sqrt{27}-\\sqrt{12}$", "$2\\sqrt{45}+\\sqrt{20}$",
   "$\\sqrt{50}-\\sqrt{32}+\\sqrt{8}$"],
  ["$5\\sqrt{2}$", "$\\sqrt{3}$", "$8\\sqrt{5}$", "$3\\sqrt{2}$"], True),

 ("Szorozd össze!",
  ["$\\sqrt{3}\\cdot\\sqrt{12}$", "$\\sqrt{2}\\cdot\\sqrt{8}$",
   "$\\sqrt[3]{2}\\cdot\\sqrt[3]{4}$", "$\\sqrt{5}\\cdot\\sqrt{5}$"],
  ["$6$", "$4$", "$2$", "$5$"], True),

 ("Számítsd ki a nevezetes azonosságok segítségével!",
  ["$\\left(\\sqrt{7}+\\sqrt{3}\\right)\\left(\\sqrt{7}-\\sqrt{3}\\right)$",
   "$\\left(\\sqrt{10}-\\sqrt{6}\\right)\\left(\\sqrt{10}+\\sqrt{6}\\right)$",
   "$\\left(\\sqrt{5}+2\\right)\\left(\\sqrt{5}-2\\right)$", "$\\left(\\sqrt{3}+1\\right)^{2}$"],
  ["$4$", "$4$", "$1$", "$4+2\\sqrt{3}$"], True),

 ("Egyszerűsítsd! $(x&gt;0)$",
  ["$\\sqrt{\\sqrt{x}}$", "$\\sqrt[3]{\\sqrt{x}}$", "$\\sqrt{x^{3}}$", "$\\sqrt{16x^{4}}$"],
  ["$\\sqrt[4]{x}$", "$\\sqrt[6]{x}$", "$x\\sqrt{x}$", "$4x^{2}$"], True),

 ("Gyöktelenítsd a nevezőt!",
  ["$\\dfrac{1}{\\sqrt{5}}$", "$\\dfrac{6}{\\sqrt{2}}$", "$\\dfrac{10}{\\sqrt{5}}$",
   "$\\dfrac{3}{\\sqrt{3}}$"],
  ["$\\dfrac{\\sqrt{5}}{5}$", "$3\\sqrt{2}$", "$2\\sqrt{5}$", "$\\sqrt{3}$"], True),

 ("Gyöktelenítsd a nevezőt! (magasabb gyökkitevő)",
  ["$\\dfrac{2}{\\sqrt[3]{4}}$", "$\\dfrac{5}{\\sqrt[3]{25}}$", "$\\dfrac{3}{\\sqrt[4]{27}}$"],
  ["$\\sqrt[3]{2}$", "$\\sqrt[3]{5}$", "$\\sqrt[4]{3}$"], True),

 ("Gyöktelenítsd a kéttagú nevezőt!",
  ["$\\dfrac{2}{\\sqrt{5}-\\sqrt{3}}$", "$\\dfrac{6}{\\sqrt{7}+1}$",
   "$\\dfrac{4}{3-\\sqrt{5}}$", "$\\dfrac{1}{\\sqrt{3}+\\sqrt{2}}$"],
  ["$\\sqrt{5}+\\sqrt{3}$", "$\\sqrt{7}-1$", "$3+\\sqrt{5}$", "$\\sqrt{3}-\\sqrt{2}$"], True),

 ("Írd át gyökös alakba! $(a&gt;0)$",
  ["$a^{\\frac{1}{2}}$", "$a^{\\frac{2}{3}}$", "$a^{-\\frac{1}{2}}$", "$a^{\\frac{3}{4}}$"],
  ["$\\sqrt{a}$", "$\\sqrt[3]{a^{2}}$", "$\\dfrac{1}{\\sqrt{a}}$", "$\\sqrt[4]{a^{3}}$"], True),

 ("Írd át hatvány alakba! $(a&gt;0)$",
  ["$\\sqrt{a}$", "$\\sqrt[3]{a^{2}}$", "$\\dfrac{1}{\\sqrt[4]{a}}$", "$\\sqrt[5]{a^{3}}$"],
  ["$a^{\\frac{1}{2}}$", "$a^{\\frac{2}{3}}$", "$a^{-\\frac{1}{4}}$", "$a^{\\frac{3}{5}}$"], True),

 ("Számítsd ki a racionális kitevőjű hatvány értékét!",
  ["$9^{\\frac{1}{2}}$", "$8^{\\frac{1}{3}}$", "$16^{\\frac{3}{4}}$",
   "$25^{-\\frac{1}{2}}$", "$27^{\\frac{2}{3}}$", "$64^{-\\frac{1}{3}}$"],
  ["$3$", "$2$", "$8$", "$\\dfrac{1}{5}$", "$9$", "$\\dfrac{1}{4}$"], True),
]

KOZEP = [
 ("Egyszerűsítsd! $(a,b&gt;0)$",
  ["$\\sqrt{a^{6}b^{4}}$", "$\\sqrt[3]{a^{9}b^{6}}$", "$\\sqrt[4]{16a^{8}}$",
   "$\\sqrt[5]{32a^{10}b^{15}}$"],
  ["$a^{3}b^{2}$", "$a^{3}b^{2}$", "$2a^{2}$", "$2a^{2}b^{3}$"], True),

 ("Most $a$ <b>tetszőleges valós szám</b>. Add meg a helyes alakot!",
  ["$\\sqrt{a^{2}}$", "$\\sqrt[4]{a^{4}}$", "$\\sqrt{a^{4}}$", "$\\sqrt[3]{a^{3}}$",
   "$\\sqrt{9a^{2}}$"],
  ["$|a|$", "$|a|$", "$a^{2}$", "$a$", "$3|a|$"], True),

 ("Számítsd ki!",
  ["$\\sqrt[3]{\\sqrt{729}}$", "$\\sqrt{\\sqrt[3]{64}}$", "$\\sqrt[4]{\\sqrt{256}}$"],
  ["$3$", "$2$", "$2$"], True),

 ("Rendezd növekvő sorrendbe! (Hozd közös gyökkitevőre!)",
  ["$\\sqrt{3}$, $\\sqrt[3]{4}$, $\\sqrt[6]{20}$", "$\\sqrt{2}$, $\\sqrt[3]{3}$, $\\sqrt[4]{5}$"],
  ["$\\sqrt[3]{4}&lt;\\sqrt[6]{20}&lt;\\sqrt{3}$",
   "$\\sqrt{2}&lt;\\sqrt[3]{3}&lt;\\sqrt[4]{5}$"], False),

 ("Végezd el a műveleteket!",
  ["$3\\sqrt{32}-2\\sqrt{50}+\\sqrt{72}$", "$\\sqrt{48}+2\\sqrt{27}-\\sqrt{75}$",
   "$2\\sqrt{63}-\\sqrt{112}+\\sqrt{7}$"],
  ["$8\\sqrt{2}$", "$5\\sqrt{3}$", "$3\\sqrt{7}$"], False),

 ("Számítsd ki a pontos értéket!",
  ["$\\left(2\\sqrt{5}+\\sqrt{3}\\right)\\left(2\\sqrt{5}-\\sqrt{3}\\right)$",
   "$\\left(\\sqrt{6}-\\sqrt{2}\\right)^{2}$",
   "$\\left(\\sqrt{7}+\\sqrt{5}\\right)^{2}-\\left(\\sqrt{7}-\\sqrt{5}\\right)^{2}$"],
  ["$17$", "$8-4\\sqrt{3}$", "$4\\sqrt{35}$"], False),

 ("Egyszerűsítsd a tört kitevő segítségével! $(a&gt;0)$",
  ["$\\sqrt{a}\\cdot\\sqrt[3]{a}$", "$\\sqrt[3]{a^{2}}:\\sqrt[6]{a}$", "$\\sqrt{a\\sqrt{a}}$"],
  ["$\\sqrt[6]{a^{5}}$", "$\\sqrt{a}$", "$\\sqrt[4]{a^{3}}$"], False),

 ("Számítsd ki a pontos értéket! (Vigyázz az előjelre!)",
  ["$\\sqrt{\\left(3-\\sqrt{10}\\right)^{2}}$", "$\\sqrt{\\left(2-\\sqrt{3}\\right)^{2}}$",
   "$\\sqrt{\\left(\\sqrt{5}-3\\right)^{2}}$"],
  ["$\\sqrt{10}-3$", "$2-\\sqrt{3}$", "$3-\\sqrt{5}$"], False),

 ("Egyszerűsítsd! $(x,y&gt;0)$",
  ["$\\sqrt{50x^{3}y}$", "$\\sqrt[3]{54x^{4}y^{6}}$", "$\\sqrt{\\dfrac{18x^{5}}{2x}}$"],
  ["$5x\\sqrt{2xy}$", "$3xy^{2}\\sqrt[3]{2x}$", "$3x^{2}$"], False),

 ("Gyöktelenítsd és hozd egyszerűbb alakra!",
  ["$\\dfrac{\\sqrt{5}}{\\sqrt{5}-\\sqrt{2}}$", "$\\dfrac{\\sqrt{3}+1}{\\sqrt{3}-1}$",
   "$\\dfrac{2}{\\sqrt{6}-\\sqrt{2}}$"],
  ["$\\dfrac{5+\\sqrt{10}}{3}$", "$2+\\sqrt{3}$", "$\\dfrac{\\sqrt{6}+\\sqrt{2}}{2}$"], False),

 ("Számítsd ki a pontos értéket!",
  ["$\\dfrac{1}{\\sqrt{3}-\\sqrt{2}}+\\dfrac{1}{\\sqrt{3}+\\sqrt{2}}$",
   "$\\dfrac{1}{\\sqrt{5}+2}-\\dfrac{1}{\\sqrt{5}-2}$",
   "$\\dfrac{3}{\\sqrt{7}-2}-\\dfrac{3}{\\sqrt{7}+2}$"],
  ["$2\\sqrt{3}$", "$-4$", "$4$"], False),

 ("Számítsd ki!",
  ["$32^{0{,}4}$", "$\\left(\\dfrac{8}{27}\\right)^{-\\frac{2}{3}}$",
   "$\\left(0{,}0625\\right)^{-\\frac{1}{4}}$", "$\\left(\\dfrac{16}{81}\\right)^{\\frac{3}{4}}$"],
  ["$4$", "$\\dfrac{9}{4}$", "$2$", "$\\dfrac{8}{27}$"], True),

 ("Hozd egyszerűbb alakra! $(a&gt;0)$",
  ["$a^{\\frac{1}{2}}\\cdot a^{\\frac{1}{3}}\\cdot a^{\\frac{1}{6}}$",
   "$\\dfrac{a^{\\frac{3}{4}}\\cdot a^{\\frac{1}{2}}}{a^{\\frac{1}{4}}}$",
   "$\\left(a^{\\frac{2}{3}}\\right)^{\\frac{3}{4}}$"],
  ["$a$", "$a$", "$\\sqrt{a}$"], True),

 ("Számítsd ki a pontos értéket!",
  ["$4^{\\frac{1}{2}}+8^{\\frac{2}{3}}+16^{\\frac{3}{4}}$",
   "$9^{-\\frac{1}{2}}+27^{-\\frac{1}{3}}$", "$\\left(2^{-2}\\right)^{-\\frac{3}{2}}$"],
  ["$14$", "$\\dfrac{2}{3}$", "$8$"], True),
]

NEHEZ = [
 ("Egyszerűsítsd! $(a&gt;0)$  $\\sqrt{a\\sqrt[3]{a\\sqrt{a}}}$", None, "$\\sqrt[4]{a^{3}}$"),
 ("Számítsd ki a pontos értéket! "
  "$\\dfrac{2}{\\sqrt{3}+1}+\\dfrac{3}{\\sqrt{3}-1}-\\dfrac{4}{\\sqrt{3}}$",
  None, "$\\dfrac{7\\sqrt{3}+3}{6}$"),
 ("Számítsd ki! (Keresd az $\\left(p+q\\right)^{2}$ alakot a gyökjel alatt.) "
  "$\\sqrt{7+4\\sqrt{3}}$", None, "$2+\\sqrt{3}$"),
 ("Mutasd meg, hogy $A=B$, ha $a&gt;0$: "
  "$A=\\sqrt[3]{a}\\cdot\\sqrt[4]{a}$, $B=\\sqrt[12]{a^{7}}$", None,
  "Mindkettő $a^{\\frac{7}{12}}$."),
 ("Számítsd ki a pontos értéket! "
  "$\\left(\\sqrt{5}+\\sqrt{3}\\right)^{2}\\cdot\\left(8-2\\sqrt{15}\\right)$", None, "$4$"),
 ("Rendezd növekvő sorrendbe: $\\sqrt[3]{2}$, $\\sqrt[4]{3}$, $\\sqrt[6]{5}$", None,
  "$\\sqrt[3]{2}&lt;\\sqrt[6]{5}&lt;\\sqrt[4]{3}$"),
]

JOKER = ("<b>Dr. Baljós vírus-kódja.</b> A rendszer ezt az azonosságot állítja <b>minden</b> valós "
         "$x$-re: $$\\sqrt{(x-5)^{2}}\\ \\overset{?}{=}\\ x-5$$ "
         "Mikor igaz és mikor hamis? Adj ellenpéldát, és írd fel a helyes alakot!",
         "Csak $x\\ge 5$ esetén igaz. Helyesen $\\sqrt{(x-5)^{2}}=|x-5|$; ellenpélda $x=2$, "
         "ahol az érték $3$, nem $-3$.")

GYE_ORAI = [
 ("Számítsd ki a számkifejezés pontos értékét! "
  "$\\left(\\dfrac{1}{2}\\right)^{-2}+\\left(-\\dfrac{1}{2}\\right)^{2}-\\dfrac{1}{2^{2}}$",
  None, "$4$"),
 ("Gyöktelenítsd és rendezd!",
  ["$\\dfrac{1}{\\sqrt{7}}$", "$\\dfrac{12}{\\sqrt{6}}$", "$\\dfrac{8}{\\sqrt{5}-1}$"],
  ["$\\dfrac{\\sqrt{7}}{7}$", "$2\\sqrt{6}$", "$2\\left(\\sqrt{5}+1\\right)$"], True),
 ("Egyszerűsítsd! $(a,b&gt;0)$",
  ["$\\sqrt{a^{8}b^{6}}$", "$\\sqrt[4]{a^{3}\\sqrt{a^{2}}}$"],
  ["$a^{4}b^{3}$", "$a$"], True),
 ("Egyszerűsítsd! $(a,b&gt;0)$ "
  "$\\left(\\dfrac{a^{3}}{b^{-2}}\\right)^{2}\\cdot\\left(\\dfrac{a^{-1}}{b^{3}}\\right)^{-1}$",
  None, "$a^{7}b^{7}$"),
 ("Végezd el a műveleteket! $\\sqrt{28}-\\sqrt{63}+2\\sqrt{7}$", None, "$\\sqrt{7}$"),
 ("Számítsd ki! $8^{\\frac{2}{3}}-16^{\\frac{1}{4}}+81^{-\\frac{1}{2}}$", None, "$\\dfrac{19}{9}$"),
 ("Rendezd növekvő sorrendbe: $\\sqrt[3]{5}$, $\\sqrt{2}$, $\\sqrt[6]{30}$", None,
  "$\\sqrt{2}&lt;\\sqrt[3]{5}&lt;\\sqrt[6]{30}$"),
 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["$\\sqrt[3]{-64}=-4$", "$\\sqrt{b^{2}}=b$ minden valós $b$-re",
   "$\\left(\\dfrac{3}{5}\\right)^{-1}=\\dfrac{5}{3}$", "$\\sqrt{16+9}=\\sqrt{16}+\\sqrt{9}$"],
  ["Igaz.", "Hamis, helyesen $|b|$.", "Igaz.", "Hamis: $5\\neq 7$."], False),
]

GYE_OTTHON = [
 ("Számítsd ki! $\\left(\\dfrac{2}{5}\\right)^{-2}-\\left(-\\dfrac{1}{2}\\right)^{-2}$",
  None, "$\\dfrac{9}{4}$"),
 ("Gyöktelenítsd!",
  ["$\\dfrac{9}{\\sqrt{3}}$", "$\\dfrac{5}{\\sqrt{10}+\\sqrt{5}}$"],
  ["$3\\sqrt{3}$", "$\\sqrt{10}-\\sqrt{5}$"], True),
 ("Egyszerűsítsd! $(x,y&gt;0)$",
  ["$\\sqrt[3]{27x^{6}y^{9}}$", "$\\sqrt[6]{x^{4}}$"],
  ["$3x^{2}y^{3}$", "$\\sqrt[3]{x^{2}}$"], True),
 ("Egyszerűsítsd! $(x&gt;0)$ "
  "$\\dfrac{x^{\\frac{2}{3}}\\cdot x^{\\frac{1}{2}}}{x^{\\frac{1}{6}}}$", None, "$x$"),
 ("Végezd el a műveleteket! "
  "$\\left(\\sqrt{11}-\\sqrt{6}\\right)\\left(\\sqrt{11}+\\sqrt{6}\\right)"
  "+\\left(\\sqrt{5}-1\\right)^{2}$", None, "$11-2\\sqrt{5}$"),
 ("Számítsd ki! "
  "$\\left(\\dfrac{27}{8}\\right)^{-\\frac{1}{3}}+\\left(\\dfrac{1}{16}\\right)^{-\\frac{3}{4}}$",
  None, "$\\dfrac{26}{3}$"),
]

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
 '    <h2 id="gyak-ellenorzo">📝 Gyakorló ellenőrző</h2>\n    ' + DISZKLEMER +
 '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYE_ORAI, "gye") +
 '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYE_OTTHON, "gyeh"),
]

ut = oldal(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
           fajl="feladatok-gyokvonas.html", cim="Gyökvonás",
           temakor="Hatványozás, gyökvonás, komplex számok",
           alcim="Gyökvonás és azonosságai, műveletek gyökös kifejezésekkel, gyöktelenítés és "
                 "racionális kitevőjű hatvány — a végén gyakorló ellenőrzővel. A végeredmény "
                 "minden feladatnál lenyitható; előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-gyoktelenites-es-racionalis-kitevo.html",
           prevc="Gyöktelenítés és racionális kitevő",
           nxt="tananyag-komplex-szam-fogalma.html", nxtc="A komplex szám fogalma")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYE_ORAI), "+", len(GYE_OTTHON))
