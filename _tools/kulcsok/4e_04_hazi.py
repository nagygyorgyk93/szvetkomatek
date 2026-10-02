# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/04 — I.V.H. Kihallgató Terem (házi).

Független forrás: a primitív függvényeket numerikusan deriváljuk (mpmath), a határozott integrálokat és a területeket
kvadratúrával, kézzel megadott zérushelyekkel/metszéspontokkal számoljuk újra — a builder sympy-számolásától
függetlenül. A felsorolt számok a kijelzett eredmények együtthatói/állandói, a szövegbeli sorrendben."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/04-integral/feladatok-hazi.html'
mp.mp.dps = 40
EPS = mp.mpf(10) ** -25


def v(*ertekek):
    return [('', e) for e in ertekek]


def P(f, Fp, *szamok):
    for p in (mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('2.3')):
        a, b = f(p), mp.diff(Fp, p)
        assert abs(a - b) < mp.mpf(10) ** -20 * max(1, abs(a)), (szamok, p, a, b)
    return v(*szamok)


def H(f, a, b, ertek, *szamok):
    assert abs(mp.quad(f, [a, b]) - ertek) < EPS, (a, b, ertek)
    return v(*szamok)


def T(h, pontok, ertek, *szamok):
    for p in pontok[1:-1]:
        assert abs(h(mp.mpf(p))) < EPS, p
    t = sum(abs(mp.quad(h, [pontok[i], pontok[i + 1]])) for i in range(len(pontok) - 1))
    assert abs(t - ertek) < EPS, (pontok, t, ertek)
    return v(*szamok)


s, c, e, ln, sq, pi = mp.sin, mp.cos, mp.exp, mp.log, mp.sqrt, mp.pi
Q = lambda p, q: mp.mpf(p) / q

# alap-3: F(2) = 7
assert 2 * 4 - 3 * 2 + 5 == 7

TESZT = {
    'alap-1': P(lambda x: 8 * x ** 3 - 3 * x ** 2 + 4, lambda x: 2 * x ** 4 - x ** 3 + 4 * x, 2, 4, 3, 4)
    + P(lambda x: 3 / sq(x) + 2 * e(x), lambda x: 6 * sq(x) + 2 * e(x), 6, 2)
    + P(lambda x: 5 / x + 2 * c(x), lambda x: 5 * ln(abs(x)) + 2 * s(x), 5, 2),
    'alap-2': P(lambda x: (6 * x + 5) ** 3, lambda x: (6 * x + 5) ** 4 / 24, 6, 5, 4, 24)
    + P(lambda x: e(4 * x - 1), lambda x: e(4 * x - 1) / 4, 4, 1, 4)
    + P(lambda x: s(2 * x + 1), lambda x: -c(2 * x + 1) / 2, 2, 1, 2),
    'alap-3': P(lambda x: 4 * x - 3, lambda x: 2 * x ** 2 - 3 * x + 5, 'F(x)=2x^2-3x+5'),
    'alap-4': H(lambda x: 3 * x ** 2 + 2 * x, 0, 2, 12, 12) + H(lambda x: 2 / sq(x), 1, 4, 4, 4)
    + H(lambda x: s(x) + 1, 0, pi, 2 + pi, 2),
    'alap-5': T(lambda x: 3 * x ** 2 + 1, [1, 2], 8, 8),
    'kozep-1': P(lambda x: 6 * x ** 2 / (x ** 3 + 5), lambda x: 2 * ln(abs(x ** 3 + 5)), 2, 3, 5)
    + P(lambda x: x * (x ** 2 + 4) ** 3, lambda x: (x ** 2 + 4) ** 4 / 8, 2, 4, 4, 8)
    + P(lambda x: c(x) * s(x) ** 4, lambda x: s(x) ** 5 / 5, 5, 5),
    'kozep-2': H(lambda x: x * (x ** 2 + 1) ** 2, 0, 2, Q(62, 3))
    + H(lambda t: t ** 2 / 2, 1, 5, Q(62, 3), 1, 5, F(1, 2), F(62, 3)),
    'kozep-3': T(lambda x: 3 - 3 * x ** 2, [0, 1, 2], 6)
    + H(lambda x: 3 - 3 * x ** 2, 0, 1, 2)
    + H(lambda x: 3 - 3 * x ** 2, 1, 2, -4)
    + H(lambda x: 3 - 3 * x ** 2, 0, 2, -2, 6, -2),
    'nehez-1': T(lambda x: (5 - x ** 2) - (x ** 2 - 2 * x + 1), [-1, 2], 9, 9),
    'nehez-2': T(lambda x: 2 - x ** 3 / 4, [0, 2], 3, 3)
    + T(lambda x: (x - 2) - (x ** 2 - 6 * x + 8), [2, 5], Q(9, 2), F(9, 2)),
}
