# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/05 — I.V.H. Kihallgató Terem (házi).

Zárt képletekkel (math.comb / math.perm / faktoriális), a builder felsorolásos számolásától függetlenül; a
kifejtésnél a látható együtthatók a szövegbeli sorrendben."""
from math import comb, perm, factorial as fakt

FAJL = '4e/05-kombinatorika/feladatok-hazi.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


TESZT = {
    'alap-1': v(6 * 4, 6 * 4 * 3, 6 + 3),
    'alap-2': v(fakt(6) // fakt(2), fakt(5) // (fakt(3) * fakt(2)), fakt(5) // fakt(3)),
    'alap-3': v(perm(13, 2), comb(13, 2), 13 - 1),
    'alap-4': v(*[comb(3, k) * 4 ** k for k in (1, 2, 3)], comb(9, 2), comb(9, 7), 9 + 1),   # (x+4)^3: 12, 48, 64
    'kozep-1': v(5 * 5 * 4, 5 * 4 + 4 * 4),              # b) 0-ra | 5-re végződik
    'kozep-2': v(comb(5, 2) * comb(7, 2), comb(12, 4) - comb(7, 4)),
    'nehez-1': v(comb(9, 4), comb(10, 4)),               # növekvő: 0 nélkül | csökkenő: a 0 is lehet (a végén)
}
