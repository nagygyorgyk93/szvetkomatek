# -*- coding: utf-8 -*-
"""3e/04 — A blokk: vektorok a sikban (A1), vektorok a terben koordinatakkal (A2).
Mentor: Crni Grom (Meduza tolmacsol). Kuldetes: A Kiralyi Iranyitotu."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import (svg_vektorok_sik, svg_vetulet, svg_ter_koord,
                         KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, HALVANY, TINTA, LILA)

T = dict(tagozat="3e", mappa="04-vektorok", temakor="Vektorok")
FGY = "feladatok-vektorok.html"
KUL = "A Királyi Irányítótű"
E1 = "../../1e/05-geometria/tananyag-vektorok.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Matrix, sqrt, cos, sin, pi, Rational, simplify, N, acos, deg, atan
E = []
def chk(n, g, w, tur=1e-9):
    if hasattr(g, "shape"):
        ok = all(simplify(u - v) == 0 for u, v in zip(g, w)) and g.shape == Matrix(w).shape
    else:
        kul = simplify(g - w)
        ok = kul == 0 or abs(float(N(kul))) <= tur
    if not ok:
        E.append((n, g, w))

def V(*k):
    return Matrix(k)

# A1 — gyors kérdés: merőleges 3 és 4 hosszú vektor összege
chk("A1-kviz1", sqrt(3**2 + 4**2), 5)
# A1 — repülő + szél
chk("A1-repulo", round(float(sqrt(200**2 + 50**2)), 1), 206.2, 1e-9)
chk("A1-repulo-szog", round(float(deg(atan(Rational(50, 200)))), 0), 14)
# A1 — szabályos hatszög (O origó, A=(1;0), pozitív körüljárás)
r3 = sqrt(3)
A, B, C, D, Ee, F, O = (V(1, 0), V(Rational(1, 2), r3/2), V(-Rational(1, 2), r3/2), V(-1, 0),
                        V(-Rational(1, 2), -r3/2), V(Rational(1, 2), -r3/2), V(0, 0))
AB = B - A
for nev, v in (("OC", C - O), ("FO", O - F), ("ED", D - Ee)):
    chk("hatszog-egyenlo-" + nev, v, AB)
for nev, v in (("BA", A - B), ("CO", O - C), ("OF", F - O), ("DE", Ee - D)):
    chk("hatszog-ellentett-" + nev, v, -AB)
chk("hatszog-c", (B - A) + (C - B), C - A)
chk("hatszog-d", 2*((O - B) - (O - C)), D - A)
a_, b_ = A - O, B - O
chk("hatszog-e1", B - A, b_ - a_)
chk("hatszog-e2", C - A, b_ - 2*a_)
# összevonás: 3(a - 2b) - 2(a - b) = a - 4b  (két tetszőleges vektorral)
p, q = V(2, 5), V(-1, 3)
chk("osszevonas", 3*(p - 2*q) - 2*(p - q), p - 4*q)
# felezőpont
chk("felezopont", (V(4, 1) + V(0, 5))/2, V(2, 3))
# skaláris vetület
chk("vet-60", 6*cos(pi/3), 3); chk("vet-120", 6*cos(2*pi/3), -3); chk("vet-90", 6*cos(pi/2), 0)
chk("vet-35", round(float(5*cos(35*pi/180)), 2), 4.10)
chk("vet-35-rad", round(float(5*math.cos(35)), 2), -4.52)
# A2 — koordináták
Ap, Bp = V(2, -1, 3), V(5, 1, -1)
chk("A2-maxi", Bp - Ap, V(3, 2, -4))
chk("A2-kviz1", V(-2, 5, 3) - V(1, 4, -2), V(-3, 1, 5))
chk("A2-kviz1-osszeg", V(-2, 5, 3) + V(1, 4, -2), V(-1, 9, 1))
a3, b3 = V(2, -1, 3), V(1, 4, -2)
chk("A2-osszeg", a3 + b3, V(3, 3, 1)); chk("A2-kulonbseg", a3 - b3, V(1, -5, 5))
chk("A2-3a", 3*a3, V(6, -3, 9)); chk("A2-2a-3b", 2*a3 - 3*b3, V(1, -14, 12))
chk("A2-parh", V(-4, 2, -6), -2*a3)
assert not (Rational(4, 2) == Rational(-2, -1) == Rational(5, 3)), "nem parhuzamos"
chk("A2-hossz", sqrt(2**2 + 1 + 2**2), 3)
chk("A2-egyseg", (V(2, -1, 2)/3).norm(), 1)
chk("A2-tav", (V(3, 1, -3) - V(1, -2, 3)).norm(), 7)
chk("A2-teglatest", sqrt(3**2 + 4**2 + 2**2), sqrt(29))
chk("A2-teglatest-alap", sqrt(3**2 + 4**2), 5)
Pa, Pb, Pd = V(1, 2, 0), V(4, 3, 1), V(2, -1, 3)
Pc = Pb + Pd - Pa
chk("par-C", Pc, V(5, 0, 4)); chk("par-DC", Pc - Pd, Pb - Pa)
chk("par-AB", (Pb - Pa).norm(), sqrt(11)); chk("par-AD", (Pd - Pa).norm(), sqrt(19))
chk("par-K", round(float(2*(sqrt(11) + sqrt(19))), 2), 15.35)
chk("par-rossz", Pa + Pb - Pd, V(3, 6, -2))
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
R3 = math.sqrt(3)
SVG_EGYENLO = svg_vektorok_sik(
    [((0.5, 0.6), (3.5, 1.6), KEK, "a"), ((4.2, 2.4), (7.2, 3.4), KEK, "a"),
     ((10.6, 1.6), (7.6, 0.6), PIROS, "−a"), ((1.0, 3.6), (1.0, 2.2), SZURKE, "c")],
    xr=(0, 11), yr=(0, 4), egyseg=42,
    leiras="Két egyenlő vektor (eltolással fedésbe hozhatók), az ellentettjük és egy "
           "más irányú vektor négyzetrácson")
SVG_OSSZEADAS = svg_vektorok_sik(
    [((0.5, 0.5), (3.5, 1.5), KEK, "a"), ((3.5, 1.5), (4.5, 3.5), BOROSTYAN, "b", {"tav": -14}),
     ((0.5, 0.5), (4.5, 3.5), ZOLD, "a + b", {"tav": 20, "dx": -6}),
     ((6.6, 0.4), (10.8, 1.4), KEK, "a", {"tav": -14}), ((6.6, 0.4), (7.8, 3.0), BOROSTYAN, "b"),
     ((6.6, 0.4), (12.0, 4.0), ZOLD, "a + b", {"tav": -16, "dx": 40, "dy": -26}),
     ((7.8, 3.0), (10.8, 1.4), PIROS, "a − b", {"tav": 14, "dx": -30, "dy": -17})],
    szakaszok=[((10.8, 1.4), (12.0, 4.0), SZURKE, "4 3"), ((7.8, 3.0), (12.0, 4.0), SZURKE, "4 3")],
    feliratok=[((2.5, 4.55), "háromszög-szabály"), ((9.3, 4.55), "paralelogramma-szabály")],
    xr=(0, 12.6), yr=(0, 4.9), egyseg=44,
    leiras="Vektorok összeadása háromszög-szabállyal és paralelogramma-szabállyal; a "
           "paralelogramma másik átlója a különbség")
_H = [(2 * math.cos(k * math.pi / 3), 2 * math.sin(k * math.pi / 3)) for k in range(6)]
SVG_HATSZOG = svg_vektorok_sik(
    [(_H[0], _H[1], KEK, "")],
    szakaszok=[(_H[i], _H[(i + 1) % 6], TINTA, None) for i in range(6)]
              + [((0, 0), _H[i], HALVANY, "4 3") for i in range(6)],
    pontok=list(zip(_H + [(0, 0)], "ABCDEFO", [14, 10, -10, -14, -10, 10, 0],
                    [5, -7, -7, 5, 19, 19, -9])),
    xr=(-2.5, 2.5), yr=(-2.15, 2.15), egyseg=62, racs=False,
    leiras="Szabályos hatszög O középponttal, kiemelve az AB vektor")
SVG_SKALAR = svg_vektorok_sik(
    [((0.5, 1.0), (2.5, 2.0), KEK, "a"), ((3.5, 0.5), (7.5, 2.5), ZOLD, "2a"),
     ((11.5, 2.5), (8.5, 1.0), PIROS, "−1,5a")],
    xr=(0, 12), yr=(0, 3.2), egyseg=40,
    leiras="Egy vektor, a kétszerese és a mínusz egy és félszerese")
SVG_VET_HEGY = svg_vetulet(55, leiras="A b vektor skaláris vetülete az a irányára hegyesszög "
                                      "esetén pozitív")
SVG_VET_TOMPA = svg_vetulet(125, leiras="A b vektor skaláris vetülete az a irányára tompaszög "
                                        "esetén negatív")
_c45 = 2.6 * math.cos(math.pi / 4)
SVG_KVIZ_SZOG = svg_vektorok_sik(
    [((0.5, 0.5), (4.5, 0.5), KEK, "a", {"tav": -16}),
     ((4.5, 0.5), (4.5 + _c45, 0.5 + _c45), BOROSTYAN, "b", {"tav": 16})],
    xr=(0, 7.2), yr=(0, 3), egyseg=40,
    leiras="Két vektor fej–láb helyzetben: a második az első végpontjából indul, 45 fokos "
           "emelkedéssel")
_c60, _s60 = 2.4 * math.cos(math.pi / 3), 2.4 * math.sin(math.pi / 3)
SVG_MAXI_SZOG = svg_vektorok_sik(
    [((0.5, 0.5), (4.0, 0.5), KEK, "a", {"tav": -16}),
     ((4.0, 0.5), (4.0 + _c60, 0.5 + _s60), BOROSTYAN, "b", {"tav": 16}),
     ((7.2, 0.5), (10.7, 0.5), KEK, "a", {"tav": -16}),
     ((7.2, 0.5), (7.2 + _c60, 0.5 + _s60), BOROSTYAN, "b", {"tav": 16})],
    szogivek=[((4.0, 0.5), (0.5, 0.5), (4.0 + _c60, 0.5 + _s60), PIROS, "120° ✘"),
              ((7.2, 0.5), (10.7, 0.5), (7.2 + _c60, 0.5 + _s60), ZOLD, "60° ✔")],
    feliratok=[((3.0, 3.35), "fej–láb helyzet", PIROS), ((9.0, 3.35), "közös kezdőpont", ZOLD)],
    xr=(0, 11.2), yr=(0, 3.7), egyseg=40,
    leiras="Maxi hibája: fej–láb helyzetben a mellékszöget, 120 fokot olvasta le; közös "
           "kezdőpontba tolva a két vektor szöge 60 fok")
SVG_TER_PONT = svg_ter_koord((3, 4, 2), egysegvektorok=False, helyvektor=False)
SVG_TER_VEKTOR = svg_ter_koord((3, 4, 2), leiras="A P(3; 4; 2) pont helyvektora és az i, j, k "
                                                 "egységvektorok a koordinátatengelyeken")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Néma Király nem beszél — <b>irányt mutat</b>. Crni Grom egyetlen '
         'hanghulláma romba dönthetné a Kristály-kamrát, de ha pontosan tudjuk, <b>merre</b> '
         'és <b>mekkora erővel</b> indul, épp ez a hullám hatástalaníthatja a kristályokat. '
         'Ehhez egy szám kevés. Egy <b>nyíl</b> kell.'),
   r'<p>A vektorokkal az 1e geometria-témakörében már '
   r'<a href="' + E1 + r'#def-vektor">megismerkedtél</a>. Ez az egység felidézi az alapokat '
   r'— mit nevezünk vektornak, hogyan adunk össze, vonunk ki és nyújtunk vektorokat —, '
   r'és hozzátesz egy új fogalmat: <b>két vektor szögét</b> és a <b>skaláris vetületet</b>. '
   r'Ez utóbbiból lesz majd a témakör egyik főszereplője, a skaláris szorzat.</p>',
 ]),

 ("Irányított szakasz és vektor", [
   r'<p>Vannak mennyiségek, amelyeket egyetlen szám leír: a hőmérséklet, a tömeg, az idő. '
   r'Másoknál a szám kevés — az elmozdulásnál, a sebességnél, az erőnél azt is tudnunk '
   r'kell, <b>merre</b> hatnak. Ezeket írjuk le vektorral.</p>',
   doboz("definicio", "Vektor",
         r'<p>Az <b>irányított szakasz</b> olyan szakasz, amelynek megkülönböztetjük a '
         r'kezdőpontját és a végpontját. Két irányított szakasz <b>egyenlő</b>, ha '
         r'<b>eltolással fedésbe hozhatók</b> — vagyis egyenlő hosszúak, párhuzamosak és '
         r'azonos irányításúak.</p>'
         r'<p>Az egymással egyenlő irányított szakaszok közös jellemzője a <b>vektor</b>. '
         r'Jele $\vec a$, vagy kezdő- és végpontjával $\overrightarrow{AB}$. Egy vektort '
         r'három adat határoz meg:</p>'
         r'<ul><li>az <b>iránya</b> (az egyenesének állása),</li>'
         r'<li>az <b>irányítása</b> (az egyenesen melyik felé mutat),</li>'
         r'<li>az <b>intenzitása</b> — más néven <b>hossza</b> vagy abszolút értéke —, '
         r'jele $|\vec a|$: az őt ábrázoló szakasz hossza.</li></ul>'
         r'<p>A <b>nullvektor</b> ($\vec 0$) kezdő- és végpontja egybeesik: intenzitása $0$, '
         r'iránya és irányítása nincs. Az $\vec a$ <b>ellentett vektora</b> ($-\vec a$) ugyanolyan '
         r'intenzitású és irányú, de <b>ellentétes irányítású</b>; például '
         r'$\overrightarrow{BA}=-\overrightarrow{AB}$. Az 1 intenzitású vektor az '
         r'<b>egységvektor</b>.</p>',
         hid="def-vektor"),
   abra(SVG_EGYENLO, 'A két kék nyíl <b>ugyanazt</b> az $\\vec a$ vektort ábrázolja — az egyik a másik '
        'eltoltja. A piros nyíl $-\\vec a$: ugyanolyan hosszú és párhuzamos, de ellentétes '
        'irányítású. A szürke $\\vec c$ más irányú, ezért nem egyenlő velük, bármilyen '
        'hosszú is.'),
   r'<p>Órán a vektor hosszát leggyakrabban <b>intenzitásnak</b> mondjuk — a tankönyvek '
   r'és a feladatok egy része viszont <b>hosszt</b> vagy <b>abszolút értéket</b> ír. '
   r'Mind a három ugyanazt jelenti: $|\vec a|$.</p>',
 ]),

 ("Összeadás és kivonás", [
   r'<p>Két vektort kétféle, egymással egyenértékű szabály szerint adhatunk össze.</p>'
   r'<ul><li><b>Háromszög-szabály:</b> a $\vec b$-t úgy toljuk el, hogy a kezdőpontja az '
   r'$\vec a$ végpontjába kerüljön; az összeg az $\vec a$ kezdőpontjából a $\vec b$ '
   r'végpontjába mutat (a két vektor ekkor <b>fej–láb helyzetben</b> van). Pontokkal: $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$.</li>'
   r'<li><b>Paralelogramma-szabály:</b> a két vektort <b>közös kezdőpontba</b> toljuk, és '
   r'kiegészítjük paralelogrammává; az összeg a közös kezdőpontból induló <b>átló</b>.</li></ul>'
   r'<p>A <b>kivonás</b> az ellentett hozzáadása: $\vec a-\vec b=\vec a+(-\vec b)$. A '
   r'paralelogrammában ez a <b>másik átló</b>, amely a $\vec b$ végpontjából az $\vec a$ '
   r'végpontjába mutat. Ugyanez pontokkal — és ezt a térbeli koordinátáknál sokszor '
   r'használjuk majd: $\overrightarrow{OB}-\overrightarrow{OA}=\overrightarrow{AB}$.</p>',
   abra(SVG_OSSZEADAS, 'Balra: háromszög-szabály. Jobbra: paralelogramma-szabály — a zöld '
        'átló az összeg, a piros átló a különbség, $\\vec a-\\vec b$ (a $\\vec b$ végpontjából '
        'az $\\vec a$ végpontjába mutat).'),
   doboz("pelda", "Kristály-kamra szimuláció — a szabályos hatszög vektorai",
         r'<p>A Kamra alapja egy $ABCDEF$ szabályos hatszög, középpontja $O$.</p>'
         + abra(SVG_HATSZOG, 'A szabályos hatszög, kékkel az $\\overrightarrow{AB}$ vektor.') +
         r'<ol type="a"><li>A csúcsok és az $O$ pont közötti vektorok közül melyek <b>egyenlők</b> '
         r'az $\overrightarrow{AB}$-vel?</li>'
         r'<li>Melyek az $\overrightarrow{AB}$ <b>ellentettjei</b>?</li>'
         r'<li>Mivel egyenlő $\overrightarrow{AB}+\overrightarrow{BC}$?</li>'
         r'<li>Mivel egyenlő $2(\overrightarrow{BO}-\overrightarrow{CO})$?</li>'
         r'<li>Legyen $\overrightarrow{OA}=\vec a$ és $\overrightarrow{OB}=\vec b$. Írd fel '
         r'$\overrightarrow{AB}$-t és $\overrightarrow{AC}$-t $\vec a$ és $\vec b$ '
         r'segítségével.</li></ol>'
         r'<p>A hatszöget az $O$-ból húzott szakaszok <b>hat szabályos háromszögre</b> bontják, '
         r'ezért minden oldal és minden „küllő” egyenlő hosszú, és a szemközti oldalak '
         r'párhuzamosak.</p>',
         hid="pelda-hatszog",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $\overrightarrow{OC}$, $\overrightarrow{FO}$ és '
                  r'$\overrightarrow{ED}$ — mind párhuzamos $AB$-vel, ugyanolyan hosszú és '
                  r'azonos irányítású.</p>'
                  r'<p><b>b)</b> $\overrightarrow{BA}$, $\overrightarrow{CO}$, '
                  r'$\overrightarrow{OF}$ és $\overrightarrow{DE}$.</p>'
                  r'<p><b>c)</b> A háromszög-szabály szerint $\overrightarrow{AB}+'
                  r'\overrightarrow{BC}=\overrightarrow{AC}$.</p>'
                  r'<p><b>d)</b> $\overrightarrow{BO}-\overrightarrow{CO}=\overrightarrow{BO}'
                  r'+\overrightarrow{OC}=\overrightarrow{BC}$. Mivel $\overrightarrow{BC}='
                  r'\overrightarrow{AO}=\overrightarrow{OD}$, a kétszerese '
                  r'$2\overrightarrow{BC}=\overrightarrow{AO}+\overrightarrow{OD}='
                  r'\overrightarrow{AD}$.</p>'
                  r'<p><b>e)</b> $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}='
                  r'\vec b-\vec a$. Az a) szerint $\overrightarrow{OC}=\overrightarrow{AB}='
                  r'\vec b-\vec a$, ezért $\overrightarrow{AC}=\overrightarrow{OC}-'
                  r'\overrightarrow{OA}=\vec b-2\vec a$.</p>'
                  r'<p class="vegeredmeny">a) $\overrightarrow{OC},\ \overrightarrow{FO},\ '
                  r'\overrightarrow{ED}$ · b) $\overrightarrow{BA},\ \overrightarrow{CO},\ '
                  r'\overrightarrow{OF},\ \overrightarrow{DE}$ · c) $\overrightarrow{AC}$ · '
                  r'd) $\overrightarrow{AD}$ · e) $\overrightarrow{AB}=\vec b-\vec a$, '
                  r'$\overrightarrow{AC}=\vec b-2\vec a$</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Egy repülőgép orra észak felé mutat, és a levegőhöz képest $200$ km/h-val '
         r'halad — közben a szél nyugat felől, <b>kelet felé</b> fúj $50$ km/h-val. '
         r'A gép nem észak felé halad, hanem a két sebességvektor <b>összegének</b> irányába: '
         r'kicsit keletre tér el (kb. $14^\circ$-kal), és a föld fölötti sebessége '
         r'$\sqrt{200^2+50^2}\approx206{,}2$ km/h. A pilóta ezért nem arra kormányoz, amerre '
         r'menni akar, hanem annyival a szél ellen, hogy az összeg mutasson a cél felé.</p>'),
   kviz(r'Az $\vec a$ intenzitása $3$, a $\vec b$ intenzitása $4$, és a két vektor merőleges '
        r'egymásra. Mekkora $|\vec a+\vec b|$?',
        ['$5$', '$7$', '$1$', '$12$'], 0,
        jo="✔ A paralelogramma most téglalap, az összeg az átlója: √(3² + 4²) = 5.",
        nem="✘ A hosszak csak akkor adódnak össze, ha a vektorok azonos irányításúak. Itt a "
            "két vektor derékszöget zár be: az összeg egy téglalap átlója, √(3² + 4²) = 5."),
 ]),

 ("Skalárral szorzás és párhuzamosság", [
   doboz("definicio", "Vektor szorzása valós számmal",
         r'<p>Ha $\lambda\ne0$ valós szám és $\vec a\ne\vec 0$, akkor a $\lambda\vec a$ vektor</p>'
         r'<ul><li>párhuzamos az $\vec a$-val, intenzitása $|\lambda|\cdot|\vec a|$;</li>'
         r'<li>$\lambda>0$ esetén <b>azonos</b>, $\lambda<0$ esetén <b>ellentétes</b> '
         r'irányítású.</li></ul>'
         r'<p>Ha $\lambda=0$ vagy $\vec a=\vec 0$, akkor $\lambda\vec a=\vec 0$.</p>'
         r'<p>Két nem nullvektor pontosan akkor <b>párhuzamos</b> (kollineáris), ha az egyik '
         r'a másik számszorosa: $\vec b=\lambda\vec a$.</p>',
         hid="def-skalarral-szorzas"),
   abra(SVG_SKALAR, 'Az $\\vec a$, a $2\\vec a$ (kétszer olyan hosszú, azonos irányítású) és '
        'a $-1{,}5\\vec a$ (másfélszer olyan hosszú, ellentétes irányítású). Mindhárom '
        'párhuzamos.'),
   doboz("tetel", "A vektorműveletek tulajdonságai",
         r'<p>Bármely $\vec a$, $\vec b$, $\vec c$ vektorra és $\lambda$, $\mu$ valós számra:</p>'
         r'<ul><li>$\vec a+\vec b=\vec b+\vec a$ <i>(kommutativitás)</i></li>'
         r'<li>$(\vec a+\vec b)+\vec c=\vec a+(\vec b+\vec c)$ <i>(asszociativitás)</i></li>'
         r'<li>$\vec a+\vec 0=\vec a$, &nbsp; $\vec a+(-\vec a)=\vec 0$</li>'
         r'<li>$\lambda(\vec a+\vec b)=\lambda\vec a+\lambda\vec b$, &nbsp; '
         r'$(\lambda+\mu)\vec a=\lambda\vec a+\mu\vec a$ <i>(disztributivitás)</i></li>'
         r'<li>$\lambda(\mu\vec a)=(\lambda\mu)\vec a$, &nbsp; $1\cdot\vec a=\vec a$, &nbsp; '
         r'$(-1)\cdot\vec a=-\vec a$</li></ul>'
         r'<p>Vagyis a vektorokkal úgy számolhatsz, mint a betűs kifejezésekkel: zárójelet '
         r'bonthatsz, összevonhatsz, kiemelhetsz.</p>',
         hid="tetel-muveletek"),
   doboz("pelda", "Kristály-kamra szimuláció — összevonás vektorokkal",
         r'<p>Egyszerűsítsd: $3(\vec a-2\vec b)-2(\vec a-\vec b)$.</p>'
         r'<p>Zárójelbontás után: $3\vec a-6\vec b-2\vec a+2\vec b$. Az $\vec a$-s és a '
         r'$\vec b$-s tagokat külön vonjuk össze — pontosan úgy, ahogy az $x$-es és az '
         r'$y$-os tagokat szoktuk.</p>',
         hid="pelda-osszevonas",
         lenyilo=("Végeredmény",
                  r'<p class="vegeredmeny">$3(\vec a-2\vec b)-2(\vec a-\vec b)=\vec a-4\vec b$</p>')),
   r'<p>Egy hasznos következmény: ha $F$ az $AB$ szakasz <b>felezőpontja</b>, akkor '
   r'$\overrightarrow{AF}=\tfrac12\overrightarrow{AB}$, és bármely $O$ pontból '
   r'$\overrightarrow{OF}=\tfrac12\left(\overrightarrow{OA}+\overrightarrow{OB}\right)$. '
   r'<i>(Indoklás: $\overrightarrow{OF}=\overrightarrow{OA}+\tfrac12\overrightarrow{AB}='
   r'\overrightarrow{OA}+\tfrac12(\overrightarrow{OB}-\overrightarrow{OA})$.)</i></p>',
 ]),

 ("Két vektor szöge és a skaláris vetület", [
   doboz("definicio", "Két vektor szöge · skaláris vetület",
         r'<p>Két nem nullvektor <b>szögét</b> úgy kapjuk, hogy <b>közös kezdőpontba toljuk</b> '
         r'őket: a $\varphi$ szög a közös pontból induló két félegyenes által meghatározott, '
         r'legfeljebb $180^\circ$-os szög. Tehát mindig $0^\circ\le\varphi\le180^\circ$: '
         r'$\varphi=0^\circ$, ha párhuzamosak és azonos irányításúak, $\varphi=180^\circ$, ha '
         r'párhuzamosak és ellentétes irányításúak, és $\varphi=90^\circ$, ha merőlegesek.</p>'
         r'<p>A $\vec b$ vektor <b>skaláris vetülete</b> az $\vec a$ irányára az előjeles szám</p>'
         r'$$b_{\vec a}=|\vec b|\cos\varphi .$$'
         r'<p>Abszolút értéke a $\vec b$ vektor $\vec a$ egyenesére eső merőleges vetületének '
         r'(az ábrán a színes szakasznak) a hossza. <b>Előjele</b> pozitív, ha a vetület az '
         r'$\vec a$-val azonos irányítású ($0^\circ\le\varphi<90^\circ$), negatív, ha ellentétes '
         r'irányítású ($90^\circ<\varphi\le180^\circ$), és $0$, ha $\varphi=90^\circ$.</p>',
         hid="def-szog-vetulet"),
   abra(SVG_VET_HEGY, 'Hegyesszög: a $\\vec b$ végpontjából merőlegest bocsátunk az $\\vec a$ '
        'egyenesére; a zöld szakasz a vetület, $|\\vec b|\\cos\\varphi>0$.'),
   abra(SVG_VET_TOMPA, 'Tompaszög: a merőleges talppontja az $O$ <b>másik oldalára</b> esik. '
        'A piros szakasz hossza $-|\\vec b|\\cos\\varphi$, a skaláris vetület tehát negatív: '
        '$b_{\\vec a}=|\\vec b|\\cos\\varphi<0$.'),
   r'<p><b>Számolás.</b> Legyen $|\vec b|=6$. Ha $\varphi=60^\circ$, a vetület '
   r'$6\cos60^\circ=6\cdot\tfrac12=3$; ha $\varphi=120^\circ$, akkor $6\cos120^\circ=-3$; '
   r'ha $\varphi=90^\circ$, akkor $0$.</p>'
   r'<p>Nem nevezetes szögnél <b>számológépet</b> használunk. $|\vec b|=5$, $\varphi=35^\circ$: '
   r'$5\cos35^\circ\approx5\cdot0{,}8192\approx4{,}10$. Figyelj arra, hogy a számológép '
   r'<b>fok</b> üzemmódban legyen (a kijelzőn <b>D</b> vagy <b>DEG</b>): radián módban '
   r'ugyanez a gombsor $-4{,}52$-t adna — egy <b>negatív</b> vetületet egy hegyesszögre, '
   r'ami azonnal elárulja a hibát.</p>',
   abra(SVG_KVIZ_SZOG),
   kviz(r'A fenti ábrán a vektorok fej–láb helyzetben vannak: a $\vec b$ az $\vec a$ '
        r'végpontjából indul, és az $\vec a$ egyenesének jobbra eső meghosszabbításával '
        r'$45^\circ$-os szöget zár be. Mekkora a két vektor szöge?',
        [r'$45^\circ$', r'$135^\circ$', r'$90^\circ$', r'$225^\circ$'], 0,
        jo="✔ Közös kezdőpontba tolva a b ugyanúgy 45°-kal emelkedik az a irányához képest.",
        nem="✘ Told a b-t az a kezdőpontjába: onnan 45°-os szöget zár be az a irányával — "
            "ez a két vektor szöge. A 135° a csatlakozásnál látszó mellékszög, a 90° semmivel "
            "sem indokolható, a 225° pedig nem is lehet, mert két vektor szöge legfeljebb 180°."),
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„A két vektor épp egymás után jön, a szögük ott van a csatlakozásnál: '
         r'$120^\circ$.”</i></p>'
         + abra(SVG_MAXI_SZOG) +
         r'<p>A csatlakozásnál látszó szög a <b>mellékszög</b>: Maxi $180^\circ-\varphi$-t '
         r'olvasott le. Két vektor szögét csak <b>közös kezdőpontba tolt</b> vektorok között '
         r'mérjük — itt $\varphi=60^\circ$.</p>'
         r'<p>Maxi másik kedvence: $|\vec a+\vec b|=|\vec a|+|\vec b|$. Ez csak <b>azonos '
         r'irányítású</b> vektorokra igaz; általában $|\vec a+\vec b|\le|\vec a|+|\vec b|$ '
         r'(a háromszög-egyenlőtlenség), ahogy az összeadásnál látott gyors kérdésben is.</p>'),
   GY(FGY + "#alap-1", "A 1–8", FGY + "#kozep-1", "K 1–5"),
   brief('<b>Medúza:</b> A síkban két irány elég mindenhez — balra-jobbra, előre-hátra. '
         'A Kristály-kamra viszont <b>térben</b> van: a kristályok a padlótól a mennyezetig '
         'lebegnek. Crni Grom azt mutatja, hogy a nyilakat ezentúl nem rajzolni fogjuk, hanem '
         '<b>számokká</b> fordítani.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> A Kamra három irányban nyúlik, és a műszerek minden pontra '
         '<b>három számot</b> adnak. Crni Grom szerint ez nem teher, hanem ajándék: ha a nyilat '
         'három számmá fordítjuk, a vektorműveletek egyszerű <b>számolássá</b> válnak. Nem kell '
         'rajzolni — elég összeadni.'),
   r'<p>Ebben az egységben felépítjük a <b>térbeli derékszögű koordináta-rendszert</b>, '
   r'megadjuk a vektorokat koordinátáikkal, és megtanuljuk, hogyan számolható ki velük '
   r'egy vektor <b>intenzitása</b> és két pont <b>távolsága</b>.</p>',
 ]),

 ("A térbeli derékszögű koordináta-rendszer", [
   doboz("definicio", "Térbeli koordináta-rendszer · a pont koordinátái",
         r'<p>A <b>térbeli derékszögű koordináta-rendszer</b> három, közös $O$ kezdőpontú, '
         r'páronként merőleges számegyenes: az $x$, az $y$ és a $z$ tengely. A rendszer '
         r'<b>jobbsodrású</b>: ha jobb kezünk hüvelykujja az $x$, mutatóujja az $y$ tengely '
         r'pozitív fele felé mutat, akkor a behajlított középső ujjunk a $z$ tengely pozitív fele '
         r'felé mutat.</p>'
         r'<p>A tér egy $P$ pontjának <b>koordinátái</b>: vetítsük merőlegesen a pontot a '
         r'három tengelyre — a vetületek helyén leolvasott három szám $P(x;y;z)$. Szemléletesen: '
         r'az $O$ és a $P$ egy olyan tengelyekkel párhuzamos élű <b>téglatest</b> testátlójának két '
         r'végpontja, amelynek élei $|x|$, $|y|$ és $|z|$. (Ha egy koordináta $0$, a „doboz” '
         r'téglalappá vagy szakasszá lapul.)</p>',
         hid="def-koordinatak"),
   abra(SVG_TER_PONT, 'A $P(3;4;2)$ pont a „dobozában”: az $x$ tengely mentén $3$, az $y$ '
        'mentén $4$, a $z$ mentén $2$ egységet haladunk.'),
   r'<p><b>Rajzolás.</b> Az $y$ tengelyt vízszintesen jobbra, a $z$ tengelyt függőlegesen '
   r'felfelé rajzoljuk; az $x$ tengely — amely valójában felénk mutat — balra lefelé, '
   r'<b>ferdén</b> halad, és rajta az egységet kb. a felére rövidítjük. Így lesz a síkbeli '
   r'rajz térhatású. (Az $x$ felénk, az $y$ jobbra, a $z$ felfelé: ez éppen jobbsodrású '
   r'rendszer.)</p>'
   r'<table class="tt-table"><tr><th>Ahol a pont van</th><th>A koordinátái</th></tr>'
   r'<tr><td>az $x$, az $y$, illetve a $z$ tengelyen</td><td>$(x;0;0)$, $(0;y;0)$, $(0;0;z)$</td></tr>'
   r'<tr><td>az $xy$ síkban (a „padlón”)</td><td>$(x;y;0)$</td></tr>'
   r'<tr><td>az $xz$ síkban</td><td>$(x;0;z)$</td></tr>'
   r'<tr><td>az $yz$ síkban</td><td>$(0;y;z)$</td></tr>'
   r'<tr><td>a kezdőpontban</td><td>$(0;0;0)$</td></tr></table>',
   doboz("pelda", "Kristály-kamra szimuláció — hol van a pont?",
         r'<p>A fenti ábra dobozának melyik csúcsa a $Q(0;4;2)$ pont? És melyik a '
         r'$R(3;4;0)$?</p>',
         hid="pelda-leolvasas",
         lenyilo=("Megoldás",
                  r'<p>$Q$-nak az $x$ koordinátája $0$, tehát az $yz$ síkban van: ez a doboz '
                  r'<b>hátsó, felső, jobb</b> csúcsa (a $4$-es jel fölött, a $2$-es jellel egy magasságban). '
                  r'$R$-nek a $z$ koordinátája $0$, tehát a „padlón” van: a doboz <b>elülső, '
                  r'alsó, jobb</b> csúcsa, közvetlenül $P$ alatt.</p>'
                  r'<p class="vegeredmeny">$Q$: hátsó felső jobb csúcs (az $yz$ síkban) · '
                  r'$R$: elülső alsó jobb csúcs, $P$ alatt (az $xy$ síkban)</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Egy 3D-nyomtató fúvókája és minden videojáték-motor pontosan így, derékszögű '
         r'<b>számhármasokkal</b> írja le a teret (a telefonod GPS-e is számhármast ad: '
         r'szélességet, hosszúságot és magasságot). Amikor egy játékban a szereplő '
         r'előrelép, a program valójában egy vektort ad hozzá a helyzetét leíró '
         r'számhármashoz — ennyi az egész.</p>'),
 ]),

 ("A vektor koordinátái", [
   r'<p>Jelölje $\vec i$, $\vec j$ és $\vec k$ az $x$, az $y$ és a $z$ tengely pozitív '
   r'irányába mutató <b>egységvektort</b>. Toljunk egy tetszőleges vektort az $O$ '
   r'kezdőpontba; a végpontja legyen $P(x;y;z)$. Ekkor a „doboz” éleit követve</p>'
   r'$$\overrightarrow{OP}=x\vec i+y\vec j+z\vec k .$$',
   doboz("definicio", "A vektor koordinátái · helyvektor",
         r'<p>Ha $\vec a=x\vec i+y\vec j+z\vec k$, akkor az $x$, $y$, $z$ számok az $\vec a$ '
         r'<b>koordinátái</b>, és röviden $\vec a=(x;y;z)$. A két írásmód egyenrangú.</p>'
         r'<p>A koordináták a vektor <b>skaláris vetületei</b> az $\vec i$, $\vec j$, $\vec k$ irányára '
         r'(<a href="tananyag-vektorok-sikban.html#def-szog-vetulet">lásd az előző egységet</a>).</p>'
         r'<p>A $P$ pont <b>helyvektora</b> az $\overrightarrow{OP}$ vektor; koordinátái '
         r'megegyeznek a $P$ pont koordinátáival.</p>',
         hid="def-vektor-koordinatai"),
   abra(SVG_TER_VEKTOR, 'A $P(3;4;2)$ helyvektora: $\\vec p=3\\vec i+4\\vec j+2\\vec k=(3;4;2)$.'),
   r'<p><b>Két pont közötti vektor.</b> Ha $A(x_1;y_1;z_1)$ és $B(x_2;y_2;z_2)$, akkor a '
   r'háromszög-szabály szerint $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$, '
   r'vagyis</p>'
   r'$$\overrightarrow{AB}=(x_2-x_1;\;y_2-y_1;\;z_2-z_1).$$'
   r'<p>Röviden: <b>végpont mínusz kezdőpont</b>.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„$A(2;-1;3)$, $B(5;1;-1)$, tehát $\overrightarrow{AB}=(2-5;\,-1-1;\,3+1)='
         r'(-3;-2;4)$.”</i></p>'
         r'<p>Maxi a kezdőpontból vonta ki a végpontot — ez a $\overrightarrow{BA}$, az '
         r'<b>ellentett</b> vektor. A helyes sorrend: <b>végpont mínusz kezdőpont</b>, '
         r'$\overrightarrow{AB}=(3;2;-4)$.</p>'
         r'<p>A másik csapda az írásmódok váltása. A $2\vec i-\vec k$ vektorban <b>nincs</b> '
         r'$\vec j$-s tag — ez azt jelenti, hogy a $\vec j$ együtthatója $0$: '
         r'$2\vec i-\vec k=(2;0;-1)$, és <b>nem</b> $(2;-1)$. Térben minden vektornak három '
         r'koordinátája van.</p>'),
   kviz(r'$A(1;4;-2)$ és $B(-2;5;3)$. Mik az $\overrightarrow{AB}$ koordinátái?',
        [r'$(-3;1;5)$', r'$(3;-1;-5)$', r'$(-1;9;1)$', r'$(-3;1;1)$'], 0,
        jo="✔ Végpont mínusz kezdőpont: (−2 − 1; 5 − 4; 3 − (−2)) = (−3; 1; 5).",
        nem="✘ Végpont mínusz kezdőpont: (−2 − 1; 5 − 4; 3 − (−2)) = (−3; 1; 5). "
            "A (3; −1; −5) a BA vektor, a (−1; 9; 1) a két pont koordinátáinak összege, a "
            "(−3; 1; 1)-nél pedig a 3 − (−2) előjele csúszott el."),
 ]),

 ("Műveletek koordinátákkal", [
   doboz("tetel", "Vektorműveletek koordinátákkal",
         r'<p>Ha $\vec a=(x_1;y_1;z_1)$, $\vec b=(x_2;y_2;z_2)$ és $\lambda$ valós szám, akkor</p>'
         r'$$\vec a\pm\vec b=(x_1\pm x_2;\;y_1\pm y_2;\;z_1\pm z_2),\qquad '
         r'\lambda\vec a=(\lambda x_1;\;\lambda y_1;\;\lambda z_1).$$'
         r'<p>Két pont közötti vektor: $\overrightarrow{AB}=(x_2-x_1;\;y_2-y_1;\;z_2-z_1)$.</p>'
         r'<p>Két nem nullvektor pontosan akkor <b>párhuzamos</b>, ha a koordinátáik '
         r'<b>arányosak</b>: van olyan $\lambda$, hogy $x_2=\lambda x_1$, $y_2=\lambda y_1$ és '
         r'$z_2=\lambda z_1$, vagyis $\vec b=\lambda\vec a$. (Nulla koordinátával ne ossz: '
         r'ott a másik vektor megfelelő koordinátájának is $0$-nak kell lennie.)</p>',
         hid="tetel-koordinatas-muveletek"),
   r'<p>Az indoklás a <a href="tananyag-vektorok-sikban.html#tetel-muveletek">műveleti '
   r'tulajdonságokból</a> jön: például $(x_1\vec i+y_1\vec j+z_1\vec k)+(x_2\vec i+y_2\vec j+'
   r'z_2\vec k)$-ban az $\vec i$-s, $\vec j$-s és $\vec k$-s tagokat külön vonjuk össze.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — számolás koordinátákkal",
         r'<p>$\vec a=(2;-1;3)$ és $\vec b=(1;4;-2)$. Számítsd ki: $\vec a+\vec b$, '
         r'$\vec a-\vec b$, $2\vec a-3\vec b$. Párhuzamos-e $\vec a$-val a '
         r'$\vec c=(-4;2;-6)$ és a $\vec d=(4;-2;5)$ vektor?</p>',
         hid="pelda-koordinatas-muveletek",
         lenyilo=("Megoldás",
                  r'<p>$\vec a+\vec b=(3;3;1)$, &nbsp; $\vec a-\vec b=(1;-5;5)$.</p>'
                  r'<p>$2\vec a-3\vec b=(4;-2;6)-(3;12;-6)=(1;-14;12)$.</p>'
                  r'<p>$\vec c=-2\cdot(2;-1;3)$, tehát $\vec c=-2\vec a$: <b>párhuzamos</b> '
                  r'(ellentétes irányítású). A $\vec d$-nél az arányok $\tfrac42=2$, '
                  r'$\tfrac{-2}{-1}=2$, de $\tfrac53\ne2$: <b>nem párhuzamos</b>.</p>'
                  r'<p class="vegeredmeny">$\vec a+\vec b=(3;3;1)$ · $\vec a-\vec b=(1;-5;5)$ · '
                  r'$2\vec a-3\vec b=(1;-14;12)$ · $\vec c\parallel\vec a$, '
                  r'$\vec d\nparallel\vec a$</p>')),
   kviz(r'Melyik a $3\vec i-2\vec k$ vektor koordinátás alakja?',
        [r'$(3;0;-2)$', r'$(3;-2)$', r'$(3;-2;0)$', r'$(-2;0;3)$'], 0,
        jo="✔ A j-s tag hiányzik, tehát a második koordináta 0.",
        nem="✘ Térben mindig három koordináta van, a sorrend i, j, k. A hiányzó j-s tag "
            "0-t jelent a MÁSODIK helyen: (3; 0; −2)."),
 ]),

 ("Intenzitás és távolság", [
   r'<p>Az $\vec a=(x;y;z)$ vektort az $O$-ba tolva a végpontja $P(x;y;z)$, és '
   r'$|\vec a|$ éppen az $OP$ szakasz hossza — a pont „dobozának” <b>testátlója</b>. A '
   r'<a href="../01-poliederek/tananyag-hasab.html#tetel-teglatest-atlo">téglatest '
   r'testátlójánál</a> tanultak szerint kétszer alkalmazzuk Pitagorasz tételét: a padlón az '
   r'alaplap átlójának négyzete $x^2+y^2$, és ehhez jön hozzá a függőleges él négyzete, '
   r'$z^2$.</p>',
   doboz("tetel", "A vektor intenzitása · két pont távolsága",
         r'$$|\vec a|=\sqrt{x^2+y^2+z^2}$$'
         r'<p>Az $A(x_1;y_1;z_1)$ és $B(x_2;y_2;z_2)$ pont <b>távolsága</b> az '
         r'$\overrightarrow{AB}$ intenzitása:</p>'
         r'$$d(A,B)=|\overrightarrow{AB}|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.$$'
         r'<p>Az $\vec a\ne\vec 0$ vektorral azonos irányítású <b>egységvektor</b>: '
         r'$\vec a_0=\dfrac{\vec a}{|\vec a|}$.</p>',
         hid="tetel-hossz"),
   r'<p><b>Három gyors példa.</b> A $P(3;4;2)$ helyvektorának intenzitása '
   r'$\sqrt{9+16+4}=\sqrt{29}\approx5{,}39$. Az $\vec a=(2;-1;2)$ intenzitása '
   r'$\sqrt{4+1+4}=3$, a vele azonos irányítású egységvektor $\vec a_0=\left(\tfrac23;-\tfrac13;'
   r'\tfrac23\right)$. Az $A(1;-2;3)$ és a $B(3;1;-3)$ pont távolsága: '
   r'$\overrightarrow{AB}=(2;3;-6)$, $|\overrightarrow{AB}|=\sqrt{4+9+36}=7$.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — a paralelogramma negyedik csúcsa",
         r'<p>Az $ABCD$ paralelogramma három csúcsa $A(1;2;0)$, $B(4;3;1)$ és $D(2;-1;3)$. '
         r'Határozd meg a $C$ csúcs koordinátáit, és számítsd ki a paralelogramma oldalainak '
         r'hosszát és a kerületét!</p>'
         r'<p><b>Ötlet.</b> A paralelogrammában a szemközti oldalak vektorai egyenlők: '
         r'$\overrightarrow{DC}=\overrightarrow{AB}$. A csúcsok sorrendje számít — $ABCD$ '
         r'körbejárva, tehát $C$ a $B$-vel és a $D$-vel szomszédos.</p>',
         hid="pelda-paralelogramma",
         lenyilo=("Megoldás",
                  r'<p>$\overrightarrow{AB}=(3;1;1)$. Mivel $\overrightarrow{DC}=\overrightarrow{AB}$, '
                  r'$C=D+\overrightarrow{AB}=(2+3;\,-1+1;\,3+1)=(5;0;4)$. '
                  r'<i>(Ugyanez képlettel: $C=B+D-A$.)</i></p>'
                  r'<p>$|\overrightarrow{AB}|=\sqrt{9+1+1}=\sqrt{11}\approx3{,}32$, '
                  r'$\overrightarrow{AD}=(1;-3;3)$, $|\overrightarrow{AD}|=\sqrt{1+9+9}='
                  r'\sqrt{19}\approx4{,}36$.</p>'
                  r'<p>A kerület $K=2\left(\sqrt{11}+\sqrt{19}\right)\approx15{,}35$.</p>'
                  r'<p><i>Ellenőrzés: $\overrightarrow{DC}=(5-2;\,0+1;\,4-3)=(3;1;1)='
                  r'\overrightarrow{AB}$ ✔. Aki $A+B-D=(3;6;-2)$-t számol, az a $D$-vel '
                  r'szemközti csúcsot kapja meg egy <b>másik</b> paralelogrammában, amelynek $AB$ az átlója.</i></p>'
                  r'<p class="vegeredmeny">$C(5;0;4)$ · $AB=\sqrt{11}\approx3{,}32$, '
                  r'$AD=\sqrt{19}\approx4{,}36$ · $K\approx15{,}35$</p>')),
   GY(FGY + "#alap-9", "A 9–18", FGY + "#kozep-6", "K 6–12"),
   brief('<b>Medúza:</b> Összeadni, kivonni és nyújtani már tudjuk a nyilakat — számokkal is. '
         'Crni Grom azonban két nyilat mutat egyszerre, és kérdőn néz: <b>hogyan lehet két '
         'vektort összeszorozni</b>, és mit kapunk eredményül? Kiderül, hogy erre két '
         'válasz is van.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-vektorok-sikban.html",
     cim="Vektorok a síkban — felidézés és szög",
     cim_tiszta="Vektorok a síkban",
     alcim="A vektor fogalma és intenzitása, az összeadás, a kivonás és a skalárral szorzás, "
           "két vektor szöge és a skaláris vetület.",
     chip=KUL + " · 1/5", szakaszok=A1,
     elozo=("index.html", "Vektorok — témakör"),
     kovetkezo=("tananyag-koordinatak-terben.html", "Vektorok a térben")),
 lap(**T, fajl="tananyag-koordinatak-terben.html",
     cim="Vektorok a térben — koordinátákkal",
     cim_tiszta="Vektorok a térben",
     alcim="A térbeli derékszögű koordináta-rendszer, a vektor koordinátái, a műveletek "
           "koordinátákkal, a vektor intenzitása és két pont távolsága.",
     chip=KUL + " · 2/5", szakaszok=A2,
     elozo=("tananyag-vektorok-sikban.html", "Vektorok a síkban"),
     kovetkezo=("tananyag-skalaris-szorzat.html", "A skaláris szorzat")),
]
for u in KI:
    print("✓", os.path.basename(u))
