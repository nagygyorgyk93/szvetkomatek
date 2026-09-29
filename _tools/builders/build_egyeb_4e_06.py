# -*- coding: utf-8 -*-
"""4e/06 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p: A vegso meghallgatas), I.V.H. Kihallgato Terem (F6h)
es a temakor-index (F5); a 4e evfolyam-lap evadzarasa.
Kuldetes: A Tuleles Eselyei (I.V.H.-meghallgatas). Mr. Szurreal (vad), Ved Vilmos (vedelem), Nagol (szakerto), SZVETI.
A terepkuldetes es a hazi adatai ujak (valos adat: Open-Meteo 2024 Split es Szabadka napi adatai, Jokic); a felmerok
(tiltott_4e_06) tipus+parameter szerint kizarva; a tananyag es a ket Zsoldos-lista (build_fgy_4e_06) atfedeseit a futas
kiirja, a tudatosakat indoklassal engedi. Minden vegeredmeny tortekkel (Fraction), ahol lehet teljes felsorolassal."""
import sys, os, re, json, glob
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, brief, GYOKER
from fgy_common import cards, oldal, w
import build_fgy_4e_06 as FG               # a Zsoldos-listák paraméterei (WEB) és a tananyagé (TANANYAG)
from abra_stat import svg_oszlop, mutatok, ezres, tized
import adat_4e_06 as ADAT
import tiltott
TILT = tiltott.modul("tiltott_4e_06")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)

T = dict(tagozat="4e", mappa="06-valoszinuseg-statisztika", temakor="Valószínűség és statisztika")
KUL = "A végső meghallgatás"
A1, A2, A3, A4, A5 = ("tananyag-esemenyek.html", "tananyag-valoszinuseg-fogalma.html",
                      "tananyag-felteteles-valoszinuseg.html", "tananyag-binomialis-valoszinuseg.html",
                      "tananyag-valoszinusegi-valtozo.html")
B1, B2 = "tananyag-adatok.html", "tananyag-statisztikai-mutatok.html"
FV, FS, FH = "feladatok-valoszinuseg.html", "feladatok-statisztika.html", "feladatok-hazi.html"
E = []
chk, FR, D, AP, M, N3 = FG.chk, FG.FR, FG.D, FG.AP, FG.M, FG.N3


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{c}</th>" for c in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    fej = f"<tr>{th}</tr>" if any(fejlec) else ""
    return f'<div class="tblwrap"><table class="tt-table">{fej}{tr}</table></div>'


def FORRAS(*kulcsok):
    r = []
    for k in kulcsok:
        cim, url = ADAT.FORRAS[k]
        r.append(f'<a href="{url}">{cim}</a>' if url else cim)
    return '<p class="cap">Forrás: ' + " · ".join(r) + '</p>'


def binom(n, p, k):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


# ==================================================================== F4 — Csalópapír
# a Csalópapír példái a tananyagéi (szándékos ismétlés) — önteszt
KK = list(product(range(1, 7), repeat=2))
chk("CS összeg 7", F(sum(1 for a, b in KK if a + b == 7), 36), F(1, 6))
chk("CS nem dupla", 1 - F(sum(1 for a, b in KK if a == b), 36), F(5, 6))
chk("CS király vagy kőr", F(4 + 13 - 1, 52), F(4, 13))
chk("CS két piros", F(comb(5, 2), comb(8, 2)), F(5, 14))
chk("CS Titanic", round(339 / 466, 3), 0.727)
chk("CS riasztók", 1 - F(1, 10) * F(2, 10) * F(3, 10), F(994, 1000))
chk("CS Jokić", binom(5, F(4, 5), 4), F(4096, 10000))
chk("CS kocka E", sum(F(k, 6) for k in range(1, 7)), F(7, 2))
PL5 = [2, 4, 4, 5, 10]
mp5 = mutatok(PL5)
chk("CS 2;4;4;5;10", (mp5["atlag"], mp5["median"], mp5["mod"], mp5["q1"], mp5["q3"], mp5["aae"], round(mp5["var"], 6)),
    (5, 4, [4], 3, 7.5, 2, 7.2))
chk("CS szórás", round(sqrt(7.2), 2), 2.68)
chk("CS legalább egy", round(1 - 0.8 ** 5, 3), 0.672)
chk("CS V5-csapda", F(3 * 3 + 5, 4), F(7, 2))
# a Csalópapír is a weben van: a példái is átmennek a tiltott-ellenőrzésen
E += TILT.ellenoriz([("kocka", 2), ("kocka", 1), ("kartya", ("francia", 1, 1)), ("golyo", (5, 3, 2)),
                     ("komb", (8, 2)), ("komb", (5, 2)), ("bernoulli", (5, "4/5", 4)), ("bernoulli", (5, "0.2", 1)),
                     ("tabla", "titanic"), ("adatsor", "2;4;4;5;10"), ("erme", 6)])

OSSZ = [
 ("🎲 Események és valószínűség", [
  TABLA(["fogalom", "jelölés, képlet", "példa"], [
      ["eseménytér " + h(A1, "def-esemenyter"), "$\\Omega$ — az összes kimenetel halmaza", "kocka: $\\Omega=\\{1;2;3;4;5;6\\}$"],
      ["ellentett esemény " + h(A1, "def-ellentett"), "$\\overline{A}$; $\\;P(\\overline{A})=1-P(A)$",
       "két kockával nem dupla: $1-\\frac{6}{36}=\\frac56$"],
      ["„vagy”, „és” " + h(A1, "def-esemeny"), "$A\\cup B$, $\\;A\\cap B$",
       "$\\overline{A\\cup B}=\\overline{A}\\cap\\overline{B}$ " + h(A1, "tetel-de-morgan")],
      ["egymást kizáró események " + h(A1, "def-kizaro"), "$A\\cap B=\\emptyset$",
       "egy dobással: 1-est dobunk, 6-ost dobunk"],
      ["klasszikus valószínűség " + h(A2, "tetel-klasszikus"), "$P(A)=\\dfrac{k}{n}$ (egyformán valószínű kimenetelek)",
       "két kocka, összeg 7: $\\frac{6}{36}=\\frac16$"],
      ["statisztikai valószínűség " + h(A2, "def-statisztikai-valoszinuseg"),
       "a relatív gyakoriság sok ismétlésnél ennek a számnak a közelében ingadozik",
       "szerbiai újszülött fiú: $\\approx0{,}515$"],
      ["unió " + h(A2, "tetel-unio"), "$P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$",
       "király vagy kőr: $\\frac{4+13-1}{52}=\\frac{4}{13}$"]]),
  r'<p>Mindig $0\le P(A)\le1$, $P(\Omega)=1$, $P(\emptyset)=0$. Ha a kimenetelek száma nagy, a kombinatorika számol: '
  r'5 piros és 3 fehér golyóból kettőt húzva $P(\text{két piros})=\dfrac{\binom52}{\binom82}=\dfrac{10}{28}=\dfrac{5}{14}$ '
  + h(A2, "pelda-golyok") + '.</p>',
 ]),

 ("🔀 Feltételes valószínűség, függetlenség, „legalább egy”", [
  r'<ul><li><b>Feltételes valószínűség</b> ' + h(A3, "def-felteteles") + r': $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$ — a '
  r'$B$-re leszűkített eseménytérben számolunk. Titanic: $P(\text{túlélt}\mid\text{nő})=\frac{339}{466}\approx0{,}727$, '
  r'de $P(\text{nő}\mid\text{túlélt})=\frac{339}{500}=0{,}678$ ' + h(A3, "pelda-titanic") + r' — a feltétel nem '
  r'cserélhető fel.</li>'
  r'<li><b>Független események</b> ' + h(A3, "def-fuggetlen") + r': $P(A\cap B)=P(A)\cdot P(B)$, azaz '
  r'(ha $P(B)>0$) $P(A\mid B)=P(A)$ — a $B$ ismerete nem változtat $A$ esélyén.</li>'
  r'<li><b>Legalább egy</b> ' + h(A3, "tetel-legalabb-egy") + r': $P(\text{legalább egy})=1-P(\text{egyik sem})$. '
  r'Három független riasztó ($0{,}9$; $0{,}8$; $0{,}7$), legalább egy jelez: $1-0{,}1\cdot0{,}2\cdot0{,}3=0{,}994$ '
  + h(A3, "pelda-riaszto") + '.</li></ul>',
 ]),

 ("🎯 Binomiális valószínűség és valószínűségi változó", [
  r'<p><b>Bernoulli-kísérletsorozat</b> ' + h(A4, "def-bernoulli") + r': $n$ független kísérlet, mindegyiknek két '
  r'kimenetele van (siker, kudarc), a siker valószínűsége mindig $p$. Pontosan $k$ siker valószínűsége '
  + h(A4, "tetel-binomialis-valoszinuseg") + r': $$P_n(k)=\binom nk p^k(1-p)^{n-k}.$$ Jokić öt büntetője, $p=0{,}8$: '
  r'$P_5(4)=5\cdot0{,}8^4\cdot0{,}2=0{,}4096$ ' + h(A4, "pelda-jokic") + r'. „Legalább” és „legfeljebb” esetén több '
  r'$k$ valószínűségét adjuk össze — vagy az ellentett eseményt számoljuk.</p>',
  TABLA(["", "képlet", "jelentés"], [
      ["eloszlás " + h(A5, "tetel-eloszlas"), "$P(X=x_i)=p_i$, $\\;p_1+\\ldots+p_n=1$",
       "melyik értéket mekkora valószínűséggel veszi fel $X$"],
      ["várható érték " + h(A5, "def-varhato-ertek"), "$E(X)=x_1p_1+\\ldots+x_np_n$",
       "sok kísérlet átlaga ennek közelében ingadozik; kocka: $E(X)=3{,}5$ — egyetlen dobással sem jön ki"],
      ["szórásnégyzet, szórás " + h(A5, "def-szorasnegyzet"), "$D^2(X)=\\sum\\bigl(x_i-E(X)\\bigr)^2p_i$, "
       "$\\;D(X)=\\sqrt{D^2(X)}$", "mennyire szóródnak az értékek — a kockázat mértéke"]]),
  r'<p class="le halvany">Döntés várható értékkel ' + h(A5, "pelda-ajanlat") + r': a játék akkor éri meg sokszor '
  r'játszva, ha a nettó nyereség (nyeremény − tét) várható értéke pozitív; ha $E(X)=0$, a játék „igazságos”.</p>',
 ]),

 ("📊 Adatok és diagramok", [
  r'<ul><li><b>Sokaság, minta</b> ' + h(B1, "def-sokasag") + r': a minta akkor jó, ha véletlenszerűen választjuk; az '
  r'önkéntes jelentkezés („aki akar, kitölti”) és a kényelmi minta („az első 30 érkező”) torzíthat.</li>'
  r'<li><b>Ismérv</b> ' + h(B1, "def-ismerv") + r': minőségi (kategóriák) vagy mennyiségi — diszkrét (megszámolt) vagy '
  r'folytonos (mért). <b>Skálák</b> ' + h(B1, "def-skalak") + r': nominális (csak megkülönböztet), ordinális (sorba '
  r'rendez), intervallum (a különbségnek is van értelme); ha valódi nullpont is van, és a hányadosnak is '
  r'van értelme (idő, hossz, darabszám), arányskáláról beszélünk.</li>'
  r'<li><b>Gyakoriság</b> ' + h(B1, "def-gyakorisag") + r': abszolút $f_i$, relatív $\frac{f_i}{n}$ (a relatív '
  r'gyakoriságok összege 1, azaz 100%).</li></ul>',
  TABLA(["diagram", "mire jó?"], [
      ["oszlopdiagram", "kategóriák vagy diszkrét értékek összehasonlítása"],
      ["kördiagram", "egy egész részeinek aránya (középponti szög: $360^\\circ\\cdot\\frac{f_i}{n}$)"],
      ["hisztogram", "folytonos adatok osztályközökben (az oszlopok összeérnek)"],
      ["vonaldiagram", "időbeli változás"]]),
  r'<p class="le halvany">Félrevezető ábra ' + h(B1, "pelda-felrevezeto") + r': nézd meg, honnan indul a függőleges '
  r'tengely — ha nem 0-tól, a 12%-os csökkenés 80%-osnak is látszhat.</p>',
 ]),

 ("📏 Középértékek és szóródás", [
  TABLA(["mutató", "hogyan?", "a $2;\\ 4;\\ 4;\\ 5;\\ 10$ adatsoron"], [
      ["módusz " + h(B2, "def-kozepertekek"), "a leggyakoribb adat (lehet több is, vagy egy sem)", "$4$"],
      ["medián", "a rendezett adatsor közepe (páros $n$-nél a két középső átlaga)", "$4$"],
      ["átlag", "$\\bar x=\\dfrac{x_1+\\ldots+x_n}{n}$; gyakorisági táblából súlyozva " + h(B2, "pelda-sulyozott"),
       "$5$"],
      ["terjedelem", "legnagyobb − legkisebb", "$10-2=8$"],
      ["kvartilisek " + h(B2, "def-kvartilis"), "$Q_1$, $Q_3$: az alsó, illetve a felső fél mediánja (páratlan "
       "$n$-nél a medián egyik félbe sem kerül)", "$Q_1=3$, $Q_3=7{,}5$"],
      ["átlagos abszolút eltérés " + h(B2, "def-szoras"), "$\\dfrac{|x_1-\\bar x|+\\ldots+|x_n-\\bar x|}{n}$", "$2$"],
      ["szórásnégyzet, szórás", "$\\sigma^2=\\dfrac{(x_1-\\bar x)^2+\\ldots+(x_n-\\bar x)^2}{n}$, "
       "$\\;\\sigma=\\sqrt{\\sigma^2}$", "$7{,}2$; $\\;\\approx2{,}68$"],
      ["standardizált érték " + h(B2, "tetel-standardizalt"), "$z=\\dfrac{x-\\bar x}{\\sigma}$ — hány szórásnyira "
       "van az átlagtól", "a $10$-é: $\\approx1{,}86$"]]),
  r'<p>A <b>dobozdiagram</b> öt számot mutat: a legkisebb adatot, $Q_1$-et, a mediánt, $Q_3$-at és a legnagyobb adatot. '
  r'Kiugró adat esetén a medián jobban jellemzi a „tipikus” értéket, mint az átlag. Az adatokat az '
  r'<a href="' + B2 + r'#s4">adatlaborban</a> is kipróbálhatod.</p>',
 ]),

 ("⚠️ Véd Vilmos csapdái, amelyekbe a legtöbben beleesnek", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A tíz leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>Összeadás metszet nélkül:</b> $P(A\cup B)=P(A)+P(B)$ csak kizáró eseményekre igaz; különben vond le '
  r'$P(A\cap B)$-t.</li>'
  r'<li><b>Felcserélt feltétel:</b> $P(A\mid B)$ nem ugyanaz, mint $P(B\mid A)$ — mindig kérdezd meg: mire szűkül az '
  r'eseménytér?</li>'
  r'<li><b>„Legalább egy” összeadással:</b> öt, egyenként $0{,}2$ valószínűségű független próbálkozásból legalább egy '
  r'sikerének valószínűsége nem $5\cdot0{,}2=1$, hanem $1-0{,}8^5\approx0{,}672$.</li>'
  r'<li><b>Elfelejtett $\binom nk$:</b> $p^k(1-p)^{n-k}$ csak EGY sorrend valószínűsége; a $k$ siker helyét '
  r'$\binom nk$-féleképpen választhatjuk ki az $n$ kísérlet közül.</li>'
  r'<li><b>A szerencsejátékos tévedése:</b> szabályos érmével hat fej után sem „jár” az írás; a következő dobás is $\frac12$ '
  r'valószínűséggel fej.</li>'
  r'<li><b>A várható érték nem „a várt érték”:</b> kockával $E(X)=3{,}5$, pedig 3,5-öt nem lehet dobni.</li>'
  r'<li><b>Súlyozás nélküli átlag:</b> három 3-as dolgozat és egy 5-ös átlaga $\frac{3\cdot3+5}{4}=3{,}5$, nem '
  r'$\frac{3+5}{2}=4$ — súlyozni kell.</li>'
  r'<li><b>Medián rendezés nélkül:</b> előbb sorba kell rendezni az adatokat.</li>'
  r'<li><b>Szórás vagy szórásnégyzet?</b> Ha az adatok °C-ban vannak, a $\sigma^2$ mértékegysége °C², a $\sigma$-é °C — a gyökvonás nem '
  r'maradhat el.</li>'
  r'<li><b>Levágott tengely:</b> a diagramot a tengely kezdőpontjával együtt olvasd.</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Valószínűség:</b> <a href="' + A1 + r'">események</a> · <a href="' + A2 + r'">a valószínűség fogalma</a> · '
  r'<a href="' + A3 + r'">feltételes valószínűség</a> · <a href="' + A4 + r'">binomiális valószínűség</a> · '
  r'<a href="' + A5 + r'">valószínűségi változó</a>. <b>Statisztika:</b> <a href="' + B1 + r'">adatok és '
  r'diagramok</a> · <a href="' + B2 + r'">középértékek és szóródás</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FV + r'">Zsoldos-lista — Valószínűség</a> · <a href="' + FS + r'">Zsoldos-lista — '
  r'Statisztika</a> · <a href="' + FH + r'">I.V.H. Kihallgató Terem</a> (házi). A témakört és az évadot '
  r'<a href="terepkuldetes.html">' + KUL + r'</a> zárja.</p></div></div>',
 ]),
]

# ==================================================================== F5p — terepküldetés (önteszt; a kulcs privát DOCX)
FIZ = [85000] * 9 + [1150000]
mf = mutatok(FIZ)
PONT = {j["szezon"]: j["pont"] for j in ADAT.JOKIC}
p23, p24 = PONT["2023–24"], PONT["2024–25"]
GYAK = {"jart": (150, 5), "nem_jart": (50, 20)}     # (létszám, elbukott)
bukott = GYAK["jart"][1] + GYAK["nem_jart"][1]
TEREP_SZAM = {
 "II1-atlag": chk("II1-atlag", mf["atlag"], F(9 * 85000 + 1150000, 10), 191500),
 "II1-median": chk("II1-median", (mf["median"], mf["mod"]), (85000, [85000])),
 "II2-valodi": chk("II2-valodi", round(100 * (p24 - p23) / p23, 1), 12.1),
 "II2-abra": chk("II2-abra", round((p24 - 26) / (p23 - 26), 6), 9.0),
 "II3-szurreal": chk("II3-szurreal", F(GYAK["nem_jart"][1], bukott), F(4, 5)),
 "II3-valodi": chk("II3-valodi", F(GYAK["nem_jart"][1], GYAK["nem_jart"][0]), F(2, 5)),
 "II3-jart": chk("II3-jart", F(GYAK["jart"][1], GYAK["jart"][0]), F(1, 30)),
 "II4-5": chk("II4-5", round(1 - 0.85 ** 5, 3), round(float(1 - F(85, 100) ** 5), 3), 0.556),
 "II4-7": chk("II4-7", round(1 - 0.85 ** 7, 3), 0.679),
 "II4-n": chk("II4-n", next(n for n in range(1, 99) if 1 - F(85, 100) ** n >= F(9, 10)), 15),
 "II5-kov": chk("II5-kov", F(sum(1 for s in product("FI", repeat=8) if s[:7] == ("F",) * 7 and s[7] == "I"),
                             sum(1 for s in product("FI", repeat=8) if s[:7] == ("F",) * 7)), F(1, 2)),
 "II5-7fej": chk("II5-7fej", F(1, 2 ** 7), F(sum(1 for s in product("FI", repeat=7) if set(s) == {"F"}), 2 ** 7)),
 "II5-hig": chk("II5-hig", round((7 + 500) / 1007, 4), 0.5035),
}
print("F5p önteszt:", "OK" if not FG.E and not E else (FG.E, E))

SVG_JOKIC_CSALO = svg_oszlop(["2023–24", "2024–25"], [p23, p24], ymin=26, ymax=30, lepes=1, w=300, h=220,
                             ertek_cimkek=[tized(p23, 1), tized(p24, 1)], szin="#b91c1c",
                             yfelirat="pont/meccs",
                             leiras="Mr. Szürreál oszlopdiagramja 26-nál kezdődő függőleges tengellyel: Jokić "
                                    "meccsenkénti pontátlaga a 2023–24-es és a 2024–25-ös szezonban")
GY_TABLA = TABLA(["gyakorló órákra", "elbukott", "sikeres", "összesen"], [
    ["járt", "5", "145", "150"], ["nem járt", "20", "30", "50"], ["összesen", "25", "175", "200"]])
chk("II3 tábla", (5 + 145, 20 + 30, 5 + 20, 145 + 30), (150, 50, bukott, 175))

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>SZVETI</b> (jegyzőkönyv): A meghallgatás utolsó napja. <b>Mr. Szürreál</b> (I.V.H.): Hét napon át hoztam '
         'a számokat. Ma öt újabb állítással bizonyítom, hogy ez az évfolyam nem tud bánni a véletlennel. '
         '<b>Véd Vilmos:</b> 🌮 <i>Burek-matek:</i> „Mi is hozunk számokat — sajátot!” <b>Nagol:</b> Ez a helyes '
         'út. A védelem két részből áll: egy saját, tisztességesen elvégzett kutatásból és Mr. Szürreál öt állításának '
         'cáfolatából. A végén a védelem záróbeszéde következik.'),
   r'<p>Minden lépésnél írd le, mit és <b>miért</b> csinálsz: melyik mutatót, képletet vagy diagramot választod, és miért '
   r'az illik ide. Számológép és táblázatkezelő (Excel, LibreOffice Calc, Google Táblázatok) használható; a mutatókat '
   r'az <a href="' + B2 + r'#s4">adatlaborban</a> is ellenőrizheted.</p>'
   r'<p><b>Beadandó:</b> a táblázatkezelő-fájl (adatok, gyakorisági táblázat, mutatók, diagram, dobozdiagram) és egy '
   r'legfeljebb két A4-es oldalas jegyzőkönyv (az I. fázis kérdése, módszere, a diagramválasztás indoklása, a '
   r'kvartilisek kézi ellenőrzése, az eredmények és az értelmezés; a II. fázis megoldásai és a záróbeszéd), valamint '
   r'egyetlen dia „a bíráknak”. A határidőt és a beadás módját a tanárod adja meg.</p>'
   r'<p><i>Tervezz rá nagyjából három-négy órát az adatgyűjtéssel együtt, egy hétre elosztva; ez beadandó munka, nem '
   r'órai feladat. Az I. fázis a pontszám fele, a II. fázis kétötöde, a záróbeszéd egytizede.</i></p>',
 ]),

 ("I. fázis — A védelem bizonyítéka: saját kutatás", [
   r'<p>Válassz egy kérdést, amelyre <b>20–30 adattal</b> felelni lehet. Gyűjtheted magad (például: hány percet '
   r'utaznak iskolába az évfolyamtársaid; hány órát alszanak egy tanítási napon; hány lépést tesznek meg naponta), vagy '
   r'dolgozhatsz nyílt adatokkal: a szerb népszámlálás (' + '<a href="' + ADAT.FORRAS["popis"][1] + r'">RZS, Popis '
   r'2022</a>), az <a href="https://ec.europa.eu/eurostat/data/database">Eurostat</a> vagy az <a href="'
   + ADAT.FORRAS["openmeteo"][1] + r'">Open-Meteo</a> időjárás-archívuma (bármely város, bármely év). Olyan kérdést '
   r'válassz, amelyet ezen a honlapon még nem dolgoztunk fel.</p>'
   r'<ol class="reszfeladatok">'
   r'<li><b>A kérdés.</b> Fogalmazd meg a kérdést egy mondatban! Mi a sokaság, mi a minta, mi az ismérv? Minőségi vagy '
   r'mennyiségi (diszkrét vagy folytonos) ismérvről van szó, és milyen skálán mérsz? Ha a teljes sokaságot vizsgálod '
   r'(például egy hónap minden napját), ezt írd le.</li>'
   r'<li><b>Az adatgyűjtés.</b> Hogyan gyűjtötted az adatokat? Lehet-e torz a mintád — és ha igen, merre torzít? '
   r'Nyílt adatnál add meg a pontos forrást (a tábla nevét és a linket).</li>'
   r'<li><b>A táblázat és a diagram.</b> Készíts gyakorisági táblázatot (abszolút és relatív gyakorisággal; folytonos '
   r'adatnál vagy sok különböző értéknél egyenlő szélességű osztályközökkel) és hozzá illő diagramot! Indokold a '
   r'diagram típusát!</li>'
   r'<li><b>A mutatók.</b> Add meg a módusz(oka)t, a mediánt, az átlagot, a terjedelmet, a két kvartilist és a szórást! '
   r'A szórást $1/n$-nel számold: táblázatkezelőben magyarul SZÓR.S, angolul STDEV.P (vigyázz: a magyar „S” a '
   r'sokaságot, az angol „S” a mintát jelenti; a SZÓR.M, illetve a STDEV.S $n-1$-gyel oszt). Készíts dobozdiagramot '
   r'(kézzel vagy az adatlaborban)! A mediánt és a kvartiliseket a rendezett adatsorból kézzel is határozd meg, és '
   r'vesd össze a táblázatkezelő eredményével (ha eltér, nézd meg, milyen kvartilisfüggvényt használt).</li>'
   r'<li><b>Az értelmezés.</b> Négy–hat mondatban: mit mondanak a számok a kérdésedre? Melyik középérték jellemzi '
   r'jobban az adataidat, és miért? Mit mond a szórás, illetve a dobozdiagram? Van-e kiugró adat?</li>'
   r'<li><b>A dia a bíráknak.</b> Egyetlen diagram és egy egymondatos következtetés — tisztességesen: a tengely 0-tól '
   r'indul (vagy jelölve van a törés), van címe, szerepel a mértékegység és az adatok forrása.</li>'
   r'</ol>',
 ]),

 ("II. fázis — Mr. Szürreál öt állítása", [
   r'<p>Mindegyik állítás hibás. Nevezd meg egy-két mondatban a hibát, és számold ki, mi a helyes!</p>'
   r'<ol class="reszfeladatok">'
   r'<li><b>A fizetések.</b> „Az I.V.H. kiképzőtábor 10 dolgozója közül kilencen havi 85&nbsp;000 dinárt keresnek, a '
   r'táborparancsnok 1&nbsp;150&nbsp;000-et. Az átlagfizetés 191&nbsp;500 dinár, tehát a táborban mindenki jól keres.” Számold ki az '
   r'átlagot és a mediánt! Melyik jellemzi jobban egy tipikus dolgozó keresetét, és miért?</li>'
   r'<li><b>A rekordszezon.</b> „Jokić a 2024–25-ös szezonban meccsenként kilencszer annyi pontot dobott, mint '
   r'egy évvel korábban — nézzék az ábrát!”'
   + f'<div class="svgwrap">{SVG_JOKIC_CSALO}</div>' + FORRAS("jokic")
   + r'Hány százalékkal nőtt valójában a pontátlag? Honnan származik a „kilencszeres”? Hogyan kellene helyesen '
   r'ábrázolni?</li>'
   r'<li><b>A gyakorló órák.</b> „Az elbukott kadétok 80%-a nem járt a gyakorló órákra. Tehát aki nem jár gyakorló '
   r'órára, az 80% eséllyel elbukik.” Az évfolyam 200 kadétjának adatai:' + GY_TABLA
   + r'Melyik feltételes valószínűséget számolta ki Mr. Szürreál? Mekkora valójában annak a valószínűsége, hogy egy, a '
   r'gyakorló órákra nem járó kadét elbukik — és mekkora ugyanez a gyakorló órákra járóknál? Mit mond a két szám '
   r'együtt?</li>'
   r'<li><b>A bevetések.</b> „Egy kadét minden bevetésen $0{,}15$ valószínűséggel kerül bajba, a bevetések egymástól '
   r'függetlenek. Öt bevetésből tehát $5\cdot0{,}15=0{,}75$ valószínűséggel kerül bajba, hét bevetésből pedig 105%-os '
   r'biztonsággal.” Miért nem lehet igaz? Mekkora a helyes valószínűség öt, illetve hét bevetésre (három tizedesre)? '
   r'Legalább hány bevetés után lesz legalább $0{,}9$ annak a valószínűsége, hogy a kadét legalább egyszer bajba '
   r'került?</li>'
   r'<li><b>A kiegyenlítés.</b> „A szabályos kísérleti érmével hétszer egymás után fej jött. A relatív gyakoriságnak $0{,}5$ felé '
   r'kell tartania, ezért most nagy valószínűséggel írás jön.” Mekkora a valószínűsége, hogy a nyolcadik dobás írás? '
   r'Mekkora volt a dobások előtt annak a valószínűsége, hogy az első hét dobás mind fej lesz? Hogyan „egyenlít ki” '
   r'mégis a relatív gyakoriság? (Segítség: mi lesz a fejek relatív gyakorisága, ha a hét fej után további 1000 '
   r'dobásból 500 fej?)</li>'
   r'</ol>',
 ]),

 ("III. fázis — A védelem záróbeszéde", [
   r'<p>Írj 6–10 mondatos záróbeszédet a bizottságnak! Használd fel legalább két saját mutatódat az I. fázisból és '
   r'legalább egy helyesen kiszámolt valószínűséget a II. fázisból. Mutasd meg, miért nem elég egyetlen szám (egy '
   r'átlag, egy százalék) egy állítás bizonyításához — és mit kell még megkérdezni mellette (legalább két ilyen szempontot fejts ki).</p>',
   brief('<b>SZVETI</b> (jegyzőkönyv): A meghallgatás lezárva. Bizonyíték: hét tárgyalási nap, két Zsoldos-lista és '
         'kadétonként egy saját kutatás. Az időszerver újraindult, a Void bezárult. <b>Mr. Szürreál:</b> Számokkal '
         'jöttem, és számokkal kaptam választ. Az I.V.H. visszavonja a metszési javaslatot — egyelőre. <b>Véd '
         'Vilmos:</b> 🌮 Ezt meg kell ünnepelni! Burek mindenkinek, egyforma adagokban — a szórás nulla. '
         '<b>Nagol:</b> A kérdés az volt, nagyobb-e nullánál annak a valószínűsége, hogy ez az évfolyam leérettségizik. '
         'A bizonyítékok szerint igen — hogy mennyivel, az már rajtatok múlik. Az utolsó ítéletet nem az I.V.H. mondja '
         'ki, hanem a vizsgabizottság. <i>A Törölt Idővonal</i> évada itt véget ér; a ti idővonalatok most kezdődik. '
         'Sok sikert az érettségin!', outro=True),
 ]),
]

# ==================================================================== F6h — I.V.H. Kihallgató Terem (házi)
SPLIT_ESO = ADAT.IDOJARAS_2024["split"]["esos_nap_havonta"]
HONAP_R = ["jan.", "febr.", "márc.", "ápr.", "máj.", "jún.", "júl.", "aug.", "szept.", "okt.", "nov.", "dec."]
HONAP_T = ["januárban", "februárban", "márciusban", "áprilisban", "májusban", "júniusban", "júliusban", "augusztusban",
           "szeptemberben", "októberben", "novemberben", "decemberben"]
SVG_SPLIT = svg_oszlop(HONAP_R, SPLIT_ESO, ymax=18, lepes=3, w=480, h=240, yfelirat="nap",
                       leiras="Oszlopdiagram: Splitben 2024-ben havonta hány napon esett legalább 1 mm csapadék")
# Szabadka 2024, napi adatok: meleg (a napi középhőmérséklet 25 °C fölött) × esős (legalább 1 mm csapadék)
_om = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "projektek", "szvetkomatek",
                             "4e", "adatok_06", "openmeteo_szabadka_2024.json"))
if _om:
    _d = json.load(open(_om[0]))["daily"]
    ME = {(m, e): sum(1 for t, p in zip(_d["temperature_2m_mean"], _d["precipitation_sum"]) if (t > 25) == m
                      and (p >= 1) == e) for m in (True, False) for e in (True, False)}
else:
    ME = {(True, True): 3, (True, False): 55, (False, True): 76, (False, False): 232}
chk("meleg × esős", (ME[True, True], ME[True, False], ME[False, True], ME[False, False]), (3, 55, 76, 232))
meleg, esos, nap = ME[True, True] + ME[True, False], ME[True, True] + ME[False, True], sum(ME.values())
chk("meleg, esős, napok", (meleg, esos, nap), (FG.MELEG, 79, 366))
ME_TABLA = FG.TABLA(["", "esős", "nem esős", "összesen"], [
    ["meleg", str(ME[True, True]), str(ME[True, False]), str(meleg)],
    ["nem meleg", str(ME[False, True]), str(ME[False, False]), str(nap - meleg)],
    ["összesen", str(esos), str(nap - esos), str(nap)]])

TESTV = {0: 4, 1: 10, 2: 7, 3: 3, 4: 1}
tv = [k for k, f in TESTV.items() for _ in range(f)]
mt = mutatok(tv)
LOVA, LOVB = [8, 9, 7, 8, 8], [10, 6, 9, 5, 10]
ma, mb = mutatok(LOVA), mutatok(LOVB)
SORS = [(20000, 1), (2000, 5), (200, 50), (0, 944)]           # (kifizetés, darab) 1000 sorsjegyből
SJ = [(k - 100, F(db, 1000)) for k, db in SORS]
E_SJ = sum(x * p for x, p in SJ)

HA_ = [
 ("Egy dobozban 7 kék, 5 sárga és 3 zöld zseton van. Egyet véletlenszerűen kihúzunk. Mekkora a valószínűsége, hogy",
  ["sárga?", "nem zöld?", "kék vagy zöld?", "piros?"],
  [M(FR(chk("h-alap-1a", F(5, 15), F(1, 3)))), M(FR(chk("h-alap-1b", 1 - F(3, 15), F(4, 5)))),
   M(FR(chk("h-alap-1c", F(7 + 3, 15), F(2, 3)))), M(chk("h-alap-1d", 0, 0))], True),
 ("Egy 28 fős osztályban 16-an kosaraznak, 10-en úsznak, és 5-en mindkét sportot űzik. Egy tanulót véletlenszerűen "
  "kiválasztunk. Mekkora a valószínűsége, hogy",
  ["kosarazik vagy úszik?", "egyiket sem űzi?", "csak úszik?"],
  [M(FR(chk("h-alap-2a", F(16 + 10 - 5, 28), F(3, 4)))), M(FR(chk("h-alap-2b", 1 - F(21, 28), F(1, 4)))),
   M(FR(chk("h-alap-2c", F(10 - 5, 28), F(5, 28))))]),
 ("Egy 25 fős kadétcsoportban megkérdezték, kinek hány testvére van: 0 testvér — 4 kadét, 1 — 10, 2 — 7, 3 — 3, "
  "4 — 1.",
  ["Mennyi a testvérek számának átlaga?", "Mennyi a mediánja?", "Mennyi a módusza?",
   "A kadétok hány százalékának van pontosan két testvére?"],
  [f"${D(mt['atlag'], 2)}$", M(int(mt["median"])), M(mt["mod"][0]),
   f"${chk('h-alap-3d', 100 * F(TESTV[2], 25), 28)}\\%$"]),
 ("Az oszlopdiagram azt mutatja, hogy Splitben 2024-ben havonta hány napon esett legalább 1 mm csapadék."
  + FG.FORRAS("openmeteo") + f'<div class="svgwrap">{SVG_SPLIT}</div>',
  ["Melyik hónapban volt a legtöbb, és melyikben a legkevesebb esős nap?",
   "Összesen hány esős nap volt az évben, és mennyi a havi átlag?",
   "A relatív gyakoriság alapján mekkora a valószínűsége, hogy Splitben egy véletlenszerűen választott napon legalább "
   "1 mm csapadék esik (a 2024-es szökőév 366 napja alapján, három tizedesre)?"],
  [f"legtöbb: {HONAP_T[SPLIT_ESO.index(max(SPLIT_ESO))]} (${max(SPLIT_ESO)}$ nap); legkevesebb: "
   f"{HONAP_T[SPLIT_ESO.index(min(SPLIT_ESO))]} (${min(SPLIT_ESO)}$ nap)",
   f"${sum(SPLIT_ESO)}$; ${FR(chk('h-alap-4b', F(sum(SPLIT_ESO), 12), 9))}$",
   AP(sum(SPLIT_ESO) / 366)]),
]
chk("h-alap-3", (F(sum(tv), len(tv)), round(mt["atlag"], 9), mt["median"], mt["mod"]), (F(37, 25), 1.48, 1, [1]))
chk("h-alap-4a", (max(SPLIT_ESO), SPLIT_ESO.index(16), min(SPLIT_ESO), SPLIT_ESO.index(1)), (16, 2, 1, 6))

HK_ = [
 ("A táblázat Szabadka 2024-es napjait mutatja aszerint, hogy a napi középhőmérséklet 25 °C fölött volt-e („meleg” nap), és esett-e "
  "legalább 1 mm csapadék („esős” nap)." + FG.FORRAS("openmeteo") + ME_TABLA,
  ["Mennyi $P(\\text{esős}\\mid\\text{meleg})$ (három tizedesre)?",
   "Mennyi $P(\\text{esős}\\mid\\text{nem meleg})$ (három tizedesre)?",
   "Független-e az „esős” esemény a „meleg” eseménytől?",
   "Mennyi $P(\\text{meleg}\\mid\\text{esős})$ (három tizedesre)?"],
  [AP(ME[True, True] / meleg), AP(ME[False, True] / (nap - meleg)), "nem", AP(ME[True, True] / esos)]),
 ("Egy kadét a célzóvizsgán minden lövésnél a többitől függetlenül $0{,}7$ valószínűséggel talál. Négy lövésből "
  "mekkora a valószínűsége, hogy",
  ["pontosan 3 találata lesz?", "legalább 3 találata lesz?", "legalább 1 találata lesz?"],
  [f"${D(binom(4, F(7, 10), 3), 4)}$", f"${D(binom(4, F(7, 10), 3) + binom(4, F(7, 10), 4), 4)}$",
   f"${D(1 - F(3, 10) ** 4, 4)}$"]),
 ("Két lövész öt-öt sorozatának pontszáma: András: 8, 9, 7, 8, 8; Bence: 10, 6, 9, 5, 10.",
  ["Mennyi a két lövész átlaga külön-külön?", "Mennyi a szórásuk külön-külön (két tizedesre)?",
   "Mennyi a mediánjuk külön-külön?",
   "Kit küldenél a versenyre, ha a kiszámíthatóság a fontos?"],
  [f"${D(ma['atlag'], 0)}$; ${D(mb['atlag'], 0)}$", f"$\\approx{D(ma['sz'], 2)}$; $\\approx{D(mb['sz'], 2)}$",
   f"${int(ma['median'])}$; ${int(mb['median'])}$", "Andrást"]),
]
chk("h-kozep-1", (F(ME[True, True], meleg), F(ME[False, True], nap - meleg)), (F(3, 58), F(76, 308)))
def _lovesek(felt):
    """a 16 találat-sorozat felsorolásával: azok valószínűségének összege, amelyekre `felt(találatok száma)` igaz"""
    return sum(F(7, 10) ** sum(s) * F(3, 10) ** (4 - sum(s)) for s in product((1, 0), repeat=4) if felt(sum(s)))


chk("h-kozep-2", (binom(4, F(7, 10), 3), binom(4, F(7, 10), 3) + binom(4, F(7, 10), 4), 1 - F(3, 10) ** 4),
    (F(4116, 10000), F(6517, 10000), F(9919, 10000)),
    (_lovesek(lambda k: k == 3), _lovesek(lambda k: k >= 3), _lovesek(lambda k: k >= 1)))
chk("h-kozep-3", (ma["atlag"], mb["atlag"], round(ma["var"], 6), round(mb["var"], 6), ma["median"], mb["median"]),
    (8, 8, 0.4, 4.4, 8, 9))

HN_ = [
 ("Az I.V.H. büféje 1000 sorsjegyet ad ki, darabját 100 kreditért. Egy sorsjegy 20 000, öt sorsjegy 2000, ötven "
  "sorsjegy 200 kreditet nyer, a többi semmit. Legyen $X$ egy sorsjegy nettó nyeresége (a nyeremény mínusz a 100 "
  "kredites ár).",
  ["Add meg $X$ eloszlását!", "Mennyi $E(X)$?", "Mennyi lenne az a jegyár, amelynél a játék igazságos "
   "($E(X)=0$)?", "Mennyi a büfé haszna, ha mind az 1000 sorsjegy elkel?"],
  ["$P(X=19\\,900)=0{,}001$; $P(X=1900)=0{,}005$; $P(X=100)=0{,}05$; $P(X=-100)=0{,}944$",
   M(chk("h-nehez-1b", E_SJ, -60)), M(chk("h-nehez-1c", sum(k * F(db, 1000) for k, db in SORS), 40)),
   M(N3(chk("h-nehez-1d", 1000 * 100 - sum(k * db for k, db in SORS), 60000)))]),
]
chk("h-nehez-1a", [x for x, _ in SJ], [19900, 1900, 100, -100])
chk("h-nehez-1 összeg", sum(p for _, p in SJ), 1)

# ==================================================================== ÖNELLENŐRZÉS: tiltott és már használt adatok
UJ_TEREP = [("adatsor", "fizetes-tabor"), ("adatsor", "jokic-pont"), ("tabla", "gyakorlo-bukas"),
            ("bernoulli", (5, "0.15", 0)), ("bernoulli", (7, "0.15", 0)), ("erme", 7), ("erme", 8)]
UJ_HAZI = [("golyo", (7, 5, 3)), ("tabla", "kosar-uszas"), ("adatsor", "testverek"), ("adatsor", "split-esos-nap"),
           ("tabla", "meleg-esos-szabadka"), ("bernoulli", (4, "0.7", 3)), ("bernoulli", (4, "0.7", 4)),
           ("adatsor", "lovesz-pontok"), ("adatsor", "sorsjegy")]
E += TILT.ellenoriz(UJ_TEREP + UJ_HAZI)


def _k(t_, p_):
    return (t_, frozenset(p_) if isinstance(p_, set) else p_)


KORABBI = {_k(*a): "Zsoldos-lista" for a in FG.WEB} | {a: "tananyag" for a in FG.TANANYAG}
ENGEDETT = {
 ("adatsor", "jokic-pont"): "terep II/2: két szezon egy levágott tengelyű ábrán (a félrevezetés cáfolata); a "
                            "tananyagban átlag–medián, a Zsoldos-listán a kezdő szezon elhagyása",
}
for a in UJ_TEREP + UJ_HAZI:
    k = _k(*a)
    if k in KORABBI and k not in ENGEDETT:
        E.append(("már használt", k, KORABBI[k]))
for a in UJ_TEREP:
    if _k(*a) in {_k(*b) for b in UJ_HAZI}:
        E.append(("terep = házi", a))
assert not E and not FG.E, (E, FG.E)
print("F6h önteszt és tiltott-ellenőrzés: OK")

# ==================================================================== F5 — témakör-index
INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Valószínűség és statisztika | 4e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="4e">
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
  <a href="../index.html"><span class="tagozat-jel">4e</span></a> ›
  <span class="itt">Valószínűség és statisztika</span>
</nav>
<div class="hero">
  <h1>Valószínűség és statisztika</h1>
  <p class="alcim">Mennyi az esély, és mit mondanak az adatok? Események, klasszikus és statisztikai valószínűség,
  feltételes valószínűség, binomiális valószínűség és várható érték — aztán az adatok: diagramok, középértékek,
  kvartilisek és szórás, valós szerbiai és európai adatokkal.</p>
  <div class="meta-sor"><span class="chip ora">10 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>⚖️ <b>06 — A Túlélés Esélyei (I.V.H.-meghallgatás).</b> Az évad utolsó fejezete. Mr. Szürreál,
  az I.V.H. vádlója számokkal akarja bizonyítani, hogy a 4. évfolyamot le kell metszeni az idővonalról. A védő Véd
  Vilmos — lelkes, de néha rosszul számol —, a szakértő tanú Nagol, a jegyzőkönyvet SZVETI vezeti. Hét tárgyalási nap:
  öt a valószínűségről, kettő a statisztikáról. A végén a kadétok saját kutatással felelnek.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🎲 Valószínűség — Mr. Szürreál vádjai</h3>
__A__
    <h3>📊 Statisztika — a bizonyítékok</h3>
__B__
    <h2>Feladatgyűjtemény</h2>
__F__
    <h2>Összefoglaló</h2>
__OSSZ__
    <h2>Terepküldetés</h2>
__TK__
    <p class="le halvany"><b>Ajánlott sorrend:</b> a hét tananyag-egység sorban (előbb a valószínűség, aztán a
    statisztika), közben a két Zsoldos-lista megfelelő feladatai (az egységek végén a Gyakorolj!-sávok mutatják, melyik
    feladat hová tartozik), a végén az I.V.H. Kihallgató Terem. A Csalópapír az ismétlést szolgálja; a témakört — és
    az évadot — <i>A végső meghallgatás</i> terepküldetés zárja.</p>
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


def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


KT = {
 "A1": kartya(A1, "A véletlen nyelve — kísérlet, kimenetel, esemény",
              "Eseménytér, biztos és lehetetlen esemény, műveletek eseményekkel, ellentett és kizáró események"),
 "A2": kartya(A2, "Mennyi az esély? — a valószínűség fogalma",
              "Relatív gyakoriság és érme-, kockaszimulátor, klasszikus valószínűség, ellentett esemény és unió"),
 "A3": kartya(A3, "Ha már tudjuk… — feltételes valószínűség",
              "Kétdimenziós táblázat (Titanic, számítógépes ismeret), függetlenség és a „legalább egy”"),
 "A4": kartya(A4, "Újra és újra — a binomiális valószínűség",
              "Bernoulli-kísérletsorozat, $\\binom nk p^k(1-p)^{n-k}$, legalább és legfeljebb — Jokić büntetői"),
 "A5": kartya(A5, "Számot a véletlennek — valószínűségi változó",
              "Eloszlás, várható érték, döntés várható értékkel, szórásnégyzet — és a valószínűség gyorsismétlője"),
 "B1": kartya(B1, "Adatokból kép — sokaság, minta, diagram",
              "Ismérvek és skálák, gyakorisági táblázat, négy diagramtípus és a félrevezető grafikon — népszámlálási "
              "adatokkal"),
 "B2": kartya(B2, "Egy szám az egész helyett — középértékek és szóródás",
              "Módusz, medián, átlag, kvartilisek, dobozdiagram, szórás, standardizált érték — adatlaborral"),
 "fv": kartya(FV, "🏋️ Zsoldos-lista — Valószínűség", "Az eseményektől a várható értékig — 25 feladat három szinten "
                                                      "és egy joker (Monty Hall)"),
 "fs": kartya(FS, "🏋️ Zsoldos-lista — Statisztika", "Ismérvektől a standardizált értékig — 20 feladat három szinten "
                                                     "és egy joker, valós adatokkal"),
 "hazi": kartya(FH, "🕹️ I.V.H. Kihallgató Terem — házi feladatok", "Rövid, vegyes gyakorlósor a témakör végére"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL, "Saját statisztikai kutatás és Mr. Szürreál öt félrevezető "
                                                "állításának cáfolata — az évad záró küldetése"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír", "Valószínűség, feltételes és binomiális valószínűség, várható "
                                                     "érték, diagramok, középértékek és szórás egy lapon"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(KT[k] for k in kulcsok) + '\n    </div>\n'


INDEX = (INDEX_TEMPLATE.replace("__A__", racs("A1", "A2", "A3", "A4", "A5")).replace("__B__", racs("B1", "B2"))
         .replace("__F__", racs("fv", "fs", "hazi")).replace("__TK__", racs("tk")).replace("__OSSZ__", racs("ossz")))
# a brief-ek és az index szövegében nincs feladat-adat (a számok a fenti, ellenőrzött listákból jönnek)

if __name__ == "__main__":
    lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon", cim_tiszta="Csalópapír",
        itt="Csalópapír",
        alcim="Események és valószínűség, feltételes és binomiális valószínűség, várható érték, diagramok, "
              "középértékek és szóródás egy lapon — ismétléshez, az érettségi előtti átfutáshoz, nyomtatáshoz.",
        chip="A Túlélés Esélyei · összefoglaló", chip_tipus="összefoglaló", szakaszok=OSSZ,
        elozo=(FH, "I.V.H. Kihallgató Terem"), kovetkezo=("terepkuldetes.html", KUL))
    print("✓ osszefoglalo.html")

    lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
        alcim="Saját statisztikai kutatás, Mr. Szürreál öt félrevezető állításának cáfolata és a védelem "
              "záróbeszéde — az évad záró küldetése. Beadható projektfeladat: a megoldásokat a tanárod ellenőrzi.",
        chip="A Túlélés Esélyei · terepküldetés", chip_tipus="terepküldetés", szakaszok=TEREP,
        elozo=("osszefoglalo.html", "Csalópapír"), kovetkezo=("index.html", "Valószínűség és statisztika — a témakör"))
    print("✓ terepkuldetes.html")

    body = [
     '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(HA_, "alap", "alap"),
     '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(HK_, "kozep", "kozep"),
     '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(HN_, "nehez", "nehez"),
    ]
    oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem", h1="I.V.H. Kihallgató Terem — házi feladatok",
          chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
                 '<span class="chip nehez">Nehéz</span>',
          alcim="Rövid, vegyes gyakorlósor a klasszikus valószínűségtől a várható értékig és a szórásig — házi "
                "feladatnak és a témakör végi ismétléshez. Az I.V.H. minden választ ellenőriz: a végeredmény "
                "lenyitható, de csak a számolás után nézd meg!",
          sections_html="\n".join(body), ossz_nev="Csalópapírt",
          prev=FS, prevc="Zsoldos-lista — Statisztika", nxt="osszefoglalo.html", nxtc="Csalópapír")
    print("✓ feladatok-hazi.html | Alap", len(HA_), "Közép", len(HK_), "Nehéz", len(HN_))

    ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
    open(ut, "w", encoding="utf-8").write(INDEX)
    print("✓ index.html")
