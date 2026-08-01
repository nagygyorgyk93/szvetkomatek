# -*- coding: utf-8 -*-
"""2e/01 — „A" altéma feladatgyűjtemény: hatványozás + hatványfüggvény.
Kiképzési Adattár. Végeredmény = KIZÁRÓLAG a végső válasz."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS (sympy) ==============================
from sympy import (symbols, Rational, simplify, sqrt, Integer, nsimplify, S)
a, b, c = symbols('a b c', positive=True)
n = symbols('n', integer=True, nonnegative=True)
E = []
def ell(nev, kif, vart):
    if simplify(kif - vart) != 0:
        E.append((nev, simplify(kif)))

R = Rational
ell("A1", R(2)**5, 32); ell("A1b", R(-3)**3, -27); ell("A1c", R(-2)**4, 16)
ell("A1d", -R(2)**4, -16); ell("A1e", R(2,3)**3, R(8,27)); ell("A1f", R(-1)**99, -1)
ell("A3b", R(3)**-2, R(1,9)); ell("A3c", R(1,2)**-3, 8); ell("A3d", R(3,4)**-2, R(16,9))
ell("A3e", R(-5)**-2, R(1,25)); ell("A3f", R(10)**-3, R(1,1000))
ell("A5a", a**3*a**-5, a**-2); ell("A5b", b**-2/b**-6, b**4)
ell("A5c", (a**-2)**-3, a**6); ell("A5d", (a/b)**-3, b**3/a**3)
ell("A6a", R(2)**-1+R(2)**-2, R(3,4)); ell("A6b", R(3)**-1-R(3)**-2, R(2,9))
ell("A6c", R(1,3)**-2+R(1,2)**-3, 17); ell("A6d", R(5)**-2*R(5)**4, 25)
ell("A7a", (-2)**4, 16); ell("A7b", (-2)**3, -8); ell("A7c", R(1,2)**4, R(1,16))
ell("K1a", R(2,5)**2-R(2,5**2)+R(-2,5)**2-R(5,2)**-2, R(2,25))
ell("K1b", R(1,3)**-2-R(-1,2)**-3+R(-2)**-2, R(69,4))
ell("K1c", (R(2)**-1+R(3)**-1)**-1, R(6,5))
ell("K2a", (a**-2/b**3)**2*(a**5*b**-1/b**2), a/b**9)
ell("K2b", (2*a**-1*b**2/c**-3)**3, 8*b**6*c**9/a**3)
ell("K2c", (a**2*b**-3)**-2/((a**-1*b**2)**3), 1/a)
ell("K3a", R(-2)**5*R(3)**4/(R(2)**3*R(3)**6), R(-4,9))
ell("K3b", R(6)**5/(R(2)**3*R(3)**4), 12)
ell("K3c", R(15)**4*R(4)**3/(R(10)**4*R(6)**3), R(3,2))
ell("K4a", simplify((2**(n+3)+2**n)/2**(n+1)), R(9,2))
ell("K4b", simplify((5**(n+2)-5**(n+1))/5**n), 20)
ell("K4c", simplify(9**n*3**(n+1)/27**n), 3)
ell("K8c", (3*R(10)**5)*(2*R(10)**-8), 6*R(10)**-3)
ell("K8d", 8*R(10)**6/(4*R(10)**-2), 2*R(10)**8)
ell("N1", ((a**-2*b**3)/(a**4*b**-1))**-2*(a**-3/b**2)**3, a**3/b**14)
ell("N2", simplify(4**(n+1)*8**(n-1)/2**(5*n-2)), 2)
ell("N3", (R(2,3)**-2-R(3,4)**-1)**-1, R(12,11))
assert Integer(3)**200 > Integer(2)**300, "N4"
ell("JOK", (2*a**-2/b**3)**-2, a**4*b**6/4)
assert not E, E
assert R(9,10)**10 < R(9,10)**5 < R(9,10)**2
assert R(-1,2)**3 < R(-1,2)**4 < R(-1,2)**2
assert R(6,10)**2 > R(6,10)**4 and R(15,10)**2 < R(15,10)**4
assert R(2,3)**5 < R(2,3)**3 and R(3)**-2 > R(3)**-3
print("sympy önteszt: OK")

# ============================== FELADATOK ==============================

ALAP = [
 ("Számítsd ki a hatványok pontos értékét!",
  ["$2^{5}$", "$(-3)^{3}$", "$(-2)^{4}$", "$-2^{4}$",
   "$\\left(\\dfrac{2}{3}\\right)^{3}$", "$(-1)^{99}$"],
  ["$32$", "$-27$", "$16$", "$-16$", "$\\dfrac{8}{27}$", "$-1$"], True),

 ("Írd fel egyetlen hatvány alakjában!",
  ["$3^{4}\\cdot 3^{7}$", "$\\dfrac{5^{9}}{5^{4}}$", "$\\left(2^{3}\\right)^{5}$",
   "$7^{6}\\cdot 7$", "$\\dfrac{a^{12}}{a^{12}}$ $(a\\neq 0)$", "$\\left((-4)^{2}\\right)^{3}$"],
  ["$3^{11}$", "$5^{5}$", "$2^{15}$", "$7^{7}$", "$1$", "$4^{6}$"], True),

 ("Számítsd ki a pontos értéket!",
  ["$5^{0}$", "$3^{-2}$", "$\\left(\\dfrac{1}{2}\\right)^{-3}$",
   "$\\left(\\dfrac{3}{4}\\right)^{-2}$", "$(-5)^{-2}$", "$10^{-3}$"],
  ["$1$", "$\\dfrac{1}{9}$", "$8$", "$\\dfrac{16}{9}$", "$\\dfrac{1}{25}$", "$\\dfrac{1}{1000}$"], True),

 ("Igaz vagy hamis? A hamis állítást javítsd ki!",
  ["$-3^{2}=9$", "$(-3)^{2}=9$", "$2^{-3}=-8$",
   "$\\left(\\dfrac{2}{5}\\right)^{-1}=\\dfrac{5}{2}$", "$0^{0}=1$", "$(-1)^{100}=1$"],
  ["Hamis, helyesen $-9$.", "Igaz.", "Hamis, helyesen $\\dfrac{1}{8}$.", "Igaz.",
   "Hamis, a $0^{0}$ nincs értelmezve.", "Igaz."], False),

 ("Hozd egyszerűbb alakra! $(a,b&gt;0)$",
  ["$a^{3}\\cdot a^{-5}$", "$\\dfrac{b^{-2}}{b^{-6}}$", "$\\left(a^{-2}\\right)^{-3}$",
   "$\\left(\\dfrac{a}{b}\\right)^{-3}$"],
  ["$\\dfrac{1}{a^{2}}$", "$b^{4}$", "$a^{6}$", "$\\dfrac{b^{3}}{a^{3}}$"], True),

 ("Számítsd ki a kifejezés pontos értékét!",
  ["$2^{-1}+2^{-2}$", "$3^{-1}-3^{-2}$",
   "$\\left(\\dfrac{1}{3}\\right)^{-2}+\\left(\\dfrac{1}{2}\\right)^{-3}$", "$5^{-2}\\cdot 5^{4}$"],
  ["$\\dfrac{3}{4}$", "$\\dfrac{2}{9}$", "$17$", "$25$"], True),

 ("Legyen $f(x)=x^{4}$ és $g(x)=x^{3}$. Számítsd ki a függvényértékeket!",
  ["$f(-2)$", "$g(-2)$", "$f\\left(\\dfrac{1}{2}\\right)$", "$g(-1)$"],
  ["$16$", "$-8$", "$\\dfrac{1}{16}$", "$-1$"], True),

 ("Döntsd el, hogy a függvény páros, páratlan, vagy egyik sem!",
  ["$y=x^{6}$", "$y=x^{7}$", "$y=x^{-2}$", "$y=x^{-3}$", "$y=x^{10}$"],
  ["Páros.", "Páratlan.", "Páros.", "Páratlan.", "Páros."], True),

 ("Add meg a függvény értelmezési tartományát és értékkészletét!",
  ["$y=x^{2}$", "$y=x^{3}$", "$y=\\dfrac{1}{x}$", "$y=\\dfrac{1}{x^{2}}$"],
  ["$D=\\mathbb{R}$, $\\mathcal{R}=[0,+\\infty)$",
   "$D=\\mathbb{R}$, $\\mathcal{R}=\\mathbb{R}$",
   "$D=\\mathbb{R}\\setminus\\{0\\}$, $\\mathcal{R}=\\mathbb{R}\\setminus\\{0\\}$",
   "$D=\\mathbb{R}\\setminus\\{0\\}$, $\\mathcal{R}=(0,+\\infty)$"], False),

 ("Melyik a nagyobb? Számolás nélkül, a hatványfüggvény tulajdonságai alapján dönts!",
  ["$0{,}6^{2}$ vagy $0{,}6^{4}$", "$1{,}5^{2}$ vagy $1{,}5^{4}$",
   "$\\left(\\dfrac{2}{3}\\right)^{5}$ vagy $\\left(\\dfrac{2}{3}\\right)^{3}$",
   "$3^{-2}$ vagy $3^{-3}$"],
  ["$0{,}6^{2}$", "$1{,}5^{4}$", "$\\left(\\dfrac{2}{3}\\right)^{3}$", "$3^{-2}$"], True),
]

KOZEP = [
 ("Számítsd ki a számkifejezés pontos értékét!",
  ["$\\left(\\dfrac{2}{5}\\right)^{2}-\\dfrac{2}{5^{2}}+\\left(-\\dfrac{2}{5}\\right)^{2}"
   "-\\left(\\dfrac{5}{2}\\right)^{-2}$",
   "$\\left(\\dfrac{1}{3}\\right)^{-2}-\\left(-\\dfrac{1}{2}\\right)^{-3}+(-2)^{-2}$",
   "$\\left(2^{-1}+3^{-1}\\right)^{-1}$"],
  ["$\\dfrac{2}{25}$", "$\\dfrac{69}{4}$", "$\\dfrac{6}{5}$"], False),

 ("Hozd egyszerűbb alakra! $(a,b,c&gt;0)$",
  ["$\\left(\\dfrac{a^{-2}}{b^{3}}\\right)^{2}\\cdot\\dfrac{a^{5}b^{-1}}{b^{2}}$",
   "$\\left(\\dfrac{2a^{-1}b^{2}}{c^{-3}}\\right)^{3}$",
   "$\\dfrac{\\left(a^{2}b^{-3}\\right)^{-2}}{\\left(a^{-1}b^{2}\\right)^{3}}$"],
  ["$\\dfrac{a}{b^{9}}$", "$\\dfrac{8b^{6}c^{9}}{a^{3}}$", "$\\dfrac{1}{a}$"], False),

 ("Számítsd ki a pontos értéket a hatványok közös alapra hozásával!",
  ["$\\dfrac{(-2)^{5}\\cdot 3^{4}}{2^{3}\\cdot 3^{6}}$", "$\\dfrac{6^{5}}{2^{3}\\cdot 3^{4}}$",
   "$\\dfrac{15^{4}\\cdot 4^{3}}{10^{4}\\cdot 6^{3}}$"],
  ["$-\\dfrac{4}{9}$", "$12$", "$\\dfrac{3}{2}$"], False),

 ("Hozd egyszerűbb alakra! $(n\\in\\mathbb{N})$",
  ["$\\dfrac{2^{n+3}+2^{n}}{2^{n+1}}$", "$\\dfrac{5^{n+2}-5^{n+1}}{5^{n}}$",
   "$\\dfrac{9^{n}\\cdot 3^{n+1}}{27^{n}}$"],
  ["$\\dfrac{9}{2}$", "$20$", "$3$"], False),

 ("Igaz-e minden $a,b&gt;0$ esetén? A hamis állításhoz adj ellenpéldát!",
  ["$(a+b)^{2}=a^{2}+b^{2}$", "$(ab)^{3}=a^{3}b^{3}$", "$a^{-1}+b^{-1}=(a+b)^{-1}$",
   "$\\left(a^{2}\\right)^{3}=\\left(a^{3}\\right)^{2}$"],
  ["Hamis; $a=b=1$ esetén $4\\neq 2$.", "Igaz.",
   "Hamis; $a=b=1$ esetén $2\\neq\\dfrac{1}{2}$.", "Igaz, mindkettő $a^{6}$."], False),

 ("Rendezd növekvő sorrendbe!",
  ["$0{,}9^{10}$, $0{,}9^{2}$, $0{,}9^{5}$",
   "$2^{-3}$, $2^{0}$, $2^{-1}$, $2^{2}$",
   "$\\left(-\\dfrac{1}{2}\\right)^{3}$, $\\left(-\\dfrac{1}{2}\\right)^{2}$, "
   "$\\left(-\\dfrac{1}{2}\\right)^{4}$"],
  ["$0{,}9^{10}&lt;0{,}9^{5}&lt;0{,}9^{2}$", "$2^{-3}&lt;2^{-1}&lt;2^{0}&lt;2^{2}$",
   "$\\left(-\\dfrac{1}{2}\\right)^{3}&lt;\\left(-\\dfrac{1}{2}\\right)^{4}"
   "&lt;\\left(-\\dfrac{1}{2}\\right)^{2}$"], False),

 ("Hány valós megoldása van az egyenletnek? Használd a hatványfüggvény grafikonját!",
  ["$x^{4}=16$", "$x^{3}=-8$", "$x^{2}=-4$", "$\\dfrac{1}{x}=0$"],
  ["Kettő: $x=\\pm 2$.", "Egy: $x=-2$.", "Egy sem.", "Egy sem."], False),

 ("Írd normálalakban, illetve végezd el a műveletet!",
  ["$0{,}00045$", "$73\\,000\\,000$", "$\\left(3\\cdot 10^{5}\\right)\\cdot\\left(2\\cdot 10^{-8}\\right)$",
   "$\\dfrac{8\\cdot 10^{6}}{4\\cdot 10^{-2}}$"],
  ["$4{,}5\\cdot 10^{-4}$", "$7{,}3\\cdot 10^{7}$", "$6\\cdot 10^{-3}$", "$2\\cdot 10^{8}$"], True),
]

NEHEZ = [
 ("Hozd egyszerűbb alakra! $(a,b&gt;0)$ "
  "$\\left(\\dfrac{a^{-2}b^{3}}{a^{4}b^{-1}}\\right)^{-2}\\cdot\\left(\\dfrac{a^{-3}}{b^{2}}\\right)^{3}$",
  None, "$\\dfrac{a^{3}}{b^{14}}$"),

 ("Számítsd ki a kifejezés értékét! $(n\\in\\mathbb{N},\\ n\\ge 1)$ "
  "$\\dfrac{4^{n+1}\\cdot 8^{n-1}}{2^{5n-2}}$",
  None, "$2$"),

 ("Számítsd ki a pontos értéket! "
  "$\\left(\\left(\\dfrac{2}{3}\\right)^{-2}-\\left(\\dfrac{3}{4}\\right)^{-1}\\right)^{-1}$",
  None, "$\\dfrac{12}{11}$"),

 ("Melyik a nagyobb: $2^{300}$ vagy $3^{200}$? Számológép nélkül dönts!",
  None, "$3^{200}$ a nagyobb."),
]

JOKER = ("<b>Sinister vírus-kódja.</b> A rendszerbe a következő átalakítás került be — "
         "az eredmény hibás. Keresd meg, melyik lépésnél romlott el, és add meg a helyes "
         "végeredményt! $(a,b&gt;0)$ "
         "$$\\left(\\frac{2a^{-2}}{b^{3}}\\right)^{-2}\\ \\overset{?}{=}\\ "
         "\\frac{2a^{4}}{b^{-6}}\\ =\\ 2a^{4}b^{6}$$",
         "A $2$-es együttható kimaradt a hatványozásból: azt is a $-2$-edik hatványra kell "
         "emelni. Helyesen $\\dfrac{a^{4}b^{6}}{4}$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
           fajl="feladatok-hatvanyozas.html", cim="Hatványozás",
           temakor="Hatványozás, gyökvonás, komplex számok",
           alcim="Hatványazonosságok, egész kitevő, összetett szám- és betűs kifejezések, "
                 "valamint a hatványfüggvény grafikonjának olvasása. A végeredmény minden "
                 "feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-hatvanyfuggveny.html", prevc="A hatványfüggvény és grafikonja",
           nxt="tananyag-gyokvonas.html", nxtc="Gyökvonás")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ), "+ Joker")
