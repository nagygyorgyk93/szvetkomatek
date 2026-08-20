# -*- coding: utf-8 -*-
"""3e/01 — A altema: terelemek (A1), meroleges es szogek (A2), poliederek (A3),
az alaplap (A4). Mentor: Prizma. Kuldetes: A Kristalypara Kristalyok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import (svg_terelem, svg_hasab, svg_gula, svg_halo, svg_platoni,
                         svg_sikidom, svg_haromszog)

T = dict(tagozat="3e", mappa="01-poliederek", temakor="Poliéderek")
FGY = "feladatok-terelemek.html"
KUL = "A Kristálypára Kristályok"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, simplify, atan, pi, deg, N
E = []
def chk(n, g, w, tur=1e-12):
    """A várt értéket FÜGGETLENÜL számoljuk ki; itt csak az egyezést ellenőrizzük."""
    elteres = simplify(g - w)
    ok = (elteres == 0) or abs(float(N(elteres))) <= tur
    if not ok:
        E.append((n, g, w))
# A2 — a kocka testátlójának hajlásszöge az alaplappal (a = 4)
a4 = 4
chk("kocka-lapatlo", sqrt(2)*a4, sqrt(a4**2 + a4**2))
chk("kocka-testatlo", sqrt(3)*a4, sqrt((sqrt(2)*a4)**2 + a4**2))
chk("kocka-szog", deg(atan(a4/(sqrt(2)*a4))), deg(atan(sqrt(2)/2)))
chk("kocka-szog-fok", N(deg(atan(sqrt(2)/2))), 35.264389682754654, 1e-9)
# A4 — a nevezetes síkidomok
chk("egyenlo-oldalu-m", 6*sqrt(3)/2, 3*sqrt(3))
chk("egyenlo-oldalu-T", 6**2*sqrt(3)/4, 9*sqrt(3))
chk("trapez-T", (10 + 6)*4/2, 32)
chk("rombusz-T", 12*8/2, 48)
chk("hatszog-T", 6*(4**2*sqrt(3)/4), 24*sqrt(3))
chk("hatszog-rho", 4*sqrt(3)/2, 2*sqrt(3))
chk("hatszog-Kro", 6*4*(2*sqrt(3))/2, 24*sqrt(3))
chk("30-60-90", 5*sqrt(3), sqrt(10**2 - 5**2))
chk("45-45-90", 7*sqrt(2), sqrt(7**2 + 7**2))
# A1/A2 — a kockára tett állítások vektoros ellenőrzése (a csúcsok: A(0,0,0), B(1,0,0),
# C(1,1,0), D(0,1,0), és a fölöttük lévő A1…D1 z = 1 magasságban)
from sympy import Matrix
KOCKA = dict(A=(0,0,0), B=(1,0,0), C=(1,1,0), D=(0,1,0),
             A1=(0,0,1), B1=(1,0,1), C1=(1,1,1), D1=(0,1,1))
def el(p, q):
    return Matrix(KOCKA[q]) - Matrix(KOCKA[p])
def helyzet(e1, e2):
    """'metszo' | 'parhuzamos' | 'kitero' — két él kölcsönös helyzete."""
    u, v = el(*e1), el(*e2)
    w = Matrix(KOCKA[e2[0]]) - Matrix(KOCKA[e1[0]])
    if u.cross(v).norm() == 0:
        return "parhuzamos"
    # egy síkban vannak-e: a három vektor vegyes szorzata nulla
    return "metszo" if Matrix([[*u], [*v], [*w]]).det() == 0 else "kitero"
chk_h = lambda n, g, w: E.append((n, g, w)) if g != w else None
chk_h("AB-CC1", helyzet(("A","B"), ("C","C1")), "kitero")
chk_h("AB-C1D1", helyzet(("A","B"), ("C1","D1")), "parhuzamos")
chk_h("AB-A1B1", helyzet(("A","B"), ("A1","B1")), "parhuzamos")
chk_h("AB-BC", helyzet(("A","B"), ("B","C")), "metszo")
chk_h("BC-DD1", helyzet(("B","C"), ("D","D1")), "kitero")
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_HELYZETEK = svg_terelem("dofes", w=330, h=225)
SVG_BENNE = svg_terelem("benne", w=330, h=210)
SVG_PARH = svg_terelem("parhuzamos", w=330, h=215)
SVG_KETSIK = svg_terelem("ket-sik", w=340, h=235)
SVG_PSIKOK = svg_terelem("parhuzamos-sikok", w=330, h=225)
SVG_KOCKA = svg_hasab("negyzet", a=1.0, m=1.0, w=320, h=270,
                      leiras="Kocka a nyolc csúcs jelölésével: A, B, C, D az alaplapon, "
                             "A1, B1, C1, D1 a fedőlapon")
SVG_MEROLEGES = svg_terelem("meroleges", w=340, h=235)
SVG_HAJLAS = svg_terelem("hajlasszog", w=340, h=235)
SVG_DIEDER = svg_terelem("dieder", w=340, h=245)
SVG_TESTATLO = svg_hasab("negyzet", a=1.0, m=1.0, testatlo=True, w=320, h=270,
                         feliratok={"D": "d"},
                         leiras="A kocka testátlója az A csúcsból a C1 csúcsba")
SVG_PLATONI = svg_platoni(w=560, h=140)
SVG_HALO_J = svg_halo("kocka", w=300, h=230,
                      leiras="Kereszt alakú kiterítés: ebből összehajtható a kocka")
SVG_HALO_R = svg_halo("kocka", hibas=True, w=300, h=230,
                      leiras="Hat négyzetből álló alakzat, amelyből NEM hajtható össze kocka")
SVG_HALO_H = svg_halo("hasab", n=6, w=330, h=250)
SVG_HAROMSZOG = svg_haromszog(csucsok=[(0, 0), (4, 0), (2, 3.4641)],
                              cimkek=("A", "B", "C"), oldalcimkek=("a", "a", "a"),
                              magassag=2, w=320, h=235,
                              leiras="Egyenlő oldalú háromszög a C csúcsból az AB oldalra "
                                     "állított magassággal")
SVG_TRAPEZ = svg_sikidom("trapez", w=330, h=210)
SVG_HATSZOG = svg_sikidom("sokszog", n=6, w=300, h=250)

# ===================================================================== A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A Karantén-Zónában a folyosók éjszakánként átrendeződnek. '
         'Tegnap még egy terem volt ott, ma egy hetven fokban megdőlt kristálylap. '
         'Mielőtt bármit kiszámolnánk — felszínt, térfogatot, energiasűrűséget —, '
         'tudnunk kell, <b>mi hol van</b>: mikor találkozik két folyosó, mikor nem '
         'találkoznak soha, és mi az, ami egyetlen síkot rögzít. Ez a kadét első '
         'térbeli reflexe.'),
   '<p>Az eddigi geometriád <b>síkgeometria</b> volt: minden alakzat egyetlen lapon feküdt. '
   'A térben két egyenes viszonyában megjelenik egy <b>harmadik</b> eset is, ami a síkban '
   'nem létezik — és pontosan ez az, amit a legtöbben elrontanak.</p>'
   '<p><b>Jelölés.</b> A pontokat nagybetűvel ($A$, $B$, $P$), az egyeneseket kisbetűvel '
   '($a$, $b$, $p$), a síkokat görög betűvel ($\\alpha$, $\\beta$) jelöljük.</p>',
 ]),

 ("Miből épül a tér", [
   '<p>A geometria <b>alapfogalmakkal</b> indul: a <b>pont</b>, az <b>egyenes</b> és a '
   '<b>sík</b> fogalmát nem definiáljuk, hanem az <b>axiómák</b> — bizonyítás nélkül '
   'elfogadott állítások — írják le, hogyan viselkednek. Minden további állítást ezekből '
   'vezetünk le.</p>',
   doboz("tetel", "A tér három alapaxiómája",
         '<ol>'
         '<li>Bármely két különböző pontra <b>pontosan egy</b> egyenes illeszkedik.</li>'
         '<li>Ha egy egyenes <b>két</b> pontja illeszkedik egy síkra, akkor az egyenes '
         '<b>minden</b> pontja illeszkedik arra a síkra.</li>'
         '<li>Ha két különböző síknak van <b>közös pontja</b>, akkor a közös pontjaik halmaza '
         '<b>pontosan egy egyenes</b> (a metszésvonaluk).</li>'
         '<li>Bármely három, <b>nem egy egyenesre eső</b> pontra pontosan egy sík illeszkedik.</li>'
         '</ol>'
         '<p>A második axióma az, amiért a vonalzó működik: ha a vonalzó élének mindkét végpontja '
         'az asztallapon van, akkor a teljes él a lapon fekszik.</p>',
         hid="tetel-axiomak"),
 ]),

 ("Mi határoz meg egy síkot", [
   doboz("tetel", "Négy eset — és mindegyik pontosan egy síkot ad",
         '<p>Egy sík <b>egyértelműen</b> meg van határozva, ha adott</p>'
         '<ul>'
         '<li><b>három</b> pont, amelyek <b>nem</b> esnek egy egyenesre;</li>'
         '<li>egy egyenes és egy rá <b>nem</b> illeszkedő pont;</li>'
         '<li><b>két metsző</b> egyenes;</li>'
         '<li><b>két párhuzamos</b> (nem egybeeső) egyenes.</li>'
         '</ul>'
         '<p>Az első eset maga is <b>axióma</b> (lásd fent); a másik három ebből következik, mert '
         'mindegyikből kiolvasható három olyan pont, amely nincs egy egyenesen. Az egy '
         'egyenesre eső (<b>kollineáris</b>) pontok tehát nem határoznak meg síkot: a rajtuk '
         'átmenő sík az egyenes körül szabadon elfordítható.</p>',
         hid="tetel-sikmeghatarozas"),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Miért nem billeg a háromlábú fényképezőállvány, és miért billeg a négylábú asztal? '
         'Mert három talppont — bármilyen hosszúak is a lábak — <b>mindig egy síkba esik</b>, '
         'és ez a sík hozzáilleszthető a padlóéhoz: az állvány addig dől, amíg mindhárom láb '
         'földet ér. Négy pont viszont általában <b>nem</b> esik egy síkba, ezért ha az egyik '
         'láb egy hajszállal rövidebb, az asztal billeg.</p>'),
   kviz('Igaz-e, hogy <b>bármely</b> három pont pontosan egy síkot határoz meg?',
        ['Nem: ha egy egyenesre esnek, végtelen sok sík megy át rajtuk',
         'Igen, bármely három pont esetén',
         'Nem: három pont mindig végtelen sok síkot határoz meg'], 0,
        jo="✔ A kikötés nem díszítés: ha a három pont egy egyenesre esik, a rajtuk átmenő sík "
           "az egyenes körül szabadon elfordítható, mint a lap a könyv gerince körül.",
        nem="✘ Próbáld ki három olyan ponttal, amely egy egyenesre esik. Hány sík fektethető "
            "rájuk?"),
 ]),

 ("Két egyenes a térben", [
   '<p>A síkban két egyenesnek két lehetősége volt: metszették egymást, vagy párhuzamosak '
   'voltak. A térben megjelenik egy <b>harmadik</b> eset.</p>',
   doboz("definicio", "Kitérő egyenesek",
         '<p>Két egyenes <b>kitérő</b>, ha nincs közös pontjuk, <b>és</b> nincs olyan sík, '
         'amelyben mindkettő benne van.</p>'
         '<p>Ezzel szemben két egyenes <b>párhuzamos</b>, ha <b>egy síkban</b> vannak, és nincs '
         'közös pontjuk — vagy ha egybeesnek.</p>'
         '<p>A térben tehát két egyenes vagy <b>metsző</b> (egy közös pont), vagy '
         '<b>párhuzamos</b>, vagy <b>kitérő</b>.</p>',
         hid="def-kitero"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Ennek a két folyosónak nincs közös pontja — akkor párhuzamosak, és a '
         'zárórendszer ugyanúgy állítható be mindkettőn."</i></p>'
         '<p>A síkban ez igaz lenne. A térben <b>nem</b>: a kitérő egyeneseknek sincs közös '
         'pontjuk. A párhuzamossághoz az is kell, hogy a két egyenes <b>egy síkban</b> legyen. '
         'Aki csak a közös pont hiányát nézi, minden kitérő élpárt párhuzamosnak hisz.</p>'),
   abra(SVG_KOCKA, 'A kockán mind a három eset megtalálható. Az <span class="math inline">\\(AB\\)</span> '
        'és a <span class="math inline">\\(BC\\)</span> él metsző, az <span class="math inline">\\(AB\\)</span> '
        'és a <span class="math inline">\\(A_1B_1\\)</span> párhuzamos, az '
        '<span class="math inline">\\(AB\\)</span> és a <span class="math inline">\\(CC_1\\)</span> pedig kitérő.'),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Az $ABCDA_1B_1C_1D_1$ kockában — ahol az $A_1$ csúcs az $A$ fölött, a $B_1$ a $B$ '
         'fölött van, és így tovább — milyen helyzetű az $AB$ és a $CC_1$ él?</p>',
         hid="pelda-kocka-elei",
         lenyilo=("Megoldás",
                  '<p>Közös pontjuk nincs: az $AB$ szakasz az alaplapon fekszik, a $CC_1$ élnek '
                  'pedig egyedül a $C$ pontja van az alaplapon, és $C$ nincs rajta az '
                  '$AB$ egyenesen.</p>'
                  '<p>Van-e olyan sík, amely mindkettőt tartalmazza? Tegyük fel, hogy van '
                  'ilyen $S$ sík. Akkor $S$ tartalmazza az $A$, $B$ és $C$ pontot, ezek '
                  'viszont nincsenek egy egyenesen, tehát $S$ <b>csak</b> az $ABCD$ sík '
                  'lehet. De a $C_1$ csúcs nincs az $ABCD$ síkon, így az $S$ nem '
                  'tartalmazhatja a $CC_1$ élt — ellentmondás.</p>'
                  '<p>Nincs tehát ilyen sík: a két él <b>kitérő</b>.</p>')),
   kviz('Az $ABCDA_1B_1C_1D_1$ kockában milyen helyzetű az $AB$ és a $C_1D_1$ él?',
        ['Párhuzamos', 'Kitérő', 'Metsző'], 0,
        jo="✔ Nem szomszédos lapon vannak, mégis párhuzamosak: mindkettő benne fekszik az "
           "ABC₁D₁ átlós síkban, és nincs közös pontjuk.",
        nem="✘ Az, hogy két él nincs ugyanazon a lapon, még nem jelenti, hogy kitérő. Keress "
            "olyan síkot, amelyben mindkettő benne van — az átlós síkokat is nézd meg."),
 ]),

 ("Egyenes és sík, sík és sík", [
   '<p>Egy egyenes és egy sík háromféleképpen helyezkedhet el egymáshoz képest: az egyenes '
   '<b>illeszkedik</b> a síkra (benne fekszik), <b>párhuzamos</b> vele (nincs közös pontjuk), '
   'vagy <b>döfi</b> — pontosan egy közös pontjuk van, ez a <b>döféspont</b>.</p>',
   abra(SVG_HELYZETEK, 'Az $a$ egyenes döfi az $\\alpha$ síkot: egyetlen közös pontjuk a $P$ döféspont.'),
   abra(SVG_BENNE, 'Az $a$ egyenes az $\\alpha$ síkban fekszik: minden pontja közös.'),
   abra(SVG_PARH, 'Az $a$ egyenes párhuzamos az $\\alpha$ síkkal: nincs közös pontjuk.'),
   '<p>Két sík pedig vagy <b>egybeesik</b>, vagy <b>párhuzamos</b> (nincs közös pontjuk), '
   'vagy <b>metszi</b> egymást — ilyenkor a közös részük a harmadik axióma szerint egy '
   '<b>egyenes</b>, a metszésvonal.</p>',
   abra(SVG_KETSIK, 'Két metsző sík és a $p$ metszésvonaluk.'),
   abra(SVG_PSIKOK, 'Két párhuzamos sík: nincs közös pontjuk.'),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A szoba két szemközti fala párhuzamos sík; a fal és a padló metsző, a '
         'metszésvonaluk az a vonal, ahol a szegélyléc fut. A sátorcövek pedig <b>döfi</b> a '
         'talaj síkját: a föld fölött és alatt is folytatódik, egyetlen közös pontja a '
         'talajszinttel a döféspont.</p>'),
   GY(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Prizma:</b> A térképed megvan: tudod, mi hol van. A következő lépés a '
         '<b>mérés</b> — mert a kristálylapok nem csak elhelyezkednek, hanem <b>szöget is '
         'zárnak be</b>, és a visszavert energia iránya ezen múlik. A térben viszont a '
         'szöget másképp kell mérni, mint a papíron.', outro=True),
 ]),
]

# ===================================================================== A2

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A kristálylap nem véletlenszerűen veri vissza az energiát: a '
         'visszaverődés irányát a lap <b>hajlásszöge</b> dönti el. Egy fokot tévedsz, és a '
         'sugár a szomszéd folyosóra érkezik. Ebben az egységben megtanuljuk, mit jelent '
         'pontosan, hogy egy egyenes <b>merőleges egy síkra</b>, és hogyan mérünk szöget a '
         'térben — mert itt nem elég ránézésre becsülni.'),
   'Két új szöget vezetünk be: az <b>egyenes és a sík</b> hajlásszögét, valamint <b>két sík</b> '
   'szögét. Mindkettőt visszavezetjük arra, amit már tudsz: két <i>egyenes</i> szögére.',
 ]),

 ("Mikor merőleges egy egyenes a síkra", [
   '<p>A „merőleges a lapra” hétköznapi kifejezés — csakhogy mihez képest merőleges? Egy '
   'síkban végtelen sok egyenes fut, és a síkot ferdén döfő egyenes is lehet merőleges '
   'közülük <b>az egyikre</b>.</p>',
   doboz("tetel", "A merőlegesség feltétele",
         '<p>Egy egyenes <b>pontosan akkor</b> merőleges egy síkra, ha a síknak <b>két '
         'metsző</b> egyenesére merőleges.</p>'
         '<p>Ekkor a síknak a döfésponton átmenő <b>minden</b> egyenesére merőleges — de a '
         'feltétel ellenőrzéséhez elég kettő, feltéve, hogy azok <b>metszik</b> egymást.</p>',
         hid="tetel-meroleges-feltetel"),
   abra(SVG_MEROLEGES, 'Az $a$ egyenes merőleges a síkra, mert merőleges a síkban fekvő, '
        'egymást metsző $b$ és $c$ egyenesre.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Ez a tartórúd merőleges a padló egyik vonalára, tehát merőleges a padlóra. '
         'A szerkezet stabil."</i></p>'
         '<p>Nem az. Dönts meg egy ceruzát az asztalon úgy, hogy az asztal lapján lévő '
         'egyik vonalra merőleges maradjon — ez könnyen megy, mégsem áll függőlegesen. '
         '<b>Egy</b> egyenesre való merőlegesség kevés; <b>két metsző</b> egyenes kell. '
         'Ha a két egyenes párhuzamos, az sem elég: azok együtt nem „feszítik ki” a síkot.</p>'),
   kviz('Az $a$ egyenes merőleges a síkban fekvő $b$ egyenesre. Következik-e ebből, hogy '
        '$a$ merőleges a síkra?',
        ['Nem — ehhez a sík két metsző egyenesére kell merőlegesnek lennie',
         'Igen, egy egyenes elég',
         'Igen, de csak ha $b$ átmegy a döfésponton'], 0,
        jo="✔ Egyetlen egyenes nem rögzíti a sík irányát; két metsző egyenes viszont igen.",
        nem="✘ Egy ferde egyenes is lehet merőleges a sík egyetlen egyenesére. A feltétel: "
            "KÉT METSZŐ egyenesre merőleges."),
 ]),

 ("Egyenes és sík hajlásszöge", [
   doboz("definicio", "Hajlásszög",
         '<p>Egy pont <b>merőleges vetülete</b> a síkon az a pont, ahol a pontból a síkra '
         'bocsátott merőleges döfi a síkot. Legyen az $a$ egyenes olyan, hogy döfi az '
         '$\\alpha$ síkot, de nem merőleges rá. Vetítsük az $a$ egyenes minden pontját '
         'merőlegesen az $\\alpha$ síkra: a vetület egy $a\'$ egyenes, amely átmegy a '
         'döfésponton. Az $a$ egyenes és az $\\alpha$ sík <b>hajlásszöge</b> az $a$ és az '
         '$a\'$ által bezárt hegyesszög.</p>'
         '<p>Két külön eset: ha $a \\perp \\alpha$, a hajlásszög $90^\\circ$; ha $a$ '
         'párhuzamos a síkkal vagy benne fekszik, a hajlásszög $0^\\circ$.</p>',
         hid="def-hajlasszog"),
   abra(SVG_HAJLAS, 'Az $A$ döféspont a síkban van, a $P$ pont merőleges vetülete pedig $P\'$. '
        'A hajlásszög az $AP$ egyenes és az $AP\'$ vetület szöge, $\\varphi$.'),
   '<p>A vetület azért fontos, mert <b>derékszögű háromszöghöz</b> juttat: az $APP\'$ '
   'háromszögben a $P\'$ csúcsnál derékszög van, tehát a szög szögfüggvénnyel számolható.</p>',
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Mekkora szöget zár be az $a = 4$ cm élű kocka testátlója az alaplappal?</p>',
         hid="pelda-testatlo-szog",
         lenyilo=("Megoldás",
                  '<p>A testátló az $A$ csúcsból a $C_1$ csúcsba fut. Merőleges vetülete az '
                  'alaplapra az $AC$ <b>lapátló</b>, hiszen a $CC_1$ él merőleges az '
                  'alaplapra. A keresett szög tehát a $C_1AC$ háromszögben van, amelyben a '
                  '$C$ csúcsnál derékszög van.</p>'
                  '<p>Itt $AC = a\\sqrt2 = 4\\sqrt2 \\approx 5{,}66$ cm és $CC_1 = a = 4$ cm, ezért</p>'
                  '$$\\operatorname{tg}\\varphi = \\frac{CC_1}{AC} = \\frac{4}{4\\sqrt2} '
                  '= \\frac{\\sqrt2}{2} \\approx 0{,}7071,$$'
                  '<p>ahonnan $\\varphi \\approx 35^\\circ 16\' \\approx 35{,}26^\\circ$.</p>'
                  '<p>Figyeld meg: általánosan is '
                  '$\\operatorname{tg}\\varphi = \\frac{a}{a\\sqrt2} = \\frac{\\sqrt2}{2}$ — az '
                  'élhossz kiesik, tehát <b>minden</b> kocka testátlója ugyanekkora szöget zár '
                  'be az alaplappal.</p>')),
   abra(SVG_TESTATLO, 'A kocka testátlója és a vetülete, az $AC$ lapátló.'),
 ]),

 ("Két sík szöge — a diéder", [
   doboz("definicio", "Diéder és lapszöge",
         '<p>Két olyan félsík, amelynek közös a határegyenese, <b>diédert</b> alkot: a közös '
         'egyenes a diéder <b>éle</b>, a két félsík pedig a diéder két <b>lapja</b>.</p>'
         '<p>A diéder <b>lapszöge</b>: vegyünk az élen egy pontot, és mindkét lapban '
         'húzzunk belőle az élre <b>merőleges</b> félegyenest — ezek szöge a lapszög. '
         'Az érték nem függ attól, melyik pontot választottuk.</p>'
         '<p>Két metsző sík szögén a keletkező négy diéder közül a <b>nem tompaszögűt</b> értjük — '
         'vagyis a hegyesszögűt, merőleges síkok esetén pedig a derékszögűt. Két sík '
         '<b>merőleges</b>, ha ez a szög $90^\\circ$.</p>',
         hid="def-dieder"),
   abra(SVG_DIEDER, 'A diéder éle a $p$ egyenes; a lapszöget az élre merőlegesen mérjük.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Ráteszem a szögmérőt a lapra, ahogy éppen esik — a lapszög úgyis '
         'ugyanannyi."</i></p>'
         '<p>Nem ugyanannyi. Ha a félegyenesek <b>nem merőlegesek az élre</b>, a mért érték a '
         'valódi lapszögnél kisebb és nagyobb is lehet — $0^\\circ$ és $180^\\circ$ között '
         'bármi kijöhet. A tetőn ezért nem mindegy, milyen irányban mérve olvasod le a lejtő '
         'szögét.</p>'),
   kviz('Hol mérjük a diéder lapszögét?',
        ['Az élen felvett pontból, mindkét lapban az élre merőlegesen',
         'Bárhol, ahol a két lap találkozik',
         'Az éllel párhuzamos irányban'], 0,
        jo="✔ Csak az élre merőleges félegyenesek adják a lapszöget — és így az érték független "
           "a pont választásától.",
        nem="✘ Ha a félegyenesek ferdén állnak az élhez képest, a mért szög változik. "
            "A definícióban ezért szerepel a merőlegesség."),
 ]),

 ("Távolságok a térben", [
   '<p>A <b>pont és sík távolsága</b> a pontból a síkra bocsátott <b>merőleges szakasz</b> '
   'hossza (ha a pont a síkban van, a távolság $0$). Ez a legrövidebb út: minden más '
   'összekötő szakasz hosszabb, mert a derékszögű háromszögben az átfogó a leghosszabb '
   'oldal.</p>'
   '<p>Ugyanígy értelmezzük egy pont és egy egyenes távolságát is. <b>Két párhuzamos sík '
   'távolsága</b> az egyik sík bármely pontjának a másik síktól mért távolsága — és ez az '
   'érték nem függ attól, melyik pontot választottuk. Hasonlóan értelmezzük egy síkkal '
   'párhuzamos egyenes és a sík távolságát.</p>',
   doboz("erdekesseg", "Ez lesz a testek magassága",
         '<p>A hasáb, a gúla és a csonkagúla <b>magassága</b> mindig ilyen merőleges '
         'távolság: a gúlánál a csúcs és az alaplap síkjának távolsága, a hasábnál a két '
         'alaplap síkjának távolsága. Ezért nem mindegy, hogy egy ferde testnél az '
         '<i>oldalélt</i> vagy a <i>magasságot</i> használod — a képletekben mindig a '
         'merőleges távolság szerepel.</p>'),
   GY(FGY + "#alap-6", "A 6–10", FGY + "#kozep-4", "K 4–7"),
   brief('<b>Prizma:</b> Mérni tudsz. Most nézzük meg, milyen <b>testeket</b> zárnak be ezek '
         'a lapok — és miért van a természetben pontosan <b>öt</b> tökéletesen szabályos '
         'kristályforma. Nem több, nem kevesebb. Ez nem megfigyelés, hanem bizonyítható.',
         outro=True),
 ]),
]

# ===================================================================== A3

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A Kristálypára nem gömbökben csapódik ki, hanem <b>lapos, éles '
         'formákban</b> — és a legtisztább kristályok tökéletesen szabályosak. A '
         'meglepetés az, hogy ilyen tökéletes testből összesen <b>pontosan öt</b> '
         'létezik. Nem azért, mert nem találtunk többet: mert nem is létezhet több. '
         'Ezt ma be is fogjuk látni.'),
   'Ebben az egységben a testeket <b>osztályozzuk</b>: mi számít poliédernek, mit jelent a '
   'konvexitás, és mitől lesz egy test szabályos. A számolás a következő egységekben jön — '
   'de a fogalmak nélkül ott csak képletet másolnánk.',
 ]),

 ("Mi a poliéder", [
   doboz("definicio", "Poliéder",
         '<p>A <b>poliéder</b> (soklapú test) olyan test, amelyet véges sok <b>síksokszög</b> '
         'határol. Ezek a sokszögek a test <b>lapjai</b>, a lapok oldalai az <b>élei</b>, a '
         'lapok csúcsai a test <b>csúcsai</b>.</p>'
         '<p>Minden él pontosan <b>két</b> lap közös oldala, és minden csúcsban legalább '
         '<b>három</b> lap találkozik.</p>',
         hid="def-polieder"),
   '<p>A henger, a kúp és a gömb <b>nem</b> poliéder: a határoló felületük nem áll csupa '
   'síksokszögből — a palástjuk görbült, az alaplapjuk pedig kör. Ezek a <b>forgástestek</b> — '
   'a következő témakör anyaga.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A kősó kockákban, a kvarc hatszögű oszlopokban, a gyémánt oktaéderes formában '
         'kristályosodik. A kristály lapjai azért síkok, mert az atomok szabályos rácsban '
         'helyezkednek el — a poliéder tehát nem emberi találmány, hanem az anyag szerkezetének a '
         'következménye.</p>'),
 ]),

 ("Konvex és nem konvex testek", [
   doboz("definicio", "Konvex test",
         '<p>Egy test <b>konvex</b>, ha bármely két pontját összekötő szakasz teljes '
         'egészében a testhez tartozik.</p>'
         '<p>Poliédernél ezzel egyenértékű: a test minden lapjának síkja két féltérre vágja a '
         'teret, és a test teljes egészében az egyik <b>zárt</b> féltérben marad (a lap maga '
         'a határoló síkban van).</p>',
         hid="def-konvex"),
   '<p>A kocka konvex; a hasáb és a gúla pontosan akkor konvex, ha az alaplapja konvex '
   'sokszög. Nem konvex például az L alakú épülettömb — ez is hasáb, de az alaplapja nem '
   'konvex: a két szárának végpontját összekötő szakasz kilép a testből. A továbbiakban — ha külön nem '
   'mondjuk — <b>konvex</b> poliéderekkel foglalkozunk.</p>',
 ]),

 ("Az öt szabályos test — és miért csak öt", [
   doboz("definicio", "Szabályos poliéder",
         '<p>Egy poliéder <b>szabályos</b>, ha</p>'
         '<ul>'
         '<li>minden lapja <b>egybevágó szabályos sokszög</b>, <b>és</b></li>'
         '<li>minden csúcsában <b>ugyanannyi</b> lap találkozik.</li>'
         '</ul>'
         '<p>A két feltételnek <b>egyszerre</b> kell teljesülnie; egyik sem következik a '
         'másikból. A szabályos poliédereket ezenfelül <b>konvexnek</b> is tekintjük.</p>',
         hid="def-szabalyos-polieder"),
   abra(SVG_PLATONI, 'Az öt szabályos poliéder — más néven platóni testek.'),
   doboz("tetel", "Pontosan öt konvex szabályos poliéder van",
         '<p>A bizonyítás gondolatmenete meglepően rövid. Egy csúcsban legalább <b>három</b> lap '
         'találkozik, és a csúcsnál összefutó <b>lapok szögeinek</b> összege <b>kisebb kell '
         'legyen $360^\\circ$-nál</b>: ha pontosan $360^\\circ$, a lapok síkba terülnek, ha '
         'több, akkor nem tudnak konvex csúcsot zárni. (Vigyázz: ezek a lapok saját szögei, '
         'nem a lapszögek — azok két lap hajlásszögei.) Nézzük végig, milyen szabályos '
         'sokszög lehet lap:</p>'
         '<ul>'
         '<li><b>szabályos háromszög</b> ($60^\\circ$): 3 lap ($180^\\circ$) → <b>tetraéder</b>, '
         '4 lap ($240^\\circ$) → <b>oktaéder</b>, 5 lap ($300^\\circ$) → <b>ikozaéder</b>; '
         '6 lap már $360^\\circ$ — nem megy;</li>'
         '<li><b>négyzet</b> ($90^\\circ$): 3 lap ($270^\\circ$) → <b>kocka</b>; 4 lap már '
         '$360^\\circ$;</li>'
         '<li><b>szabályos ötszög</b> ($108^\\circ$): 3 lap ($324^\\circ$) → '
         '<b>dodekaéder</b>; 4 lap már $432^\\circ$;</li>'
         '<li><b>szabályos hatszög</b> ($120^\\circ$): már 3 lap is $360^\\circ$ — és '
         'minden ennél több oldalú sokszögnél még rosszabb a helyzet.</li>'
         '</ul>'
         '<p>Öt eset maradt, és mind az öt esetben tényleg meg is szerkeszthető a test — '
         'esetenként pontosan egy. Több tehát nem lehet.</p>',
         hid="tetel-ot-szabalyos-test"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Minden lapja szabályos háromszög — akkor ez egy szabályos test, és a '
         'szimmetria-protokoll alkalmazható rá."</i></p>'
         '<p>Ellenpélda: ragassz össze két szabályos tetraédert egy-egy lapjuknál. Az így '
         'kapott testnek <b>mind a hat lapja</b> egybevágó szabályos háromszög — mégsem '
         'szabályos test, mert a két „hegyes” csúcsában <b>3</b>, a másik három csúcsában '
         'viszont <b>4</b> lap találkozik. A definíció második feltétele bukik el.</p>'
         '<p>Így működik a jó ellenpélda: egyetlen példa elég ahhoz, hogy egy „nyilvánvaló” '
         'állítást megdöntsünk.</p>'),
   kviz('Igaz-e: ha egy poliéder minden lapja egybevágó szabályos sokszög, akkor a poliéder '
        'szabályos?',
        ['Nem — a csúcsokban is ugyanannyi lapnak kell találkoznia',
         'Igen, a lapok szabályossága elég',
         'Igen, de csak háromszöglapok esetén'], 0,
        jo="✔ A két összeragasztott tetraéder pont ilyen ellenpélda: hat szabályos háromszöglap, "
           "mégsem szabályos test.",
        nem="✘ Gondolj a két összeragasztott tetraéderre: minden lapja szabályos háromszög, "
            "de az egyik csúcsában 3, a másikban 4 lap fut össze."),
   doboz("erdekesseg", "Csak érdekesség — az Euler-formula",
         '<p>Bármely konvex poliéderre a csúcsok ($C$), élek ($E$) és lapok ($L$) száma között '
         'fennáll, hogy</p>'
         '$$C - E + L = 2.$$'
         '<table class="tt-table">'
         '<tr><th>Test</th><th>lap alakja</th><th>lap/csúcs</th><th>$C$</th><th>$E$</th>'
         '<th>$L$</th><th>$C-E+L$</th></tr>'
         '<tr><td>tetraéder</td><td>háromszög</td><td>3</td><td>4</td><td>6</td><td>4</td><td>2</td></tr>'
         '<tr><td>kocka</td><td>négyzet</td><td>3</td><td>8</td><td>12</td><td>6</td><td>2</td></tr>'
         '<tr><td>oktaéder</td><td>háromszög</td><td>4</td><td>6</td><td>12</td><td>8</td><td>2</td></tr>'
         '<tr><td>dodekaéder</td><td>ötszög</td><td>3</td><td>20</td><td>30</td><td>12</td><td>2</td></tr>'
         '<tr><td>ikozaéder</td><td>háromszög</td><td>5</td><td>12</td><td>30</td><td>20</td><td>2</td></tr>'
         '</table>'
         '<p><b>A tantervünk ezt nem kéri számon</b> — de gyönyörű összefüggés, és jó '
         'önellenőrzés, ha egy test adatait számolod.</p>'),
 ]),

 ("Hálók — a test síkba kiterítve", [
   '<p>Vágjuk fel a poliédert néhány éle mentén — úgy, hogy a lapok egyben maradjanak —, és '
   'terítsük ki őket egy síkba, átfedés nélkül: a kapott összefüggő síkidom a test '
   '<b>hálója</b>. A háló <b>területe</b> pontosan a test felszíne — a '
   'következő egységek felszínképletei mind innen származnak.</p>',
   abra(SVG_HALO_J, 'A kocka egyik hálója: hat négyzet kereszt alakban.'),
   abra(SVG_HALO_H, 'Az egyenes hasáb hálója: két egybevágó alaplap és a palást, ami egyenes '
        'hasábnál egyetlen téglalap.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Hat négyzet — akkor ez kocka hálója.”</i></p>'
         '<p>Nem feltétlenül. Hat négyzetből <b>35</b> különböző, élben csatlakozó alakzat rakható '
         'ki (az egymásba forgatható vagy tükrözhető változatokat egynek számítva), és ezek '
         'közül csak <b>11</b> hajtható kockává. A többinél a hajtogatás során két lap '
         'egymásra kerül.</p>'),
   abra(SVG_HALO_R, 'Ez az alakzat is hat négyzetből áll, mégsem hajtható össze kockává: '
        'a hajtogatás során két lap egymásra kerülne.'),
   kviz('Hány négyzetből áll a kocka hálója, és elég-e ennyi?',
        ['Hat — de nem minden hatnégyzetes alakzat hajtható kockává',
         'Hat, és bármely hatnégyzetes alakzat jó',
         'Nyolc, a csúcsok száma miatt'], 0,
        jo="✔ A kockának hat lapja van, de az elrendezés is számít: a 35 lehetséges alakzatból 11 hajtható kockává.",
        nem="✘ A lapok száma valóban hat — de próbáld gondolatban összehajtani a lépcsős "
            "elrendezést: két lap egymásra kerül."),
   GY(FGY + "#alap-11", "A 11–15", FGY + "#kozep-8", "K 8–10"),
   brief('<b>Prizma:</b> A formákat felismered, a hálót látod. Egyetlen dolog hiányzik a '
         'számoláshoz — és ez az, amin a kadétok fele elvérzik: az <b>alaplap területe</b>. Minden '
         'test-képletben ott áll egy $B$, és ha azt elrontod, a legszebb térfogatképlet is '
         'rossz számot ad. Fegyverzet-ellenőrzés következik.', outro=True),
 ]),
]

# ===================================================================== A4

GEO = "../../1e/05-geometria/"
HAS = "../../1e/08-hasonlosag/"

A4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Minden test-képletben ott áll egy $B$ — az alaplap területe. A '
         'kadétok többsége nem a térfogatképletet rontja el, hanem az alaplapot: '
         'összekeveri a háromszög oldalát a magasságával, a trapéz szárát a magasságával, '
         'vagy a szabályos hatszögnél elfelejti, hogy hat háromszögből áll. Ez az egység a '
         '<b>fegyverzet-ellenőrzés</b>: mindaz a síkgeometria, amire a hasábnál, a gúlánál '
         'és a csonkagúlánál szükséged lesz.'),
   'Új anyag itt nincs — de a következő nyolc egység ezen áll vagy bukik. Ha valamelyik '
   'képlet bizonytalan, most nézd meg az <a href="' + GEO + 'index.html">1e geometria</a> '
   'megfelelő leckéjét, ne majd a dolgozat közben.',
 ]),

 ("Miért az alaplapon múlik minden", [
   '<p>A következő egységek képletei ilyen alakúak: a hasáb térfogata $V = B\\cdot H$, a '
   'gúláé $V = \\frac{B\\cdot H}{3}$, a felszín pedig $F = 2B + M$, illetve $F = B + M$. '
   'Itt $B$ az <b>alaplap területe</b>, $H$ a <b>test magassága</b>, $M$ pedig a '
   '<b>palást</b> (az oldallapok együttes) területe. Mindegyik képletben ott van a $B$.</p>'
   '<p>Ha a testfeladat alaplapja szabályos háromszög, akkor a feladat fele valójában '
   '„számítsd ki egy szabályos háromszög területét”. Ezért érdemes ezt a néhány képletet '
   'készségszinten tudni.</p>',
   doboz("tetel", "A képlettár",
         '<table class="tt-table">'
         '<tr><th>Síkidom</th><th>Terület</th><th>Amire figyelj</th></tr>'
         '<tr><td>háromszög</td><td>$T=\\dfrac{a\\,h_a}{2}$</td>'
         '<td>$h_a$ az $a$ oldalhoz tartozó <b>magasság</b></td></tr>'
         '<tr><td>egyenlő oldalú (szabályos) háromszög</td><td>$T=\\dfrac{a^2\\sqrt3}{4}$</td>'
         '<td>a magassága $h=\\dfrac{a\\sqrt3}{2}$</td></tr>'
         '<tr><td>négyzet</td><td>$T=a^2$</td><td>átlója $d=a\\sqrt2$</td></tr>'
         '<tr><td>téglalap</td><td>$T=ab$</td><td>átlója $d=\\sqrt{a^2+b^2}$</td></tr>'
         '<tr><td>paralelogramma</td><td>$T=a\\,h_a$</td>'
         '<td>$h_a$ az $a$ oldalhoz tartozó magasság, nem a másik oldal!</td></tr>'
         '<tr><td>trapéz</td><td>$T=\\dfrac{(a+b)\\,h}{2}$</td>'
         '<td>$a$ és $b$ a párhuzamos <b>alapok</b>, $c$ és $d$ a szárak; $h$ az alapok '
         '<b>merőleges</b> távolsága</td></tr>'
         '<tr><td>rombusz, deltoid</td><td>$T=\\dfrac{e\\,f}{2}$</td>'
         '<td>$e$ és $f$ az <b>átlók</b>; minden merőleges átlójú négyszögre igaz</td></tr>'
         '<tr><td>szabályos sokszög</td><td>$T=\\dfrac{K\\,r}{2}$</td>'
         '<td>$K$ a kerület, $r$ az apotéma (a beírt kör sugara, lásd lentebb)</td></tr>'
         '</table>',
         hid="tetel-teruletkepletek"),
 ]),

 ("Háromszögek", [
   '<p>Az általános képlet $T=\\frac{a\\,h_a}{2}$, ahol $h_a$ az $a$ oldalhoz tartozó '
   'magasság: a szemközti csúcsból az $a$ oldal egyenesére bocsátott merőleges szakasz. A '
   'testfeladatokban viszont a leggyakoribb az <b>egyenlő oldalú</b> — más néven '
   '<b>szabályos</b> — háromszög: ez az alaplapja a szabályos háromoldalú hasábnak és '
   'gúlának.</p>',
   abra(SVG_HAROMSZOG, 'Az egyenlő oldalú háromszög magassága felezi az alapot, ezért a '
        'Pitagorasz-tétel adja: $h=\\sqrt{a^2-\\left(\\frac a2\\right)^2}=\\frac{a\\sqrt3}{2}$.'),
   doboz("tetel", "Az egyenlő oldalú háromszög",
         '<p>Ha az oldal $a$, akkor</p>'
         '$$h=\\frac{a\\sqrt3}{2},\\qquad T=\\frac{a^2\\sqrt3}{4}.$$'
         '<p>A magasság az oldallal, a terület az oldal <b>négyzetével</b> arányos. A $4$-es '
         'nevező onnan jön, hogy a $T=\\frac{a\\,h}{2}$ képletbe $h=\\frac{a\\sqrt3}{2}$-t '
         'helyettesítjük: a felezés még egyszer feleződik. A magasság levezetése: felezi az '
         'alapot, majd '
         '<a href="' + HAS + 'tananyag-haromszogek-hasonlosaga.html#tetel-pitagorasz">'
         'Pitagorasz-tétel</a>.</p>',
         hid="tetel-egyenlo-oldalu"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Az oldal $6$, a $\\sqrt3$ ott van a képletben — a terület tehát $3\\sqrt3$.”</i></p>'
         '<p>A $3\\sqrt3$ a <b>magasság</b> ($\\frac{6\\sqrt3}{2}$), nem a terület. A terület '
         '$\\frac{6^2\\sqrt3}{4}=9\\sqrt3\\approx 15{,}59$. A két képlet hasonlít, de az '
         'egyikben $a$, a másikban $a^2$ áll — és a $\\sqrt3$ nevezője is más. '
         'Gyors ellenőrzés: a magasság <b>hosszúság</b> (cm), a terület <b>négyzetes</b> '
         'mennyiség (cm²). Ha a válaszod cm-ben jött ki, nem területet számoltál.</p>'),
   kviz('Mekkora a $6$ cm oldalú szabályos háromszög <b>magassága</b>?',
        ['$3\\sqrt3\\approx 5{,}20$ cm', '$9\\sqrt3\\approx 15{,}59$ cm', '$6\\sqrt3\\approx 10{,}39$ cm'], 0,
        jo="✔ $h=\\frac{a\\sqrt3}{2}=\\frac{6\\sqrt3}{2}=3\\sqrt3$.",
        nem="✘ A $9\\sqrt3$ a TERÜLET ($\\frac{a^2\\sqrt3}{4}$). A magasság $\\frac{a\\sqrt3}{2}=3\\sqrt3$."),
 ]),

 ("Négyszögek", [
   '<p>A négyszögek közül a testfeladatokban a <b>téglalap</b> (téglatest alaplapja), a '
   '<b>négyzet</b> (szabályos négyoldalú hasáb és gúla alaplapja) és a <b>trapéz</b> (a '
   'csonkagúla oldallapja!) fordul elő a leggyakrabban.</p>',
   abra(SVG_TRAPEZ, 'A trapéz magassága a két <b>párhuzamos</b> oldal merőleges távolsága — '
        'nem a szár.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Az egyenlő szárú trapéz párhuzamos oldalai $10$ és $4$, a szára $5$ — a '
         'területe tehát $\\frac{(10+4)\\cdot 5}{2}=35$."</i></p>'
         '<p>A képletben <b>magasság</b> szerepel, nem szár. A magasságot itt ki kell '
         'számolni: a szár vetülete az alapon $\\frac{10-4}{2}=3$, ezért '
         '$h=\\sqrt{5^2-3^2}=4$, és a terület $\\frac{(10+4)\\cdot 4}{2}=28$. Ugyanez a hiba '
         'a paralelogrammánál is: ott sem a másik <i>oldal</i> kell, hanem a magasság.</p>'),
   '<p>Emlékeztetőül: a trapéz tulajdonságai és a középvonala az '
   '<a href="' + GEO + 'tananyag-negyszogek.html#tetel-trapez">1e négyszögek</a> leckéjében '
   'vannak.</p>',
   kviz('Egy egyenlő szárú trapéz párhuzamos oldalai $10$ cm és $4$ cm, a szára $5$ cm. '
        'Mekkora a területe?',
        ['$28\\ \\text{cm}^2$', '$35\\ \\text{cm}^2$', '$20\\ \\text{cm}^2$'], 0,
        jo="✔ Előbb a magasság: a szár vetülete (10−4)/2 = 3, ezért h = √(25−9) = 4. "
           "Így T = (10+4)·4/2 = 28.",
        nem="✘ A képletbe a MAGASSÁG megy, nem a szár. A magasság a szárból Pitagorasz-tétellel "
            "jön ki: a vetület (10−4)/2 = 3, tehát m = √(25−9) = 4."),
 ]),

 ("Szabályos sokszögek", [
   doboz("definicio", "Apotéma és köréírt sugár",
         '<p>A szabályos sokszög <b>apotémája</b> ($r$) a középpont és egy oldal '
         'távolsága — vagyis a <b>beírt kör</b> sugara. A <b>köré írt kör</b> sugara ($R$) a '
         'középpont és egy csúcs távolsága. Mindig $r &lt; R$.</p>',
         hid="def-apotema"),
   abra(SVG_HATSZOG, 'A szabályos hatszög hat egyenlő oldalú háromszögre bomlik; itt '
        '$R=a$, az apotéma pedig $r=\\frac{a\\sqrt3}{2}$.'),
   doboz("tetel", "A szabályos sokszög területe",
         '<p>A középpontból a csúcsokba húzott szakaszok a sokszöget $n$ egybevágó háromszögre '
         'bontják; mindegyik alapja $a$, hozzá tartozó magassága pedig éppen az apotéma, '
         '$r$. Ezért</p>'
         '$$T=n\\cdot\\frac{a\\,r}{2}=\\frac{K\\,r}{2},$$'
         '<p>ahol $K=na$ a kerület. A <b>szabályos hatszög</b> külön figyelmet érdemel: '
         'ott a középponti szög $60^\\circ$, ezért a hat háromszög <b>egyenlő oldalú</b>, '
         'és így $R=a$. Emiatt</p>'
         '$$T_{6}=6\\cdot\\frac{a^2\\sqrt3}{4}=\\frac{3a^2\\sqrt3}{2},\\qquad '
         'r=\\frac{a\\sqrt3}{2}.$$',
         hid="tetel-szabalyos-sokszog"),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Mekkora a $4$ cm oldalú szabályos hatszög területe? Számold ki <b>két '
         'különböző úton</b>, és hasonlítsd össze az eredményt.</p>',
         hid="pelda-hatszog",
         lenyilo=("Megoldás",
                  '<p><b>1. út — hat egyenlő oldalú háromszög.</b></p>'
                  '$$T=6\\cdot\\frac{4^2\\sqrt3}{4}=6\\cdot 4\\sqrt3=24\\sqrt3\\approx 41{,}57\\ \\text{cm}^2.$$'
                  '<p><b>2. út — kerület és apotéma.</b> Itt $K=6\\cdot4=24$ cm és '
                  '$r=\\frac{4\\sqrt3}{2}=2\\sqrt3$ cm, ezért</p>'
                  '$$T=\\frac{K\\,r}{2}=\\frac{24\\cdot 2\\sqrt3}{2}=24\\sqrt3\\approx 41{,}57\\ \\text{cm}^2.$$'
                  '<p>Ugyanaz az eredmény — és ez nem véletlen: a második képletet éppen '
                  'ugyanabból a háromszögekre bontásból vezettük le. A kétféle számolás '
                  'tehát a <b>számolási</b> hibát szűri ki, nem a módszertanit — de erre '
                  'nagyon jó.</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A méhsejt, a csavarfej, a csempézés és a kvarckristály keresztmetszete is hatszög. '
         'Miért? Mert a szabályos háromszög, a négyzet és a szabályos hatszög az a három '
         'szabályos sokszög, amellyel a sík <b>hézagmentesen</b> kirakható — és a három közül '
         '<b>azonos kerület mellett</b> a hatszög fogja körbe a legnagyobb területet.</p>'),
 ]),

 ("A két nevezetes derékszögű háromszög", [
   '<p>A testfeladatok többségében a hiányzó adat egy derékszögű háromszögből jön ki, és '
   'kétféle háromszög fordul elő újra meg újra. Érdemes az <b>arányukat</b> fejből tudni.</p>',
   doboz("tetel", "A két nevezetes arány",
         '<p><b>$45^\\circ$–$45^\\circ$–$90^\\circ$</b> (a négyzet fele): a befogók egyenlők, '
         'az átfogó</p>'
         '$$c=a\\sqrt2\\qquad(\\text{arány } 1:1:\\sqrt2).$$'
         '<p><b>$30^\\circ$–$60^\\circ$–$90^\\circ$</b> (az egyenlő oldalú háromszög fele): '
         'a $30^\\circ$-kal szemközti befogó az átfogó fele,</p>'
         '$$a=\\frac{c}{2},\\qquad b=\\frac{c\\sqrt3}{2}\\qquad(\\text{arány } 1:\\sqrt3:2).$$',
         hid="tetel-nevezetes-haromszogek"),
   '<p>Ezekkel egy lépésben megkapod azt, amihez különben szögfüggvényre lenne szükség: a '
   'négyzet átlója és a kocka lapátlója $a\\sqrt2$ — mindkettő a $45^\\circ$-os arányból. A '
   'kocka <b>testátlója</b> $a\\sqrt3$: ez már nem a nevezetes arányokból jön, hanem a '
   'Pitagorasz-tétel <b>kétszeri</b> alkalmazásából (előbb a lapátló, aztán a testátló).</p>',
   GY(FGY + "#alap-16", "A 16–22", FGY + "#kozep-11", "K 11–14 N 1–4"),
   brief('<b>Prizma:</b> A fegyverzet rendben. Innentől minden alaplapot ki tudsz számolni — '
         'és ez pontosan az a tudás, amire a következő blokkban szükség lesz. Emeljük ki a '
         'sokszöget a síkból: jön az <b>első test</b>, a hasáb.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-terelemek.html",
     cim="Pont, egyenes, sík — a tér játékszabályai",
     cim_tiszta="Pont, egyenes, sík — a tér játékszabályai",
     alcim="A tér axiómái, a sík meghatározása, valamint az egyenesek, egyenes és sík, "
           "illetve két sík kölcsönös helyzete.",
     chip=KUL + " · 1/11", szakaszok=A1,
     elozo=("index.html", "Poliéderek"),
     kovetkezo=("tananyag-meroleges-es-szog.html", "Merőlegesség és szögek a térben")),
 lap(**T, fajl="tananyag-meroleges-es-szog.html",
     cim="Merőlegesség és szögek a térben",
     cim_tiszta="Merőlegesség és szögek a térben",
     alcim="Az egyenes és a sík merőlegességének feltétele, a hajlásszög, a diéder lapszöge "
           "és a térbeli távolságok.",
     chip=KUL + " · 2/11", szakaszok=A2,
     elozo=("tananyag-terelemek.html", "Pont, egyenes, sík"),
     kovetkezo=("tananyag-poliederek.html", "Poliéderek és szabályos poliéderek")),
 lap(**T, fajl="tananyag-poliederek.html",
     cim="Poliéderek és szabályos poliéderek",
     cim_tiszta="Poliéderek és szabályos poliéderek",
     alcim="A poliéder fogalma, a konvexitás, az öt szabályos test és a hálók.",
     chip=KUL + " · 3/11", szakaszok=A3,
     elozo=("tananyag-meroleges-es-szog.html", "Merőlegesség és szögek a térben"),
     kovetkezo=("tananyag-alaplap.html", "Az alaplap")),
 lap(**T, fajl="tananyag-alaplap.html",
     cim="Az alaplap — amin minden testszámítás áll",
     cim_tiszta="Az alaplap",
     alcim="Síkidomok területe: háromszögek, négyszögek, szabályos sokszögek és a két "
           "nevezetes derékszögű háromszög.",
     chip=KUL + " · 4/11", szakaszok=A4,
     elozo=("tananyag-poliederek.html", "Poliéderek és szabályos poliéderek"),
     kovetkezo=(FGY, "Feladatok — térelemek és poliéderek")),
]
for u in KI:
    print("✓", os.path.basename(u))
