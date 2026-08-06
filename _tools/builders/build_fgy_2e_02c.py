# -*- coding: utf-8 -*-
"""2e/02 — C altema feladatgyujtemeny: masodfoku egyenlotlensegek es rendszerek.
Gyakorlo blokk NINCS — ez az anyagresz a 2. dolgozat utan kovetkezik."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, solve, simplify, expand, Eq, sqrt, im, re as _re
x, y, m, c, t = symbols('x y m c t')
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, (list, tuple)) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 ("A1c", sorted(solve(x**2-x-6, x)), [-2, 3]), ("A1d", sorted(solve(x**2-3*x+2, x)), [1, 2]),
 ("A2b", sorted(solve(x**2-5*x+4, x)), [1, 4]),
 ("A3", sorted(solve(x**2-6*x+9, x)), [3]),
 ("A4", 4-20, -16),
 ("A5b", sorted(solve(-x**2+4*x-3, x)), [1, 3]),
 ("A6", sorted(solve(x**2-2*x-8, x)), [-2, 4]),
 ("A9", sorted(solve(x**2-x-2, x)), [-1, 2]),
 ("A10", sorted(solve(t**2-5*t+6, t)), [2, 3]),
 ("A11", sorted(solve(y**2+y-6, y)), [-3, 2]),
 ("K1a", sorted(solve(2*x**2-5*x+2, x)), [R(1,2), 2]),
 ("K2a", sorted(solve(x**2-4*x, x)), [0, 4]), ("K2b", sorted(solve(x**2-5*x+6, x)), [2, 3]),
 ("K5", sorted(solve(m**2-36, m)), [-6, 6]),
 ("K6", sorted(solve(x**2-5*x+4, x)), [1, 4]),
 ("K7", sorted(solve(x**2+2*x-3, x)), [-3, 1]),
 ("K8", sorted(solve(y**2-10*y+21, y)), [3, 7]),
 ("K9", solve(Eq(1+4*c, 0), c), [R(-1,4)]),
 ("K10", sorted(solve(y**2+3*y-40, y)), [-8, 5]),
 ("N2", sorted(solve(t**2-5*t+6, t)), [2, 3]),
 ("N3", solve(Eq(1-4*m, 0), m), [R(1,4)]),
 ("N4", sorted(solve(y**2-7*y+12, y)), [3, 4]),
 ("N5", sorted(solve(t**2-17*t+60, t)), [5, 12]),
]
for n, g, w in P:
    chk(n, g, w)
assert not E, E[:4]
print("sympy önteszt: OK")

# ============================== FELADATOK ==============================

ALAP = [
 ("Oldd meg a másodfokú egyenlőtlenséget!",
  ["$x^{2}-4&lt;0$", "$x^{2}-16&gt;0$", "$x^{2}-x-6&lt;0$", "$x^{2}-3x+2&gt;0$"],
  ["$x\\in(-2;2)$", "$x\\in(-\\infty;-4)\\cup(4;+\\infty)$", "$x\\in(-2;3)$",
   "$x\\in(-\\infty;1)\\cup(2;+\\infty)$"], False),
 ("Figyelj a végpontokra! (Zárt vagy nyílt?)",
  ["$x^{2}-9\\le 0$", "$x^{2}-5x+4\\ge 0$"],
  ["$x\\in[-3;3]$", "$x\\in(-\\infty;1]\\cup[4;+\\infty)$"], False),
 ("Oldd meg! (Itt $D=0$.)",
  ["$x^{2}-6x+9&gt;0$", "$x^{2}-6x+9\\le 0$", "$x^{2}+4x+4\\ge 0$"],
  ["$x\\in\\mathbb{R}\\setminus\\{3\\}$", "Egyetlen megoldás: $x=3$.",
   "$x\\in\\mathbb{R}$ (minden valós szám)."], False),
 ("Oldd meg! (Itt $D&lt;0$.)",
  ["$x^{2}+2x+5&gt;0$", "$x^{2}+2x+5&lt;0$", "$-x^{2}+x-3&lt;0$"],
  ["$x\\in\\mathbb{R}$", "Nincs megoldás.", "$x\\in\\mathbb{R}$"], False),
 ("Oldd meg! (Negatív főegyüttható.)",
  ["$-x^{2}+9&gt;0$", "$-x^{2}+4x-3\\ge 0$"],
  ["$x\\in(-3;3)$", "$x\\in[1;3]$"], False),
 ("Az $y=x^{2}-2x-8$ függvény grafikonja alapján add meg, hol",
  ["pozitív a függvény?", "negatív a függvény?"],
  ["$x\\in(-\\infty;-2)\\cup(4;+\\infty)$", "$x\\in(-2;4)$"], False),
 ("Oldd meg a rendszert! $y=x^{2}$ és $y=4$", None, "$(2;4)$ és $(-2;4)$"),
 ("Oldd meg a rendszert! $y=x^{2}-1$ és $y=3$", None, "$(2;3)$ és $(-2;3)$"),
 ("Oldd meg a rendszert! $y=x^{2}$ és $y=x+2$", None, "$(2;4)$ és $(-1;1)$"),
 ("Oldd meg a rendszert! $x+y=5$ és $x\\cdot y=6$", None, "$(2;3)$ és $(3;2)$"),
 ("Oldd meg a rendszert! $x-y=1$ és $x\\cdot y=6$", None, "$(3;2)$ és $(-2;-3)$"),
 ("Hány közös pontja van a görbéknek?",
  ["$y=x^{2}$ és $y=1$", "$y=x^{2}$ és $y=0$", "$y=x^{2}$ és $y=-1$"],
  ["Kettő.", "Egy (érintés az origóban).", "Egy sem."], True),
]

KOZEP = [
 ("Oldd meg!",
  ["$2x^{2}-5x+2\\le 0$", "$3x^{2}-12&gt;0$"],
  ["$x\\in\\left[\\dfrac{1}{2};2\\right]$", "$x\\in(-\\infty;-2)\\cup(2;+\\infty)$"], False),
 ("Előbb rendezz nullára!",
  ["$x^{2}&lt;4x$", "$x^{2}+6\\ge 5x$"],
  ["$x\\in(0;4)$", "$x\\in(-\\infty;2]\\cup[3;+\\infty)$"], False),
 ("A szorzat alakból közvetlenül olvasd le!",
  ["$(x-1)(x+3)&gt;0$", "$(x-2)(x-5)\\le 0$"],
  ["$x\\in(-\\infty;-3)\\cup(1;+\\infty)$", "$x\\in[2;5]$"], False),
 ("Oldd meg! $\\dfrac{x^{2}-4}{3}\\le 0$", None, "$x\\in[-2;2]$"),
 ("Milyen $m$ esetén teljesül <b>minden</b> valós $x$-re, hogy $x^{2}+mx+9&gt;0$?",
  None, "$-6&lt;m&lt;6$"),
 ("Oldd meg a rendszert! $y=x^{2}-4x+3$ és $y=x-1$", None, "$(1;0)$ és $(4;3)$"),
 ("Oldd meg a rendszert! $y=-x^{2}+4$ és $y=2x+1$", None, "$(1;3)$ és $(-3;-5)$"),
 ("Oldd meg a rendszert! $x+y=10$ és $x^{2}+y^{2}=58$", None, "$(7;3)$ és $(3;7)$"),
 ("Milyen $c$ esetén <b>érinti</b> az $y=x+c$ egyenes az $y=x^{2}$ parabolát?",
  None, "$c=-\\dfrac{1}{4}$"),
 ("Két szám különbsége $3$, szorzatuk $40$. Melyik ez a két szám?",
  None, "$8$ és $5$, illetve $-5$ és $-8$."),
 ('Egy kadét így oldotta meg az $x^2>4$ egyenlőtlenséget: <i>„Mindkét oldalból gyököt vonok, így $x>2$.”</i>',
  ['Ellenőrizd a megoldását: teljesül-e $x=-3$-ra az eredeti egyenlőtlenség?',
   'Hol csúszik el a gondolatmenet?',
   'Add meg a helyes megoldáshalmazt!'],
  ['Igen: $(-3)^2=9>4$, tehát $-3$ megoldás — a kadét válasza viszont kizárja.',
   'A négyzetgyökvonás nem őrzi meg az egyenlőtlenséget negatív számokra: $\\sqrt{x^2}=|x|$, nem $x$. A helyes lépés tehát $|x|>2$.',
   '$|x|>2$, azaz $x<-2$ vagy $x>2$: $x\\in(-\\infty;-2)\\cup(2;+\\infty)$.']),
]

NEHEZ = [
 ("Oldd meg! $\\dfrac{x-2}{x+3}\\le 0$ &nbsp;$(x\\neq -3)$", None, "$x\\in(-3;2]$"),
 ("Oldd meg! $x^{2}-5\\left|x\\right|+6&lt;0$ &nbsp;(Útmutató: legyen $t=\\left|x\\right|$.)",
  None, "$x\\in(-3;-2)\\cup(2;3)$"),
 ("Milyen $m$ esetén van az $y=x^{2}+2x+m$ parabolának és az $y=x$ egyenesnek "
  "<b>pontosan egy</b> közös pontja?", None, "$m=\\dfrac{1}{4}$"),
 ("Oldd meg a rendszert! $x^{2}+y^{2}=25$ és $x+y=7$", None, "$(4;3)$ és $(3;4)$"),
 ("Egy derékszögű háromszög befogóinak összege $17$ cm, területe $30\\ \\text{cm}^{2}$. "
  "Mekkorák a befogók?", None, "$12$ cm és $5$ cm."),
]

JOKER = ("<b>Dr. Baljós vírus-kódja.</b> A rendszer ezt a levezetést adta ki: "
         "$$x^{2}&gt;4\\ \\Rightarrow\\ x&gt;2$$ "
         "Miért hibás? Adj ellenpéldát, és írd fel a helyes megoldást!",
         "Ellenpélda: $x=-5$, mert $25&gt;4$ igaz, de $-5&gt;2$ hamis. "
         "Helyesen $x\\in(-\\infty;-2)\\cup(2;+\\infty)$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
           fajl="feladatok-egyenlotlensegek-es-rendszerek.html",
           cim="Egyenlőtlenségek és rendszerek",
           temakor="Másodfokú egyenletek és függvények",
           alcim="Másodfokú egyenlőtlenségek mind a három diszkrimináns-esetre, valamint "
                 "egy másodfokú és egy lineáris egyenletből álló rendszerek — "
                 "behelyettesítéssel és Viète-képletekkel.",
           sections_html="\n".join(body),
           prev="tananyag-masodfoku-linearis-rendszer.html",
           prevc="Másodfokú és lineáris egyenletből álló rendszer",
           nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
