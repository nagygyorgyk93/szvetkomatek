# -*- coding: utf-8 -*-
"""3e/03 — A altema: ket egyenlet ket ismeretlennel (A1), a Gauss-eljaras (A2),
a megoldasok szama (A3). Mentor: Kanrak. Kuldetes: A Rendszer Hibaja."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek
from abra_common import svg_harom_sik

T = dict(tagozat="3e", mappa="03-linearis-rendszerek", temakor="Lineáris egyenletrendszerek")
FGY = "feladatok-rendszerek.html"
KUL = "A Rendszer Hibája"
EGY1E = "../../1e/07-linearis-egyenletek-es-rendszerek/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import symbols, Eq, solve, linsolve, simplify, N
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x, y, z, t = symbols("x y z t")

# A1 — a kidolgozott 2x2-es rendszer: 3x + 2y = 16, x - y = 2
m = solve([Eq(3*x + 2*y, 16), Eq(x - y, 2)], [x, y], dict=True)[0]
chk("A1-x", m[x], 4); chk("A1-y", m[y], 2)
chk("A1-ell-1", 3*4 + 2*2, 16); chk("A1-ell-2", 4 - 2, 2)
chk("A1-kikuszoboles", (3*x + 2*y) + 2*(x - y), 5*x)
chk("A1-jobb", 16 + 2*2, 20)
chk("A1-metszes-y", (16 - 3*4)/2, 2); chk("A1-metszes-y2", 4 - 2, 2)
assert solve([Eq(x + y, 3), Eq(2*x + 2*y, 10)], [x, y]) == [], "parhuzamos: nincs megoldas"
assert len(linsolve([x + y - 3, 2*x + 2*y - 6], [x, y]).free_symbols) == 1
tp = solve(Eq(1200 + 20*t, 2000 + 12*t), t)[0]
chk("A1-tarifa-t", tp, 100)
chk("A1-tarifa-ar", 1200 + 20*100, 3200); chk("A1-tarifa-ar2", 2000 + 12*100, 3200)
chk("A1-tarifa-80", 1200 + 20*80, 2800); chk("A1-tarifa-80b", 2000 + 12*80, 2960)

# A2 — a kidolgozott 3x3-as rendszer
R1, R2, R3 = x + y + z - 6, 2*x - y + z - 3, x + 2*y - z - 2
m3 = solve([R1, R2, R3], [x, y, z], dict=True)[0]
chk("A2-x", m3[x], 1); chk("A2-y", m3[y], 2); chk("A2-z", m3[z], 3)
chk("A2-S2", simplify(R2 - 2*R1), -3*y - z + 9)      # -3y - z = -9  <=>  3y + z = 9
chk("A2-S3", simplify(R3 - R1), y - 2*z + 4)         #  y - 2z = -4
chk("A2-z-ertek", solve([Eq(3*y + z, 9), Eq(y - 2*z, -4)], [y, z], dict=True)[0][z], 3)
chk("A2-S3-3S2", (3*y + z - 9) - 3*(y - 2*z + 4), 7*z - 21)
chk("A2-visszahelyettesites", 6 - 2 - 3, 1)
chk("A2-ell-1", 1 + 2 + 3, 6); chk("A2-ell-2", 2*1 - 2 + 3, 3); chk("A2-ell-3", 1 + 4 - 3, 2)
chk("A2-egyszerusites", simplify((4*x - 6*y + 2*z - 10)/2), 2*x - 3*y + z - 5)

# A3 — (1) hatarozatlan: x+y+z=6, 2x+y-z=1, 3x+2y=7   (S3 bal oldala = S1 + S2 bal oldala)
chk("A3-S3-osszeg", simplify((x + y + z - 6) + (2*x + y - z - 1)), 3*x + 2*y - 7)
mo = list(linsolve([x + y + z - 6, 2*x + y - z - 1, 3*x + 2*y - 7], [x, y, z]))[0]
chk("A3-alt-x", mo[0].subs(mo[2], 3), 1)
chk("A3-alt-y", mo[1].subs(mo[2], 3), 2)
for cim, (a, b, c) in (("t3", (1, 2, 3)), ("t5", (5, -4, 5)), ("t0", (-5, 11, 0))):
    chk(cim + "-1", a + b + c, 6)
    chk(cim + "-2", 2*a + b - c, 1)
    chk(cim + "-3", 3*a + 2*b, 7)
chk("A3-lepcso", simplify((2*x + y - z - 1) - 2*(x + y + z - 6)), -y - 3*z + 11)
# a kidolgozott pelda eliminacios tablazata (c parameterrel a JOBB oldalon)
c = symbols("c")
chk("A3-tabla-S2", simplify((2*x + y - z - 1) - 2*(x + y + z - 6)), -y - 3*z + 11)
chk("A3-tabla-S3", simplify((3*x + 2*y - c) - 3*(x + y + z - 6)), -y - 3*z + 18 - c)
chk("A3-tabla-utolso", simplify((-y - 3*z + 18 - c) - (-y - 3*z + 11)), 7 - c)
chk("A3-tabla-c7", (7 - c).subs(c, 7), 0)
chk("A3-tabla-c10", -(7 - c).subs(c, 10), 3)
chk("A3-alak-1", (2*t - 5) + (11 - 3*t) + t, 6)
chk("A3-alak-2", 2*(2*t - 5) + (11 - 3*t) - t, 1)
chk("A3-alak-3", 3*(2*t - 5) + 2*(11 - 3*t), 7)
assert solve([Eq(x + y + z, 6), Eq(2*x + y - z, 1), Eq(3*x + 2*y, 10)], [x, y, z]) == []
chk("A3-ellentmondas", 10 - 7, 3)          # a 0 = 3 sor
m4 = solve([Eq(x + y + z, 6), Eq(2*x + y - z, 1), Eq(3*x + 2*y + z, 8)], [x, y, z], dict=True)[0]
chk("A3-hat-x", m4[x], -3); chk("A3-hat-y", m4[y], 8); chk("A3-hat-z", m4[z], 1)
chk("A3-hat-ell-1", -3 + 8 + 1, 6); chk("A3-hat-ell-2", -6 + 8 - 1, 1)
chk("A3-hat-ell-3", -9 + 16 + 1, 8)
assert solve([Eq(x + y, 5), Eq(x - y, 1)], [x, y], dict=True)[0][x] == 3
assert solve([Eq(x + y, 5), Eq(2*x + 2*y, 7)], [x, y]) == []

assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
KEK, BORO, ZOLD = "#3b82f6", "#f59e0b", "#047857"

SVG_METSZO = svg_fuggvenyek(
    [(lambda u: (16 - 3*u)/2, KEK, "3x + 2y = 16", [(-1, 6.5)]),
     (lambda u: u - 2, BORO, "x − y = 2", [(-1, 6.5)])],
    xr=(-1, 6.5), yr=(-2.5, 9.5), w=380, h=270,
    leiras="A két egyenes egyetlen pontban metszi egymást",
    pontok=[(4, 2, "(4; 2)", ZOLD, 8, 16)])
SVG_PARH = svg_fuggvenyek(
    [(lambda u: 3 - u, KEK, "x + y = 3", [(-1, 6.5)]),
     (lambda u: 5 - u, BORO, "2x + 2y = 10", [(-1, 6.5)])],
    xr=(-1, 6.5), yr=(-2.5, 6.5), w=380, h=250,
    leiras="Két párhuzamos egyenes: a rendszernek nincs megoldása")
SVG_EGYBE = svg_fuggvenyek(
    [(lambda u: 3 - u, KEK, "x + y = 3", [(-1, 6.5)]),
     (lambda u: 3 - u + 0.16, BORO, "2x + 2y = 6", [(-1, 6.5)])],
    xr=(-1, 6.5), yr=(-2.5, 6.5), w=380, h=250,
    leiras="A két egyenlet ugyanazt az egyenest írja le")
# a vizszintes tengely egysege 10 PERC, a fuggolegese EZER DINAR — kulonben a
# generator egysegnyi racsvonalai (0..160) suru fesuve valnak
SVG_HAROM_SIK = svg_harom_sik(w=620, h=205)
SVG_TARIFA = svg_fuggvenyek(
    [(lambda u: (1200 + 200*u)/1000, KEK, "A csomag", [(0, 15.5)]),
     (lambda u: (2000 + 120*u)/1000, BORO, "B csomag", [(0, 15.5)])],
    xr=(0, 15.5), yr=(0, 5.6), w=400, h=250,
    leiras="Két mobilcsomag havi díja a lebeszélt percek függvényében",
    tengely=("perc", "dinár"), egyseg=("10 perc", "1000 dinár"),
    pontok=[(10, 3.2, "100 perc · 3200 dinár", ZOLD, -132, -10)])

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> A Kristálypára-hálózat nem egyetlen ismeretlent rejt, hanem '
         '<b>többet egyszerre</b> — és minden egyes mérés csak egy <b>összefüggést</b> ad '
         'közöttük, nem magukat az értékeket. Egy összefüggés végtelen sok lehetőséget '
         'hagy nyitva. Ami kimetszi belőlük az egyetlen igazat, az a <b>rendszer</b>: '
         'több feltétel, egyszerre.'),
   '<p>Ez a témakör az 1e <b>lineáris egyenletek és rendszerek</b> témakörére épül — '
   'ott már megoldottál '
   '<a href="' + EGY1E + 'tananyag-egyenletrendszerek.html">kétismeretlenes rendszereket</a>. '
   'Most három dolgot teszünk hozzá: <b>rendszerezzük</b> a módszereket, kiterjesztjük őket '
   '<b>három ismeretlenre</b>, és megtanulunk <b>beszélni</b> arról, hogy hány megoldás van.</p>'
   '<p>Az első óra célja ezért nem az új anyag, hanem a <b>diagnózis</b>: ha a 2×2-es '
   'rendszer nem megy magabiztosan, a Gauss-eljárás sem fog.</p>',
 ]),

 ("Mi a lineáris egyenletrendszer", [
   doboz("definicio", "Lineáris egyenletrendszer",
         '<p>Egy egyenlet <b>lineáris</b> az $x$, $y$ (esetleg $z$) ismeretlenekben, ha '
         'mindegyik ismeretlen <b>legfeljebb az első hatványon</b> szerepel, az ismeretlenek '
         'nem állnak szorzatban <b>egymással</b>, és egyik sem szerepel nevezőben vagy '
         'gyökjel alatt. („Legfeljebb”, mert egy ismeretlen együtthatója nulla is lehet — '
         'ilyenkor az az ismeretlen egyszerűen nem jelenik meg az egyenletben.) '
         'Általános alakja két ismeretlennel:</p>'
         '$$ax+by=c,$$'
         '<p>ahol $a$, $b$, $c$ adott számok, és $a$, $b$ nem <b>egyszerre</b> nulla.</p>'
         '<p>Több ilyen egyenlet együtt — ha ugyanazokra az ismeretlenekre vonatkoznak — '
         'egy <b>lineáris egyenletrendszer</b>. A rendszer <b>megoldása</b> az az '
         'értékrendszer, amely <b>mindegyik</b> egyenletet igazzá teszi: két ismeretlennél '
         'egy $(x;y)$ <b>számpár</b>, háromnál egy $(x;y;z)$ számhármas.</p>',
         hid="def-rendszer"),
   '<p>Két rendszert <b>ekvivalensnek</b> nevezünk, ha ugyanaz a megoldáshalmazuk. Minden '
   'megoldási módszer azon alapul, hogy a rendszert lépésről lépésre <b>ekvivalens</b> '
   'átalakításokkal cseréljük egyszerűbbre — olyanokkal, amelyek egyetlen megoldást sem '
   'szüntetnek meg, és újat sem hoznak be.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Megoldottam: $x=4$.”</i></p>'
         '<p>Ez <b>nem megoldás</b>, csak a megoldás fele. A kétismeretlenes rendszer '
         'megoldása <b>számpár</b> — az alább megoldott rendszernél $(4;2)$. Aki csak az '
         'egyik ismeretlent írja le, az '
         'csak félig válaszolt — és ez pontveszteség akkor is, ha a számolás hibátlan '
         'volt.</p>'
         '<p>Ugyanide tartozik az <b>ellenőrzés elhagyása</b>. A kapott számpárt '
         '<b>mindkét</b> egyenletbe vissza kell helyettesíteni, nem csak abba, amelyikből '
         'kifejezted az egyiket — abban ugyanis a hibás érték is „stimmelni” fog, hiszen '
         'épp onnan származik.</p>'),
   kviz('Melyik lehet egy kétismeretlenes lineáris egyenletrendszer megoldása?',
        ['$(3;-1)$', '$x=3$', '$y=2x-1$', '$xy=3$'], 0,
        jo="✔ A megoldás számpár: egyszerre adja meg x és y értékét.",
        nem="✘ A kétismeretlenes rendszer megoldása SZÁMPÁR — egyetlen szám nem az, és "
            "egy egyenlet (akár kifejezett alakú) sem az."),
 ]),

 ("A két módszer — felidézés", [
   '<p>Két eljárást ismersz már az 1e-ből. Mindkettő ugyanarra megy ki: az egyik '
   'ismeretlent <b>eltüntetjük</b>, hogy egyismeretlenes egyenlet maradjon.</p>',
   r'<table class="tt-table">'
   r'<tr><th>Módszer</th><th>A lépés</th><th>Mikor a legjobb</th></tr>'
   r'<tr><td><b>behelyettesítés</b></td><td>az egyik egyenletből kifejezzük az egyik '
   r'ismeretlent, és beírjuk a másikba</td><td>ha valamelyik együttható $1$ vagy $-1$ — '
   r'akkor a kifejezés törtmentes</td></tr>'
   r'<tr><td><b>kiküszöbölés</b> (ellentett együtthatók módszere)</td><td>az egyenleteket '
   r'megszorozzuk úgy, hogy az egyik ismeretlen együtthatói ellentettek legyenek, majd '
   r'összeadjuk őket</td><td>ha egyik együttható sem $\pm1$, de „szép” számok</td></tr>'
   r'</table>',
   doboz("pelda", "Kristály-kamra szimuláció — ugyanaz a rendszer kétféleképpen",
         r'<p>Oldjuk meg a</p>'
         r'$$\begin{aligned}3x+2y&=16\\ x-y&=2\end{aligned}$$'
         r'<p>rendszert mindkét módszerrel.</p>'
         r'<p><b>1. Behelyettesítéssel.</b> A második egyenletben az $x$ együtthatója $1$, '
         r'ezért innen fejezzük ki: $x=y+2$. Beírjuk az elsőbe:</p>'
         r'$$3(y+2)+2y=16 \quad\Longrightarrow\quad 3y+6+2y=16 \quad\Longrightarrow\quad 5y=10,$$'
         r'<p>tehát $y=2$, és így $x=2+2=4$.</p>'
         r'<p><b>2. Kiküszöböléssel.</b> A második egyenletet $2$-vel szorozzuk, hogy az $y$ '
         r'együtthatói ellentettek legyenek:</p>'
         r'$$\begin{aligned}3x+2y&=16\\ 2x-2y&=4\end{aligned}$$'
         r'<p>Összeadva: $5x=20$, tehát $x=4$, és a második egyenletből $y=x-2=2$.</p>'
         r'<p><b>A két út ugyanoda visz</b> — ez nem véletlen, hanem éppen az ekvivalencia '
         r'következménye.</p>',
         hid="pelda-ket-modszer",
         lenyilo=("Ellenőrzés és végeredmény",
                  r'<p>$3\cdot4+2\cdot2=12+4=16$ ✔ &nbsp;&nbsp; $4-2=2$ ✔</p>'
                  r'<p class="vegeredmeny">A rendszer megoldása: $(x;y)=(4;2)$.</p>')),
 ]),

 ("Mit jelent mindez geometriailag", [
   '<p>Az $ax+by=c$ egyenlet a koordinátasíkban egy <b>egyenest</b> ír le. Ha $b\\ne0$, ez '
   'az egyenes egy lineáris függvény grafikonja — ezt az 1e-ben láttad; ha $b=0$ (például '
   '$x=3$), akkor <b>függőleges</b> egyenest kapunk, ami már nem függvénygrafikon. '
   'Két egyenlet tehát <b>két egyenes</b>, a rendszer '
   'megoldása pedig a két egyenes <b>közös pontja</b>. Ebből azonnal adódik, hogy '
   'pontosan három eset lehetséges.</p>',
   doboz("tetel", "A 2×2-es rendszer megoldásszáma",
         '<p>Két lineáris egyenlet két ismeretlennel három módon viselkedhet:</p>'
         '<table class="tt-table">'
         '<tr><th>A két egyenes</th><th>Megoldások száma</th><th>A rendszer neve</th></tr>'
         '<tr><td><b>metszi</b> egymást</td><td>pontosan egy</td><td>határozott</td></tr>'
         '<tr><td><b>párhuzamos</b> (nem esik egybe)</td><td>nincs</td><td>ellentmondásos</td></tr>'
         '<tr><td><b>egybeesik</b></td><td>végtelen sok</td><td>határozatlan</td></tr>'
         '</table>'
         '<p>Más eset <b>nincs</b>: két különböző egyenesnek legfeljebb egy közös pontja '
         'lehet, mert két ponton át pontosan egy egyenes megy.</p>',
         hid="tetel-geometriai-jelentes"),
   abra(SVG_METSZO, 'A $3x+2y=16$ és az $x-y=2$ egyenes egyetlen pontban metszi egymást: '
        'ez a metszéspont a rendszer megoldása, $(4;2)$.'),
   abra(SVG_PARH, 'Az $x+y=3$ és a $2x+2y=10$ egyenlet két <b>párhuzamos</b> egyenest ad '
        '(az egyik $y=3-x$, a másik $y=5-x$): nincs közös pont, tehát a rendszernek '
        '<b>nincs megoldása</b>.'),
   abra(SVG_EGYBE, 'Az $x+y=3$ és a $2x+2y=6$ ugyanazt az egyenest írja le (a második az '
        'első kétszerese). A két vonal az ábrán csak azért van elcsúsztatva, hogy '
        'mindkettő látszódjék — valójában <b>fedik</b> egymást, és az egyenes minden '
        'pontja megoldás: <b>végtelen sok</b> megoldás van.'),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Két mobilcsomag közül választasz. Az <b>A</b> csomag havidíja $1200$ dinár, és '
         'minden lebeszélt perc $20$ dinárba kerül; a <b>B</b> csomag havidíja $2000$ dinár, '
         'de a perc csak $12$ dinár. Melyik éri meg jobban?</p>'
         '<p>A két költség akkor egyenlő, ha $1200+20t=2000+12t$, azaz $8t=800$, tehát '
         '$t=100$ perc — ekkor mindkettő $3200$ dinár. <b>Száz percnél kevesebbet</b> beszélve az '
         'A csomag az olcsóbb ($80$ percnél $2800$ a $2960$ ellenében), <b>száz percnél '
         'többet</b> beszélve a B.</p>'
         '<p>A metszéspont tehát nem „a megoldás”, hanem a <b>fordulópont</b>: az a hely, '
         'ahol a jó válasz megváltozik. Minden ilyen döntésnél ezt keressük.</p>'
         + abra(SVG_TARIFA, 'A két csomag havi díja. A vízszintes tengelyen egy egység '
                '<b>10 perc</b>, a függőlegesen <b>ezer dinár</b>. A metszéspont a '
                'fordulópont: 100 percnél mindkettő 3200 dinár — előtte az A, utána a B '
                'az olcsóbb.')),
   kviz('Egy kétismeretlenes rendszert megoldva a $0=4$ egyenlőséghez jutsz. Mi következik ebből?',
        ['A rendszernek nincs megoldása — a két egyenes párhuzamos',
         'Elrontottad a számolást, kezdd újra',
         'A rendszernek végtelen sok megoldása van',
         'A megoldás $x=0$, $y=4$'], 0,
        jo="✔ A 0 = 4 hamis állítás: nincs olyan (x; y), amely mindkét egyenletet "
           "kielégítené. Ez a párhuzamos egyenesek esete — valódi eredmény, nem hiba.",
        nem="✘ A 0 = 4 nem számolási hiba jele, hanem eredmény: HAMIS állítás, tehát a "
            "rendszernek nincs megoldása. Geometriailag a két egyenes párhuzamos."),
 ]),

 ("Melyik módszert mikor", [
   '<p>Nincs „hivatalos” módszer — az a jó, amelyikkel a legkevesebb tört keletkezik. Két '
   'ökölszabály elég:</p>'
   '<ul>'
   '<li>ha valamelyik ismeretlen együtthatója $1$ vagy $-1$, <b>fejezd ki azt</b> és '
   'helyettesíts be;</li>'
   '<li>ha nincs ilyen, nézd meg, melyik ismeretlen együtthatóinak van <b>kis közös '
   'többszöröse</b> — azt küszöböld ki.</li>'
   '</ul>'
   '<p>A következő órán, három ismeretlennél ez a döntés már nem luxus, hanem '
   'időmegtakarítás: ott ugyanezt a választást <b>többször</b> kell meghozni.</p>',
   doboz("erdekesseg", "És ha ránézésre nem megy?",
         '<p>Épp ez a témakör oka. Két ismeretlennél még elboldogulsz ötletekkel; három '
         'ismeretlennél az ötlet elfogy. Ezért fogunk a következő órán olyan eljárást '
         'tanulni, amely <b>ötlet nélkül is működik</b>: mindig ugyanazokat a lépéseket '
         'kell végrehajtani, és a végén ott a megoldás. Ez az <b>algoritmus</b> lényege.</p>'),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Kanrak:</b> Két ismeretlen még kezes jószág. De a Kamra mérőállomásai '
         '<b>hármasával</b> küldik az adatot — és ott elfogy az ötlet. Kell egy '
         'eljárás, amit akkor is végig tudsz vinni, ha közben fogalmad sincs, hova '
         'tartasz. Ez következik.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
GAUSS_TABLA = (
 '<table class="tt-table">'
 '<tr><th>$x$</th><th>$y$</th><th>$z$</th><th>jobb oldal</th><th>művelet</th></tr>'
 '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
 '<tr><td>$2$</td><td>$-1$</td><td>$1$</td><td>$3$</td><td>$S_2-2S_1$</td></tr>'
 '<tr><td>$1$</td><td>$2$</td><td>$-1$</td><td>$2$</td><td>$S_3-S_1$</td></tr>'
 '<tr><th colspan="5">$\\sim$ &nbsp; az $x$ kiesett az alsó két sorból</th></tr>'
 '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
 '<tr><td>$0$</td><td>$-3$</td><td>$-1$</td><td>$-9$</td><td>$\\cdot(-1)$</td></tr>'
 '<tr><td>$0$</td><td>$1$</td><td>$-2$</td><td>$-4$</td><td></td></tr>'
 '<tr><th colspan="5">$\\sim$ &nbsp; $\\cdot(-1)$ <b>és</b> $S_2\\leftrightarrow S_3$ — hogy az $y$ együtthatója $1$ legyen</th></tr>'
 '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
 '<tr><td>$0$</td><td>$1$</td><td>$-2$</td><td>$-4$</td><td></td></tr>'
 '<tr><td>$0$</td><td>$3$</td><td>$1$</td><td>$9$</td><td>$S_3-3S_2$</td></tr>'
 '<tr><th colspan="5">$\\sim$ &nbsp; <b>lépcsős alak</b></th></tr>'
 '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
 '<tr><td>$0$</td><td>$1$</td><td>$-2$</td><td>$-4$</td><td></td></tr>'
 '<tr><td>$0$</td><td>$0$</td><td>$7$</td><td>$21$</td><td></td></tr>'
 '</table>')

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Három ismeretlennél a ránézés csődöt mond — nem azért, mert '
         'nehezebb, hanem mert <b>több</b>. Amire szükséged van, az egy <b>eljárás</b>: '
         'olyan lépéssorozat, amit mindig ugyanúgy hajtasz végre, és ami akkor is elvezet '
         'a megoldáshoz, ha közben nem látod előre a végét. Ez az algoritmus ereje.'),
   '<p>A <b>Gauss-eljárás</b> (más néven Gauss-elimináció) semmi újat nem használ: ugyanaz '
   'a kiküszöbölés, amit az előző órán is csináltál. Az újdonság a <b>fegyelem</b>: '
   'rögzített sorrendben, rögzített céllal végezzük.</p>',
 ]),

 ("A három megengedett lépés", [
   doboz("definicio", "Ekvivalens sorműveletek",
         '<p>Egy egyenletrendszeren a következő három lépés végezhető el úgy, hogy a '
         'megoldáshalmaz <b>nem változik</b> — az így kapott rendszer az eredetivel '
         '<b>ekvivalens</b> (jele: $\\sim$):</p>'
         '<ol>'
         '<li>két egyenlet <b>felcserélése</b>;</li>'
         '<li>egy egyenlet szorzása <b>nem nulla</b> számmal;</li>'
         '<li>egy egyenlethez egy másik egyenlet <b>számszorosának</b> hozzáadása.</li>'
         '</ol>'
         '<p>A harmadik lépés jelölése: $S_2-2S_1$ azt jelenti, hogy a második sorból '
         'kivonjuk az első sor kétszeresét, és az eredmény lesz az <b>új második sor</b> '
         '(az első sor változatlan marad).</p>',
         hid="def-ekvivalens-lepesek"),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Ha szorozhatok, akkor nullával is szorozhatok. És ha összeadhatok két '
         'egyenletet, akkor össze is szorozhatom őket.”</i></p>'
         '<p><b>Egyik sem igaz.</b></p>'
         '<ul>'
         '<li><b>Nullával szorozva</b> az egyenletből $0=0$ lesz — ez igaz állítás, de '
         'semmit nem mond. Elveszítettük az egyenletben tárolt <b>információt</b>, és így '
         'a kapott rendszernek <b>több megoldása lehet</b>, mint az eredetinek — az '
         'átalakítás tehát nem ekvivalens. Ezért kell a szorzóban a „nem nulla” '
         'kikötés.</li>'
         '<li><b>Összeszorozva</b> két egyenletet a bal oldalon $xy$-os tagok jelennek '
         'meg: az eredmény már nem is lineáris. Ráadásul a szorzat akkor is nulla, ha '
         'csak az <b>egyik</b> tényező az — vagyis ha csak az egyik egyenlet teljesül. '
         'Így olyan számpárok is átcsúsznak, amelyek az eredeti rendszernek nem '
         'megoldásai.</li>'
         '</ul>'
         '<p>Összeadni szabad, szorozni <b>számmal</b> szabad — egyenlettel nem.</p>'),
   kviz('Melyik lépés után <b>nem</b> lesz az új rendszer ekvivalens az eredetivel?',
        ['Ha az egyik egyenletet $0$-val szorozzuk',
         'Ha felcseréljük az első és a harmadik egyenletet',
         'Ha az egyik egyenletet $-3$-mal szorozzuk',
         'Ha a második egyenlethez hozzáadjuk az első ötszörösét'], 0,
        jo="✔ A nullával való szorzás az egyenletet 0 = 0-vá alakítja: az információ "
           "elvész, és a rendszernek több megoldása lehet, mint volt.",
        nem="✘ A sorcsere, a NEM NULLA számmal való szorzás és a másik sor számszorosának "
            "hozzáadása mind ekvivalens lépés. Egyedül a nullával szorzás nem az."),
 ]),

 ("A cél: a lépcsős alak", [
   r'<p>Az eljárás célja, hogy a rendszert <b>lépcsős (háromszög) alakra</b> hozzuk: az '
   r'első egyenletben mindhárom ismeretlen szerepel, a másodikban már csak kettő, a '
   r'harmadikban csak egy.</p>'
   r'$$\begin{aligned}a_{11}x+a_{12}y+a_{13}z&=b_1\\ a_{22}y+a_{23}z&=b_2\\ '
   r'a_{33}z&=b_3\end{aligned}$$'
   r'<p>Ez az alak akkor vezet egyértelmű megoldáshoz, ha a „lépcsőfokokon” álló '
   r'$a_{11}$, $a_{22}$, $a_{33}$ együtthatók egyike sem nulla. Hogy mi történik, ha '
   r'valamelyik mégis nullává válik, arról a következő órán lesz szó.</p>',
   doboz("tetel", "A Gauss-eljárás menete",
         '<p><b>1. Előre haladó szakasz (elimináció).</b></p>'
         '<ol>'
         '<li>Az első egyenlet segítségével ejtsük ki az $x$-et a második és a harmadik '
         'egyenletből.</li>'
         '<li>A (már $x$ nélküli) második egyenlet segítségével ejtsük ki az $y$-t a '
         'harmadikból.</li>'
         '</ol>'
         '<p><b>2. Visszafelé haladó szakasz (visszahelyettesítés).</b> A harmadik '
         'egyenletből $z$ közvetlenül adódik; ezt a másodikba írva megkapjuk $y$-t, majd '
         'mindkettőt az elsőbe írva $x$-et.</p>'
         '<p>Az eljárás <b>mindig</b> véget ér, és a lépcsős alakból az is leolvasható, ha '
         'a rendszernek nincs vagy végtelen sok megoldása van — erről a következő órán '
         'lesz szó.</p>',
         hid="tetel-gauss"),
   '<p>A rendezett írásmód itt nem stílus kérdése: a sorműveletet <b>a sor mellé</b> írjuk '
   'ki, hogy visszakereshető legyen, mit csináltunk. Aki ezt elhagyja, a saját hibáját nem '
   'tudja megtalálni — és a javításnál sem tudja megmutatni, hol tartott.</p>',
 ]),

 ("Egy teljes levezetés", [
   doboz("pelda", "Kristály-kamra szimuláció — Gauss-eljárás végig",
         r'<p>Oldjuk meg a</p>'
         r'$$\begin{aligned}x+y+z&=6\\ 2x-y+z&=3\\ x+2y-z&=2\end{aligned}$$'
         r'<p>rendszert. Az együtthatókat táblázatba írjuk — az ismeretlenek nevét elég '
         r'egyszer, a fejlécben kiírni:</p>'
         + GAUSS_TABLA +
         r'<p><b>Az első lépés.</b> Az $x$ együtthatója az első sorban $1$, ezért ez a sor '
         r'a legalkalmasabb az elimináláshoz: $S_2-2S_1$ és $S_3-S_1$ mindkét alsó sorból '
         r'kiejti az $x$-et.</p>'
         r'<p><b>A második lépés.</b> A kapott $-3y-z=-9$ sort $(-1)$-gyel szorozzuk '
         r'($3y+z=9$), a másik sor pedig $y-2z=-4$ maradt. Ezt a kettőt felcseréljük, '
         r'hogy az $y$ '
         r'együtthatója $1$ legyen a második sorban — így a következő lépésben nem '
         r'keletkezik tört.</p>'
         r'<p><b>A harmadik lépés.</b> $S_3-3S_2$: a $3y$ kiesik, és marad $7z=21$.</p>'
         r'<p><b>Visszahelyettesítés.</b> A harmadik sorból $z=3$. Ezt a másodikba írva '
         r'$y-2\cdot3=-4$, tehát $y=2$. Végül az elsőbe: $x+2+3=6$, tehát $x=1$.</p>',
         hid="pelda-gauss",
         lenyilo=("Ellenőrzés és végeredmény",
                  r'<p>$1+2+3=6$ ✔ &nbsp;&nbsp; $2\cdot1-2+3=3$ ✔ &nbsp;&nbsp; '
                  r'$1+2\cdot2-3=2$ ✔</p>'
                  r'<p class="vegeredmeny">A rendszer megoldása: $(x;y;z)=(1;2;3)$.</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A Gauss-elimináció az egyik <b>legtöbbet futtatott algoritmus</b> a világon. '
         'A szerkezetek statikai számítása, az áramkör-szimulációk és a 3D-s renderelés '
         'mélyén lineáris egyenletrendszerek állnak — csak nem három, hanem több millió '
         'ismeretlennel —, és ezeket a Gauss-elimináció továbbfejlesztett változatai '
         'oldják meg. (A legnagyobb rendszereknél, például az időjárás-előrejelzésben, '
         'már más, közelítő eljárások futnak.) Az elv ott is pontosan ugyanez: nullákat '
         'gyártani a főátló alá.</p>'
         '<p>A név Carl Friedrich Gaussé, de a módszer jóval régebbi: egy ókori kínai '
         'matematikai gyűjtemény, a <i>Kilenc fejezet a matematika művészetéről</i> már '
         'kétezer évvel ezelőtt lényegében ugyanígy oldott meg rendszereket.</p>'),
   kviz('A lépcsős alak utolsó sora $7z=21$. Milyen sorrendben kapod meg az ismeretleneket?',
        ['$z$, majd $y$, majd $x$', '$x$, majd $y$, majd $z$',
         '$z$, majd $x$, majd $y$', 'Mindegy, bármelyik sorrendben'], 0,
        jo="✔ A visszahelyettesítés alulról fölfelé halad: az utolsó sorban egyetlen "
           "ismeretlen van, azt kapjuk meg elsőnek.",
        nem="✘ Alulról fölfelé kell haladni: az utolsó sor csak z-t tartalmazza, ezért az "
            "adódik elsőként; az így kapott értéket írjuk vissza a fölötte lévő sorokba."),
 ]),

 ("Amikor érdemes eltérni az algoritmustól", [
   '<p>A Gauss-eljárás <b>mindig</b> működik — de nem mindig a leggyorsabb út. Két '
   'egyszerű trükk sok törtet spórol:</p>'
   '<ul>'
   '<li><b>Válaszd az $1$-es együtthatót.</b> Ha valamelyik egyenletben egy ismeretlen '
   'együtthatója $1$ vagy $-1$, azt az egyenletet tedd az élre, és azzal ejtsd ki az '
   'ismeretlent — így a szorzók egészek maradnak. A fenti példában épp ezért cseréltük '
   'fel a két alsó sort.</li>'
   '<li><b>Egyszerűsíts.</b> Ha egy egyenlet minden együtthatója (a jobb oldali számot is '
   'beleértve) osztható ugyanazzal a számmal, oszd el vele: $4x-6y+2z=10$ helyett írj '
   '$2x-3y+z=5$-öt. Ez ekvivalens lépés (2. sorművelet), és lényegesen könnyíti a további '
   'számolást.</li>'
   '</ul>'
   '<p>Az eltérés tehát <b>nem</b> az algoritmus megsértése: ugyanazokat a megengedett '
   'lépéseket használjuk, csak ügyesebb sorrendben.</p>',
   doboz("csapda", "Két gyakori elszámolás",
         '<p><b>1. Az elhagyott jobb oldal.</b> A sorművelet a sor <b>minden</b> elemére '
         'vonatkozik, a jobb oldali számra is. Aki csak az együtthatókat vonja ki, annak a '
         'rendszere már nem ekvivalens az eredetivel.</p>'
         '<p><b>2. A hiányzó ismeretlen.</b> Ha egy egyenletből hiányzik valamelyik '
         'ismeretlen (például $3x+2y=7$), a táblázatba oda <b>nulla</b> kerül, nem üres '
         'hely. A $z$ együtthatója itt $0$ — és ez a nulla ugyanúgy részt vesz a '
         'sorműveletekben.</p>'),
   GY(FGY + "#alap-7", "A 7–14", FGY + "#kozep-4", "K 4–9"),
   brief('<b>Kanrak:</b> Az eljárás fut, a lépcsők kirajzolódnak. De mi történik, ha az '
         'utolsó sorban nem $7z=21$ áll, hanem $0=0$ — vagy ami rosszabb, $0=5$? A Kamra '
         'hálózata néha <b>ellentmond önmagának</b>. Ez nem hiba: ez információ.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Az anomália-hálózat időnként olyan mérési sort küld, amelyből '
         '<b>semmi</b> nem következik — és olyat is, amely <b>önmagának mond ellent</b>. '
         'Az első esetben kevés a mérés, a másodikban valamelyik műszer hazudik. A '
         'Gauss-eljárás mindkettőt megmutatja, ha tudod, mit kell nézni.'),
   '<p>Ezen az órán nem csak kiszámoljuk a megoldást — meg is <b>indokoljuk, hány van '
   'belőle</b>. Ez a témakör egyik legfontosabb készsége: a „nincs megoldás” és a „végtelen '
   'sok megoldás” ugyanolyan teljes értékű válasz, mint egy számhármas — de csak akkor, '
   'ha meg is tudod mutatni, miből jött.</p>',
 ]),

 ("A három eset", [
   doboz("definicio", "Határozott, határozatlan, ellentmondásos",
         '<table class="tt-table">'
         '<tr><th>A rendszer</th><th>Megoldásainak száma</th><th>Példa (2×2)</th></tr>'
         '<tr><td><b>határozott</b></td><td>pontosan egy</td>'
         '<td>$x+y=5$, $x-y=1$ &nbsp;→&nbsp; $(3;2)$</td></tr>'
         '<tr><td><b>határozatlan</b></td><td>végtelen sok</td>'
         '<td>$x+y=5$, $2x+2y=10$</td></tr>'
         '<tr><td><b>ellentmondásos</b></td><td>egy sincs</td>'
         '<td>$x+y=5$, $2x+2y=7$</td></tr>'
         '</table>'
         '<p>Az utolsó két esetet együtt <b>nem határozott</b> rendszernek is szokás '
         'nevezni. Figyeld meg a két alsó példát: a bal oldalak ugyanazok, a különbség csak '
         'a jobb oldalon van. Ugyanazt az egyenletet írtuk le kétszer — egyszer '
         'következetesen, egyszer önmagának ellentmondva.</p>',
         hid="def-harom-eset"),
   kviz('Egy rendszerről kiderül, hogy <b>határozatlan</b>. Mit jelent ez?',
        ['Végtelen sok megoldása van', 'Nincs megoldása',
         'Nem lehet eldönteni, van-e megoldása', 'Pontosan egy megoldása van'], 0,
        jo="✔ A határozatlan rendszernek végtelen sok megoldása van: a feltételek "
           "kevesebbet kötnek meg, mint amennyi ismeretlen van.",
        nem="✘ A „határozatlan” nem azt jelenti, hogy nem tudjuk eldönteni, és nem is azt, "
            "hogy nincs megoldás: azt jelenti, hogy VÉGTELEN SOK megoldás van. Amelyiknek "
            "nincs megoldása, az az ellentmondásos rendszer."),
 ]),

 ("Hogyan ismerem fel a Gauss-eljárás közben", [
   doboz("tetel", "A $0=0$ és a $0=k$ sor",
         '<p>Ha az elimináció közben egy egyenlet bal oldalán minden együttható nullává '
         'válik, két eset lehetséges:</p>'
         '<ul>'
         '<li><b>$0=0$</b> — ez <b>igaz</b> állítás, minden $(x;y;z)$ kielégíti. A sor '
         'tehát <b>fölösleges</b> (nem szűkít semmit), elhagyható. Ha ezután kevesebb '
         'egyenlet marad, mint ahány ismeretlen van, <b>és közben nem keletkezett '
         '$0=k$ alakú sor sem</b>, akkor a rendszer <b>határozatlan</b>.</li>'
         '<li><b>$0=k$</b>, ahol $k\\ne0$ — ez <b>hamis</b> állítás, semmilyen $(x;y;z)$ '
         'nem elégíti ki. A rendszer <b>ellentmondásos</b>, és itt azonnal megállhatunk: '
         'tovább számolni értelmetlen.</li>'
         '</ul>',
         hid="tetel-felismeres"),
   doboz("pelda", "Kristály-kamra szimuláció — ugyanaz a bal oldal, két jobb oldal",
         r'<p>Nézzük a</p>'
         r'$$\begin{aligned}x+y+z&=6\\ 2x+y-z&=1\\ 3x+2y\phantom{{}+z}&=c\end{aligned}$$'
         r'<p>rendszert, ahol a $c$ helyére kétféle számot írunk. Figyeld meg, hogy a '
         r'harmadik egyenlet bal oldala <b>pontosan</b> az első kettő összege: '
         r'$(x+y+z)+(2x+y-z)=3x+2y$. Ezért az első két egyenletből <b>következik</b>, hogy '
         r'$3x+2y=6+1=7$.</p>'
         r'<p>Végezzük el az eliminációt egyszerre mindkét esetre — a $c$ végig együtt '
         r'utazik a jobb oldallal:</p>'
         '<table class="tt-table">'
         '<tr><th>$x$</th><th>$y$</th><th>$z$</th><th>jobb oldal</th><th>művelet</th></tr>'
         '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
         '<tr><td>$2$</td><td>$1$</td><td>$-1$</td><td>$1$</td><td>$S_2-2S_1$</td></tr>'
         '<tr><td>$3$</td><td>$2$</td><td>$0$</td><td>$c$</td><td>$S_3-3S_1$</td></tr>'
         '<tr><th colspan="5">$\\sim$ &nbsp; az alsó két sor MEGEGYEZIK a bal oldalon</th></tr>'
         '<tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$6$</td><td></td></tr>'
         '<tr><td>$0$</td><td>$-1$</td><td>$-3$</td><td>$-11$</td><td></td></tr>'
         '<tr><td>$0$</td><td>$-1$</td><td>$-3$</td><td>$c-18$</td><td>$S_3-S_2$</td></tr>'
         '<tr><th colspan="5">$\\sim$ &nbsp; az utolsó sor</th></tr>'
         '<tr><td>$0$</td><td>$0$</td><td>$0$</td><td>$c-7$</td><td></td></tr>'
         '</table>'
         r'<p><b>Ha $c=7$:</b> az utolsó sor $0=0$ — a harmadik egyenlet nem mond semmi '
         r'újat. Az elimináció '
         r'után tehát csak két független egyenlet jut három ismeretlenre, és a rendszer '
         r'<b>határozatlan</b>.</p>'
         r'<p><b>Ha $c=10$:</b> az utolsó sor $0=3$ — hamis állítás. A harmadik egyenlet '
         r'ellentmond az első kettőnek, a rendszer <b>ellentmondásos</b>: nincs megoldása.</p>'
         r'<p><b>És ha egyetlen megoldást szeretnénk?</b> Akkor a <b>bal oldalhoz</b> kell '
         r'nyúlni. Ha a harmadik egyenlet $3x+2y+z=8$, a bal oldalak már nem függenek '
         r'össze, és a rendszer <b>határozott</b> lesz.</p>'
         r'<p>Ez a példa egy fontos dolgot mutat meg: a megoldások száma <b>nem</b> egyedül '
         r'a jobb oldalon dől el. Ha egy <b>három egyenletből álló, háromismeretlenes</b> '
         r'rendszerben a bal oldalak összefüggenek, akkor a jobb oldaltól függően „nincs” '
         r'vagy „végtelen sok” megoldás lesz — de <b>pontosan egy soha</b>.</p>',
         hid="pelda-harom-eset",
         lenyilo=("Végeredmények",
                  '<p class="vegeredmeny">$c=7$: határozatlan · $c=10$: ellentmondásos · '
                  '$3x+2y+z=8$ esetén határozott, $(x;y;z)=(-3;8;1)$.</p>')),
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A $0=0$ sor azt jelenti, hogy nincs megoldás — hiszen elfogyott az '
         'egyenlet.”</i></p>'
         '<p><b>Pont fordítva van.</b> Mondd ki hangosan: <i>„a nulla egyenlő nullával”</i> '
         '— ez <b>mindig igaz</b>. Egy mindig igaz állítás senkit nem zár ki, tehát nem is '
         'szűkít semmit: a rendszernek <b>marad</b> megoldása, sőt végtelen sok.</p>'
         '<p>És most a másik: <i>„a nulla egyenlő öttel”</i> — ez <b>soha nem igaz</b>. Egy '
         'soha nem igaz állítás mindenkit kizár: <b>nincs</b> megoldás.</p>'
         '<p>Az egyetlen dolog, amit meg kell jegyezned: nem a bal oldali nulla számít, '
         'hanem az, hogy a <b>jobb oldal</b> is nulla-e.</p>'),
   kviz('A Gauss-eljárás során az egyik sorból $0=0$ lesz. Mi következik?',
        ['A sor fölösleges — elhagyható, és a rendszer határozatlan lehet',
         'A rendszernek nincs megoldása',
         'A rendszernek pontosan egy megoldása van',
         'Elszámoltuk a sorműveletet'], 0,
        jo="✔ A 0 = 0 igaz állítás: nem szűkít semmit, ezért a sor elhagyható. Ha így "
           "kevesebb egyenlet marad, mint ahány ismeretlen — és nincs 0 = k alakú sor —, "
           "a rendszer határozatlan.",
        nem="✘ A 0 = 0 IGAZ állítás, tehát nem zár ki megoldást — a sor egyszerűen "
            "fölösleges. Ami kizárja a megoldást, az a 0 = k alakú (k ≠ 0) sor."),
 ]),

 ("Hogyan írjuk fel a végtelen sok megoldást", [
   '<p>Ha a rendszer határozatlan, nem elég annyit írni, hogy „végtelen sok megoldás van”. '
   'A megoldásokat <b>fel is kell sorolni</b> — ezt egy <b>szabad paraméterrel</b> tesszük.</p>',
   r'<p>A fenti $c=7$ esetben az $S_2-2S_1$ lépés a $-y-3z=-11$, azaz az $y+3z=11$ sort '
   r'adja. Az $S_3-3S_1$ ugyanezt hozza ki a harmadik sorból ($-y-3z=-11$), ezért a kettő '
   r'különbsége már $0=0$. A lépcsős alak tehát mindössze <b>két</b> egyenletet ad három '
   r'ismeretlenre:</p>'
   r'$$\begin{aligned}x+y+z&=6\\ y+3z&=11\end{aligned}$$'
   r'<p>Legyen $z=t$ tetszőleges valós szám; ekkor a második egyenletből $y=11-3t$, az '
   r'elsőből pedig $x=6-y-z=6-(11-3t)-t=2t-5$. A megoldások tehát:</p>'
   r'$$(x;y;z)=(2t-5;\;11-3t;\;t),\qquad t\in\mathbb{R}.$$'
   r'<p>Ez <b>egyetlen</b> képlet, amely az összes megoldást leírja. Behelyettesítéssel '
   r'bármelyik ellenőrizhető: $t=3$ esetén $(1;2;3)$, $t=5$ esetén $(5;-4;5)$, $t=0$ esetén '
   r'$(-5;11;0)$ — és mindhárom kielégíti mind a három egyenletet.</p>',
   doboz("erdekesseg", "🔒 Meddig megyünk el?",
         '<p>A megoldások számának megvitatását <b>konkrét</b> rendszereken végezzük: adott '
         'számok, kiszámolt lépcsős alak, leolvasott eset. Az olyan feladat, amelyben az '
         'együtthatók között <b>paraméter</b> áll (például $ax+y=2$, és azt kell '
         'megvizsgálni, hogy $a$ mely értékeire hány megoldás van), a mi tantervünkben '
         '<b>nem szerepel</b> — az az általános és a természettudományi-matematikai '
         'program anyaga. Ugyanígy nem foglalkozunk olyan rendszerrel sem, amelyben az '
         'egyenletek és az ismeretlenek száma <b>különbözik</b> (2×3-as, 3×2-es): nálunk '
         'minden rendszer 2×2-es vagy 3×3-as.</p>'
         '<p>A szabad paraméter, amit az imént bevezettünk ($z=t$), <b>nem ilyen</b>: az a '
         '<b>megoldás</b> leírásának eszköze, nem az egyenletrendszer adata.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A mérnöki gyakorlatban a két eset két különböző üzenetet hordoz. Az '
         '<b>ellentmondásos</b> rendszer általában <b>mérési hibát</b> jelez: a műszerek '
         'olyat állítanak együtt, ami egyszerre nem lehet igaz — valamelyik rosszul mér. A '
         '<b>határozatlan</b> rendszer viszont azt mondja, hogy <b>kevés a mérés</b>: az '
         'adatok igazak, csak nem elegendők az ismeretlenek egyértelmű meghatározásához. Az '
         'első esetben javítani kell, a másodikban mérni kell még egyet.</p>'),
 ]),

 ("A geometriai kép", [
   '<p>Két ismeretlennél két egyenest néztünk. Három ismeretlennél az $ax+by+cz=d$ egyenlet '
   'a térben egy <b>síkot</b> ír le, a rendszer megoldása pedig a három sík <b>közös '
   'pontjainak</b> halmaza. Az eseteket ugyanaz a három szó írja le:</p>'
   '<table class="tt-table">'
   '<tr><th>A három sík</th><th>Közös rész</th><th>A rendszer</th></tr>'
   '<tr><td>egyetlen pontban metszi egymást</td><td>egy pont</td><td>határozott</td></tr>'
   '<tr><td>egy közös egyenesen megy át</td><td>egy egyenes</td><td>határozatlan</td></tr>'
   '<tr><td>mindhárom egybeesik</td><td>egy sík</td><td>határozatlan</td></tr>'
   '<tr><td>nincs mindháromnak közös pontja</td><td>üres halmaz</td><td>ellentmondásos</td></tr>'
   '</table>',
   abra(SVG_HAROM_SIK, 'A három eset térben. Balra a három sík <b>egyetlen pontban</b> '
        'találkozik (mint a szoba két fala és a mennyezet). Középen mindhárom ugyanazon '
        'az <b>egyenesen</b> megy át (mint egy nyitott könyv lapjai a gerincnél). Jobbra '
        'a három sík páronként metszi egymást, de a <b>három metszésvonal különböző</b> '
        'és párhuzamos — nincs olyan pont, amely mindhárom síkon rajta volna.'),
   '<p>Fogj két füzetlapot és nézz körül a szobában — a három esetet kézzel is meg tudod '
   'mutatni. A szoba két fala és a mennyezet egyetlen <b>sarokban</b> találkozik: ez a '
   'határozott eset. Egy nyitott könyv lapjai a <b>gerincnél</b> futnak össze: ez a '
   'határozatlan. Egy háromoldalú hasáb három oldallapja pedig <b>háromszöget zár be</b> '
   'anélkül, hogy volna közös pontjuk: ez az ellentmondásos eset.</p>',
   doboz("csapda", "Nem elég a válasz — indokolni is kell",
         '<p>Ha egy feladat azt kérdezi, hogy „hány megoldása van a rendszernek”, a '
         'válaszhoz <b>hozzátartozik a bizonyíték</b>: melyik sorból, milyen sorművelet után '
         'lett $0=0$ vagy $0=k$. Az önmagában álló „nincs megoldás” mondat nem megoldás, '
         'csak sejtés — akkor is, ha történetesen igaz.</p>'),
   kviz('Egy háromismeretlenes rendszer eliminációja után az utolsó sor $0=-4$. Hány megoldás van?',
        ['Egy sincs', 'Végtelen sok', 'Pontosan egy — mégpedig $z=-4$',
         'Nem lehet eldönteni a lépcsős alakból'], 0,
        jo="✔ A 0 = −4 hamis állítás, tehát nincs olyan számhármas, amely mindhárom "
           "egyenletet kielégítené: a rendszer ellentmondásos.",
        nem="✘ A jobb oldalon nem nulla áll, tehát a 0 = −4 HAMIS: a rendszer "
            "ellentmondásos, egyetlen megoldása sincs. (Ha 0 = 0 lenne, akkor volna "
            "végtelen sok.)"),
   GY(FGY + "#alap-15", "A 15–18", FGY + "#kozep-10", "K 10–13"),
   brief('<b>Kanrak:</b> Most már meg tudod mondani, <b>hány</b> megoldás van — de csak úgy, '
         'ha végigcsinálod az eliminációt. Van gyorsabb út is: egyetlen szám, amit az '
         'együtthatókból számolsz, és amely előre elárulja, hogy a rendszer határozott-e. '
         'Ehhez viszont új eszköz kell.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-ket-ismeretlen.html",
     cim="Két egyenlet, két ismeretlen — és ami mögötte van",
     cim_tiszta="Két egyenlet, két ismeretlen",
     alcim="A lineáris egyenletrendszer fogalma, a behelyettesítéses és a kiküszöböléses "
           "módszer, és a megoldás geometriai jelentése.",
     chip=KUL + " · 1/6", szakaszok=A1,
     elozo=("index.html", "Lineáris egyenletrendszerek — témakör"),
     kovetkezo=("tananyag-gauss.html", "A Gauss-eljárás")),
 lap(**T, fajl="tananyag-gauss.html",
     cim="A Gauss-eljárás",
     cim_tiszta="A Gauss-eljárás",
     alcim="A három ekvivalens sorművelet, a lépcsős alak, a visszahelyettesítés és a "
           "rendezett íráskép.",
     chip=KUL + " · 2/6", szakaszok=A2,
     elozo=("tananyag-ket-ismeretlen.html", "Két egyenlet, két ismeretlen"),
     kovetkezo=("tananyag-megoldasok-szama.html", "Hány megoldás van?")),
 lap(**T, fajl="tananyag-megoldasok-szama.html",
     cim="Hány megoldás van?",
     cim_tiszta="Hány megoldás van?",
     alcim="Határozott, határozatlan és ellentmondásos rendszer; a nullás sorok jelentése; "
           "a megoldások felírása szabad paraméterrel.",
     chip=KUL + " · 3/6", szakaszok=A3,
     elozo=("tananyag-gauss.html", "A Gauss-eljárás"),
     kovetkezo=("tananyag-determinans.html", "A determináns")),
]
for u in KI:
    print("✓", os.path.basename(u))
