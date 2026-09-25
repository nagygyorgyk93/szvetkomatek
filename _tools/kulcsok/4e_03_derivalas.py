# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/03 — Zsoldos-lista I. (deriválás).

Független forrás: a deriváltak együtthatói a 0_Feladatok (javított) kulcsából, a számértékek (f'(x0), érintők,
sebesség) itt, törtekkel és numerikus deriválással (mpmath) újraszámolva — a builder sympy-számolásától függetlenül.
A sympy-latex a mínuszjel után szóközt tesz, ezért a kifejezés-kulcsoknál az együtthatók abszolút értékét
(sorrendben) ellenőrizzük; a kézzel írt kulcsoknál előjelesen."""
import math
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/03-derivalt/feladatok-derivalas.html'
mp.mp.dps = 40


def v(*ertekek):
    return [('', e) for e in ertekek]


def d(f, x0, n=1):
    return mp.diff(f, x0, n)


def racio(b, max_nev=1000):
    r = F(mp.nstr(b, 30, min_fixed=-mp.inf, max_fixed=mp.inf)).limit_denominator(max_nev)
    assert abs(b - mp.mpf(r.numerator) / r.denominator) < mp.mpf(10) ** -15, (b, r)
    return r


def erinto(f, x0):
    """(y0, m, b): az érintő y = m·x + b alakban, numerikus deriválással."""
    y0, m = racio(f(mp.mpf(x0))), racio(d(f, mp.mpf(x0)))
    return y0, m, y0 - m * F(x0)


# 16.: növekmény
def novekmeny(f, x0, dx):
    dy = f(x0 + dx) - f(x0)
    return F(str(round(dy, 2))), F(str(round(dy / dx, 2)))


N16 = [novekmeny(lambda t: t * t, 1, 0.5), novekmeny(lambda t: t * t, 5, 0.5),
       novekmeny(math.sqrt, 0, 0.6), novekmeny(math.sqrt, 5, 0.6)]

# érintők (22. + saját)
E22 = [erinto(lambda t: t * t / 2 + 2 * t + 1, 2), erinto(lambda t: -t * t / 2 + 2 * t - 3, 4),
       erinto(lambda t: t * t / 2 + t / 2 - 3, 1), erinto(lambda t: -t * t / 2 + 1.5 * t + 2, 0),
       erinto(lambda t: -3 * t ** 3 + 3 * t * t + 3 * t + 3, -1), erinto(lambda t: -2 * t ** 3 - 2 * t * t + 2 * t - 2, 1),
       erinto(lambda t: 2 * t ** 3 + t * t / 2 - 2 * t + mp.mpf(1) / 2, -1),
       erinto(lambda t: mp.mpf(2) / 3 * t ** 3 + 3 * t * t + 3 * t + mp.mpf(1) / 3, 1)]
assert [e[1:] for e in E22] == [(4, -1), (-2, 5), (F(3, 2), F(-7, 2)), (F(3, 2), 2), (-12, -6), (-8, 4), (3, 4), (11, -4)]
K7 = [erinto(lambda t: t ** 3 - 12 * t + 1, 3), erinto(lambda t: t ** 3 - 12 * t + 1, -3)]
K8 = [erinto(lambda t: (t + 3) / (t - 1), 3), erinto(lambda t: t / (t * t + 1), 0)]

# f'(x0)-értékek
D19 = [racio(d(lambda t: t ** 4 / 4 - 4 * t * t + 16, 2)), racio(d(lambda t: 1.5 * t ** 4 + 4 * t ** 3 - t * t / 2 + 5 * t - 7, -1)),
       racio(d(lambda t: -t ** 3 + 9 * t * t + t - 1, -1))]
f19c = lambda t: t ** 3 / 4 + mp.sqrt(2) / 2 * t * t - 7 * t + 2 * mp.pi
f19e = lambda t: t ** 3 + 5 / t
f19f = lambda t: t * t - 1 / (2 * t * t)
K5 = [racio(d(f19c, mp.sqrt(2))), racio(d(f19e, 2) + d(f19e, -2)), racio(d(f19f, 2) - d(f19f, -2))]
D26 = [racio(d(lambda t: (3 * t * t - 4) ** 4, -1)), racio(d(lambda t: (t * t - 3 * t + 2) ** 5, 3)),
       racio(d(lambda t: (t - 2) * mp.e ** (2 * t), 0)), racio(d(lambda t: 3 * mp.log((t - 1) / (t + 1)), 2))]
f21 = lambda t: mp.mpf(2) / 3 * t ** 3 + t * t / 2 - mp.mpf(3) / 7 * t
g21 = lambda t: 2 * t ** 3 - mp.mpf(9) / 2 * t * t - 2 * t
N1 = [racio(d(f21, -0.5)), racio(d(g21, -0.5)), racio(7 * d(f21, -0.5) + d(g21, -0.5))]

TESZT = {
    'alap-1': v(*[z for p in N16 for z in p]),
    'alap-2': v(-2, 0, 2),
    'alap-3': v(6, 2, 3, 6, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8),
    'alap-4': v(3, 3, 2, 1, F(4, 3), 15, F(-1, 2), 2, 3, 3, 2),
    'alap-5': v(4, 3, 5, 1, 2, 2, 3, 3, 4, 1, 2, 3, 1, 6),
    'alap-6': v(7, 5, 2, 4, 3, 3, 7, 3, 4, 3),
    'alap-7': v(6, 14, 1, 10, 4, 30, 14, 1, 3, 2, 3, 1),
    'alap-8': v(1, 2, 2, 2, 3, 1),
    'alap-9': v(f"f'(2)={D19[0]}", D19[1], D19[2], f"f'(-1)={D19[1]}", f"f'(-1)={D19[2]}"),
    'alap-10': v(2, E22[0][0], E22[0][1], E22[0][2], 4, E22[1][0], E22[1][1], E22[1][2]),
    'alap-11': v(E22[2][1], E22[2][2], E22[3][1], E22[3][2]),
    'alap-12': v(-1, E22[4][0], E22[4][1], E22[4][2], 1, E22[5][0], E22[5][1], E22[5][2]),
    'alap-13': v(F(21, 3), 2 * 3 + 4, (14 - 4) // 2, F(-3) + F(4, 100) * 10),
    'alap-14': v(12, 3, 4, 3, 10, 5, 4, 1, 2, 5, 1, 2),
    'alap-15': v(3, 3, 2, 3, 4, 2, 2, 3, 3, 1),
    'alap-16': v(2, 4, 3, 2, 4, 1, 3, 4, 8, 15),
    'alap-17': v(6, 18, 4, 8, 12, 4, 1, 2, 3),
    'alap-18': v(3, -12, 9, 6, -12, 1, 3, 0, -3),
    'kozep-1': v(-1, 3, -1, 3, -1, 3),
    'kozep-2': v(2, 2, 2, 2, 1, 2, 2, 2, 2, 3, 1, 2, 3),
    'kozep-3': v(4, 2, 4, 2, 2, 1, 1, 2, 1, 1),
    'kozep-4': v(6, 3, 3, 8, 4, 4, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2),
    'kozep-5': v(*K5, 1),
    'kozep-6': v(E22[6][1], E22[6][2], E22[7][1], E22[7][2], F(-1, 3), F(-1, 3), F(2, 3)),
    'kozep-7': v(K7[0][0], K7[0][2], -3, K7[1][0], K7[1][2], -15, 17),
    'kozep-8': v(K8[0][0], K8[0][1], K8[0][2], K8[1][0], K8[1][1]),
    'kozep-9': v(1, 3, 3, 2, 2, 2, 3, 1, 2, 1, 2, 2, 1),
    'kozep-10': v(3, 2, 4, 4, 2, 2, 4, 2, 5, 7, 3),
    'kozep-11': v(D26[0], -1, D26[0], D26[1], 0, D26[2], 6, 2, D26[3]),
    'kozep-12': v(4, 1, 3, 24, 4, 12, 54, 3, 8, 3, 3, 8, 3, 3, 2, 3, 1),
    'nehez-1': v(N1[0], N1[1], N1[2], 4, 4, 0),
    'nehez-3': v(4, -6, 12, -1),
    'joker': v(4),
}
assert N16 == [(F('1.25'), F('2.5')), (F('5.25'), F('10.5')), (F('0.77'), F('1.29')), (F('0.13'), F('0.22'))]
assert D19 == [-8, 12, -20] and K5 == [F(-7, 2), F(43, 2), F(33, 4)] and D26 == [24, 240, -3, 2] and N1 == [F(-3, 7), 4, 1]
assert [k[0] for k in K7] == [-8, 10] and [k[2] for k in K7] == [-53, 55] and K8 == [(3, -1, 6), (0, 1, 0)]
