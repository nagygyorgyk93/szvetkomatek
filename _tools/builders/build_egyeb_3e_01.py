# -*- coding: utf-8 -*-
"""3e/01 — osszefoglalo (F4), terepkuldetes (F5p), Veszterem (F6h), temakor-index (F5).

Kuldetes: A Kristalypara Kristalyok. Mentor: Prizma.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, GYOKER

T = dict(tagozat="3e", mappa="01-poliederek", temakor="Poliéderek")
KUL = "A Kristálypára Kristályok"

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, sqrt, simplify, N
E = []
def chk(n, g, w, tur=1e-12):
    kul = simplify(g - w)
    if not (kul == 0 or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

# alaplap-képletek
chk("egyenlo-oldalu-T", R(1, 2)*6*(6*sqrt(3)/2), 6**2*sqrt(3)/4)
chk("hatszog-T", 6*(6**2*sqrt(3)/4), 3*6**2*sqrt(3)/2)
chk("szab-sokszog", R(1, 2)*(6*6)*(6*sqrt(3)/2), 3*6**2*sqrt(3)/2)
chk("hatszog-apotema", 6*sqrt(3)/2, sqrt(6**2 - 3**2))
# nevezetes derékszögű háromszögek
chk("30-60-90", sqrt(10**2 - 5**2), 5*sqrt(3))
chk("45-45-90", sqrt(2*7**2), 7*sqrt(2))
# hasáb-átlók
chk("teglatest-D", sqrt(3**2 + 4**2 + 12**2), 13)
chk("kocka-D", sqrt(3*8**2), 8*sqrt(3))
chk("negyzetes-D", sqrt(2*6**2 + 3**2), 9)
# gúla — a szabályos gúla derékszögű háromszögei (a = 12, m = 8)
a_, m_ = 12, 8
rho_, Ro_ = R(a_, 2), a_*sqrt(2)/2
chk("gula-mo", sqrt(m_**2 + rho_**2), 10)
chk("gula-b", sqrt(m_**2 + Ro_**2), sqrt(136))
chk("gula-R-rho", Ro_**2, rho_**2 + R(a_, 2)**2)
chk("gula-V", a_**2*m_/3, 384)
# metszet-arányok
chk("hasonlosag-T", R(1, 3)**2*81, 9)
chk("hasonlosag-V", R(1, 2)**3*216, 27)
# csonkagúla (B = 100, b = 36, m = 6)
chk("csonka-V", R(6, 3)*(100 + 36 + sqrt(100*36)), 392)
chk("csonka-M", 4*R((10 + 6)*5, 2), 160)
# mértékegységek
chk("m3-liter", R(32, 10)*1000, 3200)
assert not E, E
print("sympy önteszt: OK")

# ==================================================================== F4

def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'

TE = "tananyag-terelemek.html"
ME = "tananyag-meroleges-es-szog.html"
PO = "tananyag-poliederek.html"
AL = "tananyag-alaplap.html"
HA = "tananyag-hasab.html"
HF = "tananyag-hasab-felszin-terfogat.html"
HS = "tananyag-hasab-sikmetszetek.html"
GU = "tananyag-gula.html"
GF = "tananyag-gula-felszin-terfogat.html"
GS = "tananyag-gula-sikmetszetek.html"
CS = "tananyag-csonkagula.html"

OSSZ = [
 ("Térelemek és a tér alaptörvényei", [
  '<p><b>Mi határoz meg egy síkot?</b> Három, <b>nem egy egyenesre eső</b> pont · egy '
  'egyenes és egy rá <b>nem illeszkedő</b> pont · két <b>metsző</b> egyenes · két '
  '<b>párhuzamos, nem egybeeső</b> egyenes. Mind a négy esetben pontosan egy sík van '
  '(' + h(TE, "tetel-sikmeghatarozas") + ').</p>',
  '<p>Az alábbi táblázat mindenütt <b>két különböző</b> elemet hasonlít össze — az '
  'egybeeső esetet nem soroljuk fel:</p>'
  '<div class="tblwrap"><table>'
  '<tr><th>Két egyenes</th><td><b>metsző</b> (egy közös pont)</td>'
  '<td><b>párhuzamos</b> (egy síkban, nincs közös pont)</td>'
  '<td><b>kitérő</b> (nincs közös pontjuk, és <b>nincs közös síkjuk</b>)</td></tr>'
  '<tr><th>Egyenes és sík</th><td><b>döfi</b> (egy közös pont)</td>'
  '<td><b>benne van</b> (minden pontja közös)</td>'
  '<td><b>párhuzamos</b> (nincs közös pont)</td></tr>'
  '<tr><th>Két sík</th><td colspan="2"><b>metsző</b> (a közös rész egy egyenes)</td>'
  '<td><b>párhuzamos</b> (nincs közös pont)</td></tr>'
  '</table></div>'
  '<p>⚠️ A kitérő az egyetlen olyan helyzet, amely a síkban <b>nem létezik</b> — a '
  '„nincs közös pont” a térben nem jelent párhuzamosságot (' + h(TE, "def-kitero") + ').</p>',
  '<p><b>Merőlegesség feltétele:</b> egy egyenes akkor és csak akkor merőleges a síkra, '
  'ha a sík <b>két metsző</b> egyenesére merőleges. Egyetlen egyenes nem elég, és két '
  'párhuzamos sem (' + h(ME, "tetel-meroleges-feltetel") + ').</p>',
  '<p><b>Hajlásszög:</b> ha az egyenes nem merőleges a síkra, akkor az egyenes és a '
  'síkra eső <b>merőleges vetülete</b> által bezárt szög — ez a legkisebb szög, amit '
  'az egyenes a sík egyeneseivel bezár (merőleges egyenesnél a hajlásszög $90^\\circ$) '
  '(' + h(ME, "def-hajlasszog") + '). <b>Két sík szöge (diéder):</b> a metszésvonal egy '
  'pontjában mindkét síkban a metszésvonalra <b>merőlegesen</b> húzott két félegyenes '
  'szöge (' + h(ME, "def-dieder") + ').</p>',
 ]),
 ("Poliéderek és az alaplap", [
  '<p><b>Poliéder:</b> véges sok <b>sokszöglap</b> által határolt test. <b>Konvex</b>, ha bármely '
  'két pontját összekötő szakasz teljes egészében a testben marad '
  '(' + h(PO, "def-konvex") + '). <b>Konvex</b> szabályos poliéderből <b>pontosan öt</b> van '
  '(' + h(PO, "tetel-ot-szabalyos-test") + '):</p>'
  '<div class="tblwrap"><table>'
  '<tr><th>test</th><th>lap</th><th>lapok</th><th>élek</th><th>csúcsok</th></tr>'
  '<tr><td>tetraéder</td><td>szabályos háromszög</td><td>4</td><td>6</td><td>4</td></tr>'
  '<tr><td>kocka (hexaéder)</td><td>négyzet</td><td>6</td><td>12</td><td>8</td></tr>'
  '<tr><td>oktaéder</td><td>szabályos háromszög</td><td>8</td><td>12</td><td>6</td></tr>'
  '<tr><td>dodekaéder</td><td>szabályos ötszög</td><td>12</td><td>30</td><td>20</td></tr>'
  '<tr><td>ikozaéder</td><td>szabályos háromszög</td><td>20</td><td>30</td><td>12</td></tr>'
  '</table></div>',
  '<p><b>Az alaplap területe</b> — ezen múlik minden felszín- és térfogatszámítás '
  '(' + h(AL, "tetel-teruletkepletek") + '):</p>'
  '$$T_\\triangle=\\frac{a\\cdot m_a}{2},\\qquad '
  'T_{\\text{egyenlő oldalú}}=\\frac{a^{2}\\sqrt3}{4},\\qquad '
  'T_{\\square}=a^{2},\\qquad T_{\\text{téglalap}}=ab$$'
  '$$T_{\\text{paralelogramma}}=a\\cdot m_a,\\qquad '
  'T_{\\text{trapéz}}=\\frac{(a+c)\\cdot m}{2},\\qquad '
  'T_{\\text{rombusz}}=\\frac{e\\cdot f}{2},\\qquad '
  'T_{\\text{szab. hatszög}}=\\frac{3a^{2}\\sqrt3}{2}$$',
  '<p><b>Szabályos sokszög:</b> $T=\\dfrac{K\\cdot\\rho}{2}$, ahol $K$ a kerület és '
  '$\\rho$ az <b>apotéma</b> (a beírt kör sugara, azaz a középpont és az oldal '
  'távolsága), $R$ pedig a köré írt kör sugara (a középpont és a csúcs távolsága) '
  '(' + h(AL, "tetel-szabalyos-sokszog") + '). A szabályos hatszögnél '
  '$\\rho=\\dfrac{a\\sqrt3}{2}$ és $R=a$, a négyzetnél $\\rho=\\dfrac a2$ és '
  '$R=\\dfrac{a\\sqrt2}{2}$, a szabályos háromszögnél $\\rho=\\dfrac{a\\sqrt3}{6}$ és '
  '$R=\\dfrac{a\\sqrt3}{3}$ (' + h(AL, "def-apotema") + '). A szabályos hatszög '
  '<b>hosszabb</b> átlója $2a$, a <b>rövidebb</b> $a\\sqrt3$.</p>',
  '<p><b>A két nevezetes derékszögű háromszög</b> — enélkül a térbeli feladatok fele '
  'megoldhatatlan (' + h(AL, "tetel-nevezetes-haromszogek") + '):</p>'
  '<div class="tblwrap"><table>'
  '<tr><th>$30^\\circ$–$60^\\circ$–$90^\\circ$</th>'
  '<td>oldalai $x$ : $x\\sqrt3$ : $2x$ — a <b>rövidebb</b> befogó az átfogó fele</td></tr>'
  '<tr><th>$45^\\circ$–$45^\\circ$–$90^\\circ$</th>'
  '<td>oldalai $x$ : $x$ : $x\\sqrt2$</td></tr>'
  '</table></div>',
 ]),
 ("A hasáb", [
  '<p><b>Hasáb:</b> két egybevágó, párhuzamos alaplap, az oldallapok paralelogrammák. '
  '<b>Egyenes</b>, ha az oldalélek merőlegesek az alaplapra (ekkor az oldallapok '
  'téglalapok); <b>szabályos</b>, ha ezen felül az alaplapja szabályos sokszög '
  '(' + h(HA, "def-hasab") + ', ' + h(HA, "def-szabalyos-hasab", "szabályos") + ').</p>'
  '<p>⚠️ A „szabályos” <b>nem</b> jelenti, hogy minden éle egyenlő — a magasság '
  'tetszőleges.</p>',
  '<p><b>Átlók:</b> a <b>lapátló</b> egy lapon belül két nem szomszédos csúcsot köt '
  'össze, a <b>testátló</b> két olyan csúcsot, amely nincs közös lapon '
  '(' + h(HA, "tetel-teglatest-atlo") + '):</p>'
  '$$D_{\\text{téglatest}}=\\sqrt{a^{2}+b^{2}+c^{2}},\\qquad D_{\\text{kocka}}=a\\sqrt3,'
  '\\qquad D_{\\text{négyzetes hasáb}}=\\sqrt{2a^{2}+m^{2}}$$',
  '<p><b>Felszín és térfogat</b> — $M$ a <b>palást területe</b>; az egyenes hasábnál a '
  'palást kiterítve egyetlen téglalap (' + h(HF, "tetel-hasab-felszin") + ', ' +
  h(HF, "tetel-hasab-terfogat", "térfogat") + '):</p>'
  '$$M=K\\cdot m,\\qquad F=2B+M,\\qquad V=B\\cdot m$$'
  '<p>ahol $B$ az alapterület, $K$ az alaplap kerülete, $m$ a magasság, $M$ a palást '
  'területe és $F$ a felszín.</p>',
  '<p><b>Síkmetszetek:</b> az alaplappal <b>párhuzamos</b> metszet az alaplappal '
  '<b>egybevágó</b> (' + h(HS, "tetel-hasab-parhuzamos-metszet") + ') — a hasábnál tehát nincs '
  'kicsinyítés! Az <b>átlós metszet</b> két nem szomszédos oldalélen átmenő sík '
  'metszete; konvex alaplapú egyenes hasábnál <b>téglalap</b>, amelynek egyik oldala az '
  'alaplap átlója, a másik a magasság (' + h(HS, "tetel-hasab-atlos-metszet") + '):</p>'
  '$$T_{\\text{átlós}}=d\\cdot m$$'
  '<p>ahol $d$ az <b>alaplap</b> átlója (a testátlót végig $D$ jelöli).</p>',
  '<p><b>Mértékegységek:</b> $1\\ \\text{m}^3=1000\\ \\text{dm}^3=1000$ liter, '
  '$1\\ \\text{dm}^3=1000\\ \\text{cm}^3$. Hosszban $10$-szeres, területben '
  '$100$-szoros, térfogatban <b>$1000$-szeres</b> a váltószám '
  '(' + h(HF, "tetel-hasab-terfogat") + ').</p>',
 ]),
 ("A gúla és a csonkagúla", [
  '<p><b>Gúla:</b> egy sokszög alaplap és egy, az alaplap <b>síkján kívüli</b> csúcs — '
  'az oldallapok '
  'háromszögek. <b>Szabályos</b>, ha az alaplapja szabályos sokszög, és a magasság '
  'talppontja az alaplap <b>középpontja</b>; ekkor minden oldalél egyenlő, és minden '
  'oldallap egybevágó egyenlő szárú háromszög (' + h(GU, "def-gula") + ', ' +
  h(GU, "def-szabalyos-gula", "szabályos") + ').</p>',
  '<p><b>A szabályos gúla három derékszögű háromszöge</b> — minden gúlás feladat '
  'ezekből él (' + h(GU, "tetel-harom-haromszog") + '):</p>'
  '$$m_o^{2}=m^{2}+\\rho^{2},\\qquad b^{2}=m^{2}+R^{2},\\qquad '
  'b^{2}=m_o^{2}+\\left(\\frac a2\\right)^{2},\\qquad '
  'R^{2}=\\rho^{2}+\\left(\\frac a2\\right)^{2}$$'
  '<p>$m$ = testmagasság, $m_o$ = az oldallap magassága (a gúla apotémája), '
  '$b$ = oldalél, $\\rho$ = az alaplap apotémája, $R$ = az alaplap köré írt kör sugara.</p>',
  '<p><b>Felszín és térfogat</b> — a palást a szabályos gúlánál $n$ egybevágó '
  'háromszög (' + h(GF, "tetel-gula-felszin") + ', ' + h(GF, "tetel-gula-terfogat", "térfogat") + '):</p>'
  '$$M=\\frac{K\\cdot m_o}{2},\\qquad F=B+M,\\qquad V=\\frac{B\\cdot m}{3}$$'
  '<p>⚠️ A térfogatban a <b>test</b>magasság van, a palástban az <b>oldallap</b> '
  'magassága — a kettő összekeverése a leggyakoribb hiba.</p>',
  '<p><b>Síkmetszet és hasonlóság:</b> az alaplappal párhuzamos metszet az alaplaphoz '
  '<b>hasonló</b> sokszög. Ha a csúcstól mért magasságok aránya $k$, akkor '
  '(' + h(GS, "tetel-parhuzamos-metszet") + ', ' + h(GS, "tetel-hasonlosag-aranyok", "arányok") + '):</p>'
  '$$\\text{hosszak}:k,\\qquad \\text{területek}:k^{2},\\qquad \\text{térfogatok}:k^{3}$$',
  '<p><b>Csonkagúla:</b> a gúlának az alaplap és egy vele párhuzamos metszősík közé '
  'eső darabja. Az oldallapok <b>trapézok</b>, a szabályos csonkagúlánál egybevágó '
  'egyenlő szárú trapézok (' + h(CS, "def-csonkagula") + ', ' +
  h(CS, "tetel-csonkagula-felszin", "felszín") + ', ' +
  h(CS, "tetel-csonkagula-terfogat", "térfogat") + '):</p>'
  '$$M=n\\cdot\\frac{(a+a_1)\\cdot m_o}{2},\\qquad F=B+b+M,\\qquad '
  'V=\\frac{m}{3}\\left(B+b+\\sqrt{B\\cdot b}\\right)$$'
  '<p>ahol $a$ az alaplap, $a_1$ a fedőlap éle, $n$ az oldalak száma, $m_o$ az '
  'oldallap-trapéz magassága, $B$ az alaplap és $b$ a <b>fedőlap területe</b> — '
  'itt a $b$ tehát <b>nem</b> az oldalél!</p>',
 ]),
 ("Csapdák és utolsó ellenőrzés", [
  doboz("csapda", "Amire a dolgozaton a legtöbben ráfutnak",
        '<p>1) A <b>kitérő</b> nem ugyanaz, mint a párhuzamos — a térben a „nincs közös '
        'pont" kevés. &nbsp; 2) Merőlegességhez a síkban <b>két metsző</b> egyenes kell, '
        'nem egy. &nbsp; 3) A hasábnál az alappal párhuzamos metszet <b>egybevágó</b>, a '
        'gúlánál <b>hasonló</b>. &nbsp; 4) A gúla térfogatában a <b>test</b>magasság van, '
        'a palástban az <b>oldallap</b> magassága. &nbsp; 5) A hasonlóságnál a terület '
        '$k^{2}$-tel, a térfogat $k^{3}$-nel változik — nem $k$-val. &nbsp; 6) A '
        'csonkagúla térfogatában a $\\sqrt{Bb}$ tag nem hagyható el, és nem egyenlő '
        '$\\frac{B+b}{2}$-vel. &nbsp; 7) A „szabályos hasáb” magassága tetszőleges. '
        '&nbsp; 8) Térfogatban <b>ezerszeres</b> a váltószám, nem tízszeres. &nbsp; '
        '9) A négyzetes hasáb testátlójában $2a^{2}$ áll — az alaplap átlója '
        '$a\\sqrt2$. &nbsp; 10) Az apotéma az <b>oldalhoz</b>, a köré írt sugár a '
        '<b>csúcshoz</b> mért távolság.</p>'),
  doboz("erdekesseg", "Így állj neki bármelyik térgeometriai feladatnak",
        '<p><b>①</b> Rajzolj — a rossz ábra a leggyakoribb hibaforrás. &nbsp; '
        '<b>②</b> Keresd meg az <b>alaplapot</b>, és számold ki $B$-t és $K$-t. &nbsp; '
        '<b>③</b> Rajzold ki külön a derékszögű háromszöget, amelyben az ismeretlen van '
        '($m$, $m_o$, $b$, $\\rho$, $R$). &nbsp; <b>④</b> Pitagorasz. &nbsp; '
        '<b>⑤</b> Csak a legvégén helyettesíts be a felszín- vagy térfogatképletbe, és '
        'írd ki a mértékegységet.</p>'),
  '<div class="gyakorolj"><span class="ikon">🎯</span><div><p><b>Élesben:</b> fuss át a '
  'három feladatgyűjteményen — <a href="feladatok-terelemek.html">térelemek</a> · '
  '<a href="feladatok-hasab.html">hasáb</a> · '
  '<a href="feladatok-gula.html">gúla és csonkagúla</a> —, majd indulj a '
  '<a href="terepkuldetes.html">Kristálypára terepküldetésre</a>!</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Kristálytérkép — a témakör egy lapon",
    cim_tiszta="Kristálytérkép", itt="Kristálytérkép",
    alcim="A Kristálypára Kristályok minden definíciója, képlete és tipikus csapdája egy "
          "helyen — ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-gula.html", "Feladatok — a gúla és a csonkagúla"),
    kovetkezo=("terepkuldetes.html", "A Kristálypára terepküldetés"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

from fgy_common import cards, oldal, w

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Megtaláltuk a Kristálypára forrását — egy föld alatti kamrát, '
         'amelyet egy hatszög keresztmetszetű akna köt össze a felszíni kristálycsúccsal. '
         'A műszereink csak <b>hosszakat</b> és <b>szögeket</b> mérnek; a térfogatot, a '
         'felületet és a metszeteket nekünk kell kiszámolnunk. Három fázis, három '
         'helyszín: a <b>kamrák</b>, az <b>akna</b> és a <b>kristálycsúcs</b>.'),
   '<p class="lead">Ez a küldetés a teljes témakört használja: térelemeket és '
   'hajlásszöget, alaplap-területeket, a hasáb és a gúla felszínét és térfogatát, '
   'síkmetszeteket és a hasonlóság arányait. Dolgozz füzetben, rajzolj minden '
   'feladathoz ábrát, és a végén add le a jelentést. <b>A megoldások nincsenek fent</b> '
   '— ezt a bevetést a tanárod értékeli.</p>',
   '<p>A hosszakat, a területeket, a térfogatokat, az arányokat és a szögeket '
   '<b>két tizedesjegyre</b> kerekítve add meg. Számológépet használhatsz.</p>',
 ]),
 ("Fázis I — A kamra felmérése", [
   doboz("pelda", "I. fázis: a tér felmérése",
         '<ol class="reszfeladatok">'
         '<li>A kristálykamra kocka alakú, éle $12$ m. <b>a)</b> Mekkora az alaplapjának '
         'átlója és a testátlója? <b>b)</b> Mekkora szöget zár be a testátló az '
         'alaplappal? <b>c)</b> Hány olyan éle van a kockának, amely az egyik alapéllel '
         '<b>kitérő</b>?</li>'
         '<li>A felszínen, a kamra fölött függőleges jelzőoszlop áll, a magassága $9$ m. '
         'A vízszintes talajon két mérőpont van, az oszlop talppontjától $5$ m, illetve '
         '$12$ m távolságra. Mekkora <b>emelkedési szög</b> alatt látszik az oszlop '
         'csúcsa a két pontból?</li>'
         '<li>A kamrához csatlakozó <b>raktárkamra</b> padlója szabályos hatszög, az '
         'oldala $8$ m. Mekkora az apotémája és a területe?</li>'
         '<li>Egy harmadik, ferde mennyezetű kamrában a mennyezet lapja '
         '$60^\\circ$-os szöget zár be a padlóval. A padlón felveszünk egy pontot, amely '
         'a két sík metszésvonalától $10$ m-re van. Milyen messze van ez a pont a '
         'mennyezet síkjától? Rajzold le, melyik derékszögű háromszögben számolsz!</li>'
         '</ol>'),
 ]),
 ("Fázis II — A hasáb-akna", [
   doboz("pelda", "II. fázis: az akna",
         '<ol class="reszfeladatok">'
         '<li>Az akna szabályos hatoldalú hasáb: az alapéle $4$ m, a magassága $15$ m. '
         'Mekkora a térfogata és a felszíne?</li>'
         '<li>Hány <b>liter</b> kristálypára fér az aknába, ha teljesen megtöltjük? '
         '(Kerekíts ezer literre.)</li>'
         '<li>Az aknát a <b>hosszabb</b> alaplapátlón átmenő, az alaplapra <b>merőleges</b> '
         'síkkal (vagyis két szemközti oldalélen átmenő síkkal) metsszük el. Milyen '
         'alakzat a metszet, és mekkora a területe?</li>'
         '<li>A pára egy téglatest alakú tartályba kerül, amelynek élei $3$ m, $4$ m és '
         '$12$ m. <b>a)</b> Mekkora a tartály testátlója? <b>b)</b> Elfér-e benne az '
         'akna teljes tartalma? Ha nem, hányad része fér el?</li>'
         '</ol>'),
 ]),
 ("Fázis III — A kristálycsúcs", [
   doboz("pelda", "III. fázis: a csúcs",
         '<ol class="reszfeladatok">'
         '<li>A felszíni kristálycsúcs szabályos négyoldalú gúla: az alapéle $10$ m, a '
         'testmagassága $12$ m. Mekkora az oldallapjának magassága, a felszíne és a '
         'térfogata?</li>'
         '<li>A kristálycsúcsot <b>félmagasságban</b>, az alaplappal párhuzamos síkkal '
         'metsszük el. Mekkora a metszet területe és a levágott kis gúla térfogata?</li>'
         '<li>Mekkora az alsó darab, vagyis a keletkező <b>csonkagúla</b> térfogata? '
         'Ellenőrizd a csonkagúla térfogatképletével is!</li>'
         '<li>Egy másik kristályból szabályos négyoldalú csonkagúlát faragtak: az '
         'alapélei $10$ m és $6$ m, a testmagassága $8$ m. Mekkora a térfogata?</li>'
         '</ol>'),
   '<div class="gyakorolj"><span class="ikon">📋</span><div><p><b>Jelentés:</b> minden '
   'feladathoz legyen <b>ábra</b>, és jelöld be rajta azt a derékszögű háromszöget, '
   'amelyben számoltál. Írd le, melyik képletet miért választottad, és mindenhol tedd ki '
   'a <b>mértékegységet</b>. A kerekítési szabály betartása is pont.</p></div></div>',
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="A Kristálypára",
    cim_tiszta="A Kristálypára", itt="A Kristálypára terepküldetés",
    alcim="Háromfázisú felderítés — a kamra felmérése térelemekkel, a hasáb-akna "
          "térfogata és metszete, végül a kristálycsúcs gúlája és csonkagúlája.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Kristálytérkép"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h

E2 = []
def chk2(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not (kul == 0 or abs(float(N(kul))) <= tur):
        E2.append((n, g, w))

def Bn(n, a):
    return {3: a**2*sqrt(3)/4, 4: a**2, 6: 6*a**2*sqrt(3)/4}[n]

chk2("A2", sqrt(2)*9, 9*sqrt(2)); chk2("A2b", sqrt(3)*9, 9*sqrt(3))
chk2("A3-rho", 10*sqrt(3)/2, 5*sqrt(3)); chk2("A3-T", 6*Bn(3, 10), 150*sqrt(3))
chk2("A4-F", 2*49 + 4*7*10, 378); chk2("A4-V", 49*10, 490)
chk2("A5-F", 2*Bn(3, 6) + 3*6*9, 18*sqrt(3) + 162); chk2("A5-V", Bn(3, 6)*9, 81*sqrt(3))
chk2("A6-D", sqrt(5**2 + 6**2 + 10**2), sqrt(161))
chk2("A6-F", 2*(30 + 50 + 60), 280); chk2("A6-V", 5*6*10, 300)
chk2("A7-mo", sqrt(3**2 + 4**2), 5); chk2("A7-F", 64 + 4*8*5/2, 144)
chk2("A7-V", 64*3/3, 64)
chk2("A8", R(25, 10)*1000, 2500); chk2("A8b", R(3400, 1000), R(34, 10))
chk2("K1-m", sqrt(6**2 - 2*4**2), 2); chk2("K1-V", 16*2, 32)
chk2("K2-m", 300*sqrt(3)/Bn(6, 5), 8)
chk2("K3-m", sqrt(13**2 - 5**2), 12); chk2("K3-F", 100 + R(4*10*13, 2), 360)
chk2("K3-b", sqrt(13**2 + 5**2), sqrt(194)); chk2("K3-bk", sqrt(194), 13.928388, 1e-6)
chk2("K3-V", 100*12/3, 400)
chk2("K4-kis", R(1, 8)*288, 36); chk2("K4-also", 288 - 36, 252)
chk2("K5-M", 4*R((8 + 4)*5, 2), 120); chk2("K5-F", 64 + 16 + 120, 200)
chk2("K6-mo", sqrt(R(15, 10)**2 + 2**2), R(25, 10))
chk2("K6-M", 4*4*R(25, 10)/2, 20); chk2("K6-V", 16*R(15, 10)/3, 8)
chk2("N1-m", 6*sqrt(2)*sqrt(3), 6*sqrt(6)); chk2("N1-mk", 6*sqrt(6), 14.696938, 1e-6)
chk2("N1-F", 2*36 + 4*6*6*sqrt(6), 72 + 144*sqrt(6))
chk2("N1-Fk", 72 + 144*sqrt(6), 424.726518, 1e-5)
chk2("N1-V", 36*6*sqrt(6), 216*sqrt(6)); chk2("N1-Vk", 216*sqrt(6), 529.089777, 1e-5)
chk2("N2-F", 144 + 4*12*12/2, 432); chk2("N2-V", 144*6*sqrt(3)/3, 288*sqrt(3))
chk2("N3-m", sqrt(5**2 - 3**2), 4)
chk2("N3-F", 196 + 64 + 4*R((14 + 8)*5, 2), 480)
chk2("N3-V", R(4, 3)*(196 + 64 + sqrt(196*64)), 496)
assert not E2, E2
print("sympy önteszt (Vészterem): OK")

DR_A = [
 ("Igaz vagy hamis a <b>térben</b>?",
  ["Ha két egyenesnek nincs közös pontja, akkor párhuzamosak.",
   "Két metsző egyenes mindig meghatároz egy síkot.",
   "Ha egy egyenes merőleges a sík egy egyenesére, akkor merőleges a síkra.",
   "A hasáb alaplapjával párhuzamos síkmetszete egybevágó az alaplappal."],
  ["hamis — kitérők is lehetnek", "igaz", "hamis — két metsző egyenes kell", "igaz"], True),

 ("Egy kocka éle $9$ cm. Mekkora a lapátlója és a testátlója?", None,
  "Lapátló $9\\sqrt2\\approx 12{,}73$ cm, testátló $9\\sqrt3\\approx 15{,}59$ cm."),

 ("Egy szabályos hatszög oldala $10$ cm. Mekkora az apotémája és a területe?", None,
  "Az apotéma $5\\sqrt3\\approx 8{,}66$ cm, a terület $150\\sqrt3\\approx 259{,}81$ cm²."),

 ("Egy négyzetes hasáb alapéle $7$ cm, magassága $10$ cm. Mekkora a felszíne és a "
  "térfogata?", None, "$F=378$ cm², $V=490$ cm³."),

 ("Egy szabályos háromoldalú hasáb alapéle $6$ cm, magassága $9$ cm. Mekkora a felszíne "
  "és a térfogata?", None,
  "$F=18\\sqrt3+162\\approx 193{,}18$ cm², $V=81\\sqrt3\\approx 140{,}30$ cm³."),

 ("Egy téglatest élei $5$ cm, $6$ cm és $10$ cm. Mekkora a testátlója, a felszíne és a "
  "térfogata?", None,
  "$D=\\sqrt{161}\\approx 12{,}69$ cm, $F=280$ cm², $V=300$ cm³."),

 ("Egy szabályos négyoldalú gúla alapéle $8$ cm, a testmagassága $3$ cm. Mekkora az "
  "oldallapjának magassága, a felszíne és a térfogata?", None,
  "Az oldallap magassága $5$ cm, a felszín $144$ cm², a térfogat $64$ cm³."),

 ("Váltsd át!",
  ["$2{,}5\\ \\text{m}^3$ hány liter?", "$3400\\ \\text{cm}^3$ hány $\\text{dm}^3$?"],
  ["$2500$ liter", "$3{,}4\\ \\text{dm}^3$"], True),
]

DR_K = [
 ("Egy négyzetes hasáb alapéle $4$ cm, a testátlója $6$ cm. Mekkora a magassága és a "
  "térfogata?", None, "$m=2$ cm, $V=32$ cm³."),

 ("Egy szabályos hatoldalú hasáb térfogata $300\\sqrt3$ cm³, az alapéle $5$ cm. Mekkora "
  "a magassága?", None, "$m=8$ cm."),

 ("Egy szabályos négyoldalú gúla alapéle $10$ cm, az oldallapjának magassága $13$ cm. "
  "Mekkora a testmagassága, az oldaléle, a felszíne és a térfogata?", None,
  "A testmagasság $12$ cm, az oldalél $\\sqrt{194}\\approx 13{,}93$ cm, a felszín "
  "$360$ cm², a térfogat $400$ cm³."),

 ("Egy gúla térfogata $288$ cm³. Félmagasságban, az alaplappal párhuzamosan elmetsszük. "
  "Mekkora a felső kis gúla és az alsó csonkagúla térfogata?", None,
  "A kis gúla $36$ cm³, a csonkagúla $252$ cm³."),

 ("Egy szabályos négyoldalú csonkagúla alapélei $8$ cm és $4$ cm, az oldallap magassága "
  "$5$ cm. Mekkora a palástjának területe és a felszíne?", None,
  "A palást területe $120$ cm², a felszín $200$ cm²."),

 ("Egy sátor szabályos négyoldalú gúla alakú: az alapéle $4$ m, a magassága $1{,}5$ m. "
  "Hány négyzetméter ponyva kell hozzá (alj nélkül), és hány köbméter levegő van benne?",
  None, "$20\\ \\text{m}^2$ ponyva, $8\\ \\text{m}^3$ levegő."),
]

DR_N = [
 ("Egy négyzetes hasáb alapéle $6$ cm, és a testátlója $60^\\circ$-os szöget zár be az "
  "alaplappal. Mekkora a magassága, a felszíne és a térfogata?", None,
  "$m=6\\sqrt6\\approx 14{,}70$ cm, $F=72+144\\sqrt6\\approx 424{,}73$ cm², "
  "$V=216\\sqrt6\\approx 529{,}09$ cm³."),

 ("Egy szabályos négyoldalú gúla alapéle $12$ cm, és az oldallapja $60^\\circ$-os szöget "
  "zár be az alaplappal. Mekkora a testmagassága, a felszíne és a térfogata?", None,
  "$m=6\\sqrt3\\approx 10{,}39$ cm, $F=432$ cm², $V=288\\sqrt3\\approx 498{,}83$ cm³."),

 ("Egy szabályos négyoldalú csonkagúla alapélei $14$ cm és $8$ cm, az oldallap magassága "
  "$5$ cm. Mekkora a testmagassága, a felszíne és a térfogata?", None,
  "$m=4$ cm, $F=480$ cm², $V=496$ cm³."),
]

dr_brief = ('<div class="brief"><p>🕹️ <b>SZVETI:</b> <b>Vészterem</b> — A Kristálypára '
            'Kristályok küldetés modulja. A szimuláció a <b>teljes témakört</b> lefedi: térelemek és '
            'merőlegesség, alaplap-területek, a hasáb és a gúla felszíne és térfogata, '
            'síkmetszetek, hasonlóság és a csonkagúla. Haladj a fokozatokon: zöld → sárga '
            '→ piros. A végeredményt lenyithatod, de előbb birkózz meg vele magad!</p></div>')

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
      nxt="osszefoglalo.html", nxtc="Kristálytérkép")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5

def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = [
 kartya("tananyag-terelemek.html", "Térelemek a térben",
        "Pont, egyenes és sík, síkmeghatározás, két egyenes helyzete és a kitérő egyenesek"),
 kartya("tananyag-meroleges-es-szog.html", "Merőlegesség és szögek a térben",
        "Mikor merőleges egy egyenes a síkra, hajlásszög, diéder és távolságok"),
 kartya("tananyag-poliederek.html", "Poliéderek",
        "A poliéder fogalma, konvexitás, az öt szabályos test és a hálók"),
 kartya("tananyag-alaplap.html", "Az alaplap",
        "Háromszögek, négyszögek és szabályos sokszögek területe, apotéma, nevezetes háromszögek"),
 kartya("tananyag-hasab.html", "A hasáb és elemei",
        "Hogyan keletkezik a hasáb, fajták, a háló, valamint a lapátló és a testátló"),
 kartya("tananyag-hasab-felszin-terfogat.html", "A hasáb felszíne és térfogata",
        "A palást a hálóból, a $V=Bm$ képlet, fordított feladatok és a mértékegységek"),
 kartya("tananyag-hasab-sikmetszetek.html", "A hasáb síkmetszetei",
        "Az alappal párhuzamos metszet, az átlós metszetek és a területük kiszámítása"),
 kartya("tananyag-gula.html", "A gúla és elemei",
        "A szabályos gúla, a magasság talppontja és a három derékszögű háromszög"),
 kartya("tananyag-gula-felszin-terfogat.html", "A gúla felszíne és térfogata",
        "A palást az oldallap-magassággal, a térfogat harmada és az összetett testek"),
 kartya("tananyag-gula-sikmetszetek.html", "A gúla síkmetszetei",
        "Az alappal párhuzamos metszet, a hasonlóság arányai és a tengelymetszetek"),
 kartya("tananyag-csonkagula.html", "A csonkagúla",
        "A csonkagúla elemei, a trapéz oldallapok, a felszín és a térfogat — képlettárral"),
 kartya("feladatok-terelemek.html", "🏋️ Térelemek és poliéderek — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker — tér, merőlegesség, alaplap"),
 kartya("feladatok-hasab.html", "🏋️ A hasáb — feladatok",
        "Átlók, felszín és térfogat, fordított feladatok, mértékegységek és metszetek"),
 kartya("feladatok-gula.html", "🏋️ A gúla és a csonkagúla — feladatok",
        "A három derékszögű háromszög, felszín és térfogat, hasonlóság és csonkagúla"),
 kartya("feladatok-hazi.html", "🕹️ Vészterem — házi feladatok",
        "A teljes témakört lefedő házi feladatsor, óraszám-arányosan"),
 kartya("terepkuldetes.html", "🎯 A Kristálypára terepküldetés",
        "Háromfázisú felderítés — a kamra, a hasáb-akna és a kristálycsúcs"),
 kartya("osszefoglalo.html", "📇 Kristálytérkép",
        "Minden definíció, képlet és tipikus csapda egy helyen — dolgozat előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Poliéderek | 3e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="3e">
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
  <a href="../index.html"><span class="tagozat-jel">3e</span></a> ›
  <span class="itt">Poliéderek</span>
</nav>
<div class="hero">
  <h1>Poliéderek</h1>
  <p class="alcim">A tér alaptörvényeitől a hasáb és a gúla felszínén és térfogatán át
  a síkmetszetekig és a csonkagúláig — a harmadik év első és leghosszabb geometriai
  témaköre.</p>
  <div class="meta-sor"><span class="chip ora">21 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🔷 <b>Szektor 01 — A Kristálypára Kristályok.</b> Kiképző:
  <b>Prizma</b>. A Kristálypára minden cseppje ugyanúgy fagy meg: <b>lapokból</b> épülő
  testté. Prizma megtanítja, hogyan lehet egy testet két adatból — az <b>alaplapból</b> és
  a <b>magasságból</b> — teljesen felmérni: mekkora a felülete, mennyi fér bele, és mi
  látszik belőle, ha elmetsszük.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🧭 A tér és a poliéderek — Prizma</h3>
    <div class="racs">
''' + "\n".join(K[0:4]) + '''
    </div>

    <h3>🧱 A hasáb — Prizma</h3>
    <div class="racs">
''' + "\n".join(K[4:7]) + '''
    </div>

    <h3>🔺 A gúla és a csonkagúla — Prizma</h3>
    <div class="racs">
''' + "\n".join(K[7:11]) + '''
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
''' + "\n".join(K[11:15]) + '''
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
''' + K[15] + '''
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
''' + K[16] + '''
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> altémánként előbb a tananyag-egységek sorban,
    utána a hozzá tartozó feladatgyűjtemény; a témakör végén a Kristálytérkép, majd
    A Kristálypára terepküldetés. A Vészterem házi bármikor jöhet.</p>
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
