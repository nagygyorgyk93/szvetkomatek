# -*- coding: utf-8 -*-
"""4e/06 — a ket feladatgyujtemeny: Zsoldos-lista — Valoszinuseg (A1–A5) es Zsoldos-lista — Statisztika (B1–B2).
Feladat-terkep: projektek/szvetkomatek/4e/terkep_fgy_06-valoszinuseg-statisztika.md (jovahagyva 2026-09-29: a joker
Monty Hall; a Titanic-osztaly es a magyarorszagi szuletesek temaja rendben; minel tobb valos adatra epulo feladat).
Forrasok: K11 (Kezikonyv a Matematika 11. II. kotetehez, 382–425), VD (Vene-alapu lapok 1324–1411), V7 (Vene 7.1–7.2),
ADAT (adat_4e_06: RZS Popis 2022, Eurostat, Open-Meteo ERA5, titanic3, Jokic) + sajat.
Minden vegeredmeny tortekkel (Fraction) es — ahol lehet — teljes felsorolassal szamolva; a valos adatos feladatok a
nyers adatsorbol. A felmerok adatai (tiltott_4e_06) es a tananyag kidolgozott peldai kiszurve."""
import sys, os, re, json, glob
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import comb, sqrt
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from abra_stat import svg_oszlop, mutatok, ezres, tized, diagram_adatok
import adat_4e_06 as ADAT
import tiltott
TILT = tiltott.modul("tiltott_4e_06")

T = dict(tagozat="4e", mappa="06-valoszinuseg-statisztika", temakor="Valószínűség és statisztika")
E = []


def chk(nev, *ertekek):
    if any(e != ertekek[0] for e in ertekek[1:]):
        E.append((nev, ertekek))
    return ertekek[0]


def kozel(nev, a, b, tur=5e-4):
    if abs(a - b) > tur:
        E.append((nev, a, b))
    return a


def FR(f):
    """Fraction → KaTeX: egész vagy \\frac{p}{q}."""
    f = F(f)
    if f.denominator == 1:
        return str(f.numerator).replace("-", "-")
    s = "-" if f < 0 else ""
    return f"{s}\\frac{{{abs(f.numerator)}}}{{{f.denominator}}}"


def D(x, j=3):
    """tizedes KaTeX-be: 0{,}337"""
    return tized(float(x), j).replace(",", "{,}").replace("−", "-")


def M(s):
    return f"${s}$"


def AP(x, j=3):
    return f"$\\approx{D(x, j)}$"


def N3(n):
    return ezres(n).replace(" ", "\\,")


def FORRAS(*kulcsok):
    r = []
    for k in kulcsok:
        cim, url = ADAT.FORRAS[k]
        rov = {"popis": "RZS, Popis 2022", "eurostat": "Eurostat", "openmeteo": "Open-Meteo (ERA5)",
               "titanic": "titanic3 (Vanderbilt)", "jokic": "NBA-statisztika", "penz": "történeti kísérletek"}[k]
        r.append(f'<a href="{url}">{rov}</a>' if url else rov)
    return ' <small>(Forrás: ' + ", ".join(r) + ')</small>'


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    # a svgwrap-burok miatt kerül a táblázat a kérdés <p>-je UTÁN (fgy_common._one); egyszintű marad.
    # A kiemelt részt a fgy_common nem alakítja át, ezért itt írjuk át a $…$ képleteket \(…\)-re.
    ki = f'<div class="svgwrap"><table class="tt-table"><tr>{th}</tr>{tr}</table></div>'
    return re.sub(r"\$([^$]+)\$", r"\\(\1\\)", ki)


def TABLA_V(fej, sorok, blokk=1):
    """Álló táblázat (a sok oszlopos adatsor telefonon se gördüljön): `sorok` soronként egy rekord; `blokk` > 1
    esetén a sorokat ennyi, egymás mellé tett blokkba tördeljük (pl. jan.–jún. | júl.–dec.)."""
    n = -(-len(sorok) // blokk)
    reszek = [sorok[i * n:(i + 1) * n] for i in range(blokk)]
    uj = [sum((r[i] if i < len(r) else [""] * len(fej) for r in reszek), []) for i in range(n)]
    return TABLA(fej * blokk, uj)


def binom(n, p, k):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


KOCKA = range(1, 7)
KK = list(product(KOCKA, KOCKA))
HZ_SZ = ADAT.HAZTARTAS["szabadka"]
SG = ADAT.SZAMITOGEP["szabadka"]
SZUL = ADAT.SZULETES
IDO = ADAT.IDOJARAS_2024
_om = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "projektek", "szvetkomatek",
                             "4e", "adatok_06", "openmeteo_szabadka_2024.json"))
# a napi adatokból számolt két érték (a nyers fájl a repón kívül van; ha nem érhető el, a rögzített érték marad)
if _om:
    _d = json.load(open(_om[0]))["daily"]
    MELEG = sum(1 for t in _d["temperature_2m_mean"] if t > 25)
    JUL_MAX = [m for m, n in zip(_d["temperature_2m_max"], _d["time"]) if n[5:7] == "07"]
else:
    MELEG = 58
    JUL_MAX = [30.7, 23.6, 24.6, 25.5, 28.7, 30.5, 32.7, 34.7, 35.7, 36.0, 37.3, 37.6, 36.6, 37.0, 36.5, 37.8, 35.7,
               33.7, 34.1, 29.5, 30.4, 33.0, 31.3, 30.4, 27.6, 29.3, 31.5, 35.9, 29.0, 28.4, 31.6]
chk("napi adatok", (MELEG, len(JUL_MAX)), (58, 31))

# ================================================================ VALÓSZÍNŰSÉG — ALAP
V_ALAP = []
om1 = chk("v-alap-1a", len(list(product("FI", KOCKA))), 12)
om2 = sorted("".join(p) for p in product("FI", repeat=3))
chk("v-alap-1b", len(om2), 8)
om4 = sorted("".join(sorted(p)) for p in combinations("PKZ", 2))
V_ALAP.append((
    "Írd fel a kísérlet eseményterét, és add meg, hány eleme van!",
    ["Egy érmét és egy dobókockát dobunk fel egyszerre.", "Egy érmét háromszor egymás után feldobunk.",
     "A MATEK szó betűi közül véletlenszerűen kiválasztunk egyet.",
     "Egy dobozban egy piros (P), egy kék (K) és egy zöld (Z) golyó van; kettőt kihúzunk egyszerre."],
    [f"$\\{{F1;\\ F2;\\ \\ldots;\\ F6;\\ I1;\\ \\ldots;\\ I6\\}}$, {om1} elem",
     "$\\{" + ";\\ ".join(om2) + "\\}$, 8 elem",
     "$\\{M;\\ A;\\ T;\\ E;\\ K\\}$, 5 elem", "$\\{PK;\\ PZ;\\ KZ\\}$, 3 elem"]))

A_, B_ = {2, 3, 5}, {1, 3, 5}
OM = set(KOCKA)


def H(s):
    return "$\\{" + ";\\ ".join(map(str, sorted(s))) + "\\}$" if s else "$\\emptyset$"


V_ALAP.append((
    "Egy kockával dobunk. Legyen $A$ = „prímszámot dobunk”, $B$ = „páratlan számot dobunk”. Add meg halmazként!",
    ["$A\\cup B$", "$A\\cap B$", "$\\overline{A}$", "$B\\setminus A$", "Kizárják-e egymást $A$ és $B$?"],
    [H(A_ | B_), H(A_ & B_), H(OM - A_), H(B_ - A_), "nem"], True))

V_ALAP.append((
    "Jelölje $A$, $B$, illetve $C$ azt az eseményt, hogy Szabadkán hétfőn, kedden, illetve szerdán esik az eső. Írd "
    "fel a műveletek jeleivel!",
    ["Mindhárom nap esik.", "Egyik nap sem esik.", "Legalább egy nap esik.", "Csak hétfőn esik.",
     "Pontosan két nap esik."],
    ["$A\\cap B\\cap C$", "$\\overline{A}\\cap\\overline{B}\\cap\\overline{C}$", "$A\\cup B\\cup C$",
     "$A\\cap\\overline{B}\\cap\\overline{C}$",
     "$(A\\cap B\\cap\\overline{C})\\cup(A\\cap\\overline{B}\\cap C)\\cup(\\overline{A}\\cap B\\cap C)$"]))

MAT = "MATEMATIKA"
va4 = [chk("v-alap-4a", F(sum(1 for k in KOCKA if k < 5), 6), F(2, 3)),
       chk("v-alap-4b", F(sum(1 for k in range(1, 31) if k % 4 == 0), 30), F(7, 30)),
       chk("v-alap-4c", F(4 + 5, 15), F(3, 5)),
       chk("v-alap-4d", F(sum(1 for b in MAT if b in "AEI"), len(MAT)), F(1, 2))]
p_egy = HZ_SZ["tag_1_5_6plusz"][0] / HZ_SZ["ossz"]
V_ALAP.append((
    "Mekkora a valószínűsége?",
    ["Egy kockadobásnál 5-nél kisebb számot dobunk.", "Az $1,\\ 2,\\ \\ldots,\\ 30$ számok közül egyet véletlenszerűen "
     "kiválasztva 4-gyel osztható számot kapunk.", "Egy dobozban 4 piros, 6 kék és 5 zöld golyó van; egyet kihúzva nem kéket "
     "kapunk.",
     "A MATEMATIKA szó tíz betűje közül egyet véletlenszerűen kiválasztva magánhangzót kapunk.",
     f"Szabadka 2022-es {ezres(HZ_SZ['ossz'])} háztartása közül egyet véletlenszerűen kiválasztva egyszemélyes "
     f"háztartást kapunk (egyszemélyes háztartásból {ezres(HZ_SZ['tag_1_5_6plusz'][0])} volt; három tizedesre)."
     + FORRAS("popis")],
    [M(FR(v)) for v in va4] + [AP(p_egy)]))

# magyar kártya: 4 szín × 8 figura
MAGYAR = [(sz, f) for sz in ("piros", "zöld", "tök", "makk") for f in ("VII", "VIII", "IX", "X", "alsó", "felső",
                                                                         "király", "ász")]
kz = chk("v-alap-5b", F(sum(1 for sz, f in MAGYAR if f == "király" or sz == "zöld"), 32), F(11, 32))
p_fiu = F(SZUL["RS_M"][2024], SZUL["RS_T"][2024])
chk("v-alap-5e", round(float(p_fiu), 3), 0.516)
V_ALAP.append((
    "Használd a valószínűség tulajdonságait!",
    ["$P(A)=0{,}35$. Mennyi $P(\\overline{A})$?",
     "A 32 lapos magyar kártya négy színe piros, zöld, tök és makk, mindegyikből VII, VIII, IX, X, alsó, felső, "
     "király és ász van. Egy lapot húzunk: mekkora a valószínűsége, hogy király vagy zöld?",
     "$A$ és $B$ kizárják egymást, $P(A)=0{,}2$ és $P(B)=0{,}45$. Mennyi $P(A\\cup B)$?",
     "$P(A)=0{,}5$, $P(B)=0{,}4$ és $P(A\\cap B)=0{,}1$. Mennyi $P(A\\cup B)$?",
     "Szerbiában 2024-ben az újszülöttek 51,6%-a volt fiú. Mekkora a valószínűsége, hogy egy véletlenszerűen "
     "kiválasztott, 2024-ben Szerbiában született újszülött lány?"
     + FORRAS("eurostat")],
    ["$0{,}65$", M(FR(kz)), "$0{,}65$", "$0{,}8$", "$0{,}484$"]))

hu_fiu = SZUL["HU_M"][2024] / SZUL["HU_T"][2024]
jul_eso = IDO["szabadka"]["esos_nap_havonta"][6]
chk("v-alap-6b", jul_eso, 3)
V_ALAP.append((
    "Becsüld meg a valószínűséget a relatív gyakorisággal (három tizedesre)!",
    [f"Magyarországon 2024-ben {ezres(SZUL['HU_T'][2024])} gyermek született, közülük {ezres(SZUL['HU_M'][2024])} "
     f"fiú. Mekkora a valószínűsége, hogy egy újszülött fiú?" + FORRAS("eurostat"),
     f"Szabadkán 2024 júliusában {jul_eso} napon esett legalább 1 mm csapadék. Mekkora a valószínűsége, hogy egy "
     f"júliusi napon legalább 1 mm csapadék hullik?" + FORRAS("openmeteo"),
     f"Szabadkán 2024-ben a 366 napból {MELEG} napon volt 25 °C fölött a napi középhőmérséklet. Mekkora a "
     f"valószínűsége, hogy egy véletlenül választott napon így volt?" + FORRAS("openmeteo")],
    [AP(hu_fiu), f"$\\frac{{{jul_eso}}}{{31}}\\approx{D(jul_eso / 31)}$",
     f"$\\frac{{{MELEG}}}{{366}}\\approx{D(MELEG / 366)}$"]))

SG_TABLA = TABLA(["", "összesen", "ismeri a számító&shy;gépet"], [
    ["nő", ezres(SG["no"][0]), ezres(SG["no"][1])], ["férfi", ezres(SG["ferfi"][0]), ezres(SG["ferfi"][1])],
    ["összesen", ezres(SG["osszes"][0]), ezres(SG["osszes"][1])]])
p_no, p_ism, p_no_ism = SG["no"][0] / SG["osszes"][0], SG["osszes"][1] / SG["osszes"][0], SG["no"][1] / SG["osszes"][0]
V_ALAP.append((
    "A táblázat a szabadkai 15 éves és idősebb lakosokat mutatja nem és számítógépes ismeret szerint." + FORRAS("popis")
    + " (Az „ismeri” oszlopban a „részben ismeri” választ adók nincsenek benne.) Egy lakost véletlenszerűen "
      "kiválasztunk. Mekkora a valószínűsége (három tizedesre), hogy" + SG_TABLA,
    ["nő?", "ismeri a számítógépet?", "nő, és ismeri a számítógépet?"],
    [AP(p_no), AP(p_ism), AP(p_no_ism)], True))

va8 = [chk("v-alap-8a", F(sum(1 for e, k in product("FI", KOCKA) if e == "F" and k == 6), 12), F(1, 12)),
       chk("v-alap-8b", F(sum(1 for a, b in KK if a % 2 == 0 and b % 2 == 0), 36), F(1, 4))]
V_ALAP.append((
    "Független események: mekkora a valószínűsége?",
    ["Egy érmét és egy kockát dobunk fel: fej és hatos.", "Két kockával dobunk: mindkét szám páros.",
     "Két lövész egymástól függetlenül lő; az egyik $0{,}7$, a másik $0{,}6$ valószínűséggel talál. Mindketten "
     "találnak.",
     "Szerbiában egy újszülött $0{,}516$ valószínűséggel fiú (2024). Két, egymástól független szülésnél mindkét "
     "újszülött fiú."],
    [M(FR(va8[0])), M(FR(va8[1])), "$0{,}42$", AP(0.516 ** 2)]))

va9 = [chk("v-alap-9a", F(sum(1 for s in product("FI", repeat=4) if s.count("F") == 2), 16), F(3, 8)),
       chk("v-alap-9b", F(sum(1 for s in product(KOCKA, repeat=3) if s.count(6) == 1), 216), F(25, 72)),
       chk("v-alap-9c", F(1, 2 ** 5), F(1, 32))]
V_ALAP.append((
    "Binomiális valószínűség: mekkora a valószínűsége?",
    ["Négy érmét feldobva pontosan két fej lesz.", "Egy kockával háromszor dobva pontosan egy hatos lesz.",
     "Öt érmét feldobva mind az öt fej lesz.",
     "Három, egymástól független szerbiai szülésnél ($p=0{,}516$ a fiú valószínűsége) pontosan két fiú születik."],
    [M(FR(v)) for v in va9] + [AP(binom(3, 0.516, 2))]))

V_ALAP.append((
    "Bernoulli-kísérletsorozat-e? (Rögzített számú, egymástól független kísérlet; minden eredményt sikerre vagy "
    "kudarcra sorolunk, és a siker valószínűsége minden kísérletben ugyanaz.)",
    ["Egy kockával tízszer dobunk, és a hatosok számát figyeljük.",
     "A 32 lapos magyar kártyából visszatevés nélkül húzunk öt lapot, és a pirosak számát figyeljük.",
     "Ugyanez, de minden húzás után visszatesszük a lapot és megkeverjük a paklit.",
     "Addig dobunk egy kockával, amíg hatost nem kapunk."],
    ["igen", "nem", "igen", "nem"], True))

va11 = [chk("v-alap-11a", [F(sum(1 for s in product("FI", repeat=3) if s.count("F") == k), 8) for k in range(4)],
            [F(1, 8), F(3, 8), F(3, 8), F(1, 8)]),
        chk("v-alap-11b", F(1) - F(1, 10) - F(35, 100) - F(15, 100), F(2, 5))]
V_ALAP.append((
    "Eloszlás:",
    ["Három érmét dobunk fel; $X$ a fejek száma. Add meg $X$ eloszlását!",
     "Egy $X$ valószínűségi változó értékei 0, 1, 2 és 3; $P(X=0)=0{,}1$, $P(X=1)=0{,}35$, $P(X=3)=0{,}15$. Mennyi "
     "$P(X=2)$?"],
    ["$P(X=0)=\\frac18$, $P(X=1)=\\frac38$, $P(X=2)=\\frac38$, $P(X=3)=\\frac18$", "$0{,}4$"]))

va12 = [chk("v-alap-12a", sum(k * p for k, p in enumerate(va11[0])), F(3, 2)),
        chk("v-alap-12b", 0 * F(1, 10) + 1 * F(35, 100) + 2 * va11[1] + 3 * F(15, 100), F(8, 5)),
        chk("v-alap-12c", 1 * F(2, 10) + 2 * F(5, 10) + 5 * F(3, 10), F(27, 10))]
V_ALAP.append((
    "Számold ki a várható értéket!",
    ["az előző feladat a) részében szereplő $X$-ét;", "az előző feladat b) részében szereplő $X$-ét;",
     "ha $X$ értékei 1, 2 és 5, a valószínűségük rendre $0{,}2$, $0{,}5$ és $0{,}3$."],
    ["$1{,}5$", "$1{,}6$", "$2{,}7$"], True))

# ================================================================ VALÓSZÍNŰSÉG — KÖZÉP
V_KOZEP = []
V_KOZEP.append((
    "Egyszerűsítsd! ($A$ és $B$ ugyanannak a kísérletnek két eseménye, $\\Omega$ az eseménytér.)",
    ["$\\overline{\\overline{A}\\cap\\overline{B}}$", "$(A\\cap B)\\cup(A\\cap\\overline{B})$", "$A\\cup\\overline{A}$",
     "$A\\cap\\overline{A}$"],
    ["$A\\cup B$", "$A$", "$\\Omega$", "$\\emptyset$"], True))

vk2 = [chk("v-kozep-2a", len(list(product("FI", repeat=4))), 16),
       chk("v-kozep-2b", len(list(product(KOCKA, repeat=3))), 216),
       chk("v-kozep-2c", comb(35, 5), sum(1 for _ in combinations(range(35), 5))),
       chk("v-kozep-2d", len(list(product(range(10), repeat=3))), 1000)]
V_KOZEP.append((
    "Hány eleme van az eseménytérnek?",
    ["Egy érmét négyszer feldobunk.", "Három kockával dobunk (a kockák megkülönböztethetők).",
     "Egy sorsjátékon 35 számból húznak ki ötöt (a húzás sorrendje nem számít).",
     "Egy háromjegyű kódot (0–9 jegyekből, ismétlődhetnek) véletlenszerűen beállítunk."],
    [M(N3(v)) for v in vk2], True))

GOLYO = ["p"] * 6 + ["f"] * 4
har = list(combinations(range(10), 3))
vk3a = chk("v-kozep-3a", F(sum(1 for c in har if all(GOLYO[i] == "p" for i in c)), len(har)), F(1, 6))
vk3b = chk("v-kozep-3b", F(sum(1 for c in har if sum(GOLYO[i] == "p" for i in c) == 2), len(har)), F(1, 2))
OSZT = ["l"] * 6 + ["f"] * 4
ot = list(combinations(range(10), 5))
vk3c = chk("v-kozep-3c", F(sum(1 for c in ot if sum(OSZT[i] == "l" for i in c) == 3), len(ot)), F(10, 21))
TI = ADAT.TITANIC
tul = TI["nem"]["no"][0] + TI["nem"]["ferfi"][0]
vk3d = chk("v-kozep-3d", F(comb(tul, 2), comb(TI["utas"], 2)), F(500 * 499, 1309 * 1308))
V_KOZEP.append((
    "Valószínűség kombinatorikával:",
    ["Egy dobozban 6 piros és 4 fehér golyó van; hármat kihúzunk egyszerre. Mekkora a valószínűsége, hogy mind a "
     "három piros?", "Ugyanebben a húzásban mekkora a valószínűsége, hogy pontosan két piros?",
     "Egy 6 lányból és 4 fiúból álló csoportból sorsolással egy 5 fős csapatot választanak. Mekkora a valószínűsége, "
     "hogy pontosan 3 lány lesz benne?",
     f"A Titanic {TI['utas']} utasa közül {tul} élte túl a katasztrófát. Két utast véletlenszerűen "
     f"kiválasztva mekkora a valószínűsége, hogy mindketten túlélték?" + FORRAS("titanic")],
    [M(FR(vk3a)), M(FR(vk3b)), M(FR(vk3c)), AP(float(vk3d))]))

vk4a = chk("v-kozep-4a", F(sum(1 for k in range(1, 101) if k % 2 == 0 or k % 5 == 0), 100), F(3, 5))
p_no_v_ism = (SG["no"][0] + SG["osszes"][1] - SG["no"][1]) / SG["osszes"][0]
V_KOZEP.append((
    "Két esemény uniója:",
    ["Az $1,\\ 2,\\ \\ldots,\\ 100$ számok közül egyet választunk. Mekkora a valószínűsége, hogy 2-vel vagy 5-tel "
     "osztható?",
     "Egy évfolyam egy véletlenül választott tanulójára $A$ = „volt kirándulni az elmúlt két hónapban”, "
     "$B$ = „volt beteg az elmúlt hónapban”; $P(A)=0{,}2$, $P(B)=0{,}09$, $P(A\\cap B)=0{,}01$. Mekkora a "
     "valószínűsége, hogy legalább az egyik teljesül?",
     "Ugyanitt: $A$ teljesül, de $B$ nem?", "Ugyanitt: pontosan az egyik teljesül?",
     "Az Alapszint <a href=\"#alap-7\">7. feladatának</a> szabadkai táblázata alapján: egy véletlenül választott lakos nő, vagy ismeri a számítógépet? "
     "(A táblázat darabszámaiból számolj, és csak a végén kerekíts három tizedesre!)"],
    [M(FR(vk4a)), "$0{,}28$", "$0{,}19$", "$0{,}27$", AP(p_no_v_ism)]))

B9 = [k for k in KK if sum(k) >= 9]
vk5a = chk("v-kozep-5a", F(sum(1 for k in B9 if 4 in k), len(B9)), F(2, 5))
p4 = F(sum(1 for k in KK if 4 in k), 36)
kartya2 = list(product(range(32), repeat=2))
piros = lambda i: i < 8
vk5c = chk("v-kozep-5c", F(sum(1 for a, b in kartya2 if piros(a) and piros(b)), sum(1 for a, b in kartya2 if piros(a))),
           F(1, 4))
p_ism_no, p_no_ism2 = SG["no"][1] / SG["no"][0], SG["no"][1] / SG["osszes"][1]
V_KOZEP.append((
    "Feltételes valószínűség:",
    ["Két kockával dobunk. Feltéve, hogy a dobott számok összege legalább 9, mekkora a valószínűsége, hogy van 4-es "
     "a dobott számok között?",
     f"Független-e a „van 4-es” esemény az „összeg legalább 9” eseménytől? ($P(\\text{{van 4-es}})={FR(p4)}$)",
     "A 32 lapos magyar kártyából kétszer húzunk, visszatevéssel. Feltéve, hogy az első lap piros, mekkora a "
     "valószínűsége, hogy a második is piros?",
     "Az Alapszint <a href=\"#alap-7\">7. feladatának</a> táblázata alapján mennyi $P(\\text{ismeri}\\mid\\text{nő})$ és "
     "$P(\\text{nő}\\mid\\text{ismeri})$? (A darabszámokból számolj, a végén kerekíts három tizedesre!)"],
    [M(FR(vk5a)), "nem", M(FR(vk5c)), f"$\\approx{D(p_ism_no)}$; $\\approx{D(p_no_ism2)}$"]))

vk6a = chk("v-kozep-6a", F(sum(1 for s in product(KOCKA, repeat=3) if 6 in s), 216), F(91, 216))
V_KOZEP.append((
    "Legalább egy — független kísérletekből:",
    ["Három kockával dobunk. Mekkora a valószínűsége, hogy legalább egy hatos lesz?",
     "Egy lövész háromszor lő, minden lövésnél egymástól függetlenül $0{,}4$ valószínűséggel talál. Mekkora a "
     "valószínűsége, hogy legalább egyszer talál?",
     "Egy lámpatestben négy izzó van, mindegyik a többitől függetlenül $0{,}95$ valószínűséggel bírja ki az évet. "
     "Mekkora a valószínűsége, hogy legalább egy kiég (három tizedesre)?",
     f"Szabadkán 2024 júliusában 31 napból {jul_eso} napon hullott legalább 1 mm csapadék. Ha minden nap a "
     f"többitől függetlenül $\\frac{{{jul_eso}}}{{31}}$ valószínűséggel hullana legalább 1 mm csapadék, "
     f"mekkora lenne a valószínűsége, hogy egy júliusi héten (7 nap) legalább egy ilyen nap van?" + FORRAS("openmeteo")],
    [f"$\\frac{{91}}{{216}}\\approx{D(float(vk6a))}$", "$0{,}784$", AP(1 - 0.95 ** 4),
     AP(1 - (1 - jul_eso / 31) ** 7)]))

jokic_2526 = [j["bunteto"] for j in ADAT.JOKIC if j["szezon"] == "2025–26"][0]
chk("v-kozep-7c", jokic_2526, 0.831)
V_KOZEP.append((
    "Binomiális valószínűség, részben valós adatokkal (három tizedesre; a dobások, illetve a jelentkezők "
    "egymástól függetlenek):",
    ["Nikola Jokić a 2024–25-ös szezonban a büntetőinek 80,0%-át dobta be. Tíz büntetőből mekkora a valószínűsége, "
     "hogy pontosan nyolc megy be?" + FORRAS("jokic"),
     "Egy előadásra kilencen jelentkeztek, mindenki a többiektől függetlenül $0{,}9$ valószínűséggel jön el. "
     "Mekkora a valószínűsége, hogy pontosan heten jönnek el?",
     "A 2025–26-os szezonban Jokić büntetőinek 83,1%-át dobta be. Öt büntetőből mekkora a valószínűsége, hogy mind "
     "bemegy?" + FORRAS("jokic")],
    [AP(binom(10, 0.8, 8)), AP(binom(9, 0.9, 7)), AP(0.831 ** 5)]))

vk8c = chk("v-kozep-8c", sum(binom(5, F(1, 4), k) for k in (3, 4, 5)),
           F(sum(1 for s in product(range(4), repeat=5) if s.count(0) >= 3), 4 ** 5), F(53, 512))
V_KOZEP.append((
    "Legalább, legfeljebb, pontosan:",
    ["Egy nap 19 honlapot látogatunk meg; mindegyik a többitől függetlenül $0{,}02$ valószínűséggel vírusos. Mekkora "
     "a valószínűsége, hogy legalább egy vírusos honlapra tévedünk (három tizedesre)?",
     "Mekkora a valószínűsége, hogy pontosan egy vírusos honlapot látogatunk meg (három tizedesre)?",
     "Egy ötkérdéses tesztben minden kérdésnél 4 válasz közül egy jó. Ha valaki minden kérdésnél véletlenszerűen, "
     "a többitől függetlenül tippel, mekkora a valószínűsége, hogy legalább 3 jó válasza lesz?",
     "Szerbiában egy újszülött $0{,}516$ valószínűséggel fiú. Öt, egymástól független szülésből mekkora a "
     "valószínűsége, hogy legfeljebb egy fiú születik (három tizedesre)?" + FORRAS("eurostat")],
    [AP(1 - 0.98 ** 19), AP(binom(19, 0.02, 1)), f"$\\frac{{53}}{{512}}\\approx{D(float(vk8c))}$",
     AP(binom(5, 0.516, 0) + binom(5, 0.516, 1))]))

vk9 = chk("v-kozep-9", sum(F(800 if (a, b) == (6, 6) else (150 if a == b else 0), 36) for a, b in KK) - 50,
          F(-125, 18))
V_KOZEP.append((
    "Mr. Szürreál új játéka: a tét 50 kredit (nem jár vissza). Két kockával dobunk; dupla hatosért 800, bármely "
    "más duplaért (két egyforma számért) 150 kreditet fizet Mr. Szürreál, más esetben semmit. Legyen $X$ a játékos nyeresége (a kifizetés "
    "mínusz a tét).",
    ["Mennyi $E(X)$?", "Megéri-e sokszor játszani?"],
    [f"${FR(vk9)}\\approx{D(float(vk9), 2)}$ kredit", "nem"], True))

vk10 = chk("v-kozep-10", sum(k * F(sum(1 for a, b in KK if max(a, b) == k), 36) for k in KOCKA), F(161, 36))
chk("v-kozep-10 eloszlás", [F(sum(1 for a, b in KK if max(a, b) == k), 36) for k in KOCKA],
    [F(2 * k - 1, 36) for k in KOCKA])
jok2 = [binom(2, F(4, 5), k) for k in range(3)]
V_KOZEP.append((
    "Eloszlás és várható érték:",
    ["Két kockával dobunk; $X$ a nagyobbik dobott szám (egyenlőség esetén a közös érték). Add meg $X$ eloszlását!",
     "Mennyi ennek az $X$-nek a várható értéke?",
     "Jokić két büntetőt dob, mindegyik $0{,}8$ valószínűséggel megy be, egymástól függetlenül. $Y$ a bedobott "
     "büntetők száma. Add meg $Y$ eloszlását és várható értékét!"],
    ["$P(X=1)=\\frac{1}{36}$, $P(X=2)=\\frac{3}{36}$, $P(X=3)=\\frac{5}{36}$, $P(X=4)=\\frac{7}{36}$, "
     "$P(X=5)=\\frac{9}{36}$, "
     "$P(X=6)=\\frac{11}{36}$",
     f"$\\frac{{161}}{{36}}\\approx{D(float(vk10), 2)}$",
     "$P(Y=0)=0{,}04$; $P(Y=1)=0{,}32$; $P(Y=2)=0{,}64$; $E(Y)=1{,}6$"]))
chk("v-kozep-10c", jok2, [F(1, 25), F(8, 25), F(16, 25)])

# ================================================================ VALÓSZÍNŰSÉG — NEHÉZ
V_NEHEZ = []
O = TI["osztaly"]
TIT_TABLA = TABLA(["osztály", "túlélt", "nem élte túl", "összesen"],
                  [[f"{o}.", ezres(v[0]), ezres(v[1]), ezres(v[0] + v[1])] for o, v in O.items()]
                  + [["összesen", ezres(500), ezres(809), ezres(1309)]])
chk("v-nehez-1 össz", sum(v[0] for v in O.values()), 500)
V_NEHEZ.append((
    "A Titanic 1309 utasa jegyosztály és túlélés szerint:" + FORRAS("titanic") + TIT_TABLA,
    ["Mennyi $P(\\text{túlélt}\\mid 1.\\ \\text{osztály})$ és $P(\\text{túlélt}\\mid 3.\\ \\text{osztály})$ (három "
     "tizedesre)?",
     "Mennyi $P(1.\\ \\text{osztály}\\mid\\text{túlélt})$?",
     "Független-e a túlélés a jegyosztálytól?",
     "Mr. Szürreál: „A túlélők 36,2%-a harmadik osztályon utazott, tehát a harmadik osztályon is jó esélye volt "
     "mindenkinek.” Melyik feltételes valószínűséget számolta ki Mr. Szürreál, és mekkora valójában egy harmadik "
     "osztályon utazó túlélési esélye?"],
    [f"$\\approx{D(O['1'][0] / sum(O['1']))}$; $\\approx{D(O['3'][0] / sum(O['3']))}$",
     f"${D(200 / 500, 1)}$", "nem",
     f"$P(3.\\ \\text{{osztály}}\\mid\\text{{túlélt}})={D(181 / 500)}$; "
     f"$P(\\text{{túlélt}}\\mid 3.\\ \\text{{osztály}})\\approx{D(O['3'][0] / sum(O['3']))}$"]))

n_min = chk("v-nehez-2b", next(n for n in range(1, 50) if 1 - F(4, 5) ** n >= F(9, 10)), 11)
V_NEHEZ.append((
    "Legalább $k$ — és visszafelé:",
    ["Kilenc jelentkezőből mindenki a többiektől függetlenül $0{,}9$ valószínűséggel jön el. Mekkora a "
     "valószínűsége, hogy legalább heten eljönnek (három tizedesre)?",
     "Jokić minden büntetője a többitől függetlenül $0{,}8$ valószínűséggel megy be. Legalább hány büntetőt kell "
     "dobnia, hogy legalább $0{,}9$ valószínűséggel legyen köztük kihagyott?"],
    [AP(sum(binom(9, 0.9, k) for k in (7, 8, 9))), M(n_min)]))

C_ = [(20, F(3, 5)), (-10, F(2, 5))]
D_ = [(50, F(3, 10)), (0, F(1, 2)), (-20, F(1, 5))]
EC, ED = sum(x * p for x, p in C_), sum(x * p for x, p in D_)
DC, DD = sum((x - EC) ** 2 * p for x, p in C_), sum((x - ED) ** 2 * p for x, p in D_)
chk("v-nehez-3", (EC, ED, DC, DD), (8, 11, 216, 709))
BEF = (TABLA(["$x$", "$20$", "$-10$"], [["$P(X=x)$", "$0{,}6$", "$0{,}4$"]])
       + TABLA(["$y$", "$50$", "$0$", "$-20$"], [["$P(Y=y)$", "$0{,}3$", "$0{,}5$", "$0{,}2$"]]))
V_NEHEZ.append((
    "A kadétok két befektetés közül választhatnak. $X$ az 1., $Y$ a 2. befektetés nyeresége (kreditben); a "
    "lehetséges értékek és valószínűségeik:" + BEF,
    ["Mennyi a két befektetés várható nyeresége?", "Mennyi a szórásnégyzetük?",
     "Mennyi a szórásuk (egy tizedesre)?",
     "Melyik ígér nagyobb várható nyereséget, és melyik kevésbé kockázatos a szórás alapján?"],
    ["$E(X)=8$; $E(Y)=11$", "$D^2(X)=216$; $D^2(Y)=709$",
     f"$D(X)\\approx{D(sqrt(DC), 1)}$; $D(Y)\\approx{D(sqrt(DD), 1)}$",
     "nagyobb várható nyereség: a 2.; kevésbé kockázatos: az 1."]))

# joker: Monty Hall — teljes felsorolás
nyer_marad = nyer_valt = 0
for auto, valaszt in product(range(3), repeat=2):
    nyito = next(a for a in range(3) if a != valaszt and a != auto)
    uj = next(a for a in range(3) if a not in (valaszt, nyito))
    nyer_marad += valaszt == auto
    nyer_valt += uj == auto
chk("v-joker", (F(nyer_marad, 9), F(nyer_valt, 9)), (F(1, 3), F(2, 3)))
V_JOKER = ("Egy vetélkedőn három zárt ajtó közül választhatsz; egy mögött autó van, a másik kettő mögött semmi. "
           "Választasz egy ajtót. A műsorvezető — aki tudja, hol az autó — ezután mindig kinyit egy másik ajtót, amely "
           "mögött nincs semmi (ha két ilyen van, véletlenszerűen választ közülük), és mindig megkérdezi: maradsz, vagy átváltasz a harmadik ajtóra? Mekkora a nyerés valószínűsége, ha "
           "maradsz, és mekkora, ha váltasz?",
           "maradva $\\frac13$, váltva $\\frac23$ — érdemes váltani")

# ================================================================ STATISZTIKA — ALAP
S_ALAP = []
S_ALAP.append((
    "A 2022-es szerbiai népszámlálás néhány ismérve. Döntsd el mindegyikről, hogy minőségi vagy mennyiségi "
    "ismérv-e; ha mennyiségi, akkor diszkrét vagy folytonos!",
    ["a lakás alapterülete (m²)", "a háztartás taglétszáma", "lakóhely (település)", "számítógépes ismeret",
     "a lakás szobáinak száma", "a gyermekek száma"],
    ["mennyiségi, folytonos", "mennyiségi, diszkrét", "minőségi", "minőségi", "mennyiségi, diszkrét",
     "mennyiségi, diszkrét"], True))

S_ALAP.append((
    "Melyik skálán mérünk? (nominális, ordinális vagy intervallumskála)",
    ["a kosárlabdázók mezszáma", "iskolai végzettség", "hőmérséklet °C-ban", "a személy neme (férfi/nő)", "a verseny helyezése",
     "születési év"],
    ["nominális", "ordinális", "intervallum", "nominális", "ordinális", "intervallum"], True))

JEGY = [4, 3, 5, 2, 3, 3, 3, 4, 4, 5, 2, 2, 1, 3, 2, 4, 1, 5, 4, 3, 3, 4, 2, 1, 3, 2, 3, 4, 3, 5]
jc = Counter(JEGY)
chk("s-alap-3", [jc[k] for k in range(1, 6)], [3, 6, 10, 7, 4])
S_ALAP.append((
    "Egy 30 fős osztály matematikajegyei: " + ", ".join(map(str, JEGY)) + ".",
    ["Add meg a jegyek abszolút gyakoriságát (1-estől 5-ösig)!",
     "Add meg a relatív gyakoriságokat százalékban (egy tizedesre)!"],
    ["$3;\\ 6;\\ 10;\\ 7;\\ 4$",
     "$" + ";\\ ".join(D(100 * jc[k] / 30, 1) for k in range(1, 6)) + "$ (%)"]))

KOR = ADAT.KOR["szabadka"]["osszes"]["csoport"]
g10 = [KOR[i] + KOR[i + 1] for i in range(0, 16, 2)] + [KOR[16] + KOR[17]]
chk("s-alap-4 összeg", sum(g10), 123952)
KOR_TABLA = TABLA_V(["életkor", "lakos"], [[c, ezres(v)] for c, v in zip(
    ["0–9", "10–19", "20–29", "30–39", "40–49", "50–59", "60–69", "70–79", "80+"], g10)])
S_ALAP.append((
    "Szabadka lakói 2022-ben, 10 éves korcsoportok szerint:" + FORRAS("popis") + KOR_TABLA,
    ["Melyik a legnépesebb korcsoport?", "Hány 20 évesnél fiatalabb lakos van?",
     "A lakosok hány százaléka 60 éves vagy idősebb (egy tizedesre)?"],
    ["60–69 évesek", M(N3(g10[0] + g10[1])), f"$\\approx{D(100 * sum(g10[6:]) / 123952, 1)}\\%$"]))

S_ALAP.append((
    "Melyik diagramot választanád? (oszlop-, kör-, vonaldiagram vagy hisztogram)",
    ["a szerbiai háztartások száma taglétszám szerint (1, 2, …, 6 vagy több tag)",
     "Szabadka napi középhőmérséklete 2024 minden napján",
     'a lakosság százalékos megoszlása a számítógépes ismeret szerint (ismeri, részben ismeri, nem ismeri, ismeretlen)',
     "egy 30 fős osztály tanulóinak testmagassága (cm)"],
    ["oszlopdiagram", "vonaldiagram", "kördiagram", "hisztogram"]))

MECCS = [j["meccs"] for j in ADAT.JOKIC]
mm = mutatok(MECCS)
s6 = [chk("s-alap-6a", mutatok([10, 7, 7, 6, 13, 12, 8, 14])["median"], 9),
      chk("s-alap-6b", mutatok([17, 31, 15, 28, 35, 30, 29, 19, 19])["median"], 28),
      chk("s-alap-6c", mutatok([3, 5, 5, 7, 8, 8, 8, 10, 10, 12])["mod"], [8]),
      chk("s-alap-6d", mutatok([6, 7, 10, 12, 14])["mod"], [])]
chk("s-alap-6e", (mm["median"], mm["mod"]), (73, [73, 80]))
S_ALAP.append((
    "Középértékek:",
    ["Mi a mediánja a 10; 7; 7; 6; 13; 12; 8; 14 adatsornak?",
     "Mi a mediánja a 17; 31; 15; 28; 35; 30; 29; 19; 19 adatsornak?",
     "Mi a módusza a 3; 5; 5; 7; 8; 8; 8; 10; 10; 12 adatsornak?",
     "Mi a módusza a 6; 7; 10; 12; 14 adatsornak?",
     "Nikola Jokić NBA-alapszakaszonként lejátszott meccseinek száma: " + "; ".join(map(str, MECCS))
     + ". Mi a medián és a módusz?" + FORRAS("jokic")],
    ["$9$", "$28$", "$8$", "nincs", "medián $73$; módusz $73$ és $80$"]))

CSALAD = {0: 3, 1: 25, 2: 50, 3: 15, 4: 5, 5: 2}
HZ_SRB = ADAT.HAZTARTAS["szerbia"]
hz_atl = chk("s-alap-7b", sum((i + 1) * f for i, f in enumerate(HZ_SRB["tag_1_5_6plusz"])),
             773945 + 2 * 711946 + 3 * 459926 + 4 * 375565 + 5 * 156050 + 6 * 111912) / HZ_SRB["ossz"]
HZ_TABLA = TABLA_V(["tagok száma", "háztartás"], [[c, ezres(f)] for c, f in zip(
    ["1", "2", "3", "4", "5", "6 vagy több"], HZ_SRB["tag_1_5_6plusz"])])
S_ALAP.append((
    "Átlag gyakorisági táblázatból:",
    ["Egy községben 100 család gyerekszáma: 0 gyerek — 3 család, 1 — 25, 2 — 50, 3 — 15, 4 — 5, 5 — 2. Mennyi az "
     "átlagos gyerekszám?",
     "Szerbia 2022-es háztartásai taglétszám szerint (összesen " + ezres(HZ_SRB["ossz"]) + " háztartás):"
     + FORRAS("popis") + HZ_TABLA.replace('<div class="svgwrap">', "").replace("</div>", "")
     + " A „6 vagy több” csoportot 6-nak véve mennyi az átlagos taglétszám (két tizedesre)? Kisebb vagy nagyobb ez a "
       "hivatalos 2,55-nál?"],
    [M(FR(chk("s-alap-7a", F(sum(k * f for k, f in CSALAD.items()), 100), 2))),
     f"$\\approx{D(hz_atl, 2)}$; kisebb"]))

KF = ADAT.KOR["szerbia"]
atl_kor = (KF["ferfi"]["atlagkor"] * KF["ferfi"]["ossz"] + KF["no"]["atlagkor"] * KF["no"]["ossz"]) / KF["osszes"]["ossz"]
kozel("s-alap-8c", atl_kor, KF["osszes"]["atlagkor"], 0.01)
mj = mutatok(JEGY)
S_ALAP.append((
    "Súlyozott átlag:",
    ["Egy vállalatnál 50 szakmunkás átlagos havi nettó keresete 98 000 dinár, 40 adminisztratív dolgozóé "
     "76 000 dinár. Mennyi az átlagkereset az egész vállalatnál (egészre kerekítve)?",
     "Mennyi a 30 matekjegy (a 3. feladat adatai) átlaga, mediánja és módusza?",
     f"Szerbia 2022-es népszámlálása szerint a {ezres(KF['ferfi']['ossz'])} férfi átlagéletkora "
     f"{tized(KF['ferfi']['atlagkor'], 2)} év, a {ezres(KF['no']['ossz'])} nőé {tized(KF['no']['atlagkor'], 2)} év. "
     f"Mennyi a teljes népesség átlagéletkora (két tizedesre)?" + FORRAS("popis")],
    [f"$\\approx{N3(chk('s-alap-8a', round(F(50 * 98000 + 40 * 76000, 90)), 88222))}$ dinár",
     f"átlag ${D(mj['atlag'], 1)}$; medián ${int(mj['median'])}$; módusz ${mj['mod'][0]}$",
     f"$\\approx{D(atl_kor, 2)}$ év"]))

SZAB = IDO["szabadka"]["havi_kozep"]
ms = mutatok(SZAB)
chk("s-alap-9", (ms["min"], ms["q1"], ms["median"], round(ms["q3"], 2), ms["max"]), (2.5, 6.75, 13.75, 21.1, 26.7))
HONAP = ["jan.", "febr.", "márc.", "ápr.", "máj.", "jún.", "júl.", "aug.", "szept.", "okt.", "nov.", "dec."]
SZAB_TABLA = TABLA_V(["hónap", "°C"], [[h, tized(v, 1)] for h, v in zip(HONAP, SZAB)], 2)
S_ALAP.append((
    "Szabadka 2024-es havi középhőmérsékletei (°C):" + FORRAS("openmeteo") + SZAB_TABLA,
    ["Mennyi a legkisebb és a legnagyobb érték, valamint a terjedelem?", "Mennyi a medián?",
     "Mennyi az alsó és a felső kvartilis?"],
    [f"${D(ms['min'], 1)}$; ${D(ms['max'], 1)}$; terjedelem ${D(ms['max'] - ms['min'], 1)}$",
     f"${D(ms['median'], 2)}$", f"$Q_1={D(ms['q1'], 2)}$; $Q_3={D(ms['q3'], 1)}$"]))

m1, m2 = mutatok([2, 5, 8, 11, 14]), mutatok([2, 8, 14])
chk("s-alap-10", (m1["atlag"], m1["aae"], m1["var"], m2["atlag"], m2["aae"], m2["var"]), (8, 3.6, 18, 8, 4, 24))
ESO = IDO["szabadka"]["esos_nap_havonta"]
me = mutatok(ESO)
S_ALAP.append((
    "Szóródás:",
    ["A $2;\\ 5;\\ 8;\\ 11;\\ 14$ adatsor: mennyi az átlag, az átlagos abszolút eltérés és a szórásnégyzet?",
     "Ugyanezek a $2;\\ 8;\\ 14$ adatsorra?",
     "Szabadkán 2024-ben havonta ennyi napon esett legalább 1 mm csapadék: " + ", ".join(map(str, ESO))
     + ". Mennyi az átlag (két tizedesre), a medián és a terjedelem?" + FORRAS("openmeteo")],
    ["$8$; $3{,}6$; $18$", "$8$; $4$; $24$",
     f"$\\approx{D(me['atlag'], 2)}$; ${D(me['median'], 1)}$; ${int(me['max'] - me['min'])}$"]))

# ================================================================ STATISZTIKA — KÖZÉP
S_KOZEP = []
SGS = ADAT.SZAMITOGEP["szerbia"]["osszes"]
S_KOZEP.append((
    f"Szerbia 15 éves és idősebb lakosai ({ezres(SGS[0])} fő) számítógépes ismeret szerint 2022-ben: ismeri "
    f"{ezres(SGS[1])}, részben ismeri {ezres(SGS[2])}, nem ismeri {ezres(SGS[3])}, ismeretlen {ezres(SGS[4])} fő."
    + FORRAS("popis"),
    ["Add meg a relatív gyakoriságokat százalékban (egy tizedesre)!",
     "Kördiagramon mekkora középponti szög tartozik az egyes csoportokhoz? (A darabszámokból számolj, és csak a "
     "végén kerekíts egy tizedesre!)"],
    ["$" + ";\\ ".join(D(100 * v / SGS[0], 1) for v in SGS[1:]) + "$ (%)",
     "$" + ";\\ ".join(D(360 * v / SGS[0], 1) for v in SGS[1:]) + "$ (fok)"]))

osztalyok = [(22 + 2 * i, 24 + 2 * i) for i in range(8)]
gyak = [sum(1 for t in JUL_MAX if a <= t < b) for a, b in osztalyok]
chk("s-kozep-2", gyak, [1, 2, 1, 5, 7, 3, 5, 7])
S_KOZEP.append((
    "Szabadka 2024. júliusi napi legmagasabb hőmérsékletei (°C): " + "; ".join(tized(t, 1) for t in JUL_MAX) + "."
    + FORRAS("openmeteo"),
    ["Készíts gyakorisági táblázatot 2 °C-os osztályközökkel, 22 °C-tól ($[22;24)$, $[24;26)$, …, $[36;38)$)!",
     "Melyik osztályközökben van a legtöbb nap?", "Hány napon érte el a maximum a 34 °C-ot?"],
    ["$" + ";\\ ".join(map(str, gyak)) + "$", "$[30;32)$ és $[36;38)$",
     M(chk("s-kozep-2c", sum(1 for t in JUL_MAX if t >= 34), gyak[6] + gyak[7]))]))

S_KOZEP.append((
    "Az iskolai diákönkormányzat azt szeretné megtudni, hány órát alszanak az iskola tanulói egy tanítási napon. Melyik "
    "mintavétel torz, és melyik megfelelő?",
    ["kérdőív az iskola közösségi oldalán, aki akar, kitölti",
     "a teljes névsorból sorsolással kiválasztott 60 tanuló",
     "reggel 7-kor a kapuban megkérdezett első 30 érkező",
     "minden osztályból a létszámával arányos számú, sorsolással kiválasztott tanuló"],
    ["torz", "megfelelő", "torz", "megfelelő"], True))

SPL = IDO["split"]["havi_kozep"]
mp = mutatok(SPL)
S_KOZEP.append((
    "Szabadka és Split 2024-es havi középhőmérsékletei (°C):" + FORRAS("openmeteo")
    + TABLA_V(["hónap", "Szabadka", "Split"], [[h, tized(a, 1), tized(b, 1)] for h, a, b in zip(HONAP, SZAB, SPL)]),
    ["Mennyi a két adatsor átlaga (két tizedesre)?", "Mennyi a mediánjuk?",
     "Mennyi a szórásuk (két tizedesre; a pontos átlaggal számolj, csak a végén kerekíts)?",
     "Melyik városban ingadozik jobban a havi középhőmérséklet?"],
    [f"$\\approx{D(ms['atlag'], 2)}$; $\\approx{D(mp['atlag'], 2)}$", f"${D(ms['median'], 2)}$; ${D(mp['median'], 2)}$",
     f"$\\approx{D(ms['sz'], 2)}$; $\\approx{D(mp['sz'], 2)}$", "Szabadkán"]))

LIS = IDO["lisszabon"]["havi_kozep"]
ml = mutatok(LIS)
# a feladat a kerekített átlagot és szórást adja meg — a kulcs is azokból számol
z_sz = (max(SZAB) - round(ms["atlag"], 2)) / round(ms["sz"], 2)
z_li = (max(LIS) - round(ml["atlag"], 2)) / round(ml["sz"], 2)
kozel("s-kozep-5b", z_li, 5.49 / 3.42, 1e-9)
S_KOZEP.append((
    f"Szabadka 2024-es havi középhőmérsékleteinek átlaga {tized(ms['atlag'], 2)} °C, szórása {tized(ms['sz'], 2)} °C; "
    f"Lisszabon esetében ugyanezek: {tized(ml['atlag'], 2)} °C és {tized(ml['sz'], 2)} °C. A legmelegebb hónap mindkét városban az "
    f"augusztus volt: Szabadkán {tized(max(SZAB), 1)} °C, Lisszabonban {tized(max(LIS), 1)} °C." + FORRAS("openmeteo"),
    ["Mennyi a szabadkai augusztus standardizált értéke (két tizedesre)?",
     "Mennyi a lisszaboni augusztusé (két tizedesre)?",
     "Melyik augusztus volt szokatlanabb a saját városa havi középhőmérsékleteihez képest?"],
    [f"$\\approx{D(z_sz, 2)}$", f"$\\approx{D(z_li, 2)}$", "a lisszaboni"]))

PONT = [j["pont"] for j in ADAT.JOKIC]
mp_all, mp_uj = mutatok(PONT), mutatok(PONT[1:])
S_KOZEP.append((
    "Jokić meccsenkénti pontátlaga 11 alapszakaszban: " + "; ".join(tized(v, 1) for v in PONT)
    + ". Az átlag $\\approx22{,}45$, a medián $24{,}5$. Az első, 10,0 pontos szezon a pályafutás kezdete — hagyjuk el!"
    + FORRAS("jokic"),
    ["Mennyi a maradék 10 szezon átlaga és mediánja (két tizedesre)?",
     "Melyik változott többet: az átlag vagy a medián?"],
    [f"$\\approx{D(mp_uj['atlag'], 2)}$; ${D(mp_uj['median'], 2)}$", "az átlag"]))
chk("s-kozep-6b", abs(mp_uj["atlag"] - mp_all["atlag"]) > abs(mp_uj["median"] - mp_all["median"]), True)

ERME5 = {0: 1, 1: 4, 2: 5, 3: 6, 4: 3, 5: 1}
S_KOZEP.append((
    "Öt érmét hússzor feldobtunk, és minden alkalommal megszámoltuk a fejeket: 0 fej — 1-szer, 1 — 4-szer, "
    "2 — 5-ször, 3 — 6-szor, 4 — 3-szor, 5 — 1-szer.",
    ["Mennyi a fejek számának átlaga?", "Mennyi a fejek számának várható értéke (szabályos érméknél)?",
     "Mennyi a „3 fej” relatív gyakorisága és valószínűsége?"],
    [M(FR(chk("s-kozep-7a", F(sum(k * f for k, f in ERME5.items()), 20), F(49, 20))) + f"={D(49 / 20, 2)}"),
     "$2{,}5$", f"$0{{,}}3$; $\\frac{{10}}{{32}}={D(10 / 32, 4)}$"]))
chk("s-kozep-7b", sum(k * binom(5, F(1, 2), k) for k in range(6)), F(5, 2))

# ================================================================ STATISZTIKA — NEHÉZ
S_NEHEZ = []
hu23, hu24 = SZUL["HU_T"][2023], SZUL["HU_T"][2024]
SVG_HU = svg_oszlop(["2023", "2024"], [hu23, hu24], ymin=75000, ymax=90000, lepes=5000, w=300, h=220,
                    ertek_cimkek=[ezres(hu23), ezres(hu24)], szin="#b91c1c",
                    leiras="Oszlopdiagram 75 000-nél kezdődő függőleges tengellyel: a magyarországi születések száma "
                           "2023-ban és 2024-ben")
S_NEHEZ.append((
    "Egy hírportál ezzel az ábrával mutatta be a magyarországi születések számát:" + FORRAS("eurostat")
    + diagram_adatok(SVG_HU, "Magyarországi születések, 2023–2024",
                     ["év", "születések száma"], [["2023", ezres(hu23)], ["2024", ezres(hu24)]],
                     megjegyzes="A vízszintes tengelyen az év, a függőlegesen a születések száma szerepel. "
                                "A függőleges tengely 75 000-től 90 000-ig tart, 5000-es beosztással; az oszlopok "
                                "75 000-nél kezdődnek."),
    ["Hány százalékkal csökkent valójában a születések száma (egy tizedesre)?",
     "Az ábrán a 2024-es oszlop magassága a 2023-asnak hányad része (három tizedesre)?",
     "Honnan kellene indulnia a függőleges tengelynek, hogy az oszlopok aránya a valódi arányt mutassa?"],
    [f"$\\approx{D(100 * (hu23 - hu24) / hu23, 1)}\\%$", f"$\\approx{D((hu24 - 75000) / (hu23 - 75000))}$",
     "$0$-tól"]))

need5 = chk("s-nehez-2a", 5 * F(18, 5) - 4 * F(13, 4), 5)
need4 = 5 * 4 - 4 * F(13, 4)
CSAP = [F(str(x)) for x in IDO["szabadka"]["havi_csapadek_mm"]]
csap_atl = chk("s-nehez-2c átlag", sum(CSAP) / 12, F("40.675"))       # pontosan 40,675: nincs kerekítési bizonytalanság
hiany = chk("s-nehez-2c", 12 * csap_atl - (sum(CSAP) - CSAP[4]), F("50.1"))
S_NEHEZ.append((
    "Visszafelé az átlagból:",
    ["Egy tanuló első négy jegyének átlaga 3,25. Hányast kell kapnia az ötödikre, hogy az átlaga 3,6 legyen?",
     "Elérheti-e az ötödik jeggyel a 4,0-s átlagot?",
     f"Szabadkán 2024-ben a havi csapadékösszegek átlaga {tized(float(csap_atl), 3)} mm volt. Tizenegy hónap adata "
     "(mm, január–április és június–december): " + "; ".join(tized(float(v), 1) for i, v in enumerate(CSAP) if i != 4)
     + ". Mennyi csapadék esett májusban?" + FORRAS("openmeteo")],
    [M(need5), f"nem (${need4}$ kellene)", f"${D(float(hiany), 1)}$ mm"]))

kiugo_sz = sum(1 for x in SZAB if abs(x - ms["atlag"]) > ms["sz"])
kiugo_li = sum(1 for x in LIS if abs(x - ml["atlag"]) > ml["sz"])
chk("s-nehez-3", (kiugo_sz, kiugo_li), (6, 5))
S_NEHEZ.append((
    "Az I.V.H. új kiképzőbázist keres ott, ahol a havi középhőmérséklet a kiegyenlítettebb. Jelöltek: Szabadka "
    "és Lisszabon (2024-es adatok, °C)." + FORRAS("openmeteo")
    + TABLA_V(["hónap", "Szabadka", "Lisszabon"], [[h, tized(a, 1), tized(b, 1)] for h, a, b in zip(HONAP, SZAB, LIS)]),
    ["Mennyi a két adatsor átlaga és szórása (két tizedesre; a pontos átlaggal számolj)? Összevetheted a "
     "középszint 5. feladatában megadott értékekkel.",
     "Hány olyan hónap van az egyes városokban, amelynek középhőmérséklete több mint egy szórással tér el a saját "
     "átlagtól?", "Melyik várost javasolnád?"],
    [f"Szabadka $\\approx{D(ms['atlag'], 2)}$ és $\\approx{D(ms['sz'], 2)}$; Lisszabon $\\approx{D(ml['atlag'], 2)}$ "
     f"és $\\approx{D(ml['sz'], 2)}$", f"Szabadka ${kiugo_sz}$; Lisszabon ${kiugo_li}$", "Lisszabont"]))

S_JOKER = ("Adj meg öt pozitív egész számot, amelyeknek a módusza 3, a mediánja 4, az átlaga 5!",
           "például $3;\\ 3;\\ 4;\\ 7;\\ 8$")
pl = [3, 3, 4, 7, 8]
chk("s-joker", (mutatok(pl)["mod"], mutatok(pl)["median"], mutatok(pl)["atlag"]), ([3], 4, 5))

# ================================================================ ÖNELLENŐRZÉS
WEB = [("erme", 3), ("erme", 4), ("erme", 5), ("kocka", 2), ("kocka", 3), ("golyo", (4, 6, 5)), ("golyo", (6, 4, 3)),
       ("komb", (10, 3)), ("komb", (10, 5)), ("komb", (35, 5)), ("komb", (1309, 2)), ("kartya", ("magyar", 1, 1)),
       ("kartya", ("magyar", 2, 2)), ("bernoulli", (3, "0.516", 2)), ("bernoulli", (10, "0.8", 8)),
       ("bernoulli", (9, "0.9", 7)), ("bernoulli", (5, "0.831", 5)), ("bernoulli", (19, "0.02", 1)),
       ("bernoulli", (5, "1/4", 3)), ("bernoulli", (5, "0.516", 1)), ("bernoulli", (4, "1/2", 2)),
       ("bernoulli", (3, "1/6", 1)), ("bernoulli", (2, "0.8", 2)), ("bernoulli", (9, "0.9", 9)),
       ("tabla", "szamitogep-szabadka"), ("tabla", "titanic-osztaly"), ("adatsor", "haztartas-szerbia"),
       ("adatsor", "kor-szabadka-10"), ("adatsor", "jokic-meccs"), ("adatsor", "jokic-pont"),
       ("adatsor", "homerseklet-2024"), ("adatsor", "csapadek-2024"), ("adatsor", "julius-max-szabadka"), ("adatsor", "szuletes-hu"),
       ("szamjegy", {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}), ("szo", "MATEK"), ("szo", "MATEMATIKA")]
E += TILT.ellenoriz(WEB)
# a tananyag (build_tananyag_4e_06a/b) kidolgozott példái: típus + paraméter
TANANYAG = {("kartya", ("francia", 1, 1)), ("golyo", (5, 3, 2)), ("komb", (8, 2)), ("komb", (39, 7)),
            ("bernoulli", (3, "4/5", 2)), ("bernoulli", (5, "4/5", 4)), ("bernoulli", (6, "1/6", 2)),
            ("bernoulli", (10, "1/6", 6)), ("bernoulli", (3, "0.516", 1)), ("tabla", "titanic"),
            ("tabla", "szamitogep-srb"), ("adatsor", "haztartas-szabadka"), ("adatsor", "jokic-pont"),
            ("adatsor", "homerseklet-2024")}
ENGEDETT = {("adatsor", "jokic-pont"): "közép-6: a kezdő szezon elhagyása; a tananyagban átlag, medián, módusz",
            ("adatsor", "homerseklet-2024"): "alap-9, közép-4, közép-5, nehéz-2, nehéz-3: Szabadka havi adatai és "
                                             "más kérdések; a tananyagban Split–Lisszabon kvartilisei és szórása"}
for t_, p_ in WEB:
    kulcs = (t_, frozenset(p_) if isinstance(p_, set) else p_)
    if kulcs in TANANYAG and kulcs not in ENGEDETT:
        E.append(("tananyag-ütközés", kulcs))
assert not E, E
print("önteszt: OK | valószínűség", len(V_ALAP), len(V_KOZEP), len(V_NEHEZ), "| statisztika", len(S_ALAP),
      len(S_KOZEP), len(S_NEHEZ), "+ jokerek; tiltott és tananyag rendben")


# ================================================================ OLDALAK
def lista(A, K, N_, J):
    return "\n".join([
        '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(A, "alap", "alap"),
        '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(K, "kozep", "kozep"),
        '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(N_, "nehez", "nehez"),
        '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(J[0], J[1])])


if __name__ == "__main__":
    u1 = oldal(**T, fajl="feladatok-valoszinuseg.html", cim="Zsoldos-lista — Valószínűség",
               h1="Valószínűség — Zsoldos-lista", itt="Zsoldos-lista — Valószínűség",
               alcim=(
                         'Események, klasszikus és statisztikai valószínűség, feltételes valószínűség és függetlenség, '
                         'binomiális valószínűség, valószínűségi változó, várható érték és szórás — sok valós adattal. A '
                         'végeredmény lenyitható: előbb számolj! Ha nincs külön feltétel, a kockák szabályosak és '
                         'hatoldalúak, az érmék szabályosak, a külön dobások egymástól függetlenek; véletlen választáskor '
                         'minden elemnek azonos esélyt adunk.'
                     ),
               sections_html=lista(V_ALAP, V_KOZEP, V_NEHEZ, V_JOKER), ossz_nev="Csalópapírt",
               prev="tananyag-valoszinusegi-valtozo.html", prevc="Valószínűségi változó és várható érték",
               nxt="tananyag-adatok.html", nxtc="Adatokból kép — sokaság, minta, diagram")
    print("✓", os.path.basename(u1))
    u2 = oldal(**T, fajl="feladatok-statisztika.html", cim="Zsoldos-lista — Statisztika",
               h1="Statisztika — Zsoldos-lista", itt="Zsoldos-lista — Statisztika",
               alcim=(
                         'Ismérvek és skálák, gyakorisági táblázat, diagramok, középértékek, kvartilisek, szórás és '
                         'standardizált érték — valós szerbiai, magyarországi és nemzetközi adatokkal. A végeredmény '
                         'lenyitható: előbb számolj! Ha nincs külön feltétel, a kockák szabályosak és hatoldalúak, az érmék '
                         'szabályosak, a külön dobások egymástól függetlenek; véletlen választáskor minden elemnek azonos '
                         'esélyt adunk.'
                     ),
               sections_html=lista(S_ALAP, S_KOZEP, S_NEHEZ, S_JOKER), ossz_nev="Csalópapírt",
               prev="tananyag-statisztikai-mutatok.html", prevc="Középértékek és szóródás",
               nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
    print("✓", os.path.basename(u2))
