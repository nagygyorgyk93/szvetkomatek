# -*- coding: utf-8 -*-
"""2e/02 — A altema feladatgyujtemeny: a masodfoku egyenlet. + gyakorlo ELLENORZO."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, oldal, DISZKLEMER

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import symbols, Rational as R, solve, simplify, factor, expand, im, re as _re, I, sqrt, Eq
x, m, k, t, u = symbols('x m k t u')
def S(e): return sorted(solve(e, x), key=lambda z: (im(z), _re(z)))
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
P = [
 ("A1a", S(x**2-49), [-7, 7]), ("A1b", S(3*x**2-75), [-5, 5]),
 ("A1c", S(x**2+2*x), [-2, 0]), ("A1d", S(4*x**2-12*x), [0, 3]),
 ("A2a", S(2*x**2-50), [-5, 5]), ("A2b", S(5*x**2+15*x), [-3, 0]),
 ("A2d", S(9*x**2-1), [R(-1,3), R(1,3)]),
 ("A3a", S(x**2-5*x+6), [2, 3]), ("A3b", S(x**2+7*x+12), [-4, -3]),
 ("A3c", S(x**2-x-6), [-2, 3]), ("A3d", S(x**2+2*x-8), [-4, 2]),
 ("A4a", S(2*x**2-5*x+2), [R(1,2), 2]), ("A4b", S(3*x**2-7*x+2), [R(1,3), 2]),
 ("A4c", S(2*x**2+x-1), [-1, R(1,2)]),
 ("A5a", S((x-1)*(x+4)-6), [-5, 2]), ("A5b", S((x+2)**2-9), [-5, 1]),
 ("A5c", S(x*(x-3)-10), [-2, 5]),
 ("A7a", 16-12, 4), ("A7b", 16-16, 0), ("A7c", 16-20, -4), ("A7d", 9+8, 17),
 ("A9a", S(x**2+9), [-3*I, 3*I]), ("A9b", S(x**2-2*x+2), [1-I, 1+I]),
 ("A9c", S(x**2+4*x+13), [-2-3*I, -2+3*I]),
 ("A12c", R(6, 8), R(3,4)), ("A12d", 36-2*8, 20),
 ("A13a", expand((x-2)*(x-5)), x**2-7*x+10), ("A13b", expand((x+1)*(x-4)), x**2-3*x-4),
 ("A13c", expand((x+3)*(x+5)), x**2+8*x+15),
 ("A14a", factor(x**2-7*x+12), (x-3)*(x-4)), ("A14b", factor(x**2+x-6), (x-2)*(x+3)),
 ("A14c", factor(x**2-16), (x-4)*(x+4)), ("A14d", factor(x**2-10*x+25), (x-5)**2),
 ("A15a", factor(2*x**2-8*x+6), 2*(x-1)*(x-3)),
 ("A15b", factor(3*x**2+3*x-18), 3*(x-2)*(x+3)),
 ("A16a", S(x**4-5*x**2+4), [-2, -1, 1, 2]), ("A16b", S(x**4-10*x**2+9), [-3, -1, 1, 3]),
 ("A17a", S(x**4-3*x**2-4), [-I, -2, 2, I]), ("A17b", S(x**4+3*x**2-4), [-2*I, -1, 1, 2*I]),
 ("K1a", S(x**2-13*x+40), [5, 8]), ("K1b", S(2*x**2-11*x+12), [R(3,2), 4]),
 ("K1c", S(3*x**2+2*x-8), [-2, R(4,3)]),
 ("K2a", S(x**2/2-3*x/2+1), [1, 2]), ("K2b", S(R(1,2)*x**2-2*x+R(3,2)), [1, 3]),
 ("K3a", S((x**2+2*x)/3-x-4), [-3, 4]), ("K3b", S((x-2)*(x+5)-3*x-4), [-sqrt(14), sqrt(14)]),
 ("K3c", S((x-1)**2+(x+1)**2-34), [-4, 4]),
 ("K5", solve(Eq(m+2, 8), m), [6]),
 ("K6c", R(4, R(3,2)), R(8,3)), ("K6d", 16-3, 13),
 ("K7", 25-16, 9),
 ("K8", expand((x-4)*(x-6)), x**2-10*x+24),
 ("K11a", S(x**2-6*x+25), [3-4*I, 3+4*I]),
 ("K11b", S(2*x**2+2*x+5), [R(-1,2)-R(3,2)*I, R(-1,2)+R(3,2)*I]),
 ("K13", S(x**2-7*x+12), [3, 4]),
 ("K14a", S(4*x**4-17*x**2+4), [-2, R(-1,2), R(1,2), 2]),
 ("K14b", S(x**4-8*x**2-9), [-I, -3, 3, I]),
 ("K15", sorted(solve((x**2-3)**2-5*(x**2-3)+6, x), key=lambda z: (im(z), _re(z))),
  [-sqrt(6), -sqrt(5), sqrt(5), sqrt(6)]),
 ("K16", expand((x**2-4)*(x**2-9)), x**4-13*x**2+36),
 ("N1", sorted(solve(Eq(m**2-2*(m-1), 10), m)), [-2, 4]),
 ("N2", 3*6, 18),
 ("N3", S(2*x**2-3*x-2), [R(-1,2), 2]),
 ("N4", sorted(solve(t**2-15*t+56, t)), [7, 8]),
 ("N5", sorted(solve(t**2-17*t+60, t)), [5, 12]),
 ("N6", 1*5, 5),
 ("GY1a", S(x**2-121), [-11, 11]), ("GY1b", S(15*x-3*x**2), [0, 5]),
 ("GY1c", S(2*x**2-9*x-5), [R(-1,2), 5]), ("GY1d", S((x-1)*(x+6)-8), [-7, 2]),
 ("GY2", factor(x**2+4*x-21), (x-3)*(x+7)),
 ("GY3", factor(2*x**2-14*x+20), 2*(x-2)*(x-5)),
 ("GY5k", solve(Eq(2*k-4, 0), k), [2]), ("GY5c", 3*2-21, -15),
 ("GY5x", S(x**2-15), [-sqrt(15), sqrt(15)]),
 ("GY6", expand((x+4)*(x-6)), x**2-2*x-24),
 ("GY7", 81-2*14, 53),
 ("GYH1a", S(x**2-144), [-12, 12]), ("GYH1b", S(7*x**2+21*x), [-3, 0]),
 ("GYH1c", S(3*x**2-10*x+3), [R(1,3), 3]),
 ("GYH2a", factor(x**2-2*x-35), (x-7)*(x+5)), ("GYH2b", factor(x**2+9*x+20), (x+4)*(x+5)),
 ("GYH3", solve(Eq(100-4*m, 0), m), [25]),
 ("GYH4", R(6, 5), R(6,5)),
 ("GYH5", expand(2*(x-R(1,2))*(x+3)), 2*x**2+5*x-3),
 ("GYH6", S(x**2-4*x+29), [2-5*I, 2+5*I]),
]
for n, g, w in P:
    chk(n, g, w)
assert not E, E[:4]
print("sympy önteszt: OK")

# ============================== FELADATOK ==============================

ALAP = [
 ("Oldd meg a hiányos másodfokú egyenletet!",
  ["$x^{2}-49=0$", "$3x^{2}-75=0$", "$x^{2}+2x=0$", "$4x^{2}-12x=0$"],
  ["$x_{1,2}=\\pm 7$", "$x_{1,2}=\\pm 5$", "$x_{1}=0$, $x_{2}=-2$", "$x_{1}=0$, $x_{2}=3$"], True),
 ("Oldd meg!",
  ["$2x^{2}=50$", "$5x^{2}+15x=0$", "$x^{2}=0$", "$9x^{2}-1=0$"],
  ["$x_{1,2}=\\pm 5$", "$x_{1}=0$, $x_{2}=-3$", "$x=0$ (kettős)",
   "$x_{1,2}=\\pm\\dfrac{1}{3}$"], True),
 ("Oldd meg a megoldóképlettel!",
  ["$x^{2}-5x+6=0$", "$x^{2}+7x+12=0$", "$x^{2}-x-6=0$", "$x^{2}+2x-8=0$"],
  ["$2$ és $3$", "$-3$ és $-4$", "$3$ és $-2$", "$2$ és $-4$"], True),
 ("Oldd meg! (Vigyázz: a főegyüttható nem $1$.)",
  ["$2x^{2}-5x+2=0$", "$3x^{2}-7x+2=0$", "$2x^{2}+x-1=0$"],
  ["$2$ és $\\dfrac{1}{2}$", "$2$ és $\\dfrac{1}{3}$", "$\\dfrac{1}{2}$ és $-1$"], True),
 ("Rendezd nullára, majd oldd meg!",
  ["$(x-1)(x+4)=6$", "$(x+2)^{2}=9$", "$x(x-3)=10$"],
  ["$2$ és $-5$", "$1$ és $-5$", "$5$ és $-2$"], True),
 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["Az $x^{2}=16$ egyenletnek egy megoldása van.",
   "Az $x^{2}+4=0$ egyenletnek nincs valós megoldása.",
   "$x^{2}=5x$-ből következik, hogy $x=5$.",
   "Minden másodfokú egyenletnek van valós megoldása."],
  ["Hamis: kettő van, $\\pm 4$.", "Igaz (a komplex megoldások $\\pm 2i$).",
   "Hamis: az $x=0$ is megoldás — ne ossz $x$-szel!",
   "Hamis: ha $D&lt;0$, a megoldások komplexek."], False),
 ("Számítsd ki a diszkriminánst!",
  ["$x^{2}-4x+3$", "$x^{2}-4x+4$", "$x^{2}-4x+5$", "$2x^{2}+3x-1$"],
  ["$D=4$", "$D=0$", "$D=-4$", "$D=17$"], True),
 ("Hány valós megoldása van? (Csak a diszkriminánst számold ki!)",
  ["$x^{2}+6x+9=0$", "$x^{2}+x+1=0$", "$3x^{2}-2x-1=0$"],
  ["Egy (kettős): $D=0$.", "Egy sem: $D=-3&lt;0$ (két komplex megoldás).",
   "Kettő: $D=16&gt;0$."], True),
 ("Oldd meg a komplex számok halmazán!",
  ["$x^{2}+9=0$", "$x^{2}-2x+2=0$", "$x^{2}+4x+13=0$"],
  ["$x_{1,2}=\\pm 3i$", "$x_{1,2}=1\\pm i$", "$x_{1,2}=-2\\pm 3i$"], True),
 ("Az $x^{2}+6x+m=0$ egyenletben $m$ valós paraméter. Milyen $m$ esetén van az egyenletnek",
  ["két különböző valós megoldása?", "egy (kettős) valós megoldása?", "két komplex megoldása?"],
  ["$m&lt;9$", "$m=9$", "$m&gt;9$"], False),
 ("Olvasd le a Viète-képletekkel a gyökök összegét és szorzatát!",
  ["$x^{2}-7x+10=0$", "$x^{2}+3x-4=0$", "$2x^{2}-6x+4=0$"],
  ["összeg $7$, szorzat $10$", "összeg $-3$, szorzat $-4$", "összeg $3$, szorzat $2$"], True),
 ("Az $x^{2}-6x+8=0$ egyenlet megoldása <b>nélkül</b> számítsd ki!",
  ["$x_{1}+x_{2}$", "$x_{1}\\cdot x_{2}$",
   "$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$", "$x_{1}^{2}+x_{2}^{2}$"],
  ["$6$", "$8$", "$\\dfrac{3}{4}$", "$20$"], True),
 ("Írj fel másodfokú egyenletet, amelynek megoldásai:",
  ["$2$ és $5$", "$-1$ és $4$", "$-3$ és $-5$"],
  ["$x^{2}-7x+10=0$", "$x^{2}-3x-4=0$", "$x^{2}+8x+15=0$"], True),
 ("Bontsd tényezőkre!",
  ["$x^{2}-7x+12$", "$x^{2}+x-6$", "$x^{2}-16$", "$x^{2}-10x+25$"],
  ["$(x-3)(x-4)$", "$(x+3)(x-2)$", "$(x-4)(x+4)$", "$(x-5)^{2}$"], True),
 ("Bontsd tényezőkre! (A főegyüttható nem $1$ — ne felejtsd el kiemelni!)",
  ["$2x^{2}-8x+6$", "$3x^{2}+3x-18$"],
  ["$2(x-1)(x-3)$", "$3(x+3)(x-2)$"], True),
 ("Oldd meg a bikvadratikus egyenletet a valós számok halmazán!",
  ["$x^{4}-5x^{2}+4=0$", "$x^{4}-10x^{2}+9=0$"],
  ["$\\pm 1$ és $\\pm 2$", "$\\pm 1$ és $\\pm 3$"], True),
 ("Oldd meg a bikvadratikus egyenletet a komplex számok halmazán!",
  ["$x^{4}-3x^{2}-4=0$", "$x^{4}+3x^{2}-4=0$"],
  ["$\\pm 2$ és $\\pm i$", "$\\pm 1$ és $\\pm 2i$"], True),
 ("Igaz vagy hamis?",
  ["Minden bikvadratikus egyenletnek négy valós gyöke van.",
   "Ha a $t=x^{2}$ helyettesítés után kapott $t$ érték negatív, a hozzá tartozó $x$ komplex.",
   "A $t=x^{2}$ helyettesítés után elsőfokú egyenletet kapunk."],
  ["Hamis: lehetnek komplex gyökei is.", "Igaz.",
   "Hamis: <b>másodfokú</b> egyenletet kapunk."], False),
]

KOZEP = [
 ("Oldd meg!",
  ["$x^{2}-13x+40=0$", "$2x^{2}-11x+12=0$", "$3x^{2}+2x-8=0$"],
  ["$5$ és $8$", "$4$ és $\\dfrac{3}{2}$", "$\\dfrac{4}{3}$ és $-2$"], True),
 ("Szorozz fel, majd oldd meg!",
  ["$\\dfrac{x^{2}}{2}-\\dfrac{3x}{2}+1=0$", "$0{,}5x^{2}-2x+1{,}5=0$"],
  ["$1$ és $2$", "$1$ és $3$"], True),
 ("Rendezd, majd oldd meg!",
  ["$\\dfrac{x^{2}+2x}{3}=x+4$", "$(x-2)(x+5)=3x+4$", "$(x-1)^{2}+(x+1)^{2}=34$"],
  ["$4$ és $-3$", "$x_{1,2}=\\pm\\sqrt{14}$", "$x_{1,2}=\\pm 4$"], False),
 ("Paraméteres feladatok:",
  ["Milyen $m$ esetén van az $x^{2}-2x+m-3=0$ egyenletnek két különböző valós megoldása?",
   "Milyen $m$ esetén van az $x^{2}+mx+9=0$ egyenletnek kettős gyöke?"],
  ["$m&lt;4$", "$m=6$ vagy $m=-6$"], False),
 ("Az $x^{2}-(m+2)x+3m=0$ egyenletben $m$ valós paraméter. Milyen $m$ esetén lesz "
  "a gyökök összege $8$?", None, "$m=6$"),
 ("A $2x^{2}-8x+3=0$ egyenlet megoldása nélkül számítsd ki!",
  ["$x_{1}+x_{2}$", "$x_{1}\\cdot x_{2}$",
   "$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$", "$x_{1}^{2}+x_{2}^{2}$"],
  ["$4$", "$\\dfrac{3}{2}$", "$\\dfrac{8}{3}$", "$13$"], True),
 ("Az $x^{2}-5x+4=0$ egyenlet megoldása nélkül számítsd ki $\\left(x_{1}-x_{2}\\right)^{2}$ "
  "értékét! (Útmutató: $\\left(x_{1}-x_{2}\\right)^{2}=\\left(x_{1}+x_{2}\\right)^{2}-4x_{1}x_{2}$.)",
  None, "$9$"),
 ("Írj fel másodfokú egyenletet, amelynek gyökei az $x^{2}-5x+6=0$ egyenlet gyökeinek "
  "<b>kétszeresei</b>!", None, "$x^{2}-10x+24=0$"),
 ("Egyszerűsítsd a törtet szorzattá alakítás után! $\\dfrac{x^{2}-9}{x^{2}-x-6}$",
  None, "$\\dfrac{x+3}{x+2}$ &nbsp;(ahol $x\\neq 3$ és $x\\neq -2$)"),
 ("Egyszerűsítsd! $\\dfrac{x^{2}-5x+6}{x^{2}-4}$",
  None, "$\\dfrac{x-3}{x+2}$ &nbsp;(ahol $x\\neq 2$ és $x\\neq -2$)"),
 ("Oldd meg a komplex számok halmazán!",
  ["$x^{2}-6x+25=0$", "$2x^{2}+2x+5=0$"],
  ["$x_{1,2}=3\\pm 4i$", "$x_{1,2}=-\\dfrac{1}{2}\\pm\\dfrac{3}{2}i$"], True),
 ("Igaz-e? Indokolj!",
  ["Ha $D&gt;0$, akkor a gyökök összege pozitív.",
   "Ha $x_{1}x_{2}&lt;0$, akkor a két gyök különböző előjelű.",
   "Ha $D=0$, akkor a trinom teljes négyzet."],
  ["Hamis: az összeg $-\\dfrac{b}{a}$, ez lehet negatív is.",
   "Igaz: negatív szorzat csak ellentétes előjelű tényezőkből jöhet.",
   "Igaz: ekkor $ax^{2}+bx+c=a\\left(x-x_{0}\\right)^{2}$."], False),
 ("Az $x^{2}-7x+12=0$ egyenlet gyökeinek <b>előjelét</b> döntsd el megoldás nélkül, "
  "a Viète-képletek segítségével!", None,
  "Mindkét gyök pozitív (a szorzat $12&gt;0$, az összeg $7&gt;0$)."),
 ("Oldd meg a bikvadratikus egyenletet!",
  ["$4x^{4}-17x^{2}+4=0$", "$x^{4}-8x^{2}-9=0$ (a komplex számok halmazán)"],
  ["$\\pm 2$ és $\\pm\\dfrac{1}{2}$", "$\\pm 3$ és $\\pm i$"], True),
 ("Alkalmazd a helyettesítés módszerét! $\\left(x^{2}-3\\right)^{2}-5\\left(x^{2}-3\\right)+6=0$",
  None, "$x_{1,2}=\\pm\\sqrt{5}$ és $x_{3,4}=\\pm\\sqrt{6}$"),
 ("Írj fel bikvadratikus egyenletet, amelynek gyökei $\\pm 2$ és $\\pm 3$!",
  None, "$x^{4}-13x^{2}+36=0$"),
]

NEHEZ = [
 ("Az $x^{2}-mx+m-1=0$ egyenletben $m$ valós paraméter. Milyen $m$ esetén lesz "
  "$x_{1}^{2}+x_{2}^{2}=10$?", None, "$m=4$ vagy $m=-2$"),
 ("Az $x^{2}-9x+m=0$ egyenlet egyik gyöke a másik <b>kétszerese</b>. Mennyi $m$, "
  "és mik a gyökök?", None, "$m=18$; a gyökök $3$ és $6$."),
 ("Oldd meg! $\\dfrac{1}{x-1}+\\dfrac{1}{x+1}=\\dfrac{4}{3}$ &nbsp;$(x\\neq\\pm 1)$",
  None, "$x_{1}=2$, $x_{2}=-\\dfrac{1}{2}$"),
 ("Két szám összege $15$, szorzatuk $56$. Melyik ez a két szám?", None, "$7$ és $8$."),
 ("Egy téglalap kerülete $34$ cm, területe $60\\ \\text{cm}^{2}$. Mekkorák az oldalai?",
  None, "$12$ cm és $5$ cm."),
 ("Az $x^{2}-6x+c=0$ egyenlet egyik gyöke a másik <b>ötszöröse</b>. Mennyi $c$?",
  None, "$c=5$ (a gyökök $1$ és $5$)."),
]

JOKER = ("<b>Dr. Baljós vírus-kódja.</b> A rendszer a következő szorzattá alakítást adta ki. "
         "Hol a hiba, és mi a helyes alak? "
         "$$3x^{2}-12x+9\\ \\overset{?}{=}\\ (x-1)(x-3)$$",
         "A $3$-as főegyüttható kimaradt. Helyesen $3(x-1)(x-3)$ "
         "(kibontva valóban $3x^{2}-12x+9$).")

GYE_ORAI = [
 ("Oldd meg a másodfokú egyenletet!",
  ["$x^{2}-121=0$", "$15x-3x^{2}=0$", "$2x^{2}-9x-5=0$", "$(x-1)(x+6)=8$"],
  ["$x_{1,2}=\\pm 11$", "$x_{1}=0$, $x_{2}=5$", "$5$ és $-\\dfrac{1}{2}$", "$2$ és $-7$"], True),
 ("Bontsd tényezőkre! $x^{2}+4x-21$", None, "$(x-3)(x+7)$"),
 ("Bontsd tényezőkre! $2x^{2}-14x+20$", None, "$2(x-2)(x-5)$"),
 ("Milyen $m$ esetén van az $x^{2}-8x+m=0$ egyenletnek komplex megoldása?", None, "$m&gt;16$"),
 ("Az $x^{2}-(2k-4)x+3k-21=0$ egyenlet gyökei ellentett számok. Mennyi $k$, és mik a gyökök?",
  None, "$k=2$; az egyenlet $x^{2}-15=0$, a gyökök $\\pm\\sqrt{15}$."),
 ("Írj fel másodfokú egyenletet, amelynek megoldásai a $-4$ és a $6$ számok!",
  None, "$x^{2}-2x-24=0$"),
 ("Az $x^{2}-9x+14=0$ egyenlet megoldása nélkül számítsd ki!",
  ["$x_{1}+x_{2}$", "$x_{1}\\cdot x_{2}$", "$x_{1}^{2}+x_{2}^{2}$"],
  ["$9$", "$14$", "$53$"], True),
 ("Igaz vagy hamis? A hamisat javítsd ki!",
  ["$x^{2}=25$-ből következik, hogy $x=5$.",
   "Ha $D=0$, akkor egy kettős gyök van.",
   "Az $x^{2}+1=0$ egyenletnek nincs komplex megoldása.",
   "A trinom szorzattá alakításánál a főegyüttható elhagyható."],
  ["Hamis: $x_{1,2}=\\pm 5$.", "Igaz.", "Hamis: $x_{1,2}=\\pm i$.",
   "Hamis: $ax^{2}+bx+c=a\\left(x-x_{1}\\right)\\left(x-x_{2}\\right)$."], False),
]

GYE_OTTHON = [
 ("Oldd meg!",
  ["$x^{2}-144=0$", "$7x^{2}+21x=0$", "$3x^{2}-10x+3=0$"],
  ["$x_{1,2}=\\pm 12$", "$x_{1}=0$, $x_{2}=-3$", "$3$ és $\\dfrac{1}{3}$"], True),
 ("Bontsd tényezőkre!",
  ["$x^{2}-2x-35$", "$x^{2}+9x+20$"], ["$(x-7)(x+5)$", "$(x+4)(x+5)$"], True),
 ("Milyen $m$ esetén van az $x^{2}+10x+m=0$ egyenletnek kettős gyöke? Mennyi ekkor a gyök?",
  None, "$m=25$, és a kettős gyök $x=-5$."),
 ("A $2x^{2}-12x+10=0$ egyenletre — megoldás nélkül:",
  ["$x_{1}+x_{2}$", "$x_{1}\\cdot x_{2}$", "$\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$"],
  ["$6$", "$5$", "$\\dfrac{6}{5}$"], True),
 ("Írj fel másodfokú egyenletet, amelynek gyökei $\\dfrac{1}{2}$ és $-3$!",
  None, "$2x^{2}+5x-3=0$"),
 ("Oldd meg a komplex számok halmazán! $x^{2}-4x+29=0$", None, "$x_{1,2}=2\\pm 5i$"),
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

ut = oldal(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
           fajl="feladatok-masodfoku-egyenletek.html", cim="A másodfokú egyenlet",
           temakor="Másodfokú egyenletek és függvények",
           alcim="Hiányos és teljes egyenletek, diszkrimináns és paraméteres feladatok, "
                 "Viète-képletek, szorzattá alakítás és bikvadratikus egyenletek — a végén "
                 "gyakorló ellenőrzővel. A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-bikvadratikus.html", prevc="Másodfokúra visszavezethető egyenletek",
           nxt="tananyag-masodfoku-fuggveny.html", nxtc="A másodfokú függvény és grafikonja")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker | gyakorló:", len(GYE_ORAI), "+", len(GYE_OTTHON))
