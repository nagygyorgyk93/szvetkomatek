# -*- coding: utf-8 -*-
"""3e/01 — C altema: a gula (C1), felszin es terfogat (C2), sikmetszetek (C3),
csonkagula (C4). Mentor: Prizma. Kuldetes: A Kristalypara Kristalyok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_gula, svg_csonkagula, svg_halo, svg_haztest, svg_haromszog

T = dict(tagozat="3e", mappa="01-poliederek", temakor="Poliéderek")
FGY = "feladatok-gula.html"
KUL = "A Kristálypára Kristályok"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, simplify, N
E = []
def chk(n, g, w, tur=1e-12):
    e = simplify(g - w)
    if not (e == 0 or abs(float(N(e))) <= tur):
        E.append((n, g, w))

# C1 — szabályos négyoldalú gúla: a = 6, m = 4
a_, m_ = 6, 4
rho = R(a_, 2)                      # a négyzet apotémája
Ro = a_*sqrt(2)/2                   # köréírt sugár
mo = sqrt(m_**2 + rho**2)           # oldallap magassága
b_ = sqrt(m_**2 + Ro**2)            # oldalél
chk("g4-rho", rho, 3)
chk("g4-mo", mo, 5)
chk("g4-R", Ro, 3*sqrt(2))
chk("g4-b", b_, sqrt(34))
chk("g4-b-mo", sqrt(mo**2 + (R(a_, 2))**2), b_)   # a harmadik derékszögű háromszög
chk("g4-mo-kisebb", 1 if mo < b_ else 0, 1)
# C2 — ugyanaz a gúla: felszín és térfogat
chk("g4-B", a_**2, 36)
chk("g4-M", 4*a_*mo/2, 60)
chk("g4-F", a_**2 + 4*a_*mo/2, 96)
chk("g4-V", R(a_**2*m_, 3), 48)
# C2 — szabályos hatoldalú gúla: a = 4, m_o = 5
B6 = 6*4**2*sqrt(3)/4
chk("g6-B", B6, 24*sqrt(3))
chk("g6-M", 6*4*5/2, 60)
chk("g6-m", sqrt(5**2 - (4*sqrt(3)/2)**2), sqrt(13))
# C2 — összetett test: hasáb (6×6×5) + gúla (m = 4)
chk("osszetett-V", 6*6*5 + R(36*4, 3), 228)
# C3 — hasonlóság
for k in (R(1, 2), R(1, 3), R(2, 3)):
    chk(f"metszet-T-{k}", k**2*36, 36*k**2)
chk("felmagassag-T", R(1, 2)**2*36, 9)
chk("felmagassag-V", R(1, 2)**3*48, 6)
# C4 — szabályos négyoldalú csonkagúla: a = 10, a1 = 4, m_o = 5
Bc, bc = 10**2, 4**2
Mc = 4*(10 + 4)/2*5
mc = sqrt(5**2 - ((10 - 4)/2)**2)
chk("cs-M", Mc, 140)
chk("cs-F", Bc + bc + Mc, 256)
chk("cs-m", mc, 4)
chk("cs-V", R(1, 3)*mc*(Bc + bc + sqrt(Bc*bc)), 208)
chk("cs-hibas-V", R(1, 3)*mc*(Bc + bc), R(464, 3))    # a √(Bb) elhagyása
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_GULA = svg_gula("negyzet", a=1.0, m=1.5, apotema=True, oldalel=True, sugar=True,
                    w=340, h=310, feliratok={"a": "a"},
                    leiras="Szabályos négyoldalú gúla: magasság, apotéma, köréírt sugár, "
                           "oldallap-magasság és oldalél")
SVG_GULA3 = svg_gula("haromszog", a=1.0, m=1.4, apotema=True, w=310, h=295,
                     feliratok={"a": "a"},
                     leiras="Szabályos háromoldalú gúla az oldallap magasságával; "
                            "a csúcs itt a D pont")
SVG_GULA6 = svg_gula("hatszog", a=1.0, m=1.5, apotema=True, w=340, h=300,
                     leiras="Szabályos hatoldalú gúla")
SVG_HALO_G = svg_halo("gula", w=320, h=280)
SVG_HAZ = svg_haztest(a=1.0, b=1.0, m=0.55, mt=0.6, w=330, h=270,
                      leiras="Összetett test: négyzetes hasáb és a rá állított gúla")
SVG_METSZET_G = svg_gula("negyzet", a=1.0, m=1.6, metszet="parhuzamos", arany=R(1, 2),
                         w=330, h=300,
                         leiras="A gúla alappal párhuzamos metszete félmagasságban")
SVG_CSONKA = svg_csonkagula("negyzet", a=1.0, a1=0.45, m=1.0, magassag=True,
                            kiegeszites=True, w=330, h=290,
                            leiras="Csonkagúla; a levágott csúcsrész szaggatottan")
SVG_CSONKA6 = svg_csonkagula("hatszog", a=1.0, a1=0.55, m=0.9, w=330, h=260,
                             leiras="Szabályos hatoldalú csonkagúla")
SVG_TRAPEZ_LAP = svg_haromszog(csucsok=[(0, 0), (5, 0), (3.5, 3), (1.5, 3)],
                               cimkek=("A", "B", "C"), w=300, h=210,
                               leiras="A csonkagúla oldallapja trapéz") \
    if False else None

# ===================================================================== C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A Zóna mélyén a kristályok <b>tüskévé</b> húzódnak össze: az '
         'alaplapból minden él egyetlen pontba fut. Ez a gúla. A gúlafeladatokban ritkán a '
         'képlet a nehéz — sokkal inkább az, hogy megtaláld, <b>melyik derékszögű háromszögben</b> van '
         'az az adat, amit keresel. Ez az egység erről szól, és ha ezt megérted, a következő '
         'két egység már csak behelyettesítés.'),
   '<p>Három derékszögű háromszög lakik minden szabályos gúlában. Aki ezt a hármat látja, '
   'annak a gúla nem okoz gondot; aki nem, az a képletet is hiába tudja.</p>',
 ]),

 ("Hogyan keletkezik a gúla", [
   doboz("definicio", "A gúla",
         '<p>Vegyünk egy síksokszöget és egy olyan $E$ pontot, amely nincs a sokszög '
         'síkjában. Kössük össze $E$-t a (konvex) sokszög minden csúcsával. Az így '
         'keletkező háromszögek az alaplappal együtt egy testet zárnak közre: ez a '
         '<b>gúla</b>.</p>'
         '<p>A sokszög az <b>alaplap</b>, az $E$ pont a gúla <b>csúcsa</b>, az onnan induló '
         'szakaszok az <b>oldalélek</b>, az oldalélek és az alapélek által határolt '
         'háromszögek pedig az <b>oldallapok</b>. Az oldallapok együtt a <b>palást</b>.</p>'
         '<p>A gúla <b>magassága</b> a csúcsból az alaplap síkjára bocsátott merőleges '
         'szakasz — illetve ennek hossza, vagyis a csúcs távolsága az alaplap '
         'síkjától.</p>',
         hid="def-gula"),
   '<p>A gúlát is az alaplapja szerint nevezzük el: háromoldalú, négyoldalú, hatoldalú gúla. '
   'A <b>háromoldalú</b> gúlának négy háromszöglapja van — ezt <b>tetraédernek</b> is '
   'hívjuk.</p>',
 ]),

 ("Szabályos gúla — hol van a magasság talppontja", [
   doboz("definicio", "Szabályos gúla",
         '<p>Egy gúla <b>szabályos</b>, ha az alaplapja <b>szabályos sokszög</b>, és a '
         'magasság talppontja az alaplap <b>középpontja</b>.</p>'
         '<p>Ebből következik, hogy a szabályos gúla minden <b>oldaléle</b> egyenlő, és '
         'minden <b>oldallapja</b> egybevágó egyenlő szárú háromszög.</p>',
         hid="def-szabalyos-gula"),
   '<p>A „középpont” itt a szabályos sokszög beírt és köréírt körének közös középpontját '
   'jelenti. <b>Vigyázz a szóhasználattal:</b> nálunk az <b>apotéma</b> mindig az '
   '<i>alaplap</i> apotémája; a szerb tankönyvek <i>apotema piramide</i> néven az oldallap '
   'magasságát értik — azt itt végig $m_o$ jelöli. Innen az alapél <b>felezőpontjáig</b> mért távolság az apotéma ($\\rho$), a '
   '<b>csúcsig</b> mért távolság pedig a köréírt kör sugara ($R$) — mindkettőre szükség '
   'lesz.</p>',
   abra(SVG_GULA, 'Szabályos négyoldalú gúla: a magasság ($m$, piros), az alaplap apotémája '
        '($\\rho$, zöld), a köréírt kör sugara ($R$, lila), az oldallap magassága '
        '($m_o$, narancs) és az oldalél ($b$, kék).'),
 ]),

 ("A szabályos gúla három derékszögű háromszöge", [
   '<p>A szabályos gúla adatai három derékszögű háromszögbe rendeződnek. Mindháromban '
   'szerepel a magasság vagy az alapél fele, és mindhárom a Pitagorasz-tétellel dolgozik.</p>',
   doboz("tetel", "A szabályos gúla három derékszögű háromszöge",
         '<p>Ezek a képletek <b>szabályos</b> gúlára érvényesek: kell hozzájuk, hogy a '
         'magasság talppontja az alaplap középpontja legyen. Jelölje $a$ az alapélt, $m$ a magasságot, $\\rho$ az alaplap apotémáját, $R$ az '
         'alaplap köréírt sugarát, $m_o$ az oldallap magasságát és $b$ az oldalélt. Ekkor</p>'
         '<ol>'
         '<li>a magasság, az apotéma és az <b>oldallap magassága</b>: '
         '$m_o^{2}=m^{2}+\\rho^{2}$;</li>'
         '<li>a magasság, a köréírt sugár és az <b>oldalél</b>: $b^{2}=m^{2}+R^{2}$;</li>'
         '<li>az oldallap magassága, az alapél fele és az <b>oldalél</b>: '
         '$b^{2}=m_o^{2}+\\left(\\frac{a}{2}\\right)^{2}$.</li>'
         '</ol>'
         '<p>A harmadik háromszög magában az <b>oldallapban</b> fekszik: az egyenlő szárú '
         'háromszöget a magassága két derékszögű háromszögre vágja.</p>'
         '<p>Van egy negyedik, immár <b>síkbeli</b> összefüggés is, amely az alaplapon '
         'belül köti össze a két sugarat:</p>'
         '$$R^{2}=\\rho^{2}+\\left(\\frac{a}{2}\\right)^{2}.$$'
         '<p>A leggyakoribb alaplapokra:</p>'
         '<table class="tt-table">'
         '<tr><th>alaplap</th><th>apotéma $\\rho$</th><th>köréírt sugár $R$</th></tr>'
         '<tr><td>négyzet</td><td>$\\dfrac{a}{2}$</td><td>$\\dfrac{a\\sqrt2}{2}$</td></tr>'
         '<tr><td>szabályos háromszög</td><td>$\\dfrac{a\\sqrt3}{6}$</td>'
         '<td>$\\dfrac{a\\sqrt3}{3}$</td></tr>'
         '<tr><td>szabályos hatszög</td><td>$\\dfrac{a\\sqrt3}{2}$</td><td>$a$</td></tr>'
         '</table>'
         '<p>Mivel $\\rho &lt; R$, mindig $m_o &lt; b$: az <b>oldallap magassága rövidebb</b>, '
         'mint az oldalél.</p>',
         hid="tetel-harom-haromszog"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Az oldalél és az oldallap magassága — mindkettő a csúcsba fut, tehát '
         'ugyanaz."</i></p>'
         '<p>Nem ugyanaz. Az <b>oldalél</b> ($b$) a csúcsot az alaplap egy <b>csúcsával</b> '
         'köti össze, az <b>oldallap magassága</b> ($m_o$) pedig egy alapél '
         '<b>felezőpontjával</b>. A kettő két különböző derékszögű háromszögben él, és '
         'mindig $m_o &lt; b$. A palásthoz $m_o$ kell — ha $b$-vel számolsz, túl nagy felszínt '
         'kapsz.</p>'),
   abra(SVG_GULA3, 'Szabályos háromoldalú gúla — itt az alaplap $ABC$, a gúla csúcsa pedig '
        '$D$. Az oldallap magassága az alapél felezőpontjába érkezik, nem a csúcsába.'),
   kviz('A szabályos gúla melyik derékszögű háromszöge köti össze az <b>oldalélt</b> a '
        '<b>magassággal</b>?',
        ['A magasság és a köréírt sugár ($R$) alkotta háromszögben',
         'A magasság és az apotéma ($\\rho$) alkotta háromszögben',
         'Egyikben sem — az oldalél nem derékszögű háromszög oldala'], 0,
        jo="✔ b² = m² + R²: az oldalél az alaplap CSÚCSÁIG fut, ezért a köréírt sugár tartozik hozzá.",
        nem="✘ Az apotéma az alapél felezőpontjához vezet, tehát az az oldallap magasságához "
            "tartozik. Az oldalél a csúcsba fut, oda a köréírt sugár visz."),
 ]),

 ("Adatból adat", [
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos négyoldalú gúla alapéle $6$ cm, magassága $4$ cm. Számítsd ki az '
         'apotémát, az oldallap magasságát, a köréírt sugarat és az oldalélt!</p>',
         hid="pelda-gula-adatok",
         lenyilo=("Megoldás",
                  '<p><b>Apotéma.</b> Négyzet alaplapnál az apotéma az oldal fele: '
                  '$\\rho=\\frac{a}{2}=3$ cm.</p>'
                  '<p><b>Oldallap magassága</b> (1. háromszög):</p>'
                  '$$m_o=\\sqrt{m^2+\\rho^2}=\\sqrt{4^2+3^2}=\\sqrt{25}=5\\ \\text{cm}.$$'
                  '<p><b>Köréírt sugár.</b> A négyzet átlójának fele: '
                  '$R=\\frac{a\\sqrt2}{2}=3\\sqrt2\\approx 4{,}24$ cm.</p>'
                  '<p><b>Oldalél</b> (2. háromszög):</p>'
                  '$$b=\\sqrt{m^2+R^2}=\\sqrt{16+18}=\\sqrt{34}\\approx 5{,}83\\ \\text{cm}.$$'
                  '<p><b>Ellenőrzés a 3. háromszöggel:</b> '
                  '$\\sqrt{m_o^2+\\left(\\frac a2\\right)^2}=\\sqrt{25+9}=\\sqrt{34}$ — '
                  'ugyanaz. És valóban $m_o=5<5{,}83=b$.</p>')),
 ]),

 ("A tetraéder", [
   '<p>A háromoldalú gúlát <b>tetraédernek</b> nevezzük. Vigyázz a szóhasználattal:</p>'
   '<ul>'
   '<li><b>tetraéder</b>: bármely háromoldalú gúla (négy háromszöglap);</li>'
   '<li><b>szabályos tetraéder</b>: az, amelynek mind a hat éle egyenlő — ez az egyik '
   'szabályos test.</li>'
   '</ul>'
   '<p>Minden szabályos tetraéder szabályos háromoldalú gúla, de fordítva nem igaz: a '
   '<b>szabályos háromoldalú gúlának</b> az oldaléle lehet hosszabb az alapélnél. Azt is '
   'érdemes tudni, hogy a tetraédernek nincs kitüntetett alaplapja: bármelyik lapja lehet '
   'az alaplap — ez a magasság számításánál számít.</p>',
   kviz('Igaz-e: minden szabályos háromoldalú gúla egyben szabályos tetraéder?',
        ['Nem — az oldalél lehet hosszabb az alapélnél',
         'Igen, mert az alaplapja szabályos háromszög',
         'Igen, mert minden oldallapja egybevágó'], 0,
        jo="✔ A szabályos tetraéderhez az kell, hogy MIND A HAT él egyenlő legyen — egy magas, "
           "hegyes gúla is szabályos háromoldalú gúla.",
        nem="✘ Képzelj el egy nagyon magas, hegyes gúlát szabályos háromszög alaplappal: "
            "szabályos gúla, de az oldalélei jóval hosszabbak az alapélnél."),
   GY(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Prizma:</b> A három háromszög a kezedben van — innentől minden hiányzó adatot '
         'ki tudsz számolni. Jöhet a mérés: mennyi anyag kell a tüske burkolatához, és '
         'mennyi energiát zár be. Az utóbbinál vár rád a témakör legmakacsabb száma: egy '
         '<b>harmad</b>.', outro=True),
 ]),
]

# ===================================================================== C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Ugyanakkora alapon és ugyanakkora magassággal a tüske térfogata '
         '<b>harmadakkora</b>, mint az oszlopé. Nem közelítés, nem ökölszabály: '
         'pontosan egyharmad, és be is lehet látni. Ez az arány adja a Zóna '
         'energiamérlegének nagy részét.'),
   '<p>A felszín az alaplapból és a palástból áll össze; a hibák szinte mind a palástnál '
   'csúsznak be, mert ott az <b>oldallap magassága</b> kell, nem az oldalél. Ezért kezdjük '
   'ezzel.</p>',
 ]),

 ("A felszín", [
   '<p>A gúla palástja csupa háromszögből áll. <b>Szabályos</b> gúlánál ezek egybevágó '
   'egyenlő szárú háromszögek: mindegyik alapja $a$, magassága $m_o$, tehát egy oldallap '
   'területe $\\frac{a\\,m_o}{2}$.</p>',
   doboz("tetel", "A szabályos gúla felszíne",
         '<p>Ha az alaplap $n$ oldalú, akkor</p>'
         '$$M=n\\cdot\\frac{a\\,m_o}{2}=\\frac{K\\,m_o}{2},\\qquad F=B+M,$$'
         '<p>ahol $K=na$ az alaplap kerülete, $B$ az alaplap területe, $m_o$ pedig az '
         'oldallapnak az <b>alapélhez tartozó magassága</b>.</p>'
         '<p>A gúlának <b>egy</b> alaplapja van (a hasábnak alaplapja és fedőlapja is), ezért '
         'itt $B$ és nem $2B$ szerepel. Ha a gúla nem szabályos, az oldallapokat egyenként '
         'kell kiszámolni.</p>',
         hid="tetel-gula-felszin"),
   abra(SVG_HALO_G, 'A négyzetes gúla hálója: az alaplap és a négy oldallap. A háromszögek '
        'magassága $m_o$ — ez a szám kell a palásthoz.'),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Az oldallap háromszög, az oldala $b$ — a területe tehát '
         '$\\frac{a\\cdot b}{2}$."</i></p>'
         '<p>A háromszög területéhez az alaphoz tartozó <b>magasság</b> kell, nem a szár. '
         'Az oldallap alapja $a$, a hozzá tartozó magasság $m_o$ — az oldalél ($b$) csak a '
         'háromszög szára, és mindig hosszabb, mint $m_o$. Ha $b$-vel számolsz, a palást '
         'túl nagy lesz.</p>'),
   kviz('Melyik képlet adja a szabályos négyoldalú gúla palástját?',
        ['$M=4\\cdot\\frac{a\\,m_o}{2}$, ahol $m_o$ az oldallap magassága',
         '$M=4\\cdot\\frac{a\\,b}{2}$, ahol $b$ az oldalél',
         '$M=4a^2$'], 0,
        jo="✔ A háromszög területéhez a hozzá tartozó magasság kell — az oldallapé m_o.",
        nem="✘ Az oldallapok háromszögek, nem négyzetek — és a területükhöz nem az oldalél kell, "
            "hanem az alapélhez tartozó magasság, m_o."),
 ]),

 ("Miért harmad a térfogat", [
   doboz("tetel", "A gúla térfogata",
         '<p>Minden gúla térfogata</p>'
         '$$V=\\frac{B\\cdot m}{3},$$'
         '<p>ahol $B$ az alaplap területe, $m$ pedig a magasság.</p>',
         hid="tetel-gula-terfogat"),
   '<p>A <b>harmad</b> nem önkényes szám. Vegyük az $ABCA_1B_1C_1$ háromoldalú hasábot, és '
   'bontsuk fel a következő három gúlára: $A_1ABC$, $A_1B_1BC$ és $A_1B_1C_1C$.</p>'
   '<ul>'
   '<li>Az első kettőnek közös a $C$ csúcsa, az alapjuk pedig az $A_1AB$, illetve az '
   '$A_1B_1B$ háromszög — ezek az $ABB_1A_1$ paralelogramma két fele, tehát egyenlő '
   'területűek és egy síkban vannak.</li>'
   '<li>A második és a harmadik közös csúcsa $A_1$, az alapjuk a $B_1BC$, illetve a '
   '$B_1C_1C$ háromszög — a $BCC_1B_1$ paralelogramma két fele.</li>'
   '</ul>'
   '<p>Az <b>egyenlő alapterületű és egyenlő magasságú gúlák térfogata egyenlő</b> — ezt '
   'itt alapelvként fogadjuk el, a pontos bizonyítása nem tananyagunk. Eszerint mind a '
   'három darab térfogata ugyanakkora, és együtt kiadják a hasábot, tehát</p>'
   '$$V_{\\text{gúla}}=\\frac{V_{\\text{hasáb}}}{3}=\\frac{B\\cdot m}{3}.$$'
   '<p>Tetszőleges alapú gúlára ebből következik a képlet: az alaplapot háromszögekre '
   'bontjuk, minden darab háromoldalú gúla lesz — <b>ugyanazzal az $m$ magassággal</b>, '
   'hiszen a csúcs közös —, ezért a térfogatok összege '
   '$\\frac{B_1m}{3}+\\dots+\\frac{B_km}{3}=\\frac{Bm}{3}$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Ezért fér egy kúpos fagylalttölcsérbe pontosan harmadannyi, mint egy ugyanolyan '
         'széles és magas hengeres pohárba — a kúpra ugyanez a harmad érvényes, ahogy azt a '
         'következő témakörben látni fogjuk. És ezért van a sátortető alatt jóval kevesebb '
         'levegő van, mint amennyit a tetőtér magassága alapján gondolnánk.</p>'),
 ]),

 ("Kidolgozott példák", [
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos négyoldalú gúla alapéle $6$ cm, magassága $4$ cm. Mekkora a '
         'felszíne és a térfogata?</p>',
         hid="pelda-gula-felszin",
         lenyilo=("Megoldás",
                  '<p>Az <a href="tananyag-gula.html#pelda-gula-adatok">előző egységben</a> '
                  'már kiszámoltuk: az alaplap apotémája $\\rho=\\frac a2=3$ cm, az oldallap '
                  'magassága pedig $m_o=\\sqrt{4^2+3^2}=5$ cm.</p>'
                  '<p><b>Alaplap:</b> $B=a^2=36\\ \\text{cm}^2$. '
                  '<b>Kerület:</b> $K=4\\cdot 6=24$ cm.</p>'
                  '<p><b>Palást:</b> $M=\\frac{K\\,m_o}{2}=\\frac{24\\cdot 5}{2}='
                  '60\\ \\text{cm}^2$.</p>'
                  '<p><b>Felszín:</b> $F=B+M=36+60=96\\ \\text{cm}^2$.</p>'
                  '<p><b>Térfogat:</b> $V=\\frac{B\\,m}{3}=\\frac{36\\cdot 4}{3}='
                  '48\\ \\text{cm}^3$.</p>')),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos hatoldalú gúla alapéle $4$ cm, az oldallap magassága $5$ cm. '
         'Mekkora a felszíne? És a magassága?</p>',
         hid="pelda-hatszog-gula",
         lenyilo=("Megoldás",
                  '<p><b>Alaplap:</b> $B=6\\cdot\\frac{4^2\\sqrt3}{4}=24\\sqrt3\\approx '
                  '41{,}57\\ \\text{cm}^2$.</p>'
                  '<p><b>Palást:</b> $K=24$ cm, ezért '
                  '$M=\\frac{24\\cdot 5}{2}=60\\ \\text{cm}^2$, és '
                  '$F=24\\sqrt3+60\\approx 101{,}57\\ \\text{cm}^2$.</p>'
                  '<p><b>Magasság.</b> A szabályos hatszög apotémája '
                  '$\\rho=\\frac{a\\sqrt3}{2}=2\\sqrt3$ cm, tehát abból a derékszögű '
                  'háromszögből, amely a magasságot, az apotémát és az oldallap '
                  'magasságát köti össze:</p>'
                  '$$m=\\sqrt{m_o^2-\\rho^2}=\\sqrt{25-12}=\\sqrt{13}\\approx '
                  '3{,}61\\ \\text{cm}.$$')),
   abra(SVG_GULA6, 'Szabályos hatoldalú gúla.'),
 ]),

 ("Összetett testek", [
   '<p>A valós tárgyak ritkán „tiszta” testek: egy torony alsó része hasáb, a teteje gúla. '
   'Ilyenkor a <b>térfogatokat összeadjuk</b>, a <b>felszínnél</b> viszont figyelni kell: '
   'az összeillesztésnél lévő lapok <b>belülre</b> kerülnek, tehát nem tartoznak a '
   'felszínhez.</p>',
   abra(SVG_HAZ, 'Négyzetes hasáb és a rá állított szabályos négyoldalú gúla. A közös '
        'négyzetlap belülre kerül: a felszínbe nem számít bele.'),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy torony alsó része $6$ m alapélű, $5$ m magas négyzetes hasáb; a teteje a '
         'hasáb fedőlapjára illesztett, $4$ m magas szabályos négyoldalú gúla. Mekkora a '
         'torony térfogata és a felszíne?</p>',
         hid="pelda-gula-osszetett",
         lenyilo=("Megoldás",
                  '<p>A hasáb térfogata $V_1=6^2\\cdot 5=180\\ \\text{m}^3$.</p>'
                  '<p>A gúla alaplapja ugyanaz a négyzet, ezért '
                  '$V_2=\\frac{36\\cdot 4}{3}=48\\ \\text{m}^3$.</p>'
                  '<p>A torony térfogata $V=180+48=228\\ \\text{m}^3$.</p>'
                  '<p><b>Felszín.</b> A hasáb fedőlapja és a gúla alaplapja egymáshoz '
                  'simul, tehát belülre kerül; a talpon lévő négyzet viszont látszik. A gúla '
                  'oldallap-magassága $m_o=\\sqrt{4^2+3^2}=5$ m, ezért</p>'
                  '$$F=36+4\\cdot 6\\cdot 5+\\frac{24\\cdot 5}{2}=36+120+60='
                  '216\\ \\text{m}^2,$$'
                  '<p>ahol a három tag rendre a talp, a hasáb palástja és a gúla palástja.</p>')),
   kviz('Egy hasábra a fedőlapjával <b>pontosan egybevágó</b> alaplapú gúlát állítunk. '
        'Hogyan kapjuk meg az összetett test <b>felszínét</b>?',
        ['A hasáb alaplapja + a hasáb palástja + a gúla palástja',
         'A hasáb teljes felszíne + a gúla teljes felszíne',
         'A hasáb palástja + a gúla palástja'], 0,
        jo="✔ A hasáb fedőlapja és a gúla alaplapja egymáshoz simul, tehát belülre kerül; "
           "a talpon lévő alaplap viszont a felszín része.",
        nem="✘ Két lapot nem szabad beleszámolni: a hasáb fedőlapját és a gúla alaplapját — "
            "ezek az összeillesztésnél belülre kerülnek. A test alján lévő lap viszont látszik."),
   GY(FGY + "#alap-6", "A 6–15", FGY + "#kozep-5", "K 5–12"),
   brief('<b>Prizma:</b> A tüske mérve van. Most jön a kérdés, amiben Maxi a legtöbb '
         'kadétot elkapja: ha a tüskét az alaplappal párhuzamos síkkal, <b>félmagasságban</b> '
         'elvágjuk, mekkora a metszet <b>területe</b>? '
         'A válasz nem az, amit elsőre gondolnál.', outro=True),
 ]),
]

# ===================================================================== C3

C3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Vágd el a tüskét félmagasságban. A metszet <b>nem</b> feleakkora '
         'területű, mint az alaplap, hanem <b>negyedakkora</b>. Aki ezt elrontja, a '
         'Kristálypára felét számolja el — és ez az a hiba, amit Maxi a torz '
         'tér-egyenleteiben szándékosan meghagy.'),
   '<p>Ebben az egységben a gúla metszeteit nézzük meg, és közben egy olyan szabály '
   'bukkan elő, ami az egész geometriában érvényes: a hasonlóság <b>hossz–terület–térfogat</b> '
   'arányai.</p>',
 ]),

 ("Alappal párhuzamos metszet", [
   doboz("tetel", "A metszet hasonló az alaplaphoz",
         '<p>Ha a gúlát az alaplappal <b>párhuzamos</b> síkkal metsszük, a metszet az '
         'alaplaphoz <b>hasonló</b> sokszög. A hasonlóság aránya</p>'
         '$$k=\\frac{x}{m},$$'
         '<p>ahol $x$ a <b>metszősík</b> csúcstól mért távolsága (a magasságon mérve), $m$ pedig '
         'a gúla magassága. Értelmes metszethez $0&lt;k&lt;1$ kell: $k=1$ maga az '
         'alaplap, $k=0$ pedig már csak a csúcs.</p>'
         '<p>A metszet fölötti rész maga is gúla — az eredetihez hasonló, $k$ arányban '
         'kicsinyítve.</p>',
         hid="tetel-parhuzamos-metszet"),
   abra(SVG_METSZET_G, 'Félmagasságban metszve $k=\\frac12$: a metszet oldalai feleakkorák, '
        'mint az alaplapé.'),
 ]),

 ("A területek aránya", [
   doboz("tetel", "Hossz, terület, térfogat a hasonlóságnál",
         '<p>Ha két hasonló alakzat hasonlósági aránya $k$, akkor</p>'
         '<ul>'
         '<li>a megfelelő <b>hosszúságok</b> aránya $k$,</li>'
         '<li>a <b>területek</b> aránya $k^{2}$,</li>'
         '<li>a <b>térfogatok</b> aránya $k^{3}$.</li>'
         '</ul>'
         '<p>A gúla alappal párhuzamos metszetére tehát</p>'
         '$$T_{\\text{metszet}}=k^{2}\\cdot B.$$',
         hid="tetel-hasonlosag-aranyok"),
   '<table class="tt-table">'
   '<tr><th>$k=\\frac{x}{m}$</th><th>hosszak aránya</th>'
   '<th>a metszet területe / $B$</th><th>a <b>kis gúla</b> térfogata / $V$</th></tr>'
   '<tr><td>$\\frac12$</td><td>$\\frac12$</td><td>$\\frac14$</td><td>$\\frac18$</td></tr>'
   '<tr><td>$\\frac13$</td><td>$\\frac13$</td><td>$\\frac19$</td><td>$\\frac1{27}$</td></tr>'
   '<tr><td>$\\frac23$</td><td>$\\frac23$</td><td>$\\frac49$</td><td>$\\frac8{27}$</td></tr>'
   '</table>',
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos négyoldalú gúla alapéle $6$ cm, magassága $4$ cm (tehát '
         '$B=36\\ \\text{cm}^2$ és $V=48\\ \\text{cm}^3$). Elvágjuk félmagasságban. Mekkora '
         'a metszet területe, és mekkora a levágott kis gúla térfogata?</p>',
         hid="pelda-felmagassag",
         lenyilo=("Megoldás",
                  '<p>Félmagasságban $k=\\frac12$, ezért a metszet oldalai feleakkorák: az '
                  'oldala $3$ cm. A metszet területe</p>'
                  '$$T=k^2\\cdot B=\\frac14\\cdot 36=9\\ \\text{cm}^2,$$'
                  '<p>tehát <b>negyedakkora</b>, nem feleakkora. Ellenőrzés közvetlenül: a '
                  'metszet $3$ cm oldalú négyzet, területe $3^2=9\\ \\text{cm}^2$. ✔</p>'
                  '<p>A levágott kis gúla térfogata</p>'
                  '$$V_{\\text{kis}}=k^3\\cdot V=\\frac18\\cdot 48=6\\ \\text{cm}^3.$$'
                  '<p>Ez azt is jelenti, hogy az <b>alsó</b> darab (a csonkagúla) térfogata '
                  '$48-6=42\\ \\text{cm}^3$ — vagyis a test térfogatának hétnyolcada van '
                  'alul, pedig félmagasságban vágtunk.</p>')),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Félmagasságban vágtam, tehát a metszet feleakkora, és a levágott rész is a '
         'térfogat fele."</i></p>'
         '<p>Egyik sem igaz. A <b>hosszak</b> feleződnek, a <b>területek</b> negyedelődnek, '
         'a <b>térfogatok</b> nyolcadolódnak. Ez a hasonlóság alapszabálya, és nemcsak a '
         'gúlára igaz: ezért kerül négyszer annyi festék egy kétszer akkora táblára, és '
         'ezért nyolcszor nehezebb egy kétszer akkora, ugyanabból az anyagból készült '
         'szobor.</p>'),
   kviz('Egy gúlát a magasság <b>harmadánál</b> metszünk el (a csúcstól mérve). Hányadrésze '
        'a metszet területe az alaplapénak?',
        ['$\\frac19$', '$\\frac13$', '$\\frac1{27}$'], 0,
        jo="✔ A területek aránya k² = (1/3)² = 1/9.",
        nem="✘ A hosszak aránya 1/3, a területeké ennek a <b>négyzete</b> (1/9), a térfogatoké pedig a <b>köbe</b> (1/27)."),
 ]),

 ("Tengelymetszetek", [
   '<p>A <b>tengelymetszet</b> az a metszet, amely a gúla magasságát (a „tengelyt”) '
   'tartalmazza. Ilyen síkból végtelen sok van; <b>páros</b> oldalszámú szabályos gúlánál '
   'kettő közülük nevezetes:</p>'
   '<ul>'
   '<li>ha a két szemközti <b>oldalél</b> által meghatározott síkkal metszünk, a metszet '
   'egyenlő szárú háromszög: a szárai az <b>oldalélek</b> ($b$), az alapja pedig az '
   'alaplapnak a <b>középpontján átmenő átlója</b>;</li>'
   '<li>ha a két szemközti <b>oldallap magasságvonalán</b> át fektetjük a síkot, a metszet '
   'szárai az <b>oldallap-magasságok</b> ($m_o$), az alapja pedig $2\\rho$ — négyzet '
   'alaplapnál ez éppen $a$, hiszen ott $\\rho=\\frac a2$.</li>'
   '</ul>'
   '<p>Mindkét háromszög magassága a gúla magassága, $m$. Páratlan oldalszámnál (például '
   'szabályos háromoldalú gúlánál) nincs szemközti oldalél és szemközti oldallap: ott egy '
   'oldalél és a vele szemközti oldallap magassága esik egy síkba.</p>',
   doboz("erdekesseg", "Csak érdekesség",
         '<p>A szabályos négyoldalú gúlánál a két nevezetes tengelymetszet <b>nem egyforma</b>: az '
         'oldaléleken átmenő szélesebb (az alapja $a\\sqrt2$), az oldallap-magasságokon '
         'átmenő keskenyebb (az alapja $a$). Ha egy feladat „a tengelymetszet szabályos '
         'háromszög" feltételt ad, mindig nézd meg, melyikről beszél.</p>'),
 ]),

 ("Ha levágjuk a csúcsot", [
   '<p>Az alappal párhuzamos metszet a gúlát <b>két</b> testre bontja: fölül egy kisebb, az '
   'eredetihez hasonló gúlára, alul pedig egy olyan testre, amelynek két párhuzamos, '
   '<b>hasonló</b> alaplapja van, az oldallapjai pedig trapézok.</p>'
   '<p>Ez az alsó darab a <b>csonkagúla</b> — a témakör utolsó teste.</p>',
   GY(FGY + "#alap-16", "A 16–19", FGY + "#kozep-13", "K 13–15"),
   brief('<b>Prizma:</b> A vágás megtörtént. Ami alul maradt, önálló test — és a Zónában ez '
         'a leggyakoribb forma: a csonkagúla. Egy új képlet vár, benne egy meglepő taggal, '
         'amit a kadétok fele elhagy. Ne te legyél az.', outro=True),
 ]),
]

# ===================================================================== C4

C4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A levágott hegyű kristály a leggyakoribb forma a Zónában — és a '
         'hétköznapokban is: a szemetes, a rakodólap és a betonoszlop talpazata jellemzően ilyen '
         'alakú, a vödör és a virágcserép pedig ennek kerek rokona. Két új képlet vár rád, de minden elemük ismerős: két lap, trapéz '
         'oldallapok, és egy meglepő tag a térfogatban.'),
   '<p>Ez az utolsó test, amellyel ebben a témakörben megismerkedünk. A végén egy '
   '<b>gyorsismétlő</b> is vár: a három test képlettára egyetlen táblázatban.</p>',
 ]),

 ("Hogyan keletkezik a csonkagúla", [
   doboz("definicio", "A csonkagúla",
         '<p>Metsszük el a gúlát az alaplappal <b>párhuzamos</b> síkkal, és hagyjuk el a '
         'csúcsot tartalmazó részt. A megmaradó test a <b>csonkagúla</b>.</p>'
         '<p>A két párhuzamos lap az <b>alaplap</b> ($B$ területű) és a <b>fedőlap</b> '
         '($b$ területű) — ezek <b>hasonló</b> sokszögek. Az oldallapok <b>trapézok</b>, '
         'együtt a palást.</p>'
         '<p>A csonkagúla <b>szabályos</b>, ha szabályos gúlából származik: ekkor az '
         'alaplapja és a fedőlapja szabályos sokszög, az oldallapjai pedig egybevágó '
         'egyenlő szárú trapézok.</p>',
         hid="def-csonkagula"),
   abra(SVG_CSONKA, 'A csonkagúla a gúla alsó darabja. Szürke szaggatottal a levágott csúcsrész, feketével '
        'a takart élek, pirossal a magasság.'),
 ]),

 ("A csonkagúla elemei", [
   '<p>Öt hosszúságot kell megkülönböztetned — plusz a lenti dobozban még az apotémákat és '
   'a köréírt sugarakat:</p>'
   '<ul>'
   '<li>$a$ és $a_1$ — az alaplap és a fedőlap éle;</li>'
   '<li>$m$ — a test <b>magassága</b>, vagyis a két lap síkjának távolsága;</li>'
   '<li>$m_o$ — az <b>oldallap magassága</b>: a trapéz alakú oldallapon az alsó és a '
   'felső él távolsága;</li>'
   '<li>$c$ — az <b>oldalél</b>, vagyis a trapéz alakú oldallap szára. (Vigyázz: a $b$ '
   'betűt itt a <b>fedőlap területe</b> foglalja el, ezért kap az oldalél másik jelet.)</li>'
   '</ul>',
   doboz("tetel", "A szabályos csonkagúla derékszögű háromszögei",
         '<p>Feltesszük, hogy a test <b>szabályos</b>, tehát a két lap középpontját összekötő '
         'szakasz merőleges mindkét lapra. Jelölje $\\rho$ és $\\rho_1$ az alaplap, '
         'illetve a fedőlap <a href="tananyag-gula.html#tetel-harom-haromszog">'
         'apotémáját</a>, $R$ és $R_1$ a köréírt sugarakat. Ha a fedőlapot merőlegesen '
         'levetítjük az alaplapra, a megfelelő szakaszok különbsége adja a befogókat:</p>'
         '$$m_o^{2}=m^{2}+(\\rho-\\rho_1)^{2},\\qquad c^{2}=m^{2}+(R-R_1)^{2},'
         '\\qquad c^{2}=m_o^{2}+\\left(\\frac{a-a_1}{2}\\right)^{2}.$$'
         '<p>Négyzet alaplapnál $\\rho-\\rho_1=\\frac{a-a_1}{2}$, tehát</p>'
         '$$m_o=\\sqrt{m^{2}+\\left(\\frac{a-a_1}{2}\\right)^{2}}.$$'
         '<p>A gondolat ugyanaz, mint a gúlánál: a keresett szakasz mindig egy derékszögű '
         'háromszög átfogója, és a befogók egyike a magasság vagy az oldallap '
         'magassága.</p>',
         hid="tetel-csonkagula-haromszogek"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A magasság és az oldallap magassága — mindkettő „magasság”, tehát '
         'behelyettesíthetem bármelyiket."</i></p>'
         '<p>Nem. A <b>felszínbe</b> (a palásthoz) az <b>oldallap magassága</b> ($m_o$) megy, a '
         '<b>térfogatba</b> a <b>test magassága</b>. A kettő között éppen a fenti '
         'Pitagorasz-összefüggés teremt kapcsolatot, és mindig $m &lt; m_o$. Ha a feladat csak '
         'az egyiket adja meg, a másikat ki kell számolni.</p>'),
 ]),

 ("A felszín", [
   doboz("tetel", "A szabályos csonkagúla felszíne",
         '<p>Az oldallapok egybevágó trapézok: párhuzamos oldalaik $a$ és $a_1$, magasságuk '
         '$m_o$. Egy oldallap területe tehát $\\frac{(a+a_1)m_o}{2}$, és $n$ oldal esetén</p>'
         '$$M=n\\cdot\\frac{(a+a_1)\\,m_o}{2}=\\frac{(K+K_1)\\,m_o}{2},\\qquad F=B+b+M,$$'
         '<p>ahol $B$ és $b$ az alaplap, illetve a fedőlap <b>területe</b>, $K$ és $K_1$ pedig a '
         '<b>kerületük</b>. $M$ a palást (az oldallapok együttes) területe.</p>',
         hid="tetel-csonkagula-felszin"),
   abra(SVG_CSONKA6, 'Szabályos hatoldalú csonkagúla: az oldallapjai egyenlő szárú trapézok.'),
 ]),

 ("A térfogat", [
   doboz("tetel", "A csonkagúla térfogata",
         '$$V=\\frac{m}{3}\\left(B+b+\\sqrt{B\\,b}\\right),$$'
         '<p>ahol $B$ és $b$ a két lap területe, $m$ pedig a test magassága.</p>'
         '<p>A képlet a két gúla térfogatának különbségéből származik (a teljes gúláéból '
         'kivonjuk a levágott kicsiét); a $\\sqrt{Bb}$ tag — a két lapterület <b>mértani '
         'közepe</b> — ennek a különbségnek az átrendezéséből jön.</p>'
         '<p><b>Határesetben</b> ellenőrizhetjük a képletet (ezek maguk már nem csonkagúlák). Ha $b=B$, akkor '
         '$V=\\frac{m}{3}\\cdot 3B=Bm$ — vagyis a hasáb térfogatát kapjuk vissza, ami helyes, '
         'hiszen egyenlő lapokkal a test hasáb. Ha pedig $b=0$, akkor '
         '$V=\\frac{Bm}{3}$ — a gúla képlete.</p>',
         hid="tetel-csonkagula-terfogat"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Két alaplap van, tehát az átlaguk kell: '
         '$V=\\frac{m\\,(B+b)}{2}$."</i></p>'
         '<p>A trapéz területképletét nem lehet átvinni a térfogatra. A helyes képletben '
         'három tag áll, köztük a <b>mértani közép</b>, $\\sqrt{Bb}$ — és ennek elhagyása '
         'nem apró eltérés. A lenti példában a helyes érték $208\\ \\text{cm}^3$, a '
         '$\\frac{m(B+b)}{2}$ képlet viszont $232\\ \\text{cm}^3$-t adna, a $\\sqrt{Bb}$ '
         'nélküli harmados alak pedig $154{,}7\\ \\text{cm}^3$-t. Egyik sem jó.</p>'),
   doboz("pelda", "Kristály-kamra szimuláció",
         '<p>Egy szabályos négyoldalú csonkagúla alapélei $10$ cm és $4$ cm, az oldallap '
         'magassága $5$ cm. Mekkora a felszíne és a térfogata?</p>',
         hid="pelda-csonkagula",
         lenyilo=("Megoldás",
                  '<p><b>Lapok:</b> $B=10^2=100\\ \\text{cm}^2$, '
                  '$b=4^2=16\\ \\text{cm}^2$.</p>'
                  '<p><b>Palást:</b> négy egybevágó trapéz, mindegyik területe '
                  '$\\frac{(10+4)\\cdot 5}{2}=35\\ \\text{cm}^2$, tehát '
                  '$M=4\\cdot 35=140\\ \\text{cm}^2$.</p>'
                  '<p><b>Felszín:</b> $F=B+b+M=100+16+140=256\\ \\text{cm}^2$.</p>'
                  '<p><b>Magasság.</b> A trapéz magasságából (ez az $m_o$) és a '
                  '$\\frac{a-a_1}{2}=3$ cm-es vetületből:</p>'
                  '$$m=\\sqrt{m_o^2-\\left(\\frac{a-a_1}{2}\\right)^2}='
                  '\\sqrt{25-9}=4\\ \\text{cm}.$$'
                  '<p><b>Térfogat:</b></p>'
                  '$$V=\\frac{4}{3}\\left(100+16+\\sqrt{100\\cdot 16}\\right)'
                  '=\\frac{4}{3}\\cdot 156=208\\ \\text{cm}^3.$$')),
   kviz('Egy csonkagúla alaplapja $36\\ \\text{cm}^2$, fedőlapja $9\\ \\text{cm}^2$, '
        'magassága $5$ cm. Mekkora a térfogata?',
        ['$105\\ \\text{cm}^3$', '$112{,}5\\ \\text{cm}^3$', '$75\\ \\text{cm}^3$'], 0,
        jo="✔ √(Bb) = √324 = 18, ezért V = (5/3)(36 + 9 + 18) = 105.",
        nem="✘ Se a két lap átlagával nem számolunk (az 112,5 lenne), se a √(Bb) tagot nem "
            "hagyjuk el (az 75-öt adna): V = (5/3)(36 + 9 + √324) = (5/3)·63 = 105."),
 ]),

 ("🧾 Gyorsismétlő — a poliéderek képlettára", [
   '<table class="tt-table">'
   '<tr><th>Test</th><th>Felszín</th><th>Térfogat</th><th>Amire figyelj</th></tr>'
   '<tr><td><a href="tananyag-hasab-felszin-terfogat.html#tetel-hasab-felszin">egyenes hasáb</a></td>'
   '<td>$F=2B+K\\,m$</td><td>$V=B\\,m$</td>'
   '<td>a palásthoz a <b>kerület</b> kell, nem a terület</td></tr>'
   '<tr><td><a href="tananyag-gula-felszin-terfogat.html#tetel-gula-felszin">szabályos gúla</a></td>'
   '<td>$F=B+\\dfrac{K\\,m_o}{2}$</td><td>$V=\\dfrac{B\\,m}{3}$</td>'
   '<td>a palásthoz $m_o$ kell, nem az oldalél</td></tr>'
   '<tr><td><a href="#tetel-csonkagula-felszin">szabályos csonkagúla</a></td>'
   '<td>$F=B+b+\\dfrac{(K+K_1)m_o}{2}$</td>'
   '<td>$V=\\dfrac{m}{3}\\left(B+b+\\sqrt{Bb}\\right)$</td>'
   '<td>a $\\sqrt{Bb}$ tag nem hagyható el</td></tr>'
   '</table>'
   '<p><b>Jelölések:</b> $B$ és $b$ az alaplap, illetve a fedőlap <b>területe</b>; $K$ és '
   '$K_1$ a <b>kerületük</b>; $m$ a <b>test</b> magassága; $m_o$ az <b>oldallap</b> '
   'magassága.</p>'
   '<p>A három derékszögű háromszög (<a href="tananyag-gula.html#tetel-harom-haromszog">'
   'gúlánál</a>) és a hasonlóság $k$–$k^2$–$k^3$ szabálya '
   '(<a href="tananyag-gula-sikmetszetek.html#tetel-hasonlosag-aranyok">metszeteknél</a>) '
   'az a két eszköz, amivel a hiányzó adatok előkerülnek.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A betonoszlopok talpazata, a szemetesek és a rakodólapok jellemzően csonkagúla '
         'alakúak; a vödör, a virágcserép és a lámpaernyő ugyanennek a kerek változata, '
         '<b>csonkakúp</b> (a következő témakör anyaga). A forma nem véletlen: a test '
         'stabilan áll, a fala felfelé haladva kevesebb anyagot igényel, ráadásul a darabok '
         'egymásba rakhatók — ezért lehet a műanyag poharakat egyetlen oszlopba tornyozni.</p>'),
   GY(FGY + "#alap-20", "A 20–26", FGY + "#kozep-16", "K 16–21"),
   brief('<b>Prizma:</b> A Kristálypára szögletes formáit legyőzted: hasáb, gúla, '
         'csonkagúla — felszín, térfogat, metszet. De a Zóna mélyén már mozgásba lendült '
         'valami: a következő kristályok <b>nem szögletesek</b>. Ha a sokszög helyére '
         '<b>kör</b> kerül, a sík elhajlik, és a lapokból palást lesz. Medúza vár rád az '
         'Átalakulás Kamrájában.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-gula.html",
     cim="A gúla és elemei — a három derékszögű háromszög",
     cim_tiszta="A gúla és elemei",
     alcim="A gúla keletkezése, a szabályos gúla, a magasság, az oldallap-magasság és az "
           "oldalél kapcsolata.",
     chip=KUL + " · 8/11", szakaszok=C1,
     elozo=("feladatok-hasab.html", "Feladatok — a hasáb"),
     kovetkezo=("tananyag-gula-felszin-terfogat.html", "A gúla felszíne és térfogata")),
 lap(**T, fajl="tananyag-gula-felszin-terfogat.html",
     cim="A gúla felszíne és térfogata",
     cim_tiszta="A gúla felszíne és térfogata",
     alcim="A palást az oldallap-magassággal, a térfogat harmada, és az összetett testek.",
     chip=KUL + " · 9/11", szakaszok=C2,
     elozo=("tananyag-gula.html", "A gúla és elemei"),
     kovetkezo=("tananyag-gula-sikmetszetek.html", "A gúla síkmetszetei")),
 lap(**T, fajl="tananyag-gula-sikmetszetek.html",
     cim="A gúla síkmetszetei — a hasonlóság szabálya",
     cim_tiszta="A gúla síkmetszetei",
     alcim="Az alappal párhuzamos metszet, a hasonlóság hossz–terület–térfogat arányai és a "
           "tengelymetszetek.",
     chip=KUL + " · 10/11", szakaszok=C3,
     elozo=("tananyag-gula-felszin-terfogat.html", "A gúla felszíne és térfogata"),
     kovetkezo=("tananyag-csonkagula.html", "A csonkagúla")),
 lap(**T, fajl="tananyag-csonkagula.html",
     cim="A csonkagúla",
     cim_tiszta="A csonkagúla",
     alcim="A csonkagúla elemei, a trapéz oldallapok, a felszín és a térfogat képlete — "
           "a témakör képlettárával.",
     chip=KUL + " · 11/11", szakaszok=C4,
     elozo=("tananyag-gula-sikmetszetek.html", "A gúla síkmetszetei"),
     kovetkezo=(FGY, "Feladatok — a gúla és a csonkagúla")),
]
for u in KI:
    print("✓", os.path.basename(u))
