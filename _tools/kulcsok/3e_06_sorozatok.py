# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/06 — sorozatok (egyetlen gyűjtemény).

A várt értékeket ITT számoljuk ki, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F

FAJL = '3e/06-indukcio-sorozatok/feladatok-sorozatok.html'


def SZ(a1, d, n):
    return F(a1) + (n - 1)*F(d)


def SS(a1, d, n):
    return F(n, 2)*(2*F(a1) + (n - 1)*F(d))


def MB(b1, q, n):
    return F(b1)*F(q)**(n - 1)


def MSU(b1, q, n):
    return F(b1)*(F(q)**n - 1)/(F(q) - 1)


def v(*ertekek):
    """(betűjel nélküli) várt értékek sorrendben."""
    return [('', e) for e in ertekek]


def tagok(f, n):
    return [f(k) for k in range(1, n + 1)]


TESZT = {
    # --- A1: a sorozat fogalma
    'alap-1': v(*tagok(lambda k: F(3*k + 1, k + 2), 5), *tagok(lambda k: F(6*k, 2*k - 1), 5),
                *tagok(lambda k: F((-1)**k, k*k + 1), 5), *tagok(lambda k: F(k*k, 2**k), 5)),
    'alap-2': v(3, 5, 9, 15, 23, 1, 3, 7, 15, 31),
    'alap-3': v(7, 5, 17, 0),
    'alap-4': v(*tagok(lambda k: 2*k - 5, 6), 3),
    'alap-5': v(7*5 - 5, 7*6 - 5, 2*3**4, 2*3**5, 25, 36),
    'alap-6': v(10, 'nem tagja'),
    'alap-7': v('novekvo', 'csokkeno', 'nem monoton'),
    'alap-8': v(*tagok(lambda k: k*k - k, 4), *tagok(lambda k: F(2*k + 3, k), 4), 'csokkeno'),
    'alap-9': v(3, 4, -1, 1, 1, 'nem korlatos'),
    'alap-10': v(0, 2, 1, 6, 'nem monoton'),
    'alap-11': v(1, 0, -1, -2, F(5, 2), F(8, 3), 3),
    'alap-12': v(-1, F(1, 2), F(-1, 3), F(1, 4), 'nem monoton'),
    # --- B1: számtani sorozat
    'alap-13': v(*[SZ(a, d, k) for a, d in [(3, 2), (-2, 5), (7, -3), (-5, -2)] for k in range(1, 5)]),
    'alap-14': v(SZ(3, 4, 8), SZ(-5, 2, 12), SZ(4, F(-1, 4), 13), SZ(-5, -2, 16)),
    'alap-15': v(SS(1, 3, 12), SS(-8, 5, 36)),
    'alap-16': v(SZ(2, 6, 15), SS(2, 6, 27)),
    'alap-17': v(SZ(12, -3, 12), SS(12, -3, 36)),
    'alap-18': v(7, SS(-5, 3, 7), 5, SS(-1, -3, 5), 12, SS(4, 7, 12), 16, SS(3, -5, 16)),
    'alap-19': v(SZ(7, 3, 20), SS(7, 3, 20), SZ(3, 6, 28), SS(3, 6, 28),
                 SZ(-6, -3, 27), SS(-6, -3, 27), SZ(-1, 2, 16), SS(-1, 2, 16)),
    'alap-20': v(F(3 + 11, 2), 12 + (12 - 5)),
    # --- B2: mértani sorozat és kamat
    'alap-21': v(*[MB(b, q, k) for b, q in [(2, 3), (3, F(-1, 3)), (1, -2), (-4, 2)]
                   for k in range(1, 5)]),
    'alap-22': v(3, *[MB(5, 3, k) for k in range(1, 6)], -3, *[MB(3, -3, k) for k in range(1, 6)],
                 F(3, 4), *[MB(F(2, 3), F(3, 4), k) for k in range(1, 6)],
                 -2, *[MB(-6, -2, k) for k in range(1, 6)]),
    'alap-23': v(MB(-1, 3, 8), MB(-5, -2, 6), MB(F(-3, 2), -4, 4), MB(2, 4, 5)),
    'alap-24': v(MSU(2, -2, 9)),
    'alap-25': v(6, MSU(3, 4, 6), 4, MSU(27, F(2, 3), 4)),
    'alap-26': v(MB(2, -4, 4), MSU(2, -4, 4), MB(1, 3, 6), MSU(1, 3, 6),
                 MB(-1, 5, 5), MSU(-1, 5, 5), MB(3, F(1, 3), 4), MSU(3, F(1, 3), 4)),
    'alap-27': v(10, -10, 6, -6),
    'alap-28': v(80000*(1 + F(5, 100)*3), F(round(80000*F(105, 100)**3, 2))),
    # --- közép
    'kozep-1': v(*[SZ(2, 3, k) for k in range(1, 6)]),
    'kozep-2': v(2**16 - 1, 2**16),
    'kozep-3': v(3, 4),
    'kozep-4': v((4 - 1)*(4 - 2)*(4 - 3) + 2*4 - 1),
    'kozep-5': v(F(1, 2), 2),
    'kozep-6': v(F(1, 2), 1),
    'kozep-7': v(3, F(3, 2), 2, F(9, 4), 3),
    'kozep-8': v(*tagok(lambda k: k*k - 12*k + 40, 8), 6),
    'kozep-9': v(5, 3, *[SZ(3, 5, k) for k in range(1, 5)],
                 -2, 12, *[SZ(12, -2, k) for k in range(1, 5)]),
    'kozep-10': v(-3, 18, SS(18, -3, 18)),
    'kozep-11': v(7, -6, *[SZ(-6, 7, k) for k in range(1, 6)]),
    'kozep-12': v(3, 2, 8, -3, 5, 3),
    'kozep-13': v(SZ(5, 3, 8), SZ(4, 5, 8), SZ(-3, 4, 10)),
    'kozep-14': v(20, SZ(3, 1, 20), 4, SZ(18, -3, 4), 9, SZ(18, -3, 9),
                  10, SZ(2, 5, 10), 15, SZ(-2, -5, 15)),
    'kozep-15': v(5, MB(2, F(1, 2), 5), 4, MB(2, -3, 4)),
    'kozep-16': v(*[MB(b, q, k) for b, q in [(4, 2), (-5, -2), (-3, -3), (F(2, 3), 3)]
                    for k in range(1, 5)],
                  *[MB(F(-2, 3), -3, k) for k in range(1, 5)]),
    'kozep-17': v(*[MB(-4, 2, k) for k in range(1, 5)], *[MB(1, 3, k) for k in range(1, 5)],
                  *[MB(1, -3, k) for k in range(1, 5)], *[MB(1, 3, k) for k in range(1, 5)]),
    'kozep-18': v(MB(3, 2, 6), MB(2, 3, 6), MB(4, 2, 9)),
    'kozep-19': v(3, 3, *[MB(3, 3, k) for k in range(1, 5)]),
    'kozep-20': v(F('79031.45'), F('126973.46')),
    # --- nehéz
    'nehez-1': v(10, 1, 3),
    'nehez-2': v(1, 3, *[SZ(1, 3, k) for k in range(1, 5)]),
    'nehez-3': v(105, 994, 128, SS(105, 7, 128)),
    'nehez-4': v(3, 2, MB(2, 3, 6), MB(2, 3, 7), 7),
    'nehez-5': v(4, 2, 4, -2, -16, F(1, 2), -16, F(-1, 2)),
    'nehez-6': v(50*3**7, 50*3**6, 50*3**10, 50*3**9),
    'nehez-7': v(2, 6, 18, 3, 12, 21, 9),
    'nehez-8': v(13),
    'joker': v(F('102.4'), 42),
}
