# -*- coding: utf-8 -*-
"""4e/06 — B blokk: statisztika. B1 adatok (sokasag, ismerv, minta, gyakorisag, diagramok, felrevezeto grafikon) ·
B2 statisztikai mutatok (kozepertekek, kvartilisek, szoras, standardizalt ertek, adatlabor) + 🧾 Gyorsismetlo.
Kuldetes: A Tuleles Eselyei. Nagol & Ved Vilmos vs. Mr. Szurreal grafikonjai.
Specifikacio: projektek/szvetkomatek/4e/narrativa_06-valoszinuseg-statisztika.md
Valos adatok: adat_4e_06.py (forrasokkal). Tiltott adatok: tiltott_4e_06 — lent ellenorizve. 06-os felmero nincs."""
import sys, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, _fmt, GYOKER
from abra_stat import (svg_oszlop, svg_hisztogram, svg_kor, svg_vonal, svg_doboz, svg_adatlabor, mutatok, ezres,
                       tized)
import adat_4e_06 as ADAT
import tiltott
TILT = tiltott.modul("tiltott_4e_06")

T = dict(tagozat="4e", mappa="06-valoszinuseg-statisztika", temakor="Valószínűség és statisztika")
KUL = "A Túlélés Esélyei"
FA = "feladatok-statisztika.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(FA + k_h, k_c, FA + n_h, n_c, tagozat="4e")


def NEHEZ(n, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FA}#nehez-{n}">Zsoldos-lista, nehéz {n}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table">{"<tr>" + th + "</tr>" if any(fejlec) else ""}{tr}</table></div>'


def FORRAS(*kulcsok):
    reszek = []
    for k in kulcsok:
        cim, url = ADAT.FORRAS[k]
        reszek.append(f'<a href="{url}">{cim}</a>' if url else cim)
    return '<p class="cap">Forrás: ' + " · ".join(reszek) + '</p>'


def K(szam, jegy=2):
    return tized(szam, jegy).replace(",", "{,}")


def E3(n):
    return ezres(n).replace(" ", "\\,")


def L(adat):
    """Adatsor sima szövegként (tördelhető), egy tizedesre: 8,0; 8,1; … — a hosszú soros KaTeX telefonon kilógna."""
    return "; ".join(tized(v, 1) for v in adat)


# ---------------------------------------------------------------- adatok + önteszt
E = []


def chk(nev, a, b):
    if a != b:
        E.append((nev, a, b))


def kozel(nev, a, b, tur=5e-3):
    if abs(a - b) > tur:
        E.append((nev, a, b))


HZ = ADAT.HAZTARTAS["szabadka"]
hz_rel = [100 * f / HZ["ossz"] for f in HZ["tag_1_5_6plusz"]]
chk("B1 háztartás %", [tized(v, 1) for v in hz_rel], ["33,7", "29,4", "17,4", "13,0", "4,3", "2,2"])
chk("B1 háztartás % összeg", round(sum(round(v, 1) for v in hz_rel), 1), 100.0)
SGS = ADAT.SZAMITOGEP["szabadka"]["osszes"]
chk("B1 szg Szabadka összeg", sum(SGS[1:]), SGS[0])
KOR = ADAT.KOR["szabadka"]["osszes"]
chk("B1 kor összeg", sum(KOR["csoport"]), 123952)
kor20 = [sum(KOR["csoport"][i:i + 4]) for i in (0, 4, 8, 12)] + [sum(KOR["csoport"][16:18])]
chk("B1 kor 20 év", kor20, [24365, 28168, 35043, 31077, 5299])
NEP = ADAT.NEPESSEG
sz11, sz22 = NEP["szabadka_varos"][NEP["evek"].index(2011)], NEP["szabadka_varos"][NEP["evek"].index(2022)]
chk("B1 Szabadka 2011/2022", (sz11, sz22), (141554, 123952))
chk("B1 csökkenés", sz11 - sz22, 17602)
kozel("B1 csökkenés %", (sz11 - sz22) / sz11, 0.124, 5e-4)
chk("B1 levágott", (sz11 - 120000, sz22 - 120000), (21554, 3952))
chk("B1 ötöde", (sz22 - 120000) / (sz11 - 120000) < 0.2, True)
# B2
PONT = [j["pont"] for j in ADAT.JOKIC]
mj = mutatok(PONT)
chk("B2 Jokić n", mj["n"], 11)
chk("B2 Jokić összeg", round(sum(PONT), 1), 246.9)
chk("B2 Jokić medián", mj["median"], 24.5)
chk("B2 Jokić módusz", mj["mod"], [26.4])
kozel("B2 Jokić átlag", mj["atlag"], 22.445, 1e-3)
chk("B2 súlyozott", Fr(3 * 3 + 5, 4), Fr(7, 2))
chk("B2 zsebpénz", (sum([2000, 2500, 2500, 3000, 40000]) / 5, sorted([2000, 2500, 2500, 3000, 40000])[2]), (10000, 2500))
IDO = ADAT.IDOJARAS_2024
SPLIT, LISSZ, SZAB = IDO["split"]["havi_kozep"], IDO["lisszabon"]["havi_kozep"], IDO["szabadka"]["havi_kozep"]
ms, ml = mutatok(SPLIT), mutatok(LISSZ)
chk("B2 Split kvartilisek", (round(ms["median"], 2), round(ms["q1"], 2), round(ms["q3"], 2)), (17.05, 11.35, 22.6))
chk("B2 Lissz kvartilisek", (round(ml["median"], 2), round(ml["q1"], 2), round(ml["q3"], 2)), (17.1, 14.0, 20.05))
chk("B2 Split terjedelem", round(ms["max"] - ms["min"], 2), 20.6)
chk("B2 Lissz terjedelem", round(ml["max"] - ml["min"], 2), 10.6)
kozel("B2 Split átlag", ms["atlag"], 17.19); kozel("B2 Lissz átlag", ml["atlag"], 17.31)
kozel("B2 Split szórás", ms["sz"], 6.97); kozel("B2 Lissz szórás", ml["sz"], 3.42)
kozel("B2 Lissz szórásnégyzet", ml["var"], 11.7, 0.05)
kis = mutatok([2, 4, 4, 5, 10])
chk("B2 kis példa", (kis["atlag"], kis["aae"], round(kis["var"], 6)), (5, 2, 7.2))
kozel("B2 kis szórás", kis["sz"], 2.68)
chk("B2 z", (Fr(78 - 70, 5), Fr(85 - 80, 10)), (Fr(8, 5), Fr(1, 2)))
chk("B2 kvíz A/B", (mutatok([10] * 4)["atlag"], mutatok([0, 5, 15, 20])["atlag"], mutatok([10] * 4)["sz"]), (10, 10, 0))
E += TILT.ellenoriz([("adatsor", "haztartas-szabadka"), ("adatsor", "kor-szabadka"), ("adatsor", "nepesseg-szabadka"),
                     ("adatsor", "szamitogep-szabadka"), ("adatsor", "jokic-pont"), ("adatsor", "homerseklet-2024"),
                     ("adatsor", (2, 4, 4, 5, 10)), ("adatsor", (2000, 2500, 2500, 3000, 40000))])
assert not E, E
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_HZ = svg_oszlop(["1", "2", "3", "4", "5", "6+"], [round(v, 1) for v in hz_rel], ymax=40, lepes=10, szazalek=True,
                    ertek_cimkek=[tized(v, 1) + "%" for v in hz_rel], yfelirat="a háztartások %-a",
                    xfelirat="a háztartás taglétszáma",
                    leiras="Oszlopdiagram: a szabadkai háztartások megoszlása taglétszám szerint 2022-ben: 1 tag 33,7%, "
                           "2 tag 29,4%, 3 tag 17,4%, 4 tag 13,0%, 5 tag 4,3%, 6 vagy több 2,2%")
SVG_KOR = svg_kor(["ismeri", "részben ismeri", "nem ismeri", "ismeretlen"], SGS[1:],
                  leiras="Kördiagram: a szabadkai 15 éves és idősebb lakosok számítógépes ismerete 2022-ben: ismeri "
                         "43,3%, részben ismeri 32,9%, nem ismeri 23,3%, ismeretlen 0,6%")
hatarok = list(range(0, 95, 5))
SVG_HISZT = svg_hisztogram(hatarok, KOR["csoport"], ymax=10000, lepes=2000,
                           xcimkek={i: (str(hatarok[i]) if i < 17 else "85+") for i in range(0, 18, 2)} | {17: "85+"},
                           yfelirat="fő", xfelirat="életkor (év), 5 éves korcsoportok",
                           leiras="Hisztogram: Szabadka lakói 5 éves korcsoportok szerint 2022-ben; a legnépesebb "
                                  "csoportok a 40–44 és a 65–69 évesek")
SVG_VONAL = svg_vonal(NEP["evek"], NEP["szabadka_varos"], ymin=0, ymax=160000, lepes=40000, yfelirat="lakos",
                      pont_cimkek=[ezres(v) if e in (1948, 1981, 2022) else "" for e, v in
                                   zip(NEP["evek"], NEP["szabadka_varos"])],
                      xfelirat="a népszámlálás éve",
                      leiras="Vonaldiagram: Szabadka város lakossága a népszámlálások szerint 1948 és 2022 között; "
                             "1981-ig nő (154 611 főig), azután csökken (2022: 123 952)")
SVG_ROSSZ = svg_oszlop(["2011", "2022"], [sz11, sz22], ymin=120000, ymax=145000, lepes=5000, w=300, h=230,
                       ertek_cimkek=[ezres(sz11), ezres(sz22)], szin="#b91c1c",
                       leiras="Félrevezető oszlopdiagram: a függőleges tengely 120 000-nél kezdődik, ezért a 2022-es "
                              "oszlop a 2011-esnek kevesebb mint ötöde")
SVG_JO = svg_oszlop(["2011", "2022"], [sz11, sz22], ymin=0, ymax=150000, lepes=30000, w=300, h=230,
                    ertek_cimkek=[ezres(sz11), ezres(sz22)], szin="#047857",
                    leiras="Helyes oszlopdiagram: a függőleges tengely 0-tól indul, a két oszlop magassága alig tér el")
SVG_BOX = svg_doboz([("Split", SPLIT), ("Lisszabon", LISSZ)], xfelirat="havi középhőmérséklet, °C (2024)",
                    tengely=(5, 30, 5),
                    leiras="Dobozdiagram: Split és Lisszabon 2024-es havi középhőmérséklete. A két medián majdnem "
                           "egyforma (17,05 és 17,1 °C), de Split doboza és bajuszai sokkal szélesebbek")
SVG_LAB = svg_adatlabor([("Split, havi középhőmérséklet 2024 (°C)", SPLIT),
                         ("Lisszabon, havi középhőmérséklet 2024 (°C)", LISSZ),
                         ("Szabadka, havi középhőmérséklet 2024 (°C)", SZAB),
                         ("Jokić pont/meccs, 11 NBA-alapszakasz", PONT)], kezdo=0,
                        felirat="Válassz adatsort, vagy írd át a számokat — a mutatók és az ábra azonnal frissülnek.")

# a mém: súlyzógép-kopás (a forrás: projektek/4e/munkafajlok/6_…/Képek) — WebP, 480 px
KEP = "img/sulyzo-kopas.webp"
if not os.path.isfile(os.path.join(GYOKER, T["tagozat"], T["mappa"], KEP)):
    print("⚠ hiányzik:", KEP)
MEM = (f'<figure><img src="{KEP}" alt="Egy edzőtermi súlyzógép súlylapjai 10-től 110 kilogrammig; a középső '
       f'súlyoknál a legnagyobb a kopás, a két szél felé egyre kisebb" width="480" height="600" loading="lazy" '
       f'decoding="async"><figcaption>„Normális eloszlás” — egy súlyzógép kopásnyoma. (Internetes mém.)</figcaption>'
       f'</figure>')

# ---------------------------------------------------------------- B1
hz_sorok = [[("6 vagy több" if i == 5 else str(i + 1)), ezres(f), tized(hz_rel[i], 1)]
            for i, f in enumerate(HZ["tag_1_5_6plusz"])] + [["<b>összesen</b>", ezres(HZ["ossz"]), "100,0"]]
kor_sorok = [[c, ezres(v), tized(100 * v / 123952, 1)] for c, v in
             zip(["0–19", "20–39", "40–59", "60–79", "80 és több"], kor20)] + [["<b>összesen</b>", ezres(123952), "100"]]

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál</b> kivetít egy oszlopdiagramot: Szabadka lakossága 2011 és 2022 között „összeomlott” — a '
         '2022-es oszlop alig ötöde a 2011-esnek. <b>Véd Vilmos:</b> Nézze meg valaki a függőleges tengelyt! '
         '<b>Nagol:</b> A csökkenés valós, de nem ekkora. Mielőtt bármit ábrázolunk, tisztázzuk: honnan jön az adat, '
         'mit mérünk, és melyik diagram mit mutat. <b>SZVETI:</b> A tengelyt 120 000-nél vágták el. Rögzítve.'),
 ]),
 ("Sokaság, ismérv, minta", [
   '<p class="lead">A statisztika adatokat gyűjt, rendez, ábrázol és értelmez. A 2022-es szerbiai népszámlálás (Popis '
   '2022) jó példa: minden lakosról ugyanazokat az adatokat rögzítették.</p>',
   doboz("definicio", "Sokaság, egyed, minta",
         '<p>A vizsgált dolgok összessége a <b>sokaság</b> (populáció), egy-egy tagja az <b>egyed</b>. Ha nem az egész '
         'sokaságot vizsgáljuk, hanem csak egy részét, az a <b>minta</b>. A népszámlálás a teljes sokaságot vizsgálja '
         '(Szerbia 6 647 003 lakosát), egy közvélemény-kutatás csak egy mintát (például 1000 megkérdezettet).</p>',
         hid="def-sokasag"),
   doboz("definicio", "Ismérv",
         '<p>Az <b>ismérv</b> (változó) az a tulajdonság, amelyet az egyedeken megfigyelünk. <b>Minőségi</b> ismérv '
         'kategóriákat ad (nem, számítógépes ismeret, kedvenc sport). <b>Mennyiségi</b> ismérv számértéket ad, amellyel '
         'számolni is van értelme; lehet <b>diszkrét</b> (megszámolható: a háztartás taglétszáma) vagy '
         '<b>folytonos</b> (mért: életkor, testmagasság, hőmérséklet).</p>', hid="def-ismerv"),
   doboz("definicio", "Mérési skálák",
         '<p>A <b>nominális</b> skála csak megkülönböztet (nem, mezszám, irányítószám). Az <b>ordinális</b> skála sorba '
         'is rendez (számítógépes ismeret: nem ismeri &lt; részben ismeri &lt; ismeri; iskolai végzettség). Az '
         '<b>intervallumskálán</b> a különbségeknek is van értelme (hőmérséklet °C-ban, évszám, pontszám).</p>',
         hid="def-skalak"),
   '<p>A minta akkor mond valamit a sokaságról, ha <b>véletlenszerűen</b> választjuk: minden egyednek ugyanakkora '
   'esélye van bekerülni. Ha csak a könnyen elérhetőket kérdezzük meg (a barátainkat, egy közösségi oldal '
   'követőit), a minta <b>torz</b> lesz, és a következtetés sem érvényes a sokaságra.</p>',
   doboz("csapda", "Véd Vilmos csapda — „a barátaim szerint…”",
         '<p>Vilmos megkérdezte hét barátját, szeretik-e a matekot. Mind igent mondtak, ezért kijelentette: „a '
         'gimnazisták 100%-a szereti a matekot”. A minta kicsi és torz: a barátok hasonlítanak egymásra, és a '
         'kérdezőnek is szívesen mondanak igent. Egy másik gyakori hiba: ami szám, azt mennyiségi ismérvnek hinni. A '
         'mezszám nominális — a 23-as játékos nem „23-szor annyi”, mint az 1-es, és a mezszámok átlagának nincs '
         'értelme.</p>'),
   kviz('Melyik mennyiségi ismérv?',
        ['a háztartás taglétszáma', 'a kosárlabdázók mezszáma', 'a lakcím irányítószáma', 'a kedvenc sport'], 0,
        jo="✔ A taglétszám megszámolható mennyiség (diszkrét), átlagolni is van értelme.",
        nem="✘ A mezszám és az irányítószám csak azonosít (nominális), a kedvenc sport kategória. Mennyiségi a "
            "taglétszám."),
 ]),
 ("Gyakorisági táblázat", [
   '<p class="lead">Az összegyűjtött adatokat először táblázatba rendezzük: melyik érték hányszor fordul elő.</p>',
   doboz("definicio", "Abszolút és relatív gyakoriság",
         r'<p>Egy érték <b>abszolút gyakorisága</b> ($f_i$) az, hogy hányszor fordul elő; a <b>relatív gyakorisága</b> '
         r'$\frac{f_i}{n}$, ahol $n$ az összes adat száma. A relatív gyakoriságok összege 1 — gyakran százalékban '
         r'adjuk meg, akkor 100%.</p>', hid="def-gyakorisag"),
   doboz("pelda", "I.V.H. Akták — a szabadkai háztartások",
         TABLA(["taglétszám", "háztartás (abszolút gyakoriság)", "relatív gyakoriság (%)"], hz_sorok)
         + FORRAS("popis"), hid="pelda-haztartasok"),
   '<p>Ha az ismérv sokféle értéket vehet fel (életkor, jövedelem), az adatokat <b>osztályközökbe</b> soroljuk, '
   'például 0–19, 20–39 éves. Szabadka 123 952 lakosa 20 éves korcsoportokban:</p>',
   doboz("pelda", "I.V.H. Akták — Szabadka korösszetétele",
         TABLA(["életkor (év)", "lakos", "relatív gyakoriság (%)"], kor_sorok) + FORRAS("popis")
         + '<p>(A százalékok egy tizedesre kerekítve; a kerekítés miatt az összegük 100,1.) Az 5 éves korcsoportokat '
           'a következő szakasz hisztogramja mutatja.</p>', hid="pelda-korosszetetel"),
 ]),
 ("Melyik diagram mire jó?", [
   '<p class="lead">Ugyanaz az adat többféleképpen ábrázolható, de nem mindegy, hogyan: a diagram típusa az ismérv '
   'típusától és a kérdéstől függ.</p>',
   abra(SVG_HZ, "<b>Oszlopdiagram</b> — kategóriák vagy diszkrét értékek összehasonlítására. A szabadkai háztartások "
                "taglétszám szerint (%), 2022."),
   abra(SVG_KOR, "<b>Kördiagram</b> — egy egész részeinek arányára. A szabadkai 15 éves és idősebb lakosok "
                 "(105 873 fő) számítógépes ismerete, 2022. (A kerekítés miatt a százalékok összege 100,1.)"),
   abra(SVG_HISZT, "<b>Hisztogram</b> — osztályközökbe sorolt mennyiségi adatra; az oszlopok összeérnek. Szabadka "
                   "lakói 5 éves korcsoportok szerint (fő), 2022; az utolsó oszlop a 85 évesek és idősebbek nyitott "
                   "csoportja."),
   abra(SVG_VONAL, "<b>Vonaldiagram</b> — időbeli változásra. Szabadka város lakossága a népszámlálások szerint "
                   "(fő). A népszámlálások módszertana az évtizedek során többször változott."),
   FORRAS("popis"),
   TABLA(["kérdés, adattípus", "diagram"], [
       ["kategóriák vagy diszkrét értékek összehasonlítása", "oszlopdiagram"],
       ["egy egész részeinek aránya", "kördiagram"],
       ["mennyiségi adat eloszlása osztályközökben", "hisztogram"],
       ["változás az időben", "vonaldiagram"]]),
   doboz("csapda", "Véd Vilmos csapda — rossz diagram, rossz üzenet",
         '<p>Kördiagram csak akkor jó, ha a részek egy egészet adnak ki: ha valaki több sportot is űz, a „kedvenc '
         'sportok” százalékainak összege 100 fölé mehet — ide oszlopdiagram kell. A hisztogram oszlopai összeérnek, '
         'mert az osztályközök egymáshoz csatlakoznak; ha az osztályközök nem egyforma szélesek, azt jelezni kell.</p>'),
   doboz("erdekesseg", "A kopás mint hisztogram",
         '<p>Egy edzőtermi súlyzógépen a lyukak körüli kopás megmutatja, melyik súlyt használják a legtöbben: a középső '
         'értékeknél a legnagyobb, a két szél felé fogy — mint egy harang alakú hisztogram. (A harang alakú, '
         '„normális” eloszlásról a felsőbb matematika szól.)</p>' + MEM),
   kviz('Melyik diagram mutatja a legjobban, hogyan változott Szabadka lakossága 1948 és 2022 között?',
        ['vonaldiagram', 'kördiagram', 'hisztogram', 'dobozdiagram'], 0,
        jo="✔ Időbeli változásra a vonaldiagram való: a vízszintes tengelyen az évek, a pontok összekötve.",
        nem="✘ A kördiagram egy egész részeit mutatja, a hisztogram egy eloszlást — az időbeli változást a "
            "vonaldiagram mutatja."),
 ]),
 ("Félrevezető grafikonok", [
   '<p class="lead">Egy grafikon adatai lehetnek pontosak, a kép mégis félrevezethet.</p>',
   abra(SVG_ROSSZ, "Mr. Szürreál ábrája: a függőleges tengely 120 000-nél kezdődik."),
   abra(SVG_JO, "Ugyanezek az adatok helyesen: a tengely 0-tól indul."),
   FORRAS("popis"),
   doboz("pelda", "I.V.H. Akták — mennyit csökkent?",
         r'<p>A népszámlálások szerint Szabadka lakossága 2011-ben $' + E3(sz11) + r'$, 2022-ben $' + E3(sz22)
         + r'$ fő volt. A csökkenés $' + E3(sz11 - sz22) + r'$ fő, vagyis $$\frac{' + E3(sz11 - sz22) + r'}{'
         + E3(sz11) + r'}\approx0{,}124=12{,}4\%.$$ Mr. Szürreál ábráján a tengely 120 000-nél kezdődik, ezért az '
           r'oszlopok látható magassága $' + E3(sz11 - 120000) + r'$ és $' + E3(sz22 - 120000) + r'$ egységnyi: a '
           r'2022-es oszlop a 2011-esnek kevesebb mint ötöde, mintha a lakosság 80%-kal fogyott volna.</p>'
         + '<p>Más gyakori torzítások: a térhatású (3D) kördiagram, amelyen a közelebbi cikk nagyobbnak látszik; a '
           'képes diagram, amelyen a kétszer magasabb ikon négyszer akkora területű; és a különböző skálájú tengelyek '
           'két egymás melletti ábrán.</p>', hid="pelda-felrevezeto"),
   doboz("erdekesseg", "Tisztességes adathasználat",
         '<p>A levágott tengely önmagában nem tilos — kis változásokat néha csak így lehet látni —, de akkor jelezni '
         'kell (a tengelyen egy törésjellel), és a szövegnek a valódi arányt kell mondania. A tudatos manipuláció '
         'akkor is félrevezetés, ha minden szám pontos.</p>'),
   NEHEZ(1, "egy félrevezető ábra elemzése — mi a valódi arány?"),
   GY("#alap-1", "A 1–5", "#kozep-1", "K 1–3"),
   brief('<b>Mr. Szürreál:</b> Rendben, a tengelyem… kreatív volt. De van egy másik számom: az átlag. <b>Véd '
         'Vilmos:</b> Az átlag hazudik, ha egyedül hagyják! <b>Nagol:</b> Ezért tesszük mellé a mediánt és a '
         'szórást.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
split_rend, lissz_rend = sorted(SPLIT), sorted(LISSZ)
MUT_TABLA = TABLA(["mutató", "Split", "Lisszabon"], [
    ["átlag", _fmt(ms["atlag"]), _fmt(ml["atlag"])],
    ["medián", _fmt(ms["median"]), _fmt(ml["median"])],
    ["legkisebb / legnagyobb", _fmt(ms["min"]) + " / " + _fmt(ms["max"]), _fmt(ml["min"]) + " / " + _fmt(ml["max"])],
    ["terjedelem", _fmt(ms["max"] - ms["min"]), _fmt(ml["max"] - ml["min"])],
    ["$Q_1$ / $Q_3$", _fmt(ms["q1"]) + " / " + _fmt(ms["q3"]), _fmt(ml["q1"]) + " / " + _fmt(ml["q3"])],
    ["interkvartilis terjedelem", _fmt(ms["q3"] - ms["q1"]), _fmt(ml["q3"] - ml["q1"])],
    ["szórás ($\\sigma$)", _fmt(ms["sz"]), _fmt(ml["sz"])]])
FUGG_TABLA = TABLA(["mutató", "magyar nyelvű program", "angol nyelvű program"], [
    ["átlag", '<span class="kbd">ÁTLAG</span>', '<span class="kbd">AVERAGE</span>'],
    ["medián", '<span class="kbd">MEDIÁN</span>', '<span class="kbd">MEDIAN</span>'],
    ["módusz", '<span class="kbd">MÓDUSZ.EGY</span>', '<span class="kbd">MODE.SNGL</span>'],
    ["kvartilis", '<span class="kbd">KVARTILIS.KIZÁR</span>', '<span class="kbd">QUARTILE.EXC</span>'],
    ["átlagos abszolút eltérés", '<span class="kbd">ÁTL.ELTÉRÉS</span>', '<span class="kbd">AVEDEV</span>'],
    ["szórásnégyzet ($1/n$)", '<span class="kbd">VAR.P</span>', '<span class="kbd">VAR.P</span>'],
    ["szórás ($1/n$)", '<span class="kbd">SZÓR.P</span>', '<span class="kbd">STDEV.P</span>']])

B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál:</b> Két kiképzőbázis közül kell választani: Split vagy Lisszabon. 2024-ben a havi '
         'középhőmérsékletek átlaga mindkettőben kb. 17 °C, tehát az éghajlatuk egyforma. <b>Véd Vilmos:</b> '
         'Egyforma? Splitben januárban 8 °C volt, augusztusban 28,6! <b>Nagol:</b> Az átlag egyetlen szám: megmutatja, '
         'hol van a „közép”, de azt nem, mennyire szóródnak az adatok. Ehhez további mutatók kellenek.'),
 ]),
 ("Középértékek", [
   '<p class="lead">Egy adatsort egyetlen számmal szeretnénk jellemezni. Háromféle „közép” van, és nem mindig ugyanazt '
   'mutatják.</p>',
   doboz("definicio", "Módusz, medián, átlag",
         r'<p>A <b>módusz</b> ($Mo$) a leggyakrabban előforduló érték (több is lehet, vagy egy sem). A <b>medián</b> '
         r'($Me$) a nagyság szerint rendezett adatsor középső eleme; páros elemszámnál a két középső átlaga — az adatok '
         r'legalább fele legfeljebb, legalább fele legalább ekkora. Az <b>átlag</b> (számtani közép) az adatok összege '
         r'osztva az elemszámmal: $$\bar x=\frac{x_1+x_2+\ldots+x_n}{n}.$$</p>', hid="def-kozepertekek"),
   doboz("pelda", "I.V.H. Akták — Jokić pontjai",
         r'<p>Nikola Jokić meccsenkénti pontátlaga az NBA-ben töltött 11 alapszakaszában (2015–16-tól 2025–26-ig), '
         r'nagyság szerint rendezve: ' + L(mj["s"]) + r'. Módusz: $26{,}4$ (kétszer fordul elő). Medián: a 6. '
         r'adat, $24{,}5$. Átlag: $\frac{246{,}9}{11}\approx22{,}4$.</p><p>Az átlag kisebb a mediánnál, mert az első '
         r'szezon 10,0 pontja lefelé húzza: egy kiugró érték az átlagot sokkal jobban elmozdítja, mint a '
         r'mediánt.</p>' + FORRAS("jokic"), hid="pelda-jokic-pontok"),
   doboz("pelda", "I.V.H. Akták — súlyozott átlag gyakorisági táblából",
         r'<p>Ha az adatok gyakorisági táblában vannak, minden értéket a gyakoriságával szorzunk: '
         r'$$\bar x=\frac{x_1f_1+x_2f_2+\ldots+x_kf_k}{f_1+f_2+\ldots+f_k}.$$ A szabadkai háztartásoknál (a „6 vagy '
         r'több” helyett 6-tal) ez $\frac{121\,455}{52\,491}\approx2{,}31$ — pontosan az, amit a '
         r'<a href="tananyag-valoszinusegi-valtozo.html#pelda-varhato">valószínűségi változónál várható értékként</a> '
         r'kaptunk. Nem véletlen: a relatív gyakoriságokkal súlyozott átlag ugyanaz a képlet, mint a valószínűségekkel '
         r'súlyozott várható érték.</p>', hid="pelda-sulyozott"),
   doboz("csapda", "Véd Vilmos csapda — átlagok átlaga",
         r'<p>Vilmos három dolgozatának átlaga 3,0, a negyedik 5-ös lett. „Az új átlagom $\frac{3+5}2=4$!” Nem: a 3,0 '
         r'három jegy átlaga, tehát háromszoros súllyal számít: $$\frac{3\cdot3+5}4=\frac{14}4=3{,}5.$$</p>'),
   kviz('Öt barát havi zsebpénze (dinárban): 2000, 2500, 2500, 3000, 40 000. Melyik szám jellemzi jobban a „tipikus” '
        'zsebpénzt?', ['a medián, 2500', 'az átlag, 10 000', 'a legnagyobb érték, 40 000', 'a legkisebb érték, 2000'],
        0,
        jo="✔ Az egyetlen kiugró 40 000 az átlagot 10 000-re húzza, holott négyen 3000 alatt kapnak. A medián, 2500, "
           "tipikusabb.",
        nem="✘ Az átlag (10 000) egyetlen kiugró érték miatt ilyen nagy — öt barátból négynek 3000 vagy kevesebb jut. "
            "A medián (2500) jobban jellemzi a tipikus értéket."),
 ]),
 ("Terjedelem és kvartilisek", [
   '<p class="lead">A középérték mellé az is kell, mennyire vannak szétszórva az adatok. A legegyszerűbb mutatók a '
   'rendezett adatsorból olvashatók le.</p>',
   doboz("definicio", "Terjedelem, kvartilisek, dobozdiagram",
         r'<p>A <b>terjedelem</b> a legnagyobb és a legkisebb adat különbsége. A rendezett adatsort a medián két félre '
         r'osztja (páratlan elemszámnál a medián egyik félbe sem kerül); az alsó fél mediánja az <b>alsó kvartilis</b> '
         r'($Q_1$), a felső félé a <b>felső kvartilis</b> ($Q_3$). Az adatok nagyjából negyede $Q_1$ alatt, negyede '
         r'$Q_3$ fölött van; a középső fél a $[Q_1;\,Q_3]$ szakaszba esik, ennek hossza az <b>interkvartilis '
         r'terjedelem</b>, $Q_3-Q_1$. A <b>dobozdiagram</b> öt számot mutat: a legkisebb adatot, $Q_1$-et, a mediánt, '
         r'$Q_3$-at és a legnagyobb adatot.</p>', hid="def-kvartilis"),
   doboz("pelda", "I.V.H. Akták — Split és Lisszabon",
         r'<p>A 2024-es havi középhőmérsékletek (°C) nagyság szerint rendezve:</p>'
         r'<p>Split: ' + L(split_rend) + r'</p><p>Lisszabon: ' + L(lissz_rend) + r'</p>'
         r'<p>Splitben a medián a két középső adat átlaga: $\frac{15{,}7+18{,}4}2=17{,}05$; az alsó hat adat mediánja '
         r'$Q_1=\frac{11{,}0+11{,}7}2=11{,}35$, a felső hat adaté $Q_3=\frac{21{,}4+23{,}8}2=22{,}6$.</p>'
         + MUT_TABLA + abra(SVG_BOX, "Dobozdiagram: a medián majdnem egyforma, a szóródás nagyon különböző.")
         + FORRAS("openmeteo"), hid="pelda-split-lisszabon"),
   doboz("erdekesseg", "A táblázatkezelő másképp számolhat",
         '<p>A kvartilisnek több elfogadott definíciója van. A táblázatkezelők <span class="kbd">KVARTILIS.TARTALMAZ</span> '
         '(QUARTILE.INC) és <span class="kbd">KVARTILIS.KIZÁR</span> (QUARTILE.EXC) függvénye két szomszédos adat '
         'között arányosan osztva számol, ezért kis adatsornál kissé eltérő értéket adhat. Ezen az oldalon — és az '
         'adatlaborban — a „fél mediánja” módszert használjuk.</p>'),
 ]),
 ("Szórás", [
   '<p class="lead">A terjedelem csak a két szélső adatot nézi. A szórás minden adatot figyelembe vesz: azt méri, '
   'átlagosan mennyire térnek el az adatok az átlagtól.</p>',
   doboz("definicio", "Átlagos abszolút eltérés, szórásnégyzet, szórás",
         r'<p>$$\text{átlagos abszolút eltérés}=\frac{|x_1-\bar x|+\ldots+|x_n-\bar x|}{n},\qquad '
         r'\sigma^2=\frac{(x_1-\bar x)^2+\ldots+(x_n-\bar x)^2}{n},\qquad \sigma=\sqrt{\sigma^2}.$$ A $\sigma^2$ az '
         r'<b>átlagos négyzetes eltérés</b> (szórásnégyzet), a $\sigma$ a <b>szórás</b>. A szórás mértékegysége '
         r'ugyanaz, mint az adatoké.</p>', hid="def-szoras"),
   doboz("pelda", "I.V.H. Akták — lépésről lépésre",
         r'<p>A $2;\ 4;\ 4;\ 5;\ 10$ adatsor átlaga $\bar x=5$. Az eltérések: $-3;\ -1;\ -1;\ 0;\ 5$ — az összegük 0 '
         r'(ez mindig így van). Az átlagos abszolút eltérés $\frac{3+1+1+0+5}5=2$; a szórásnégyzet '
         r'$\frac{9+1+1+0+25}5=7{,}2$; a szórás $\sqrt{7{,}2}\approx2{,}68$.</p>'
         r'<p>Split és Lisszabon: az átlag szinte ugyanaz, a szórás Splitben $\sigma\approx' + K(ms["sz"], 1)
         + r'$ °C, Lisszabonban $\sigma\approx' + K(ml["sz"], 1) + r'$ °C. Lisszabon éghajlata kiegyenlítettebb '
           r'(óceáni), Splité szélsőségesebb.</p>', hid="pelda-szoras"),
   doboz("tetel", "Standardizált érték",
         r'<p>Különböző átlagú és szórású adatsorok összehasonlításakor azt nézzük, hány szórásnyira van egy adat a '
         r'saját átlagától: $$z=\frac{x-\bar x}{\sigma}.$$</p>', hid="tetel-standardizalt"),
   doboz("pelda", "I.V.H. Akták — melyik teszt sikerült jobban?",
         r'<p>Egy kadét a logikai teszten 78 pontot ért el (a csoport átlaga 70, szórása 5), a statisztikai teszten '
         r'85-öt (átlag 80, szórás 10). Nyers pontszámban a statisztika a jobb, de $$z_{\text{logika}}=\frac{78-70}5='
         r'1{,}6,\qquad z_{\text{statisztika}}=\frac{85-80}{10}=0{,}5.$$ A csoportjához képest a logikai teszt '
         r'sikerült jobban.</p>', hid="pelda-standardizalt"),
   doboz("csapda", "Véd Vilmos csapda — szórás vagy szórásnégyzet?",
         r'<p>Vilmos szerint a lisszaboni hőmérsékletek „szórása ' + tized(ml["var"], 1) + r' °C²”. Két hiba egyszerre: '
         r'a ' + tized(ml["var"], 1) + r' a szórásnégyzet (nem vont gyököt), és a szórás mértékegysége °C, nem °C². A '
         r'szórás $\sqrt{' + K(ml["var"], 1) + r'}\approx' + K(ml["sz"], 1) + r'$ °C.</p>'),
   kviz('Két adatsor: $A$: 10, 10, 10, 10 és $B$: 0, 5, 15, 20. Mi igaz?',
        ['Az átlaguk azonos, de $B$ szórása nagyobb.', 'Az átlaguk és a szórásuk is azonos.', '$B$ átlaga nagyobb.',
         '$A$ szórása nagyobb.'], 0,
        jo="✔ Mindkét átlag 10. Az $A$ adatai nem térnek el az átlagtól (szórás 0), a $B$-éi nagyon.",
        nem="✘ Az átlag mindkettőnél 10 — de az azonos átlag nem jelent azonos adatokat. $A$ szórása 0, $B$-é nagy."),
 ]),
 ("Adatlabor", [
   '<p class="lead">Válassz egy valós adatsort, vagy írd be a sajátodat (például az osztálytársak magasságát), és '
   'figyeld, hogyan változnak a mutatók. Egy kiugró adat — írj be egy 100-at! — az átlagot és a szórást elhúzza, a '
   'mediánt alig.</p>',
   SVG_LAB,
   FORRAS("openmeteo", "jokic"),
   doboz("erdekesseg", "Táblázatkezelő-sarok",
         '<p>Ugyanezek a mutatók egy táblázatkezelőben (Excel, LibreOffice Calc, Google Táblázatok) egy-egy függvénnyel '
         'számolhatók, például <span class="kbd">=ÁTLAG(A1:A12)</span>:</p>' + FUGG_TABLA
         + '<p>A <span class="kbd">VAR.S</span> és a <span class="kbd">STDEV.S</span> típusú függvények $n$ helyett '
           '$n-1$-gyel osztanak — ez a mintából becslő, „korrigált” változat, amelyet most nem használunk.</p>'),
   NEHEZ(2, "hiányzó adat visszafelé az átlagból"),
   NEHEZ(3, "két adatsor összevetése középértékkel és szórással"),
   GY("#alap-6", "A 6–10", "#kozep-4", "K 4–7"),
 ]),
 ("🧾 Gyorsismétlő", [
   TABLA(["mutató", "kiszámítás", "mit mond?"], [
       ["módusz", "a leggyakoribb érték", "a „divatos” érték — kategóriára is"],
       ["medián", "a rendezett adatsor közepe", "fele alatta, fele fölötte; a kiugró érték alig mozdítja"],
       ["átlag", "$\\bar x=\\dfrac{x_1+\\ldots+x_n}{n}$", "a „kiegyenlített” érték; a kiugró érték elhúzza"],
       ["terjedelem", "legnagyobb − legkisebb", "a teljes szélesség"],
       ["kvartilisek", "a két fél mediánja", "a középső 50% helye: $[Q_1;\\,Q_3]$"],
       ["szórás", "$\\sigma=\\sqrt{\\dfrac{(x_1-\\bar x)^2+\\ldots+(x_n-\\bar x)^2}{n}}$",
        "átlagosan mennyire térnek el az adatok az átlagtól"],
       ["standardizált érték", "$z=\\dfrac{x-\\bar x}{\\sigma}$", "hány szórásnyira van az átlagtól"]]),
   brief('<b>Mr. Szürreál:</b> Elfogytak a grafikonjaim. <b>Nagol:</b> A bizottság utolsó kérése: a kadétok saját '
         'adatokkal feleljenek — kérdés, adatgyűjtés, táblázat, diagram, mutatók, értelmezés. <b>Véd Vilmos:</b> Ez a '
         '<a href="terepkuldetes.html">terepküldetés</a>, a végső meghallgatás. És utána? Az utolsó ítéletet nem az '
         'I.V.H. mondja ki, hanem a vizsgabizottság. Arra már készen álltok.', outro=True),
 ]),
]

lapok = [
 lap(**T, fajl="tananyag-adatok.html",
     cim="Adatokból kép — sokaság, minta, gyakoriság, diagram",
     alcim="Sokaság, ismérv, minta és mintavétel, gyakorisági táblázat, négy diagramtípus és a félrevezető grafikon.",
     chip=KUL + " · 6/7", szakaszok=B1,
     elozo=("feladatok-valoszinuseg.html", "Zsoldos-lista — Valószínűség"),
     kovetkezo=("tananyag-statisztikai-mutatok.html", "Statisztikai mutatók")),
 lap(**T, fajl="tananyag-statisztikai-mutatok.html",
     cim="Egy szám az egész helyett — középértékek és szóródás",
     alcim="Módusz, medián, átlag, terjedelem, kvartilisek, dobozdiagram, szórás és standardizált érték — adatlaborral "
           "és a statisztika gyorsismétlőjével.",
     chip=KUL + " · 7/7", szakaszok=B2,
     elozo=("tananyag-adatok.html", "Adatokból kép"),
     kovetkezo=(FA, "Zsoldos-lista — Statisztika")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
