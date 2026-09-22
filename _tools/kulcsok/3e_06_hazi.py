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


TESZT = {
    'alap-1': v(*[F(k + 4, 2*k) for k in range(1, 5)]),
    'alap-2': v(3, 2, 5, 3, 2, 5, 'novekvo'),
    'alap-3': v(SZ(-4, 6, 20), SS(-4, 6, 20), *[SZ(-4, 6, k) for k in range(1, 5)], 6, -10, 6),
    'alap-4': v(MB(-3, 2, 7), MSU(-3, 2, 7)),
    'alap-5': v(120000, F('1.06'), 127200, 120000, F('1.03'), 2, F('127308')),
    'kozep-1': v(F(61 - 25, 16 - 7), 25 - 6*F(61 - 25, 16 - 7), SS(1, 4, 16)),
    'kozep-2': v(12, SZ(3, 5, 12)),
    'kozep-3': v(2, 5, *[MB(5, 2, k) for k in range(1, 5)], MSU(5, 2, 6)),
    'nehez-1': v(6, -7, *[SZ(-7, 6, k) for k in range(1, 5)]),
    'nehez-2': v(5, 400, F(1, 2), 5, F('12.5'), 6, 36, F('6.25')),
}
