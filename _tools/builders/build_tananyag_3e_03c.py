# -*- coding: utf-8 -*-
"""3e/03 — C altema: szoveges feladatok (C1). Mentor: Kanrak.
Kuldetes: A Rendszer Hibaja. Zaro egyseg, atvezetes a 04. Vektorok temakorre."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj

T = dict(tagozat="3e", mappa="03-linearis-rendszerek", temakor="Lineáris egyenletrendszerek")
FGY = "feladatok-rendszerek.html"
KUL = "A Rendszer Hibája"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import symbols, Eq, solve, simplify, N
E = []
def chk(n, g, w, tur=1e-9):
    kul = simplify(g - w)
    if not ((kul == 0) or abs(float(N(kul))) <= tur):
        E.append((n, g, w))

x, y, z = symbols("x y z")

# C1 — 2x2: 3 toll + 2 fuzet = 1560 din; 5 toll + 4 fuzet = 2900 din
m = solve([Eq(3*x + 2*y, 1560), Eq(5*x + 4*y, 2900)], [x, y], dict=True)[0]
chk("C1-toll", m[x], 220); chk("C1-fuzet", m[y], 450)
chk("C1-ell-1", 3*220 + 2*450, 1560)
chk("C1-ell-2", 5*220 + 4*450, 2900)
chk("C1-kikuszoboles", 2*(3*220 + 2*450) - (5*220 + 4*450), 220)   # 6x+4y - (5x+4y) = x
chk("C1-kerdes", 4*220 + 3*450, 2230)
# C1 — 3x3: kicsi + kozepes + nagy = 30 db; 2x + 5y + 9z = 112 liter; y = 2z
m3 = solve([Eq(x + y + z, 30), Eq(2*x + 5*y + 9*z, 112), Eq(y - 2*z, 0)],
           [x, y, z], dict=True)[0]
chk("C1-kicsi", m3[x], 18); chk("C1-kozepes", m3[y], 8); chk("C1-nagy", m3[z], 4)
chk("C1-3-ell-1", 18 + 8 + 4, 30)
chk("C1-3-ell-2", 2*18 + 5*8 + 9*4, 112)
chk("C1-3-ell-3", 8, 2*4)
chk("C1-3-lepes", (2*x + 5*y + 9*z) - 2*(x + y + z), 3*y + 7*z)
chk("C1-3-jobb", 112 - 2*30, 52)
chk("C1-3-z", solve(Eq(3*(2*z) + 7*z, 52), z)[0], 4)
chk("C1-3-kerdes", 5*8, 40)
from sympy import Matrix
chk("C1-3-determinans", Matrix([[1, 1, 1], [2, 5, 9], [0, 1, -2]]).det(), -13)
# C1 — a kvizhez: ket szam osszege 40, kulonbsege 8
mk = solve([Eq(x + y, 40), Eq(x - y, 8)], [x, y], dict=True)[0]
chk("C1-kviz-x", mk[x], 24); chk("C1-kviz-y", mk[y], 16)
chk("C1-kviz-szorzat", 24*16, 384)
# C1 — sebesseg-ido-ut mintapelda a felsorolashoz
mh = solve([Eq(4*(x + y), 120), Eq(6*(x - y), 120)], [x, y], dict=True)[0]
chk("C1-hajo-sajat", mh[x], 25)
chk("C1-hajo-sodras", mh[y], 5)
chk("C1-hajo-ell-1", 4*(25 + 5), 120)
chk("C1-hajo-ell-2", 6*(25 - 5), 120)

assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- C1
C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> A Kamra nem egyenletrendszerekben beszél, hanem <b>mérési '
         'jegyzőkönyvekben</b>: „a hármas tartály és a hatos tartály együtt kétszer annyit '
         'nyelt el, mint a négyes”. A nehéz rész nem a megoldás — azt már tudod. A nehéz '
         'rész a <b>fordítás</b>: szövegből jelekbe.'),
   '<p>Ez a témakör egyetlen <b>alapszintű</b> kimenete, és egyben a legfontosabb: az '
   'egyenletrendszer önmagában nem hasznos, csak akkor, ha fel tudod írni. A fordítás '
   'képessége az, ami a matematikát az iskolán kívül is használhatóvá teszi.</p>',
 ]),

 ("A négy lépés", [
   doboz("tetel", "A szöveges feladat menete",
         '<ol>'
         '<li><b>Mi az ismeretlen?</b> Írd le <b>szavakkal is</b>, és ne csak betűvel: '
         '„legyen $x$ egy toll ára dinárban”. A mértékegység a megnevezés része.</li>'
         '<li><b>Az adatokat közlő mondatokból lesznek az egyenletek.</b> Haladj sorban a '
         'szövegen — a legtöbb ilyen mondat egy-egy egyenletet ad. Annyi egyenlet kell, '
         'ahány ismeretlent bevezettél, és <b>egyik se következzen a többiből</b>.</li>'
         '<li><b>Oldd meg</b> a rendszert — behelyettesítéssel, kiküszöböléssel, '
         'Gauss-eljárással vagy Cramer-szabállyal, amelyik kényelmesebb.</li>'
         '<li><b>Ellenőrizz a szöveggel</b>, ne csak az egyenlettel — és <b>olvasd vissza a '
         'kérdést</b>: pontosan arra válaszolj, amit kérdeztek.</li>'
         '</ol>',
         hid="tetel-negy-lepes"),
   '<p>A negyedik lépés két külön dolgot takar. Az <b>egyenletbe</b> való visszahelyettesítés '
   'a számolási hibát szűri ki; a <b>szöveggel</b> való ellenőrzés viszont a felírás '
   'hibájára világít rá. Ha $-3$ toll jött ki, vagy egy ember életkorára $180$ év, akkor '
   'valami biztosan hibás — és először a felírást nézd meg, mert azt az egyenletbe való '
   'visszahelyettesítés <b>nem</b> szűri ki.</p>',
   doboz("csapda", "Maxi trükkje",
         '<p><i>„Megvan: $x=220$. Kész.”</i></p>'
         '<p>Csakhogy ha a kérdés az volt, hogy <b>mennyibe kerül együtt</b> négy toll és '
         'három füzet, akkor a válasz nem $x$ értéke, hanem $4x+3y$ — azt még ki kell '
         'számolni.</p>'
         '<p>Ez a leggyakoribb pontveszteség a szöveges feladatoknál — nem tudáshiány, '
         'hanem figyelmetlenség. Az utolsó lépés mindig ugyanaz: <b>olvasd vissza a '
         'kérdést</b>, és fogalmazd meg a választ egész mondatban, mértékegységgel együtt. '
         'A mértékegység elhagyása ugyanígy pontlevonás: a „$220$” nem válasz, a „$220$ '
         'dinár” az.</p>'
         '<p>Ugyanez a hiba fordítva is előfordul: van, aki a részeredményeket '
         '<b>nem</b> írja le, csak a végszámot. A dolgozatban mindkettő kell — az '
         'ismeretlenek értéke <b>és</b> a kérdésre adott válasz.</p>'),
   kviz('Két szám összege $40$, különbsége $8$. Mennyi a két szám <b>szorzata</b>?',
        ['$384$', '$24$', '$16$', '$320$'], 0,
        jo="✔ A rendszerből x = 24 és y = 16, a kérdés viszont a szorzatra vonatkozott: "
           "24 · 16 = 384.",
        nem="✘ A rendszer megoldása x = 24, y = 16 — de a kérdés a SZORZATUKAT kérte: "
            "24 · 16 = 384. Mindig olvasd vissza, mit kérdeztek."),
 ]),

 ("A visszatérő feladattípusok", [
   '<p>A szöveges feladatok néhány visszatérő mintát követnek. Ha felismered a mintát, a '
   'felírás fele már megvan.</p>',
   '<table class="tt-table">'
   '<tr><th>Típus</th><th>Az ismeretlenek</th><th>Az egyenletek forrása</th></tr>'
   '<tr><td><b>mennyiség — egységár — összérték</b></td><td>a darabárak</td>'
   '<td>minden vásárlás egy egyenlet: $\\text{darab}\\cdot\\text{ár}$ tagok összege</td></tr>'
   '<tr><td><b>sebesség — idő — út</b></td><td>a sebességek</td>'
   '<td>minden szakaszra $s=v\\cdot t$; folyón az áramlás hozzáadódik vagy levonódik</td></tr>'
   '<tr><td><b>keverés</b></td><td>a keverendő mennyiségek</td>'
   '<td>egy egyenlet az össztömegre, egy a hatóanyagra</td></tr>'
   '<tr><td><b>életkorok</b></td><td>a mai életkorok</td>'
   '<td>„$n$ év múlva” minden életkorhoz $+n$, „$n$ éve” $-n$</td></tr>'
   '<tr><td><b>kétjegyű szám számjegyei</b></td><td>a számjegyek</td>'
   '<td>maga a szám $10a+b$, a felcserélt $10b+a$</td></tr>'
   '</table>',
   '<p>Egy tipikus sebességes példa: egy hajó $120$ km-t tesz meg a folyón lefelé $4$ óra '
   'alatt, fölfelé ugyanezt $6$ óra alatt. Ha $x$ a hajó saját sebessége és $y$ a folyó '
   'sodrásáé, akkor $4(x+y)=120$ és $6(x-y)=120$, ahonnan $x=25$ km/h és $y=5$ km/h.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>A <b>keverési feladat</b> pontosan az, amit a gyógyszertárban, a festékkeverő '
         'gépnél és a laborban csinálnak: adott töménységű oldatokból kell adott '
         'töménységűt kikeverni. A <b>sebesség–idő–út</b> típus pedig minden menetrend '
         'mögött ott van — és minden repülőút-tervezésben, ahol a szél ugyanúgy '
         'hozzáadódik vagy levonódik, mint a folyó sodrása.</p>'
         '<p>Közös bennük, hogy a valóságban is <b>több</b> ismeretlen van, és soha nem '
         'mérjük őket közvetlenül: csak összefüggéseket látunk. Ezért a rendszer nem '
         'iskolai mesterkéltség, hanem a helyzet természetes leírása.</p>'),
   kviz('„Egy jegy felnőtteknek $x$ dinár, diákoknak $y$ dinár. Három felnőtt és két diák '
        'együtt $1300$ dinárt fizetett.” Melyik egyenlet írja le ezt a mondatot?',
        ['$3x+2y=1300$', '$x+y=1300$', '$3x\\cdot2y=1300$', '$5(x+y)=1300$'], 0,
        jo="✔ Minden jegytípusnál a darabszám szorozza az árat, és a szorzatokat adjuk "
           "össze: 3x + 2y = 1300.",
        nem="✘ A darabszám az árat SZOROZZA, és a különböző jegytípusok összegződnek: "
            "3x + 2y = 1300. Az árakat összeszorozni értelmetlen, és a darabszámokat sem "
            "vonhatjuk össze, mert eltérő az ár."),
 ]),

 ("Kidolgozott példa — két ismeretlen", [
   doboz("pelda", "Kristály-kamra szimuláció — a raktár árlistája",
         r'<p><b>Feladat.</b> A Kamra írószerraktárában három toll és két füzet együtt '
         r'$1560$ dinárba kerül, öt toll és négy füzet pedig $2900$ dinárba. '
         r'<b>Mennyibe kerül együtt négy toll és három füzet?</b></p>'
         r'<p><b>1. Az ismeretlenek.</b> Legyen $x$ egy toll ára dinárban, $y$ pedig egy '
         r'füzeté dinárban.</p>'
         r'<p><b>2. Az egyenletek.</b> A két mondat egy-egy egyenletet ad:</p>'
         r'$$\begin{aligned}3x+2y&=1560\\ 5x+4y&=2900\end{aligned}$$'
         r'<p><b>3. A megoldás.</b> Az $y$ együtthatói $2$ és $4$: az elsőt $2$-vel '
         r'szorozva egyenlővé tehetők, majd kivonjuk a másodikat:</p>'
         r'$$\begin{aligned}6x+4y&=3120\\ 5x+4y&=2900\end{aligned}$$'
         r'<p>A különbség $x=220$. Ezt az első eredeti egyenletbe írva '
         r'$660+2y=1560$, tehát $2y=900$ és $y=450$.</p>'
         r'<p><b>4. Ellenőrzés és válasz.</b> $3\cdot220+2\cdot450=660+900=1560$ ✔, '
         r'$5\cdot220+4\cdot450=1100+1800=2900$ ✔. Az árak reálisak (pozitívak, egész '
         r'dinárok).</p>'
         r'<p>De a kérdés <b>nem</b> az árakra vonatkozott! Négy toll és három füzet ára:</p>'
         r'$$4\cdot220+3\cdot450=880+1350=2230.$$',
         hid="pelda-arak",
         lenyilo=("Végeredmény",
                  r'<p>Egy toll $220$ dinár, egy füzet $450$ dinár.</p>'
                  r'<p class="vegeredmeny">Négy toll és három füzet együtt <b>2230 dinár</b>.</p>')),
   '<p>Figyeld meg, hogy a megoldás <b>három</b> számot tartalmaz: a két ismeretlen értékét '
   'és a kérdésre adott választ. A dolgozatban mindhármat le kell írni — az első kettőt '
   'azért, mert azok a rendszer megoldásai, a harmadikat azért, mert az a válasz.</p>',
 ]),

 ("Kidolgozott példa — három ismeretlen", [
   doboz("pelda", "Kristály-kamra szimuláció — a tartályleltár",
         r'<p><b>Feladat.</b> A Kamrában háromféle kristálytartály van: kicsi, közepes és '
         r'nagy. Összesen $30$ darab áll a raktárban. A kicsibe $2$, a közepesbe $5$, a '
         r'nagyba $9$ liter fér, és a raktár teljes űrtartalma $112$ liter. Közepesből '
         r'kétszer annyi van, mint nagyból. <b>Hány liter fér összesen a közepes '
         r'tartályokba?</b></p>'
         r'<p><b>1. Az ismeretlenek.</b> Legyen $x$ a kicsi, $y$ a közepes és $z$ a nagy '
         r'tartályok <b>darabszáma</b>.</p>'
         r'<p><b>2. Az egyenletek.</b> Három adatközlő mondat, három egyenlet:</p>'
         r'$$\begin{aligned}x+y+z&=30 &&\text{(a darabszám)}\\ '
         r'2x+5y+9z&=112 &&\text{(az űrtartalom)}\\ y&=2z &&\text{(az arány)}\end{aligned}$$'
         r'<p><b>3. A megoldás.</b> A harmadik egyenlet már kifejezett alakban áll, ezért '
         r'nem kell hozzá se teljes Gauss-eljárás, se Cramer-szabály: elég egyetlen kiejtés '
         r'és egy behelyettesítés. Először az első két egyenletből ejtsük ki az $x$-et — az '
         r'$S_2-2S_1$ lépéssel:</p>'
         r'$$(2x+5y+9z)-2(x+y+z)=3y+7z,\qquad 112-2\cdot30=52,$$'
         r'<p>tehát $3y+7z=52$. Ide beírva $y=2z$-t:</p>'
         r'$$6z+7z=52 \quad\Longrightarrow\quad 13z=52 \quad\Longrightarrow\quad z=4.$$'
         r'<p>Innen $y=2\cdot4=8$, és az első egyenletből $x=30-8-4=18$.</p>'
         r'<p><b>4. Ellenőrzés és válasz.</b> $18+8+4=30$ ✔, '
         r'$2\cdot18+5\cdot8+9\cdot4=36+40+36=112$ ✔, és $8=2\cdot4$ ✔. Mindhárom '
         r'darabszám pozitív egész — a szöveg szerint is értelmes.</p>'
         r'<p>A kérdés viszont a közepes tartályok <b>összes űrtartalmára</b> vonatkozott: '
         r'$8\cdot5=40$ liter.</p>',
         hid="pelda-harom-termek",
         lenyilo=("Végeredmény",
                  r'<p>$18$ kicsi, $8$ közepes és $4$ nagy tartály van.</p>'
                  r'<p class="vegeredmeny">A közepes tartályokba összesen <b>40 liter</b> fér.</p>')),
   '<p>Ez a feladat jól mutatja, hogy a <b>megoldás módszerét</b> is a szöveg választja ki. '
   'A harmadik egyenlet ($y=2z$) már kifejezett alakban áll — kár lenne determinánsokat '
   'számolni hozzá.</p>'
   '<p>Menne persze Cramer-szabállyal is: a rendszer fő determinánsa</p>'
   '$$D=\\begin{vmatrix}1&1&1\\\\ 2&5&9\\\\ 0&1&-2\\end{vmatrix}=-13\\ne0,$$'
   '<p>tehát a rendszer határozott, és a megoldás felírható a négy determináns '
   'hányadosaként. Csak épp <b>négy</b> harmadrendű determinánst kellene kiszámolni '
   'ahhoz, amihez itt egyetlen behelyettesítés is elég. A gyorsabb út majdnem mindig '
   'az, amelyik az adott szöveghez illik.</p>',
   doboz("csapda", "Az arány iránya",
         '<p>„Közepesből <b>kétszer annyi</b> van, mint nagyból” — ez $y=2z$, nem $2y=z$. '
         'Az ellenőrzés egyszerű: ha nagyból $4$ van, akkor közepesből $8$-nak kell lennie — '
         'és valóban, $y=2z$ mellett $8=2\\cdot4$. A $2y=z$ épp a fordítottját mondaná: '
         'nagyból volna kétszer annyi.</p>'
         '<p>Ha bizonytalan vagy, <b>próbáld ki számokkal</b>, mielőtt továbbmennél. Egy rossz '
         'irányú arány az egész megoldást használhatatlanná teszi — és a saját (hibás) '
         'egyenleteidbe visszahelyettesítve minden „stimmelni” fog. Ezért kell a '
         '<b>szöveggel</b> ellenőrizni, nem az egyenlettel. (Ebben a feladatban szerencsénk '
         'van: a $2y=z$ változattal $17y=52$ jönne ki, ami nem egész — a hiba azonnal '
         'kibukna. De erre nem szabad számítani.)</p>'),
   GY(FGY + "#alap-19", "A 19–24", FGY + "#kozep-14", "K 14–19"),
   brief('<b>Kanrak:</b> A Rendszer Hibáját megtaláltuk: nem a mérésekben volt, hanem '
         'abban, ahogyan összeolvastuk őket. Innen már a te dolgod — a Kamra hálózata '
         'olvasható. <b>Crni Grom</b> következik: a rendszert megtörtük, most az '
         '<b>irányt</b> kell eltalálni. Ehhez pedig olyan mennyiség kell, amelynek nemcsak '
         'nagysága van, hanem iránya is.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-szoveges-feladatok.html",
     cim="Szövegből rendszer",
     cim_tiszta="Szövegből rendszer",
     alcim="A szöveges feladat négy lépése, a visszatérő feladattípusok, és két végig "
           "kidolgozott példa — kettő, illetve három ismeretlennel.",
     chip=KUL + " · 6/6", szakaszok=C1,
     elozo=("tananyag-cramer.html", "A Cramer-szabály"),
     kovetkezo=(FGY, "Feladatok — egyenletrendszerek")),
]
for u in KI:
    print("✓", os.path.basename(u))
