# -*- coding: utf-8 -*-
"""2e/04 — osszefoglalo (F4), terepkuldetes (F5p), Vészterem (F6h), temakor-index (F5)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, GYOKER
from fgy_common import cards, oldal, w

T = dict(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
         temakor="Trigonometrikus függvények")

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (Rational as R, pi, sqrt, sin, cos, tan, cot, asin, acos, rad, deg,
                   simplify, nsimplify, N)
E = []
def chk(n, g, w_, tol=None):
    ok = abs(float(g) - w_) < tol if tol is not None else simplify(g - w_) == 0
    if not ok:
        E.append((n, g, w_))
# --- terepküldetés I (grafikonok)
chk("TI1-A", R(6 - (-2), 2), 4); chk("TI1-d", R(6 + (-2), 2), 2)
chk("TI1-b", 2*pi/(4*pi), R(1, 2))
chk("TI2-p", 2*pi/2, pi); chk("TI2-f", R(1, 2)*pi/2, pi/4)
chk("TI3", pi/2 - pi/3, pi/6)
chk("TI4-p", 2*pi/(120*pi), R(1, 60)); chk("TI4-f", 60, 60)
# --- terepküldetés II
chk("TII1a", [simplify(f(rad(225))) for f in (sin, cos, tan, cot)],
    [-sqrt(2)/2, -sqrt(2)/2, 1, 1]) if False else None
for nev, A, w_ in [("TII1a", 225, [-sqrt(2)/2, -sqrt(2)/2, 1, 1]),
                   ("TII1b", 150, [R(1, 2), -sqrt(3)/2, -sqrt(3)/3, -sqrt(3)])]:
    got = [simplify(f(rad(A))) for f in (sin, cos, tan, cot)]
    if got != w_:
        E.append((nev, got, w_))
chk("TII2", R(-9, 41)**2 + R(40, 41)**2, 1)
chk("TII3a", cos(rad(15)), (sqrt(6) + sqrt(2))/4)
chk("TII3b", 2*R(3, 5)*R(4, 5), R(24, 25))
chk("TII3c", R(4, 5)**2 - R(3, 5)**2, R(7, 25))
chk("TII4", sin(2*(pi/6)), sqrt(3)/2)
chk("TII4b", sin(2*(pi/3)), sqrt(3)/2)
# --- terepküldetés III
chk("TIII1-b", 180 - 38 - 61, 81)
chk("TIII1-b2", 24*sin(rad(81))/sin(rad(38)), 38.50252, 1e-4)
chk("TIII1-c", 24*sin(rad(61))/sin(rad(38)), 34.09483, 1e-4)
aa = sqrt(17**2 + 23**2 - 2*17*23*cos(rad(64)))
chk("TIII2", aa, 21.79894, 1e-4)
chk("TIII2b", deg(asin(17*sin(rad(64))/aa)), 44.502, 6e-3)
chk("TIII3", R(1, 2)*17*23*sin(rad(64)), 175.7142, 1e-3)
BT = 80*sin(rad(25))/sin(rad(16))
chk("TIII4-BT", BT, 122.6592, 1e-3); chk("TIII4-h", BT*sin(rad(41)), 80.47168, 1e-3)
# --- Vészterem
chk("DA1", nsimplify(rad(135))/pi, R(3, 4))
chk("DA2", deg(R(11, 6)*pi), 330)
chk("DA3", sin(rad(240)), -sqrt(3)/2)
chk("DA4", cos(rad(315)), sqrt(2)/2)
chk("DA5", R(3, 5)**2 + R(4, 5)**2, 1)
chk("DA6", sin(rad(15)), (sqrt(6) - sqrt(2))/4)
chk("DA7", 2*R(12, 13)*R(5, 13), R(120, 169))
chk("DA8", sin(rad(75)) + sin(rad(15)) - sqrt(6)/2, 0, 1e-25)
chk("DA9", 2*pi/4, pi/2)
chk("DA10", sin(pi/6), R(1, 2))
chk("DA11", R(1, 2)*9*12*sin(rad(30)), 27)
chk("DA12", sqrt(6**2 + 8**2 - 2*6*8*cos(rad(60))), 7.2111026, 1e-6)
chk("DK1", R(-15, 17)**2 + R(8, 17)**2, 1)
chk("DK2", cos(rad(105)), (sqrt(2) - sqrt(6))/4)
chk("DK3", R(7, 25)**2 - R(24, 25)**2, R(-527, 625))
chk("DK4", sqrt((1 + R(-3, 5))/2), 0.4472136, 1e-6)
chk("DK5", sin(2*(5*pi/12)), R(1, 2))
chk("DK6", 20*sin(rad(75))/sin(rad(45)), 27.32051, 1e-5)
chk("DK7", deg(acos(R(7**2 + 9**2 - 12**2, 2*7*9))), 96.3794, 1e-3)
chk("DK8", R(1, 2)*11*14*sin(rad(115)), 69.7857, 1e-3)
chk("DN1", cos(rad(20))*cos(rad(40))*cos(rad(80)) - R(1, 8), 0, 1e-20)
chk("DN2", sin(pi/4) - cos(pi/4), 0)
chk("DN3", sqrt(2), 1.414214, 1e-5)
chk("DN4", sqrt(21*8*7*6), 84, 1e-6)
assert not E, E
print("sympy önteszt: OK")

# ==================================================================== F4

OSSZ = [
 ("Szögmérés és a trigonometrikus kör", [
  '<p><b>Forgásszög:</b> pozitív irány az óramutatóval <b>ellentétes</b>. Az '
  '$\\alpha$ és az $\\alpha+k\\cdot 360^\\circ$ ugyanaz az irány, tehát minden '
  'szögfüggvényük megegyezik '
  '(<a href="tananyag-szogmeres-es-radian.html#tetel-tarsszogek">→</a>).</p>',
  '<p><b>Radián:</b> $180^\\circ=\\pi$. Fokból radiánba: $\\cdot\\tfrac{\\pi}{180}$; '
  'radiánból fokba: a $\\pi$ helyére $180^\\circ$ '
  '(<a href="tananyag-szogmeres-es-radian.html#tetel-atvaltas">→</a>).</p>'
  '<div class="tblwrap"><table>'
  '<tr><th>fok</th><td>$30^\\circ$</td><td>$45^\\circ$</td><td>$60^\\circ$</td>'
  '<td>$90^\\circ$</td><td>$180^\\circ$</td><td>$270^\\circ$</td><td>$360^\\circ$</td></tr>'
  '<tr><th>rad</th><td>$\\tfrac{\\pi}{6}$</td><td>$\\tfrac{\\pi}{4}$</td>'
  '<td>$\\tfrac{\\pi}{3}$</td><td>$\\tfrac{\\pi}{2}$</td><td>$\\pi$</td>'
  '<td>$\\tfrac{3\\pi}{2}$</td><td>$2\\pi$</td></tr></table></div>',
  '<p><b>Definíció az egységkörön:</b> $P(\\cos\\alpha;\\sin\\alpha)$ — előbb a '
  'koszinusz! $\\operatorname{tg}\\alpha=\\tfrac{\\sin\\alpha}{\\cos\\alpha}$, '
  '$\\operatorname{ctg}\\alpha=\\tfrac{\\cos\\alpha}{\\sin\\alpha}$ '
  '(<a href="tananyag-trigonometrikus-kor.html#def-trigonometrikus-kor">→</a>). '
  'Ebből azonnal: $-1\\le\\sin\\alpha\\le 1$ és $-1\\le\\cos\\alpha\\le 1$.</p>',
  '<p><b>Előjelek:</b> I. mind + · II. csak $\\sin$ · III. csak $\\operatorname{tg}$ és '
  '$\\operatorname{ctg}$ · IV. csak $\\cos$ '
  '(<a href="tananyag-trigonometrikus-kor.html#tetel-elojelek">→</a>).</p>',
  '<p><b>Jellegzetes szögek:</b> a $\\sin$ sora '
  '$0,\\ \\tfrac12,\\ \\tfrac{\\sqrt2}{2},\\ \\tfrac{\\sqrt3}{2},\\ 1$; a $\\cos$ '
  'ugyanez visszafelé '
  '(<a href="tananyag-trigonometrikus-kor.html#tetel-jellegzetes">→</a>).</p>',
  '<p><b>Visszavezetés:</b> ① teljes fordulatok le · ② alapszög az I. negyedben · '
  '③ előjel a negyed szerint. $\\sin(-\\alpha)=-\\sin\\alpha$ (páratlan), '
  '$\\cos(-\\alpha)=\\cos\\alpha$ (páros) '
  '(<a href="tananyag-visszavezetes.html#tetel-visszavezetes">→</a>).</p>',
 ]),
 ("Azonosságok", [
  '<p><b>Alapazonosságok:</b></p>'
  '$$\\sin^{2}\\alpha+\\cos^{2}\\alpha=1,\\qquad'
  '\\operatorname{tg}\\alpha\\cdot\\operatorname{ctg}\\alpha=1,\\qquad'
  '1+\\operatorname{tg}^{2}\\alpha=\\frac{1}{\\cos^{2}\\alpha}$$'
  '<p>⚠️ A gyökvonásnál az előjelet <b>a negyed</b> dönti el '
  '(<a href="tananyag-alapazonossagok.html#tetel-alapazonossagok">→</a>).</p>',
  '<p><b>Addíciós képletek:</b></p>'
  '$$\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta$$'
  '$$\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta$$'
  '<p>A koszinusznál a jel <b>megfordul</b> '
  '(<a href="tananyag-addicios-kepletek.html#tetel-addicios">→</a>).</p>',
  '<p><b>Kétszeres szög:</b></p>'
  '$$\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha,\\qquad'
  '\\cos 2\\alpha=\\cos^{2}\\alpha-\\sin^{2}\\alpha=2\\cos^{2}\\alpha-1='
  '1-2\\sin^{2}\\alpha$$'
  '<p>(<a href="tananyag-addicios-kepletek.html#tetel-ketszeres">→</a>)</p>',
  '<p><b>Félszög:</b> $\\sin\\tfrac{\\alpha}{2}=\\pm\\sqrt{\\tfrac{1-\\cos\\alpha}{2}}$, '
  '$\\cos\\tfrac{\\alpha}{2}=\\pm\\sqrt{\\tfrac{1+\\cos\\alpha}{2}}$ — az előjelet '
  'a <b>felezett</b> szög negyede adja '
  '(<a href="tananyag-felszog-es-szorzatta-alakitas.html#tetel-felszog">→</a>).</p>',
  '<p><b>Szorzattá alakítás:</b></p>'
  '$$\\sin u\\pm\\sin v=2\\begin{Bmatrix}\\sin\\\\ \\cos\\end{Bmatrix}'
  '\\frac{u+v}{2}\\begin{Bmatrix}\\cos\\\\ \\sin\\end{Bmatrix}\\frac{u-v}{2}$$'
  '$$\\cos u+\\cos v=2\\cos\\frac{u+v}{2}\\cos\\frac{u-v}{2},\\qquad'
  '\\cos u-\\cos v=-2\\sin\\frac{u+v}{2}\\sin\\frac{u-v}{2}$$'
  '<p>(<a href="tananyag-felszog-es-szorzatta-alakitas.html#tetel-szorzatta">→</a>)</p>',
 ]),
 ("Függvények és egyenletek", [
  '<div class="tblwrap"><table>'
  '<tr><th></th><th>$\\sin x$</th><th>$\\cos x$</th><th>$\\operatorname{tg}x$</th></tr>'
  '<tr><td>ÉT</td><td colspan="2">$\\mathbb{R}$</td>'
  '<td>$x\\neq\\tfrac{\\pi}{2}+k\\pi$</td></tr>'
  '<tr><td>ÉK</td><td colspan="2">$[-1;1]$</td><td>$\\mathbb{R}$</td></tr>'
  '<tr><td>Periódus</td><td colspan="2">$2\\pi$</td><td><b>$\\pi$</b></td></tr>'
  '<tr><td>Nullahely</td><td>$k\\pi$</td><td>$\\tfrac{\\pi}{2}+k\\pi$</td>'
  '<td>$k\\pi$</td></tr>'
  '<tr><td>Szimmetria</td><td>páratlan</td><td>páros</td><td>páratlan</td></tr>'
  '</table></div>'
  '<p>(<a href="tananyag-trig-fuggvenyek-grafikonja.html#tetel-sincos">→</a>)</p>',
  '<p><b>$y=A\\sin(bx+c)+d$:</b> amplitúdó $|A|$ · periódus $\\tfrac{2\\pi}{|b|}$ · '
  'vízszintes eltolás <b>$-\\tfrac{c}{b}$</b> (a $b$-t ki kell emelni!) · középvonal $d$, '
  'értékkészlet $[d-|A|;\\,d+|A|]$ '
  '(<a href="tananyag-osszetett-trig-fuggvenyek.html#tetel-teljes-alak">→</a>).</p>',
  '<p><b>Egyenletek:</b> $\\sin x=a$ és $\\cos x=a$ csak $|a|\\le 1$ esetén oldható meg, '
  'és <b>két</b> megoldáscsaládot ad ($+2k\\pi$); a $\\operatorname{tg}x=a$ bármely '
  '$a$-ra megoldható, és <b>egy</b> családot ad ($+k\\pi$) '
  '(<a href="tananyag-trigonometrikus-egyenletek.html#tetel-alaptipusok">→</a>).</p>',
  '<p><b>$bx$ alakú szög:</b> oldd meg a $bx$-re, és <b>a legvégén</b> ossz $b$-vel — '
  'a $2k\\pi$-t is! Így a periódus $\\tfrac{2\\pi}{b}$ lesz '
  '(<a href="tananyag-trigonometrikus-egyenletek.html#tetel-bx">→</a>).</p>',
 ]),
 ("Háromszögek", [
  '<p><b>Szinusztétel:</b> $\\dfrac{a}{\\sin\\alpha}=\\dfrac{b}{\\sin\\beta}='
  '\\dfrac{c}{\\sin\\gamma}=2R$ — akkor, ha van teljes <b>oldal–szög pár</b> '
  '(<a href="tananyag-szinusz-es-koszinusztetel.html#tetel-szinusztetel">→</a>).</p>',
  '<p><b>Koszinusztétel:</b> $a^{2}=b^{2}+c^{2}-2bc\\cos\\alpha$, illetve '
  '$\\cos\\alpha=\\dfrac{b^{2}+c^{2}-a^{2}}{2bc}$ — SAS és SSS esetén '
  '(<a href="tananyag-szinusz-es-koszinusztetel.html#tetel-koszinusztetel">→</a>).</p>',
  '<p><b>Terület:</b> $T=\\tfrac12 ab\\sin\\gamma$ — a szög a két oldal <b>között</b> '
  '(<a href="tananyag-haromszog-megoldasa.html#tetel-terulet">→</a>).</p>',
  '<div class="tblwrap"><table>'
  '<tr><th>Adat</th><th>Első lépés</th></tr>'
  '<tr><td>ASA / AAS</td><td>harmadik szög, majd szinusztétel</td></tr>'
  '<tr><td>SAS</td><td>koszinusztétel, majd a <b>kisebbik</b> oldal szöge</td></tr>'
  '<tr><td>SSS</td><td>koszinusztétel a <b>legnagyobb</b> oldal szögére</td></tr>'
  '<tr><td>SSA</td><td>szinusztétel — ⚠️ lehet <b>két</b> megoldás</td></tr>'
  '</table></div>'
  '<p>(<a href="tananyag-haromszog-megoldasa.html#tetel-recept">→</a>)</p>',
  doboz("csapda", "Amire a dolgozaton a legtöbben ráfutnak",
        '<p>1) A negyed <b>előbb</b>, az érték utána — írd ki az előjelet, mielőtt '
        'számolsz. &nbsp; 2) $\\sin(\\alpha+\\beta)\\neq\\sin\\alpha+\\sin\\beta$ és '
        '$\\cos 2\\alpha\\neq 2\\cos\\alpha$. &nbsp; 3) A koszinuszos addíciós képletben '
        'a jel <b>megfordul</b>. &nbsp; 4) A félszögnél a <b>felezett</b> szög negyede '
        'számít. &nbsp; 5) Az egyenletnél ne felejtsd a $+2k\\pi$-t és a <b>második</b> '
        'megoldáscsaládot. &nbsp; 6) A $\\operatorname{tg}$ periódusa $\\pi$. &nbsp; '
        '7) A számológép <b>DEG</b> módban legyen. &nbsp; 8) Kerekítés: '
        'szögfüggvényérték <b>öt</b>, oldalhossz <b>két</b> tizedes.</p>'),
  '<div class="gyakorolj"><span class="ikon">🎯</span><p>Élesben: nézd át a négy '
  '<a href="feladatok-haromszogek.html">feladatgyűjteményt</a>, majd indulj '
  '<a href="terepkuldetes.html">A Fantom-frekvencia terepküldetésre</a>!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Taktikai memóriakártya",
    cim_tiszta="Taktikai memóriakártya", itt="Taktikai memóriakártya",
    alcim="A Fázisugrás minden képlete, protokollja és tipikus csapdája egy helyen — "
          "ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip="A Fázisugrás · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-haromszogek.html", "Feladatok — háromszögek"),
    kovetkezo=("terepkuldetes.html", "A Fantom-frekvencia terepküldetés"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> Ismeretlen jel érkezik a Baljós-bázisról, és nem tudjuk '
         'megfejteni. A műszer csak a <b>grafikont</b> rajzolja ki — nekünk kell '
         'kiolvasnunk belőle a képletet. Utána Kurt bemér néhány szöget a körön, '
         'végül pedig háromszögeléssel megkeressük magát a bázist. Három fázis, '
         'három eszköz: <b>grafikon</b>, <b>azonosság</b>, <b>háromszög</b>.'),
   '<p class="lead">Ez a küldetés a teljes témakört használja: grafikonolvasást és '
   'modellalkotást, a trigonometrikus kört, az azonosságokat, egyenletmegoldást, '
   'valamint a szinusz- és koszinusztételt. Dolgozz füzetben, és a végén add le a '
   'jelentést. <b>A megoldások nincsenek fent</b> — ezt a bevetést a tanárod értékeli.</p>',
 ]),
 ("Fázis I — A jel megfejtése", [
   doboz("pelda", "I. fázis: grafikonból képletet",
         '<ol class="reszfeladatok">'
         '<li>Az elfogott jel legnagyobb értéke $6$, a legkisebb $-2$, a periódusa '
         '$4\\pi$. Írd fel a jelet $y=A\\sin(bx)+d$ alakban! (Add meg $A$-t, $b$-t és '
         '$d$-t is külön.)</li>'
         '<li>Egy másik csatornán ezt fogtuk: $y=3\\sin\\left(2x-\\tfrac{\\pi}{2}\\right)$. '
         'Add meg az <b>amplitúdóját</b>, a <b>periódusát</b>, a <b>fáziseltolását</b> '
         '(irány és mérték!) és az <b>értékkészletét</b>.</li>'
         '<li>Ábrázold közös koordináta-rendszerben a $[0;2\\pi]$ intervallumon az '
         '$y=\\sin x$ és az $y=2\\sin\\left(x+\\tfrac{\\pi}{3}\\right)$ függvényt! '
         'Hol veszi fel a második a maximumát?</li>'
         '<li>A bázis áramellátása $y=0{,}5\\sin(120\\pi t)$ alakú (a $t$ '
         'másodpercben). Mekkora a rezgés <b>periódusa</b> és <b>frekvenciája</b>?</li>'
         '</ol>'),
 ]),
 ("Fázis II — A körön", [
   doboz("pelda", "II. fázis: szögek és azonosságok",
         '<ol class="reszfeladatok">'
         '<li>Add meg mind a négy szögfüggvény pontos értékét! '
         '<b>a)</b> $225^\\circ$ &nbsp; <b>b)</b> $\\tfrac{5\\pi}{6}$</li>'
         '<li>A jel fáziskódja egy $\\alpha$ szög, amelyre $\\cos\\alpha=-\\tfrac{9}{41}$ '
         'és $\\sin\\alpha&gt;0$. Számold ki a másik három szögfüggvény pontos értékét!</li>'
         '<li><b>a)</b> Számold ki addíciós képlettel $\\cos 15^\\circ$ pontos értékét. '
         '<b>b)</b> Ha $\\sin\\beta=\\tfrac35$ és $\\beta$ hegyesszög, mennyi '
         '$\\sin 2\\beta$ és $\\cos 2\\beta$?</li>'
         '<li>A zárókód a $2\\sin 2x=\\sqrt3$ egyenlet megoldása. Add meg az '
         '<b>összes</b> megoldást!</li>'
         '</ol>'),
 ]),
 ("Fázis III — A bemérés", [
   doboz("pelda", "III. fázis: háromszögelés",
         '<p>Minden számításnál a szögfüggvények értékeit <b>öt</b>, a hosszakat '
         '<b>két</b> tizedesre kerekítsd!</p>'
         '<ol class="reszfeladatok">'
         '<li>Két megfigyelőpont és a bázis háromszöget alkot: $\\alpha=38^\\circ$, '
         '$\\gamma=61^\\circ$, és a szemközti oldal $a=24$ km. Oldd meg a háromszöget!</li>'
         '<li>Egy másik felderítés adatai: $b=17$ km, $c=23$ km, a közbezárt szög '
         '$\\alpha=64^\\circ$. Mekkora az $a$ oldal?</li>'
         '<li>Mekkora a 2. feladatbeli háromszög <b>területe</b>?</li>'
         '<li>A bázison álló antennatorony tövéhez nem lehet közel menni. Az $A$ '
         'pontból a csúcsát $25^\\circ$-os, $80$ méterrel közelebbről, a $B$ pontból '
         '$41^\\circ$-os emelkedési szögben látjuk. Milyen magas a torony?</li>'
         '</ol>'),
   '<div class="gyakorolj"><span class="ikon">📋</span><p><b>Jelentés:</b> az I. '
   'fázisnál legyen ott a <b>grafikon</b> és a leolvasott paraméterek, a II.-nál a '
   'használt <b>azonosság neve</b>, a III.-nál pedig az, hogy <b>melyik tételt</b> '
   'miért választottad. A kerekítési szabály betartása is pont.</p></div>',
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="A Fantom-frekvencia",
    cim_tiszta="A Fantom-frekvencia", itt="A Fantom-frekvencia terepküldetés",
    alcim="Háromfázisú felderítés — ismeretlen jel megfejtése grafikonból, "
          "fáziskód a trigonometrikus körön, végül a bázis bemérése háromszögeléssel.",
    chip="A Fázisugrás · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Taktikai memóriakártya"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h


# ==================================================================
# STK2 / reprezentáció-váltó pótlás a Vészteremhez (2026-08 audit)
# ==================================================================
# --- 2e/04 Trigonometrikus függvények ---
DR_A_UJ_04 = [
 ("Döntsd el, igaz vagy hamis, és <b>ha hamis, adj ellenpéldát</b>!",
  ["$\\sin x$ értéke bármely valós $x$-re $-1$ és $1$ közé esik.",
   "$\\sin(x+y)=\\sin x+\\sin y$ minden $x$-re és $y$-ra.",
   "A $\\operatorname{tg}$ függvény minden valós számra értelmezett.",
   "$\\cos(-x)=\\cos x$ minden valós $x$-re."],
  ["Igaz — ez a szinusz értékkészlete.",
   "Hamis: $x=y=90^\\circ$ esetén a bal oldal $\\sin 180^\\circ=0$, a jobb oldal $2$.",
   "Hamis: ahol $\\cos x=0$ (például $x=90^\\circ$), ott nincs értelmezve.",
   "Igaz: a koszinusz páros függvény, grafikonja szimmetrikus az $y$ tengelyre."]),
]
DR_K_UJ_04 = [
 ("Egy szinuszos rezgést leíró függvény grafikonjáról ennyi olvasható le: a legnagyobb "
  "érték $3$, a legkisebb $-3$, és a görbe $4$ egységenként ismétlődik.",
  ["Mekkora az amplitúdó és a periódus?",
   "Írd fel a függvényt $y=A\\sin(Bx)$ alakban!",
   "Hogyan változna a képlet, ha a legnagyobb érték $5$, a legkisebb pedig $-1$ lenne?"],
  ["Az amplitúdó $3$, a periódus $4$.",
   "A periódus $\\dfrac{2\\pi}{B}=4$, ezért $B=\\dfrac{\\pi}{2}$, tehát "
   "$y=3\\sin\\!\\left(\\dfrac{\\pi}{2}x\\right)$.",
   "A két szélsőérték közepe $2$, a fél távolságuk $3$, tehát a görbe $2$-vel feljebb "
   "tolódik: $y=3\\sin\\!\\left(\\dfrac{\\pi}{2}x\\right)+2$."]),
]

DR_A = [
 ("Váltsd át!", ["$135^\\circ$ radiánba", "$\\tfrac{11\\pi}{6}$ fokba"],
  ["$\\dfrac{3\\pi}{4}$", "$330^\\circ$"], True),
 ("Melyik $[0^\\circ;360^\\circ)$ szöggel egyezik meg?",
  ["$405^\\circ$", "$-120^\\circ$"], ["$45^\\circ$", "$240^\\circ$"], True),
 ("Add meg mind a négy szögfüggvény pontos értékét! $240^\\circ$", None,
  "$\\sin=-\\tfrac{\\sqrt3}{2}$, $\\cos=-\\tfrac12$, $\\operatorname{tg}=\\sqrt3$, "
  "$\\operatorname{ctg}=\\tfrac{\\sqrt3}{3}$"),
 ("Számold ki pontosan!",
  ["$\\cos 315^\\circ$", "$\\sin 150^\\circ$", "$\\operatorname{tg}210^\\circ$"],
  ["$\\dfrac{\\sqrt2}{2}$", "$\\dfrac12$", "$\\dfrac{\\sqrt3}{3}$"], True),
 ("Számold ki a másik három szögfüggvényt! $\\sin\\alpha=\\tfrac35$, $\\alpha$ hegyesszög.",
  None, "$\\cos\\alpha=\\tfrac45$, $\\operatorname{tg}\\alpha=\\tfrac34$, "
        "$\\operatorname{ctg}\\alpha=\\tfrac43$"),
 ("Számold ki addíciós képlettel! $\\sin 15^\\circ$", None,
  "$\\sin(45^\\circ-30^\\circ)=\\dfrac{\\sqrt6-\\sqrt2}{4}\\approx 0{,}25882$"),
 ("Számold ki $\\sin 2\\alpha$ értékét, ha $\\cos\\alpha=\\tfrac{12}{13}$ és "
  "$\\alpha$ hegyesszög!", None,
  "$\\sin\\alpha=\\tfrac{5}{13}$, tehát $\\sin 2\\alpha=\\tfrac{120}{169}$"),
 ("Alakítsd szorzattá, majd egyszerűsítsd! $\\sin 75^\\circ+\\sin 15^\\circ$", None,
  "$2\\sin 45^\\circ\\cos 30^\\circ=\\dfrac{\\sqrt6}{2}\\approx 1{,}22474$"),
 ("Add meg a periódust és az amplitúdót! $y=3\\cos 4x$", None,
  "Amplitúdó $3$; periódus $\\dfrac{2\\pi}{4}=\\dfrac{\\pi}{2}$."),
 ("Oldd meg! $2\\sin x-1=0$", None,
  "$x=\\tfrac{\\pi}{6}+2k\\pi$ vagy $x=\\tfrac{5\\pi}{6}+2k\\pi$, $k\\in\\mathbb{Z}$"),
 ("Mekkora a háromszög területe? $a=9$, $b=12$, $\\gamma=30^\\circ$", None,
  "$T=\\tfrac12\\cdot 9\\cdot 12\\cdot 0{,}5=27$"),
 ("Számítsd ki a harmadik oldalt! $b=6$, $c=8$, $\\alpha=60^\\circ$", None,
  "$a^{2}=36+64-2\\cdot 6\\cdot 8\\cdot 0{,}5=52$, tehát $a=\\sqrt{52}\\approx 7{,}21$."),
]

DR_A = DR_A + DR_A_UJ_04
DR_K = [
 ("Számold ki a másik három szögfüggvényt! $\\cos\\alpha=-\\tfrac{15}{17}$ és "
  "$\\operatorname{tg}\\alpha&lt;0$.", None,
  "A koszinusz negatív, a tangens negatív → II. negyed: $\\sin\\alpha=\\tfrac{8}{17}$, "
  "$\\operatorname{tg}\\alpha=-\\tfrac{8}{15}$, $\\operatorname{ctg}\\alpha=-\\tfrac{15}{8}$."),
 ("Számold ki addíciós képlettel! $\\cos 105^\\circ$", None,
  "$\\cos(60^\\circ+45^\\circ)=\\dfrac{\\sqrt2-\\sqrt6}{4}\\approx -0{,}25882$"),
 ("Számold ki $\\sin 2\\alpha$ és $\\cos 2\\alpha$ értékét, ha "
  "$\\sin\\alpha=\\tfrac{24}{25}$ és $\\alpha$ hegyesszög!", None,
  "$\\cos\\alpha=\\tfrac{7}{25}$; $\\sin 2\\alpha=\\tfrac{336}{625}$, "
  "$\\cos 2\\alpha=-\\tfrac{527}{625}$."),
 ("Számold ki $\\cos\\tfrac{\\alpha}{2}$ pontos értékét, ha $\\cos\\alpha=-\\tfrac35$ "
  "és $\\alpha\\in\\left(\\tfrac{\\pi}{2};\\pi\\right)$!", None,
  "$\\tfrac{\\alpha}{2}$ az I. negyedben van, tehát pozitív: "
  "$\\cos\\tfrac{\\alpha}{2}=\\sqrt{\\tfrac{1-\\tfrac35}{2}}=\\sqrt{\\tfrac15}="
  "\\tfrac{\\sqrt5}{5}\\approx 0{,}44721$."),
 ("Oldd meg! $2\\sin 2x-1=0$", None,
  "$2x=\\tfrac{\\pi}{6}+2k\\pi$ vagy $2x=\\tfrac{5\\pi}{6}+2k\\pi$, tehát "
  "$x=\\tfrac{\\pi}{12}+k\\pi$ vagy $x=\\tfrac{5\\pi}{12}+k\\pi$."),
 ("Oldd meg a háromszöget! $\\alpha=45^\\circ$, $\\beta=75^\\circ$, $a=20$. "
  "(Szögfüggvény öt, oldal két tizedes.)", None,
  "$\\gamma=60^\\circ$; $b=\\dfrac{20\\sin 75^\\circ}{\\sin 45^\\circ}\\approx 27{,}32$; "
  "$c=\\dfrac{20\\sin 60^\\circ}{\\sin 45^\\circ}\\approx 24{,}49$."),
 ("Egy háromszög oldalai $7$, $9$ és $12$. Hegyes-, derék- vagy tompaszögű?", None,
  "A legnagyobb oldallal szemközti szög: "
  "$\\cos\\gamma=\\dfrac{49+81-144}{2\\cdot 7\\cdot 9}=-\\dfrac{14}{126}\\approx -0{,}11111$, "
  "tehát $\\gamma\\approx 96{,}38^\\circ$ — <b>tompaszögű</b>."),
 ("Mekkora annak a háromszögnek a területe, amelyben $a=11$, $b=14$ és a közbezárt "
  "szög $115^\\circ$?", None,
  "$T=\\tfrac12\\cdot 11\\cdot 14\\cdot\\sin 115^\\circ\\approx 69{,}79$."),
]

DR_K = DR_K + DR_K_UJ_04
DR_N = [
 ("Igazold! $\\dfrac{1-\\cos 2\\alpha}{\\sin 2\\alpha}=\\operatorname{tg}\\alpha$", None,
  "$1-\\cos 2\\alpha=2\\sin^{2}\\alpha$ és $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha$, "
  "a hányados $\\operatorname{tg}\\alpha$ ✔"),
 ("Oldd meg! $\\sin x=\\cos x$", None,
  "$\\operatorname{tg}x=1$, tehát $x=\\tfrac{\\pi}{4}+k\\pi$."),
 ("Add meg az $y=\\sin x+\\cos x$ függvény legnagyobb és legkisebb értékét!", None,
  "$\\sqrt2\\sin\\left(x+\\tfrac{\\pi}{4}\\right)$ alakban: a maximum $\\sqrt2\\approx "
  "1{,}41421$, a minimum $-\\sqrt2$."),
 ("Egy háromszög oldalai $13$, $14$, $15$. Mekkora a területe és a legnagyobb "
  "magassága?", None,
  "$T=84$ (Héron-képlettel vagy koszinusztétel + területképlet). A legnagyobb magasság "
  "a <b>legrövidebb</b> oldalhoz tartozik: $m=\\dfrac{2T}{13}=\\dfrac{168}{13}"
  "\\approx 12{,}92$."),
]

dr_brief = ('<div class="brief"><p>🕹️ <b>SZVETI:</b> <b>Vészterem</b> — A Fázisugrás '
            'modul. A szimuláció a <b>teljes témakört</b> lefedi: szögátváltás, '
            'trigonometrikus kör, visszavezetés, alapazonosságok, addíciós és kétszeres '
            'szög, szorzattá alakítás, grafikonok, egyenletek, valamint a szinusz- és '
            'koszinusztétel. Haladj a fokozatokon: zöld → sárga → piros. A végeredményt '
            'lenyithatod, de előbb küzdd le magad!</p></div>')

dr_body = ('    ' + dr_brief + '\n'
           '    <h2 id="alap">🟢 Alapfokozat</h2>\n' + cards(DR_A, "alap", "alap") +
           '\n    <h2 id="kozep">🟡 Középfokozat</h2>\n' + cards(DR_K, "kozep", "kozep") +
           '\n    <h2 id="nehez">🔴 Nehéz fokozat</h2>\n' + cards(DR_N, "nehez", "nehez"))

oldal(**T, fajl="feladatok-hazi.html", cim="Vészterem",
      h1="🕹️ Vészterem — házi feladatgyűjtemény", itt="Vészterem — házi",
      alcim="Egyetlen, a teljes témakört lefedő házi feladatsor, óraszám-arányosan. "
            "Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      sections_html=dr_body,
      prev="index.html", prevc="Témakör Főhadiszállása",
      nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5 index


def kartya(href, cim, le):
    # a kártyacím is átmegy a matek-konverzión (pl. „Az $i$ hatványai")
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = [
 kartya("tananyag-szogmeres-es-radian.html", "Szögmérés és a szög általánosítása",
        "Forgásszög, azonos állású szögek, a radián fogalma és a fok–radián átváltás"),
 kartya("tananyag-trigonometrikus-kor.html", "A trigonometrikus kör",
        "A négy függvény definíciója az egységkörön, előjelek, jellegzetes szögek"),
 kartya("tananyag-visszavezetes.html", "Visszavezetés az első negyedre",
        "Alapszög, a négy negyed és az előjelek — bármely szög két lépésben"),
 kartya("tananyag-alapazonossagok.html", "Alapazonosságok",
        "A trigonometriai Pitagorasz-tétel és a leggyakoribb feladattípus: érték + negyed"),
 kartya("tananyag-addicios-kepletek.html", "Addíciós képletek és a kétszeres szög",
        "Két szög összege és különbsége, a képletek felismerése, $\\cos 2\\alpha$ három alakja"),
 kartya("tananyag-felszog-es-szorzatta-alakitas.html", "Félszög és szorzattá alakítás",
        "A félszög függvényei és az összeg–különbség szorzattá alakításának négy képlete"),
 kartya("tananyag-trig-fuggvenyek-grafikonja.html", "A trigonometrikus függvények grafikonja",
        "A négy görbe, a periodicitás, az értékkészlet és a szimmetriák"),
 kartya("tananyag-osszetett-trig-fuggvenyek.html", "Amplitúdó, periódus és fáziseltolás",
        "Az $y=A\\sin(bx+c)+d$ alak négy paramétere és leolvasásuk a grafikonról"),
 kartya("tananyag-trigonometrikus-egyenletek.html", "Egyszerű trigonometrikus egyenletek",
        "A három alaptípus, a végtelen sok megoldás és a $bx$ alakú szögek"),
 kartya("tananyag-szinusz-es-koszinusztetel.html", "Szinusz- és koszinusztétel",
        "A két tétel, a bizonyítás gondolata és a választás szempontjai"),
 kartya("tananyag-haromszog-megoldasa.html", "Háromszög megoldása és alkalmazások",
        "A négy alapeset receptje, a területképlet, magasság- és távolságmérés"),
 kartya("feladatok-trigonometrikus-kor.html", "🏋️ A trigonometrikus kör — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker — szögek, értékek, visszavezetés"),
 kartya("feladatok-azonossagok.html", "🏋️ Azonosságok — feladatok",
        "Alapazonosságok, addíciós és kétszeres szög, félszög, szorzattá alakítás"),
 kartya("feladatok-trig-fuggvenyek-egyenletek.html", "🏋️ Függvények és egyenletek",
        "Grafikonok, amplitúdó–periódus–fázis és minden egyenlet-alaptípus"),
 kartya("feladatok-haromszogek.html", "🏋️ Háromszögek — feladatok",
        "Szinusz- és koszinusztétel, terület, bemérési és navigációs feladatok"),
 kartya("feladatok-hazi.html", "🕹️ Vészterem — házi feladatok",
        "A teljes témakört lefedő házi feladatsor, óraszám-arányosan"),
 kartya("terepkuldetes.html", "🎯 A Fantom-frekvencia terepküldetés",
        "Háromfázisú felderítés — jelfejtés, fáziskód és háromszögelés"),
 kartya("osszefoglalo.html", "📇 Taktikai memóriakártya",
        "Minden képlet, protokoll és tipikus csapda egy helyen — dolgozat előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trigonometrikus függvények | 2e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="2e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">&#8730;</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">2e</span></a> ›
  <span class="itt">Trigonometrikus függvények</span>
</nav>
<div class="hero">
  <h1>Trigonometrikus függvények</h1>
  <p class="alcim">A trigonometrikus körtől az azonosságokon és a hullámfüggvényeken át
  a szinusz- és koszinusztételig — a második év leghosszabb témaköre.</p>
  <div class="meta-sor"><span class="chip ora">34 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧬 <b>Szektor 04 — A Fázisugrás.</b> Kiképzők:
  <b>Éjjáró</b> (a kör és az azonosságok) és <b>Szürke Janka</b> (hullámok, egyenletek,
  bemérés). Kurt minden teleportálása egy <b>szög</b> a körön — és 360 fok után ugyanoda
  ér vissza: ez a periodicitás. Janka telepatikus <b>hullámai</b> adják a szinuszgörbét
  amplitúdóval és fázissal, a küldetés végén pedig háromszögeléssel mérjük be a
  Baljós-bázist.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🌀 A trigonometrikus kör — Éjjáró</h3>
    <div class="racs">
''' + "\n".join(K[0:3]) + '''
    </div>

    <h3>🧩 Azonosságok — Éjjáró</h3>
    <div class="racs">
''' + "\n".join(K[3:6]) + '''
    </div>

    <h3>🌊 Függvények és egyenletek — Szürke Janka</h3>
    <div class="racs">
''' + "\n".join(K[6:9]) + '''
    </div>

    <h3>📐 Háromszögek — Szürke Janka</h3>
    <div class="racs">
''' + "\n".join(K[9:11]) + '''
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
''' + "\n".join(K[11:16]) + '''
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
''' + K[16] + '''
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
''' + K[17] + '''
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> altémánként előbb a tananyag-egységek sorban,
    utána a hozzá tartozó feladatgyűjtemény; a témakör végén a Taktikai memóriakártya, majd
    A Fantom-frekvencia terepküldetés. A Vészterem házi bármikor jöhet.</p>
  </div>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {delimiters:[
    {left:'\\\\(', right:'\\\\)', display:false},
    {left:'\\\\[', right:'\\\\]', display:true}
  ]});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
