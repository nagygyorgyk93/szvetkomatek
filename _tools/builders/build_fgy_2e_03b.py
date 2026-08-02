# -*- coding: utf-8 -*-
"""2e/03 — B altema feladatgyujtemeny: a logaritmus fogalma, azonossagai,
attetes mas alapra es alkalmazasok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, log, N, solve, simplify, sqrt, floor, Integer
x = symbols('x', positive=True)
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        if abs(float(g) - w) > tol:
            E.append((n, float(g), w))
    elif (g != w) if isinstance(w, (list, tuple)) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 ("A3a", log(16, 2), 4), ("A3b", log(27, 3), 3),
 ("A3c", log(125, 5), 3), ("A3d", log(1000, 10), 3),
 ("A4a", log(R(1, 8), 2), -3), ("A4b", log(R(1, 81), 3), -4),
 ("A4c", log(R(1, 100), 10), -2),
 ("A5a", log(2, 4), R(1, 2)), ("A5b", log(3, 9), R(1, 2)), ("A5c", log(2, 8), R(1, 3)),
 ("A6a", log(8, R(1, 2)), -3), ("A6b", log(9, R(1, 3)), -2),
 ("A7a", log(1, 7), 0), ("A7b", log(6, 6), 1), ("A7c", log(32, 2), 5),
 ("A8a", log(12, 2) - log(3, 2), 2), ("A8b", log(2, 10) + log(5, 10), 1),
 ("A9a", log(50, 10) + log(2, 10), 2), ("A9b", log(40, 2) - log(5, 2), 3),
 ("A10a", log(sqrt(3), 3), R(1, 2)), ("A10b", log(4**R(1, 3), 2), R(2, 3)),
 ("A11a", 2*log(5, 5), 2), ("A11b", 3*log(4, 2), 6), ("A11c", R(1, 2)*log(81, 3), 2),
 ("A17a", N(log(10, 2)), 3.32192809489, 1e-9),
 ("A17b", N(log(20, 3)), 2.72683302786, 1e-9),
 ("K1", log(48, 2) - log(3, 2), 4),
 ("K2", log(4, 6) + log(9, 6), 2),
 ("K3", log(25, 10) + 2*log(2, 10), 2),
 ("K5", log(9**R(1, 3), 3), R(2, 3)),
 ("K7a", solve(x - 32, x), [32]), ("K7b", R(1, 9), R(1, 9)),
 ("K8", log(32, 4), R(5, 2)),
 ("K9", log(8, sqrt(2)), 6),
 ("K11", log(4, 10) + log(250, 10), 3),
 ("K12", 10*log(100, 10), 20),
 ("K13", -log(R(1, 100000), 10), 5),
 ("K14", N(log(2)/log(R(108, 100))), 9.006468342, 1e-8),
 ("N1", log(3, 2)*log(4, 3)*log(8, 4), 3),
 ("N2a", 2*R(3010, 10000) + R(4771, 10000), R(10791, 10000)),
 ("N2b", R(4771, 10000) - R(3010, 10000), R(1761, 10000)),
 ("N3", floor(100*N(log(2, 10), 20)) + 1, 31),
 ("N4", log(32, R(1, 2)) + log(R(1, 32), 2), -10),
 ("N5", sorted(solve(x**2 - 2*x - 8, x)), [4]),
 ("N6", log(R(1, 8), R(1, 2)), 3),
 ("J", log(64, 2), 6),
]
for it in P:
    chk(*it)
assert not E, E
print("sympy önteszt: OK —", len(P), "assert")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Írd át hatványalakba!",
  ["$\\log_{2}8=3$", "$\\log_{5}25=2$", "$\\log_{3}\\tfrac19=-2$"],
  ["$2^{3}=8$", "$5^{2}=25$", "$3^{-2}=\\dfrac19$"], True),
 ("Írd át logaritmus alakba!",
  ["$2^{4}=16$", "$10^{3}=1000$", "$5^{-1}=\\tfrac15$"],
  ["$\\log_{2}16=4$", "$\\lg 1000=3$", "$\\log_{5}\\tfrac15=-1$"], True),
 ("Számold ki a definíció alapján!",
  ["$\\log_{2}16$", "$\\log_{3}27$", "$\\log_{5}125$", "$\\lg 1000$"],
  ["$4$", "$3$", "$3$", "$3$"], True),
 ("Számold ki!",
  ["$\\log_{2}\\tfrac18$", "$\\log_{3}\\tfrac{1}{81}$", "$\\lg 0{,}01$"],
  ["$-3$", "$-4$", "$-2$"], True),
 ("Számold ki! (A válasz törtszám lesz.)",
  ["$\\log_{4}2$", "$\\log_{9}3$", "$\\log_{8}2$"],
  ["$\\dfrac12$", "$\\dfrac12$", "$\\dfrac13$"], True),
 ("Számold ki! (Az alap kisebb $1$-nél.)",
  ["$\\log_{\\frac12}8$", "$\\log_{\\frac13}9$"], ["$-3$", "$-2$"], True),
 ("Számold ki fejben, az alapösszefüggések alapján!",
  ["$\\log_{7}1$", "$\\log_{6}6$", "$\\log_{2}2^{5}$", "$3^{\\log_{3}7}$"],
  ["$0$", "$1$", "$5$", "$7$"], True),
 ("Vond össze, majd számold ki!",
  ["$\\log_{2}12-\\log_{2}3$", "$\\lg 2+\\lg 5$"],
  ["$\\log_{2}4=2$", "$\\lg 10=1$"], True),
 ("Számold ki!", ["$\\lg 50+\\lg 2$", "$\\log_{2}40-\\log_{2}5$"],
  ["$\\lg 100=2$", "$\\log_{2}8=3$"], True),
 ("Számold ki! (Írd a gyököt hatványalakba.)",
  ["$\\log_{3}\\sqrt3$", "$\\log_{2}\\sqrt[3]{4}$"],
  ["$\\dfrac12$", "$\\dfrac23$"], True),
 ("Számold ki!",
  ["$2\\log_{5}5$", "$3\\log_{2}4$", "$\\tfrac12\\log_{3}81$"],
  ["$2$", "$6$", "$2$"], True),
 ("Bontsd fel az azonosságok segítségével!",
  ["$\\log_{a}(xy)$", "$\\log_{a}\\dfrac{x}{y}$", "$\\log_{a}x^{5}$"],
  ["$\\log_{a}x+\\log_{a}y$", "$\\log_{a}x-\\log_{a}y$", "$5\\log_{a}x$"], True),
 ("Bontsd fel! $\\log_{a}\\dfrac{x^{2}y^{3}}{z}$", None,
  "$2\\log_{a}x+3\\log_{a}y-\\log_{a}z$"),
 ("Vond össze egyetlen logaritmussá! $\\log_{a}x+\\log_{a}y-\\log_{a}z$", None,
  "$\\log_{a}\\dfrac{xy}{z}$"),
 ("Vond össze egyetlen logaritmussá! $3\\log_{a}x-2\\log_{a}y$", None,
  "$\\log_{a}\\dfrac{x^{3}}{y^{2}}$"),
 ("Írd fel tizes alapú logaritmusokkal (áttérés más alapra)!",
  ["$\\log_{2}7$", "$\\log_{5}12$"],
  ["$\\dfrac{\\lg 7}{\\lg 2}$", "$\\dfrac{\\lg 12}{\\lg 5}$"], True),
 ("Számold ki számológéppel, négy tizedesre kerekítve!",
  ["$\\log_{2}10$", "$\\log_{3}20$"],
  ["$\\approx 3{,}3219$", "$\\approx 2{,}7268$"], True),
 ("Igaz vagy hamis? Indokold!",
  ["$\\lg(3+4)=\\lg 3+\\lg 4$", "$\\lg(3\\cdot 4)=\\lg 3+\\lg 4$",
   "$\\log_{2}(-8)=-3$"],
  ["<b>Hamis</b> — a logaritmusnak az összeadásról nincs mondanivalója.",
   "<b>Igaz</b> — ez a szorzatra vonatkozó azonosság.",
   "<b>Hamis</b> — negatív szám logaritmusa nem létezik."], True),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Számold ki! $\\log_{2}48-\\log_{2}3$", None, "$\\log_{2}16=4$"),
 ("Számold ki! $\\log_{6}4+\\log_{6}9$", None, "$\\log_{6}36=2$"),
 ("Számold ki! $\\lg 25+2\\lg 2$", None,
  "$2\\lg 2=\\lg 4$, tehát $\\lg 25+\\lg 4=\\lg 100=2$"),
 ("Legyen $\\lg 2=a$. Fejezd ki $a$-val!",
  ["$\\lg 5$", "$\\lg 20$", "$\\lg 50$"],
  ["$\\lg\\tfrac{10}{2}=1-a$", "$\\lg(2\\cdot 10)=1+a$", "$\\lg\\tfrac{100}{2}=2-a$"], True),
 ("Számold ki! $\\log_{3}\\sqrt[3]{9}$", None,
  "$\\sqrt[3]{9}=3^{2/3}$, tehát az érték $\\dfrac23$."),
 ("Számold ki!", ["$5^{\\log_{5}12}$", "$2^{\\log_{2}3+1}$"],
  ["$12$ — a logaritmus és a hatványozás kioltják egymást.",
   "$2^{\\log_{2}3}\\cdot 2=3\\cdot 2=6$"], True),
 ("Oldd meg!", ["$\\log_{2}x=5$", "$\\log_{3}x=-2$"],
  ["$x=2^{5}=32$", "$x=3^{-2}=\\dfrac19$"], True),
 ("Számold ki! $\\log_{4}32$", None,
  "Közös alap a $2$: $\\dfrac{\\log_{2}32}{\\log_{2}4}=\\dfrac{5}{2}$."),
 ("Számold ki! $\\log_{\\sqrt2}8$", None,
  "$\\sqrt2=2^{1/2}$ és $8=2^{3}$, tehát $\\dfrac{3}{1/2}=6$."),
 ("Igazold, hogy $\\log_{a}b\\cdot\\log_{b}a=1$!", None,
  "Áttéréssel $\\log_{b}a=\\dfrac{\\lg a}{\\lg b}$ és $\\log_{a}b=\\dfrac{\\lg b}{\\lg a}$; "
  "a szorzatuk $1$. (Feltétel: $a,b&gt;0$ és egyik sem $1$.)"),
 ("Számold ki! $\\lg 4+\\lg 250$", None, "$\\lg 1000=3$"),
 ("Egy hangforrás intenzitása a százszorosára nő. Hány decibellel nő a hangerő, "
  "ha $L=10\\lg\\dfrac{I}{I_{0}}$?", None,
  "$10\\lg 100=10\\cdot 2=20$ dB-lel."),
 ("Egy oldat hidrogénion-koncentrációja $[\\mathrm{H}^{+}]=10^{-5}$. Mennyi a pH-ja, "
  "ha $\\mathrm{pH}=-\\lg[\\mathrm{H}^{+}]$? És mennyi lesz, ha az oldat "
  "<b>százszor savasabb</b> lesz?", None,
  "$\\mathrm{pH}=5$. Százszor savasabb: $[\\mathrm{H}^{+}]=10^{-3}$, tehát "
  "$\\mathrm{pH}=3$ — a pH <b>kettővel csökken</b>."),
 ("Egy befektetés évi $8\\%$-kal gyarapszik. Hány év alatt duplázódik meg?", None,
  "$1{,}08^{n}=2$, tehát $n=\\dfrac{\\lg 2}{\\lg 1{,}08}\\approx 9{,}01$ — "
  "a <b>10. év</b> folyamán éri el a kétszeresét."),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Számold ki! $\\log_{2}3\\cdot\\log_{3}4\\cdot\\log_{4}8$", None,
  "Áttéréssel minden tényező tizes alapra írható, és a tört „teleszkopikusan” "
  "kiesik: $\\dfrac{\\lg 3}{\\lg 2}\\cdot\\dfrac{\\lg 4}{\\lg 3}\\cdot"
  "\\dfrac{\\lg 8}{\\lg 4}=\\dfrac{\\lg 8}{\\lg 2}=\\log_{2}8=3$."),
 ("Tudjuk, hogy $\\lg 2\\approx 0{,}3010$ és $\\lg 3\\approx 0{,}4771$. "
  "Számold ki <b>táblázat nélkül</b>!",
  ["$\\lg 12$", "$\\lg 1{,}5$"],
  ["$\\lg(4\\cdot 3)=2\\lg 2+\\lg 3\\approx 1{,}0791$",
   "$\\lg\\tfrac32=\\lg 3-\\lg 2\\approx 0{,}1761$"], True),
 ("Hány jegyű a $2^{100}$ szám a tízes számrendszerben? "
  "($\\lg 2\\approx 0{,}30103$)", None,
  "$\\lg 2^{100}=100\\lg 2\\approx 30{,}103$, tehát $10^{30}&lt;2^{100}&lt;10^{31}$: "
  "a szám <b>31 jegyű</b>."),
 ("Számold ki! $\\log_{\\frac12}32+\\log_{2}\\tfrac{1}{32}$", None,
  "$-5+(-5)=-10$."),
 ("Oldd meg! $\\log_{2}x+\\log_{2}(x-2)=3$", None,
  "ÉT: $x&gt;2$. Összevonva $\\log_{2}\\big(x(x-2)\\big)=3$, tehát $x^{2}-2x=8$, "
  "azaz $x^{2}-2x-8=0$: $x_{1}=4$, $x_{2}=-2$. Az ÉT miatt csak $x=4$ jó."),
 ("Egy radioaktív anyag felezési ideje $5$ nap. Hány nap alatt csökken a mennyisége "
  "a <b>nyolcadára</b>?", None,
  "A modell $\\left(\\tfrac12\\right)^{t/5}=\\tfrac18=\\left(\\tfrac12\\right)^{3}$, "
  "tehát $\\dfrac{t}{5}=3$ és $t=15$ nap."),
]

JOKER = ("Számold ki! $\\log_{2}3\\cdot\\log_{3}4\\cdot\\log_{4}5\\cdot\\ldots"
         "\\cdot\\log_{63}64$",
         "Írd át minden tényezőt tizes alapra: $\\dfrac{\\lg 3}{\\lg 2}\\cdot"
         "\\dfrac{\\lg 4}{\\lg 3}\\cdot\\ldots\\cdot\\dfrac{\\lg 64}{\\lg 63}$. "
         "Minden számláló kiesik a következő nevezővel, marad "
         "$\\dfrac{\\lg 64}{\\lg 2}=\\log_{2}64=\\boxed{6}$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
           fajl="feladatok-logaritmus.html", cim="A logaritmus",
           temakor="Exponenciális és logaritmusfüggvény",
           alcim="Definíció szerinti számolás, az azonosságok mindkét irányban, "
                 "áttérés más alapra és logaritmikus skálák. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-attetes-mas-alapra.html", prevc="Áttérés más alapra és alkalmazások",
           nxt="tananyag-inverz-es-logaritmusfuggveny.html",
           nxtc="Az inverz függvény és a logaritmusfüggvény")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
