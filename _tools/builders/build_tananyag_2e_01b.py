# -*- coding: utf-8 -*-
"""2e / 01 — „B" altéma: gyökvonás (B1), műveletek gyökökkel (B2),
gyöktelenítés és racionális kitevő (B3). Mentor: Vihar Vera."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj

T = dict(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
         temakor="Hatványozás, gyökvonás, komplex számok")
FGY = "feladatok-gyokvonas.html"

# =====================================================================  B1

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Vihar Vera:</b> Eddig előre néztünk: adott alap, adott kitevő, mekkora az eredmény? '
         'Most fordítsd meg a kérdést. Ismerem a vihar <b>energiáját</b> — mekkora volt a kiváltó ok? '
         'Ez a gyökvonás: a hatványozás visszafejtése. És itt van az évad első igazi csapdája — '
         'a <b>páros</b> gyökkitevő nem viselkedik úgy, mint a páratlan. Dr. Baljós pontosan ezen a résen fér be.'),
   'A gyökvonás a hatványozás <b>inverz művelete</b>: azt a számot keressük, amelynek adott '
   'kitevőjű hatványa a megadott szám. A definíciót viszont <b>két külön esetre</b> kell bontanunk — '
   'és ennek a kettéválasztásnak messzemenő következményei lesznek.',
 ]),

 ("Az $n$-edik gyök fogalma", [
   doboz("definicio", "Az $n$-edik gyök",
         '<p>Legyen $a\\in\\mathbb{R}$ és $n\\in\\mathbb{N}$, $n\\ge 2$. Az $a$ szám '
         '<b>$n$-edik gyöke</b>, jelben $\\sqrt[n]{a}$:</p>'
         '<ul>'
         '<li>ha $n$ <b>páratlan</b>: az az <b>egyetlen</b> valós szám, amelynek $n$-edik '
         'hatványa $a$ — ilyen <b>minden</b> valós $a$ esetén létezik;</li>'
         '<li>ha $n$ <b>páros</b>: az az egyetlen <b>nemnegatív</b> valós szám, amelynek '
         '$n$-edik hatványa $a$ — ez csak $a\\ge 0$ esetén létezik.</li>'
         '</ul>'
         '<p>Az $a$ a <b>gyök alapja</b> (a gyökjel alatti mennyiség), $n$ a <b>gyökkitevő</b>. '
         'A négyzetgyöknél ($n=2$) a gyökkitevőt nem szoktuk kiírni: $\\sqrt{a}$.</p>',
         hid="def-nedik-gyok"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki, ahol létezik: $\\sqrt{144}$, $\\sqrt[3]{-125}$, $\\sqrt[4]{16}$, '
         '$\\sqrt[5]{-32}$, $\\sqrt{-49}$.</p>',
         hid="pelda-gyok-ertekek",
         lenyilo=("Megoldás",
                  '<p>$\\sqrt{144}=12$ (nem $\\pm12$! a négyzetgyök definíció szerint '
                  '<b>nemnegatív</b>) · $\\sqrt[3]{-125}=-5$ (páratlan gyökkitevő, negatív alap '
                  'megengedett) · $\\sqrt[4]{16}=2$ · $\\sqrt[5]{-32}=-2$ · '
                  '$\\sqrt{-49}$ a valós számok halmazán <b>nem értelmezett</b> '
                  '(páros gyökkitevő, negatív alap).</p>')),
   doboz("erdekesseg", "Miért csak a nemnegatív gyök?",
         '<p>A $x^{2}=9$ egyenletnek <b>két</b> megoldása van: $x=3$ és $x=-3$. '
         'A $\\sqrt{9}$ jel viszont <b>egy</b> konkrét számot kell hogy jelöljön — különben '
         'nem lehetne vele számolni. Megállapodás szerint ez a <b>nemnegatív</b>, tehát '
         '$\\sqrt{9}=3$. Az egyenlet két megoldását ezért írjuk $x=\\pm\\sqrt{9}$ alakban.</p>'),
 ]),

 ("A definíció két következménye", [
   doboz("tetel", "Gyök és hatvány egymás után",
         '<p>Ha $\\sqrt[n]{a}$ létezik, akkor</p>'
         '$$\\left(\\sqrt[n]{a}\\right)^{n}=a,$$'
         '<p>viszont fordított sorrendben <b>nem</b> mindig ez jön ki:</p>'
         '$$\\sqrt[n]{a^{n}}=\\begin{cases} a, &\\text{ha } n \\text{ páratlan},\\\\[2pt] '
         '|a|, &\\text{ha } n \\text{ páros}.\\end{cases}$$',
         hid="tetel-gyok-hatvany"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A mutálódott kódban ez áll: $\\sqrt{a^{2}}=a$ <b>minden valós $a$-ra</b>. '
         '<b>Hamis.</b> Próbáld ki $a=-7$-tel:</p>'
         '$$\\sqrt{(-7)^{2}}=\\sqrt{49}=7\\neq -7.$$'
         '<p>A helyes alak $\\sqrt{a^{2}}=|a|$. Páratlan gyökkitevőnél viszont nincs baj: '
         '$\\sqrt[3]{(-7)^{3}}=\\sqrt[3]{-343}=-7$. <b>Ökölszabály:</b> ha a gyökkitevő páros és '
         'a betűről nem tudod, hogy nemnegatív, <b>abszolút érték kell</b>. '
         'Ha a feladat kiköti, hogy a betűk pozitívak, akkor elhagyható.</p>'),
   kviz('Mennyi $\\sqrt[4]{(-3)^{4}}$?',
        ['$3$', '$-3$', 'Nincs értelmezve.'], 0,
        jo="✔ Páros gyökkitevő: az eredmény |−3| = 3.",
        nem="✘ (−3)⁴ = 81, és ⁴√81 = 3. Páros gyökkitevőnél az eredmény |a|."),
 ]),

 ("A gyökvonás azonosságai", [
   'Az alábbi szabályok $a,b\\ge 0$ és $m,n,k\\in\\mathbb{N}$ mellett mindig érvényesek. '
   '(Páratlan gyökkitevőnél negatív alapra is igazak, de a biztonság kedvéért a feladatokban '
   'többnyire nemnegatív alapokkal dolgozunk.)',
   doboz("tetel", "A gyökvonás hat azonossága",
         '$$\\sqrt[n]{a}\\cdot\\sqrt[n]{b}=\\sqrt[n]{a\\cdot b}\\qquad\\qquad '
         '\\frac{\\sqrt[n]{a}}{\\sqrt[n]{b}}=\\sqrt[n]{\\frac{a}{b}}\\ \\ (b\\neq 0)$$'
         '$$\\left(\\sqrt[n]{a}\\right)^{m}=\\sqrt[n]{a^{m}}\\qquad\\qquad '
         '\\sqrt[m]{\\sqrt[n]{a}}=\\sqrt[m\\cdot n]{a}$$'
         '$$\\sqrt[n]{a^{m}}=\\sqrt[n\\cdot k]{a^{m\\cdot k}}\\qquad\\qquad '
         'b\\cdot\\sqrt[n]{a}=\\sqrt[n]{a\\cdot b^{n}}$$'
         '<p>Az ötödik a gyökkitevő <b>bővítése</b> és <b>egyszerűsítése</b> (mint a törteknél!), '
         'a hatodik a tényező <b>bevitele</b> a gyökjel alá.</p>',
         hid="tetel-gyok-azonossagok"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>Nincs olyan azonosság, hogy $\\sqrt{a+b}=\\sqrt{a}+\\sqrt{b}$. Ellenpélda:</p>'
         '$$\\sqrt{9+16}=\\sqrt{25}=5,\\qquad\\text{de}\\qquad \\sqrt{9}+\\sqrt{16}=3+4=7.$$'
         '<p>A gyökvonás a <b>szorzással és osztással</b> barátkozik — az összeadással soha.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Egyszerűsítsd ($a&gt;0$): $\\sqrt[6]{a^{4}}$, valamint számítsd ki '
         '$\\sqrt[3]{\\sqrt{64}}$ értékét.</p>',
         lenyilo=("Megoldás",
                  '<p>$\\sqrt[6]{a^{4}}=\\sqrt[6:2]{a^{4:2}}=\\sqrt[3]{a^{2}}$ — a gyökkitevőt és '
                  'a hatványkitevőt ugyanazzal a számmal egyszerűsíthetjük. '
                  '$\\sqrt[3]{\\sqrt{64}}=\\sqrt[6]{64}=2$, mert $2^{6}=64$.</p>')),
   gyakorolj(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Vihar Vera:</b> Megvan a nyelvtan — jöjjön a mondatalkotás. A gyököket össze kell tudnod '
         'vonni, szorozni, egymásba ágyazni. Ez a rész tiszta kézügyesség: sok kis lépés, '
         'mindegyik egyszerű, de egyetlen elrontott előjel az egész számítást viszi.',
         outro=True),
 ]),
]

# =====================================================================  B2

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Vihar Vera:</b> A műszerek tucatnyi gyökös jelet dobnak ki egyszerre, és ránézésre '
         'mind különbözőnek látszik. Pedig $\\sqrt{20}$, $\\sqrt{45}$ és $\\sqrt{80}$ ugyanannak '
         'a jelnek a többszörösei — csak <b>ki kell hozni</b> belőlük a közös részt. '
         'Aki ezt látja, két sorban rendet tesz ott, ahol más fél oldalt számol.'),
   'Ebben az egységben megtanuljuk a gyökös kifejezések „házimunkáját": tényezőt viszünk '
   'ki és be, összevonjuk a hasonló tagokat, szorzunk, és egymásba ágyazott gyököket bontunk.',
 ]),

 ("Tényező kivitele és bevitele", [
   'A $b\\cdot\\sqrt[n]{a}=\\sqrt[n]{a\\cdot b^{n}}$ azonosság <b>mindkét irányban</b> használható. '
   'Balról jobbra <b>bevisszük</b> a tényezőt a gyökjel alá, jobbról balra <b>kihozzuk</b>.',
   doboz("pelda", "Vészterem-szimuláció — kihozatal",
         '<p>Hozd ki a gyökjel alól a lehető legnagyobb tényezőt: '
         '$\\sqrt{72}$, $\\sqrt[3]{54}$, $\\sqrt{50a^{3}}$ ($a&gt;0$).</p>',
         hid="pelda-kihozatal",
         lenyilo=("Megoldás",
                  '<p>A trükk: keresd meg a legnagyobb <b>teljes hatvány</b> osztót.</p>'
                  '<p>$\\sqrt{72}=\\sqrt{36\\cdot 2}=6\\sqrt{2}$ · '
                  '$\\sqrt[3]{54}=\\sqrt[3]{27\\cdot 2}=3\\sqrt[3]{2}$ · '
                  '$\\sqrt{50a^{3}}=\\sqrt{25a^{2}\\cdot 2a}=5a\\sqrt{2a}$.</p>')),
   doboz("pelda", "Vészterem-szimuláció — bevitel",
         '<p>Vidd be a gyökjel alá: $3\\sqrt{5}$ és $2\\sqrt[3]{7}$.</p>',
         lenyilo=("Megoldás",
                  '<p>$3\\sqrt{5}=\\sqrt{5\\cdot 3^{2}}=\\sqrt{45}$ · '
                  '$2\\sqrt[3]{7}=\\sqrt[3]{7\\cdot 2^{3}}=\\sqrt[3]{56}$. '
                  'Figyelj: a tényező a <b>gyökkitevő</b> hatványán megy be.</p>')),
 ]),

 ("Hasonló gyökös tagok összevonása", [
   'Két gyökös tag akkor <b>hasonló</b>, ha kihozatal után ugyanaz marad a gyökjel alatt. '
   'A hasonló tagokat úgy vonjuk össze, mint az algebrai kifejezésekben az $x$-eket: '
   'az együtthatókat adjuk össze.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Végezd el a műveleteket: '
         '$3\\sqrt{20}-\\sqrt{45}+2\\sqrt{80}-\\sqrt{125}$.</p>',
         hid="pelda-osszevonas",
         lenyilo=("Megoldás",
                  '<p>Először mindent $\\sqrt{5}$-re hozunk: $\\sqrt{20}=2\\sqrt5$, '
                  '$\\sqrt{45}=3\\sqrt5$, $\\sqrt{80}=4\\sqrt5$, $\\sqrt{125}=5\\sqrt5$. Így</p>'
                  '$$3\\cdot 2\\sqrt5-3\\sqrt5+2\\cdot 4\\sqrt5-5\\sqrt5'
                  '=(6-3+8-5)\\sqrt5=6\\sqrt5.$$')),
   kviz('Mennyi $\\sqrt{18}+\\sqrt{8}$?',
        ['$5\\sqrt{2}$', '$\\sqrt{26}$', '$2\\sqrt{13}$'], 0,
        jo="✔ √18 = 3√2 és √8 = 2√2, összegük 5√2.",
        nem="✘ Gyököt nem adhatunk össze a gyökjel alatt! Hozd ki: 3√2 + 2√2 = 5√2."),
 ]),

 ("Szorzás, osztás, nevezetes azonosságok", [
   'Gyökös kifejezéseket ugyanúgy szorzunk, mint bármely kéttagú kifejezést — és a '
   'nevezetes azonosságok itt különösen hasznosak, mert a négyzetre emelés '
   '<b>eltünteti</b> a négyzetgyököt.',
   doboz("tetel", "A két leghasznosabb alak",
         '$$\\left(\\sqrt{a}+\\sqrt{b}\\right)\\left(\\sqrt{a}-\\sqrt{b}\\right)=a-b$$'
         '$$\\left(\\sqrt{a}\\pm\\sqrt{b}\\right)^{2}=a\\pm 2\\sqrt{ab}+b$$'
         '<p>Az elsőben a gyökök <b>teljesen eltűnnek</b> — ez lesz a gyöktelenítés motorja '
         'a következő egységben.</p>',
         hid="tetel-gyokos-nevezetes"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki: '
         '<b>a)</b> $\\left(\\sqrt{11}+\\sqrt{7}\\right)\\left(\\sqrt{11}-\\sqrt{7}\\right)$; '
         '<b>b)</b> $\\left(\\sqrt{5}+\\sqrt{3}\\right)^{2}$.</p>',
         hid="pelda-nevezetes",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $11-7=4$ — egyetlen lépés, nem kell kibontani.</p>'
                  '<p><b>b)</b> $5+2\\sqrt{5\\cdot 3}+3=8+2\\sqrt{15}$.</p>')),
 ]),

 ("Beágyazott gyökök és a gyökök összehasonlítása", [
   'Az egymásba ágyazott gyököket a $\\sqrt[m]{\\sqrt[n]{a}}=\\sqrt[m\\cdot n]{a}$ azonosság '
   'bontja fel. Ha a gyökök alatt hatványok is vannak, a legbiztosabb út a <b>közös '
   'gyökkitevőre hozás</b> — pontosan úgy, ahogy a törteket közös nevezőre hozzuk.',
   doboz("pelda", "Vészterem-szimuláció — beágyazott gyök",
         '<p>Egyszerűsítsd ($x&gt;0$): $\\sqrt[3]{x\\sqrt{x}}$.</p>',
         hid="pelda-beagyazott",
         lenyilo=("Megoldás",
                  '<p>Belül: $x\\cdot\\sqrt{x}=\\sqrt{x^{2}}\\cdot\\sqrt{x}=\\sqrt{x^{3}}$. Így</p>'
                  '$$\\sqrt[3]{\\sqrt{x^{3}}}=\\sqrt[6]{x^{3}}=\\sqrt[6:3]{x^{3:3}}=\\sqrt{x}.$$')),
   doboz("pelda", "Vészterem-szimuláció — összehasonlítás",
         '<p>Állítsd növekvő sorrendbe: $\\sqrt{2}$, $\\sqrt[3]{3}$, $\\sqrt[6]{10}$.</p>',
         hid="pelda-osszehasonlitas",
         lenyilo=("Megoldás",
                  '<p>A gyökkitevők legkisebb közös többszöröse $6$, ezért mindet '
                  '6-odik gyökre bővítjük:</p>'
                  '$$\\sqrt{2}=\\sqrt[6]{2^{3}}=\\sqrt[6]{8},\\qquad '
                  '\\sqrt[3]{3}=\\sqrt[6]{3^{2}}=\\sqrt[6]{9},\\qquad \\sqrt[6]{10}.$$'
                  '<p>Azonos gyökkitevőnél már csak a gyök alatti számokat kell összevetni:</p>'
                  '$$\\sqrt{2}&lt;\\sqrt[3]{3}&lt;\\sqrt[6]{10}.$$')),
   kviz('Mivel egyenlő $\\sqrt{\\sqrt[3]{a}}$, ha $a&gt;0$?',
        ['$\\sqrt[6]{a}$', '$\\sqrt[5]{a}$', '$\\sqrt[3]{a^{2}}$'], 0,
        jo="✔ A gyökkitevők összeszorzódnak: 2 · 3 = 6.",
        nem="✘ Egymásba ágyazott gyököknél a gyökkitevők szorzódnak: 2 · 3 = 6."),
   gyakorolj(FGY + "#alap-6", "A 6–11", FGY + "#kozep-5", "K 5–9"),
   brief('<b>Vihar Vera:</b> Egy dolog maradt, ami elrontja a jelentéseinket: a <b>nevezőben álló gyök</b>. '
         'Ki kell onnan takarítani — és közben rájössz, hogy a hatvány és a gyök valójában '
         'ugyanaz a művelet, két különböző jelöléssel.',
         outro=True),
 ]),
]

# =====================================================================  B3

B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Vihar Vera:</b> Utolsó lépés a viharok fejezetében — és a legelegánsabb. '
         'Megszabadulunk a nevezőben álló gyököktől, aztán felfedezzük, hogy a '
         '$\\sqrt[n]{a^{m}}$ jelölés valójában <b>hatvány</b>: $a^{m/n}$. Ettől kezdve nincs '
         'külön gyök- és külön hatványszabály — <b>egyetlen</b> szabályrendszer van. '
         'Ez a felismerés készít fel a következő évadra: az exponenciális függvényre.'),
 ]),

 ("Miért gyöktelenítünk?", [
   doboz("erdekesseg", "Egy szokás, amit érdemes megérteni",
         '<p>A számológépek előtti korban a $\\dfrac{1}{\\sqrt{2}}$ kiszámítása azt jelentette, '
         'hogy $1$-et el kellett osztani egy végtelen tizedes törttel — kézzel, papíron. '
         'Ezzel szemben a $\\dfrac{\\sqrt{2}}{2}$ alaknál elég $1{,}41421\\ldots$-t elosztani '
         '<b>kettővel</b>. Ma már a számológép mindkettőt elvégzi, de a gyöktelenített alak '
         'maradt a <b>megállapodás szerinti végalak</b>: így két megoldás összehasonlítható, '
         'és a további átalakítások is egyszerűbbek.</p>'),
 ]),

 ("Egytagú nevező", [
   'Ha a nevezőben egyetlen gyökös tag áll, olyan tényezővel bővítünk, amitől a nevezőben '
   '<b>teljes hatvány</b> keletkezik a gyökjel alatt.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Gyöktelenítsd: <b>a)</b> $\\dfrac{6}{\\sqrt{3}}$; <b>b)</b> $\\dfrac{5}{\\sqrt[3]{4}}$.</p>',
         hid="pelda-egytagu",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $\\sqrt{3}$-mal bővítünk: '
                  '$\\dfrac{6}{\\sqrt3}=\\dfrac{6\\sqrt3}{3}=2\\sqrt3$.</p>'
                  '<p><b>b)</b> A nevezőben $\\sqrt[3]{4}=\\sqrt[3]{2^{2}}$ áll — még egy $2$ '
                  'hiányzik a köbhöz, ezért $\\sqrt[3]{2}$-vel bővítünk:</p>'
                  '$$\\frac{5}{\\sqrt[3]{4}}=\\frac{5\\sqrt[3]{2}}{\\sqrt[3]{8}}'
                  '=\\frac{5\\sqrt[3]{2}}{2}.$$')),
 ]),

 ("Kéttagú nevező — a konjugált", [
   'Ha a nevező kéttagú, a $\\left(\\sqrt a+\\sqrt b\\right)\\left(\\sqrt a-\\sqrt b\\right)=a-b$ '
   'azonosságot használjuk: az összeg <b>konjugáltja</b> a különbség (és fordítva). '
   'A bővítés után a nevezőből eltűnik a gyök.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Gyöktelenítsd: <b>a)</b> $\\dfrac{4}{\\sqrt{7}-\\sqrt{3}}$; '
         '<b>b)</b> $\\dfrac{10}{3+\\sqrt{7}}$.</p>',
         hid="pelda-kettagu",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> A konjugált $\\sqrt7+\\sqrt3$, a nevező $7-3=4$ lesz:</p>'
                  '$$\\frac{4\\left(\\sqrt7+\\sqrt3\\right)}{4}=\\sqrt7+\\sqrt3.$$'
                  '<p><b>b)</b> A konjugált $3-\\sqrt7$, a nevező $9-7=2$:</p>'
                  '$$\\frac{10\\left(3-\\sqrt7\\right)}{2}=5\\left(3-\\sqrt7\\right)=15-5\\sqrt7.$$')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>„A konjugálttal bővítés annyi, hogy átírom a nevező előjelét." — <b>Hamis.</b> '
         'A törtet a konjugálttal <b>bővíteni</b> kell, tehát a <b>számlálót is</b> szorozni:</p>'
         '$$\\frac{4}{\\sqrt7-\\sqrt3}\\neq\\frac{4}{\\sqrt7+\\sqrt3}.$$'
         '<p>Ha csak a nevezőt írnád át, egy másik számot kapnál. Bővítés = a számlálót és '
         'a nevezőt <b>ugyanazzal</b> szorozzuk.</p>'),
 ]),

 ("Racionális kitevőjű hatvány", [
   'Most jön a témakör egyik legszebb gondolata. Mi legyen $a^{1/2}$? Ismét a '
   '<b>permanenciaelvet</b> hívjuk segítségül: legyen igaz a $\\left(a^{m}\\right)^{n}=a^{mn}$ '
   'szabály a tört kitevőre is. Akkor',
   '$$\\left(a^{1/2}\\right)^{2}=a^{\\frac12\\cdot 2}=a^{1}=a,$$',
   'vagyis $a^{1/2}$ olyan szám, amelynek a négyzete $a$ — tehát $a^{1/2}=\\sqrt{a}$. '
   'Nincs más választás.',
   doboz("definicio", "Racionális kitevőjű hatvány",
         '<p>Ha $a\\in\\mathbb{R}$, $a&gt;0$, $m\\in\\mathbb{Z}$ és $n\\in\\mathbb{N}$, $n\\ge2$, akkor</p>'
         '$$a^{\\frac{m}{n}}=\\sqrt[n]{a^{m}}.$$'
         '<p>Ezzel a hatványozás <b>öt azonossága</b> minden racionális kitevőre érvényes marad — '
         'és a gyökvonás hat azonossága ennek már csak következménye.</p>',
         hid="def-racionalis-kitevo"),
   doboz("erdekesseg", "Miért kell $a&gt;0$?",
         '<p>Negatív alapnál az átírás ellentmondáshoz vezet: $\\frac13=\\frac26$, tehát '
         '$(-8)^{1/3}$ és $(-8)^{2/6}$ ugyanaz kellene, hogy legyen. Csakhogy '
         '$\\sqrt[3]{-8}=-2$, míg $\\sqrt[6]{(-8)^{2}}=\\sqrt[6]{64}=2$. '
         'Ezért a tört kitevőt <b>csak pozitív alapra</b> értelmezzük.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki: $8^{\\frac{2}{3}}$, $16^{-\\frac{3}{4}}$, $32^{0{,}4}$.</p>',
         hid="pelda-racionalis-kitevo",
         lenyilo=("Megoldás",
                  '<p>Írjuk az alapot közös prímhatványként:</p>'
                  '<p>$8^{2/3}=\\left(2^{3}\\right)^{2/3}=2^{2}=4$ · '
                  '$16^{-3/4}=\\left(2^{4}\\right)^{-3/4}=2^{-3}=\\dfrac18$ · '
                  '$32^{0{,}4}=32^{2/5}=\\left(2^{5}\\right)^{2/5}=2^{2}=4$.</p>')),
   kviz('Mennyi $27^{-\\frac{2}{3}}$?',
        ['$\\dfrac{1}{9}$', '$-9$', '$9$'], 0,
        jo="✔ 27 = 3³, tehát 27^(−2/3) = 3^(−2) = 1/9.",
        nem="✘ Írd az alapot 3 hatványaként: (3³)^(−2/3) = 3^(−2) = 1/9. A negatív kitevő reciprokot jelent, nem előjelváltást."),
 ]),

 ("Hatvány és gyök együtt", [
   'A tört kitevő igazi haszna, hogy a <b>vegyes</b> kifejezéseket egyetlen nyelvre fordítja: '
   'átírunk mindent hatványra, összeadjuk a kitevőket, majd — ha kell — visszaírjuk gyökös alakba.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Egyszerűsítsd ($a&gt;0$): $\\dfrac{\\sqrt[3]{a^{2}}\\cdot\\sqrt[6]{a}}{\\sqrt{a}}$.</p>',
         hid="pelda-vegyes",
         lenyilo=("Megoldás",
                  '<p>Tört kitevőre írva: $a^{2/3}\\cdot a^{1/6}:a^{1/2}$. '
                  'A kitevők közös nevezője $6$:</p>'
                  '$$\\frac{4}{6}+\\frac{1}{6}-\\frac{3}{6}=\\frac{2}{6}=\\frac13,$$'
                  '<p>tehát az eredmény $a^{1/3}=\\sqrt[3]{a}$.</p>')),
   gyakorolj(FGY + "#alap-12", "A 12–17", FGY + "#kozep-10", "K 10–14"),
   brief('<b>X. Károly professzor:</b> Vihar Vera elvégezte a dolgát, kadét — innen én veszem át. '
         'Van egy egyenlet, amit a valós számok minden ereje sem tud megoldani: $x^{2}=-1$. '
         'Nem azért, mert nehéz. Azért, mert a megoldása <b>nincs benne</b> abban a világban, '
         'amit eddig ismertél. Dr. Baljós már régen kilépett ebből a világból. '
         'Ideje utánamennünk.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

ki = []
ki.append(lap(**T, fajl="tananyag-gyokvonas.html",
              cim="Gyökvonás", cim_tiszta="Gyökvonás",
              alcim="Az $n$-edik gyök definíciója páros és páratlan gyökkitevőre, a "
                    "$\\sqrt[n]{a^{n}}=|a|$ csapda, valamint a gyökvonás hat azonossága.",
              chip="A Képzelet Határa · 3/8", szakaszok=B1,
              elozo=("feladatok-hatvanyozas.html", "Feladatok — hatványozás"),
              kovetkezo=("tananyag-muveletek-gyokokkel.html", "Műveletek a gyökökkel")))
ki.append(lap(**T, fajl="tananyag-muveletek-gyokokkel.html",
              cim="Műveletek a gyökökkel", cim_tiszta="Műveletek a gyökökkel",
              alcim="Tényező kivitele és bevitele, hasonló tagok összevonása, szorzás nevezetes "
                    "azonosságokkal, beágyazott gyökök és gyökök összehasonlítása.",
              chip="A Képzelet Határa · 4/8", szakaszok=B2,
              elozo=("tananyag-gyokvonas.html", "Gyökvonás"),
              kovetkezo=("tananyag-gyoktelenites-es-racionalis-kitevo.html",
                         "Gyöktelenítés és racionális kitevő")))
ki.append(lap(**T, fajl="tananyag-gyoktelenites-es-racionalis-kitevo.html",
              cim="Gyöktelenítés és racionális kitevő",
              cim_tiszta="Gyöktelenítés és racionális kitevő",
              alcim="A nevező gyöktelenítése egy- és kéttagú esetben, a racionális kitevőjű "
                    "hatvány értelmezése, valamint hatvány és gyök együttes kezelése.",
              chip="A Képzelet Határa · 5/8", szakaszok=B3,
              elozo=("tananyag-muveletek-gyokokkel.html", "Műveletek a gyökökkel"),
              kovetkezo=("feladatok-gyokvonas.html", "Feladatok — gyökvonás")))

for u in ki:
    print("✓", os.path.basename(u))
