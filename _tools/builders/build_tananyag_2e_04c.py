# -*- coding: utf-8 -*-
"""2e/04 — C altema: a trigonometrikus fuggvenyek grafikonja (C1), az A·sin(bx+c) alak (C2),
egyszeru trigonometrikus egyenletek (C3). Mentor: Szürke Janka."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra

T = dict(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
         temakor="Trigonometrikus függvények")
FGY = "feladatok-trig-fuggvenyek-egyenletek.html"

# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, pi, sqrt, sin, cos, tan, rad, simplify, solve, Symbol
E = []
def chk(n, g, w, tol=None):
    ok = abs(float(g) - w) < tol if tol is not None else simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
chk("C1-per", sin(0) - sin(2*pi), 0)
chk("C1-paratlan", sin(-pi/6) + sin(pi/6), 0)
chk("C1-paros", cos(-pi/3) - cos(pi/3), 0)
chk("C1-tgper", tan(rad(30)) - tan(rad(210)), 0)
chk("C2-per2", 2*pi/2, pi)
chk("C2-per3", 2*pi/3, 2*pi/3)
chk("C2-perhalf", 2*pi/R(1, 2), 4*pi)
chk("C3-1", sin(pi/6), R(1, 2))
chk("C3-1b", sin(5*pi/6), R(1, 2))
chk("C3-2", cos(5*pi/6), -sqrt(3)/2)
chk("C3-2b", cos(7*pi/6), -sqrt(3)/2)
chk("C3-3", tan(pi/4), 1)
chk("C3-4", sin(5*pi/4), -sqrt(2)/2)
chk("C3-4b", sin(7*pi/4), -sqrt(2)/2)
chk("C3-5", cos(pi/6), sqrt(3)/2)
chk("C3-bx", sin(2*(5*pi/8)), -sqrt(2)/2)
chk("C3-bx2", sin(2*(7*pi/8)), -sqrt(2)/2)
chk("C3-cx", cos(3*(pi/18)), sqrt(3)/2)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák (π-osztású)
PIC = [(-2*math.pi, "−2π"), (-1.5*math.pi, ""), (-math.pi, "−π"), (-0.5*math.pi, ""),
       (0.5*math.pi, "π/2"), (math.pi, "π"), (1.5*math.pi, ""), (2*math.pi, "2π")]


def svg_hullam(gorbek, xr, yr, w=560, h=230, leiras="Trigonometrikus függvény grafikonja",
               xticks=PIC, aszimptotak=(), jelmagyarazat=True):
    x0, x1 = xr
    y0, y1 = yr
    bal, jobb, fent, lent = 30, 14, 16, 26
    px, py = w - bal - jobb, h - fent - lent

    def X(x):
        return bal + (x - x0)/(x1 - x0)*px

    def Y(y):
        return fent + (y1 - y)/(y1 - y0)*py

    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}">',
          '  <defs><marker id="nyilh" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" '
          'markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker></defs>']
    for v, cimke in xticks:
        if x0 < v < x1:
            ki.append(f'  <line x1="{X(v):.1f}" y1="{Y(y0):.1f}" x2="{X(v):.1f}" '
                      f'y2="{Y(y1):.1f}" stroke="#e2e8f0" stroke-width=".8"/>')
            if cimke:
                ki.append(f'  <text x="{X(v):.1f}" y="{Y(0) + 15:.1f}" font-size="10" '
                          f'fill="#475569" text-anchor="middle">{cimke}</text>')
    t = math.ceil(y0)
    while t <= y1:
        if t != 0:
            ki.append(f'  <line x1="{X(x0):.1f}" y1="{Y(t):.1f}" x2="{X(x1):.1f}" '
                      f'y2="{Y(t):.1f}" stroke="#e2e8f0" stroke-width=".8"/>')
            ki.append(f'  <text x="{X(0) - 6:.1f}" y="{Y(t) + 4:.1f}" font-size="10" '
                      f'fill="#475569" text-anchor="end">{t}</text>')
        t += 1
    for v in aszimptotak:
        if x0 < v < x1:
            ki.append(f'  <line x1="{X(v):.1f}" y1="{Y(y0):.1f}" x2="{X(v):.1f}" '
                      f'y2="{Y(y1):.1f}" stroke="#ef4444" stroke-width="1" '
                      'stroke-dasharray="4 3"/>')
    ki.append(f'  <line x1="{X(x0):.1f}" y1="{Y(0):.1f}" x2="{X(x1):.1f}" y2="{Y(0):.1f}" '
              'stroke="#0f172a" stroke-width="1.3" marker-end="url(#nyilh)"/>')
    ki.append(f'  <line x1="{X(0):.1f}" y1="{Y(y0):.1f}" x2="{X(0):.1f}" y2="{Y(y1):.1f}" '
              'stroke="#0f172a" stroke-width="1.3" marker-end="url(#nyilh)"/>')
    for f, szin, cimke in gorbek:
        darab, pts = [], []
        n = 600
        for i in range(n + 1):
            x = x0 + (x1 - x0)*i/n
            try:
                y = f(x)
            except (ZeroDivisionError, ValueError):
                y = None
            if y is None or y < y0 - 0.3 or y > y1 + 0.3:
                if len(pts) > 1:
                    darab.append(pts)
                pts = []
                continue
            pts.append(f"{X(x):.1f},{Y(y):.1f}")
        if len(pts) > 1:
            darab.append(pts)
        for d in darab:
            ki.append(f'  <polyline points="{" ".join(d)}" fill="none" stroke="{szin}" '
                      'stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>')
    if jelmagyarazat:
        ly = fent + 2
        szeles = 4 + max(len(c) for _, _, c in gorbek)*6.6 + 26
        bx = max(6, w - szeles - 6)
        ki.append(f'  <rect x="{bx:.0f}" y="{fent - 3}" width="{szeles:.0f}" '
                  f'height="{len(gorbek)*17 + 6}" rx="4" fill="#ffffff" fill-opacity=".9"/>')
        for _, szin, cimke in gorbek:
            ki.append(f'  <line x1="{bx + 4:.0f}" y1="{ly + 4}" x2="{bx + 22:.0f}" y2="{ly + 4}" '
                      f'stroke="{szin}" stroke-width="2.4"/>')
            ki.append(f'  <text x="{bx + 27:.0f}" y="{ly + 8}" font-size="11" '
                      f'fill="#0f172a">{cimke}</text>')
            ly += 17
    ki.append('</svg>')
    return "\n".join(ki)


P2 = math.pi
SVG_SINCOS = svg_hullam(
    [(math.sin, "#047857", "y = sin x"), (math.cos, "#3b82f6", "y = cos x")],
    xr=(-2.2*P2, 2.3*P2), yr=(-1.6, 1.9),
    leiras="A szinusz- és a koszinuszgörbe: azonos alakú hullámok, fél pí eltolással")

SVG_TG = svg_hullam(
    [(lambda x: math.tan(x) if abs(math.cos(x)) > 1e-3 else None, "#047857", "y = tg x")],
    xr=(-1.7*P2, 1.8*P2), yr=(-4.2, 4.6), h=250,
    aszimptotak=[-1.5*P2, -0.5*P2, 0.5*P2, 1.5*P2],
    leiras="A tangensfüggvény grafikonja függőleges aszimptotákkal")

SVG_CTG = svg_hullam(
    [(lambda x: 1/math.tan(x) if abs(math.sin(x)) > 1e-3 else None, "#8b5cf6", "y = ctg x")],
    xr=(-1.7*P2, 1.8*P2), yr=(-4.2, 4.6), h=250,
    aszimptotak=[-P2, 0, P2, 2*P2],
    leiras="A kotangensfüggvény grafikonja függőleges aszimptotákkal")

SVG_AMPL = svg_hullam(
    [(math.sin, "#94a3b8", "y = sin x"),
     (lambda x: 2*math.sin(x), "#047857", "y = 2 sin x"),
     (lambda x: 0.5*math.sin(x), "#8b5cf6", "y = ½ sin x")],
    xr=(-0.4*P2, 2.3*P2), yr=(-2.4, 2.9), h=250,
    leiras="Az amplitúdó hatása: a görbe függőlegesen nyúlik vagy lapul")

SVG_PER = svg_hullam(
    [(math.sin, "#94a3b8", "y = sin x"),
     (lambda x: math.sin(2*x), "#047857", "y = sin 2x"),
     (lambda x: math.sin(x/2), "#3b82f6", "y = sin ½x")],
    xr=(-0.4*P2, 2.3*P2), yr=(-1.6, 2.0), h=240,
    leiras="A periódus hatása: a görbe vízszintesen sűrűsödik vagy ritkul")

SVG_FAZIS = svg_hullam(
    [(math.sin, "#94a3b8", "y = sin x"),
     (lambda x: math.sin(x + math.pi/2), "#047857", "y = sin(x + π/2)"),
     (lambda x: 2*math.sin(x - math.pi/3) + 1, "#ef4444", "y = 2sin(x − π/3) + 1")],
    xr=(-0.6*P2, 2.3*P2), yr=(-2.4, 3.4), h=260,
    leiras="Fáziseltolás és függőleges eltolás az alapgörbéhez képest")

SVG_EGY = svg_hullam(
    [(math.sin, "#047857", "y = sin x"), (lambda x: 0.5, "#ef4444", "y = ½")],
    xr=(-0.4*P2, 2.3*P2), yr=(-1.5, 1.9), h=230,
    leiras="A sin x egyenlő fél egyenlet megoldásai: a görbe és a vízszintes egyenes "
           "metszéspontjai")

# ===================================================================== C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> Amikor telepatikusan keresek valakit, nem egy pontot érzékelek, '
         'hanem egy <b>hullámot</b>. Minden elme saját frekvencián rezeg — és a rezgés '
         'matematikai alakja pontosan az, amit most rajzolunk fel. Eddig egy-egy szögnél '
         'kérdeztük meg a szinuszt; most nézzük meg, mit csinál <b>végig</b>, minden '
         'szögre egyszerre.'),
   'A trigonometrikus kör ehhez kész eszköz: ha a pont körbefut a körön, a szinusza (az '
   '$y$-koordinátája) fel-le mozog $-1$ és $1$ között. Ezt a mozgást „kiterítve” kapjuk '
   'a hullámot.',
 ]),

 ("A szinusz- és a koszinuszgörbe", [
   abra(SVG_SINCOS, "A két görbe <b>alakja azonos</b> — a koszinusz a szinusz "
                    "$\\tfrac{\\pi}{2}$-vel balra tolt képe: "
                    "$\\cos x=\\sin\\left(x+\\tfrac{\\pi}{2}\\right)$."),
   doboz("tetel", "Az $y=\\sin x$ és az $y=\\cos x$ tulajdonságai",
         '<div class="tblwrap"><table>'
         '<tr><th>Tulajdonság</th><th>$\\sin x$</th><th>$\\cos x$</th></tr>'
         '<tr><td>Értelmezési tartomány</td><td colspan="2">$\\mathbb{R}$</td></tr>'
         '<tr><td>Értékkészlet</td><td colspan="2">$[-1;1]$</td></tr>'
         '<tr><td>Periódus</td><td colspan="2">$2\\pi$ ($360^\\circ$)</td></tr>'
         '<tr><td>Nullahelyek</td><td>$x=k\\pi$</td><td>$x=\\tfrac{\\pi}{2}+k\\pi$</td></tr>'
         '<tr><td>Maximum ($1$)</td><td>$x=\\tfrac{\\pi}{2}+2k\\pi$</td><td>$x=2k\\pi$</td></tr>'
         '<tr><td>Minimum ($-1$)</td><td>$x=\\tfrac{3\\pi}{2}+2k\\pi$</td>'
         '<td>$x=\\pi+2k\\pi$</td></tr>'
         '<tr><td>Szimmetria</td><td><b>páratlan</b> (origóra)</td>'
         '<td><b>páros</b> ($y$-tengelyre)</td></tr>'
         '</table></div>'
         '<p>A szimmetria képlettel: $\\sin(-x)=-\\sin x$ és $\\cos(-x)=\\cos x$ — '
         'ezt a visszavezetésnél már használtuk.</p>',
         hid="tetel-sincos"),
   doboz("definicio", "Periodikus függvény",
         '<p>Az $f$ függvény <b>periodikus</b>, ha van olyan $p\\neq 0$ szám, hogy minden '
         '$x$-re</p>'
         '$$f(x+p)=f(x).$$'
         '<p>A legkisebb ilyen pozitív $p$ a függvény <b>periódusa</b>. A szinusznál és a '
         'koszinusznál ez $2\\pi$: egy teljes körbefordulás után minden ismétlődik.</p>',
         hid="def-periodikus"),
   kviz('Hol van az $y=\\cos x$ függvénynek maximuma?',
        ['$x=2k\\pi$', '$x=\\tfrac{\\pi}{2}+2k\\pi$', '$x=k\\pi$'], 0,
        jo="✔ cos 0 = 1, és ez 2π-ként ismétlődik.",
        nem="✘ A koszinusz a 0-ban veszi fel az 1-et, tehát x = 2kπ."),
 ]),

 ("A tangens és a kotangens", [
   abra(SVG_TG, "Az $y=\\operatorname{tg}x$ görbe. A szaggatott piros vonalak a "
                "<b>függőleges aszimptoták</b> ($x=\\tfrac{\\pi}{2}+k\\pi$), ahol a "
                "koszinusz nulla, tehát a függvény nincs értelmezve."),
   abra(SVG_CTG, "Az $y=\\operatorname{ctg}x$ görbe: <b>csökkenő</b> ágak, az aszimptoták "
                 "a $\\sin x=0$ helyeken, azaz $x=k\\pi$."),
   doboz("tetel", "Az $y=\\operatorname{tg}x$ és az $y=\\operatorname{ctg}x$",
         '<div class="tblwrap"><table>'
         '<tr><th>Tulajdonság</th><th>$\\operatorname{tg}x$</th><th>$\\operatorname{ctg}x$</th></tr>'
         '<tr><td>Értelmezési tartomány</td><td>$x\\neq\\tfrac{\\pi}{2}+k\\pi$</td>'
         '<td>$x\\neq k\\pi$</td></tr>'
         '<tr><td>Értékkészlet</td><td colspan="2">$\\mathbb{R}$ — <b>minden</b> valós értéket felvesz</td></tr>'
         '<tr><td>Periódus</td><td colspan="2">$\\pi$ ($180^\\circ$) — <b>nem</b> $2\\pi$!</td></tr>'
         '<tr><td>Nullahelyek</td><td>$x=k\\pi$</td><td>$x=\\tfrac{\\pi}{2}+k\\pi$</td></tr>'
         '<tr><td>Monotonitás</td><td>minden ágon <b>növekvő</b></td>'
         '<td>minden ágon <b>csökkenő</b></td></tr>'
         '<tr><td>Szimmetria</td><td colspan="2">mindkettő <b>páratlan</b></td></tr>'
         '</table></div>',
         hid="tetel-tgctg"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>A tangens periódusa $\\pi$, nem $2\\pi$!</b> Ezért a '
         '$\\operatorname{tg}x=1$ egyenlet megoldása $x=\\tfrac{\\pi}{4}+k\\pi$ — '
         'egyetlen családdal, míg a $\\sin x=a$ típusnál <b>kettő</b> kell.</p>'
         '<p>És a tangens értékkészlete a <b>teljes</b> $\\mathbb{R}$: a '
         '$\\operatorname{tg}x=100$ egyenletnek <b>van</b> megoldása, míg a '
         '$\\sin x=100$-nak nincs.</p>'),
   kviz('Mennyi az $y=\\operatorname{tg}x$ függvény periódusa?',
        ['$\\pi$', '$2\\pi$', '$\\tfrac{\\pi}{2}$'], 0,
        jo="✔ A tangens 180°-onként ismétlődik.",
        nem="✘ A tg és a ctg periódusa π, csak a sin és a cos periódusa 2π."),
   gyakorolj(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–3"),
 ]),
]

# ===================================================================== C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> Egy valódi jel sosem a tiszta $\\sin x$. Van <b>erőssége</b> '
         '(mekkorát hullámzik), <b>frekvenciája</b> (milyen sűrűn) és <b>fázisa</b> '
         '(mikor kezdődik). Ez a három adat az $A$, a $b$ és a $c$ — és mindhárom '
         'ugyanúgy viselkedik, mint a korábbi függvénytranszformációknál. Ha ezt '
         'elolvasod egy grafikonról, gyakorlatilag megfejtetted a jelet.'),
 ]),

 ("Az amplitúdó", [
   abra(SVG_AMPL, "Az $y=A\\sin x$ görbe $|A|$-szorosára nyúlik függőlegesen. "
                  "Az értékkészlet $[-|A|;|A|]$, a periódus <b>nem változik</b>."),
   doboz("tetel", "Amplitúdó",
         '<p>Az $y=A\\sin x$ függvény <b>amplitúdója</b> $|A|$: ennyivel tér ki a görbe '
         'a középvonaltól. Az értékkészlet $[-|A|;|A|]$.</p>'
         '<p>Ha $A&lt;0$, a görbe ezen felül <b>tükröződik</b> az $x$-tengelyre.</p>',
         hid="tetel-amplitudo"),
 ]),

 ("A periódus", [
   abra(SVG_PER, "Az $y=\\sin bx$ görbe vízszintesen <b>összenyomódik</b> ($b&gt;1$) "
                 "vagy <b>széthúzódik</b> ($0&lt;b&lt;1$)."),
   doboz("tetel", "Periódus",
         '<p>Az $y=\\sin bx$ (és az $y=\\cos bx$) függvény periódusa</p>'
         '$$p=\\frac{2\\pi}{|b|}\\qquad(b\\neq 0),$$'
         '<p>az $y=\\operatorname{tg}bx$ függvényé pedig $p=\\dfrac{\\pi}{|b|}$.</p>'
         '<p>Vagyis $b$ azt mondja meg, <b>hányszor</b> fut le egy teljes hullám a '
         'megszokott $2\\pi$ hosszon.</p>',
         hid="tetel-periodus"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A $b$ <b>osztja</b> a periódust, nem szorozza. Az $y=\\sin 2x$ periódusa '
         '$\\pi$ (rövidebb!), az $y=\\sin\\tfrac{x}{2}$ periódusa $4\\pi$ (hosszabb).</p>'
         '<p>Ez fordítottan hat, mint az amplitúdó — érdemes minden feladatnál egy '
         'próbaértéket behelyettesíteni.</p>'),
   kviz('Mekkora az $y=\\sin(3x)$ függvény periódusa?',
        ['$\\tfrac{2\\pi}{3}$', '$2\\pi$', '$6\\pi$'], 0,
        jo="✔ A B szorzó OSZTJA a periódust: 2π/3. Nagyobb B → sűrűbb, rövidebb hullám.",
        nem="✘ Vigyázz, ez fordítva hat, mint az amplitúdó: az y = sin(Bx) periódusa 2π/B, "
            "tehát B = 3 esetén 2π/3 — a görbe SŰRŰBB lesz."),
 ]),

 ("Fáziseltolás és a teljes alak", [
   abra(SVG_FAZIS, "A $+c$ a kitevőben <b>balra</b>, a $-c$ <b>jobbra</b> tolja a görbét; "
                   "a végén álló $+d$ pedig <b>felfelé</b>."),
   doboz("tetel", "Az $y=A\\sin(bx+c)+d$ alak",
         '<div class="tblwrap"><table>'
         '<tr><th>Paraméter</th><th>Neve</th><th>Hatása</th></tr>'
         '<tr><td>$A$</td><td>amplitúdó</td><td>függőleges nyújtás $|A|$-szorosára; '
         '$A&lt;0$ → tükrözés</td></tr>'
         '<tr><td>$b$</td><td>körfrekvencia</td><td>a periódus $\\tfrac{2\\pi}{|b|}$</td></tr>'
         '<tr><td>$c$</td><td>fázis</td><td>vízszintes eltolás '
         '<b>$-\\tfrac{c}{b}$-vel</b></td></tr>'
         '<tr><td>$d$</td><td>középvonal</td><td>függőleges eltolás; az értékkészlet '
         '$[d-|A|;\\,d+|A|]$</td></tr>'
         '</table></div>'
         '<p>⚠️ A vízszintes eltolás <b>nem</b> $c$, hanem $-\\tfrac{c}{b}$ — mert a '
         'zárójelből ki kell emelni a $b$-t: $bx+c=b\\left(x+\\tfrac{c}{b}\\right)$.</p>',
         hid="tetel-teljes-alak"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Add meg az $y=3\\sin\\left(2x-\\tfrac{\\pi}{3}\\right)+1$ függvény '
         'amplitúdóját, periódusát, fáziseltolását és értékkészletét!</p>',
         hid="pelda-teljes-alak",
         lenyilo=("Megoldás",
                  '<p><b>Amplitúdó:</b> $|A|=3$.</p>'
                  '<p><b>Periódus:</b> $p=\\dfrac{2\\pi}{2}=\\pi$.</p>'
                  '<p><b>Fáziseltolás:</b> emeljük ki a $2$-t: '
                  '$2x-\\tfrac{\\pi}{3}=2\\left(x-\\tfrac{\\pi}{6}\\right)$, tehát a görbe '
                  '$\\tfrac{\\pi}{6}$-tal <b>jobbra</b> tolódik.</p>'
                  '<p><b>Értékkészlet:</b> a középvonal $y=1$, az amplitúdó $3$, tehát '
                  '$[1-3;\\,1+3]=\\boxed{[-2;4]}$.</p>')),
   doboz("erdekesseg", "Ez a hangod és a váltakozó áram is",
         '<p>Egy tiszta hang matematikai alakja $y=A\\sin(2\\pi f t)$: az $A$ a '
         '<b>hangerő</b>, az $f$ a <b>frekvencia</b> (hertzben), ami a magasságot adja. '
         'A hálózati feszültség szintén ilyen: $230\\,\\text{V}$ effektív érték, '
         '$50\\,\\text{Hz}$ — vagyis másodpercenként ötvenszer fut le a teljes hullám.</p>'),
   kviz('Mennyi az $y=\\sin 3x$ függvény periódusa?',
        ['$\\tfrac{2\\pi}{3}$', '$6\\pi$', '$3\\pi$'], 0,
        jo="✔ p = 2π / |b| = 2π/3.",
        nem="✘ A b OSZTJA a periódust: 2π/3."),
   gyakorolj(FGY + "#alap-6", "A 6–11", FGY + "#kozep-4", "K 4–8"),
 ]),
]

# ===================================================================== C3

C3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> És most a lényeg: <i>mikor</i> éri el a jel a keresett '
         'értéket? Ez trigonometrikus egyenlet — és van benne egy csavar, amihez nem '
         'vagy hozzászokva. Mivel a hullám <b>ismétlődik</b>, nem egy megoldás van, '
         'hanem <b>végtelen sok</b>. A feladat nem egy szám, hanem egy <b>képlet</b>, '
         'amely az összeset megadja.'),
 ]),

 ("Az alapegyenletek", [
   abra(SVG_EGY, "A $\\sin x=\\tfrac12$ egyenlet megoldásai ott vannak, ahol a "
                 "hullám metszi az $y=\\tfrac12$ egyenest — <b>periódusonként kétszer</b>."),
   doboz("tetel", "A három alaptípus",
         '<p>Legyen $\\alpha$ az az <b>alapszög</b> az első negyedben, amelyre a keresett '
         'függvényérték abszolút értéke teljesül.</p>'
         '<p><b>1.</b> $\\sin x=a$ (csak ha $|a|\\le 1$): <b>két</b> megoldáscsalád, mert a '
         'szinusz két negyedben veszi fel ugyanazt az értéket.</p>'
         '<p><b>2.</b> $\\cos x=a$ (csak ha $|a|\\le 1$): szintén két család, amelyek '
         'gyakran $\\pm$ alakba vonhatók össze.</p>'
         '<p><b>3.</b> $\\operatorname{tg}x=a$ (bármely $a$-ra): <b>egyetlen</b> család, '
         'mert a periódus $\\pi$.</p>'
         '<p>Minden megoldáshoz oda kell írni a periódust — és a $k\\in\\mathbb{Z}$-t!</p>',
         hid="tetel-alaptipusok"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg! <b>a)</b> $2\\sin x-1=0$; <b>b)</b> $2\\cos x+\\sqrt3=0$; '
         '<b>c)</b> $\\operatorname{tg}x=1$.</p>',
         hid="pelda-alapegyenletek",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\sin x=\\tfrac12$. Az alapszög $\\tfrac{\\pi}{6}$, és a '
                  'szinusz az <b>I. és a II.</b> negyedben pozitív:</p>'
                  '$$x=\\frac{\\pi}{6}+2k\\pi\\quad\\text{vagy}\\quad '
                  'x=\\frac{5\\pi}{6}+2k\\pi,\\qquad k\\in\\mathbb{Z}$$'
                  '<p><b>b)</b> $\\cos x=-\\tfrac{\\sqrt3}{2}$. Az alapszög '
                  '$\\tfrac{\\pi}{6}$, és a koszinusz a <b>II. és a III.</b> negyedben '
                  'negatív:</p>'
                  '$$x=\\frac{5\\pi}{6}+2k\\pi\\quad\\text{vagy}\\quad '
                  'x=\\frac{7\\pi}{6}+2k\\pi,\\qquad k\\in\\mathbb{Z}$$'
                  '<p><b>c)</b> A tangens periódusa $\\pi$, ezért egyetlen család elég:</p>'
                  '$$x=\\frac{\\pi}{4}+k\\pi,\\qquad k\\in\\mathbb{Z}$$')),
   doboz("tetel", "A négy speciális eset",
         '<p>Ha az érték épp $\\pm 1$ vagy $0$, a két család <b>egybeesik</b>:</p>'
         '<div class="tblwrap"><table>'
         '<tr><th>Egyenlet</th><th>Megoldás</th></tr>'
         '<tr><td>$\\sin x=1$</td><td>$x=\\tfrac{\\pi}{2}+2k\\pi$</td></tr>'
         '<tr><td>$\\sin x=-1$</td><td>$x=\\tfrac{3\\pi}{2}+2k\\pi$</td></tr>'
         '<tr><td>$\\sin x=0$</td><td>$x=k\\pi$</td></tr>'
         '<tr><td>$\\cos x=1$</td><td>$x=2k\\pi$</td></tr>'
         '<tr><td>$\\cos x=-1$</td><td>$x=\\pi+2k\\pi$</td></tr>'
         '<tr><td>$\\cos x=0$</td><td>$x=\\tfrac{\\pi}{2}+k\\pi$</td></tr>'
         '</table></div>',
         hid="tetel-specialis"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Három visszatérő hiba:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>Elhagyni a $+2k\\pi$-t.</b> A $x=\\tfrac{\\pi}{6}$ önmagában <b>nem</b> '
         'a megoldás, csak egy megoldás. A feladat az <b>összeset</b> kérdezi.</li>'
         '<li><b>Csak az egyik családot megadni.</b> A $\\sin x=\\tfrac12$-nek '
         '<b>két</b> családja van — a második nem $\\tfrac{\\pi}{6}$-ból, hanem a '
         'másik negyedből jön.</li>'
         '<li><b>Nem venni észre, ha nincs megoldás.</b> A $\\sin x=1{,}5$ vagy a '
         '$\\cos x=-3$ egyenletnek <b>nincs</b> megoldása, mert az értékkészlet '
         '$[-1;1]$.</li>'
         '</ol>'),
 ]),

 ("Ha a szög nem $x$, hanem $bx$", [
   'Ez a leggyakoribb továbblépés — és pontosan itt szokott elcsúszni a periódus.',
   doboz("tetel", "A helyettesítéses gondolat",
         '<p>Ha az egyenlet $\\sin bx=a$ alakú, kezeld a $bx$-et <b>egyetlen szögként</b>: '
         'oldd meg a $bx$-re, és <b>csak a legvégén</b> ossz $b$-vel — a $2k\\pi$-t is!</p>'
         '<p>Így a megoldások periódusa $\\tfrac{2k\\pi}{b}$ lesz, tehát '
         '<b>sűrűbben</b> következnek.</p>',
         hid="tetel-bx"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg! <b>a)</b> $2\\sin 2x+\\sqrt2=0$; <b>b)</b> $2\\cos 3x=\\sqrt3$.</p>',
         hid="pelda-bx",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\sin 2x=-\\tfrac{\\sqrt2}{2}$. Az alapszög '
                  '$\\tfrac{\\pi}{4}$, a szinusz a III. és a IV. negyedben negatív:</p>'
                  '$$2x=\\frac{5\\pi}{4}+2k\\pi\\quad\\text{vagy}\\quad '
                  '2x=\\frac{7\\pi}{4}+2k\\pi$$'
                  '<p>Most osztunk $2$-vel — <b>minden</b> tagot:</p>'
                  '$$x=\\frac{5\\pi}{8}+k\\pi\\quad\\text{vagy}\\quad '
                  'x=\\frac{7\\pi}{8}+k\\pi,\\qquad k\\in\\mathbb{Z}$$'
                  '<p><b>b)</b> $\\cos 3x=\\tfrac{\\sqrt3}{2}$, az alapszög '
                  '$\\tfrac{\\pi}{6}$, a koszinusz az I. és a IV. negyedben pozitív:</p>'
                  '$$3x=\\pm\\frac{\\pi}{6}+2k\\pi\\ \\Longrightarrow\\ '
                  'x=\\pm\\frac{\\pi}{18}+\\frac{2k\\pi}{3},\\qquad k\\in\\mathbb{Z}$$')),
   kviz('Mi a $\\sin x=-1$ egyenlet megoldása?',
        ['$x=\\tfrac{3\\pi}{2}+2k\\pi$', '$x=-\\tfrac{\\pi}{2}+k\\pi$',
         '$x=\\tfrac{\\pi}{2}+2k\\pi$'], 0,
        jo="✔ A szinusz a 3π/2-ben (270°-ban) veszi fel a −1-et, és ez 2π-ként ismétlődik.",
        nem="✘ A minimumhely x = 3π/2 + 2kπ (ez ugyanaz, mint −π/2 + 2kπ)."),
   gyakorolj(FGY + "#alap-12", "A 12–18", FGY + "#kozep-9", "K 9–14"),
   brief('<b>Szürke Janka:</b> A hullámot értjük, az egyenleteket megoldjuk. Egy dolog maradt, '
         'és az a legkézzelfoghatóbb az egészben: ha a terepen ismerek <b>néhány</b> '
         'távolságot és szöget, ki tudom-e számolni a többit? Ehhez két tétel kell — és '
         'ezekkel bemérhető egy torony, egy hegy vagy egy ellenséges bázis.', outro=True),
 ]),

 ("Alap trigonometrikus egyenlőtlenségek", [
   'Az egyenletnél azt kérdeztük: <b>hol</b> veszi fel a függvény az adott értéket. Az '
   'egyenlőtlenségnél azt: <b>hol nagyobb</b> (vagy kisebb) nála. A megoldás ezért nem néhány pont lesz, hanem <b>szögtartomány</b> — és a periodicitás miatt abból is végtelen sok.',
   doboz("tetel", "A menet — három lépés",
         '<ol><li>Keresd meg a <b>határszögeket</b>: oldd meg az egyenlőséget ($\\sin x=\\tfrac12$).</li>'
         '<li>Nézd meg a <b>trigonometrikus körön</b> (vagy a grafikonon), a két határ <b>melyik oldalán</b> teljesül az egyenlőtlenség.</li>'
         '<li>Írd fel a tartományt, és told el <b>periódusonként</b>: $+k\\cdot 360^\\circ$, ahol $k\\in\\mathbb{Z}$.</li></ol>'
         '<p>A zárójel a szokásos: szigorú egyenlőtlenségnél <b>nyílt</b>, $\\le$ vagy $\\ge$ esetén <b>zárt</b> végpont.</p>',
         hid="tetel-trig-egyenlotlenseg"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $\\sin x&gt;\\tfrac12$; <b>b)</b> $\\cos x\\le\\tfrac12$.</p>',
         hid="pelda-trig-egyenlotlenseg",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> A határszögek: $\\sin x=\\tfrac12$ esetén $x=30^\\circ$ és $x=150^\\circ$. A körön a szinusz az <b>y-koordináta</b>, ez a kettő <b>között</b> nagyobb $\\tfrac12$-nél (ott halad a felső ív). Tehát</p>'
                  '$$x\\in\\left(30^\\circ+k\\cdot 360^\\circ;\\ 150^\\circ+k\\cdot 360^\\circ\\right).$$'
                  '<p>Ellenőrzés: $x=90^\\circ$ benne van, és $\\sin 90^\\circ=1&gt;\\tfrac12$ ✔; $x=200^\\circ$ nincs benne, és $\\sin 200^\\circ&lt;0$ ✔</p>'
                  '<p><b>b)</b> A határszögek: $\\cos x=\\tfrac12$ esetén $x=60^\\circ$ és $x=300^\\circ$. A koszinusz az <b>x-koordináta</b>, és a két határ <b>között</b> (a kör bal oldalán haladva) kisebb $\\tfrac12$-nél. Mivel $\\le$ áll, a végpontok is beletartoznak:</p>'
                  '$$x\\in\\left[60^\\circ+k\\cdot 360^\\circ;\\ 300^\\circ+k\\cdot 360^\\circ\\right].$$'
                  '<p>Ellenőrzés: $x=180^\\circ$ benne van, és $\\cos 180^\\circ=-1\\le\\tfrac12$ ✔; $x=10^\\circ$ nincs benne, és $\\cos 10^\\circ\\approx 0{,}98&gt;\\tfrac12$ ✔</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>„Megvan a két határszög, kész.”</b> — Nem. Két dolog hiányzik még: '
         'melyik <b>oldalon</b> teljesül az egyenlőtlenség, és a <b>periódus</b>.</p>'
         '<p>A $+k\\cdot 360^\\circ$ elhagyása a leggyakoribb hiba: az egyenlőtlenségnek <b>végtelen sok</b> megoldás-intervalluma van, nem csak egy. Ha a feladat mégis egyetlen körre szorítkozik (pl. $x\\in[0^\\circ;360^\\circ)$), azt a szöveg külön kimondja.</p>'),
   kviz('Mi a $\\sin x&gt;\\tfrac12$ megoldása a $[0^\\circ;360^\\circ)$ körön?',
        ['$(30^\\circ;150^\\circ)$', '$(150^\\circ;330^\\circ)$', '$(0^\\circ;30^\\circ)$'], 0,
        jo="✔ A két határszög 30° és 150°, és közöttük halad a kör felső íve, ahol a szinusz (az y-koordináta) nagyobb 1/2-nél.",
        nem="✘ A határszögek 30° és 150°. Kérdés, hogy közöttük vagy rajtuk kívül nagyobb a szinusz 1/2-nél: a kör FELSŐ ívén, tehát 30° és 150° KÖZÖTT."),
 ]),

]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-trig-fuggvenyek-grafikonja.html",
     cim="A trigonometrikus függvények grafikonja",
     cim_tiszta="A trigonometrikus függvények grafikonja",
     alcim="A szinusz-, koszinusz-, tangens- és kotangensgörbe, a periodicitás, "
           "az értékkészlet és a szimmetriák.",
     chip="A Fázisugrás · 7/11", szakaszok=C1,
     elozo=("feladatok-azonossagok.html", "Feladatok — azonosságok"),
     kovetkezo=("tananyag-osszetett-trig-fuggvenyek.html",
                "Amplitúdó, periódus és fáziseltolás")),
 lap(**T, fajl="tananyag-osszetett-trig-fuggvenyek.html",
     cim="Amplitúdó, periódus és fáziseltolás",
     cim_tiszta="Amplitúdó, periódus és fáziseltolás",
     alcim="Az $y=A\\sin(bx+c)+d$ alakú függvények: mit csinál külön-külön a négy "
           "paraméter, és hogyan olvasható le egy grafikonról.",
     chip="A Fázisugrás · 8/11", szakaszok=C2,
     elozo=("tananyag-trig-fuggvenyek-grafikonja.html",
            "A trigonometrikus függvények grafikonja"),
     kovetkezo=("tananyag-trigonometrikus-egyenletek.html",
                "Egyszerű trigonometrikus egyenletek")),
 lap(**T, fajl="tananyag-trigonometrikus-egyenletek.html",
     cim="Egyszerű trigonometrikus egyenletek",
     cim_tiszta="Egyszerű trigonometrikus egyenletek",
     alcim="A három alaptípus, a végtelen sok megoldás felírása, a speciális esetek "
           "és a $bx$ alakú szögek kezelése.",
     chip="A Fázisugrás · 9/11", szakaszok=C3,
     elozo=("tananyag-osszetett-trig-fuggvenyek.html", "Amplitúdó, periódus és fáziseltolás"),
     kovetkezo=(FGY, "Feladatok — függvények és egyenletek")),
]
for u in KI:
    print("✓", os.path.basename(u))
