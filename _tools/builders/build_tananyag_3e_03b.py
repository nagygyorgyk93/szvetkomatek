# -*- coding: utf-8 -*-
"""3e/03 — B altema: a determinans (B1) es a Cramer-szabaly (B2).
Mentor: Kanrak. Kuldetes: A Rendszer Hibaja."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_sarrus

T = dict(tagozat="3e", mappa="03-linearis-rendszerek", temakor="Lineáris egyenletrendszerek")
FGY = "feladatok-determinans.html"
KUL = "A Rendszer Hibája"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Matrix, symbols, Eq, solve, simplify, N, Rational
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x, y, z = symbols("x y z")

# B1 — masodrendu determinans
chk("B1-masodrendu", Matrix([[3, 2], [1, -4]]).det(), -14)
chk("B1-kepletbol", 3*(-4) - 2*1, -14)
# a 2x2-es rendszer kikuszobolese: (ad - bc) x = ed - bf
a, b, c, d, e, f = symbols("a b c d e f")
chk("B1-levezetes", simplify(d*(a*x + b*y - e) - b*(c*x + d*y - f)),
    (a*d - b*c)*x - (e*d - b*f))
# B1 — a fo pelda determinansa
M = Matrix([[2, -1, 3], [1, 4, -2], [3, 0, 5]])
chk("B1-D", M.det(), 15)
# Sarrus: harom lefele (+) es harom folfele (-) atlo
chk("B1-sarrus-plusz", 2*4*5 + (-1)*(-2)*3 + 3*1*0, 46)
chk("B1-sarrus-minusz", 3*4*3 + 2*(-2)*0 + (-1)*1*5, 31)
chk("B1-sarrus", 46 - 31, 15)
# kifejtes a harmadik sor szerint (ott van a nulla)
chk("B1-kifejtes-1", Matrix([[-1, 3], [4, -2]]).det(), -10)
chk("B1-kifejtes-2", Matrix([[2, -1], [1, 4]]).det(), 9)
chk("B1-kifejtes", 3*(-10) - 0 + 5*9, 15)
# B1 — kifejtes oszlop szerint, sok nullaval
M2 = Matrix([[2, 0, 1], [3, -1, 4], [5, 0, 2]])
chk("B1-M2", M2.det(), 1)
chk("B1-M2-kifejtes", -1*Matrix([[2, 1], [5, 2]]).det(), 1)
chk("B1-M2-sarrus", (2*(-1)*2 + 0*4*5 + 1*3*0) - (1*(-1)*5 + 2*4*0 + 0*3*2), 1)
# B1 — tulajdonsagok
chk("B1-nullsor", Matrix([[1, 2, 3], [0, 0, 0], [4, 5, 6]]).det(), 0)
chk("B1-aranyos", Matrix([[1, 2, 3], [2, 4, 6], [5, 0, 1]]).det(), 0)
chk("B1-sorcsere", Matrix([[1, 4, -2], [2, -1, 3], [3, 0, 5]]).det(), -15)
chk("B1-egyenlo-sor", Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3]]).det(), 0)

# B2 — Cramer: ugyanaz az egyutthato-matrix, jobb oldal (6; 4; 11)
J = Matrix([6, 4, 11])
D = M.det()
Dx = M.copy(); Dx[:, 0] = J
Dy = M.copy(); Dy[:, 1] = J
Dz = M.copy(); Dz[:, 2] = J
chk("B2-Dx-kifejtes-1", Matrix([[-1, 3], [4, -2]]).det(), -10)
chk("B2-Dx-kifejtes-2", Matrix([[6, -1], [4, 4]]).det(), 28)
chk("B2-Dx-kifejtes", 11*(-10) + 5*28, 30)
chk("B2-D", D, 15)
chk("B2-Dx", Dx.det(), 30); chk("B2-Dy", Dy.det(), 15); chk("B2-Dz", Dz.det(), 15)
chk("B2-x", Rational(Dx.det(), D), 2)
chk("B2-y", Rational(Dy.det(), D), 1)
chk("B2-z", Rational(Dz.det(), D), 1)
mo = solve([Eq(2*x - y + 3*z, 6), Eq(x + 4*y - 2*z, 4), Eq(3*x + 5*z, 11)], [x, y, z], dict=True)[0]
chk("B2-ell-x", mo[x], 2); chk("B2-ell-y", mo[y], 1); chk("B2-ell-z", mo[z], 1)
chk("B2-behely-1", 2*2 - 1 + 3*1, 6)
chk("B2-behely-2", 2 + 4*1 - 2*1, 4)
chk("B2-behely-3", 3*2 + 5*1, 11)
# B2 — D = 0 eset (ugyanaz a rendszer, mint az A3-ban)
N0 = Matrix([[1, 1, 1], [2, 1, -1], [3, 2, 0]])
chk("B2-D-nulla", N0.det(), 0)
J0 = Matrix([6, 1, 7])
D0x = N0.copy(); D0x[:, 0] = J0
chk("B2-D-nulla-Dx", D0x.det(), 0)
J1 = Matrix([6, 1, 10])
D1x = N0.copy(); D1x[:, 0] = J1
chk("B2-ellentmondas-Dx", D1x.det(), -6)
assert solve([Eq(x + y + z, 6), Eq(2*x + y - z, 1), Eq(3*x + 2*y, 10)], [x, y, z]) == []

assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_SARRUS = svg_sarrus(((2, -1, 3), (1, 4, -2), (3, 0, 5)), w=470, h=250,
                        leiras="A 2, −1, 3 / 1, 4, −2 / 3, 0, 5 determináns Sarrus-sémája: "
                               "az első két oszlop megismételve, a hat átló nyíllal")
SVG_SARRUS_ALT = svg_sarrus((("a<tspan baseline-shift='sub' font-size='10'>11</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>12</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>13</tspan>"),
                             ("a<tspan baseline-shift='sub' font-size='10'>21</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>22</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>23</tspan>"),
                             ("a<tspan baseline-shift='sub' font-size='10'>31</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>32</tspan>",
                              "a<tspan baseline-shift='sub' font-size='10'>33</tspan>")),
                            w=470, h=250,
                            leiras="A Sarrus-séma általánosan, az elemek jelölésével")

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> A determináns egyetlen <b>szám</b>, amelyet egy négyzetes '
         'táblázatból számolunk ki — és ez az egy szám előre megmondja, hogy a rendszernek '
         'van-e egyértelmű megoldása. Nem varázslat és nem új matematika: a kiküszöbölés '
         'menete van belesűrítve.'),
   '<p>A determináns — és a rá épülő Cramer-szabály — olyan <b>eszköz</b>, amelyhez az új '
   'szabványban <b>nem tartozik önálló kimenet</b>: nem önmagáért tanuljuk, hanem azért, '
   'mert a rendszerek megoldását szolgálja. Ezért végig azzal a kérdéssel a fejünkben '
   'használjuk, hogy <i>mit mond a rendszerről</i>.</p>',
 ]),

 ("A másodrendű determináns", [
   doboz("definicio", "Másodrendű determináns",
         r'<p>Egy $2\times2$-es számtáblázat determinánsa:</p>'
         r'$$\begin{vmatrix}a&b\\ c&d\end{vmatrix}=ad-bc.$$'
         r'<p>A jelölés <b>két függőleges vonal</b> (nem zárójel!). A számítás menete: '
         r'a <b>főátló</b> ($a$ és $d$) szorzatából kivonjuk a <b>mellékátló</b> ($b$ és '
         r'$c$) szorzatát.</p>',
         hid="def-determinans"),
   r'<p>Például $\begin{vmatrix}3&2\\ 1&-4\end{vmatrix}=3\cdot(-4)-2\cdot1=-12-2=-14$. '
   r'A determináns értéke lehet negatív is — nem terület, hanem <b>előjeles</b> mennyiség.</p>',
   doboz("tetel", "Honnan jön ez a képlet?",
         r'<p>Oldjuk meg általánosan a</p>'
         r'$$\begin{aligned}ax+by&=e\\ cx+dy&=f\end{aligned}$$'
         r'<p>rendszert kiküszöböléssel. Szorozzuk az első egyenletet $d$-vel, a másodikat '
         r'$b$-vel, majd vonjuk ki őket egymásból:</p>'
         r'$$(ad-bc)\,x=ed-bf.$$'
         r'<p>Az $x$ együtthatója pontosan a determináns. Ha $ad-bc\ne0$, oszthatunk vele, '
         r'és $x$-re <b>egyetlen</b> érték adódik. Ha viszont $ad-bc=0$, nem oszthatunk — '
         r'és épp ez a nem határozott eset.</p>'
         r'<p>A determináns tehát nem a semmiből jött: ez az a szám, amellyel a '
         r'kiküszöbölés végén osztani szeretnénk.</p>',
         hid="tetel-honnan"),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A $2\times2$-es determináns abszolút értéke annak a <b>paralelogrammának a '
         r'területe</b>, amelyet a táblázat két oszlopa mint vektor kifeszít; a '
         r'$3\times3$-asé pedig a három oszlopvektor által kifeszített <b>paralelepipedon '
         r'térfogata</b>.</p>'
         r'<p>Innen érthető, hogy miért jelent gondot a $0$: ha a determináns nulla, az '
         r'irányok „összelapultak” — a paralelogramma egyenessé, a test lappá zsugorodott. '
         r'Ilyenkor az irányok nem függetlenek, és a rendszernek nincs egyértelmű '
         r'megoldása. Ez a szemlélet a <b>04. témakörben</b>, a vektoriális szorzatnál tér '
         r'majd vissza.</p>'),
 ]),

 ("A harmadrendű determináns — a Sarrus-szabály", [
   doboz("tetel", "Sarrus-szabály",
         r'<p>Írjuk a $3\times3$-as determináns mellé <b>újra az első két oszlopát</b>. '
         r'Ekkor hat átló keletkezik: három <b>lefelé</b> haladó (balról jobbra lefelé) és '
         r'három <b>fölfelé</b> haladó. A determináns a lefelé haladó átlók szorzatainak '
         r'összege <b>mínusz</b> a fölfelé haladó átlók szorzatainak összege:</p>'
         r'$$\begin{vmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ '
         r'a_{31}&a_{32}&a_{33}\end{vmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}'
         r'+a_{13}a_{21}a_{32}-a_{31}a_{22}a_{13}-a_{32}a_{23}a_{11}-a_{33}a_{21}a_{12}.$$'
         r'<p>A képletet <b>nem kell</b> megjegyezni — az ábrát kell.</p>',
         hid="tetel-sarrus"),
   abra(SVG_SARRUS_ALT, 'A Sarrus-séma általánosan: a szürke sávban a megismételt első két '
        'oszlop áll. A <b>zöld</b> (lefelé haladó) átlók szorzatait összeadjuk, a '
        '<b>piros</b> (fölfelé haladó) átlókét kivonjuk.'),
   doboz("pelda", "Kristály-kamra szimuláció — Sarrus a gyakorlatban",
         r'<p>Számítsuk ki a</p>'
         r'$$D=\begin{vmatrix}2&-1&3\\ 1&4&-2\\ 3&0&5\end{vmatrix}$$'
         r'<p>determinánst. Írjuk mellé az első két oszlopot:</p>'
         + abra(SVG_SARRUS, 'A konkrét determináns Sarrus-sémája.') +
         r'<p><b>A lefelé haladó átlók (+):</b></p>'
         r'$$2\cdot4\cdot5+(-1)\cdot(-2)\cdot3+3\cdot1\cdot0=40+6+0=46.$$'
         r'<p><b>A fölfelé haladó átlók (−):</b></p>'
         r'$$3\cdot4\cdot3+0\cdot(-2)\cdot2+5\cdot1\cdot(-1)=36+0-5=31.$$'
         r'<p>Most vond ki a második összeget az elsőből — ez a determináns értéke.</p>',
         hid="pelda-sarrus",
         lenyilo=("Végeredmény",
                  '<p>$46-31=15$.</p>'
                  '<p class="vegeredmeny">$D=15$.</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„A Sarrus-szabály jó — akkor négy sorra is felírom.”</i></p>'
         r'<p><b>Nem működik.</b> A Sarrus-szabály <b>kizárólag $3\times3$-as</b> '
         r'determinánsra érvényes. Négyedrendű determinánsnál az „átlós” eljárás nem a '
         r'helyes értéket adja (ott $24$ tagra volna szükség, nem $8$-ra) — a $4\times4$-es '
         r'determinánst kifejtéssel kell számolni, és az már nem a mi tananyagunk.</p>'
         r'<p>A másik gyakori hiba az <b>előjelek elkeverése</b>. Segít, ha mindig ugyanúgy '
         r'rajzolod meg a sémát: előbb az <b>összes</b> zöld átlót, összeadod őket, aztán az '
         r'<b>összes</b> pirosat, és csak a végén vonod ki a második összeget az elsőből. Aki '
         r'tagonként váltogatja az előjelet, az előbb-utóbb eltéveszti.</p>'),
   kviz(r'Mennyi $\begin{vmatrix}1&2\\ 3&4\end{vmatrix}$ értéke?',
        ['$-2$', '$2$', '$10$', '$-10$'], 0,
        jo="✔ 1 · 4 − 2 · 3 = 4 − 6 = −2.",
        nem="✘ A főátló szorzatából vonjuk ki a mellékátlóét: 1 · 4 − 2 · 3 = −2. "
            "(Aki 10-et kapott, összeadta a két szorzatot.)"),
 ]),

 ("Kifejtés sor vagy oszlop szerint", [
   r'<p>A Sarrus-szabály gyors, de csak $3\times3$-ra jó, és sokat kell szorozni. A '
   r'<b>kifejtés</b> más úton jut ugyanoda: a harmadrendű determinánst három '
   r'<b>másodrendűre</b> vezeti vissza.</p>',
   doboz("tetel", "Kifejtés sor, illetve oszlop szerint",
         r'<p>Válasszunk ki egy tetszőleges sort vagy oszlopot. Minden eleméhez tartozik '
         r'egy <b>aldetermináns</b>: az a másodrendű determináns, amely az elem sorának és '
         r'oszlopának <b>elhagyása</b> után marad. A determináns értéke az elemek és a '
         r'hozzájuk tartozó aldeterminánsok szorzatainak <b>előjeles</b> összege.</p>'
         r'<p>Az előjelek sakktáblaszerűen váltakoznak:</p>'
         r'$$\begin{matrix}+&-&+\\ -&+&-\\ +&-&+\end{matrix}$$'
         r'<p>A bal felső sarokban $+$ áll, és onnan minden <b>vízszintes vagy '
         r'függőleges</b> lépéssel vált az előjel; átlósan lépve nem változik.</p>'
         r'<p><b>Melyik sort vagy oszlopot válasszuk?</b> Amelyikben a legtöbb <b>nulla</b> '
         r'van: a nulla '
         r'elemhez tartozó tagot ki sem kell számolni.</p>',
         hid="tetel-kifejtes"),
   doboz("pelda", "Kristály-kamra szimuláció — ugyanaz a determináns kifejtéssel",
         r'<p>Fejtsük ki a fenti $D$ determinánst a <b>harmadik sora</b> szerint — itt van '
         r'ugyanis nulla:</p>'
         r'$$D=\begin{vmatrix}2&-1&3\\ 1&4&-2\\ 3&0&5\end{vmatrix}$$'
         r'<p>A harmadik sor előjelei $+\,-\,+$, az elemei pedig $3$, $0$, $5$:</p>'
         r'$$D=+3\cdot\begin{vmatrix}-1&3\\ 4&-2\end{vmatrix}'
         r'-0\cdot\begin{vmatrix}2&3\\ 1&-2\end{vmatrix}'
         r'+5\cdot\begin{vmatrix}2&-1\\ 1&4\end{vmatrix}.$$'
         r'<p>Az aldeterminánsok: $(-1)\cdot(-2)-3\cdot4=2-12=-10$, illetve '
         r'$2\cdot4-(-1)\cdot1=8+1=9$. A középső tag nulla, mert $0$-val szorozzuk. Tehát</p>'
         r'<p>Add össze a két tagot — és vesd össze a Sarrus-szabállyal kapott '
         r'értékkel.</p>',
         hid="pelda-ketfele",
         lenyilo=("Végeredmény",
                  r'<p>$D=3\cdot(-10)+5\cdot9=-30+45=15$ — ugyanaz az érték, mint a '
                  r'Sarrus-szabállyal.</p>'
                  '<p class="vegeredmeny">$D=15$ mindkét módszerrel.</p>')),
   r'<p>A két módszer viszonya egyszerű: ha a determinánsban <b>nincs</b> nulla, a '
   r'Sarrus-szabály általában gyorsabb; ha van benne nulla — különösen kettő egy sorban —, a kifejtés '
   r'lényegesen kevesebb munka. A dolgozatban <b>mindkettő</b> elfogadható, ha a lépések '
   r'követhetők.</p>',
 ]),

 ("Tulajdonságok, amelyek időt takarítanak meg", [
   '<p>Mielőtt bármit kiszámolnál, érdemes ránézni a determinánsra. Néha ugyanis a '
   'végeredmény azonnal látszik.</p>',
   doboz("tetel", "Négy tulajdonság, amit érdemes fejből tudni",
         '<p>A determináns értéke <b>nulla</b>, ha</p>'
         '<ul>'
         '<li>valamelyik <b>sora vagy oszlopa csupa nulla</b>;</li>'
         '<li>van két <b>egyenlő</b> sora (vagy oszlopa);</li>'
         '<li>van két <b>arányos</b> sora (vagy oszlopa) — azaz az egyik a másik '
         'számszorosa;</li>'
         '<li>valamelyik sora (vagy oszlopa) a másik kettőből <b>összeadással és '
         'számmal szorzással</b> előáll — például az egyik sor a másik kettő összege.</li>'
         '</ul>'
         '<p>Egy negyedik, számolást könnyítő tulajdonság: két sor (vagy oszlop) '
         '<b>felcserélése</b> a determináns <b>előjelét megfordítja</b>, az abszolút '
         'értékét nem változtatja.</p>',
         hid="tetel-tulajdonsagok"),
   r'<p>Például $\begin{vmatrix}1&2&3\\ 2&4&6\\ 5&0&1\end{vmatrix}=0$, mert a második sor '
   r'az első kétszerese — nem kell számolni. Ha viszont a fenti $D$ determinánsban '
   r'felcseréljük az első két sort, az érték $15$ helyett $-15$ lesz.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„A sorcsere nem számít, hiszen ugyanazok a számok maradnak.”</i></p>'
         '<p><b>Számít.</b> A sorcsere <b>előjelet vált</b>. Ez az egyik legmakacsabb hiba, '
         'mert a Gauss-eljárásban a sorcsere teljesen ártalmatlan (ott a megoldás nem '
         'változik tőle) — a determinánsnál viszont nem az.</p>'
         '<p>Érdemes összeszedni, melyik lépés mit csinál a determinánssal:</p>'
         '<table class="tt-table">'
         '<tr><th>Lépés</th><th>A determináns</th></tr>'
         '<tr><td>két sor cseréje</td><td><b>előjelet vált</b></td></tr>'
         '<tr><td>egy sor szorzása $k$-val</td><td>$k$-szorosára <b>változik</b> '
         '(felére, ha $k=\\tfrac12$; előjelet is vált, ha $k<0$)</td></tr>'
         '<tr><td>egy sorhoz egy másik sor számszorosának hozzáadása</td>'
         '<td><b>nem változik</b></td></tr>'
         '</table>'
         '<p>A harmadik sor a legmeglepőbb — és épp ez teszi lehetővé, hogy a determinánst '
         'a Gauss-eljárás lépéseivel nullákkal teli alakra hozzuk, mielőtt kifejtenénk.</p>'),
   kviz(r'Egy harmadrendű determináns értéke $12$. Mennyi lesz, ha felcseréljük az első és '
        r'a második sorát?',
        ['$-12$', '$12$', '$24$', '$0$'], 0,
        jo="✔ Egyetlen sorcsere megfordítja a determináns előjelét: 12 helyett −12.",
        nem="✘ A sorcsere nem hagyja változatlanul a determinánst: ELŐJELET VÁLT. "
            "Az érték tehát −12."),
   GY(FGY + "#alap-1", "A 1–8", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Kanrak:</b> Megvan a szám, amely eldönti a kérdést. De egy jó eszköz többet '
         'tud annál, hogy igent vagy nemet mond: ha a determináns nem nulla, a megoldás '
         '<b>képlettel</b> is felírható. Három osztás, és kész — feltéve, hogy nem ugrod át '
         'a feltételt.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
CSERE_TABLA = (
 '<table class="tt-table">'
 '<tr><th>Determináns</th><th>Az 1. oszlop</th><th>A 2. oszlop</th><th>A 3. oszlop</th></tr>'
 '<tr><td>$D$</td><td>$x$ együtthatói</td><td>$y$ együtthatói</td><td>$z$ együtthatói</td></tr>'
 '<tr><td>$D_x$</td><td><b>a jobb oldal</b></td><td>$y$ együtthatói</td>'
 '<td>$z$ együtthatói</td></tr>'
 '<tr><td>$D_y$</td><td>$x$ együtthatói</td><td><b>a jobb oldal</b></td>'
 '<td>$z$ együtthatói</td></tr>'
 '<tr><td>$D_z$</td><td>$x$ együtthatói</td><td>$y$ együtthatói</td>'
 '<td><b>a jobb oldal</b></td></tr>'
 '</table>')

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Ha a determináns nem nulla, a megoldás <b>képlettel</b> felírható: '
         'négy determináns, három osztás, és kész. De van egy feltétel — és aki azt '
         'átugorja, az a legrosszabb fajta hibát követi el: <b>magabiztosan</b> ad rossz '
         'választ.'),
   '<p>A Cramer-szabály nem helyettesíti a Gauss-eljárást, hanem <b>kiegészíti</b>. Az '
   'óra végére azt is el kell tudnod dönteni, melyiket mikor érdemes elővenni.</p>',
 ]),

 ("A négy determináns", [
   r'<p>Induljunk ki egy háromismeretlenes rendszerből:</p>'
   r'$$\begin{aligned}a_{11}x+a_{12}y+a_{13}z&=b_1\\ a_{21}x+a_{22}y+a_{23}z&=b_2\\ '
   r'a_{31}x+a_{32}y+a_{33}z&=b_3\end{aligned}$$'
   r'<p>A rendszer <b>fő determinánsa</b> ($D$) az együtthatók determinánsa. A három '
   r'<b>helyettesítési determinánst</b> úgy kapjuk, hogy $D$-ben a keresett ismeretlen '
   r'<b>oszlopát</b> kicseréljük a jobb oldalak oszlopára:</p>'
   r'$$D=\begin{vmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ '
   r'a_{31}&a_{32}&a_{33}\end{vmatrix},\qquad '
   r'D_x=\begin{vmatrix}b_1&a_{12}&a_{13}\\ b_2&a_{22}&a_{23}\\ '
   r'b_3&a_{32}&a_{33}\end{vmatrix},$$'
   r'$$D_y=\begin{vmatrix}a_{11}&b_1&a_{13}\\ a_{21}&b_2&a_{23}\\ '
   r'a_{31}&b_3&a_{33}\end{vmatrix},\qquad '
   r'D_z=\begin{vmatrix}a_{11}&a_{12}&b_1\\ a_{21}&a_{22}&b_2\\ '
   r'a_{31}&a_{32}&b_3\end{vmatrix}.$$',
   CSERE_TABLA,
   '<p>Érdemes észrevenni a rendszert: <b>mindig ugyanaz a négy oszlop</b> szerepel, csak '
   'más-más helyen. A jobb oldal oszlopa oda kerül, amelyik ismeretlenre kíváncsiak '
   'vagyunk — az $x$-hez az elsőre, az $y$-hoz a másodikra, a $z$-hez a harmadikra.</p>',
   '<p>Fontos, hogy a rendszert előbb <b>rendezett alakra</b> hozzuk: minden egyenletben '
   'ugyanabban a sorrendben álljanak az ismeretlenek, a jobb oldalon pedig csak a '
   'konstans. Ha egy egyenletből hiányzik egy ismeretlen, oda <b>nulla</b> kerül a '
   'determinánsba.</p>',
   kviz(r'Hogyan áll elő a $D_y$ determináns?',
        [r'A $D$ <b>második</b> oszlopát cseréljük a jobb oldalak oszlopára',
         r'A $D$ <b>első</b> oszlopát cseréljük a jobb oldalak oszlopára',
         r'A $D$ <b>második sorát</b> cseréljük a jobb oldalak oszlopára',
         r'A $D$ értékét elosztjuk $y$-nal'], 0,
        jo="✔ Az y a második ismeretlen, ezért a második OSZLOP helyére kerül a jobb "
           "oldalak oszlopa.",
        nem="✘ Mindig annak az ismeretlennek az OSZLOPÁT cseréljük, amelyiket keressük — "
            "az y-nál tehát a másodikat. Sort soha nem cserélünk."),
 ]),

 ("A Cramer-szabály", [
   doboz("tetel", "Cramer-szabály",
         r'<p>Egy $n$ egyenletből álló, $n$ ismeretlenes rendszer <b>akkor és csak akkor</b> '
         r'határozott, ha a fő determinánsa nem nulla. Ha $D\ne0$, akkor tehát pontosan '
         r'egy megoldás van, és ez a megoldás:</p>'
         r'$$x=\frac{D_x}{D},\qquad y=\frac{D_y}{D},\qquad z=\frac{D_z}{D}.$$'
         r'<p>A $D\ne0$ feltétel <b>nem díszítés</b>: nélküle a képletnek nincs értelme, '
         r'hiszen nullával nem oszthatunk.</p>'
         r'<p>Kétismeretlenes rendszerre ugyanez érvényes, csak két determinánssal: '
         r'$x=\frac{D_x}{D}$ és $y=\frac{D_y}{D}$.</p>',
         hid="tetel-cramer"),
   doboz("pelda", "Kristály-kamra szimuláció — Cramer-szabály végig",
         r'<p>Oldjuk meg a</p>'
         r'$$\begin{aligned}2x-y+3z&=6\\ x+4y-2z&=4\\ 3x\phantom{{}+0y}+5z&=11\end{aligned}$$'
         r'<p>rendszert. A harmadik egyenletben nincs $y$, tehát ott az együttható $0$.</p>'
         r'<p><b>A fő determináns</b> (ezt már kiszámoltuk az előző órán):</p>'
         r'$$D=\begin{vmatrix}2&-1&3\\ 1&4&-2\\ 3&0&5\end{vmatrix}=15\ne0,$$'
         r'<p>tehát a Cramer-szabály <b>alkalmazható</b>, és a rendszer határozott.</p>'
         r'<p><b>A helyettesítési determinánsok.</b> A jobb oldalak oszlopa: $6$, $4$, $11$. '
         r'Számoljuk ki a $D_x$-et kifejtéssel — a harmadik sorában van egy nulla:</p>'
         r'$$D_x=\begin{vmatrix}6&-1&3\\ 4&4&-2\\ 11&0&5\end{vmatrix}=11\cdot\begin{vmatrix}-1&3\\ 4&-2\end{vmatrix}-0+5\cdot\begin{vmatrix}6&-1\\ 4&4\end{vmatrix}=11\cdot(-10)+5\cdot28=30.$$'
         r'<p>A másik kettő ugyanígy megy:</p>'
         r'$$D_y=\begin{vmatrix}2&6&3\\ 1&4&-2\\ 3&11&5\end{vmatrix}=15,\qquad '
         r'D_z=\begin{vmatrix}2&-1&6\\ 1&4&4\\ 3&0&11\end{vmatrix}=15.$$'
         r'<p>(A $D_y=D_z=D=15$ egybeesés véletlen — nem elírás.)</p>'
         r'<p><b>A megoldás:</b></p>'
         r'$$x=\frac{30}{15}=2,\qquad y=\frac{15}{15}=1,\qquad z=\frac{15}{15}=1.$$',
         hid="pelda-cramer",
         lenyilo=("Ellenőrzés és végeredmény",
                  r'<p>$2\cdot2-1+3\cdot1=6$ ✔ &nbsp;&nbsp; $2+4\cdot1-2\cdot1=4$ ✔ '
                  r'&nbsp;&nbsp; $3\cdot2+5\cdot1=11$ ✔</p>'
                  r'<p class="vegeredmeny">A rendszer megoldása: $(x;y;z)=(2;1;1)$.</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p><i>„$D=0$? Semmi baj: $x=\frac{D_x}{D}=\frac{0}{0}=1$.”</i></p>'
         r'<p><b>A nullával osztás nem művelet</b>, és a $\frac00$ nem $1$ — semmi. Ha '
         r'$D=0$, a Cramer-szabály nem „nehezebben használható”, hanem <b>érvénytelen</b>: '
         r'a képlet feltétele nem teljesül, tehát a képlet nem mond semmit.</p>'
         r'<p>És ha $D=0$, de $D_x$ történetesen <b>nem</b> nulla? Akkor a hányados alakja '
         r'$\frac{\text{nem nulla}}{0}$ — ez ugyanúgy értelmetlen. A $D=0$ tehát minden '
         r'esetben kizárja a szabály használatát, nem csak akkor, ha a helyettesítési '
         r'determinánsok is nullák.</p>'
         r'<p>A másik gyakori hiba: <b>rossz oszlopot</b> cserélnek. A $D_y$-nál a '
         r'<b>második</b> oszlop helyére kerül a jobb oldal — nem a második sor, és nem az '
         r'első oszlop. Aki a sémát egyszer rendesen felírja (lásd a fenti táblázatot), az '
         r'többé nem téveszti el.</p>'),
 ]),

 ("Mit jelent, ha a determináns nulla", [
   doboz("tetel", "A Cramer-szabály korlátja",
         r'<p>Ha $D=0$, a Cramer-szabály <b>nem alkalmazható</b>. Ilyenkor a rendszer '
         r'<b>nem határozott</b>: vagy <b>határozatlan</b> (végtelen sok megoldás), vagy '
         r'<b>ellentmondásos</b> (nincs megoldás) — de hogy melyik, azt a determinánsokból '
         r'<b>nem</b> lehet eldönteni. Ehhez a Gauss-eljárást kell elvégezni.</p>'
         r'<p>Vigyázat a megfogalmazásra: a $D=0$ nem azt jelenti, hogy „nincs megoldás”. '
         r'Azt jelenti, hogy <b>nincs pontosan egy</b> megoldás.</p>',
         hid="tetel-cramer-korlat"),
   doboz("pelda", "Kristály-kamra szimuláció — amikor $D=0$",
         r'<p>Vegyük a <b>megoldások számáról</b> szóló órán megismert rendszert:</p>'
         r'$$\begin{aligned}x+y+z&=6\\ 2x+y-z&=1\\ 3x+2y\phantom{{}+z}&=7\end{aligned}$$'
         r'<p>A fő determináns:</p>'
         r'$$D=\begin{vmatrix}1&1&1\\ 2&1&-1\\ 3&2&0\end{vmatrix}=0,$$'
         r'<p>hiszen a harmadik sor az első kettő összege (a megfelelő elemeket adva '
         r'össze: $1+2=3$, $1+1=2$, $1+(-1)=0$). A Cramer-szabály tehát <b>nem '
         r'használható</b>. A helyettesítési determinánsok kiszámítása sem vezet '
         r'megoldáshoz: $D_x$ is nulla, vagyis a képlet az értelmetlen $\frac00$ alakot '
         r'adná.</p>'
         r'<p>A Gauss-eljárás viszont válaszol: ahogyan a megoldások számáról szóló órán '
         r'láttuk, ez a rendszer '
         r'<b>határozatlan</b>, megoldásai $(2t-5;\;11-3t;\;t)$.</p>'
         r'<p>Ha a harmadik egyenlet jobb oldalán $7$ helyett $10$ állna, a fő determináns '
         r'ugyanúgy $0$ maradna (a bal oldal nem változott), a $D_x$ viszont $-6$ lenne '
         r'— és a rendszer, ahogyan azt ott a Gauss-eljárással láttuk, '
         r'<b>ellentmondásos</b>. Ugyanaz a $D=0$, két különböző eset: ezért nem '
         r'elég a determináns.</p>',
         hid="pelda-D-nulla",
         lenyilo=("Végeredmény",
                  r'<p class="vegeredmeny">$D=0$ — a Cramer-szabály nem alkalmazható; a '
                  r'Gauss-eljárás szerint a rendszer határozatlan.</p>')),
   kviz(r'Egy rendszer fő determinánsa $D=0$. Mi következik ebből?',
        ['Nincs pontosan egy megoldás — hogy nulla vagy végtelen sok, azt a Gauss dönti el',
         'Biztosan nincs megoldás, mert nullával nem lehet osztani',
         'Biztosan végtelen sok megoldás van, mert eltűnt egy feltétel',
         'A megoldás $x=y=z=0$, mert minden számláló nullával osztódik'], 0,
        jo="✔ A D = 0 csak annyit zár ki, hogy pontosan egy megoldás legyen. A két "
           "megmaradó eset között a Gauss-eljárás választ.",
        nem="✘ A D = 0 nem azonos azzal, hogy „nincs megoldás”: lehet végtelen sok is. "
            "A determináns csak a HATÁROZOTT esetet zárja ki; a döntéshez Gauss kell."),
 ]),

 ("Melyik módszert válasszam", [
   '<p>Két teljes értékű eljárásod van. Nem versenytársak — más a hatókörük.</p>',
   '<table class="tt-table">'
   '<tr><th></th><th>Cramer-szabály</th><th>Gauss-eljárás</th></tr>'
   '<tr><td><b>Mikor működik</b></td><td>csak ha $D\\ne0$</td><td>mindig</td></tr>'
   '<tr><td><b>Mit ad</b></td><td>a megoldást, képlettel</td>'
   '<td>a megoldást <b>és</b> a megoldások számát</td></tr>'
   '<tr><td><b>Mikor gyors</b></td><td>ha csak <b>egy</b> ismeretlen kell (elég $D$ és egy '
   'helyettesítési determináns)</td><td>ha az együtthatók között sok az $1$ és a $0$</td></tr>'
   '<tr><td><b>Mikor kényelmetlen</b></td><td>ha mind a három ismeretlen kell: négy '
   'determinánst kell kiszámolni</td><td>ha törtek keletkeznek menet közben</td></tr>'
   '</table>',
   '<p>Gyakorlati tanács a dolgozatra: ha a feladat azt kérdezi, hogy <b>hány megoldása '
   'van</b> a rendszernek, kezdd a determinánssal — ha nem nulla, egy mondatban kész a '
   'válasz. Ha viszont a feladat a <b>megoldást</b> kéri, és nem tudod előre, hogy '
   'határozott-e, a Gauss-eljárás a biztosabb út: az soha nem akad el.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Gabriel Cramer svájci matematikus $1750$-ben publikálta a szabályt (bár '
         'lényegében ugyanezt már Leibniz és Maclaurin is ismerte). A képlet elegáns, és '
         'kézzel, három ismeretlenre kényelmes.</p>'
         '<p>Nagy rendszerekre viszont <b>használhatatlanul lassú</b>: a determinánsok '
         'kiszámításának munkája az ismeretlenek számával robbanásszerűen nő. Egy '
         'húszismeretlenes rendszernél a Cramer-szabály egy átlagos számítógépen már '
         '<b>évekig</b> futna, míg a Gauss-eljárás ezredmásodpercek alatt végez. Ezért '
         'épül minden komoly numerikus eljárás a Gauss-elimináció <b>elvére</b> — a '
         'Cramer-szabály <b>elméleti</b> eszköz maradt, nem számolási.</p>'),
   GY(FGY + "#alap-9", "A 9–16", FGY + "#kozep-5", "K 5–11"),
   brief('<b>Kanrak:</b> A gép megvan: eljárás, képlet, döntési szabály. De a Kamra '
         'műszerei nem egyenletrendszerekben beszélnek, hanem <b>mérési jegyzőkönyvekben</b>. '
         'A következő lépés a legnehezebb az egész témakörben — és nem a számolás lesz az.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-determinans.html",
     cim="A determináns",
     cim_tiszta="A determináns",
     alcim="Másod- és harmadrendű determináns, a Sarrus-szabály, a kifejtés sor vagy "
           "oszlop szerint, és a számolást rövidítő tulajdonságok.",
     chip=KUL + " · 4/6", szakaszok=B1,
     elozo=("tananyag-megoldasok-szama.html", "Hány megoldás van?"),
     kovetkezo=("tananyag-cramer.html", "A Cramer-szabály")),
 lap(**T, fajl="tananyag-cramer.html",
     cim="A Cramer-szabály — és a korlátja",
     cim_tiszta="A Cramer-szabály",
     alcim="A négy determináns, a megoldóképlet, a $D\\ne0$ feltétel jelentése, és a "
           "Cramer–Gauss összehasonlítás.",
     chip=KUL + " · 5/6", szakaszok=B2,
     elozo=("tananyag-determinans.html", "A determináns"),
     kovetkezo=("tananyag-szoveges-feladatok.html", "Szövegből rendszer")),
]
for u in KI:
    print("✓", os.path.basename(u))
