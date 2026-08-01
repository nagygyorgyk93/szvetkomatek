# -*- coding: utf-8 -*-
"""2e/01 — összefoglaló (F4), terepküldetés (F5p), Danger Room házi (F6h), témakör-index (F5)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, GYOKER, mat
from fgy_common import cards, oldal, w

T = dict(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
         temakor="Hatványozás, gyökvonás, komplex számok")

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import (symbols, I, Rational as R, simplify, expand, sqrt, root, Integer,
                   Abs, re as Re, im as Im, conjugate, solve, Eq)
a, b, c, x = symbols('a b c x', positive=True)
xr, yr = symbols('xr yr', real=True)
n = symbols('n', integer=True, nonnegative=True)
E = []
def ell(nev, kif, vart):
    if simplify(kif - vart) != 0:
        E.append((nev, simplify(kif), vart))

for nev, k, v in [
  # terepküldetés
  ("TI1", Integer(2)**12*Integer(2)**9*Integer(2)**-3, Integer(2)**18),
  ("TI2", Integer(6)**5*Integer(3)**-2/(Integer(2)**3*Integer(3)**2), 12),
  ("TI3", R(42,10)*Integer(10)**7/(6*Integer(10)**-3), 7*Integer(10)**9),
  ("TI4", simplify((5**(n+2)-5**n)/5**(n+1)), R(24,5)),
  ("TII1", 12/sqrt(6), 2*sqrt(6)),
  ("TII2", 10/(sqrt(7)-sqrt(2)), 2*(sqrt(7)+sqrt(2))),
  ("TII3", root(16*a**8*b**12, 4), 2*a**2*b**3),
  ("TII4", root(a**4,3)*sqrt(a)/root(a,6), a**R(5,3)),
  ("TIII1", Abs(6+8*I), 10), ("TIII1b", conjugate(2-3*I), 2+3*I),
  ("TIII2", simplify(((6+8*I)+(2-3*I))/2), 4+R(5,2)*I),
  ("TIII3", expand((6+8*I)*(2-3*I)), 36-2*I),
  ("TIII4", simplify(20/(3-I)), 6+2*I),
  ("TIII5", expand(I**2027+I**2026), -1-I),
  # Danger Room
  ("DA1", Integer(3)**-2, R(1,9)), ("DA1b", R(2,5)**-1, R(5,2)),
  ("DA1c", Integer(-2)**-3, R(-1,8)),
  ("DA3a", sqrt(225), 15), ("DA3c", root(625,4), 5),
  ("DA4a", sqrt(48), 4*sqrt(3)), ("DA4b", sqrt(162), 9*sqrt(2)),
  ("DA4c", root(24,3), 2*root(3,3)),
  ("DA5", sqrt(12)+sqrt(75)-sqrt(27), 4*sqrt(3)),
  ("DA6a", 8/sqrt(2), 4*sqrt(2)),
  ("DA6b", 3/(sqrt(6)-sqrt(3)), sqrt(6)+sqrt(3)),
  ("DA7a", Integer(16)**R(1,4), 2), ("DA7b", Integer(27)**R(-2,3), R(1,9)),
  ("DA7c", Integer(100)**R(1,2), 10),
  ("DA8", Abs(-3+4*I), 5),
  ("DA9a", expand((2+I)+(3-4*I)), 5-3*I), ("DA9b", expand((2+I)*(3-4*I)), 10-5*I),
  ("DA9c", expand((5+I)-(2+6*I)), 3-5*I),
  ("DK1", (a**-2*b**3/c)**-2*(a**-3/b**4), a*c**2/b**10),
  ("DK2", simplify((3**(n+2)+3**(n+1))/3**n), 12),
  ("DK3", sqrt(x*root(x**2,3)), root(x**5,6)),
  ("DK6", simplify((4+3*I)/(2-I)), 1+2*I),
  ("DN1", (1/(sqrt(5)-2)-1/(sqrt(5)+2))**2, 16),
  ("DN3", expand((1+I)**10), 32*I),
]:
    ell(nev, k, v)
for nev, egy, vart in [("TIII6", Eq(2*(xr+yr*I)+3*conjugate(xr+yr*I), 25-5*I), 5+5*I),
                       ("DN2", Eq(3*(xr+yr*I)-2*conjugate(xr+yr*I), 5+15*I), 5+3*I)]:
    s = solve([Eq(Re(egy.lhs-egy.rhs), 0), Eq(Im(egy.lhs-egy.rhs), 0)], [xr, yr], dict=True)[0]
    if simplify(s[xr]+s[yr]*I - vart) != 0:
        E.append((nev, s[xr]+s[yr]*I, vart))
assert not E, E[:5]
assert sqrt(2) < root(3,3) < root(7,4)
assert root(9,3) > sqrt(4)
print("sympy önteszt: OK")

# ==================================================================== F4

OSSZ = [
 ("Hatványozás", [
  '<p><b>Definíció:</b> $a^{n}$ az $n$ tényezős szorzat '
  '(<a href="tananyag-hatvanyozas.html#def-hatvany">→ tananyag</a>). '
  '<b>Egész kitevő</b> ($a\\neq 0$): $a^{0}=1$, $a^{-n}=\\dfrac{1}{a^{n}}$, '
  '$\\left(\\dfrac{a}{b}\\right)^{-n}=\\left(\\dfrac{b}{a}\\right)^{n}$ '
  '(<a href="tananyag-hatvanyozas.html#def-egesz-kitevo">→</a>). '
  'A $0^{0}$ <b>nincs értelmezve</b>.</p>',
  '<p><b>Azonosságok</b> (<a href="tananyag-hatvanyozas.html#tetel-hatvany-azonossagok">→</a>): '
  '$a^{m}a^{n}=a^{m+n}$ · $\\dfrac{a^{m}}{a^{n}}=a^{m-n}$ · $\\left(a^{m}\\right)^{n}=a^{mn}$ · '
  '$a^{m}b^{m}=(ab)^{m}$ · $\\dfrac{a^{m}}{b^{m}}=\\left(\\dfrac{a}{b}\\right)^{m}$.</p>',
  '<p><b>Előjel:</b> $-2^{4}=-16$, de $(-2)^{4}=16$; a negatív <b>kitevő</b> soha nem tesz '
  'negatívvá ($(-2)^{-2}=\\frac14$) '
  '(<a href="tananyag-hatvanyozas.html#s4">→</a>). '
  '<b>Nagyságrend:</b> $a&gt;1$ és $m&gt;n$ → $a^{m}&gt;a^{n}$; $0&lt;a&lt;1$ esetén fordítva '
  '(<a href="tananyag-hatvanyozas.html#tetel-hatvany-elojel">→</a>).</p>',
  '<p><b>Kitevőben betű:</b> emelj ki! Pl. '
  '$\\dfrac{3^{n+2}-3^{n}}{3^{n+1}}=\\dfrac{3^{n}(9-1)}{3^{n}\\cdot 3}=\\dfrac{8}{3}$ '
  '(<a href="tananyag-hatvanyozas.html#pelda-kitevoben-betu">→</a>).</p>',
 ]),
 ("A hatványfüggvény", [
  '<p><b>Páros kitevő</b> ($y=x^{2k}$): $D=\\mathbb{R}$, $\\mathcal{R}=[0,+\\infty)$, '
  '$y$-tengelyre <b>tükrös</b>, egy zérushely ($x=0$), konvex '
  '(<a href="tananyag-hatvanyfuggveny.html#tetel-paros-kitevo">→</a>).</p>',
  '<p><b>Páratlan kitevő</b> ($y=x^{2k+1}$): $D=\\mathcal{R}=\\mathbb{R}$, <b>origóra</b> '
  'szimmetrikus, mindenütt növekvő '
  '(<a href="tananyag-hatvanyfuggveny.html#tetel-paratlan-kitevo">→</a>).</p>',
  '<p><b>Negatív kitevő</b> ($y=x^{-n}$): $D=\\mathbb{R}\\setminus\\{0\\}$, hiperbola, '
  'a két tengely <b>aszimptota</b>; páros $n$ → mindkét ág fent, páratlan $n$ → 1. és 3. síknegyed '
  '(<a href="tananyag-hatvanyfuggveny.html#tetel-negativ-kitevo">→</a>).</p>',
  '<p><b>Kölcsönös helyzet:</b> ha $x\\in(0,1)$: $x&gt;x^{2}&gt;x^{3}&gt;\\ldots$; '
  'ha $x&gt;1$: $x&lt;x^{2}&lt;x^{3}&lt;\\ldots$ '
  '(<a href="tananyag-hatvanyfuggveny.html#tetel-kolcsonos-helyzet">→</a>).</p>',
 ]),
 ("Gyökvonás", [
  '<p><b>Definíció:</b> $\\sqrt[n]{a}$ — <b>páratlan</b> $n$: minden valós $a$-ra létezik, egyértelmű; '
  '<b>páros</b> $n$: csak $a\\ge 0$-ra, és az érték <b>nemnegatív</b> '
  '(<a href="tananyag-gyokvonas.html#def-nedik-gyok">→</a>).</p>',
  '<p><b>A nagy csapda:</b> $\\left(\\sqrt[n]{a}\\right)^{n}=a$ mindig, de</p>'
  '$$\\sqrt[n]{a^{n}}=\\begin{cases} a, &amp; n \\text{ páratlan},\\\\ |a|, &amp; n \\text{ páros}.\\end{cases}$$'
  '<p>(<a href="tananyag-gyokvonas.html#tetel-gyok-hatvany">→</a>) '
  'Ha a feladat kiköti, hogy a betűk pozitívak, az abszolút érték elhagyható.</p>',
  '<p><b>Azonosságok</b> ($a,b\\ge0$) '
  '(<a href="tananyag-gyokvonas.html#tetel-gyok-azonossagok">→</a>): '
  '$\\sqrt[n]{a}\\sqrt[n]{b}=\\sqrt[n]{ab}$ · '
  '$\\dfrac{\\sqrt[n]{a}}{\\sqrt[n]{b}}=\\sqrt[n]{\\dfrac{a}{b}}$ · '
  '$\\left(\\sqrt[n]{a}\\right)^{m}=\\sqrt[n]{a^{m}}$ · '
  '$\\sqrt[m]{\\sqrt[n]{a}}=\\sqrt[mn]{a}$ · '
  '$\\sqrt[n]{a^{m}}=\\sqrt[nk]{a^{mk}}$ · $b\\sqrt[n]{a}=\\sqrt[n]{ab^{n}}$. '
  '<b>Nincs</b> ilyen: $\\sqrt{a+b}=\\sqrt{a}+\\sqrt{b}$ — ellenpélda $9$ és $16$.</p>',
 ]),
 ("Műveletek és gyöktelenítés", [
  '<p><b>Kihozatal/bevitel:</b> keresd a legnagyobb teljes hatvány osztót — $\\sqrt{72}=6\\sqrt2$; '
  'visszafelé $3\\sqrt5=\\sqrt{45}$ '
  '(<a href="tananyag-muveletek-gyokokkel.html#pelda-kihozatal">→</a>). '
  '<b>Összevonás:</b> csak <b>hasonló</b> (azonos gyök alatti) tagok '
  '(<a href="tananyag-muveletek-gyokokkel.html#pelda-osszevonas">→</a>).</p>',
  '<p><b>Nevezetes azonosságok:</b> '
  '$\\left(\\sqrt a+\\sqrt b\\right)\\left(\\sqrt a-\\sqrt b\\right)=a-b$ és '
  '$\\left(\\sqrt a\\pm\\sqrt b\\right)^{2}=a\\pm 2\\sqrt{ab}+b$ '
  '(<a href="tananyag-muveletek-gyokokkel.html#tetel-gyokos-nevezetes">→</a>).</p>',
  '<p><b>Gyöktelenítés:</b> egytagú nevezőnél olyan tényezővel bővíts, hogy teljes hatvány '
  'keletkezzen ($\\frac{5}{\\sqrt[3]{4}}\\to\\sqrt[3]2$-vel) '
  '(<a href="tananyag-gyoktelenites-es-racionalis-kitevo.html#pelda-egytagu">→</a>); '
  'kéttagúnál a <b>konjugálttal</b> — és a <b>számlálót is</b> szorozd! '
  '(<a href="tananyag-gyoktelenites-es-racionalis-kitevo.html#pelda-kettagu">→</a>)</p>',
  '<p><b>Összehasonlítás:</b> hozd közös gyökkitevőre (a gyökkitevők LKT-ja), aztán elég a '
  'gyök alatti számokat összevetni '
  '(<a href="tananyag-muveletek-gyokokkel.html#pelda-osszehasonlitas">→</a>).</p>',
 ]),
 ("Racionális kitevőjű hatvány", [
  '<p><b>Definíció</b> ($a&gt;0$): $a^{\\frac{m}{n}}=\\sqrt[n]{a^{m}}$ '
  '(<a href="tananyag-gyoktelenites-es-racionalis-kitevo.html#def-racionalis-kitevo">→</a>). '
  'Ezzel a hatványozás <b>öt azonossága minden racionális kitevőre</b> érvényes.</p>',
  '<p><b>Miért kell $a&gt;0$?</b> Negatív alapnál $\\sqrt[3]{-8}=-2$, de '
  '$\\sqrt[6]{(-8)^{2}}=2$ — pedig $\\frac13=\\frac26$. '
  '<b>Stratégia:</b> írj mindent tört kitevőre, add össze a kitevőket, majd — ha kell — '
  'írd vissza gyökös alakba '
  '(<a href="tananyag-gyoktelenites-es-racionalis-kitevo.html#pelda-vegyes">→</a>).</p>',
 ]),
 ("Komplex számok", [
  '<p><b>Képzetes egység:</b> $i^{2}=-1$; <b>algebrai alak:</b> $z=x+yi$, ahol '
  '$x=\\operatorname{Re}(z)$, $y=\\operatorname{Im}(z)$ — mindkettő <b>valós</b> '
  '(<a href="tananyag-komplex-szam-fogalma.html#def-komplex-szam">→</a>). '
  '<b>Egyenlőség:</b> $z_{1}=z_{2}$ pontosan akkor, ha a valós ÉS a képzetes részek egyenlők — '
  'egy komplex egyenlet <b>két</b> valós egyenlet '
  '(<a href="tananyag-komplex-szam-fogalma.html#tetel-komplex-egyenloseg">→</a>).</p>',
  '<p><b>Gauss-sík:</b> $z=x+yi$ ↔ az $(x;y)$ pont. <b>Konjugált:</b> $\\overline{z}=x-yi$ '
  '(tükrözés a valós tengelyre); <b>modulusz:</b> $|z|=\\sqrt{x^{2}+y^{2}}$ (a helyvektor hossza) '
  '(<a href="tananyag-komplex-szam-fogalma.html#def-konjugalt-modulusz">→</a>). '
  'Kulcs: $z\\cdot\\overline{z}=|z|^{2}$ — mindig <b>valós</b> '
  '(<a href="tananyag-komplex-szam-fogalma.html#tetel-z-zkonj">→</a>).</p>',
  '<p><b>Műveletek:</b> összeadás/kivonás tagonként; szorzás kibontással, $i^{2}\\to-1$ '
  'helyettesítéssel; <b>osztás:</b> bővíts a nevező konjugáltjával — ugyanaz a fogás, mint a '
  'gyöktelenítés '
  '(<a href="tananyag-muveletek-komplex-szamokkal.html#tetel-komplex-osztas">→</a>).</p>',
  '<p><b>$i$ hatványai — négyes ciklus:</b> $i^{4k}=1$, $i^{4k+1}=i$, $i^{4k+2}=-1$, '
  '$i^{4k+3}=-i$; oszd a kitevőt $4$-gyel és nézd a maradékot '
  '(<a href="tananyag-i-hatvanyai-es-egyenletek.html#tetel-i-hatvanyai">→</a>).</p>',
  '<p><b>Egyenletek:</b> $az=b$ → osztás (konjugálttal bővítve). Ha $z$ és $\\overline{z}$ is '
  'szerepel: írd $z=x+yi$ alakban, és bontsd két valós egyenletre '
  '(<a href="tananyag-i-hatvanyai-es-egyenletek.html#pelda-z-es-konjugalt">→</a>).</p>',
  doboz("csapda", "Amire a dolgozaton a legtöbben ráfutnak",
        '<p>1) $\\sqrt{a^{2}}=|a|$, nem $a$. &nbsp; 2) $-2^{4}\\neq(-2)^{4}$. &nbsp; '
        '3) $(2i)^{2}=-4$, nem $-2$. &nbsp; 4) Bővítéskor a <b>számlálót is</b> szorozd. &nbsp; '
        '5) Negatív szám négyzetgyökét ne írd $\\sqrt{-9}$ alakban — az $x^{2}=-9$ '
        'megoldásai $\\pm 3i$.</p>'),
  '<div class="gyakorolj"><span class="ikon">🎯</span><p>Élesben: a '
  '<a href="feladatok-komplex-szamok.html#gyak-dolgozat">gyakorló dolgozattal</a> mérd fel magad, '
  'majd indulj a <a href="terepkuldetes.html">Genoshai terepküldetésre</a>!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Taktikai memóriakártya",
    cim_tiszta="Taktikai memóriakártya", itt="Taktikai memóriakártya",
    alcim="A Képzelet Határa minden definíciója, azonossága és fogása egy helyen — "
          "ismétléshez, dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip="A Képzelet Határa · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-komplex-szamok.html", "Feladatok — komplex számok"),
    kovetkezo=("terepkuldetes.html", "Genoshai terepküldetés"))
print("✓ osszefoglalo.html")

# ==================================================================== F5p

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Professor X:</b> Kadét, ez már nem szimuláció. A Cerebro bemérte Sinister bázisát '
         '<b>Genosha</b> szigetén: egy rezonancia-torony, amely az M-Hullámot erősíti. '
         'Három védelmi réteget kell áttörnie — mindegyikhez más matematikai fegyver kell. '
         'A jelentését <b>egyben</b> adja le: minden fázis végén írja fel a kulcsértéket.'),
   '<p class="lead">Ez a küldetés a teljes témakört használja: hatványozást, gyökvonást és '
   'komplex számokat. Dolgozz füzetben, a végén pedig foglald össze a három fázis eredményét '
   'egyetlen jelentésben. <b>A megoldások nincsenek fent</b> — ezt a bevetést a tanárod értékeli.</p>',
 ]),
 ("Fázis I — Az energiaszint dekódolása", [
   doboz("pelda", "I. védelmi réteg: a generátorok",
         '<p>A torony három generátora rendre $2^{12}$, $2^{9}$ és $2^{-3}$ egységnyi energiát ad le.</p>'
         '<ol class="reszfeladatok">'
         '<li>Add meg a három energia <b>szorzatát</b> egyetlen hatvány alakjában!</li>'
         '<li>A pajzs energiaigénye $\\dfrac{6^{5}\\cdot 3^{-2}}{2^{3}\\cdot 3^{2}}$. '
         'Számítsd ki a <b>pontos értékét</b>!</li>'
         '<li>A műszerek $4{,}2\\cdot 10^{7}$ és $6\\cdot 10^{-3}$ mérőszámot mutatnak. '
         'Mennyi a <b>hányadosuk</b> normálalakban?</li>'
         '<li>Az M-Hullám erőssége $\\dfrac{5^{n+2}-5^{n}}{5^{n+1}}$, ahol $n$ a lüktetés sorszáma. '
         'Mutasd meg, hogy az érték <b>nem függ $n$-től</b>, és add meg!</li>'
         '</ol>'),
 ]),
 ("Fázis II — A pajzsfrekvencia hangolása", [
   doboz("pelda", "II. védelmi réteg: a rezonanciapajzs",
         '<p>A pajzsot csak akkor lehet kikapcsolni, ha a frekvenciákat <b>pontos, gyöktelenített</b> '
         'alakban adod meg (a torony a közelítő értéket elutasítja).</p>'
         '<ol class="reszfeladatok">'
         '<li>Az alapfrekvencia $f=\\dfrac{12}{\\sqrt{6}}$. Gyöktelenítsd!</li>'
         '<li>A rezonanciafrekvencia $r=\\dfrac{10}{\\sqrt{7}-\\sqrt{2}}$. Gyöktelenítsd!</li>'
         '<li>A csillapítás $c=\\sqrt[4]{16a^{8}b^{12}}$, ahol $a,b&gt;0$. Egyszerűsítsd!</li>'
         '<li>A torony teljesítménye $P=\\dfrac{\\sqrt[3]{a^{4}}\\cdot\\sqrt{a}}{\\sqrt[6]{a}}$ '
         '($a&gt;0$). Add meg <b>racionális kitevős</b> alakban!</li>'
         '<li>A záróellenőrzés: melyik nagyobb, $\\sqrt[3]{9}$ vagy $\\sqrt{4}$? '
         'Számológép nélkül indokolj!</li>'
         '</ol>'),
 ]),
 ("Fázis III — A kapu koordinátái", [
   doboz("pelda", "III. védelmi réteg: a dimenziókapu",
         '<p>A kapu a <b>Gauss-síkon</b> nyílik. Két sarokpontja $z_{1}=6+8i$ és $z_{2}=2-3i$.</p>'
         '<ol class="reszfeladatok">'
         '<li>Ábrázold a két pontot, és add meg $\\left|z_{1}\\right|$-et és '
         '$\\overline{z_{2}}$-t!</li>'
         '<li>A kapu középpontja $\\dfrac{z_{1}+z_{2}}{2}$. Számítsd ki!</li>'
         '<li>A stabilizáló kód $z_{1}\\cdot z_{2}$. Számítsd ki!</li>'
         '<li>A zárókulcs az a $z$, amelyre $(3-i)z=20$. Oldd meg!</li>'
         '<li>Az önmegsemmisítő szekvencia $i^{2027}+i^{2026}$. Mennyi?</li>'
         '<li><b>Sinister utolsó csapdája:</b> a kapu csak akkor marad nyitva, ha megtalálod '
         'azt a $z$ komplex számot, amelyre $2z+3\\overline{z}=25-5i$.</li>'
         '</ol>'),
   doboz("erdekesseg", "Jelentés a Főhadiszállásnak",
         '<p>Zárásként foglald össze <b>egyetlen táblázatban</b> a három fázis kulcsértékeit: '
         'az energiaszintet, a két gyöktelenített frekvenciát és a kapu zárókulcsát. '
         'Írj mellé <b>2–3 mondatot</b> arról, melyik fázisnál melyik azonosságot használtad — '
         'a Professor X a gondolatmenetre is kíváncsi, nem csak a számokra.</p>'),
   brief('<b>Professor X:</b> Ha a hat kulcsérték helyes, a torony leáll, és Genosha felett '
         'elül az M-Hullám. De ne dőljön hátra, kadét: Sinister nem lineárisan gondolkodik. '
         'A következő támadás <b>másodfokon</b> érkezik — és ott már a röppályát is ki kell '
         'számolnia. Wolverine és Cyclops készen áll.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim="Genoshai terepküldetés",
    cim_tiszta="Genoshai terepküldetés", itt="Genoshai terepküldetés",
    alcim="Háromfázisú bevetés Sinister rezonancia-tornya ellen: hatványok, gyöktelenített "
          "frekvenciák és a dimenziókapu komplex koordinátái.",
    chip="A Képzelet Határa · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Taktikai memóriakártya"),
    kovetkezo=("index.html", "Vissza a témakörhöz"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h

DR_A = [
 ("Számítsd ki a pontos értéket!",
  ["$3^{-2}$", "$\\left(\\dfrac{2}{5}\\right)^{-1}$", "$(-2)^{-3}$", "$7^{0}$"],
  ["$\\dfrac{1}{9}$", "$\\dfrac{5}{2}$", "$-\\dfrac{1}{8}$", "$1$"], True),
 ("Írd fel egyetlen hatvány alakjában! $(a,b,c&gt;0)$",
  ["$a^{5}a^{-2}$", "$\\left(b^{-3}\\right)^{2}$", "$\\dfrac{c^{4}}{c^{-1}}$"],
  ["$a^{3}$", "$b^{-6}$", "$c^{5}$"], True),
 ("Számítsd ki!",
  ["$\\sqrt{225}$", "$\\sqrt[3]{-1000}$", "$\\sqrt[4]{625}$"],
  ["$15$", "$-10$", "$5$"], True),
 ("Hozd ki a gyökjel alól a legnagyobb tényezőt!",
  ["$\\sqrt{48}$", "$\\sqrt{162}$", "$\\sqrt[3]{24}$"],
  ["$4\\sqrt{3}$", "$9\\sqrt{2}$", "$2\\sqrt[3]{3}$"], True),
 ("Végezd el a műveleteket! $\\sqrt{12}+\\sqrt{75}-\\sqrt{27}$", None, "$4\\sqrt{3}$"),
 ("Gyöktelenítsd!",
  ["$\\dfrac{8}{\\sqrt{2}}$", "$\\dfrac{3}{\\sqrt{6}-\\sqrt{3}}$"],
  ["$4\\sqrt{2}$", "$\\sqrt{6}+\\sqrt{3}$"], True),
 ("Számítsd ki!",
  ["$16^{\\frac{1}{4}}$", "$27^{-\\frac{2}{3}}$", "$100^{\\frac{1}{2}}$"],
  ["$2$", "$\\dfrac{1}{9}$", "$10$"], True),
 ("Legyen $z=-3+4i$. Add meg a valós részét, a képzetes részét, a konjugáltját és a moduluszát!",
  None, "$\\operatorname{Re}(z)=-3$, $\\operatorname{Im}(z)=4$, $\\overline{z}=-3-4i$, $|z|=5$"),
 ("Végezd el a műveleteket!",
  ["$(2+i)+(3-4i)$", "$(2+i)(3-4i)$", "$(5+i)-(2+6i)$"],
  ["$5-3i$", "$10-5i$", "$3-5i$"], True),
]

DR_K = [
 ("Egyszerűsítsd! $(a,b,c&gt;0)$  "
  "$\\left(\\dfrac{a^{-2}b^{3}}{c}\\right)^{-2}\\cdot\\dfrac{a^{-3}}{b^{4}}$",
  None, "$\\dfrac{ac^{2}}{b^{10}}$"),
 ("Hozd egyszerűbb alakra! $(n\\in\\mathbb{N})$  $\\dfrac{3^{n+2}+3^{n+1}}{3^{n}}$",
  None, "$12$"),
 ("Egyszerűsítsd! $(x&gt;0)$  $\\sqrt{x\\sqrt[3]{x^{2}}}$", None, "$\\sqrt[6]{x^{5}}$"),
 ("Rendezd növekvő sorrendbe: $\\sqrt[4]{7}$, $\\sqrt{2}$, $\\sqrt[3]{3}$", None,
  "$\\sqrt{2}&lt;\\sqrt[3]{3}&lt;\\sqrt[4]{7}$"),
 ("Add meg a függvény paritását, értelmezési tartományát és értékkészletét!",
  ["$y=x^{-4}$", "$y=x^{5}$"],
  ["Páros; $D=\\mathbb{R}\\setminus\\{0\\}$, $\\mathcal{R}=(0,+\\infty)$.",
   "Páratlan; $D=\\mathcal{R}=\\mathbb{R}$."], False),
 ("Számítsd ki! $\\dfrac{4+3i}{2-i}$", None, "$1+2i$"),
]

DR_N = [
 ("Számítsd ki a pontos értéket! "
  "$\\left(\\dfrac{1}{\\sqrt{5}-2}-\\dfrac{1}{\\sqrt{5}+2}\\right)^{2}$", None, "$16$"),
 ("Oldd meg a komplex számok halmazán! $3z-2\\overline{z}=5+15i$", None, "$z=5+3i$"),
 ("Számítsd ki! $(1+i)^{10}$", None, "$32i$"),
]

dr_brief = ('<div class="brief"><p>🕹️ <b>SZVETI:</b> <b>Veszélyterem</b> — A Képzelet Határa modul. '
            'Ez a Danger Room otthoni edzésváltozata: a <b>teljes témakört</b> lefedi — hatványozás, '
            'hatványfüggvény, gyökvonás, gyöktelenítés, racionális kitevő és komplex számok. '
            'Haladj a fokozatokon: zöld → sárga → piros. A végeredményt lenyithatod, de előbb '
            'küzdd le magad!</p></div>')

dr_body = (f'    {dr_brief}\n'
           '    <h2 id="alap">🟢 Alapfokozat</h2>\n' + cards(DR_A, "alap", "alap") +
           '\n    <h2 id="kozep">🟡 Középfokozat</h2>\n' + cards(DR_K, "kozep", "kozep") +
           '\n    <h2 id="nehez">🔴 Nehéz fokozat</h2>\n' + cards(DR_N, "nehez", "nehez"))

oldal(**T, fajl="feladatok-hazi.html", cim="Danger Room",
      h1="🕹️ Danger Room — házi feladatgyűjtemény", itt="Danger Room — házi",
      alcim="Egyetlen, a teljes témakört lefedő házi feladatsor, óraszám-arányosan. "
            "Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      sections_html=dr_body,
      prev="index.html", prevc="Témakör Főhadiszállása",
      nxt="osszefoglalo.html", nxtc="Taktikai memóriakártya")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5 index

def kartya(href, cim, le):
    return (f'      <a class="kartya" href="{href}">\n        <h3>{cim}</h3>\n'
            f'        <p class="le">{w(le)}</p>\n      </a>')

K = {}
K[1] = kartya("tananyag-hatvanyozas.html", "Hatványozás egész kitevővel",
        "A hatvány fogalma és azonosságai, a nulla és a negatív kitevő, előjelszabályok, összetett kifejezések")
K[2] = kartya("tananyag-hatvanyfuggveny.html", "A hatványfüggvény és grafikonja",
        "Az $y=x^{{n}}$ családok páros, páratlan és negatív kitevőre, kölcsönös helyzet, aszimptoták")
K[3] = kartya("tananyag-gyokvonas.html", "Gyökvonás",
        "Az $n$-edik gyök definíciója, a $\\\\sqrt[n]{{a^{{n}}}}=|a|$ csapda és a gyökvonás hat azonossága")
K[4] = kartya("tananyag-muveletek-gyokokkel.html", "Műveletek a gyökökkel",
        "Kihozatal és bevitel, összevonás, nevezetes azonosságok, beágyazott gyökök, összehasonlítás")
K[5] = kartya("tananyag-gyoktelenites-es-racionalis-kitevo.html", "Gyöktelenítés és racionális kitevő",
        "Egy- és kéttagú nevező, a tört kitevő értelmezése, hatvány és gyök együtt")
K[6] = kartya("tananyag-komplex-szam-fogalma.html", "A komplex szám fogalma",
        "Számhalmaz-bővítés, a képzetes egység, algebrai alak, Gauss-sík, konjugált és modulusz")
K[7] = kartya("tananyag-muveletek-komplex-szamokkal.html", "Műveletek a komplex számokkal",
        "A négy alapművelet — az osztás a nevező konjugáltjával való bővítéssel")
K[8] = kartya("tananyag-i-hatvanyai-es-egyenletek.html", "Az $i$ hatványai és egyenletek",
        "A négyes ciklus, összetett kifejezések, lineáris egyenletek, $z$ és $\\\\overline{{z}}$ együtt")
K[9] = kartya("feladatok-hatvanyozas.html", "🏋️ Hatványozás — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker")
K[10] = kartya("feladatok-gyokvonas.html", "🏋️ Gyökvonás — feladatok",
        "Alap · Közép · Nehéz + Joker, a végén <b>gyakorló ellenőrzővel</b>")
K[11] = kartya("feladatok-komplex-szamok.html", "🏋️ Komplex számok — feladatok",
        "Alap · Közép · Nehéz + Joker, a végén <b>gyakorló dolgozattal</b> a teljes témakörre")
K[12] = kartya("feladatok-hazi.html", "🕹️ Danger Room — házi feladatok",
        "A teljes témakört lefedő házi feladatsor, óraszám-arányosan")
K[13] = kartya("terepkuldetes.html", "🌋 Genoshai terepküldetés",
        "Háromfázisú bevetés Sinister rezonancia-tornya ellen — a teljes témakör egyben")
K[14] = kartya("osszefoglalo.html", "📇 Taktikai memóriakártya",
        "Minden definíció, azonosság és tipikus csapda egy helyen — dolgozat előtti átfutáshoz")

INDEX = f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hatványozás, gyökvonás, komplex számok | 2e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="2e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">√</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">2e</span></a> ›
  <span class="itt">Hatványozás, gyökvonás, komplex számok</span>
</nav>
<div class="hero">
  <h1>Hatványozás, gyökvonás, komplex számok</h1>
  <p class="alcim">A hatvány kiterjesztése nulla, negatív és tört kitevőre, a gyökvonás és a
  gyöktelenítés, végül a valós számok halmazának kibővítése a komplex számokkal.</p>
  <div class="meta-sor"><span class="chip ora">22 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧬 <b>Szektor 01 — A Képzelet Határa.</b> Kiképzők: <b>Storm</b>
  (hatványok, gyökök) és <b>Professor X</b> (komplex számok). A Nullpont-anomália lezárása után
  a valóság megremegett: az M-Hullám olyan egyenleteket sodor a kampuszra, amelyeknek a régi
  számhalmazokban <b>nincs megoldásuk</b>. Célod uralni a vihar erejét, visszafejteni a gyökereit —
  majd átlépni a <b>képzelet határán</b>, és megérteni a valóság új, komplex dimenzióit,
  mielőtt <b>Mister Sinister</b> visszafordíthatatlan jövőt kódol a rendszerbe.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>⚡ Hatványozás — Storm</h3>
    <div class="racs">
{K[1]}
{K[2]}
    </div>

    <h3>🌊 Gyökvonás — Storm</h3>
    <div class="racs">
{K[3]}
{K[4]}
{K[5]}
    </div>

    <h3>🧠 Komplex számok — Professor X</h3>
    <div class="racs">
{K[6]}
{K[7]}
{K[8]}
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
{K[9]}
{K[10]}
{K[11]}
{K[12]}
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
{K[13]}
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
{K[14]}
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> altémánként előbb a tananyag-egységek sorban,
    utána a hozzá tartozó feladatgyűjtemény; a témakör végén a Taktikai memóriakártya, majd a
    Genoshai terepküldetés. A Danger Room házi bármikor jöhet — az a saját tempódban végzett edzés.</p>
  </div>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {{delimiters:[
    {{left:'\\\\(', right:'\\\\)', display:false}},
    {{left:'\\\\[', right:'\\\\]', display:true}}
  ]}});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
