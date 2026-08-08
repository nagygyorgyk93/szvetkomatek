# -*- coding: utf-8 -*-
"""2e/03 — B altema: a logaritmus fogalma (B1), azonossagai (B2), attetes mas alapra
es alkalmazasok (B3). Mentor: Dr. Bestia."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="2e", mappa="03-exponencialis-es-logaritmus-fuggveny",
         temakor="Exponenciális és logaritmusfüggvény")
FGY = "feladatok-logaritmus.html"

# ---------------------------------------------------------------- önteszt
from sympy import symbols, Rational as R, log, N, simplify, solve, nsimplify
x = symbols('x', real=True)
E = []
def chk(n, g, w, tol=None):
    if tol is not None:
        if abs(float(g) - w) > tol:
            E.append((n, float(g), w))
    elif simplify(g - w) != 0:
        E.append((n, g, w))
chk("B1-1", log(8, 2), 3);            chk("B1-2", log(R(1, 9), 3), -2)
chk("B1-3", log(1, 7), 0);            chk("B1-4", log(5, 5), 1)
chk("B1-5", log(R(1, 32), 2), -5);    chk("B1-6", log(100, 10), 2)
chk("B1-7", log(2, 4), R(1, 2));      chk("B1-8", log(27, R(1, 3)), -3)
chk("B2-1", log(6, 2) - (log(2, 2) + log(3, 2)), 0)
chk("B2-2", log(3, 5) + log(75, 5), 2 + 2*log(3, 5))
chk("B2-3", log(1000, 10) - log(10, 10), 2)
chk("B2-4", log(32, 2), 5);           chk("B2-5", 2*log(9, 3), 4)
chk("B2-6", log(R(64), 4), 3)
chk("B2-pelda", log(50, 10) + log(2, 10), 2)
chk("B2-pelda2", log(48, 2) - log(3, 2), 4)
chk("B3-1", N(log(12, 11)), 1.03628656263, 1e-9)
chk("B3-2", N(log(23, 7)), 1.61132528008, 1e-9)
chk("B3-3", N(log(1000000, 2)), 19.9315685693, 1e-9)
chk("B3-4", N(log(2)/log(R(105, 100))), 14.2066990829, 1e-8)
chk("B3-5", log(R(1, 8), R(1, 2)), 3)
assert not E, E
print("sympy önteszt: OK")

# ===================================================================== B1

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> Az előző küldetésben azt kérdeztük: <i>mennyi lesz a fertőzött '
         'sejtek száma $x$ óra múlva?</i> A válasz $2^{x}$ volt. De a valódi kérdés a labor '
         'szempontjából fordított: <b>hány óra kell ahhoz</b>, hogy elérje a milliót? '
         'Ez az $x$ a <b>kitevőben</b> ül, és eddig csak akkor tudtuk kihalászni, ha '
         'a két oldal szerencsésen közös alapra hozható volt. Most kapunk egy eszközt, '
         'amely <b>mindig</b> működik: a <b>logaritmust</b>.'),
   'A logaritmus nem előzmény nélküli új művelet — a hatványozás <b>fordítottja</b>, '
   'ugyanúgy, ahogy a kivonás az összeadásé vagy a gyökvonás a négyzetre emelésé. '
   'A hatványozásnak azonban <b>két</b> fordított művelete van, mert <b>két bemenő adatból</b> '
   '— az alapból és a kitevőből — állítja elő az eredményt, tehát kétféleképpen fordítható meg:',
   doboz("tetel", "A hatványozás két fordítottja",
         '<p>A $2^{3}=8$ egyenlőségben három szám szerepel. Attól függően, melyiket '
         'keressük, más művelet kell:</p>'
         '<div class="tblwrap"><table>'
         '<tr><th>Mit keresünk?</th><th>Kérdés</th><th>Művelet</th></tr>'
         '<tr><td>az eredményt</td><td>$2^{3}=?$</td><td>hatványozás</td></tr>'
         '<tr><td>az <b>alapot</b></td><td>$?^{3}=8$</td><td><b>gyökvonás</b>: $\\sqrt[3]{8}=2$</td></tr>'
         '<tr><td>a <b>kitevőt</b></td><td>$2^{?}=8$</td><td><b>logaritmus</b>: $\\log_{2}8=3$</td></tr>'
         '</table></div>',
         hid="tetel-ket-fordito"),
 ]),

 ("A logaritmus fogalma", [
   doboz("definicio", "Logaritmus",
         '<p>Legyen $a&gt;0$, $a\\neq 1$ és $b&gt;0$. A $b$ szám <b>$a$ alapú '
         'logaritmusán</b> azt a kitevőt értjük, amelyre az $a$-t emelve $b$-t kapunk:</p>'
         '$$\\log_{a}b=c\\iff a^{c}=b.$$'
         '<p>Az $a$ a logaritmus <b>alapja</b>, a $b$ az <b>argumentum</b> (a logaritmus '
         'alatti hatványérték), a $c$ pedig maga a logaritmus.</p>',
         hid="def-logaritmus"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Csak pozitív szám logaritmusa létezik!</b> A $\\log_{2}(-8)$ nem értelmezhető, '
         'mert nincs olyan $c$ kitevő, amelyre $2^{c}=-8$ lenne — a $2^{c}$ mindig pozitív '
         '(ezt az <a href="tananyag-exponencialis-fuggveny.html#tetel-tulajdonsagok">exponenciális függvény '
         'értékkészleténél</a> láttuk). Ugyanígy '
         '$\\log_{2}0$ sem létezik.</p>'
         '<p><b>És miért nem lehet az alap $1$?</b> Mert $1^{c}=1$ minden $c$-re: a '
         '$\\log_{1}5$ nem létezne (nincs ilyen kitevő), a $\\log_{1}1$ pedig bármi lehetne '
         '— a logaritmus így nem lenne egyértelmű. Negatív alapnál pedig már maga az $a^{c}$ '
         'sem értelmes a legtöbb $c$-re.</p>'
         '<p>Ez lesz később az <b>értelmezési tartomány</b> vizsgálatának az alapja: '
         'a $\\log_{a}\\big(f(x)\\big)$ kifejezésnél mindig ki kell kötni, hogy '
         '$f(x)&gt;0$.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p class="halvany">Kelleni fog a <a href="../01-hatvanyozas-gyokvonas-komplex-szamok/'
         'tananyag-hatvanyozas.html#def-egesz-kitevo">negatív</a> és a '
         '<a href="../01-hatvanyozas-gyokvonas-komplex-szamok/'
         'tananyag-gyoktelenites-es-racionalis-kitevo.html#def-racionalis-kitevo">tört kitevő</a> '
         '— például $\\tfrac19=3^{-2}$ és $\\sqrt{4}=4^{1/2}$.</p>'
         '<p>Számold ki a definíció alapján: <b>a)</b> $\\log_{2}8$; '
         '<b>b)</b> $\\log_{3}\\tfrac19$; <b>c)</b> $\\log_{4}2$; '
         '<b>d)</b> $\\log_{\\frac13}27$.</p>',
         hid="pelda-definicio",
         lenyilo=("Megoldás",
                  '<p>Minden esetben ugyanaz a kérdés: <i>hányadik hatványra kell emelni '
                  'az alapot?</i></p>'
                  '<p><b>a)</b> $2^{?}=8$, és $2^{3}=8$, tehát $\\boxed{\\log_{2}8=3}$.</p>'
                  '<p><b>b)</b> $3^{?}=\\tfrac19$. Mivel $\\tfrac19=3^{-2}$, '
                  '$\\boxed{\\log_{3}\\tfrac19=-2}$.</p>'
                  '<p><b>c)</b> $4^{?}=2$. Mivel $\\sqrt{4}=2$, azaz $4^{1/2}=2$, '
                  '$\\boxed{\\log_{4}2=\\tfrac12}$ — a logaritmus <b>törtszám is lehet</b>.</p>'
                  '<p><b>d)</b> $\\left(\\tfrac13\\right)^{?}=27$. Mivel '
                  '$\\left(\\tfrac13\\right)^{-3}=3^{3}=27$, '
                  '$\\boxed{\\log_{\\frac13}27=-3}$.</p>')),
   kviz('Mennyi $\\log_{5}125$?',
        ['$3$', '$25$', '$5$'], 0,
        jo="✔ 5³ = 125, tehát a keresett kitevő 3.",
        nem="✘ A kérdés nem az, hogy mennyi 125 vagy mennyi az alap, hanem hogy 5 "
            "hányadik hatványa 125. Mivel 5³ = 125, a válasz 3."),
 ]),

 ("A négy alapösszefüggés", [
   doboz("tetel", "Amit fejből kell tudni",
         '<p>Legyen $a&gt;0$ és $a\\neq 1$. Ekkor minden $b&gt;0$ esetén:</p>'
         '$$\\log_{a}1=0,\\qquad \\log_{a}a=1,\\qquad a^{\\log_{a}b}=b,$$'
         '<p>és tetszőleges $k\\in\\mathbb{R}$ kitevőre:</p>'
         '$$\\log_{a}a^{k}=k.$$'
         '<p>Figyeld meg a különbséget: az $a^{k}$ magától pozitív, ezért a negyedikhez '
         'nem kell külön kikötés; az $a^{\\log_{a}b}=b$-hez viszont kell a $b&gt;0$, '
         'különben a $\\log_{a}b$ le sem írható.</p>'
         '<p>Az első kettő közvetlenül a definícióból jön ($a^{0}=1$, $a^{1}=a$). '
         'A harmadik és a negyedik azt fejezi ki, hogy a <b>logaritmus és a hatványozás '
         'kioltják egymást</b> — pontosan úgy, ahogy a négyzetre emelés és a négyzetgyök.</p>',
         hid="tetel-alaposszefuggesek",
         lenyilo=("Miért igaz a harmadik és a negyedik?",
                  '<p><b>A harmadik.</b> A $\\log_{a}a^{k}$ arra kérdez rá, hogy az $a$-t '
                  'hányadik hatványra kell emelni ahhoz, hogy $a^{k}$-t kapjunk. A válasz '
                  'ránézésre adódik: a $k$-adikra — tehát $\\log_{a}a^{k}=k$.</p>'
                  '<p><b>A negyedik.</b> A $\\log_{a}b$ definíció szerint az a kitevő, amelyre '
                  '$a$-t emelve $b$-t kapunk. Ha tehát $a$-t épp erre a kitevőre emeljük, '
                  'definíció szerint $b$-t kell kapnunk. Ez a legfontosabb azonosság a '
                  'logaritmusos egyenletek megoldásánál.</p>')),
   doboz("definicio", "Két kitüntetett alap",
         '<p><b>Tízes alapú (Briggs-féle) logaritmus:</b> ha az alap $10$, gyakran '
         'elhagyjuk a jelölésből:</p>'
         '$$\\log_{10}b=\\lg b\\quad(\\text{vagy egyszerűen }\\log b).$$'
         '<p><b>Természetes alapú logaritmus:</b> az alap az $e\\approx 2{,}71828$ '
         'Euler-féle szám:</p>'
         '$$\\log_{e}b=\\ln b.$$'
         '<p>A számológépeden ez a két gomb szerepel — minden más alapú logaritmust '
         'ezekre kell visszavezetni (lásd az <a href="tananyag-attetes-mas-alapra.html">Áttérés más alapra</a> egységben).</p>',
         hid="def-lg-ln"),
   doboz("erdekesseg", "Miért találták ki?",
         '<p>John Napier 1614-ben azért publikálta a logaritmustáblákat, hogy a csillagászok '
         'megússzák a többjegyű <b>szorzásokat</b>: a logaritmus a szorzást összeadássá '
         'alakítja. Három és fél évszázadon át a logarléc volt a mérnökök „számológépe” — az '
         'Apollo-küldetések űrhajósai is vittek magukkal egyet.</p>'),
   kviz('Mennyi $\\log_{7}1+\\log_{4}4$?',
        ['$1$', '$0$', '$2$'], 0,
        jo="✔ log₇1 = 0 és log₄4 = 1, az összeg 1.",
        nem="✘ Bármely alap esetén log 1 = 0, és logₐa = 1 — az összeg 0 + 1 = 1."),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–3"),
   brief('<b>Dr. Bestia:</b> A fogalom megvan: a logaritmus egy <b>kitevő</b>. Ha ezt nem engeded elúszni, a következő rész magától adódik — a hatványozás minden azonossága átfordul logaritmusra: a szorzásból összeadás lesz, a hatványozásból szorzás.', outro=True),
 ]),
]

# ===================================================================== B2

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> A definíció szép, de lassú. Ha minden logaritmust fejben kellene '
         'visszafejtenünk, sosem érnénk a küldetés végére. Szerencsére a logaritmus '
         '<b>örökli</b> a hatványozás azonosságait — méghozzá egy fokkal '
         '<b>egyszerűbb</b> alakban: a szorzásból összeadás lesz, az osztásból kivonás, '
         'a hatványozásból szorzás. Ez a logaritmus igazi ereje.'),
 ]),

 ("A három azonosság", [
   doboz("tetel", "A logaritmus azonosságai",
         '<p>Legyen $a&gt;0$, $a\\neq 1$, továbbá $u&gt;0$ és $v&gt;0$. Ekkor</p>'
         '$$\\log_{a}(u\\cdot v)=\\log_{a}u+\\log_{a}v,$$'
         '$$\\log_{a}\\frac{u}{v}=\\log_{a}u-\\log_{a}v,$$'
         '$$\\log_{a}u^{k}=k\\cdot\\log_{a}u\\qquad(k\\in\\mathbb{R}).$$'
         '<p>Vagyis a logaritmus <b>egy szinttel lejjebb viszi</b> a műveletet: '
         'szorzás → összeadás, osztás → kivonás, hatványozás → szorzás.</p>',
         hid="tetel-azonossagok",
         lenyilo=("Miért igaz mind a három?",
                  '<p>Legyen $\\log_{a}u=p$ és $\\log_{a}v=q$. Definíció szerint ez azt '
                  'jelenti, hogy $u=a^{p}$ és $v=a^{q}$. Ekkor</p>'
                  '$$u\\cdot v=a^{p}\\cdot a^{q}=a^{p+q},$$'
                  '<p>ami épp azt mondja, hogy $\\log_{a}(uv)=p+q=\\log_{a}u+\\log_{a}v$.</p>'
                  '<p>A <b>hányadosra</b> ugyanezzel a jelöléssel: '
                  '$\\dfrac{u}{v}=\\dfrac{a^{p}}{a^{q}}=a^{p-q}$, tehát '
                  '$\\log_{a}\\dfrac{u}{v}=p-q=\\log_{a}u-\\log_{a}v$.</p>'
                  '<p>A <b>hatványra</b>: $u^{k}=\\left(a^{p}\\right)^{k}=a^{pk}$, tehát '
                  '$\\log_{a}u^{k}=pk=k\\log_{a}u$.</p>'
                  '<p>Mindhárom ugyanarra épül: a logaritmus a <b>kitevőt</b> adja vissza, a hatványozás azonosságai pedig épp a kitevőkkel végzett műveleteket írják le.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A leggyakoribb — és legköltségesebb — hiba az azonosságok <b>összegre</b> '
         'való alkalmazása:</p>'
         '<p>✘ $\\log_{a}(u+v)=\\log_{a}u+\\log_{a}v$ &nbsp;&nbsp; '
         '✔ $\\log_{a}(u\\cdot v)=\\log_{a}u+\\log_{a}v$</p>'
         '<p>Próbáld ki (a $\\lg$ a <a href="tananyag-logaritmus-fogalma.html#def-lg-ln">tízes alapú logaritmus</a>): $\\lg(1+9)=\\lg 10=1$, míg $\\lg 1+\\lg 9=0+\\lg 9\\approx 0{,}95$ — '
         'nem egyenlők. <b>A logaritmusnak a szorzásról van mondanivalója, az összeadásról nincs.</b></p>'
         '<p>Ugyanígy hibás: $\\dfrac{\\log_{a}u}{\\log_{a}v}=\\log_{a}\\dfrac{u}{v}$. Az '
         'argumentumok osztásából a logaritmusok <b>kivonása</b> lesz, nem az osztásuk. '
         '(A logaritmusok hányadosának egyébként van jelentése — de egészen más: erre való '
         'az <a href="tananyag-attetes-mas-alapra.html">áttérési képlet</a>.)</p>'
         '<p>Végül vigyázz a <b>páros</b> kitevőre: a $\\log_{a}(x^{2})$ minden $x\\neq 0$-ra '
         'létezik, a $2\\log_{a}x$ viszont csak $x&gt;0$-ra — a kettő tehát nem ugyanaz. '
         'Helyesen $\\log_{a}(x^{2})=2\\log_{a}|x|$. Bontáskor mindig kérdezd meg: az új '
         'alak ugyanazokra az $x$-ekre értelmes-e, mint a régi?</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számold ki: <b>a)</b> $\\lg 50+\\lg 2$; <b>b)</b> $\\log_{2}48-\\log_{2}3$; '
         '<b>c)</b> $\\log_{3}\\sqrt{27}$; <b>d)</b> $2\\log_{3}9$.</p>',
         hid="pelda-azonossagok",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\lg 50+\\lg 2=\\lg(50\\cdot 2)=\\lg 100=\\boxed{2}$.</p>'
                  '<p><b>b)</b> $\\log_{2}48-\\log_{2}3=\\log_{2}\\tfrac{48}{3}=\\log_{2}16=\\boxed{4}$.</p>'
                  '<p><b>c)</b> $\\sqrt{27}=27^{1/2}=3^{3/2}$, tehát '
                  '$\\log_{3}3^{3/2}=\\boxed{\\tfrac32}$. (Vagy: '
                  '$\\log_{3}\\sqrt{27}=\\tfrac12\\log_{3}27=\\tfrac12\\cdot 3=\\tfrac32$.)</p>'
                  '<p><b>d)</b> A hatvány-azonossággal visszafelé: '
                  '$2\\log_{3}9=\\log_{3}9^{2}=\\log_{3}81=\\boxed{4}$. '
                  '(Ellenőrzésül a definícióból: $\\log_{3}9=2$, tehát $2\\cdot 2=4$.)</p>')),
 ]),

 ("Kifejezések bontása és összevonása", [
   'Az azonosságokat <b>mindkét irányban</b> használjuk — de a két irány nem egyformán '
   'ártalmatlan: összevonáskor az értelmezési tartomány bővülhet, bontáskor szűkül, ezért '
   'egyenletmegoldásnál a végén mindig ellenőrizni kell a kapott gyököket. '
   'Egyenletmegoldásnál általában '
   '<b>összevonunk</b> (hogy egyetlen logaritmus maradjon), számoláskor pedig '
   '<b>szétbontunk</b> (hogy ismert értékekre jussunk).',
   doboz("pelda", "Vészterem-szimuláció",
         '<p><b>a)</b> Bontsd fel: $\\log_{a}\\dfrac{x^{3}\\sqrt{y}}{z}$.<br>'
         '<b>b)</b> Vond össze egyetlen logaritmussá: '
         '$2\\log_{a}x+\\tfrac12\\log_{a}y-3\\log_{a}z$.</p>',
         hid="pelda-bontas",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> Először a hányados, majd a szorzat, végül a hatvány:</p>'
                  '$$\\log_{a}\\frac{x^{3}\\sqrt{y}}{z}=\\log_{a}x^{3}+\\log_{a}\\sqrt{y}-\\log_{a}z'
                  '=3\\log_{a}x+\\frac12\\log_{a}y-\\log_{a}z.$$'
                  '<p><b>b)</b> Fordított sorrendben: az együtthatók kitevővé válnak, '
                  'az összeadás szorzattá, a kivonás hányadossá:</p>'
                  '$$2\\log_{a}x+\\frac12\\log_{a}y-3\\log_{a}z=\\log_{a}\\frac{x^{2}\\sqrt{y}}{z^{3}}.$$')),
   kviz('Mivel egyenlő $\\log_{2}5+\\log_{2}4$?',
        ['$\\log_{2}20$', '$\\log_{2}9$', '$\\log_{2}\\tfrac54$'], 0,
        jo="✔ Az összeg szorzattá válik az argumentumban: log₂(5·4) = log₂20.",
        nem="✘ A logaritmusok ÖSSZEGE az argumentumok SZORZATÁnak logaritmusa: log₂20."),
   gyakorolj(FGY + "#alap-7", "A 7–12", FGY + "#kozep-4", "K 4–8"),
   brief('<b>Dr. Bestia:</b> Három azonosság, és bármit szét tudsz szedni. Egy dolog hiányzik még: a számológépeden csak <b>két</b> gomb van, $\lg$ és $\ln$. Hogyan számolsz ki egy $\log_{3}20$-at? Egyetlen képlet kell hozzá.', outro=True),
 ]),
]

# ===================================================================== B3

B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Dr. Bestia:</b> Itt az igazság pillanata. A számológépeden két logaritmus-gomb van: '
         '<b>lg</b> és <b>ln</b>. De a vírus kettesével szaporodik, tehát nekem '
         '$\\log_{2}$ kellene. Elakadtunk? Nem — létezik egy képlet, amely '
         '<b>bármely</b> alapot visszavezet egy másikra. Ezzel a logaritmus '
         'végre használható eszközzé válik a laborban is.'),
 ]),

 ("Áttérés más alapra", [
   doboz("tetel", "Az áttérési képlet",
         '<p>Legyen $a,t&gt;0$, $a\\neq 1$, $t\\neq 1$ és $b&gt;0$ — a $t$ az <b>új alap</b>. '
         'Ekkor</p>'
         '$$\\log_{a}b=\\frac{\\log_{t}b}{\\log_{t}a}.$$'
         '<p>A gyakorlatban $t=10$ (vagy $t=e$), így a számológéppel bármi kiszámolható:</p>'
         '$$\\log_{a}b=\\frac{\\lg b}{\\lg a}=\\frac{\\ln b}{\\ln a}.$$',
         hid="tetel-attetes",
         lenyilo=("Miért igaz?",
                  '<p>Legyen $\\log_{a}b=c$, azaz $a^{c}=b$ (a $c$ itt is a logaritmus '
                  'értéke, mint a definícióban). Vegyük mindkét oldal $t$ alapú '
                  'logaritmusát:</p>'
                  '$$\\log_{t}a^{c}=\\log_{t}b\\ \\Longrightarrow\\ c\\cdot\\log_{t}a=\\log_{t}b.$$'
                  '<p>Mivel $a\\neq 1$, a $\\log_{t}a\\neq 0$, tehát oszthatunk vele: '
                  '$c=\\dfrac{\\log_{t}b}{\\log_{t}a}$.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Ne keverd össze!</b> A képletben <b>osztás</b> áll, nem kivonás; a '
         'számlálóban az <b>argumentum</b> logaritmusa áll, a nevezőben az <b>alapé</b>:</p>'
         '<p>✔ $\\log_{2}7=\\dfrac{\\lg 7}{\\lg 2}$ &nbsp;&nbsp;&nbsp; '
         '✘ $\\log_{2}7=\\dfrac{\\lg 2}{\\lg 7}$ &nbsp;&nbsp;&nbsp; '
         '✘ $\\log_{2}7=\\lg 7-\\lg 2$</p>'
         '<p>Ellenőrzés fejben: $\\log_{2}7$ valahol $2$ és $3$ között van (mert '
         '$2^{2}=4&lt;7&lt;8=2^{3}$). Ha a géped $0{,}36$-ot ad, felcserélted a törtet.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számold ki négy tizedesjegy pontossággal: <b>a)</b> $\\log_{11}12$; '
         '<b>b)</b> $\\log_{7}23$.</p>',
         hid="pelda-attetes",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\log_{11}12=\\dfrac{\\lg 12}{\\lg 11}\\approx'
                  '\\dfrac{1{,}07918}{1{,}04139}\\approx\\boxed{1{,}0363}$.</p>'
                  '<p>Józan ész: a $12$ épp csak nagyobb $11$-nél, tehát a kitevőnek '
                  'kicsit $1$ fölött kell lennie. ✔</p>'
                  '<p><b>b)</b> $\\log_{7}23=\\dfrac{\\lg 23}{\\lg 7}\\approx'
                  '\\dfrac{1{,}36173}{0{,}84510}\\approx\\boxed{1{,}6113}$.</p>'
                  '<p>Ellenőrzés: $7^{1}=7&lt;23&lt;49=7^{2}$, tehát a válasznak '
                  '$1$ és $2$ között kell lennie. ✔</p>')),
   kviz('Melyik alakban írható át $\\log_{3}20$ a számológéphez?',
        ['$\\dfrac{\\lg 20}{\\lg 3}$', '$\\dfrac{\\lg 3}{\\lg 20}$', '$\\lg 20-\\lg 3$'], 0,
        jo="✔ Felülre az argumentum logaritmusa kerül, alulra az alapé.",
        nem="✘ logₐb = lg b / lg a — felül az argumentum (20) logaritmusa, alul az alapé (3)."),
 ]),

 ("Mire jó a logaritmus?", [
   'A logaritmus azért fontos, mert <b>a nagyságrendeket kezelhetővé teszi</b>. Ahol '
   'a mért mennyiségek több nagyságrendet fognak át, ott szinte biztosan logaritmikus '
   'skálát találsz.',
   doboz("erdekesseg", "Logaritmikus skálák a természetben",
         '<div class="tblwrap"><table>'
         '<tr><th>Skála</th><th>Képlet</th><th>Mit mér?</th></tr>'
         '<tr><td>pH</td><td>$\\mathrm{pH}=-\\lg[\\mathrm{H}^{+}]$</td>'
         '<td>a savasságot; egy egység = <b>tízszeres</b> különbség</td></tr>'
         '<tr><td>Richter</td><td>$M=\\lg\\dfrac{A}{A_{0}}$</td>'
         '<td>a földrengés <b>kilengését</b>; egy egység = tízszeres kilengés, tehát a 6-os '
         '<b>ezerszer</b> akkora kilengésű, mint a 3-as</td></tr>'
         '<tr><td>decibel</td><td>$L=10\\lg\\dfrac{I}{I_{0}}$</td>'
         '<td>a hangerőt</td></tr>'
         '</table></div>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p><b>a)</b> A fertőzött sejtek száma óránként megkétszereződik, egyetlen sejtből '
         'indulva. Hány óra múlva éri el az egymilliót?<br>'
         '<b>b)</b> Egy bankban a pénz évi $5\\%$-kal gyarapszik. Hány év alatt '
         'duplázódik meg?</p>',
         hid="pelda-alkalmazas",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> A modell: $2^{x}=1\\,000\\,000$. Innen</p>'
                  '$$x=\\log_{2}1\\,000\\,000=\\frac{\\lg 10^{6}}{\\lg 2}='
                  '\\frac{6}{0{,}30103}\\approx 19{,}93.$$'
                  '<p>Tehát a <b>20. órában</b> lépi át az egymilliót — a modell óránként duplázódik, és $2^{19}=524\\,288$ még kevesebb, $2^{20}=1\\,048\\,576$ már több. Figyeld meg: '
                  'a millió hatalmas szám, de a logaritmusa csak $20$ — ez a '
                  'nagyságrend-kezelés lényege.</p>'
                  '<p><b>b)</b> A modell: $1{,}05^{n}=2$, tehát</p>'
                  '$$n=\\log_{1{,}05}2=\\frac{\\lg 2}{\\lg 1{,}05}\\approx'
                  '\\frac{0{,}30103}{0{,}02119}\\approx 14{,}21.$$'
                  '<p>Vagyis nagyjából <b>15 év</b> alatt duplázódik meg a pénz (a 14. '
                  'év végén még nincs meg a kétszeres).</p>')),
   kviz('Hányszorosa egy 7-es erősségű földrengés kilengése a 4-esének?',
        ['1000-szer', '3-szor', '$\\tfrac74$-szer'], 0,
        jo="✔ A Richter-skála logaritmikus: 3 egység különbség = 10³ = 1000-szeres.",
        nem="✘ A skála logaritmikus — minden egység tízszeres kilengést jelent, tehát 10³ = 1000."),
   gyakorolj(FGY + "#alap-13", "A 13–18", FGY + "#kozep-9", "K 9–14"),
   brief('<b>Dr. Bestia:</b> Megvan az eszköz. Most már bármelyik exponenciális egyenletet meg '
         'tudjuk oldani — akkor is, ha a két oldal nem hozható közös alapra. Egy dolog '
         'maradt hátra: ha a logaritmus a hatványozás fordítottja, akkor a '
         '<b>logaritmusfüggvény</b> az exponenciális függvény <b>inverze</b>. '
         'A következő küldetésben ezt a tükörképet nézzük meg.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-logaritmus-fogalma.html",
     cim="A logaritmus fogalma", cim_tiszta="A logaritmus fogalma",
     alcim="A hatványozás második fordított művelete, a definíció szerinti számolás, "
           "a négy alapösszefüggés, valamint a tízes és a természetes alapú logaritmus.",
     chip="Az Evolúciós Ugrás · 4/8", szakaszok=B1,
     elozo=("feladatok-exponencialis.html", "Feladatok — exponenciális függvény"),
     kovetkezo=("tananyag-logaritmus-azonossagai.html", "A logaritmus azonosságai")),
 lap(**T, fajl="tananyag-logaritmus-azonossagai.html",
     cim="A logaritmus azonosságai", cim_tiszta="A logaritmus azonosságai",
     alcim="Szorzat, hányados és hatvány logaritmusa — kifejezések bontása és "
           "összevonása, a leggyakoribb hibákkal együtt.",
     chip="Az Evolúciós Ugrás · 5/8", szakaszok=B2,
     elozo=("tananyag-logaritmus-fogalma.html", "A logaritmus fogalma"),
     kovetkezo=("tananyag-attetes-mas-alapra.html", "Áttérés más alapra és alkalmazások")),
 lap(**T, fajl="tananyag-attetes-mas-alapra.html",
     cim="Áttérés más alapra és alkalmazások",
     cim_tiszta="Áttérés más alapra és alkalmazások",
     alcim="Az áttérési képlet, a számológép használata, valamint a logaritmikus "
           "skálák és a növekedési feladatok.",
     chip="Az Evolúciós Ugrás · 6/8", szakaszok=B3,
     elozo=("tananyag-logaritmus-azonossagai.html", "A logaritmus azonosságai"),
     kovetkezo=(FGY, "Feladatok — logaritmus")),
]
for u in KI:
    print("✓", os.path.basename(u))
