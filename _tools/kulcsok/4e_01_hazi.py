# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/01 — I.V.H. Kihallgató Terem (házi).

Független számolás: a határértékek NUMERIKUSAN (mpmath, 80 jegy, n = 10^20 és 10^21), a sorok és
a szakaszos törtek saját képlettel — a builder sympy-szimbolikus számolásától függetlenül."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/01-sorozatok-hatarerteke/feladatok-hazi.html'
PV, MV = 'pluszvegtelen', 'minuszvegtelen'
mp.mp.dps = 80
sq = mp.sqrt


def lim(f, e=False):
    """f(n) határértéke numerikusan; e=True: e^k alakban a k kitevő."""
    a, b = f(mp.mpf(10) ** 20), f(mp.mpf(10) ** 21)
    if e:
        a, b = mp.log(a), mp.log(b)
    if a > 10 ** 6 and b > a:
        return PV
    if a < -10 ** 6 and b < a:
        return MV
    if abs(b) < mp.mpf(10) ** -30:
        return F(0)
    x = F(mp.nstr(b, 50, min_fixed=-mp.inf, max_fixed=mp.inf))
    r = x.limit_denominator(1000)
    assert abs(x - r) < F(1, 10 ** 8), (x, r)
    return r


def L(*fk, e=False):
    return [lim(f, e) for f in fk]


def sor(b1, q):
    b1, q = F(b1), F(q)
    assert abs(q) < 1
    return b1 / (1 - q)


def szakaszos(nem_ism, ism):
    k, p = len(nem_ism), len(ism)
    return F(int(nem_ism + ism) - int(nem_ism or 0), (10 ** p - 1) * 10 ** k)


def v(*ertekek):
    return [('', x) for x in ertekek]


TESZT = {
    'alap-1': v(*[F(4*k+2, k+1) for k in range(1, 6)], lim(lambda n: (4*n+2)/(n+1))),
    'alap-2': v(*L(lambda n: (9*n**2-4*n)/(3*n**2+5), lambda n: (7*n+2)/(n**3+1),
                   lambda n: (4-n**3)/(2*n**2+n))),
    'alap-3': v(lim(lambda n: (mp.mpf(5)/7)**n), lim(lambda n: 2+7/n**2), 'divergens', F(-6, 5)),
    'alap-4': v(*L(lambda n: (1+1/n)**(5*n), lambda n: (1+3/n)**(2*n), e=True)),
    'alap-5': v(*[24 * F(5, 8) ** k for k in range(1, 4)], sor(24, F(5, 8))),
    'kozep-1': v(*L(lambda n: (6*n+1)/sq(4*n**2+n), lambda n: sq(81*n**2-5)/(2-3*n))),
    'kozep-2': v(*L(lambda n: (1-2/n)**(5*n), lambda n: (1+6/n)**(n/4), e=True)),
    'kozep-3': v(szakaszos('', '45'), szakaszos('1', '2'), 'nincs', F(-25, 2) / 10),
    'nehez-1': v(*L(lambda n: (n**2+4)/(n+2)-(n**2-2)/(n+3), lambda n: 3*n**2/(3*n+1)-(n**2+1)/(n+2))),
    'nehez-2': v(*L(lambda n: ((n+5)/(n+1))**(3*n), lambda n: (1+2/(3*n+1))**(n+5), e=True)),
}
