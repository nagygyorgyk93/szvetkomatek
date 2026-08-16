# -*- coding: utf-8 -*-
"""2e/02 — A altéma: a másodfokú egyenlet (A1–A4). Mentor: Nagol.
Küldetés: Az M-Faktor (A Parabola-csapás)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj

T = dict(tagozat="2e", mappa="02-masodfoku-egyenletek-es-fuggvenyek",
         temakor="Másodfokú egyenletek és függvények")
FGY = "feladatok-masodfoku-egyenletek.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, solve, simplify, factor, expand, im, re as _re, I, sqrt
x, m, t = symbols('x m t')
def S(e): return sorted(solve(e, x), key=lambda z: (im(z), _re(z)))
E = []
def chk(n, g, w):
    if (g != w) if isinstance(w, list) else (simplify(g - w) != 0):
        E.append((n, g, w))
chk("A1-1", S(3*x**2-27), [-3, 3]);            chk("A1-2", S(5*x**2+20*x), [-4, 0])
chk("A1-3", S(2*x**2-7*x+3), [R(1,2), 3]);     chk("A1-4", S((x-3)*(x+2)-6), [-3, 4])
chk("A1-5", S(x**2-5*x), [0, 5])
chk("A2-1", S(x**2-6*x+5), [1, 5]);            chk("A2-2", S(x**2-6*x+9), [3])
chk("A2-3", S(x**2-6*x+13), [3-2*I, 3+2*I]);   chk("A2-4", S(x**2+2*x+5), [-1-2*I, -1+2*I])
chk("A2-D", 16-4*m, 16-4*m)
chk("A3-1", S(2*x**2-10*x+8), [1, 4]);         chk("A3-2", S(x**2-7*x+10), [2, 5])
chk("A3-3", R(1,2)+R(1,5), R(7,10));           chk("A3-4", 49-2*10, 29)
chk("A3-5", expand((x+3)*(x-5)), x**2-2*x-15)
chk("A3-6", factor(2*x**2-10*x+12), 2*(x-2)*(x-3))
chk("A3-7", factor(2*x**2+5*x-3), (2*x-1)*(x+3))
chk("A4-1", solve(t**2-13*t+36, t), [4, 9]);   chk("A4-2", solve(t**2-5*t-36, t), [-4, 9])
chk("A4-3", solve(t**2+3*t-4, t), [-4, 1])
chk("A4-4", S(x**4-5*x**2-36), [-2*I, -3, 3, 2*I])
assert not E, E
print("sympy önteszt: OK")

# =====================================================================  A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Kölyök, az első félévben minden szépen sorban állt: '
         'ha nőtt a baj, <b>egyenletesen</b> nőtt. Ennek vége. Dr. Baljós új fegyvere '
         '<b>másodfokon</b> terjed — a fenyegetés nem lineárisan, hanem <b>négyzetesen</b> '
         'gyorsul. Az ilyet nem lehet átrendezéssel elintézni: fel kell darabolni. '
         'Én ehhez a karmomat használom, te a <b>megoldóképletet</b>. Ugyanaz az elv: '
         'megkeresed a gyenge pontot, és két részre vágod.'),
   'A másodfokú egyenlet a matematika egyik legjobban kidolgozott eszköze: van rá '
   '<b>képlet</b>, ami mindig működik. De mielőtt előrántanád, érdemes megnézni — sokszor '
   'sokkal gyorsabb út is van.',
 ]),

 ("A másodfokú egyenlet alakja", [
   doboz("definicio", "Másodfokú egyenlet",
         '<p>Az egyismeretlenes <b>másodfokú egyenlet</b> általános alakja</p>'
         '$$ax^{2}+bx+c=0,\\qquad a,b,c\\in\\mathbb{R},\\ a\\neq 0.$$'
         '<p>Itt $a$ a <b>főegyüttható</b>, $b$ a lineáris tag együtthatója, $c$ a '
         '<b>konstans tag</b>. Az $a\\neq 0$ kikötés lényeges: ha $a=0$ lenne, az egyenlet '
         '<b>elsőfokúvá</b> esne szét.</p>',
         hid="def-masodfoku-egyenlet"),
   doboz("erdekesseg", "Hol találkozol vele?",
         '<p>Ferde hajításnál a test pályája parabola, és a „mikor ér földet?” kérdés '
         'másodfokú egyenlet. Ugyanígy másodfokú a szabadesés úttörvénye, egy téglalap '
         'területének maximalizálása adott kerület mellett, és a fizika szinte minden '
         'olyan képlete, amelyben egy mennyiség <b>négyzete</b> szerepel.</p>'),
 ]),

 ("Hiányos másodfokú egyenletek", [
   'Ha $b=0$ vagy $c=0$ (esetleg mindkettő), az egyenletet <b>hiányosnak</b> nevezzük. '
   'Ezeket <b>nem érdemes</b> megoldóképlettel bántani — sokkal gyorsabb út is van.',
   doboz("tetel", "A három hiányos eset",
         '<p><b>1.</b> $ax^{2}=0$ &nbsp;→&nbsp; egyetlen (kettős) megoldás: $x=0$.</p>'
         '<p><b>2.</b> $ax^{2}+bx=0$ &nbsp;→&nbsp; <b>kiemelés</b>: $x(ax+b)=0$, tehát '
         '$x_{1}=0$ és $x_{2}=-\\dfrac{b}{a}$.</p>'
         '<p><b>3.</b> $ax^{2}+c=0$ &nbsp;→&nbsp; rendezés és <b>négyzetgyökvonás</b>: '
         '$x^{2}=-\\dfrac{c}{a}$, tehát $x_{1,2}=\\pm\\sqrt{-\\dfrac{c}{a}}$ — ha a jobb oldal '
         'negatív, a megoldások <b>komplexek</b>.</p>',
         hid="tetel-hianyos"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: <b>a)</b> $3x^{2}-27=0$; <b>b)</b> $5x^{2}+20x=0$.</p>',
         hid="pelda-hianyos",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $3x^{2}=27\\Rightarrow x^{2}=9\\Rightarrow x_{1,2}=\\pm 3$.</p>'
                  '<p><b>b)</b> Kiemeléssel $5x(x+4)=0$, és egy szorzat pontosan akkor nulla, '
                  'ha valamelyik tényezője nulla: $x_{1}=0$, $x_{2}=-4$.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Az $x^{2}=5x$ egyenletet a mutálódott kód így „oldja meg”: elosztja mindkét '
         'oldalt $x$-szel, és kihozza, hogy $x=5$. <b>Hibás!</b> Az osztás csak akkor '
         'megengedett, ha $x\\neq 0$ — és épp az $x=0$ is <b>megoldás</b>. '
         'Helyesen rendezünk és kiemelünk:</p>'
         '$$x^{2}-5x=0\\ \\Rightarrow\\ x(x-5)=0\\ \\Rightarrow\\ x_{1}=0,\\ x_{2}=5.$$'
         '<p><b>Ökölszabály:</b> ismeretlent tartalmazó kifejezéssel <b>soha</b> ne oszd '
         'az egyenletet — kiemelj helyette.</p>'),
   kviz('Hány valós megoldása van a $4x^{2}-9x=0$ egyenletnek?',
        ['Kettő: $0$ és $\\dfrac{9}{4}$.', 'Egy: $\\dfrac{9}{4}$.', 'Egy sem.'], 0,
        jo="✔ Kiemelés: x(4x−9)=0 → x₁=0, x₂=9/4.",
        nem="✘ Emelj ki x-et: x(4x−9)=0. Az x=0 is megoldás — ne oszd el x-szel!"),
 ]),

 ("A teljes egyenlet és a megoldóképlet", [
   'Ha mindhárom együttható nem nulla, <b>teljes</b> másodfokú egyenletről beszélünk. '
   'Ilyenkor jön a nehéztüzérség.',
   doboz("tetel", "A megoldóképlet",
         '<p>Az $ax^{2}+bx+c=0$ ($a\\neq 0$) egyenlet megoldásai</p>'
         '$$x_{1,2}=\\frac{-b\\pm\\sqrt{b^{2}-4ac}}{2a}.$$',
         hid="tetel-megoldokeplet",
         lenyilo=("Honnan jön? — teljes négyzetté alakítás",
                  '<p>Osszunk $a$-val, majd egészítsük ki teljes négyzetté:</p>'
                  '$$x^{2}+\\frac{b}{a}x+\\frac{c}{a}=0'
                  '\\ \\Rightarrow\\ \\left(x+\\frac{b}{2a}\\right)^{2}'
                  '=\\frac{b^{2}}{4a^{2}}-\\frac{c}{a}=\\frac{b^{2}-4ac}{4a^{2}}.$$'
                  '<p>Innen gyököt vonva $x+\\dfrac{b}{2a}=\\pm\\dfrac{\\sqrt{b^{2}-4ac}}{2a}$, '
                  'és átrendezve épp a megoldóképletet kapjuk. Vagyis a képlet nem varázslat: '
                  'a teljes négyzetté alakítás <b>egyszer s mindenkorra</b> elvégzett változata.</p>')),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: $2x^{2}-7x+3=0$.</p>',
         hid="pelda-teljes",
         lenyilo=("Megoldás",
                  '<p>$a=2$, $b=-7$, $c=3$, tehát $b^{2}-4ac=49-24=25$, és $\\sqrt{25}=5$:</p>'
                  '$$x_{1,2}=\\frac{7\\pm 5}{4}\\ \\Rightarrow\\ x_{1}=3,\\quad '
                  'x_{2}=\\frac{1}{2}.$$'
                  '<p><b>Ellenőrzés:</b> $2\\cdot 9-21+3=0$ ✔</p>')),
 ]),

 ("Amikor nem látszik, hogy másodfokú", [
   'A feladatok jó része <b>nem</b> rendezett alakban érkezik. Az első lépés mindig ugyanaz: '
   'bontsd fel a zárójeleket, vonj össze, és rendezz nullára.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: $(x-3)(x+2)=6$.</p>',
         hid="pelda-rendezes",
         lenyilo=("Megoldás",
                  '<p>Kibontva $x^{2}-x-6=6$, rendezve $x^{2}-x-12=0$. '
                  'Itt $D=1+48=49$, $\\sqrt{49}=7$:</p>'
                  '$$x_{1,2}=\\frac{1\\pm 7}{2}\\ \\Rightarrow\\ x_{1}=4,\\quad x_{2}=-3.$$')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A mutálódott kód a $(x-3)(x+2)=6$ egyenletre azt írja: „szorzat, tehát '
         '$x-3=6$ vagy $x+2=6$". <b>Hibás!</b> A „szorzat = 0” szabály <b>kizárólag</b> '
         'akkor működik, ha a jobb oldalon <b>nulla</b> áll. Hatnak végtelen sok '
         'szorzatfelbontása van — nullának viszont csak úgy, ha valamelyik tényező nulla.</p>'),
   kviz('Melyik lépés helyes elsőként az $(x+1)(x-4)=6$ egyenletnél?',
        ['Kibontás és rendezés nullára.',
         '$x+1=6$ és $x-4=6$ külön megoldása.',
         'Osztás $(x-4)$-gyel.'], 0,
        jo="✔ A „szorzat = 0” szabály csak nulla jobb oldal mellett használható.",
        nem="✘ A jobb oldal nem nulla, ezért előbb ki kell bontani és rendezni: x²−3x−10=0."),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Nagol:</b> Megvan a képlet. De nekem nem elég <b>megoldani</b> — előre '
         'tudni akarom, <b>mi vár rám</b>, mielőtt belemegyek. Van a képletben egy szám, '
         'a gyökjel alatt, ami mindent elárul: hány megoldás lesz, és egyáltalán '
         'valósak-e. Ez a következő lecke.',
         outro=True),
 ]),
]

# =====================================================================  A2

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> A jó felderítő nem akkor tudja meg, hogy csapdába sétált, '
         'amikor már benne van. A megoldóképlet gyökjele alatt álló szám — a '
         '<b>diszkrimináns</b> — egyetlen számolással megmondja, mi vár rád: két '
         'különböző megoldás, egyetlen kettős, vagy olyan gyökök, amelyek kiléptek '
         'a valós világból. Dr. Baljós paraméteres egyenletei pontosan ezen a ponton támadnak.'),
   'A „diszkriminál” szó itt a régi értelmében szerepel: <b>megkülönböztet</b>. '
   'Ez a szám különbözteti meg egymástól a három lehetséges esetet.',
 ]),

 ("Mi a diszkrimináns?", [
   doboz("definicio", "Diszkrimináns",
         '<p>Az $ax^{2}+bx+c=0$ egyenlet — ahol $a\\neq 0$ — <b>diszkriminánsa</b></p>'
         '$$D=b^{2}-4ac.$$'
         '<p>A megoldóképlet ezzel $x_{1,2}=\\dfrac{-b\\pm\\sqrt{D}}{2a}$ alakot ölt — '
         'látszik, hogy minden a $\\sqrt{D}$-n múlik.</p>',
         hid="def-diszkriminans"),
 ]),

 ("A megoldások természete", [
   doboz("tetel", "Három eset",
         '<p><b>$D&gt;0$:</b> $\\sqrt{D}$ pozitív valós szám → <b>két különböző valós</b> megoldás.</p>'
         '<p><b>$D=0$:</b> $\\sqrt{D}=0$ → <b>egy (kettős)</b> valós megoldás, '
         '$x_{1}=x_{2}=-\\dfrac{b}{2a}$.</p>'
         '<p><b>$D&lt;0$:</b> negatív szám gyöke a valósban nincs → <b>két konjugált komplex</b> '
         'megoldás. (A <a href="../01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-komplex-szam-fogalma.html">komplex számok</a> után ez már nem akadály!)</p>',
         hid="tetel-megoldasok-termeszete"),
   doboz("pelda", "Vészterem-szimuláció — mindhárom eset",
         '<p>Vizsgáld meg és oldd meg: <b>a)</b> $x^{2}-6x+5=0$; <b>b)</b> $x^{2}-6x+9=0$; '
         '<b>c)</b> $x^{2}-6x+13=0$.</p>',
         hid="pelda-harom-eset",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $D=36-20=16&gt;0$ → $x_{1,2}=\\dfrac{6\\pm 4}{2}$, tehát '
                  '$x_{1}=5$, $x_{2}=1$.</p>'
                  '<p><b>b)</b> $D=36-36=0$ → $x_{1}=x_{2}=3$ (kettős gyök).</p>'
                  '<p><b>c)</b> $D=36-52=-16&lt;0$ → $\\sqrt{-16}$ helyett $4i$-vel számolunk: '
                  '$x_{1,2}=\\dfrac{6\\pm 4i}{2}=3\\pm 2i$.</p>'
                  '<p>Figyeld meg: a három egyenlet csak a konstans tagban különbözik — '
                  'mégis három egészen más eredmény.</p>')),
   kviz('Mennyi az $x^{2}+4x+4=0$ egyenlet diszkriminánsa, és mit jelent?',
        ['$D=0$ — egy kettős valós gyök.', '$D=16$ — két valós gyök.',
         '$D=-16$ — két komplex gyök.'], 0,
        jo="✔ D = 16 − 16 = 0, tehát x = −2 kettős gyök.",
        nem="✘ D = 4² − 4·1·4 = 0 → egyetlen (kettős) valós gyök, x = −2."),
 ]),

 ("Paraméteres feladatok", [
   'A vizsgahelyzetek kedvence: az egyenletben egy <b>paraméter</b> szerepel, és arra '
   'kérdeznek rá, mikor hányféle megoldás van. A recept mindig ugyanaz: '
   '<b>írd fel $D$-t a paraméterrel</b>, aztán oldd meg a $D&gt;0$, $D=0$, $D&lt;0$ '
   'egyenlőtlenségeket.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Az $m$ paraméter mely értékeire van az $x^{2}-4x+m=0$ egyenletnek két '
         'különböző valós megoldása? Mikor van egy kettős, és mikor komplex?</p>',
         hid="pelda-parameteres",
         lenyilo=("Megoldás",
                  '<p>$D=(-4)^{2}-4\\cdot 1\\cdot m=16-4m$.</p>'
                  '<p>$16-4m&gt;0\\iff m&lt;4$ → két különböző valós megoldás.</p>'
                  '<p>$16-4m=0\\iff m=4$ → egy kettős megoldás ($x=2$).</p>'
                  '<p>$16-4m&lt;0\\iff m&gt;4$ → két konjugált komplex megoldás.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Ha a paraméter a <b>főegyütthatóban</b> áll, egy külön esetet is meg kell '
         'vizsgálni. Például az $(m-2)x^{2}+4x+1=0$ egyenlet <b>nem másodfokú</b>, ha '
         '$m=2$ — akkor a $4x+1=0$ elsőfokú egyenletet kapjuk, egyetlen megoldással '
         '($x=-\\tfrac14$). A diszkriminánst tehát csak $m\\neq 2$ mellett szabad használni.</p>'
         '<p><b>Ellenőrző kérdés minden paraméteres feladatnál:</b> hol áll a paraméter? '
         'Ha a főegyütthatóban, akkor van egy „elfajuló” eset is.</p>'),
 ]),

 ("Amikor a gyökök komplexek", [
   'A $D&lt;0$ eset korábban azt jelentette: „nincs megoldás”. A '
   '<a href="../01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-komplex-szam-fogalma.html">komplex számok</a> '
   'bevezetése után már tudjuk, hogy <b>van</b> — csak nem a valós számok között.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg a komplex számok halmazán: $x^{2}+2x+5=0$.</p>',
         hid="pelda-komplex-gyokok",
         lenyilo=("Megoldás",
                  '<p>$D=4-20=-16$. Negatív szám négyzetgyöke a valós számok között nem értelmezett — a komplex számok halmazán viszont keresünk olyan számot, amelynek a négyzete $-16$. Ilyen a $4i$, hiszen $(4i)^{2}=16i^{2}=-16$. A megoldóképletbe tehát ezt írjuk:</p>'
                  '$$x_{1,2}=\\frac{-2\\pm 4i}{2}=-1\\pm 2i.$$'
                  '<p><b>Ellenőrzés:</b> $(-1+2i)^{2}+2(-1+2i)+5=(1-4i-4)+(-2+4i)+5=0$ ✔</p>')),
   doboz("erdekesseg", "A gyökök mindig párban járnak",
         '<p>Ha egy <b>valós együtthatós</b> másodfokú egyenletnek van komplex gyöke, akkor '
         'a másik gyök annak <b>konjugáltja</b>: ha $x_{1}=p+qi$, akkor $x_{2}=p-qi$. '
         'Ez a megoldóképletből azonnal látszik — a $\\pm$ jel csak a képzetes rész '
         'előjelét fordítja meg.</p>'),
   kviz('Az $x^{2}-2x+10=0$ egyenlet egyik gyöke $1+3i$. Mi a másik?',
        ['$1-3i$', '$-1-3i$', '$-1+3i$'], 0,
        jo="✔ Valós együtthatóknál a komplex gyökök konjugált párt alkotnak.",
        nem="✘ A megoldóképlet ± jele csak a képzetes rész előjelét váltja: 1 − 3i."),
   gyakorolj(FGY + "#alap-7", "A 7–10", FGY + "#kozep-5", "K 5–8"),
   brief('<b>Nagol:</b> Most jön a rész, amit a legjobban szeretek. Kiderül, hogy '
         'a gyököket <b>nem is kell kiszámolni</b> ahhoz, hogy tudjunk róluk. Az összegük '
         'és a szorzatuk közvetlenül az együtthatókból leolvasható — és ezzel az egész '
         'egyenletet darabokra lehet szedni.',
         outro=True),
 ]),
]

# =====================================================================  A3

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Van egy trükk, amit François Viète francia matematikus talált ki '
         'a 16. században, és azóta minden vizsgázó hálás érte. A gyökök <b>összege</b> és '
         '<b>szorzata</b> ránézésre kiolvasható az együtthatókból — megoldóképlet nélkül. '
         'Ez nemcsak gyorsít: ezzel lehet <b>szétvágni</b> a másodfokú kifejezést két '
         'elsőfokú tényezőre. Az én szakterületem.'),
 ]),

 ("A Viète-képletek", [
   doboz("tetel", "Viète-képletek",
         '<p>Ha az $ax^{2}+bx+c=0$ egyenlet gyökei $x_{1}$ és $x_{2}$, akkor</p>'
         '$$x_{1}+x_{2}=-\\frac{b}{a},\\qquad x_{1}\\cdot x_{2}=\\frac{c}{a}.$$'
         '<p>Az $x^{2}+px+q=0$ alakú (normált) egyenletnél még egyszerűbb: '
         '$x_{1}+x_{2}=-p$ és $x_{1}x_{2}=q$.</p>',
         hid="tetel-viete",
         lenyilo=("Levezetés",
                  '<p>A megoldóképletből $x_{1}=\\dfrac{-b+\\sqrt D}{2a}$ és '
                  '$x_{2}=\\dfrac{-b-\\sqrt D}{2a}$. Összeadva a $\\sqrt D$ kiesik:</p>'
                  '$$x_{1}+x_{2}=\\frac{-2b}{2a}=-\\frac{b}{a}.$$'
                  '<p>Összeszorozva a négyzetek különbsége azonosságot használjuk:</p>'
                  '$$x_{1}x_{2}=\\frac{b^{2}-D}{4a^{2}}=\\frac{b^{2}-(b^{2}-4ac)}{4a^{2}}'
                  '=\\frac{4ac}{4a^{2}}=\\frac{c}{a}.$$'
                  '<p>Figyeld meg: a levezetés <b>nem használta</b>, hogy $D\\ge0$ — '
                  'a képletek a komplex gyökökre is érvényesek.</p>')),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Ellenőrizd a Viète-képleteket a $2x^{2}-10x+8=0$ egyenleten!</p>',
         lenyilo=("Megoldás",
                  '<p>A képletek szerint $x_{1}+x_{2}=\\dfrac{10}{2}=5$ és '
                  '$x_{1}x_{2}=\\dfrac{8}{2}=4$. Megoldva: $D=100-64=36$, '
                  '$x_{1,2}=\\dfrac{10\\pm 6}{4}$, tehát $x_{1}=4$ és $x_{2}=1$. '
                  'Valóban $4+1=5$ és $4\\cdot 1=4$ ✔</p>')),
 ]),

 ("Szimmetrikus kifejezések — számolás gyökök nélkül", [
   'A Viète-képletek igazi haszna: olyan kifejezéseket is ki tudunk számolni, amelyekben '
   'a két gyök <b>szimmetrikusan</b> szerepel — anélkül, hogy a gyököket megkeresnénk. '
   'A trükk: alakítsuk át a kifejezést úgy, hogy csak az <b>összeg</b> és a <b>szorzat</b> '
   'szerepeljen benne.',
   doboz("tetel", "A két leggyakoribb átalakítás",
         '<p>Az elsőhöz kell, hogy egyik gyök se legyen $0$ — ez pontosan azt jelenti, hogy '
         '$c\\neq 0$, hiszen $x_{1}x_{2}=\\dfrac{c}{a}$.</p>'
         '$$\\frac{1}{x_{1}}+\\frac{1}{x_{2}}=\\frac{x_{1}+x_{2}}{x_{1}x_{2}}\\qquad(c\\neq 0)$$'
         '$$x_{1}^{2}+x_{2}^{2}=\\left(x_{1}+x_{2}\\right)^{2}-2x_{1}x_{2}$$'
         '<p>A második az $(u+v)^{2}=u^{2}+2uv+v^{2}$ azonosság átrendezése. '
         'Hasonlóan: $\\left(x_{1}-x_{2}\\right)^{2}=\\left(x_{1}+x_{2}\\right)^{2}-4x_{1}x_{2}$.</p>',
         hid="tetel-szimmetrikus"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Az $x^{2}-7x+10=0$ egyenlet megoldása <b>nélkül</b> számítsd ki: '
         '<b>a)</b> $\\dfrac{1}{x_{1}}+\\dfrac{1}{x_{2}}$; <b>b)</b> $x_{1}^{2}+x_{2}^{2}$.</p>',
         hid="pelda-szimmetrikus",
         lenyilo=("Megoldás",
                  '<p>Viète: $x_{1}+x_{2}=7$, $x_{1}x_{2}=10$.</p>'
                  '<p><b>a)</b> $\\dfrac{x_{1}+x_{2}}{x_{1}x_{2}}=\\dfrac{7}{10}$.</p>'
                  '<p><b>b)</b> $7^{2}-2\\cdot 10=49-20=29$.</p>'
                  '<p>(Ellenőrzésképp a gyökök $2$ és $5$: '
                  '$\\tfrac12+\\tfrac15=\\tfrac{7}{10}$ ✔ és $4+25=29$ ✔)</p>')),
   kviz('Egy másodfokú egyenlet gyökeinek összege $9$, szorzata $20$. Melyik az egyenlet?',
        ['$x^{2}-9x+20=0$', '$x^{2}+9x+20=0$', '$x^{2}-9x-20=0$'], 0,
        jo="✔ A gyökökből felírt alak x² − (összeg)·x + (szorzat) = 0, tehát x² − 9x + 20 = 0.",
        nem="✘ Figyelj az előjelre: az összeg MÍNUSSZAL, a szorzat PLUSSZAL kerül be: "
            "x² − 9x + 20 = 0. (A gyökök 4 és 5.)"),
 ]),

 ("Egyenlet felírása adott gyökökből", [
   'A Viète-képletek visszafelé is működnek: ha ismerem a két gyököt, fel tudom írni '
   'az egyenletet.',
   doboz("tetel", "Az egyenlet a gyökeiből",
         '<p>Ha a keresett gyökök $x_{1}$ és $x_{2}$, akkor</p>'
         '$$x^{2}-\\left(x_{1}+x_{2}\\right)x+x_{1}x_{2}=0$$'
         '<p>egy megfelelő egyenlet. (Bármely nem nulla számmal szorozva szintén jó.)</p>',
         hid="tetel-egyenlet-gyokokbol"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Írj fel másodfokú egyenletet, amelynek gyökei $-3$ és $5$!</p>',
         lenyilo=("Megoldás",
                  '<p>Az összeg $-3+5=2$, a szorzat $-3\\cdot 5=-15$, tehát</p>'
                  '$$x^{2}-2x-15=0.$$')),
 ]),

 ("A másodfokú trinom szorzattá bontása", [
   'Most jön a „szétvágás”. Ha ismerjük a gyököket, a másodfokú kifejezés két elsőfokú '
   'tényező szorzatára esik szét.',
   doboz("tetel", "Szorzattá alakítás",
         '<p>Ha az $ax^{2}+bx+c$ trinom gyökei $x_{1}$ és $x_{2}$, akkor</p>'
         '$$ax^{2}+bx+c=a\\left(x-x_{1}\\right)\\left(x-x_{2}\\right).$$'
         '<p><b>Mikor ad ez valós tényezőket?</b> Akkor, ha $D\\ge 0$ — vagyis ha vannak valós gyökök. Ha $D&lt;0$, a trinom a <b>valós</b> számok körében <b>nem</b> bontható két elsőfokú tényezőre; a fenti alak ilyenkor is felírható, de a gyökök konjugált komplex párt alkotnak.</p>',
         hid="tetel-szorzatta-alakitas"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>„Minden másodfokú kifejezés felbontható két zárójel szorzatára.” — <b>A valós számok körében nem.</b> Nézd meg az $x^{2}+1$ kifejezést: $D=0-4=-4&lt;0$, tehát nincs valós gyöke — a grafikonja végig az $x$ tengely fölött halad, sehol nem metszi.</p>'
         '<p>Mielőtt tényezőkre bontasz, <b>számold ki a diszkriminánst</b>. Ha negatív, a valós körben készen vagy: a kifejezés tovább nem bontható.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Bontsd tényezőkre: <b>a)</b> $x^{2}-x-12$; <b>b)</b> $2x^{2}-10x+12$.</p>',
         hid="pelda-szorzatta",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $D=1+48=49$, a gyökök $4$ és $-3$, a főegyüttható $1$:</p>'
                  '$$x^{2}-x-12=(x-4)(x+3).$$'
                  '<p><b>b)</b> $D=100-96=4$, a gyökök $3$ és $2$, a főegyüttható $2$:</p>'
                  '$$2x^{2}-10x+12=2(x-3)(x-2).$$')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A mutálódott kód a $2x^{2}+5x-3$ bontását így írja: gyökök $\\tfrac12$ és $-3$, '
         'tehát $\\left(x-\\tfrac12\\right)(x+3)$. <b>Hiányos!</b> A <b>főegyüttható</b> '
         'lemaradt — így a szorzat kibontva $x^{2}+\\tfrac52x-\\tfrac32$ lenne, nem az '
         'eredeti. Helyesen:</p>'
         '$$2x^{2}+5x-3=2\\left(x-\\tfrac12\\right)(x+3)=(2x-1)(x+3).$$'
         '<p>Az utolsó lépésben a $2$-t „beszoroztuk” az első tényezőbe — így szebb az alak.</p>'),
   kviz('Bontsd tényezőkre: $x^{2}-9x+20$.',
        ['$(x-4)(x-5)$', '$(x+4)(x+5)$', '$(x-2)(x-10)$'], 0,
        jo="✔ A gyökök 4 és 5; az összegük 9, a szorzatuk 20.",
        nem="✘ Keresd azt a két számot, amelynek összege 9 és szorzata 20: ezek a 4 és az 5."),
   gyakorolj(FGY + "#alap-11", "A 11–15", FGY + "#kozep-9", "K 9–13"),
   brief('<b>Nagol:</b> Utolsó kör az egyenletekből. Dr. Baljós néha <b>negyedfokú</b> '
         'kódot küld — de ha jól nézed, az is csak egy másodfokú, álruhában. '
         'Egyetlen jó helyettesítés, és összeomlik.',
         outro=True),
 ]),
]

# =====================================================================  A4

A4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Ez a kód négyzetre emelt négyzeteket tartalmaz — '
         '$x^{4}$-es tagot. Ne ijedj meg tőle. Ha a kitevők <b>4, 2 és 0</b> — vagyis csak '
         '$x^{4}$, $x^{2}$ és konstans áll az egyenletben —, egyetlen új ismeretlen '
         'bevezetésével visszavezetheted arra, amit már tudsz. '
         'A neve <b>bikvadratikus</b>, és a leggyakoribb hiba nem a megoldásában, '
         'hanem a <b>visszahelyettesítésben</b> van.'),
 ]),

 ("Új ismeretlen bevezetése ($t=x^{2}$)", [
   doboz("definicio", "Bikvadratikus egyenlet",
         '<p><b>Bikvadratikusnak</b> nevezzük az</p>'
         '$$ax^{4}+bx^{2}+c=0,\\qquad a\\neq 0$$'
         '<p>alakú egyenletet. Csak <b>páros</b> kitevők szerepelnek benne — épp ezért '
         'lehet másodfokúra visszavezetni.</p>',
         hid="def-bikvadratikus"),
   doboz("tetel", "Az eljárás",
         '<p><b>1.</b> Vezessük be a $t=x^{2}$ új ismeretlent. Valós $x$ esetén $t=x^{2}\\ge 0$ — ezt a végén meg kell nézni. Ekkor $x^{4}=t^{2}$, és az '
         'egyenlet $at^{2}+bt+c=0$ alakú — <b>közönséges másodfokú</b>.</p>'
         '<p><b>2.</b> Oldjuk meg $t$-re.</p>'
         '<p><b>3.</b> <b>Helyettesítsünk vissza:</b> minden kapott $t$ értékre oldjuk meg '
         'az $x^{2}=t$ egyenletet. Ez $t&gt;0$ esetén <b>két</b> valós megoldást ad '
         '($x=\\pm\\sqrt{t}$), $t=0$ esetén <b>egyet</b> ($x=0$), $t&lt;0$ esetén '
         'pedig a valós számok között <b>egyet sem</b>.</p>'
         '<p>Valós megoldásból tehát $0$, $1$, $2$, $3$ vagy $4$ lehet — például az '
         '$x^{4}-4x^{2}=0$ egyenletnek <b>három</b> valós gyöke van: $0$ és $\\pm 2$.</p>',
         hid="tetel-bikvadratikus"),
   kviz('A bikvadratikus egyenletnél $t=x^{2}$ helyettesítéssel $t=-4$ adódik. Mit jelent ez?',
        ['Ebből nem jön valós $x$', 'Ebből $x=-2$ jön', 'Ebből $x=\\pm 2$ jön'], 0,
        jo="✔ Az x² = −4 egyenletnek nincs valós megoldása, mert négyzet nem lehet negatív. "
           "A t negatív értékeit tehát a valós körben elvetjük.",
        nem="✘ A visszahelyettesítés x² = −4 alakú: ennek NINCS valós megoldása. "
            "Csak a nemnegatív t értékekből kapunk valós x-et."),
 ]),

 ("Kidolgozott példák", [
   doboz("pelda", "Vészterem-szimuláció — négy valós gyök",
         '<p>Oldd meg: $x^{4}-13x^{2}+36=0$.</p>',
         hid="pelda-bikv-valos",
         lenyilo=("Megoldás",
                  '<p>Legyen $t=x^{2}$: $t^{2}-13t+36=0$, ahol $D=169-144=25$, tehát</p>'
                  '$$t_{1,2}=\\frac{13\\pm 5}{2}\\ \\Rightarrow\\ t_{1}=9,\\quad t_{2}=4.$$'
                  '<p>Visszahelyettesítve: $x^{2}=9\\Rightarrow x=\\pm 3$, és '
                  '$x^{2}=4\\Rightarrow x=\\pm 2$.</p>'
                  '<p><b>Négy megoldás:</b> $-3,\\ -2,\\ 2,\\ 3$.</p>')),
   doboz("pelda", "Vészterem-szimuláció — komplex gyökökkel",
         '<p>Oldd meg a komplex számok halmazán: $x^{4}-5x^{2}-36=0$.</p>',
         hid="pelda-bikv-komplex",
         lenyilo=("Megoldás",
                  '<p>$t=x^{2}$: $t^{2}-5t-36=0$, $D=25+144=169$:</p>'
                  '$$t_{1,2}=\\frac{5\\pm 13}{2}\\ \\Rightarrow\\ t_{1}=9,\\quad t_{2}=-4.$$'
                  '<p>$x^{2}=9\\Rightarrow x=\\pm 3$ (valós), és $x^{2}=-4\\Rightarrow x=\\pm 2i$ '
                  '(komplex).</p>'
                  '<p><b>Négy megoldás:</b> $\\pm 3$ és $\\pm 2i$.</p>')),
 ]),

 ("A visszahelyettesítés buktatói", [
   doboz("erdekesseg", "A módszer ennél tágabb",
         '<p>Nem csak az $x^{2}$-et nevezhetjük $t$-nek — bármit, ami az egyenletben <b>négyzeten és elsőfokon</b> is szerepel. Ha például $\\left(x^{2}-3\\right)^{2}-5\\left(x^{2}-3\\right)+6=0$, legyen $t=x^{2}-3$: így $t^{2}-5t+6=0$, ahonnan $t_{1}=2$ és $t_{2}=3$ — és utána <b>mindkettőt</b> vissza kell helyettesíteni ($x^{2}-3=2$, illetve $x^{2}-3=3$).</p>'
         '<p>Ugyanez a fogás működik $\\sqrt{x}=t$ helyettesítéssel is; ott a kikötés $t\\ge 0$.</p>'),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Két klasszikus hiba:</p>'
         '<ol class="reszfeladatok">'
         '<li><b>Megállni $t$-nél.</b> A kód azt írja: „a megoldások $9$ és $4$”. '
         'Nem — azok a <b>segédismeretlen</b> értékei! A kérdés $x$-re szólt, tehát '
         'vissza kell helyettesíteni.</li>'
         '<li><b>Elhagyni a ± jelet.</b> Az $x^{2}=9$ egyenletnek <b>két</b> megoldása van, '
         'nem egy. Egy bikvadratikus egyenletnek — a komplexeket is beleszámítva — '
         'mindig <b>négy</b> gyöke van (a többszörösöket többszörösen számolva).</li>'
         '</ol>'),
   doboz("erdekesseg", "Ha csak valós megoldást keresünk",
         '<p>Ha a feladat kifejezetten a <b>valós</b> megoldásokat kéri, a negatív $t$ '
         'értékeket egyszerűen elvetjük (hiszen $x^{2}\\ge 0$ minden valós $x$-re). '
         'A komplex számok halmazán viszont ezek is gyököket adnak — mostantól tehát '
         '<b>oda kell figyelni, melyik halmazon dolgozunk</b>.</p>'),
   kviz('Hány megoldása van az $x^{4}+3x^{2}-4=0$ egyenletnek a valós számok halmazán?',
        ['Kettő: $\\pm 1$.', 'Négy: $\\pm 1$ és $\\pm 2$.', 'Egy sem.'], 0,
        jo="✔ t = 1 vagy t = −4; csak a t = 1 ad valós x-et: ±1.",
        nem="✘ t² + 3t − 4 = 0 → t = 1 vagy t = −4. A t = −4-hez nincs valós x, tehát csak ±1."),
   gyakorolj(FGY + "#alap-16", "A 16–18", FGY + "#kozep-14", "K 14–16"),
   brief('<b>Küklopsz:</b> Nagol elvégezte a durva munkát — innen én veszem át. '
         'Eddig azt kérdeztük: <b>hol nulla</b> a kifejezés. Most azt fogjuk kérdezni: '
         '<b>hogyan viselkedik mindenütt</b>. Az optikai sugaraim röppályája ugyanaz a görbe, '
         'mint amit a másodfokú függvény rajzol — és ha ismered a görbét, egyetlen '
         'pillantással látod azt is, amit az egyenlet csak hosszú számolás után árul el.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-masodfoku-egyenlet.html",
     cim="A másodfokú egyenlet", cim_tiszta="A másodfokú egyenlet",
     alcim="Az egyenlet alakja, a hiányos esetek gyors megoldása, a megoldóképlet "
           "és annak levezetése, valamint a rendezést igénylő feladatok.",
     chip="Az M-Faktor · 1/8", szakaszok=A1,
     elozo=("index.html", "Témakör-nyitó"),
     kovetkezo=("tananyag-diszkriminans.html", "A diszkrimináns")),
 lap(**T, fajl="tananyag-diszkriminans.html",
     cim="A diszkrimináns", cim_tiszta="A diszkrimináns",
     alcim="A $D=b^{2}-4ac$ szám és a megoldások természete, paraméteres feladatok, "
           "valamint a komplex gyökpárok.",
     chip="Az M-Faktor · 2/8", szakaszok=A2,
     elozo=("tananyag-masodfoku-egyenlet.html", "A másodfokú egyenlet"),
     kovetkezo=("tananyag-viete-es-szorzatta-alakitas.html", "Viète-képletek és szorzattá alakítás")),
 lap(**T, fajl="tananyag-viete-es-szorzatta-alakitas.html",
     cim="Viète-képletek és szorzattá alakítás",
     cim_tiszta="Viète-képletek és szorzattá alakítás",
     alcim="A gyökök összege és szorzata az együtthatókból, szimmetrikus kifejezések "
           "számolása, egyenlet felírása a gyökeiből és a trinom tényezőkre bontása.",
     chip="Az M-Faktor · 3/8", szakaszok=A3,
     elozo=("tananyag-diszkriminans.html", "A diszkrimináns"),
     kovetkezo=("tananyag-bikvadratikus.html", "Másodfokúra visszavezethető egyenletek")),
 lap(**T, fajl="tananyag-bikvadratikus.html",
     cim="Másodfokúra visszavezethető egyenletek",
     cim_tiszta="Másodfokúra visszavezethető egyenletek",
     alcim="A bikvadratikus egyenlet és a $t=x^{2}$ helyettesítés, a visszahelyettesítés "
           "buktatói, valós és komplex gyökök.",
     chip="Az M-Faktor · 4/8", szakaszok=A4,
     elozo=("tananyag-viete-es-szorzatta-alakitas.html", "Viète-képletek és szorzattá alakítás"),
     kovetkezo=(FGY, "Feladatok — másodfokú egyenletek")),
]
for u in KI:
    print("✓", os.path.basename(u))
