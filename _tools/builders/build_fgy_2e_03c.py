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
  ["$x-5&gt;0$, tehát $x\\in(5;+\\infty)$", "$2x+6&gt;0$, tehát $x\\in(-3;+\\infty)$"], True),
 ("Add meg az értelmezési tartományt!",
  ["$y=\\lg(4-x)$", "$y=\\log_{5}x^{2}$"],
  ["$4-x&gt;0$, tehát $x\\in(-\\infty;4)$",
   "$x^{2}&gt;0$, tehát minden $x\\neq 0$"], True),
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
  ["$x-4=1$, tehát $x=5$", "$\\log_{2}x=3$, tehát $x=8$"], True),
 ("Írd fel a függvény inverzét!",
  ["$y=3^{x}$", "$y=\\log_{5}x$", "$y=\\left(\\tfrac12\\right)^{x}$"],
  ["$y=\\log_{3}x$", "$y=5^{x}$", "$y=\\log_{\\frac12}x$"], True),
 ("Oldd meg!", ["$\\log_{2}x=4$", "$\\log_{3}x=-1$"],
  ["$x=2^{4}=16$", "$x=3^{-1}=\\dfrac13$"], True),
 ("Oldd meg! (Ne feledd az értelmezési tartományt.)",
  ["$\\log_{2}(x-1)=3$", "$\\log_{5}(2x+3)=2$"],
  ["ÉT: $x&gt;1$; $x-1=8$, tehát $x=9$", "ÉT: $x&gt;-\\tfrac32$; $2x+3=25$, tehát $x=11$"], True),
 ("Oldd meg!", ["$\\lg(3x-1)=\\lg(x+7)$", "$\\log_{2}(5x-2)=\\log_{2}(2x+7)$"],
  ["$3x-1=x+7$, tehát $x=4$ (az ÉT-ben van)",
   "$5x-2=2x+7$, tehát $x=3$ (az ÉT-ben van)"], True),
 ("Oldd meg! $\\log_{4}(x^{2}-3x)=1$", None,
  "ÉT: $x^{2}-3x&gt;0$, azaz $x&lt;0$ vagy $x&gt;3$. Az egyenlet: $x^{2}-3x=4$, "
  "innen $x_{1}=-1$ és $x_{2}=4$ — <b>mindkettő</b> jó, mert az argumentum értéke "
  "mindkét esetben $4&gt;0$."),
 ("Oldd meg! $\\log_{2}x+\\log_{2}4=5$", None,
  "$\\log_{2}(4x)=5$, tehát $4x=32$ és $x=8$."),
 ("Oldd meg!", ["$\\log_{2}x&lt;3$", "$\\log_{3}x&gt;2$"],
  ["ÉT: $x&gt;0$; $x&lt;8$, tehát $x\\in(0;8)$",
   "ÉT: $x&gt;0$; $x&gt;9$, tehát $x\\in(9;+\\infty)$"], True),
 ("Oldd meg!", ["$\\log_{2}(x-1)\\le 2$", "$\\log_{5}(x+2)\\ge 1$"],
  ["ÉT: $x&gt;1$; $x-1\\le 4$, tehát $x\\in(1;5]$",
   "ÉT: $x&gt;-2$; $x+2\\ge 5$, tehát $x\\in[3;+\\infty)$"], True),
 ("Oldd meg! $\\log_{\\frac12}x&gt;2$", None,
  "ÉT: $x&gt;0$. Az alap kisebb $1$-nél, a jel <b>fordul</b>: "
  "$x&lt;\\left(\\tfrac12\\right)^{2}=\\tfrac14$. A metszet: "
  "$x\\in\\left(0;\\tfrac14\\right)$."),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Ábrázold, és jellemezd (ÉT, aszimptota, nullahely, monotonitás)! "
  "$y=\\log_{2}(x+3)-1$", None,
  "ÉT: $x&gt;-3$; aszimptota: $x=-3$; nullahely: $\\log_{2}(x+3)=1$, azaz $x=-1$; "
  "szigorúan növekvő. A grafikon az $y=\\log_{2}x$ görbe $3$-mal balra és $1$-gyel lejjebb."),
 ("Az $y=2^{x}$ és az $y=\\log_{2}x$ grafikonja hogyan viszonyul egymáshoz? "
  "Mit tudsz mondani a metszéspontjaikról?", None,
  "Egymás tükörképei az $y=x$ egyenesre (a két függvény egymás inverze). Mivel az "
  "$y=2^{x}$ végig az $y=x$ egyenes <b>fölött</b> halad, a két görbének "
  "<b>nincs</b> közös pontja."),
 ("Oldd meg! $\\log_{3}(x-2)+\\log_{3}(x+2)=1$", None,
  "ÉT: $x&gt;2$. Összevonva $\\log_{3}(x^{2}-4)=1$, tehát $x^{2}-4=3$ és "
  "$x=\\pm\\sqrt7$. Az ÉT miatt csak $x=\\sqrt7\\approx 2{,}65$ jó."),
 ("Oldd meg! $\\lg(x-3)+\\lg(x+1)=\\lg 5$", None,
  "ÉT: $x&gt;3$. Innen $(x-3)(x+1)=5$, azaz $x^{2}-2x-8=0$: $x_{1}=4$, $x_{2}=-2$. "
  "Az ÉT miatt csak $x=4$ jó."),
 ("Oldd meg! $\\log_{2}(x+1)-\\log_{2}(x-1)=1$", None,
  "ÉT: $x&gt;1$. Összevonva $\\log_{2}\\dfrac{x+1}{x-1}=1$, tehát "
  "$\\dfrac{x+1}{x-1}=2$, azaz $x+1=2x-2$ és $x=3$."),
 ("Oldd meg helyettesítéssel! $\\left(\\log_{2}x\\right)^{2}-3\\log_{2}x+2=0$", None,
  "ÉT: $x&gt;0$. Legyen $t=\\log_{2}x$: $t^{2}-3t+2=0$, innen $t_{1}=1$, $t_{2}=2$, "
  "tehát $x_{1}=2$ és $x_{2}=4$."),
 ("Oldd meg! $\\log_{3}x+\\log_{x}3=2$", None,
  "ÉT: $x&gt;0$, $x\\neq 1$. Mivel $\\log_{x}3=\\dfrac{1}{\\log_{3}x}$, a $t=\\log_{3}x$ "
  "helyettesítéssel $t+\\dfrac1t=2$, azaz $t^{2}-2t+1=0$: $t=1$, tehát $x=3$."),
 ("Oldd meg! $\\log_{0,5}(x-1)&gt;\\log_{0,5}(2x-5)$", None,
  "ÉT: $x&gt;1$ és $x&gt;\\tfrac52$, azaz $x&gt;\\tfrac52$. Az alap kisebb $1$-nél, "
  "a jel fordul: $x-1&lt;2x-5$, tehát $x&gt;4$. A metszet: $x\\in(4;+\\infty)$."),
 ("Oldd meg! $\\log_{2}(x^{2}-5x+7)=0$", None,
  "A jobb oldal $0$, tehát $x^{2}-5x+7=1$, azaz $x^{2}-5x+6=0$: $x_{1}=2$, $x_{2}=3$. "
  "Az argumentum mindkét esetben $1&gt;0$, tehát mindkettő jó."),
 ("Oldd meg! $\\log_{3}(2x-1)\\le 2$", None,
  "ÉT: $x&gt;\\tfrac12$. Az alap $3&gt;1$: $2x-1\\le 9$, tehát $x\\le 5$. "
  "A metszet: $x\\in\\left(\\tfrac12;5\\right]$."),
 ("Oldd meg! $\\lg(x^{2}-4)&lt;\\lg(3x)$", None,
  "ÉT: $x^{2}-4&gt;0$ és $3x&gt;0$, azaz $x&gt;2$. Az alap $10&gt;1$: "
  "$x^{2}-4&lt;3x$, tehát $x^{2}-3x-4&lt;0$, azaz $-1&lt;x&lt;4$. "
  "A metszet: $x\\in(2;4)$."),
 ("Oldd meg! $\\log_{\\frac13}(x+2)\\ge -1$", None,
  "ÉT: $x&gt;-2$. Az alap kisebb $1$-nél, a jel fordul: "
  "$x+2\\le\\left(\\tfrac13\\right)^{-1}=3$, tehát $x\\le 1$. "
  "A metszet: $x\\in(-2;1]$."),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Oldd meg! $\\lg^{2}x-\\lg x^{2}-3=0$", None,
  "ÉT: $x&gt;0$. Mivel $\\lg x^{2}=2\\lg x$, a $t=\\lg x$ helyettesítéssel "
  "$t^{2}-2t-3=0$: $t_{1}=3$, $t_{2}=-1$, tehát $x_{1}=1000$ és "
  "$x_{2}=\\dfrac{1}{10}$."),
 ("Oldd meg! $\\log_{2}(x-1)+\\log_{2}(x-2)=1$", None,
  "ÉT: $x&gt;2$. Innen $(x-1)(x-2)=2$, azaz $x^{2}-3x=0$: $x_{1}=0$, $x_{2}=3$. "
  "Az ÉT miatt csak $x=3$ jó."),
 ("Oldd meg! $\\log_{x}4=2$", None,
  "ÉT: $x&gt;0$ és $x\\neq 1$. A definíció szerint $x^{2}=4$, tehát $x=\\pm 2$ — "
  "de az alap nem lehet negatív, így csak $x=2$."),
 ("Oldd meg! $\\log_{3}(3^{x}-6)=x-1$", None,
  "A definíció szerint $3^{x}-6=3^{x-1}=\\dfrac{3^{x}}{3}$, tehát "
  "$3^{x}\\left(1-\\tfrac13\\right)=6$, azaz $\\tfrac23\\cdot 3^{x}=6$ és $3^{x}=9$: "
  "$x=2$. (Ellenőrzés: $9-6=3$ és $\\log_{3}3=1=2-1$ ✔)"),
 ("Oldd meg! $\\log_{0,25}(3x+1)\\ge\\log_{0,25}(9-x)$", None,
  "ÉT: $x&gt;-\\tfrac13$ és $x&lt;9$. Az alap kisebb $1$-nél, a jel fordul: "
  "$3x+1\\le 9-x$, tehát $x\\le 2$. A metszet: "
  "$x\\in\\left(-\\tfrac13;2\\right]$."),
 ("Oldd meg! $\\log_{2}\\dfrac{x+1}{x-1}\\le 1$", None,
  "ÉT: $\\dfrac{x+1}{x-1}&gt;0$, azaz $x&lt;-1$ vagy $x&gt;1$. Az alap $2&gt;1$: "
  "$\\dfrac{x+1}{x-1}\\le 2$, rendezve $\\dfrac{3-x}{x-1}\\le 0$, ami $x&lt;1$ vagy "
  "$x\\ge 3$. A metszet: $x\\in(-\\infty;-1)\\cup[3;+\\infty)$."),
]

JOKER = ("Oldd meg! $x^{\\lg x}=100x$",
         "ÉT: $x&gt;0$. Vegyük mindkét oldal tizes alapú logaritmusát: "
         "$\\lg x\\cdot\\lg x=\\lg 100+\\lg x$, azaz $t^{2}-t-2=0$, ahol $t=\\lg x$. "
         "A gyökök $t_{1}=2$ és $t_{2}=-1$, tehát $\\boxed{x_{1}=100}$ és "
         "$\\boxed{x_{2}=\\tfrac{1}{10}}$.")

# ============================== GYAKORLÓ DOLGOZAT ==============================

GYD_ORAI = [
 ("Számold ki!",
  ["$\\log_{2}64$", "$4^{3}-3\\log_{2}32$", "$\\log_{6}108-\\log_{6}3$"],
  ["$6$", "$64-15=49$", "$\\log_{6}36=2$"], True),
 ("Ábrázold a függvényt!",
  ["$y=\\left(\\tfrac12\\right)^{x}+2$", "$y=3^{x-1}$", "$y=\\log_{3}x$"],
  ["Csökkenő, $2$-vel feljebb; aszimptota: $y=2$.",
   "Növekvő, $1$-gyel jobbra; aszimptota az $x$-tengely.",
   "Növekvő logaritmusgörbe; ÉT: $x&gt;0$; aszimptota az $y$-tengely."], True),
 ("Oldd meg az egyenleteket!",
  ["$\\left(\\tfrac12\\right)^{-2x}=\\tfrac{1}{16}$", "$2^{6x}=4^{9}$",
   "$\\log_{4}(3x-2)=2$", "$7^{x+2}-7^{x}=336$"],
  ["$2^{2x}=2^{-4}$, tehát $x=-2$", "$2^{6x}=2^{18}$, tehát $x=3$",
   "ÉT: $x&gt;\\tfrac23$; $3x-2=16$, tehát $x=6$",
   "$48\\cdot 7^{x}=336$, azaz $7^{x}=7$, tehát $x=1$"], True),
 ("Oldd meg az egyenlőtlenséget, és ábrázold a megoldást a számegyenesen!",
  ["$3^{2x+7}&lt;81$", "$\\log_{0,5}(3x-1)\\ge\\log_{0,5}(x+5)$"],
  ["$2x+7&lt;4$, tehát $x\\in\\left(-\\infty;-\\tfrac32\\right)$",
   "ÉT: $x&gt;\\tfrac13$; az alap kisebb $1$-nél, a jel fordul: $3x-1\\le x+5$, "
   "azaz $x\\le 3$. A metszet: $x\\in\\left(\\tfrac13;3\\right]$"], True),
 ("★ Oldd meg! $\\lg(x-\\sqrt5)+\\lg(x+\\sqrt5)=\\lg(9-x)+\\lg x$", None,
  "ÉT: $x&gt;\\sqrt5$ és $x&lt;9$. Összevonva $x^{2}-5=9x-x^{2}$, azaz "
  "$2x^{2}-9x-5=0$. A diszkrimináns $81+40=121$, a gyökök $x_{1}=5$ és "
  "$x_{2}=-\\tfrac12$ — az utóbbi az ÉT miatt kiesik. Megoldás: $x=5$."),
]

GYD_OTTHON = [
 ("Számold ki! (A b) eredményét öt tizedesre kerekítve add meg.)",
  ["$\\log_{3}243$", "$\\log_{2}5$", "$\\lg 20+\\lg 5$"],
  ["$5$", "$\\dfrac{\\lg 5}{\\lg 2}\\approx 2{,}32193$", "$\\lg 100=2$"], True),
 ("Ábrázold a függvényt!", ["$y=2^{x}-3$", "$y=\\log_{2}(x+1)$"],
  ["Növekvő, $3$-mal lejjebb; aszimptota: $y=-3$; nullahely: $x=\\log_{2}3\\approx 1{,}58$.",
   "$1$-gyel balra tolt logaritmusgörbe; ÉT: $x&gt;-1$; aszimptota: $x=-1$."], True),
 ("Oldd meg!", ["$3^{5x}=27^{3}$", "$\\log_{2}(x-3)=4$"],
  ["$3^{5x}=3^{9}$, tehát $x=\\dfrac95$", "ÉT: $x&gt;3$; $x-3=16$, tehát $x=19$"], True),
 ("Oldd meg! $4^{x}-6\\cdot 2^{x}+8=0$", None,
  "$t=2^{x}$: $t^{2}-6t+8=0$, innen $t_{1}=2$, $t_{2}=4$, tehát $x_{1}=1$ és $x_{2}=2$."),
 ("Oldd meg! $\\log_{3}(2x+1)&lt;2$", None,
  "ÉT: $x&gt;-\\tfrac12$. Az alap $3&gt;1$: $2x+1&lt;9$, tehát $x&lt;4$. "
  "A metszet: $x\\in\\left(-\\tfrac12;4\\right)$."),
 ("★ Oldd meg! $\\log_{2}\\dfrac{2x+1}{x-1}\\le 2$", None,
  "ÉT: $\\dfrac{2x+1}{x-1}&gt;0$, azaz $x&lt;-\\tfrac12$ vagy $x&gt;1$. "
  "Az alap $2&gt;1$: $\\dfrac{2x+1}{x-1}\\le 4$, rendezve $\\dfrac{5-2x}{x-1}\\le 0$, "
  "ami $x&lt;1$ vagy $x\\ge\\tfrac52$. A metszet: "
  "$x\\in\\left(-\\infty;-\\tfrac12\\right)\\cup\\left[\\tfrac52;+\\infty\\right)$."),
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
