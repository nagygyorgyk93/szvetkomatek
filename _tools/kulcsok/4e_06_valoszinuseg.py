# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/06 — Zsoldos-lista, valószínűség.

A várt értékeket ITT számoljuk ki, zárt képlettel (klasszikus modell, komplementer, binomiális képlet), a builder
felsorolásos számolásától függetlenül. A valós adatok nyers darabszámai kézzel átírva a forrásokból (RZS Popis 2022,
Eurostat demo_fasec, titanic3, Open-Meteo ERA5); a kerekítést felfelé-kerekítéssel (ROUND_HALF_UP) végezzük a pontos
törtből. A tisztán szimbolikus kulcsokat (eseményalgebra) nem nézzük."""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
from math import comb

FAJL = '4e/06-valoszinuseg-statisztika/feladatok-valoszinuseg.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


def k(x, j=3):
    """a kulcsban kiírt kerekített érték (pontos törtből vagy lebegőpontos számból)"""
    x = F(x) if not isinstance(x, float) else F(repr(x))
    d = Decimal(x.numerator) / Decimal(x.denominator)
    return F(str(d.quantize(Decimal(1).scaleb(-j), rounding=ROUND_HALF_UP)))


def bin_(n, p, i):
    return comb(n, i) * p ** i * (1 - p) ** (n - i)


# nyers darabszámok
HAZTARTAS_SZ, EGYSZEMELYES = 52491, 17702                  # Szabadka, 2022
SG_OSSZ, SG_NO, SG_ISM, SG_NO_ISM = 105873, 55593, 45792, 24786   # Szabadka, 15+ évesek
HU24_OSSZ, HU24_FIU = 78868, 40840                          # Magyarország, 2024
JUL_ESO, EVES_MELEG = 3, 58                                 # Szabadka 2024: esős júliusi nap, 25 °C feletti nap
TIT_UTAS, TIT_TULELO = 1309, 339 + 161
TIT_1, TIT_3 = (200, 123), (181, 528)                       # (túlélt, nem élte túl)
P_FIU_RS = F(516, 1000)

PRIM, PARATLAN, KOCKA = {2, 3, 5}, {1, 3, 5}, set(range(1, 7))
_osszeg9 = [(a, b) for a in KOCKA for b in KOCKA if a + b >= 9]

TESZT = {
    'alap-1': v(2 * 6, 2 ** 3, len(set("MATEK")), comb(3, 2)),
    'alap-2': v(*sorted(PRIM | PARATLAN), *sorted(PRIM & PARATLAN), *sorted(KOCKA - PRIM), *sorted(PARATLAN - PRIM),
                'nem'),
    'alap-4': v(F(4, 6), F(30 // 4, 30), F(15 - 6, 15), F(sum("MATEMATIKA".count(b) for b in "AEI"), 10),
                k(F(EGYSZEMELYES, HAZTARTAS_SZ))),
    'alap-5': v(1 - F(35, 100), F(4 + 8 - 1, 32), F(2, 10) + F(45, 100), F(5, 10) + F(4, 10) - F(1, 10), 1 - P_FIU_RS),
    'alap-6': v(k(F(HU24_FIU, HU24_OSSZ)), F(JUL_ESO, 31), k(F(JUL_ESO, 31)), F(EVES_MELEG, 366),
                k(F(EVES_MELEG, 366))),
    'alap-7': v(k(F(SG_NO, SG_OSSZ)), k(F(SG_ISM, SG_OSSZ)), k(F(SG_NO_ISM, SG_OSSZ))),
    'alap-8': v(F(1, 2) * F(1, 6), F(1, 2) ** 2, F(7, 10) * F(6, 10), k(P_FIU_RS ** 2)),
    'alap-9': v(bin_(4, F(1, 2), 2), bin_(3, F(1, 6), 1), F(1, 2) ** 5, k(bin_(3, P_FIU_RS, 2))),
    'alap-10': v('igen nem igen nem'),
    'alap-11': v(*[F(comb(3, i), 8) for i in range(4)], 1 - F(1, 10) - F(35, 100) - F(15, 100)),
    'alap-12': v(3 * F(1, 2), F(35, 100) + 2 * F(4, 10) + 3 * F(15, 100), F(2, 10) + 2 * F(5, 10) + 5 * F(3, 10)),
    'kozep-2': v(2 ** 4, 6 ** 3, comb(35, 5), 10 ** 3),
    'kozep-3': v(F(comb(6, 3), comb(10, 3)), F(comb(6, 2) * 4, comb(10, 3)), F(comb(6, 3) * comb(4, 2), comb(10, 5)),
                 k(F(comb(TIT_TULELO, 2), comb(TIT_UTAS, 2)))),
    'kozep-4': v(F(50 + 20 - 10, 100), F(2, 10) + F(9, 100) - F(1, 100), F(2, 10) - F(1, 100),
                 F(2, 10) + F(9, 100) - 2 * F(1, 100), k(F(SG_NO + SG_ISM - SG_NO_ISM, SG_OSSZ))),
    'kozep-5': v(F(sum(1 for p in _osszeg9 if 4 in p), len(_osszeg9)), 'nem', F(8, 32),
                 k(F(SG_NO_ISM, SG_NO)), k(F(SG_NO_ISM, SG_ISM))),
    'kozep-6': v(1 - F(5, 6) ** 3, k(1 - F(5, 6) ** 3), 1 - F(6, 10) ** 3, k(1 - F(95, 100) ** 4),
                 k(1 - (1 - F(JUL_ESO, 31)) ** 7)),
    'kozep-7': v(k(bin_(10, F(8, 10), 8)), k(bin_(9, F(9, 10), 7)), k(F(831, 1000) ** 5)),
    'kozep-8': v(k(1 - F(98, 100) ** 19), k(bin_(19, F(2, 100), 1)), sum(bin_(5, F(1, 4), i) for i in (3, 4, 5)),
                 k(sum(bin_(5, F(1, 4), i) for i in (3, 4, 5))), k(bin_(5, P_FIU_RS, 0) + bin_(5, P_FIU_RS, 1))),
    'kozep-9': v(F(800, 36) + F(5 * 150, 36) - 50, k(F(800, 36) + F(5 * 150, 36) - 50, 2), 'nem'),
    'kozep-10': v(*[F(2 * i - 1, 36) for i in range(1, 7)], sum(F(i * (2 * i - 1), 36) for i in range(1, 7)),
                  k(sum(F(i * (2 * i - 1), 36) for i in range(1, 7)), 2),
                  *[bin_(2, F(4, 5), i) for i in range(3)], 2 * F(4, 5)),
    'nehez-1': v(k(F(TIT_1[0], sum(TIT_1))), k(F(TIT_3[0], sum(TIT_3))), F(TIT_1[0], TIT_TULELO), 'nem',
                 k(F(TIT_3[0], TIT_TULELO)), k(F(TIT_3[0], sum(TIT_3)))),
    'nehez-2': v(k(sum(bin_(9, F(9, 10), i) for i in (7, 8, 9))),
                 min(n for n in range(1, 100) if F(4, 5) ** n <= F(1, 10))),
    'nehez-3': v(20 * F(6, 10) - 10 * F(4, 10), 50 * F(3, 10) - 20 * F(2, 10),
                 (20 - 8) ** 2 * F(6, 10) + (-10 - 8) ** 2 * F(4, 10),
                 (50 - 11) ** 2 * F(3, 10) + 11 ** 2 * F(5, 10) + (-20 - 11) ** 2 * F(2, 10),
                 k(216 ** 0.5, 1), k(709 ** 0.5, 1), 'nagyobb várható nyereség: a 2.; kevésbé kockázatos: az 1.'),
    'joker': v(F(1, 3), F(2, 3), 'érdemes váltani'),
}
