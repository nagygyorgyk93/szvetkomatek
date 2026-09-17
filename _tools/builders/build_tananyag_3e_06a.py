# -*- coding: utf-8 -*-
"""3e/06 — A blokk: a sorozat fogalma (A1), monotonitas es korlatossag (A2).
Mentor: Prizma. Kuldetes: A Vegtelen Mutacio."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="3e", mappa="06-indukcio-sorozatok", temakor="Matematikai indukció. Sorozatok")
FGY = "feladatok-sorozatok.html"
KUL = "A Végtelen Mutáció"
E2F = "../../2e/03-exponencialis-es-logaritmus-fuggveny/index.html"

KEK, BORO, ZOLD, PIROS, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#475569"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational, simplify, symbols, solve, nsimplify
E = []
def chk(nev, kapott, vart):
    ok = (len(kapott) == len(vart) and all(simplify(a - b) == 0 for a, b in zip(kapott, vart))) \
        if isinstance(kapott, (list, tuple)) else simplify(kapott - vart) == 0
    if not ok:
        E.append((nev, kapott, vart))

n = symbols("n", positive=True)
A = lambda k: Rational(2*k - 1, k + 2)
chk("A1-elso-ot", [A(k) for k in range(1, 6)],
    [Rational(1, 3), Rational(3, 4), 1, Rational(7, 6), Rational(9, 7)])
chk("A1-nyolcadik", A(8), Rational(15, 10))
rek = [5]
for _ in range(7):
    rek.append(2*rek[-1] - 3)
chk("A1-rekurziv", rek[:6], [5, 7, 11, 19, 35, 67])
chk("A1-rekurziv-7", rek[6], 131)
chk("A1-hanyadik-100", solve(3*n - 2 - 100, n), [34])
chk("A1-hanyadik-47", solve(3*n - 2 - 47, n), [Rational(49, 3)])
chk("A1-kviz-rekurzio", 3*4 - 1, 11)          # a_1 = 2 -> 2,5,14,41: a_2 = 3*2-1 = 5
chk("A2-kulonbseg", simplify((n + 1)/(n + 3) - n/(n + 2)), 2/((n + 2)*(n + 3)))
chk("A2-egy-per-n", [1 + Rational(1, k) for k in range(1, 5)],
    [2, Rational(3, 2), Rational(4, 3), Rational(5, 4)])
chk("A2-nem-monoton", [k*k - 10*k + 3 for k in range(1, 8)], [-6, -13, -18, -21, -22, -21, -18])
chk("A2-valtakozo", [Rational((-1)**k * k, k + 1) for k in range(1, 5)],
    [Rational(-1, 2), Rational(2, 3), Rational(-3, 4), Rational(4, 5)])
chk("A2-kviz-csokken", 1 + Rational(1, 100), Rational(101, 100))
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_PONTOK = svg_fuggvenyek(
    [], xr=(0, 9), yr=(0, 2.2), w=380, h=240, jelmagyarazat=False,
    tengely=("n", "aₙ"),
    leiras="Az aₙ = (2n − 1)/(n + 2) sorozat első nyolc tagja különálló pontokként, "
           "a pontok balról jobbra emelkednek és 2 alatt maradnak",
    pontok=[(k, float(A(k)), "", ZOLD) for k in range(1, 9)])
SVG_NO_KORLATOS = svg_fuggvenyek(
    [], xr=(0, 9), yr=(0, 1.6), w=330, h=210, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Növekvő, felülről 1-gyel korlátos sorozat pontjai",
    pontok=[(k, k/(k + 2), "", ZOLD) for k in range(1, 9)])
SVG_CSOKKEN = svg_fuggvenyek(
    [], xr=(0, 9), yr=(0, 2.6), w=330, h=210, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Csökkenő, de alulról 1-gyel korlátos sorozat pontjai",
    pontok=[(k, 1 + 1/k, "", KEK) for k in range(1, 9)])
SVG_VALTAKOZO = svg_fuggvenyek(
    [], xr=(0, 9), yr=(-1.4, 1.4), w=330, h=210, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Váltakozó előjelű, de korlátos sorozat pontjai",
    pontok=[(k, (-1)**k * k/(k + 1), "", BORO) for k in range(1, 9)])
SVG_NEM_KORLATOS = svg_fuggvenyek(
    [], xr=(0, 9), yr=(0, 11), w=330, h=210, jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Növekvő és felülről nem korlátos sorozat pontjai",
    pontok=[(k, k*k/6, "", PIROS) for k in range(1, 9)])
SVG_NEM_MONOTON = svg_fuggvenyek(
    [], xr=(0, 11), yr=(-3, 2.6), w=380, h=230, jelmagyarazat=False, tengely=("n", "aₙ"),
    egyseg=("1", "10"),
    leiras="Az aₙ = n² − 10n + 3 sorozat pontjai: előbb csökkennek, az ötödik tag után emelkednek",
    pontok=[(k, (k*k - 10*k + 3)/10, "", PIROS) for k in range(1, 11)])

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> A Kristálypára-generátor <b>lépésekben</b> dolgozik. Minden lépéshez '
         'pontosan egy mérőszám tartozik: az újonnan kicsapódó kristályréteg vastagsága. A napló '
         'ezért nem görbe, hanem <b>számozott lista</b> — és ha ki tudjuk olvasni belőle a '
         'szabályt, akkor a századik lépést is meg tudjuk mondani anélkül, hogy megvárnánk.'),
 ]),

 ("Minden sorszámhoz egy szám", [
   r'<p class="lead">A generátor naplója így néz ki: az 1. lépésnél $0{,}33$, a 2.-nál $0{,}75$, '
   r'a 3.-nál $1$… A lényeg a <b>hozzárendelés</b>: a lépés sorszámához tartozik egy szám. '
   r'Pontosan ez a sorozat.</p>',
   doboz("definicio", "A sorozat",
         r'<p><b>Sorozatnak</b> nevezzük azt a hozzárendelést, amely minden $n$ természetes számhoz '
         r'egyetlen valós számot rendel. Ez a szám a sorozat <b>$n$-edik tagja</b> (vagy általános '
         r'tagja), jele $a_n$; magát a sorozatot $(a_n)$-nel jelöljük.</p>'
         r'<p>Az $n$ a tag <b>sorszáma</b> (indexe): $a_1$ az első, $a_2$ a második tag. '
         r'Megállapodás szerint az indexelést <b>1-től</b> kezdjük.</p>',
         hid="def-sorozat"),
   doboz("pelda", "Az első tagok kiszámítása",
         r'<p>Írjuk fel az $a_n=\dfrac{2n-1}{n+2}$ sorozat első öt tagját!</p>'
         r'<p>A képletbe rendre $n=1,2,3,4,5$-öt helyettesítünk:</p>'
         r'$$a_1=\frac{1}{3},\quad a_2=\frac{3}{4},\quad a_3=\frac{5}{5}=1,\quad '
         r'a_4=\frac{7}{6},\quad a_5=\frac{9}{7} .$$'
         r'<p>Az $n$ helyére mindig a sorszám kerül — a képlet egyszerre mond el végtelen sok '
         r'adatot.</p>', hid="pelda-altalanos-tag"),
 ]),

 ("Hogyan adhatunk meg egy sorozatot?", [
   r'<p>Három úton szoktuk megadni, és mindháromnak megvan a maga haszna.</p>'
   r'<p><b>1. Az általános tag képletével.</b> Ez a leggyorsabb: bármelyik tagot egy lépésben '
   r'megkapjuk, a századikat is.</p>'
   r'<p><b>2. Rekurzívan.</b> Megadjuk a kezdőtagot, és azt a szabályt, ahogyan egy tagból a '
   r'következő adódik. Ilyenkor lépésről lépésre haladunk.</p>'
   r'<p><b>3. Felsorolással.</b> Leírjuk az első néhány tagot. Ez a legkényelmesebb — és a '
   r'legcsalókább.</p>',
   doboz("definicio", "Rekurzív megadás",
         r'<p>A sorozat <b>rekurzív</b> megadásához két dolog kell: a <b>kezdőtag</b> (esetleg az első '
         r'néhány tag), és a <b>továbblépési szabály</b>, amely megmondja, hogyan kapjuk az előző '
         r'tagból (tagokból) a következőt.</p>'
         r'<p>Például $a_1=2$ és $a_{n+1}=3a_n-1$: a sorozat $2,\ 5,\ 14,\ 41,\ \dots$ — '
         r'a kezdőtag nélkül a szabály önmagában semmit nem határoz meg.</p>',
         hid="def-rekurzio"),
   doboz("pelda", "Kristály-kamra szimuláció — a rétegek naplója",
         r'<p>A generátor naplója rekurzív: $a_1=5$, és minden további réteg az előző '
         r'kétszerese mínusz 3, azaz $a_{n+1}=2a_n-3$. Írjuk fel az első hat réteget, és '
         r'állapítsuk meg, hányadik lépésnél lépi át a vastagság a 100 egységet!</p>'
         r'<p>Lépésről lépésre haladunk:</p>'
         r'$$5,\quad 7,\quad 11,\quad 19,\quad 35,\quad 67 .$$'
         r'<p>A hatodik tag még $67$, a következő viszont $a_7=2\cdot67-3=131$: a <b>7. lépésnél</b> '
         r'lépi át a 100-at. '
         r'Rekurzív megadásnál nincs ugrás — a hetedik taghoz tényleg végig kell számolni az összes '
         r'előzőt.</p>', hid="pelda-rekurziv"),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi bemutat három számot — $3,\ 5,\ 7,\ \dots$ —, és azt állítja, hogy a következő '
         r'„nyilvánvalóan” a $9$.</p>'
         r'<p>Csakhogy ez lehet a <b>páratlan számok</b> sorozata (akkor $9$ jön), de lehet a '
         r'<b>prímszámok</b> sorozata is a 3-tól kezdve (akkor $11$). Mindkettő tökéletesen illik az '
         r'első három tagra.</p>'
         r'<p><b>A felsorolás nem definíció.</b> Egyértelművé csak a képlet vagy a rekurzív szabály '
         r'teszi a sorozatot; a felsorolásból legfeljebb <b>sejtünk</b> egy szabályt. A feladatokban '
         r'ezért mindig azt kérdezzük, melyik a <i>legegyszerűbb</i> szabály, amely illik rá.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A <b>Fibonacci-sorozat</b> rekurzív: $a_1=1$, $a_2=1$, és minden további tag az előző '
         r'kettő összege — $1, 1, 2, 3, 5, 8, 13, \dots$ Ez írja le a nyúlpárok szaporodását, a '
         r'napraforgó magjainak spirálszámait és a levelek elhelyezkedését.</p>'
         r'<p>Sorozat a havi villanyóra-állás, a törlesztőrészletek listája és egy játék '
         r'szintjeinek pontküszöbe is: mindegyiknél sorszámhoz tartozik egy szám.</p>'),
   kviz(r'Melyik sorozatot határozza meg <b>egyértelműen</b> az $a_{n+1}=3a_n-1$ szabály?',
        [r'egyiket sem — kezdőtag nélkül a szabály nem határoz meg sorozatot',
         r'a $2,\ 5,\ 14,\ 41,\dots$ sorozatot',
         r'a $3,\ 8,\ 23,\dots$ sorozatot',
         r'az $1,\ 2,\ 5,\ 14,\dots$ sorozatot'], 0,
        jo="✔ A rekurzív megadáshoz KÉT dolog kell: a kezdőtag és a továbblépési szabály. "
           "Ugyanez a szabály a₁ = 2-ből 2, 5, 14, 41-et, a₁ = 3-ból 3, 8, 23-at ad.",
        nem="✘ Mindhárom felsorolt sorozat kielégíti a szabályt — csak más a kezdőtagjuk. "
            "A rekurzív szabály önmagában, kezdőtag nélkül nem határoz meg sorozatot."),
 ]),

 ("Hányadik tag? Tagja-e egyáltalán?", [
   r'<p>Gyakori kérdés a fordítottja is: adott egy szám, és azt kérdezzük, <b>szerepel-e</b> a '
   r'sorozatban, és ha igen, hányadikként. Ilyenkor egyenletet oldunk meg — majd a megoldásról '
   r'ellenőrizzük, hogy <b>természetes szám-e</b>.</p>',
   doboz("pelda", "Tagja-e a sorozatnak?",
         r'<p>Az $a_n=3n-2$ sorozatról két kérdést teszünk fel.</p>'
         r'<p><b>a)</b> Tagja-e a $100$? Az egyenlet $3n-2=100$, ebből $3n=102$, tehát $n=34$. Ez '
         r'természetes szám, tehát a $100$ a sorozat <b>34. tagja</b>.</p>'
         r'<p><b>b)</b> Tagja-e a $47$? Most $3n-2=47$, ebből $3n=49$, azaz $n=\frac{49}{3}$. Ez '
         r'nem természetes szám, tehát a $47$ <b>nem tagja</b> a sorozatnak (a 16. tag $46$, a 17. '
         r'már $49$).</p>', hid="pelda-hanyadik"),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi kiszámolja, hogy $n=\frac{49}{3}\approx16{,}33$, és bejelenti: „a $47$ a sorozat '
         r'16,33-adik tagja”.</p>'
         r'<p>Ilyen tag nincs. A sorozatnak <b>csak egész sorszámú</b> tagjai vannak: van 16. és van '
         r'17. tag, a kettő között semmi. Ha az egyenlet megoldása tört vagy negatív, a válasz az, '
         r'hogy a szám <b>nem tagja</b> a sorozatnak.</p>'),
 ]),

 ("A sorozat grafikonja", [
   r'<p>A tagokat ábrázolhatjuk is: a vízszintes tengelyre a sorszámot, a függőlegesre a tag '
   r'értékét mérjük, és felrajzoljuk az $(n;a_n)$ pontokat. A kép ugyanazt mondja el, mint a '
   r'képlet — csak egy pillantás alatt.</p>',
   abra(SVG_PONTOK, 'Az $a_n=\\frac{2n-1}{n+2}$ sorozat első nyolc tagja. A pontok balról jobbra '
        'emelkednek, és $2$ alatt maradnak — a grafikon <b>különálló pontokból</b> áll.'),
   doboz("erdekesseg", "Sorozat és függvény",
         r'<p>A sorozat valójában <b>függvény</b>, csak az értelmezési tartománya nem intervallum, '
         r'hanem a természetes számok halmaza: külön álló, elszigetelt helyek. Ezért nincs értelme '
         r'$a_{2{,}5}$-ről beszélni, és ezért nem kötjük össze a pontokat.</p>'
         r'<p>Az <a href="' + E2F + r'">exponenciális és a logaritmusfüggvény</a> grafikonja '
         r'folytonos vonal; a sorozaté pontsor, amely „ráül” egy ilyen görbére — a vízszintes tengelyen '
         r'az $x=n$ pozitív egész helyeken. A mértani sorozatnál ezt látni is fogjuk.</p>',
         hid="erd-fuggveny"),
   kviz(r'Hogyan néz ki egy sorozat grafikonja?',
        [r'különálló pontokból áll, a sorszámok fölött',
         r'folytonos görbe, mert minden valós $x$-hez tartozik érték',
         r'törött vonal: a szomszédos tagokat szakasszal kötjük össze',
         r'vízszintes egyenes, mert a tagok egy sorban vannak'], 0,
        jo="✔ A sorozat csak természetes sorszámokon van értelmezve, ezért a grafikonja "
           "különálló pontok sora.",
        nem="✘ A sorozat értelmezési tartománya a természetes számok halmaza: az 1 és a 2 sorszám "
            "között nincs tag, tehát összekötni sincs mit. A grafikon különálló pontokból áll."),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Prizma:</b> A naplót már olvassuk. A következő kérdés viszont a védelemé: '
         'a mutáció <b>minden lépésben nő</b>, vagy néha vissza is húzódik? És van-e olyan szint, '
         'amit soha nem lép át? Ez a két kérdés dönti el, hogy a zóna tartható-e.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma:</b> Két adat kell a parancsnokságnak. Az egyik: <b>emelkedik-e</b> a görbe '
         'minden egyes lépésben — ez a monotonitás. A másik: van-e <b>olyan szint, amit a mutáció '
         'soha nem lép át</b> — ez a korlátosság. A kettő együtt mondja meg, hogy a Kristály '
         'Karantén-Zóna kitart-e.'),
 ]),

 ("Növekvő, csökkenő, se nem", [
   r'<p class="lead">A kérdés mindig két <b>szomszédos</b> tag viszonya: mi történik, ha egy '
   r'lépéssel továbbmegyünk?</p>',
   doboz("definicio", "Monoton sorozatok",
         r'<p>Az $(a_n)$ sorozat</p>'
         r'<ul>'
         r'<li><b>szigorúan monoton növekvő</b>, ha minden $n$-re $a_{n+1}\gt a_n$;</li>'
         r'<li><b>szigorúan monoton csökkenő</b>, ha minden $n$-re $a_{n+1}\lt a_n$;</li>'
         r'<li><b>monoton növekvő</b> (illetve <b>csökkenő</b>), ha a fenti egyenlőtlenségek '
         r'megengedik az egyenlőséget is ($a_{n+1}\ge a_n$, illetve $a_{n+1}\le a_n$).</li>'
         r'</ul>'
         r'<p>Ha sem az $a_{n+1}\ge a_n$, sem az $a_{n+1}\le a_n$ nem igaz az <b>összes</b> $n$-re, '
         r'a sorozat <b>nem monoton</b>. A minden $n$-re szó a lényeg: egyetlen kivétel elrontja.</p>',
         hid="def-monoton"),
   r'<p>Az $1,\ 1,\ 2,\ 2,\ 3,\ 3,\dots$ sorozat például monoton növekvő, de nem szigorúan '
   r'(vannak egyenlő szomszédok). A $7,\ 7,\ 7,\dots$ állandó sorozat egyszerre monoton növekvő és '
   r'csökkenő. A $-1,\ 1,\ -1,\ 1,\dots$ váltakozó sorozat pedig nem monoton.</p>',
 ]),

 ("Hogyan döntjük el?", [
   r'<p>Nem az első néhány tagot nézzük meg, hanem <b>általánosan</b> kiszámoljuk a szomszédos '
   r'tagok különbségét, és megvizsgáljuk az előjelét. Ha <b>minden</b> $n$-re</p>'
   r'$$a_{n+1}-a_n\gt 0,\ \text{ a sorozat szigorúan növekvő;}\qquad '
   r'a_{n+1}-a_n\lt 0,\ \text{ a sorozat szigorúan csökkenő.}$$'
   r'<p>Ha a különbség előjele $n$-től függően változik, a sorozat nem monoton.</p>',
   doboz("pelda", "A legegyszerűbb eset",
         r'<p>Az $a_n=3n-2$ sorozatnál $a_{n+1}-a_n=3(n+1)-2-(3n-2)=3$, ami minden $n$-re pozitív: '
         r'a sorozat szigorúan monoton növekvő. Ilyenkor a különbség állandó — a következő '
         r'egységben látni fogjuk, hogy ez a számtani sorozat ismertetőjele.</p>'),
   doboz("pelda", "A különbség előjele",
         r'<p>Monoton-e az $a_n=\dfrac{n}{n+2}$ sorozat?</p>'
         r'<p>Írjuk fel a következő tagot, és vonjuk ki belőle az előzőt:</p>'
         r'$$a_{n+1}-a_n=\frac{n+1}{n+3}-\frac{n}{n+2}'
         r'=\frac{(n+1)(n+2)-n(n+3)}{(n+2)(n+3)}=\frac{2}{(n+2)(n+3)} .$$'
         r'<p>A nevező minden $n$-re pozitív, a számláló $2$, tehát a különbség <b>pozitív</b>: a '
         r'sorozat szigorúan monoton növekvő. (Az első tagok: $\frac13,\ \frac12,\ \frac35,\ '
         r'\frac23,\dots$)</p>', hid="pelda-monotonitas"),
   doboz("pelda", "Kristály-kamra szimuláció — a megtévesztő szakasz",
         r'<p>A generátor egyik mérősorozata $a_n=n^2-10n+3$. Az első tagok:</p>'
         r'$$-6,\ -13,\ -18,\ -21,\ -22,\ -21,\ -18,\dots$$'
         r'<p>Az <b>ötödik tagig csökken</b>, a <b>hatodik tagtól nő</b>: a sorozat '
         r'<b>nem monoton</b>. Általánosan is látszik: '
         r'$a_{n+1}-a_n=2n-9$, ami $n\le4$ esetén negatív, $n\ge5$ esetén pozitív.</p>',
         hid="pelda-nem-monoton"),
   abra(SVG_NEM_MONOTON, 'Az $a_n=n^2-10n+3$ sorozat: a pontok előbb süllyednek, az ötödik tag után '
        'emelkednek. A függőleges tengely egy osztása $10$ egység.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi kiszámolja az első három tagot, látja, hogy csökkennek, és kijelenti: '
         r'„a mutáció visszahúzódik, a sorozat csökkenő”.</p>'
         r'<p>Ez a fenti sorozatnál éppen a csapda: az ötödik tagig tényleg csökkenés, a hatodik '
         r'tagtól viszont emelkedés. <b>Néhány tagból nem lehet monotonitást kimondani</b> — a döntéshez '
         r'az $a_{n+1}-a_n$ különbség előjelét kell megvizsgálni <i>minden</i> $n$-re.</p>'),
   kviz(r'Mi alapján dönthető el biztosan, hogy egy sorozat monoton növekvő-e?',
        [r'az $a_{n+1}-a_n$ különbség előjele minden $n$-re',
         r'az első három tag: ha nőnek, a sorozat növekvő',
         r'az első tag előjele',
         r'az, hogy a képletben szerepel-e mínuszjel'], 0,
        jo="✔ Az általánosan felírt különbség előjele minden lépésre egyszerre ad választ.",
        nem="✘ Néhány tag csak sejtést ad: az aₙ = n² − 10n + 3 sorozat öt lépésen át csökken, "
            "aztán nő. A döntés az a_{n+1} − aₙ különbség előjelén múlik."),
 ]),

 ("Korlátosság", [
   doboz("definicio", "Alsó és felső korlát",
         r'<p>A $K$ szám az $(a_n)$ sorozat <b>felső korlátja</b>, ha minden tag legfeljebb akkora: '
         r'$a_n\le K$ minden $n$-re. A $k$ szám <b>alsó korlát</b>, ha $a_n\ge k$ minden $n$-re.</p>'
         r'<p>A sorozat <b>korlátos</b>, ha van alsó és felső korlátja is, azaz minden tagja egy '
         r'$k\le a_n\le K$ „sávban” marad.</p>', hid="def-korlatos"),
   r'<p>A korlát <b>nem egyetlen szám</b>: ha $K$ felső korlát, akkor minden nála nagyobb szám is '
   r'az. Az $a_n=\frac{n}{n+2}$ sorozatnál például $1$ felső korlát, de $5$ és $100$ is — csak az '
   r'$1$ a leghasznosabb, mert az mond a legtöbbet.</p>',
   abra(SVG_CSOKKEN, 'Az $a_n=1+\\frac1n$ sorozat: $2,\\ \\frac32,\\ \\frac43,\\ \\frac54,\\dots$ — '
        'csökken, mégis minden tagja nagyobb $1$-nél.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi szerint „ami csökken, az előbb-utóbb minden határon túl süllyed, tehát alulról '
         r'nem korlátos”.</p>'
         r'<p>Az $a_n=1+\frac1n$ sorozat csökken — de minden tagja nagyobb $1$-nél, az $1$-et soha '
         r'nem éri el. Ez a sorozat <b>korlátos</b>: alulról az $1$, '
         r'felülről az első tagja, a $2$ korlátozza.</p>'
         r'<p>Fordítva ugyanez: a monoton csökkenő sorozat <b>felülről</b> mindig korlátos (az első '
         r'tagjával), a monoton növekvő pedig <b>alulról</b> — a másik irányról külön kell dönteni.</p>'),
   kviz(r'Igaz-e, hogy egy csökkenő sorozat soha nem korlátos alulról?',
        [r'nem igaz — például az $1+\frac1n$ sorozat csökken, de minden tagja nagyobb $1$-nél',
         r'igaz, mert a csökkenés előbb-utóbb minden határon túl visz',
         r'igaz, ha a sorozat minden tagja pozitív',
         r'csak akkor korlátos, ha véges sok tagja van'], 0,
        jo="✔ A csökkenés önmagában nem jelent határtalan süllyedést: a tagok „megtorpanhatnak” "
           "egy szint fölött.",
        nem="✘ Az aₙ = 1 + 1/n sorozat csökken (2; 1,5; 1,33; …), mégis minden tagja 1 fölött "
            "marad — alulról korlátos. A csökkenés és a korlátosság két külön kérdés."),
 ]),

 ("Négy sorozat, négy jellemzés", [
   r'<p>A monotonitás és a korlátosság <b>független</b> egymástól: a négy kombináció mindegyike '
   r'előfordul. Nézd meg a négy ábrát, és mondd ki magadban a jellemzést, mielőtt elolvasod a '
   r'képaláírást!</p>',
   abra(SVG_NO_KORLATOS, '<b>Növekvő és korlátos:</b> $a_n=\\frac{n}{n+2}$ — nő, de $1$ fölé nem ér.'),
   abra(SVG_CSOKKEN, '<b>Csökkenő és korlátos:</b> $a_n=1+\\frac1n$ — csökken, de $1$ alá nem megy.'),
   abra(SVG_VALTAKOZO, '<b>Nem monoton, de korlátos:</b> $a_n=(-1)^n\\frac{n}{n+1}$ — a tagok '
        'felváltva negatívak és pozitívak, de mindig a $-1$ és $1$ közötti sávban maradnak.'),
   abra(SVG_NEM_KORLATOS, '<b>Növekvő és felülről nem korlátos:</b> $a_n=\\frac{n^2}{6}$ — minden '
        'határon túl nő.'),
   r'<p>Ez a négy kép a mutáció négy forgatókönyve: az első három, korlátos sorozat kezelhető, a '
   r'negyedik nem. Épp ezért kell megtudnunk, <b>milyen szabály szerint</b> nő a láncreakció — '
   r'ez a következő két egység témája.</p>',
   GY(FGY + "#alap-7", "A 7–12", FGY + "#kozep-5", "K 5–8"),
   brief('<b>Prizma:</b> A mérések beérkeztek: a mutáció első fázisában minden lépés '
         '<b>ugyanannyit</b> tesz hozzá a kristályhoz. Ez a legegyszerűbb szabály, amit a generátor '
         'követhet — és Kanrak szerint van rá képlet, amivel a századik lépés is egyetlen sorban '
         'kiszámolható.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-sorozat-fogalma.html",
     cim="A sorozat fogalma és megadása",
     cim_tiszta="A sorozat fogalma",
     alcim="Mi a sorozat, hogyan adjuk meg képlettel és rekurzívan, hányadik tag egy adott szám, "
           "és hogyan néz ki a sorozat grafikonja.",
     chip=KUL + " · 1/5", szakaszok=A1,
     elozo=("index.html", "Matematikai indukció. Sorozatok — témakör"),
     kovetkezo=("tananyag-monotonitas-es-korlatossag.html", "Monotonitás és korlátosság")),
 lap(**T, fajl="tananyag-monotonitas-es-korlatossag.html",
     cim="Monotonitás és korlátosság",
     alcim="Mikor növekvő vagy csökkenő egy sorozat, hogyan döntjük el a szomszédos tagok "
           "különbségéből, és mit jelent az alsó és a felső korlát.",
     chip=KUL + " · 2/5", szakaszok=A2,
     elozo=("tananyag-sorozat-fogalma.html", "A sorozat fogalma"),
     kovetkezo=("tananyag-szamtani-sorozat.html", "A számtani sorozat")),
]
for u in KI:
    print("✓", os.path.basename(u))
