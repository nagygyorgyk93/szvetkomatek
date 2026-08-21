# -*- coding: utf-8 -*-
"""3e/02 — C altema: a gombfelulet es a gomb (C1), a gomb felszine es terfogata (C2),
osszetett es ureges testek (C3). Mentor: Meduza."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_gomb, svg_osszetett, svg_forgatas, svg_henger, svg_kup

T = dict(tagozat="3e", mappa="02-forgastestek", temakor="Forgástestek")
FGY = "feladatok-gomb.html"
KUL = "Az Átalakulás Kamrája"
POLI = "../01-poliederek/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, pi, simplify, N, symbols, solve, Eq, cbrt
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x = symbols("x", positive=True)
F_g = lambda Rr: 4*Rr**2*pi
V_g = lambda Rr: R(4, 3)*Rr**3*pi
V_h = lambda r, H: r**2*pi*H
V_k = lambda r, H: r**2*pi*H/3
# C1 — a sík és a gömbfelület: R = 13, d = 5
chk("C1-metszetkor", sqrt(13**2 - 5**2), 12)
# C2 — az r = 3 gömb: a felszín és a térfogat SZÁMA megegyezik
chk("C2-F", F_g(3), 36*pi)
chk("C2-V", V_g(3), 36*pi)
chk("C2-F-egyenlo-V", F_g(3) - V_g(3), 0)
# C2 — a gömb a köré írt henger térfogatának kétharmada
chk("C2-arany", V_g(x)/V_h(x, 2*x), R(2, 3))
chk("C2-felszin-arany", F_g(x), 4*x**2*pi)
# C2 — a sugár duplázása nyolcszorozza a térfogatot
chk("C2-duplazas", V_g(2*x)/V_g(x), 8)
# C2 — fordított: F = 100π → R = 5 ; V = 288π → R = 6
chk("C2-ford-F", solve(Eq(F_g(x), 100*pi), x)[0], 5)
chk("C2-ford-V", solve(Eq(V_g(x), 288*pi), x)[0], 6)
# C2 — acélgolyó: r = 5 cm, sűrűség 7,85 g/cm3
chk("C2-golyo-V", V_g(5), R(500, 3)*pi)
chk("C2-golyo-V-kozelites", N(V_g(5), 10), 523.5987756, 1e-6)
chk("C2-golyo-tomeg", N(V_g(5)*R(785, 100), 10), 4110.250388, 1e-5)
# C3 — víztorony: henger (r = 3, H = 10) + félgömb (R = 3)
chk("C3-vt-V", V_h(3, 10) + V_g(3)/2, 108*pi)
chk("C3-vt-kulso-F", 2*3*pi*10 + F_g(3)/2, 78*pi)
chk("C3-vt-teljes-F", 2*3*pi*10 + F_g(3)/2 + 3**2*pi, 87*pi)
# C3 — cső: R = 5, r = 4, H = 20
chk("C3-cso-V", V_h(5, 20) - V_h(4, 20), 180*pi)
chk("C3-cso-gyuruk", 2*(5**2*pi - 4**2*pi), 18*pi)
chk("C3-cso-F", 2*(5**2 - 4**2)*pi + 2*5*pi*20 + 2*4*pi*20, 378*pi)
# C3 — tölcsér: kúp (r = 3, H = 4) + henger (r = 3, H = 6)
chk("C3-tolcser-V", V_k(3, 4) + V_h(3, 6), 66*pi)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_GOMB = svg_gomb(w=280, h=250, leiras="Gömb a középpontjával és egy sugarával")
SVG_GOMB_METSZ = svg_gomb(sik="metszo", metszetkor=True, tavolsag=True, w=310, h=260,
    leiras="A sík metszi a gömbfelületet: a metszet kör")
SVG_GOMB_ERINT = svg_gomb(sik="erinto", w=300, h=250,
    leiras="A sík érinti a gömbfelületet: egyetlen közös pont")
SVG_GOMB_ELKER = svg_gomb(sik="elkerulo", w=300, h=250,
    leiras="A sík elkerüli a gömbfelületet: nincs közös pont")
SVG_GOMB_HENGER = svg_gomb(korulirt_henger=True, w=290, h=280,
    leiras="Gömb a köré írt hengerben: a térfogatok aránya 2:3")
SVG_F_FELKOR = svg_forgatas("felkor", w=430, h=250)
SVG_VIZTORONY = svg_osszetett("henger-felgomb", w=290, h=300)
SVG_TOLCSER = svg_osszetett("henger-kup", w=290, h=300)
SVG_CSO = svg_osszetett("cso", w=300, h=280)
SVG_FURT = svg_osszetett("furt-henger", w=290, h=280)

# ===================================================================== C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Kristálypára legstabilabb formája a <b>gömb</b> — minden '
         'pontja ugyanolyan messze van a középponttól, ezért nincs rajta gyenge pont, '
         'amin a nyomás beszakíthatná. Ezért gömbölyű a buborék, a bolygó és a '
         'vízcsepp.'),
   '<p>A gömb az egyetlen test a témakörben, amelyet <b>egyetlen adat</b> — a sugár — '
   'teljesen meghatároz. Nincs alapkör, nincs alkotó, nincs magasság: csak $R$.</p>'
   '<p>Ebben az egységben a fogalmakat rakjuk le, és megnézzük, mi történik, ha egy '
   'gömböt <b>síkkal</b> találunk el.</p>',
 ]),

 ("A gömbfelület és a gömb", [
   doboz("definicio", "Gömbfelület és gömb",
         '<p>Adott egy $O$ pont és egy $R>0$ szám.</p>'
         '<ul>'
         '<li>A <b>gömbfelület</b> azoknak a térbeli pontoknak a halmaza, amelyek az $O$ '
         'ponttól pontosan $R$ távolságra vannak.</li>'
         '<li>A <b>gömb</b> (gömbtest) a gömbfelület és az általa körbezárt belső '
         'tartomány <b>együtt</b> — vagyis azok a pontok, amelyek $O$-tól '
         '<b>legfeljebb</b> $R$ távolságra vannak.</li>'
         '</ul>'
         '<p>Az $O$ a <b>középpont</b>, az $R$ a <b>sugár</b>. A középponton átmenő húr '
         'az <b>átmérő</b>, hossza $2R$; a gömbfelület két pontját összekötő szakasz a '
         '<b>húr</b>.</p>',
         hid="def-gombfelulet"),
   abra(SVG_GOMB, 'A gömb középpontja és sugara ($R$). A szürke ellipszis a '
        '„vízszintes” főkör — csak a térbeliség érzékeltetésére.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A labda átmérője $20$ cm, tehát $R=20$."</i></p>'
         '<p>A képletekben <b>mindig a sugár</b> áll, az átmérő ennek a kétszerese. Ha '
         'a feladat átmérőt ad meg, az <b>első</b> lépés a felezés: $R=10$ cm.</p>'
         '<p>A hiba ára óriási, mert a sugár a térfogatban <b>köbön</b> szerepel: '
         '$20$-szal számolva nyolcszoros térfogatot kapnál.</p>'
         '<p>A másik gyakori csúszás a <b>szóhasználat</b>: a gömbfelület csak a '
         '„héj”, a gömb pedig a kitöltött test. Felszínt a felületről, térfogatot a '
         'testről beszélünk — de a köznyelvben mindkettőt „gömbnek” hívjuk, és ez '
         'megbocsátható.</p>'),
   kviz('Egy focilabda átmérője $22$ cm. Mekkora a sugara?',
        ['$11$ cm', '$22$ cm', '$44$ cm'], 0,
        jo="✔ A sugár az átmérő fele: R = 11 cm. A képletekbe MINDIG ez megy.",
        nem="✘ Az átmérő a sugár kétszerese, tehát R = 22 : 2 = 11 cm."),
 ]),

 ("A gömb mint forgástest", [
   '<p>A gömb is forgástest: egy <b>félkört</b> forgatunk meg az <b>átmérője</b> '
   'körül.</p>',
   abra(SVG_F_FELKOR, 'A félkör az átmérője körül forgatva gömböt ad.'),
   doboz("definicio", "Főkör",
         '<p>A gömb <b>főköre</b> az a metszet, amelyet a <b>középponton átmenő</b> '
         'síkkal kapunk. A főkör sugara maga a gömb sugara, $R$ — ez a gömb lehető '
         'legnagyobb síkmetszete.</p>'
         '<p>A gömb az egyetlen test, amelynek <b>minden</b> tengelymetszete '
         'egybevágó: mindegyik ugyanaz a főkör. Ezért nincs a gömbnek kitüntetett '
         '„álló” helyzete — bárhogy forgatod, ugyanúgy néz ki.</p>',
         hid="def-fokor"),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A Föld <b>Egyenlítője</b> főkör, a szélességi körök viszont nem — azok '
         'kisebb, az Egyenlítővel párhuzamos metszetkörök. Ezért rövidebb két pont '
         'között a repülőút, ha a főkör mentén (az úgynevezett ortodrómán) haladunk: '
         'a gömbfelületen két pont legrövidebb összekötése mindig főkörív.</p>'),
 ]),

 ("A gömbfelület és a sík kölcsönös helyzete", [
   '<p>Ez a témakör egyetlen olyan kérdése, ahol nem számolunk, hanem <b>eldöntünk</b>: '
   'két szám összevetése adja a választ.</p>',
   doboz("tetel", "A három eset",
         '<p>Legyen $d$ a gömb középpontjának távolsága a síktól, $R$ pedig a gömb '
         'sugara. Ekkor</p>'
         '<table class="tt-table">'
         '<tr><th>Feltétel</th><th>Helyzet</th><th>Közös pontok</th></tr>'
         '<tr><td>$d &gt; R$</td><td>a sík <b>elkerüli</b></td><td>nincs közös pont</td></tr>'
         '<tr><td>$d = R$</td><td>a sík <b>érinti</b></td><td>pontosan <b>egy</b> pont</td></tr>'
         '<tr><td>$d &lt; R$</td><td>a sík <b>metszi</b></td><td>egy <b>kör</b></td></tr>'
         '</table>'
         '<p>Ez pontosan a síkbeli „kör és egyenes” eset térbeli megfelelője — ott is a '
         'középpont-egyenes távolságot vetettük össze a sugárral.</p>',
         hid="tetel-gomb-sik"),
   abra(SVG_GOMB_METSZ, '$d &lt; R$: a sík <b>metszi</b> a gömbfelületet, a metszet kör.'),
   abra(SVG_GOMB_ERINT, '$d = R$: a sík <b>érinti</b> — egyetlen közös pont.'),
   abra(SVG_GOMB_ELKER, '$d &gt; R$: a sík <b>elkerüli</b> a gömbfelületet.'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy gömb sugara $13$ cm. Milyen helyzetben van a gömbfelülethez képest az '
         'a sík, amely a középponttól $5$ cm, illetve $13$ cm, illetve $20$ cm '
         'távolságra van?</p>',
         hid="pelda-gomb-sik",
         lenyilo=("Megoldás",
                  '<ul>'
                  '<li>$d=5 &lt; 13=R$ — a sík <b>metszi</b> a gömbfelületet, a metszet '
                  'egy kör.</li>'
                  '<li>$d=13=R$ — a sík <b>érinti</b>: pontosan egy közös pontjuk van.</li>'
                  '<li>$d=20 &gt; 13=R$ — a sík <b>elkerüli</b>, nincs közös pontjuk.</li>'
                  '</ul>'
                  '<p>Nem kell semmit kiszámolni: elég a $d$ és az $R$ összevetése.</p>')),
   doboz("tetel", "Az érintősík",
         '<p>Ha egy sík <b>érinti</b> a gömbfelületet, akkor <b>merőleges</b> az '
         'érintési pontba húzott sugárra — és fordítva: a sugár végpontjában a sugárra '
         'állított merőleges sík érintősík.</p>'
         '<p>Ez a síkbeli érintőkör-tétel („az érintő merőleges az érintési pontba '
         'húzott sugárra”) térbeli megfelelője.</p>',
         hid="tetel-erintosik"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Minél messzebb van a sík, annál kisebb kört metsz ki."</i></p>'
         '<p>A mondat első fele igaz, a második viszont csak <b>$d&lt;R$ esetén</b>. Ha '
         'a sík eléri a sugarat ($d=R$), a „kör” egyetlen ponttá zsugorodik, azon túl '
         'pedig <b>nincs</b> metszet — nem lesz „nagyon kicsi kör”, hanem semmi.</p>'
         '<p>Ezért a feladatokban mindig <b>először</b> a helyzetet döntsd el, és csak '
         'utána számolj.</p>'),
   doboz("erdekesseg", "A metszetkör sugara",
         '<p>Ha a sík metszi a gömbfelületet, a keletkező kör sugara Pitagorasz-tétellel '
         'adódik: a középpont, a metszetkör középpontja és a metszetkör egy pontja '
         'derékszögű háromszöget alkot, ezért</p>'
         '$$r=\\sqrt{R^{2}-d^{2}}.$$'
         '<p>Az előző példa első esetében ez $r=\\sqrt{169-25}=12$ cm.</p>'
         '<p><b>Ez nálunk nem számonkérés</b> — a tanterv a mi szakunkon csak a '
         '<b>kölcsönös helyzet</b> eldöntését várja el. Azért érdemes látni, mert a '
         'nehezebb gyakorlófeladatokban felbukkan, és mert szép: a földrajzi szélességi '
         'körök sugara pontosan így számolható.</p>',
         hid="erd-metszetkor"),
   kviz('Egy gömb sugara $8$ cm, egy sík a középponttól $8$ cm távolságra van. Hány '
        'közös pontja van a síknak és a gömbfelületnek?',
        ['Pontosan egy', 'Végtelen sok (egy kör)', 'Egy sem'], 0,
        jo="✔ d = R, tehát a sík ÉRINTI a gömbfelületet: pontosan egy közös pont.",
        nem="✘ Itt d = R = 8, ez az érintés esete — pontosan EGY közös pont. Kört akkor "
            "metszene ki, ha d < R lenne."),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Medúza:</b> A forma megvan. Most jön az a két képlet, amely az egészet '
         'leírja — és mindkettőben ugyanaz az egyetlen adat szerepel.', outro=True),
 ]),
]

# ===================================================================== C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A gömbnél <b>egyetlen adat</b>, a sugár mindent eldönt. Ez a '
         'jó hír. A rossz: ugyanez teszi a legveszélyesebbé is — aki a sugarat rontja '
         'el (mert átmérőt kapott, vagy rosszul olvasta), az <b>minden</b> további '
         'számítást elront.'),
   '<p>Két képlet van, és mindkettőt megadjuk — a levezetésük túlmutat a mi '
   'eszközeinken. Cserébe megnézzük, <b>miért hihetők</b>: mindkettőhöz tartozik egy '
   'szemléletes kép, ami segít megjegyezni.</p>',
 ]),

 ("A felszín", [
   doboz("tetel", "A gömb felszíne",
         '$$F=4R^{2}\\pi.$$'
         '<p>Vagyis a gömbfelület területe pontosan <b>négyszerese</b> a főkör '
         '($R^2\\pi$) területének.</p>',
         hid="tetel-gomb-felszin"),
   '<p><b>Miért hihető?</b> Végezd el a narancshéj-kísérletet: hámozz meg egy narancsot, '
   'és rajzolj körbe a papíron négy kört a narancs „egyenlítője” mentén. A héj '
   'darabjaival pontosan a <b>négy</b> kört töltöd ki — nem hármat, nem ötöt. Ez nem '
   'bizonyítás, de meggyőző, és pontosan azt mutatja, amit a képlet állít.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A felszín $F=4R\\pi$, a térfogat $V=\\frac{4R^2\\pi}{3}$."</i></p>'
         '<p>A <b>kitevők</b> csúsztak el. Ellenőrizd őket a <b>mértékegységgel</b>:</p>'
         '<ul>'
         '<li>a felszín <b>terület</b>, tehát cm² — ehhez a sugár <b>négyzete</b> kell: '
         '$4R^2\\pi$;</li>'
         '<li>a térfogat <b>köbös</b> mennyiség, tehát cm³ — ehhez a sugár <b>köbe</b>: '
         '$\\frac{4R^3\\pi}{3}$.</li>'
         '</ul>'
         '<p>Ez az ellenőrzés minden képletnél működik, és két másodpercbe kerül. Ha a '
         'mértékegység nem stimmel, a képlet sem.</p>'),
   kviz('Melyik képlet adja meg a gömb <b>felszínét</b>?',
        ['$F=4R^2\\pi$', '$F=\\dfrac{4R^3\\pi}{3}$', '$F=4R\\pi$'], 0,
        jo="✔ A felszín terület (cm²), ezért a sugár NÉGYZETEN áll: F = 4R²π.",
        nem="✘ Nézd a mértékegységet: a felszín cm², tehát a sugár négyzetén kell "
            "állnia. A köbös alak a térfogaté."),
 ]),

 ("A térfogat", [
   doboz("tetel", "A gömb térfogata",
         '$$V=\\frac{4R^{3}\\pi}{3}.$$',
         hid="tetel-gomb-terfogat"),
   '<p><b>Miért hihető?</b> Írjunk a gömb köré a lehető legszorosabb <b>hengert</b>: '
   'ennek az alapköre a főkör ($r=R$), a magassága pedig az átmérő ($H=2R$). A henger '
   'térfogata</p>'
   '$$V_{\\text{henger}}=R^2\\pi\\cdot2R=2R^3\\pi,$$'
   '<p>a gömbé pedig ennek pontosan a <b>kétharmada</b>:</p>'
   '$$\\frac{V_{\\text{gömb}}}{V_{\\text{henger}}}='
   '\\frac{\\frac{4R^3\\pi}{3}}{2R^3\\pi}=\\frac23.$$',
   abra(SVG_GOMB_HENGER, 'A gömb és a köré írt henger: a térfogatok aránya $2:3$.'),
   doboz("erdekesseg", "Arkhimédész sírköve",
         '<p>Ezt az arányt <b>Arkhimédész</b> fedezte fel, és annyira büszke volt rá, '
         'hogy — Cicero beszámolója szerint — a sírkövére a hengerbe írt gömböt '
         'vésették, a $2:3$ aránnyal. A sírt Cicero állítólag több mint száz évvel '
         'később, benőtt bozótban találta meg épp erről a jelről.</p>'
         '<p>Az arány a felszínekre is igaz: a gömb felszíne ($4R^2\\pi$) a köré írt '
         'henger <b>teljes</b> felszínének ($2R^2\\pi+2R\\pi\\cdot2R=6R^2\\pi$) szintén '
         'a kétharmada.</p>'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy gömb sugara $3$ cm. Számítsd ki a felszínét és a térfogatát!</p>',
         hid="pelda-gomb-3",
         lenyilo=("Megoldás",
                  '$$F=4\\cdot3^2\\pi=36\\pi\\ \\text{cm}^2,\\qquad '
                  'V=\\frac{4\\cdot3^3\\pi}{3}=36\\pi\\ \\text{cm}^3.$$'
                  '<p>A két <b>szám</b> megegyezik — de ez puszta véletlen, és csak '
                  'ennél az egy sugárnál fordul elő. A két mennyiség nem '
                  '<b>összehasonlítható</b>: az egyik cm²-ben, a másik cm³-ben mérendő, '
                  'mint ahogy egy szoba alapterületét sem hasonlítod a levegőjéhez.</p>'
                  '<p>Ellenőrizd $R=4$-gyel: $F=64\\pi$, de '
                  '$V=\\frac{256\\pi}{3}\\approx85{,}33\\pi$ — már nem egyeznek.</p>')),
   kviz('Egy gömb sugarát <b>megduplázzuk</b>. Hányszorosára nő a térfogata?',
        ['Nyolcszorosára', 'Kétszeresére', 'Négyszeresére'], 0,
        jo="✔ A sugár KÖBÖN szerepel: (2R)³ = 8R³, tehát a térfogat nyolcszorozódik. "
           "(A felszín közben négyszereződik.)",
        nem="✘ V = 4R³π/3 — a sugár köbön áll, ezért (2R)³ = 8R³: nyolcszoros térfogat."),
 ]),

 ("Fordított irányban és valós számítások", [
   '<p>Ha a felszín vagy a térfogat adott, a sugarat egyetlen lépésben megkapod:</p>'
   '$$R=\\sqrt{\\frac{F}{4\\pi}},\\qquad R=\\sqrt[3]{\\frac{3V}{4\\pi}}.$$'
   '<p>A gyakorlatban nem szoktuk ezeket a képleteket megjegyezni — egyszerűbb az '
   'alapképletbe behelyettesíteni, és megoldani az egyenletet. Ha $F=100\\pi$, akkor '
   '$4R^2\\pi=100\\pi$, tehát $R^2=25$ és $R=5$.</p>',
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Mekkora egy $5$ cm sugarú <b>acélgolyó</b> tömege, ha az acél sűrűsége '
         '$7{,}85\\ \\text{g/cm}^3$?</p>',
         hid="pelda-tomeg",
         lenyilo=("Megoldás",
                  '<p><b>Térfogat.</b></p>'
                  '$$V=\\frac{4\\cdot5^3\\pi}{3}=\\frac{500\\pi}{3}\\approx523{,}60\\ \\text{cm}^3.$$'
                  '<p><b>Tömeg.</b> A tömeg a sűrűség és a térfogat szorzata:</p>'
                  '$$m=\\varrho V\\approx7{,}85\\cdot523{,}60\\approx4110{,}25\\ \\text{g}'
                  '\\approx4{,}11\\ \\text{kg}.$$'
                  '<p>Itt <b>indokolt</b> a közelítés: a tömeg valós, mérhető mennyiség, '
                  'és a sűrűség maga is közelítő adat. Két tizedesnél tovább nincs '
                  'értelme számolni — a mért sűrűség pontossága úgysem engedi.</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A Föld sugara nagyjából $6371$ km, ebből a felszíne körülbelül '
         '$510$ millió km², a térfogata pedig $1{,}08\\cdot10^{12}$ km³. Ugyanezzel a '
         'két képlettel számol a meteorológus a jégeső szemcséinél, az orvos a '
         'sejteknél, és a cukrász, amikor megbecsüli, mennyi csokoládé kell a '
         'bonbonok bevonásához.</p>'),
   GY(FGY + "#alap-7", "A 7–16", FGY + "#kozep-4", "K 4–11"),
   brief('<b>Medúza:</b> A négy alaptest megvan. A valóságban viszont ritkán áll egy '
         'test magában — a Kamra minden szerkezete <b>összetett</b>. Ez lesz az utolsó '
         'lépés.', outro=True),
 ]),
]

# ===================================================================== C3

C3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A valóságban nincs „tiszta henger”. Van víztorony (henger + '
         'félgömb), van tölcsér (kúp + henger), és van cső (henger a hengerben). A '
         'módszer viszont mindig ugyanaz: <b>bontsd részekre</b>, számold ki a részeket, '
         'aztán rakd össze — de a felszínnél nagyon figyelj, mit raksz össze.'),
   '<p>Ez az egység nem hoz új képletet. Amit hoz, az egy <b>eljárás</b> és egy '
   'figyelmeztetés: a térfogatok összeadódnak, a felszínek <b>nem</b>.</p>',
 ]),

 ("Az összeadás elve — a térfogat", [
   doboz("tetel", "Összetett test térfogata",
         '<p>Ha egy testet <b>átfedés nélkül</b> felbontunk részekre, a térfogata a '
         'részek térfogatának <b>összege</b>:</p>'
         '$$V=V_1+V_2+\\dots+V_n.$$'
         '<p>Ez akkor is igaz, ha a részek különböző fajtájúak (henger, kúp, félgömb) — '
         'a térfogat „nem tudja”, hogy hol a határ.</p>',
         hid="tetel-osszetett-terfogat"),
   '<p>A gyakorlati lépések:</p>'
   '<ol>'
   '<li>Rajzold le a testet, és <b>húzd be</b> a határvonalakat, ahol a részek '
   'találkoznak.</li>'
   '<li>Nevezd meg a részeket, és írd fel mindegyik adatait — figyelj arra, hogy a '
   'közös határnál a sugarak általában <b>megegyeznek</b>.</li>'
   '<li>Számold ki a részek térfogatát, és add össze őket.</li>'
   '</ol>',
   abra(SVG_VIZTORONY, 'Víztorony: hengeres tartály félgömb tetővel. A határvonal '
        'szaggatva.'),
 ]),

 ("A felszín nem adódik össze", [
   doboz("tetel", "Összetett test felszíne",
         '<p>A felszínbe <b>csak a kívülről látható</b> felületek számítanak. Ahol két '
         'rész illeszkedik, ott a közös felület <b>egyik</b> testnél sem tartozik a '
         'felszínhez — mert nem határolja a testet a külvilág felé.</p>'
         '<p>Ezért a felszín <b>soha nem</b> a részek felszínének összege: abból a közös '
         'felületet <b>kétszer</b> vonni kell le.</p>',
         hid="tetel-osszetett-felszin"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A víztorony felszíne = a henger felszíne + a félgömb felszíne."</i></p>'
         '<p>A henger felszínében ott van a <b>felső</b> körlapja, a félgömb '
         '„felszínében” pedig az <b>alapköre</b> — pedig e kettő ugyanaz a kör, és '
         'kívülről <b>egyáltalán nem látszik</b>: a félgömb pontosan rajta ül.</p>'
         '<p><b>A biztos módszer:</b> rajzold le a testet, és satírozd be, ami kívülről '
         'látszik. Csak azt add össze. Ha a feladat azt mondja, hogy a tárgy a földön '
         'áll és nem festjük az alját, akkor az alsó körlap is kimarad.</p>'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy víztorony tartálya hengerből ($r=3$ m, $H=10$ m) és a rá épített '
         'félgömb tetőből áll. Mennyi víz fér bele, és mekkora a <b>külső</b> '
         'felülete, ha az alsó körlapot nem számítjuk?</p>',
         hid="pelda-viztorony",
         lenyilo=("Megoldás",
                  '<p><b>Térfogat.</b> A henger $V_1=9\\pi\\cdot10=90\\pi$, a félgömb '
                  '$V_2=\\frac12\\cdot\\frac{4\\cdot3^3\\pi}{3}=18\\pi$, tehát</p>'
                  '$$V=90\\pi+18\\pi=108\\pi\\approx339{,}29\\ \\text{m}^3.$$'
                  '<p><b>Felszín.</b> Kívülről a <b>hengerpalást</b> és a <b>félgömb</b> '
                  'látszik:</p>'
                  '<ul>'
                  '<li>hengerpalást: $2r\\pi H=2\\cdot3\\pi\\cdot10=60\\pi$;</li>'
                  '<li>félgömb: $\\frac12\\cdot4\\cdot3^2\\pi=18\\pi$.</li>'
                  '</ul>'
                  '$$F=60\\pi+18\\pi=78\\pi\\approx245{,}04\\ \\text{m}^2.$$'
                  '<p>A henger <b>felső</b> körlapja kimaradt — azon ül a félgömb. Ha a '
                  'feladat az alsó körlapot is kérné, még $9\\pi$ jönne hozzá, '
                  'összesen $87\\pi$.</p>')),
   kviz('Egy kúp és egy vele azonos sugarú henger alaplapjukkal összeillesztve alkotnak '
        'egy testet. Melyik állítás igaz?',
        ['A térfogatok összeadódnak, a felszínek nem',
         'Mindkettő összeadódik', 'A felszínek összeadódnak, a térfogatok nem'], 0,
        jo="✔ A térfogat összeadódik. A felszínnél viszont az illeszkedő két körlap "
           "eltűnik — azokat nem számoljuk.",
        nem="✘ A térfogatok mindig összeadódnak. A felszínből viszont az illeszkedő "
            "(eltakart) felületek kiesnek."),
   abra(SVG_TOLCSER, 'Kúppal fedett hengeres torony: az illeszkedő körlap kívülről nem '
        'látszik.'),
 ]),

 ("Üreges testek — a kivonás elve", [
   '<p>A cső, a betongyűrű és a fúrt alkatrész úgy keletkezik, hogy egy testből '
   '<b>kiveszünk</b> egy másikat. A térfogat ilyenkor <b>különbség</b>:</p>'
   '$$V=V_{\\text{külső}}-V_{\\text{belső}}.$$'
   '<p>A felszínnél viszont épp fordítva: az üreg <b>új felületet</b> hoz létre, ami '
   'nagyon is látszik — bele lehet nézni a csőbe.</p>',
   abra(SVG_CSO, 'Cső: két koncentrikus henger különbsége. A belső palást is a '
        'felszín része.'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy $20$ cm hosszú cső külső sugara $5$ cm, belső sugara $4$ cm. Mekkora a '
         'térfogata (az anyag mennyisége) és a teljes felszíne?</p>',
         hid="pelda-cso",
         lenyilo=("Megoldás",
                  '<p><b>Térfogat.</b></p>'
                  '$$V=25\\pi\\cdot20-16\\pi\\cdot20=500\\pi-320\\pi=180\\pi\\ \\text{cm}^3.$$'
                  '<p><b>Felszín.</b> A cső felülete <b>négy</b> részből áll:</p>'
                  '<ul>'
                  '<li>a két végén egy-egy <b>körgyűrű</b>: '
                  '$2\\cdot(25\\pi-16\\pi)=18\\pi$;</li>'
                  '<li>a <b>külső</b> palást: $2\\cdot5\\pi\\cdot20=200\\pi$;</li>'
                  '<li>a <b>belső</b> palást: $2\\cdot4\\pi\\cdot20=160\\pi$.</li>'
                  '</ul>'
                  '$$F=18\\pi+200\\pi+160\\pi=378\\pi\\ \\text{cm}^2.$$'
                  '<p>A belső palást a leggyakrabban elfelejtett rész — pedig ha a csövet '
                  'belülről is le kell festeni vagy szigetelni, épp az a lényeg.</p>')),
   abra(SVG_FURT, 'Hengerből kifúrt kúp: a térfogat különbség, a felszínben viszont '
        'megjelenik a fúrat palástja is.'),
   kviz('Hány felületdarabból áll egy mindkét végén nyitott cső felszíne?',
        ['Négyből: két körgyűrű, a külső és a belső palást',
         'Kettőből: a külső és a belső palást',
         'Háromból: két körgyűrű és a külső palást'], 0,
        jo="✔ Két körgyűrű a végeken, plusz a külső ÉS a belső palást — összesen négy.",
        nem="✘ A végeken körgyűrűk vannak (nem teli körök), és a belső palást is "
            "látszik: összesen négy darab."),
   GY(FGY + "#alap-17", "A 17–22", FGY + "#kozep-12", "K 12–17"),
 ]),

 ("🧾 Gyorsismétlő — a forgástestek képlettára", [
   '<table class="tt-table">'
   '<tr><th>Test</th><th>Felszín</th><th>Térfogat</th><th>Amire figyelj</th></tr>'
   '<tr><td><a href="tananyag-henger-felszin-terfogat.html#tetel-henger-felszin">henger</a></td>'
   '<td>$F=2r\\pi(r+H)$</td><td>$V=r^2\\pi H$</td>'
   '<td><b>két</b> alapkör; a palásthoz a <b>kerület</b> kell</td></tr>'
   '<tr><td><a href="tananyag-kup-felszin-terfogat.html#tetel-kup-felszin">kúp</a></td>'
   '<td>$F=r\\pi(r+s)$</td><td>$V=\\dfrac{r^2\\pi H}{3}$</td>'
   '<td>a palástban az <b>alkotó</b>, a térfogatban a <b>magasság</b></td></tr>'
   '<tr><td><a href="tananyag-csonkakup.html#tetel-csonkakup-felszin">csonkakúp</a></td>'
   '<td>$F=R^2\\pi+r^2\\pi+(R+r)\\pi s$</td>'
   '<td>$V=\\dfrac{H\\pi}{3}\\left(R^2+Rr+r^2\\right)$</td>'
   '<td>a palástban $R+r$, a háromszögben $R-r$</td></tr>'
   '<tr><td><a href="tananyag-gomb-felszin-terfogat.html#tetel-gomb-felszin">gömb</a></td>'
   '<td>$F=4R^2\\pi$</td><td>$V=\\dfrac{4R^3\\pi}{3}$</td>'
   '<td>a <b>sugár</b> kell, nem az átmérő; a kitevőket a mértékegység ellenőrzi</td></tr>'
   '</table>'
   '<p><b>Jelölések:</b> $r$ az alapkör sugara (a csonkakúpnál a <b>felső</b>, $R$ az '
   'alsó; a gömbnél $R$ maga a sugár), $H$ a testmagasság, $s$ az <b>alkotó</b>, '
   '$B=r^2\\pi$ az alapterület, $M$ a palást területe.</p>'
   '<p>A két legfontosabb összefüggés, amiből a hiányzó adat előkerül:</p>'
   '$$\\underbrace{s^2=r^2+H^2}_{\\text{kúp}},\\qquad '
   '\\underbrace{s^2=H^2+(R-r)^2}_{\\text{csonkakúp}}.$$',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Nézz körül a konyhában: a bögre henger, a tölcsér kúp, a virágcserép '
         'csonkakúp, a narancs gömb, a fánk pedig — na, az már egy ötödik test, a '
         '<b>tórusz</b>, amivel itt nem foglalkozunk. Az első négy viszont lefedi '
         'majdnem minden hétköznapi tárgy formáját, vagy azok kombinációját.</p>'),
   brief('<b>Medúza:</b> A formákat legyőztük — henger, kúp, csonkakúp, gömb, és minden, '
         'amit ezekből össze lehet rakni. Ami marad, az már nem forma, hanem '
         '<b>rendszer</b>. Átadom a szót Kanraknak.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-gomb.html",
     cim="A gömbfelület és a gömb",
     cim_tiszta="A gömbfelület és a gömb",
     alcim="Gömbfelület, gömb, főkör; a sík és a gömbfelület kölcsönös helyzete és az "
           "érintősík.",
     chip=KUL + " · 8/10", szakaszok=C1,
     elozo=("tananyag-csonkakup.html", "A csonkakúp"),
     kovetkezo=("tananyag-gomb-felszin-terfogat.html", "A gömb felszíne és térfogata")),
 lap(**T, fajl="tananyag-gomb-felszin-terfogat.html",
     cim="A gömb felszíne és térfogata",
     cim_tiszta="A gömb felszíne és térfogata",
     alcim="A két képlet, a köré írt henger 2:3 aránya, a fordított feladatok és a "
           "valós számítások.",
     chip=KUL + " · 9/10", szakaszok=C2,
     elozo=("tananyag-gomb.html", "A gömbfelület és a gömb"),
     kovetkezo=("tananyag-osszetett-testek.html", "Összetett és üreges testek")),
 lap(**T, fajl="tananyag-osszetett-testek.html",
     cim="Összetett és üreges testek",
     cim_tiszta="Összetett és üreges testek",
     alcim="Az összeadás és a kivonás elve, a felszín buktatói, és a témakör "
           "képlettára.",
     chip=KUL + " · 10/10", szakaszok=C3,
     elozo=("tananyag-gomb-felszin-terfogat.html", "A gömb felszíne és térfogata"),
     kovetkezo=(FGY, "Feladatok — a gömb és az összetett testek")),
]
for u in KI:
    print("✓", os.path.basename(u))
