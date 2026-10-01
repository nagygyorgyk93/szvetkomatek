# -*- coding: utf-8 -*-
"""2e/03 — C altema feladatgyujtemeny: a logaritmusfuggveny, logaritmusos egyenletek
es egyenlotlensegek. + gyakorlo DOLGOZAT (a teljes temakor: exp + log)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, log, N, solve, simplify, sqrt
x, t = symbols('x t', real=True)
def S(e): return sorted(solve(e, x))
def T(e): return sorted(solve(e, t))
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        if abs(float(g) - w) > tol:
            E.append((n, float(g), w))
    elif (g != w) if isinstance(w, (list, tuple)) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 # --- ALAP
 ("A5a", S(x - 4 - 1), [5]), ("A5b", S(x - 8), [8]),
 ("A7a", 2**4, 16), ("A7b", R(3)**-1, R(1, 3)),
 ("A8a", S(x - 1 - 8), [9]), ("A8b", S(2*x + 3 - 25), [11]),
 ("A9a", S(3*x - 1 - (x + 7)), [4]), ("A9b", S(5*x - 2 - (2*x + 7)), [3]),
 ("A10", S(x**2 - 3*x - 4), [-1, 4]),
 ("A10et1", (-1)**2 - 3*(-1), 4), ("A10et2", 4**2 - 3*4, 4),
 ("A11", S(4*x - 32), [8]),
 ("A12a", S(x - 8), [8]), ("A12b", S(x - 9), [9]),
 ("A13a", S(x - 1 - 4), [5]), ("A13b", S(x + 2 - 5), [3]),
 ("A14", S(4*x - 1), [R(1, 4)]),
 # --- KÖZÉP
 ("K1", S(x + 3 - 2), [-1]),
 ("K3", S(x**2 - 7), [-sqrt(7), sqrt(7)]),
 ("K4", S(x**2 - 2*x - 8), [-2, 4]),
 ("K5", S(x + 1 - 2*(x - 1)), [3]),
 ("K6", T(t**2 - 3*t + 2), [1, 2]),
 ("K7", T(t**2 - 2*t + 1), [1]),
 ("K8", S(x - 1 - (2*x - 5)), [4]),
 ("K9", S(x**2 - 5*x + 6), [2, 3]),
 ("K10", S(2*x - 1 - 9), [5]),
 ("K11", S(x**2 - 3*x - 4), [-1, 4]),
 ("K12", S(x + 2 - 3), [1]),
 # --- NEHÉZ
 ("N1", T(t**2 - 2*t - 3), [-1, 3]),
 ("N2", S(x**2 - 3*x), [0, 3]),
 ("N3", S(x**2 - 4), [-2, 2]),
 ("N4", S(3**x - 9), [2]), ("N4e", 3**2 - 6, 3),
 ("N5", S(3*x + 1 - (9 - x)), [2]),
 ("N6", S(3 - x), [3]),
 # --- JOKER
 ("J", T(t**2 - t - 2), [-1, 2]),
 # --- gyakorló dolgozat (órai)
 ("GO1a", log(64, 2), 6), ("GO1b", 4**3 - 3*log(32, 2), 49),
 ("GO1c", log(108, 6) - log(3, 6), 2),
 ("GO3a", S(2*x + 4), [-2]), ("GO3b", S(6*x - 18), [3]),
 ("GO3c", S(3*x - 2 - 16), [6]),
 ("GO3d", 7*(49 - 1), 336), ("GO3dx", S(x - 1), [1]),
 ("GO4a", S(2*x + 7 - 4), [R(-3, 2)]),
 ("GO4b", S(3*x - 1 - (x + 5)), [3]), ("GO4bet", S(3*x - 1), [R(1, 3)]),
 ("GO5", sorted(solve(2*x**2 - 9*x - 5, x)), [R(-1, 2), 5]),
 # --- gyakorló dolgozat (otthoni)
 ("GH1a", log(243, 3), 5), ("GH1b", N(log(5, 2)), 2.32192809489, 1e-9),
 ("GH1c", log(20, 10) + log(5, 10), 2),
 ("GH3a", S(5*x - 9), [R(9, 5)]), ("GH3b", S(x - 3 - 16), [19]),
 ("GH4", T(t**2 - 6*t + 8), [2, 4]),
 ("GH5", S(2*x + 1 - 9), [4]),
 ("GH6", S(5 - 2*x), [R(5, 2)]),
]
for it in P:
    chk(*it)
assert not E, E
print("sympy önteszt: OK —", len(P), "assert")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Add meg az értelmezési tartományt!",
  ["$y=\\log_{2}(x-5)$", "$y=\\log_{3}(2x+6)$"],
  ['$x\\in(5;+\\infty)$', '$x\\in(-3;+\\infty)$'], True),
 ("Add meg az értelmezési tartományt!",
  ["$y=\\lg(4-x)$", "$y=\\log_{5}x^{2}$"],
  ['$x\\in(-\\infty;4)$', '$x\\in\\mathbb{R}\\setminus\\{0\\}$'], True),
 ("Ábrázold közös koordináta-rendszerben! Mi a kapcsolat a két görbe között?",
  ["$y=\\log_{2}x$", "$y=\\log_{\\frac12}x$"],
  ["Növekvő, az $(1;0)$ ponton át; aszimptota az $y$-tengely.",
   "Csökkenő, szintén az $(1;0)$ ponton át — a két görbe az $x$-tengelyre tükrös."], True),
 ("Ábrázold! (Add meg az aszimptotát is.)",
  ["$y=\\log_{2}(x-2)$", "$y=\\log_{2}x+1$"],
  ["$2$-vel jobbra tolva; aszimptota: $x=2$; ÉT: $x&gt;2$.",
   "$1$-gyel feljebb tolva; aszimptota az $y$-tengely; ÉT: $x&gt;0$."], True),
 ("Hol van a függvény nullahelye?",
  ["$y=\\log_{3}(x-4)$", "$y=\\log_{2}x-3$"],
  ['$x=5$', '$x=8$'], True),
 ("Írd fel a függvény inverzét!",
  ["$y=3^{x}$", "$y=\\log_{5}x$", "$y=\\left(\\tfrac12\\right)^{x}$"],
  ["$y=\\log_{3}x$", "$y=5^{x}$", "$y=\\log_{\\frac12}x$"], True),
 ("Oldd meg!", ["$\\log_{2}x=4$", "$\\log_{3}x=-1$"],
  ['$x=16$', '$x=\\dfrac13$'], True),
 ("Oldd meg! (Ne feledd az értelmezési tartományt.)",
  ["$\\log_{2}(x-1)=3$", "$\\log_{5}(2x+3)=2$"],
  ['$x=9$', '$x=11$'], True),
 ("Oldd meg!", ["$\\lg(3x-1)=\\lg(x+7)$", "$\\log_{2}(5x-2)=\\log_{2}(2x+7)$"],
  ['$x=4$', '$x=3$'], True),
 ("Oldd meg! $\\log_{4}(x^{2}-3x)=1$", None,
  '$x_{1}=-1$, $x_{2}=4$.'),
 ("Oldd meg! $\\log_{2}x+\\log_{2}4=5$", None,
  '$x=8$.'),
 ("Oldd meg!", ["$\\log_{2}x&lt;3$", "$\\log_{3}x&gt;2$"],
  ['$x\\in(0;8)$', '$x\\in(9;+\\infty)$'], True),
 ("Oldd meg!", ["$\\log_{2}(x-1)\\le 2$", "$\\log_{5}(x+2)\\ge 1$"],
  ['$x\\in(1;5]$', '$x\\in[3;+\\infty)$'], True),
 ("Oldd meg! $\\log_{\\frac12}x&gt;2$", None,
  "ÉT: $x&gt;0$. Az alap kisebb $1$-nél, a jel <b>fordul</b>: "
  "$x&lt;\\left(\\tfrac12\\right)^{2}=\\tfrac14$. A metszet: "
  "$x\\in\\left(0;\\tfrac14\\right)$."),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Ábrázold, és jellemezd (ÉT, aszimptota, nullahely, monotonitás)! "
  "$y=\\log_{2}(x+3)-1$", None,
  'ÉT: $(-3;+\\infty)$; aszimptota: $x=-3$; nullahely: $x=-1$; szigorúan növekvő; a $\\log_{2}x$ görbe $3$-mal balra és $1$-gyel lejjebb tolva.'),
 ("Az $y=2^{x}$ és az $y=\\log_{2}x$ grafikonja hogyan viszonyul egymáshoz? "
  "Mit tudsz mondani a metszéspontjaikról?", None,
  'Az $y=x$ egyenesre tükrösek; nincs közös pontjuk.'),
 ("Oldd meg! $\\log_{3}(x-2)+\\log_{3}(x+2)=1$", None,
  '$x=\\sqrt7\\approx 2{,}65$.'),
 ("Oldd meg! $\\lg(x-3)+\\lg(x+1)=\\lg 5$", None,
  '$x=4$.'),
 ("Oldd meg! $\\log_{2}(x+1)-\\log_{2}(x-1)=1$", None,
  '$x=3$.'),
 ("Oldd meg helyettesítéssel! $\\left(\\log_{2}x\\right)^{2}-3\\log_{2}x+2=0$", None,
  '$x_{1}=2$, $x_{2}=4$.'),
 ("Oldd meg! $\\log_{3}x+\\log_{x}3=2$", None,
  '$x=3$.'),
 ("Oldd meg! $\\log_{0,5}(x-1)&gt;\\log_{0,5}(2x-5)$", None,
  '$x\\in(4;+\\infty)$.'),
 ("Oldd meg! $\\log_{2}(x^{2}-5x+7)=0$", None,
  '$x_{1}=2$, $x_{2}=3$.'),
 ("Oldd meg! $\\log_{3}(2x-1)\\le 2$", None,
  '$x\\in\\left(\\tfrac12;5\\right]$.'),
 ("Oldd meg! $\\lg(x^{2}-4)&lt;\\lg(3x)$", None,
  '$x\\in(2;4)$.'),
 ("Oldd meg! $\\log_{\\frac13}(x+2)\\ge -1$", None,
  '$x\\in(-2;1]$.'),
 ('A logaritmus definíciójában kikötjük, hogy az alap pozitív és <b>nem</b> $1$. Nézzük meg, miért.',
  ['Próbáld megoldani az $1^{x}=8$ egyenletet! Mi történik?',
   'És az $1^{x}=1$ egyenletet?',
   'Fogalmazd meg egy mondatban, miért nem lehet a logaritmus alapja $1$.'],
  ['Nincs megoldás.', 'Minden $x\\in\\mathbb{R}$ megoldás.', 'Az 1-es alapnál a kitevő nem határozható meg egyértelműen.']),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Oldd meg! $\\lg^{2}x-\\lg(x^{2})-3=0$", None,
  '$x_{1}=1000$, $x_{2}=\\dfrac{1}{10}$.'),
 ("Oldd meg! $\\log_{2}(x-1)+\\log_{2}(x-2)=1$", None,
  '$x=3$.'),
 ("Oldd meg! $\\log_{x}4=2$", None,
  '$x=2$.'),
 ("Oldd meg! $\\log_{3}(3^{x}-6)=x-1$", None,
  '$x=2$.'),
 ("Oldd meg! $\\log_{0,25}(3x+1)\\ge\\log_{0,25}(9-x)$", None,
  '$x\\in\\left(-\\tfrac13;2\\right]$.'),
 ("Oldd meg! $\\log_{2}\\dfrac{x+1}{x-1}\\le 1$", None,
  '$x\\in(-\\infty;-1)\\cup[3;+\\infty)$.'),
]

JOKER = ("Oldd meg! $x^{\\lg x}=100x$",
         '$\\boxed{x_{1}=100}$, $\\boxed{x_{2}=\\tfrac{1}{10}}$.')

# ============================== GYAKORLÓ DOLGOZAT ==============================

GYD_ORAI = [
 ("Számold ki!",
  ["$\\log_{2}64$", "$4^{3}-3\\log_{2}32$", "$\\log_{6}108-\\log_{6}3$"],
  ['$6$', '$49$', '$2$'], True),
 ("Ábrázold a függvényt!",
  ["$y=\\left(\\tfrac12\\right)^{x}+2$", "$y=3^{x-1}$", "$y=\\log_{3}x$"],
  ["Csökkenő, $2$-vel feljebb; aszimptota: $y=2$.",
   "Növekvő, $1$-gyel jobbra; aszimptota az $x$-tengely.",
   "Növekvő logaritmusgörbe; ÉT: $x&gt;0$; aszimptota az $y$-tengely."], True),
 ("Oldd meg az egyenleteket!",
  ["$\\left(\\tfrac12\\right)^{-2x}=\\tfrac{1}{16}$", "$2^{6x}=4^{9}$",
   "$\\log_{4}(3x-2)=2$", "$7^{x+2}-7^{x}=336$"],
  ['$x=-2$', '$x=3$', '$x=6$', '$x=1$'], True),
 ("Oldd meg az egyenlőtlenséget, és ábrázold a megoldást a számegyenesen!",
  ["$3^{2x+7}&lt;81$", "$\\log_{0,5}(3x-1)\\ge\\log_{0,5}(x+5)$"],
  ['$x\\in\\left(-\\infty;-\\tfrac32\\right)$', '$x\\in\\left(\\tfrac13;3\\right]$'], True),
 ("★ Oldd meg! $\\lg(x-\\sqrt5)+\\lg(x+\\sqrt5)=\\lg(9-x)+\\lg x$", None,
  '$x=5$.'),
]

GYD_OTTHON = [
 ("Számold ki! (A b) eredményét öt tizedesre kerekítve add meg.)",
  ["$\\log_{3}243$", "$\\log_{2}5$", "$\\lg 20+\\lg 5$"],
  ['$5$', '$\\dfrac{\\lg 5}{\\lg 2}\\approx 2{,}32193$', '$2$'], True),
 ("Ábrázold a függvényt!", ["$y=2^{x}-3$", "$y=\\log_{2}(x+1)$"],
  ["Növekvő, $3$-mal lejjebb; aszimptota: $y=-3$; nullahely: $x=\\log_{2}3\\approx 1{,}58$.",
   "$1$-gyel balra tolt logaritmusgörbe; ÉT: $x&gt;-1$; aszimptota: $x=-1$."], True),
 ("Oldd meg!", ["$3^{5x}=27^{3}$", "$\\log_{2}(x-3)=4$"],
  ['$x=\\dfrac95$', '$x=19$'], True),
 ("Oldd meg! $4^{x}-6\\cdot 2^{x}+8=0$", None,
  '$x_{1}=1$, $x_{2}=2$.'),
 ("Oldd meg! $\\log_{3}(2x+1)&lt;2$", None,
  '$x\\in\\left(-\\tfrac12;4\\right)$.'),
 ("★ Oldd meg! $\\log_{2}\\dfrac{2x+1}{x-1}\\le 2$", None,
  '$x\\in\\left(-\\infty;-\\tfrac12\\right)\\cup\\left[\\tfrac52;+\\infty\\right)$.'),
]

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
 '    <h2 id="gyak-dolgozat">📝 Gyakorló dolgozat</h2>\n    ' + DISZKLEMER +
 '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYD_ORAI, "gyd") +
 '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYD_OTTHON, "gydh"),
]

ut = oldal(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
           fajl="feladatok-logaritmusfuggveny.html",
           cim="A logaritmusfüggvény",
           temakor="Exponenciális és logaritmusfüggvény",
           alcim="Értelmezési tartomány, inverz és grafikon, logaritmusos egyenletek és "
                 "egyenlőtlenségek — a végén gyakorló dolgozattal a teljes témakörből. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-logaritmusos-egyenletek.html",
           prevc="Logaritmusos egyenletek és egyenlőtlenségek",
           nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYD_ORAI), "+", len(GYD_OTTHON))
