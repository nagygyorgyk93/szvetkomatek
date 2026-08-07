# -*- coding: utf-8 -*-
"""2e/02 — B altema feladatgyujtemeny: a masodfoku fuggveny. + gyakorlo DOLGOZAT (A+B blokk)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, solve, simplify, expand, im, re as _re, I, sqrt, Eq
x, m, c, t = symbols('x m c t')
def S(e): return sorted(solve(e, x), key=lambda z: (im(z), _re(z)))
def csucs(a, b, cc): return (R(-b, 2*a), a*R(-b, 2*a)**2 + b*R(-b, 2*a) + cc)
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, (list, tuple)) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 ("A2a", csucs(1, -4, 3), (2, -1)), ("A2b", csucs(1, 6, 5), (-3, -4)),
 ("A2c", csucs(1, -2, 0), (1, -1)),
 ("A3a", S(x**2-9), [-3, 3]), ("A3b", S(x**2-5*x+4), [1, 4]), ("A3c", S(x**2+3*x), [-3, 0]),
 ("A5a", expand((x-1)**2+4), x**2-2*x+5), ("A5b", expand((x+2)**2-3), x**2+4*x+1),
 ("A5c", expand((x-3)**2), x**2-6*x+9),
 ("A6a", csucs(1, -8, 20), (4, 4)), ("A6b", csucs(-1, 2, 3), (1, 4)),
 ("A6c", csucs(2, -4, 1), (1, -1)),
 ("A7c", csucs(1, -6, 5), (3, -4)),
 ("A11", csucs(1, 0, -4), (0, -4)),
 ("K1a", S(x**2-6*x+8), [2, 4]), ("K1a2", csucs(1, -6, 8), (3, -1)),
 ("K1b", S(x**2+2*x-3), [-3, 1]), ("K1b2", csucs(1, 2, -3), (-1, -4)),
 ("K2", S(-x**2+6*x-5), [1, 5]), ("K2b", csucs(-1, 6, -5), (3, 4)),
 ("K3", S(2*x**2-8*x+6), [1, 3]), ("K3b", csucs(2, -8, 6), (2, -2)),
 ("K4a", expand((x+3)**2-4), x**2+6*x+5), ("K4b", expand(-(x-2)**2+9), -x**2+4*x+5),
 ("K6", solve(Eq(36-4*c, 0), c), [9]),
 ("K8", csucs(1, -10, 0), (5, -25)),
 ("K9", csucs(-1, 12, 0), (6, 36)),
 ("K10", S(-2*x**2+8*x-6), [1, 3]), ("K10b", csucs(-2, 8, -6), (2, 2)),
 ("N1", expand((x-2)**2-3), x**2-4*x+1),
 ("N2", expand(2*(x+1)*(x-3)), 2*x**2-4*x-6),
 ("N3", csucs(-5, 20, 0), (2, 20)), ("N3b", S(-5*x**2+20*x), [0, 4]),
 ("N4", sorted(solve(m**2-m-6, m)), [-2, 3]),
 ("N5", S(x**2-4*x+7-2*x-2), [1, 5]),
 ("GY1a", S(6*x**2+42*x), [-7, 0]), ("GY1b", S(x**2-256), [-16, 16]),
 ("GY1c", S(2*x**2-x-6), [R(-3,2), 2]), ("GY1d", S((x+1)*(x-5)-16), [-3, 7]),
 ("GY2a", expand((x-4)*(x-7)), x**2-11*x+28), ("GY2b", expand((x+6)*(x+7)), x**2+13*x+42),
 ("GY4", R(11, 28), R(11,28)), ("GY4b", 121-2*28, 65),
 ("GY5", S(x**2-4*x+3), [1, 3]), ("GY5b", csucs(1, -4, 3), (2, -1)),
 ("GY6", S(-x**2+2*x+8), [-2, 4]), ("GY6b", csucs(-1, 2, 8), (1, 9)),
 ("GY7", sorted(solve(t**2-29*t+100, t)), [4, 25]),
 ("GY8", sorted(solve(t**2-7*t-18, t)), [-2, 9]),
 ("GY9", expand((x+2)*(x-7)), x**2-5*x-14),
 ("GY10", csucs(-1, 14, 0), (7, 49)),
 ("GYH1a", S(4*x**2-100), [-5, 5]), ("GYH1b", S(x**2+8*x), [-8, 0]),
 ("GYH1c", S(5*x**2-13*x-6), [R(-2,5), 3]),
 ("GYH2", expand(3*(x-2)*(x-5)), 3*x**2-21*x+30),
 ("GYH3", solve(Eq(144-4*m, 0), m), [36]),
 ("GYH4", S(x**2+2*x-8), [-4, 2]), ("GYH4b", csucs(1, 2, -8), (-1, -9)),
 ("GYH5", sorted(solve(t**2-20*t+64, t)), [4, 16]),
]
for n, g, w in P:
    chk(n, g, w)
assert not E, E[:4]
print("sympy önteszt: OK")

VIZSG = "Ábrázold a grafikont, és vizsgáld ki! (értékkészlet, szélsőérték, zérushely(ek), konvexitás)"

# ============================== FELADATOK ==============================

ALAP = [
 ("Milyen a parabola nyílásiránya, és karcsúbb vagy szélesebb az $y=x^{2}$-nél?",
  ["$y=3x^{2}$", "$y=-2x^{2}$", "$y=\\dfrac{1}{3}x^{2}$", "$y=-\\dfrac{1}{2}x^{2}$"],
  ["Felfelé nyílik, karcsúbb.", "Lefelé nyílik, karcsúbb.",
   "Felfelé nyílik, szélesebb.", "Lefelé nyílik, szélesebb."], True),
 ("Add meg a csúcspontot a képlettel!",
  ["$y=x^{2}-4x+3$", "$y=x^{2}+6x+5$", "$y=x^{2}-2x$"],
  ["$C(2;-1)$", "$C(-3;-4)$", "$C(1;-1)$"], True),
 ("Add meg a zérushelyeket!",
  ["$y=x^{2}-9$", "$y=x^{2}-5x+4$", "$y=x^{2}+3x$"],
  ["$\\pm 3$", "$1$ és $4$", "$0$ és $-3$"], True),
 ("Mennyi az $y$-tengelymetszet?",
  ["$y=x^{2}-4x+7$", "$y=2x^{2}+3x$", "$y=-x^{2}+5$"],
  ["$7$", "$0$", "$5$"], True),
 ("Írd kanonikus (teljes négyzetes) alakba!",
  ["$y=x^{2}-2x+5$", "$y=x^{2}+4x+1$", "$y=x^{2}-6x+9$"],
  ["$y=(x-1)^{2}+4$", "$y=(x+2)^{2}-3$", "$y=(x-3)^{2}$"], True),
 ("Van-e minimuma vagy maximuma, és mennyi az értéke?",
  ["$y=x^{2}-8x+20$", "$y=-x^{2}+2x+3$", "$y=2x^{2}-4x+1$"],
  ["Minimum, értéke $4$ (az $x=4$ helyen).", "Maximum, értéke $4$ (az $x=1$ helyen).",
   "Minimum, értéke $-1$ (az $x=1$ helyen)."], False),
 ("Add meg az értékkészletet!",
  ["$y=x^{2}+1$", "$y=-x^{2}-2$", "$y=x^{2}-6x+5$"],
  ["$[1;+\\infty)$", "$(-\\infty;-2]$", "$[-4;+\\infty)$"], True),
 ("Hány zérushelye van a függvénynek?",
  ["$y=x^{2}-4x+4$", "$y=x^{2}+x+3$", "$y=x^{2}-x-6$"],
  ["Egy (kettős): $D=0$.", "Egy sem: $D=-11&lt;0$.", "Kettő: $D=25&gt;0$."], True),
 ("Olvasd le a kanonikus alakból a csúcspontot és a szélsőértéket!",
  ["$y=(x-2)^{2}+3$", "$y=-(x+1)^{2}+5$", "$y=2(x-4)^{2}$"],
  ["$C(2;3)$, minimum $3$.", "$C(-1;5)$, maximum $5$.", "$C(4;0)$, minimum $0$."], True),
 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["A másodfokú függvény értelmezési tartománya $\\mathbb{R}$.",
   "Ha $a&lt;0$, a függvénynek minimuma van.",
   "A csúcspont mindig az $y$-tengelyen van.",
   "A parabola szimmetrikus a csúcsponton átmenő függőleges egyenesre."],
  ["Igaz.", "Hamis: ekkor <b>maximuma</b> van.",
   "Hamis: csak akkor, ha $b=0$.", "Igaz."], False),
 ("Vizsgáld meg teljesen az $y=x^{2}-4$ függvényt!", None,
  "Felfelé nyílik (konvex); zérushelyek $\\pm 2$; $y$-tengelymetszet $-4$; "
  "csúcspont $C(0;-4)$; minimum $-4$; értékkészlet $[-4;+\\infty)$."),
]

KOZEP = [
 ("Végezd el a teljes vizsgálatot! " + VIZSG,
  ["$y=x^{2}-6x+8$", "$y=x^{2}+2x-3$"],
  ["Zérushelyek $2$ és $4$; $C(3;-1)$; minimum $-1$; értékkészlet $[-1;+\\infty)$; "
   "$y$-metszet $8$; konvex.",
   "Zérushelyek $1$ és $-3$; $C(-1;-4)$; minimum $-4$; értékkészlet $[-4;+\\infty)$; "
   "$y$-metszet $-3$; konvex."], False),
 ("Végezd el a teljes vizsgálatot! $y=-x^{2}+6x-5$", None,
  "Zérushelyek $1$ és $5$; $C(3;4)$; maximum $4$; értékkészlet $(-\\infty;4]$; "
  "$y$-metszet $-5$; konkáv."),
 ("Végezd el a teljes vizsgálatot! $y=2x^{2}-8x+6$", None,
  "Zérushelyek $1$ és $3$; $C(2;-2)$; minimum $-2$; értékkészlet $[-2;+\\infty)$; "
  "$y$-metszet $6$; konvex."),
 ("Írd át általános alakba!",
  ["$y=(x+3)^{2}-4$", "$y=-(x-2)^{2}+9$"],
  ["$y=x^{2}+6x+5$", "$y=-x^{2}+4x+5$"], True),
 ("Melyik függvény illik a leíráshoz?",
  ["Csúcspontja az origó, felfelé nyílik, karcsúbb az $y=x^{2}$-nél.",
   "Csúcspontja $(0;-2)$, felfelé nyílik, ugyanolyan karcsú, mint $y=x^{2}$.",
   "Csúcspontja $(2;0)$, lefelé nyílik."],
  ["Pl. $y=3x^{2}$.", "$y=x^{2}-2$.", "Pl. $y=-(x-2)^{2}$."], False),
 ("Milyen $c$ esetén <b>érinti</b> az $y=x^{2}-6x+c$ parabola az $x$-tengelyt?",
  None, "$c=9$"),
 ("Milyen $m$ esetén <b>nincs</b> zérushelye az $y=x^{2}+4x+m$ függvénynek?",
  None, "$m&gt;4$"),
 ("Egy szám és a nála $10$-zel kisebb szám szorzata mikor a legkisebb? Mennyi ekkor "
  "a szorzat?", None, "Az $x=5$ helyen; a legkisebb szorzat $-25$."),
 ("Egy téglalap kerülete $24$ méter. Mekkora a lehető legnagyobb területe?",
  None, "$36\\ \\text{m}^{2}$ (a téglalap ekkor $6\\times 6$-os négyzet)."),
 ("Végezd el a teljes vizsgálatot! $y=-2x^{2}+8x-6$", None,
  "Zérushelyek $1$ és $3$; $C(2;2)$; maximum $2$; értékkészlet $(-\\infty;2]$; "
  "$y$-metszet $-6$; konkáv."),
]

NEHEZ = [
 ("Írd fel a parabola egyenletét, ha a csúcspontja $C(2;-3)$, és átmegy a $(0;1)$ ponton!",
  None, "$y=(x-2)^{2}-3=x^{2}-4x+1$"),
 ("Írd fel a parabola egyenletét, ha a zérushelyei $-1$ és $3$, és átmegy az $(1;-8)$ ponton!",
  None, "$y=2(x+1)(x-3)=2x^{2}-4x-6$"),
 ("Egy feldobott tárgy magassága $t$ másodperc múlva $h(t)=-5t^{2}+20t$ méter.",
  ["Mikor és milyen magasan van a legmagasabban?", "Mikor ér földet?"],
  ["A $t=2$ s pillanatban, $20$ méter magasan.", "A $t=4$ s pillanatban."], False),
 ("Milyen $m$ esetén van az $y=x^{2}-2mx+m+6$ parabola csúcspontja az $x$-tengelyen?",
  None, "$m=3$ vagy $m=-2$"),
 ("Hol metszi egymást az $y=x^{2}-4x+7$ parabola és az $y=2x+2$ egyenes?",
  None, "Az $(1;4)$ és az $(5;12)$ pontban."),
]

JOKER = ("<b>Dr. Baljós vírus-kódja.</b> A rendszer az $y=x^{2}-6x+5$ függvény csúcspontját "
         "így számolta: „$u=-\\dfrac{b}{2a}=-\\dfrac{6}{2}=-3$, tehát $C(-3;32)$”. "
         "Hol a hiba, és mi a helyes csúcspont?",
         "A $b=-6$, ezért $u=-\\dfrac{-6}{2}=3$ (nem $-3$). Helyesen $C(3;-4)$.")

GYD_ORAI = [
 ("Oldd meg a másodfokú egyenletet!",
  ["$6x^{2}+42x=0$", "$x^{2}-256=0$", "$2x^{2}-x-6=0$", "$(x+1)(x-5)=16$"],
  ["$x_{1}=0$, $x_{2}=-7$", "$x_{1,2}=\\pm 16$", "$2$ és $-\\dfrac{3}{2}$", "$7$ és $-3$"], True),
 ("Bontsd tényezőkre!",
  ["$x^{2}-11x+28$", "$x^{2}+13x+42$"], ["$(x-4)(x-7)$", "$(x+6)(x+7)$"], True),
 ("Vizsgáld meg az $x^{2}+10x+m=0$ <b>egyenlet</b> megoldásainak számát és típusát "
  "az $m$ paraméter függvényében!", None,
  "$m&lt;25$: két különböző valós; $m=25$: egy kettős ($x=-5$); $m&gt;25$: két komplex."),
 ("Az $x^{2}-11x+28=0$ egyenlet megoldása nélkül számítsd ki!",
  ["$x_{1}+x_{2}$ és $x_{1}\\cdot x_{2}$", "$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$",
   "$x_{1}^{2}+x_{2}^{2}$"],
  ["$11$ és $28$", "$\\dfrac{11}{28}$", "$65$"], True),
 ("Adott az $y=x^{2}-4x+3$ függvény. " + VIZSG, None,
  "Zérushelyek $1$ és $3$; $C(2;-1)$; minimum $-1$; értékkészlet $[-1;+\\infty)$; konvex."),
 ("Adott az $y=-x^{2}+2x+8$ függvény. " + VIZSG, None,
  "Zérushelyek $-2$ és $4$; $C(1;9)$; maximum $9$; értékkészlet $(-\\infty;9]$; konkáv."),
 ("Oldd meg a bikvadratikus egyenletet! $x^{4}-29x^{2}+100=0$", None, "$\\pm 5$ és $\\pm 2$"),
 ("Oldd meg a komplex számok halmazán! $x^{4}-7x^{2}-18=0$", None,
  "$\\pm 3$ és $\\pm i\\sqrt{2}$"),
 ("Írj fel másodfokú egyenletet, amelynek megoldásai a $-2$ és a $7$ számok!",
  None, "$x^{2}-5x-14=0$"),
 ("Egy téglalap kerülete $28$ cm. Mekkora a lehető legnagyobb területe?",
  None, "$49\\ \\text{cm}^{2}$ (a téglalap ekkor $7\\times 7$-es négyzet)."),
]

GYD_OTTHON = [
 ("Oldd meg!",
  ["$4x^{2}-100=0$", "$x^{2}+8x=0$", "$5x^{2}-13x-6=0$"],
  ["$x_{1,2}=\\pm 5$", "$x_{1}=0$, $x_{2}=-8$", "$3$ és $-\\dfrac{2}{5}$"], True),
 ("Bontsd tényezőkre! $3x^{2}-21x+30$", None, "$3(x-2)(x-5)$"),
 ("Milyen $m$ esetén van az $x^{2}-12x+m=0$ egyenletnek kettős gyöke? Mennyi ekkor a gyök?",
  None, "$m=36$, és a kettős gyök $x=6$."),
 ("Adott az $y=x^{2}+2x-8$ függvény. " + VIZSG, None,
  "Zérushelyek $2$ és $-4$; $C(-1;-9)$; minimum $-9$; értékkészlet $[-9;+\\infty)$; konvex."),
 ("Oldd meg! $x^{4}-20x^{2}+64=0$", None, "$\\pm 4$ és $\\pm 2$"),
 ("A $3x^{2}-9x+6=0$ egyenletre — megoldás nélkül: $x_{1}+x_{2}$ és $x_{1}\\cdot x_{2}$.",
  None, "$3$ és $2$"),
]

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
 '    <h2 id="gyak-dolgozat">📝 Gyakorló dolgozat — egyenletek és függvény</h2>\n    ' + DISZKLEMER +
 '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYD_ORAI, "gyd") +
 '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYD_OTTHON, "gydh"),
]

ut = oldal(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
           fajl="feladatok-masodfoku-fuggveny.html", cim="A másodfokú függvény",
           temakor="Másodfokú egyenletek és függvények",
           alcim="Csúcspont és kanonikus alak, zérushelyek, szélsőérték és értékkészlet, "
                 "teljes függvényvizsgálat és szélsőérték-feladatok — a végén gyakorló "
                 "dolgozattal az egyenletekre és a függvényre együtt.",
           sections_html="\n".join(body),
           prev="tananyag-fuggvenyvizsgalat.html", prevc="A másodfokú függvény vizsgálata",
           nxt="tananyag-masodfoku-egyenlotlensegek.html", nxtc="Másodfokú egyenlőtlenségek")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYD_ORAI), "+", len(GYD_OTTHON))
