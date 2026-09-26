# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/04 — Zsoldos-lista II. (határozott integrál és terület).

Független forrás: minden határozott integrált numerikus kvadratúrával (mpmath.quad), minden területet a
kézzel megadott zérushelyek/metszéspontok közötti |integrálok| összegeként, a közelítő összegeket közvetlen
összegzéssel számolunk újra — a builder sympy-számolásától függetlenül."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/04-integral/feladatok-hatarozott-integral.html'
mp.mp.dps = 40
EPS = mp.mpf(10) ** -25


def v(*ertekek):
    return [('', e) for e in ertekek]


def _q(f, pontok):
    return mp.quad(f, [mp.mpf(p) if not isinstance(p, mp.mpf) else p for p in pontok])


def H(f, a, b, ertek, *szamok):
    """∫_a^b f = ertek."""
    assert abs(_q(f, [a, b]) - ertek) < EPS, (a, b, _q(f, [a, b]), ertek)
    return v(*szamok)


def T(h, pontok, ertek, *szamok):
    """A h = f − g (vagy f) és a tengely közötti terület: a megadott pontok (zérushelyek) közötti |∫| összege.
    A pontok valóban zérushelyek (a szélsők kivételével), és közöttük h nem vált előjelet."""
    for p in pontok[1:-1]:
        assert abs(h(mp.mpf(p))) < EPS, p
    for i in range(len(pontok) - 1):
        a, b = mp.mpf(pontok[i]), mp.mpf(pontok[i + 1])
        jel = [mp.sign(h(a + (b - a) * k / 10)) for k in range(1, 10)]
        assert len(set(jel)) == 1, (pontok, i)
    t = sum(abs(_q(h, [pontok[i], pontok[i + 1]])) for i in range(len(pontok) - 1))
    assert abs(t - ertek) < EPS, (pontok, t, ertek)
    return v(*szamok)


s, c, e, ln, sq, tg, ctg, pi = mp.sin, mp.cos, mp.exp, mp.log, mp.sqrt, mp.tan, mp.cot, mp.pi


def Q(p, q):
    return mp.mpf(p) / q


# alap-1: x² a [0; 2]-n, n = 4
_f = [mp.mpf(k) ** 2 / 4 for k in range(5)]
assert sum(_f[:4]) / 2 == Q(7, 4) and sum(_f[1:]) / 2 == Q(15, 4)
# közép-1: 4 − x²/4, n = 4, csökkenő
_g = [4 - mp.mpf(k) ** 2 / 4 for k in range(5)]
assert sum(_g[:4]) == Q(25, 2) and sum(_g[1:]) == Q(17, 2) and (sum(_g[:4]) + sum(_g[1:])) / 2 == Q(21, 2)


# alap-2: törtvonal
def tv(t):
    pts = [(0, 0), (1, 3), (2, 0), (3, -2), (4, -2), (5, 0), (6, 2)]
    for (a, fa), (b, fb) in zip(pts, pts[1:]):
        if a <= t <= b:
            return fa + (fb - fa) * (t - a) / (b - a)


_tv = lambda a, b, *k: _q(tv, [a, *k, b])
assert abs(_tv(0, 2, 1) - 3) < EPS and abs(_tv(2, 5, 3, 4) + 4) < EPS and abs(_tv(0, 6, 1, 2, 3, 4, 5)) < EPS
# a tulajdonságok (alap-7): ∫₀³f = 7, ∫₀⁵f = 4, ∫₀³g = −2
assert [-7, 4 - 7, 2 * 7 - 3 * (-2), 7 + 3] == [-7, -3, 20, 10]

f12 = lambda x: x ** 2 - 4 * x + 3
_r = [_q(f12, [0, 1]), _q(f12, [1, 3]), _q(f12, [3, 4])]
assert abs(_r[0] - Q(4, 3)) < EPS and abs(_r[1] + Q(4, 3)) < EPS and abs(_r[2] - Q(4, 3)) < EPS
assert abs(sum(_r) - Q(4, 3)) < EPS and abs(_r[0] - _r[1] + _r[2] - 4) < EPS

TESZT = {
    'alap-1': H(lambda x: x ** 2, 0, 2, Q(8, 3), F(7, 4), F(15, 4), F(8, 3)),
    'alap-2': v(3, 4, 3, -4, 0, 8),
    'alap-3': H(lambda x: x ** 3, 1, 3, 20, 20) + H(lambda x: 1 - 2 * x + 3 * x ** 2, -1, 3, 24, 24)
    + H(lambda x: x ** 3 - 2 * x ** 2 + 5, -1, 3, Q(64, 3), F(64, 3)) + H(lambda x: x ** 2 + 2 * x, -2, 1, 0, 0),
    'alap-4': H(lambda x: mp.cbrt(x ** 2), 1, 8, Q(93, 5), F(93, 5)) + H(lambda x: 1 / mp.cbrt(x ** 2), 1, 8, 3, 3)
    + H(lambda x: (x - 1) / sq(x), 1, 9, Q(40, 3), F(40, 3)) + H(lambda x: sq(x) - 1 / sq(x), 1, 4, Q(8, 3), F(8, 3)),
    'alap-5': H(e, -1, 1, mp.e - 1 / mp.e, 1) + H(lambda x: 1 / x, 1, mp.e ** 3, 3, 3)
    + H(lambda x: 2 * e(x), 0, ln(5), 8, 8) + H(lambda x: 1 / x + x, 1, 2, ln(2) + Q(3, 2), 2, F(3, 2)),
    'alap-6': H(lambda x: c(x) - s(x), -pi / 2, pi / 2, 2, 2) + H(lambda x: 1 / s(x) ** 2, pi / 4, pi / 3, 1 - sq(3) / 3, 1, 3)
    + H(lambda x: 1 / c(x) ** 2 - s(x), -pi / 4, pi / 4, 2, 2)
    + H(lambda x: c(x) + 1 / s(x) ** 2, pi / 6, pi / 2, Q(1, 2) + sq(3), F(1, 2), 3),
    'alap-7': v(-7, 4, -3, 20, 10, 0),
    'alap-8': T(lambda x: x ** 2 - 2 * x + 3, [0, 3], 9, 9),
    'alap-9': T(lambda x: x ** 3 + 1, [0, 2], 6, 6) + T(lambda x: 4 - x ** 2, [-1, 1], Q(22, 3), F(22, 3))
    + T(lambda x: sq(x) + 1, [1, 4], Q(23, 3), F(23, 3)),
    'alap-10': T(lambda x: -x ** 2 + 2 * x, [0, 2], Q(4, 3), 0, 2, F(4, 3))
    + T(lambda x: 6 - x - x ** 2, [-3, 2], Q(125, 6), -3, 2, F(125, 6)),
    'kozep-1': H(lambda x: 4 - x ** 2 / 4, 0, 4, Q(32, 3), F(25, 2), F(17, 2), F(21, 2), F(32, 3)),
    'kozep-2': H(lambda x: (2 * x - 1) ** 3, 2, 3, 68, 68) + H(lambda x: e(3 * x), 0, 1, (mp.e ** 3 - 1) / 3, 3, -1, 3)
    + H(lambda x: 1 / (11 + 5 * x) ** 3, -2, -1, Q(7, 72), F(7, 72)) + H(lambda x: c(2 * x), 0, pi / 4, Q(1, 2), F(1, 2)),
    'kozep-3': H(lambda x: (2 * x ** 3 + 1) ** 4 * x ** 2, 0, 1, Q(121, 15), F(121, 15))
    + H(lambda t: t ** 4 / 6, 1, 3, Q(121, 15))
    + H(lambda x: x ** 2 / (1 + x ** 3), 0, 1, ln(2) / 3, F(1, 3), 2, 3)
    + H(lambda x: s(x) * c(x) ** 2, 0, pi / 2, Q(1, 3), F(1, 3)) + H(lambda x: x / sq(x ** 2 + 1), 0, sq(3), 1, F(1, 2), 4, 1),
    'kozep-4': H(lambda x: (3 * x ** 2 - 4) / x, 1, 9, 120 - 8 * ln(3), 120, -8, 3)
    + H(lambda x: x ** 2 + 1 / x ** 4, 1, 2, Q(21, 8), F(21, 8)) + H(lambda x: (x + sq(x)) / x, 1, 4, 5, 5)
    + H(lambda x: (x + 1) ** 2 / x ** 2, 1, 2, Q(3, 2) + 2 * ln(2), F(3, 2), 2, 2),
    'kozep-5': H(lambda x: 1 / c(x) ** 2 + 1 / s(x) ** 2, pi / 6, pi / 3, 4 * sq(3) / 3, 4, 3, 3)
    + H(lambda x: ctg(x) ** 2, pi / 4, pi / 2, 1 - pi / 4, 1, 4)
    + H(lambda x: (s(x) + c(x)) ** 2, 0, pi / 4, pi / 4 + Q(1, 2), 4, F(1, 2))
    + H(lambda x: s(2 * x) * c(x), 0, pi / 2, Q(2, 3), F(2, 3)),
    'kozep-6': T(lambda x: x ** 2 - 6 * x + 5, [1, 5], Q(32, 3), 1, 5)
    + H(lambda x: x ** 2 - 6 * x + 5, 1, 5, -Q(32, 3), F(-32, 3), F(32, 3))
    + T(lambda x: x ** 3 - 8, [0, 2], 12) + H(lambda x: x ** 3 - 8, 0, 2, -12, -12, 12),
    'kozep-7': T(lambda x: x * (x - 1) * (x - 2), [0, 1, 2], Q(1, 2), 0, 1, 2)
    + H(lambda x: x * (x - 1) * (x - 2), 0, 1, Q(1, 4), F(1, 4)) + H(lambda x: x * (x - 1) * (x - 2), 1, 2, -Q(1, 4), F(-1, 4))
    + v(F(1, 2)),
    'kozep-8': H(lambda x: x ** 2 - 3 * x, 0, 3, -Q(9, 2), 3, F(-9, 2)) + H(lambda x: x ** 2 - 3 * x, 3, 4, Q(11, 6), F(11, 6))
    + T(lambda x: x ** 2 - 3 * x, [0, 3, 4], Q(19, 3), F(19, 3)) + H(lambda x: x ** 2 - 3 * x, 0, 4, -Q(8, 3), F(-8, 3)),
    'kozep-9': T(lambda x: s(2 * x), [0, pi / 2], 1, 1) + T(lambda x: 3 * c(x), [-pi / 2, pi / 2], 6, 6)
    + T(lambda x: 2 * s(x), [0, pi, 2 * pi], 8, 8) + H(lambda x: 2 * s(x), 0, 2 * pi, 0, 0, 2, 2, 0),
    'kozep-10': T(lambda x: e(x / 2), [0, 2 * ln(3)], 4, 4) + T(lambda x: e(x) + e(-x), [-ln(2), ln(2)], 3, F(3, 2), F(-3, 2), 3),
    'kozep-11': H(lambda x: x ** 2 - x - 2, 0, 3, -Q(3, 2))
    + H(lambda x: x ** 2 - x - 2, 0, 2, -Q(10, 3), 2, F(-10, 3)) + H(lambda x: x ** 2 - x - 2, 2, 3, Q(11, 6), F(11, 6))
    + T(lambda x: x ** 2 - x - 2, [0, 2, 3], Q(31, 6), F(31, 6)),
    'kozep-12': T(f12, [0, 1, 3, 4], 4, 'A c) kifejezés', F(4, 3), F(-4, 3), F(4, 3), 4, F(4, 3)),
    'nehez-1': T(lambda x: (x + 8) - (x ** 2 / 2 + 2 * x + 4), [-4, 2], 18, -4, 2, 18)
    + T(lambda x: (x + 4) - (x ** 2 + 4 * x), [-4, 1], Q(125, 6), -4, 1, F(125, 6)),
    'nehez-2': T(lambda x: (x ** 2 + 10) - (2 * x ** 2 + 1), [-3, 3], 36, -3, 3, 36)
    + T(lambda x: (-2 * x ** 2 + 18) - (x ** 2 - 8 * x + 18), [0, Q(8, 3)], Q(256, 27), F(8, 3), F(256, 27)),
    'nehez-3': T(lambda x: (x - 2) ** 2, [0, 2], Q(8, 3), F(8, 3))
    + T(lambda x: 4 - e(x), [0, ln(4)], 8 * ln(2) - 3, 8, 2, -3, F(51, 20))
    + T(lambda x: sq(4 - x), [0, 4], Q(16, 3), F(16, 3)),
    'nehez-4': T(lambda x: x ** 2 - 5 * x + 4, [0, 1], Q(11, 6), 1, 4, F(11, 6))
    + T(lambda x: (1 - x) - (x ** 2 - 4 * x + 1), [0, 3], Q(9, 2), 0, 3, F(9, 2), 2)
    + T(lambda x: 8 - x ** 3, [0, 2], 12, 12),
    'joker': T(lambda x: 4 - x ** 2, [-2, 2], Q(32, 3), -2, 2, F(32, 3), 8, F(32, 3)),
}
assert abs(Q(4, 3) * 8 - Q(32, 3)) < EPS
