# -*- coding: utf-8 -*-
"""3e/06 — B blokk: szamtani sorozat (B1), mertani sorozat es kamatos kamat (B2).
Mentor: Kanrak. Kuldetes: A Vegtelen Mutacio."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="3e", mappa="06-indukcio-sorozatok", temakor="Matematikai indukció. Sorozatok")
FGY = "feladatok-sorozatok.html"
KUL = "A Végtelen Mutáció"
KAMAT1E = "../../1e/04-aranyossag/tananyag-kamatszamitas.html"
LIN3E = "../03-linearis-rendszerek/tananyag-ket-ismeretlen.html"
EXP2E = "../../2e/03-exponencialis-es-logaritmus-fuggveny/index.html"

KEK, BORO, ZOLD, PIROS, TINTA, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#0f172a", "#475569"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational, simplify, symbols, solve, Eq, sympify
E = []
def _egyenlo(a, b):
    k = simplify(a - b)
    try:
        return abs(float(k)) < 1e-9
    except TypeError:
        return k == 0


def chk(nev, kapott, vart):
    ok = (len(kapott) == len(vart) and all(_egyenlo(a, b) for a, b in zip(kapott, vart))) \
        if isinstance(kapott, (list, tuple)) else _egyenlo(kapott, vart)
    if not ok:
        E.append((nev, kapott, vart))

n, x = symbols("n x", positive=True)
SZ = lambda a1, d, k: a1 + (k - 1)*d
SS = lambda a1, d, k: sympify(k)/2*(2*a1 + (k - 1)*d)
# B1 — retegek: a1 = 6, d = 4
chk("B1-a25", SZ(6, 4, 25), 102)
chk("B1-S25", SS(6, 4, 25), 1350)
chk("B1-S25-masik", Rational(25*(6 + 102), 2), 1350)
chk("B1-gauss-tagok", [SZ(6, 4, k) for k in range(1, 7)], [6, 10, 14, 18, 22, 26])
chk("B1-gauss-par", 6 + 26, 32)
chk("B1-gauss-S6", SS(6, 4, 6), 96)
# B1 — ket tagbol
d_ = Rational(39 - 11, 7); a1_ = 11 - 3*d_
chk("B1-d", d_, 4); chk("B1-a1", a1_, -1); chk("B1-S20", SS(a1_, d_, 20), 740)
chk("B1-a4", SZ(a1_, d_, 4), 11); chk("B1-a11", SZ(a1_, d_, 11), 39)
# B1 — egyenlet: 3 + 7 + 11 + ... + x = 210
meg = [s for s in solve(Eq(SS(3, 4, n), 210), n) if s.is_positive]
chk("B1-egyenlet-n", meg, [10]); chk("B1-egyenlet-x", SZ(3, 4, 10), 39)
chk("B1-egyenlet-D", 1 + 4*2*210, 41**2)
# B1 — Maxi-doboz adatai (a kidolgozott peldatol kulonbozo szamok)
chk("B1-maxi-d", Rational(32 - 8, 9 - 3), 4)
chk("B1-maxi-a3", SZ(8 - 2*4, 4, 3), 8); chk("B1-maxi-a9", SZ(8 - 2*4, 4, 9), 32)
# B1 — szeksorok
chk("B1-szek", SS(18, 3, 14), 525)
chk("B1-kviz-tagszam", solve(Eq(SZ(2, 3, n), 29), n), [10])
chk("B1-kviz-osszeg", SS(2, 3, 10), 155)
# B2 — mertani
MB = lambda b1, q, k: b1*q**(k - 1)
MS = lambda b1, q, k: b1*(q**k - 1)/(q - 1)
chk("B2-b10", MB(3, 2, 10), 1536)
chk("B2-S10", MS(3, 2, 10), 3069)
chk("B2-kuszob", [k for k in range(1, 20) if MS(3, 2, k) > 5000][0], 11)
chk("B2-S11", MS(3, 2, 11), 6141)
chk("B2-ket-tagbol-q", solve(Eq(MB(1, x, 5)/MB(1, x, 2), 8), x), [2])
chk("B2-ket-tagbol-b1", Rational(12, 2), 6)
chk("B2-b5", MB(6, 2, 5), 96)
chk("B2-kozep", MB(6, 2, 3)**2 - MB(6, 2, 2)*MB(6, 2, 4), 0)
chk("B2-valto", [MB(4, Rational(-1, 2), k) for k in range(1, 5)], [4, -2, 1, Rational(-1, 2)])
# B2 — kamat (200 000 din, 6%, 5 ev)
K0, p, ev = 200000, Rational(6, 100), 5
egyszeru = K0*(1 + p*ev)
kamatos = K0*(1 + p)**ev
negyed = K0*(1 + p/4)**(4*ev)
chk("B2-egyszeru", egyszeru, 260000)
chk("B2-kamatos-ker", round(float(kamatos), 2), 267645.12)
chk("B2-negyed-ker", round(float(negyed), 2), 269371.00)
chk("B2-maxi", round(float((Rational(11, 10)**20 - 1)*100), 1), 572.7)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_EGYENESEN = svg_fuggvenyek(
    [(lambda u: (4*u + 2)/10, KEK, "y = 4x + 2", [(0, 7.4)])],
    xr=(0, 7.6), yr=(0, 3.4), w=390, h=250, egyseg=("1", "10"), tengely=("n", "aₙ"),
    leiras="A 6, 10, 14, … számtani sorozat pontjai mind egy egyenesre esnek",
    pontok=[(k, (4*k + 2)/10, "", ZOLD) for k in range(1, 8)])
SVG_MERTANI = svg_fuggvenyek(
    [(lambda u: 0.3*2**u, BORO, "y = 1,5 · 2ˣ", [(0.2, 5.3)])],
    xr=(0, 5.8), yr=(0, 11), w=390, h=250, egyseg=("1", "5"), tengely=("n", "bₙ"),
    jelmagyarazat=False,
    leiras="A 3, 6, 12, 24, 48 mértani sorozat pontjai egy exponenciális görbére esnek",
    pontok=[(k, 3*2**(k - 1)/5, str(3*2**(k - 1)), ZOLD, (-24 if k == 5 else -6), -10)
            for k in range(1, 6)])
SVG_KAMAT = svg_fuggvenyek(
    [(lambda u: 2 + 0.12*u, KEK, "egyszerű kamat", [(0, 10.2)]),
     (lambda u: 2*1.06**u, BORO, "kamatos kamat", [(0, 10.2)])],
    xr=(0, 10.8), yr=(0, 5), w=400, h=260, egyseg=("1 év", "100 000"), tengely=("év", "dinár"),
    leiras="200 000 dinár 10 éven át, évi 6%-kal: az egyszerű kamat egyenes vonal mentén, "
           "a kamatos kamat egyre meredekebben nő",
    pontok=[(10, 3.2, "320 000", KEK, -70, 18), (10, 2*1.06**10, "358 170", BORO, -70, -10)])


def svg_gauss():
    """Gauss-parositas: a 6, 10, 14, 18, 22, 26 sorozat ket sorban, oszloponkent 32."""
    tag = [6, 10, 14, 18, 22, 26]
    x0, dx, y1, y2 = 46, 62, 42, 86
    ki = ['<svg viewBox="0 0 440 150" width="440" height="150" role="img" '
          'aria-label="A 6, 10, 14, 18, 22, 26 sorozat egyszer előrefelé, egyszer visszafelé '
          'felírva; minden oszlopban a két szám összege 32">',
          f'  <text x="8" y="{y1 + 4}" font-size="12" fill="{SZURKE}">S₆ =</text>',
          f'  <text x="8" y="{y2 + 4}" font-size="12" fill="{SZURKE}">S₆ =</text>']
    for i, t in enumerate(tag):
        cx = x0 + i*dx
        ki.append(f'  <text x="{cx}" y="{y1 + 4}" font-size="14" fill="{TINTA}" '
                  f'text-anchor="middle" font-weight="600">{t}</text>')
        ki.append(f'  <text x="{cx}" y="{y2 + 4}" font-size="14" fill="{TINTA}" '
                  f'text-anchor="middle" font-weight="600">{tag[-1 - i]}</text>')
        ki.append(f'  <line x1="{cx}" y1="{y1 + 10}" x2="{cx}" y2="{y2 - 12}" '
                  f'stroke="{KEK}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        ki.append(f'  <text x="{cx}" y="{y2 + 28}" font-size="12" fill="{KEK}" '
                  f'text-anchor="middle">32</text>')
        if i < len(tag) - 1:
            ki.append(f'  <text x="{cx + dx/2:.0f}" y="{y1 + 4}" font-size="12" '
                      f'fill="{SZURKE}" text-anchor="middle">+</text>')
            ki.append(f'  <text x="{cx + dx/2:.0f}" y="{y2 + 4}" font-size="12" '
                      f'fill="{SZURKE}" text-anchor="middle">+</text>')
    ki.append(f'  <line x1="20" y1="{y2 + 40}" x2="420" y2="{y2 + 40}" stroke="{SZURKE}" '
              f'stroke-width="1"/>')
    ki.append(f'  <text x="220" y="{y2 + 58}" font-size="13" fill="{TINTA}" text-anchor="middle">'
              f'2 · S₆ = 6 · 32 = 192,  tehát  S₆ = 96</text>')
    ki.append(f'  <text x="220" y="16" font-size="12" fill="{SZURKE}" text-anchor="middle">'
              f'ugyanaz az összeg kétszer: egyszer előrefelé, egyszer visszafelé</text>')
    ki.append('</svg>')
    return "\n".join(ki)


SVG_GAUSS = svg_gauss()

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> A mutáció első fázisában a generátor <b>ugyanannyit</b> tesz hozzá minden '
         'lépésben. Ez a legszelídebb forgatókönyv — és a legjobban számolható: nem kell '
         'végigkövetnünk száz lépést, egyetlen képlet megmondja a századik réteg vastagságát és '
         'azt is, mennyi anyag épült be összesen.'),
 ]),

 ("Az állandó különbség", [
   r'<p class="lead">Nézd meg a naplót: $6,\ 10,\ 14,\ 18,\ 22,\dots$ — minden lépésben pontosan '
   r'$4$-gyel nő. Ez az állandó „adag” a sorozat különbsége.</p>',
   doboz("definicio", "A számtani sorozat",
         r'<p>Az $(a_n)$ sorozat <b>számtani</b> (aritmetikai), ha bármely tagjából ugyanannak a '
         r'$d$ számnak a hozzáadásával kapjuk a következőt:</p>'
         r'$$a_{n+1}=a_n+d,\qquad\text{azaz}\qquad d=a_{n+1}-a_n .$$'
         r'<p>A $d$ szám a sorozat <b>különbsége</b> (differenciája). Ha $d\gt0$, a sorozat növekvő, '
         r'ha $d\lt0$, csökkenő, ha $d=0$, állandó.</p>', hid="def-szamtani"),
   r'<p>Ellenőrizni könnyű: kivonjuk egymásból a szomszédos tagokat, és megnézzük, mindig ugyanazt '
   r'kapjuk-e. A $2,\ 6,\ 18,\ 54,\dots$ sorozatnál a különbségek $4,\ 12,\ 36$ — <b>nem</b> '
   r'számtani (ott nem hozzáadunk, hanem szorzunk; ez lesz a következő egység témája).</p>',
 ]),

 ("Az n-edik tag", [
   r'<p>Az első tagtól az $n$-edikig <b>$n-1$ lépést</b> teszünk meg, és minden lépésben $d$-t adunk '
   r'hozzá. Innen a képlet:</p>',
   doboz("tetel", "A számtani sorozat n-edik tagja",
         r'$$a_n=a_1+(n-1)d$$'
         r'<p>Az $a_1$ és a $d$ ismeretében tehát a sorozat <b>bármely</b> tagja egy lépésben '
         r'megkapható. Két tetszőleges tag között ugyanez a gondolat: annyiszor lépünk, ahány a '
         r'sorszámok különbsége — $a_m=a_k+(m-k)d$.</p>',
         hid="tetel-szamtani-an"),
   abra(SVG_EGYENESEN, 'A $6,\\ 10,\\ 14,\\dots$ sorozat pontjai mind az $y=4x+2$ egyenesre esnek: a '
        'számtani sorozat „lineáris” növekedés, a meredekség éppen a $d$. A függőleges tengely egy '
        'osztása $10$ egység.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a 10. réteget így számolja: $a_{10}=a_1+10d$.</p>'
         r'<p>Ez egy lépéssel több a kelleténél. Az első tagnál még <b>nulla</b> lépést tettünk meg, '
         r'a másodiknál egyet, a tizediknél kilencet — ezért $a_{10}=a_1+9d$. A képletben azért áll '
         r'$(n-1)$, mert a <b>lépések száma</b> mindig eggyel kevesebb, mint a tagok száma.</p>'
         r'<p>Ugyanez a hiba bújik meg abban is, amikor valaki két tagból így keresi a különbséget: '
         r'$a_3=8$, $a_9=32$, tehát „$d=\frac{32-8}{9}$”. A helyes osztó a <b>lépések száma</b>, '
         r'$9-3=6$: $d=\frac{24}{6}=4$.</p>'),
   kviz(r'Egy számtani sorozat első tagja $a_1=7$, különbsége $d=5$. Mennyi $a_{12}$?',
        [r'$62$', r'$67$', r'$60$', r'$72$'], 0,
        jo="✔ a₁₂ = 7 + 11 · 5 = 62 — a 12. tagig 11 lépést teszünk meg.",
        nem="✘ A 12. tagig nem 12, hanem 11 lépés vezet: a₁₂ = a₁ + 11d = 7 + 55 = 62."),
 ]),

 ("Az első n tag összege", [
   r'<p>A generátornak nemcsak az egyes rétegek vastagsága érdekes, hanem az is, hogy <b>összesen</b> '
   r'mennyi anyag épült be. Írjuk fel az összeget kétszer: egyszer előrefelé, egyszer visszafelé.</p>',
   abra(SVG_GAUSS, 'A párok összege mindig ugyanannyi: $a_1+a_6=6+26=32$. Hat ilyen párunk van, de '
        'közben az összeget kétszer írtuk fel — ezért osztunk kettővel.'),
   doboz("tetel", "Az első n tag összege",
         r'$$S_n=\frac{n\,(a_1+a_n)}{2}=\frac{n}{2}\bigl(2a_1+(n-1)d\bigr)$$'
         r'<p>Az <b>első alakot</b> akkor használjuk, ha ismerjük az utolsó tagot is; a '
         r'<b>másodikat</b> akkor, ha csak az $a_1$ és a $d$ adott. A kettő ugyanaz: az '
         r'$a_n=a_1+(n-1)d$ behelyettesítésével egymásba mennek át.</p>',
         hid="tetel-szamtani-sn"),
   doboz("erdekesseg", "A kilencéves Gauss",
         r'<p>A történet szerint a tanító azzal akarta lefoglalni az osztályt, hogy adja össze az '
         r'$1$-től $100$-ig terjedő számokat. Carl Friedrich Gauss percek alatt végzett: észrevette, '
         r'hogy $1+100=101$, $2+99=101$, és így tovább — ötven ilyen pár van, tehát az összeg '
         r'$50\cdot101=5050$. Pontosan ezt a párosítást általánosítja a fenti képlet.</p>',
         hid="erd-gauss"),
   doboz("pelda", "Kristály-kamra szimuláció — a beépült anyag",
         r'<p>A rétegek vastagsága számtani sorozatot alkot: $a_1=6$, $d=4$. Mekkora a 25. réteg, és '
         r'mennyi anyag épült be az első 25 lépésben?</p>'
         r'<p>A 25. réteg: $a_{25}=6+24\cdot4=102$.</p>'
         r'<p>Az összeg az első alakkal: $S_{25}=\dfrac{25\,(6+102)}{2}=\dfrac{25\cdot108}{2}=1350$.</p>'
         r'<p>Ellenőrzésképp a második alakkal: '
         r'$S_{25}=\dfrac{25}{2}\bigl(12+24\cdot4\bigr)=\dfrac{25\cdot108}{2}=1350$ ✔</p>',
         hid="pelda-retegek"),
   kviz(r'Hány tagot adunk össze a $2+5+8+\dots+29$ összegben?',
        [r'$10$-et', r'$29$-et', r'$9$-et', r'$28$-at'], 0,
        jo="✔ Itt a₁ = 2, d = 3, és 3n − 1 = 29 miatt n = 10. (Az összeg 155.)",
        nem="✘ Az összegképletben az n a TAGOK SZÁMA, nem az utolsó tag értéke. Az aₙ = 2 + (n − 1)·3 = 29 "
            "egyenletből n = 10 adódik."),
 ]),

 ("Két adatból az egész sorozat", [
   r'<p>A számtani sorozatot <b>két adat</b> meghatározza: az $a_1$ és a $d$. Ha más két adatot '
   r'ismerünk, egyenletrendszert írunk fel rájuk — pontosan úgy, ahogy a '
   r'<a href="' + LIN3E + r'">lineáris egyenletrendszereknél</a> tanultuk.</p>',
   doboz("pelda", "Két megadott tagból",
         r'<p>Egy számtani sorozat negyedik tagja $a_4=11$, tizenegyedik tagja $a_{11}=39$. '
         r'Mennyi az első húsz tag összege?</p>'
         r'<p>A két adat két egyenlet:</p>'
         r'$$a_1+3d=11,\qquad a_1+10d=39 .$$'
         r'<p>Kivonva az elsőt a másodikból: $7d=28$, tehát $d=4$, és innen $a_1=11-12=-1$.</p>'
         r'<p>Az összeghez még kell $a_{20}=-1+19\cdot4=75$, majd</p>'
         r'$$S_{20}=\frac{20\,(-1+75)}{2}=10\cdot74=740 .$$', hid="pelda-ket-tagbol"),
   doboz("pelda", "Meddig tart az összeadás?",
         r'<p>Oldjuk meg az egyenletet: $3+7+11+\dots+x=210$.</p>'
         r'<p>A bal oldal számtani sorozat összege $a_1=3$, $d=4$ mellett. Az $n$ tagszám még '
         r'ismeretlen:</p>'
         r'$$\frac{n}{2}\bigl(6+(n-1)\cdot4\bigr)=210\ \Longrightarrow\ n(2n+1)=210 .$$'
         r'<p>A $2n^2+n-210=0$ egyenlet diszkriminánsa $D=1+1680=1681=41^2$, a megoldásai '
         r'$n=\frac{-1+41}{4}=10$ és $n=-\frac{21}{2}$. A tagszám csak természetes szám lehet, '
         r'tehát $n=10$, és $x=a_{10}=3+9\cdot4=39$.</p>'),
 ]),

 ("Számtani közép és valós helyzetek", [
   doboz("tetel", "A számtani közép",
         r'<p>A számtani sorozat minden tagja (az elsőt kivéve) a két szomszédja <b>számtani '
         r'közepe</b>:</p>'
         r'$$a_n=\frac{a_{n-1}+a_{n+1}}{2}\qquad (n\ge2).$$'
         r'<p>Ezért ha három szám számtani sorozatot alkot, a középső a másik kettő átlaga — ez sok '
         r'feladatban rövidíti le a számolást.</p>', hid="tetel-szamtani-kozep"),
   doboz("pelda", "A nézőtér",
         r'<p>Egy nézőtér első sorában $18$ hely van, és minden további sorban $3$-mal több, mint az '
         r'előzőben. Hány hely van $14$ sorban?</p>'
         r'<p>A sorok férőhelyei számtani sorozatot alkotnak: $a_1=18$, $d=3$, $n=14$. '
         r'Az utolsó sor: $a_{14}=18+13\cdot3=57$, az összes hely:</p>'
         r'$$S_{14}=\frac{14\,(18+57)}{2}=7\cdot75=525 .$$'
         r'<p>A válasz tehát <b>525 hely</b>. Vegyük észre, hogy a szöveget először le kellett '
         r'fordítanunk a sorozat nyelvére ($a_1$, $d$, $n$), a végén pedig vissza.</p>',
         hid="pelda-szeksorok"),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Számtani sorozat az egyenlő <b>tőkerészletekben</b> törlesztett kölcsön fennálló '
         r'tartozása, a fix '
         r'alapdíj + óradíj szerinti számla, az egyenletesen gyorsuló mozgás másodpercenként megtett '
         r'útja, és a raktárban minden nap ugyanannyival csökkenő készlet.</p>'),
   GY(FGY + "#alap-13", "A 13–20", FGY + "#kozep-9", "K 9–14"),
   brief('<b>Kanrak:</b> A generátor átkapcsolt. A műszerek szerint a következő fázisban már nem '
         'hozzáad, hanem <b>szoroz</b>: minden lépés az előző állapot többszöröse. Ez az a pont, '
         'ahol a láncreakció veszélyessé válik — és ahol a bank is dolgozik.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Nézd a különbséget: az előbb minden lépés ugyanannyit tett hozzá, most '
         'minden lépés <b>ugyanazzal a számmal szorozza</b> az energiát. Ez dönti el, hogy egy hét '
         'múlva vagy egy órán belül éri el a kritikus szintet. Ugyanez a matematika működik a '
         'bankban is, amikor a kamat a kamatra rakódik.'),
 ]),

 ("Az állandó hányados és az n-edik tag", [
   r'<p class="lead">A napló új szakasza: $3,\ 6,\ 12,\ 24,\ 48,\dots$ — minden tag az előző '
   r'<b>kétszerese</b>. A különbségek ($3, 6, 12, \dots$) nem állandók, a hányadosok ($2, 2, 2,\dots$) '
   r'viszont igen.</p>',
   doboz("definicio", "A mértani sorozat",
         r'<p>A $(b_n)$ sorozat <b>mértani</b> (geometriai), ha bármely tagját ugyanazzal a $q\ne0$ '
         r'számmal szorozva kapjuk a következőt:</p>'
         r'$$b_{n+1}=b_n\cdot q,\qquad\text{azaz}\qquad q=\frac{b_{n+1}}{b_n}\quad (b_n\ne0).$$'
         r'<p>A $q$ szám a sorozat <b>hányadosa</b> (kvóciense). Megköveteljük, hogy $b_1\ne0$ és '
         r'$q\ne0$ legyen — különben csupa nulla tagot kapnánk, és a hányados sem volna '
         r'értelmezhető.</p>', hid="def-mertani"),
   doboz("tetel", "A mértani sorozat n-edik tagja",
         r'<p>Az első tagtól az $n$-edikig $n-1$ szorzás vezet, ezért</p>'
         r'$$b_n=b_1\cdot q^{\,n-1} .$$'
         r'<p>Két tetszőleges tag között ugyanígy: $b_m=b_k\cdot q^{\,m-k}$.</p>',
         hid="tetel-mertani-bn"),
   r'<p>Az alábbi táblázat <b>pozitív első tag</b> ($b_1\gt0$) esetére érvényes; negatív első '
   r'tagnál minden tag előjelet vált, és a növekvő–csökkenő szerep megfordul.</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>a hányados</th><th>a sorozat</th><th>példa</th></tr>'
   r'<tr><td>$q\gt1$</td><td>növekvő</td><td>$3,\ 6,\ 12,\ 24,\dots$</td></tr>'
   r'<tr><td>$0\lt q\lt1$</td><td>csökkenő, de pozitív marad</td><td>$80,\ 40,\ 20,\ 10,\dots$</td></tr>'
   r'<tr><td>$q\lt0$</td><td>váltakozó előjelű</td><td>$4,\ -2,\ 1,\ -\frac12,\dots$</td></tr>'
   r'<tr><td>$q=1$</td><td>állandó</td><td>$5,\ 5,\ 5,\dots$</td></tr>'
   r'</table></div>',
   abra(SVG_MERTANI, 'A $3,\\ 6,\\ 12,\\ 24,\\ 48$ sorozat pontjai egy exponenciális görbére ülnek — '
        'ahogy a számtani sorozat pontjai egyenesre. A függőleges tengely egy osztása $5$ egység.'),
   doboz("erdekesseg", "Ismerős görbe",
         r'<p>A pontok az <a href="' + EXP2E + r'">exponenciális függvény</a> grafikonjára esnek: a '
         r'$b_n=3\cdot2^{\,n-1}$ sorozat ugyanaz, mint az $y=1{,}5\cdot2^{x}$ függvény értékei a '
         r'pozitív egész $x=n$ helyeken. Ezért nő a mértani sorozat olyan gyorsan: a kitevőben van '
         r'az $n$.</p>'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi két hibát is elkövet, és mindkettő ugyanoda vezet: túl nagy vagy rossz előjelű '
         r'energiát jelent.</p>'
         r'<p><b>1.</b> $b_{10}=b_1\cdot q^{10}$ — egy szorzással több a kelleténél. Helyesen a '
         r'kitevő $n-1=9$.</p>'
         r'<p><b>2.</b> A $(-2)^n$ és a $-2^n$ összekeverése. A $(-2)^4=16$, de $-2^4=-16$: a '
         r'zárójel nélküli alakban a hatványozás megelőzi az előjelet. Váltakozó előjelű sorozatnál '
         r'ezért mindig zárójelbe tesszük a negatív hányadost.</p>'),
   kviz(r'Egy mértani sorozat első tagja $b_1=5$, hányadosa $q=-2$. Mennyi $b_4$?',
        [r'$-40$', r'$40$', r'$-80$', r'$80$'], 0,
        jo="✔ b₄ = 5 · (−2)³ = 5 · (−8) = −40: három szorzás, és a páratlan kitevő miatt negatív.",
        nem="✘ b₄ = b₁ · q³ = 5 · (−2)³. A kitevő 3 (nem 4), és a (−2)³ = −8, tehát b₄ = −40."),
 ]),

 ("Az első n tag összege", [
   r'<p>Az összeghez most is trükk kell, csak más: írjuk fel $S_n$-t, szorozzuk meg $q$-val, és '
   r'vonjuk ki a kettőt egymásból — a középső tagok kiesnek:</p>'
   r'$$S_n=b_1+b_1q+\dots+b_1q^{\,n-1},\qquad q\,S_n=b_1q+\dots+b_1q^{\,n-1}+b_1q^{\,n} .$$'
   r'<p>A különbség $q\,S_n-S_n=b_1q^{\,n}-b_1$, azaz $S_n(q-1)=b_1(q^{\,n}-1)$.</p>',
   doboz("tetel", "Az első n tag összege",
         r'$$S_n=b_1\cdot\frac{q^{\,n}-1}{q-1}\qquad (q\ne1)$$'
         r'<p>A $q=1$ eset külön megy: akkor minden tag ugyanaz, tehát $S_n=n\cdot b_1$. '
         r'(A képletben ilyenkor nullával osztanánk — ezért a kikötés.)</p>',
         hid="tetel-mertani-sn"),
   doboz("pelda", "Kristály-kamra szimuláció — a láncreakció",
         r'<p>A láncreakció energiája mértani sorozat: $b_1=3$, $q=2$. Mekkora a 10. lépés energiája, '
         r'mennyi az első 10 lépés összenergiája, és hányadik lépésnél lépi át az összenergia az '
         r'$5000$ egységet?</p>'
         r'<p>A 10. lépés: $b_{10}=3\cdot2^{9}=3\cdot512=1536$.</p>'
         r'<p>Az összeg: $S_{10}=3\cdot\dfrac{2^{10}-1}{2-1}=3\cdot1023=3069$.</p>'
         r'<p>A küszöb: $S_{11}=3\cdot(2^{11}-1)=3\cdot2047=6141\gt5000$, míg $S_{10}=3069\lt5000$ — '
         r'tehát a <b>11. lépésnél</b> lépi át. Ez a mértani növekedés lényege: a 9. lépésnél még '
         r'csak $S_9=1533$-nál tartott — az 5000 harmadánál sem.</p>', hid="pelda-lancreakcio"),
   doboz("erdekesseg", "A rizsszemek a sakktáblán",
         r'<p>A legenda szerint a sakk feltalálója annyi rizsszemet kért jutalmul, hogy az első '
         r'mezőre egy szem kerüljön, a másodikra kettő, a harmadikra négy, és így tovább. A hatvannégy '
         r'mezőn $S_{64}=2^{64}-1$ szem lenne — több, mint a világ mai rizstermésének több száz '
         r'évnyi mennyisége. '
         r'A király a számtani sorozatra gondolt, a feltaláló a mértanira.</p>',
         hid="erd-sakktabla"),
 ]),

 ("Adatokból a sorozat", [
   doboz("tetel", "A középső tag",
         r'<p>A mértani sorozat minden tagjának négyzete a két szomszédja szorzata:</p>'
         r'$$b_n^{\,2}=b_{n-1}\cdot b_{n+1}\qquad (n\ge2).$$'
         r'<p>Ezért ha három szám mértani sorozatot alkot, a középső négyzete a két szélső szorzata. '
         r'(A <i>mértani közép</i> maga $\sqrt{b_{n-1}b_{n+1}}=\lvert b_n\rvert$ — a középső tag '
         r'ugyanis negatív is lehet.)</p>', hid="tetel-mertani-kozep"),
   doboz("pelda", "Két megadott tagból",
         r'<p>Egy mértani sorozat második tagja $b_2=12$, ötödik tagja $b_5=96$. Határozzuk meg a '
         r'sorozatot!</p>'
         r'<p>A két tag között három szorzás van, ezért</p>'
         r'$$\frac{b_5}{b_2}=q^{3}=\frac{96}{12}=8\ \Longrightarrow\ q=2 .$$'
         r'<p>Innen $b_1=\dfrac{b_2}{q}=6$, a sorozat pedig $6,\ 12,\ 24,\ 48,\ 96,\dots$</p>'
         r'<p><i>Vigyázzunk a gyökvonásnál:</i> ha <b>páros</b> kitevőjű hatvány adódik (például '
         r'$q^2=9$), akkor <b>két</b> megoldás van, $q=3$ és $q=-3$ — ilyenkor mindkettőt végig kell '
         r'gondolni, és a feladat szövege dönt (például „növekvő sorozat”).</p>',
         hid="pelda-ket-tagbol-mertani"),
   kviz(r'Egy mértani sorozatban $b_2=5$ és $b_6=80$. Mennyi a hányados (ha pozitív)?',
        [r'$2$', r'$4$', r'$16$', r'$\frac{75}{4}$'], 0,
        jo="✔ b₆ / b₂ = q⁴ = 16, tehát q = 2 (a negatív gyök, −2, akkor jönne szóba, ha a feladat "
           "megengedné).",
        nem="✘ A két tag között NÉGY szorzás van, tehát q⁴ = 80/5 = 16, ebből q = 2. "
            "A hányadost nem osztással kapjuk a sorszámok különbségéből."),
 ]),

 ("Kamat: egyszerű és kamatos", [
   r'<p>A két sorozat különbsége a pénzügyekben a legszemléletesebb. Az '
   r'<a href="' + KAMAT1E + r'#s1">egyszerű kamat</a> mindig a kezdő tőkére jár: minden évben '
   r'ugyanakkora összeggel nő a számla — ez <b>számtani</b> sorozat. A <b>kamatos kamat</b> esetén a '
   r'kamat is kamatozik tovább: minden évben ugyanazzal a szorzóval nő a számla — ez '
   r'<b>mértani</b> sorozat.</p>',
   doboz("tetel", "A kamatos kamat képlete",
         r'<p>Ha a kezdő tőke $K_0$, az éves kamatláb $p\%$, és a kamatot évente egyszer írják jóvá, '
         r'akkor $n$ év múlva</p>'
         r'$$K_n=K_0\left(1+\frac{p}{100}\right)^{n} .$$'
         r'<p>Ha évente $t$-szer írnak jóvá kamatot (negyedévente $t=4$, havonta $t=12$), akkor egy '
         r'jóváírásnál a kamatláb $\frac{p}{t}$ százalék, a jóváírások száma pedig $t\cdot n$:</p>'
         r'$$K_n=K_0\left(1+\frac{p}{100\,t}\right)^{t\,n} .$$'
         r'<p>Az egyszerű kamat ugyanezekkel a jelölésekkel $K_n=K_0\left(1+\frac{p}{100}n\right)$.</p>'
         r'<p><b>Miért $n$ a kitevő, és nem $n-1$?</b> Mert a kiinduló összeg a <b>nulladik</b> év '
         r'adata, $K_0$ — a mértani sorozat nyelvén ez az első tag, $b_1=K_0$, tehát $K_n=b_{n+1}$. '
         r'Ha a számlálást $K_0$-tól kezdjük, a kitevő éppen az eltelt évek száma.</p>',
         hid="tetel-kamatos-kamat"),
   doboz("pelda", "Kristálypára-bank — három szám egymás mellett",
         r'<p>$200\,000$ dinárt helyezünk el $5$ évre, évi $6\%$-os kamatláb mellett. Mennyi lesz a '
         r'számlán, ha a kamatot <b>a)</b> egyszerű kamatként, <b>b)</b> évente egyszer, '
         r'<b>c)</b> negyedévente írják jóvá? (Kerekítsünk két tizedesjegyre!)</p>'
         r'<p><b>a)</b> $200\,000\left(1+0{,}06\cdot5\right)=200\,000\cdot1{,}3=260\,000$ dinár.</p>'
         r'<p><b>b)</b> $200\,000\cdot1{,}06^{5}=267\,645{,}12$ dinár.</p>'
         r'<p><b>c)</b> Negyedévente $\frac{6}{4}=1{,}5\%$, összesen $20$ jóváírás: '
         r'$200\,000\cdot1{,}015^{20}=269\,371{,}00$ dinár.</p>'
         r'<p>Ugyanaz a kamatláb, három különböző végösszeg — a különbség abból jön, hogy a kamat '
         r'mikortól kezd maga is kamatozni.</p>', hid="pelda-kamat"),
   abra(SVG_KAMAT, '$200\\,000$ dinár $10$ éven át, évi $6\\%$-kal. Az egyszerű kamat egyenes mentén '
        'nő, a kamatos kamat egyre meredekebben. A függőleges tengely egy osztása $100\\,000$ dinár.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi fejben számol: „$20$ év, évi $10\%$ — az összesen $200\%$, vagyis a pénzem '
         r'háromszorosa”.</p>'
         r'<p>Ez az <b>egyszerű</b> kamat esete. Kamatos kamatnál a szorzók szorzódnak: '
         r'$1{,}1^{20}\approx6{,}7275$, tehát a tőke nem háromszorosára, hanem közel '
         r'<b>hétszeresére</b> nő — a kamat $572{,}7\%$. Minél hosszabb a futamidő, annál nagyobb a '
         r'különbség; hitelnél ugyanez a mechanizmus dolgozik az adós ellen.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Kamatos kamat szerint nő a megtakarítás és a hiteltartozás, és ugyanígy — csak lefelé — '
         r'működik az infláció (a pénz értéke évente ugyanazzal a szorzóval csökken) meg a gyógyszer '
         r'kiürülése a szervezetből (felezési idő: $q=\frac12$).</p>'),
   kviz(r'Évi $6\%$ kamat, <b>havi</b> jóváírás, $5$ év. Melyik számolás helyes?',
        [r'$K_0\left(1+\frac{0{,}06}{12}\right)^{60}$', r'$K_0\left(1+0{,}06\right)^{60}$',
         r'$K_0\left(1+0{,}06\right)^{12}$', r'$K_0\left(1+\frac{0{,}06}{12}\right)^{5}$'], 0,
        jo="✔ Egy hónapra 6/12 = 0,5% jár, és 5 év alatt 60 jóváírás történik.",
        nem="✘ A gyakoribb jóváírás nem az éves kamatlábat hatványozza többször: egy időszakra "
            "a kamatláb p/t (itt 0,06/12), a kitevő pedig a jóváírások száma (itt 12 · 5 = 60)."),
 ]),

 ("🧾 Gyorsismétlő", [
   r'<p>A két sorozat egymás mellett — ennyi kell az ellenőrzőhöz.</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th></th><th>számtani</th><th>mértani</th></tr>'
   r'<tr><td>a szabály</td><td>$a_{n+1}=a_n+d$</td><td>$b_{n+1}=b_n\cdot q$</td></tr>'
   r'<tr><td>a jellemző adat</td><td>$d=a_{n+1}-a_n$</td><td>$q=\frac{b_{n+1}}{b_n}$</td></tr>'
   r'<tr><td>az $n$-edik tag</td><td>$a_n=a_1+(n-1)d$</td><td>$b_n=b_1q^{\,n-1}$</td></tr>'
   r'<tr><td>az első $n$ tag összege</td><td>$S_n=\frac{n(a_1+a_n)}{2}=\frac n2\bigl(2a_1+(n-1)d\bigr)$</td>'
   r'<td>$S_n=b_1\frac{q^{\,n}-1}{q-1}$ ($q\ne1$)</td></tr>'
   r'<tr><td>a középső tag ($n\ge2$)</td><td>$a_n=\frac{a_{n-1}+a_{n+1}}{2}$</td>'
   r'<td>$b_n^{\,2}=b_{n-1}b_{n+1}$</td></tr>'
   r'<tr><td>a grafikon</td><td>pontok egy <b>egyenesen</b></td>'
   r'<td>pontok egy <b>exponenciális</b> görbén</td></tr>'
   r'</table></div>'
   r'<p><b>Melyik melyik?</b> Vond ki egymásból a szomszédos tagokat: ha mindig ugyanazt kapod, '
   r'számtani. Oszd el egymással a szomszédos tagokat: ha mindig ugyanazt kapod, mértani. '
   r'A $2,\ 4,\ 8$ például mértani ($q=2$), a $2,\ 4,\ 6$ pedig számtani ($d=2$).</p>'
   r'<p><b>És a leggyakoribb hiba mindkettőnél ugyanaz:</b> a kitevőben, illetve a szorzóban '
   r'$n$ helyett $n-1$ áll, mert az első tagtól az $n$-edikig csak $n-1$ lépés vezet.</p>',
   GY(FGY + "#alap-21", "A 21–28", FGY + "#kozep-15", "K 15–20"),
   brief('<b>Kanrak:</b> A képletek megvannak, a küszöb kiszámolva. Előbb éles helyzetben is '
         'használd őket — a Kiképzési Adattár és a Kristály-kamra vár —, aztán jön a nehezebb '
         'kérdés: honnan tudjuk, hogy ezek a képletek <b>minden</b> $n$-re igazak, nem csak az első '
         'néhány lépésre?', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-szamtani-sorozat.html",
     cim="A számtani sorozat",
     alcim="Az állandó különbség, az n-edik tag, az első n tag összege Gauss trükkjével, és a "
           "sorozat felírása két adatból.",
     chip=KUL + " · 3/5", szakaszok=B1,
     elozo=("tananyag-monotonitas-es-korlatossag.html", "Monotonitás és korlátosság"),
     kovetkezo=("tananyag-mertani-sorozat.html", "A mértani sorozat és a kamatos kamat")),
 lap(**T, fajl="tananyag-mertani-sorozat.html",
     cim="A mértani sorozat és a kamatos kamat",
     cim_tiszta="A mértani sorozat",
     alcim="Az állandó hányados, az n-edik tag, az összegképlet, a sorozat felírása adatokból, "
           "valamint az egyszerű és a kamatos kamat.",
     chip=KUL + " · 4/5", szakaszok=B2,
     elozo=("tananyag-szamtani-sorozat.html", "A számtani sorozat"),
     kovetkezo=(FGY, "Sorozatok — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
