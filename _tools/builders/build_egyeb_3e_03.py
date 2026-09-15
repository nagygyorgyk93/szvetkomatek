# -*- coding: utf-8 -*-
"""3e/03 — osszefoglalo (F4); a terepkuldetes (F5p), a Veszterem (F6h) es a
temakor-index (F5) ide kerul majd. Mentor: Kanrak. Kuldetes: A Rendszer Hibaja."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, abra
from abra_common import svg_sarrus, svg_harom_sik

T = dict(tagozat="3e", mappa="03-linearis-rendszerek", temakor="Lineáris egyenletrendszerek")
KUL = "A Rendszer Hibája"

# ---------------------------------------------------------------- önteszt
from sympy import Matrix, symbols, linsolve, FiniteSet, EmptySet
x, y, z = symbols('x y z')
E = []


def chk(n, g, w):
    if g != w:
        E.append((n, g, w))


chk("pelda-2x2", linsolve([x + y - 5, x - y - 1], [x, y]), FiniteSet((3, 2)))
chk("pelda-hatarozatlan", linsolve([x + y - 5, 2*x + 2*y - 10], [x, y]), FiniteSet((5 - y, y)))
chk("pelda-ellentmondasos", linsolve([x + y - 5, 2*x + 2*y - 7], [x, y]), EmptySet)
chk("det2", Matrix([[2, 1], [3, 4]]).det(), 5)
A, b = Matrix([[2, 1], [1, -1]]), Matrix([5, 1])
Dx, Dy = A.copy(), A.copy()
Dx[:, 0] = b
Dy[:, 1] = b
chk("cramer-D", (A.det(), Dx.det(), Dy.det()), (-3, -6, -3))
chk("cramer-m", tuple(A.LUsolve(b)), (2, 1))
assert not E, E
print("sympy önteszt: OK")


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


KI = "tananyag-ket-ismeretlen.html"
GA = "tananyag-gauss.html"
MS = "tananyag-megoldasok-szama.html"
DE = "tananyag-determinans.html"
CR = "tananyag-cramer.html"
SZ = "tananyag-szoveges-feladatok.html"

SUB = "<tspan baseline-shift='sub' font-size='10'>{}</tspan>"
SVG_SARRUS = svg_sarrus(tuple(tuple("a" + SUB.format(f"{i}{j}") for j in (1, 2, 3)) for i in (1, 2, 3)),
                        w=470, h=250, azon="ossz",
                        leiras="A Sarrus-séma általánosan: az első két oszlop megismételve, "
                               "a három lefelé haladó átló pozitív, a három fölfelé haladó negatív")
SVG_HAROM_SIK = svg_harom_sik(w=620, h=205)

# ==================================================================== F4
OSSZ = [
 ("A rendszer és a megoldása", [
  '<p>Egy egyenlet <b>lineáris</b>, ha minden ismeretlen legfeljebb az <b>első hatványon</b> '
  'szerepel, az ismeretlenek nem állnak <b>szorzatban</b> egymással, és egyik sincs nevezőben '
  'vagy gyökjel alatt (' + h(KI, "def-rendszer") + '). A rendszer <b>megoldása</b> minden olyan '
  'számpár $(x;y)$ — három ismeretlennél számhármas $(x;y;z)$ —, amely <b>mindegyik</b> '
  'egyenletet igazzá teszi.</p>'
  '<table class="tt-table">'
  '<tr><th>Módszer</th><th>A lényege</th><th>Mikor érdemes</th></tr>'
  '<tr><td><b>behelyettesítés</b></td><td>az egyik egyenletből kifejezünk egy ismeretlent, és '
  'beírjuk a másikba</td><td>ha valamelyik együttható $1$ vagy $-1$</td></tr>'
  '<tr><td><b>kiküszöbölés</b></td><td>az egyenleteket úgy szorozzuk, hogy egy ismeretlen '
  'együtthatói egyenlők legyenek, majd kivonjuk (vagy összeadjuk) őket</td>'
  '<td>ha az együtthatók könnyen egyenlővé tehetők</td></tr>'
  '<tr><td><b>Gauss-eljárás</b></td><td>lépcsős alak, majd visszahelyettesítés</td>'
  '<td>mindig működik; három ismeretlennél általában ez a legrövidebb</td></tr>'
  '<tr><td><b>Cramer-szabály</b></td><td>determinánsok hányadosa</td>'
  '<td>ha $D\\ne0$, főleg ha csak egy ismeretlen kell</td></tr>'
  '</table>'
  '<p><b>Két ismeretlen, két egyenes</b> (' + h(KI, "tetel-geometriai-jelentes") + '):</p>'
  '<table class="tt-table">'
  '<tr><th>A két egyenes</th><th>Megoldások száma</th><th>Példa</th></tr>'
  '<tr><td>metszi egymást ($D\\ne0$)</td><td>pontosan egy</td><td>$x+y=5$, $x-y=1$ → $(3;2)$</td></tr>'
  '<tr><td>párhuzamos, nem esik egybe</td><td>nincs</td><td>$x+y=5$, $2x+2y=7$</td></tr>'
  '<tr><td>egybeesik</td><td>végtelen sok</td><td>$x+y=5$, $2x+2y=10$</td></tr>'
  '</table>'
  '<p>✅ <b>Ellenőrzés:</b> a kapott értékeket <b>minden</b> egyenletbe vissza kell '
  'helyettesíteni, nem csak abba, amelyikből kifejeztük.</p>',
 ]),

 ("A Gauss-eljárás", [
  '<p>Jelölés: $S_1$, $S_2$, $S_3$ az első, a második és a harmadik egyenlet (sor). '
  '<b>A három megengedett lépés</b> — az így kapott rendszer az eredetivel ekvivalens, a kettő '
  'közé $\\sim$ jelet írunk (' + h(GA, "def-ekvivalens-lepesek") + '):</p>'
  '<ol><li>két egyenlet <b>felcserélése</b>;</li>'
  '<li>egy egyenlet szorzása <b>nem nulla</b> számmal;</li>'
  '<li>egy egyenlethez egy másik egyenlet <b>számszorosának hozzáadása</b> — például '
  '$S_2-2S_1$: a második egyenletből kivonjuk az első kétszeresét.</li></ol>'
  '<p><b>A menet</b> (' + h(GA, "tetel-gauss") + '):</p>'
  '<ol><li><b>Elimináció:</b> az első egyenlet segítségével kiejtjük az első ismeretlent '
  '(általában $x$-et) a második és a harmadik egyenletből, majd a második egyenlettel a '
  'következőt a harmadikból — ez a <b>lépcsős alak</b>. Ha a kiejtéshez használt egyenletből '
  'éppen hiányzik az adott ismeretlen, előbb cseréljünk sort.</li>'
  '<li><b>Visszahelyettesítés:</b> alulról fölfelé, $z\\ \\to\\ y\\ \\to\\ x$.</li></ol>'
  '<p><b>Rendezett írásmód:</b> a lépéseket egymás alá, a sorműveletet a sor mellé írjuk. '
  'A sorművelet a <b>jobb oldalra</b> is vonatkozik, és a hiányzó ismeretlen '
  '<b>együtthatója $0$</b> (a táblázatba nullát írunk, nem üres helyet). Ha egy egyenlet minden '
  'együtthatója és a jobb oldala is osztható ugyanazzal a számmal, előbb egyszerűsítsünk.</p>',
 ]),

 ("Hány megoldás van?", [
  '<table class="tt-table">'
  '<tr><th>A rendszer</th><th>Megoldásainak száma</th><th>A lépcsős alakban</th></tr>'
  '<tr><td><b>határozott</b></td><td>pontosan egy</td><td>nem keletkezik sem $0=0$, sem $0=k$ sor</td></tr>'
  '<tr><td><b>határozatlan</b></td><td>végtelen sok</td>'
  '<td>$0=0$ sor keletkezik, és nincs $0=k$ sor</td></tr>'
  '<tr><td><b>ellentmondásos</b></td><td>nincs</td><td>$0=k$ sor keletkezik, ahol $k\\ne0$</td></tr>'
  '</table>'
  '<p class="cap">A táblázat az olyan rendszerekre vonatkozik, amelyekben ugyanannyi egyenlet '
  'van, ahány ismeretlen — nálunk mindig ez a helyzet.</p>'
  '<p>A $0=0$ <b>mindig igaz</b>, ezért nem szűkít semmit: a sor elhagyható. A $0=k$ '
  '($k\\ne0$) <b>soha nem igaz</b>: a rendszer ellentmondásos, és itt meg is állhatunk '
  '(' + h(MS, "tetel-felismeres") + '). A válaszhoz az indoklás is hozzátartozik: melyik '
  'sorművelet után lett $0=0$ vagy $0=k$.</p>'
  '<p><b>A határozatlan rendszer megoldásai:</b> az az ismeretlen lesz <b>szabad</b> '
  '(jelöljük $t$-vel), amelyiknek az értéke a lépcsős alakból nem jön ki egyértelműen — '
  'többnyire a $z$. A többi ismeretlent $t$-vel fejezzük ki, például '
  '$(x;y;z)=(2t-3;\\ 5-3t;\\ t)$, ahol $t$ tetszőleges valós szám. Ha a lépcsős alakban csak '
  '<b>egyetlen</b> nem nulla sor marad, két ismeretlen is szabad.</p>'
  '<p><b>Három ismeretlen, három sík:</b> a rendszer megoldása a három sík közös pontjainak '
  'halmaza — egy pont (határozott), egy egyenes vagy egy sík (határozatlan), vagy üres '
  '(ellentmondásos).</p>',
  abra(SVG_HAROM_SIK, 'Egy-egy példa a három esetre: balra a három sík egyetlen pontban '
       'találkozik, középen egy közös egyenesen megy át, jobbra a három metszésvonal különböző és '
       'párhuzamos. (Ellentmondásos a rendszer akkor is, ha két sík párhuzamos.)'),
 ]),

 ("A determináns", [
  '<p><b>Másodrendű</b> (' + h(DE, "def-determinans") + '): a főátló szorzatából kivonjuk a '
  'mellékátlóét:</p>'
  '$$\\begin{vmatrix}a&b\\\\ c&d\\end{vmatrix}=ad-bc,\\qquad\\text{például}\\quad '
  '\\begin{vmatrix}2&1\\\\ 3&4\\end{vmatrix}=8-3=5.$$'
  '<p><b>Harmadrendű, Sarrus-szabály</b> (' + h(DE, "tetel-sarrus") + '): a determináns mellé '
  'újra leírjuk az első két oszlopot; a három <b>lefelé</b> haladó átló szorzatainak összegéből '
  'kivonjuk a három <b>fölfelé</b> haladóét. Kizárólag $3\\times3$-as determinánsra érvényes.</p>',
  abra(SVG_SARRUS, 'A Sarrus-séma: a zöld átlók szorzatai pozitív, a pirosaké negatív előjellel '
       'adódnak hozzá.'),
  '<p><b>Kifejtés sor vagy oszlop szerint</b> (' + h(DE, "tetel-kifejtes") + '): a kiválasztott '
  'sor (oszlop) <b>mindhárom elemét</b> megszorozzuk azzal a másodrendű '
  '<b>aldeterminánssal</b>, amely az elem sorának és oszlopának elhagyása után marad, és a '
  'szorzatokat a sakktábla-előjelek szerint összeadjuk:</p>'
  '$$\\begin{matrix}+&-&+\\\\ -&+&-\\\\ +&-&+\\end{matrix}$$'
  '<p>Azt a sort vagy oszlopot válasszuk, amelyikben a <b>legtöbb nulla</b> van.</p>'
  '<p><b>Mikor nulla a determináns</b> (' + h(DE, "tetel-tulajdonsagok") + ')? Ha valamelyik '
  'sora (oszlopa) csupa nulla; ha van két egyenlő vagy arányos sora (oszlopa); vagy ha egy sora '
  '(oszlopa) a többi sor (oszlop) számszorosainak összege.</p>'
  '<table class="tt-table">'
  '<tr><th>Lépés</th><th>A determináns</th></tr>'
  '<tr><td>két sor (oszlop) cseréje</td><td><b>előjelet vált</b></td></tr>'
  '<tr><td>egy sor szorzása $k$-val</td><td>$k$-szorosára <b>változik</b></td></tr>'
  '<tr><td>egy sorhoz egy másik sor számszorosának hozzáadása</td><td><b>nem változik</b></td></tr>'
  '</table>'
  '<p>⚠️ A Gauss-eljárásban a sorcsere és a sor szorzása ártalmatlan — a determinánsnál nem.</p>',
 ]),

 ("A Cramer-szabály", [
  '<p><b>Előbb rendezzünk:</b> minden egyenlet $ax+by+cz=d$ alakú legyen, az ismeretlenek '
  'mindenhol ugyanabban a sorrendben.</p>'
  '<p><b>A determinánsok:</b> $D$ az együtthatókból áll; a $D_x$, $D_y$, $D_z$ '
  'determinánsban az adott ismeretlen <b>oszlopa helyére</b> a jobb oldalak oszlopa kerül — '
  '$D_y$-nál tehát a <b>második</b> oszlop helyére. (Három ismeretlennél négy, kettőnél három '
  'determináns kell.)</p>'
  '<p><b>A szabály</b> (' + h(CR, "tetel-cramer") + '): egy $n$ egyenletből álló, $n$ '
  'ismeretlenes rendszer <b>akkor és csak akkor</b> határozott, ha $D\\ne0$, és ekkor</p>'
  '$$x=\\frac{D_x}{D},\\qquad y=\\frac{D_y}{D},\\qquad z=\\frac{D_z}{D}.$$'
  '<p>Példa: a $2x+y=5$, $x-y=1$ rendszernél $D=-3$, $D_x=-6$ és $D_y=-3$, így a megoldás '
  '$(x;y)=(2;1)$.</p>'
  '<p>⛔ <b>A korlát</b> (' + h(CR, "tetel-cramer-korlat") + '): ha $D=0$, a szabály '
  '<b>nem alkalmazható</b>. A rendszer ilyenkor határozatlan <b>vagy</b> ellentmondásos — '
  'hogy melyik, azt a Gauss-eljárás dönti el. A $D=0$ nem azt jelenti, hogy „nincs megoldás”, '
  'hanem hogy nincs <b>pontosan egy</b>.</p>'
  '<table class="tt-table">'
  '<tr><th></th><th>Cramer-szabály</th><th>Gauss-eljárás</th></tr>'
  '<tr><td><b>Mikor működik</b></td><td>csak ha $D\\ne0$</td><td>mindig</td></tr>'
  '<tr><td><b>Mit ad</b></td><td>a megoldást, képlettel</td>'
  '<td>a megoldást <b>és</b> a megoldások számát</td></tr>'
  '<tr><td><b>Mikor gyors</b></td><td>ha csak <b>egy</b> ismeretlen kell</td>'
  '<td>ha az együtthatók között sok az $1$ és a $0$</td></tr>'
  '</table>',
 ]),

 ("Szövegből rendszer", [
  '<p><b>A négy lépés</b> (' + h(SZ, "tetel-negy-lepes") + '):</p>'
  '<ol><li><b>Mi az ismeretlen?</b> Írd le szavakkal is, mértékegységgel: „legyen $x$ egy toll '
  'ára dinárban”.</li>'
  '<li>Az adatokat közlő <b>mondatokból</b> lesznek az egyenletek — annyi egyenlet kell, ahány '
  'ismeretlen, és egyik se következzen a többiből.</li>'
  '<li><b>Oldd meg</b> a rendszert a legkényelmesebb módszerrel.</li>'
  '<li><b>Ellenőrizz a szöveggel</b> (ésszerű-e: pozitív-e a darabszám, számjegy-e a '
  'számjegy), és olvasd vissza a kérdést: arra válaszolj, amit kérdeztek.</li></ol>'
  '<table class="tt-table">'
  '<tr><th>Típus</th><th>Az ismeretlenek</th><th>Az egyenletek forrása</th></tr>'
  '<tr><td><b>mennyiség — egységár — összérték</b></td><td>az egységárak</td>'
  '<td>minden vásárlás egy egyenlet: $\\text{darab}\\cdot\\text{ár}$ tagok összege</td></tr>'
  '<tr><td><b>sebesség — idő — út</b></td><td>a sebességek</td>'
  '<td>minden szakaszra $s=v\\cdot t$; folyón lefelé $v+v_f$, fölfelé $v-v_f$</td></tr>'
  '<tr><td><b>keverés</b></td><td>a keverendő mennyiségek</td>'
  '<td>egy egyenlet az össztömegre, egy a hatóanyagra</td></tr>'
  '<tr><td><b>életkorok</b></td><td>a mai életkorok</td>'
  '<td>„$n$ év múlva” minden életkorhoz $+n$, „$n$ évvel ezelőtt” $-n$</td></tr>'
  '<tr><td><b>számjegyek</b></td><td>a számjegyek</td>'
  '<td>kétjegyű szám: $10a+b$ (felcserélve $10b+a$); háromjegyű: $100a+10b+c$</td></tr>'
  '</table>'
  '<p>⚠️ <b>Az arány iránya:</b> ha $y$ a közepes, $z$ a nagy darabok száma, akkor a „közepesből '
  'kétszer annyi van, mint nagyból” mondat $y=2z$, nem $2y=z$. Ha bizonytalan vagy, próbáld ki '
  'számokkal.</p>',
 ]),

 ("A nyolc leggyakoribb hiba", [
  '<div class="brief"><p>🚨 <b>1)</b> A megoldás egyetlen szám — pedig számpár vagy számhármas '
  'kell, és minden egyenletbe vissza kell helyettesíteni. &nbsp; <b>2)</b> Egy egyenletet '
  '<b>nullával</b> szoroznak, vagy két egyenletet <b>összeszoroznak</b> — egyik sem ekvivalens '
  'lépés. &nbsp; <b>3)</b> A sorműveletnél elmarad a <b>jobb oldal</b>, vagy a hiányzó '
  'ismeretlen együtthatója helyére nem $0$ kerül. &nbsp; <b>4)</b> A $0=0$ sort „nincs '
  'megoldás”-nak olvassák — fordítva van: a $0=0$ sor elhagyható, és ha nincs $0=k$ sor, '
  '<b>végtelen sok</b> megoldást jelez; a $0=k$ jelzi az ellentmondást. &nbsp; <b>5)</b> A '
  'Sarrus-szabályt $4\\times4$-es determinánsra is alkalmazzák, a kifejtésnél elhagyják az '
  '<b>előjelet</b>, vagy elfelejtik, hogy a <b>sorcsere</b> előjelet vált. &nbsp; <b>6)</b> '
  '$D=0$ mellett „$\\frac{0}{0}=1$” — nullával nem osztunk, a $\\frac{0}{0}$ nem szám, a '
  'Cramer-szabály ilyenkor nem alkalmazható. &nbsp; <b>7)</b> A helyettesítési determinánsban '
  '<b>rossz oszlopot</b> cserélnek: $D_y$-nál a második oszlop helyére kerül a jobb oldalak '
  'oszlopa. &nbsp; <b>8)</b> A szöveges feladatnál nem a <b>kérdésre</b> válaszolnak: ha $x$ egy '
  'toll, $y$ egy füzet ára, és két toll meg három füzet együttes ára a kérdés, akkor a válasz '
  '$2x+3y$, nem $x$.</p></div>',
 ]),

 ("Mit hol találsz?", [
  '<div class="brief"><p>📚 <b>Tananyag:</b> '
  '<a href="' + KI + '">két egyenlet, két ismeretlen</a> · '
  '<a href="' + GA + '">a Gauss-eljárás</a> · '
  '<a href="' + MS + '">hány megoldás van?</a> · '
  '<a href="' + DE + '">a determináns</a> · '
  '<a href="' + CR + '">a Cramer-szabály</a> · '
  '<a href="' + SZ + '">szövegből rendszer</a>.</p>'
  '<p>🎯 <b>Gyakorlás:</b> '
  '<a href="feladatok-rendszerek.html">egyenletrendszerek</a> · '
  '<a href="feladatok-determinans.html">a determináns és a Cramer-szabály</a> — majd indulj '
  'a <a href="terepkuldetes.html">Rendszer Hibájának</a> felderítésére!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Töréspont-térkép — a témakör egy lapon",
    cim_tiszta="Töréspont-térkép", itt="Töréspont-térkép",
    alcim="A lineáris egyenletrendszerek minden definíciója, eljárása és tipikus csapdája egy "
          "helyen — ismétléshez, ellenőrző előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-determinans.html", "Feladatok — a determináns és a Cramer-szabály"),
    kovetkezo=("terepkuldetes.html", "A Rendszer Hibája"))
print("✓ osszefoglalo.html")
