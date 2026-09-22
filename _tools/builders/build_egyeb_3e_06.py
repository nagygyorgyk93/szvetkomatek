# -*- coding: utf-8 -*-
"""3e/06 — osszefoglalo (F4), terepkuldetes (F5p), Veszterem (F6h) es a temakor-index (F5).
Kuldetes: A Vegtelen Mutacio. Mentor: Prizma es Kanrak."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, abra, brief, svg_fuggvenyek

T = dict(tagozat="3e", mappa="06-indukcio-sorozatok", temakor="Matematikai indukció. Sorozatok")
KUL = "A Végtelen Mutáció"
ZOLD, KEK, BORO, PIROS = "#047857", "#3b82f6", "#f59e0b", "#ef4444"

A1 = "tananyag-sorozat-fogalma.html"
A2 = "tananyag-monotonitas-es-korlatossag.html"
B1 = "tananyag-szamtani-sorozat.html"
B2 = "tananyag-mertani-sorozat.html"
C = "tananyag-indukcio.html"
FGY = "feladatok-sorozatok.html"

# ==================================================================== önteszt
from sympy import (symbols, simplify, Rational as Q, solve, Eq, summation, factor, expand, N as NN)
E = []


def chk(nev, g, w, tur=None):
    ok = abs(float(NN(g)) - float(w)) <= tur if tur is not None else simplify(g - w) == 0
    if not ok:
        E.append((nev, g, w))


n, k, a1, d, b1, q = symbols("n k a1 d b1 q", positive=True)
i = symbols("i", integer=True, positive=True)
u, v = symbols("u v", real=True)   # elojel-korlat nelkuli ismeretlenek
# a ket osszegkeplet levezetese (szimbolikusan)
chk("szamtani-Sn", simplify(summation(a1 + (i - 1)*d, (i, 1, n)) - n*(2*a1 + (n - 1)*d)/2), 0)
chk("szamtani-Sn2", simplify(n*(2*a1 + (n - 1)*d)/2 - n*(a1 + (a1 + (n - 1)*d))/2), 0)
chk("mertani-Sn", simplify(summation(b1*q**(i - 1), (i, 1, 3)) - b1*(q**3 - 1)/(q - 1)), 0)
chk("szamtani-kozep", simplify(((a1 + (k - 2)*d) + (a1 + k*d))/2 - (a1 + (k - 1)*d)), 0)
chk("mertani-kozep", simplify((b1*q**(k - 1))**2 - (b1*q**(k - 2))*(b1*q**k)), 0)
assert not E, E
print("F4 önteszt: OK")


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


# ==================================================================== F4
OSSZ = [
 ("📇 A sorozat", [
  r'<p class="lead">A sorozat minden $n$ természetes számhoz egyetlen valós számot rendel: ez a '
  r'sorozat $n$-edik tagja, $a_n$. Az indexelést $1$-től kezdjük.</p>'
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th>Mit</th><th>Hogyan</th><th>Megjegyzés</th></tr>'
  r'<tr><td>megadás képlettel (' + h(A1, "def-sorozat") + r')</td><td>$a_n$ az $n$ függvényeként</td>'
  r'<td>bármelyik tag egy lépésben megkapható</td></tr>'
  r'<tr><td>megadás rekurzívan (' + h(A1, "def-rekurzio") + r')</td>'
  r'<td>kezdőtag + továbblépési szabály</td><td>kezdőtag nélkül semmit nem határoz meg</td></tr>'
  r'<tr><td>„hányadik tag?”</td><td>oldd meg az $a_n=c$ egyenletet</td>'
  r'<td>csak <b>természetes</b> $n$ jó; különben a szám nem tagja a sorozatnak</td></tr>'
  r'<tr><td>grafikon</td><td>az $(n;a_n)$ pontok</td><td><b>különálló pontok</b>, nem összekötött vonal</td></tr>'
  r'<tr><td>monotonitás (' + h(A2, "def-monoton") + r')</td>'
  r'<td>$a_{n+1}-a_n\gt0$ szigorúan növekvő · $\lt0$ szigorúan csökkenő</td>'
  r'<td><b>minden</b> $n$-re kell teljesülnie — nem elég néhány tag</td></tr>'
  r'<tr><td>korlátosság (' + h(A2, "def-korlatos") + r')</td>'
  r'<td>$k\le a_n\le K$ minden $n$-re</td><td>a korlát nem egyetlen szám: ha $K$ felső korlát, minden '
  r'nála nagyobb is az. A monoton csökkenő sorozat felülről, a növekvő alulról mindig korlátos az első '
  r'tagjával — a másik irányról külön kell dönteni</td></tr>'
  r'</table></div>',
 ]),

 ("📐 Számtani és mértani sorozat", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th></th><th>számtani (' + h(B1, "def-szamtani") + r')</th>'
  r'<th>mértani (' + h(B2, "def-mertani") + r')</th></tr>'
  r'<tr><td>a szabály</td><td>$a_{n+1}=a_n+d$</td><td>$b_{n+1}=b_n\cdot q$ ($b_1\ne0$, $q\ne0$)</td></tr>'
  r'<tr><td>a jellemző adat</td><td>$d=a_{n+1}-a_n$</td><td>$q=\dfrac{b_{n+1}}{b_n}$</td></tr>'
  r'<tr><td>az $n$-edik tag</td><td>$a_n=a_1+(n-1)d$</td><td>$b_n=b_1q^{\,n-1}$</td></tr>'
  r'<tr><td>két tag között</td><td>$a_m=a_k+(m-k)d$</td><td>$b_m=b_k\cdot q^{\,m-k}$</td></tr>'
  r'<tr><td>az első $n$ tag összege</td>'
  r'<td>$S_n=\dfrac{n(a_1+a_n)}{2}=\dfrac n2\bigl(2a_1+(n-1)d\bigr)$</td>'
  r'<td>$S_n=b_1\dfrac{q^{\,n}-1}{q-1}$, ha $q\ne1$; $q=1$ esetén $S_n=n\,b_1$</td></tr>'
  r'<tr><td>a középső tag ($n\ge2$)</td><td>$a_n=\dfrac{a_{n-1}+a_{n+1}}{2}$</td>'
  r'<td>$b_n^{\,2}=b_{n-1}\cdot b_{n+1}$</td></tr>'
  r'<tr><td>a grafikon</td><td>pontok egy <b>egyenesen</b> ($d$ a meredekség)</td>'
  r'<td>$q\gt0$ esetén pontok egy <b>exponenciális</b> görbén; $q\lt0$ esetén a pontok váltakozva a '
  r'tengely fölött és alatt vannak</td></tr>'
  r'<tr><td>mikor melyik</td><td>a szomszédos tagok <b>különbsége</b> állandó</td>'
  r'<td>a szomszédos tagok <b>hányadosa</b> állandó</td></tr>'
  r'</table></div>'
  r'<p><b>Két adat elég.</b> Mindkét sorozatot meghatározza az első tag és a jellemző adat ($d$, '
  r'illetve $q$); ha más két adat ismert, egyenletrendszert írunk fel rájuk. ⚠️ Mértani sorozatnál '
  r'<b>páros</b> lépéstávolságból ($q^2=9$, $q^4=16$ …) a hányados <b>előjele kétféle</b> lehet — '
  r'ilyenkor mindkét esetet végig kell gondolni. Ha a keresett $n$ az összegképletben van, másodfokú '
  r'egyenletre jutunk; ha a kitevőben, a hatványok kiszámításával keressük meg a legkisebb megfelelő '
  r'$n$-t — és a tagszám mindig <b>természetes szám</b>.</p>',
 ]),

 ("Kamat: egyszerű és kamatos", [
  r'<div class="tblwrap"><table class="tt-table">'
  r'<tr><th></th><th>képlet</th><th>milyen sorozat</th></tr>'
  r'<tr><td>egyszerű kamat</td><td>$K_n=K_0\left(1+\dfrac{p}{100}\,n\right)$</td>'
  r'<td><b>számtani</b>: minden évben ugyanannyival nő</td></tr>'
  r'<tr><td>kamatos kamat (' + h(B2, "tetel-kamatos-kamat") + r')</td>'
  r'<td>$K_n=K_0\left(1+\dfrac{p}{100}\right)^{n}$</td>'
  r'<td><b>mértani</b>: minden évben ugyanazzal a szorzóval nő</td></tr>'
  r'<tr><td>évi $t$-szeri jóváírás</td>'
  r'<td>$K_n=K_0\left(1+\dfrac{p}{100\,t}\right)^{t\,n}$</td>'
  r'<td>egy időszakra $\frac pt$ százalék, a jóváírások száma $t\cdot n$</td></tr>'
  r'</table></div>'
  r'<p>A kitevőben azért áll $n$ (és nem $n-1$), mert a kiinduló összeg a <b>nulladik</b> év adata, '
  r'$K_0$ — ez a tudatos kivétel az „1-től indexelünk” megállapodás alól (a mértani sorozat nyelvén '
  r'$b_1=K_0$). Pénznél mindig <b>két tizedesjegyre</b> kerekítünk.</p>',
 ]),

 ("⚠️ Maxi csapdái — amin a legtöbben elcsúsznak", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A hét leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>Index-eltolás:</b> ✗ $a_n=a_1+nd$, ✗ $b_n=b_1q^{\,n}$ — helyesen $a_n=a_1+(n-1)d$ és '
  r'$b_n=b_1q^{\,n-1}$, mert az első tagtól az $n$-edikig csak $n-1$ lépés vezet.</li>'
  r'<li><b>Két tagból a különbség:</b> $a_3=8$, $a_9=32$ esetén nem $9$-cel, hanem a lépések számával, '
  r'$9-3=6$-tal osztunk.</li>'
  r'<li><b>Az összegképlet felezése:</b> ✗ $S_n=n(a_1+a_n)$ — helyesen $S_n=\frac{n(a_1+a_n)}{2}$; '
  r'a kettővel osztás nem maradhat el.</li>'
  r'<li><b>Negatív hányados:</b> $(-2)^4=16$, de $-2^4=-16$; a negatív $q$-t mindig zárójelbe tesszük.</li>'
  r'<li><b>Nem egész sorszám:</b> ha az $a_n=c$ egyenletből tört jön ki, a szám <b>nem tagja</b> a sorozatnak.</li>'
  r'<li><b>Monotonitás néhány tagból:</b> az $a_n=n^2-10n+3$ sorozat az ötödik tagig csökken, '
  r'a hatodiktól nő.</li>'
  r'<li><b>Kamat összeadással:</b> „20 év, évi 10% = 200%” — ez az <b>egyszerű</b> kamat esete; '
  r'kamatos kamatnál a szorzók szorzódnak ($1{,}1^{20}\approx6{,}73$, vagyis $572{,}7\%$).</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A1 + r'">a sorozat fogalma</a> · '
  r'<a href="' + A2 + r'">monotonitás és korlátosság</a> · '
  r'<a href="' + B1 + r'">a számtani sorozat</a> · '
  r'<a href="' + B2 + r'">a mértani sorozat és a kamatos kamat</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FGY + r'">Kiképzési Adattár</a> (alap · közép · nehéz · joker) '
  r'és a <a href="feladatok-hazi.html">Kristály-kamra</a> házi feladatsor.</p>'
  r'<p><b>Külön lapon:</b> a <a href="' + C + r'">hiányos és a teljes indukció</a> — ebből nincs '
  r'számonkérés, de érdemes elolvasni; a témakör zárása pedig '
  r'<a href="terepkuldetes.html">A Végtelen Mutáció</a> küldetés.</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Taktikai memóriakártya — a témakör egy lapon",
    cim_tiszta="Taktikai memóriakártya", itt="Taktikai memóriakártya",
    alcim="A sorozatok képletei, jellemzői és tipikus csapdái egy helyen — ismétléshez, az ellenőrző "
          "előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=OSSZ,
    elozo=(C, "Hiányos és teljes indukció"),
    kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p
EE = []


def ck(nev, g, w, tur=1e-9):
    try:
        ok = abs(float(NN(g)) - float(w)) <= tur
    except TypeError:
        ok = simplify(g - w) == 0
    if not ok:
        EE.append((nev, g, w))


SZ = lambda x1, dd, m: x1 + (m - 1)*dd
SS = lambda x1, dd, m: Q(m, 2)*(2*x1 + (m - 1)*dd)
MB = lambda y1, qq, m: y1*qq**(m - 1)
MSU = lambda y1, qq, m: y1*(qq**m - 1)/(qq - 1)
# I. fazis — kristalyretegek: a1 = 9, d = 7
ck("I-a12", SZ(9, 7, 12), 86)
ck("I-S12", SS(9, 7, 12), 570)
ck("I-kuszob", [m for m in range(1, 60) if SZ(9, 7, m) > 200][0], 29)
ck("I-a29", SZ(9, 7, 29), 205)
ck("I-a28", SZ(9, 7, 28), 198)
ck("I-egyenes", SZ(9, 7, n) - (7*n + 2), 0)
# II. fazis — energiakaszkad: b1 = 4, q = 3
ck("II-b8", MB(4, 3, 8), 8748)
ck("II-S8", MSU(4, 3, 8), 13120)
ck("II-S7", MSU(4, 3, 7), 4372)
ck("II-kuszob", [m for m in range(1, 20) if MSU(4, 3, m) > 10000][0], 8)
# III. fazis — kamat: 150 000 din, evi 8%, 4 ev
ck("III-egyszeru", 150000*(1 + Q(8, 100)*4), 198000)
ck("III-kamatos", round(float(150000*Q(108, 100)**4), 2), 204073.34)
ck("III-negyedev", round(float(150000*(1 + Q(8, 400))**16), 2), 205917.86)
ck("III-kulonbseg", round(float(150000*Q(108, 100)**4 - 198000), 2), 6073.34)
# IV. fazis — Maxi alkeplete: 12n^2 - 24n + 16 egyezik n = 1, 2, 3-ra, n = 4-re nem
for m in (1, 2, 3):
    ck(f"IV-egyezik-{m}", 12*m*m - 24*m + 16, MSU(4, 3, m))
ck("IV-maxi4", 12*16 - 24*4 + 16, 112)
ck("IV-valodi4", MSU(4, 3, 4), 160)
assert not EE, EE
print("F5p önteszt: OK")

SVG_RETEG = svg_fuggvenyek(
    [(lambda u: (7*u + 2)/5, KEK, "y = 7x + 2", [(0, 6.3)])],
    xr=(0, 6.6), yr=(0, 9.5), w=380, h=250, egyseg=("1", "5"), tengely=("n", "aₙ"),
    leiras="A kristályrétegek vastagsága: a pontok egy egyenesre esnek",
    pontok=[(m, (9 + (m - 1)*7)/5, "", ZOLD) for m in range(1, 7)])

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma és Kanrak:</b> Maxi elindította a láncreakciót, és a Kristály Karantén-Zóna '
         'három ütemben mutálódik: előbb egyenletesen vastagodó kristályrétegek, aztán ugrásszerűen '
         'erősödő energiakaszkád, közben pedig a Kristálypára-bank kamatra dolgozó tartaléka. A '
         'feladatod: mindhárom ütemet bemérni, és megmondani, <b>hányadik lépésnél</b> lépi át a '
         'rendszer a kritikus szintet — a bankban pedig azt, mennyit hoz a tartalék. A végén Maxi '
         'saját képletét is ellenőrizd: mert az hazudik.'),
   r'<p>Négy fázis. Minden lépésnél írd le, melyik sorozatot ismerted fel, és melyik képletet '
   r'használtad. Számológép használható: a nem egész eredményeket két tizedesjegyre kerekítsd, és '
   r'jelöld a kerekítést. A választ fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, '
   r'mint máshol a számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><b>Amire szükséged lesz:</b> a számtani és a mértani sorozat $n$-edik tagja és összegképlete, '
   r'az egyszerű és a kamatos kamat, valamint a sorozatok ábrázolása.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — A kristályrétegek", [
   r'<p>A generátor minden lépésben egy új kristályréteget csap ki. Az első réteg vastagsága $9$ '
   r'egység, és minden további réteg $7$ egységgel vastagabb az előzőnél.</p>',
   abra(SVG_RETEG, 'Az első hat réteg vastagsága: $9,\\ 16,\\ 23,\\ 30,\\ 37,\\ 44$. A függőleges '
        'tengely egy osztása $5$ egység.'),
   r'<ol class="reszfeladatok">'
   r'<li>Milyen sorozatot alkotnak a rétegvastagságok? Add meg az $n$-edik tag képletét!</li>'
   r'<li>Mekkora a $12.$ réteg, és mennyi az első $12$ réteg együttes vastagsága?</li>'
   r'<li>A zóna fala akkor repedezik meg, amikor <b>egyetlen réteg</b> eléri a $200$ egység '
   r'vastagságot. Hányadik réteg lesz maga is legalább $200$ egység vastag? <i>(Nem az '
   r'összvastagságot kérdezzük!)</i></li>'
   r'<li>Az ábra pontjai egy egyenesre esnek. Írd fel ennek az egyenesnek az egyenletét, és mondd '
   r'meg, mi a kapcsolat a meredeksége és a sorozat között!</li>'
   r'</ol>',
 ]),

 ("II. fázis — Az energiakaszkád", [
   r'<p>A láncreakció energiája más ütemben nő: az első lépés $4$ egységnyi energiát szabadít fel, '
   r'és minden további lépés az előző <b>háromszorosát</b>.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Milyen sorozatot alkotnak a lépések energiái? Add meg az $n$-edik tag képletét!</li>'
   r'<li>Mekkora energia szabadul fel a $8.$ lépésben?</li>'
   r'<li>Mennyi az első $8$ lépés <b>összenergiája</b>?</li>'
   r'<li>A Karantén-Zóna pajzsa $10\,000$ egységnyi összenergiát bír ki. Hányadik lépésnél szakad át? '
   r'<i>(Számold ki az összeget az előző lépésig is!)</i></li>'
   r'<li>Vesd össze a két fázist: melyik nő gyorsabban, és miért? Hány lépés kell a rétegeknél ahhoz, '
   r'hogy az <b>összvastagság</b> meghaladja a $13\,120$-at? <i>(Elég megbecsülni.)</i></li>'
   r'</ol>',
 ]),

 ("III. fázis — A Kristálypára-bank", [
   r'<p>A Királyi Család tartaléka $150\,000$ dinár, amit $4$ évre helyeztek el évi $8\%$-os '
   r'kamatlábbal. Kerekíts két tizedesjegyre!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Mennyi lenne a tartalék a futamidő végén <b>egyszerű</b> kamat mellett?</li>'
   r'<li>És <b>kamatos</b> kamat mellett, évente egyszeri jóváírással? Mekkora a különbség a kettő '
   r'között?</li>'
   r'<li>Mennyi lenne, ha a kamatot <b>negyedévente</b> írnák jóvá?</li>'
   r'<li>Melyik sorozat írja le az egyszerű, és melyik a kamatos kamatot? Indokold meg!</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Maxi képlete", [
   r'<p>Maxi a kamra falára írta a saját képletét az energiakaszkád összenergiájára:</p>'
   r'$$S_n=12n^2-24n+16 .$$'
   r'<p>Azt állítja, hogy ez minden lépésre igaz, és a pajzs ezért sokkal tovább bírja, mint hinnénk.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Ellenőrizd Maxi képletét $n=1$, $n=2$ és $n=3$ esetén! Mit tapasztalsz?</li>'
   r'<li>Számold ki most $n=4$-re a képlet szerinti és a <b>valódi</b> összenergiát is! Mekkora az '
   r'eltérés?</li>'
   r'<li>Mit tanultál ebből arról, hogy elég-e néhány esetben ellenőrizni egy állítást? Fogalmazd meg '
   r'két-három mondatban — ez a <b>hiányos indukció</b> csapdája '
   r'(<a href="' + C + r'#def-hianyos-indukcio">olvasnivaló</a>).</li>'
   r'<li>Hányadik lépésnél szakadna át a pajzs Maxi képlete szerint, és hányadiknál a valóságban? '
   r'<b>Hány lépésnyi</b> hamis biztonságot ígér a hazugsága? <i>(A küszöböt elég próbálgatással '
   r'megkeresni.)</i></li>'
   r'</ol>',
   brief('<b>Prizma:</b> A láncreakció be van mérve: tudjuk, melyik lépésnél mekkora, és tudjuk, hol '
         'szakad át a pajzs. Maxi arra épített, hogy a falra írt képletét senki nem ellenőrzi elég '
         'sokáig. A számításaidat a tanárod ellenőrzi; a kulcs nem kerül a hálózatra. '
         '<b>A Kristálypára-anomália lezárva.</b>', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: a kristályrétegek, az energiakaszkád, a Kristálypára-bank és Maxi hamis "
          "képlete. Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Taktikai memóriakártya"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — Vészterem
from fgy_common import cards, oldal

HE = []


def hk(nev, g, w, tur=1e-9):
    try:
        ok = abs(float(NN(g)) - float(w)) <= tur
    except TypeError:
        ok = simplify(g - w) == 0
    if not ok:
        HE.append((nev, g, w))


for nev, g, w in [("h1a", Q(5, 2), Q(1 + 4, 2)), ("h1b", Q(6, 4), Q(3, 2)),
                  ("h1c", Q(7, 6), Q(3 + 4, 6)), ("h1d", Q(8, 8), 1)]:
    hk(nev, g, w)
for m, wv in zip(range(1, 5), [2, Q(7, 2), 4, Q(17, 4)]):
    hk(f"h2-{m}", 5 - Q(3, m), wv)
hk("h2-kulonbseg", simplify((5 - 3/(n + 1)) - (5 - 3/n)) - 3/(n*(n + 1)), 0)
hk("h2-korlat", 5 - Q(3, 1000000), 5 - Q(3, 1000000))
hk("h3a", SZ(-4, 6, 20), 110); hk("h3S", SS(-4, 6, 20), 1060)
hk("h3-tagok", [SZ(-4, 6, m) for m in range(1, 5)], [-4, 2, 8, 14]) if False else None
for m, wv in zip(range(1, 5), [-4, 2, 8, 14]):
    hk(f"h3-tag{m}", SZ(-4, 6, m), wv)
hk("h3-egyenes", SZ(-4, 6, n) - (6*n - 10), 0)
hk("h4b", MB(-3, 2, 7), -192); hk("h4S", MSU(-3, 2, 7), -381)
hk("h5a", 120000*(1 + Q(3, 100)*2), 127200)
hk("h5b", round(float(120000*Q(103, 100)**2), 2), 127308.00)
d6 = Q(61 - 25, 16 - 7); a6 = 25 - 6*d6
hk("h6d", d6, 4); hk("h6a1", a6, 1); hk("h6S", SS(a6, d6, 16), 496)
n6 = [m for m in range(1, 40) if SS(3, 5, m) == 366][0]
hk("h7n", n6, 12); hk("h7x", SZ(3, 5, 12), 58)
q8 = solve(Eq(MB(1, q, 6)/MB(1, q, 3), 8), q)[0]
hk("h8q", q8, 2); hk("h8b1", Q(20, 4), 5); hk("h8S", MSU(5, 2, 6), 315)
s9 = solve([Eq(SZ(u, v, 3) + SZ(u, v, 7), 34), Eq(SS(u, v, 10), 200)], [u, v], dict=True)[0]
hk("h9a1", s9[u], -7); hk("h9d", s9[v], 6)
hk("h9-ell", [SZ(-7, 6, 3) + SZ(-7, 6, 7), SS(-7, 6, 10)], [34, 200]) if False else None
hk("h9-ell1", SZ(-7, 6, 3) + SZ(-7, 6, 7), 34); hk("h9-ell2", SS(-7, 6, 10), 200)
hk("h10-30ora", 400*Q(1, 2)**5, Q(25, 2))
hk("h10-kuszob", [m for m in range(1, 12) if 400*Q(1, 2)**m < 10][0], 6)
hk("h10-6ido", 400*Q(1, 2)**6, Q(25, 4))
assert not HE, HE
print("F6h önteszt: OK")

HA = [
 (r"Írd fel az $a_n=\frac{n+4}{2n}$ sorozat első négy tagját!", None,
  r"$\frac{5}{2};\ \frac{3}{2};\ \frac{7}{6};\ 1$"),
 (r"Vizsgáld meg az $a_n=5-\frac{3}{n}$ sorozatot: monoton-e, és korlátos-e? Az állításaidat "
  r"indokold is meg!", None,
  r"$a_{n+1}-a_n=\frac{3}{n(n+1)}\gt 0$, tehát szigorúan növekvő; az első tag $2$ alsó korlát, és "
  r"$a_n\lt 5$ minden $n$-re, mert $\frac{3}{n}\gt 0$ — a sorozat korlátos: $2\le a_n\lt 5$"),
 (r"Egy számtani sorozat első tagja $a_1=-4$, különbsége $d=6$.",
  [r"Számítsd ki $a_{20}$ és $S_{20}$ értékét!",
   r"Ábrázold az első négy tagot, és írd fel annak az egyenesnek az egyenletét, amelyre a pontok "
   r"esnek! Mi köze a meredekségnek a különbséghez?"],
  [r"$a_{20}=110$ és $S_{20}=1060$",
   r"a tagok $-4;\ 2;\ 8;\ 14$, az egyenes $y=6x-10$ — a meredeksége éppen a különbség, $6$"]),
 (r"Egy mértani sorozat első tagja $b_1=-3$, hányadosa $q=2$. Számítsd ki $b_7$ és $S_7$ értékét!",
  None, r"$b_7=-192$ és $S_7=-381$"),
 (r"💰 $120\,000$ dinárt kötsz le $2$ évre, évi $3\%$-os kamatláb mellett. Mennyi lesz a számlán a "
  r"futamidő végén, ha a kamat",
  [r"egyszerű kamatként jár?", r"kamatos kamatként, évente egyszeri jóváírással jár?"],
  [r"$120\,000\cdot 1{,}06=127\,200$ dinár",
   r"$120\,000\cdot 1{,}03^{2}=127\,308{,}00$ dinár"]),
]
HK = [
 (r"Egy számtani sorozat hetedik tagja $a_7=25$, tizenhatodik tagja $a_{16}=61$. Számítsd ki az első "
  r"$16$ tag összegét!", None, r"a különbség $4$, az első tag $1$, és $S_{16}=496$"),
 (r"Oldd meg az egyenletet: $3+8+13+\dots+x=366$!", None, r"$n=12$ tagot adunk össze, és $x=58$"),
 (r"Egy mértani sorozat harmadik tagja $b_3=20$, hatodik tagja $b_6=160$. Írd fel a sorozat első "
  r"négy tagját, és számítsd ki az első hat tag összegét!", None,
  r"$q=2$, $b_1=5$: $5;\ 10;\ 20;\ 40$, és $S_6=315$"),
]
HN = [
 (r"Egy számtani sorozatban $a_3+a_7=34$, az első tíz tag összege pedig $200$. Írd fel a sorozat "
  r"első négy tagját!", None, r"a különbség $6$, az első tag $-7$: $-7;\ -1;\ 5;\ 11$"),
 (r"Egy gyógyszer hatóanyagából a szervezetben maradó mennyiség $6$ óránként a felére csökken. "
  r"Közvetlenül a gyógyszer bevétele után $400$ mg van a szervezetben.",
  [r"Mennyi marad $30$ óra múlva?",
   r"Hányadik hatórás időszak végén csökken a mennyiség $10$ mg alá?"],
  [r"$30$ óra alatt $5$ felezés történik: $400\cdot\left(\frac{1}{2}\right)^{5}=12{,}5$ mg",
   r"a $6.$ időszak végén (vagyis $36$ óra múlva): $6{,}25$ mg"]),
]

body = [
 '    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(HA, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(HK, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(HN, "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="Kristály-kamra", h1="Kristály-kamra — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a sorozatokból — házi feladatnak és a témazáró ellenőrző előtti "
            "bemelegítésnek. Az indukcióból nincs feladat. Számológép használható: a nem egész "
            "eredményeket két tizedesjegyre kerekítsd. A végeredmény minden feladatnál lenyitható!",
      sections_html="\n".join(body),
      prev=FGY, prevc="Sorozatok — feladatok", nxt=C, nxtc="Hiányos és teljes indukció")
print("✓ feladatok-hazi.html | Alap", len(HA), "Közép", len(HK), "Nehéz", len(HN))

# ==================================================================== F5 — témakör-index
from tananyag_common import GYOKER
from fgy_common import w


def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = {
 "A1": kartya(A1, "A sorozat fogalma", "Mi a sorozat, megadás képlettel és rekurzívan, „hányadik tag?”, a pontgrafikon"),
 "A2": kartya(A2, "Monotonitás és korlátosság", "Növekvő, csökkenő, nem monoton; alsó és felső korlát, leolvasás a grafikonról"),
 "B1": kartya(B1, "A számtani sorozat", "Állandó különbség, az n-edik tag, Gauss trükkje és az összegképlet"),
 "B2": kartya(B2, "A mértani sorozat", "Állandó hányados, az n-edik tag, összegképlet — és a kamatos kamat"),
 "C": kartya(C, "Hiányos és teljes indukció", "Mikor sejtés és mikor bizonyítás — olvasnivaló, számonkérés nincs belőle"),
 "fgy": kartya(FGY, "🏋️ Sorozatok — feladatok",
               "Általános tag, monotonitás, korlátosság, számtani és mértani sorozat, kamat — 57 feladat"),
 "hazi": kartya("feladatok-hazi.html", "🕹️ Kristály-kamra — házi feladatok",
                "Rövid, vegyes gyakorlósor az ellenőrző előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 A Végtelen Mutáció",
              "Négyfázisú záróküldetés — kristályrétegek, energiakaszkád, a bank és Maxi hamis képlete"),
 "ossz": kartya("osszefoglalo.html", "📇 Taktikai memóriakártya",
                "A sorozatok képletei, jellemzői és tipikus csapdái egy lapon — ellenőrző előtti átfutáshoz"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(K[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Matematikai indukció. Sorozatok | 3e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="3e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">&#8730;</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">3e</span></a> ›
  <span class="itt">Matematikai indukció. Sorozatok</span>
</nav>
<div class="hero">
  <h1>Matematikai indukció. Sorozatok</h1>
  <p class="alcim">Lépésekhez rendelt számok: a sorozat fogalma, monotonitás és korlátosság, a számtani
  és a mértani sorozat, a kamatos kamat — és a végén az, hogy mit jelent egy állítást tényleg bizonyítani.</p>
  <div class="meta-sor"><span class="chip ora">12 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>♾️ <b>Szektor 06 — A Végtelen Mutáció.</b> Kiképzők: <b>Prizma</b> és
  <b>Kanrak</b>. Maxi bemérve, de amit elindított, nem áll meg magától: a Kristálypára-generátor
  láncreakciója lépésről lépésre nő tovább. Ha ki tudod számolni, hol tart az <i>n</i>-edik lépésnél,
  azt is tudod, hol lehet megállítani. Ez az évad utolsó küldetése.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🔷 A sorozat — Prizma</h3>
''' + racs("A1", "A2") + '''
    <h3>🔶 Számtani és mértani sorozat — Kanrak</h3>
''' + racs("B1", "B2") + '''
    <h3>♾️ Indukció — Prizma és Kanrak</h3>
''' + racs("C") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("fgy", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> a négy sorozat-egység sorban, utána a Kiképzési
    Adattár és a Kristály-kamra — ezekre épül a témazáró ellenőrző. Az indukciós lap ezután jön,
    olvasnivalóként; a Taktikai memóriakártya az ismétlésé, A Végtelen Mutáció pedig a záróküldetés.</p>
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
  renderMathInElement(document.body, {delimiters:[
    {left:'\\\\(', right:'\\\\)', display:false},
    {left:'\\\\[', right:'\\\\]', display:true}
  ]});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
