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
  'ÉT: $x\\ne\\tfrac{\\pi}{2}+k\\pi$, $k\\in\\mathbb{Z}$; ÉK: $\\mathbb{R}$; periódus: $\\pi$.'),
 ("Melyik páros és melyik páratlan függvény?",
  ["$\\sin x$", "$\\cos x$", "$\\operatorname{tg}x$"],
  ['páratlan',
   'páros',
   'páratlan (ahol értelmezett)'], True),
 ("Hol van maximuma és hol minimuma az $y=\\sin x$ függvénynek?", None,
  'Maximum $1$: $x=\\tfrac{\\pi}{2}+2k\\pi$; minimum $-1$: $x=\\tfrac{3\\pi}{2}+2k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Add meg az amplitúdót és az értékkészletet!",
  ["$y=3\\sin x$", "$y=-2\\cos x$", "$y=\\tfrac12\\sin x$"],
  ['Amplitúdó $3$; ÉK: $[-3;3]$',
   'Amplitúdó $2$; ÉK: $[-2;2]$',
   'Amplitúdó $\\tfrac12$; ÉK: $[-\\tfrac12;\\tfrac12]$'], True),
 ("Add meg a periódust!",
  ["$y=\\sin 2x$", "$y=\\cos 3x$", "$y=\\sin\\tfrac{x}{2}$"],
  ["$\\pi$", "$\\dfrac{2\\pi}{3}$", "$4\\pi$"], True),
 ("Add meg a periódust!",
  ["$y=\\cos 4x$", "$y=\\operatorname{tg}2x$", "$y=\\sin\\tfrac{2x}{3}$"],
  ['$\\dfrac{\\pi}{2}$',
   '$\\dfrac{\\pi}{2}$',
   '$3\\pi$'], True),
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
  ['$x=\\tfrac{\\pi}{6}+2k\\pi$ vagy $x=\\tfrac{5\\pi}{6}+2k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=\\pm\\tfrac{\\pi}{3}+2k\\pi$, $k\\in\\mathbb{Z}$'], True),
 ("Oldd meg!", ["$2\\sin x+\\sqrt2=0$", "$2\\cos x+\\sqrt3=0$"],
  ['$x=\\tfrac{5\\pi}{4}+2k\\pi$ vagy $x=\\tfrac{7\\pi}{4}+2k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=\\tfrac{5\\pi}{6}+2k\\pi$ vagy $x=\\tfrac{7\\pi}{6}+2k\\pi$, $k\\in\\mathbb{Z}$'], True),
 ("Oldd meg!", ["$\\operatorname{tg}x=\\sqrt3$", "$\\operatorname{tg}x=-1$"],
  ['$x=\\tfrac{\\pi}{3}+k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=\\tfrac{3\\pi}{4}+k\\pi$, $k\\in\\mathbb{Z}$'], True),
 ("Oldd meg! (Speciális esetek.)",
  ["$\\sin x=1$", "$\\cos x=-1$", "$\\sin x=0$"],
  ['$x=\\tfrac{\\pi}{2}+2k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=\\pi+2k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=k\\pi$, $k\\in\\mathbb{Z}$'], True),
 ("Van-e megoldása? Indokold!",
  ["$\\sin x=1{,}5$", "$\\cos x=-0{,}8$", "$\\operatorname{tg}x=100$"],
  ["<b>Nincs</b> — a szinusz értékkészlete $[-1;1]$.",
   "<b>Van</b> — a $-0{,}8$ beleesik az értékkészletbe.",
   "<b>Van</b> — a tangens értékkészlete a teljes $\\mathbb{R}$."], True),
 ("Oldd meg!", ["$2\\sin 2x-1=0$", "$2\\cos 3x-\\sqrt3=0$"],
  ['$x=\\tfrac{\\pi}{12}+k\\pi$ vagy $x=\\tfrac{5\\pi}{12}+k\\pi$, $k\\in\\mathbb{Z}$',
   '$x=\\pm\\tfrac{\\pi}{18}+\\tfrac{2k\\pi}{3}$, $k\\in\\mathbb{Z}$'],
  False),
 ("Oldd meg! $\\operatorname{tg}2x=1$", None,
  '$x=\\tfrac{\\pi}{8}+\\tfrac{k\\pi}{2}$, $k\\in\\mathbb{Z}$.'),
 ('Oldd meg a $[0^\\circ;360^\\circ)$ körön! Add meg a megoldáshalmazt!',
  ['$\\sin x&gt;\\tfrac{\\sqrt2}{2}$', '$\\cos x&lt;\\tfrac12$',
   '$\\sin x\\le 0$'],
  ['$(45^\\circ;135^\\circ)$', '$(60^\\circ;300^\\circ)$',
   '$\\{0^\\circ\\}\\cup[180^\\circ;360^\\circ)$']),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Add meg az $y=3\\sin\\left(2x-\\tfrac{\\pi}{3}\\right)+1$ függvény amplitúdóját, "
  "periódusát, fáziseltolását és értékkészletét!", None,
  'Amplitúdó $3$; periódus $\\pi$; fáziseltolás $\\tfrac{\\pi}{6}$-tal jobbra; ÉK: $[-2;4]$.'),
 ("Add meg az $y=-2\\cos\\left(\\tfrac{x}{2}+\\tfrac{\\pi}{4}\\right)$ függvény "
  "amplitúdóját, periódusát és fáziseltolását!", None,
  'Amplitúdó $2$; periódus $4\\pi$; fáziseltolás $\\tfrac{\\pi}{2}$-vel balra.'),
 ('Egy szinuszos rezgés amplitúdója $4$, periódusa $\\pi$. Adj meg egy lehetséges hozzárendelési szabályt fáziseltolás nélkül!', None,
  '$y=4\\sin 2x$.'),
 ('Egy grafikonról leolvasható: a legnagyobb érték $5$, a legkisebb $-1$, a periódus $4\\pi$. Tegyük fel, hogy $A>0$ és $b>0$. Mennyi $A$, $b$ és $d$ az $y=A\\sin(bx)+d$ alakban?', None,
  '$A=3$, $b=\\tfrac12$, $d=2$.'),
 ("Hol metszi az $y$-tengelyt az $y=2\\sin\\left(x+\\tfrac{\\pi}{6}\\right)$ függvény?",
  None, 'A $(0;1)$ pontban.'),
 ("Oldd meg! $2\\sin 2x+\\sqrt2=0$", None,
  '$x=\\tfrac{5\\pi}{8}+k\\pi$ vagy $x=\\tfrac{7\\pi}{8}+k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $\\sqrt2\\cos\\left(x-\\tfrac{\\pi}{4}\\right)=1$", None,
  '$x=2k\\pi$ vagy $x=\\tfrac{\\pi}{2}+2k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $\\sin\\left(x+\\tfrac{\\pi}{6}\\right)=1$", None,
  '$x=\\tfrac{\\pi}{3}+2k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg a $[0;2\\pi)$ intervallumon! $2\\cos x+1=0$", None,
  '$x=\\tfrac{2\\pi}{3}$ vagy $x=\\tfrac{4\\pi}{3}$.'),
 ("Oldd meg a $[0;2\\pi)$ intervallumon! $\\operatorname{tg}x=\\tfrac{\\sqrt3}{3}$",
  None, '$x=\\tfrac{\\pi}{6}$ vagy $x=\\tfrac{7\\pi}{6}$.'),
 ("Oldd meg! $\\sin^{2}x=\\tfrac14$", None,
  '$x=\\pm\\tfrac{\\pi}{6}+k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $\\sin x\\cos x=0$", None,
  '$x=\\tfrac{k\\pi}{2}$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $2\\sin x\\cos x=\\tfrac{\\sqrt3}{2}$", None,
  '$x=\\tfrac{\\pi}{6}+k\\pi$ vagy $x=\\tfrac{\\pi}{3}+k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Egy hullám alakja $y=0{,}2\\sin(100\\pi t)$ (méterben, $t$ másodpercben). "
  "Mekkora az amplitúdója és a frekvenciája?", None,
  'Amplitúdó $0{,}2$ m; frekvencia $50$ Hz.'),
 ('Oldd meg az egyenlőtlenséget a valós számok halmazán — a periódust is írd ki!',
  ['$\\cos x\\ge\\tfrac12$', '$\\sin x&lt;-\\tfrac{\\sqrt3}{2}$'],
  ['$x\\in[-60^\\circ+k\\cdot360^\\circ;\\ 60^\\circ+k\\cdot360^\\circ]$, ahol $k\\in\\mathbb{Z}$',
   '$x\\in(240^\\circ+k\\cdot360^\\circ;\\ 300^\\circ+k\\cdot360^\\circ)$, ahol $k\\in\\mathbb{Z}$']),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Oldd meg! $\\sin x=\\cos x$", None,
  '$x=\\tfrac{\\pi}{4}+k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $\\cos 2x=\\tfrac12$", None,
  '$x=\\pm\\tfrac{\\pi}{6}+k\\pi$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $2\\sin^{2}x-1=0$", None,
  '$x=\\tfrac{\\pi}{4}+\\tfrac{k\\pi}{2}$, $k\\in\\mathbb{Z}$.'),
 ("Oldd meg! $\\cos 2x+\\cos x=0$ a $[0;2\\pi)$ intervallumon.", None,
  '$x\\in\\{\\tfrac{\\pi}{3},\\pi,\\tfrac{5\\pi}{3}\\}$.'),
 ("Add meg az $y=\\sin x+\\cos x$ függvény legnagyobb értékét! (Alakítsd át "
  "$A\\sin(x+c)$ alakra.)", None,
  '$\\sin x+\\cos x=\\sqrt2\\sin(x+\\tfrac{\\pi}{4})$; maximuma $\\sqrt2$.'),
 ("Hány megoldása van a $\\sin x=\\tfrac13$ egyenletnek a $[0;4\\pi]$ "
  "intervallumon?", None,
  '<b>4 megoldása</b>.'),
 ('Egy kadét így oldotta meg a $\\sin x&gt;\\tfrac12$ egyenlőtlenséget: <i>„A határszögek $30^\\circ$ és $150^\\circ$, tehát a megoldás $x=30^\\circ$ és $x=150^\\circ$.”</i>',
  ['Hol a hiba a gondolatmenetében?',
   'Add meg a helyes megoldást a $[0^\\circ;360^\\circ)$ körön!',
   'Mit kell még hozzátenni, ha a teljes valós számhalmazon keresünk megoldást?'],
  ['A határszögek az egyenlőség megoldásai; az egyenlőtlenség megoldása intervallum.',
   '$x\\in(30^\\circ;150^\\circ)$.',
   '$x\\in(30^\\circ+360^\\circ k;150^\\circ+360^\\circ k)$, $k\\in\\mathbb{Z}$.']),
]

JOKER = ("Oldd meg! $\\sin x+\\sin 3x=0$",
         '$x=\\dfrac{k\\pi}{2}$, $k\\in\\mathbb{Z}$.')

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
