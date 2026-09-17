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
