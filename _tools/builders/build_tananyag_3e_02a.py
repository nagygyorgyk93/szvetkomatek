# -*- coding: utf-8 -*-
"""3e/02 — A altema: forgastestek (A1), a henger es elemei (A2),
a henger felszine es terfogata (A3). Mentor: Meduza.
Kuldetes: Az Atalakulas Kamraja. Jeloles-kanon: _JELOLESEK.md (r, H, s, B, M)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import (svg_forgatas, svg_osszetett, svg_henger, svg_halo,
                         svg_sikidom, svg_kup, svg_gomb)

T = dict(tagozat="3e", mappa="02-forgastestek", temakor="Forgástestek")
FGY = "feladatok-henger.html"
KUL = "Az Átalakulás Kamrája"
POLI = "../01-poliederek/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, pi, simplify, N, symbols, solve, Eq
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x = symbols("x", positive=True)
V_h = lambda r, H: r**2*pi*H
F_h = lambda r, H: 2*r**2*pi + 2*r*pi*H
# A1 — ugyanaz a 3x4-es téglalap két tengely körül
chk("A1-negy-korul", V_h(3, 4), 36*pi)
chk("A1-harom-korul", V_h(4, 3), 48*pi)
chk("A1-arany", V_h(4, 3)/V_h(3, 4), R(4, 3))
# A2 — konzervdoboz címkéje (r = 4, H = 11)
chk("A2-cimke", 2*4*pi*11, 88*pi)
chk("A2-cimke-kozelites", N(88*pi, 8), 276.46015, 1e-4)
# A2 — egyenlő oldalú henger: a tengelymetszet négyzet
chk("A2-eo-tm", 2*5, 10)
# A3 — tartály r = 3 dm, H = 8 dm
chk("A3-V", V_h(3, 8), 72*pi)
chk("A3-V-liter", N(72*pi, 8), 226.19467, 1e-4)
chk("A3-F", F_h(3, 8), 66*pi)
chk("A3-M", 2*3*pi*8, 48*pi)
# A3 — fordított: V = 500π, r = 5 → H
chk("A3-ford-H", solve(Eq(V_h(5, x), 500*pi), x)[0], 20)
# A3 — fordított: F = 150π, H = 10 → r (másodfokú, csak a pozitív gyök)
chk("A3-ford-r", solve(Eq(F_h(x, 10), 150*pi), x)[0], 5)
# A3 — a sugár duplázása négyszerezi a térfogatot
chk("A3-duplazas", V_h(2*x, 8)/V_h(x, 8), 4)
# A3 — mértékegység
chk("A3-dm3-liter", 1, 1)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_F_TEGLALAP = svg_forgatas("teglalap", w=430, h=250)
SVG_F_HAROMSZOG = svg_forgatas("haromszog", w=430, h=250)
SVG_F_FELKOR = svg_forgatas("felkor", w=430, h=250)
SVG_F_TRAPEZ = svg_forgatas("trapez", w=430, h=250)
SVG_KUPKUP = svg_osszetett("kup-kup", w=300, h=290,
    leiras="Derékszögű háromszög az átfogója körül forgatva: két kúp közös alaplappal")
SVG_HENGER = svg_henger(alkoto=True, tengely=True, w=310, h=280,
    leiras="Egyenes henger: alapkörök, palást, alkotó, tengely és magasság")
SVG_HENGER_TM = svg_henger(tengelymetszet=True, magassag=True, w=310, h=270,
    leiras="A henger tengelymetszete téglalap")
SVG_HENGER_PM = svg_henger(parhuzamos_metszet=True, sugar=False, magassag=False,
    w=300, h=270, leiras="A tengelyre merőleges metszet kör")
SVG_HALO_HENGER = svg_halo("henger", w=340, h=280)
SVG_KUP_TM = svg_kup(tengelymetszet=True, alkoto=False, w=300, h=280,
    leiras="A kúp tengelymetszete egyenlő szárú háromszög")
SVG_GOMB_FO = svg_gomb(w=270, h=250,
    leiras="A gömb minden tengelymetszete főkör")

# ===================================================================== A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Az Átalakulás Kamrájában a Kristálypára már nem szögletesen '
         'csapódik ki — <b>pörög</b>. És ami pörög, az gömbölyű nyomot hagy: hengert, '
         'kúpot, gömböt. A Kamra tartályai, tölcsérei és gömbszelencéi mind így '
         'készültek. Mielőtt bármit kiszámolnánk, értsük meg a <b>keletkezésüket</b>: '
         'melyik lapos formából mi lesz, ha megpörgetjük.'),
   '<p>Az előző témakörben (<a href="' + POLI + 'index.html">poliéderek</a>) minden '
   'testet <b>lapok</b> határoltak. Most olyan testek '
   'jönnek, amelyek felülete <b>görbe</b>: nem lehet őket sokszögekre bontani. Közös '
   'bennük, hogy mindegyik egy <b>síkidom megforgatásával</b> keletkezik — ezért hívjuk '
   'őket <b>forgástesteknek</b>.</p>'
   '<p>A jó hír: a görbült felület nem tesz nehezebbé semmit. A képletekben ugyanaz a $B$ '
   '(alapterület) és $H$ (magasság) szerepel, mint a hasábnál és a gúlánál — csak az '
   'alaplap most <b>kör</b>.</p>',
 ]),

 ("Mi a forgástest", [
   doboz("definicio", "Forgástest",
         '<p>Vegyünk egy <b>síkidomot</b> és a síkjában egy <b>egyenest</b> (ez lesz a '
         '<b>forgástengely</b>). Ha a síkidomot a tengely körül teljesen körbeforgatjuk, '
         'a bejárt pontok halmaza egy <b>forgástest</b>.</p>'
         '<p>A forgatás közben a síkidom minden pontja <b>körpályán</b> mozog; a kör '
         'síkja merőleges a tengelyre, a középpontja pedig a tengelyen van.</p>',
         hid="def-forgastest"),
   '<p>Ebből a definícióból két dolog rögtön következik, és mindkettőre szükségünk lesz:</p>'
   '<ul>'
   '<li>a tengelyen fekvő pontok <b>helyben maradnak</b> — ezért lesz a kúpnak csúcsa;</li>'
   '<li>a tengelytől $d$ távolságra lévő pont egy $d$ sugarú kört ír le — ezért kör '
   'minden, a tengelyre <b>merőleges</b> metszet.</li>'
   '</ul>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A fazekaskorongon a hüvelykujj a tengelytől mért <b>távolságot</b> állítja '
         'be — a korong pörgése a többit elvégzi. Ugyanez az elve az <b>esztergapadnak</b>: '
         'a munkadarab forog, a kés csak a profilt vágja ki. Ezért olyan olcsó ipari '
         'szempontból minden forgásszimmetrikus alkatrész — csavar, tengely, palack —, '
         'és ezért drága, ami nem az.</p>'),
 ]),

 ("Melyik síkidomból mi lesz", [
   '<p>Négy alapesetet érdemes fejből tudni. Mindegyiknél figyelj arra, hogy a tengely '
   '<b>hol</b> van — ez dönti el, mi keletkezik.</p>',
   abra(SVG_F_TEGLALAP, 'A <b>téglalap</b> az egyik oldala körül forgatva <b>hengert</b> '
        'ad: a tengellyel párhuzamos oldal lesz a magasság ($H$), a rá merőleges pedig a '
        'sugár ($r$).'),
   abra(SVG_F_HAROMSZOG, 'A <b>derékszögű háromszög</b> az egyik <b>befogója</b> körül '
        'forgatva <b>kúpot</b> ad: a tengely a magasság ($H$), a másik befogó a sugár '
        '($r$), az átfogó pedig az alkotó ($s$).'),
   abra(SVG_F_FELKOR, 'A <b>félkör</b> az átmérője körül forgatva <b>gömböt</b> ad.'),
   abra(SVG_F_TRAPEZ, 'A <b>derékszögű trapéz</b> a derékszögű szára körül forgatva '
        '<b>csonkakúpot</b> ad: a két párhuzamos oldal a két sugár ($R$ és $r$).'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Mindegy, melyik oldala körül forgatom — ugyanaz a test lesz.”</i></p>'
         '<p><b>Nem mindegy.</b> Vegyünk egy $3\\times4$-es téglalapot:</p>'
         '<ul>'
         '<li>a $4$ egység hosszú oldala körül forgatva $r=3$ és $H=4$, tehát '
         '$V=9\\pi\\cdot4=36\\pi$;</li>'
         '<li>a $3$ egység hosszú oldala körül forgatva $r=4$ és $H=3$, tehát '
         '$V=16\\pi\\cdot3=48\\pi$.</li>'
         '</ul>'
         '<p>A második <b>egyharmadával</b> nagyobb ($48\\pi:36\\pi=4:3$), pedig '
         'ugyanabból a téglalapból lett. Az ok: a sugár <b>négyzetesen</b> számít, a magasság csak lineárisan — ezért '
         'mindig a nagyobb sugarú változat a testesebb.</p>'
         '<p>Ugyanez a háromszögnél: a két befogó körül forgatva a sugár és a magasság '
         '<b>felcserélődik</b>, és két különböző térfogatú kúpot kapsz.</p>'),
   doboz("erdekesseg", "És ha az átfogó körül forgatjuk?",
         '<p>A derékszögű háromszöget az <b>átfogója</b> körül is meg lehet forgatni. '
         'Ekkor nem egy kúp keletkezik, hanem <b>kettő</b>, közös alaplappal '
         'összeragasztva — a közös alapkör sugara az átfogóhoz tartozó <b>magasság</b>.</p>'
         '<p>A közös alapkör sugara az átfogóhoz tartozó <b>magassággal</b> egyenlő '
         '(az ábrán $r$), a két kúp magassága pedig az átfogó két szelete — ezek '
         '<b>általában különbözők</b>, ezért a két kúp sem egybevágó.</p>'
         + abra(SVG_KUPKUP, 'Az átfogó körüli forgatás eredménye: két kúp közös '
                'alaplappal, általában különböző magassággal.'),
         hid="erd-atfogo"),
   kviz('Egy $5\\times8$-as téglalapot megforgatunk. Melyik tengely körül lesz nagyobb a '
        'keletkező henger térfogata?',
        ['Az $5$ egység hosszú oldala körül', 'A $8$ egység hosszú oldala körül',
         'Mindkét esetben ugyanakkora'], 0,
        jo="✔ Az 5-ös oldal körül forgatva a sugár 8 lesz: V = 64π · 5 = 320π. A másik "
           "esetben V = 25π · 8 = 200π. A nagyobb sugár nyer.",
        nem="✘ A sugár négyzetesen számít, ezért a NAGYOBB sugarú változat a nagyobb. Az "
            "5-ös oldal körül forgatva lesz 8 a sugár — az ad 320π-t a 200π ellenében."),
 ]),

 ("Amit minden forgástest tud", [
   '<p>Bármelyik forgástestet nézzük, két metszetfajta mindig ugyanúgy viselkedik. Ez a '
   'két állítás végigkíséri az egész témakört.</p>',
   doboz("tetel", "A tengelyre merőleges metszet",
         '<p>Ha a témakör testeit (henger, kúp, csonkakúp, gömb) a <b>tengelyükre '
         'merőleges</b> síkkal metsszük el, a metszet mindig <b>kör</b> (pontosabban '
         'körlap), és a középpontja a tengelyen van.</p>'
         '<p>Ez közvetlenül a keletkezésből jön: a metszősík magasságában lévő pontok '
         'mind ugyanakkora körpályát írtak le a forgatás közben.</p>',
         hid="tetel-meroleges-metszet"),
   abra(SVG_HENGER_PM, 'A hengert a tengelyére merőlegesen elmetszve az alapkörrel '
        '<b>egybevágó</b> kört kapunk.'),
   doboz("definicio", "Tengelymetszet",
         '<p>A forgástest <b>tengelymetszete</b> az a metszet, amelyet a forgástengelyt '
         '<b>tartalmazó</b> síkkal kapunk. Minden forgástest tengelymetszete '
         '<b>tengelyesen szimmetrikus</b> — a szimmetriatengelye maga a forgástengely.</p>'
         '<table class="tt-table">'
         '<tr><th>Test</th><th>A tengelymetszete</th></tr>'
         '<tr><td>henger</td><td>téglalap ($2r$ széles, $H$ magas)</td></tr>'
         '<tr><td>kúp</td><td>egyenlő szárú háromszög (alapja $2r$, szárai az alkotók)</td></tr>'
         '<tr><td>csonkakúp</td><td>egyenlő szárú trapéz</td></tr>'
         '<tr><td>gömb</td><td><b>főkör</b> — a gömb legnagyobb köre, sugara $R$</td></tr>'
         '</table>',
         hid="def-tengelymetszet"),
   abra(SVG_HENGER_TM, 'A henger tengelymetszete téglalap: az egyik oldala az '
        '<b>átmérő</b> ($2r$), a másik a magasság ($H$).'),
   abra(SVG_KUP_TM, 'A kúp tengelymetszete egyenlő szárú háromszög.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A tengelymetszet is kör, hiszen minden metszet kör.”</i></p>'
         '<p>A <b>tengelyre merőleges</b> metszet kör. A <b>tengelyt tartalmazó</b> '
         'metszet viszont soha nem az: a hengeré téglalap, a kúpé háromszög, a gömbé '
         'pedig kör ugyan, de az a <b>főkör</b> — a lehető legnagyobb, nem akármelyik.</p>'
         '<p>Segít, ha úgy gondolsz rá, hogy a merőleges metszet <b>keresztben</b> vágja '
         'a testet (mint a szalámit), a tengelymetszet pedig <b>hosszában</b> (mint a '
         'kettévágott alma).</p>'),
   kviz('Mi lesz a henger metszete, ha a <b>tengelyét tartalmazó</b> síkkal '
        'metsszük el?',
        ['Téglalap', 'Kör', 'Ellipszis'], 0,
        jo="✔ A tengelymetszet téglalap: az egyik oldala az átmérő (2r), a másik a "
           "magasság (H).",
        nem="✘ Kört a tengelyre MERŐLEGES metszet ad. A tengelyt tartalmazó sík "
            "hosszában vágja a hengert — az eredmény téglalap."),
 ]),

 ("A henger- és a kúpfelület", [
   '<p>Eddig a keletkezés felől néztük a testeket. Van egy másik, precízebb út is, és a '
   'tankönyv ezt használja — érdemes felismerni, ha találkozol vele.</p>',
   doboz("definicio", "Hengerfelület és kúpfelület",
         '<p>Adott egy <b>zárt görbe</b> (a <b>vezérgörbe</b>) és egy egyenes, amely nem '
         'esik a görbe síkjába.</p>'
         '<ul>'
         '<li><b>Hengerfelület:</b> a vezérgörbe minden pontján át az adott egyenessel '
         '<b>párhuzamos</b> egyenest húzunk. Ezek az egyenesek az <b>alkotók</b>.</li>'
         '<li><b>Kúpfelület:</b> a vezérgörbe minden pontját összekötjük egy rögzített, '
         'a görbe síkján kívüli <b>ponttal</b> (a csúccsal).</li>'
         '</ul>'
         '<p>Ha a vezérgörbe <b>kör</b>, <b>körhenger-</b>, illetve '
         '<b>körkúpfelületről</b> beszélünk. A továbbiakban mindig ez az eset szerepel, '
         'ezért a „kör” jelzőt el is hagyjuk.</p>',
         hid="def-hengerfelulet"),
   '<p>A <b>test</b> ebből úgy lesz, hogy a felületet két párhuzamos síkkal (henger), '
   'illetve egy síkkal és a csúccsal (kúp) elmetsszük, és a közbezárt részt tekintjük.</p>'
   '<p>A forgatásos és a vezérgörbés megközelítés ugyanoda vezet, ha az alkotók '
   '<b>merőlegesek</b> az alaplapra — ezek az <b>egyenes</b> testek. Ha nem merőlegesek, '
   '<b>ferde</b> hengert, illetve kúpot kapunk; ezek felszínével és térfogatával nem '
   'foglalkozunk, csak a fogalmat kell felismerned.</p>',
   GY(FGY + "#alap-1", "A 1–4", FGY + "#kozep-1", "K 1–2"),
   brief('<b>Medúza:</b> A fogalmak megvannak. A Kamra legegyszerűbb tartálya a '
         '<b>henger</b> — nézzük meg közelről, mi micsoda rajta, és hogyan lehet '
         'kiteríteni.', outro=True),
 ]),
]

# ===================================================================== A2

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Kamra tartályai mind hengeresek — a párakondenzátortól a '
         'gyűjtőciszternáig. Mielőtt a kapacitásukat számolnánk, nevezzük néven, mi '
         'micsoda rajtuk. Aki nem tudja megkülönböztetni az <b>alkotót</b> a '
         '<b>magasságtól</b>, az a felszínt fogja a térfogat helyére írni.'),
   '<p>Ebben az egységben <b>felépítjük</b> a hengert: megnevezzük az elemeit, és '
   'kiterítjük a felületét. A háló az a lépés, amelyből a felszín képlete egyetlen '
   'mondatban következik majd.</p>',
 ]),

 ("Hogyan keletkezik a henger", [
   '<p>Kétféleképpen is eljuthatunk ugyanahhoz a testhez, és mindkét út hasznos:</p>'
   '<ul>'
   '<li><b>Forgatással:</b> egy <b>téglalapot</b> megforgatunk az egyik oldala körül.</li>'
   '<li><b>Metszéssel:</b> egy hengerfelületet elmetszünk két <b>párhuzamos</b> síkkal, '
   'és a közbezárt részt vesszük.</li>'
   '</ul>'
   '<p>A henger <b>egyenes</b>, ha az alkotói merőlegesek az alaplapokra — a forgatásból '
   'mindig ilyen keletkezik. Ha az alkotók ferdék, <b>ferde</b> hengerről beszélünk; '
   'ilyenkor az alkotó hosszabb a magasságnál. A továbbiakban „henger” mindig egyenes '
   'hengert jelent.</p>',
   abra(SVG_HENGER, 'Az egyenes henger: két egybevágó, párhuzamos <b>alapkör</b>, '
        'közöttük a <b>palást</b>. A tengely (szürke) a két középpontot köti össze.'),
 ]),

 ("A henger elemei", [
   doboz("definicio", "A henger részei",
         '<ul>'
         '<li><b>Alapkörök</b> — a két egybevágó, párhuzamos határoló kör; sugaruk $r$. '
         '<b>Egy</b> alapkör területe a $B=r^2\\pi$ alapterület.</li>'
         '<li><b>Palást</b> — a görbe oldalfelület; területe $M$.</li>'
         '<li><b>Alkotó</b> ($s$) — a két alapkört összekötő, a palástot alkotó szakasz. '
         '<b>Egyenes hengernél $s=H$.</b></li>'
         '<li><b>Tengely</b> — a két alapkör középpontját összekötő szakasz; az őt '
         'tartalmazó egyenes a forgatás tengelye.</li>'
         '<li><b>Magasság</b> ($H$) — a két alapkör síkjának távolsága.</li>'
         '</ul>',
         hid="def-henger"),
   '<p>Az <b>alkotó</b> és a <b>magasság</b> egyenes hengernél ugyanaz a szám. Ne '
   'gondold, hogy ezért fölösleges a két név: a <b>kúpnál</b> és a <b>csonkakúpnál</b> '
   'már élesen különböznek, és ott a legtöbb hiba abból származik, hogy valaki a '
   'kettőt összekeveri. Érdemes már itt szokni a különbségtételt.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Miért hengeres a konzervdoboz, a boiler és a búvárpalack? Két oka van. '
         'Egyrészt adott térfogathoz a henger <b>kevés anyaggal</b> beéri — a gömb '
         'ennél is jobb, de gömb alakú dobozt nem lehet egymásra rakni. Másrészt a '
         'belső nyomás a hengeres falon <b>egyenletesen</b> oszlik el; egy szögletes '
         'tartály éleinél feszültséggyűjtő helyek keletkeznének, és ott szakadna el.</p>'),
 ]),

 ("A henger hálója", [
   '<p>A <b>háló</b> az a síkbeli alakzat, amelyet a test felületének „szétvágásából és '
   'kiterítéséből” kapunk. A hengernél ez a lépés vezet el egyenesen a felszínhez.</p>',
   doboz("tetel", "Az egyenes henger hálója",
         '<p>Vágjuk fel a palástot egyetlen alkotó mentén, és terítsük ki. A palástból '
         '<b>téglalap</b> lesz, amelynek</p>'
         '<ul>'
         '<li>az egyik oldala az alapkör <b>kerülete</b>, azaz $2r\\pi$;</li>'
         '<li>a másik oldala a henger <b>magassága</b>, azaz $H$.</li>'
         '</ul>'
         '<p>A háló tehát egy $2r\\pi\\times H$-es téglalapból és <b>két</b> $r$ sugarú '
         'körből áll.</p>',
         hid="tetel-henger-halo"),
   abra(SVG_HALO_HENGER, 'A henger hálója: a palástból téglalap lesz, amelynek az egyik '
        'oldala az alapkör kerülete ($2r\\pi$).'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A háló téglalapjának oldala az átmérő, tehát $2r$.”</i></p>'
         '<p>A palást a <b>kerület</b> mentén simul rá az alapkörre, nem az átmérő '
         'mentén. A helyes oldalhossz $2r\\pi$ — vagyis nagyjából <b>háromszor</b> '
         'akkora, mint az átmérő.</p>'
         '<p>Ellenőrizd magad egy címkével: ha egy konzervdoboz átmérője $8$ cm, a '
         'címkéje nem $8$ cm hosszú, hanem $8\\pi\\approx25$ cm. Tekerd rá — látni '
         'fogod, hogy a $8$ cm épp csak a doboz harmadát érné körbe.</p>'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy hengeres konzervdoboz alapkörének sugara $4$ cm, magassága $11$ cm. '
         'Mekkora annak a papírcímkének a területe, amely pontosan körbeéri a dobozt?</p>',
         hid="pelda-halo",
         lenyilo=("Megoldás",
                  '<p>A címke a <b>palást</b> kiterítése, tehát téglalap:</p>'
                  '<ul>'
                  '<li>az egyik oldala az alapkör kerülete: $2r\\pi=8\\pi$ cm;</li>'
                  '<li>a másik a magasság: $H=11$ cm.</li>'
                  '</ul>'
                  '<p>A területe ezért</p>'
                  '$$M=8\\pi\\cdot11=88\\pi\\approx276{,}46\\ \\text{cm}^2.$$'
                  '<p>Az alapkörök nem tartoznak hozzá — a címke nem fedi a doboz '
                  'tetejét és alját. Ez a különbség a <b>palást</b> és a <b>felszín</b> '
                  'között, és a feladat szövege mindig eldönti, melyikre van szükség.</p>')),
   kviz('Egy henger alapkörének sugara $6$ cm. Milyen hosszú a hálóban a palástból '
        'kapott téglalapnak az az oldala, amely az <b>alapkörre simult</b>?',
        ['$12\\pi$ cm', '$12$ cm', '$6\\pi$ cm'], 0,
        jo="✔ A palást a kerület mentén simul rá: 2rπ = 12π ≈ 37,70 cm.",
        nem="✘ A 12 cm az ÁTMÉRŐ. A palást kiterítve az alapkör KERÜLETE hosszú: "
            "2rπ = 12π."),
 ]),

 ("Az egyenlő oldalú henger", [
   '<p>Egy elnevezés, amely rendszeresen felbukkan a feladatokban — és amelyet könnyű '
   'félreérteni.</p>',
   doboz("definicio", "Egyenlő oldalú henger",
         '<p>A henger <b>egyenlő oldalú</b>, ha a <b>tengelymetszete négyzet</b>.</p>'
         '<p>A tengelymetszet oldalai az <b>átmérő</b> ($2r$) és a <b>magasság</b> ($H$), '
         'ezért a feltétel pontosan azt jelenti, hogy</p>'
         '$$H=2r.$$',
         hid="def-egyenlo-oldalu-henger"),
   abra(SVG_HENGER_TM, 'Egyenlő oldalú hengernél ez a téglalap éppen négyzet: '
        '$H=2r$.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Egyenlő oldalú, tehát a magasság egyenlő a sugárral: $H=r$.”</i></p>'
         '<p>A tengelymetszet oldala nem a sugár, hanem az <b>átmérő</b>. A helyes '
         'összefüggés $H=2r$ — a magasság az átmérővel egyenlő.</p>'
         '<p>Ez a különbség nem apró: ha $H=r$-rel számolsz, a térfogatod a helyes érték '
         '<b>fele</b> lesz. Gyors ellenőrzés: az egyenlő oldalú henger „álló” alakú '
         '(magasabb, mint amilyen széles)? Nem — pont olyan magas, mint amilyen '
         'széles.</p>'),
   '<p>Az egyenlő oldalú hengernél a felszín és a térfogat is egyetlen adattól függ:</p>'
   '$$F=2r^2\\pi+2r\\pi\\cdot2r=6r^2\\pi,\\qquad V=r^2\\pi\\cdot2r=2r^3\\pi.$$'
   '<p>Ezért az ilyen feladatokban a felszínből vagy a térfogatból <b>egy lépésben</b> '
   'megkapod a sugarat.</p>',
   kviz('Egy egyenlő oldalú henger alapkörének sugara $5$ cm. Mekkora a magassága?',
        ['$10$ cm', '$5$ cm', '$5\\pi$ cm'], 0,
        jo="✔ A tengelymetszet négyzet, tehát H = 2r = 10 cm.",
        nem="✘ A tengelymetszet négyzet: az oldala az ÁTMÉRŐ, ezért H = 2r = 10 cm."),
   GY(FGY + "#alap-5", "A 5–9", FGY + "#kozep-3", "K 3–5"),
   brief('<b>Medúza:</b> A háló ki van terítve, a jelölések a helyükön. Innen a '
         '<b>felszín</b> egyetlen összeadás — és a térfogat sem több egy szorzásnál.',
         outro=True),
 ]),
]

# ===================================================================== A3

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Egy tartályról két dolgot kell tudni: <b>mennyi fér bele</b> és '
         '<b>mennyi anyag kell hozzá</b>. Az első a térfogat, a második a felszín. A '
         'Kamrában ez a két szám külön naplóba megy — aki összekeveri őket, az vagy '
         'kifolyatja a párát, vagy elpazarolja a lemezt.'),
   '<p>A felszín <b>területjellegű</b> mennyiség (cm², m²), a térfogat <b>köbös</b> '
   '(cm³, m³). Ha a végeredményed mértékegysége nem stimmel, nem is kell tovább '
   'ellenőrizned: rossz képletet használtál.</p>',
 ]),

 ("A palást a hálóból", [
   '<p>A palást területét nem kell külön kitalálni — az előző egységben már '
   '<a href="tananyag-henger.html#tetel-henger-halo">kiterítettük</a>. '
   'A palást kiterítve <b>téglalap</b>, az oldalai $2r\\pi$ és $H$, tehát a területe a '
   'kettő szorzata.</p>',
   doboz("tetel", "A henger palástja és felszíne",
         '<p>Az egyenes henger palástjának területe</p>'
         '$$M=2r\\pi\\cdot H.$$'
         '<p>A felszín ehhez a <b>két</b> alapkört adja hozzá:</p>'
         '$$F=2B+M=2r^2\\pi+2r\\pi H=2r\\pi(r+H).$$'
         '<p>A jobb szélső, <b>kiemelt</b> alak a legkényelmesebb: egyetlen szorzás két '
         'szám összegével. Ezt érdemes megjegyezni.</p>',
         hid="tetel-henger-felszin"),
   abra(SVG_HALO_HENGER, 'A felszín a háló összterülete: két kör és egy téglalap.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Felszín = alapkör + palást, tehát $F=r^2\\pi+2r\\pi H$.”</i></p>'
         '<p>A hengernek <b>két</b> alapköre van — egy alul, egy felül. A felszínben '
         'ezért $2r^2\\pi$ áll.</p>'
         '<p><b>Ellenpróba, amikor viszont tényleg csak egy kell:</b> egy nyitott '
         'vödörnél, egy virágcserépnél vagy egy fedél nélküli tartálynál a feladat '
         'kifejezetten mondja, hogy nincs teteje. Ilyenkor $F=r^2\\pi+2r\\pi H$ a helyes. '
         'A képlet tehát nem „szabály”, hanem a <b>szöveg</b> következménye — mindig '
         'olvasd el, mit kell befedni.</p>'),
   kviz('Egy $8$ cm sugarú, $10$ cm magas hengeres <b>doboz</b> teljes felszíne:',
        ['$288\\pi\\ \\text{cm}^2$', '$224\\pi\\ \\text{cm}^2$', '$160\\pi\\ \\text{cm}^2$'], 0,
        jo="✔ F = 2rπ(r + H) = 16π · 18 = 288π cm².",
        nem="✘ A dobozt teljesen bezárjuk, tehát KÉT alapkör kell: "
            "F = 2·64π + 2·8·10π = 128π + 160π = 288π."),
 ]),

 ("A térfogat", [
   '<p>A térfogatnál nincs új gondolat — a hasábnál megismert szabály folytatódik. Ott '
   '$V=B\\cdot H$ volt, és ez minden olyan testre igaz, amelynek a „vízszintes” metszetei '
   'egybevágóak. A henger pontosan ilyen: minden, a tengelyre <b>merőleges</b> metszete '
   'ugyanaz az $r$ sugarú kör.</p>',
   doboz("tetel", "A henger térfogata",
         '$$V=B\\cdot H=r^2\\pi H.$$'
         '<p>Ugyanaz a képlet, mint a '
         '<a href="' + POLI + 'tananyag-hasab-felszin-terfogat.html#tetel-hasab-terfogat">'
         'hasábnál</a> — csak az alaplap most kör. A henger úgy is felfogható, mint egy '
         'hasáb, amelynek az alaplapját egyre több oldalú szabályos sokszögekkel '
         'közelítjük.</p>',
         hid="tetel-henger-terfogat"),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy hengeres tartály alapkörének sugara $3$ dm, magassága $8$ dm. Hány '
         '<b>liter</b> fér bele, és hány négyzetdeciméter lemez kell a gyártásához?</p>',
         hid="pelda-tartaly",
         lenyilo=("Megoldás",
                  '<p><b>Térfogat.</b></p>'
                  '$$V=r^2\\pi H=9\\pi\\cdot8=72\\pi\\ \\text{dm}^3.$$'
                  '<p>Mivel $1\\ \\text{dm}^3=1$ liter, a tartály űrtartalma '
                  '$72\\pi\\approx226{,}19$ liter. (Itt <b>indokolt</b> a közelítés: a '
                  'liter valós, mérhető mennyiség.)</p>'
                  '<p><b>Felszín.</b></p>'
                  '$$F=2r\\pi(r+H)=6\\pi\\cdot11=66\\pi\\ \\text{dm}^2.$$'
                  '<p>Ez körülbelül $207{,}35\\ \\text{dm}^2$, azaz nagyjából '
                  '$2{,}07\\ \\text{m}^2$ lemez.</p>')),
   kviz('Egy henger sugarát <b>megduplázzuk</b>, a magasságát változatlanul hagyjuk. '
        'Hányszorosára nő a térfogata?',
        ['Négyszeresére', 'Kétszeresére', 'Nyolcszorosára'], 0,
        jo="✔ V = r²πH, és a sugár NÉGYZETESEN szerepel: (2r)² = 4r², tehát a térfogat "
           "négyszereződik.",
        nem="✘ A sugár a képletben négyzeten áll: (2r)²πH = 4r²πH. A térfogat tehát "
            "négyszereződik, nem duplázódik."),
 ]),

 ("Fordított irányban", [
   '<p>A feladatok fele nem a képlet behelyettesítését kéri, hanem az <b>ellenkezőjét</b>: '
   'adott a végeredmény, és egy hiányzó adatot keresünk. A recept mindig ugyanaz — írd '
   'fel a képletet, helyettesítsd be, amit tudsz, és oldd meg az egyenletet.</p>',
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy henger térfogata $500\\pi$ cm³, az alapkör sugara $5$ cm. Mekkora a '
         'magassága?</p>',
         hid="pelda-forditott",
         lenyilo=("Megoldás",
                  '<p>$V=r^2\\pi H$, tehát</p>'
                  '$$25\\pi\\cdot H=500\\pi\\quad\\Longrightarrow\\quad H=\\frac{500}{25}=20\\ \\text{cm}.$$'
                  '<p>A $\\pi$ mindkét oldalon szerepel, ezért <b>kiesik</b> — ez a '
                  'legtöbb ilyen feladatban így van, és sokat egyszerűsít. Épp ezért '
                  'érdemes a $\\pi$-t végig jelként vinni, és nem $3{,}14$-ként.</p>')),
   '<p>Ha a <b>felszínből</b> keressük a sugarat, <b>másodfokú</b> egyenletet kapunk — a '
   'sugár ugyanis <b>négyzeten</b> is szerepel benne. Ilyenkor a megoldóképlet két '
   'gyököt ad, '
   'de a sugár csak <b>pozitív</b> lehet, ezért a negatív gyököt eldobjuk.</p>',
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy henger felszíne $150\\pi$ cm², magassága $10$ cm. Mekkora az alapkör '
         'sugara?</p>',
         hid="pelda-masodfoku",
         lenyilo=("Megoldás",
                  '<p>$F=2r^2\\pi+2r\\pi H$, tehát</p>'
                  '$$2r^2\\pi+20r\\pi=150\\pi.$$'
                  '<p>Osztunk $2\\pi$-vel:</p>'
                  '$$r^2+10r-75=0.$$'
                  '<p>A megoldóképlet szerint</p>'
                  '$$r=\\frac{-10\\pm\\sqrt{100+300}}{2}=\\frac{-10\\pm20}{2},$$'
                  '<p>ami $r=5$ vagy $r=-15$. A sugár nem lehet negatív, ezért '
                  '<b>$r=5$ cm</b>.</p>'
                  '<p>Ellenőrzés: $F=2\\cdot25\\pi+2\\cdot5\\cdot10\\pi=50\\pi+100\\pi=150\\pi$ — '
                  'stimmel.</p>')),
 ]),

 ("Nagyságrend és mértékegység", [
   '<p>A hengeres tartályok a valóságban <b>literben</b> vannak megadva, a képlet viszont '
   'köbegységet ad. A váltás egyetlen összefüggésen múlik:</p>'
   '$$1\\ \\text{dm}^3=1\\ \\text{liter},\\qquad 1\\ \\text{m}^3=1000\\ \\text{dm}^3=1000\\ \\text{liter}.$$'
   '<p>Ezért érdemes a hengeres tartályok adatait <b>deciméterben</b> felvenni: akkor a '
   'térfogat rögtön literben jön ki.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A tartály $0{,}4\\ \\text{m}^3$-es, tehát $40$ liter.”</i></p>'
         '<p>A hosszúságnál $1$ m $=10$ dm, de a <b>térfogatnál</b> a váltószám ennek a '
         '<b>köbe</b>: $1\\ \\text{m}^3=1000\\ \\text{dm}^3$. A helyes érték tehát '
         '<b>400 liter</b> — tízszer annyi.</p>'),
   doboz("erdekesseg", "Mikor számolj $\\pi$-vel, és mikor $3{,}14$-dal?",
         '<p>A matematikaórán a végeredmény <b>pontos alakban</b> áll: $V=72\\pi$ cm³. '
         'Ez nem lustaság, hanem pontosság — a $\\pi$ irracionális, minden közelítés '
         'hibát visz be.</p>'
         '<p>Közelítést akkor adunk, ha a feladat <b>valós, mérhető</b> mennyiséget kér: '
         'hány liter fér bele, hány kilogramm festék kell, mennyibe kerül az anyag. '
         'Ilyenkor általában két tizedesre kerekítünk, és a szöveg is jelzi, hogy '
         'közelítő értéket vár.</p>'
         '<p>Az iparban ez nem elméleti kérdés: egy nagy tartálynál a $3{,}14$ és a '
         'valódi $\\pi$ közötti eltérés egy $1000\\ \\text{m}^3$-es olajtartálynál már '
         'több száz liter — ezért '
         'számolnak a gyártók sokkal több tizedessel.</p>'),
   kviz('Egy hengeres hordó térfogata $0{,}75\\ \\text{m}^3$. Hány liter fér bele?',
        ['$750$ liter', '$75$ liter', '$7500$ liter'], 0,
        jo="✔ 1 m³ = 1000 liter, tehát 0,75 · 1000 = 750 liter.",
        nem="✘ A térfogat váltószáma 1000 (nem 100 és nem 10 000): "
            "0,75 m³ = 750 liter."),
   GY(FGY + "#alap-10", "A 10–20", FGY + "#kozep-6", "K 6–14"),
   brief('<b>Medúza:</b> A henger megvan — kapacitás és anyagszükséglet egyaránt. Most '
         'jön a kérdés, amitől a Kamra tölcsérei megszülettek: mi történik, ha a henger '
         'egyik alapkörét <b>egyetlen pontba</b> húzzuk össze?', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-forgastestek.html",
     cim="Forgástestek — amikor a sík alakzat körbefordul",
     cim_tiszta="Forgástestek",
     alcim="A forgatás mint művelet, a négy alapeset, a tengelymetszet és a "
           "tengelyre merőleges metszet.",
     chip=KUL + " · 1/10", szakaszok=A1,
     elozo=("index.html", "Forgástestek — témakör"),
     kovetkezo=("tananyag-henger.html", "A henger és elemei")),
 lap(**T, fajl="tananyag-henger.html",
     cim="A henger és elemei",
     cim_tiszta="A henger és elemei",
     alcim="Alapkörök, palást, alkotó, tengely, magasság; a háló és az egyenlő oldalú "
           "henger.",
     chip=KUL + " · 2/10", szakaszok=A2,
     elozo=("tananyag-forgastestek.html", "Forgástestek"),
     kovetkezo=("tananyag-henger-felszin-terfogat.html", "A henger felszíne és térfogata")),
 lap(**T, fajl="tananyag-henger-felszin-terfogat.html",
     cim="A henger felszíne és térfogata",
     cim_tiszta="A henger felszíne és térfogata",
     alcim="A palást a hálóból, a felszín kiemelt alakja, a térfogat, a fordított "
           "feladatok és a literes mértékegységváltás.",
     chip=KUL + " · 3/10", szakaszok=A3,
     elozo=("tananyag-henger.html", "A henger és elemei"),
     kovetkezo=(FGY, "Feladatok — a henger")),
]
for u in KI:
    print("✓", os.path.basename(u))
