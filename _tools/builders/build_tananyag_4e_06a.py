# -*- coding: utf-8 -*-
"""4e/06 — A blokk: valoszinuseg. A1 esemenyek · A2 a valoszinuseg fogalma · A3 feltételes valoszinuseg ·
A4 binomialis valoszinuseg · A5 valoszinusegi valtozo (+ 🧾 Gyorsismetlo).
Kuldetes: A Tuleles Eselyei (I.V.H.-meghallgatas). Mr. Szurreal (vad) vs. Ved Vilmos (vedelem), Nagol szakerto.
Specifikacio: projektek/szvetkomatek/4e/narrativa_06-valoszinuseg-statisztika.md
Valos adatok: adat_4e_06.py (forrasokkal). Tiltott adatok: tiltott_4e_06 (= a 05-os kombinatorika-ellenorzo
helyzetei) — lent ellenorizve. 06-os felmero nincs."""
import sys, os
from fractions import Fraction as Fr
from itertools import product, combinations
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_venn
from abra_stat import svg_oszlop, svg_mozaik, svg_bernoulli_fa, svg_szimulacio, ezres, tized
import adat_4e_06 as ADAT
import tiltott
TILT = tiltott.modul("tiltott_4e_06")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)

T = dict(tagozat="4e", mappa="06-valoszinuseg-statisztika", temakor="Valószínűség és statisztika")
KUL = "A Túlélés Esélyei"
FA = "feladatok-valoszinuseg.html"
KOMB = "../05-kombinatorika/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(FA + k_h, k_c, FA + n_h, n_c, tagozat="4e")


def NEHEZ(n, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FA}#nehez-{n}">Zsoldos-lista, nehéz {n}</a>.</p>')


def TABLA(fejlec, sorok, osztaly="tt-table"):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="{osztaly}">{"<tr>" + th + "</tr>" if any(fejlec) else ""}{tr}</table></div>'


def FORRAS(*kulcsok):
    reszek = []
    for k in kulcsok:
        cim, url = ADAT.FORRAS[k]
        reszek.append(f'<a href="{url}">{cim}</a>' if url else cim)
    return '<p class="cap">Forrás: ' + " · ".join(reszek) + '</p>'


def K(szam, jegy=3):
    """KaTeX-be illő tizedesvesszős szám: 0.727 → 0{,}727"""
    return tized(szam, jegy).replace(",", "{,}")


def E3(n):
    """KaTeX-be illő ezres tagolás: 15380937 → 15\\,380\\,937"""
    return ezres(n).replace(" ", "\\,")


# ---------------------------------------------------------------- önteszt: minden szám képlettel ÉS felsorolással
E = []


def chk(nev, a, b):
    if a != b:
        E.append((nev, a, b))


def kozel(nev, a, b, tur=5e-4):
    if abs(a - b) > tur:
        E.append((nev, a, b))


KOCKA = range(1, 7)
KETKOCKA = list(product(KOCKA, KOCKA))
# A1
chk("A1 két érme", len(list(product("FI", repeat=2))), 4)
chk("A1 két kocka", len(KETKOCKA), 36)
A_ = {2, 4, 6}; B_ = {5, 6}; OM = set(KOCKA)
chk("A1 unió", A_ | B_, {2, 4, 5, 6}); chk("A1 metszet", A_ & B_, {6})
chk("A1 ellentett", OM - A_, {1, 3, 5}); chk("A1 különbség", A_ - B_, {2, 4})
chk("A1 De Morgan", OM - (A_ | B_), (OM - A_) & (OM - B_)); chk("A1 De Morgan2", OM - (A_ | B_), {1, 3})
# A2
chk("A2 összeg 7", Fr(sum(1 for a, b in KETKOCKA if a + b == 7), 36), Fr(1, 6))
chk("A2 összeg 2", Fr(sum(1 for a, b in KETKOCKA if a + b == 2), 36), Fr(1, 36))
chk("A2 nem dupla", 1 - Fr(sum(1 for a, b in KETKOCKA if a == b), 36), Fr(5, 6))
chk("A2 1 fej", Fr(sum(1 for p in product("FI", repeat=2) if p.count("F") == 1), 4), Fr(1, 2))
PAKLI = [(sz, e) for sz in ("kőr", "káró", "treff", "pikk") for e in range(13)]   # e == 12: király
chk("A2 király vagy kőr", Fr(sum(1 for sz, e in PAKLI if e == 12 or sz == "kőr"), 52), Fr(4, 13))
chk("A2 kosár/foci", Fr(4, 10) + Fr(5, 10) - Fr(2, 10), Fr(7, 10))
GOLYO = ["p"] * 5 + ["f"] * 3
parok = list(combinations(range(8), 2))
chk("A2 két piros", Fr(sum(1 for i, j in parok if GOLYO[i] == GOLYO[j] == "p"), len(parok)), Fr(5, 14))
chk("A2 egy piros", Fr(sum(1 for i, j in parok if {GOLYO[i], GOLYO[j]} == {"p", "f"}), len(parok)), Fr(15, 28))
chk("A2 két fehér", Fr(sum(1 for i, j in parok if GOLYO[i] == GOLYO[j] == "f"), len(parok)), Fr(3, 28))
chk("A2 lottó", comb(39, 7), 15380937)
PF = ADAT.PENZFELDOBAS
chk("A2 történeti", [(p["ki"], p["dobas"], p["fej"]) for p in PF],
    [("Buffon", 4040, 2048), ("Kerrich", 10000, 5067), ("Pearson", 24000, 12012)])
SZ = ADAT.SZULETES
fiu_arany = {ev: SZ["RS_M"][ev] / SZ["RS_T"][ev] for ev in sorted(SZ["RS_T"])}
for ev in fiu_arany:
    chk(f"A2 szül. {ev}", SZ["RS_M"][ev] + SZ["RS_F"][ev], SZ["RS_T"][ev])
chk("A2 fiú 2024", tized(fiu_arany[2024], 3), "0,516")
ESO = sum(ADAT.IDOJARAS_2024["szabadka"]["esos_nap_havonta"])
chk("A2 esős nap", (ESO, ADAT.IDOJARAS_2024["szabadka"]["napok"]), (79, 366))
# A3
TI = ADAT.TITANIC
no_t, no_n = TI["nem"]["no"]; fe_t, fe_n = TI["nem"]["ferfi"]
chk("A3 Titanic összeg", no_t + no_n + fe_t + fe_n, 1309)
chk("A3 túlélt", no_t + fe_t, 500)
kozel("A3 P(túlélt)", 500 / 1309, 0.382); kozel("A3 P(nő)", 466 / 1309, 0.356); kozel("A3 P(nő∩t)", 339 / 1309, 0.259)
kozel("A3 P(t|nő)", no_t / (no_t + no_n), 0.727); kozel("A3 P(t|férfi)", fe_t / (fe_t + fe_n), 0.191)
kozel("A3 P(nő|t)", no_t / 500, 0.678)
chk("A3 kocka páros | ≥4", Fr(len({4, 5, 6} & A_), 3), Fr(2, 3))
chk("A3 független páros, ≤2", Fr(len(A_ & {1, 2}), 6), Fr(1, 2) * Fr(1, 3))
SG = ADAT.SZAMITOGEP["szerbia"]
p_ism, p_ism_no, p_ism_fe = SG["osszes"][1] / SG["osszes"][0], SG["no"][1] / SG["no"][0], SG["ferfi"][1] / SG["ferfi"][0]
kozel("A3 ismeri", p_ism, 0.457); kozel("A3 ismeri|nő", p_ism_no, 0.466); kozel("A3 ismeri|férfi", p_ism_fe, 0.448)
chk("A3 SG összeg", SG["no"][0] + SG["ferfi"][0], SG["osszes"][0])
chk("A3 riasztó", round(1 - 0.1 * 0.2 * 0.3, 10), 0.994)
kozel("A3 de Méré 1", 1 - (5 / 6) ** 4, 0.518); kozel("A3 de Méré 2", 1 - (35 / 36) ** 24, 0.491)
chk("A3 kizáró/0.12", round(0.3 * 0.4, 10), 0.12)
# A4
p = Fr(4, 5)
BIN = [comb(5, k) * p ** k * (1 - p) ** (5 - k) for k in range(6)]
chk("A4 Jokić 0.800", [j["bunteto"] for j in ADAT.JOKIC if j["szezon"] == "2024–25"], [0.8])
chk("A4 P5(4)", BIN[4], Fr(4096, 10000))
chk("A4 felsorolás", sum(Fr(4, 5) ** s.count("S") * Fr(1, 5) ** s.count("K") for s in product("SK", repeat=5)
                        if s.count("S") == 4), BIN[4])
chk("A4 összeg", sum(BIN), 1)
chk("A4 3-ból 2", 3 * Fr(4, 5) ** 2 * Fr(1, 5), Fr(384, 1000))
chk("A4 legalább 4", BIN[4] + BIN[5], Fr(73728, 100000))
chk("A4 hat dobás két hatos", comb(6, 2) * Fr(1, 6) ** 2 * Fr(5, 6) ** 4, Fr(9375, 46656))
kozel("A4 fiú 3-ból", 1 - (1 - 0.516) ** 3, 0.887)
chk("A4 10-ből 6 hatos", comb(10, 6) * Fr(1, 6) ** 6 * Fr(5, 6) ** 4, Fr(131250, 60466176))
kozel("A4 10-ből 6 ≈", 131250 / 60466176, 0.0022, 5e-5)
chk("A4 három érme 2 fej", Fr(sum(1 for s in product("FI", repeat=3) if s.count("F") == 2), 8), Fr(3, 8))
kozel("A4 legalább egy hatos", 1 - (5 / 6) ** 6, 0.665)
# A5
chk("A5 két érme E", 0 * Fr(1, 4) + 1 * Fr(1, 2) + 2 * Fr(1, 4), 1)
chk("A5 kocka E", Fr(sum(KOCKA), 6), Fr(7, 2))
HZ = ADAT.HAZTARTAS["szabadka"]
chk("A5 háztartás összeg", sum(HZ["tag_1_5_6plusz"]), HZ["ossz"])
szorzat = sum((i + 1) * f for i, f in enumerate(HZ["tag_1_5_6plusz"]))
chk("A5 háztartás szorzatösszeg", szorzat, 121455)
kozel("A5 háztartás E", szorzat / HZ["ossz"], 2.31, 5e-3)
chk("A5 hivatalos átlag", HZ["atlag"], 2.33)
chk("A5 ajánlat", 400 * Fr(1, 6) - 100 * Fr(5, 6), Fr(-50, 3))
SA = [(30, Fr(1, 2)), (10, Fr(3, 10)), (-20, Fr(1, 5))]
SB = [(60, Fr(3, 10)), (0, Fr(1, 2)), (-30, Fr(1, 5))]
EA, EB = sum(x * q for x, q in SA), sum(x * q for x, q in SB)
chk("A5 E(A)", EA, 14); chk("A5 E(B)", EB, 12)
chk("A5 D2(A)", sum((x - EA) ** 2 * q for x, q in SA), 364)
chk("A5 D2(B)", sum((x - EB) ** 2 * q for x, q in SB), 1116)
chk("A5 sima átlag A", Fr(30 + 10 - 20, 3), Fr(20, 3)); chk("A5 sima átlag B", Fr(60 + 0 - 30, 3), 10)
chk("A5 játék 2", (40 * Fr(1, 2) - 20 * Fr(1, 2), (40 - 10) ** 2 * Fr(1, 2) + (-20 - 10) ** 2 * Fr(1, 2)), (10, 900))
chk("A5 kvíz p", Fr(1) - Fr(2, 10) - Fr(5, 10), Fr(3, 10))

WEB = [("erme", 2), ("kocka", 2), ("kartya", ("francia", 1, 1)), ("golyo", (5, 3, 2)), ("komb", (8, 2)),
       ("komb", (5, 2)), ("komb", (39, 7)), ("bernoulli", (3, "4/5", 2)), ("bernoulli", (5, "4/5", 4)),
       ("bernoulli", (6, "1/6", 2)), ("bernoulli", (10, "1/6", 6)), ("bernoulli", (3, "0.516", 1)),
       ("erme", 3), ("tabla", "titanic"), ("tabla", "szamitogep-srb"), ("adatsor", "haztartas-szabadka")]
E += TILT.ellenoriz(WEB)
assert not E, E
print("önteszt: OK")


# ---------------------------------------------------------------- ábrák
def _svg(w, h, leiras, belso):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, system-ui, sans-serif">\n' + "\n".join(belso)
            + "\n</svg>")


def svg_kizaro():
    ki = ['  <rect x="6" y="6" width="188" height="128" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
          '  <text x="182" y="126" font-size="12" font-style="italic" fill="#475569" text-anchor="end">Ω</text>',
          '  <circle cx="62" cy="68" r="36" fill="#f59e0b" fill-opacity=".30" stroke="#047857" stroke-width="2"/>',
          '  <circle cx="140" cy="68" r="36" fill="#f59e0b" fill-opacity=".30" stroke="#3b82f6" stroke-width="2"/>',
          '  <text x="62" y="26" font-size="13" font-style="italic" fill="#047857" font-weight="600" '
          'text-anchor="middle">C</text>',
          '  <text x="140" y="26" font-size="13" font-style="italic" fill="#3b82f6" font-weight="600" '
          'text-anchor="middle">D</text>']
    return _svg(200, 140, "Két kizáró esemény: a két halmaznak nincs közös része", ki)


def VENN(svg, felirat):
    return f'<div class="vbox">{svg}<p class="cap">{felirat}</p></div>'


VENNEK = ('<div class="venn">'
          + VENN(svg_venn(("A", "B"), ("A", "B", "AB"), "Ω", 200, 140, "Az A és B uniója"), "$A\\cup B$ — A vagy B")
          + VENN(svg_venn(("A", "B"), ("AB",), "Ω", 200, 140, "Az A és B metszete"), "$A\\cap B$ — A és B")
          + VENN(svg_venn(("A", "B"), ("B", "-"), "Ω", 200, 140, "Az A ellentettje"), "$\\overline{A}$ — nem A")
          + VENN(svg_venn(("A", "B"), ("A",), "Ω", 200, 140, "Az A és B különbsége"), "$A\\setminus B$ — A, de nem B")
          + VENN(svg_kizaro(), "kizárók: $C\\cap D=\\emptyset$")
          + '</div>')


def kocka_tabla(kiemel=None, osszeg=True):
    fej = '<tr><th>piros \\ kék</th>' + "".join(f"<th>{j}</th>" for j in KOCKA) + "</tr>"
    sorok = ""
    for i in KOCKA:
        cellak = ""
        for j in KOCKA:
            tartalom = str(i + j) if osszeg else f"{i};{j}"
            cls = ' class="res"' if kiemel and kiemel(i, j) else ""
            cellak += f"<td{cls}>{tartalom}</td>"
        sorok += f"<tr><th>{i}</th>{cellak}</tr>"
    return f'<div class="tblwrap"><table class="tt-table">{fej}{sorok}</table></div>'


SVG_SZIM = svg_szimulacio(
    kezdo_dobas=200, mag=2026,
    felirat="Nyomd meg a gombokat! A kék görbe a fej (vagy a hatos) relatív gyakorisága az addigi dobások után, a "
            "piros szaggatott vonal a klasszikus valószínűség. A kezdőkép 200 érmedobás; kockára váltva újraindul.")

SVG_MOZAIK = svg_mozaik([("nők", TI["nem"]["no"]), ("férfiak", TI["nem"]["ferfi"])], ("túlélt", "nem élte túl"),
                        leiras="Mozaikábra: a Titanic utasai nem és túlélés szerint. A nők oszlopa keskenyebb, de "
                               "nagyobb része zöld (túlélt), a férfiaké szélesebb, kisebb zöld résszel.")

SVG_FA3 = svg_bernoulli_fa(leiras="Fadiagram három büntetőhöz: minden elágazásnál siker (0,8) vagy kudarc (0,2); a "
                                  "pontosan két sikert tartalmazó három ág kiemelve")

SVG_JOKIC = svg_oszlop([str(k) for k in range(6)], [float(b) for b in BIN], ymax=0.5, lepes=0.1,
                       ertek_cimkek=[tized(float(b), 4) for b in BIN], kiemel=(4,),
                       yfelirat="valószínűség", xfelirat="a bedobott büntetők száma (k) öt dobásból",
                       leiras="Oszlopdiagram: öt büntetőből pontosan k bedobás valószínűsége, ha p = 0,8. A legmagasabb "
                              "oszlop a k = 4, 0,4096")

SVG_KETERME = svg_oszlop(["0", "1", "2"], [0.25, 0.5, 0.25], ymax=0.6, lepes=0.2, ertek_cimkek=["1/4", "1/2", "1/4"],
                         yfelirat="P(X = x)", xfelirat="a fejek száma (x)", w=320, h=220,
                         leiras="Oszlopdiagram: két érmedobásnál a fejek számának eloszlása: 0 fej 1/4, 1 fej 1/2, "
                                "2 fej 1/4")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál</b> (I.V.H.): Megnyitom a meghallgatást. A 4. évfolyam érettségije véletlen kísérlet, '
         'kimenetele: bukás. Javaslom a teljes évfolyam megmetszését. <b>Véd Vilmos</b> (a védelem): Tiltakozom! Előbb '
         'mondja meg, milyen kimenetelek vannak egyáltalán. Itt van például két érme. 🌮 <i>Burek-matek:</i> 0, 1 vagy '
         '2 fej — három kimenetel, igaz? <b>Nagol</b> (szakértő): Nem. Ha az első érme fej és a második írás, az más, '
         'mint fordítva. Négy kimenetel van: FF, FI, IF, II. <b>SZVETI</b> (jegyzőkönyv): Rögzítve. A védő az első '
         'percben tévedett.'),
 ]),
 ("Kísérlet és kimenetel", [
   '<p class="lead">A valószínűségszámítás olyan helyzetekről szól, amelyeknek az eredményét előre nem tudjuk — de azt '
   'igen, hogy <b>mi történhet</b>.</p>',
   doboz("definicio", "Véletlen kísérlet, kimenetel",
         '<p><b>Véletlen kísérlet</b> minden olyan megfigyelés vagy cselekvés, amely (legalább elvben) azonos '
         'feltételek mellett akárhányszor megismételhető, és amelynek az eredménye előre nem jósolható meg biztosan: '
         'érmedobás, kockadobás, húzás egy dobozból, egy vizsga. A kísérlet lehetséges eredményei a '
         '<b>kimenetelek</b> (más néven elemi események).</p>', hid="def-kiserlet"),
   doboz("definicio", "Eseménytér",
         r'<p>Egy kísérlet összes lehetséges kimenetelének halmaza az <b>eseménytér</b>, jele $\Omega$ (omega).</p>',
         hid="def-esemenyter"),
   doboz("pelda", "I.V.H. Akták — négy eseménytér",
         r'<p>Érmedobás: $\Omega=\{F;\ I\}$ (fej, írás). Kockadobás: $\Omega=\{1;\ 2;\ 3;\ 4;\ 5;\ 6\}$. Két érme: '
         r'$\Omega=\{FF;\ FI;\ IF;\ II\}$ — az első betű az első érme, a második a második. Két kocka (egy piros és egy '
         r'kék): a kimenetelek rendezett számpárok, $6\cdot6=36$ darab. Az alábbi táblázat minden cellája egy '
         r'kimenetel; a cellában a két dobott szám áll (piros; kék):</p>' + kocka_tabla(osszeg=False),
         hid="pelda-ket-kocka"),
   doboz("csapda", "Véd Vilmos csapda — összevont kimenetelek",
         '<p>Vilmos két érménél három kimenetelt látott: 0, 1 vagy 2 fej. Ezek valóban a lehetséges <i>fejszámok</i>, '
         'de nem egyenrangúak: az „1 fej” két kimenetelből áll, FI-ből és IF-ből. Ha a két érmét megkülönböztetjük '
         '(például egy régi és egy új pénzérme), rögtön látszik. A következő leckében ebből az összevonásból lesz a '
         'hibás $\\frac13$.</p>'),
 ]),
 ("Események", [
   '<p class="lead">Egy kísérletnél általában nem egyetlen kimenetel érdekel, hanem egy kérdés: páros számot dobtunk-e, '
   'átment-e legalább egy kadét.</p>',
   doboz("definicio", "Esemény, biztos és lehetetlen esemény",
         r'<p><b>Esemény</b> az eseménytér bármely részhalmaza. Az $A$ esemény <b>bekövetkezik</b>, ha a kísérlet '
         r'kimenetele $A$ egyik eleme. Két szélső eset: a <b>biztos esemény</b> maga $\Omega$ (mindig bekövetkezik), a '
         r'<b>lehetetlen esemény</b> az üres halmaz, $\emptyset$ (soha nem következik be).</p>', hid="def-esemeny"),
   doboz("pelda", "I.V.H. Akták — események egy kockadobásnál",
         r'<p>$A$ = „páros számot dobunk” $=\{2;\ 4;\ 6\}$ · $B$ = „legalább 5-öt dobunk” $=\{5;\ 6\}$ · '
         r'$C$ = „legfeljebb 6-ot dobunk” $=\Omega$, biztos esemény · $D$ = „7-est dobunk” $=\emptyset$, lehetetlen '
         r'esemény.</p><p>Ha a dobás 6, akkor $A$ is és $B$ is bekövetkezett; ha 5, akkor csak $B$; ha 3, akkor egyik '
         r'sem.</p>'),
   kviz('Egy kockával egyszer dobunk. Melyik esemény biztos?',
        ['legfeljebb 6-ot dobunk', 'nem dobunk 1-est', 'legalább 2-t dobunk', '7-nél kisebb prímszámot dobunk'], 0,
        jo="✔ Minden kimenetel (1, 2, …, 6) legfeljebb 6 — ez az egész eseménytér, $\\Omega$.",
        nem="✘ A biztos esemény nem „nagyon valószínű”, hanem MINDEN kimenetelnél bekövetkezik. Az 1-es dobásnál a "
            "„nem dobunk 1-est” és a „legalább 2” nem teljesül, a prímes esemény pedig 1-nél, 4-nél és 6-nál sem. "
            "Csak a „legfeljebb 6” biztos."),
 ]),
 ("Műveletek eseményekkel", [
   '<p class="lead">Mivel az események halmazok, a halmazműveletekkel újabb eseményeket képezhetünk — és mindegyiknek '
   'egy hétköznapi kötőszó felel meg.</p>',
   VENNEK,
   TABLA(["művelet", "jelölés", "jelentés", "a kockás példában"], [
       ["unió", "$A\\cup B$", "$A$ vagy $B$ (vagy mindkettő) bekövetkezik", "$\\{2;\\ 4;\\ 5;\\ 6\\}$"],
       ["metszet", "$A\\cap B$", "$A$ és $B$ is bekövetkezik", "$\\{6\\}$"],
       ["ellentett", "$\\overline{A}$", "$A$ nem következik be", "$\\{1;\\ 3;\\ 5\\}$"],
       ["különbség", "$A\\setminus B$", "$A$ bekövetkezik, $B$ nem", "$\\{2;\\ 4\\}$"]]),
   doboz("definicio", "Ellentett esemény",
         r'<p>Az $A$ esemény <b>ellentettje</b>, $\overline{A}$, pontosan akkor következik be, amikor $A$ nem: '
         r'$\overline{A}=\Omega\setminus A$. Egy esemény és az ellentettje egyszerre nem következhet be, de az egyikük '
         r'mindig: $A\cap\overline{A}=\emptyset$ és $A\cup\overline{A}=\Omega$.</p>', hid="def-ellentett"),
   doboz("definicio", "Kizáró események",
         r'<p>Két esemény <b>kizárja egymást</b>, ha nem következhetnek be egyszerre: $A\cap B=\emptyset$. Például '
         r'kockadobásnál $C$ = „1-est dobunk” és $D$ = „6-ost dobunk”.</p>', hid="def-kizaro"),
   doboz("tetel", "A „legalább egy” ellentettje",
         r'<p>$$\overline{A\cup B}=\overline{A}\cap\overline{B},\qquad \overline{A\cap B}=\overline{A}\cup\overline{B}.$$ '
         r'Szavakkal: „nem igaz, hogy $A$ vagy $B$” ugyanaz, mint „sem $A$, sem $B$”; „nem igaz, hogy $A$ és $B$ is” '
         r'ugyanaz, mint „legalább az egyik nem”. A kockás példában $\overline{A\cup B}=\{1;\ 3\}$, és valóban '
         r'$\overline{A}\cap\overline{B}=\{1;\ 3;\ 5\}\cap\{1;\ 2;\ 3;\ 4\}=\{1;\ 3\}$. (Ezek a De Morgan-azonosságok; a '
         r'halmazokra vonatkozó változatukat az <a href="../../1e/01-logika-halmazok-fuggvenyek/'
         r'tananyag-halmazmuveletek.html#muveletek">1e halmazműveleteinél</a> találod.)</p>', hid="tetel-de-morgan"),
   doboz("csapda", "Véd Vilmos csapda — kizáró nem ugyanaz, mint ellentett",
         '<p>Az „1-est dobunk” és a „6-ost dobunk” esemény kizárja egymást, de nem ellentettek: ha 3-ast dobunk, egyik '
         'sem következik be. Az ellentett párnak a kizáráson túl <b>ki is kell töltenie</b> az eseményteret. Egy másik '
         'gyakori hiba a köznapi „vagy”: a matematikában a „vagy” megengedő, az $A\\cup B$ akkor is bekövetkezik, ha '
         'mindkét esemény bekövetkezik.</p>'),
   kviz('Kockadobásnál $A$ = „páros számot dobunk”, $B$ = „1-est vagy 3-ast dobunk”. Mi igaz?',
        ['kizárják egymást, de nem ellentettek', 'ellentett események', 'nem zárják ki egymást',
         'ugyanaz a két esemény'], 0,
        jo="✔ $A=\\{2;4;6\\}$ és $B=\\{1;3\\}$ közös eleme nincs, tehát kizárók. Az 5-ös dobásnál viszont egyik sem "
           "következik be, így nem ellentettek.",
        nem="✘ A két halmaznak nincs közös eleme — kizárók. Ellentettek akkor lennének, ha együtt kiadnák az egész "
            "eseményteret, de az 5 kimarad."),
 ]),
 ("Szövegből jelölés — és vissza", [
   r'<p class="lead">Három kadét — Ádám, Bea és Csaba — érettségizik. Jelölje $A$, $B$ és $C$ azt az eseményt, hogy '
   r'Ádám, Bea, illetve Csaba átmegy. A szöveges állításokat a műveletekkel írhatjuk le:</p>',
   TABLA(["állítás", "jelölés"], [
       ["mindhárman átmennek", "$A\\cap B\\cap C$"],
       ["egyikük sem megy át", "$\\overline{A}\\cap\\overline{B}\\cap\\overline{C}$"],
       ["legalább egyikük átmegy", "$A\\cup B\\cup C$"],
       ["pontosan egyikük megy át",
        "$(A\\cap\\overline{B}\\cap\\overline{C})\\cup(\\overline{A}\\cap B\\cap\\overline{C})\\cup"
        "(\\overline{A}\\cap\\overline{B}\\cap C)$"],
       ["legfeljebb ketten mennek át", "$\\overline{A\\cap B\\cap C}$"]]),
   doboz("pelda", "I.V.H. Akták — visszafelé",
         r'<p>Mit jelent $A\cap\overline{B}$? Ádám átmegy, Bea nem — Csabáról nem állít semmit.</p>'
         r'<p>És $\overline{A\cup B\cup C}$? „Nem igaz, hogy legalább egyikük átmegy” — vagyis egyikük sem. Ez ugyanaz, '
         r'mint $\overline{A}\cap\overline{B}\cap\overline{C}$: a De Morgan-azonosság három eseményre.</p>',
         hid="pelda-harom-kadet"),
   GY("#alap-1", "A 1–3", "#kozep-1", "K 1–2"),
   brief('<b>Mr. Szürreál:</b> Szép definíciók. A bizottság azonban számot kér: <i>mekkora</i> az esély? <b>Véd '
         'Vilmos:</b> Számot? Azt tudok. Hozom a pénzérméimet.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
tort_sorok = [[p["ki"], ezres(p["dobas"]), ezres(p["fej"]), "$" + K(p["fej"] / p["dobas"], 4) + "$"] for p in PF]
szul_sorok = [[str(ev), ezres(SZ["RS_T"][ev]), ezres(SZ["RS_M"][ev]), "$" + K(fiu_arany[ev], 3) + "$"]
              for ev in sorted(SZ["RS_T"])]

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál:</b> Az I.V.H. ezer idővonalat szimulált. A kadétok 997-ben elbuknak. <b>Véd Vilmos:</b> '
         'Szimulálni én is tudok! Fej vagy írás — dobjunk. Sokat. <b>Nagol:</b> Jó ötlet, csak figyeljük meg, mi '
         'rajzolódik ki a sok dobás után. <b>SZVETI:</b> A védő pénzérméje egyébként burekzsíros. Jegyzőkönyvbe '
         'véve.'),
 ]),
 ("Sok dobás után", [
   '<p class="lead">Egy egyszerű kísérlet: az osztályban mindenki tízszer feldob egy pénzérmét, és összesítjük a fejek '
   'számát. Egy tanuló tíz dobásából bármi kijöhet — 3 fej, 7 fej —, az osztály néhány száz dobásánál viszont a fejek '
   'aránya meglepően közel lesz a feléhez. Próbáld ki a szimulátorral is!</p>',
   doboz("definicio", "Gyakoriság és relatív gyakoriság",
         r'<p>Ha egy kísérletet $n$-szer végzünk el, és közben az $A$ esemény $k$-szor következik be, akkor $k$ az $A$ '
         r'<b>gyakorisága</b>, a $\dfrac kn$ hányados pedig a <b>relatív gyakorisága</b>. Nyilván '
         r'$0\le\dfrac kn\le1$.</p>', hid="def-relativ-gyakorisag"),
   SVG_SZIM,
   '<p>Nem mi vagyunk az elsők, akik ezt kipróbálták:</p>',
   TABLA(["ki dobott", "dobások", "fej", "relatív gyakoriság"], tort_sorok),
   FORRAS("penz"),
   doboz("definicio", "A valószínűség statisztikai értelmezése",
         r'<p>Ha egy kísérlet sokszori ismétlésekor egy esemény relatív gyakorisága egy szám körül ingadozik, és az '
         r'ismétlések számának növelésével egyre kevésbé tér el tőle, akkor ezt a számot az esemény '
         r'<b>valószínűségének</b> nevezzük. Jele $P(A)$ (a <i>probabilitas</i>, valószínűség szóból).</p>',
         hid="def-statisztikai-valoszinuseg"),
   doboz("pelda", "I.V.H. Akták — fiú vagy lány?",
         '<p>Szerbiában évente 60–65 ezer gyermek születik. Az újszülöttek között a fiúk aránya évről évre:</p>'
         + TABLA(["év", "született", "ebből fiú", "a fiúk aránya"], szul_sorok) + FORRAS("eurostat")
         + '<p>Hat év alatt a fiúk aránya $0{,}513$ és $0{,}516$ között mozog. Annak a valószínűsége, hogy egy '
           'Szerbiában született újszülött fiú, nagyjából $0{,}515$ — nem pontosan $\\frac12$, hanem kicsit több (ez '
           'világszerte így van). Hasonlóan: 2024-ben Szabadkán 366 napból 79-en esett legalább 1 mm csapadék, a '
           'relatív gyakoriság $\\frac{79}{366}\\approx0{,}216$.</p>', hid="pelda-szuletesek"),
   doboz("erdekesseg", "Az érme nem emlékszik",
         '<p>Ha öt fej jött egymás után, a hatodik dobásnál is $\\frac12$ a fej valószínűsége. A relatív gyakoriság nem '
         'azért közelít $\\frac12$-hez, mert a véletlen „kiegyenlít”, hanem mert a sok új dobás mellett a korai eltérés '
         'egyre kisebb súlyú. A <i>szerencsejátékos tévedése</i> ennek az ellenkezőjét hiszi: hogy egy hosszú '
         'fejsorozat után „már jár” az írás.</p>'),
   kviz('Egy szabályos érmével ötször egymás után fejet dobtunk. Mekkora a valószínűsége, hogy a hatodik dobás is fej?',
        ['$\\frac12$', 'kisebb, mint $\\frac12$, mert most már az írás jön', 'nagyobb, mint $\\frac12$, mert '
         '„fejsorozat” van', '$\\frac1{64}$'], 0,
        jo="✔ Az érme nem emlékszik: minden dobásnál $\\frac12$. (Az $\\frac1{64}$ a hat fejből álló sorozat "
           "valószínűsége lett volna a dobások ELŐTT.)",
        nem="✘ A dobások függetlenek egymástól, az érme nem „tartozik” írással. A hatodik dobás fej valószínűsége "
            "$\\frac12$."),
 ]),
 ("A klasszikus valószínűség", [
   '<p class="lead">Sokszor kísérletezés nélkül is tudjuk a valószínűséget: ha a kimenetelek <b>szimmetrikusak</b> — '
   'egyik sem kitüntetett —, akkor mindegyik ugyanakkora eséllyel jön ki.</p>',
   doboz("tetel", "A klasszikus valószínűség",
         r'<p>Ha a kísérletnek véges sok, $n$ kimenetele van, és ezek <b>egyformán valószínűek</b>, akkor egy $A$ '
         r'esemény valószínűsége $$P(A)=\frac{\text{az }A\text{ szempontjából kedvező kimenetelek száma}}'
         r'{\text{az összes kimenetel száma}}=\frac kn.$$</p>', hid="tetel-klasszikus"),
   doboz("pelda", "I.V.H. Akták — két kocka",
         r'<p>Két kockával dobunk. Mekkora a valószínűsége, hogy a dobott számok összege 7? A 36 kimenetel egyformán '
         r'valószínű; a táblázat cellájában most a két szám összege áll, a 7-esek kiemelve:</p>'
         + kocka_tabla(kiemel=lambda i, j: i + j == 7)
         + r'<p>Az összeg hat cellában 7: (1;6), (2;5), (3;4), (4;3), (5;2), (6;1). Tehát '
           r'$$P(\text{összeg}=7)=\frac6{36}=\frac16.$$ Az összeg 2 viszont csak egyféleképpen jöhet ki (1;1): '
           r'$P=\frac1{36}$.</p>', hid="pelda-ket-kocka-osszeg"),
   doboz("csapda", "Véd Vilmos csapda — tizenegy összeg, tizenegy esély?",
         r'<p>Vilmos szerint az összeg 2 és 12 között 11-féle lehet, ezért $P(7)=\frac1{11}$. A képlet azonban csak '
         r'<b>egyformán valószínű</b> kimenetelekre érvényes, az összegek pedig nem ilyenek: a 7 hat cellában áll, a 2 '
         r'csak egyben. Ugyanez a hiba volt az A1 „0, 1, 2 fej”-e: $P(\text{pontosan 1 fej})$ nem $\frac13$, hanem '
         r'$\frac24=\frac12$.</p>'),
   kviz('Két kockával dobunk. Mekkora a valószínűsége, hogy a dobott számok összege 7?',
        ['$\\frac16$', '$\\frac1{11}$', '$\\frac7{36}$', '$\\frac1{12}$'], 0,
        jo="✔ 36 egyformán valószínű számpár, ebből 6 adja a 7-et: $\\frac6{36}=\\frac16$.",
        nem="✘ A 11 lehetséges összeg nem egyformán valószínű. A 36 számpárból 6 ad 7-et: $\\frac6{36}=\\frac16$."),
   doboz("erdekesseg", "Egy szerencsejáték, amelyből tudományág lett",
         '<p>A valószínűségszámítás 1654-ben kezdődött: Antoine Gombaud, de Méré lovag kockajátékokról tett fel '
         'kérdéseket Blaise Pascalnak, aki Pierre de Fermat-val levélben dolgozta ki a választ. A klasszikus '
         'valószínűséget Pierre-Simon Laplace foglalta össze 1812-ben. De Méré egyik kérdésére az A3 végén '
         'visszatérünk.</p>'),
 ]),
 ("A valószínűség tulajdonságai", [
   '<p class="lead">A relatív gyakoriság és a klasszikus valószínűség is 0 és 1 közötti hányados — ebből következnek '
   'azok a szabályok, amelyek minden valószínűségre igazak.</p>',
   doboz("tetel", "Alaptulajdonságok és az ellentett esemény",
         r'<p>$$0\le P(A)\le1,\qquad P(\Omega)=1,\qquad P(\emptyset)=0,\qquad P(\overline{A})=1-P(A).$$ Az utolsó a '
         r'leghasznosabb: ha egy esemény valószínűségét nehéz kiszámolni, az ellentettjéé gyakran könnyű. Két kockánál '
         r'annak a valószínűsége, hogy <i>nem</i> dobunk duplát: $1-\frac6{36}=\frac56$.</p>', hid="tetel-ellentett"),
   doboz("tetel", "Két esemény uniója",
         r'<p>Ha $A$ és $B$ kizárják egymást, akkor $P(A\cup B)=P(A)+P(B)$. Általában — ha lehetnek közös '
         r'kimeneteleik — a metszetet egyszer le kell vonni, különben kétszer számolnánk: '
         r'$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$</p>', hid="tetel-unio"),
   doboz("pelda", "I.V.H. Akták — király vagy kőr",
         r'<p>Egy 52 lapos francia kártyacsomagból egy lapot húzunk. Mekkora a valószínűsége, hogy király vagy kőr? '
         r'Király 4 van, kőr 13, de a kőr király mindkettőben benne van: '
         r'$$P=\frac4{52}+\frac{13}{52}-\frac1{52}=\frac{16}{52}=\frac4{13}\approx0{,}308.$$</p>', hid="pelda-kiraly"),
   doboz("csapda", "Véd Vilmos csapda — a kétszer számolt kőr király",
         r'<p>Vilmos összeadta: $\frac4{52}+\frac{13}{52}=\frac{17}{52}$. A kőr királyt kétszer számolta. A puszta '
         r'összeadás csak kizáró eseményeknél helyes.</p>'),
   kviz('Egy osztályban annak a valószínűsége, hogy egy véletlenül választott tanuló kosarazik, $0{,}4$; hogy '
        'focizik, $0{,}5$; hogy mindkettőt űzi, $0{,}2$. Mekkora a valószínűsége, hogy kosarazik vagy focizik?',
        ['$0{,}7$', '$0{,}9$', '$0{,}2$', '$0{,}1$'], 0,
        jo="✔ $0{,}4+0{,}5-0{,}2=0{,}7$ — a mindkettőt űzőket csak egyszer számoljuk.",
        nem="✘ Az események nem kizárók (van, aki mindkettőt űzi), ezért a metszetet le kell vonni: "
            "$0{,}4+0{,}5-0{,}2=0{,}7$."),
 ]),
 ("Valószínűség kombinatorikával", [
   '<p class="lead">Ha az összes és a kedvező kimenetelek száma nagy, a <a href="' + KOMB + 'index.html">kombinatorika</a> '
   'számolja meg őket helyettünk.</p>',
   doboz("pelda", "I.V.H. Akták — két golyó",
         r'<p>Egy dobozban 5 piros és 3 fehér golyó van; egyszerre kihúzunk kettőt. Mekkora a valószínűsége, hogy '
         r'mindkettő piros?</p><p>Az összes kimenetel a 8 golyóból választott párok száma, $\binom82=28$; a kedvezők '
         r'az 5 pirosból választott párok, $\binom52=10$: $$P(\text{két piros})=\frac{10}{28}=\frac5{14}\approx0{,}357.$$ '
         r'Pontosan egy piros: egy piros ÉS egy fehér, $5\cdot3=15$ pár, tehát $\frac{15}{28}$. Két fehér: '
         r'$\frac{\binom32}{28}=\frac3{28}$. A három valószínűség összege $\frac{10+15+3}{28}=1$ — ahogy kell.</p>',
         hid="pelda-golyok"),
   doboz("pelda", "I.V.H. Akták — a lottó",
         r'<p>A szerbiai Loto 7/39-en 39 számból hetet húznak. Egy szelvény akkor telitalálat, ha mind a hét szám '
         r'egyezik. Az összes lehetséges húzás $\binom{39}7=' + E3(comb(39, 7)) + r'$, ebből egy kedvező: '
         r'$$P(\text{telitalálat})=\frac1{' + E3(comb(39, 7)) + r'}\approx0{,}000\,000\,065.$$ (A lottószámok '
         r'kombinációiról a <a href="' + KOMB + r'tananyag-kombinaciok.html#erdekesseg-lotto">05-ös leckében</a> '
         r'volt szó.)</p>', hid="pelda-lotto"),
   GY("#alap-4", "A 4–6", "#kozep-3", "K 3–4"),
   brief('<b>Mr. Szürreál:</b> Új bizonyíték. A Titanic 1309 utasából mindössze 500 élte túl a katasztrófát. Ilyen '
         'esélyekkel indulnak a kadétok is. <b>Véd Vilmos:</b> Tiltakozom! És ha tudjuk, <i>ki</i> volt az utas? '
         '<b>Nagol:</b> Akkor feltételes valószínűséget számolunk.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
TITANIC_TABLA = TABLA(["", "túlélt", "nem élte túl", "összesen"], [
    ["<b>nő</b>", ezres(no_t), ezres(no_n), ezres(no_t + no_n)],
    ["<b>férfi</b>", ezres(fe_t), ezres(fe_n), ezres(fe_t + fe_n)],
    ["<b>összesen</b>", ezres(no_t + fe_t), ezres(no_n + fe_n), ezres(1309)]])
SG_TABLA = TABLA(["2022, 15 éves és idősebb", "összesen", "ismeri a számítógépet", "arány"], [
    ["nő", ezres(SG["no"][0]), ezres(SG["no"][1]), "$" + K(p_ism_no) + "$"],
    ["férfi", ezres(SG["ferfi"][0]), ezres(SG["ferfi"][1]), "$" + K(p_ism_fe) + "$"],
    ["összesen", ezres(SG["osszes"][0]), ezres(SG["osszes"][1]), "$" + K(p_ism) + "$"]])

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál:</b> A Titanic 1309 utasából 500 élte túl a katasztrófát — alig több mint minden harmadik. '
         'A kadétok esélye sem jobb. <b>Véd Vilmos:</b> Tisztelt bizottság, a mentőcsónakokba a „nők és gyermekek '
         'először” szabály szerint szálltak be. Ha tudjuk, hogy az utas nő volt, egészen más a kép! <b>Nagol:</b> A '
         'védőnek most igaza van. A többletinformáció alapján feltételes valószínűséget számolunk; ez eltérhet az '
         'eredetitől.'),
 ]),
 ("Kétdimenziós táblázat", [
   '<p class="lead">A Titanic 1309 utasát két ismérv szerint rendezzük táblázatba: nem és túlélés. Egy véletlenül '
   'kiválasztott utas bármelyik utas lehet egyforma eséllyel, ezért a táblázatból klasszikus valószínűségeket '
   'olvashatunk ki.</p>',
   TITANIC_TABLA, FORRAS("titanic"),
   r'<p>$P(\text{túlélt})=\frac{500}{1309}\approx0{,}382$ · $P(\text{nő})=\frac{466}{1309}\approx0{,}356$ · '
   r'$P(\text{nő és túlélt})=\frac{339}{1309}\approx0{,}259$.</p>',
   abra(SVG_MOZAIK, "Ugyanez mozaikábrán: az oszlop szélessége a csoport létszámával, a zöld sáv magassága a túlélők "
                    "arányával arányos."),
 ]),
 ("Leszűkített eseménytér", [
   r'<p class="lead">Ha tudjuk, hogy a kiválasztott utas nő, akkor már csak a táblázat „nő” sora számít: az '
   r'eseménytér 466 utasra szűkül. Közülük 339 élte túl: $\frac{339}{466}\approx0{,}727$ — majdnem kétszer annyi, '
   r'mint a feltétel nélküli $0{,}382$.</p>',
   doboz("definicio", "Feltételes valószínűség",
         r'<p>Az $A$ esemény $B$ feltétel melletti valószínűsége (ahol $P(B)>0$) $$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$ '
         r'Olvasd: „$A$ valószínűsége, feltéve, hogy $B$ bekövetkezett”. Egyformán valószínű kimeneteleknél ez '
         r'egyszerűen $\frac{k_{A\cap B}}{k_B}$: a $B$-hez tartozó kimenetelek közül hány tartozik $A$-hoz is.</p>',
         hid="def-felteteles"),
   doboz("pelda", "I.V.H. Akták — nők és férfiak",
         r'<p>$$P(\text{túlélt}\mid\text{nő})=\frac{339}{466}\approx0{,}727,\qquad '
         r'P(\text{túlélt}\mid\text{férfi})=\frac{161}{843}\approx0{,}191.$$ A képlettel ugyanez jön ki: '
         r'$P(\text{túlélt}\mid\text{nő})=\dfrac{339/1309}{466/1309}=\dfrac{339}{466}$.</p>'
         r'<p>Egy kockadobás: ha tudjuk, hogy legalább 4-et dobtunk ($\{4;\ 5;\ 6\}$), akkor a páros szám feltételes '
         r'valószínűsége $\frac23$ (a 4 és a 6), noha feltétel nélkül csak $\frac12$.</p>', hid="pelda-titanic"),
   doboz("csapda", "Véd Vilmos csapda — a felcserélt feltétel",
         r'<p>Mr. Szürreál kedvenc trükkje: „a túlélők 67,8%-a nő volt”. Ez $P(\text{nő}\mid\text{túlélt})='
         r'\frac{339}{500}=0{,}678$ — a <b>túlélők</b> közül számol. A kérdés viszont az volt, hogy egy <b>nő</b> '
         r'mekkora eséllyel élte túl: $P(\text{túlélt}\mid\text{nő})\approx0{,}727$. A $P(A\mid B)$ és a $P(B\mid A)$ '
         r'általában különbözik. Mindig nézd meg, melyik sor vagy oszlop a „tudjuk, hogy…” rész: az adja a '
         r'nevezőt.</p>'),
   kviz('A Titanic táblázata alapján melyik szám a $P(\\text{túlélt}\\mid\\text{férfi})$?',
        ['$\\frac{161}{843}$', '$\\frac{161}{500}$', '$\\frac{161}{1309}$', '$\\frac{682}{843}$'], 0,
        jo="✔ A feltétel a „férfi” sor (843 utas); közülük 161 élte túl.",
        nem="✘ A „tudjuk, hogy férfi” rész adja a nevezőt: a férfiak sora, 843 fő; közülük 161 élte túl. A "
            "$\\frac{161}{500}$ a túlélők közti férfiarány, vagyis a fordított feltétel."),
 ]),
 ("Független események", [
   '<p class="lead">Két esemény akkor független, ha az egyik bekövetkezése semmit nem árul el a másikról.</p>',
   doboz("definicio", "Független események",
         r'<p>Az $A$ és a $B$ esemény <b>független</b>, ha $P(A\cap B)=P(A)\cdot P(B)$. Ha $P(B)>0$, ez '
         r'egyenértékű azzal, hogy $P(A\mid B)=P(A)$: a feltétel nem változtat a valószínűségen.</p>',
         hid="def-fuggetlen"),
   doboz("tetel", "Független események szorzata",
         r'<p>Két független eseményre $$P(A\cap B)=P(A)\cdot P(B).$$ Ez az egyenlőség a függetlenség '
         r'ellenőrzésére is használható. Ha $P(B)>0$, akkor $P(A\cap B)=P(A\mid B)\cdot P(B)$ miatt a két '
         r'megfogalmazás egyenértékű; $P(B)=0$ esetén is alkalmazható a szorzatfeltétel.</p>',
         hid="tetel-szorzas-fuggetlen"),
   doboz("pelda", "I.V.H. Akták — független-e?",
         r'<p>Két kocka: „az első hatos” és „a második hatos” független (a kockák nem hatnak egymásra), így '
         r'$P=\frac16\cdot\frac16=\frac1{36}$ — egyezik a 36 cella egyikével.</p>'
         r'<p>Egy kockadobásnál $A$ = „páros” és $B$ = „legfeljebb 2”: $P(A\cap B)=P(\{2\})=\frac16$, és '
         r'$P(A)\cdot P(B)=\frac12\cdot\frac13=\frac16$. Függetlenek — pedig ugyanazon a dobáson múlnak!</p>'
         r'<p>Valós adat: a számítógépes ismeret Szerbiában, 2022-ben, a 15 éves és idősebb lakosok körében:</p>'
         + SG_TABLA + FORRAS("popis")
         + r'<p>$P(\text{ismeri})\approx' + K(p_ism) + r'$, $P(\text{ismeri}\mid\text{nő})\approx' + K(p_ism_no)
         + r'$, $P(\text{ismeri}\mid\text{férfi})\approx' + K(p_ism_fe) + r'$. A feltétel alig változtat: a '
           r'számítógépes ismeret és a nem közel független (a különbség kb. 2 százalékpont). A Titanicon a túlélés és a '
           r'nem erősen függött: $0{,}727$ és $0{,}191$ a $0{,}382$ helyett. Valós adatoknál a pontos egyenlőség '
           r'szinte sosem teljesül — az a kérdés, mekkora az eltérés.</p>', hid="pelda-szamitogep"),
   doboz("csapda", "Véd Vilmos csapda — kizáró nem ugyanaz, mint független",
         r'<p>Vilmos szerint az „1-est dobunk” és a „6-ost dobunk” független, „hiszen semmi közük egymáshoz”. Épp '
         r'ellenkezőleg: kizárják egymást, tehát ha tudjuk, hogy 1-es jött, a 6-os <b>lehetetlen</b>. '
         r'$P(A\cap B)=0$, de $P(A)\cdot P(B)=\frac1{36}$. Két pozitív valószínűségű, kizáró esemény mindig '
         r'függő.</p>'),
   kviz('Az $A$ és a $B$ esemény kizárják egymást, $P(A)=0{,}3$ és $P(B)=0{,}4$. Függetlenek?',
        ['Nem, mert $P(A\\cap B)=0\\ne0{,}12$.', 'Igen, mert kizárják egymást.', 'Igen, mert $0{,}3+0{,}4<1$.',
         'A megadott adatokból nem dönthető el.'], 0,
        jo="✔ Kizáró eseményeknél $P(A\\cap B)=0$, a függetlenséghez viszont $0{,}3\\cdot0{,}4=0{,}12$ kellene.",
        nem="✘ Ha kizárják egymást, $P(A\\cap B)=0$; ha függetlenek volnának, $P(A)\\cdot P(B)=0{,}12$ lenne. Ez nem "
            "teljesül, tehát függők."),
 ]),
 ("Legalább egy — független kísérletekből", [
   '<p class="lead">A „legalább egy” esemény sokféleképpen jöhet létre, az ellentettje viszont egyetlen eset: '
   '<i>egyik sem</i>. Kölcsönösen független eseményeknél ez szorzással számolható.</p>',
   doboz("tetel", "Legalább egy",
         r'<p>$$P(\text{legalább egy bekövetkezik})=1-P(\text{egyik sem következik be}).$$ Ha $A_1,\ldots,A_n$ '
         r'kölcsönösen függetlenek, akkor $P(\text{egyik sem})=\bigl(1-P(A_1)\bigr)\cdot\ldots\cdot\bigl(1-P(A_n)\bigr)$.</p>',
         hid="tetel-legalabb-egy"),
   doboz("pelda", "I.V.H. Akták — három riasztó",
         r'<p>Az I.V.H.-archívumot három, egymástól függetlenül működő riasztó védi; behatoláskor $0{,}9$, $0{,}8$, '
         r'illetve $0{,}7$ valószínűséggel jeleznek. Mekkora a valószínűsége, hogy legalább egy jelez? '
         r'$$1-0{,}1\cdot0{,}2\cdot0{,}3=1-0{,}006=0{,}994.$$</p>', hid="pelda-riaszto"),
   doboz("erdekesseg", "De Méré lovag két fogadása",
         r'<p>Egyenlő összegű nyeremény és veszteség mellett De Méré lovag első fogadása kedvező: egy kockával négy '
         r'dobásból legalább egy hatos lesz $1-\left(\frac56\right)^4\approx0{,}518$ valószínűséggel. A második '
         r'fogadás viszont így már nem kedvező: két kockával 24 dobásból '
         r'legalább egyszer dupla hatos jön: $1-\left(\frac{35}{36}\right)^{24}\approx0{,}491$. A furcsaság Pascalt és '
         r'Fermat-t is foglalkoztatta — és a „legalább egy” képlete adja a választ.</p>'),
   NEHEZ(1, "feltételes valószínűség kétdimenziós táblázatból — és döntés"),
   GY("#alap-7", "A 7–8", "#kozep-5", "K 5–6"),
   brief('<b>Véd Vilmos:</b> Megvan a kiút! Ha egy kísérlet független, újra és újra megismételhetem — mint egy '
         'büntetődobást. <b>Nagol:</b> Akkor jöhet a binomiális valószínűség. <b>Mr. Szürreál:</b> Ismétlés. Az '
         'I.V.H. kedvenc szava.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A4
A4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Tisztelt bizottság, a védelem tanúja Nikola Jokić! A 2024–25-ös NBA-alapszakaszban '
         'büntetőinek 80,0%-át dobta be. Öt büntetőből tehát pontosan négy megy be. Biztosan. <b>Mr. Szürreál:</b> A '
         'bizonyosság hivatali fogalom, kadét. <b>Nagol:</b> A 80% azt jelenti, hogy egy dobás $0{,}8$ '
         'valószínűséggel sikeres. Hogy ötből pontosan négy menjen be, annak kiszámolható az esélye — és korántsem '
         'biztos.'),
 ]),
 ("Bernoulli-kísérletsorozat", [
   '<p class="lead">Sok helyzetben ugyanazt a kísérletet ismételjük meg, és minden alkalommal csak az érdekel, hogy '
   '<b>sikerült-e</b>: bement-e a büntető, fej lett-e, hatost dobtunk-e.</p>',
   doboz("definicio", "Bernoulli-kísérletsorozat",
         r'<p>Egy kísérletet $n$-szer, egymástól <b>függetlenül</b> ismétlünk; minden alkalom eredményét két '
         r'csoportba soroljuk: <b>siker</b> vagy <b>kudarc</b>. A siker valószínűsége minden alkalommal ugyanaz, '
         r'$p$ (a kudarcé $1-p$). A '
         r'kérdés: mekkora a valószínűsége, hogy pontosan $k$ siker lesz? (Jakob Bernoulli, 1713)</p>',
         hid="def-bernoulli"),
   abra(SVG_FA3, "Három büntető: minden elágazásnál S (siker, $0{,}8$) vagy K (kudarc, $0{,}2$). A pontosan két "
                 "sikert adó három ág zöld."),
   r'<p>Az ágak mentén szorzunk, mert a dobások függetlenek. Pontosan két siker háromféle sorrendben jöhet: SSK, SKS, '
   r'KSS — ahány helyre a kudarc kerülhet, $\binom32=3$. Mindhárom ág valószínűsége $0{,}8\cdot0{,}8\cdot0{,}2=0{,}128$, '
   r'tehát $$P(\text{pontosan 2 siker a 3-ból})=3\cdot0{,}8^2\cdot0{,}2=0{,}384.$$ A büntetőket függetlennek és azonos '
   r'$p$-jűnek tekintjük — ez <b>modell</b>. A valóságban a fáradtság vagy a meccs állása is számíthat, a modell mégis '
   r'jól közelít.</p>',
 ]),
 ("A binomiális képlet", [
   doboz("tetel", "Binomiális valószínűség",
         r'<p>Egy $n$ tagú Bernoulli-kísérletsorozatban, ahol a siker valószínűsége $p$, pontosan $k$ siker '
         r'valószínűsége $$P_n(k)=\binom nk p^k(1-p)^{n-k}\qquad(k=0,\,1,\,\ldots,\,n).$$ A $\binom nk$ megszámolja, '
         r'hányféleképpen lehet a $k$ siker az $n$ helyen, a $p^k(1-p)^{n-k}$ pedig egy ilyen sorrend '
         r'valószínűsége.</p>', hid="tetel-binomialis-valoszinuseg"),
   doboz("pelda", "I.V.H. Akták — Jokić öt büntetője",
         r'<p>$n=5$, $p=0{,}8$, $k=4$: $$P_5(4)=\binom54\cdot0{,}8^4\cdot0{,}2=5\cdot0{,}4096\cdot0{,}2=0{,}4096.$$ '
         r'Vagyis az esetek kb. 41%-ában megy be pontosan négy — a többi 59%-ban nem. A teljes eloszlás:</p>'
         + abra(SVG_JOKIC, "Öt büntetőből pontosan $k$ bedobás valószínűsége, ha $p=0{,}8$.")
         + FORRAS("jokic")
         + r'<p>Egy másik példa: egy kockával hatszor dobunk. Pontosan két hatos valószínűsége '
           r'$$P_6(2)=\binom62\left(\frac16\right)^2\left(\frac56\right)^4=15\cdot\frac1{36}\cdot\frac{625}{1296}='
           r'\frac{9375}{46\,656}\approx0{,}201.$$</p>', hid="pelda-jokic"),
   doboz("erdekesseg", "A binomiális tétel visszaköszön",
         r'<p>Az összes valószínűség összege $$\sum_{k=0}^{n}\binom nk p^k(1-p)^{n-k}=\bigl(p+(1-p)\bigr)^n=1^n=1$$ — '
         r'ez éppen a <a href="' + KOMB + r'tananyag-binomialis-tetel.html#tetel-binomialis">binomiális tétel</a> '
         r'$a=p$, $b=1-p$ választással. Innen a név.</p>'),
   doboz("csapda", "Véd Vilmos csapda — egy sorrend nem elég",
         r'<p>Vilmos így számolt: $0{,}8^4\cdot0{,}2=0{,}08192$. Ez csak <b>egy</b> sorrend (például SSSSK) '
         r'valószínűsége; a kimaradó dobás az öt közül bármelyik lehet, ezért még $\binom54=5$-tel szorozni kell. És a '
         r'„80% → biztosan 4 az 5-ből” sem igaz: a 4 a legvalószínűbb eredmény, de csak $0{,}41$ '
         r'valószínűséggel.</p>'),
   kviz('Három szabályos érmét dobunk fel. Mekkora a valószínűsége, hogy pontosan két fej lesz?',
        ['$\\frac38$', '$\\frac18$', '$\\frac23$', '$\\frac12$'], 0,
        jo="✔ $\\binom32\\left(\\frac12\\right)^2\\cdot\\frac12=\\frac38$ — FFI, FIF, IFF.",
        nem="✘ Egy sorrend (például FFI) valószínűsége $\\frac18$, de három sorrend van: "
            "$\\binom32\\cdot\\frac18=\\frac38$."),
 ]),
 ("Legalább, legfeljebb — és mennyire meglepő?", [
   '<p class="lead">A „legalább” és a „legfeljebb” kérdésekben több $k$ valószínűségét adjuk össze — vagy az ellentett '
   'eseményt számoljuk ki.</p>',
   doboz("pelda", "I.V.H. Akták — legalább",
         r'<p>Jokić öt büntetőjéből legalább négy megy be: $$P_5(4)+P_5(5)=0{,}4096+0{,}32768=0{,}73728.$$</p>'
         r'<p>Egy szerbiai újszülött kb. $0{,}516$ valószínűséggel fiú (a 2024-es adat, A2). Három újszülöttből '
         r'legalább egy fiú: $$1-P(\text{egy sem})=1-0{,}484^3\approx1-0{,}113=0{,}887.$$</p>', hid="pelda-legalabb"),
   doboz("pelda", "I.V.H. Akták — gyanús kocka",
         r'<p>Mr. Szürreál kockája tíz dobásból hatszor mutatott hatost. Ha a kocka szabályos, ennek a valószínűsége '
         r'$$P_{10}(6)=\binom{10}6\left(\frac16\right)^6\left(\frac56\right)^4=\frac{210\cdot625}{60\,466\,176}'
         r'\approx0{,}0022.$$ Szabályos kockánál ez ezer próbálkozásból kb. kétszer fordulna elő. Ez még nem '
         r'bizonyíték, de erős gyanú: a valószínűség segít eldönteni, mennyire meglepő egy megfigyelt eredmény.</p>',
         hid="pelda-gyanus-kocka"),
   kviz('Egy kockával hatszor dobunk. Mekkora a valószínűsége, hogy legalább egy hatos lesz?',
        ['$1-\\left(\\frac56\\right)^6\\approx0{,}665$', '$6\\cdot\\frac16=1$', '$\\left(\\frac16\\right)^6$',
         '$\\frac56$'], 0,
        jo="✔ Az ellentett esemény: egyik dobás sem hatos, $\\left(\\frac56\\right)^6\\approx0{,}335$. Tehát "
           "$1-0{,}335=0{,}665$.",
        nem="✘ A $6\\cdot\\frac16=1$ biztos eseményt jelentene — pedig hat dobásból is lehet, hogy egy hatos sem jön. "
            "Az ellentettel: $1-\\left(\\frac56\\right)^6\\approx0{,}665$."),
   NEHEZ(2, "„legalább $k$” siker egy Bernoulli-kísérletsorozatban"),
   GY("#alap-9", "A 9–10", "#kozep-7", "K 7–8"),
   brief('<b>Nagol:</b> Eddig azt kérdeztük, mekkora egy esemény valószínűsége. A következő lépés: minden '
         'kimenetelhez egy számot rendelünk — hány büntető ment be, mennyit nyerünk —, és azt kérdezzük, mit várhatunk '
         'átlagosan. <b>Mr. Szürreál:</b> Az I.V.H.-nak éppen van egy ajánlata.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A5
hz_p = [f / HZ["ossz"] for f in HZ["tag_1_5_6plusz"]]
HZ_TABLA = TABLA(["$x_i$ (tagok száma)", "1", "2", "3", "4", "5", "6 vagy több"], [
    ["háztartás"] + [ezres(f) for f in HZ["tag_1_5_6plusz"]],
    ["$p_i$"] + ["$" + K(q) + "$" for q in hz_p]])
STRAT_TABLA = TABLA(["A stratégia: nyereség", "valószínűség", "", "B stratégia: nyereség", "valószínűség"], [
    ["$30$", "$0{,}5$", "", "$60$", "$0{,}3$"],
    ["$10$", "$0{,}3$", "", "$0$", "$0{,}5$"],
    ["$-20$", "$0{,}2$", "", "$-30$", "$0{,}2$"]])

A5 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Mr. Szürreál:</b> Az I.V.H. nagyvonalú. Egy kockadobás, a tét 100 kredit. Ha hatost dobnak, 500 kreditet '
         'kapnak. <b>Véd Vilmos:</b> Ötszörös nyeremény? Elfogadjuk! <b>Nagol:</b> Várjunk. Előbb számoljuk ki, '
         'mennyit nyerünk vagy veszítünk <i>átlagosan</i>, ha sokszor játszunk. <b>SZVETI:</b> A védő egyszer már '
         'elvesztette a burekpénzét egy hasonló ajánlaton.'),
 ]),
 ("Valószínűségi változó és eloszlása", [
   '<p class="lead">Sok kísérlet kimenetele eleve szám (a dobott pontszám), máskor mi rendelünk számot a kimenetelhez: '
   'hány fej lett, mennyi a nyereség.</p>',
   doboz("definicio", "Valószínűségi változó",
         r'<p>A <b>valószínűségi változó</b> a kísérlet minden kimeneteléhez egy valós számot rendel; jele többnyire '
         r'$X$. Ha véges sok értéke van ($x_1,x_2,\ldots,x_n$), akkor <b>diszkrét</b>. Az <b>eloszlása</b> megmondja, '
         r'melyik értéket mekkora valószínűséggel veszi fel: $p_i=P(X=x_i)$.</p>', hid="def-valoszinusegi-valtozo"),
   doboz("pelda", "I.V.H. Akták — fejek száma",
         r'<p>Két érmét dobunk fel, $X$ a fejek száma. A négy egyformán valószínű kimenetel (FF, FI, IF, II) közül '
         r'$X=2$ egynél, $X=1$ kettőnél, $X=0$ egynél teljesül:</p>'
         + TABLA(["$x_i$", "$0$", "$1$", "$2$"], [["$p_i$", "$\\frac14$", "$\\frac12$", "$\\frac14$"]])
         + abra(SVG_KETERME, "A fejek számának eloszlása oszlopdiagramon."), hid="pelda-ket-erme"),
   doboz("tetel", "Az eloszlás összege 1",
         r'<p>Minden kimenetelhez pontosan egy érték tartozik, ezért a valószínűségek összege mindig '
         r'$$p_1+p_2+\ldots+p_n=1.$$</p>', hid="tetel-eloszlas"),
   doboz("pelda", "I.V.H. Akták — egy szabadkai háztartás",
         r'<p>A 2022-es népszámlálás szerint Szabadkán ' + E3(HZ["ossz"]) + r' háztartás volt. Válasszunk ki egyet '
         r'véletlenszerűen, és legyen $X$ a taglétszáma:</p>' + HZ_TABLA + FORRAS("popis")
         + r'<p>Itt a valószínűségek a relatív gyakoriságok — az A2 statisztikai valószínűsége. Az utolsó érték '
           r'„6 vagy több”; erről a következő szakaszban még lesz szó.</p>', hid="pelda-haztartas"),
   kviz('Egy valószínűségi változó eloszlása: $P(X=1)=0{,}2$, $P(X=2)=0{,}5$, $P(X=3)=p$, és más értéket nem vesz '
        'fel. Mennyi a $p$?', ['$0{,}3$', '$0{,}7$', 'bármennyi lehet', '$0{,}5$'], 0,
        jo="✔ $0{,}2+0{,}5+p=1$, tehát $p=0{,}3$.",
        nem="✘ Az eloszlás valószínűségeinek összege mindig 1: $0{,}2+0{,}5+p=1$, így $p=0{,}3$."),
 ]),
 ("Várható érték", [
   '<p class="lead">Ha a kísérletet sokszor megismételjük, $X$ értékeinek átlaga egy szám körül stabilizálódik — ahogy '
   'a relatív gyakoriság is. Ez a szám a várható érték.</p>',
   doboz("definicio", "Várható érték",
         r'<p>A diszkrét $X$ valószínűségi változó <b>várható értéke</b> az értékek valószínűségekkel súlyozott '
         r'összege: $$E(X)=x_1p_1+x_2p_2+\ldots+x_np_n.$$</p>', hid="def-varhato-ertek"),
   doboz("pelda", "I.V.H. Akták — három várható érték",
         r'<p>Két érme: $E(X)=0\cdot\frac14+1\cdot\frac12+2\cdot\frac14=1$ — átlagosan egy fej.</p>'
         r'<p>Kocka: $E(X)=\frac{1+2+3+4+5+6}6=3{,}5$. A 3,5-öt egyetlen dobással sem lehet megkapni: a várható érték '
         r'nem „a várt dobás”, hanem sok dobás átlaga.</p>'
         r'<p>Szabadkai háztartás, a „6 vagy több” helyett 6-tal számolva: '
         r'$$E(X)\approx\frac{1\cdot' + E3(HZ["tag_1_5_6plusz"][0]) + r'+2\cdot' + E3(HZ["tag_1_5_6plusz"][1])
         + r'+3\cdot' + E3(HZ["tag_1_5_6plusz"][2]) + r'+4\cdot' + E3(HZ["tag_1_5_6plusz"][3]) + r'+5\cdot'
         + E3(HZ["tag_1_5_6plusz"][4]) + r'+6\cdot' + E3(HZ["tag_1_5_6plusz"][5]) + r'}{' + E3(HZ["ossz"])
         + r'}=\frac{' + E3(szorzat) + r'}{' + E3(HZ["ossz"]) + r'}\approx2{,}31.$$ A népszámlálás szerinti átlagos '
           r'taglétszám $2{,}33$. A becslésünk azért kisebb, mert a „6 vagy több” csoportban 7 és 8 tagú háztartások '
           r'is vannak, mi pedig mindet 6-nak vettük.</p>', hid="pelda-varhato"),
   kviz('A kockadobás várható értéke $3{,}5$. Mit jelent ez?',
        ['Sok dobás átlaga $3{,}5$ körül lesz.', 'Egy dobásnál $3{,}5$-öt várunk.',
         'A $3$ és a $4$ a legvalószínűbb dobás.', 'A $3{,}5$ a leggyakoribb dobás.'], 0,
        jo="✔ A várható érték hosszú távú átlag — egyetlen dobás sosem 3,5.",
        nem="✘ Mind a hat érték egyformán valószínű, és 3,5-öt nem is lehet dobni. A várható érték a sok dobás "
            "átlaga, amely 3,5 körül stabilizálódik."),
 ]),
 ("Megéri? — döntés várható értékkel", [
   doboz("pelda", "I.V.H. Akták — Mr. Szürreál ajánlata",
         r'<p>Legyen $X$ a nyereség egy játékban. Hatosnál $+400$ kredit (az 500-ból 100 a saját tétünk volt), '
         r'máskor $-100$: $$E(X)=400\cdot\frac16+(-100)\cdot\frac56=\frac{400-500}6\approx-16{,}7.$$ Játékonként '
         r'átlagosan 16,7 kreditet veszítünk — az ajánlat Mr. Szürreálnak éri meg. Az „ötszörös nyeremény” azért '
         r'csalóka, mert a hatos csak minden hatodik dobásnál jön.</p>', hid="pelda-ajanlat"),
   doboz("pelda", "I.V.H. Akták — két stratégia",
         r'<p>A kadétok két túlélési stratégia közül választhatnak; a nyereség (pontban) és a valószínűségek:</p>'
         + STRAT_TABLA
         + r'<p>$$E(A)=30\cdot0{,}5+10\cdot0{,}3+(-20)\cdot0{,}2=15+3-4=14,$$ '
           r'$$E(B)=60\cdot0{,}3+0\cdot0{,}5+(-30)\cdot0{,}2=18+0-6=12.$$ Várható értékben az A a jobb.</p>',
         hid="pelda-strategia"),
   doboz("csapda", "Véd Vilmos csapda — az értékek sima átlaga",
         r'<p>Vilmos súlyozás nélkül átlagolta az értékeket: az A-nál $\frac{30+10-20}3\approx6{,}7$, a B-nél '
         r'$\frac{60+0-30}3=10$, és a B-t választotta. Csakhogy az A-nál a $-20$ ritka ($0{,}2$), a $30$ gyakori '
         r'($0{,}5$): a valószínűségekkel súlyozni kell.</p>'),
   doboz("erdekesseg", "Miért nyer mindig a kaszinó?",
         '<p>A szerencsejátékokat úgy tervezik, hogy a játékos nyereségének várható értéke negatív legyen, a szervezőé '
         'pedig pozitív. Egy-egy játékos nyerhet, de sok játékban az átlag a várható érték felé tart — a szervező '
         'javára.</p>'),
 ]),
 ("Mennyire kockázatos? — szórásnégyzet", [
   '<p class="lead">Két játéknak lehet ugyanakkora a várható értéke, mégis nagyon különbözhetnek: az egyik biztos, a '
   'másik szélsőséges.</p>',
   doboz("definicio", "Szórásnégyzet és szórás",
         r'<p>A diszkrét $X$ <b>szórásnégyzete</b> az értékek várható értéktől való eltérésének négyzeteiből képzett '
         r'súlyozott összeg: $$D^2(X)=\bigl(x_1-E(X)\bigr)^2p_1+\ldots+\bigl(x_n-E(X)\bigr)^2p_n,$$ a <b>szórás</b> '
         r'pedig ennek négyzetgyöke: $D(X)=\sqrt{D^2(X)}$. Minél nagyobb, annál jobban szóródnak az értékek a várható '
         r'érték körül — annál nagyobb a kockázat.</p>', hid="def-szorasnegyzet"),
   doboz("pelda", "I.V.H. Akták — biztos és kockázatos",
         r'<p>Az 1. játék biztosan $+10$ kreditet ad: $E=10$, $D^2=0$. A 2. játék $\frac12$ valószínűséggel $+40$, '
         r'$\frac12$ valószínűséggel $-20$ kreditet: $$E=40\cdot\frac12+(-20)\cdot\frac12=10,\qquad '
         r'D^2=(40-10)^2\cdot\frac12+(-20-10)^2\cdot\frac12=900,\qquad D=30.$$ A várható érték azonos, a kockázat '
         r'nagyon különböző.</p><p>A két stratégiánál: $D^2(A)=364$, $D(A)\approx19{,}1$; $D^2(B)=1116$, '
         r'$D(B)\approx33{,}4$. Az A tehát nemcsak többet ígér, hanem kiszámíthatóbb is.</p>', hid="pelda-kockazat"),
   doboz("csapda", "Véd Vilmos csapda — négyzet és gyök",
         r'<p>Két gyakori hiba: a négyzetre emelés elmarad (az eltérések súlyozott összege mindig 0 — próbáld ki!), '
         r'vagy a szórásnégyzetet mondjuk szórásnak. A szórás mértékegysége ugyanaz, mint az értékeké (kredit), a '
         r'szórásnégyzeté ennek négyzete (kredit²).</p>'),
   NEHEZ(3, "döntés várható értékkel és szórásnégyzettel"),
   GY("#alap-11", "A 11–12", "#kozep-9", "K 9–10"),
 ]),
 ("🧾 Gyorsismétlő", [
   TABLA(["kérdés", "eszköz", "képlet"], [
       ["egyformán valószínű kimenetelek", "klasszikus valószínűség", "$P(A)=\\dfrac kn$"],
       ["nem következik be", "ellentett esemény", "$P(\\overline{A})=1-P(A)$"],
       ["$A$ vagy $B$", "unió", "$P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$"],
       ["„tudjuk, hogy $B$”", "feltételes valószínűség", "$P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}$"],
       ["$A$ és $B$, függetlenek", "szorzás", "$P(A\\cap B)=P(A)\\cdot P(B)$"],
       ["legalább egy", "ellentett esemény", "$1-P(\\text{egyik sem})$"],
       ["pontosan $k$ siker $n$-ből", "binomiális valószínűség", "$\\binom nk p^k(1-p)^{n-k}$"],
       ["átlagosan mennyi?", "várható érték", "$E(X)=\\sum x_ip_i$"],
       ["mennyire szóródik?", "szórásnégyzet, szórás", "$D^2(X)=\\sum\\bigl(x_i-E(X)\\bigr)^2p_i$"]]),
   brief('<b>Mr. Szürreál:</b> Érdekes elmélet. Az I.V.H. azonban nem jóslatokkal dolgozik, hanem adatokkal. '
         'Grafikonjaim vannak. <b>Nagol:</b> Akkor nézzük meg a grafikonjait. Onnan kezdődik a statisztika.',
         outro=True),
 ]),
]

lapok = [
 lap(**T, fajl="tananyag-esemenyek.html",
     cim="A véletlen nyelve — kísérlet, kimenetel, esemény",
     alcim="Eseménytér, biztos és lehetetlen esemény, műveletek eseményekkel, ellentett és kizáró események.",
     chip=KUL + " · 1/7", szakaszok=A1,
     elozo=("index.html", "Valószínűség és statisztika — áttekintés"),
     kovetkezo=("tananyag-valoszinuseg-fogalma.html", "A valószínűség fogalma")),
 lap(**T, fajl="tananyag-valoszinuseg-fogalma.html",
     cim="Mennyi az esély? — a valószínűség fogalma",
     alcim="Relatív gyakoriság és statisztikai valószínűség, a klasszikus valószínűség, az ellentett esemény és az "
           "unió, valószínűség kombinatorikával.",
     chip=KUL + " · 2/7", szakaszok=A2,
     elozo=("tananyag-esemenyek.html", "Kísérlet, kimenetel, esemény"),
     kovetkezo=("tananyag-felteteles-valoszinuseg.html", "Feltételes valószínűség")),
 lap(**T, fajl="tananyag-felteteles-valoszinuseg.html",
     cim="Ha már tudjuk… — feltételes valószínűség és függetlenség",
     alcim="Kétdimenziós táblázat, leszűkített eseménytér, független események és a „legalább egy”.",
     chip=KUL + " · 3/7", szakaszok=A3,
     elozo=("tananyag-valoszinuseg-fogalma.html", "A valószínűség fogalma"),
     kovetkezo=("tananyag-binomialis-valoszinuseg.html", "Binomiális valószínűség")),
 lap(**T, fajl="tananyag-binomialis-valoszinuseg.html",
     cim="Újra és újra — a binomiális valószínűség",
     alcim="Bernoulli-kísérletsorozat, a binomiális képlet, legalább és legfeljebb — és mennyire meglepő egy eredmény.",
     chip=KUL + " · 4/7", szakaszok=A4,
     elozo=("tananyag-felteteles-valoszinuseg.html", "Feltételes valószínűség"),
     kovetkezo=("tananyag-valoszinusegi-valtozo.html", "Valószínűségi változó")),
 lap(**T, fajl="tananyag-valoszinusegi-valtozo.html",
     cim="Számot a véletlennek — valószínűségi változó és várható érték",
     alcim="Diszkrét valószínűségi változó és eloszlása, várható érték, döntés várható értékkel, szórásnégyzet — és a "
           "valószínűség gyorsismétlője.",
     chip=KUL + " · 5/7", szakaszok=A5,
     elozo=("tananyag-binomialis-valoszinuseg.html", "Binomiális valószínűség"),
     kovetkezo=(FA, "Zsoldos-lista — Valószínűség")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
