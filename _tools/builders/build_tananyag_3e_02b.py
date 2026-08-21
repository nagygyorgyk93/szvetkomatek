# -*- coding: utf-8 -*-
"""3e/02 — B altema: a kup (B1), a kup felszine es terfogata (B2),
a henger es a kup sikmetszetei (B3), a csonkakup (B4). Mentor: Meduza."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import (svg_kup, svg_halo, svg_henger, svg_csonkakup,
                         svg_forgatas, svg_haromszog, svg_sikidom)

T = dict(tagozat="3e", mappa="02-forgastestek", temakor="Forgástestek")
FGY = "feladatok-kup.html"
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
M_k = lambda r, s: r*pi*s
F_k = lambda r, s: r**2*pi + r*pi*s
V_k = lambda r, H: r**2*pi*H/3
# B1 — a tölcsér: r = 6, H = 8
chk("B1-s", sqrt(6**2 + 8**2), 10)
chk("B1-fi", 360*R(6, 10), 216)
chk("B1-iv", 2*6*pi, 12*pi)
# B1 — egyenlő oldalú kúp: a tengelymetszet szabályos háromszög
chk("B1-eo-H", sqrt((2*x)**2 - x**2), x*sqrt(3))
# B2 — a 3-4-5 kúp
chk("B2-s", sqrt(3**2 + 4**2), 5)
chk("B2-M", M_k(3, 5), 15*pi)
chk("B2-F", F_k(3, 5), 24*pi)
chk("B2-V", V_k(3, 4), 12*pi)
chk("B2-eo-F", F_k(x, 2*x), 3*x**2*pi)
# B2 — a körcikkes levezetés: (fi/360)*s^2*pi = r*pi*s, ha fi/360 = r/s
chk("B2-levezetes", (R(1, 1)*x/5)*5**2*pi, M_k(x, 5))
# B2 — fordított: F = 24π és r = 3 → s
chk("B2-ford-s", solve(Eq(F_k(3, x), 24*pi), x)[0], 5)
chk("B2-ford-H", solve(Eq(V_k(3, x), 12*pi), x)[0], 4)
# B3 — az r = 5, H = 12 kúp tengelymetszete
chk("B3-s", sqrt(5**2 + 12**2), 13)
chk("B3-T", 2*5*12/2, 60)
chk("B3-K", 2*13 + 2*5, 36)
chk("B3-henger-T", 2*5*12, 120)
# B4 — a 6-3-4 csonkakúp
chk("B4-s", sqrt(4**2 + (6 - 3)**2), 5)
chk("B4-M", (6 + 3)*pi*5, 45*pi)
chk("B4-F", 6**2*pi + 3**2*pi + 45*pi, 90*pi)
chk("B4-V", R(4, 3)*pi*(6**2 + 6*3 + 3**2), 84*pi)
# B4 — ellenőrzés a teljes kúp mínusz a levágott kis kúp úton
chk("B4-teljes-H", 6*R(4, 6 - 3), 8)
chk("B4-ket-ut", V_k(6, 8) - V_k(3, 4), 84*pi)
chk("B4-nem-negyzet", 6**2 + 6*3 + 3**2, 63)
chk("B4-negyzet", (6 + 3)**2, 81)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_KUP = svg_kup(haromszog=True, w=310, h=290,
    leiras="Egyenes körkúp: alapkör, csúcs, alkotó, magasság és a jellemző derékszögű "
           "háromszög")
SVG_KUP_TISZTA = svg_kup(w=300, h=280, leiras="Egyenes körkúp a jelölésekkel")
SVG_HALO_KUP = svg_halo("kup", w=360, h=260)
SVG_KUP_TM = svg_kup(tengelymetszet=True, alkoto=True, w=300, h=280,
    leiras="A kúp tengelymetszete egyenlő szárú háromszög")
SVG_KUP_PM = svg_kup(parhuzamos_metszet=True, alkoto=False, w=300, h=280,
    leiras="A kúp alaplappal párhuzamos metszete az alapkörhöz hasonló kör")
SVG_HENGER_TM = svg_henger(tengelymetszet=True, w=310, h=270,
    leiras="A henger tengelymetszete téglalap")
SVG_CSONKA = svg_csonkakup(kiegeszites=True, w=300, h=280,
    leiras="Csonkakúp; szaggatva a levágott kúp, amelyből keletkezett")
SVG_CSONKA_H = svg_csonkakup(trapez=True, kiegeszites=False, w=300, h=250,
    leiras="A csonkakúp jellemző derékszögű háromszöge: befogói H és R mínusz r, "
           "átfogója az alkotó")
SVG_F_TRAPEZ = svg_forgatas("trapez", w=430, h=250)
SVG_TM_HAROM = svg_haromszog(csucsok=[(0, 0), (10, 0), (5, 12)],
    cimkek=("A", "B", "C"), oldalcimkek=("10", "13", "13"), magassag=2, w=320, h=250,
    leiras="A kúp tengelymetszete: egyenlő szárú háromszög, alapja 10, szárai 13")

# ===================================================================== B1

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Kamra szűkülő aknái kúpot formáznak — a pára fölfelé halad '
         'bennük, és egyetlen pontban távozik. A kúpnál <b>három</b> adat van: sugár, '
         'magasság, alkotó. És a feladatok pontosan azt hallgatják el, amelyikre '
         'szükséged lenne.'),
   '<p>Jó hír, hogy a három adat nem független: egy <b>derékszögű háromszög</b> köti '
   'össze őket. Ha kettőt tudsz, a harmadik egy Pitagorasz-tétel. Ebben az egységben ezt '
   'a háromszöget építjük fel, és kiterítjük a kúp palástját.</p>',
 ]),

 ("Hogyan keletkezik a kúp", [
   '<p>A kúp is kétféleképpen írható le, és mindkettőt érdemes látni:</p>'
   '<ul>'
   '<li><b>Forgatással:</b> egy <b>derékszögű háromszöget</b> megforgatunk az egyik '
   '<b>befogója</b> körül. A tengely lesz a magasság, a másik befogó a sugár, az átfogó '
   'pedig az alkotó.</li>'
   '<li><b>Metszéssel:</b> egy '
   '<a href="tananyag-forgastestek.html#def-hengerfelulet">kúpfelületet</a> elmetszünk '
   'egy olyan síkkal, amely <b>minden alkotót</b> metsz és nem megy át a csúcson; a '
   'csúcs és a sík közötti darabot vesszük.</li>'
   '</ul>'
   '<p>A kúp <b>egyenes</b>, ha a csúcsot az alapkör <b>középpontjával</b> összekötő '
   'szakasz merőleges az alaplapra — a forgatásból mindig ilyen keletkezik. Ha a csúcs '
   'oldalra csúszik, <b>ferde</b> kúpról beszélünk; ennek a felszínével és térfogatával '
   'nem foglalkozunk.</p>',
   abra(SVG_KUP_TISZTA, 'Az egyenes körkúp: egy <b>alapkör</b>, egy <b>csúcs</b>, és a '
        'kettőt összekötő görbe palást.'),
 ]),

 ("A kúp elemei", [
   doboz("definicio", "A kúp részei",
         '<ul>'
         '<li><b>Alapkör</b> — a határoló kör, sugara $r$; területe $B=r^2\\pi$.</li>'
         '<li><b>Csúcs</b> — az a pont, ahol az alkotók összefutnak.</li>'
         '<li><b>Alkotó</b> ($s$) — a csúcsot az alapkör egy pontjával összekötő szakasz. '
         'Egyenes kúpnál minden alkotó <b>egyenlő hosszú</b>.</li>'
         '<li><b>Magasság</b> ($H$) — a csúcs távolsága az alaplap síkjától.</li>'
         '<li><b>Tengely</b> — a csúcsot az alapkör középpontjával összekötő egyenes.</li>'
         '</ul>',
         hid="def-kup"),
   '<p>A hengernél az alkotó és a magasság ugyanaz volt. <b>A kúpnál nem</b> — és ez a '
   'témakör legfontosabb különbsége. Az alkotó a palást <b>felületén</b> fut, a magasság '
   'a test <b>belsejében</b>; a kettő közül mindig az alkotó a hosszabb.</p>',
 ]),

 ("A kúp derékszögű háromszöge", [
   '<p>Vágjuk el a kúpot a tengelyén <b>átmenő síkkal</b>. A kapott háromszög — ezt '
   'nevezzük <b>tengelymetszetnek</b> — <b>fele</b> egy derékszögű háromszög, amelynek '
   'a befogói a sugár és a magasság, az átfogója pedig az alkotó.</p>',
   doboz("tetel", "A kúp három adata",
         '<p>Az egyenes körkúpban</p>'
         '$$s^{2}=r^{2}+H^{2}.$$'
         '<p>Ez a témakör legtöbbet használt összefüggése: bármelyik két adatból megadja '
         'a harmadikat. Mivel az alkotó az <b>átfogó</b>, mindig</p>'
         '$$s>r\\quad\\text{és}\\quad s>H.$$'
         '<p>A gúlánál (<a href="' + POLI + 'tananyag-gula.html#tetel-harom-haromszog">'
         '01-es témakör</a>) <b>három</b> ilyen derékszögű háromszög volt. Ott az alaplap '
         'beírt és köré írt köre <b>különböző</b> ($r\\ne R$), a kúpnál viszont '
         '<b>egybeesik</b> — és alapél sincs, amihez a harmadik háromszög tartozna. '
         'Ezért marad egyetlen háromszög.</p>',
         hid="tetel-kup-haromszog"),
   abra(SVG_KUP, 'A kiemelt derékszögű háromszög befogói $r$ és $H$, átfogója az '
        'alkotó ($s$).'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Az alkotó a sugár és a magasság összege: $s=r+H$.”</i></p>'
         '<p>Ez a háromszög-egyenlőtlenség szerint lehetetlen: az átfogó mindig '
         '<b>kisebb</b> a két befogó összegénél. Ha $r=6$ és $H=8$, akkor $s=10$, nem '
         '$14$.</p>'
         '<p><b>Gyors önellenőrzés:</b> ha egy feladatban az „alkotó” a három adat közül '
         'a <b>legkisebb</b>, valamit félreolvastál — az alkotó soha nem lehet rövidebb '
         'sem a sugárnál, sem a magasságnál.</p>'),
   kviz('Egy kúp alapkörének sugara $9$ cm, magassága $12$ cm. Mekkora az alkotója?',
        ['$15$ cm', '$21$ cm', '$\\sqrt{63}\\approx 7{,}94$ cm'], 0,
        jo="✔ s² = 81 + 144 = 225, tehát s = 15 cm — hosszabb mindkét befogónál.",
        nem="✘ Az alkotó az ÁTFOGÓ: s = √(r² + H²) = √225 = 15. A 21 az összeg lenne, a "
            "√63 pedig kivonásból jönne — de itt összeadás kell."),
 ]),

 ("A kúp hálója", [
   '<p>Vágjuk fel a palástot egyetlen alkotó mentén, és terítsük ki. Nem téglalapot '
   'kapunk, mint a hengernél, hanem <b>körcikket</b> — hiszen a palást minden pontja '
   'ugyanolyan messze van a csúcstól.</p>',
   doboz("tetel", "Az egyenes kúp hálója",
         '<p>A kiterített palást <b>körcikk</b>, amelynek</p>'
         '<ul>'
         '<li>a <b>sugara</b> az alkotó, $s$ (mert minden alkotó egyenlő hosszú);</li>'
         '<li>az <b>ívhossza</b> az alapkör kerülete, $2r\\pi$ (mert a palást pontosan '
         'körbeéri az alapkört).</li>'
         '</ul>'
         '<p>A középponti szöge ebből következik: az ív a teljes $s$ sugarú kör '
         'kerületének ($2s\\pi$) annyiad része, amennyi a szög a teljes szöghöz képest, '
         'ezért</p>'
         '$$\\frac{\\varphi}{360^\\circ}=\\frac{2r\\pi}{2s\\pi}=\\frac rs,'
         '\\qquad\\text{azaz}\\qquad \\varphi=360^\\circ\\cdot\\frac rs.$$'
         '<p>A háló tehát ez a körcikk és egy $r$ sugarú kör.</p>',
         hid="tetel-kup-halo"),
   abra(SVG_HALO_KUP, 'A kúp hálója: körcikk (sugara az alkotó, íve az alapkör kerülete) '
        'és az alapkör.'),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy papírtölcsér alapkörének sugara $6$ cm, magassága $8$ cm. Mekkora '
         'körcikkből lehet kivágni?</p>',
         hid="pelda-tolcser",
         lenyilo=("Megoldás",
                  '<p><b>Az alkotó.</b> $s^2=6^2+8^2=100$, tehát $s=10$ cm — ez lesz a '
                  'körcikk sugara.</p>'
                  '<p><b>Az ívhossz.</b> $2r\\pi=12\\pi$ cm.</p>'
                  '<p><b>A középponti szög.</b></p>'
                  '$$\\varphi=360^\\circ\\cdot\\frac rs=360^\\circ\\cdot\\frac{6}{10}=216^\\circ.$$'
                  '<p>Tehát egy $10$ cm sugarú körből kell egy $216^\\circ$-os cikket '
                  'kivágni. A maradék $144^\\circ$ a hulladék. <b>Azonos alkotó '
                  'mellett</b> a laposabb, szélesebb tölcsérnél nagyobb ez a szög, '
                  'tehát arányosan kevesebb a hulladék.</p>')),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A körcikk sugara az alapkör sugara, tehát $r$.”</i></p>'
         '<p>A körcikk sugara az <b>alkotó</b> ($s$), nem az alapköré. Gondolj bele: a '
         'kiterített palást minden pontja onnan indul, ahol a <b>csúcs</b> volt — és a '
         'csúcstól minden palástpont pontosan $s$ távolságra van.</p>'
         '<p>Az alapkör sugara ($r$) a körcikk <b>ívének</b> hosszában bújik meg: '
         'az ív $2r\\pi$ hosszú.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Nézd meg egy papír fagylalttölcsér vagy egy partikalap kiterített mintáját: '
         'mindig körcikk. Ugyanezért körcikk alakú a szabásminta a kúpos lámpaernyőnél és '
         'a kémény bádogsapkájánál is — aki lemezből kúpot akar, körcikket vág ki és '
         'összehajtja.</p>'),
   kviz('Egy kúp alkotója $12$ cm, alapkörének sugara $4$ cm. Mekkora a kiterített '
        'palást (körcikk) középponti szöge?',
        ['$120^\\circ$', '$30^\\circ$', '$360^\\circ$'], 0,
        jo="✔ φ = 360° · r/s = 360° · 4/12 = 120°.",
        nem="✘ A képlet φ = 360° · r/s — a SUGARAT osztjuk az ALKOTÓVAL: "
            "360° · 4/12 = 120°."),
 ]),

 ("Az egyenlő oldalú kúp", [
   doboz("definicio", "Egyenlő oldalú kúp",
         '<p>A kúp <b>egyenlő oldalú</b>, ha a <b>tengelymetszete szabályos '
         '(egyenlő oldalú) háromszög</b>.</p>'
         '<p>A tengelymetszet alapja az átmérő ($2r$), a szárai az alkotók, ezért a '
         'feltétel azt jelenti, hogy</p>'
         '$$s=2r,\\qquad\\text{és ebből}\\qquad H=\\sqrt{(2r)^2-r^2}=r\\sqrt3.$$',
         hid="def-egyenlo-oldalu-kup"),
   '<p>Az egyenlő oldalú kúpnál is <b>egyetlen</b> adat határoz meg mindent: ha ismered '
   '$r$-t, adódik az alkotó és a magasság is. Sok feladat pontosan ezért indul innen — '
   'egyetlen számot ad meg, és a többit neked kell felépítened.</p>',
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Medúza:</b> A háromszög és a körcikk a helyén van. Innen a palást területe '
         'már nem definíció kérdése, hanem <b>levezetés</b> — a témakör egyetlen igazi '
         'levezetése.', outro=True),
 ]),
]

# ===================================================================== B2

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A kúpnál <b>két különböző</b> hosszúság szerepel a két '
         'képletben: a palástban az <b>alkotó</b>, a térfogatban a <b>magasság</b>. Aki '
         'ezt összekeveri, jó úton indul el, és rossz helyre érkezik — a számolása '
         'hibátlan lesz, az eredménye mégis rossz.'),
   '<p>Ebben az egységben egyetlen képletet <b>levezetünk</b> (a palástét), a többit '
   'pedig a már ismert szabályokból kapjuk. A levezetés nem formalitás: ha érted, '
   'honnan jön a $r\\pi s$ alak, soha nem fogod $H$-val felírni.</p>',
 ]),

 ("A palást a körcikkből", [
   '<p>A kiterített palást <a href="tananyag-kup.html#tetel-kup-halo">körcikk</a>, '
   'amelynek a sugara $s$, a középponti szöge pedig $\\varphi=360^\\circ\\cdot\\frac rs$. '
   'A palást területe tehát a körcikk területe.</p>',
   doboz("tetel", "A kúp palástja és felszíne",
         '<p><b>Levezetés.</b> A $\\varphi$ középponti szögű, $s$ sugarú körcikk területe '
         'a teljes kör területének $\\frac{\\varphi}{360^\\circ}$-ad része:</p>'
         '$$M=\\frac{\\varphi}{360^\\circ}\\cdot s^2\\pi.$$'
         '<p>Az előző egységből tudjuk (<a href="tananyag-kup.html#tetel-kup-halo">'
         'a kúp hálója</a>), hogy $\\frac{\\varphi}{360^\\circ}=\\frac rs$, ezért</p>'
         '$$M=\\frac rs\\cdot s^2\\pi=r\\pi s.$$'
         '<p>A felszín ehhez az <b>egyetlen</b> alapkört adja hozzá:</p>'
         '$$F=B+M=r^2\\pi+r\\pi s=r\\pi(r+s).$$',
         hid="tetel-kup-felszin"),
   '<p>Érdemes összevetni a hengerrel: ott $F=2r\\pi(r+H)$ volt, itt $F=r\\pi(r+s)$. A '
   'szerkezet ugyanaz, de a hengernél <b>két</b> alapkör van és a magasság szerepel, a '
   'kúpnál <b>egy</b> alapkör és az alkotó.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A palást $M=r\\pi H$, hiszen a magasság a test mérete.”</i></p>'
         '<p>A palást a test <b>felületén</b> fekszik — kiterítve pontosan az az '
         'alkotókból álló körcikk. Ezért az <b>alkotó</b> kell hozzá.</p>'
         '<p>A térfogat viszont „felfelé” épül, a test <b>belsejét</b> tölti ki, ezért '
         'ott a <b>magasság</b> szerepel. Egy mondatban: <b>a felületen az alkotó, a '
         'belsejében a magasság.</b></p>'
         '<p>A hiba ára nem kicsi: az $r=3$, $H=4$ (tehát $s=5$) kúpnál $M=15\\pi$ a helyes '
         'érték, a '
         'magassággal számolva $12\\pi$ jönne ki — 20 %-kal kevesebb.</p>'),
   kviz('Egy kúp alapkörének sugara $5$ cm, magassága $12$ cm. Mekkora a '
        '<b>palástjának</b> területe?',
        ['$65\\pi\\ \\text{cm}^2$', '$60\\pi\\ \\text{cm}^2$', '$25\\pi\\ \\text{cm}^2$'], 0,
        jo="✔ Előbb az alkotó: s = √(25 + 144) = 13. Ezután M = rπs = 5 · 13π = 65π cm².",
        nem="✘ A palásthoz az ALKOTÓ kell, nem a magasság. s = 13, tehát M = 5 · 13π = "
            "65π (a 60π a magassággal számolt, hibás érték)."),
 ]),

 ("A térfogat", [
   '<p>A térfogatnál a gúlánál megismert szabály folytatódik: az azonos alapú és '
   'magasságú <b>hasáb és gúla</b> térfogatának aránya $3:1$ volt, és ugyanez igaz a '
   '<b>henger és a kúp</b> párosra is.</p>',
   doboz("tetel", "A kúp térfogata",
         '$$V=\\frac{B\\cdot H}{3}=\\frac{r^2\\pi H}{3}.$$'
         '<p>Ugyanaz a harmadolás, mint a '
         '<a href="' + POLI + 'tananyag-gula-felszin-terfogat.html#tetel-gula-terfogat">'
         'gúlánál</a>. Szemléletesen: ha egy kúp alakú edénnyel háromszor merítesz, '
         'pontosan megtöltöd a vele azonos alapú és magasságú hengert.</p>',
         hid="tetel-kup-terfogat"),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Ezért fér a fagylalttölcsérbe harmadannyi, mint egy ugyanolyan széles és '
         'magas pohárba — és ezért csalódás, ha a gombóc nem magasodik ki belőle.</p>'
         '<p>A kiöntött homok, cement vagy gabona magától <b>kúp</b> alakú halomba áll. '
         'Az iparban ebből becsülik a mennyiséget: elég megmérni a halom kerületét és '
         'magasságát, a többi a $\\frac{r^2\\pi H}{3}$ képlet.</p>'),
   kviz('Egy henger és egy kúp alapköre és magassága is megegyezik. Hogyan aránylik a '
        'térfogatuk?',
        ['A kúpé a henger térfogatának harmada', 'A kúpé a henger térfogatának fele',
         'Egyenlők'], 0,
        jo="✔ V_kúp = r²πH/3, V_henger = r²πH — a kúp : henger arány pontosan 1 : 3.",
        nem="✘ A felezés a síkban igaz (háromszög és téglalap), a térben harmadolás van: "
            "a kúp a henger térfogatának HARMADA."),
 ]),

 ("A 3–4–5 kúp — minden adat egyszerre", [
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy kúp alapkörének sugara $3$ cm, magassága $4$ cm. Számítsd ki az '
         'alkotóját, a palástját, a felszínét és a térfogatát!</p>',
         hid="pelda-kup-345",
         lenyilo=("Megoldás",
                  '<p><b>Alkotó:</b> $s=\\sqrt{3^2+4^2}=\\sqrt{25}=5$ cm.</p>'
                  '<table class="tt-table">'
                  '<tr><th>Mennyiség</th><th>Képlet</th><th>Érték</th></tr>'
                  '<tr><td>alapterület</td><td>$B=r^2\\pi$</td><td>$9\\pi\\ \\text{cm}^2$</td></tr>'
                  '<tr><td>palást</td><td>$M=r\\pi s$</td><td>$15\\pi\\ \\text{cm}^2$</td></tr>'
                  '<tr><td>felszín</td><td>$F=B+M$</td><td>$24\\pi\\ \\text{cm}^2$</td></tr>'
                  '<tr><td>térfogat</td><td>$V=\\dfrac{r^2\\pi H}{3}$</td><td>$12\\pi\\ \\text{cm}^3$</td></tr>'
                  '</table>'
                  '<p>Figyeld meg: a <b>palástban</b> az $5$-ös (alkotó), a '
                  '<b>térfogatban</b> a $4$-es (magasság) szerepel. Ez a $3$–$4$–$5$ kúp '
                  'a témakör „mértékegysége”: érdemes fejből tudni, mert sok feladat '
                  'ennek a nagyítása.</p>')),
   '<p>Az <a href="tananyag-kup.html#def-egyenlo-oldalu-kup">egyenlő oldalú kúpnál</a> '
   '($s=2r$) a felszín különösen egyszerű lesz:</p>'
   '$$F=r\\pi(r+2r)=3r^2\\pi.$$'
   '<p>A térfogata pedig $V=\\dfrac{r^2\\pi\\cdot r\\sqrt3}{3}=\\dfrac{r^3\\pi\\sqrt3}{3}$.</p>',
 ]),

 ("Fordított irányban", [
   '<p>A kúpos feladatok többsége nem a behelyettesítést kéri. A recept ugyanaz, mint a '
   'hengernél — de itt <b>előbb</b> szinte mindig a hiányzó harmadik adatot kell '
   'előállítani a $s^2=r^2+H^2$ összefüggésből.</p>'
   '<p>A tipikus sorrend:</p>'
   '<ol>'
   '<li>Melyik két adat van meg a $r$, $H$, $s$ hármasból? A harmadikat Pitagorasszal '
   'számold ki.</li>'
   '<li>Csak ezután írd fel a felszín- vagy a térfogatképletet.</li>'
   '</ol>',
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy kúp felszíne $24\\pi$ cm², az alapkör sugara $3$ cm. Mekkora az '
         'alkotója és a térfogata?</p>',
         hid="pelda-kup-forditva",
         lenyilo=("Megoldás",
                  '<p><b>Az alkotó a felszínből.</b></p>'
                  '$$F=r\\pi(r+s)=3\\pi(3+s)=24\\pi.$$'
                  '<p>Osztunk $3\\pi$-vel: $3+s=8$, tehát $s=5$ cm.</p>'
                  '<p><b>A magasság Pitagorasszal.</b></p>'
                  '$$H=\\sqrt{s^2-r^2}=\\sqrt{25-9}=4\\ \\text{cm}.$$'
                  '<p><b>A térfogat.</b></p>'
                  '$$V=\\frac{9\\pi\\cdot4}{3}=12\\pi\\ \\text{cm}^3.$$'
                  '<p>A $\\pi$ az osztásnál kiesett — ezért érdemes végig '
                  '<b>szimbólumként</b> vinni, és nem $3{,}14$-dal számolni.</p>')),
   GY(FGY + "#alap-7", "A 7–16", FGY + "#kozep-4", "K 4–11"),
   brief('<b>Medúza:</b> A kúp minden adata a kezünkben van. A következő kérdés az, amit '
         'a Kamra minden zárt tartályánál fel kell tenni: <b>mi látszik, ha elvágjuk?</b>',
         outro=True),
 ]),
]

# ===================================================================== B3

B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A lezárt tartályokat <b>metszéssel</b> nyitjuk fel — de csak '
         'akkor, ha előre tudjuk, milyen alakzatot kapunk, és mekkora a területe. Vakon '
         'vágni drága: a Kamrában egy rossz metszet a teljes párakészletet elveszíti.'),
   '<p>A <a href="' + POLI + 'tananyag-hasab-sikmetszetek.html#def-sikmetszet">'
   'síkmetszet</a> fogalma a poliédereknél már megvolt: a test és a metszősík közös '
   'pontjainak halmaza. A forgástesteknél két metszet fordul elő újra és újra, és '
   'mindkettőt fejből kell tudni.</p>',
 ]),

 ("Tengelymetszet", [
   doboz("tetel", "A tengelymetszet alakja",
         '<p>A forgástengelyt <b>tartalmazó</b> síkkal vett metszet</p>'
         '<ul>'
         '<li>a <b>hengernél</b> téglalap: az egyik oldala az átmérő ($2r$), a másik a '
         'magasság ($H$);</li>'
         '<li>a <b>kúpnál</b> egyenlő szárú háromszög: az alapja az átmérő ($2r$), a '
         'szárai az <b>alkotók</b> ($s$), a magassága a test magassága ($H$).</li>'
         '</ul>',
         hid="tetel-tengelymetszet"),
   abra(SVG_HENGER_TM, 'A henger tengelymetszete téglalap.'),
   abra(SVG_KUP_TM, 'A kúp tengelymetszete egyenlő szárú háromszög.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A tengelymetszet-háromszög szára a magasság.”</i></p>'
         '<p>A <b>szár</b> az <b>alkotó</b> ($s$), a <b>magasság</b> pedig a háromszög '
         'magassága, ami a test $H$ magassága. A kettő csak akkor esne egybe, ha a '
         'háromszög elfajulna — vagyis ha a kúpnak nem lenne szélessége.</p>'
         '<p>A háromszög adatai tehát: alap $2r$, szárak $s$, magasság $H$. Ha egy '
         'feladat a tengelymetszet <b>kerületét</b> adja meg, az $2r+2s$; ha a '
         '<b>területét</b>, az $\\frac{2r\\cdot H}{2}=rH$.</p>'),
   kviz('Egy kúp tengelymetszetének <b>kerülete</b> $36$ cm, az alapkör sugara $5$ cm. '
        'Mekkora az alkotó?',
        ['$13$ cm', '$18$ cm', '$26$ cm'], 0,
        jo="✔ A kerület 2r + 2s = 36, tehát 10 + 2s = 36, ahonnan s = 13 cm.",
        nem="✘ A tengelymetszet egyenlő szárú háromszög: kerülete 2r + 2s. Innen "
            "2s = 36 − 10 = 26, tehát s = 13."),
 ]),

 ("Az alaplappal párhuzamos metszet", [
   doboz("tetel", "A párhuzamos metszet alakja",
         '<p>Az alaplappal párhuzamos síkkal vett metszet mindkét testnél <b>kör</b>, '
         'de a méretében élesen különböznek:</p>'
         '<ul>'
         '<li>a <b>hengernél</b> az alapkörrel <b>egybevágó</b> — bárhol metszünk, '
         'ugyanaz az $r$ sugarú kör;</li>'
         '<li>a <b>kúpnál</b> az alapkörhöz <b>hasonló</b>, és a hasonlóság aránya a '
         '<b>csúcstól mért magasságok aránya</b>. Ha a metszősík a csúcstól a magasság '
         '$k$-szorosánál van, a metszetkör sugara $k\\cdot r$. Ha a feladat az '
         '<b>alaplaptól</b> mért $d$ távolságot adja meg, akkor '
         '$k=\\frac{H-d}{H}$.</li>'
         '</ul>',
         hid="tetel-parhuzamos-metszet"),
   abra(SVG_KUP_PM, 'A kúp párhuzamos metszete az alapkörhöz <b>hasonló</b> kör — annál '
        'kisebb, minél közelebb van a csúcshoz.'),
   '<p>A hasonlóság aránya ugyanúgy működik, mint a '
   '<a href="' + POLI + 'tananyag-gula-sikmetszetek.html#tetel-hasonlosag-aranyok">'
   'gúlánál</a>: ha a hosszak aránya $k$, akkor a <b>területeké</b> $k^2$, a '
   '<b>térfogatoké</b> pedig $k^3$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A szeletelt sonka, a fatörzs évgyűrűi és a CT-felvétel mind alappal '
         'párhuzamos metszetek sorozata. A CT épp azért működik, mert a szervezetről '
         'készült sok vékony metszetből a számítógép vissza tudja építeni a testet — '
         'ugyanaz az elv, mint amikor a metszetek területéből következtetünk a '
         'térfogatra.</p>'),
   kviz('Egy kúpot a csúcstól mért magasság <b>felénél</b> metszünk el az alaplappal '
        'párhuzamosan. Hogyan aránylik a metszetkör területe az alapkörhöz?',
        ['A negyede', 'A fele', 'Ugyanakkora'], 0,
        jo="✔ A hosszak aránya k = ½, a területeké k² = ¼ — a metszet területe az "
           "alapkör negyede.",
        nem="✘ Ez nem a henger: a kúpnál a metszet HASONLÓ, nem egybevágó. A hosszak "
            "aránya ½, a területeké ennek a négyzete: ¼."),
 ]),

 ("A metszet területe — számolás", [
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy kúp alapkörének sugara $5$ cm, magassága $12$ cm. Mekkora a '
         'tengelymetszetének a területe és a kerülete?</p>',
         hid="pelda-metszet-terulet",
         lenyilo=("Megoldás",
                  '<p><b>Az alkotó.</b> $s=\\sqrt{25+144}=13$ cm.</p>'
                  '<p>A tengelymetszet egyenlő szárú háromszög: az alapja '
                  '$2r=10$ cm, a szárai $13$ cm, a magassága $H=12$ cm.</p>'
                  '<p><b>Terület:</b></p>'
                  '$$T=\\frac{2r\\cdot H}{2}=\\frac{10\\cdot12}{2}=60\\ \\text{cm}^2.$$'
                  '<p><b>Kerület:</b> $K=2r+2s=10+26=36$ cm.</p>'
                  '<p>Figyeld meg, hogy a <b>területbe</b> a magasság megy (mert a '
                  'háromszög területéhez az alaphoz tartozó magasság kell), a '
                  '<b>kerületbe</b> pedig az alkotó.</p>')),
   abra(SVG_TM_HAROM, 'A kapott háromszög külön kirajzolva: alapja $10$, szárai $13$, '
        'magassága $12$.'),
   '<p><b>Párhuzamos metszet.</b> Ha ugyanezt a kúpot a csúcstól mért magasság '
   'harmadánál metsszük el az alaplappal párhuzamosan, a metszetkör sugara '
   '$\\frac13\\cdot5=\\frac53$, a területe pedig '
   '$\\left(\\frac13\\right)^2\\cdot25\\pi=\\frac{25\\pi}{9}$ cm².</p>'
   '<p>A tengelymetszet területe általában:</p>'
   '<ul>'
   '<li><b>henger:</b> $T=2r\\cdot H$ (téglalap);</li>'
   '<li><b>kúp:</b> $T=\\dfrac{2r\\cdot H}{2}=r\\,H$ (háromszög).</li>'
   '</ul>'
   '<p>Ezek a képletek az egyenlő oldalú testeknél különösen hasznosak: az '
   '<a href="tananyag-henger.html#def-egyenlo-oldalu-henger">egyenlő oldalú '
   'hengernél</a> a tengelymetszet négyzet ($H=2r$), az '
   '<a href="tananyag-kup.html#def-egyenlo-oldalu-kup">egyenlő oldalú kúpnál</a> '
   'szabályos háromszög ($s=2r$, $H=r\\sqrt3$) — egyetlen adatból minden kijön.</p>',
   GY(FGY + "#alap-17", "A 17–21", FGY + "#kozep-12", "K 12–15"),
   brief('<b>Medúza:</b> Ha az alaplappal párhuzamosan vágunk, és a <b>felső</b> darabot '
         'eldobjuk, egy új test marad a kezünkben. A Kamra hűtőaknái pontosan ilyenek.',
         outro=True),
 ]),
]

# ===================================================================== B4

B4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Kamra hűtőaknái felfelé szűkülnek — ez <b>csonkakúp</b>. A '
         'képletei hosszabbak minden eddiginél, ezért nem magolni kell őket, hanem '
         'érteni, <b>honnan jönnek</b>. Aki érti, annak három sor; aki magol, annak '
         'három hiba.'),
   '<p>Jó hír: mindegyik képlet a csonkagúláénak a „kerek” megfelelője. Ha ott megvolt a '
   '<a href="' + POLI + 'tananyag-csonkagula.html#tetel-csonkagula-terfogat">három tag</a> '
   'a térfogatban, itt is három lesz.</p>',
 ]),

 ("Hogyan keletkezik a csonkakúp", [
   '<p>Két úton is eljutunk ugyanahhoz a testhez:</p>'
   '<ul>'
   '<li><b>Csonkolással:</b> egy kúpot elmetszünk az alaplapjával <b>párhuzamos</b> '
   'síkkal, és a <b>csúcsot tartalmazó</b> részt elhagyjuk.</li>'
   '<li><b>Forgatással:</b> egy <b>derékszögű trapézt</b> megforgatunk azon szára '
   'körül, amely <b>merőleges</b> a párhuzamos oldalakra.</li>'
   '</ul>',
   abra(SVG_F_TRAPEZ, 'A derékszögű trapéz a derékszögű szára körül forgatva csonkakúpot '
        'ad: a két párhuzamos oldal lesz a két sugár.'),
   doboz("definicio", "A csonkakúp részei",
         '<ul>'
         '<li><b>Alapkör</b> — az alsó, nagyobb kör; sugara $R$.</li>'
         '<li><b>Fedőkör</b> — a felső, kisebb kör; sugara $r$. A két kör síkja '
         '<b>párhuzamos</b>, a középpontjaik pedig ugyanazon a rájuk merőleges '
         'tengelyen vannak.</li>'
         '<li><b>Alkotó</b> ($s$) — az alapkör és a fedőkör egy-egy pontját összekötő, a '
         'paláston fekvő szakasz.</li>'
         '<li><b>Magasság</b> ($H$) — a két kör síkjának távolsága.</li>'
         '</ul>'
         '<p>Csak <b>egyenes</b> csonkakúppal foglalkozunk — ilyenkor minden alkotó '
         'egyenlő hosszú, és a palást képlete is erre érvényes.</p>',
         hid="def-csonkakup"),
   abra(SVG_CSONKA, 'A csonkakúp a kúp alsó darabja; szaggatva a levágott csúcsrész.'),
 ]),

 ("A jellemző derékszögű háromszög", [
   '<p>Ha a fedőkört merőlegesen levetítjük az alaplapra, a két <b>sugár különbsége</b> '
   '($R-r$) jelenik meg befogóként.</p>',
   doboz("tetel", "A csonkakúp három adata",
         '$$s^{2}=H^{2}+(R-r)^{2}.$$'
         '<p>A derékszögű háromszög befogói a <b>magasság</b> ($H$) és a két sugár '
         '<b>különbsége</b> ($R-r$), az átfogója pedig az <b>alkotó</b> ($s$).</p>',
         hid="tetel-csonkakup-haromszog"),
   abra(SVG_CSONKA_H, 'A fél tengelymetszet (sárga) és benne a derékszögű háromszög: '
        'a szaggatott vízszintes befogó a két sugár <b>különbsége</b>, az átfogó az '
        'alkotó.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A befogó a két sugár összege: $R+r$.”</i></p>'
         '<p>Nézd meg az ábrát: a kisebb kör pontosan a nagyobb <b>fölött</b> van, közös '
         'tengelyen. A vetítés után a szélei közötti vízszintes távolság ezért '
         '$R-r$, nem $R+r$.</p>'
         '<p>Számokkal: $R=6$, $r=3$, $H=4$ esetén a helyes alkotó '
         '$s=\\sqrt{16+9}=5$; az összeggel számolva $\\sqrt{16+81}=\\sqrt{97}\\approx9{,}85$ '
         'jönne ki — majdnem a duplája.</p>'
         '<p>Ugyanez a hiba bújik meg a térfogatnál is: '
         '$R^2+Rr+r^2\\ne(R+r)^2$. A fenti számokkal $63$ az egyik és $81$ a másik.</p>'),
   kviz('Egy csonkakúp sugarai $10$ cm és $4$ cm, magassága $8$ cm. Mekkora az '
        'alkotója?',
        ['$10$ cm', '$\\sqrt{260}\\approx16{,}12$ cm', '$14$ cm'], 0,
        jo="✔ s² = H² + (R − r)² = 64 + 36 = 100, tehát s = 10 cm.",
        nem="✘ A befogó a sugarak KÜLÖNBSÉGE: R − r = 6. Innen s² = 64 + 36 = 100, "
            "azaz s = 10 cm."),
 ]),

 ("A felszín", [
   '<p>A palást kiterítve <b>körgyűrűcikk</b> (két körcikk különbsége). A területe '
   'ugyanúgy áll elő, mint a csonkagúla palástjáé: ott az oldallap-trapéz '
   '<b>középvonala</b> szorzódott az oldallap magasságával, itt a két alapkör '
   'kerületének <b>átlaga</b> szorzódik az alkotóval:</p>'
   '$$M=\\frac{2R\\pi+2r\\pi}{2}\\cdot s=(R+r)\\pi s.$$',
   doboz("tetel", "A csonkakúp felszíne",
         '<p>A palást területe</p>'
         '$$M=(R+r)\\pi s,$$'
         '<p>a felszín pedig a <b>két</b> kört is hozzáadja:</p>'
         '$$F=R^{2}\\pi+r^{2}\\pi+(R+r)\\pi s.$$'
         '<p>A palástban tehát a sugarak <b>összege</b> szerepel (mint a trapéz '
         'középvonalában), a derékszögű háromszögben viszont a <b>különbségük</b> — '
         'érdemes a kettőt tudatosan szétválasztani.</p>',
         hid="tetel-csonkakup-felszin"),
 ]),

 ("A térfogat és egy példa két úton", [
   doboz("tetel", "A csonkakúp térfogata",
         '$$V=\\frac{H\\pi}{3}\\left(R^{2}+Rr+r^{2}\\right).$$'
         '<p>A zárójelben <b>három</b> tag áll, középen a két sugár <b>szorzatával</b> — '
         'pontosan úgy, ahogy a '
         '<a href="' + POLI + 'tananyag-csonkagula.html#tetel-csonkagula-terfogat">'
         'csonkagúlánál</a> a $\\sqrt{B_1B_2}$ mértani közép. A képlet a teljes kúp és a '
         'levágott kis kúp térfogatának különbségéből származik.</p>'
         '<p><b>Határeset-ellenőrzés:</b> ha $r=R$, akkor '
         '$V=\\frac{H\\pi}{3}\\cdot3R^2=R^2\\pi H$ — a henger térfogata. Ha $r=0$, akkor '
         '$V=\\frac{R^2\\pi H}{3}$ — a kúpé. Mindkét határeset stimmel.</p>',
         hid="tetel-csonkakup-terfogat"),
   doboz("pelda", "Átalakulás-kamra szimuláció",
         '<p>Egy csonkakúp alapkörének sugara $6$ cm, fedőköréé $3$ cm, magassága '
         '$4$ cm. Számítsd ki az alkotóját, a felszínét és a térfogatát — a térfogatot '
         '<b>két különböző úton</b> is!</p>',
         hid="pelda-csonkakup",
         lenyilo=("Megoldás",
                  '<p><b>Alkotó:</b> $s=\\sqrt{4^2+(6-3)^2}=\\sqrt{25}=5$ cm.</p>'
                  '<p><b>Palást:</b> $M=(6+3)\\pi\\cdot5=45\\pi\\ \\text{cm}^2$.</p>'
                  '<p><b>Felszín:</b> '
                  '$F=36\\pi+9\\pi+45\\pi=90\\pi\\ \\text{cm}^2$.</p>'
                  '<p><b>Térfogat, 1. út — a képlettel.</b></p>'
                  '$$V=\\frac{4\\pi}{3}\\left(36+18+9\\right)=\\frac{4\\pi}{3}\\cdot63'
                  '=84\\pi\\ \\text{cm}^3.$$'
                  '<p><b>Térfogat, 2. út — kivonással.</b> A levágott kis kúp és a teljes '
                  'kúp hasonlóak; a sugarak aránya $\\frac36=\\frac12$, ezért a kis kúp '
                  'magassága a teljesnek a fele. Ha a teljes kúp magassága $x$, akkor '
                  '$x-\\frac x2=4$, tehát $x=8$ és a kis kúp magassága $4$.</p>'
                  '$$V=\\frac{36\\pi\\cdot8}{3}-\\frac{9\\pi\\cdot4}{3}=96\\pi-12\\pi'
                  '=84\\pi\\ \\text{cm}^3.$$'
                  '<p>A két út ugyanazt adja — ez a legjobb önellenőrzés, ha nem vagy '
                  'biztos a képletben.</p>')),
   kviz('Egy csonkakúp sugarai $R=6$ és $r=3$. Mennyi a térfogatképlet zárójeles '
        'része, $R^2+Rr+r^2$?',
        ['$63$', '$81$', '$45$'], 0,
        jo="✔ 36 + 18 + 9 = 63. (A 81 az (R + r)² lenne — az NEM ugyanaz.)",
        nem="✘ Tagonként: R² = 36, Rr = 18, r² = 9, összesen 63. A 81 az (R + r)² = 9², "
            "ami más kifejezés."),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A virágcserép, a vödör, a lámpaernyő, a papírpohár és a hűtőtorony mind '
         'csonkakúp. Nem véletlen: a szűkülő forma <b>egymásba rakható</b> (ezért lehet '
         'a poharakat toronyba állítani), és a ferde fal <b>merevebb</b> is, mint a '
         'függőleges.</p>'),
   GY(FGY + "#alap-22", "A 22–28", FGY + "#kozep-16", "K 16–21"),
   brief('<b>Medúza:</b> A szögletes és a szűkülő formák megvannak. Marad a '
         'legtökéletesebb — az a test, amelynek a <b>felülete</b> minden pontjában '
         'ugyanolyan messze van a középponttól: a <b>gömb</b>. De előbb bevetés: a kúp '
         'feladatai.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-kup.html",
     cim="A kúp és elemei",
     cim_tiszta="A kúp és elemei",
     alcim="Alapkör, csúcs, alkotó, magasság; a kúp derékszögű háromszöge, a körcikkes "
           "háló és az egyenlő oldalú kúp.",
     chip=KUL + " · 4/10", szakaszok=B1,
     elozo=("tananyag-henger-felszin-terfogat.html", "A henger felszíne és térfogata"),
     kovetkezo=("tananyag-kup-felszin-terfogat.html", "A kúp felszíne és térfogata")),
 lap(**T, fajl="tananyag-kup-felszin-terfogat.html",
     cim="A kúp felszíne és térfogata",
     cim_tiszta="A kúp felszíne és térfogata",
     alcim="A palást levezetése a körcikkből, a felszín, a harmadolás és a fordított "
           "feladatok.",
     chip=KUL + " · 5/10", szakaszok=B2,
     elozo=("tananyag-kup.html", "A kúp és elemei"),
     kovetkezo=("tananyag-sikmetszetek.html", "A henger és a kúp síkmetszetei")),
 lap(**T, fajl="tananyag-sikmetszetek.html",
     cim="A henger és a kúp síkmetszetei",
     cim_tiszta="A henger és a kúp síkmetszetei",
     alcim="Tengelymetszet és alaplappal párhuzamos metszet: az alakjuk, a hasonlóság "
           "aránya és a területük.",
     chip=KUL + " · 6/10", szakaszok=B3,
     elozo=("tananyag-kup-felszin-terfogat.html", "A kúp felszíne és térfogata"),
     kovetkezo=("tananyag-csonkakup.html", "A csonkakúp")),
 lap(**T, fajl="tananyag-csonkakup.html",
     cim="A csonkakúp",
     cim_tiszta="A csonkakúp",
     alcim="Keletkezés, a jellemző derékszögű háromszög, a felszín és a háromtagú "
           "térfogatképlet.",
     chip=KUL + " · 7/10", szakaszok=B4,
     elozo=("tananyag-sikmetszetek.html", "A henger és a kúp síkmetszetei"),
     kovetkezo=(FGY, "Feladatok — a kúp")),
]
for u in KI:
    print("✓", os.path.basename(u))
