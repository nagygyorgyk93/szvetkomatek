# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/06 — Kristály-kamra (Vészterem, házi feladatsor)."""
from fractions import Fraction as F

FAJL = '3e/06-indukcio-sorozatok/feladatok-hazi.html'


def SZ(a1, d, n):
    return F(a1) + (n - 1)*F(d)


def SS(a1, d, n):
    return F(n, 2)*(2*F(a1) + (n - 1)*F(d))


def MB(b1, q, n):
    return F(b1)*F(q)**(n - 1)


def MSU(b1, q, n):
    return F(b1)*(F(q)**n - 1)/(F(q) - 1)


def v(*e):
    return [('', x) for x in e]


def vegso(vartak, *helyek):
    # A kifejezés továbbra is függetlenül számol; csak a köztes értékek maradnak ki.
    return [vartak[i] for i in helyek]


TESZT = {
    'alap-1': v(*[F(k + 4, 2*k) for k in range(1, 5)]),
    'alap-2': vegso(v('novevo', 'korlatos'), 1),
    'alap-3': v(SZ(-4, 6, 20), SS(-4, 6, 20), *[SZ(-4, 6, k) for k in range(1, 5)], 6, -10, 6),
    'alap-4': v(MB(-3, 2, 7), MSU(-3, 2, 7)),
    'alap-5': v(120000, F('1.06'), 127200, 120000, F('1.03'), 2, F('127308')),
    'kozep-1': v(SS(1, 4, 16)),
    'kozep-2': v(SZ(3, 5, 12)),
    'kozep-3': v(2, 5, *[MB(5, 2, k) for k in range(1, 5)], MSU(5, 2, 6)),
    'nehez-1': v(6, -7, *[SZ(-7, 6, k) for k in range(1, 5)]),
    'nehez-2': v(F('12.5'), 6, 36),
}
