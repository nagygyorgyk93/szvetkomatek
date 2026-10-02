# -*- coding: utf-8 -*-
"""4e/05 — a kozos feladatgyujtemeny: Zsoldos-lista (kombinatorika + binomialis tetel).
Feladat-terkep: projektek/szvetkomatek/4e/terkep_fgy_05-kombinatorika.md (jovahagyva 2026-09-28: a tiszta sorrend
n = 3, 4, 9, 10 elemmel; a nehez-4 x-mentes tagja maradhat a nehez savban — ellenorzoben SOHA; a kozep-11 (1+gyok2)^4
marad). Forrasok: Jokovic_4 (Szucs E.), 6. Feladatok - Kombinatorika, kombinatorika_gyakorlasra, Nemzeti, SM11, Vene 6.
Minden vegeredmeny ketfelekeppen: keplettel ES teljes felsorolassal (itertools) vagy sympyval; a felmerok adatai
(tiltott_4e_05) es a tananyag kidolgozott peldai kiszurve."""
import sys, os
from itertools import permutations, product, combinations
from math import comb, perm, factorial as fakt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
import tiltott
TILT = tiltott.modul("tiltott_4e_05")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)
import sympy
from sympy import symbols, expand, sqrt, Poly

x, a_, b_ = symbols("x a b")
T = dict(tagozat="4e", mappa="05-kombinatorika", temakor="Kombinatorika")
TINTA, KEK, HALV = "#0f172a", "#1d4ed8", "#94a3b8"
E = []                  # önteszt-hibák


def chk(nev, *ertekek):
    """Minden megadott úton ugyanaz jöjjön ki (képlet, felsorolás, sympy)."""
    if any(e != ertekek[0] for e in ertekek[1:]):
        E.append((nev, ertekek))
    return ertekek[0]


def N(n):
    """Szám a kulcsba: 10 000-től vékony szóközös tagolással."""
    s = str(abs(n))
    if abs(n) >= 10000:
        g = []
        while s:
            g.insert(0, s[-3:]); s = s[:-3]
        s = r"\,".join(g)
        return ("-" if n < 0 else "") + s
    return str(n)


def M(n):
    return f"${N(n)}$"


def szamok(jegyek, k, ism, felt=lambda p: True):
    it = product(jegyek, repeat=k) if ism else permutations(jegyek, k)
    return sum(1 for p in it if p[0] != 0 and felt(p))


def ertek(p):
    return int("".join(map(str, p)))


def pol(kif, valt=x):
    """sympy-kifejezés → TeX, csökkenő hatványok szerint."""
    # tömör alak (4x^{3}+6x^{2}), hogy a kulcs-önteszt az előjeles együtthatót egyben lássa
    return sympy.latex(expand(kif), order="lex").replace(" ", "")


# ================================================================ ALAP
A1 = chk("alap-1a", 3 * 4, len(list(product(range(3), range(4)))))
A1b = chk("alap-1b", 4 * 5 * 3, len(list(product(range(4), range(5), range(3)))))
A1c = chk("alap-1c", 6 * 6, len(list(product(range(1, 7), repeat=2))))
A1d = chk("alap-1d", 2 ** 3, len(list(product("FI", repeat=3))))
ALAP = [(
    "Számold ki a szorzási szabállyal!",
    ["$A$-ból $B$-be 3 út vezet, $B$-ből $C$-be 4. Hányféleképpen juthatunk el $A$-ból $C$-be, $B$-n keresztül?",
     "Egy étteremben 4-féle előétel, 5-féle főétel és 3-féle desszert közül lehet választani. Hányféle háromfogásos "
     "menü állítható össze?",
     "Egy piros és egy kék dobókockával dobunk. Hány különböző (piros, kék) eredménypár lehetséges?",
     "Egy érmét háromszor egymás után feldobunk. Hány különböző fej–írás sorozat lehetséges?"],
    [M(A1), M(A1b), M(A1c), M(A1d)])]

ALAP.append((
    "Nyalka Vili utazókönyvtárában 12 regény és 7 verseskötet áll, a kampusz-polcon pedig 3 matematika- és 5 "
    "fizikakönyv (mind különböző). Döntsd el, hogy a szorzási („ÉS”) vagy az összeadási („VAGY”) szabály kell-e, és "
    "számolj!",
    ["Vili egyetlen könyvet visz magával: egy regényt vagy egy verseskötetet.",
     "Vili egy regényt és egy verseskötetet visz magával.",
     "A kampusz-polcról egy könyvet vesz le: matematika- vagy fizikakönyvet.",
     "A kampusz-polcról egy matematika- és egy fizikakönyvet vesz le."],
    [f"VAGY: {M(chk('alap-2a', 12 + 7, len(range(12)) + len(range(7))))}",
     f"ÉS: {M(chk('alap-2b', 12 * 7, len(list(product(range(12), range(7))))))}",
     f"VAGY: {M(chk('alap-2c', 3 + 5, 8))}",
     f"ÉS: {M(chk('alap-2d', 3 * 5, len(list(product(range(3), range(5))))))}"]))

D = range(10)
ALAP.append((
    "Hány olyan pozitív egész szám van, amely",
    ["háromjegyű, és minden jegye páratlan?", "négyjegyű, és minden jegye páros?", "kétjegyű?", "négyjegyű?"],
    [M(chk("alap-3a", 5 ** 3, szamok([1, 3, 5, 7, 9], 3, True))),
     M(chk("alap-3b", 4 * 5 ** 3, szamok([0, 2, 4, 6, 8], 4, True))),
     M(chk("alap-3c", 9 * 10, szamok(D, 2, True))),
     M(chk("alap-3d", 9 * 10 ** 3, szamok(D, 4, True)))], True))

P123 = sorted("".join(map(str, p)) for p in permutations([1, 2, 3]))
P123_TX = ",\\ ".join(P123)
ALAP.append((
    "Sorba állítva:",
    ["Írd fel az $\\{1,2,3\\}$ halmaz elemeinek összes sorrendjét! Hány ilyen sorrend van?",
     "Hányféleképpen rakhatunk sorba 4 különböző könyvet a polcon?",
     "Hányféleképpen állhat sorba 9 különböző Vilmos-variáns a Multiverzum-tablóhoz?",
     "Hányféle sorrendben olvasható fel 10 különböző név?"],
    [f"${P123_TX}$ — {M(chk('alap-4a', fakt(3), len(P123)))} sorrend",
     M(chk("alap-4b", fakt(4), len(list(permutations(range(4)))))),
     M(chk('alap-4c', fakt(9), sum(1 for _ in permutations(range(9))))),
     M(chk('alap-4d', fakt(10), 3628800))]))

n = symbols("n", positive=True, integer=True)
ALAP.append((
    "Számold ki, illetve egyszerűsítsd!",
    ["$6!$", "$\\dfrac{8!}{6!}$", "$\\dfrac{10!}{8!\\cdot 2!}$", "$\\dfrac{(n+1)!}{n!}$"],
    [M(chk("alap-5a", fakt(6), 720)), M(chk("alap-5b", fakt(8) // fakt(6), 8 * 7)),
     M(chk("alap-5c", fakt(10) // (fakt(8) * fakt(2)), comb(10, 2))),
     f"${sympy.latex(sympy.simplify(sympy.factorial(n + 1) / sympy.factorial(n)))}$"], True))
if sympy.simplify(sympy.factorial(n + 1) / sympy.factorial(n)) != n + 1:
    E.append(("alap-5d", "n+1"))

ALAP.append((
    "Ismétléses permutáció: hány különböző sorrendje van a szó betűinek (értelmetlen betűsor is számít, és minden betűt "
    "pontosan annyiszor használunk, ahányszor a szóban szerepel)?",
    ["MAMA", "ALABAMA", "KEREKES",
     "3 piros és 2 kék golyót teszünk egy sorba (az egyforma színűek nem különböztethetők meg). Hány különböző "
     "színsorrend lehetséges?"],
    [M(chk("alap-6a", fakt(4) // (fakt(2) * fakt(2)), len(set(permutations("MAMA"))))),
     M(chk("alap-6b", fakt(7) // fakt(4), len(set(permutations("ALABAMA"))))),
     M(chk("alap-6c", fakt(7) // (fakt(2) * fakt(3)), len(set(permutations("KEREKES"))))),
     M(chk("alap-6d", fakt(5) // (fakt(3) * fakt(2)), len(set(permutations("PPPKK")))))]))

ALAP.append((
    "Dobogó és tisztségek:",
    ["Egy bajnokságon 12 csapat indul. Hányféleképpen oszthatják ki az arany-, az ezüst- és a bronzérmet (holtverseny "
     "nincs)?",
     "Egy 30 fős osztály elnököt, titkárt és pénztárost választ (egy tanuló legfeljebb egy tisztséget kaphat). "
     "Hányféleképpen?",
     "Hány olyan kétjegyű szám van, amelynek számjegyei különbözők, és az 1, 2, 3, 4, 5, 6, 7 számjegyek közül "
     "valók?"],
    [M(chk("alap-7a", perm(12, 3), len(list(permutations(range(12), 3))))),
     M(chk("alap-7b", perm(30, 3), 30 * 29 * 28)),
     M(chk("alap-7c", perm(7, 2), szamok(range(1, 8), 2, False)))]))

ALAP.append((
    "Ismétlés megengedett:",
    ["Egy év végi bizonyítványban 10 tantárgy szerepel, mindegyikből 1-es, 2-es, 3-as, 4-es vagy 5-ös osztályzat "
     "lehet. Hányféle bizonyítvány lehetséges?",
     "Hány olyan nyolcjegyű szám van, amelynek minden számjegye 1 vagy 2?",
     "A totószelvényen 13 mérkőzés eredményét kell tippelni: 1, X vagy 2. Hányféleképpen tölthető ki egy oszlop?",
     "Hány négyjegyű szám írható fel az 1, 2, 3, 4 számjegyekből, ha egy számjegy többször is szerepelhet?"],
    [M(chk('alap-8a', 5 ** 10, 9765625)),
     M(chk('alap-8b', 2 ** 8, szamok([1, 2], 8, True))),
     M(chk('alap-8c', 3 ** 13, 1594323)),
     M(chk('alap-8d', 4 ** 4, szamok([1, 2, 3, 4], 4, True)))]))

ALAP.append((
    "Az 1, 3, 6, 8, 9 számjegyekből négyjegyű, a 2, 5, 7 számjegyekből kétjegyű számokat képezünk. Hány szám "
    "képezhető, ha",
    ["négyjegyűt képezünk, és minden számjegy legfeljebb egyszer szerepelhet;",
     "négyjegyűt képezünk, és egy számjegy többször is szerepelhet;",
     "kétjegyűt képezünk, ismétlés nélkül;", "kétjegyűt képezünk, ismétléssel?"],
    [M(chk("alap-9a", perm(5, 4), szamok([1, 3, 6, 8, 9], 4, False))),
     M(chk("alap-9b", 5 ** 4, szamok([1, 3, 6, 8, 9], 4, True))),
     M(chk("alap-9c", perm(3, 2), szamok([2, 5, 7], 2, False))),
     M(chk("alap-9d", 3 ** 2, szamok([2, 5, 7], 2, True)))]))

ALAP.append((
    "Csapat, nem sorrend:",
    ["Egy 25 fős osztályból 3 egyenrangú tagot választanak a diákparlamentbe. Hányféleképpen?",
     "Egy kosárban 7 különböző színű labda van. Hányféleképpen vehetünk ki közülük 4-et?",
     "Egy találkozón 25 résztvevő mindegyike mindenkivel egyszer fog kezet. Hány kézfogás történik?",
     "Hány átlója van a konvex tízszögnek?"],
    [M(chk("alap-10a", comb(25, 3), len(list(combinations(range(25), 3))))),
     M(chk("alap-10b", comb(7, 4), len(list(combinations(range(7), 4))))),
     M(chk("alap-10c", comb(25, 2), len(list(combinations(range(25), 2))))),
     M(chk("alap-10d", comb(10, 2) - 10, sum(1 for i, j in combinations(range(10), 2) if (j - i) % 10 not in (1, 9))))]))

ALAP.append((
    "<b>Számít-e a sorrend?</b> Döntsd el, és számolj!",
    ["Egy 15 fős kórusból 4 egyenrangú szólistát választanak.",
     "Ugyanebből a kórusból egy szopránt, egy altot, egy tenort és egy basszust választanak (mindenki bármelyik "
     "szólamot el tudja énekelni, de csak egyet kaphat).",
     "Egy pontból 5 félegyenes indul. Hány szöget határoznak meg, ha bármely két félegyenes egy, legfeljebb "
     "$180^\\circ$-os szöget határoz meg?",
     "9 futó közül hányféleképpen alakulhat a dobogó (1., 2. és 3. hely)?"],
    [f"nem számít: {M(chk('alap-11a', comb(15, 4), len(list(combinations(range(15), 4)))))}",
     f"számít: {M(chk('alap-11b', perm(15, 4), len(list(permutations(range(15), 4)))))}",
     f"nem számít: {M(chk('alap-11c', comb(5, 2), len(list(combinations(range(5), 2)))))}",
     f"számít: {M(chk('alap-11d', perm(9, 3), len(list(permutations(range(9), 3)))))}"]))

ALAP.append((
    "Pontok, egyenesek, részhalmazok:",
    ["Egy egyenesen 5 pontot jelölünk meg. Hány olyan szakasz van, amelynek mindkét végpontja a megjelölt pontok "
     "közül való?",
     "A síkon 9 pont van, közülük semelyik 3 nem esik egy egyenesre. Hány egyenest határoznak meg?",
     "Hány háromszöget határoz meg ugyanez a 9 pont?",
     "Hány háromelemű részhalmaza van az $\\{1,2,\\ldots,8\\}$ halmaznak?"],
    [M(chk("alap-12a", comb(5, 2), len(list(combinations(range(5), 2))))),
     M(chk("alap-12b", comb(9, 2), len(list(combinations(range(9), 2))))),
     M(chk("alap-12c", comb(9, 3), len(list(combinations(range(9), 3))))),
     M(chk("alap-12d", comb(8, 3), len(list(combinations(range(1, 9), 3)))))]))

SOROK = ["\\ ".join(str(comb(r, k)) for k in range(r + 1)) for r in range(7)]
for r in range(7):
    chk(f"alap-13 sor {r}", [comb(r, k) for k in range(r + 1)],
        [int(c) for c in Poly(expand((a_ + b_) ** r), a_, b_).coeffs()] if r else [1])
ALAP.append((
    "A Pascal-háromszög és a kifejtés:",
    ["Írd fel a Pascal-háromszög 0–6. sorát!", "Fejtsd ki: $(x+1)^4$", "Fejtsd ki: $(a-b)^3$",
     "Fejtsd ki: $(x+3)^3$"],
    ["; ".join(f"${s}$" for s in SOROK),
     f"${pol((x + 1) ** 4)}$", f"${pol((a_ - b_) ** 3)}$", f"${pol((x + 3) ** 3)}$"]))

ALAP.append((
    "Binomiális együtthatók:",
    ["$\\binom72$", "$\\binom75$", "$\\binom80$", "$\\binom88$",
     "Hány részhalmaza van egy 6 elemű halmaznak?",
     "Számold ki az $1+5+10+10+5+1$ összeget, és írd fel 2 hatványaként!"],
    [M(chk("alap-14a", comb(7, 2), 21)), M(chk("alap-14b", comb(7, 5), comb(7, 2))), M(comb(8, 0)), M(comb(8, 8)),
     M(chk("alap-14e", 2 ** 6, sum(comb(6, k) for k in range(7)), len([s for k in range(7) for s in combinations(range(6), k)]))),
     f"$32=2^5$" if chk("alap-14f", 1 + 5 + 10 + 10 + 5 + 1, 2 ** 5) == 32 else "?"]))

# ================================================================ KÖZÉP
KOZEP = [(
    "Korlátozott helyek és komplementer — hány olyan pozitív egész szám van, amely",
    ["négyjegyű, és legalább egy számjegye 5-ös?", "háromjegyű, és az utolsó két számjegye megegyezik?",
     "négyjegyű, és osztható 5-tel?", "négyjegyű, és osztható 10-zel?"],
    [M(chk("kozep-1a", 9000 - 8 * 9 ** 3, sum(1 for v in range(1000, 10000) if "5" in str(v)))),
     M(chk("kozep-1b", 9 * 10, sum(1 for v in range(100, 1000) if str(v)[1] == str(v)[2]))),
     M(chk("kozep-1c", 9 * 10 * 10 * 2, sum(1 for v in range(1000, 10000) if v % 5 == 0))),
     M(chk("kozep-1d", 9 * 10 * 10, sum(1 for v in range(1000, 10000) if v % 10 == 0)))])]

KOZEP.append((
    "Modellezés:",
    ["Egy ország rendszámtábláin 2 betű (26-féle) után 4 számjegy áll; a betűk és a számjegyek is ismétlődhetnek. "
     "Hány különböző rendszám adható ki?",
     "Nyalka Vili előételnek vagy levest (3-féle), vagy salátát (2-féle) kér, aztán főételt (4-féle), végül vagy "
     "desszertet (3-féle), vagy kávét (2-féle). Hányféle menüt állíthat össze?"],
    [M(chk("kozep-2a", 26 ** 2 * 10 ** 4, 6760000)),
     M(chk("kozep-2b", (3 + 2) * 4 * (3 + 2), len(list(product(range(5), range(4), range(5))))))]))


def mellett(p, a, b):
    return abs(p.index(a) - p.index(b)) == 1


KOZEP.append((
    "Feltételes sorrend:",
    ["Az 1, 2, …, 9 számokat sorba rendezzük. Hány olyan sorrend van, amelyben az 1 és a 2 egymás mellett áll?",
     "4 fiú és 2 lány áll sorba úgy, hogy a két lány a sor két szélén álljon. Hányféleképpen?",
     "6 különböző könyvet teszünk a polcra úgy, hogy két adott könyv egymás mellé kerüljön. Hányféleképpen?",
     "5 ember áll sorba úgy, hogy két adott ember <b>ne</b> álljon egymás mellett. Hányféleképpen?"],
    [M(chk("kozep-3a", 2 * fakt(8), sum(1 for p in permutations(range(1, 10)) if mellett(p, 1, 2)))),
     M(chk("kozep-3b", 2 * fakt(4), sum(1 for p in permutations("FGHIKL") if {p[0], p[-1]} == {"K", "L"}))),
     M(chk("kozep-3c", 2 * fakt(5), sum(1 for p in permutations(range(6)) if mellett(p, 0, 1)))),
     M(chk("kozep-3d", fakt(5) - 2 * fakt(4), sum(1 for p in permutations(range(5)) if not mellett(p, 0, 1))))]))

KOZEP.append((
    "Minden számjegy pontosan egyszer:",
    ["Hány ötjegyű szám írható fel a 0, 1, 2, 3, 4 számjegyekből, ha mindegyiket pontosan egyszer használjuk?",
     "Hány páratlan ötjegyű szám írható fel az 1, 2, 3, 4, 5 számjegyekből, ha mindegyiket pontosan egyszer "
     "használjuk?",
     "A 0, 1, …, 9 számjegyeket egy sorba írjuk úgy, hogy az első öt helyen a páratlan jegyek álljanak. Hány ilyen "
     "sorrend van?"],
    [M(chk("kozep-4a", fakt(5) - fakt(4), szamok(range(5), 5, False))),
     M(chk("kozep-4b", 3 * fakt(4), szamok(range(1, 6), 5, False, lambda p: p[-1] % 2 == 1))),
     M(chk("kozep-4c", fakt(5) * fakt(5), len(list(permutations([1, 3, 5, 7, 9]))) * len(list(permutations([0, 2, 4, 6, 8])))))]))

KOZEP.append((
    "Ismétléses permutáció számjegyekkel és bábukkal:",
    ["Hány hétjegyű szám írható fel, amelyben az 1-es háromszor, a 2-es és a 3-as kétszer-kétszer szerepel (más jegy "
     "nem)?",
     "Hány hatjegyű szám írható fel, amelyben a 0 háromszor, az 1-es kétszer, a 2-es egyszer szerepel (más számjegy "
     "nem)?",
     "A sakktábla első sorába 2 bástyát, 2 futót, 2 huszárt, egy királyt és egy vezért állítunk. Hányféle sorrendben? "
     "(Az egyforma bábuk nem különböztethetők meg.)"],
    [M(chk("kozep-5a", fakt(7) // (fakt(3) * fakt(2) * fakt(2)), len({p for p in permutations([1, 1, 1, 2, 2, 3, 3])}))),
     M(chk("kozep-5b", fakt(6) // (fakt(3) * fakt(2)) - fakt(5) // (fakt(2) * fakt(2)),
           len({p for p in permutations([0, 0, 0, 1, 1, 2]) if p[0] != 0}))),
     M(chk("kozep-5c", fakt(8) // (fakt(2) ** 3), len(set(permutations("BBFFHHKV")))))]))

KOZEP.append((
    "Variáció feltétellel — hány olyan pozitív egész szám van, amely",
    ["ötjegyű, számjegyei különbözők, és a 0 nem szerepel benne?",
     "3000 és 5000 közé esik, és a számjegyei különbözők?",
     "négyjegyű, 5-tel kezdődik, és a 0, 1, …, 7 számjegyekből áll (egy számjegy többször is szerepelhet)?",
     "négyjegyű, 5-tel kezdődik, és a 0, 1, …, 7 számjegyekből áll, mindegyik legfeljebb egyszer?"],
    [M(chk("kozep-6a", perm(9, 5), szamok(range(1, 10), 5, False))),
     M(chk("kozep-6b", 2 * perm(9, 3), sum(1 for v in range(3001, 5000) if len(set(str(v))) == 4))),
     M(chk("kozep-6c", 8 ** 3, szamok(range(8), 4, True, lambda p: p[0] == 5))),
     M(chk("kozep-6d", perm(7, 3), szamok(range(8), 4, False, lambda p: p[0] == 5)))]))

KOZEP.append((
    "Ismétléses variáció és komplementer:",
    ["A Braille-írás egy jele 6 pontból áll, mindegyik pont kiemelt vagy sima. Hány különböző jel képezhető, ha "
     "legalább egy pontnak kiemeltnek kell lennie?",
     "5 különböző golyót 3 különböző (számozott) dobozba teszünk; egy dobozba több golyó is kerülhet, egy doboz "
     "üresen is maradhat. Hányféleképpen?",
     "Egy I.V.H.-széf zárján 3 tárcsa van, mindegyiken az A, B, C, D, E, F betűk. Hány olyan beállítás van, amelyben "
     "legalább két tárcsán ugyanaz a betű áll?",
     "Hány 5-re végződő ötjegyű szám írható fel az 1, 2, …, 9 számjegyekből, ha egy számjegy többször is "
     "szerepelhet?"],
    [M(chk("kozep-7a", 2 ** 6 - 1, sum(1 for p in product((0, 1), repeat=6) if any(p)))),
     M(chk("kozep-7b", 3 ** 5, len(list(product(range(3), repeat=5))))),
     M(chk('kozep-7c', 6 ** 3 - perm(6, 3), sum(1 for p in product("ABCDEF", repeat=3) if len(set(p)) < 3))),
     M(chk("kozep-7d", 9 ** 4, szamok(range(1, 10), 5, True, lambda p: p[-1] == 5)))]))

LANY, FIU = [("L", i) for i in range(12)], [("F", i) for i in range(11)]
KOZEP.append((
    "Két csoportból, pontosan:",
    ["Egy osztályba 12 lány és 11 fiú jár. Hányféleképpen választható ki közülük egy 3 lányból és 4 fiúból álló "
     "csapat?",
     "Egy 10 fős csapatból egy vezetőt és rajta kívül 4 (egyenrangú) képviselőt választanak. Hányféleképpen?",
     "Egy dobozban 6 piros és 4 kék golyó van (mind megkülönböztethető). Hányféleképpen húzhatunk ki 3 golyót úgy, "
     "hogy pontosan 1 kék legyen köztük?"],
    [M(chk("kozep-8a", comb(12, 3) * comb(11, 4), len(list(combinations(LANY, 3))) * len(list(combinations(FIU, 4))))),
     M(chk("kozep-8b", 10 * comb(9, 4), sum(1 for v in range(10) for _ in combinations([i for i in range(10) if i != v], 4)))),
     M(chk("kozep-8c", comb(4, 1) * comb(6, 2),
           sum(1 for c in combinations(["P"] * 6 + ["K"] * 4 and [("P", i) for i in range(6)] + [("K", i) for i in range(4)], 3)
               if sum(t == "K" for t, _ in c) == 1)))]))

EMB = [("F", i) for i in range(4)] + [("N", i) for i in range(4)]
CSOP = [("L", i) for i in range(16)] + [("F", i) for i in range(20)]
KOZEP.append((
    "Legalább, többség, kizárás:",
    ["4 férfi és 4 nő közül 5 fős bizottságot választanak úgy, hogy a nők legyenek többségben. Hányféleképpen?",
     "Egy 16 lányból és 20 fiúból álló csoportból 4 tanulót választanak. Hányféleképpen, ha legalább egy lánynak "
     "lennie kell köztük?",
     "12 versenyzőből 9-et kell kiválasztani, de két adott versenyző, $A$ és $B$ nem kerülhet be egyszerre. "
     "Hányféleképpen?"],
    [M(chk("kozep-9a", comb(4, 3) * comb(4, 2) + comb(4, 4) * comb(4, 1),
           sum(1 for c in combinations(EMB, 5) if sum(t == "N" for t, _ in c) >= 3))),
     M(chk("kozep-9b", comb(36, 4) - comb(20, 4), sum(1 for c in combinations(CSOP, 4) if any(t == "L" for t, _ in c)))),
     M(chk("kozep-9c", comb(12, 9) - comb(10, 7), sum(1 for c in combinations(range(12), 9) if not (0 in c and 1 in c))))]))

KOZEP.append((
    "Visszafelé — és „Mit rontott el Véd Vilmos?”",
    ["Egy sakkversenyen mindenki mindenkivel pontosan egyszer játszott, összesen 120 játszma volt. Hányan indultak?",
     "Egy csoportból 90-féleképpen választható elnök és elnökhelyettes (két különböző ember). Hány tagú a csoport?",
     "Véd Vilmos: „9 ember mindegyike mindenkivel egyszer fog kezet, ez $9\\cdot 8=72$ kézfogás.” Mit rontott el, és "
     "mennyi a helyes szám?"],
    [f"${chk('kozep-10a', *[n_ for n_ in range(2, 100) if comb(n_, 2) == 120])}$ versenyző",
     f"${chk('kozep-10b', *[n_ for n_ in range(2, 100) if perm(n_, 2) == 90])}$ tagú",
     f"minden kézfogást kétszer számolt (az $A$–$B$ és a $B$–$A$ ugyanaz); helyesen "
     f"{M(chk('kozep-10c', comb(9, 2), len(list(combinations(range(9), 2))), 9 * 8 // 2))}"]))

KOZEP.append((
    "Fejtsd ki a binomiális tétellel!",
    ["$(2x-1)^3$", "$(x+2)^5$", "$\\left(1+\\sqrt2\\right)^4$"],
    [f"${pol((2 * x - 1) ** 3)}$", f"${pol((x + 2) ** 5)}$",
     "$17+12\\sqrt2$"]))
if expand((1 + sqrt(2)) ** 4) != 17 + 12 * sqrt(2):
    E.append(("kozep-11c", expand((1 + sqrt(2)) ** 4)))

K12a = chk("kozep-12a", comb(6, 4) * 3 ** 4, Poly(expand((x + 3) ** 6), x).coeff_monomial(x ** 2))
K12b = chk("kozep-12b", comb(5, 2) * 2 ** 3, Poly(expand((2 * x + 1) ** 5), x).all_coeffs()[2])
KOZEP.append((
    "Egy tag, egy együttható:",
    ["Mennyi az $x^2$ együtthatója az $(x+3)^6$ kifejtésében?",
     "Írd fel a $(2x+1)^5$ kifejtésének harmadik tagját (az $x$ csökkenő hatványai szerint rendezve)!",
     "Véd Vilmos: „$(x+2)^3=x^3+3x^2+3x+8$.” Mit rontott el?"],
    [M(K12a), f"${K12b}x^3$",
     f"a két középső tagból kimaradt a $2$ hatványa (a $3x^2$ helyett $3\\cdot 2\\,x^2$, a $3x$ helyett "
     f"$3\\cdot 2^2x$ kell); helyesen ${pol((x + 2) ** 3)}$"]))

# ================================================================ NEHÉZ


def sorszam(szo):
    betuk = sorted(szo)
    return chk(f"nehez-1 {szo}", sorted("".join(p) for p in permutations(betuk)).index(szo) + 1,
               _sorszam_keplet(szo))


def _sorszam_keplet(szo):
    ki, marad = 0, sorted(szo)
    for i, b in enumerate(szo):
        ki += marad.index(b) * fakt(len(marad) - 1)
        marad.remove(b)
    return ki + 1


NEHEZ = [(
    "Szótári sorrend:",
    ["Az A, I, K, L, M betűk összes sorrendjét (mind az öt betűt felhasználva) ábécérendbe írjuk. Hányadik a MILKA?",
     "Az A, D, I, L, N, Z betűk összes sorrendjét ábécérendbe írjuk. Hányadik az IZLAND?"],
    [f"a ${sorszam('MILKA')}.$", f"a ${sorszam('IZLAND')}.$"])]

NEHEZ.append((
    "Esetszétválasztás — a 0 és a párosság:",
    ["Hány ötjegyű páros szám írható fel a 0, 1, 2, 3, 5 számjegyekből, ha mindegyiket pontosan egyszer használjuk?",
     "Hány páratlan ötjegyű szám van, amelynek jegyei különbözők?",
     "Hány négyjegyű páros szám írható fel a 0, 1, 2, 3, 4, 5, 8 számjegyekből, ha mindegyik legfeljebb egyszer "
     "szerepelhet?"],
    [M(chk("nehez-2a", fakt(4) + 3 * fakt(3), szamok([0, 1, 2, 3, 5], 5, False, lambda p: p[-1] % 2 == 0))),
     M(chk("nehez-2b", 5 * 8 * perm(8, 3), sum(1 for v in range(10000, 100000) if v % 2 and len(set(str(v))) == 5))),
     M(chk("nehez-2c", perm(6, 3) + 3 * 5 * perm(5, 2),
           szamok([0, 1, 2, 3, 4, 5, 8], 4, False, lambda p: p[-1] % 2 == 0)))]))

SZO = "VARIÁNS"
RACS = [[SZO[i + j] for j in range(4)] for i in range(4)]


def utak(m, n_):
    """rácsutak (m×n lépés) dinamikus programozással"""
    d = [[1] * (n_ + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n_ + 1):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[m][n_]


def kiolvas():
    """a VARIÁNS kiolvasásai a táblázatban (jobbra/le), teljes bejárással"""
    db = 0
    for lep in product("JL", repeat=6):
        i = j = 0; s = RACS[0][0]
        for l in lep:
            i, j = (i, j + 1) if l == "J" else (i + 1, j)
            if i > 3 or j > 3:
                s = None; break
            s += RACS[i][j]
        db += s == SZO
    return db


def svg_racs():
    c = 46
    g = [f'<rect x="{10 + j * c}" y="{10 + i * c}" width="{c}" height="{c}" fill="#fff" stroke="{TINTA}" stroke-width="1.5"/>'
         f'<text x="{10 + j * c + c / 2}" y="{10 + i * c + c / 2 + 7}" text-anchor="middle" font-size="20" '
         f'font-family="Georgia,serif" fill="{TINTA}">{RACS[i][j]}</text>' for i in range(4) for j in range(4)]
    return (f'<div class="svgwrap"><svg viewBox="0 0 {20 + 4 * c} {20 + 4 * c}" width="{20 + 4 * c}" role="img" '
            f'aria-label="4×4-es betűtábla: V A R I / A R I Á / R I Á N / I Á N S">{"".join(g)}</svg></div>')


NEHEZ.append((
    "Rácsutak:" + svg_racs(),
    ["A fenti táblázat bal felső sarkából indulva, minden lépésben jobbra vagy lefelé haladva olvassuk ki a VARIÁNS "
     "szót. Hányféleképpen tehetjük ezt meg?",
     "Egy bábu a sakktábla a1 mezőjéről a h8 mezőre megy; minden lépésben egy mezőt léphet jobbra vagy felfelé. "
     "Hányféle úton juthat el?"],
    [M(chk("nehez-3a", comb(6, 3), kiolvas(), utak(3, 3))), M(chk("nehez-3b", comb(14, 7), utak(7, 7)))]))


def konstans(kif):
    return Poly(sympy.expand(kif * x ** 40), x).coeff_monomial(x ** 40)


NEHEZ.append((
    "Határozd meg a kifejtésben az $x$-et nem tartalmazó tagot!",
    ["$\\left(x+\\dfrac1x\\right)^4$", "$\\left(x^2+\\dfrac1x\\right)^6$", "$\\left(2x-\\dfrac1x\\right)^6$"],
    [M(chk("nehez-4a", comb(4, 2), konstans((x + 1 / x) ** 4))),
     M(chk("nehez-4b", comb(6, 4), konstans((x ** 2 + 1 / x) ** 6))),
     M(chk("nehez-4c", -comb(6, 3) * 2 ** 3, konstans((2 * x - 1 / x) ** 6)))], True))


def teglalapok(k):
    vonal = range(k + 1)
    return sum(1 for x1, x2 in combinations(vonal, 2) for y1, y2 in combinations(vonal, 2))


def svg_halo():
    c, k = 36, 4
    v = "".join(f'<line x1="{10 + i * c}" y1="10" x2="{10 + i * c}" y2="{10 + k * c}" stroke="{TINTA}" stroke-width="1.5"/>'
                f'<line x1="10" y1="{10 + i * c}" x2="{10 + k * c}" y2="{10 + i * c}" stroke="{TINTA}" stroke-width="1.5"/>'
                for i in range(k + 1))
    return (f'<div class="svgwrap"><svg viewBox="0 0 {20 + k * c} {20 + k * c}" width="{20 + k * c}" role="img" '
            f'aria-label="4×4-es négyzetháló">{v}</svg></div>')


JOKER = ("Egy $4\\times4$-es négyzetrács 16 kis négyzetből áll (ábra). Hány olyan téglalap van, amelynek oldalai "
         "a rácsvonalakon fekszenek? (A négyzetek is téglalapok.)" + svg_halo(),
         M(chk("joker", comb(5, 2) ** 2, teglalapok(4))))

# ================================================================ ÖNELLENŐRZÉS
# tiltott adatok (a 4. ellenőrző 25/26-os és 26/27-es változatai): típus + paraméter
WEB = [("perm", 3), ("perm", 4), ("perm", 9), ("perm", 10),
       ("szamjegy", {1, 3, 5, 7, 9}), ("szamjegy", {0, 2, 4, 6, 8}), ("szamjegy", set(range(1, 8))),
       ("szamjegy", {1, 2}), ("szamjegy", {1, 2, 3, 4}), ("szamjegy", {1, 3, 6, 8, 9}), ("szamjegy", {2, 5, 7}),
       ("szamjegy", {0, 1, 2, 3, 4}), ("szamjegy", {1, 2, 3, 4, 5}), ("szamjegy", set(range(1, 10))),
       ("szamjegy", set(range(8))), ("szamjegy", {0, 1, 2, 3, 5}), ("szamjegy", {0, 1, 2, 3, 4, 5, 8}),
       ("szamjegy", {1, 2, 3}), ("szamjegy", {0, 1, 2}),
       ("szo", "MAMA"), ("szo", "ALABAMA"), ("szo", "KEREKES"), ("szo", "MILKA"), ("szo", "IZLAND"), ("szo", "VARIÁNS"),
       ("ismvar", (5, 10)), ("ismvar", (2, 8)), ("ismvar", (3, 13)), ("ismvar", (4, 4)), ("ismvar", (5, 4)),
       ("ismvar", (3, 2)), ("ismvar", (2, 6)), ("ismvar", (3, 5)), ("ismvar", (6, 3)), ("ismvar", (9, 4)),
       ("ismvar", (8, 3)), ("ismvar", (5, 3)), ("ismvar", (2, 3)), ("ismvar", (6, 2)),
       ("valaszt2", 25), ("valaszt2", 5), ("valaszt2", 9), ("valaszt2", 16), ("valaszt2", 10),
       ("komb", (25, 3)), ("komb", (7, 4)), ("komb", (15, 4)), ("komb", (9, 3)), ("komb", (8, 3)), ("komb", (12, 3)),
       ("komb", (11, 4)), ("komb", (9, 4)), ("komb", (6, 2)), ("komb", (36, 4)), ("komb", (20, 4)), ("komb", (12, 9)),
       ("komb", (10, 7)), ("komb", (5, 2)), ("komb", (4, 3)), ("komb", (4, 2)),
       ("binom", (1, 4)), ("binom", (3, 3)), ("binom", (2, 5)), ("binom", (3, 6)), ("binom", (2, 3))]
E += TILT.ellenoriz(WEB)
# a tananyag (build_tananyag_4e_05a/b) kidolgozott példái és kvízei: típus + paraméter
TANANYAG = {("perm", 3), ("perm", 4), ("szamjegy", frozenset({0, 1, 2, 3})), ("szamjegy", frozenset({2, 4, 5, 8})),
            ("szamjegy", frozenset({0, 1, 2, 3, 4})), ("szo", "ANNA"), ("szo", "MISSISSIPPI"), ("szo", "ÁRAD"),
            ("ismvar", (5, 2)), ("ismvar", (5, 3)), ("ismvar", (10, 4)), ("ismvar", (10, 3)), ("ismvar", (4, 3)),
            ("ismvar", (2, 4)), ("valaszt2", 10), ("valaszt2", 6), ("komb", (10, 2)), ("komb", (6, 2)),
            ("komb", (20, 3)), ("komb", (4, 3)), ("komb", (10, 3)), ("komb", (18, 4)), ("komb", (39, 7)),
            ("komb", (90, 5)), ("binom", (-2, 3)), ("binom", (2, 6)), ("binom", (3, 5)), ("binom", (1, 3)),
            ("binom", (2, 3))}
# tudatos átfedések: ugyanaz a paraméter, de MÁS kérdés (a térkép jóváhagyta)
ENGEDETT = {("perm", 3): "alap-4 a): felírás, a tananyagban az ABC betűkkel",
            ("perm", 4): "alap-4 b): könyvek, a tananyagban 4 variáns",
            ("szamjegy", frozenset({0, 1, 2, 3, 4})): "közép-4 a): ötjegyű, mind az öt jegy; a tananyagban páros háromjegyű",
            ("valaszt2", 10): "alap-10 d): tízszög átlói, közép-10 b): 90 → 10; a tananyagban 10 fő kézfogása",
            ("komb", (6, 2)): "közép-8 c): pontosan 1 kék (6 pirosból 2); a tananyagban 6 fő koccintása",
            ("komb", (4, 3)): "közép-9 a): nők többségben; a tananyagban 4-ből 3 (sorrend-kapcsoló)",
            ("ismvar", (5, 3)): "alap-3 a): háromjegyű, csupa páratlan jegy; a tananyagban 5 jelből 3 hosszú kód",
            ("binom", (2, 3)): "közép-12 c): Vilmos hibája $(x+2)^3$-ban; a tananyagban kvíz $(x+2)^3$ tagszámáról"}
for t_, p_ in WEB:
    kulcs = (t_, frozenset(p_) if isinstance(p_, set) else p_)
    if kulcs in TANANYAG and kulcs not in ENGEDETT:
        E.append(("tananyag-ütközés", kulcs))
assert not E, E
print("önteszt: OK |", len(ALAP), "alap,", len(KOZEP), "közép,", len(NEHEZ), "nehéz + joker; tiltott és tananyag rendben")


# ================================================================ OLDAL
def lista(A, K, N_, J):
    return "\n".join([
        '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(A, "alap", "alap"),
        '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(K, "kozep", "kozep"),
        '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(N_, "nehez", "nehez"),
        '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(J[0], J[1])])


if __name__ == "__main__":
    u = oldal(**T, fajl="feladatok-kombinatorika.html", cim="Zsoldos-lista — Kombinatorika",
              h1="Kombinatorika — Zsoldos-lista", itt="Zsoldos-lista — Kombinatorika",
              alcim="Szorzási és összeadási szabály, permutációk, variációk, kombinációk, a Pascal-háromszög és a "
                    "binomiális tétel. Minden feladat előtt két kérdés: számít-e a sorrend, és ismétlődhet-e egy elem? "
                    "A végeredmény lenyitható — előbb számolj!",
              sections_html=lista(ALAP, KOZEP, NEHEZ, JOKER), ossz_nev="Csalópapírt",
              prev="tananyag-binomialis-tetel.html", prevc="A Pascal-háromszög és a binomiális tétel",
              nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
    print("✓", os.path.basename(u), "|", len(ALAP), len(KOZEP), len(NEHEZ), "+ Joker")
