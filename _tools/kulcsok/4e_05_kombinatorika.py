# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/05 — Zsoldos-lista (kombinatorika + binomiális tétel).

A várt értékeket ITT számoljuk ki — zárt képlettel (math.comb / math.perm / hatványok), a builder felsorolásos és
sympy-s számolásától függetlenül. A kifejtéseknél a kijelzett együtthatókat soroljuk fel, a szövegbeli sorrendben
(az 1 és a −1 együttható nem látszik, a konstans tag igen)."""
from math import comb, perm, factorial as fakt

FAJL = '4e/05-kombinatorika/feladatok-kombinatorika.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


def kifejtes(n, a=1, b=1):
    """(a·x + b)^n látható együtthatói, csökkenő hatványok szerint."""
    ki = []
    for k in range(n + 1):                 # x^(n-k) együtthatója: C(n,k)·a^(n-k)·b^k
        c = comb(n, k) * a ** (n - k) * b ** k
        if n - k == 0 or abs(c) != 1:
            ki.append(c)
    return ki


def ism_perm(*db):
    return fakt(sum(db)) // __import__('math').prod(fakt(d) for d in db)


TESZT = {
    'alap-1': v(3 * 4, 4 * 5 * 3, 6 ** 2, 2 ** 3),
    'alap-2': v(12 + 7, 12 * 7, 3 + 5, 3 * 5),
    'alap-3': v(5 ** 3, 4 * 5 ** 3, 90, 9000),
    'alap-4': v(123, 132, 213, 231, 312, 321, fakt(3), fakt(4), fakt(9), fakt(10)),
    'alap-5': v(fakt(6), fakt(8) // fakt(6), comb(10, 2), 1),
    'alap-6': v(ism_perm(2, 2), ism_perm(4, 1, 1, 1), ism_perm(2, 3, 1, 1), ism_perm(3, 2)),
    'alap-7': v(perm(12, 3), perm(30, 3), perm(7, 2)),
    'alap-8': v(5 ** 10, 2 ** 8, 3 ** 13, 4 ** 4),
    'alap-9': v(perm(5, 4), 5 ** 4, perm(3, 2), 3 ** 2),
    'alap-10': v(comb(25, 3), comb(7, 4), comb(25, 2), 10 * 7 // 2),
    'alap-11': v(comb(15, 4), perm(15, 4), comb(5, 2), perm(9, 3)),
    'alap-12': v(comb(5, 2), comb(9, 2), comb(9, 3), comb(8, 3)),
    'alap-13': v(*[comb(6, k) for k in range(7)], *kifejtes(4), -comb(3, 1), comb(3, 2), *kifejtes(3, 1, 3)),   # (a−b)^3: csak a −3 és a 3 látszik
    'alap-14': v(comb(7, 2), comb(7, 5), comb(8, 0), comb(8, 8), 2 ** 6, 2 ** 5),
    'kozep-1': v(9000 - 8 * 9 ** 3, 9 * 10, 9000 // 5, 9000 // 10),
    'kozep-2': v(26 ** 2 * 10 ** 4, 5 * 4 * 5),
    'kozep-3': v(2 * fakt(8), 2 * fakt(4), 2 * fakt(5), fakt(5) - 2 * fakt(4)),
    'kozep-4': v(4 * fakt(4), 3 * fakt(4), fakt(5) ** 2),
    'kozep-5': v(ism_perm(3, 2, 2), ism_perm(3, 2, 1) - ism_perm(2, 2, 1), ism_perm(2, 2, 2, 1, 1)),
    'kozep-6': v(perm(9, 5), 2 * 9 * 8 * 7, 8 ** 3, perm(7, 3)),
    'kozep-7': v(2 ** 6 - 1, 3 ** 5, 6 ** 3 - 6 * 5 * 4, 9 ** 4),   # c) összes − csupa különböző betű
    'kozep-8': v(comb(12, 3) * comb(11, 4), 10 * comb(9, 4), 4 * comb(6, 2)),
    'kozep-9': v(comb(4, 3) * comb(4, 2) + comb(4, 1), comb(36, 4) - comb(20, 4), comb(12, 9) - comb(10, 7)),
    'kozep-10': v(next(n for n in range(2, 99) if n * (n - 1) == 240), next(n for n in range(2, 99) if n * (n - 1) == 90),
                  9 * 8 // 2),
    'kozep-11': v(*kifejtes(3, 2, -1), *kifejtes(5, 1, 2), 1 + 6 * 2 + 4, 4 + 4 * 2),   # (1+√2)^4 = 17 + 12√2
    'kozep-12': v(comb(6, 4) * 3 ** 4, comb(5, 2) * 2 ** 3, *kifejtes(3, 1, 2)[1:]),
    'nehez-1': v(4 * fakt(4) + 1 * fakt(3) + 2 * fakt(2) + 1 + 1,
                 2 * fakt(5) + 4 * fakt(4) + 2 * fakt(3) + 0 + 1 + 1),
    'nehez-2': v(fakt(4) + 3 * fakt(3), 5 * 8 * 8 * 7 * 6, 6 * 5 * 4 + 3 * 5 * 5 * 4),  # a) 0 | 2 a végén
    'nehez-3': v(comb(6, 3), comb(14, 7)),
    'nehez-4': v(comb(4, 2), comb(6, 4), comb(6, 3) * 2 ** 3 * (-1) ** 3),
    'joker': v(comb(5, 2) ** 2),
}
