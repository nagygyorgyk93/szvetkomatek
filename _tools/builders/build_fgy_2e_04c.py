# -*- coding: utf-8 -*-
"""2e/04 — C altema feladatgyujtemeny: trigonometrikus fuggvenyek grafikonja,
A·sin(bx+c) alak, egyszeru trigonometrikus egyenletek."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, pi, sqrt, sin, cos, tan, rad, simplify, solve, Symbol
E = []
def chk(n, g, w, tol=None):
    ok = abs(float(g) - w) < tol if tol is not None else simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
# periódusok
for b, p in [(2, pi), (3, 2*pi/3), (R(1, 2), 4*pi), (4, pi/2), (R(2, 3), 3*pi)]:
    chk(f"per{b}", 2*pi/b, p)
chk("pertg2", pi/2, pi/2)
# értékkészletek / amplitúdó
chk("amp1", 3, 3); chk("amp2", abs(-2), 2)
# egyenletmegoldások (ellenőrzés behelyettesítéssel)
chk("e1a", sin(pi/6), R(1, 2));         chk("e1b", sin(5*pi/6), R(1, 2))
chk("e2a", cos(pi/3), R(1, 2));         chk("e2b", cos(5*pi/3), R(1, 2))
chk("e3a", sin(5*pi/4), -sqrt(2)/2);    chk("e3b", sin(7*pi/4), -sqrt(2)/2)
chk("e4a", cos(5*pi/6), -sqrt(3)/2);    chk("e4b", cos(7*pi/6), -sqrt(3)/2)
chk("e5", tan(pi/3), sqrt(3))
chk("e6", tan(3*pi/4), -1)
chk("e7", sin(pi/2), 1); chk("e8", cos(pi), -1); chk("e9", sin(pi), 0)
chk("e10a", sin(2*(pi/12)), R(1, 2));   chk("e10b", sin(2*(5*pi/12)), R(1, 2))
chk("e11a", cos(3*(pi/18)), sqrt(3)/2)
chk("e12a", sin(2*(5*pi/8)), -sqrt(2)/2); chk("e12b", sin(2*(7*pi/8)), -sqrt(2)/2)
chk("e13", tan(2*(pi/8)), 1)
chk("e14a", cos(pi/4 - pi/4), 1)
chk("e15a", sin(pi/3 + pi/6), 1)
# fáziseltolás
chk("f1", -R(-1, 3)/2, R(1, 6))     # 2x − π/3 → jobbra π/6 (együttható-alak)
chk("f2", -R(1, 4)/2, R(-1, 8))
# nehéz
chk("N1a", sin(pi/4), sqrt(2)/2); chk("N1b", cos(pi/4), sqrt(2)/2)
chk("N2", 2*sin(pi/6)**2 - 1, R(-1, 2))
chk("N3a", sin(pi/6), R(1, 2))
chk("N4", 1 - 2*R(1, 2)**2, R(1, 2))
chk("J1", sin(rad(30))*2, 1)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Add meg az $y=\\sin x$ függvény értékkészletét, periódusát és nullahelyeit!", None,
  "ÉK: $[-1;1]$; periódus: $2\\pi$; nullahelyek: $x=k\\pi$, $k\\in\\mathbb{Z}$."),
 ("Add meg az $y=\\cos x$ függvény értékkészletét, periódusát és nullahelyeit!", None,
  "ÉK: $[-1;1]$; periódus: $2\\pi$; nullahelyek: "
  "$x=\\tfrac{\\pi}{2}+k\\pi$, $k\\in\\mathbb{Z}$."),
 ("Add meg az $y=\\operatorname{tg}x$ függvény értelmezési tartományát, "
  "értékkészletét és periódusát!", None,
  "ÉT: $x\\neq\\tfrac{\\pi}{2}+k\\pi$; ÉK: $\\mathbb{R}$; periódus: $\\pi$."),
 ("Melyik páros és melyik páratlan függvény?",
  ["$\\sin x$", "$\\cos x$", "$\\operatorname{tg}x$"],
  ["páratlan ($\\sin(-x)=-\\sin x$)", "páros ($\\cos(-x)=\\cos x$)", "páratlan"], True),
 ("Hol van maximuma és hol minimuma az $y=\\sin x$ függvénynek?", None,
  "Maximum ($1$): $x=\\tfrac{\\pi}{2}+2k\\pi$; minimum ($-1$): "
  "$x=\\tfrac{3\\pi}{2}+2k\\pi$."),
 ("Add meg az amplitúdót és az értékkészletet!",
  ["$y=3\\sin x$", "$y=-2\\cos x$", "$y=\\tfrac12\\sin x$"],
  ["$|A|=3$, ÉK: $[-3;3]$", "$|A|=2$, ÉK: $[-2;2]$ (az $x$-tengelyre tükrözve)",
   "$|A|=\\tfrac12$, ÉK: $\\left[-\\tfrac12;\\tfrac12\\right]$"], True),
 ("Add meg a periódust!",
  ["$y=\\sin 2x$", "$y=\\cos 3x$", "$y=\\sin\\tfrac{x}{2}$"],
  ["$\\pi$", "$\\dfrac{2\\pi}{3}$", "$4\\pi$"], True),
 ("Add meg a periódust!",
  ["$y=\\cos 4x$", "$y=\\operatorname{tg}2x$", "$y=\\sin\\tfrac{2x}{3}$"],
  ["$\\dfrac{\\pi}{2}$", "$\\dfrac{\\pi}{2}$ (a tangens periódusa $\\pi$!)",
   "$3\\pi$"], True),
 ("Add meg az értékkészletet!",
  ["$y=\\sin x+2$", "$y=3\\cos x-1$"],
  ["$[1;3]$", "$[-4;2]$"], True),
 ("Merre és mennyivel tolódik el az alapgörbe?",
  ["$y=\\sin\\left(x+\\tfrac{\\pi}{2}\\right)$",
   "$y=\\cos\\left(x-\\tfrac{\\pi}{3}\\right)$"],
  ["$\\tfrac{\\pi}{2}$-vel <b>balra</b>", "$\\tfrac{\\pi}{3}$-mal <b>jobbra</b>"], True),
 ("Ábrázold egy perióduson! $y=2\\sin x$ és $y=\\sin 2x$ — mi a különbség?", None,
  "Az $y=2\\sin x$ kétszer olyan <b>magas</b> (amplitúdó $2$, periódus $2\\pi$); "
  "az $y=\\sin 2x$ kétszer olyan <b>sűrű</b> (amplitúdó $1$, periódus $\\pi$)."),
 ("Oldd meg!", ["$2\\sin x-1=0$", "$2\\cos x-1=0$"],
  ["$x=\\tfrac{\\pi}{6}+2k\\pi$ vagy $x=\\tfrac{5\\pi}{6}+2k\\pi$",
   "$x=\\pm\\tfrac{\\pi}{3}+2k\\pi$"], True),
 ("Oldd meg!", ["$2\\sin x+\\sqrt2=0$", "$2\\cos x+\\sqrt3=0$"],
  ["$x=\\tfrac{5\\pi}{4}+2k\\pi$ vagy $x=\\tfrac{7\\pi}{4}+2k\\pi$",
   "$x=\\tfrac{5\\pi}{6}+2k\\pi$ vagy $x=\\tfrac{7\\pi}{6}+2k\\pi$"], True),
 ("Oldd meg!", ["$\\operatorname{tg}x=\\sqrt3$", "$\\operatorname{tg}x=-1$"],
  ["$x=\\tfrac{\\pi}{3}+k\\pi$", "$x=\\tfrac{3\\pi}{4}+k\\pi$"], True),
 ("Oldd meg! (Speciális esetek.)",
  ["$\\sin x=1$", "$\\cos x=-1$", "$\\sin x=0$"],
  ["$x=\\tfrac{\\pi}{2}+2k\\pi$", "$x=\\pi+2k\\pi$", "$x=k\\pi$"], True),
 ("Van-e megoldása? Indokold!",
  ["$\\sin x=1{,}5$", "$\\cos x=-0{,}8$", "$\\operatorname{tg}x=100$"],
  ["<b>Nincs</b> — a szinusz értékkészlete $[-1;1]$.",
   "<b>Van</b> — a $-0{,}8$ beleesik az értékkészletbe.",
   "<b>Van</b> — a tangens értékkészlete a teljes $\\mathbb{R}$."], True),
 ("Oldd meg!", ["$2\\sin 2x-1=0$", "$2\\cos 3x-\\sqrt3=0$"],
  ["$2x=\\tfrac{\\pi}{6}+2k\\pi$ vagy $\\tfrac{5\\pi}{6}+2k\\pi$, tehát "
   "$x=\\tfrac{\\pi}{12}+k\\pi$ vagy $x=\\tfrac{5\\pi}{12}+k\\pi$",
   "$3x=\\pm\\tfrac{\\pi}{6}+2k\\pi$, tehát $x=\\pm\\tfrac{\\pi}{18}+\\tfrac{2k\\pi}{3}$"],
  False),
 ("Oldd meg! $\\operatorname{tg}2x=1$", None,
  "$2x=\\tfrac{\\pi}{4}+k\\pi$, tehát $x=\\tfrac{\\pi}{8}+\\tfrac{k\\pi}{2}$."),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Add meg az $y=3\\sin\\left(2x-\\tfrac{\\pi}{3}\\right)+1$ függvény amplitúdóját, "
  "periódusát, fáziseltolását és értékkészletét!", None,
  "$|A|=3$; $p=\\tfrac{2\\pi}{2}=\\pi$; a zárójelből kiemelve "
  "$2\\left(x-\\tfrac{\\pi}{6}\\right)$, tehát $\\tfrac{\\pi}{6}$-tal <b>jobbra</b>; "
  "ÉK: $[1-3;1+3]=[-2;4]$."),
 ("Add meg az $y=-2\\cos\\left(\\tfrac{x}{2}+\\tfrac{\\pi}{4}\\right)$ függvény "
  "amplitúdóját, periódusát és fáziseltolását!", None,
  "$|A|=2$ (és tükrözve); $p=\\tfrac{2\\pi}{1/2}=4\\pi$; kiemelve "
  "$\\tfrac12\\left(x+\\tfrac{\\pi}{2}\\right)$, tehát $\\tfrac{\\pi}{2}$-vel "
  "<b>balra</b>."),
 ("Egy szinuszos rezgés amplitúdója $4$, periódusa $\\pi$. Írd fel a "
  "hozzárendelési szabályt (fáziseltolás nélkül)!", None,
  "$p=\\tfrac{2\\pi}{b}=\\pi$, tehát $b=2$: a függvény $y=4\\sin 2x$."),
 ("Egy grafikonról leolvasható: a legnagyobb érték $5$, a legkisebb $-1$, a periódus "
  "$4\\pi$. Mennyi $A$, $b$ és $d$ az $y=A\\sin(bx)+d$ alakban?", None,
  "A középvonal $d=\\tfrac{5+(-1)}{2}=2$; az amplitúdó "
  "$A=\\tfrac{5-(-1)}{2}=3$; $b=\\tfrac{2\\pi}{4\\pi}=\\tfrac12$. "
  "Tehát $y=3\\sin\\tfrac{x}{2}+2$."),
 ("Hol metszi az $y$-tengelyt az $y=2\\sin\\left(x+\\tfrac{\\pi}{6}\\right)$ függvény?",
  None, "Az $x=0$ helyen: $y=2\\sin\\tfrac{\\pi}{6}=2\\cdot\\tfrac12=1$, "
        "tehát a $(0;1)$ pontban."),
 ("Oldd meg! $2\\sin 2x+\\sqrt2=0$", None,
  "$\\sin 2x=-\\tfrac{\\sqrt2}{2}$; $2x=\\tfrac{5\\pi}{4}+2k\\pi$ vagy "
  "$2x=\\tfrac{7\\pi}{4}+2k\\pi$, tehát $x=\\tfrac{5\\pi}{8}+k\\pi$ vagy "
  "$x=\\tfrac{7\\pi}{8}+k\\pi$."),
 ("Oldd meg! $\\sqrt2\\cos\\left(x-\\tfrac{\\pi}{4}\\right)=1$", None,
  "$\\cos\\left(x-\\tfrac{\\pi}{4}\\right)=\\tfrac{\\sqrt2}{2}$, tehát "
  "$x-\\tfrac{\\pi}{4}=\\pm\\tfrac{\\pi}{4}+2k\\pi$: "
  "$x=\\tfrac{\\pi}{2}+2k\\pi$ vagy $x=2k\\pi$."),
 ("Oldd meg! $\\sin\\left(x+\\tfrac{\\pi}{6}\\right)=1$", None,
  "$x+\\tfrac{\\pi}{6}=\\tfrac{\\pi}{2}+2k\\pi$, tehát "
  "$x=\\tfrac{\\pi}{3}+2k\\pi$."),
 ("Oldd meg a $[0;2\\pi)$ intervallumon! $2\\cos x+1=0$", None,
  "$\\cos x=-\\tfrac12$, az alapszög $\\tfrac{\\pi}{3}$, a koszinusz a II. és a III. "
  "negyedben negatív: $x=\\tfrac{2\\pi}{3}$ és $x=\\tfrac{4\\pi}{3}$."),
 ("Oldd meg a $[0;2\\pi)$ intervallumon! $\\operatorname{tg}x=\\tfrac{\\sqrt3}{3}$",
  None, "$x=\\tfrac{\\pi}{6}$ és $x=\\tfrac{7\\pi}{6}$ (a periódus $\\pi$, tehát "
        "$[0;2\\pi)$-ben két megoldás van)."),
 ("Oldd meg! $\\sin^{2}x=\\tfrac14$", None,
  "$\\sin x=\\pm\\tfrac12$, tehát négy megoldáscsalád; összevonva "
  "$x=\\pm\\tfrac{\\pi}{6}+k\\pi$."),
 ("Oldd meg! $\\sin x\\cos x=0$", None,
  "Szorzat akkor nulla, ha valamelyik tényezője az: $\\sin x=0$ → $x=k\\pi$, "
  "vagy $\\cos x=0$ → $x=\\tfrac{\\pi}{2}+k\\pi$. Összevonva: "
  "$x=\\tfrac{k\\pi}{2}$."),
 ("Oldd meg! $2\\sin x\\cos x=\\tfrac{\\sqrt3}{2}$", None,
  "A bal oldal $\\sin 2x$, tehát $\\sin 2x=\\tfrac{\\sqrt3}{2}$: "
  "$2x=\\tfrac{\\pi}{3}+2k\\pi$ vagy $2x=\\tfrac{2\\pi}{3}+2k\\pi$, ahonnan "
  "$x=\\tfrac{\\pi}{6}+k\\pi$ vagy $x=\\tfrac{\\pi}{3}+k\\pi$."),
 ("Egy hullám alakja $y=0{,}2\\sin(100\\pi t)$ (méterben, $t$ másodpercben). "
  "Mekkora az amplitúdója és a frekvenciája?", None,
  "Amplitúdó: $0{,}2$ m. A periódus $p=\\tfrac{2\\pi}{100\\pi}=0{,}02$ s, tehát a "
  "frekvencia $f=\\tfrac{1}{p}=50$ Hz."),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Oldd meg! $\\sin x=\\cos x$", None,
  "Osztva $\\cos x$-szel: $\\operatorname{tg}x=1$, tehát "
  "$x=\\tfrac{\\pi}{4}+k\\pi$. (A $\\cos x=0$ eset nem megoldás, mert ott "
  "$\\sin x=\\pm 1$.)"),
 ("Oldd meg! $\\cos 2x=\\tfrac12$", None,
  "$2x=\\pm\\tfrac{\\pi}{3}+2k\\pi$, tehát $x=\\pm\\tfrac{\\pi}{6}+k\\pi$."),
 ("Oldd meg! $2\\sin^{2}x-1=0$", None,
  "A bal oldal $-\\cos 2x$, tehát $\\cos 2x=0$: $2x=\\tfrac{\\pi}{2}+k\\pi$, "
  "ahonnan $x=\\tfrac{\\pi}{4}+\\tfrac{k\\pi}{2}$."),
 ("Oldd meg! $\\cos 2x+\\cos x=0$ a $[0;2\\pi)$ intervallumon.", None,
  "$\\cos 2x=2\\cos^{2}x-1$, tehát $2c^{2}+c-1=0$, ahol $c=\\cos x$. Innen "
  "$c=\\tfrac12$ vagy $c=-1$. Az elsőből $x=\\tfrac{\\pi}{3}$ és "
  "$x=\\tfrac{5\\pi}{3}$, a másodikból $x=\\pi$."),
 ("Add meg az $y=\\sin x+\\cos x$ függvény legnagyobb értékét! (Alakítsd át "
  "$A\\sin(x+c)$ alakra.)", None,
  "$\\sin x+\\cos x=\\sqrt2\\sin\\left(x+\\tfrac{\\pi}{4}\\right)$, tehát a "
  "legnagyobb érték $\\sqrt2\\approx 1{,}41421$ (és a legkisebb $-\\sqrt2$)."),
 ("Hány megoldása van a $\\sin x=\\tfrac13$ egyenletnek a $[0;4\\pi]$ "
  "intervallumon?", None,
  "Periódusonként <b>két</b> megoldás van, és a $[0;4\\pi]$ két teljes periódust "
  "fog át: <b>4 megoldás</b>."),
]

JOKER = ("Oldd meg! $\\sin x+\\sin 3x=0$",
         "Alakítsuk a bal oldalt szorzattá ($\\sin u+\\sin v$, félösszeg $2x$, "
         "félkülönbség $-x$):"
         "$$2\\sin 2x\\cos(-x)=2\\sin 2x\\cos x=0.$$"
         "A szorzat akkor nulla, ha valamelyik tényezője az. "
         "$\\sin 2x=0$ → $2x=k\\pi$, azaz $x=\\tfrac{k\\pi}{2}$; "
         "$\\cos x=0$ → $x=\\tfrac{\\pi}{2}+k\\pi$ — ez utóbbi benne van az elsőben. "
         "A megoldás tehát $\\boxed{x=\\dfrac{k\\pi}{2}},\\ k\\in\\mathbb{Z}$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
           fajl="feladatok-trig-fuggvenyek-egyenletek.html",
           cim="Függvények és egyenletek", temakor="Trigonometrikus függvények",
           alcim="Grafikonok, amplitúdó–periódus–fázis, valamint az egyszerű "
                 "trigonometrikus egyenletek minden alaptípusa. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-trigonometrikus-egyenletek.html",
           prevc="Egyszerű trigonometrikus egyenletek",
           nxt="tananyag-szinusz-es-koszinusztetel.html", nxtc="Szinusz- és koszinusztétel")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
