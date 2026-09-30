# -*- coding: utf-8 -*-
"""2e/03 — A altema feladatgyujtemeny: exponencialis fuggveny, egyenletek,
egyenlotlensegek. + gyakorlo ELLENORZO (3. ellenorzo = csak exponencialis)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, solve, simplify, sqrt, Eq
x, t = symbols('x t', real=True)
def S(e): return sorted(solve(e, x))
def T(e): return sorted(solve(e, t))
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, (list, tuple)) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 # --- ALAP
 ("A5a", R(2)**-4, R(1, 16)), ("A5b", R(1, 3)**-2, 9),
 ("A5c", R(5)**0, 1), ("A5d", R(16)**R(1, 2), 4),
 ("A7a", S(x - 5), [5]), ("A7b", S(x - 4), [4]), ("A7c", S(x + 2), [-2]),
 ("A8a", S(3*x - 6), [2]), ("A8b", S(2*x - 4), [2]), ("A8c", S(x + 1 - 2), [1]),
 ("A9a", S(2*x - 3), [R(3, 2)]), ("A9b", S(2*x - 3), [R(3, 2)]),
 ("A9c", S(3*x + 2), [R(-2, 3)]),
 ("A10a", S(x**2 - 3*x - 4), [-1, 4]), ("A10b", S(x**2 - 4), [-2, 2]),
 ("A11a", S(-x - 3), [-3]), ("A11b", S(-x + 4), [4]),
 ("A12a", 2**3*(2 + 1), 24), ("A12a2", S(x - 3), [3]),
 ("A12b", 3**3*(3 - 1), 54), ("A12b2", S(x - 3), [3]),
 ("A13a", 5**1*(25 - 1), 120), ("A13b", 2**2*(8 + 2), 40),
 ("A14", T(t**2 - 5*t + 4), [1, 4]),
 ("A15a", S(x - 4), [4]), ("A15b", S(x - 3), [3]),
 ("A16a", S(x + 1 - 3), [2]), ("A16b", S(2*x - 3), [R(3, 2)]),
 ("A17a", S(x + 2), [-2]), ("A17b", S(x + 2), [-2]),
 ("A18a", S(x - 1 - 3), [4]), ("A18b", S(2*x - 2), [1]),
 ("A19", S(3*x - 1 + 2), [R(-1, 3)]),
 # --- KÖZÉP
 ("K4a", S(3*x - 6), [2]), ("K4b", S(3*x - 2 - 3), [R(5, 3)]),
 ("K5", S(2*x + 6), [-3]), ("K5e", simplify(R(9, 4)**3 - R(2, 3)**-6), 0),
 ("K6", T(t**2 - 6*t + 8), [2, 4]),
 ("K7", T(t**2 - 4*t + 3), [1, 3]),
 ("K8", T(t**2 - 6*t + 5), [1, 5]),
 ("K9", T(t**2 + t - 2), [-2, 1]),
 ("K10", T(3*t**2 - 10*t + 3), [R(1, 3), 3]),
 ("K11", S(x**2 - 5*x + 6), [2, 3]),
 ("K12", T(t**2 - 8*t + 16), [4]),
 ("K13", S(x**2 - 3*x - 4), [-1, 4]),
 ("K14", S(x**2 - 4), [-2, 2]),
 # --- NEHÉZ
 ("N1", T(t**2 - 6*t + 8), [2, 4]),
 ("N2", T(t**2 + 3*t - 4), [-4, 1]),
 ("N3", T(2*t**2 - 9*t + 4), [R(1, 2), 4]),
 ("N4", T(t**2 - 10*t + 9), [1, 9]),
 ("N5", T(t**2 - 5*t + 4), [1, 4]),
 ("N6", S(x - 6), [6]),
 # --- JOKER
 ("J", sorted(solve(x**2 - x - 1, x)), [R(1, 2) - sqrt(5)/2, R(1, 2) + sqrt(5)/2]),
 # --- gyakorló ellenőrző
 ("GO1a", R(2)**-2, R(1, 4)), ("GO1b", R(1, 5)**-1, 5),
 ("GO1c", R(3, 4)**0, 1), ("GO1d", R(25)**R(1, 2), 5),
 ("GO3", S(2*x + 6), [-3]), ("GO3e", simplify(R(16, 9)**3 - R(3, 4)**-6), 0),
 ("GO4", S(x**2 - 7*x + 12), [3, 4]),
 ("GO5", 5**2*(25 - 1), 600), ("GO5x", S(x - 2), [2]),
 ("GO6", S(4*x + 2 - 3), [R(1, 4)]),
 ("GO7", S(3*x - 1 - 3), [R(4, 3)]),
 ("GO8", T(t**2 - 6*t + 5), [1, 5]),
 ("GH1a", R(4)**-2, R(1, 16)), ("GH1b", R(2, 7)**0, 1),
 ("GH1c", R(1, 2)**-4, 16), ("GH1d", R(36)**R(1, 2), 6),
 ("GH3a", S(5*x - 5), [1]), ("GH3b", S(2*x + 4), [-2]),
 ("GH4", 2**3*(8 + 1), 72), ("GH4x", S(x - 3), [3]),
 ("GH5", S(x + 1 - 2), [1]),
 ("GH6", T(t**2 - 10*t + 16), [2, 8]),
]
for n, g, w in P:
    chk(n, g, w)
assert not E, E
print("sympy önteszt: OK —", len(P), "assert")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Ábrázold közös koordináta-rendszerben!",
  ["$y=2^{x}$", "$y=\\left(\\tfrac13\\right)^{x}$"],
  ["Növekvő görbe, áthalad a $(0;1)$ ponton, aszimptota az $x$-tengely.",
   "Csökkenő görbe, áthalad a $(0;1)$ ponton, aszimptota az $x$-tengely."], True),
 ("Ábrázold! (Add meg az aszimptotát is.)",
  ["$y=3^{x}+2$", "$y=2^{x}-4$"],
  ["Az $y=3^{x}$ görbe $2$-vel feljebb; aszimptota: $y=2$.",
   "Az $y=2^{x}$ görbe $4$-gyel lejjebb; aszimptota: $y=-4$."], True),
 ("Ábrázold!",
  ["$y=2^{x-1}$", "$y=3^{x+2}$"],
  ["Az $y=2^{x}$ görbe $1$ egységgel <b>jobbra</b> tolva.",
   "Az $y=3^{x}$ görbe $2$ egységgel <b>balra</b> tolva."], True),
 ("Add meg az értelmezési tartományt és az értékkészletet!",
  ["$y=5^{x}$", "$y=\\left(\\tfrac12\\right)^{x}+3$"],
  ["ÉT: $\\mathbb{R}$, ÉK: $(0;+\\infty)$.",
   "ÉT: $\\mathbb{R}$, ÉK: $(3;+\\infty)$."], True),
 ("Számold ki!",
  ["$2^{-4}$", "$\\left(\\tfrac13\\right)^{-2}$", "$5^{0}$", "$16^{0,5}$"],
  ["$\\dfrac{1}{16}$", "$9$", "$1$", "$4$"], True),
 ("Melyik a nagyobb? Indokold a monotonitással!",
  ["$2^{5}$ vagy $2^{3}$", "$\\left(\\tfrac12\\right)^{5}$ vagy $\\left(\\tfrac12\\right)^{3}$"],
  ['$2^{5}=32$ a nagyobb; a $2^{x}$ növekvő.', '$\\left(\\tfrac12\\right)^{3}=\\tfrac18$ a nagyobb; a $\\left(\\tfrac12\\right)^{x}$ csökkenő.'], True),
 ("Oldd meg!", ["$2^{x}=32$", "$3^{x}=81$", "$5^{x}=\\tfrac{1}{25}$"],
  ["$x=5$", "$x=4$", "$x=-2$"], True),
 ("Oldd meg!", ["$2^{3x}=64$", "$3^{2x}=81$", "$7^{x+1}=49$"],
  ["$x=2$", "$x=2$", "$x=1$"], True),
 ("Oldd meg! (Az alapok itt nem azonosak — hozd közös alapra!)",
  ["$4^{x}=8$", "$9^{x}=27$", "$8^{x}=\\tfrac14$"],
  ["$x=\\dfrac32$", "$x=\\dfrac32$", "$x=-\\dfrac23$"], True),
 ("Oldd meg!", ["$2^{x^{2}-3x}=16$", "$3^{x^{2}-4}=1$"],
  ["$x_{1}=-1$, $x_{2}=4$", "$x_{1,2}=\\pm 2$"], True),
 ("Oldd meg!", ["$\\left(\\tfrac12\\right)^{x}=8$", "$\\left(\\tfrac13\\right)^{x}=\\tfrac{1}{81}$"],
  ["$x=-3$", "$x=4$"], True),
 ("Oldd meg kiemeléssel!", ["$2^{x+1}+2^{x}=24$", "$3^{x+1}-3^{x}=54$"],
  ['$x=3$', '$x=3$'], True),
 ("Oldd meg kiemeléssel!", ["$5^{x+2}-5^{x}=120$", "$2^{x+3}+2^{x+1}=40$"],
  ['$x=1$', '$x=2$'], True),
 ("Oldd meg a $t=2^{x}$ helyettesítéssel! $4^{x}-5\\cdot 2^{x}+4=0$", None,
  '$x_{1}=0$, $x_{2}=2$.'),
 ("Oldd meg!", ["$2^{x}&lt;16$", "$3^{x}&gt;27$"],
  ["$x\\in(-\\infty;4)$", "$x\\in(3;+\\infty)$"], True),
 ("Oldd meg!", ["$2^{x+1}\\le 8$", "$5^{2x}\\ge 125$"],
  ["$x\\in(-\\infty;2]$", "$x\\in\\left[\\tfrac32;+\\infty\\right)$"], True),
 ("Oldd meg! (Figyelj az alapra!)",
  ["$\\left(\\tfrac12\\right)^{x}&gt;4$", "$\\left(\\tfrac13\\right)^{x}\\le 9$"],
  ["A jel fordul: $x\\in(-\\infty;-2)$", "A jel fordul: $x\\in[-2;+\\infty)$"], True),
 ("Oldd meg!",
  ["$\\left(\\tfrac12\\right)^{x-1}\\ge\\tfrac18$", "$\\left(\\tfrac15\\right)^{2x}&lt;\\tfrac{1}{25}$"],
  ['$x\\in(-\\infty;4]$', '$x\\in(1;+\\infty)$'], True),
 ("Oldd meg! $2^{3x-1}\\ge\\tfrac14$", None,
  '$x\\in\\left[-\\tfrac13;+\\infty\\right)$.'),
 ("Válaszolj, és indokolj az értékkészlettel!",
  ["Lehet-e $2^{x}=0$?", "Lehet-e $3^{x}=-9$?", "Igaz-e, hogy $5^{x}&gt;0$ minden $x$-re?"],
  ["Nem — az exponenciális függvény értéke sosem nulla.",
   "Nem — az érték mindig pozitív.",
   "Igen, ez épp az értékkészlet: $(0;+\\infty)$."], True),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Ábrázold, és jellemezd (ÉT, ÉK, aszimptota, monotonitás)! $y=2^{x-1}+3$", None,
  'ÉT: $\\mathbb{R}$; ÉK: $(3;+\\infty)$; aszimptota: $y=3$; szigorúan növekvő; az $y=2^x$ görbe $1$-gyel jobbra és $3$-mal feljebb tolva.'),
 ("Ábrázold közös koordináta-rendszerben, és mondd meg, milyen kapcsolat van közöttük!",
  ["$y=2^{x}$ és $y=-2^{x}$", "$y=2^{x}$ és $y=2^{-x}$"],
  ["Az $x$-tengelyre tükrösek.",
   "Az $y$-tengelyre tükrösek — és $2^{-x}=\\left(\\tfrac12\\right)^{x}$."], True),
 ("Egy exponenciális függvény grafikonja átmegy a $(0;1)$ és a $(2;9)$ ponton. "
  "Mi a függvény hozzárendelési szabálya?", None,
  '$y=3^{x}$.'),
 ("Oldd meg!", ["$2^{x}\\cdot 4^{x}=64$", "$3^{x}\\cdot 9^{x-1}=27$"],
  ['$x=2$', '$x=\\dfrac53$'], True),
 ("Oldd meg! $\\left(\\tfrac23\\right)^{2x}=\\left(\\tfrac94\\right)^{3}$", None,
  '$x=-3$.'),
 ("Oldd meg helyettesítéssel! $2^{2x}-6\\cdot 2^{x}+8=0$", None,
  '$x_{1}=1$, $x_{2}=2$.'),
 ("Oldd meg! $9^{x}-4\\cdot 3^{x}+3=0$", None,
  '$x_{1}=0$, $x_{2}=1$.'),
 ("Oldd meg! $25^{x}-6\\cdot 5^{x}+5=0$", None,
  '$x_{1}=0$, $x_{2}=1$.'),
 ("Oldd meg! $4^{x}+2^{x}-2=0$", None,
  '$x=0$.'),
 ("Oldd meg! $3^{2x+1}-10\\cdot 3^{x}+3=0$", None,
  '$x_{1}=-1$, $x_{2}=1$.'),
 ("Oldd meg! $2^{x^{2}-5x+6}=1$", None,
  '$x_{1}=2$, $x_{2}=3$.'),
 ("Oldd meg! $4^{x}-2^{x+3}+16=0$", None,
  '$x=2$.'),
 ("Oldd meg! $2^{x^{2}-3x}&lt;16$", None,
  '$x\\in(-1;4)$.'),
 ("Oldd meg! $\\left(\\tfrac13\\right)^{x^{2}-4}\\ge 1$", None,
  '$x\\in[-2;2]$.'),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Oldd meg! $4^{x}-3\\cdot 2^{x+1}+8=0$", None,
  '$x_{1}=1$, $x_{2}=2$.'),
 ("Oldd meg! $9^{x}+3^{x+1}-4=0$", None,
  '$x=0$.'),
 ("Oldd meg! $2^{2x+1}-9\\cdot 2^{x}+4=0$", None,
  '$x_{1}=-1$, $x_{2}=2$.'),
 ("Oldd meg! $3^{x}+3^{2-x}=10$", None,
  '$x_{1}=0$, $x_{2}=2$.'),
 ("Oldd meg! $4^{x}-5\\cdot 2^{x}+4&lt;0$", None,
  '$x\\in(0;2)$.'),
 ("Egy baktériumtelep óránként megkétszereződik. Hány óra alatt lesz "
  "<b>64-szeres</b> a telep? Írd fel a modellt is!", None,
  '$N(t)=N_{0}\\cdot 2^{t}$; $t=6$ óra.'),
]

JOKER = ("Oldd meg! $2^{x}\\cdot 3^{x}=6^{x^{2}-1}$",
         '$x_{1,2}=\\dfrac{1\\pm\\sqrt5}{2}$.')

# ============================== GYAKORLÓ ELLENŐRZŐ ==============================

GYE_ORAI = [
 ("Számold ki!",
  ["$2^{-2}$", "$\\left(\\tfrac15\\right)^{-1}$", "$\\left(\\tfrac34\\right)^{0}$", "$25^{0,5}$"],
  ["$\\dfrac14$", "$5$", "$1$", "$5$"], True),
 ("Ábrázold a függvényt!", ["$y=2^{x}+1$", "$y=\\left(\\tfrac13\\right)^{x}$"],
  ["Az $y=2^{x}$ görbe $1$-gyel feljebb; aszimptota: $y=1$.",
   "Csökkenő görbe a $(0;1)$ ponton át; aszimptota az $x$-tengely."], True),
 ("Oldd meg! $\\left(\\tfrac34\\right)^{2x}=\\left(\\tfrac{16}{9}\\right)^{3}$", None,
  '$x=-3$.'),
 ("Oldd meg! $2^{x^{2}-7x+12}=1$", None,
  '$x_{1}=3$, $x_{2}=4$.'),
 ("Oldd meg! $5^{x+2}-5^{x}=600$", None,
  '$x=2$.'),
 ("Oldd meg! $3^{4x+2}\\ge 27$", None,
  '$x\\in\\left[\\tfrac14;+\\infty\\right)$.'),
 ("Oldd meg! $\\left(\\tfrac12\\right)^{3x-1}&gt;\\tfrac18$", None,
  '$x\\in\\left(-\\infty;\\tfrac43\\right)$.'),
 ("★ Oldd meg! $25^{x}-6\\cdot 5^{x}+5=0$", None,
  '$x_{1}=0$, $x_{2}=1$.'),
]

GYE_OTTHON = [
 ("Számold ki!",
  ["$4^{-2}$", "$\\left(\\tfrac27\\right)^{0}$", "$\\left(\\tfrac12\\right)^{-4}$", "$36^{0,5}$"],
  ["$\\dfrac{1}{16}$", "$1$", "$16$", "$6$"], True),
 ("Ábrázold a függvényt!", ["$y=3^{x-1}$", "$y=\\left(\\tfrac12\\right)^{x}-2$"],
  ["Az $y=3^{x}$ görbe $1$-gyel jobbra.",
   "A csökkenő görbe $2$-vel lejjebb; aszimptota: $y=-2$."], True),
 ("Oldd meg!", ["$2^{5x}=32$", "$9^{x}=\\tfrac{1}{81}$"], ["$x=1$", "$x=-2$"], True),
 ("Oldd meg! $2^{x+3}+2^{x}=72$", None,
  '$x=3$.'),
 ("Oldd meg! $\\left(\\tfrac14\\right)^{x+1}\\le\\tfrac{1}{16}$", None,
  '$x\\in[1;+\\infty)$.'),
 ("★ Oldd meg! $4^{x}-10\\cdot 2^{x}+16=0$", None,
  '$x_{1}=1$, $x_{2}=3$.'),
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

ut = oldal(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
           fajl="feladatok-exponencialis.html", cim="Exponenciális függvény",
           temakor="Exponenciális és logaritmusfüggvény",
           alcim="Grafikonok és transzformációk, közös alapra hozás, kiemelés, "
                 "helyettesítéses egyenletek és egyenlőtlenségek — a végén gyakorló "
                 "ellenőrzővel. A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-exponencialis-egyenlotlensegek.html",
           prevc="Exponenciális egyenlőtlenségek",
           nxt="tananyag-logaritmus-fogalma.html", nxtc="A logaritmus fogalma")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYE_ORAI), "+", len(GYE_OTTHON))
