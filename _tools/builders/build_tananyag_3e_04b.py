# -*- coding: utf-8 -*-
"""3e/04 — B blokk: a skalaris szorzat (B1), a vektorialis szorzat (B2); C blokk: vektorok
alkalmazasa (C1). Mentor: Crni Grom (Meduza tolmacsol). Kuldetes: A Kiralyi Iranyitotu."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import (svg_vektorok_sik, svg_vetulet, svg_vektorialis,
                         KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA)

T = dict(tagozat="3e", mappa="04-vektorok", temakor="Vektorok")
FGY = "feladatok-szorzatok.html"
KUL = "A Királyi Irányítótű"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Matrix, sqrt, cos, sin, pi, simplify, N, acos, Rational
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

def fok(x):
    return float(N(acos(x) * 180 / pi))

# B1
chk("B1-def", 4*5*cos(pi/3), 10)
chk("B1-def-150", 2*3*cos(5*pi/6), -3*sqrt(3)); chk("B1-def-150-kerek", round(float(-3*sqrt(3)), 2), -5.20)
chk("B1-munka", round(float(50*10*cos(pi/6)), 0), 433)
a, b = V(2, -1, 3), V(1, 4, -2)
chk("B1-koord", a.dot(b), -8)
chk("B1-ijk", V(1, 0, 0).dot(V(1, 0, 0)) + V(1, 0, 0).dot(V(0, 1, 0)), 1)
p, q = V(4, 1, 0), V(-1, 3, 0)
chk("B1-majdnem", p.dot(q), -1)
chk("B1-majdnem-szog", round(fok(p.dot(q) / (p.norm() * q.norm())), 1), 94.4)
u, v, d = V(3, -1, 2), V(1, 2, 4), V(2, 4, -1)
chk("B1-pelda-sk", u.dot(v), 9); chk("B1-pelda-u", u.norm(), sqrt(14)); chk("B1-pelda-v", v.norm(), sqrt(21))
chk("B1-pelda-cos", round(float(9 / sqrt(294)), 4), 0.5249)
chk("B1-pelda-fok", round(fok(9 / sqrt(294)), 1), 58.3)
chk("B1-pelda-294", 14 * 21, 294)
chk("B1-meroleges", u.dot(d), 0)
chk("B1-maxi-vektor", V(3*1, -1*2, 2*4), V(3, -2, 8))
# B2
chk("B2-terulet", 4*6*sin(pi/6), 12)
chk("B2-szamologep", round(float(5*3*sin(40*pi/180)), 2), 9.64)
axb = a.cross(b)
chk("B2-kereszt", axb, V(-10, 7, 9))
chk("B2-mer-a", a.dot(axb), 0); chk("B2-mer-b", b.dot(axb), 0)
chk("B2-maxi", a.dot(V(-10, -7, 9)), 14)
chk("B2-ijk", V(1, 0, 0).cross(V(0, 1, 0)), V(0, 0, 1))
chk("B2-jk", V(0, 1, 0).cross(V(0, 0, 1)), V(1, 0, 0))
chk("B2-ki", V(0, 0, 1).cross(V(1, 0, 0)), V(0, 1, 0))
A_, B_, C_ = V(1, 0, 2), V(3, 1, 1), V(2, 3, 4)
n = (B_ - A_).cross(C_ - A_)
chk("B2-AB", B_ - A_, V(2, 1, -1)); chk("B2-AC", C_ - A_, V(1, 3, 2))
chk("B2-n", n, V(5, -5, 5)); chk("B2-n-hossz", n.norm(), 5*sqrt(3))
chk("B2-T", round(float(n.norm() / 2), 2), 4.33)
chk("B2-par", a.cross(V(-4, 2, -6)), V(0, 0, 0))
chk("B2-anti", b.cross(a), -axb)
# (2a - b) x (a + 3b) = 7 (a x b) — altalanos vektorokkal ellenorizve
x1, x2 = V(1, 2, -1), V(0, 3, 5)
chk("B2-tul", (2*x1 - x2).cross(x1 + 3*x2), 7 * x1.cross(x2))
chk("B2-tul-konkret", 7 * V(1, -2, 2), V(7, -14, 14)); chk("B2-tul-hossz", V(7, -14, 14).norm(), 21)
chk("B2-kviz", -V(2, -3, 1), V(-2, 3, -1))
# C1
A, B, C = V(2, 1, 0), V(4, 3, 1), V(1, 3, 2)
AB, AC, BC = B - A, C - A, C - B
chk("C1-AB", AB, V(2, 2, 1)); chk("C1-AC", AC, V(-1, 2, 2)); chk("C1-BC", BC, V(-3, 0, 1))
chk("C1-|AB|", AB.norm(), 3); chk("C1-|AC|", AC.norm(), 3); chk("C1-|BC|", BC.norm(), sqrt(10))
chk("C1-sk", AB.dot(AC), 4)
chk("C1-alfa", round(fok(Rational(4, 9)), 1), 63.6)
chk("C1-maxi", round(fok(-Rational(4, 9)), 1), 116.4)
chk("C1-beta-sk", (A - B).dot(C - B), 5)
chk("C1-beta", round(fok(5 / (3*sqrt(10))), 1), 58.2)
chk("C1-kereszt", AB.cross(AC), V(2, -5, 6)); chk("C1-kereszt-h", AB.cross(AC).norm(), sqrt(65))
chk("C1-T", round(float(sqrt(65) / 2), 2), 4.03)
chk("C1-T-sin", round(float(Rational(9, 2) * sqrt(1 - Rational(16, 81))), 2), 4.03)
chk("C1-D", B + C - A, V(3, 5, 3))
chk("C1-szogosszeg", round(fok(Rational(4, 9)) + 2 * fok(5 / (3*sqrt(10))), 6), 180, 1e-6)
F1, F2, s = V(2, 3, 1), V(1, -1, 1), V(4, 1, 0)
R = F1 + F2
chk("C1-R", R, V(3, 2, 2)); chk("C1-|R|", R.norm(), sqrt(17)); chk("C1-|R|-kerek", round(float(sqrt(17)), 2), 4.12)
chk("C1-W", R.dot(s), 14)
chk("C1-W-szog", 40*5*cos(pi/3), 100)
chk("C1-W1", F1.dot(s), 11); chk("C1-W2", F2.dot(s), 3)
chk("C1-maxi-BC2", 9 + 9 - 18*(-Rational(4, 9)), 26)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_VET_B1 = svg_vetulet(50, a_hossz=4.6, b_hossz=3.6,
                         leiras="A skaláris szorzat: az a intenzitása szorozva a b skaláris "
                                "vetületével az a irányára")


def _par(o, szog, h=2.3):
    fi = math.radians(szog)
    return (o[0] + h * math.cos(fi), o[1] + h * math.sin(fi))


_O = [(0.6, 0.95), (5.2, 0.95), (10.6, 0.95)]
_Bv = [_par(_O[0], 50), _par(_O[1], 90), _par(_O[2], 130)]
SVG_ELOJEL = svg_vektorok_sik(
    [v for i in range(3) for v in (
        (_O[i], (_O[i][0] + 3, _O[i][1]), KEK, "a", {"tav": 13, "dx": 40}),
        (_O[i], _Bv[i], BOROSTYAN, "b", {"tav": 13}))],
    szogivek=[(_O[i], (_O[i][0] + 3, _O[i][1]), _Bv[i], LILA, "") for i in range(3)],
    feliratok=[((_O[0][0] + 1.5, 0.05), "a · b > 0", ZOLD, 15),
               ((_O[1][0] + 1.5, 0.05), "a · b = 0", SZURKE, 15),
               ((_O[2][0] + 1.5, 0.05), "a · b < 0", PIROS, 15),
               ((_O[0][0] + 1.6, 3.55), "hegyesszög", SZURKE, 13),
               ((_O[1][0] + 1.5, 3.55), "derékszög", SZURKE, 13),
               ((_O[2][0] + 1.0, 3.55), "tompaszög", SZURKE, 13)],
    xr=(0, 14), yr=(-0.35, 3.85), egyseg=40, racs=False,
    leiras="Hegyesszög esetén a skaláris szorzat pozitív, derékszögnél nulla, tompaszögnél negatív")
SVG_VX = svg_vektorialis()
SVG_VX_ANTI = svg_vektorialis(ellentett=True, leiras="Az a × b és a b × a ellentett vektorok: "
                                                    "ugyanarra a síkra merőlegesek, de ellentétes irányításúak")

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Egy hanghullám csak annyit ér, amennyi belőle <b>a cél irányába</b> '
         'esik. A többi elszáll a Kamra falai felé. Crni Grom most két nyilat tart egymás mellé: '
         'az egyik a hullám, a másik a cél iránya. Amit tőlük kapunk, az <b>egyetlen szám</b> — '
         'és ez a szám megmondja, dolgozik-e a hullám a cél felé.'),
   r'<p>Ebben az egységben a két vektorból számot adó <b>skaláris szorzattal</b> '
   r'ismerkedünk meg. Két kérdésre ad választ: <b>merőleges-e</b> két vektor, és <b>mekkora a '
   r'szögük</b>. A szöget számológéppel fogjuk kiszámítani.</p>',
 ]),

 ("A definíció", [
   doboz("definicio", "Skaláris szorzat",
         r'<p>Két vektor <b>skaláris szorzata</b> az intenzitásaik és a közös kezdőpontba tolt '
         r'vektorok $\varphi$ szöge ($0^\circ\le\varphi\le180^\circ$) koszinuszának szorzata:</p>'
         r'$$\vec a\cdot\vec b=|\vec a|\,|\vec b|\cos\varphi .$$'
         r'<p>Az eredmény <b>szám</b> (skalár) — innen a neve. Ha valamelyik vektor a '
         r'nullvektor, a skaláris szorzat $0$.</p>',
         hid="def-skalaris"),
   r'<p><b>Kapcsolat a vetülettel.</b> A $|\vec b|\cos\varphi$ a $\vec b$ '
   r'<a href="tananyag-vektorok-sikban.html#def-szog-vetulet">skaláris vetülete</a> az $\vec a$ '
   r'irányára. A skaláris szorzat tehát: <b>az egyik vektor intenzitása szorozva a másik '
   r'rá eső előjeles (skaláris) vetületével</b>.</p>',
   abra(SVG_VET_B1, '$\\vec a\\cdot\\vec b=|\\vec a|\\cdot\\left(|\\vec b|\\cos\\varphi\\right)$: '
        'az $\\vec a$ hossza szorozva a zöld szakasz előjeles hosszával.'),
   r'<p><b>Számolás a definícióval.</b> Ha $|\vec a|=4$, $|\vec b|=5$ és $\varphi=60^\circ$, '
   r'akkor $\vec a\cdot\vec b=4\cdot5\cdot\tfrac12=10$. Ha $|\vec a|=2$, $|\vec b|=3$ és '
   r'$\varphi=150^\circ$, akkor $\vec a\cdot\vec b=2\cdot3\cdot\left(-\tfrac{\sqrt3}{2}\right)'
   r'=-3\sqrt3\approx-5{,}20$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A fizikában a <b>munka</b> skaláris szorzat: $W=\vec F\cdot\vec s$. Ha egy szánkót '
         r'$50$ N erővel húzol, a kötél $30^\circ$-os szöget zár be a talajjal, és a szánkó '
         r'$10$ m-t halad, akkor a munka $W=50\cdot10\cdot\cos30^\circ\approx433$ J — nem '
         r'$500$ J, mert az erőnek csak a mozgás irányába eső része dolgozik. A felfelé húzó '
         r'része nem végez munkát, mert merőleges az elmozdulásra.</p>'),
   kviz(r'Milyen típusú az $\vec a\cdot\vec b$ skaláris szorzat eredménye?',
        ['egy valós szám', r'az $\vec a$-val párhuzamos vektor',
         r'az $\vec a$-ra és $\vec b$-re merőleges vektor', 'egy szám, de csak ha a két vektor párhuzamos'], 0,
        jo="✔ A skaláris szorzat két vektorból egyetlen számot ad.",
        nem="✘ A skaláris szorzat MINDIG szám: két intenzitás és egy koszinusz szorzata. "
            "(A mindkettőre merőleges vektort a vektoriális szorzat adja — az a következő egység.)"),
 ]),

 ("Az előjel jelentése", [
   r'<p>Nem nullvektoroknál $|\vec a|$ és $|\vec b|$ pozitív, ezért a skaláris szorzat előjelét a '
   r'$\cos\varphi$ dönti el:</p>',
   abra(SVG_ELOJEL, 'A skaláris szorzat előjele a két vektor szögéről árulkodik.'),
   r'<table class="tt-table"><tr><th>A szög</th><th>$\cos\varphi$</th><th>$\vec a\cdot\vec b$</th></tr>'
   r'<tr><td>hegyesszög vagy $0^\circ$: $0^\circ\le\varphi<90^\circ$</td><td>pozitív</td><td>$>0$</td></tr>'
   r'<tr><td>derékszög, $\varphi=90^\circ$</td><td>$0$</td><td>$=0$</td></tr>'
   r'<tr><td>tompaszög vagy $180^\circ$: $90^\circ<\varphi\le180^\circ$</td><td>negatív</td><td>$<0$</td></tr></table>',
   doboz("tetel", "A merőlegesség feltétele",
         r'<p>Két nem nullvektor pontosan akkor <b>merőleges</b>, ha a skaláris szorzatuk nulla:</p>'
         r'$$\vec a\perp\vec b\iff\vec a\cdot\vec b=0 .$$'
         r'<p><i>Indoklás:</i> $|\vec a|\ne0$ és $|\vec b|\ne0$, ezért a szorzat csak úgy lehet '
         r'$0$, ha $\cos\varphi=0$, vagyis $\varphi=90^\circ$.</p>',
         hid="tetel-merolegesseg"),
   r'<p>Ez a témakör egyik legtöbbet használt eszköze: merőlegességet <b>rajz nélkül</b>, '
   r'egyetlen számolással dönthetünk el — mihelyt a koordinátákból ki tudjuk számolni a '
   r'skaláris szorzatot. Ez következik.</p>',
   kviz(r'Az $\vec a$ és a $\vec b$ nem nullvektorok, és $\vec a\cdot\vec b=0$. Mi következik ebből?',
        [r'$\vec a$ és $\vec b$ merőleges', r'$\vec a\cdot\vec b$ a nullvektor',
         r'$\vec a$ és $\vec b$ párhuzamos', r'$\vec a=-\vec b$'], 0,
        jo="✔ Nem nullvektoroknál a nulla skaláris szorzat pontosan a merőlegességet jelenti.",
        nem="✘ A 0 itt a SZÁM nulla, nem nullvektor — a skaláris szorzat mindig szám. Mivel "
            "egyik vektor sem nullvektor, cos φ = 0, tehát φ = 90°: a két vektor merőleges."),
 ]),

 ("Koordinátákkal", [
   r'<p>Az egységvektorok egymással vett szorzatai a definícióból: $\vec i\cdot\vec i='
   r'1\cdot1\cdot\cos0^\circ=1$, és ugyanígy $\vec j\cdot\vec j=\vec k\cdot\vec k=1$; a '
   r'különbözők merőlegesek, ezért $\vec i\cdot\vec j=\vec j\cdot\vec k=\vec k\cdot\vec i=0$. '
   r'Ha az $(x_1\vec i+y_1\vec j+z_1\vec k)\cdot(x_2\vec i+y_2\vec j+z_2\vec k)$ szorzatban '
   r'minden tagot minden taggal összeszorzunk, a kilenc tagból hat nulla lesz, és csak ez marad:</p>',
   doboz("tetel", "A skaláris szorzat koordinátákkal · tulajdonságok",
         r'<p>Ha $\vec a=(x_1;y_1;z_1)$ és $\vec b=(x_2;y_2;z_2)$, akkor</p>'
         r'$$\vec a\cdot\vec b=x_1x_2+y_1y_2+z_1z_2 .$$'
         r'<p>Bármely vektorokra és $\lambda$ valós számra:</p>'
         r'<ul><li>$\vec a\cdot\vec b=\vec b\cdot\vec a$ <i>(kommutativitás)</i></li>'
         r'<li>$\vec a\cdot(\vec b+\vec c)=\vec a\cdot\vec b+\vec a\cdot\vec c$ <i>(disztributivitás)</i></li>'
         r'<li>$(\lambda\vec a)\cdot\vec b=\lambda(\vec a\cdot\vec b)$</li>'
         r'<li>$\vec a\cdot\vec a=|\vec a|^2$</li></ul>',
         hid="tetel-skalaris-koordinatak"),
   r'<p><b>Példa.</b> $\vec a=(2;-1;3)$ és $\vec b=(1;4;-2)$: '
   r'$\vec a\cdot\vec b=2\cdot1+(-1)\cdot4+3\cdot(-2)=2-4-6=-8$. A szorzat negatív, tehát a két '
   r'vektor <b>tompaszöget</b> zár be.</p>'
   r'<p><b>Az ábra és a szám.</b> Az $xy$ síkban fekvő $\vec p=(4;1;0)$ és $\vec q=(-1;3;0)$ '
   r'vektort felrajzolva „majdnem merőlegesnek” látszanak. A szám dönt: '
   r'$\vec p\cdot\vec q=-4+3+0=-1<0$, tehát a szögük <b>kicsit nagyobb</b> $90^\circ$-nál '
   r'(számológéppel kb. $94{,}4^\circ$). A rajz becslésre jó, a döntést a skaláris szorzat hozza.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„$(3;-1;2)\cdot(1;2;4)=(3\cdot1;\,-1\cdot2;\,2\cdot4)=(3;-2;8)$.”</i></p>'
         r'<p>Maxi a koordinátánkénti szorzatokat <b>vektorba</b> írta — pedig a skaláris '
         r'szorzat <b>egyetlen szám</b>. A három szorzatot össze kell adni: '
         r'$3-2+8=9$.</p>'
         r'<p>Maxi másik reakciója: <i>„negatív lett a koszinusz, biztos elszámoltam”</i>. '
         r'Nem feltétlenül! $\cos\varphi<0$ egyszerűen azt jelenti, hogy a szög '
         r'<b>tompaszög</b> — és a számológép ilyenkor $90^\circ$-nál nagyobb szöget ad.</p>'),
 ]),

 ("A két vektor szögének kiszámítása", [
   r'<p>A definíciót és a koordinátás képletet összekapcsolva kifejezhető a két vektor '
   r'szögének koszinusza — <b>csupa koordinátákból számolható</b> mennyiséggel:</p>'
   r'$$\cos\varphi=\frac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}'
   r'=\frac{x_1x_2+y_1y_2+z_1z_2}{\sqrt{x_1^2+y_1^2+z_1^2}\cdot\sqrt{x_2^2+y_2^2+z_2^2}} .$$',
   doboz("pelda", "Kristály-kamra szimuláció — a szög számológéppel",
         r'<p>Számítsd ki az $\vec a=(3;-1;2)$ és a $\vec b=(1;2;4)$ vektor szögét fokban, '
         r'egy tizedesjegyre kerekítve! Merőleges-e az $\vec a$ a $\vec d=(2;4;-1)$ vektorra?</p>',
         hid="pelda-szog",
         lenyilo=("Megoldás",
                  r'<p><b>1. A skaláris szorzat:</b> $\vec a\cdot\vec b=3\cdot1+(-1)\cdot2+2\cdot4=9$.</p>'
                  r'<p><b>2. Az intenzitások:</b> $|\vec a|=\sqrt{9+1+4}=\sqrt{14}$, '
                  r'$|\vec b|=\sqrt{1+4+16}=\sqrt{21}$.</p>'
                  r'<p><b>3. A koszinusz:</b> $\cos\varphi=\dfrac{9}{\sqrt{14}\cdot\sqrt{21}}='
                  r'\dfrac{9}{\sqrt{294}}\approx0{,}5249$.</p>'
                  r'<p><b>4. A szög számológéppel</b> (fok üzemmódban, <b>D</b>/<b>DEG</b>), két '
                  r'lépésben: előbb <code>9 ÷ √294 =</code> (ez $0{,}5249\ldots$), majd '
                  r'<code>SHIFT</code> <code>cos</code> <code>Ans</code> <code>=</code> — a '
                  r'<code>SHIFT cos</code> a $\cos^{-1}$. Az eredmény $58{,}34\ldots$, kerekítve '
                  r'$\varphi\approx58{,}3^\circ$. <i>Az <code>Ans</code> a teljes részeredményt '
                  r'viszi tovább, így nem kerekítesz menet közben.</i></p>'
                  r'<p><b>5. Merőlegesség:</b> $\vec a\cdot\vec d=3\cdot2+(-1)\cdot4+2\cdot(-1)='
                  r'6-4-2=0$, tehát $\vec a\perp\vec d$.</p>'
                  r'<p class="vegeredmeny">$\varphi\approx58{,}3^\circ$ · $\vec a\cdot\vec d=0$, '
                  r'tehát $\vec a$ és $\vec d$ merőleges</p>')),
   r'<p><b>Ellenőrzés fejben.</b> Mielőtt a gépet elővennéd, nézd meg a skaláris szorzat '
   r'<b>előjelét</b>: pozitívnál $90^\circ$ alatti, negatívnál fölötti szöget kell kapnod — ha '
   r'nem így van, elírtad a törtet. Ha pedig $0$ és $3{,}14$ közötti tizedes tört jön ki, a gép '
   r'valószínűleg <b>radiánban</b> számol: nézd meg, hogy <b>D</b> (DEG) áll-e a kijelzőn.</p>',
   GY(FGY + "#alap-1", "A 1–8", FGY + "#kozep-1", "K 1–6"),
   brief('<b>Medúza:</b> A skaláris szorzat számot adott: megmondta, mennyire dolgozik egyik '
         'nyíl a másik irányában. Crni Grom most két hullámot indít egyszerre, és a kristály '
         'egy <b>harmadik</b> irányba rezdül meg. Van egy másik szorzat is — és az '
         '<b>vektort</b> ad.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Amikor a hullám két irányból érkezik, a kristály egy <b>harmadik</b> '
         'irányban rezdül meg — mindkettőre merőlegesen. Crni Grom a jobb kezét emeli: '
         'hüvelykujj, mutatóujj, középső ujj. A vektoriális szorzat ezt a harmadik irányt adja '
         'meg, a hossza pedig elárulja, <b>mekkora felületet</b> feszít ki a két hullám.'),
   r'<p>Ebben az egységben a két vektorból <b>vektort</b> adó szorzattal ismerkedünk meg. '
   r'A legfontosabb alkalmazása a <b>terület</b>: paralelogrammáé és háromszögé, akár '
   r'térbeli pontokból is. A koordinátás kiszámításához a '
   r'<a href="../03-linearis-rendszerek/tananyag-determinans.html#tetel-kifejtes">determináns '
   r'kifejtését</a> használjuk.</p>',
 ]),

 ("A definíció", [
   doboz("definicio", "Vektoriális szorzat",
         r'<p>Két vektor <b>vektoriális szorzata</b> az az $\vec a\times\vec b$ <b>vektor</b>, amelynek</p>'
         r'<ul><li><b>intenzitása</b> $|\vec a\times\vec b|=|\vec a|\,|\vec b|\sin\varphi$;</li>'
         r'<li><b>iránya</b> merőleges az $\vec a$-ra és a $\vec b$-re is (tehát a két vektor '
         r'síkjára);</li>'
         r'<li><b>irányítása</b> a <b>jobbkéz-szabály</b> szerinti: ha jobb kezünk hüvelykujja '
         r'az $\vec a$, mutatóujja a $\vec b$ irányába mutat, akkor a behajlított középső ujjunk '
         r'az $\vec a\times\vec b$ irányítását mutatja.</li></ul>'
         r'<p>Ha $\vec a$ és $\vec b$ párhuzamos (vagy valamelyik nullvektor), akkor '
         r'$\vec a\times\vec b=\vec 0$.</p>',
         hid="def-vektorialis"),
   abra(SVG_VX, 'Az $\\vec a$ és a $\\vec b$ a kék paralelogrammát feszíti ki; az $\\vec a\\times\\vec b$ '
        'merőleges a síkjára, és a jobbkéz-szabály szerint felfelé mutat. (A paralelogrammát '
        'térben, vízszintes síkban fekvőnek képzeld el.)'),
   r'<p>Figyeld meg: a definícióban <b>szinusz</b> áll, nem koszinusz. A szorzat intenzitása '
   r'merőleges vektoroknál ($\sin90^\circ=1$) a legnagyobb, párhuzamosaknál '
   r'($\sin0^\circ=\sin180^\circ=0$) nulla — éppen fordítva, mint a skaláris szorzat abszolút '
   r'értéke.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A <b>forgatónyomaték</b> vektoriális szorzat: $\vec M=\vec r\times\vec F$, ahol '
         r'$\vec r$ a forgástengelytől az erő támadáspontjáig mutat. Ezért könnyű az ajtót a '
         r'kilincsnél — a zsanértól <b>távol</b> és <b>merőlegesen</b> — tolni, és ezért nem mozdul, '
         r'ha a zsanér felé nyomod: ott $\sin\varphi=0$. A nyomaték vektora a forgástengely '
         r'irányába mutat.</p>'),
   kviz(r'Melyik állítás igaz a két szorzat eredményére?',
        [r'$\vec a\cdot\vec b$ szám, $\vec a\times\vec b$ vektor',
         'mindkettő szám', 'mindkettő vektor',
         r'$\vec a\cdot\vec b$ vektor, $\vec a\times\vec b$ szám'], 0,
        jo="✔ A skaláris szorzat szám, a vektoriális szorzat vektor — a hossza az, ami szám.",
        nem="✘ A skaláris szorzat szám (|a|·|b|·cos φ). A vektoriális szorzat vektor, amely "
            "merőleges mindkét tényezőre; csak az INTENZITÁSA szám, |a|·|b|·sin φ."),
 ]),

 ("A szorzat intenzitása: terület", [
   r'<p>Az $\vec a$ és a $\vec b$ által kifeszített paralelogramma alapja $|\vec a|$, a hozzá '
   r'tartozó magassága $|\vec b|\sin\varphi$. A területe tehát $|\vec a|\,|\vec b|\sin\varphi$ '
   r'— és ez éppen $|\vec a\times\vec b|$.</p>',
   doboz("tetel", "Terület a vektoriális szorzattal",
         r'$$T_{\text{paralelogramma}}=|\vec a\times\vec b|,\qquad '
         r'T_{\text{háromszög}}=\frac12\,|\vec a\times\vec b| ,$$'
         r'<p>ahol $\vec a$ és $\vec b$ a paralelogramma, illetve a háromszög <b>egy csúcsból '
         r'kiinduló</b> két oldalvektora.</p>',
         hid="tetel-terulet"),
   r'<p><b>Példa.</b> $|\vec a|=4$, $|\vec b|=6$, $\varphi=30^\circ$: a paralelogramma '
   r'területe $4\cdot6\cdot\sin30^\circ=12$, a két vektor által kifeszített háromszögé $6$. '
   r'Számológéppel: $|\vec a|=5$, $|\vec b|=3$, $\varphi=40^\circ$ esetén a paralelogramma '
   r'területe $T=15\sin40^\circ\approx9{,}64$.</p>'
   r'<p>A $\tfrac12|\vec a\times\vec b|$ képlet a háromszög területének ismert '
   r'$T=\tfrac12ab\sin\gamma$ képlete — csak most vektorokkal írva. Az igazi ereje akkor látszik, amikor a háromszög <b>három térbeli '
   r'pontjával</b> adott, és a szögét nem ismerjük: ekkor a koordinátás képlet segít.</p>',
 ]),

 ("Koordinátákkal — determinánssal", [
   doboz("tetel", "A vektoriális szorzat koordinátákkal",
         r'<p>Ha $\vec a=(x_1;y_1;z_1)$ és $\vec b=(x_2;y_2;z_2)$, akkor</p>'
         r'$$\begin{aligned}\vec a\times\vec b&=\begin{vmatrix}\vec i&\vec j&\vec k\\ x_1&y_1&z_1\\ x_2&y_2&z_2\end{vmatrix}\\'
         r'&=\vec i\begin{vmatrix}y_1&z_1\\ y_2&z_2\end{vmatrix}'
         r'-\vec j\begin{vmatrix}x_1&z_1\\ x_2&z_2\end{vmatrix}'
         r'+\vec k\begin{vmatrix}x_1&y_1\\ x_2&y_2\end{vmatrix} ,\end{aligned}$$'
         r'<p>vagyis $\vec a\times\vec b=\left(y_1z_2-z_1y_2;\;\;-(x_1z_2-z_1x_2);\;\;'
         r'x_1y_2-y_1x_2\right)$.</p>',
         hid="tetel-vektorialis-koordinatak"),
   r'<p>A „determináns” első sorában vektorok állnak, ezért ez nem igazi szám-determináns — '
   r'<b>emlékeztető séma</b>: az első sor szerinti kifejtés előjelszabálya ($+\,-\,+$) adja '
   r'a helyes képletet. A $2\times2$-es aldeterminánsokat úgy kapod, hogy letakarod az adott '
   r'egységvektor sorát és oszlopát; értékük $\begin{vmatrix}p&q\\ r&s\end{vmatrix}=ps-qr$.</p>'
   r'<p><b>Példa.</b> $\vec a=(2;-1;3)$, $\vec b=(1;4;-2)$:</p>'
   r'$$\begin{aligned}\vec a\times\vec b&=\vec i\begin{vmatrix}-1&3\\ 4&-2\end{vmatrix}'
   r'-\vec j\begin{vmatrix}2&3\\ 1&-2\end{vmatrix}+\vec k\begin{vmatrix}2&-1\\ 1&4\end{vmatrix}'
   r'\\&=\vec i\,(2-12)-\vec j\,(-4-3)+\vec k\,(8+1)=(-10;\,7;\,9).\end{aligned}$$'
   r'<p><b>Ellenőrzés:</b> az eredménynek mindkét tényezőre merőlegesnek kell lennie. '
   r'$(2;-1;3)\cdot(-10;7;9)=-20-7+27=0$ ✔ és $(1;4;-2)\cdot(-10;7;9)=-10+28-18=0$ ✔.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„$\vec a\times\vec b=\vec i\,(2-12)+\vec j\,(-4-3)+\vec k\,(8+1)=(-10;\,-7;\,9)$.”</i></p>'
         r'<p>Maxi a <b>középső tag előtti mínuszt</b> hagyta el. A kifejtés előjelei '
         r'$+\vec i$, $-\vec j$, $+\vec k$ — a középső aldeterminánst ellentett előjellel kell '
         r'venni. A merőlegességi próba azonnal leleplezi: '
         r'$(2;-1;3)\cdot(-10;-7;9)=-20+7+27=14\ne0$.</p>'
         r'<p>Maxi másik tévedése: <i>„a sorrend mindegy, mint a szorzásnál”</i>. A vektoriális '
         r'szorzatban a sorrend felcserélése <b>előjelet vált</b> — erről szól a következő szakasz.</p>'),
   doboz("pelda", "Kristály-kamra szimuláció — háromszög területe három pontból",
         r'<p>Egy kristálylap csúcsai $A(1;0;2)$, $B(3;1;1)$ és $C(2;3;4)$. Mekkora a '
         r'területe?</p>',
         hid="pelda-haromszog-terulet",
         lenyilo=("Megoldás",
                  r'<p><b>1. Két oldalvektor ugyanabból a csúcsból:</b> '
                  r'$\overrightarrow{AB}=(2;1;-1)$, $\overrightarrow{AC}=(1;3;2)$.</p>'
                  r'<p><b>2. A vektoriális szorzat:</b></p>'
                  r'$$\overrightarrow{AB}\times\overrightarrow{AC}='
                  r'\vec i\begin{vmatrix}1&-1\\ 3&2\end{vmatrix}-\vec j\begin{vmatrix}2&-1\\ 1&2\end{vmatrix}'
                  r'+\vec k\begin{vmatrix}2&1\\ 1&3\end{vmatrix}=5\vec i-5\vec j+5\vec k=(5;-5;5).$$'
                  r'<p><b>3. Az intenzitása:</b> $\sqrt{25+25+25}=\sqrt{75}=5\sqrt3$.</p>'
                  r'<p><b>4. A terület a fele:</b> $T=\dfrac{5\sqrt3}{2}\approx4{,}33$.</p>'
                  r'<p class="vegeredmeny">$T=\dfrac{5\sqrt3}{2}\approx4{,}33$ területegység</p>')),
 ]),

 ("Tulajdonságok", [
   doboz("tetel", "A vektoriális szorzat tulajdonságai",
         r'<p>Bármely $\vec a$, $\vec b$, $\vec c$ vektorra és $\lambda$ valós számra:</p>'
         r'<ul><li>$\vec b\times\vec a=-\left(\vec a\times\vec b\right)$ '
         r'<i>(antikommutativitás — a sorrend felcserélése előjelet vált)</i></li>'
         r'<li>$\vec a\times(\vec b+\vec c)=\vec a\times\vec b+\vec a\times\vec c$ <i>(disztributivitás)</i></li>'
         r'<li>$(\lambda\vec a)\times\vec b=\vec a\times(\lambda\vec b)=\lambda\left(\vec a\times\vec b\right)$</li>'
         r'<li>$\vec a\times\vec a=\vec 0$; két nem nullvektor pontosan akkor párhuzamos, ha '
         r'$\vec a\times\vec b=\vec 0$</li>'
         r'<li>$\vec i\times\vec j=\vec k$, &nbsp; $\vec j\times\vec k=\vec i$, &nbsp; '
         r'$\vec k\times\vec i=\vec j$ &nbsp; (és például $\vec j\times\vec i=-\vec k$)</li></ul>',
         hid="tetel-vektorialis-tulajdonsagok"),
   abra(SVG_VX_ANTI, 'A $\\vec b\\times\\vec a$ ugyanolyan hosszú, mint az $\\vec a\\times\\vec b$, '
        'de ellentétes irányítású: a jobb kéz hüvelykujja most a $\\vec b$, mutatóujja az '
        '$\\vec a$ irányába mutat, így a középső ujj lefelé mutat.'),
   r'<p>A párhuzamossági feltétel koordinátákkal is kényelmes: '
   r'$(2;-1;3)\times(-4;2;-6)=(0;0;0)$, tehát a két vektor párhuzamos — ezt az '
   r'<a href="tananyag-koordinatak-terben.html#tetel-koordinatas-muveletek">arányos '
   r'koordinátákból</a> is láttuk.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — egyszerűsítés a tulajdonságokkal",
         r'<p>Egyszerűsítsd a $(2\vec a-\vec b)\times(\vec a+3\vec b)$ kifejezést! Mennyi az '
         r'értéke és az intenzitása, ha $\vec a\times\vec b=(1;-2;2)$?</p>',
         hid="pelda-tulajdonsagok",
         lenyilo=("Megoldás",
                  r'<p>Tagonként szorzunk — a <b>sorrendet megtartva</b>:</p>'
                  r'$$(2\vec a-\vec b)\times(\vec a+3\vec b)=2\,\vec a\times\vec a+6\,\vec a\times\vec b'
                  r'-\vec b\times\vec a-3\,\vec b\times\vec b .$$'
                  r'<p>$\vec a\times\vec a=\vec b\times\vec b=\vec 0$, és $-\vec b\times\vec a='
                  r'+\vec a\times\vec b$, így az eredmény $6\,\vec a\times\vec b+\vec a\times\vec b='
                  r'7\,(\vec a\times\vec b)$.</p>'
                  r'<p>Behelyettesítve: $7\cdot(1;-2;2)=(7;-14;14)$, intenzitása '
                  r'$\sqrt{49+196+196}=\sqrt{441}=21$.</p>'
                  r'<p class="vegeredmeny">$(2\vec a-\vec b)\times(\vec a+3\vec b)=7\,(\vec a\times\vec b)'
                  r'=(7;-14;14)$, intenzitása $21$</p>')),
   kviz(r'Tudjuk, hogy $\vec a\times\vec b=(2;-3;1)$. Mivel egyenlő $\vec b\times\vec a$?',
        [r'$(-2;3;-1)$', r'$(2;-3;1)$', r'$(1;-3;2)$', r'$(0;0;0)$'], 0,
        jo="✔ A sorrend felcserélése előjelet vált: b × a = −(a × b).",
        nem="✘ A vektoriális szorzat NEM kommutatív: b × a = −(a × b) = (−2; 3; −1). A két "
            "vektor ugyanarra a síkra merőleges, de ellentétes irányba mutat."),
   GY(FGY + "#alap-9", "A 9–16", FGY + "#kozep-7", "K 7–12"),
   brief('<b>Medúza:</b> Két szorzat, két kérdés. Mekkora a <b>szög</b>? Arra a skaláris '
         'szorzat felel. Mekkora a <b>terület</b>? Arra a vektoriális. Crni Grom most a Kamra '
         'valódi kristálylapjait mutatja — ideje, hogy az eszközöket élesben használjuk.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- C1
C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Az irányítótű elkészült. Most már nem az a kérdés, hogyan számolunk, '
         'hanem hogy <b>melyik eszközt</b> vesszük elő. Szög? Merőlegesség? Terület? Erő? Crni '
         'Grom szerint minden kérdésnek megvan a maga szorzata — és aki rosszat választ, az '
         'hibátlan számolással is rossz eredményt kap.'),
   r'<p>Ez a témakör záró egysége: rendszerezzük, <b>mire melyik szorzat</b> való, egy '
   r'háromszögről három pontból mindent kiszámolunk, és egy rövid kitekintésben megnézzük, '
   r'hogyan számol a fizika erőkkel és munkával.</p>',
 ]),

 ("Melyik szorzat mire jó", [
   doboz("tetel", "Melyik eszköz melyik kérdésre",
         r'<table class="tt-table"><tr><th>A kérdés</th><th>Az eszköz</th><th>A képlet</th></tr>'
         r'<tr><td>két pont távolsága, egy oldal hossza</td><td>intenzitás</td>'
         r'<td>ha $\overrightarrow{AB}=(x;y;z)$: $|\overrightarrow{AB}|=\sqrt{x^2+y^2+z^2}$</td></tr>'
         r'<tr><td>két vektor <b>szöge</b></td><td>skaláris szorzat</td>'
         r'<td>$\cos\varphi=\dfrac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}$</td></tr>'
         r'<tr><td><b>merőleges</b>-e</td><td>skaláris szorzat</td><td>$\vec a\cdot\vec b=0$</td></tr>'
         r'<tr><td>a $\vec b$ skaláris vetülete az $\vec a$ irányára, munka</td><td>skaláris szorzat</td>'
         r'<td>$\dfrac{\vec a\cdot\vec b}{|\vec a|}$, &nbsp; $W=\vec F\cdot\vec s$</td></tr>'
         r'<tr><td>paralelogramma, háromszög <b>területe</b></td><td>vektoriális szorzat</td>'
         r'<td>$|\vec a\times\vec b|$, &nbsp; $\tfrac12|\vec a\times\vec b|$</td></tr>'
         r'<tr><td><b>párhuzamos</b>-e</td><td>vektoriális szorzat (vagy arányos koordináták)</td>'
         r'<td>$\vec a\times\vec b=\vec 0$</td></tr>'
         r'<tr><td>mindkét vektorra <b>merőleges irány</b></td><td>vektoriális szorzat</td>'
         r'<td>$\vec a\times\vec b$</td></tr></table>',
         hid="tetel-melyik-szorzat"),
   r'<p>A táblázat egy mondatban: <b>a skaláris szorzat a szöghöz, a vektoriális a '
   r'területhez</b> tartozik. A skaláris vetület képlete a definícióból jön: '
   r'$|\vec b|\cos\varphi=\dfrac{\vec a\cdot\vec b}{|\vec a|}$.</p>',
   kviz('Melyik párosítás <b>hibás</b>?',
        [r'háromszög területe → skaláris szorzat', r'két vektor szöge → skaláris szorzat',
         r'merőlegesség → a skaláris szorzat $0$',
         r'párhuzamosság → a vektoriális szorzat $\vec 0$'], 0,
        jo="✔ A területhez a vektoriális szorzat intenzitása kell: T = ½·|AB × AC|.",
        nem="✘ A hibás párosítás a terület: azt a vektoriális szorzat intenzitása adja "
            "(T = ½·|AB × AC|), nem a skaláris szorzat. A többi három párosítás helyes."),
 ]),

 ("Geometriai alkalmazások", [
   doboz("pelda", "Kristály-kamra szimuláció — egy háromszögről mindent",
         r'<p>A Kamra egyik kristálylapja az $A(2;1;0)$, $B(4;3;1)$, $C(1;3;2)$ csúcsú háromszög. '
         r'Számítsd ki</p>'
         r'<ol type="a"><li>az oldalai hosszát,</li>'
         r'<li>az $A$ csúcsnál lévő $\alpha$ szögét (fokban, egy tizedesre),</li>'
         r'<li>a területét!</li></ol>',
         hid="pelda-haromszog",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $\overrightarrow{AB}=(2;2;1)$, $\overrightarrow{AC}=(-1;2;2)$, '
                  r'$\overrightarrow{BC}=(-3;0;1)$. Hosszuk: $AB=\sqrt{4+4+1}=3$, '
                  r'$AC=\sqrt{1+4+4}=3$, $BC=\sqrt{9+0+1}=\sqrt{10}\approx3{,}16$. '
                  r'<i>(A háromszög egyenlő szárú.)</i></p>'
                  r'<p><b>b)</b> Az $A$-nál lévő szöghöz az <b>$A$-ból induló</b> két vektor kell: '
                  r'$\overrightarrow{AB}\cdot\overrightarrow{AC}=-2+4+2=4$, így '
                  r'$\cos\alpha=\dfrac{4}{3\cdot3}=\dfrac49\approx0{,}4444$, és számológéppel '
                  r'$\alpha\approx63{,}6^\circ$.</p>'
                  r'<p><b>c)</b></p>$$\overrightarrow{AB}\times\overrightarrow{AC}='
                  r'\vec i\begin{vmatrix}2&1\\ 2&2\end{vmatrix}-\vec j\begin{vmatrix}2&1\\ -1&2\end{vmatrix}'
                  r'+\vec k\begin{vmatrix}2&2\\ -1&2\end{vmatrix}=(2;-5;6),$$<p>intenzitása '
                  r'$\sqrt{4+25+36}=\sqrt{65}$, tehát $T=\dfrac{\sqrt{65}}{2}\approx4{,}03$.</p>'
                  r'<p><i>Ellenőrzés: $T=\tfrac12\cdot AB\cdot AC\cdot\sin\alpha='
                  r'\tfrac12\cdot3\cdot3\cdot\sin63{,}6^\circ\approx4{,}03$ ✔.</i></p>'
                  r'<p class="vegeredmeny">a) $AB=AC=3$, $BC=\sqrt{10}\approx3{,}16$ · '
                  r'b) $\alpha\approx63{,}6^\circ$ · c) $T=\dfrac{\sqrt{65}}{2}\approx4{,}03$</p>')),
   r'<p><b>Négyszögek.</b> Ha az $ABC$ háromszöget a $D=B+C-A=(3;5;3)$ csúcs egészíti ki '
   r'$ABDC$ paralelogrammává, akkor a fenti számokból rögtön látszik a fajtája is: a két szomszédos '
   r'oldal egyenlő ($AB=AC=3$), tehát <b>rombusz</b>; a skaláris szorzatuk viszont $4\ne0$, tehát '
   r'<b>nem négyzet</b>. Általában egy paralelogramma <b>pontosan akkor téglalap</b>, ha két '
   r'szomszédos oldalvektorának skaláris szorzata $0$; <b>pontosan akkor rombusz</b>, ha két '
   r'szomszédos oldala egyenlő hosszú; és <b>négyzet</b>, ha mindkettő teljesül.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„Az $A$ csúcsnál lévő szöghöz az $\overrightarrow{AB}$ és a '
         r'$\overrightarrow{CA}$ vektort vettem: $\overrightarrow{AB}\cdot\overrightarrow{CA}='
         r'-4$, $\cos\alpha=-\tfrac49$, $\alpha\approx116{,}4^\circ$.”</i></p>'
         r'<p>A $\overrightarrow{CA}$ <b>befelé</b> mutat az $A$ csúcsba, nem onnan kifelé — '
         r'így Maxi a <b>mellékszöget</b> kapta: $180^\circ-63{,}6^\circ=116{,}4^\circ$. Egy '
         r'háromszög csúcsánál lévő szöghöz mindkét vektor <b>abból a csúcsból induljon</b>: '
         r'az $A$-nál $\overrightarrow{AB}$ és $\overrightarrow{AC}$, a $B$-nél '
         r'$\overrightarrow{BA}$ és $\overrightarrow{BC}$.</p>'
         r'<p><i>Árulkodó jel: ha az $A$-nál tompaszög volna, a vele szemközti $BC$ oldalra '
         r'$BC^2>AB^2+AC^2=18$ teljesülne (a koszinusztétel szerint $116{,}4^\circ$ mellett '
         r'$BC^2=26$ lenne). A valóságban $BC^2=10<18$, tehát az $A$-nál hegyesszög van.</i></p>'),
   kviz(r'Az $ABC$ háromszög $B$ csúcsánál lévő szögét számolod. Melyik vektorpár skaláris '
        r'szorzatából indulj ki?',
        [r'$\overrightarrow{BA}$ és $\overrightarrow{BC}$', r'$\overrightarrow{AB}$ és $\overrightarrow{BC}$',
         r'$\overrightarrow{BA}$ és $\overrightarrow{CB}$', r'$\overrightarrow{AB}$ és $\overrightarrow{AC}$'], 0,
        jo="✔ Mindkét vektor a B csúcsból indul — így a háromszög belső szögét kapod.",
        nem="✘ A B-nél lévő szöghöz mindkét vektornak a B-ből kell indulnia: BA és BC. Ha az "
            "egyiket megfordítod (AB vagy CB), a mellékszöget kapod; az AB és AC pedig az A-nál "
            "lévő szöget adja."),
 ]),

 ("Fizikai alkalmazások", [
   r'<p>A fizikában az erő, az elmozdulás és a sebesség vektor — a velük végzett számolás '
   r'pontosan az, amit ebben a témakörben tanultál. Két alapeset:</p>'
   r'<ul><li>Több erő együttes hatása az <b>eredő erő</b>: a vektorok <b>összege</b>; '
   r'nagysága (erőnél így mondjuk az intenzitást) az összeg intenzitása.</li>'
   r'<li>Az állandó $\vec F$ erő <b>munkája</b> az $\vec s$ elmozdulás során a <b>skaláris '
   r'szorzat</b>: $W=\vec F\cdot\vec s=|\vec F|\,|\vec s|\cos\varphi$. Például egy $40$ N-os, '
   r'az elmozdulással $60^\circ$-os szöget bezáró erő munkája $5$ m-es elmozdulás során '
   r'$40\cdot5\cdot\tfrac12=100$ J.</li></ul>',
   doboz("pelda", "Kristály-kamra szimuláció — eredő erő és munka",
         r'<p>Egy kristályra két erő hat: $\vec F_1=(2;3;1)$ N és $\vec F_2=(1;-1;1)$ N. '
         r'a) Mekkora az eredő erő, és mekkora a nagysága? b) Miközben a két erő hat rá, a kristály '
         r'elmozdulása $\vec s=(4;1;0)$ m. Mennyi munkát végez az eredő erő?</p>',
         hid="pelda-ero",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $\vec F=\vec F_1+\vec F_2=(3;2;2)$ N, nagysága '
                  r'$|\vec F|=\sqrt{9+4+4}=\sqrt{17}\approx4{,}12$ N.</p>'
                  r'<p><b>b)</b> $W=\vec F\cdot\vec s=3\cdot4+2\cdot1+2\cdot0=14$ J. '
                  r'<i>Ellenőrzés: a két erő munkája külön $\vec F_1\cdot\vec s=11$ J és '
                  r'$\vec F_2\cdot\vec s=3$ J, összesen szintén $14$ J.</i></p>'
                  r'<p class="vegeredmeny">a) $\vec F=(3;2;2)$ N, $|\vec F|=\sqrt{17}\approx4{,}12$ N · '
                  r'b) $W=14$ J</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Egy darut, hidat vagy tetőszerkezetet tervező mérnök minden rúdban és kötélben '
         r'ébredő erőt vektorként kezel: a nyugalom egyik feltétele, hogy minden csomópontban az erők '
         r'<b>összege nullvektor</b>. Ez a <b>statika</b> — és a számolás lépései pontosan azok, '
         r'amelyeket most koordinátákkal végeztél.</p>'),
   GY(FGY + "#alap-17", "A 17–22", FGY + "#kozep-13", "K 13–18"),
   brief('<b>Medúza:</b> Crni Grom leereszti a kezét — a Királyi Irányítótű a tiéd. Az irányt '
         'már ismered. A Kamra térképén azonban nem elég tudni, <b>merre</b> kell menni: pontosan '
         'be kell mérni, <b>hol</b> fekszenek az egyenesek és a körök. Az irányítótűt ezért '
         'Kanrak és Tér-eb viszi tovább — a következő küldetés az <b>analitikus geometria</b>.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-skalaris-szorzat.html",
     cim="A skaláris szorzat",
     cim_tiszta="A skaláris szorzat",
     alcim="A definíció és a skaláris vetület, az előjel jelentése és a merőlegesség feltétele, "
           "a koordinátás képlet és két vektor szögének kiszámítása számológéppel.",
     chip=KUL + " · 3/5", szakaszok=B1,
     elozo=("tananyag-koordinatak-terben.html", "Vektorok a térben"),
     kovetkezo=("tananyag-vektorialis-szorzat.html", "A vektoriális szorzat")),
 lap(**T, fajl="tananyag-vektorialis-szorzat.html",
     cim="A vektoriális szorzat",
     cim_tiszta="A vektoriális szorzat",
     alcim="A definíció a jobbkéz-szabállyal, a szorzat intenzitása mint terület, a "
           "determinánsos képlet és a tulajdonságok.",
     chip=KUL + " · 4/5", szakaszok=B2,
     elozo=("tananyag-skalaris-szorzat.html", "A skaláris szorzat"),
     kovetkezo=("tananyag-vektorok-alkalmazasa.html", "Vektorok munkában")),
 lap(**T, fajl="tananyag-vektorok-alkalmazasa.html",
     cim="Vektorok munkában — szög, terület, erő",
     cim_tiszta="Vektorok munkában",
     alcim="Melyik szorzat mire való; egy térbeli háromszög oldalai, szöge és területe; eredő erő "
           "és munka.",
     chip=KUL + " · 5/5", szakaszok=C1,
     elozo=("tananyag-vektorialis-szorzat.html", "A vektoriális szorzat"),
     kovetkezo=(FGY, "Feladatok — szorzatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
