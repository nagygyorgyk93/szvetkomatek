# -*- coding: utf-8 -*-
"""3e/01 — B altema: a hasab (B1), felszin es terfogat (B2), sikmetszetek (B3).
Mentor: Prizma. Kuldetes: A Kristalypara Kristalyok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_hasab, svg_halo, svg_sikidom

T = dict(tagozat="3e", mappa="01-poliederek", temakor="Poliéderek")
FGY = "feladatok-hasab.html"
KUL = "A Kristálypára Kristályok"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, simplify, N, Matrix
E = []
def chk(n, g, w, tur=1e-12):
    """A várt értéket FÜGGETLENÜL számoljuk ki; itt csak az egyezést ellenőrizzük."""
    e = simplify(g - w)
    if not (e == 0 or abs(float(N(e))) <= tur):
        E.append((n, g, w))

# B1 — átlók
a, b, c = 3, 4, 12
chk("teglatest-atlo", sqrt(a**2 + b**2 + c**2), 13)
chk("kocka-lapatlo", sqrt(5**2 + 5**2), 5*sqrt(2))
chk("kocka-testatlo", sqrt((5*sqrt(2))**2 + 5**2), 5*sqrt(3))
# B2 — szabályos háromoldalú hasáb: a = 6, m = 10
B3o = 6**2*sqrt(3)/4
chk("h3-B", B3o, 9*sqrt(3))
chk("h3-M", 3*6*10, 180)
chk("h3-F", 2*B3o + 180, 18*sqrt(3) + 180)
chk("h3-V", B3o*10, 90*sqrt(3))
# B2 — szabályos hatoldalú hasáb: a = 4, m = 9
B6o = 6*4**2*sqrt(3)/4
chk("h6-B", B6o, 24*sqrt(3))
chk("h6-M", 6*4*9, 216)
chk("h6-F", 2*B6o + 216, 48*sqrt(3) + 216)
chk("h6-V", B6o*9, 216*sqrt(3))
chk("h6-V-kozelito", N(B6o*9), 374.1229744348775, 1e-9)
# B2 — fordított: V = 1080, a = 6 (négyzet alap) → m
chk("forditott-m", R(1080, 6**2), 30)
# B2 — mértékegység
chk("m3-dm3", 1000, 10**3)
# B3 — metszetek
chk("negyzet-atlos-T", 6*sqrt(2)*8, 48*sqrt(2))
chk("hatszog-hosszu-atlo", 2*5, 10)
chk("hatszog-rovid-atlo", sqrt(3)*5, 5*sqrt(3))
chk("hatszog-metszet-hosszu", 2*5*7, 70)
chk("hatszog-metszet-rovid", 5*sqrt(3)*7, 35*sqrt(3))
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_HASAB3 = svg_hasab("haromszog", a=1.0, m=1.5, w=300, h=280,
                       feliratok={"a": "a"},
                       leiras="Szabályos háromoldalú hasáb")
SVG_HASAB6 = svg_hasab("hatszog", a=1.0, m=1.6, magassag=True, w=340, h=290,
                       feliratok={"a": "a", "m": "m"},
                       leiras="Szabályos hatoldalú hasáb a magasságával")
SVG_TEGLATEST = svg_hasab("teglalap", a=1.6, b=0.9, m=1.1, testatlo=True, alapatlo=True,
                          w=340, h=265, feliratok={"D": "D", "d": "d"},
                          leiras="Téglatest az alaplap átlójával és a testátlójával")
SVG_HALO6 = svg_halo("hasab", n=6, w=330, h=250)
SVG_HALO4 = svg_halo("hasab", n=4, w=320, h=240,
                     leiras="A négyzetes hasáb hálója: két négyzet és a palást téglalapja")
SVG_METSZET_ATLOS = svg_hasab("negyzet", a=1.0, m=1.4, metszet="atlos", w=310, h=280,
                              leiras="A négyzetes hasáb átlós metszete az AC és A1C1 átlókon át")
SVG_METSZET_PARH = svg_hasab("hatszog", a=1.0, m=1.6, metszet="parhuzamos", w=330, h=290,
                             leiras="Az alaplappal párhuzamos metszet egybevágó az alaplappal")
SVG_HATSZOG_ATLOK = svg_sikidom("sokszog", n=6, w=300, h=250,
                                leiras="A szabályos hatszög apotémája és köréírt sugara")

# ===================================================================== B1

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A Karantén-Zóna legtöbb kristálya <b>oszlopos</b>: egy sokszög '
         'elindul a saját síkjából, és söpör végig egy térrészt. Ez a hasáb. Ha meg tudod mondani, '
         'melyik éle mekkora, akkor a benne tárolt energiát is ki tudod számolni — de előbb '
         'ismerni kell a test <b>alkatrészeit</b>: melyik él az alapél, mekkora a magasság, '
         'és mi az a testátló, amit a kadétok fele meg sem talál a testben.'),
   '<p>Ebben a blokkban találkozol az első igazi <b>testtel</b>. Az előző egységekben a tér szabályait és '
   '<a href="tananyag-alaplap.html">az alaplapot</a> néztük meg — most ezek összeállnak.</p>',
 ]),

 ("Hogyan keletkezik a hasáb", [
   doboz("definicio", "A hasáb",
         '<p>Vegyünk egy síksokszöget, és toljuk el a saját síkjából egy irányba. A '
         'kiindulási sokszög és az eltolt képe a test két <b>alaplapja</b> (a felsőt szokás '
         '<b>fedőlapnak</b> is hívni), a megfelelő csúcsokat összekötő szakaszok az '
         '<b>oldalélek</b>, a köztük keletkező paralelogrammák pedig az <b>oldallapok</b>. '
         'Az oldallapok együtt alkotják a <b>palástot</b>.</p>'
         '<p>A két alaplap <b>egybevágó és párhuzamos</b>, az oldalélek pedig egyenlő '
         'hosszúak és párhuzamosak egymással.</p>',
         hid="def-hasab"),
   '<p>A hasáb <b>magassága</b> ($m$) a két alaplap síkjának távolsága — vagyis merőleges '
   'távolság, ahogy azt a <a href="tananyag-meroleges-es-szog.html#def-hajlasszog">'
   'szögek és távolságok</a> egységben láttuk. Ez nem mindig egyezik meg az oldalél '
   'hosszával: csak akkor, ha az oldalélek merőlegesek az alaplapra.</p>',
 ]),

 ("Fajták", [
   '<p>Az elnevezések három dolgot rögzítenek: hogy állnak az oldalélek, milyen az '
   'alaplap, és hány oldalú. Az alapél az alaplap egy oldala; a <b>magasságot</b> $m$-mel '
   'jelöljük.</p>',
   doboz("definicio", "Egyenes, ferde és szabályos hasáb",
         '<ul>'
         '<li><b>Egyenes</b> a hasáb, ha az oldalélei merőlegesek az alaplapra. Ekkor az '
         'oldallapok téglalapok, és a magasság megegyezik az oldalél hosszával.</li>'
         '<li><b>Ferde</b> a hasáb, ha az oldalélei nem merőlegesek az alaplapra. Ekkor a '
         'magasság <b>rövidebb</b>, mint az oldalél.</li>'
         '<li><b>Szabályos</b> a hasáb, ha <b>egyenes</b>, és az alaplapja <b>szabályos '
         'sokszög</b>.</li>'
         '</ul>'
         '<p>A hasábot az alaplapja szerint nevezzük el: háromoldalú, négyoldalú, hatoldalú '
         'hasáb. A négyzet alapú egyenes hasábot röviden <b>négyzetes hasábnak</b> is '
         'hívjuk — ez ugyanaz, mint a szabályos négyoldalú hasáb.</p>',
         hid="def-szabalyos-hasab"),
   abra(SVG_HASAB3, 'Szabályos háromoldalú hasáb: az alaplapja egyenlő oldalú háromszög, '
        'az oldalélei merőlegesek rá.'),
   doboz("definicio", "Paralelepipedon, téglatest, kocka",
         '<p>Ha a hasáb alaplapja <b>paralelogramma</b>, a testet <b>paralelepipedonnak</b> '
         'nevezzük. Ennek minden lapja paralelogramma.</p>'
         '<p>A <b>téglatest</b> olyan egyenes hasáb, amelynek az alaplapja téglalap — így '
         'mind a hat lapja téglalap. Ha ezenfelül minden éle egyenlő, <b>kockát</b> kapunk.</p>',
         hid="def-teglatest"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Szabályos hasáb — akkor minden éle egyenlő, tehát az alapélből következik '
         'a magasság is."</i></p>'
         '<p>Nem következik. A „szabályos” itt csak az <b>alaplapra</b> és az oldalélek '
         '<b>állására</b> vonatkozik: a magasság ettől függetlenül bármekkora lehet. Egy '
         '$2$ cm alapélű, $50$ cm magas szabályos négyoldalú hasáb ugyanolyan szabályos, '
         'mint egy $2$ cm magas. Az az <b>egyenes</b> hasáb, amelynek az alaplapja '
         'négyzet és minden éle egyenlő, a <b>kocka</b> — az csak egy speciális eset.</p>'),
   kviz('Melyik állítás igaz <b>minden</b> szabályos négyoldalú hasábra?',
        ['Az alaplapja négyzet, a magassága viszont tetszőleges',
         'Minden éle egyenlő hosszú',
         'Az oldallapjai négyzetek'], 0,
        jo="✔ A „szabályos” az alaplapra és az oldalélek merőlegességére vonatkozik, a magasságra nem.",
        nem="✘ Gondolj egy hosszú, vékony oszlopra: az alaplapja négyzet, az oldalélei merőlegesek "
            "rá — szabályos hasáb, pedig sem az élei nem egyenlők, sem az oldallapjai nem négyzetek."),
 ]),

 ("A hasáb hálója", [
   '<p>Vágjuk fel a hasábot az egyik oldaléle mentén, és a két alaplap kerülete mentén is — '
   'de mindkét alaplapnál hagyjunk egy élt, amellyel az alaplap a paláston marad. Ezután '
   'terítsük ki a lapokat egy síkba. <b>Egyenes</b> hasábnál a palást egyetlen <b>téglalappá</b> nyílik ki: '
   'ennek egyik oldala az alaplap <b>kerülete</b>, a másik a hasáb <b>magassága</b>.</p>',
   abra(SVG_HALO6, 'A szabályos hatoldalú hasáb hálója: két szabályos hatszög és a palást '
        'téglalapja, hat egyenlő részre osztva.'),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A dobozok gyártása pontosan ez a művelet visszafelé: a gép egyetlen '
         'kartonlapból stancolja ki a hálót, és a hajtásélek adják a test éleit. Ezért '
         'számít a csomagolóiparban a <b>háló területe</b> — vagyis a felszín —, nem a '
         'doboz térfogata.</p>'),
 ]),

 ("Átlók: lapátló és testátló", [
   '<p>A hasábban kétféle átló lehet: a <b>lapátló</b> egy lapon belül köt össze két '
   '<b>nem szomszédos</b> csúcsot, a <b>testátló</b> pedig két olyan csúcsot, amelyek '
   'nincsenek egy lapon. (Háromoldalú hasábnak nincs testátlója: bármely két csúcsa közös '
   'lapon van.)</p>',
   abra(SVG_TEGLATEST, 'A téglatest alaplapjának átlója ($d$, narancs) és a testátló '
        '($D$, kék). A levezetésben előbb a $d$-t számoljuk ki, aztán abból a $D$-t.'),
   doboz("tetel", "A téglatest testátlója",
         '<p>Ez a képlet <b>téglatestre</b> szól. Ha az egy csúcsból induló élek $a$, $b$ és '
         '$c$ — ahol $a$ és $b$ az alaplap élei, $c$ pedig a magasság —, akkor a testátló</p>'
         '$$D=\\sqrt{a^2+b^2+c^2}.$$'
         '<p><b>Levezetés két lépésben.</b> Az alaplap átlója a Pitagorasz-tétel szerint '
         '$d=\\sqrt{a^2+b^2}$. Ez a lapátló az oldaléllel és a testátlóval egy derékszögű '
         'háromszöget alkot (az oldalél merőleges az alaplapra), ezért '
         '$D=\\sqrt{d^2+c^2}=\\sqrt{a^2+b^2+c^2}$.</p>'
         '<p>Kockára ($a=b=c$): a <b>lapátló</b> $a\\sqrt2$, a <b>testátló</b> '
         '$a\\sqrt3$.</p>',
         hid="tetel-teglatest-atlo"),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy téglatest alaplapjának élei $3$ cm és $4$ cm, a magassága $12$ cm. Mekkora a '
         'testátlója, és mekkora szöget zár be az alaplappal?</p>',
         hid="pelda-teglatest-atlo",
         lenyilo=("Megoldás",
                  '<p>Az alaplap átlója $d=\\sqrt{3^2+4^2}=5$ cm, a testátló pedig</p>'
                  '$$D=\\sqrt{3^2+4^2+12^2}=\\sqrt{169}=13\\ \\text{cm}.$$'
                  '<p>A testátló vetülete az alaplapon éppen a $d$ lapátló, ezért a keresett '
                  'szögre $\\operatorname{tg}\\varphi=\\frac{12}{5}=2{,}4$, ahonnan '
                  '$\\varphi\\approx 67{,}38^\\circ$.</p>')),
   kviz('Mekkora az $5$ cm élű kocka <b>testátlója</b>?',
        ['$5\\sqrt3\\approx 8{,}66$ cm', '$5\\sqrt2\\approx 7{,}07$ cm', '$15$ cm'], 0,
        jo="✔ A testátló a√3 = 5√3; az 5√2 a lapátló volna.",
        nem="✘ Két lépés: a lapátló 5√2, majd ezzel és az éllel újra Pitagorasz: "
            "√(50+25) = √75 = 5√3."),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Prizma:</b> Az alkatrészeket ismered, a hálót látod. A háló területe a '
         '<b>felszín</b>, a test által bezárt tér a <b>térfogat</b> — a kristály '
         'hűlési sebessége az egyikből, az energiája a másikból jön. Számoljuk ki mindkettőt.',
         outro=True),
 ]),
]

# ===================================================================== B2

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Két szám, két külön képlet — és a legtöbb hiba abból ered, hogy a '
         'kadét összekeveri őket. A <b>felszín</b> a testet határoló lapok területének '
         'összege — ennyi anyag kell a burkolatához (m²) —, a <b>térfogat</b> pedig azt '
         'mondja meg, mennyi fér bele (m³). Ha egy kristálytartályt festeni akarsz, '
         'felszínt számolsz; ha tölteni, térfogatot.'),
   '<p>Mindkét képlet abból következik, amit már láttunk: a felszín a <b>hálóból</b>, a térfogat '
   'pedig a téglatestből általánosítva.</p>',
 ]),

 ("A felszín a hálóból", [
   doboz("tetel", "Az egyenes hasáb felszíne",
         '<p><b>Egyenes</b> hasáb esetén a palást kiterítve téglalap, amelynek egyik oldala az '
         'alaplap kerülete ($K$), a másik a magasság ($m$). A palást területét $M$-mel, a '
         'felszínt $F$-fel jelöljük:</p>'
         '$$M=K\\cdot m,\\qquad F=2B+M=2B+K\\cdot m,$$'
         '<p>ahol $B$ az alaplap területe. A $2B$ azért szerepel, mert a testnek <b>két</b> '
         'egybevágó alaplapja van.</p>'
         '<p><b>Ferde</b> hasábnál ez a képlet nem érvényes: ott az oldallapok '
         'paralelogrammák, és külön-külön kell kiszámolni a területüket, majd összeadni.</p>',
         hid="tetel-hasab-felszin"),
   abra(SVG_HALO4, 'A négyzetes hasáb hálója: a palást téglalapjának egyik oldala az '
        'alaplap kerülete, a másik a magasság.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A palást az alaplap és a magasság szorzata.”</i></p>'
         '<p>A palásthoz az alaplap <b>kerülete</b> kell, nem a <b>területe</b>. '
         'Gondolj a fenti hálóra: a téglalap egyik oldalára az alaplap kerülete simul rá. Ellenőrzés mértékegységgel: $K\\cdot m$ hosszúság × hosszúság = terület '
         '(cm²) — ez rendben van; $B\\cdot m$ viszont terület × hosszúság = <b>térfogat</b> '
         '(cm³), tehát az biztosan nem lehet a palást.</p>'),
 ]),

 ("A térfogat", [
   doboz("tetel", "A hasáb térfogata",
         '<p>Minden hasáb térfogata</p>'
         '$$V=B\\cdot m,$$'
         '<p>ahol $B$ az alaplap területe, $m$ pedig a magasság (a két alaplap síkjának '
         'távolsága). A képlet a <b>ferde</b> hasábra is igaz — de csak a magassággal, nem '
         'az oldaléllel.</p>',
         hid="tetel-hasab-terfogat"),
   '<p>Miért éppen ennyi? A téglatestnél a térfogat $abc$: az alaplap területe $ab$, a '
   'magasság $c$, tehát tényleg $V=B\\cdot m$. Tetszőleges hasábnál a következő '
   '<b>alapelvre</b> támaszkodunk: ha két testet az alaplapjukkal párhuzamosan, bármilyen '
   'magasságban elmetszünk, és a két metszet területe mindig egyenlő, akkor a két test '
   'térfogata is egyenlő. Állítsunk a hasáb mellé egy vele azonos alapterületű és azonos '
   'magasságú téglatestet: minden metszet területe mindkettőnél $B$, tehát a térfogatuk is '
   'egyenlő — vagyis $V=B\\cdot m$. (Ennek az alapelvnek a pontos kimondása és '
   'bizonyítása már nem tananyagunk.)</p>',
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos hatoldalú hasáb alapéle $4$ cm, magassága $9$ cm. Számítsd ki a '
         'felszínét és a térfogatát!</p>',
         hid="pelda-hatszog-hasab",
         lenyilo=("Megoldás",
                  '<p><b>Alaplap.</b> A szabályos hatszög hat egyenlő oldalú háromszögre '
                  'bomlik (lásd <a href="tananyag-alaplap.html#tetel-szabalyos-sokszog">'
                  'az alaplap egységet</a>):</p>'
                  '$$B=6\\cdot\\frac{4^2\\sqrt3}{4}=24\\sqrt3\\approx 41{,}57\\ \\text{cm}^2.$$'
                  '<p><b>Palást.</b> A kerület $K=6\\cdot 4=24$ cm, ezért '
                  '$M=K\\cdot m=24\\cdot 9=216\\ \\text{cm}^2$.</p>'
                  '<p><b>Felszín.</b> $F=2B+M=48\\sqrt3+216\\approx 299{,}14\\ \\text{cm}^2$.</p>'
                  '<p><b>Térfogat.</b> $V=B\\cdot m=24\\sqrt3\\cdot 9=216\\sqrt3\\approx '
                  '374{,}12\\ \\text{cm}^3$.</p>')),
   abra(SVG_HASAB6, 'Szabályos hatoldalú hasáb: az alapél $a$, a magasság $m$.'),
 ]),

 ("Fordított irányban", [
   '<p>A feladatok jó része nem a képlet behelyettesítését kéri, hanem a <b>fordított</b> '
   'utat: adott térfogatból a magasságot vagy az alapélt. Ilyenkor a képletbe '
   'behelyettesítünk, és <b>egyenletet oldunk meg</b>.</p>',
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy négyzetes hasáb alapéle $6$ cm, térfogata $1080\\ \\text{cm}^3$. Mekkora a '
         'magassága és a felszíne?</p>',
         hid="pelda-forditott-hasab",
         lenyilo=("Megoldás",
                  '<p>Az alaplap területe $B=6^2=36\\ \\text{cm}^2$. A '
                  '$V=B\\cdot m$ képletből</p>'
                  '$$m=\\frac{V}{B}=\\frac{1080}{36}=30\\ \\text{cm}.$$'
                  '<p>Ezután $K=4\\cdot 6=24$ cm, $M=24\\cdot 30=720\\ \\text{cm}^2$, tehát</p>'
                  '$$F=2\\cdot 36+720=792\\ \\text{cm}^2.$$')),
   kviz('Egy felül nyitott, hasáb alakú tartályt kívülről festünk le, az alját is. Melyik '
        'kifejezés adja a festendő területet?',
        ['$B+M$', '$2B+M$', '$M$'], 0,
        jo="✔ Egy alaplap van (a fenék), plusz a palást — a fedőlap hiányzik.",
        nem="✘ Számold össze a lapokat: a tartálynak van feneke és oldalfala, de nincs teteje."),
 ]),

 ("Mértékegységek és nagyságrend", [
   '<p>A térfogat mértékegységei köbegységek, ezért a szomszédos egységek váltószáma nem '
   '$10$ és nem $100$, hanem $1000$:</p>'
   '$$1\\ \\text{m}^3=1000\\ \\text{dm}^3=1\\,000\\,000\\ \\text{cm}^3,\\qquad '
   '1\\ \\text{dm}^3=1\\ \\text{liter}.$$'
   '<p>A terület (és így a felszín) mértékegységeinél a váltószám $100$: '
   '$1\\ \\text{m}^2=100\\ \\text{dm}^2$.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A tartály $2{,}5\\ \\text{m}^3$-es, tehát $250$ liter fér bele.”</i></p>'
         '<p>Nem $250$, hanem <b>$2500$</b> liter: aki így számol, a <b>területek</b> '
         'váltószámával ($100$) dolgozik térfogatnál. A hosszúságnál $1$ m $=10$ dm, a '
         'térfogatnál viszont a $10$-es szorzó <b>háromszor</b> lép be: $10^3=1000$. Itt a '
         'tévedés tízszeres — de aki $\\text{cm}^3$-t néz $\\text{m}^3$-nek, az már '
         'milliószorosat téved, és ez a betonrendelésnél az árban is meglátszik.</p>'),
   kviz('Hány liter fér egy $0{,}75\\ \\text{m}^3$-es tartályba?',
        ['$750$ liter', '$75$ liter', '$7500$ liter'], 0,
        jo="✔ 1 m³ = 1000 dm³ = 1000 liter, tehát 0,75 · 1000 = 750.",
        nem="✘ 1 m³ = 1000 liter (nem 100 és nem 10 000), ezért 0,75 m³ = 750 liter."),
   GY(FGY + "#alap-7", "A 7–16", FGY + "#kozep-5", "K 5–12"),
   brief('<b>Prizma:</b> Kívülről és belülről is megmérted a kristályt. Most jön a '
         'kérdés, amit a Zónában a leggyakrabban feltesznek: <b>mi van benne?</b> Ehhez '
         'el kell metszeni — és tudni kell, milyen alakzatot kapunk.', outro=True),
 ]),
]

# ===================================================================== B3

B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A kristály belsejét nem lehet megnézni anélkül, hogy elmetszenénk. '
         'A metszés viszont nem véletlenszerű: attól függ, <b>hogyan áll a metszősík</b>, '
         'hogy háromszöget, téglalapot vagy éppen szabályos hatszöget kapunk. Két kérdésre '
         'kell tudnod válaszolni: <b>milyen alakzat</b> a metszet, és <b>mekkora</b> a '
         'területe.'),
   '<p>Ez a témakör harmadik tanulási célja. A felmérőkön rendszeresen szerepel — általában '
   'úgy, hogy a metszet fajtáját megadják, és a területet kell kiszámolni.</p>',
 ]),

 ("Mi a síkmetszet", [
   doboz("definicio", "Síkmetszet",
         '<p>Egy test <b>síkmetszete</b> a test és egy sík közös része. Konvex <b>poliédernél</b> '
         '— ha a sík a test belsejébe is behatol — ez mindig <b>síksokszög</b>: a határa '
         'azokból a szakaszokból áll, amelyek mentén a metszősík a test lapjait metszi. (Ha a '
         'sík csak érinti a testet, a közös rész lehet pont, szakasz vagy egy egész lap.)</p>'
         '<p>A metszet csúcsai tehát ott vannak, ahol a metszősík a test <b>éleit</b> '
         'döfi.</p>',
         hid="def-sikmetszet"),
   '<p>Ebből következik egy hasznos szabály: a metszet <b>annyi oldalú</b>, ahány lapját a '
   'sík ténylegesen elmetszi — egy lapból legfeljebb egy oldal származhat. A négyzetes '
   'hasábnak hat lapja van, ezért a metszete legfeljebb hatszög; a hatoldalú hasábnak nyolc '
   'lapja van, ott a metszet akár nyolcszög is lehet.</p>',
 ]),

 ("Alappal párhuzamos metszet", [
   doboz("tetel", "Az alappal párhuzamos metszet",
         '<p>Ha a metszősík <b>párhuzamos az alaplappal</b>, a metszet az alaplappal '
         '<b>egybevágó</b> sokszög — függetlenül attól, milyen magasan metszünk.</p>'
         '<p>Ez a hasáb sajátossága: minden alappal párhuzamos keresztmetszete ugyanakkora. (A gúlánál ez '
         'másképp lesz — ott a metszet <b>hasonló</b>, de kisebb.)</p>',
         hid="tetel-hasab-parhuzamos-metszet"),
   abra(SVG_METSZET_PARH, 'Az alaplappal párhuzamos metszet egybevágó az alaplappal.'),
 ]),

 ("Átlós metszetek", [
   '<p>Az <b>átlós metszet</b> az a metszet, amelyet két <b>nem szomszédos oldalélen</b> '
   'átmenő sík ad. Ez a sík az alaplapot annak egyik <b>átlója</b> mentén metszi.</p>',
   doboz("tetel", "Az egyenes hasáb átlós metszete",
         '<p><b>Egyenes</b> hasáb átlós metszete <b>téglalap</b>, amelynek</p>'
         '<ul>'
         '<li>egyik oldala az alaplap megfelelő <b>átlója</b> ($d$),</li>'
         '<li>a másik oldala a hasáb <b>magassága</b> ($m$),</li>'
         '</ul>'
         '<p>ezért a területe $T=d\\cdot m$.</p>'
         '<p>Ferde hasábnál a metszet általában csak paralelogramma — a kikötés tehát nem '
         'elhagyható.</p>',
         hid="tetel-hasab-atlos-metszet"),
   abra(SVG_METSZET_ATLOS, 'A négyzetes hasáb átlós metszete az $AC$ és az $A_1C_1$ átlón át.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A hasáb metszete olyan, mint az alaplapja — hatszög alapú hasábnál mindig '
         'hatszög."</i></p>'
         '<p>Csak az <b>alappal párhuzamos</b> metszetre igaz. Egyenes hasábnál az átlós metszet '
         '<b>téglalap</b>, egy ferdén álló sík metszete pedig sem az alaplappal nem '
         'egybevágó, sem nem téglalap. Metszet előtt mindig azt kérdezd: <b>hogyan áll a '
         'sík?</b> — nem azt, hogy milyen a test.</p>'),
 ]),

 ("A metszet területének kiszámítása", [
   '<p>A számolás mindig két lépés: (1) melyik alaplapi <b>átló</b> mentén metszünk, '
   '(2) az átló és a magasság szorzata. Az első lépés a nehezebb, mert a szabályos '
   'sokszögeknek <b>többféle hosszúságú</b> átlójuk van. A szabályos hatszögnél a hosszabb '
   'átló a szemközti csúcsokat köti össze, és átmegy a középponton, ezért a köréírt kör '
   'átmérője: $2R=2a$. A rövidebb átló egy csúcsot hagy ki, és a beírt kör átmérőjével '
   'egyenlő: $2\\rho=a\\sqrt3$.</p>',
   abra(SVG_HATSZOG_ATLOK, 'A szabályos hatszögben a köréírt kör sugara $R=a$, az apotéma '
        '$\\rho=\\frac{a\\sqrt3}{2}$. Innen a hosszabb átló $2R=2a$, a rövidebb pedig '
        '$2\\rho=a\\sqrt3$.'),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos hatoldalú hasáb alapéle $5$ cm, magassága $7$ cm. Mekkora a '
         'kétféle átlós metszetének a területe?</p>',
         hid="pelda-hatszog-metszet",
         lenyilo=("Megoldás",
                  '<p>A szabályos hatszögnek <b>kétféle</b> átlója van:</p>'
                  '<ul>'
                  '<li>a <b>hosszabb</b> a szemközti csúcsokat köti össze, és átmegy a '
                  'középponton: $d_1=2R=2a=10$ cm;</li>'
                  '<li>a <b>rövidebb</b> egy csúcsot hagy ki, és a beírt kör átmérője: '
                  '$d_2=2\\rho=a\\sqrt3=5\\sqrt3\\approx 8{,}66$ cm.</li>'
                  '</ul>'
                  '<p>A két metszet területe ezért</p>'
                  '$$T_1=d_1\\cdot m=10\\cdot 7=70\\ \\text{cm}^2,\\qquad '
                  'T_2=d_2\\cdot m=5\\sqrt3\\cdot 7=35\\sqrt3\\approx 60{,}62\\ \\text{cm}^2.$$'
                  '<p>Ugyanaz a test, két különböző metszet — a feladat szövegéből mindig ki '
                  'kell derülnie, melyikről van szó.</p>')),
   doboz("erdekesseg", "Csak érdekesség",
         '<p>A kockát el lehet metszeni úgy is, hogy a metszet <b>szabályos hatszög</b> '
         'legyen: a metszősík hat élt döf, mindegyiket a felezőpontjában. Ez az egyik '
         'legszebb példa arra, hogy a metszet alakját a <b>sík állása</b> dönti el, '
         'nem a testé.</p>'),
   kviz('Egy szabályos <b>hatoldalú</b> hasáb alapéle $5$ cm. Melyik lehet az átlós '
        'metszetének az <b>alaplapban fekvő</b> oldala?',
        ['$10$ cm vagy $5\\sqrt3$ cm — kétféle átló van',
         'Csak $10$ cm, mert az átló mindig a szemközti csúcsokat köti össze',
         'Csak $5$ cm, mert az átló egyenlő az oldallal'], 0,
        jo="✔ A szabályos hatszögnek kétféle hosszúságú átlója van: a hosszabb 2a = 10 cm, "
           "a rövidebb a√3 = 5√3 cm.",
        nem="✘ Rajzold be a hatszög átlóit! Kétféle hosszúságút találsz: az egyik átmegy a "
            "középponton (2a), a másik egy csúcsot hagy ki (a√3)."),
   GY(FGY + "#alap-17", "A 17–20", FGY + "#kozep-13", "K 13–16"),
   brief('<b>Prizma:</b> Az oszlopos kristályokkal végeztünk: ismered a felszínüket, a '
         'térfogatukat és a belsejüket is. A Zóna mélyén viszont olyan képződmények nőnek, '
         'amelyek <b>egyetlen pontba futnak össze</b>. Más test, más képlet — és egy '
         'meglepően makacs $\\frac13$. Jön a <b>gúla</b>.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-hasab.html",
     cim="A hasáb — amikor a sokszög elindul a térbe",
     cim_tiszta="A hasáb",
     alcim="A hasáb keletkezése, fajtái, hálója, valamint a lapátló és a testátló.",
     chip=KUL + " · 5/11", szakaszok=B1,
     elozo=("feladatok-terelemek.html", "Feladatok — térelemek és poliéderek"),
     kovetkezo=("tananyag-hasab-felszin-terfogat.html", "A hasáb felszíne és térfogata")),
 lap(**T, fajl="tananyag-hasab-felszin-terfogat.html",
     cim="A hasáb felszíne és térfogata",
     cim_tiszta="A hasáb felszíne és térfogata",
     alcim="A palást a hálóból, a térfogat képlete, fordított feladatok és a köbös "
           "mértékegységek.",
     chip=KUL + " · 6/11", szakaszok=B2,
     elozo=("tananyag-hasab.html", "A hasáb"),
     kovetkezo=("tananyag-hasab-sikmetszetek.html", "A hasáb síkmetszetei")),
 lap(**T, fajl="tananyag-hasab-sikmetszetek.html",
     cim="A hasáb síkmetszetei",
     cim_tiszta="A hasáb síkmetszetei",
     alcim="Az alappal párhuzamos metszet, az átlós metszet és a metszet területének "
           "kiszámítása.",
     chip=KUL + " · 7/11", szakaszok=B3,
     elozo=("tananyag-hasab-felszin-terfogat.html", "A hasáb felszíne és térfogata"),
     kovetkezo=(FGY, "Feladatok — a hasáb")),
]
for u in KI:
    print("✓", os.path.basename(u))
