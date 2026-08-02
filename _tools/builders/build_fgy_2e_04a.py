# -*- coding: utf-8 -*-
"""2e/04 — A altema feladatgyujtemeny: a trigonometrikus kor."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, pi, sqrt, sin, cos, tan, cot, rad, deg, nsimplify, simplify, N
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        ok = abs(float(g) - w) < tol
    elif isinstance(w, (list, tuple)):
        ok = list(g) == list(w)
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
def negy(A): return [simplify(f(rad(A))) for f in (sin, cos, tan, cot)]
for a, w in [(30, R(1, 6)), (60, R(1, 3)), (90, R(1, 2)), (180, 1), (120, R(2, 3)),
             (210, R(7, 6)), (225, R(5, 4)), (330, R(11, 6)), (15, R(1, 12)),
             (75, R(5, 12)), (105, R(7, 12)), (195, R(13, 12))]:
    chk(f"r{a}", nsimplify(rad(a))/pi, w)
for f, w in [(R(1, 6), 30), (R(1, 3), 60), (R(3, 4), 135), (R(5, 3), 300), (R(7, 6), 210),
             (R(5, 4), 225), (R(11, 6), 330), (2, 360), (R(5, 18), 50), (R(7, 9), 140),
             (R(13, 12), 195)]:
    chk(f"d{f}", deg(f*pi), w)
chk("t390", 390 - 360, 30); chk("t750", 750 - 720, 30)
chk("t-30", -30 + 360, 330); chk("t-200", -200 + 360, 160)
chk("n30", negy(30), [R(1, 2), sqrt(3)/2, sqrt(3)/3, sqrt(3)])
chk("n45", negy(45), [sqrt(2)/2, sqrt(2)/2, 1, 1])
chk("n60", negy(60), [sqrt(3)/2, R(1, 2), sqrt(3), sqrt(3)/3])
chk("n120", negy(120), [sqrt(3)/2, R(-1, 2), -sqrt(3), -sqrt(3)/3])
chk("n135", negy(135), [sqrt(2)/2, -sqrt(2)/2, -1, -1])
chk("n150", negy(150), [R(1, 2), -sqrt(3)/2, -sqrt(3)/3, -sqrt(3)])
chk("n210", negy(210), [R(-1, 2), -sqrt(3)/2, sqrt(3)/3, sqrt(3)])
chk("n225", negy(225), [-sqrt(2)/2, -sqrt(2)/2, 1, 1])
chk("n240", negy(240), [-sqrt(3)/2, R(-1, 2), sqrt(3), sqrt(3)/3])
chk("n300", negy(300), [-sqrt(3)/2, R(1, 2), -sqrt(3), -sqrt(3)/3])
chk("n315", negy(315), [-sqrt(2)/2, sqrt(2)/2, -1, -1])
chk("n330", negy(330), [R(-1, 2), sqrt(3)/2, -sqrt(3)/3, -sqrt(3)])
chk("neg-30", sin(rad(-30)), R(-1, 2)); chk("neg-60", cos(rad(-60)), R(1, 2))
chk("neg-45", tan(rad(-45)), -1)
chk("K3a", nsimplify(9*pi/4 - 2*pi)/pi, R(1, 4))
chk("K3b", nsimplify(17*pi/6 - 2*pi)/pi, R(5, 6))
chk("K3c", nsimplify(-5*pi/3 + 2*pi)/pi, R(1, 3))
chk("K4a", sin(rad(1000)) + sin(rad(80)), 0)
chk("K4b", cos(rad(1110)), sqrt(3)/2)
chk("K5", sin(rad(420))*cos(rad(330)), R(3, 4))
chk("K6", sin(rad(150)) + cos(rad(240)) + tan(rad(315)), -1)
chk("K7", 2*sin(rad(120)) - 3*cos(rad(150)) + tan(rad(240)), 7*sqrt(3)/2)
chk("K11", [N(sin(rad(200)), 5) < N(sin(rad(30)), 5),
            N(sin(rad(30)), 5) < N(sin(rad(100)), 5)], [True, True])
chk("K12", 6*rad(60), 2*pi)
chk("K13", R(1, 2)*16*(pi/6), 4*pi/3)
chk("N1", sin(rad(120))**2 + cos(rad(120))**2, 1)
chk("N3a", sin(pi/4) - cos(pi/4), 0); chk("N3b", sin(5*pi/4) - cos(5*pi/4), 0)
chk("N4", 2*pi*R(3, 20), 3*pi/10)
chk("N5", cos(0) + cos(rad(60)) + cos(rad(120)) + cos(rad(180)), 0)
chk("J", sum(sin(rad(k))**2 for k in range(10, 81, 10)), 4)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Váltsd át radiánba!", ["$30^\\circ$", "$60^\\circ$", "$90^\\circ$", "$180^\\circ$"],
  ["$\\dfrac{\\pi}{6}$", "$\\dfrac{\\pi}{3}$", "$\\dfrac{\\pi}{2}$", "$\\pi$"], True),
 ("Váltsd át radiánba!", ["$120^\\circ$", "$210^\\circ$", "$225^\\circ$", "$330^\\circ$"],
  ["$\\dfrac{2\\pi}{3}$", "$\\dfrac{7\\pi}{6}$", "$\\dfrac{5\\pi}{4}$",
   "$\\dfrac{11\\pi}{6}$"], True),
 ("Váltsd át fokba!",
  ["$\\dfrac{\\pi}{6}$", "$\\dfrac{\\pi}{3}$", "$\\dfrac{3\\pi}{4}$", "$\\dfrac{5\\pi}{3}$"],
  ["$30^\\circ$", "$60^\\circ$", "$135^\\circ$", "$300^\\circ$"], True),
 ("Váltsd át fokba!",
  ["$\\dfrac{7\\pi}{6}$", "$\\dfrac{5\\pi}{4}$", "$\\dfrac{11\\pi}{6}$", "$2\\pi$"],
  ["$210^\\circ$", "$225^\\circ$", "$330^\\circ$", "$360^\\circ$"], True),
 ("Melyik $[0^\\circ;360^\\circ)$ közötti szöggel egyezik meg?",
  ["$390^\\circ$", "$750^\\circ$", "$-30^\\circ$", "$-200^\\circ$"],
  ["$30^\\circ$", "$30^\\circ$", "$330^\\circ$", "$160^\\circ$"], True),
 ("Melyik negyedben van a szög?",
  ["$100^\\circ$", "$200^\\circ$", "$300^\\circ$", "$400^\\circ$"],
  ["II.", "III.", "IV.", "I. (mert $400^\\circ-360^\\circ=40^\\circ$)"], True),
 ("Add meg mind a négy szögfüggvény pontos értékét!",
  ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$"],
  ["$\\tfrac12$, $\\tfrac{\\sqrt3}{2}$, $\\tfrac{\\sqrt3}{3}$, $\\sqrt3$",
   "$\\tfrac{\\sqrt2}{2}$, $\\tfrac{\\sqrt2}{2}$, $1$, $1$",
   "$\\tfrac{\\sqrt3}{2}$, $\\tfrac12$, $\\sqrt3$, $\\tfrac{\\sqrt3}{3}$"], False),
 ("Add meg mind a négy szögfüggvény pontos értékét!",
  ["$120^\\circ$", "$135^\\circ$", "$150^\\circ$"],
  ["$\\tfrac{\\sqrt3}{2}$, $-\\tfrac12$, $-\\sqrt3$, $-\\tfrac{\\sqrt3}{3}$",
   "$\\tfrac{\\sqrt2}{2}$, $-\\tfrac{\\sqrt2}{2}$, $-1$, $-1$",
   "$\\tfrac12$, $-\\tfrac{\\sqrt3}{2}$, $-\\tfrac{\\sqrt3}{3}$, $-\\sqrt3$"], False),
 ("Add meg mind a négy szögfüggvény pontos értékét!",
  ["$210^\\circ$", "$225^\\circ$", "$240^\\circ$"],
  ["$-\\tfrac12$, $-\\tfrac{\\sqrt3}{2}$, $\\tfrac{\\sqrt3}{3}$, $\\sqrt3$",
   "$-\\tfrac{\\sqrt2}{2}$, $-\\tfrac{\\sqrt2}{2}$, $1$, $1$",
   "$-\\tfrac{\\sqrt3}{2}$, $-\\tfrac12$, $\\sqrt3$, $\\tfrac{\\sqrt3}{3}$"], False),
 ("Add meg mind a négy szögfüggvény pontos értékét!",
  ["$300^\\circ$", "$315^\\circ$", "$330^\\circ$"],
  ["$-\\tfrac{\\sqrt3}{2}$, $\\tfrac12$, $-\\sqrt3$, $-\\tfrac{\\sqrt3}{3}$",
   "$-\\tfrac{\\sqrt2}{2}$, $\\tfrac{\\sqrt2}{2}$, $-1$, $-1$",
   "$-\\tfrac12$, $\\tfrac{\\sqrt3}{2}$, $-\\tfrac{\\sqrt3}{3}$, $-\\sqrt3$"], False),
 ("Add meg a szögfüggvények értékét (ahol létezik)!",
  ["$0$", "$\\dfrac{\\pi}{2}$", "$\\pi$"],
  ["$\\sin=0$, $\\cos=1$, $\\operatorname{tg}=0$, $\\operatorname{ctg}$ nem létezik",
   "$\\sin=1$, $\\cos=0$, $\\operatorname{tg}$ nem létezik, $\\operatorname{ctg}=0$",
   "$\\sin=0$, $\\cos=-1$, $\\operatorname{tg}=0$, $\\operatorname{ctg}$ nem létezik"], False),
 ("Milyen előjelű? (Csak az előjelet add meg!)",
  ["$\\sin 100^\\circ$", "$\\cos 200^\\circ$", "$\\operatorname{tg}300^\\circ$",
   "$\\operatorname{ctg}160^\\circ$"],
  ["$+$ (II. negyed)", "$-$ (III. negyed)", "$-$ (IV. negyed)", "$-$ (II. negyed)"], True),
 ("Vezesd vissza az első negyedre! (Csak az alakot írd fel, ne számold ki.)",
  ["$\\sin 160^\\circ$", "$\\cos 190^\\circ$", "$\\operatorname{tg}320^\\circ$"],
  ["$\\sin 20^\\circ$", "$-\\cos 10^\\circ$", "$-\\operatorname{tg}40^\\circ$"], True),
 ("Számold ki pontosan!",
  ["$\\sin 150^\\circ$", "$\\cos 240^\\circ$", "$\\operatorname{tg}225^\\circ$"],
  ["$\\dfrac12$", "$-\\dfrac12$", "$1$"], True),
 ("Számold ki pontosan!",
  ["$\\cos 300^\\circ$", "$\\sin 315^\\circ$", "$\\operatorname{ctg}210^\\circ$"],
  ["$\\dfrac12$", "$-\\dfrac{\\sqrt2}{2}$", "$\\sqrt3$"], True),
 ("Számold ki pontosan! (Használd a szimmetriát.)",
  ["$\\sin(-30^\\circ)$", "$\\cos(-60^\\circ)$", "$\\operatorname{tg}(-45^\\circ)$"],
  ["$-\\dfrac12$", "$\\dfrac12$", "$-1$"], True),
 ("Add meg az $\\alpha$ szöget, ha $0^\\circ\\le\\alpha&lt;360^\\circ$, "
  "$\\sin\\alpha=\\tfrac12$ és $\\cos\\alpha&lt;0$!", None,
  "A szinusz pozitív, a koszinusz negatív → II. negyed, alapszög $30^\\circ$: "
  "$\\alpha=150^\\circ$."),
 ("Add meg az $\\alpha$ szöget, ha $0^\\circ\\le\\alpha&lt;360^\\circ$, "
  "$\\cos\\alpha=\\tfrac{\\sqrt2}{2}$ és $\\sin\\alpha&lt;0$!", None,
  "A koszinusz pozitív, a szinusz negatív → IV. negyed, alapszög $45^\\circ$: "
  "$\\alpha=315^\\circ$."),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Váltsd át radiánba!", ["$15^\\circ$", "$75^\\circ$", "$105^\\circ$", "$195^\\circ$"],
  ["$\\dfrac{\\pi}{12}$", "$\\dfrac{5\\pi}{12}$", "$\\dfrac{7\\pi}{12}$",
   "$\\dfrac{13\\pi}{12}$"], True),
 ("Váltsd át fokba!",
  ["$\\dfrac{5\\pi}{18}$", "$\\dfrac{7\\pi}{9}$", "$\\dfrac{13\\pi}{12}$"],
  ["$50^\\circ$", "$140^\\circ$", "$195^\\circ$"], True),
 ("Melyik $[0;2\\pi)$ közötti szöggel egyezik meg?",
  ["$\\dfrac{9\\pi}{4}$", "$\\dfrac{17\\pi}{6}$", "$-\\dfrac{5\\pi}{3}$"],
  ["$\\dfrac{\\pi}{4}$", "$\\dfrac{5\\pi}{6}$", "$\\dfrac{\\pi}{3}$"], True),
 ("Számold ki! (A nem pontos értéket öt tizedesre kerekítsd.)",
  ["$\\sin 1000^\\circ$", "$\\cos 1110^\\circ$"],
  ["$1000-2\\cdot 360=280$; a IV. negyedben a szinusz negatív: "
   "$-\\sin 80^\\circ\\approx -0{,}98481$",
   "$1110-3\\cdot 360=30$, tehát $\\cos 30^\\circ=\\dfrac{\\sqrt3}{2}$"], False),
 ("Számold ki pontosan! $\\sin 420^\\circ\\cdot\\cos 330^\\circ$", None,
  "$\\sin 420^\\circ=\\sin 60^\\circ=\\tfrac{\\sqrt3}{2}$ és "
  "$\\cos 330^\\circ=\\tfrac{\\sqrt3}{2}$, a szorzat $\\dfrac34$."),
 ("Számold ki pontosan! $\\sin 150^\\circ+\\cos 240^\\circ+\\operatorname{tg}315^\\circ$",
  None, "$\\tfrac12+\\left(-\\tfrac12\\right)+(-1)=-1$"),
 ("Számold ki pontosan! "
  "$2\\sin 120^\\circ-3\\cos 150^\\circ+\\operatorname{tg}240^\\circ$", None,
  "$2\\cdot\\tfrac{\\sqrt3}{2}-3\\cdot\\left(-\\tfrac{\\sqrt3}{2}\\right)+\\sqrt3="
  "\\sqrt3+\\tfrac{3\\sqrt3}{2}+\\sqrt3=\\dfrac{7\\sqrt3}{2}$"),
 ("Add meg az $\\alpha$ szöget, ha $0\\le\\alpha&lt;2\\pi$, "
  "$\\operatorname{tg}\\alpha=-1$ és $\\sin\\alpha&gt;0$!", None,
  "A tangens negatív, a szinusz pozitív → II. negyed, alapszög $\\tfrac{\\pi}{4}$: "
  "$\\alpha=\\dfrac{3\\pi}{4}$."),
 ("Add meg az $\\alpha$ szöget, ha $0\\le\\alpha&lt;2\\pi$, "
  "$\\operatorname{ctg}\\alpha=\\sqrt3$ és $\\cos\\alpha&lt;0$!", None,
  "A kotangens pozitív → I. vagy III. negyed; a koszinusz negatív → III. negyed. "
  "Az alapszög $\\tfrac{\\pi}{6}$, tehát $\\alpha=\\dfrac{7\\pi}{6}$."),
 ("Igaz-e, hogy $\\sin 100^\\circ&gt;\\sin 80^\\circ$? Indokold!", None,
  "<b>Nem</b> — a két érték <b>egyenlő</b>, mert $100^\\circ$ a II. negyedben van, "
  "alapszöge $80^\\circ$, és ott a szinusz pozitív: $\\sin 100^\\circ=\\sin 80^\\circ$."),
 ("Rendezd nagyság szerint növekvően! $\\sin 30^\\circ$, $\\sin 100^\\circ$, "
  "$\\sin 200^\\circ$", None,
  "$\\sin 200^\\circ\\approx -0{,}34202&lt;\\sin 30^\\circ=0{,}5&lt;"
  "\\sin 100^\\circ\\approx 0{,}98481$"),
 ("Mekkora a $6$ egység sugarú kör $60^\\circ$-os középponti szögéhez tartozó "
  "ívhossza? (Az ívhossz $\\ell=r\\cdot\\alpha$, ahol $\\alpha$ <b>radiánban</b> van.)",
  None, "$\\alpha=\\tfrac{\\pi}{3}$, tehát $\\ell=6\\cdot\\tfrac{\\pi}{3}=2\\pi\\approx 6{,}28$."),
 ("Mekkora annak a körcikknek a területe, amelynek sugara $4$, középponti szöge "
  "$\\tfrac{\\pi}{6}$? ($T=\\tfrac{r^{2}\\alpha}{2}$)", None,
  "$T=\\dfrac{16\\cdot\\tfrac{\\pi}{6}}{2}=\\dfrac{4\\pi}{3}\\approx 4{,}19$"),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Számold ki pontosan! $\\sin^{2}120^\\circ+\\cos^{2}120^\\circ$", None,
  "Az alapazonosság szerint <b>minden</b> szögre $1$ — nem kell behelyettesíteni. "
  "(Ellenőrzésül: $\\tfrac34+\\tfrac14=1$.)"),
 ("Egyszerűsítsd! $\\sin(180^\\circ-\\alpha)+\\cos(180^\\circ+\\alpha)+"
  "\\operatorname{tg}(360^\\circ-\\alpha)$", None,
  "$\\sin\\alpha+(-\\cos\\alpha)+(-\\operatorname{tg}\\alpha)="
  "\\sin\\alpha-\\cos\\alpha-\\operatorname{tg}\\alpha$"),
 ("Mely $\\alpha\\in[0;2\\pi)$ szögekre teljesül, hogy $\\sin\\alpha=\\cos\\alpha$?",
  None, "Osztva $\\cos\\alpha$-val: $\\operatorname{tg}\\alpha=1$, tehát "
        "$\\alpha=\\dfrac{\\pi}{4}$ vagy $\\alpha=\\dfrac{5\\pi}{4}$. "
        "(A $\\cos\\alpha=0$ eset nem ad megoldást, mert ott a szinusz $\\pm 1$.)"),
 ("Egy kerék $20$ másodperc alatt fordul körbe egyszer. Mekkora szöget fordul "
  "$3$ másodperc alatt? (Radiánban add meg.)", None,
  "A teljes fordulat $2\\pi$, tehát $\\dfrac{3}{20}\\cdot 2\\pi=\\dfrac{3\\pi}{10}"
  "\\approx 0{,}94$ radián (azaz $54^\\circ$)."),
 ("Számold ki pontosan! $\\cos 0^\\circ+\\cos 60^\\circ+\\cos 120^\\circ+\\cos 180^\\circ$",
  None, "$1+\\tfrac12+\\left(-\\tfrac12\\right)+(-1)=0$ — a tagok páronként kiejtik "
        "egymást, mert $\\cos(180^\\circ-\\varphi)=-\\cos\\varphi$."),
 ("Mely szögekre nem értelmezett a $\\operatorname{tg}$, és melyekre a "
  "$\\operatorname{ctg}$? Indokold a definícióval!", None,
  "$\\operatorname{tg}\\alpha=\\tfrac{\\sin\\alpha}{\\cos\\alpha}$, tehát ott nincs "
  "értelmezve, ahol $\\cos\\alpha=0$: $\\alpha=\\tfrac{\\pi}{2}+k\\pi$. "
  "$\\operatorname{ctg}\\alpha=\\tfrac{\\cos\\alpha}{\\sin\\alpha}$ ott nincs, ahol "
  "$\\sin\\alpha=0$: $\\alpha=k\\pi$."),
]

JOKER = ("Számold ki! $\\sin^{2}10^\\circ+\\sin^{2}20^\\circ+\\sin^{2}30^\\circ+\\ldots"
         "+\\sin^{2}80^\\circ$",
         "Nyolc tag van. Párosítsuk a végekről: mivel $\\sin 80^\\circ=\\cos 10^\\circ$, "
         "$\\sin 70^\\circ=\\cos 20^\\circ$ és így tovább,"
         "$$\\sin^{2}10^\\circ+\\sin^{2}80^\\circ=\\sin^{2}10^\\circ+\\cos^{2}10^\\circ=1.$$"
         "Ugyanígy a $20^\\circ$–$70^\\circ$, a $30^\\circ$–$60^\\circ$ és a "
         "$40^\\circ$–$50^\\circ$ pár is $1$-et ad. Négy pár, tehát az összeg "
         "$\\boxed{4}$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
           fajl="feladatok-trigonometrikus-kor.html", cim="A trigonometrikus kör",
           temakor="Trigonometrikus függvények",
           alcim="Szögátváltás, forgásszögek, a négy függvény pontos értékei, előjelek "
                 "negyedenként és visszavezetés az első negyedre. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-visszavezetes.html", prevc="Visszavezetés az első negyedre",
           nxt="tananyag-alapazonossagok.html", nxtc="Alapazonosságok")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
