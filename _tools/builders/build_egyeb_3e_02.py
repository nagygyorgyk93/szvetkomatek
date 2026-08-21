# -*- coding: utf-8 -*-
"""3e/02 — osszefoglalo (F4), terepkuldetes (F5p), Veszterem (F6h), temakor-index (F5).
Mentor: Meduza. Kuldetes: Az Atalakulas Kamraja."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, abra, GYOKER
from abra_common import svg_henger, svg_kup, svg_csonkakup, svg_gomb, svg_osszetett

T = dict(tagozat="3e", mappa="02-forgastestek", temakor="Forgástestek")
KUL = "Az Átalakulás Kamrája"
POLI = "../01-poliederek/"

# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, sqrt, pi, simplify, N, symbols, solve, Eq
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x = symbols('x', positive=True)
V_h = lambda r, H: r**2*pi*H
F_h = lambda r, H: 2*r**2*pi + 2*r*pi*H
V_k = lambda r, H: r**2*pi*H/3
F_k = lambda r, s: r**2*pi + r*pi*s
V_g = lambda Rr: R(4, 3)*Rr**3*pi
F_g = lambda Rr: 4*Rr**2*pi
V_cs = lambda Rr, r, H: H*pi/3*(Rr**2 + Rr*r + r**2)

# --- terepküldetés: I. a hengeres tartály (r = 4 m, H = 9 m)
chk("I-V", V_h(4, 9), 144*pi)
chk("I-liter", N(V_h(4, 9)*1000, 10), 452389.342, 1e-2)
chk("I-M", 2*4*pi*9, 72*pi)
chk("I-F", F_h(4, 9), 104*pi)
chk("I-tm", 2*4*9, 72)
# --- II. a kúpos tölcsér (r = 6 m, H = 8 m)
chk("II-s", sqrt(6**2 + 8**2), 10)
chk("II-M", 6*pi*10, 60*pi)
chk("II-F", F_k(6, 10), 96*pi)
chk("II-V", V_k(6, 8), 96*pi)
chk("II-fi", 360*R(6, 10), 216)
# --- II/b: a tölcsér alsó darabja csonkakúp (a magasság felénél vágva)
chk("II-kis-r", 6*R(1, 2), 3)
chk("II-csonka", V_cs(6, 3, 4), 84*pi)
chk("II-ellenorzes", V_k(6, 8) - V_k(3, 4), 84*pi)
# --- III. a gömbszelence (R = 3 m) és a torony (henger + félgömb)
chk("III-F", F_g(3), 36*pi)
chk("III-V", V_g(3), 36*pi)
chk("III-sik", 3, 3)
chk("III-torony-V", V_h(3, 7) + V_g(3)/2, 81*pi)
chk("III-torony-F", 2*3*pi*7 + F_g(3)/2 + 3**2*pi, 69*pi)
# --- Vészterem
chk("D1", V_h(5, 6), 150*pi)
chk("D2", F_h(3, 7), 60*pi)
chk("D3-s", sqrt(9**2 + 12**2), 15);   chk("D3-F", F_k(9, 15), 216*pi)
chk("D4", V_k(6, 10), 120*pi)
chk("D5", V_g(6), 288*pi)
chk("D6", solve(Eq(F_g(x), 144*pi), x)[0], 6)
chk("D7", V_cs(8, 5, 9), 3*pi*129)
chk("D8", solve(Eq(V_h(x, 10), 250*pi), x)[0], 5)
chk("K1-r", solve(Eq(F_h(x, 2*x), 96*pi), x)[0], 4)
chk("K1-V", V_h(4, 8), 128*pi)
chk("K2-s", solve(Eq(F_k(5, x), 90*pi), x)[0], 13)
chk("K2-H", sqrt(13**2 - 5**2), 12)
chk("K3", V_h(4, 12) - V_h(3, 12), 84*pi)
chk("K4-H", solve(Eq(V_cs(6, 4, x), 152*pi), x)[0], 6)
chk("K5", V_h(2, 10) + V_g(2)/2, 40*pi + R(16, 3)*pi)
chk("K6", V_g(2*x)/V_g(x), 8)
chk("N1-r", solve(Eq(V_k(x, 3*x), 64*pi), x)[0], 4)
chk("N1-H", 3*4, 12)
chk("N2", V_k(6, 8) + V_h(6, 5), 276*pi)
chk("N3-arany", V_g(x)/V_h(x, 2*x), R(2, 3))
assert not E, E
print("sympy önteszt: OK")


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'

FO = "tananyag-forgastestek.html"
HE = "tananyag-henger.html"
HF = "tananyag-henger-felszin-terfogat.html"
KU = "tananyag-kup.html"
KF = "tananyag-kup-felszin-terfogat.html"
SM = "tananyag-sikmetszetek.html"
CK = "tananyag-csonkakup.html"
GO = "tananyag-gomb.html"
GF = "tananyag-gomb-felszin-terfogat.html"
OT = "tananyag-osszetett-testek.html"

# ==================================================================== F4

OSSZ = [
 ("Forgástestek — a keletkezés", [
  '<p>Minden forgástest egy <b>síkidom</b> és egy <b>tengely</b> párosából születik '
  '(' + h(FO, "def-forgastest") + '):</p>'
  '<table class="tt-table">'
  '<tr><th>Síkidom</th><th>Tengely</th><th>A keletkező test</th></tr>'
  '<tr><td>téglalap</td><td>az egyik oldala</td><td><b>henger</b></td></tr>'
  '<tr><td>derékszögű háromszög</td><td>az egyik <b>befogó</b></td><td><b>kúp</b></td></tr>'
  '<tr><td>derékszögű háromszög</td><td>az <b>átfogó</b></td>'
  '<td>két kúp közös alaplappal</td></tr>'
  '<tr><td>félkör</td><td>az átmérője</td><td><b>gömb</b></td></tr>'
  '<tr><td>derékszögű trapéz</td><td>a merőleges szára</td><td><b>csonkakúp</b></td></tr>'
  '</table>'
  '<p>⚠️ A tengely megválasztása <b>nem</b> mindegy: a téglalap két oldala körül '
  'forgatva két <b>különböző</b> térfogatú henger keletkezik, mert a sugár '
  'négyzetesen, a magasság csak lineárisan számít.</p>',
 ]),

 ("Metszetek", [
  '<p><b>Tengelyre merőleges</b> metszet: mindig <b>kör</b> '
  '(' + h(FO, "tetel-meroleges-metszet") + '). Hengernél az alapkörrel '
  '<b>egybevágó</b>, kúpnál <b>hasonló</b> — a hasonlóság aránya a <b>csúcstól</b> '
  'mért magasságok aránya (' + h(SM, "tetel-parhuzamos-metszet") + ').</p>'
  '<p><b>Tengelymetszet</b> (a tengelyt <b>tartalmazó</b> síkkal, '
  + h(SM, "tetel-tengelymetszet") + '):</p>'
  '<table class="tt-table">'
  '<tr><th>Test</th><th>A tengelymetszete</th><th>Területe</th></tr>'
  '<tr><td>henger</td><td>téglalap ($2r\\times H$)</td><td>$T=2r\\,H$</td></tr>'
  '<tr><td>kúp</td><td>egyenlő szárú háromszög (alap $2r$, szárak $s$)</td>'
  '<td>$T=r\\,H$</td></tr>'
  '<tr><td>csonkakúp</td><td>egyenlő szárú trapéz</td><td>$T=(R+r)H$</td></tr>'
  '<tr><td>gömb</td><td><b>főkör</b> ($R$ sugarú)</td><td>$T=R^2\\pi$</td></tr>'
  '</table>'
  '<p>Ha a tengelymetszet <b>négyzet</b>, a henger <b>egyenlő oldalú</b> ($H=2r$, '
  + h(HE, "def-egyenlo-oldalu-henger") + '); ha <b>szabályos háromszög</b>, a kúp '
  'egyenlő oldalú ($s=2r$, $H=r\\sqrt3$, ' + h(KU, "def-egyenlo-oldalu-kup") + ').</p>',
 ]),

 ("A négy test képlete", [
  '<table class="tt-table">'
  '<tr><th>Test</th><th>Felszín</th><th>Térfogat</th><th>Kulcs-összefüggés</th></tr>'
  '<tr><td><a href="' + HF + '#tetel-henger-felszin">henger</a></td>'
  '<td>$F=2r\\pi(r+H)$</td><td>$V=r^2\\pi H$</td><td>$s=H$</td></tr>'
  '<tr><td><a href="' + KF + '#tetel-kup-felszin">kúp</a></td>'
  '<td>$F=r\\pi(r+s)$</td><td>$V=\\dfrac{r^2\\pi H}{3}$</td>'
  '<td>$s^2=r^2+H^2$</td></tr>'
  '<tr><td><a href="' + CK + '#tetel-csonkakup-felszin">csonkakúp</a></td>'
  '<td>$F=R^2\\pi+r^2\\pi+(R+r)\\pi s$</td>'
  '<td>$V=\\dfrac{H\\pi}{3}\\left(R^2+Rr+r^2\\right)$</td>'
  '<td>$s^2=H^2+(R-r)^2$</td></tr>'
  '<tr><td><a href="' + GF + '#tetel-gomb-felszin">gömb</a></td>'
  '<td>$F=4R^2\\pi$</td><td>$V=\\dfrac{4R^3\\pi}{3}$</td>'
  '<td>egyetlen adat: $R$</td></tr>'
  '</table>'
  '<p><b>Jelölések:</b> $r$ az alapkör sugara (csonkakúpnál a <b>felső</b>, $R$ az '
  'alsó; gömbnél $R$ maga a sugár) · $H$ a testmagasság · $s$ az <b>alkotó</b> · '
  '$B=r^2\\pi$ az alapterület · $M$ a palást területe.</p>'
  '<p><b>A palást külön:</b> henger $M=2r\\pi H$ · kúp $M=r\\pi s$ · csonkakúp '
  '$M=(R+r)\\pi s$ · a kúp hálójában a körcikk szöge '
  '$\\varphi=360^\\circ\\cdot\\dfrac rs$ (' + h(KU, "tetel-kup-halo") + ').</p>',
 ]),

 ("Összetett és üreges testek", [
  '<p><b>Térfogat:</b> a részek térfogata <b>összeadódik</b> '
  '(' + h(OT, "tetel-osszetett-terfogat") + '); üreges testnél <b>kivonunk</b>.</p>'
  '<p><b>Felszín:</b> csak a <b>kívülről látható</b> felületek számítanak — az '
  'illeszkedő lapok <b>kiesnek</b> (' + h(OT, "tetel-osszetett-felszin") + '). A '
  'biztos módszer: rajzold le, és satírozd be, ami látszik.</p>'
  '<p>A cső felszíne <b>négy</b> darabból áll: két körgyűrű, a külső és a '
  '<b>belső</b> palást.</p>'
  '<p><b>Fél-testek:</b> félgömb térfogata $\\frac23R^3\\pi$, görbült felülete '
  '$2R^2\\pi$ — az alapköre csak akkor számít, ha kívülről látszik.</p>',
 ]),

 ("A gömb és a sík", [
  '<p>A helyzetet a középpont–sík távolság ($d$) és a sugár ($R$) viszonya dönti el '
  '(' + h(GO, "tetel-gomb-sik") + '):</p>'
  '<table class="tt-table">'
  '<tr><th>Feltétel</th><th>Helyzet</th><th>Közös pontok</th></tr>'
  '<tr><td>$d &gt; R$</td><td>elkerüli</td><td>nincs</td></tr>'
  '<tr><td>$d = R$</td><td><b>érinti</b></td><td>pontosan egy</td></tr>'
  '<tr><td>$d &lt; R$</td><td>metszi</td><td>egy kör</td></tr>'
  '</table>'
  '<p>Az <b>érintősík</b> merőleges az érintési pontba húzott sugárra '
  '(' + h(GO, "tetel-erintosik") + ').</p>',
 ]),

 ("A hét leggyakoribb hiba", [
  '<div class="brief"><p>🚨 <b>1)</b> A palástba a <b>magasságot</b> írják az '
  '<b>alkotó</b> helyett ($M=r\\pi H$) — a felületen az alkotó, a belsejében a '
  'magasság. &nbsp; <b>2)</b> A henger felszínébe csak <b>egy</b> alapkört tesznek — '
  'kettő van (kivéve, ha a feladat nyitott edényről szól). &nbsp; <b>3)</b> A háló '
  'téglalapjának oldalára $2r$-t írnak $2r\\pi$ helyett. &nbsp; <b>4)</b> Az egyenlő '
  'oldalú hengernél $H=r$-rel számolnak $H=2r$ helyett. &nbsp; <b>5)</b> A '
  'csonkakúp derékszögű háromszögében $R+r$ szerepel $R-r$ helyett — és '
  '$R^2+Rr+r^2\\ne(R+r)^2$. &nbsp; <b>6)</b> A gömbnél az <b>átmérőt</b> '
  'helyettesítik a sugár helyére; a kitevőket a <b>mértékegység</b> ellenőrzi '
  '(felszín → négyzet, térfogat → köb). &nbsp; <b>7)</b> Összetett testnél a '
  'felszíneket <b>összeadják</b> — az illeszkedő lapok nem látszanak.</p></div>',
 ]),

 ("Mit hol találsz?", [
  '<div class="brief"><p>📚 <b>Tananyag:</b> '
  '<a href="' + FO + '">forgástestek</a> · '
  '<a href="' + HE + '">henger</a> · '
  '<a href="' + HF + '">henger F és V</a> · '
  '<a href="' + KU + '">kúp</a> · '
  '<a href="' + KF + '">kúp F és V</a> · '
  '<a href="' + SM + '">síkmetszetek</a> · '
  '<a href="' + CK + '">csonkakúp</a> · '
  '<a href="' + GO + '">gömb</a> · '
  '<a href="' + GF + '">gömb F és V</a> · '
  '<a href="' + OT + '">összetett testek</a>.</p>'
  '<p>🎯 <b>Gyakorlás:</b> '
  '<a href="feladatok-henger.html">henger</a> · '
  '<a href="feladatok-kup.html">kúp és csonkakúp</a> · '
  '<a href="feladatok-gomb.html">gömb és összetett testek</a> — majd indulj '
  '<a href="terepkuldetes.html">Az Átalakulás Kamrájába</a>!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Átalakulás-térkép — a témakör egy lapon",
    cim_tiszta="Átalakulás-térkép", itt="Átalakulás-térkép",
    alcim="A forgástestek minden definíciója, képlete és tipikus csapdája egy helyen — "
          "ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-gomb.html", "Feladatok — a gömb és az összetett testek"),
    kovetkezo=("terepkuldetes.html", "Az Átalakulás Kamrája"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

from fgy_common import cards, oldal, w

SVG_TOROY = svg_osszetett("henger-felgomb", w=260, h=280,
    leiras="A kondenzátortorony: hengeres test félgömb tetővel")

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Az Átalakulás Kamrája három szerkezetből áll: egy hengeres '
         '<b>gyűjtőtartályból</b>, egy kúpos <b>tölcsérből</b>, amely a párát a '
         'tartályba vezeti, és egy gömb alakú <b>szelencéből</b>, amelyben a kész '
         'kristály ül. A műszereink csak hosszakat mérnek — a kapacitást, a '
         'felületet és a metszeteket nekünk kell kiszámolnunk.'),
   '<p>Három fázis, három szerkezet. Minden fázis végén írd fel a végeredményt '
   '<b>pontos alakban</b> ($\\pi$-vel), és csak ott adj közelítést, ahol a feladat '
   'kifejezetten kéri. A számolás menetét is jegyezd fel — a Kamra naplója '
   'ellenőrizni fogja.</p>'
   '<p><b>Amit vinned kell:</b> a négy test felszín- és térfogatképlete, a kúp '
   'derékszögű háromszöge, a hasonlóság $k$–$k^2$–$k^3$ szabálya és a '
   'mértékegység-váltás ($1\\ \\text{m}^3=1000$ liter).</p>',
 ]),

 ("I. fázis — A gyűjtőtartály", [
   '<p>A hengeres gyűjtőtartály alapkörének sugara $4$ m, magassága $9$ m.</p>'
   '<ol class="reszfeladatok">'
   '<li>Hány <b>liter</b> párakondenzátum fér bele? (Egészre kerekítve.)</li>'
   '<li>Mekkora a <b>palástja</b>, és mekkora a teljes <b>felszíne</b>?</li>'
   '<li>A tartályt függőlegesen, a tengelyén át kettévágjuk. Milyen síkidomot '
   'kapunk, és mekkora a területe?</li>'
   '<li>Mekkora annak a téglalapnak a két oldala, amelyből a palástot '
   'hajlítottuk?</li>'
   '</ol>',
 ]),

 ("II. fázis — A tölcsér", [
   '<p>A kúpos tölcsér alapkörének sugara $6$ m, magassága $8$ m.</p>'
   '<ol class="reszfeladatok">'
   '<li>Mekkora az <b>alkotója</b>?</li>'
   '<li>Mekkora a palástja és a felszíne?</li>'
   '<li>Mekkora a térfogata?</li>'
   '<li>A tölcsér palástját egyetlen lemezből vágjuk ki. Mekkora <b>középponti '
   'szögű</b> körcikk kell hozzá, és mekkora a körcikk sugara?</li>'
   '<li>A tölcsért a magassága <b>felénél</b> elvágjuk, és a felső darabot '
   'kicseréljük. Mekkora a megmaradó alsó darab (csonkakúp) térfogata? Ellenőrizd '
   '<b>két</b> úton!</li>'
   '</ol>',
 ]),

 ("III. fázis — A szelence és a torony", [
   '<p>A gömb alakú kristályszelence sugara $3$ m.</p>'
   '<ol class="reszfeladatok">'
   '<li>Mekkora a felszíne és a térfogata?</li>'
   '<li>Egy vízszintes vezérlősík a szelence középpontjától $3$ m-re halad. Milyen '
   'helyzetben van a gömbfelülethez képest? Hány közös pontjuk van?</li>'
   '<li>A kész <b>kondenzátortornyot</b> egy $3$ m sugarú, $7$ m magas hengerből és '
   'a rá épített, azonos sugarú félgömb tetőből állítjuk össze. Mekkora a '
   'térfogata?</li>'
   '<li>Mekkora a torony <b>teljes külső</b> felülete (az alsó körlappal együtt, mert '
   'a torony lábakon áll)?</li>'
   '</ol>',
   abra(SVG_TOROY, 'A kondenzátortorony: hengeres test félgömb tetővel.'),
   brief('<b>Medúza:</b> Ha mind a három fázis stimmel, a Kamra üzemkész. A '
         'megoldásokat a tanárod ellenőrzi — a kulcs nem kerül a hálózatra.',
         outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="Az Átalakulás Kamrája",
    cim_tiszta="Az Átalakulás Kamrája", itt="Terepküldetés",
    alcim="Három fázis, három szerkezet: hengeres tartály, kúpos tölcsér és gömb alakú "
          "szelence. Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Átalakulás-térkép"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h

DR_A = [
 ("Egy henger alapkörének sugara $5$ cm, magassága $6$ cm. Mekkora a térfogata?", None,
  "$V=25\\pi\\cdot6=150\\pi\\ \\text{cm}^3$."),
 ("Egy henger alapkörének sugara $3$ cm, magassága $7$ cm. Mekkora a felszíne?", None,
  "$F=2r\\pi(r+H)=6\\pi\\cdot10=60\\pi\\ \\text{cm}^2$."),
 ("Egy kúp alapkörének sugara $9$ cm, magassága $12$ cm. Mekkora az alkotója és a "
  "felszíne?", None,
  "$s=\\sqrt{81+144}=15$ cm, ezért $F=81\\pi+9\\cdot15\\pi=216\\pi\\ \\text{cm}^2$."),
 ("Egy kúp alapkörének sugara $6$ cm, magassága $10$ cm. Mekkora a térfogata?", None,
  "$V=\\frac{36\\pi\\cdot10}{3}=120\\pi\\ \\text{cm}^3$."),
 ("Egy gömb sugara $6$ cm. Mekkora a térfogata?", None,
  "$V=\\frac{4\\cdot216\\pi}{3}=288\\pi\\ \\text{cm}^3$."),
 ("Egy gömb felszíne $144\\pi\\ \\text{cm}^2$. Mekkora a sugara?", None,
  "$4R^2\\pi=144\\pi$, tehát $R^2=36$ és $R=6$ cm."),
 ("Egy csonkakúp alapkörének sugara $R=8$ cm, fedőköréé $r=5$ cm, magassága "
  "$H=9$ cm. Mekkora a térfogata?", None,
  "$V=\\frac{9\\pi}{3}(64+40+25)=3\\pi\\cdot129=387\\pi\\ \\text{cm}^3$."),
 ("Egy henger térfogata $250\\pi\\ \\text{cm}^3$, magassága $10$ cm. Mekkora az "
  "alapkörének sugara?", None,
  "$r^2\\pi\\cdot10=250\\pi$, tehát $r^2=25$ és $r=5$ cm."),
]

DR_K = [
 ("Egy henger felszíne $96\\pi\\ \\text{cm}^2$, és a magassága az átmérővel egyenlő. "
  "Mekkora a térfogata?", None,
  "A feltétel szerint $H=2r$, tehát $F=6r^2\\pi=96\\pi$, ahonnan $r=4$ cm és "
  "$H=8$ cm. Így $V=16\\pi\\cdot8=128\\pi\\ \\text{cm}^3$."),
 ("Egy kúp felszíne $90\\pi\\ \\text{cm}^2$, alapkörének sugara $5$ cm. Mekkora az "
  "alkotója és a magassága?", None,
  "$5\\pi(5+s)=90\\pi$, tehát $5+s=18$ és $s=13$ cm. Innen "
  "$H=\\sqrt{169-25}=12$ cm."),
 ("Egy $12$ cm hosszú cső külső sugara $4$ cm, belső sugara $3$ cm. Mekkora az anyag "
  "térfogata?", None,
  "$V=16\\pi\\cdot12-9\\pi\\cdot12=192\\pi-108\\pi=84\\pi\\ \\text{cm}^3$."),
 ("Egy csonkakúp alapkörének sugara $R=6$ cm, fedőköréé $r=4$ cm, térfogata "
  "$152\\pi\\ \\text{cm}^3$. Mekkora a magassága?", None,
  "$\\frac{H\\pi}{3}(36+24+16)=\\frac{76H\\pi}{3}=152\\pi$, tehát "
  "$H=\\frac{152\\cdot3}{76}=6$ cm."),
 ("Egy hengeres tartály ($r=2$ cm, $H=10$ cm) tetején azonos sugarú félgömb van. "
  "Mekkora a test térfogata?", None,
  "A henger $4\\pi\\cdot10=40\\pi$, a félgömb "
  "$\\frac12\\cdot\\frac{4\\cdot8\\pi}{3}=\\frac{16\\pi}{3}$, tehát "
  "$V=40\\pi+\\frac{16\\pi}{3}=\\frac{136\\pi}{3}\\ \\text{cm}^3$."),
 ("Egy gömb sugarát megduplázzuk. Hányszorosára nő a térfogata, és hányszorosára a "
  "felszíne?", None,
  "A térfogat a <b>nyolcszorosára</b> nő (a sugár köbön áll), a felszín a "
  "<b>négyszeresére</b> (a sugár négyzeten áll)."),
]

DR_N = [
 ("Egy kúp magassága az alapkör sugarának <b>háromszorosa</b>, a térfogata "
  "$64\\pi\\ \\text{cm}^3$. Mekkora a sugara és a magassága?", None,
  "$\\frac{r^2\\pi\\cdot3r}{3}=r^3\\pi=64\\pi$, tehát $r=4$ cm és $H=12$ cm."),
 ("Egy hengerre ($r=6$ cm, $H=5$ cm) kúp alakú tetőt teszünk ($r=6$ cm, $H=8$ cm). "
  "Mekkora a keletkező test térfogata?", None,
  "A kúp $\\frac{36\\pi\\cdot8}{3}=96\\pi$, a henger $36\\pi\\cdot5=180\\pi$, tehát "
  "$V=276\\pi\\ \\text{cm}^3$."),
 ("Igazold, hogy a gömb térfogata a köré írt henger térfogatának pontosan a "
  "<b>kétharmada</b>!", None,
  "A köré írt henger alapköre a főkör ($r=R$), a magassága az átmérő ($H=2R$), ezért "
  "$V_{\\text{henger}}=R^2\\pi\\cdot2R=2R^3\\pi$. A gömbé $\\frac{4R^3\\pi}{3}$, "
  "tehát az arány $\\frac{4R^3\\pi/3}{2R^3\\pi}=\\frac23$ — ez Arkhimédész tétele."),
]

body_dr = [
 '    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(DR_A, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(DR_K, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(DR_N, "nehez", "nehez"),
]

oldal(**T, fajl="feladatok-hazi.html", cim="Vészterem",
      alcim="Rövid, vegyes gyakorlósor a forgástestekhez — házi feladatnak és dolgozat "
            "előtti bemelegítésnek. A végeredmény minden feladatnál lenyitható!",
      sections_html="\n".join(body_dr),
      prev="index.html", prevc="Témakör Főhadiszállása",
      nxt="osszefoglalo.html", nxtc="Átalakulás-térkép")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5

def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = [
 kartya("tananyag-forgastestek.html", "Forgástestek",
        "A forgatás mint művelet, a négy alapeset, a tengelymetszet és a merőleges metszet"),
 kartya("tananyag-henger.html", "A henger és elemei",
        "Alapkörök, palást, alkotó, tengely; a háló és az egyenlő oldalú henger"),
 kartya("tananyag-henger-felszin-terfogat.html", "A henger felszíne és térfogata",
        "A palást a hálóból, a $F=2r\\pi(r+H)$ alak, fordított feladatok és a literek"),
 kartya("tananyag-kup.html", "A kúp és elemei",
        "A kúp derékszögű háromszöge, a körcikkes háló és az egyenlő oldalú kúp"),
 kartya("tananyag-kup-felszin-terfogat.html", "A kúp felszíne és térfogata",
        "A palást levezetése a körcikkből, a harmadolás és a fordított feladatok"),
 kartya("tananyag-sikmetszetek.html", "A henger és a kúp síkmetszetei",
        "Tengelymetszet és párhuzamos metszet: alak, hasonlósági arány és terület"),
 kartya("tananyag-csonkakup.html", "A csonkakúp",
        "Keletkezés, a jellemző derékszögű háromszög és a háromtagú térfogatképlet"),
 kartya("tananyag-gomb.html", "A gömbfelület és a gömb",
        "Főkör, a sík és a gömbfelület kölcsönös helyzete, az érintősík"),
 kartya("tananyag-gomb-felszin-terfogat.html", "A gömb felszíne és térfogata",
        "A két képlet, Arkhimédész 2:3 aránya és a valós számítások"),
 kartya("tananyag-osszetett-testek.html", "Összetett és üreges testek",
        "Az összeadás és a kivonás elve, a felszín buktatói — a témakör képlettárával"),
 kartya("feladatok-henger.html", "🏋️ A henger — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker — forgatás, háló, felszín, térfogat"),
 kartya("feladatok-kup.html", "🏋️ A kúp és a csonkakúp — feladatok",
        "Alkotó és magasság, a körcikkes háló, síkmetszetek és a csonkakúp képletei"),
 kartya("feladatok-gomb.html", "🏋️ A gömb és az összetett testek — feladatok",
        "A sík és a gömb helyzete, a két gömbképlet, csövek, tornyok és fúrt testek"),
 kartya("feladatok-hazi.html", "🕹️ Vészterem — házi feladatok",
        "A teljes témakört lefedő rövid házi feladatsor, dolgozat előtti bemelegítésnek"),
 kartya("terepkuldetes.html", "🎯 Az Átalakulás Kamrája",
        "Háromfázisú küldetés — a gyűjtőtartály, a kúpos tölcsér és a gömbszelence"),
 kartya("osszefoglalo.html", "📇 Átalakulás-térkép",
        "Minden definíció, képlet és tipikus csapda egy helyen — dolgozat előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Forgástestek | 3e | Szvetkó matek</title>
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
  <span class="itt">Forgástestek</span>
</nav>
<div class="hero">
  <h1>Forgástestek</h1>
  <p class="alcim">A hengertől és a kúptól a csonkakúpon át a gömbig és az összetett
  testekig — minden test egyetlen síkidom megforgatásából születik.</p>
  <div class="meta-sor"><span class="chip ora">18 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🔷 <b>Szektor 02 — Az Átalakulás Kamrája.</b> Kiképző:
  <b>Medúza</b>. Ebben a kamrában a Kristálypára már nem szögletesen csapódik ki, hanem
  <b>pörög</b> — és ami pörög, az gömbölyű nyomot hagy. Medúza megmutatja, hogyan lehet
  minden ilyen testet ugyanazzal a két adattal — a <b>sugárral</b> és a <b>magassággal</b> —
  felmérni, és mikor kell melléjük az <b>alkotó</b>.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🛢️ Forgástestek és a henger — Medúza</h3>
    <div class="racs">
''' + "\n".join(K[0:3]) + '''
    </div>

    <h3>🔻 A kúp és a csonkakúp — Medúza</h3>
    <div class="racs">
''' + "\n".join(K[3:7]) + '''
    </div>

    <h3>🔮 A gömb és az összetett testek — Medúza</h3>
    <div class="racs">
''' + "\n".join(K[7:10]) + '''
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
''' + "\n".join(K[10:14]) + '''
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
''' + K[14] + '''
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
''' + K[15] + '''
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> altémánként előbb a tananyag-egységek sorban,
    utána a hozzá tartozó feladatgyűjtemény; a témakör végén az Átalakulás-térkép, majd
    Az Átalakulás Kamrája küldetés. A Vészterem házi bármikor jöhet.</p>
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
