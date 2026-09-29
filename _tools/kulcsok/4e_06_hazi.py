# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/06 — I.V.H. Kihallgató Terem (házi).

Zárt képletekkel (klasszikus modell, unió, súlyozott átlag, binomiális képlet, 1/n-es szórás), a builder felsorolásos
számolásától függetlenül. Nyers adatok kézzel átírva: Split 2024 esős napjai havonta és Szabadka 2024 napjainak
meleg × esős táblázata (Open-Meteo ERA5). Kerekítés: ROUND_HALF_UP a pontos értékből."""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
from math import comb

FAJL = '4e/06-valoszinuseg-statisztika/feladatok-hazi.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


def k(x, j=3):
    x = F(x) if not isinstance(x, float) else F(repr(x))
    d = Decimal(x.numerator) / Decimal(x.denominator)
    return F(str(d.quantize(Decimal(1).scaleb(-j), rounding=ROUND_HALF_UP)))


def bin_(n, p, i):
    return comb(n, i) * p ** i * (1 - p) ** (n - i)


def szoras(xs):
    a = F(sum(xs), len(xs))
    return (sum((x - a) ** 2 for x in xs) / len(xs)) ** 0.5


SPLIT_ESO = [12, 8, 16, 6, 15, 9, 1, 5, 10, 10, 7, 9]
MELEG_ESOS, MELEG_SZARAZ, HUVOS_ESOS, HUVOS_SZARAZ = 3, 55, 76, 232
TESTVER = {0: 4, 1: 10, 2: 7, 3: 3, 4: 1}
ANDRAS, BENCE = [8, 9, 7, 8, 8], [10, 6, 9, 5, 10]
SORSJEGY = {20000: 1, 2000: 5, 200: 50, 0: 944}
_n = sum(TESTVER.values())
_rendezett = sorted(x for x, f in TESTVER.items() for _ in range(f))
_kifiz = F(sum(x * db for x, db in SORSJEGY.items()), 1000)

TESZT = {
    'alap-1': v(F(5, 7 + 5 + 3), 1 - F(3, 15), F(7 + 3, 15), 0),
    'alap-2': v(F(16 + 10 - 5, 28), 1 - F(16 + 10 - 5, 28), F(10 - 5, 28)),
    'alap-3': v(F(sum(x * f for x, f in TESTVER.items()), _n), _rendezett[_n // 2],
                max(TESTVER, key=TESTVER.get), 100 * F(TESTVER[2], _n)),
    'alap-4': v('márciusban', max(SPLIT_ESO), 'júliusban', min(SPLIT_ESO), sum(SPLIT_ESO), F(sum(SPLIT_ESO), 12),
                k(F(sum(SPLIT_ESO), 366))),
    'kozep-1': v(k(F(MELEG_ESOS, MELEG_ESOS + MELEG_SZARAZ)), k(F(HUVOS_ESOS, HUVOS_ESOS + HUVOS_SZARAZ)), 'nem',
                 k(F(MELEG_ESOS, MELEG_ESOS + HUVOS_ESOS))),
    'kozep-2': v(bin_(4, F(7, 10), 3), bin_(4, F(7, 10), 3) + bin_(4, F(7, 10), 4), 1 - F(3, 10) ** 4),
    'kozep-3': v(F(sum(ANDRAS), 5), F(sum(BENCE), 5), k(szoras(ANDRAS), 2), k(szoras(BENCE), 2),
                 sorted(ANDRAS)[2], sorted(BENCE)[2], 'Andrást'),
    'nehez-1': v(20000 - 100, F(1, 1000), 2000 - 100, F(5, 1000), 200 - 100, F(50, 1000), -100, F(944, 1000),
                 _kifiz - 100, _kifiz, 1000 * 100 - 1000 * _kifiz),
}
