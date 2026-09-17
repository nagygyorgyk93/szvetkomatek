# -*- coding: utf-8 -*-
"""3e/05 — F4 osszefoglalo (Koordinata-terkep). A kesobbi fazisok (F5p terepkuldetes, F6h ket Veszterem,
F5 temakor-index) ugyanide kerulnek. Mentor: Kanrak (es Ter-eb)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, abra, brief
from abra_common import svg_koordsik, KEK

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
KUL = "A Térkép Hálózata"

# ---------------------------------------------------------------- önteszt (a képletek általános ellenőrzése)
from sympy import symbols, sqrt, expand, simplify, solve, Poly, Matrix, factor
E = []


def chk(n, g, w):
    if simplify(g - w) != 0:
        E.append((n, g, w))


x, y, x1, y1, x2, y2, x3, y3 = symbols("x y x1 y1 x2 y2 x3 y3", real=True)
a, b, p, q, r, k, n, m, s = symbols("a b p q r k n m s", positive=True)
D3 = Matrix([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]).det()
chk("terulet-kifejtes", D3, x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
chk("osztopont", ((n*x1 + m*x2) / (m + n) - x1) / (x2 - (n*x1 + m*x2) / (m + n)), m / n)
# pont-egyenes tavolsag: a talppont tavolsaga
A_, B_, C_, X0, Y0, t = symbols("A B C X0 Y0 t", real=True)
tt = solve(A_*(X0 + A_*t) + B_*(Y0 + B_*t) + C_, t)[0]
chk("tavolsag", (A_*tt)**2 + (B_*tt)**2, (A_*X0 + B_*Y0 + C_)**2 / (A_**2 + B_**2))


def disz(gorbe, par):
    e = expand(gorbe.subs(y, k*x + par))
    c2, c1, c0 = Poly(e, x).all_coeffs()
    return factor(c1**2 - 4*c2*c0)


# erintesi feltetelek = D=0
Dk = disz((x - p)**2 + (y - q)**2 - r**2, n)
assert simplify(Dk + 4*((k*p - q + n)**2 - r**2*(1 + k**2))) == 0, Dk
De = disz(x**2/a**2 + y**2/b**2 - 1, n)
assert all(simplify(u**2 - (a**2*k**2 + b**2)) == 0 for u in solve(De, n))
Dh = disz(x**2/a**2 - y**2/b**2 - 1, n)
assert all(simplify(u**2 - (a**2*k**2 - b**2)) == 0 for u in solve(Dh, n))
Dp = disz(y**2 - 2*p*x, n)
chk("par-felt", solve(Dp, p)[0], 2*k*n)
# erinto sajat pontban: a pont rajta van, es a meredekseg egyezik az implicit derivalttal
for nev, g, er in [("ell", x**2/a**2 + y**2/b**2 - 1, x1*x/a**2 + y1*y/b**2 - 1),
                   ("hip", x**2/a**2 - y**2/b**2 - 1, x1*x/a**2 - y1*y/b**2 - 1),
                   ("par", y**2 - 2*p*x, y1*y - p*(x + x1)),
                   ("kor", (x - p)**2 + (y - q)**2 - r**2, (x1 - p)*(x - p) + (y1 - q)*(y - q) - r**2)]:
    gx, gy = g.diff(x).subs({x: x1, y: y1}), g.diff(y).subs({x: x1, y: y1})
    ex, ey = er.diff(x), er.diff(y)
    chk("erinto-" + nev + "-irany", gx*ey - gy*ex, 0)
    chk("erinto-" + nev + "-rajta", er.subs({x: x1, y: y1}) - g.subs({x: x1, y: y1}), 0)
chk("kor-altalanos", expand((x + s/2)**2 - s**2/4), expand(x**2 + s*x))
assert not E, E
print("sympy önteszt: OK")


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


A1 = "tananyag-pontok-a-sikban.html"
A2 = "tananyag-haromszog-terulete.html"
B1 = "tananyag-egyenes-egyenlete.html"
B2 = "tananyag-ket-egyenes.html"
B3 = "tananyag-pont-es-egyenes-tavolsaga.html"
C1 = "tananyag-kor-egyenlete.html"
C2 = "tananyag-kor-es-egyenes.html"
D1 = "tananyag-ellipszis.html"
D2 = "tananyag-ellipszis-es-egyenes.html"
D3 = "tananyag-hiperbola.html"
D4 = "tananyag-hiperbola-es-egyenes.html"
E1 = "tananyag-parabola.html"
E2 = "tananyag-parabola-es-egyenes.html"

# ==================================================================== F4
OSSZ = [
 ("📇 I. rész — pontok a síkban", [
  r'<p>Az első rész a <b>3. dolgozat</b> anyaga. A pontokat $A(x;y)$ alakban írjuk, a két koordinátát '
  r'pontosvessző választja el.</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Mit</th><th>Képlet</th><th>Megjegyzés</th></tr>'
  r'<tr><td>két pont távolsága (' + h(A1, "tetel-tavolsag") + r')</td>'
  r'<td>$|AB|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$</td><td>a kivonás sorrendje mindegy; az origótól: $\sqrt{x^2+y^2}$</td></tr>'
  r'<tr><td>osztópont, $AC:CB=m:n$ (' + h(A1, "tetel-osztopont") + r')</td>'
  r'<td>$C\left(\dfrac{n\,x_1+m\,x_2}{m+n};\ \dfrac{n\,y_1+m\,y_2}{m+n}\right)$</td><td>keresztbe súlyozunk</td></tr>'
  r'<tr><td>felezőpont</td><td>$F\left(\dfrac{x_1+x_2}{2};\ \dfrac{y_1+y_2}{2}\right)$</td>'
  r'<td>paralelogrammában az átlók felezik egymást: $D=A+C-B$ (koordinátánként)</td></tr>'
  r'<tr><td>súlypont (' + h(A1, "tetel-sulypont") + r')</td>'
  r'<td>$S\left(\dfrac{x_1+x_2+x_3}{3};\ \dfrac{y_1+y_2+y_3}{3}\right)$</td><td>a csúcsok koordinátáinak átlaga</td></tr>'
  r'<tr><td>háromszög területe (' + h(A2, "tetel-terulet") + r')</td>'
  r'<td>$T=\frac12|D|$, $D=x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)$</td>'
  r'<td>a $D$ előjele a körüljárástól függ; sokszög: háromszögekre bontjuk</td></tr>'
  r'<tr><td>egy egyenesen van-e (' + h(A2, "tetel-kollinearitas") + r')</td><td>$D=0$</td>'
  r'<td>a „háromszög” területe $0$</td></tr>'
  r'</table></div>',
 ]),

 ("I. rész — az egyenes", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Alak</th><th>Egyenlet</th><th>Mit olvasunk le</th></tr>'
  r'<tr><td>explicit (' + h(B1, "tetel-explicit") + r')</td><td>$y=kx+n$</td>'
  r'<td>$k=\operatorname{tg}\alpha$ az iránytényező, $(0;n)$ az $y$-tengelymetszet</td></tr>'
  r'<tr><td>általános (' + h(B1, "tetel-altalanos") + r')</td><td>$ax+by+c=0$</td>'
  r'<td>$k=-\frac ab$ (ha $b\ne0$); a függőleges egyenes is ilyen: $x=-\frac ca$</td></tr>'
  r'<tr><td>tengelymetszetes (' + h(B1, "tetel-tengelymetszetes") + r')</td><td>$\dfrac xm+\dfrac yn=1$</td>'
  r'<td>$(m;0)$ és $(0;n)$; nincs ilyen alakja az origón átmenő és a tengellyel párhuzamos egyenesnek</td></tr>'
  r'<tr><td>pontból és iránytényezőből (' + h(B1, "tetel-ket-pont") + r')</td><td>$y-y_1=k(x-x_1)$</td>'
  r'<td>két pontból: előbb $k=\dfrac{y_2-y_1}{x_2-x_1}$; ha $x_1=x_2$, az egyenes $x=x_1$</td></tr>'
  r'</table></div>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Két egyenes, pont és egyenes</th><th>Feltétel, képlet</th></tr>'
  r'<tr><td>kölcsönös helyzet (' + h(B2, "tetel-kolcsonos-helyzet") + r')</td>'
  r'<td>$k_1\ne k_2$: metszők (a közös pont az egyenletrendszer megoldása); $k_1=k_2$: párhuzamosak vagy egybeesnek</td></tr>'
  r'<tr><td>párhuzamos, merőleges (' + h(B2, "tetel-parhuzamos-meroleges") + r')</td>'
  r'<td>$k_1=k_2$, illetve $k_1\cdot k_2=-1$; a vízszintes és a függőleges egyenes is merőleges</td></tr>'
  r'<tr><td>két egyenes szöge (' + h(B2, "tetel-szog") + r')</td>'
  r'<td>$\operatorname{tg}\varphi=\left|\dfrac{k_2-k_1}{1+k_1k_2}\right|$, $0^\circ\lt\varphi\le90^\circ$; ha $1+k_1k_2=0$, akkor $90^\circ$</td></tr>'
  r'<tr><td>pont és egyenes távolsága (' + h(B3, "tetel-tavolsagkeplet") + r')</td>'
  r'<td>$d=\dfrac{|a\,x_0+b\,y_0+c|}{\sqrt{a^2+b^2}}$ — csak <b>általános alakból</b></td></tr>'
  r'<tr><td>két párhuzamos egyenes távolsága</td><td>az egyik egyenes egy pontjának távolsága a másiktól</td></tr>'
  r'<tr><td>háromszög magassága</td><td>$m_c$ = a $C$ csúcs távolsága az $AB$ egyenestől; $T=\dfrac{|AB|\cdot m_c}{2}$</td></tr>'
  r'</table></div>'
  r'<p><b>Szög számológéppel:</b> fok üzemmód (<b>D</b>/<b>DEG</b>), a tört értéke után <code>SHIFT tan Ans =</code> '
  r'(más gépeken <code>2nd tan</code> vagy <code>INV tan</code>); egy tizedesre kerekítünk.</p>',
 ]),

 ("II. rész — a négy görbe egy táblázatban", [
  r'<p>A második rész a <b>4. dolgozat</b> anyaga. Minden görbe középpontja, illetve csúcsa az origóban van, '
  r'a kör kivételével.</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th></th><th>definíció (mértani hely)</th><th>egyenlet</th><th>adatok</th></tr>'
  r'<tr><td>kör (' + h(C1, "tetel-kor-egyenlete") + r')</td><td>a $C$ ponttól $r$ távolságra lévő pontok</td>'
  r'<td>${(x-p)^2+(y-q)^2=r^2}$</td>'
  r'<td>$C(p;q)$, $r$</td></tr>'
  r'<tr><td>ellipszis (' + h(D1, "tetel-ellipszis-egyenlete") + r')</td><td>két ponttól (a fókuszoktól) mért távolságok <b>összege</b> állandó: $2a$</td>'
  r'<td>$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$</td>'
  r'<td>$a\gt b$; $e^2=a^2-b^2$; $F(\pm e;0)$; csúcsok $(\pm a;0)$, $(0;\pm b)$</td></tr>'
  r'<tr><td>hiperbola (' + h(D3, "tetel-hiperbola-egyenlete") + r')</td><td>a fókuszoktól mért távolságok <b>különbségének abszolút értéke</b> állandó: $2a$</td>'
  r'<td>$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$</td>'
  r'<td>$e^2=a^2+b^2$; $F(\pm e;0)$; csúcsok $(\pm a;0)$; aszimptoták ${y=\pm\frac bax}$ (' + h(D3, "tetel-aszimptotak") + r')</td></tr>'
  r'<tr><td>parabola (' + h(E1, "tetel-parabola-egyenlete") + r')</td><td>egy ponttól (fókusz) és egy egyenestől (vezéregyenes) egyenlő távolságra lévő pontok</td>'
  r'<td>$y^2=2px$</td><td>$p\gt0$; $F\left(\frac p2;0\right)$, vezéregyenes ${x=-\frac p2}$</td></tr>'
  r'</table></div>'
  r'<p><b>A kör általános alakja</b> (' + h(C1, "tetel-altalanos-alak") + r'): $x^2+y^2+dx+ey+f=0$, ahol $p=-\frac d2$, '
  r'$q=-\frac e2$, $r^2=p^2+q^2-f$. Kör csak akkor, ha $r^2\gt0$, és $x^2$, $y^2$ együtthatója egyenlő.</p>'
  r'<p><b>A parabola négy alakja</b> ($p\gt0$): $y^2=2px$ jobbra, $y^2=-2px$ balra, $x^2=2py$ felfelé, $x^2=-2py$ '
  r'lefelé nyílik. A fókusz mindig a nyílás irányában, a csúcstól $\frac p2$-re van, a vezéregyenes '
  r'ugyanilyen messze az ellenkező oldalon.</p>',
 ]),

 ("II. rész — egyenes és görbe", [
  r'<p><b>A közös recept</b> (' + h(C2, "tetel-kolcsonos-helyzet-kor") + r'): az egyenes egyenletéből kifejezzük az egyik '
  r'ismeretlent, behelyettesítjük a görbe egyenletébe, és megvizsgáljuk a kapott egyenletet.</p>'
  r'<ul>'
  r'<li><b>Másodfokú</b> egyenlet: $D\gt0$ két közös pont (szelő), $D=0$ egy közös pont (érintő), $D\lt0$ nincs közös pont.</li>'
  r'<li><b>Elsőfokú</b> egyenlet: egy közös pont, de <b>nem érintés</b>. Ez akkor fordul elő, ha az egyenes a hiperbola '
  r'egyik aszimptotájával (' + h(D4, "tetel-kolcsonos-helyzet-hiperbola") + r'), illetve a parabola tengelyével '
  r'(' + h(E2, "tetel-kolcsonos-helyzet-parabola") + r') párhuzamos.</li>'
  r'<li>Körnél gyorsabb: ha a középpont és az egyenes távolsága $d$, akkor $d\lt r$ szelő, $d=r$ érintő, $d\gt r$ nincs közös pont.</li>'
  r'<li>A <b>húr hossza</b> a két metszéspont távolsága.</li>'
  r'</ul>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th></th><th>érintő a görbe $T(x_1;y_1)$ pontjában</th><th>érintési feltétel ($y=kx+n$)</th></tr>'
  r'<tr><td>kör</td><td>$(x_1-p)(x-p)+(y_1-q)(y-q)=r^2$ (' + h(C2, "tetel-erinto-kor") + r')</td>'
  r'<td>$r^2(1+k^2)=(kp-q+n)^2$ (' + h(C2, "tetel-erintesi-feltetel-kor") + r')</td></tr>'
  r'<tr><td>ellipszis</td><td>$\dfrac{x_1x}{a^2}+\dfrac{y_1y}{b^2}=1$ (' + h(D2, "tetel-erinto-ellipszis") + r')</td>'
  r'<td>$a^2k^2+b^2=n^2$ (' + h(D2, "tetel-erintesi-feltetel-ellipszis") + r')</td></tr>'
  r'<tr><td>hiperbola</td><td>$\dfrac{x_1x}{a^2}-\dfrac{y_1y}{b^2}=1$ (' + h(D4, "tetel-erinto-hiperbola") + r')</td>'
  r'<td>$a^2k^2-b^2=n^2$, ha $|k|\gt\frac ba$ (' + h(D4, "tetel-erintesi-feltetel-hiperbola") + r')</td></tr>'
  r'<tr><td>parabola</td><td>$y_1y=p\,(x+x_1)$ (' + h(E2, "tetel-erinto-parabola") + r')</td>'
  r'<td>$p=2kn$, ha $k\ne0$ (' + h(E2, "tetel-erintesi-feltetel-parabola") + r')</td></tr>'
  r'</table></div>'
  r'<p>A saját pontbeli érintő képlete a <b>„fele-fele” mintát</b> követi: $x^2\to x_1x$, $y^2\to y_1y$, $2x\to x+x_1$. '
  r'Előtte mindig ellenőrizd, hogy a pont rajta van a görbén. Az érintési feltétel ugyanazt adja, mint a recept '
  r'$D=0$ esete; a feltétellel dolgozó feladatok a gyűjtemények <b>nehéz</b> sávjában vannak.</p>',
 ]),

 ("Maxi trükkjei — a tipikus hibák", [
  r'<ul>'
  r'<li><b>Elveszett mínuszjel a távolságnál:</b> az $A(-2;5)$ és a $B(6;-1)$ pontnál $x_2-x_1=6-(-2)=8$, nem $6-2$ (' + h(A1, "tetel-tavolsag") + r').</li>'
  r'<li><b>Iránytényező az általános alakból:</b> a $2x-3y+6=0$ egyenesnél nem $2$, hanem $k=\frac23$ — előbb $y$-ra rendezz.</li>'
  r'<li><b>Merőleges iránytényező:</b> nem az ellentett és nem a reciprok, hanem a <b>negatív reciprok</b>: $4\to-\frac14$.</li>'
  r'<li><b>Távolság explicit alakból:</b> az $y=kx+n$ egyenletből nem olvasható ki $a$, $b$, $c$; előbb $kx-y+n=0$.</li>'
  r'<li><b>Terület előjele:</b> a $D$ lehet negatív, a terület nem: $T=\frac12|D|$.</li>'
  r'<li><b>Kör leolvasása:</b> $(x+3)^2+(y-1)^2=16$ középpontja $C(-3;1)$, sugara $4$ — nem $C(3;-1)$ és nem $16$.</li>'
  r'<li><b>Az ellipszis együtthatói nem féltengelyek:</b> $9x^2+16y^2=144$-ből előbb osztunk: $a=4$, $b=3$.</li>'
  r'<li><b>Felcserélt $e$-képlet:</b> ellipszis $e^2=a^2-b^2$, hiperbola $e^2=a^2+b^2$ — a hiperbola fókusza a csúcsokon kívül van.</li>'
  r'<li><b>A parabola fókusza:</b> $y^2=12x$-ben $2p=12$, $p=6$, a fókusz $\left(\frac p2;0\right)=(3;0)$.</li>'
  r'<li><b>Érintő olyan pontban, amely nincs a görbén:</b> a képlet ekkor is ad egy egyenest, de az nem érintő.</li>'
  r'<li><b>„Egy közös pont, tehát érintő”:</b> a körnél és az ellipszisnél igaz, a hiperbolánál és a parabolánál nem mindig.</li>'
  r'</ul>',
 ]),

 ("Mit hol találsz?", [
  '<div class="brief"><p>📚 <b>Tananyag — I. rész:</b> '
  '<a href="' + A1 + '">pontok a síkban</a> · <a href="' + A2 + '">a háromszög területe</a> · '
  '<a href="' + B1 + '">az egyenes egyenlete</a> · <a href="' + B2 + '">két egyenes</a> · '
  '<a href="' + B3 + '">pont és egyenes távolsága</a>.</p>'
  '<p>📚 <b>Tananyag — II. rész:</b> '
  '<a href="' + C1 + '">a kör egyenlete</a> · <a href="' + C2 + '">a kör és az egyenes</a> · '
  '<a href="' + D1 + '">az ellipszis</a> · <a href="' + D2 + '">az ellipszis és az egyenes</a> · '
  '<a href="' + D3 + '">a hiperbola</a> · <a href="' + D4 + '">a hiperbola és az egyenes</a> · '
  '<a href="' + E1 + '">a parabola</a> · <a href="' + E2 + '">a parabola és az egyenes</a>.</p>'
  '<p>🎯 <b>Gyakorlás:</b> '
  '<a href="feladatok-pontok.html">pontok</a> · <a href="feladatok-egyenesek.html">egyenesek</a> · '
  '<a href="feladatok-kor.html">a kör</a> · <a href="feladatok-ellipszis-hiperbola.html">ellipszis és hiperbola</a> · '
  '<a href="feladatok-parabola.html">a parabola</a>.</p>'
  '<p>🕹️ <b>Vészterem:</b> <a href="feladatok-hazi.html">I. rész</a> (a 3. dolgozat előtt) · '
  '<a href="feladatok-hazi-2.html">II. rész</a> (a 4. dolgozat előtt) — majd indulj '
  '<a href="terepkuldetes.html">A Térkép Hálózata</a> küldetésre!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Koordináta-térkép — a témakör egy lapon",
    cim_tiszta="Koordináta-térkép", itt="Koordináta-térkép",
    alcim="A síkbeli analitikus geometria képletei, feltételei és tipikus csapdái egy helyen, a két dolgozat "
          "szerint két részre bontva — ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=OSSZ,
    elozo=("feladatok-parabola.html", "A parabola — feladatok"),
    kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p
from sympy import Rational as Q, atan, pi, N as NN
EE = []


def ck(nev, g, w, tur=None):
    ok = abs(float(NN(g)) - float(w)) <= tur if tur is not None else simplify(g - w) == 0
    if not ok:
        EE.append((nev, g, w))


X, Y, C0 = symbols("X Y C0", real=True)


def met(g, l):
    sol = solve([g, l], [X, Y], dict=True)
    return sorted([(u[X], u[Y]) for u in sol if u[X].is_real], key=lambda u: (float(u[0]), float(u[1])))


tv = lambda u, v: sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
A_, B_, C_ = (-3, -1), (5, 3), (1, 7)
ck("I1", tv(A_, B_), 4*sqrt(5)); ck("I1b", tv(A_, C_), 4*sqrt(5)); ck("I1c", tv(B_, C_), 4*sqrt(2))
ck("I1k", 4*sqrt(5), 8.94, .005); ck("I1k2", 4*sqrt(2), 5.66, .005)
ck("I2S", (A_[0] + B_[0] + C_[0]) / Q(3), 1); ck("I2S2", (A_[1] + B_[1] + C_[1]) / Q(3), 3)
Dd = (B_[0] - A_[0])*(C_[1] - A_[1]) - (B_[1] - A_[1])*(C_[0] - A_[0]); ck("I2T", abs(Dd) / Q(2), 24)
lBC = X + Y - 8; assert lBC.subs({X: 5, Y: 3}) == 0 and lBC.subs({X: 1, Y: 7}) == 0
lma = X - Y + 2; assert lma.subs({X: -3, Y: -1}) == 0
ck("I3F", met(lBC, lma)[0][0], 3); ck("I3F2", met(lBC, lma)[0][1], 5)
ck("I3F-fel", ((5 + 1) / Q(2), (3 + 7) / Q(2))[0], 3)
ma = abs(-3 - 1 - 8) / sqrt(2)
ck("I4", ma, 6*sqrt(2)); ck("I4T", tv(B_, C_) * ma / 2, 24); ck("I4k", 6*sqrt(2), 8.49, .005)
ck("I5", atan(abs((2 - Q(1, 2)) / (1 + 2*Q(1, 2)))) * 180 / pi, 36.9, .05)
assert (X + Y + 4).subs({X: -3, Y: -1}) == 0
Kk = X**2 + Y**2 - 2*X - 6*Y
ck("II1", expand((X - 1)**2 + (Y - 3)**2 - 10 - Kk), 0)
ck("II2", [(x0 - 1)**2 + (y0 - 3)**2 for x0, y0 in (A_, B_, C_)][0], 32)
assert [(x0 - 1)**2 + (y0 - 3)**2 for x0, y0 in (A_, B_, C_)] == [32, 16, 16]
M2 = met(Kk, lBC)
assert M2 == [(2, 6), (4, 4)], M2
ck("II3", tv(*M2), 2*sqrt(2)); ck("II3d", abs(1 + 3 - 8) / sqrt(2), 2*sqrt(2)); ck("II3k", sqrt(10), 3.16, .005)
assert Kk.subs({X: 4, Y: 2}) == 0 and met(Kk, 3*X - Y - 10) == [(4, 2)]
ck("II4", solve((3*X - 10), X)[0], Q(10, 3))
nn = solve(abs(1 + 3 - C0) / sqrt(2) - sqrt(10), C0)
assert sorted(nn, key=float) == [4 - 2*sqrt(5), 4 + 2*sqrt(5)], nn
assert all(len(met(Kk, Y + X - v)) == 1 for v in nn)
ck("II5k", 4 + 2*sqrt(5), 8.47, .005); ck("II5k2", 4 - 2*sqrt(5), -0.47, .005)
F1, F2, Pp = (5, 0), (-5, 0), (3, 4)
ck("III1", [tv(Pp, F1), tv(Pp, F2)][0], 2*sqrt(5)); ck("III1b", tv(Pp, F2), 4*sqrt(5))
ck("III1c", tv(Pp, F1) + tv(Pp, F2), 6*sqrt(5)); ck("III1k", 6*sqrt(5), 13.42, .005)
Ell = X**2/45 + Y**2/20 - 1
ck("III2", 45 - 25, 20); assert Ell.subs({X: 3, Y: 4}) == 0
ck("III2k", 3*sqrt(5), 6.71, .005); ck("III2k2", 2*sqrt(5), 4.47, .005)
M3 = met(Ell, Y - 2*X + 2)
assert M3 == [(Q(-6, 5), Q(-22, 5)), (3, 4)], M3
ck("III3", tv(*M3), 21*sqrt(5)/5); ck("III3k", 21*sqrt(5)/5, 9.39, .005)
assert met(Ell, X + 3*Y - 15) == [(3, 4)]
assert met(Ell, 4*X + 3*Y - 30) == [(6, 2)] and met(Ell, 4*X + 3*Y + 30) == [(-6, -2)]
ck("III5", 45*Q(16, 9) + 20, 100)
Hip = X**2/5 - Y**2/20 - 1
assert Hip.subs({X: 3, Y: 4}) == 0 and tv(Pp, F2) - tv(Pp, F1) == 2*sqrt(5)
ck("III6", 25 - 5, 20)
assert not EE, EE
print("sympy önteszt (terep): OK")

SVG_DRON = svg_koordsik(
    xr=(-4, 6), yr=(-2, 8), egyseg=28,
    sokszogek=[([(-3, -1), (5, 3), (1, 7)], KEK, {"kitolt": 0.12})],
    pontok=[((-3, -1), "A", {"dx": -14, "dy": 4}), ((5, 3), "B", {"dx": 14, "dy": 4}),
            ((1, 7), "C", {"dx": 14, "dy": 4})],
    leiras="A három drón helye a koordináta-rendszerben: A(−3;−1), B(5;3), C(1;7)")

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Tér-eb a Kristály-kamra hálózatában csak pontos egyenesek és metszéspontok mentén '
         'ugorhat. Három drón jelöli ki a hálózat csomópontjait, egy teleport-kör köti össze őket, a kamra '
         'szélén pedig az anomália-mag körül ellipszis-pályán kering a figyelődrón. Ha mindent pontosan '
         'bemérsz, Tér-eb hazahozza az utolsó adatcsomagot.'),
   r'<p>Három fázis. Minden lépésnél írd le, melyik képletet használod és miért. Számológép használható: a '
   r'szögeket egy, minden más közelítő értéket két tizedesre kerekíts, és jelöld a kerekítést. A választ '
   r'fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű részfeladat a <b>Kristály-protokoll</b>: érintési feltétellel dolgozik, ezért nehezebb.</p>'
   r'<p><b>Amire szükséged lesz:</b> távolság, súlypont és terület koordinátákból, az egyenes egyenletei, '
   r'pont és egyenes távolsága, a kör és az ellipszis egyenlete, az érintő képletei.</p>',
 ]),

 ("I. fázis — A drónháromszög", [
   r'<p>A három drón helye: $A(-3;-1)$, $B(5;3)$ és $C(1;7)$.</p>',
   abra(SVG_DRON, 'A drónok helye a hálózatban.'),
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki a háromszög oldalait! Milyen a háromszög az oldalai szerint?</li>'
   r'<li>Határozd meg a háromszög súlypontját és területét!</li>'
   r'<li>Írd fel a $BC$ oldal egyenesének és az $A$ csúcsból induló magasságvonalnak az egyenletét, és '
   r'határozd meg a magasság talppontját! Mit veszel észre a talpponttal kapcsolatban? Miért van ez így?</li>'
   r'<li>Számítsd ki az $m_a$ magasságot a pont és egyenes távolságának képletével, és ezzel is számold ki a '
   r'háromszög területét!</li>'
   r'<li>Mekkora szöget zár be az $AB$ és az $AC$ egyenes?</li>'
   r'<li>Maxi szerint az $A$-n átmenő, $BC$-vel párhuzamos egyenes egyenlete $x-y+2=0$. Mit rontott el? '
   r'Mi a helyes egyenlet?</li>'
   r'</ol>',
 ]),

 ("II. fázis — A teleport-kör", [
   r'<p>A drónokat a $K\colon x^2+y^2-2x-6y=0$ teleport-kör köti össze.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Határozd meg a kör középpontját és sugarát! A drónháromszög melyik nevezetes pontja a középpont?</li>'
   r'<li>A körön belül, a körön vagy a körön kívül van a három drón?</li>'
   r'<li>Metszi-e a $BC$ útvonal a kört? Határozd meg a metszéspontokat és a húr hosszát, és a középpont '
   r'meg az egyenes távolságával is indokold a választ!</li>'
   r'<li>Tér-eb a kör $T(4;2)$ pontjából az érintő mentén ugrik tovább. Ellenőrizd, hogy $T$ a körön van, írd '
   r'fel az érintőt, és határozd meg, hol metszi az $x$-tengelyt!</li>'
   r'<li>🔴 Írd fel a körnek a $BC$ egyenessel párhuzamos érintőit! Bontsd lépésekre: milyen alakú az '
   r'egyenes, mi a feltétele annak, hogy pontosan egy közös pontja legyen a körrel, és mik az érintők?</li>'
   r'</ol>',
 ]),

 ("III. fázis — Az ellipszis-pálya", [
   r'<p>A figyelődrón pályája ellipszis. A fókuszai az anomália-mag két pólusa, $F_1(5;0)$ és $F_2(-5;0)$, '
   r'és a pálya átmegy a $P(3;4)$ ponton.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Milyen messze van $P$ a két fókusztól? Mekkora a pálya nagytengelye?</li>'
   r'<li>Írd fel a pálya egyenletét, és add meg a csúcspontjait!</li>'
   r'<li>A figyelődrón az $y=2x-2$ egyenes mentén repül be a pályára. Hol metszi az egyenes a pályát? '
   r'Milyen hosszú az útvonal pálya belsejébe eső szakasza?</li>'
   r'<li>Írd fel a pálya érintőjét a $P$ pontban!</li>'
   r'<li>🔴 Írd fel a pályának a $4x+3y=0$ egyenessel párhuzamos érintőit, és határozd meg az érintési '
   r'pontokat!</li>'
   r'<li>Maxi az 1. részben a két távolság <b>különbségével</b> számolt. Milyen görbét kapott volna így '
   r'ugyanazokkal a fókuszokkal és ugyanazzal a $P$ ponttal? Írd fel az egyenletét!</li>'
   r'</ol>',
   brief('<b>Kanrak:</b> Ha megvan a háromszög, a kör és a pálya, Tér-eb minden ugrása célba ér. A '
         'számításaidat a tanárod ellenőrzi — a kulcs nem kerül a hálózatra.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Három fázis: a drónháromszög, a teleport-kör és az ellipszis-pálya. Beadható projektfeladat — "
          "a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Koordináta-térkép"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — két Vészterem
from fgy_common import cards, oldal

H = []


def hk(nev, g, w, tur=None):
    ok = abs(float(NN(g)) - float(w)) <= tur if tur is not None else simplify(g - w) == 0
    if not ok:
        H.append((nev, g, w))


# --- I. rész
hk("h1", tv((-4, 3), (2, -5)), 10); assert ((-4 + 2) / Q(2), (3 - 5) / Q(2)) == (-1, -1)
hk("h2S", ((0 + 6 + 2) / Q(3)), Q(8, 3)); hk("h2S2", (-2 + 1 + 4) / Q(3), 1)
hk("h2T", abs(6*6 - 3*2) / Q(2), 15)
l3 = 2*X + Y - 2; assert l3.subs({X: -1, Y: 4}) == 0 and l3.subs({X: 3, Y: -4}) == 0
assert expand((X / 1 + Y / 2 - 1) * 2 - l3) == 0
assert (5*X - 2*Y + 19).subs({X: -3, Y: 2}) == 0 and (2*X + 5*Y - 4).subs({X: -3, Y: 2}) == 0 and 5*2 + (-2)*5 == 0
hk("h5", abs(4*1 - 3*(-2) + 5) / Q(5), 3)
hk("h6", atan(abs((Q(-1, 2) - 3) / (1 + 3*Q(-1, 2)))) * 180 / pi, 81.9, .05)
lAB = X - 3*Y + 2; assert lAB.subs({X: 1, Y: 1}) == 0 and lAB.subs({X: 7, Y: 3}) == 0
mc = abs(3 - 21 + 2) / sqrt(10)
hk("h7", mc, 16 / sqrt(10)); hk("h7k", mc, 5.06, .005); hk("h7T", abs(6*6 - 2*2) / Q(2), 16)
hk("h7T2", sqrt(40) * mc / 2, 16)
assert met(2*X + Y - 7, X - Y - 2) == [(3, 1)] and (X + Y - 4).subs({X: 3, Y: 1}) == 0 and (X + Y - 4).subs({X: -1, Y: 5}) == 0
hk("h9", solve(-C0 / 4 * 2 + 1, C0)[0], 2); hk("h9b", solve(-C0 / 4 - 2, C0)[0], -8)
tP = solve((X - 1)**2 + (X + 1)**2 - (X - 5)**2 - (X - 1)**2, X)
hk("h10", tP[0], 2); hk("h10T", abs(4*3 - 2*1) / Q(2), 5)
assert sorted(solve(abs(C0 + 2) / 5 - 2, C0)) == [-12, 8]
# --- II. rész
hk("g1", expand((X + 4)**2 + (Y - 1)**2 - 25 - (X**2 + Y**2 + 8*X - 2*Y - 8)), 0)
hk("g2", tv((-1, -2), (5, 6)) / 2, 5)
hk("g3", sqrt(25 - 4), sqrt(21)); hk("g4", sqrt(4 + 25), sqrt(29))
assert met((X - 2)**2 + (Y - 2)**2 - 25, 3*X + 4*Y - 39) == [(5, 6)]
assert (4*X**2 + 25*Y**2 - 100).subs({X: 3, Y: Q(8, 5)}) == 0 and met(4*X**2 + 25*Y**2 - 100, 3*X + 10*Y - 25) == [(3, Q(8, 5))]
assert all((X**2/40 + Y**2/10 - 1).subs({X: a0, Y: b0}) == 0 for a0, b0 in [(6, 1), (2, 3)])
M9 = met(X**2 + Y**2 - 25, X + Y - 1); assert M9 == [(-3, 4), (4, -3)]
hk("g9", tv(*M9), 7*sqrt(2)); hk("g9k", 7*sqrt(2), 9.90, .005)
assert met(X**2 - Y**2 - 9, Y - X + 1) == [(5, 4)]
assert met(Y**2 - 8*X, 2*X - 3*Y + 8) == [(2, 4), (8, 8)]
assert met(Y**2 - 8*X, Y - X - 2) == [(2, 4)] and met(Y**2 - 8*X, X - 2*Y + 8) == [(8, 8)]
nk = sorted(solve((-2 - 2 + C0)**2 - 20 * 5, C0), key=float); assert nk == [-6, 14]
assert all(len(met((X + 1)**2 + (Y - 2)**2 - 20, Y - 2*X - v)) == 1 for v in nk)
assert met(3*X**2 - Y**2 - 27, Y - 2*X - 3) == [(-6, -9)] and met(3*X**2 - Y**2 - 27, Y - 2*X + 3) == [(6, 9)]
assert not H, H
print("sympy önteszt (Vészterem): OK")

H1A = [
 (r"Adott az $A(-4;3)$ és a $B(2;-5)$ pont. Számítsd ki az $AB$ szakasz hosszát, és határozd meg a "
  r"felezőpontját!", None, r"$AB=10$, $F(-1;-1)$"),
 (r"Határozd meg az $A(0;-2)$, $B(6;1)$, $C(2;4)$ csúcsú háromszög súlypontját és területét!", None,
  r"$S\left(\tfrac83;1\right)$, $T=15$"),
 (r"Írd fel a $P(-1;4)$ és a $Q(3;-4)$ ponton átmenő egyenes egyenletét általános és tengelymetszetes "
  r"alakban, és ábrázold a tengelymetszetei segítségével!", None,
  r"$2x+y-2=0$; $\dfrac x1+\dfrac y2=1$; a tengelymetszetek $(1;0)$ és $(0;2)$"),
 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy az $M(-3;2)$ ponton, és",
  [r"párhuzamos az $e\colon 5x-2y+3=0$ egyenessel;", r"merőleges az $e$ egyenesre!"],
  [r"$5x-2y+19=0$", r"$2x+5y-4=0$"], True),
 (r"Számítsd ki az $M(1;-2)$ pont távolságát a $4x-3y+5=0$ egyenestől!", None, r"$d=3$"),
]
H1K = [
 (r"Mekkora szöget zár be az $y=3x-1$ és az $x+2y-4=0$ egyenes? (Számológéppel, egy tizedesre.)", None,
  r"$\operatorname{tg}\varphi=7$, $\varphi\approx81{,}9^\circ$"),
 (r"Az $ABC$ háromszög csúcsai $A(1;1)$, $B(7;3)$ és $C(3;7)$.",
  [r"Írd fel az $AB$ oldal egyenesének egyenletét!", r"Számítsd ki az $m_c$ magasságot!",
   r"Számítsd ki a területet kétféleképpen: determinánssal, illetve az $AB$ oldalból és $m_c$-ből!"],
  [r"$x-3y+2=0$", r"$m_c=\dfrac{16}{\sqrt{10}}\approx5{,}06$", r"$T=16$ mindkét módon"]),
 (r"Írd fel annak az egyenesnek az egyenletét, amely átmegy a $2x+y-7=0$ és az $x-y-2=0$ egyenes "
  r"metszéspontján, valamint a $(-1;5)$ ponton!", None, r"a metszéspont $(3;1)$, az egyenes $x+y-4=0$"),
 (r"Adott az $ax+4y-1=0$ és a $2x-y+3=0$ egyenes. Határozd meg $a$ értékét úgy, hogy a két egyenes",
  [r"merőleges legyen;", r"párhuzamos legyen!"], [r"$a=2$", r"$a=-8$"], True),
]
H1N = [
 (r"Határozd meg az $y=x+1$ egyenesnek azt a $P$ pontját, amely egyenlő távolságra van az $A(1;0)$ és a "
  r"$B(5;2)$ ponttól! Mekkora az $ABP$ háromszög területe?", None, r"$P(2;3)$, $T=5$"),
 (r"Írd fel azoknak az egyeneseknek az egyenletét, amelyek párhuzamosak a $3x+4y-2=0$ egyenessel, és "
  r"$2$ egységnyire vannak tőle!", None, r"$3x+4y+8=0$ és $3x+4y-12=0$"),
]

H2A = [
 (r"Határozd meg az $x^2+y^2+8x-2y-8=0$ kör középpontját és sugarát!", None, r"$C(-4;1)$, $r=5$"),
 (r"Írd fel annak a körnek az egyenletét, amelynek egyik átmérője az $A(-1;-2)$, $B(5;6)$ szakasz!", None,
  r"$(x-2)^2+(y-2)^2=25$"),
 (r"Határozd meg a $4x^2+25y^2=100$ ellipszis féltengelyeit, lineáris excentricitását és fókuszait!", None,
  r"$a=5$, $b=2$, $e=\sqrt{21}\approx4{,}58$, $F\left(\pm\sqrt{21};0\right)$"),
 (r"Határozd meg a $25x^2-4y^2=100$ hiperbola féltengelyeit, fókuszait és aszimptotáit!", None,
  r"$a=2$, $b=5$, $e=\sqrt{29}$, $F\left(\pm\sqrt{29};0\right)$, $y=\pm\tfrac52x$"),
 (r"Határozd meg az $y^2=-6x$ parabola paraméterét, fókuszát és vezéregyenesét! Merre nyílik?", None,
  r"$p=3$, $F\left(-\tfrac32;0\right)$, $x=\tfrac32$; balra"),
 (r"Érinti-e a $3x+4y-39=0$ egyenes a $(x-2)^2+(y-2)^2=25$ kört? Ha igen, hol?", None,
  r"igen, az érintési pont $(5;6)$"),
 (r"Írd fel a $4x^2+25y^2=100$ ellipszis érintőjét a $\left(3;\tfrac85\right)$ pontjában!", None,
  r"$3x+10y-25=0$"),
]
H2K = [
 (r"Írd fel annak az ellipszisnek az egyenletét, amely átmegy a $P(6;1)$ és a $Q(2;3)$ ponton!", None,
  r"$\dfrac{x^2}{40}+\dfrac{y^2}{10}=1$"),
 (r"Milyen hosszú húrt metsz ki az $x^2+y^2=25$ kör az $x+y-1=0$ egyenesből?", None,
  r"a metszéspontok $(4;-3)$ és $(-3;4)$, a húr $7\sqrt2\approx9{,}90$"),
 (r"Hány közös pontja van az $x^2-y^2=9$ hiperbolának és az $y=x-1$ egyenesnek? Érintő-e az egyenes?", None,
  r"egy: $(5;4)$; nem érintő, mert párhuzamos az $y=x$ aszimptotával"),
 (r"Határozd meg az $y^2=8x$ parabola és a $2x-3y+8=0$ egyenes metszéspontjait, majd írd fel a parabola "
  r"érintőit ezekben a pontokban!", None, r"$(2;4)$ és $(8;8)$; az érintők $y=x+2$ és $x-2y+8=0$"),
]
H2N = [
 (r"Írd fel a $(x+1)^2+(y-2)^2=20$ kör azon érintőit, amelyek párhuzamosak az $y=2x$ egyenessel!",
  [r"Milyen alakú az érintő egyenlete?", r"Milyen $n$ esetén érinti az egyenes a kört?", r"Írd fel az érintőket!"],
  [r"$y=2x+n$", r"$n=14$ vagy $n=-6$", r"$y=2x+14$ és $y=2x-6$"]),
 (r"Írd fel a $3x^2-y^2=27$ hiperbola azon érintőit, amelyek párhuzamosak az $y=2x$ egyenessel, és add meg az "
  r"érintési pontokat!", None, r"$y=2x+3$, érintési pont $(-6;-9)$; $y=2x-3$, érintési pont $(6;9)$"),
]


def vesz(fajl, a_, k_, n_, cim, alcim, prev, prevc, nxt, nxtc):
    body = [
     '    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(a_, "alap", "alap"),
     '    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(k_, "kozep", "kozep"),
     '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(n_, "nehez", "nehez"),
    ]
    oldal(**T, fajl=fajl, cim=cim, h1=cim + " — házi feladatok",
          chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
                 '<span class="chip nehez">Nehéz</span>',
          alcim=alcim, sections_html="\n".join(body), prev=prev, prevc=prevc, nxt=nxt, nxtc=nxtc)
    print("✓", fajl, "| Alap", len(a_), "Közép", len(k_), "Nehéz", len(n_))


vesz("feladatok-hazi.html", H1A, H1K, H1N, "Vészterem I.",
     "Rövid, vegyes gyakorlósor az I. részhez (pontok és egyenesek) — házi feladatnak és a 3. dolgozat előtti "
     "bemelegítésnek. Számológép használható: a szögeket egy, minden más közelítő értéket két tizedesre kerekíts. "
     "A végeredmény minden feladatnál lenyitható!",
     "index.html", "Témakör Főhadiszállása", "feladatok-hazi-2.html", "Vészterem II.")
vesz("feladatok-hazi-2.html", H2A, H2K, H2N, "Vészterem II.",
     "Rövid, vegyes gyakorlósor a II. részhez (kör, ellipszis, hiperbola, parabola) — házi feladatnak és a "
     "4. dolgozat előtti bemelegítésnek. Számológép használható: a szögeket egy, minden más közelítő értéket két "
     "tizedesre kerekíts. A végeredmény minden feladatnál lenyitható!",
     "feladatok-hazi.html", "Vészterem I.", "osszefoglalo.html", "Koordináta-térkép")

# ==================================================================== F5 — témakör-index
from tananyag_common import GYOKER
from fgy_common import w


def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = {
 "A1": kartya(A1, "Pontok a síkban", "A koordináta-rendszer, két pont távolsága, osztópont, felezőpont és súlypont"),
 "A2": kartya(A2, "A háromszög területe", "Darabolás, területképlet determinánssal, három pont egy egyenesen"),
 "B1": kartya(B1, "Az egyenes egyenlete", "Iránytényező; explicit, általános és tengelymetszetes alak; ábrázolás"),
 "B2": kartya(B2, "Két egyenes", "Kölcsönös helyzet, párhuzamosság és merőlegesség, két egyenes szöge"),
 "B3": kartya(B3, "Pont és egyenes távolsága", "A távolságképlet, párhuzamos egyenesek távolsága, a háromszög magassága"),
 "C1": kartya(C1, "A kör egyenlete", "Mértani hely, a kör középponti és általános egyenlete"),
 "C2": kartya(C2, "A kör és az egyenes", "Szelő, érintő, elkerülő egyenes; húr; érintő a kör egy pontjában"),
 "D1": kartya(D1, "Az ellipszis", "Mértani hely, egyenlet, féltengelyek és fókuszok, felírás adatokból"),
 "D2": kartya(D2, "Az ellipszis és az egyenes", "Közös pontok, húr, érintő az ellipszis egy pontjában"),
 "D3": kartya(D3, "A hiperbola", "Mértani hely, egyenlet, aszimptoták, felírás adatokból"),
 "D4": kartya(D4, "A hiperbola és az egyenes", "Az aszimptotával párhuzamos egyenes csapdája, érintő a hiperbola egy pontjában"),
 "E1": kartya(E1, "A parabola", "Mértani hely, egyenlet, fókusz és vezéregyenes, kapcsolat a másodfokú függvénnyel"),
 "E2": kartya(E2, "A parabola és az egyenes", "Közös pontok, érintő a parabola egy pontjában — és a négy görbe egy táblázatban"),
 "fp": kartya("feladatok-pontok.html", "🏋️ Pontok — feladatok", "Távolság, felezőpont, súlypont, osztópont, terület"),
 "fe": kartya("feladatok-egyenesek.html", "🏋️ Egyenesek — feladatok", "Az egyenes egyenletei, két egyenes, szög, távolság"),
 "fk": kartya("feladatok-kor.html", "🏋️ A kör — feladatok", "Kör egyenlete, kör és egyenes, húr, érintő"),
 "fh": kartya("feladatok-ellipszis-hiperbola.html", "🏋️ Ellipszis és hiperbola — feladatok",
              "Egyenlet adatokból és pontokból, közös pontok egyenessel, húr, érintő"),
 "fa": kartya("feladatok-parabola.html", "🏋️ A parabola — feladatok", "Paraméter, fókusz, vezéregyenes, közös pontok, érintő"),
 "h1": kartya("feladatok-hazi.html", "🕹️ Vészterem I. — házi feladatok", "Pontok és egyenesek — a 3. dolgozat előtti bemelegítéshez"),
 "h2": kartya("feladatok-hazi-2.html", "🕹️ Vészterem II. — házi feladatok", "Kör, ellipszis, hiperbola, parabola — a 4. dolgozat előttre"),
 "tk": kartya("terepkuldetes.html", "🎯 A Térkép Hálózata",
              "Háromfázisú küldetés — a drónháromszög, a teleport-kör és az ellipszis-pálya"),
 "ossz": kartya("osszefoglalo.html", "📇 Koordináta-térkép",
                "A két rész képletei, feltételei és tipikus csapdái egy helyen — dolgozat előtti átfutáshoz"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(K[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Síkbeli analitikus geometria | 3e | Szvetkó matek</title>
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
  <span class="itt">Síkbeli analitikus geometria</span>
</nav>
<div class="hero">
  <h1>Síkbeli analitikus geometria</h1>
  <p class="alcim">Pontból számpár, egyenesből és görbéből egyenlet: távolság és terület koordinátákból, az egyenes,
  a kör, az ellipszis, a hiperbola és a parabola — és mindezek közös pontjai.</p>
  <div class="meta-sor"><span class="chip ora">29 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🗺️ <b>Szektor 05 — A Térkép Hálózata.</b> Kiképző: <b>Kanrak</b> — mellette
  <b>Tér-eb</b>, a teleportáló kutya, aki csak pontos egyenesek és metszéspontok mentén ugorhat. Feltörtük
  Maxi navigációs hálózatát, de térkép helyett számpárokat és egyenleteket találtunk. Aki olvasni tudja
  őket, az bemérheti Maxi drónjait, kapuit és pályáit.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag — I. rész (3. dolgozat)</h2>

    <h3>📍 Pontok — Kanrak</h3>
''' + racs("A1", "A2") + '''
    <h3>📏 Egyenesek — Kanrak</h3>
''' + racs("B1", "B2", "B3") + '''
    <h2>Tananyag — II. rész (4. dolgozat)</h2>

    <h3>⭕ A kör — Kanrak</h3>
''' + racs("C1", "C2") + '''
    <h3>🪐 Ellipszis és hiperbola — Kanrak</h3>
''' + racs("D1", "D2", "D3", "D4") + '''
    <h3>🛰️ A parabola — Kanrak</h3>
''' + racs("E1", "E2") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("fp", "fe", "fk", "fh", "fa", "h1", "h2") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> a tizenhárom tananyag-egység sorban; minden altéma
    végén a hozzá tartozó feladatgyűjtemény. A Vészterem I. a 3., a Vészterem II. a 4. dolgozat előtt jön.
    A témakör végén a Koordináta-térkép, majd A Térkép Hálózata küldetés.</p>
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
