# -*- coding: utf-8 -*-
"""4e/01 — A es B blokk (1. resz): a hatarertek fogalma (A), racionalis tortek (B1),
gyokos kifejezesek (B2). Mentor: Ved Vilmos (Nagol javit). Kuldetes: A Vegtelenbe es... Ne Tovabb!
Specifikacio: projektek/4e/munkafajlok/narrativa_01-sorozatok-hatarerteke.md"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="4e", mappa="01-sorozatok-hatarerteke", temakor="Sorozatok határértéke")
FGY = "feladatok-hatarertek.html"
KUL = "A Végtelenbe és… Ne Tovább!"
E306 = "../../3e/06-indukcio-sorozatok/"

KEK, BORO, ZOLD, PIROS = "#3b82f6", "#f59e0b", "#047857", "#ef4444"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FGY}#nehez-{tol}">Zsoldos-lista, nehéz {tol}–{ig}</a>.</p>')


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, symbols, limit, oo, sqrt, simplify, together, fraction, expand
E = []


def chk(nev, kapott, vart):
    ok = (len(kapott) == len(vart) and all(a == b or simplify(a - b) == 0 for a, b in zip(kapott, vart))) \
        if isinstance(kapott, (list, tuple)) else (kapott == vart or simplify(kapott - vart) == 0)
    if not ok:
        E.append((nev, kapott, vart))


n = symbols("n", positive=True, integer=True)
L = lambda e: limit(e, n, oo)
a = lambda k: R(2*k + 1, k)
chk("A-besurusodes", [a(k) for k in (1, 2, 5, 10, 100, 1000)],
    [3, R(5, 2), R(11, 5), R(21, 10), R(201, 100), R(2001, 1000)])
chk("A-lim", L((2*n + 1)/n), 2)
chk("A-sav-03", min(k for k in range(1, 50) if abs(a(k) - 2) < R(3, 10)), 4)
chk("A-sav-01", min(k for k in range(1, 50) if abs(a(k) - 2) < R(1, 10)), 11)
b = lambda k: R(3*k - 1, k + 1)
chk("A-pelda", [b(k) for k in (1, 10, 100, 1000)], [1, R(29, 11), R(299, 101), R(2999, 1001)])
chk("A-pelda-lim", L((3*n - 1)/(n + 1)), 3)
chk("A-pelda-tav", simplify(3 - (3*n - 1)/(n + 1)), 4/(n + 1))
chk("A-q-fel", [R(1, 2)**k for k in range(1, 5)], [R(1, 2), R(1, 4), R(1, 8), R(1, 16)])
chk("A-q-minusz-fel", [R(-1, 2)**k for k in range(1, 5)], [R(-1, 2), R(1, 4), R(-1, 8), R(1, 16)])
chk("A-q-ketto", [2**k for k in range(1, 5)], [2, 4, 8, 16])
chk("A-q-minusz-ketto", [(-2)**k for k in range(1, 5)], [-2, 4, -8, 16])
chk("A-muv-1", L(3 + 2/n), 3)
chk("A-muv-2", L((5 - 1/n**2)*(2 + 1/n)), 10)
chk("A-muv-3", L((4 - 1/n)/(2 + 3/n)), 2)
chk("A-hat-1", L((n + 5) - n), 5)
chk("A-hat-2", L(n**2 - n), oo)
chk("A-hat-3", [L(n/n), L(n**2/n), L(n/n**2)], [1, oo, 0])
chk("A-kviz-3", L((n + 3) - n), 3)
# B1
f1 = (6*n**2 - 5*n + 1)/(3*n**2 + 4)
chk("B1-kiemeles", L(f1), 2)
chk("B1-tabla", [f1.subs(n, k) for k in (10, 100, 1000)], [R(551, 304), R(59501, 30004), R(5995001, 3000004)])
chk("B1-eset-0", L((4*n + 7)/(2*n**2 - 3)), 0)
chk("B1-eset-minusz-vegtelen", L((n**2 - 4*n)/(5 - 2*n)), -oo)
chk("B1-kviz-1", L((3*n**2 + 1)/(6*n**3 - n)), 0)
chk("B1-szorzat", L((3*n - 1)**2/((n + 2)*(2*n + 5))), R(9, 2))
chk("B1-kob", L((1 - 2*n)**3/(4*n**3 + 1)), -2)
kul = (3*n**2 + 1)/(n + 2) - (3*n**2 - n)/(n + 1)
szam, nev = fraction(together(kul))
chk("B1-kulonbseg-szamlalo", expand(szam), -2*n**2 + 3*n + 1)
chk("B1-kulonbseg-nevezo", expand(nev), n**2 + 3*n + 2)
chk("B1-kulonbseg", L(kul), -2)
chk("B1-kviz-2", L(n**2/(n + 1) - n), -1)
# B2
chk("B2-pelda", L(sqrt(16*n**2 + 5*n - 2)/(3*n + 1)), R(4, 3))
chk("B2-kviz", L(sqrt(4*n**2 + 1)/(3*n)), R(2, 3))
chk("B2-nulla", L(sqrt(n**2 + 1)/n**2), 0)
chk("B2-vegtelen", L(n**2/sqrt(4*n**2 + 3)), oo)
chk("B2-negativ", L(sqrt(9*n**2 + 2)/(2 - 5*n)), R(-3, 5))
chk("B2-vegyes", L((2*n + sqrt(n**2 + 1))/(3*n)), 1)
assert not E, E
print("sympy önteszt: OK")


# ---------------------------------------------------------------- ábrák
def sav(svg, xr, yr, w, h, A, eps, felirat=""):
    """Vízszintes sáv (A − eps, A + eps) és szaggatott A-vonal a rácsháló fölé.
    A koordináta-leképezés a `svg_fuggvenyek` margóival egyezik."""
    bal, jobb, fent, lent = 26, 12, 14, 22
    px, py = w - bal - jobb, h - fent - lent
    X = lambda x: bal + (x - xr[0]) / (xr[1] - xr[0]) * px
    Y = lambda y: fent + (yr[1] - y) / (yr[1] - yr[0]) * py
    reszlet = (f'  <rect x="{X(xr[0]):.1f}" y="{Y(A + eps):.1f}" width="{px:.1f}" '
               f'height="{Y(A - eps) - Y(A + eps):.1f}" fill="#10b981" fill-opacity=".16"/>\n'
               f'  <line x1="{X(xr[0]):.1f}" y1="{Y(A):.1f}" x2="{X(xr[1]):.1f}" y2="{Y(A):.1f}" '
               f'stroke="#047857" stroke-width="1.2" stroke-dasharray="5 4"/>\n')
    if felirat:
        reszlet += (f'  <text x="{X(xr[1]) - 4:.1f}" y="{Y(A + eps) - 4:.1f}" font-size="11" '
                    f'fill="#047857" text-anchor="end">{felirat}</text>\n')
    i = svg.index("  </g>") + len("  </g>\n")
    return svg[:i] + reszlet + svg[i:]


XR, YR, W, H = (0, 13), (0, 3.4), 400, 250
SVG_SAV = sav(svg_fuggvenyek(
    [], xr=XR, yr=YR, w=W, h=H, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Az aₙ = (2n + 1)/n sorozat első tizenkét tagja pontokként; a pontok a 2-es "
           "szinthez közelítenek, és a negyedik tagtól kezdve mind a 2 körüli sávban vannak",
    pontok=[(k, float(a(k)), "", ZOLD if k >= 4 else PIROS) for k in range(1, 13)]),
    XR, YR, W, H, 2, 0.3, "2 ± 0,3")

SVG_DIVERGENS = svg_fuggvenyek(
    [], xr=(0, 9), yr=(-1.6, 1.6), w=330, h=200, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Az aₙ = (−1)ⁿ sorozat pontjai felváltva −1-en és 1-en: nincs olyan szám, amelyhez egy tagtól kezdve mind közel lennének",
    pontok=[(k, (-1)**k, "", BORO) for k in range(1, 9)])

# ---------------------------------------------------------------- A
A = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Kismotorral indulok. Az első percben 1 km-t teszek meg, a másodikban '
         'ennek a felét, a harmadikban a negyedét, és így tovább — végtelen sok lépés, tehát végtelen '
         'messzire jutok. 🌮 <i>Burek-matek:</i> „végtelen sok lépés = végtelen távolság.” '
         '<b>Nagol:</b> Hibás. A lépések egyre rövidebbek, és a megtett út egy <b>jól meghatározott '
         'számhoz</b> közelít, amelyet soha nem ér el. Ebben a témakörben azt tanuljuk meg, hogyan '
         'számoljuk ki, <b>mihez közelít</b> valami, ami soha nem ér oda.'),
 ]),

 ("Emlékeztető: mit tudunk a sorozatokról?", [
   r'<p class="lead">A tavalyi évből négy dolog kell. A <b>sorozat</b> minden $n$ természetes számhoz '
   r'egy valós számot rendel, ez az $a_n$ általános tag. <b>Monoton</b> a sorozat, ha a tagjai '
   r'végig nőnek (vagy legalábbis nem csökkennek), vagy végig csökkennek; <b>korlátos</b>, ha minden tagja két rögzített szám közé esik. '
   r'A <b>mértani sorozat</b> első $n$ tagjának összegére képletünk van.</p>'
   r'<p>Ha bármelyik bizonytalan, itt a tavalyi anyag: '
   '<a href="' + E306 + 'tananyag-sorozat-fogalma.html#def-sorozat">a sorozat fogalma</a> · '
   '<a href="' + E306 + 'tananyag-monotonitas-es-korlatossag.html#def-monoton">monotonitás</a> · '
   '<a href="' + E306 + 'tananyag-monotonitas-es-korlatossag.html#def-korlatos">korlátosság</a> · '
   '<a href="' + E306 + 'tananyag-mertani-sorozat.html#tetel-mertani-sn">a mértani sorozat összege</a>.</p>',
 ]),

 ("Amikor a tagok egy számhoz közelítenek", [
   r'<p class="lead">Vizsgáljuk meg az $a_n=\dfrac{2n+1}{n}$ sorozatot. Kiszámolunk néhány tagot, '
   r'egyre nagyobb sorszámokra:</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>$n$</th><td>1</td><td>2</td><td>5</td><td>10</td><td>100</td><td>1000</td></tr>'
   r'<tr><th>$a_n$</th><td>$3$</td><td>$2{,}5$</td><td>$2{,}2$</td><td>$2{,}1$</td><td>$2{,}01$</td>'
   r'<td>$2{,}001$</td></tr></table></div>'
   r'<p>A tagok egyre közelebb kerülnek a $2$-höz. Ez nem véletlen: $a_n=\dfrac{2n+1}{n}=2+\dfrac1n$, és '
   r'az $\dfrac1n$ tag egyre kisebb. A $2$-t viszont <b>egyik tag sem éri el</b> — mindegyik nagyobb '
   r'nála.</p>',
   abra(SVG_SAV, 'Az $a_n=\\frac{2n+1}{n}$ sorozat első tizenkét tagja. A zöld sáv a $2\\pm0{,}3$ '
        'sáv: a <b>negyedik tagtól kezdve</b> minden pont benne van.'),
   doboz("pelda", "I.V.H. Akták — határérték táblázatból",
         r'<p>Sejtsük meg az $a_n=\dfrac{3n-1}{n+1}$ sorozat határértékét!</p>'
         r'<div class="tblwrap"><table class="tt-table">'
         r'<tr><th>$n$</th><td>1</td><td>10</td><td>100</td><td>1000</td></tr>'
         r'<tr><th>$a_n$</th><td>$1$</td><td>$\approx2{,}636$</td><td>$\approx2{,}960$</td>'
         r'<td>$\approx2{,}996$</td></tr></table></div>'
         r'<p>A sejtés: a tagok a $3$-hoz tartanak. Az ellenőrzés sem nehéz: '
         r'$3-a_n=\dfrac{3(n+1)-(3n-1)}{n+1}=\dfrac{4}{n+1}$, és ez a különbség tetszőlegesen kicsi lesz, ha $n$ elég nagy.</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a táblázat csak <b>sejtést</b> ad — a pontos értéket a '
         r'következő lecke módszere, a kiemelés adja.”</p>', hid="pelda-tablazat"),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Az ókori görög Zénón azt állította, hogy Akhilleusz sosem éri utol a teknőst: mire odaér, '
         r'ahol a teknős volt, az már odébb jár, és így tovább, végtelen sokszor. A paradoxon feloldása '
         r'épp a határérték: végtelen sok, egyre rövidebb idő összege lehet <b>véges</b>. Az ilyen összegeket a '
         r'témakör utolsó leckéjében (A végtelen mértani sor) ki is számoljuk.</p>'),
 ]),

 ("A határérték — kimondva", [
   r'<p class="lead">A „közelít” szót most pontossá tesszük. A kép a sáv: rajzoljunk az $A$ szám köré '
   r'akármilyen keskeny sávot — ha a sorozat tagjai <b>egy bizonyos tagtól kezdve mind</b> a sávba '
   r'esnek, akkor $A$ a határérték.</p>',
   doboz("definicio", "A sorozat határértéke",
         r'<p>Az $(a_n)$ sorozat <b>határértéke</b> az $A$ szám, ha az $A$ bármilyen kicsi '
         r'környezetébe (sávjába) a sorozatnak <b>egy tagjától kezdve minden tagja</b> beleesik. '
         r'Jelölése:</p>$$\lim_{n\to\infty}a_n=A .$$'
         r'<p>Ilyenkor azt mondjuk, hogy a sorozat <b>konvergens</b>, és $A$-hoz <b>tart</b>.</p>',
         hid="def-hatarertek"),
   r'<p>Az előző sorozatnál a $2\pm0{,}3$ sávba a negyedik tagtól esik minden tag, a $2\pm0{,}1$ sávba a '
   r'tizenegyediktől ($\frac1n\lt0{,}1$ akkor, ha $n\gt10$; a tizedik tag, $2{,}1$, éppen a sáv szélén '
   r'van, a szélét nem számítjuk bele). Minél keskenyebb a sáv, annál később '
   r'„lép be” a sorozat — de mindig belép. A tanterv ennél a pontnál megáll: a definíció szerinti '
   r'bizonyítást nem gyakoroljuk, a sáv-kép a lényeg.</p>',
   doboz("definicio", "Konvergens és divergens sorozat",
         r'<p>Ha a sorozatnak van (véges) határértéke, <b>konvergens</b>; ha nincs, <b>divergens</b>. '
         r'A divergens sorozatok két csoportja:</p>'
         r'<ul><li>a tagok minden határon túl nőnek (csökkennek): ilyenkor azt írjuk, hogy '
         r'$\lim a_n=+\infty$ (illetve $-\infty$), és azt mondjuk, hogy a sorozat a végtelenbe tart — '
         r'például $a_n=n^2$, illetve $a_n=-3n$. Ez is divergencia, mert a $+\infty$ nem szám;</li>'
         r'<li>a tagok sem egy számhoz, sem a végtelenbe nem tartanak — például az $a_n=(-1)^n$ sorozat '
         r'tagjai felváltva $-1$ és $1$ (az ilyen sorozatot <b>oszcillálónak</b> nevezzük).</li></ul>',
         hid="def-konvergens"),
   abra(SVG_DIVERGENS, 'Az $a_n=(-1)^n$ sorozat tagjai két érték között ugrálnak: nincs olyan szám, '
        'amelynek a keskeny sávjába egy tagtól kezdve mind beleesnének.'),
   kviz(r'Mi igaz az $a_n=\frac1n$ sorozatra?',
        [r'a határértéke $0$, pedig egyik tagja sem $0$',
         r'a határértéke $0$, mert elég nagy $n$-re a tag pontosan $0$ lesz',
         r'a határértéke $1$, mert az első tagja $1$',
         r'nincs határértéke, mert a tagok soha nem érik el a $0$-t'], 0,
        jo="✔ A határértéknek nem kell tagnak lennie: elég, ha a tagok egy idő után bármilyen "
           "kicsi sávba beleesnek körülötte.",
        nem="✘ A határértéknek nem kell a sorozat tagjának lennie, és a tagoknak nem kell elérniük. Az 1/n "
            "tagjai (1; 0,5; 0,33; 0,25; …; a 100. tag 0,01) egyre közelebb kerülnek a 0-hoz — ennyi a feltétel."),
 ]),

 ("Nevezetes határértékek", [
   r'<p class="lead">Néhány határértéket minden számolásnál felhasználunk. Ezeket nem kell minden '
   r'alkalommal újra megsejteni — a táblázatból vagy a sáv-képből azonnal látszanak.</p>',
   doboz("tetel", "Nevezetes határértékek",
         r'<ul><li>állandó sorozat: $\lim\limits_{n\to\infty}c=c$;</li>'
         r'<li>$\lim\limits_{n\to\infty}\dfrac1n=0$, és általában $\lim\limits_{n\to\infty}\dfrac{c}{n^k}=0$ '
         r'bármely $c$ számra és $k\gt0$ kitevőre;</li>'
         r'<li>$\lim\limits_{n\to\infty}n^k=+\infty$, ha $k\gt0$;</li>'
         r'<li>a $q^n$ sorozat: ha $\lvert q\rvert\lt1$, akkor $\lim q^n=0$; ha $q=1$, akkor $\lim q^n=1$; '
         r'ha $q\gt1$, akkor $\lim q^n=+\infty$; ha $q\le-1$, a sorozat divergens (oszcillál).</li></ul>',
         hid="tetel-nevezetes"),
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>$q$</th><th>$q^1$</th><th>$q^2$</th><th>$q^3$</th><th>$q^4$</th><th>határérték</th></tr>'
   r'<tr><td>$\frac12$</td><td>$\frac12$</td><td>$\frac14$</td><td>$\frac18$</td><td>$\frac1{16}$</td><td>$0$</td></tr>'
   r'<tr><td>$-\frac12$</td><td>$-\frac12$</td><td>$\frac14$</td><td>$-\frac18$</td><td>$\frac1{16}$</td><td>$0$</td></tr>'
   r'<tr><td>$2$</td><td>$2$</td><td>$4$</td><td>$8$</td><td>$16$</td><td>$+\infty$</td></tr>'
   r'<tr><td>$-2$</td><td>$-2$</td><td>$4$</td><td>$-8$</td><td>$16$</td><td>nincs</td></tr>'
   r'</table></div>'
   r'<p>A $-\frac12$ sora a tanulságos: a tagok előjele váltakozik, a <b>távolságuk a $0$-tól</b> '
   r'viszont feleződik — ezért a sorozat mégis a $0$-hoz tart.</p>',
   kviz(r'Mihez tart az $a_n=\left(-\frac12\right)^n$ sorozat?',
        [r'a $0$-hoz',
         r'sehova, mert az előjele váltakozik',
         r'a $-\frac12$-hez',
         r'$-\infty$-hez, mert negatív alapot hatványozunk'], 0,
        jo="✔ |q| = 1/2 < 1, ezért qⁿ → 0. Az előjel váltakozik, de a tagok távolsága a 0-tól "
           "feleződik.",
        nem="✘ A váltakozó előjel még nem divergencia: a tagok (−0,5; 0,25; −0,125; …) mind "
            "közelebb kerülnek a 0-hoz. |q| < 1 esetén qⁿ → 0."),
 ]),

 ("Műveletek és határozatlan alakok", [
   r'<p class="lead">Konvergens sorozatokkal úgy számolhatunk, ahogy a számokkal szokás. A tételt '
   r'bizonyítás nélkül mondjuk ki.</p>',
   doboz("tetel", "Műveletek konvergens sorozatokkal",
         r'<p>Ha $\lim a_n=A$ és $\lim b_n=B$, akkor</p>'
         r'$$\lim(a_n\pm b_n)=A\pm B,\qquad \lim(a_n\cdot b_n)=A\cdot B,\qquad '
         r'\lim(c\cdot a_n)=c\cdot A,$$'
         r'$$\lim\frac{a_n}{b_n}=\frac AB\quad(\text{ha }B\ne0\text{ és }b_n\ne0).$$'
         r'<p>A továbbiakban röviden $\lim a_n$-t írunk; ez mindig $n\to\infty$ esetén értendő.</p>',
         hid="tetel-muveletek"),
   doboz("pelda", "I.V.H. Akták — a szabályok munkában",
         r'<p>$\lim\left(3+\dfrac2n\right)=3+0=3$; '
         r'$\ \lim\left(5-\dfrac1{n^2}\right)\left(2+\dfrac1n\right)=5\cdot2=10$; '
         r'$\ \lim\dfrac{4-\frac1n}{2+\frac3n}=\dfrac42=2$.</p>', hid="pelda-muveletek"),
   r'<p>Ha valamelyik sorozat a végtelenbe tart, néhány eset még egyértelmű: $\dfrac{c}{\pm\infty}$ '
   r'alakú hányados a $0$-hoz tart, $(+\infty)+(+\infty)$ is $+\infty$, és $c\cdot(+\infty)$ is '
   r'végtelen, ha $c\ne0$ (az előjel a $c$-é). Más esetekben viszont a „végeredmény” a konkrét sorozaton '
   r'múlik. Ezeket <b>határozatlan alakoknak</b> nevezzük:</p>'
   r'$$\frac{\infty}{\infty},\qquad \infty-\infty,\qquad 0\cdot\infty,\qquad \frac00,\qquad 1^{\infty}.$$'
   r'<p>Például $\dfrac nn\to1$, $\dfrac{n^2}{n}\to+\infty$ és $\dfrac{n}{n^2}\to0$ — mindhárom '
   r'„$\frac\infty\infty$” alakú, mégis más a határértékük. A határozatlan alakokat a következő leckék '
   r'módszerei oldják fel.</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „$\frac\infty\infty=1$, mert ami egyforma, az kiejti egymást”, és '
         r'„$\infty-\infty=0$”.</p>'
         r'<p>A $\infty$ nem szám, hanem annak a rövidítése, hogy valami <b>minden határon túl nő</b> — '
         r'és nem mindegy, milyen gyorsan. Az $(n+5)-n$ sorozat „$\infty-\infty$” alakú, mégis $5$ a '
         r'határértéke; az $n^2-n$ szintén, és ez $+\infty$-hez tart.</p>'),
   kviz(r'Mennyi a $\lim\limits_{n\to\infty}\bigl((n+3)-n\bigr)$ határérték?',
        [r'$3$', r'$0$, mert $\infty-\infty=0$', r'$+\infty$', r'nincs határértéke'], 0,
        jo="✔ (n + 3) − n = 3 minden n-re, tehát a határérték 3. A „∞ − ∞” alak határozatlan.",
        nem="✘ Mielőtt határértéket veszünk, egyszerűsítsünk: (n + 3) − n = 3. A ∞ − ∞ nem "
            "„nulla”, hanem határozatlan alak."),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Véd Vilmos:</b> Táblázatozni lassú, és a számológépem is lemerült. '
         '<b>Nagol:</b> Akkor jöjjön a módszer. Ha a tag egy tört, a számláló és a nevező '
         '„versenyét” egyetlen lépéssel eldönthetjük — ez a kiemelés.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> A számláló is nő, a nevező is nő. Ki nyer? Én a számlálóra fogadok, '
         'mert szimpatikusabb. <b>Nagol:</b> Ne fogadj, hanem emeld ki a legnagyobb hatványt. Az '
         'eredményt a <b>fokszámok</b> döntik el — és ezt egyetlen sorban meg lehet mutatni.'),
 ]),

 ("Kiemelés lépésről lépésre", [
   r'<p class="lead">A $\frac{\infty}{\infty}$ alakú törtnél a számlálóból a számláló, a nevezőből a '
   r'nevező legmagasabb $n$-hatványát emeljük ki. A zárójelekben a főegyütthatón kívül csak '
   r'$\frac{c}{n^k}$ alakú tagok maradnak, ezek $0$-hoz tartanak; az $n$-hatványok egyszerűsítése után '
   r'látszik, marad-e $n$ a számlálóban vagy a nevezőben.</p>',
   doboz("pelda", "I.V.H. Akták — kiemelés",
         r'<p>Számítsuk ki a $\lim\limits_{n\to\infty}\dfrac{6n^2-5n+1}{3n^2+4}$ határértéket!</p>'
         r'<p>A legmagasabb hatvány $n^2$; ezt emeljük ki számlálóból és nevezőből:</p>'
         r'$$\frac{6n^2-5n+1}{3n^2+4}=\frac{n^2\left(6-\frac5n+\frac1{n^2}\right)}'
         r'{n^2\left(3+\frac4{n^2}\right)}=\frac{6-\frac5n+\frac1{n^2}}{3+\frac4{n^2}}'
         r'\ \longrightarrow\ \frac{6-0+0}{3+0}=2 .$$'
         r'<p>Ellenőrzés táblázattal: $n=10$-re $\approx1{,}813$, $n=100$-ra $\approx1{,}983$, '
         r'$n=1000$-re $\approx1{,}998$ — a tagok valóban a $2$-höz közelítenek.</p>',
         hid="pelda-kiemeles"),
   doboz("erdekesseg", "Miért éppen a legnagyobb hatvány?",
         r'<p>$n=1000$-nél a számláló $6n^2=6\,000\,000$ tagja mellett az $5n=5000$ csak '
         r'$0{,}08\%$-ot jelent. Nagy $n$-re a legmagasabb fokú tag „mindent visz”, a többi elhanyagolható '
         r'— a kiemelés ezt teszi pontossá.</p>'),
 ]),

 ("Három eset — egy szabály", [
   r'<p class="lead">A kiemelés után mindig ugyanaz derül ki: csak a két <b>főtag</b> (a legmagasabb '
   r'fokú tag az együtthatójával) számít.</p>',
   doboz("tetel", "A fokszám-szabály",
         r'<p>Legyen a számláló $p$-edfokú, $a$ főegyütthatóval, a nevező $r$-edfokú, $b$ '
         r'főegyütthatóval. Ekkor $n\to\infty$ esetén a tört határértéke</p>'
         r'<ul><li>$\dfrac ab$, ha $p=r$ (azonos fokszám);</li>'
         r'<li>$0$, ha $p\lt r$ (a nevező „győz”);</li>'
         r'<li>$+\infty$ vagy $-\infty$, ha $p\gt r$ — az előjelet az $\dfrac ab$ előjele adja.</li></ul>',
         hid="tetel-fokszam"),
   doboz("pelda", "I.V.H. Akták — a másik két eset",
         r'<p><b>a)</b> $\lim\dfrac{4n+7}{2n^2-3}$: a számláló elsőfokú, a nevező másodfokú. '
         r'Kiemelve $\dfrac{n\left(4+\frac7n\right)}{n^2\left(2-\frac3{n^2}\right)}='
         r'\dfrac1n\cdot\dfrac{4+\frac7n}{2-\frac3{n^2}}\to0\cdot2=0$.</p>'
         r'<p><b>b)</b> $\lim\dfrac{n^2-4n}{5-2n}$: a számláló magasabb fokú, tehát a határérték '
         r'végtelen — de melyik? Kiemelve $\dfrac{n^2\left(1-\frac4n\right)}{n\left(\frac5n-2\right)}'
         r'=n\cdot\dfrac{1-\frac4n}{\frac5n-2}$, ahol a második tényező $-\frac12$-hez tart, az $n$ pedig '
         r'$+\infty$-hez. A határérték $-\infty$.</p>', hid="pelda-harom-eset"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos minden törtnél a főegyütthatók hányadosát írja: a b) példára „$\frac{1}{-2}$”-t.</p>'
         r'<p>Ez <b>csak azonos fokszámnál</b> igaz. Előbb mindig a fokszámokat hasonlítjuk össze, és '
         r'ha a számláló a magasabb fokú, a végtelen <b>előjelére</b> is figyelünk: itt a számláló '
         r'főtagja pozitív ($n^2$), a nevezőé negatív ($-2n$), ezért $-\infty$ az eredmény.</p>'),
   kviz(r'Mennyi a $\lim\limits_{n\to\infty}\dfrac{3n^2+1}{6n^3-n}$ határérték?',
        [r'$0$', r'$\frac12$', r'$2$', r'$+\infty$'], 0,
        jo="✔ A nevező harmadfokú, a számláló csak másodfokú: a nevező „győz”, a határérték 0.",
        nem="✘ A 3/6 = 1/2 csak azonos fokszámnál lenne jó. Itt a nevező magasabb fokú, "
            "ezért a tört a 0-hoz tart."),
 ]),

 ("Szorzat és hatvány a törtben", [
   r'<p class="lead">Ha a számlálóban vagy a nevezőben szorzat vagy hatvány áll, nem kell mindent '
   r'kibontani: elég a <b>főtagokat</b> összeszorozni.</p>',
   doboz("pelda", "I.V.H. Akták — főtagok szorzata",
         r'<p><b>a)</b> $\lim\dfrac{(3n-1)^2}{(n+2)(2n+5)}$: a számláló főtagja $(3n)^2=9n^2$, a nevezőé '
         r'$n\cdot2n=2n^2$. Azonos fokszám, tehát a határérték $\dfrac92$.</p>'
         r'<p><b>b)</b> $\lim\dfrac{(1-2n)^3}{4n^3+1}$: a számláló főtagja $(-2n)^3=-8n^3$, így a '
         r'határérték $\dfrac{-8}{4}=-2$.</p>', hid="pelda-szorzat"),
 ]),

 ("Két tört különbsége: $\\infty-\\infty$", [
   r'<p class="lead">Ha két, külön-külön a végtelenbe tartó tört különbsége a kérdés, a „$\infty-\infty$” '
   r'alak határozatlan. A megoldás: <b>közös nevezőre hozunk</b>, és az így kapott egyetlen törtre '
   r'alkalmazzuk a fokszám-szabályt. Ez a témakör legnehezebb számolása.</p>',
   doboz("pelda", "I.V.H. Akták — közös nevezővel",
         r'<p>Számítsuk ki: $\lim\limits_{n\to\infty}\left(\dfrac{3n^2+1}{n+2}-\dfrac{3n^2-n}{n+1}\right)$.</p>'
         r'<p>Mindkét tört $+\infty$-hez tart, tehát közös nevezőre hozunk:</p>'
         r'$$\frac{(3n^2+1)(n+1)-(3n^2-n)(n+2)}{(n+2)(n+1)} .$$'
         r'<p>A számlálóban a harmadfokú tagok kiesnek: $(3n^3+3n^2+n+1)-(3n^3+5n^2-2n)=-2n^2+3n+1$. '
         r'A nevező $n^2+3n+2$. Így</p>'
         r'$$\lim\frac{-2n^2+3n+1}{n^2+3n+2}=\frac{-2}{1}=-2 .$$', hid="pelda-kulonbseg"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„Mindkét tört a végtelenbe tart, a különbségük tehát $\infty-\infty=0$” — írja Véd Vilmos.</p>'
         r'<p>A két tört nagyjából ugyanolyan gyorsan nő (mindkettő körülbelül $3n$), de nem pontosan '
         r'egyformán: a különbségük itt $-2$-höz tart. '
         r'Határozatlan alaknál <b>soha nem</b> vesszük külön a két tag határértékét — előbb átalakítunk.</p>'),
   kviz(r'Mennyi a $\lim\limits_{n\to\infty}\left(\dfrac{n^2}{n+1}-n\right)$ határérték?',
        [r'$-1$', r'$0$', r'$1$', r'$+\infty$'], 0,
        jo="✔ Közös nevezővel: (n² − n² − n)/(n + 1) = −n/(n + 1) → −1.",
        nem="✘ A ∞ − ∞ határozatlan alak. Közös nevezőre hozva a különbség −n/(n + 1), "
            "és ez a −1-hez tart."),
   NEHEZ(1, 3, "a $\\infty-\\infty$ alakú különbségek"),
   GY(FGY + "#alap-7", "A 7–14", FGY + "#kozep-4", "K 4–6"),
   brief('<b>Véd Vilmos:</b> Kiemelni már tudok. De mi van, ha a nevezőben egy gyökjel ül, és '
         'onnan néz rám? <b>Nagol:</b> Akkor a gyökjel alól is kiemelünk — ugyanaz a verseny, '
         'csak álcában.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> A gyökjel nem fal, csak álca. Alatta ugyanaz a fokszám-verseny zajlik, '
         'mint eddig. <b>Véd Vilmos:</b> Tehát ha bebújok a gyökjel alá, nem találsz meg? '
         '<b>Nagol:</b> De. Egyszerűen a főegyütthatódból is gyököt vonok.'),
 ]),

 ("$\\sqrt{n^2}=n$ — és ami alatta van", [
   r'<p class="lead">A sorozatoknál $n$ mindig pozitív, ezért $\sqrt{n^2}=n$. Ezzel a gyökjel alól is '
   r'kiemelhetjük $n^2$-et, és a gyök elé $n$ kerül.</p>',
   doboz("tetel", "Kiemelés a gyökjel alól",
         r'<p>Ha $n\gt0$ és $a\gt0$, akkor</p>'
         r'$$\sqrt{an^2+bn+c}=\sqrt{n^2\left(a+\frac bn+\frac c{n^2}\right)}'
         r'=n\sqrt{a+\frac bn+\frac c{n^2}} ,$$'
         r'<p>és a gyökjel alatti kifejezés $a$-hoz tart, így a jobb oldali $\sqrt{a+\frac bn+\frac c{n^2}}$ '
         r'tényező $\sqrt a$-hoz.</p>',
         hid="tetel-gyok-kiemeles"),
   doboz("pelda", "I.V.H. Akták — gyök a számlálóban",
         r'<p>Számítsuk ki: $\lim\limits_{n\to\infty}\dfrac{\sqrt{16n^2+5n-2}}{3n+1}$.</p>'
         r'$$\frac{n\sqrt{16+\frac5n-\frac2{n^2}}}{n\left(3+\frac1n\right)}'
         r'=\frac{\sqrt{16+\frac5n-\frac2{n^2}}}{3+\frac1n}\ \longrightarrow\ \frac{\sqrt{16}}{3}=\frac43 .$$',
         hid="pelda-gyokos"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint a fenti határérték $\frac{16}{3}$, „mert a főegyütthatók hányadosa”.</p>'
         r'<p>A $16$ a gyökjel <b>alatt</b> van: a főtag nem $16n$, hanem $\sqrt{16n^2}=4n$. A gyök '
         r'alatti együtthatóból is gyököt kell vonni — ezért lesz az eredmény $\frac43$.</p>'),
   kviz(r'Mennyi a $\lim\limits_{n\to\infty}\dfrac{\sqrt{4n^2+1}}{3n}$ határérték?',
        [r'$\frac23$', r'$\frac43$', r'$\frac{2}{9}$', r'$+\infty$'], 0,
        jo="✔ √(4n² + 1) főtagja √(4n²) = 2n, így az eredmény 2n/3n → 2/3.",
        nem="✘ A 4 a gyökjel alatt van: a főtag √(4n²) = 2n, nem 4n. Az eredmény 2/3."),
 ]),

 ("A gyök „fokszáma”", [
   r'<p class="lead">A $\sqrt{an^2+\dots}$ kifejezés úgy viselkedik, mint egy <b>elsőfokú</b> tag '
   r'($\sqrt a\cdot n$). Ezzel a fokszám-szabály három esete gyökös törtekre is működik.</p>',
   doboz("pelda", "I.V.H. Akták — a három eset gyökkel",
         r'<p><b>a)</b> $\lim\dfrac{\sqrt{n^2+1}}{n^2}=0$: a számláló „elsőfokú”, a nevező másodfokú.</p>'
         r'<p><b>b)</b> $\lim\dfrac{n^2}{\sqrt{4n^2+3}}=+\infty$: most a számláló a magasabb fokú.</p>'
         r'<p><b>c)</b> $\lim\dfrac{\sqrt{9n^2+2}}{2-5n}$: azonos fokszám, a főtagok $3n$ és $-5n$, a '
         r'határérték tehát $-\dfrac35$. Az előjelre itt is figyelni kell: a nevező főtagja negatív.</p>',
         hid="pelda-gyokos-negativ"),
   doboz("pelda", "I.V.H. Akták — gyök és polinom együtt",
         r'<p>$\lim\dfrac{2n+\sqrt{n^2+1}}{3n}$: a számlálóban a két elsőfokú tag összeadódik, '
         r'$2n+n=3n$ a főtag, így a határérték $\dfrac{3}{3}=1$.</p>'
         r'<p><i>Vigyázat:</i> ha a főtagok kiejtik egymást (például $\sqrt{n^2+1}-n$), az $\infty-\infty$ '
         r'alak, és ez a rövidítés nem használható.</p>', hid="pelda-gyok-polinom"),
   r'<p>Emlékeztető: a három eset pontos megfogalmazása a <a href="tananyag-racionalis-tortek.html#tetel-fokszam">'
   r'fokszám-szabálynál</a> van.</p>',
   GY(FGY + "#alap-15", "A 15–16", FGY + "#kozep-7", "K 7–11"),
   brief('<b>Véd Vilmos:</b> Kiemeléssel mindent megoldok! <b>Nagol:</b> Majdnem. Van egy '
         'határozatlan alak, amelyen semmilyen kiemelés nem segít: az $1^\\infty$. Az alap $1$-hez tart, a '
         'kitevő a végtelenbe — és a legegyszerűbb esetben egy új, nevezetes szám jön ki.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-hatarertek-fogalma.html",
     cim="A sorozat határértéke",
     cim_tiszta="A sorozat határértéke",
     alcim="Mihez közelít egy sorozat: közelítés, sáv-kép, konvergens és divergens sorozat, "
           "nevezetes határértékek, műveletek és a határozatlan alakok.",
     chip=KUL + " · 1/5", szakaszok=A,
     elozo=("index.html", "Sorozatok határértéke — témakör"),
     kovetkezo=("tananyag-racionalis-tortek.html", "Kiemelés — törtek határértéke")),
 lap(**T, fajl="tananyag-racionalis-tortek.html",
     cim="Kiemelés — törtek határértéke",
     alcim="Racionális törtek határértéke kiemeléssel, a fokszám-szabály három esete, szorzatok a "
           "törtben, és a $\\infty-\\infty$ alakú különbség közös nevezővel.",
     chip=KUL + " · 2/5", szakaszok=B1,
     elozo=("tananyag-hatarertek-fogalma.html", "A sorozat határértéke"),
     kovetkezo=("tananyag-gyokos-kifejezesek.html", "Gyökös kifejezések határértéke")),
 lap(**T, fajl="tananyag-gyokos-kifejezesek.html",
     cim="Gyökös kifejezések határértéke",
     alcim="Kiemelés a gyökjel alól, és a fokszám-szabály gyökös törtekre.",
     chip=KUL + " · 3/5", szakaszok=B2,
     elozo=("tananyag-racionalis-tortek.html", "Kiemelés — törtek határértéke"),
     kovetkezo=("tananyag-az-e-szam.html", "Az e szám")),
]
for u in KI:
    print("✓", os.path.basename(u))
