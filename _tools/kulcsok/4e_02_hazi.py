# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/02 — I.V.H. Kihallgató Terem (házi).

Független számolás: a határértékek numerikusan (mpmath), a paritás véletlen pontokban, a többi kézi
levezetésből (tényezőkre bontás) — a builder sympy-számolásától függetlenül."""
import random
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/02-fuggvenyek/feladatok-hazi.html'
PV, MV = 'pluszvegtelen', 'minuszvegtelen'
mp.mp.dps = 60
H = mp.mpf(10) ** -25


def lim(f, a):
    b = f(mp.mpf(a) + H)
    assert abs(b - f(mp.mpf(a) - H)) < mp.mpf(10) ** -15
    return F(mp.nstr(b, 40, min_fixed=-mp.inf, max_fixed=mp.inf)).limit_denominator(1000)


def vegtelen(f, s):
    b = f(s * mp.mpf(10) ** 20)
    if abs(b) > 10 ** 10:
        return PV if b > 0 else MV
    return F(mp.nstr(b, 40, min_fixed=-mp.inf, max_fixed=mp.inf)).limit_denominator(1000)


def oldal(f, a, s):
    b = f(mp.mpf(a) + s * H)
    return PV if b > 0 else MV


def paritas(f):
    random.seed(3)
    t = [random.uniform(0.2, 2.5) for _ in range(10)]
    if all(abs(f(-u) - f(u)) < 1e-9 for u in t):
        return 'páros'
    if all(abs(f(-u) + f(u)) < 1e-9 for u in t):
        return 'páratlan'
    return 'egyik sem'


def v(*ertekek):
    return [('', e) for e in ertekek]


TESZT = {
    'alap-1': v(0, 4, 4, -6),                        # x(x−4) ≠ 0 ; 8 − 2x ≥ 0 ; x + 6 > 0
    'alap-2': v(-1, 3, 3, -1, -1, 3, -3, 3, -3, -2, 3, -3, -2, 3),
    'alap-3': [('', ' '.join(paritas(f) for f in (lambda u: u**6 - 2*u**2, lambda u: u*abs(u),
                                                     lambda u: u**2 + 3*u, lambda u: 3**u + 3**(-u))))],
    'alap-4': v(lim(lambda u: (u**2 - 5*u + 6)/(u - 3), 3), lim(lambda u: (u**2 + 4*u + 3)/(u**2 - 1), -1),
                vegtelen(lambda u: (4*u**2 - 1)/(2*u**2 + u), 1)),
    'alap-5': v(1, 3, -2, 2, 0),
    'kozep-1': v(lim(lambda u: (mp.sqrt(u + 2) - 2)/(u - 2), 2), lim(lambda u: (mp.sqrt(9 + u) - 3)/u, 0)),
    'kozep-2': v(oldal(lambda u: (u + 1)/(4 - u), 4, -1), oldal(lambda u: (u + 1)/(4 - u), 4, 1)),
    'kozep-3': v(vegtelen(lambda u: (2*u**3 - u)/(u**2 + 5), -1), vegtelen(lambda u: (3 - u**2)/(u + 1), -1)),
    'nehez-1': v(1, 3, 1, -2, 5, -1, -2, -2),        # x² − 3x + 5 = (x − 1)(x − 2) + 3 ; a teljes számsor
    'nehez-2': v(1, 1, -2, -2, F(4, 3), -2, 2),     # (x − 2)(x + 2)/((x − 1)(x + 2)) ; x³ − x = x(x² − 4) + 3x
}
