# -*- coding: utf-8 -*-
"""2e / 01 — „A" altéma: Hatványozás (A1) és a hatványfüggvény grafikonja (A2).

Mentor: Vihar Vera. Küldetés: „A Képzelet Határa".
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
         temakor="Hatványozás, gyökvonás, komplex számok")
FGY = "feladatok-hatvanyozas.html"

# =====================================================================  A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Vihar Vera:</b> Kadét, a vihar ereje nem összeadódik — <b>szorzódik</b>. '
         'Egy villám feszültsége nem „valamivel több" a másiknál: <b>nagyságrendekkel</b> nagyobb. '
         'Ez a hatványozás nyelve, és az M-Hullám is ezen a nyelven beszél. '
         'Ha nem tudod egyetlen tömör alakba sűríteni a kaotikus kifejezéseket, '
         'Dr. Baljós mutációi olvashatatlanná torzítják a műszereinket. Kezdjük az alapoknál.'),
   'Az általánosban a hatványozás csak rövidítés volt az ismételt szorzásra. Idén <b>kitágítjuk</b>: '
   'lesz nulla, negatív, majd (a témakör végére) <b>tört</b> kitevő is. A trükk mindvégig ugyanaz — '
   'úgy bővítünk, hogy a megszokott <b>azonosságok érvényben maradjanak</b>.',
 ]),

 ("A hatvány fogalma", [
   doboz("definicio", "Természetes kitevőjű hatvány",
         '<p>Ha $a\\in\\mathbb{R}$ és $n\\in\\mathbb{N}$, akkor az $a$ szám $n$-edik hatványa '
         'az az $n$ tényezős szorzat, amelynek minden tényezője $a$:</p>'
         '$$a^{n}=\\underbrace{a\\cdot a\\cdot\\ldots\\cdot a}_{n\\ \\text{tényező}}$$'
         '<p>Itt $a$ a hatvány <b>alapja</b>, $n$ pedig a <b>kitevője</b>.</p>',
         hid="def-hatvany"),
   doboz("erdekesseg", "Hol találkozol vele? — a normálalak",
         '<p>A természettudomány a nagyon nagy és nagyon kicsi mennyiségeket <b>normálalakban</b> '
         '(tudományos jelöléssel) írja: $a\\cdot 10^{k}$, ahol $1\\le a&lt;10$ és $k\\in\\mathbb{Z}$. '
         'Egy fényév kb. $9{,}46\\cdot 10^{15}\\ \\text{m}$, egy elektron tömege '
         '$9{,}11\\cdot 10^{-31}\\ \\text{kg}$. A két szám kiírva 16, illetve 31 jegyű volna — '
         'a hatvány itt nem dísz, hanem <b>olvashatóság</b>.</p>'),
 ]),

 ("A hatványozás azonosságai", [
   'Ezek a szabályok a definícióból egyenesen következnek: elég megszámolni, hány tényező van.',
   doboz("tetel", "A hatványozás öt alapazonossága",
         '<p>Ha $a,b\\in\\mathbb{R}$ és $m,n\\in\\mathbb{N}$, akkor</p>'
         '$$a^{m}\\cdot a^{n}=a^{m+n}\\qquad '
         '\\frac{a^{m}}{a^{n}}=a^{m-n}\\ (a\\neq 0)\\qquad '
         '\\left(a^{m}\\right)^{n}=a^{m\\cdot n}$$'
         '$$a^{m}\\cdot b^{m}=(a\\cdot b)^{m}\\qquad '
         '\\frac{a^{m}}{b^{m}}=\\left(\\frac{a}{b}\\right)^{m}\\ (b\\neq 0)$$',
         hid="tetel-hatvany-azonossagok",
         lenyilo=("Miért igaz az első?",
                  '<p>Az $a^{m}$ pontosan $m$ darab $a$ tényező szorzata, az $a^{n}$ pedig $n$ darabé. '
                  'Egymás mellé írva összesen $m+n$ tényezőt kapunk — ez éppen $a^{m+n}$. '
                  'A többi azonosság ugyanígy, tényezőszámlálással igazolható.</p>')),
   doboz("tetel", "Előjel és nagyságrend",
         '<p>$1^{m}=1$, továbbá $0^{m}=0$ minden $m&gt;0$ esetén, és</p>'
         '$$(-1)^{m}=\\begin{cases}\\ \\ 1,&\\text{ha } m \\text{ páros},\\\\ -1,&\\text{ha } m \\text{ páratlan}.\\end{cases}$$'
         '<p>Ha $m&gt;n$, akkor $a&gt;1$ esetén $a^{m}&gt;a^{n}$, viszont $0&lt;a&lt;1$ esetén '
         '$a^{m}&lt;a^{n}$ — a törtszám hatványai <b>csökkennek</b>.</p>',
         hid="tetel-hatvany-elojel"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Állítsd növekvő sorrendbe: $A=\\dfrac{1}{3}$, $B=-\\dfrac{1}{3}$, '
         '$C=\\left(-\\dfrac{1}{3}\\right)^{2}$, $D=\\left(-\\dfrac{1}{3}\\right)^{3}$.</p>',
         lenyilo=("Megoldás",
                  '<p>$C=\\dfrac{1}{9}$ (páros kitevő → pozitív), $D=-\\dfrac{1}{27}$ '
                  '(páratlan kitevő → negatív). A két negatív közül $B=-\\dfrac{1}{3}$ a kisebb, '
                  'a két pozitív közül $C=\\dfrac19$ a kisebb. Tehát</p>'
                  '$$B&lt;D&lt;C&lt;A.$$')),
   kviz('Mennyi $(-2)^{4}$ és mennyi $-2^{4}$?',
        ['$16$ és $-16$', 'Mindkettő $16$', 'Mindkettő $-16$'], 0,
        jo="✔ A zárójel dönt: (−2)⁴ = 16 (a −2-t emeljük negyedikre), "
           "míg −2⁴ = −(2⁴) = −16 (csak a 2-t, az előjel kívül marad).",
        nem="✘ A zárójel nem díszítés: (−2)⁴ = 16, de −2⁴ = −(2⁴) = −16. "
            "A második esetben a hatványozás ERŐSEBBEN köt, mint az előjel."),
 ]),

 ("Nulla és negatív kitevő", [
   'Mi legyen $a^{0}$ vagy $a^{-3}$? A definíció („ennyi tényező szorzata") itt már nem segít — '
   'nem lehet nulla darab vagy mínusz három darab tényezőt összeszorozni. Ezért nem <i>kitaláljuk</i> '
   'az értéküket, hanem <b>kikényszerítjük</b>: úgy definiáljuk őket, hogy a fenti azonosságok '
   'továbbra is igazak maradjanak. Ezt hívják <b>permanenciaelvnek</b>.',
   doboz("tetel", "Így jön ki a nulla és a negatív kitevő",
         '<p>Legyen $a\\neq 0$. Ha az $\\dfrac{a^{m}}{a^{n}}=a^{m-n}$ szabály $m=n$-re is érvényes:</p>'
         '$$1=\\frac{a^{n}}{a^{n}}=a^{n-n}=a^{0}.$$'
         '<p>Ha pedig $m=0$-ra is érvényes:</p>'
         '$$\\frac{1}{a^{n}}=\\frac{a^{0}}{a^{n}}=a^{0-n}=a^{-n}.$$'
         '<p>Nincs választásunk: <b>ez az egyetlen</b> értelmezés, amivel az azonosságok megmaradnak.</p>',
         hid="tetel-permanencia"),
   doboz("definicio", "Egész kitevőjű hatvány",
         '<p>Ha $a\\in\\mathbb{R}$, $a\\neq 0$ és $n\\in\\mathbb{N}$, akkor</p>'
         '$$a^{0}=1,\\qquad a^{-n}=\\frac{1}{a^{n}}=\\left(\\frac{1}{a}\\right)^{n}.$$'
         '<p>Speciálisan $\\left(\\dfrac{a}{b}\\right)^{-n}=\\left(\\dfrac{b}{a}\\right)^{n}$ — '
         'a negatív kitevő a törtet <b>megfordítja</b>. Ezek után az öt azonosság már '
         '<b>minden egész</b> kitevőre érvényes.</p>',
         hid="def-egesz-kitevo"),
   kviz('Mennyi $\\left(\\dfrac{2}{5}\\right)^{-2}$?',
        ['$\\dfrac{25}{4}$', '$-\\dfrac{4}{25}$', '$\\dfrac{4}{25}$'], 0,
        jo="✔ A negatív kitevő megfordítja a törtet: (5/2)² = 25/4.",
        nem="✘ Fordítsd meg a törtet, majd emelj négyzetre: (2/5)⁻² = (5/2)² = 25/4."),
 ]),

 ("Előjelek — ahol Dr. Baljós a leggyakrabban támad", [
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A mutálódott kód négy klasszikus hibát rejt. Mindegyik <b>hamis</b>:</p>'
         '<ol class="reszfeladatok">'
         '<li>$-2^{4}=16$ — <b>nem</b>: a hatványozás előbb jön, mint az előjel, tehát '
         '$-2^{4}=-\\left(2^{4}\\right)=-16$. Ezzel szemben $(-2)^{4}=16$.</li>'
         '<li>$(-2)^{-2}=-\\dfrac14$ — <b>nem</b>: $(-2)^{-2}=\\dfrac{1}{(-2)^{2}}=\\dfrac14$. '
         'A negatív <b>kitevő</b> soha nem tesz negatívvá egy hatványt.</li>'
         '<li>$a^{-n}=-a^{n}$ — <b>nem</b>: a negatív kitevő <b>reciprokot</b> jelent, nem ellentettet.</li>'
         '<li>$0^{0}=1$ — <b>nem</b>: a $0^{0}$ kifejezés <b>nincs értelmezve</b> '
         '(a $a^{0}=1$ szabály csak $a\\neq0$ mellett érvényes).</li>'
         '</ol>'),
   kviz('Mennyi $-3^{2}+(-3)^{2}$?',
        ['$0$', '$18$', '$-18$'], 0,
        jo="✔ −3² = −9, (−3)² = 9, az összegük 0.",
        nem="✘ Figyelj a zárójelre: −3² = −(3²) = −9, de (−3)² = +9. Az összeg 0."),
 ]),

 ("Összetett hatványkifejezések", [
   'A vizsgahelyzetek nagy része két típus: <b>számkifejezés pontos értéke</b> és '
   '<b>betűs kifejezés egyszerűsítése</b>. Mindkettőnél ugyanaz a stratégia — '
   'előbb minden hatványt közös alapra hozunk, aztán az azonosságokkal összevonunk.',
   doboz("pelda", "Vészterem-szimuláció — számkifejezés",
         '<p>Számítsd ki: $\\left(\\dfrac{3}{5}\\right)^{2}-\\dfrac{3}{5^{2}}'
         '+\\left(-\\dfrac{3}{5}\\right)^{2}-\\left(\\dfrac{5}{3}\\right)^{-2}$.</p>',
         hid="pelda-szamkifejezes",
         lenyilo=("Megoldás",
                  '<p>Tagonként: $\\left(\\dfrac35\\right)^{2}=\\dfrac{9}{25}$; '
                  '$\\dfrac{3}{5^{2}}=\\dfrac{3}{25}$ (itt csak az 5 van négyzeten!); '
                  '$\\left(-\\dfrac35\\right)^{2}=\\dfrac{9}{25}$; '
                  '$\\left(\\dfrac53\\right)^{-2}=\\left(\\dfrac35\\right)^{2}=\\dfrac{9}{25}$. Így</p>'
                  '$$\\frac{9}{25}-\\frac{3}{25}+\\frac{9}{25}-\\frac{9}{25}=\\frac{6}{25}.$$')),
   doboz("pelda", "Vészterem-szimuláció — betűs kifejezés",
         '<p>Egyszerűsítsd ($a,b,c&gt;0$): '
         '$\\left(\\dfrac{a^{-1}}{b^{2}c}\\right)^{2}\\cdot\\dfrac{a^{3}b^{-2}}{c^{4}}$.</p>',
         hid="pelda-betus",
         lenyilo=("Megoldás",
                  '<p>Az első tényező: $\\dfrac{a^{-2}}{b^{4}c^{2}}=a^{-2}b^{-4}c^{-2}$. '
                  'A második: $a^{3}b^{-2}c^{-4}$. Kitevőnként összeadva: '
                  '$a$: $-2+3=1$; $b$: $-4-2=-6$; $c$: $-2-4=-6$. Tehát</p>'
                  '$$a^{1}b^{-6}c^{-6}=\\frac{a}{b^{6}c^{6}}.$$')),
   doboz("pelda", "Vészterem-szimuláció — kitevőben betű",
         '<p>Hozd egyszerűbb alakra ($n\\in\\mathbb{N}$): $\\dfrac{3^{n+2}-3^{n}}{3^{n+1}}$.</p>',
         hid="pelda-kitevoben-betu",
         lenyilo=("Megoldás",
                  '<p>A kulcs a <b>kiemelés</b>: a számlálóban $3^{n+2}=3^{n}\\cdot 3^{2}$ és '
                  '$3^{n}=3^{n}\\cdot 1$, a nevezőben $3^{n+1}=3^{n}\\cdot 3$. Így</p>'
                  '$$\\frac{3^{n}\\left(9-1\\right)}{3^{n}\\cdot 3}=\\frac{8}{3}.$$'
                  '<p>A $3^{n}$ kiesik — az eredmény <b>nem függ</b> $n$-től.</p>')),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–5, 8"),
   brief('<b>Vihar Vera:</b> A hatvány mostantól nem csak szám — <b>függvény</b> is. '
         'Ha az alapot rögzítjük és a kitevőt változtatjuk, exponenciális görbét kapunk (az a tavaszi küldetés). '
         'Ha viszont a <b>kitevőt</b> rögzítjük és az alapot változtatjuk, megkapjuk a '
         '<b>hatványfüggvényt</b> — és annak a képe elárulja, hogyan viselkedik a rendszer. Nézzük meg.',
         outro=True),
 ]),
]

# =====================================================================  A2

TUL_PAROS = (
 '<ul>'
 '<li><b>Értelmezési tartomány:</b> $\\mathbb{R}$; <b>értékkészlet:</b> $[0;+\\infty)$.</li>'
 '<li><b>Zérushely:</b> egyetlen, az $x=0$; itt van a grafikon legalsó pontja.</li>'
 '<li><b>Monotonitás:</b> csökkenő a $(-\\infty,0]$, növekvő a $[0;+\\infty)$ intervallumon.</li>'
 '<li><b>Paritás:</b> <b>páros</b> függvény, mert $(-x)^{2k}=x^{2k}$ — a grafikon '
 'az $y$-tengelyre <b>tükrös</b>.</li>'
 '<li><b>Konvexitás:</b> az egész $\\mathbb{R}$-en konvex (alulról „öblös").</li>'
 '</ul>')

TUL_PARATLAN = (
 '<ul>'
 '<li><b>Értelmezési tartomány:</b> $\\mathbb{R}$; <b>értékkészlet:</b> $\\mathbb{R}$.</li>'
 '<li><b>Zérushely:</b> egyetlen, az $x=0$.</li>'
 '<li><b>Monotonitás:</b> az egész $\\mathbb{R}$-en <b>növekvő</b>.</li>'
 '<li><b>Paritás:</b> <b>páratlan</b> függvény, mert $(-x)^{2k+1}=-x^{2k+1}$ — a grafikon '
 'az <b>origóra</b> középpontosan szimmetrikus.</li>'
 '<li><b>Előjel:</b> negatív a $(-\\infty,0)$, pozitív a $(0;+\\infty)$ intervallumon.</li>'
 '</ul>')

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Vihar Vera:</b> Egy szám még nem fenyegetés. A fenyegetés az, ahogyan a szám <b>változik</b>. '
         'A hatványfüggvény grafikonja egyetlen pillantással megmutatja, mi történik: hol nő, milyen '
         'gyorsan, szimmetrikus-e, van-e hova „elszaladnia". Dr. Baljós mutációi görbék alakjában '
         'jelennek meg az UMOTRON műszerein — ezért kell felismerned őket.'),
   'Ebben az egységben a rögzített kitevőjű $y=x^{n}$ függvényeket vizsgáljuk. Minden a kitevő '
   '<b>paritásán</b> és <b>előjelén</b> múlik — három családot kapunk.',
 ]),

 ("Valós függvény, értelmezési tartomány, értékkészlet", [
   'A <b>valós függvény</b> minden megengedett $x$ valós számhoz pontosan egy $y$ valós számot rendel: '
   '$f:D\\to\\mathbb{R}$. A megengedett $x$-ek halmaza az <b>értelmezési tartomány</b> ($D$), '
   'a felvett $y$-ok halmaza az <b>értékkészlet</b>. A függvény <b>grafikonja</b> az '
   '$\\left(x;f(x)\\right)$ pontok halmaza a koordináta-rendszerben.',
   doboz("erdekesseg", "Emlékeztető",
         '<p>A függvényfogalmat, a grafikon olvasását és a monotonitást tavaly vettük — '
         'ha bizonytalan vagy, nézd át: '
         '<a href="../../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggveny-fogalma.html">'
         '1e · A függvény fogalma</a> és '
         '<a href="../../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggvenytulajdonsagok.html">'
         'Függvénytulajdonságok</a>. Idén ugyanaz a szótár, csak új görbékre alkalmazzuk.</p>'),
   doboz("definicio", "Hatványfüggvény",
         '<p>Minden $n\\ge 1$ egész szám esetén az $f:\\mathbb{R}\\to\\mathbb{R}$, $f(x)=x^{n}$ '
         'valós függvényt <b>hatványfüggvénynek</b> nevezzük. (Az $n=0$ kivétel: $x^{0}=1$ minden $x\\neq 0$-ra, a grafikon egy „lyukas” vízszintes egyenes — ezért nem soroljuk a családba.) Az $n=1$ eset a lineáris '
         'függvény, az $n=2$ a másodfokú alapfüggvény (a <b>parabola</b>), az $n=3$ '
         'a harmadfokú alapfüggvény.</p>',
         hid="def-hatvanyfuggveny"),
 ]),

 ("Páros kitevő: az $x^{2k}$ család", [
   abra(svg_fuggvenyek(
        [(lambda x: x**2, "#047857", "y = x²", [(-2.1, 2.1)]),
         (lambda x: x**4, "#3b82f6", "y = x⁴", [(-1.45, 1.45)])],
        xr=(-2.5, 2.5), yr=(-1.0, 4.3),
        leiras="Az y = x² és y = x⁴ függvények grafikonja: mindkettő az y-tengelyre tükrös, "
               "legalsó pontjuk az origó"),
        "Páros kitevő: a görbe az $y$-tengelyre tükrös, és soha nem megy az $x$-tengely alá."),
   'A $y=x^{2}$ grafikonját <b>parabolának</b> hívjuk; a nagyobb páros kitevők grafikonja '
   'hasonló jellegű (de már nem parabola): a $(-1;1)$ intervallumon <b>közelebb simul</b> '
   'az $x$-tengelyhez, azon kívül pedig <b>meredekebben emelkedik</b>.',
   doboz("tetel", "Az $x^{2k}$ függvény tulajdonságai", TUL_PAROS, hid="tetel-paros-kitevo"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>„A $y=x^{2}$ függvény minden $y$ értéket felvesz." — <b>Hamis.</b> '
         'Az értékkészlet csak $[0;+\\infty)$: negatív szám <b>nem</b> lehet páros kitevőjű '
         'hatvány értéke. Ezért nincs valós megoldása az $x^{2}=-1$ egyenletnek — '
         'és pontosan ez lesz a témakör harmadik szakaszának, a komplex számoknak a kiindulópontja.</p>'),
   kviz('Hány megoldása van valós számok között az $x^{2}=-1$ egyenletnek?',
        ['Egy sem', 'Egy', 'Kettő'], 0,
        jo="✔ Páros kitevőnél a hatvány értéke sosem negatív, tehát nincs ilyen valós x.",
        nem="✘ Bármely valós szám NÉGYZETE nemnegatív, ezért a −1 nem állhat elő így. "
            "Épp ez vezet majd a komplex számok bevezetéséhez."),
 ]),

 ("Páratlan kitevő: az $x^{2k+1}$ család", [
   abra(svg_fuggvenyek(
        [(lambda x: x**3, "#047857", "y = x³", [(-1.62, 1.62)]),
         (lambda x: x**5, "#3b82f6", "y = x⁵", [(-1.33, 1.33)])],
        xr=(-2.5, 2.5), yr=(-4.2, 4.2),
        leiras="Az y = x³ és y = x⁵ függvények grafikonja: mindkettő az origóra "
               "középpontosan szimmetrikus és növekvő"),
        "Páratlan kitevő: a görbe átmegy a harmadik síknegyedbe, és végig növekvő."),
   'A $y=x^{3}$ grafikonja a <b>harmadfokú parabola</b>. A páros esettel szemben itt '
   'a negatív $x$-ekhez negatív érték tartozik — a görbe „átfordul" az origóban.',
   doboz("tetel", "Az $x^{2k+1}$ függvény tulajdonságai", TUL_PARATLAN, hid="tetel-paratlan-kitevo"),
   kviz('Melyik állítás igaz a $y=x^{5}$ függvényre?',
        ['Az origóra középpontosan szimmetrikus.',
         'Az $y$-tengelyre tükrös.',
         'Az értékkészlete $[0;+\\infty)$.'], 0,
        jo="✔ Páratlan kitevő → páratlan függvény → origóra szimmetrikus.",
        nem="✘ A kitevő páratlan: (−x)⁵ = −x⁵, tehát origóra szimmetrikus, és minden valós értéket felvesz."),
 ]),

 ("A grafikonok kölcsönös helyzete", [
   'Melyik nagyobb: $x^{2}$ vagy $x^{3}$? A válasz attól függ, <b>hol</b> vagyunk. '
   'Ez a témakör egyik legtöbbször félreértett részlete.',
   doboz("tetel", "Sorrend a $(0;1)$ és az $(1;+\\infty)$ intervallumon",
         '<p>Ha $x\\in(0;1)$, akkor a nagyobb kitevő <b>kisebb</b> értéket ad:</p>'
         '$$x&gt;x^{2}&gt;x^{3}&gt;x^{4}&gt;\\ldots$$'
         '<p>Ha $x\\in(1;+\\infty)$, akkor a nagyobb kitevő <b>nagyobb</b> értéket ad:</p>'
         '$$x&lt;x^{2}&lt;x^{3}&lt;x^{4}&lt;\\ldots$$'
         '<p>Az $x=0$ és $x=1$ helyeken minden <b>pozitív egész kitevőjű</b> hatványfüggvény '
         'ugyanazt az értéket veszi fel ($0$, illetve $1$) — itt találkoznak a görbék. (Páros kitevőknél az $x=-1$ is közös pont.)</p>'
         '<p>Ha $x&lt;0$: a páros kitevőjű hatvány pozitív, a páratlan negatív, tehát ott <b>mindig a páros kitevőjű a nagyobb</b>; a páros kitevők között pedig ugyanúgy az $|x|$ dönt, mint a pozitív oldalon.</p>',
         hid="tetel-kolcsonos-helyzet",
         lenyilo=("Miért?",
                  '<p>Legyen $0&lt;x&lt;1$. Ekkor $x$-szel szorozva az egyenlőtlenség iránya '
                  'megmarad, de az érték csökken: $x\\cdot x&lt;1\\cdot x$, azaz $x^{2}&lt;x$. '
                  'Ugyanezt ismételve kapjuk a teljes sort. Ha $x&gt;1$, ugyanez a lépés '
                  '<b>növeli</b> az értéket, így a sorrend megfordul.</p>')),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Melyik a nagyobb: $0{,}7^{3}$ vagy $0{,}7^{5}$? És $1{,}2^{3}$ vagy $1{,}2^{5}$?</p>',
         lenyilo=("Megoldás",
                  '<p>$0{,}7\\in(0;1)$, tehát a nagyobb kitevő kisebb értéket ad: '
                  '$0{,}7^{3}&gt;0{,}7^{5}$. Viszont $1{,}2&gt;1$, tehát ott fordítva: '
                  '$1{,}2^{3}&lt;1{,}2^{5}$. <b>Számolni nem kell</b> — elég a szabály.</p>')),
 ]),

 ("Negatív kitevő: az $x^{-n}$ család", [
   'Eddig a <b>hatványfüggvény</b> kitevője pozitív egész volt. A negatív kitevőt a hatványozásnál már bevezettük — most nézzük meg, milyen <b>görbét</b> ad — a hozzárendelési szabály ugyanaz marad, az értelmezési tartomány viszont szűkül.',
   'Ha a kitevő negatív, a függvény $f(x)=x^{-n}=\\dfrac{1}{x^{n}}$ alakú, és $f:\\mathbb{R}\\setminus\\{0\\}\\to\\mathbb{R}$. A $0$ tehát <b>kimarad</b> az értelmezési tartományból — nullával nem osztunk.',
   abra(svg_fuggvenyek(
        [(lambda x: 1 / x, "#047857", "y = 1/x", [(-4.2, -0.26), (0.26, 4.2)]),
         (lambda x: 1 / x**2, "#3b82f6", "y = 1/x²", [(-4.2, -0.5), (0.5, 4.2)])],
        xr=(-4.3, 4.3), yr=(-3.6, 4.2), w=380, h=260,
        leiras="Az y = 1/x hiperbola és az y = 1/x² grafikonja az aszimptotákkal"),
        "Az $x$- és az $y$-tengely <b>aszimptota</b>: a görbe tetszőlegesen megközelíti, de sosem éri el."),
   doboz("definicio", "Aszimptota",
         '<p>Az $f:\\mathbb{R}\\setminus\\{0\\}\\to\\mathbb{R}$, $f(x)=\\dfrac{1}{x^{n}}=x^{-n}$ '
         'függvény grafikonja <b>hiperbola</b> jellegű görbe. Az egyenest, amelyhez a görbe '
         'tetszőlegesen közel kerül, de nem éri el, <b>aszimptotának</b> nevezzük. '
         'Itt két aszimptota van: az $x=0$ és az $y=0$ egyenes (a két koordinátatengely).</p>',
         hid="def-aszimptota"),
   doboz("tetel", "Páros vagy páratlan $n$?",
         '<p>Ha $n$ <b>páros</b> ($y=\\frac{1}{x^{2}},\\frac{1}{x^{4}},\\ldots$): a függvényértékek '
         'mindig <b>pozitívak</b>, a grafikon két ága az $x$-tengely <b>fölött</b> van, '
         'a görbe az $y$-tengelyre tükrös.</p>'
         '<p>Ha $n$ <b>páratlan</b> ($y=\\frac{1}{x},\\frac{1}{x^{3}},\\ldots$): a negatív '
         '$x$-ekhez negatív érték tartozik, a két ág az <b>első és a harmadik</b> síknegyedben van, '
         'a görbe az <b>origóra</b> szimmetrikus.</p>'
         '<p><b>Értelmezési tartomány:</b> $\\mathbb{R}\\setminus\\{0\\}$ · <b>zérushely nincs</b> · <b>értékkészlet:</b> páros $n$-re $(0;+\\infty)$, páratlan $n$-re $\\mathbb{R}\\setminus\\{0\\}$.</p>'
         '<p>⚠️ <b>A monotonitás ágankénti!</b> Az $y=\\dfrac1x$ mindkét ágon csökken, de a két ág <b>együtt nem</b> alkot csökkenő függvényt: $-1&lt;1$, mégis $f(-1)=-1&lt;f(1)=1$. A monotonitást tehát mindig a $(-\\infty;0)$ és a $(0;+\\infty)$ intervallumon külön mondjuk ki.</p>',
         hid="tetel-negativ-kitevo"),
   kviz('Mi az $f(x)=\\dfrac{1}{x^{2}}$ függvény értékkészlete?',
        ['$(0;+\\infty)$', '$[0;+\\infty)$', '$\\mathbb{R}\\setminus\\{0\\}$'], 0,
        jo="✔ Pozitív értékek, de a 0-t sosem éri el (az x-tengely aszimptota).",
        nem="✘ A tört értéke sosem 0 és sosem negatív → az értékkészlet (0; +∞)."),
   gyakorolj(FGY + "#alap-7", "A 7–10", FGY + "#kozep-6", "K 6–7"),
   brief('<b>Vihar Vera:</b> Uraltad a vihar erejét — most fejtsd is vissza. Ha ismerem a hatvány '
         '<b>eredményét</b>, meg tudom-e találni az <b>alapot</b>? Ez a gyökvonás, és vele '
         'megérkezik az első igazi buktató is: a páros gyökkitevő. Vigyázz a lábad elé.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

MAPPA = T["mappa"]
ki = []
ki.append(lap(**T, fajl="tananyag-hatvanyozas.html",
              cim="Hatványozás egész kitevővel", cim_tiszta="Hatványozás egész kitevővel",
              alcim="A hatvány fogalma és azonosságai, a nulla és a negatív kitevő értelmezése, "
                    "előjelszabályok, összetett szám- és betűs kifejezések egyszerűsítése.",
              chip="A Képzelet Határa · 1/8", szakaszok=A1,
              elozo=("index.html", "Témakör-nyitó"),
              kovetkezo=("tananyag-hatvanyfuggveny.html", "A hatványfüggvény és grafikonja")))
ki.append(lap(**T, fajl="tananyag-hatvanyfuggveny.html",
              cim="A hatványfüggvény és grafikonja", cim_tiszta="A hatványfüggvény és grafikonja",
              alcim="Az $y=x^{n}$ függvénycsaládok páros és páratlan kitevőre, a grafikonok "
                    "kölcsönös helyzete, valamint a negatív kitevő és az aszimptoták.",
              chip="A Képzelet Határa · 2/8", szakaszok=A2,
              elozo=("tananyag-hatvanyozas.html", "Hatványozás egész kitevővel"),
              kovetkezo=("feladatok-hatvanyozas.html", "Feladatok — hatványozás")))

for u in ki:
    print("✓", os.path.relpath(u, os.path.dirname(os.path.dirname(os.path.dirname(u)))))
