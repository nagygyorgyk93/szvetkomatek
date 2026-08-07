# -*- coding: utf-8 -*-
"""2e/04 — B altema: alapazonossagok (B1), addicios kepletek es ketszeres szog (B2),
felszog es osszeg-szorzat atalakitas (B3). Mentor: Éjjáró."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_egysegkor

T = dict(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
         temakor="Trigonometrikus függvények")
FGY = "feladatok-azonossagok.html"

# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, sin, cos, tan, cot, rad, simplify, radsimp, N
E = []
def chk(n, g, w, tol=None):
    ok = abs(float(g) - w) < tol if tol is not None else simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
# B1
chk("B1-1", R(3, 5)**2 + R(-4, 5)**2, 1)
chk("B1-2", R(-5, 13)**2 + R(-12, 13)**2, 1)
chk("B1-tg", R(3, 5)/R(-4, 5), R(-3, 4))
chk("B1-ctg", R(-12, 13)/R(-5, 13), R(12, 5))
chk("B1-pit", 1 + tan(rad(60))**2 - 1/cos(rad(60))**2, 0)
# B2
chk("B2-cos75", cos(rad(75)), (sqrt(6) - sqrt(2))/4)
chk("B2-sin15", sin(rad(15)), (sqrt(6) - sqrt(2))/4)
chk("B2-sin105", sin(rad(105)), (sqrt(6) + sqrt(2))/4)
chk("B2-tg75", tan(rad(75)) - (2 + sqrt(3)), 0, 1e-25)
chk("B2-osszeg", R(3, 5)*R(5, 13) + R(4, 5)*R(12, 13), R(63, 65))
chk("B2-osszeg2", R(4, 5)*R(5, 13) - R(3, 5)*R(12, 13), R(-16, 65))
chk("B2-2a", 2*R(4, 5)*R(3, 5), R(24, 25))
chk("B2-2b", R(3, 5)**2 - R(4, 5)**2, R(-7, 25))
chk("B2-felism", sin(rad(25))*cos(rad(35)) + cos(rad(25))*sin(rad(35)) - sqrt(3)/2, 0, 1e-25)
chk("B2-felism2", cos(rad(70))*cos(rad(25)) + sin(rad(70))*sin(rad(25)) - sqrt(2)/2, 0, 1e-25)
# B3
chk("B3-sinf", sqrt((1 - R(7, 25))/2), R(3, 5))
chk("B3-cosf", sqrt((1 + R(7, 25))/2), R(4, 5))
chk("B3-sin225", sin(rad(R(45, 2))) - sqrt(2 - sqrt(2))/2, 0, 1e-25)
chk("B3-sz1", sin(rad(75)) + sin(rad(15)) - sqrt(6)/2, 0, 1e-25)
chk("B3-sz2", cos(rad(40)) + cos(rad(20)) - sqrt(3)*cos(rad(10)), 0, 1e-25)
chk("B3-sz3", cos(rad(20)) - cos(rad(80)) - sin(rad(50)), 0, 1e-25)
assert not E, E
print("sympy önteszt: OK")

SVG_ALAP = svg_egysegkor(
    szogek=[(52, "P(cos α; sin α)", "#047857")], w=340, h=310, vetulet=True,
    leiras="Az egységkörön a P pont vetületei adják a koszinuszt és a szinuszt; a sugár, a vetület és a vetítővonal derékszögű háromszöget alkot, erre írjuk fel a Pitagorasz-tételt",
    sugar_cimke="1")

# ===================================================================== B1

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Éjjáró:</b> Van egy visszatérő helyzet a terepen: tudom az egyik '
         'koordinátámat, és tudom, melyik <b>negyedben</b> vagyok — a másikat magamtól '
         'kell kitalálnom. Erre való az alapazonosság. Egyetlen képlet, egyetlen '
         'négyzetgyök, és a <b>negyed dönti el az előjelet</b>. Ez a témakör '
         'leggyakoribb feladattípusa, úgyhogy érdemes automatikussá tenni.'),
 ]),

 ("Az alapazonosságok", [
   abra(SVG_ALAP, "A $P$ pont koordinátái $\\cos\\alpha$ és $\\sin\\alpha$, a sugár $1$ — "
                  "a sugárból és a két vetületből álló derékszögű háromszögre felírt "
                  "Pitagorasz-tétel adja a <b>négyzetes alapazonosságot</b>."),
   doboz("tetel", "A hat alapazonosság",
         '<p>Az első <b>minden</b> szögre igaz; a többi csak ott, ahol a szereplő '
         'függvények értelmezve vannak — a feltételt mindegyik mellé odaírtuk.</p>'
         '$$\\sin^{2}\\alpha+\\cos^{2}\\alpha=1$$'
         '$$\\operatorname{tg}\\alpha=\\frac{\\sin\\alpha}{\\cos\\alpha}\\ (\\cos\\alpha\\neq 0),\\qquad'
         '\\operatorname{ctg}\\alpha=\\frac{\\cos\\alpha}{\\sin\\alpha}\\ (\\sin\\alpha\\neq 0)$$'
         '$$\\operatorname{tg}\\alpha\\cdot\\operatorname{ctg}\\alpha=1\\qquad\\left(\\alpha\\neq k\\cdot\\tfrac{\\pi}{2}\\right)$$'
         '<p>A négyzetes azonosságot $\\cos^{2}\\alpha$-val osztva (ez $\\cos\\alpha\\neq 0$ '
         'esetén tehető meg), illetve $\\sin^{2}\\alpha$-val osztva ($\\sin\\alpha\\neq 0$ '
         'esetén) két további adódik:</p>'
         '$$1+\\operatorname{tg}^{2}\\alpha=\\frac{1}{\\cos^{2}\\alpha}\\ (\\cos\\alpha\\neq 0),\\qquad'
         '1+\\operatorname{ctg}^{2}\\alpha=\\frac{1}{\\sin^{2}\\alpha}\\ (\\sin\\alpha\\neq 0).$$',
         hid="tetel-alapazonossagok"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>A négyzetre emelés elveszíti az előjelet</b> — nem a gyökvonás enged meg két '
         'értéket, hiszen $\\sqrt{\\cos^{2}\\alpha}=|\\cos\\alpha|$. Abból viszont, hogy '
         '$\\cos^{2}\\alpha$ ismert, két lehetséges $\\cos\\alpha$ következik:</p>'
         '$$\\cos\\alpha=\\pm\\sqrt{1-\\sin^{2}\\alpha},\\qquad'
         '\\sin\\alpha=\\pm\\sqrt{1-\\cos^{2}\\alpha}$$'
         '<p>A negyed dönti el, melyik kell — <b>függvényenként külön</b>: a koszinusz a II. és '
         'a III., a szinusz a III. és a IV. negyedben negatív. Ezért ad a feladatszöveg '
         '<b>jellemzően</b> egy második információt ($\\cos\\alpha&lt;0$, '
         '$\\operatorname{tg}\\alpha&gt;0$, $\\alpha\\in\\left(\\tfrac{\\pi}{2};\\pi\\right)$…) '
         '— enélkül a feladatnak két megoldása van.</p>'),
   kviz('Mennyi $\\sin^{2}\\alpha+\\cos^{2}\\alpha$ értéke?',
        ['$1$ — minden valós $\\alpha$-ra', '$\\alpha$', 'Az $\\alpha$-tól függ'], 0,
        jo="✔ Ez a négyzetes alapazonosság. Az egységkörön a P pont koordinátái cos α és "
           "sin α, az origótól mért távolsága pedig mindig 1.",
        nem="✘ Ez a trigonometria legfontosabb azonossága: minden valós α-ra 1. "
            "Az egységkörön a koordináták négyzetösszege a sugár négyzete, azaz 1."),
 ]),

 ("A tipikus feladat: egy érték + a negyed", [
   doboz("tetel", "A munkamenet",
         '<p><b>1.</b> A két adatból derítsd ki, <b>melyik negyedben</b> van a szög.</p>'
         '<p><b>2.</b> Az alapazonosságból számold ki a hiányzó másikat, és tedd elé a '
         'negyednek megfelelő <b>előjelet</b>.</p>'
         '<p><b>3.</b> A $\\operatorname{tg}$ és a $\\operatorname{ctg}$ már csak osztás — '
         'de az előjelüket érdemes az előjeltáblázattal <b>ellenőrizni</b>.</p>',
         hid="tetel-menetrend"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számold ki a másik három függvény pontos értékét! '
         '<b>a)</b> $\\sin\\alpha=\\tfrac35$ és $\\cos\\alpha&lt;0$; '
         '<b>b)</b> $\\cos\\alpha=-\\tfrac{12}{13}$ és $\\sin\\alpha&lt;0$.</p>',
         hid="pelda-alapazonossag",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\sin\\alpha&gt;0$ és $\\cos\\alpha&lt;0$ → <b>II. negyed</b>.</p>'
                  '$$\\cos^{2}\\alpha=1-\\left(\\tfrac35\\right)^{2}=\\tfrac{16}{25}'
                  '\\ \\Longrightarrow\\ \\cos\\alpha=\\pm\\tfrac45$$'
                  '<p>A II. negyedben a koszinusz negatív, tehát $\\cos\\alpha=-\\tfrac45$.</p>'
                  '<p>$\\operatorname{tg}\\alpha=\\dfrac{3/5}{-4/5}=-\\dfrac34$, &nbsp; '
                  '$\\operatorname{ctg}\\alpha=-\\dfrac43$. A II. negyedben mindkettő '
                  'negatív ✔</p>'
                  '<p><b>b)</b> Mindkettő negatív → <b>III. negyed</b>.</p>'
                  '$$\\sin^{2}\\alpha=1-\\left(\\tfrac{12}{13}\\right)^{2}=\\tfrac{25}{169}'
                  '\\ \\Longrightarrow\\ \\sin\\alpha=\\pm\\tfrac{5}{13}$$'
                  '<p>A III. negyedben a szinusz negatív, tehát $\\sin\\alpha=-\\tfrac{5}{13}$.</p>'
                  '<p>$\\operatorname{tg}\\alpha=\\dfrac{-5/13}{-12/13}=\\dfrac{5}{12}$, &nbsp; '
                  '$\\operatorname{ctg}\\alpha=\\dfrac{12}{5}$ — a III. negyedben mindkettő '
                  'pozitív ✔</p>')),
   doboz("erdekesseg", "Pitagoraszi számhármasok",
         '<p>A feladatokban ismétlődnek ugyanazok a törtek: $\\tfrac35$–$\\tfrac45$, '
         '$\\tfrac{5}{13}$–$\\tfrac{12}{13}$, $\\tfrac{8}{17}$–$\\tfrac{15}{17}$, '
         '$\\tfrac{9}{41}$–$\\tfrac{40}{41}$, $\\tfrac{20}{29}$–$\\tfrac{21}{29}$. Nem '
         'véletlenül: ezek <b>pitagoraszi számhármasok</b> ($3,4,5$ · $5,12,13$ · '
         '$8,15,17$ · $9,40,41$ · $20,21,29$), így a gyökvonás mindig „szép” eredményt ad. '
         'Ha felismered őket, a számolás fele kész.</p>'),
   kviz('Ha $\\cos\\alpha=\\tfrac{4}{5}$ és $\\operatorname{tg}\\alpha&lt;0$, mennyi $\\sin\\alpha$?',
        ['$-\\tfrac35$', '$\\tfrac35$', '$-\\tfrac45$'], 0,
        jo="✔ cos > 0 és tg < 0 → IV. negyed, ott a szinusz negatív.",
        nem="✘ A cos pozitív, a tg negatív → IV. negyed → a szinusz negatív: −3/5."),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
 ]),
]

# ===================================================================== B2

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Éjjáró:</b> Eddig csak a $30$–$45$–$60$-as szögeket tudtuk pontosan. '
         'De mi van, ha $75^\\circ$-ra kell ugranom? Egyszerű: $75=45+30$ — <b>két ugrás '
         'egymás után</b>. Az addíciós képletek pontosan ezt mondják meg: hogyan lehet '
         'két szög összegének a szögfüggvényét a külön-külön ismert értékekből '
         'kiszámolni.'),
 ]),

 ("Az addíciós képletek", [
   doboz("tetel", "Két szög összege és különbsége",
         '$$\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta$$'
         '$$\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta$$'
         '$$\\operatorname{tg}(\\alpha\\pm\\beta)=\\frac{\\operatorname{tg}\\alpha\\pm'
         '\\operatorname{tg}\\beta}{1\\mp\\operatorname{tg}\\alpha\\operatorname{tg}\\beta}$$'
         '<p>Figyeld meg a <b>jelek</b> viselkedését: a szinusznál a jel „átmegy”, a '
         'koszinusznál <b>megfordul</b> ($\\mp$). Ez a legtöbbet elrontott részlet.</p>'
         '<p class="halvany">A szinuszos és a koszinuszos képlet <b>minden</b> valós $\\alpha$-ra és $\\beta$-ra érvényes. A tangenses csak ott, ahol mindhárom tangens értelmezett — tehát $\\cos\\alpha\\neq 0$, $\\cos\\beta\\neq 0$ és $\\cos(\\alpha\\pm\\beta)\\neq 0$ —, és ahol a nevező nem tűnik el: $1\\mp\\operatorname{tg}\\alpha\\operatorname{tg}\\beta\\neq 0$.</p>',
         hid="tetel-addicios"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>A szögfüggvény nem „szorzó”!</b></p>'
         '<p>✘ $\\sin(\\alpha+\\beta)=\\sin\\alpha+\\sin\\beta$ &nbsp;&nbsp; '
         '✔ $\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta$</p>'
         '<p>Próbáld ki: $\\sin(30^\\circ+60^\\circ)=\\sin 90^\\circ=1$, míg '
         '$\\sin 30^\\circ+\\sin 60^\\circ=\\tfrac12+\\tfrac{\\sqrt3}{2}\\approx 1{,}37$ — '
         'nem egyenlők.</p>'
         '<p>A koszinusznál pedig <b>ellentétes</b> a jel: $\\cos(\\alpha+\\beta)$-ban '
         '<b>mínusz</b> áll, $\\cos(\\alpha-\\beta)$-ban <b>plusz</b>.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p><b>a)</b> Számold ki pontosan: $\\cos 75^\\circ$.<br>'
         '<b>b)</b> Számold ki $\\sin(\\alpha+\\beta)$-t, ha $\\sin\\alpha=\\tfrac35$ és '
         '$\\cos\\beta=\\tfrac{5}{13}$, mindkét szög hegyesszög.</p>',
         hid="pelda-addicios",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $75^\\circ=45^\\circ+30^\\circ$:</p>'
                  '$$\\cos 75^\\circ=\\cos 45^\\circ\\cos 30^\\circ-\\sin 45^\\circ\\sin 30^\\circ'
                  '=\\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2}-\\frac{\\sqrt2}{2}\\cdot\\frac12'
                  '=\\boxed{\\frac{\\sqrt6-\\sqrt2}{4}}\\approx 0{,}25882$$'
                  '<p><b>b)</b> Előbb a hiányzó értékek (hegyesszög → minden pozitív): '
                  '$\\cos\\alpha=\\tfrac45$, $\\sin\\beta=\\tfrac{12}{13}$.</p>'
                  '$$\\sin(\\alpha+\\beta)=\\frac35\\cdot\\frac{5}{13}+\\frac45\\cdot'
                  '\\frac{12}{13}=\\frac{15+48}{65}=\\boxed{\\frac{63}{65}}$$')),
 ]),

 ("Felismerés — a képlet visszafelé", [
   'A vizsgákon gyakoribb az a feladat, amelyben a képlet <b>jobb</b> oldala van megadva, '
   'és a bal oldalt kell felismerni. Ez sokkal gyorsabb, mint kiszámolni.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számold ki az értéküket! '
         '<b>a)</b> $\\sin 25^\\circ\\cos 35^\\circ+\\cos 25^\\circ\\sin 35^\\circ$; '
         '<b>b)</b> $\\cos 70^\\circ\\cos 25^\\circ+\\sin 70^\\circ\\sin 25^\\circ$.</p>',
         hid="pelda-felismeres",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> Ez pontosan a $\\sin(\\alpha+\\beta)$ képlet jobb oldala '
                  '$\\alpha=25^\\circ$, $\\beta=35^\\circ$ mellett:</p>'
                  '$$=\\sin(25^\\circ+35^\\circ)=\\sin 60^\\circ=\\boxed{\\frac{\\sqrt3}{2}}$$'
                  '<p><b>b)</b> Két koszinusz szorzata <b>plusz</b> két szinuszé → '
                  '$\\cos(\\alpha-\\beta)$:</p>'
                  '$$=\\cos(70^\\circ-25^\\circ)=\\cos 45^\\circ=\\boxed{\\frac{\\sqrt2}{2}}$$')),
   kviz('Mivel egyenlő $\\cos 50^\\circ\\cos 20^\\circ+\\sin 50^\\circ\\sin 20^\\circ$?',
        ['$\\cos 30^\\circ$', '$\\cos 70^\\circ$', '$\\sin 70^\\circ$'], 0,
        jo="✔ cos α cos β + sin α sin β = cos(α − β) = cos 30°.",
        nem="✘ A PLUSZ jel a koszinusznál KÜLÖNBSÉGET jelent: cos(50° − 20°) = cos 30°."),
 ]),

 ("A kétszeres szög", [
   'Ha az addíciós képletben $\\beta=\\alpha$, azonnal megkapjuk a kétszeres szög '
   'képleteit — nem kell külön megjegyezni őket, csak levezetni.',
   doboz("tetel", "Kétszeres szög",
         '$$\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha$$'
         '$$\\cos 2\\alpha=\\cos^{2}\\alpha-\\sin^{2}\\alpha=2\\cos^{2}\\alpha-1='
         '1-2\\sin^{2}\\alpha$$'
         '$$\\operatorname{tg}2\\alpha=\\frac{2\\operatorname{tg}\\alpha}'
         '{1-\\operatorname{tg}^{2}\\alpha}$$'
         '<p>A koszinusznak <b>három</b> alakja van — mindig azt válaszd, amelyikben '
         'szereplő függvény értékét ismered.</p>',
         hid="tetel-ketszeres",
         lenyilo=("Honnan a másik két alak?",
                  '<p>Az alapazonosságból $\\sin^{2}\\alpha=1-\\cos^{2}\\alpha$, ezt beírva</p>'
                  '$$\\cos 2\\alpha=\\cos^{2}\\alpha-(1-\\cos^{2}\\alpha)=2\\cos^{2}\\alpha-1.$$'
                  '<p>Ugyanígy $\\cos^{2}\\alpha=1-\\sin^{2}\\alpha$ helyettesítéssel jön a '
                  'harmadik alak.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>✘ $\\sin 2\\alpha=2\\sin\\alpha$ &nbsp;&nbsp; ✘ $\\cos 2\\alpha=2\\cos\\alpha$</p>'
         '<p>A „$2$” a <b>szögre</b> vonatkozik, nem a függvényértékre! Ellenőrzés: '
         '$\\sin(2\\cdot 30^\\circ)=\\sin 60^\\circ\\approx 0{,}87$, míg '
         '$2\\sin 30^\\circ=1$.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számold ki $\\sin 2\\alpha$ és $\\cos 2\\alpha$ pontos értékét, ha '
         '$\\sin\\alpha=\\tfrac45$ és $\\alpha$ hegyesszög!</p>',
         hid="pelda-ketszeres",
         lenyilo=("Megoldás",
                  '<p>Hegyesszög → $\\cos\\alpha=\\sqrt{1-\\tfrac{16}{25}}=\\tfrac35$.</p>'
                  '$$\\sin 2\\alpha=2\\cdot\\frac45\\cdot\\frac35=\\boxed{\\frac{24}{25}}$$'
                  '$$\\cos 2\\alpha=\\left(\\frac35\\right)^{2}-\\left(\\frac45\\right)^{2}'
                  '=\\frac{9-16}{25}=\\boxed{-\\frac{7}{25}}$$'
                  '<p><b>Ellenőrzés:</b> $\\left(\\tfrac{24}{25}\\right)^{2}+'
                  '\\left(\\tfrac{7}{25}\\right)^{2}=\\tfrac{576+49}{625}=1$ ✔ — a $2\\alpha$-ra '
                  'is teljesül az alapazonosság.</p>')),
   kviz('Ha $\\cos\\alpha=\\tfrac13$, mennyi $\\cos 2\\alpha$?',
        ['$-\\tfrac79$', '$\\tfrac23$', '$\\tfrac19$'], 0,
        jo="✔ cos 2α = 2cos²α − 1 = 2/9 − 1 = −7/9.",
        nem="✘ Használd a 2cos²α − 1 alakot: 2·(1/9) − 1 = −7/9."),
   gyakorolj(FGY + "#alap-7", "A 7–13", FGY + "#kozep-5", "K 5–10"),
 ]),
]

# ===================================================================== B3

B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Éjjáró:</b> Ha a kétszeres szög működik, működnie kell <b>visszafelé</b> '
         'is: a felére. És van még egy trükk, ami a terepen a leghasznosabb — két '
         'szögfüggvény <b>összegét szorzattá</b> alakítani. Miért jó ez? Mert a szorzattal '
         'lehet egyszerűsíteni, nullára hozni, egyenletet megoldani. Az összeggel nem.'),
 ]),

 ("A félszög függvényei", [
   doboz("tetel", "Félszög-képletek",
         '$$\\sin\\frac{\\alpha}{2}=\\pm\\sqrt{\\frac{1-\\cos\\alpha}{2}},\\qquad'
         '\\cos\\frac{\\alpha}{2}=\\pm\\sqrt{\\frac{1+\\cos\\alpha}{2}}$$'
         '$$\\operatorname{tg}\\frac{\\alpha}{2}=\\pm\\sqrt{\\frac{1-\\cos\\alpha}'
         '{1+\\cos\\alpha}}=\\frac{\\sin\\alpha}{1+\\cos\\alpha}$$'
         '<p>Az előjelet <b>mindig az $\\tfrac{\\alpha}{2}$ negyede</b> dönti el — nem az '
         '$\\alpha$-é!</p>'
         '<p class="halvany">A tangenses alakhoz kikötés is jár: a nevező nem lehet nulla, tehát $1+\\cos\\alpha\\neq 0$, azaz $\\alpha\\neq 180^\\circ+k\\cdot 360^\\circ$. Épp ezeknél a szögeknél lenne a felezett szög $90^\\circ$ páratlan többszöröse — ott pedig a tangens sincs értelmezve.</p>',
         hid="tetel-felszog",
         lenyilo=("Honnan jönnek?",
                  '<p>A $\\cos 2u=1-2\\sin^{2}u$ alakba írjunk $u=\\tfrac{\\alpha}{2}$-t:</p>'
                  '$$\\cos\\alpha=1-2\\sin^{2}\\frac{\\alpha}{2}\\ \\Longrightarrow\\ '
                  '\\sin^{2}\\frac{\\alpha}{2}=\\frac{1-\\cos\\alpha}{2}.$$'
                  '<p>A koszinuszos alak a $\\cos 2u=2\\cos^{2}u-1$ képletből ugyanígy jön.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Ha $\\alpha\\in\\left(\\tfrac{\\pi}{2};\\pi\\right)$ (II. negyed), akkor '
         '$\\tfrac{\\alpha}{2}\\in\\left(\\tfrac{\\pi}{4};\\tfrac{\\pi}{2}\\right)$ — '
         'vagyis az <b>első</b> negyedben, ahol minden pozitív. A felezés '
         '<b>negyedet válthat</b>, ezért az előjelet mindig a <b>felezett</b> szögre '
         'kell megállapítani.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p><b>a)</b> Számold ki $\\sin\\tfrac{\\alpha}{2}$ és $\\cos\\tfrac{\\alpha}{2}$ '
         'pontos értékét, ha $\\cos\\alpha=\\tfrac{7}{25}$ és '
         '$\\alpha\\in\\left(0;\\tfrac{\\pi}{2}\\right)$.<br>'
         '<b>b)</b> Számold ki $\\sin 22^\\circ 30\'$ pontos értékét.</p>',
         hid="pelda-felszog",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\alpha$ az I. negyedben van, tehát '
                  '$\\tfrac{\\alpha}{2}\\in\\left(0;\\tfrac{\\pi}{4}\\right)$ — szintén az '
                  'I. negyedben, minden <b>pozitív</b>.</p>'
                  '$$\\sin\\frac{\\alpha}{2}=\\sqrt{\\frac{1-\\tfrac{7}{25}}{2}}='
                  '\\sqrt{\\frac{18}{50}}=\\boxed{\\frac35},\\qquad'
                  '\\cos\\frac{\\alpha}{2}=\\sqrt{\\frac{1+\\tfrac{7}{25}}{2}}='
                  '\\sqrt{\\frac{32}{50}}=\\boxed{\\frac45}$$'
                  '<p><b>b)</b> $22^\\circ 30\'$ a $45^\\circ$ fele, és '
                  '$\\cos 45^\\circ=\\tfrac{\\sqrt2}{2}$:</p>'
                  '$$\\sin 22^\\circ30\'=\\sqrt{\\frac{1-\\tfrac{\\sqrt2}{2}}{2}}='
                  '\\boxed{\\frac{\\sqrt{2-\\sqrt2}}{2}}\\approx 0{,}38268$$')),
 ]),

 ("Összeg és különbség szorzattá alakítása", [
   doboz("tetel", "A négy képlet",
         '$$\\sin u+\\sin v=2\\sin\\frac{u+v}{2}\\cos\\frac{u-v}{2}$$'
         '$$\\sin u-\\sin v=2\\cos\\frac{u+v}{2}\\sin\\frac{u-v}{2}$$'
         '$$\\cos u+\\cos v=2\\cos\\frac{u+v}{2}\\cos\\frac{u-v}{2}$$'
         '$$\\cos u-\\cos v=-2\\sin\\frac{u+v}{2}\\sin\\frac{u-v}{2}$$'
         '<p>Mind a négyben ugyanaz a két szög szerepel: a <b>félösszeg</b> és a '
         '<b>félkülönbség</b>. Csak az kérdés, melyik függvény kerül hova — és hogy az '
         'utolsóban ott a <b>mínusz</b>.</p>',
         hid="tetel-szorzatta"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Alakítsd szorzattá, majd egyszerűsítsd! '
         '<b>a)</b> $\\sin 75^\\circ+\\sin 15^\\circ$; '
         '<b>b)</b> $\\cos 40^\\circ+\\cos 20^\\circ$; '
         '<b>c)</b> $\\cos 20^\\circ-\\cos 80^\\circ$.</p>',
         hid="pelda-szorzatta",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> Félösszeg $45^\\circ$, félkülönbség $30^\\circ$:</p>'
                  '$$2\\sin 45^\\circ\\cos 30^\\circ=2\\cdot\\frac{\\sqrt2}{2}\\cdot'
                  '\\frac{\\sqrt3}{2}=\\boxed{\\frac{\\sqrt6}{2}}\\approx 1{,}22474$$'
                  '<p><b>b)</b> Félösszeg $30^\\circ$, félkülönbség $10^\\circ$:</p>'
                  '$$2\\cos 30^\\circ\\cos 10^\\circ=\\boxed{\\sqrt3\\cos 10^\\circ}'
                  '\\approx 1{,}70574$$'
                  '<p><b>c)</b> Félösszeg $50^\\circ$, félkülönbség $-30^\\circ$:</p>'
                  '$$-2\\sin 50^\\circ\\sin(-30^\\circ)=2\\sin 50^\\circ\\cdot\\frac12='
                  '\\boxed{\\sin 50^\\circ}\\approx 0{,}76604$$'
                  '<p>(A $\\sin(-30^\\circ)=-\\sin 30^\\circ$ előjelváltás vitte el a '
                  'mínuszt — a szinusz páratlan függvény.)</p>')),
   doboz("erdekesseg", "Miért éri meg a szorzat?",
         '<p>Egy <b>szorzat</b> akkor nulla, ha valamelyik tényezője nulla — ezért a '
         'trigonometrikus egyenleteknél az első lépés szinte mindig a szorzattá alakítás. '
         'Az összeggel ilyet nem lehet kezdeni. Ugyanez az ok, amiért a másodfokú '
         'egyenletnél is szorzattá bontottunk.</p>'),
   kviz('Mivel egyenlő $\\sin 80^\\circ+\\sin 20^\\circ$?',
        ['$\\sqrt3\\sin 50^\\circ$', '$\\sin 100^\\circ$', '$2\\sin 50^\\circ$'], 0,
        jo="✔ 2 sin 50° cos 30° = 2 · sin 50° · (√3/2) = √3 sin 50°.",
        nem="✘ sin u + sin v = 2 sin((u+v)/2) cos((u−v)/2) = 2 sin 50° cos 30° = √3 sin 50°."),
   gyakorolj(FGY + "#alap-14", "A 14–18", FGY + "#kozep-11", "K 11–14"),
   brief('<b>Éjjáró:</b> Az azonosságok készen vannak — ez a <b>4. ellenőrző</b> '
         'anyagának a gerince. Innentől viszont átadom a szót Janka-nek: ő nem egyetlen '
         'szöggel dolgozik, hanem a <b>teljes hullámmal</b>. Meglátod, hogy néz ki a '
         'szinusz, ha nem egy pontban nézed, hanem végig.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-alapazonossagok.html",
     cim="Alapazonosságok", cim_tiszta="Alapazonosságok",
     alcim="A négyzetes alapazonosság, a tangens és a kotangens kapcsolata, "
           "valamint a témakör leggyakoribb feladattípusa: egy érték és a negyed.",
     chip="A Fázisugrás · 4/11", szakaszok=B1,
     elozo=("feladatok-trigonometrikus-kor.html", "Feladatok — a trigonometrikus kör"),
     kovetkezo=("tananyag-addicios-kepletek.html", "Addíciós képletek és a kétszeres szög")),
 lap(**T, fajl="tananyag-addicios-kepletek.html",
     cim="Addíciós képletek és a kétszeres szög",
     cim_tiszta="Addíciós képletek és a kétszeres szög",
     alcim="Két szög összegének és különbségének szögfüggvényei, a képletek felismerése "
           "visszafelé, és a kétszeres szög három koszinusz-alakja.",
     chip="A Fázisugrás · 5/11", szakaszok=B2,
     elozo=("tananyag-alapazonossagok.html", "Alapazonosságok"),
     kovetkezo=("tananyag-felszog-es-szorzatta-alakitas.html",
                "Félszög és szorzattá alakítás")),
 lap(**T, fajl="tananyag-felszog-es-szorzatta-alakitas.html",
     cim="Félszög és szorzattá alakítás", cim_tiszta="Félszög és szorzattá alakítás",
     alcim="A félszög függvényei és az előjel kérdése, valamint az összeg és a "
           "különbség szorzattá alakításának négy képlete.",
     chip="A Fázisugrás · 6/11", szakaszok=B3,
     elozo=("tananyag-addicios-kepletek.html", "Addíciós képletek és a kétszeres szög"),
     kovetkezo=(FGY, "Feladatok — azonosságok")),
]
for u in KI:
    print("✓", os.path.basename(u))
