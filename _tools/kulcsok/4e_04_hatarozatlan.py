# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/04 — Zsoldos-lista I. (határozatlan integrál).

Független forrás: minden primitív függvényt itt, kézzel beírt lambdaként (a kulcs kijelzett alakjából) numerikusan
deriválunk (mpmath), és összevetjük a feladat integrandusával — a builder sympy-számolásától függetlenül.
A felsorolt számok a kijelzett primitív függvény együtthatói/kitevői/állandói, a szövegbeli sorrendben
(a sympy-latex a mínuszjel után szóközt tesz, ezért azokat abszolút értékben)."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/04-integral/feladatok-hatarozatlan-integral.html'
mp.mp.dps = 40
_PTS = (0.7, 1.3, 2.3, 0.4, 3.1)


def v(*ertekek):
    return [('', e) for e in ertekek]


def _valos(z):
    return not isinstance(z, mp.mpc) or abs(mp.im(z)) < mp.mpf(10) ** -30


def P(f, Fp, *szamok, rend=1):
    """Fp (rend-szeres) deriváltja = f legalább két pontban (ahol mindkettő valós)."""
    jo = 0
    for p in _PTS:
        p = mp.mpf(p)
        try:
            a, b = f(p), mp.diff(Fp, p, rend)
        except (ValueError, ZeroDivisionError):
            continue
        if not (_valos(a) and _valos(b)):
            continue
        assert abs(mp.re(a) - mp.re(b)) < mp.mpf(10) ** -20 * max(1, abs(a)), (szamok, p, a, b)
        jo += 1
    assert jo >= 2, szamok
    return v(*szamok)


s, c, e, ln, sq, tg, ctg = mp.sin, mp.cos, mp.exp, mp.log, mp.sqrt, mp.tan, mp.cot
cb = mp.cbrt


def gy(x, n):
    return mp.root(x, n)


# a „mit rontott el” párok: a hibás primitív deriváltja NEM az integrandus
assert abs(mp.diff(lambda x: (3 * x + 2) ** 4 / 4, 1) - 5 ** 3) > 1
assert abs(mp.diff(lambda x: (4 * x - 1) ** 6 / 6, 1) - 3 ** 5) > 1
# ponton átmenő primitív függvények
assert [1 ** 3 * 0 + 2 ** 3 - 3 * 2 ** 2 + 5, 1 - 1 + 3, 1 + 1] == [1, 3, 2]
assert abs(e(0) + 0 - 2 + 1) < 1e-30 and abs(s(mp.pi / 2) - c(mp.pi / 2) + 1 - 2) < 1e-30
assert abs(tg(mp.pi / 4) + ctg(mp.pi / 4) - 2) < 1e-30 and -3 + 1 + 6 == 4
# kétszer integrálva: f(0), f(2) és f(1), f(2)
assert abs(e(0) + 0 - 2 + 1) < 1e-30 and abs(e(2) + 2 - 2 - e(2)) < 1e-30
assert 1 - 2 + 1 == 0 and 8 - 8 + 2 == 2

TESZT = {
    'alap-1': P(lambda x: 4 * x, lambda x: 2 * x ** 2, 2, 2) + P(lambda x: x ** 4, lambda x: x ** 5 / 5, 5, 5)
    + P(lambda t: -4 * t ** 3, lambda t: -t ** 4, 4) + P(lambda x: -5 * s(x), lambda x: 5 * c(x), 5)
    + P(lambda x: 2 * e(x), lambda x: 2 * e(x), 2),
    'alap-2': P(lambda x: 3 * x ** 2 - 4 * x + 1, lambda x: x ** 3 - 2 * x ** 2 + x - 5, 'igen')
    + P(lambda x: 1 / x ** 2, lambda x: 7 - 1 / x, 'nem')
    + P(lambda x: (3 * x + 2) ** 3, lambda x: (3 * x + 2) ** 4 / 12, '3-mal', 12),
    'alap-3': P(lambda x: 3 * x ** 2 - 6 * x, lambda x: x ** 3 - 3 * x ** 2 + 5, 5, 5)
    + P(lambda x: 2 * x - 4 * x ** 3, lambda x: x ** 2 - x ** 4 + 3, 3, 3)
    + P(lambda x: 2 * x - 2 / x ** 3, lambda x: x ** 2 + 1 / x ** 2, 0),
    'alap-4': P(lambda x: 1 / x ** 3, lambda x: -1 / (2 * x ** 2), 2) + P(lambda x: 4 / x ** 5, lambda x: -1 / x ** 4, 4)
    + P(lambda x: x * sq(x), lambda x: 2 * x ** 2 * sq(x) / 5, 5)
    + P(lambda x: cb(x ** 2), lambda x: 3 * x * cb(x ** 2) / 5, 3, 5)
    + P(lambda x: 3 / gy(x, 4), lambda x: 4 * gy(x ** 3, 4), 4, 3),
    'alap-5': P(lambda x: 5 * x ** 3 - 4 * x ** 2 - 3 * x + 5,
                lambda x: 5 * x ** 4 / 4 - 4 * x ** 3 / 3 - 3 * x ** 2 / 2 + 5 * x, 5, 4, 4, 4, 3, 3, 3, 2, 2, 5)
    + P(lambda x: x ** 3 - 2 * x ** 2 + 2 * x - 1, lambda x: x ** 4 / 4 - 2 * x ** 3 / 3 + x ** 2 - x, 4, 4, 2, 3, 3, 2)
    + P(lambda x: 2 * x ** 2 - 3 * x + 4, lambda x: 2 * x ** 3 / 3 - 3 * x ** 2 / 2 + 4 * x, 2, 3, 3, 3, 2, 2, 4)
    + P(lambda x: 9 * x ** 8 - 6 * x ** 5 + x - 7, lambda x: x ** 9 - x ** 6 + x ** 2 / 2 - 7 * x, 9, 6, 2, 2, 7),
    'alap-6': P(lambda x: 3 * e(x) - 2 * s(x), lambda x: 3 * e(x) + 2 * c(x), 3, 2)
    + P(lambda x: 4 * c(x) + 1 / c(x) ** 2, lambda x: 4 * s(x) + tg(x), 4)
    + P(lambda x: 2 ** x + 1 / s(x) ** 2, lambda x: 2 ** x / ln(2) - ctg(x), 2, 2)
    + P(lambda x: 5 * e(x) - 3 / x, lambda x: 5 * e(x) - 3 * ln(abs(x)), 5, 3),
    'alap-7': P(lambda x: x ** 4 - sq(x) + x * cb(x) + 1 / x ** 2,
                lambda x: x ** 5 / 5 - 2 * x * sq(x) / 3 + 3 * x ** 2 * cb(x) / 7 - 1 / x, 5, 5, 2, 3, 3, 2, 3, 7, 1)
    + P(lambda x: 4 * sq(x ** 3) + 2 / sq(x), lambda x: 8 * x ** 2 * sq(x) / 5 + 4 * sq(x), 8, 2, 5, 4)
    + P(lambda x: cb(x) - 1 / cb(x ** 2), lambda x: 3 * x * cb(x) / 4 - 3 * cb(x), 3, 3, 4, 3, 3),
    'alap-8': P(lambda x: (x - 2) / x ** 3, lambda x: -1 / x + 1 / x ** 2, 1, 1, 2)
    + P(lambda x: (10 * x ** 8 + 3) / x ** 4, lambda x: 2 * x ** 5 - 1 / x ** 3, 2, 5, 1, 3)
    + P(lambda x: (3 * x ** 3 + 1) / (5 * x), lambda x: x ** 3 / 5 + ln(abs(x)) / 5, 3, 5, F(1, 5))
    + P(lambda x: (6 + 2 * x + x ** 2) / x ** 4, lambda x: -2 / x ** 3 - 1 / x ** 2 - 1 / x, 2, 3, 1, 2, 1),
    'alap-9': P(lambda x: (3 * x + 1) ** 4, lambda x: (3 * x + 1) ** 5 / 15, 3, 1, 5, 15)
    + P(lambda x: (5 - 2 * x) ** 9, lambda x: -(5 - 2 * x) ** 10 / 20, 5, 2, 10, 20)
    + P(lambda x: (x / 2 + 1) ** 3, lambda x: (x / 2 + 1) ** 4 / 2, 2, 1, 4, 2)
    + P(lambda x: cb(4 * x + 3), lambda x: 3 * (4 * x + 3) * cb(4 * x + 3) / 16, 3, 4, 3, 3, 4, 3, 16),
    'alap-10': P(lambda x: sq(3 * x + 1), lambda x: 2 * (3 * x + 1) * sq(3 * x + 1) / 9, 2, 3, 1, 3, 1, 9)
    + P(lambda x: 1 / sq(4 * x - 1), lambda x: sq(4 * x - 1) / 2, 4, 1, 2)
    + P(lambda x: 1 / (5 * x + 2), lambda x: ln(abs(5 * x + 2)) / 5, F(1, 5), 5, 2)
    + P(lambda x: 3 / (2 - x), lambda x: -3 * ln(abs(2 - x)), -3, 2)
    + P(lambda x: 1 / (2 * x + 1) ** 2, lambda x: -1 / (2 * (2 * x + 1)), 1, 2, 2, 1),
    'alap-11': P(lambda x: e(5 * x), lambda x: e(5 * x) / 5, 5, 5) + P(lambda x: e(1 - x), lambda x: -e(1 - x), 1)
    + P(lambda x: s(3 * x + 2), lambda x: -c(3 * x + 2) / 3, 3, 2, 3)
    + P(lambda x: c(x / 2), lambda x: 2 * s(x / 2), 2, 2) + P(lambda x: 1 / c(3 * x) ** 2, lambda x: tg(3 * x) / 3, 3, 3),
    'alap-12': P(lambda x: (4 * x - 1) ** 5, lambda x: (4 * x - 1) ** 6 / 24, 'hibás', 24)
    + P(lambda x: e(-4 * x), lambda x: -e(-4 * x) / 4, 4)
    + P(lambda x: 2 / (3 * x - 1), lambda x: 2 * ln(abs(3 * x - 1)) / 3, F(2, 3), 3),
    'kozep-1': P(lambda x: e(x) + 2 * x, lambda x: e(x) + x ** 2 - 2, -1, -2)
    + P(lambda x: s(x) + c(x), lambda x: s(x) - c(x) + 1, 1, 2, 1)
    + P(lambda x: 1 / c(x) ** 2 - 1 / s(x) ** 2, lambda x: tg(x) + ctg(x), 4, 2, 2)
    + P(lambda x: 3 / x ** 2 - 2 / x ** 3, lambda x: -3 / x + 1 / x ** 2 + 6, -2, 4, 6),
    'kozep-2': P(lambda x: e(x), lambda x: e(x) + x - 2, -1, -2, -2, rend=2)
    + P(lambda x: 6 * x - 4, lambda x: x ** 3 - 2 * x ** 2 + x, 0, 3, -2, 2, rend=2),
    'kozep-3': P(lambda x: (x + 1) * (x ** 2 - 3) / (3 * x ** 2), lambda x: x ** 2 / 6 + x / 3 - ln(abs(x)) + 1 / x, 2, 6, 3, 1)
    + P(lambda x: (sq(x) + 1) * (x - sq(x) + 1), lambda x: 2 * x ** 2 * sq(x) / 5 + x, 2, 2, 5)
    + P(lambda x: (x ** 2 + 1) ** 2, lambda x: x ** 5 / 5 + 2 * x ** 3 / 3 + x, 5, 5, 2, 3, 3)
    + P(lambda x: (1 - sq(x)) ** 2 / x, lambda x: ln(abs(x)) - 4 * sq(x) + x, -4),
    'kozep-4': P(lambda x: (x - sq(x)) * (1 + sq(x)) / sq(x), lambda x: x ** 2 / 2 - x, 2, 2)
    + P(lambda x: (x ** 4 + sq(x ** 3) + sq(x) + 3) / (x * sq(x)),
        lambda x: 2 * x ** 3 * sq(x) / 7 + x + ln(abs(x)) - 6 / sq(x), F(2, 7), 3, 6)
    + P(lambda x: (x ** 2 + sq(x ** 3) + 3) / sq(x), lambda x: 2 * x ** 2 * sq(x) / 5 + x ** 2 / 2 + 6 * sq(x), 2, 2, 5, 2, 2, 6),
    'kozep-5': P(lambda x: (e(x) + 1) / e(x), lambda x: x - e(-x), 'x - e^-x + C')
    + P(lambda x: tg(x) ** 2, lambda x: tg(x) - x, 'tg x - x + C')
    + P(lambda x: (2 * c(x) ** 2 + 1) / c(x) ** 2, lambda x: 2 * x + tg(x), 2)
    + P(lambda x: c(2 * x) / (s(x) ** 2 * c(x) ** 2), lambda x: -ctg(x) - tg(x), 'ctg x - tg x + C')
    + P(lambda x: (1 - s(x) ** 3) / s(x) ** 2, lambda x: -ctg(x) + c(x), 'ctg x + x + C'),
    'kozep-6': P(lambda x: (2 * x + 1) / (x ** 2 + x - 3), lambda x: ln(abs(x ** 2 + x - 3)), 2, -3)
    + P(lambda x: x ** 2 / (x ** 3 + 1), lambda x: ln(abs(x ** 3 + 1)) / 3, F(1, 3), 3, 1)
    + P(lambda x: e(x) / (e(x) + 1), lambda x: ln(e(x) + 1), 1)
    + P(lambda x: ctg(x), lambda x: ln(abs(s(x))))
    + P(lambda x: c(x) / (1 + 2 * s(x)), lambda x: ln(abs(1 + 2 * s(x))) / 2, F(1, 2), 1, 2)
    + P(lambda x: 1 / (x * ln(x)), lambda x: ln(abs(ln(x)))),
    'kozep-7': P(lambda x: x * (x ** 2 - 1) ** 4, lambda x: (x ** 2 - 1) ** 5 / 10, 2, 1, 5, 10)
    + P(lambda x: x / (x ** 2 + 1) ** 2, lambda x: -1 / (2 * (x ** 2 + 1)), 1, 2, 2, 1)
    + P(lambda x: s(x) ** 2 * c(x), lambda x: s(x) ** 3 / 3, 3, 3)
    + P(lambda x: s(x) / c(x) ** 3, lambda x: 1 / (2 * c(x) ** 2), 1, 2, 2)
    + P(lambda x: x ** 2 / sq(1 + x ** 3), lambda x: 2 * sq(1 + x ** 3) / 3, 2, 1, 3, 3),
    'kozep-8': P(lambda x: x ** 2 * e(x ** 3), lambda x: e(x ** 3) / 3, 3, 3)
    + P(lambda x: e(s(x)) * c(x), lambda x: e(s(x)))
    + P(lambda x: e(1 / x) / x ** 2, lambda x: -e(1 / x), 1)
    + P(lambda x: 3 ** (x ** 2) * x, lambda x: 3 ** (x ** 2) / (2 * ln(3)), 3, 2, 2, 3),
    'kozep-9': P(lambda x: x * c(x ** 2 + 1), lambda x: s(x ** 2 + 1) / 2, 2, 1, 2)
    + P(lambda x: s(sq(x)) / sq(x), lambda x: -2 * c(sq(x)), 2)
    + P(lambda x: x ** 2 / c(x ** 3) ** 2, lambda x: tg(x ** 3) / 3, 3, 3)
    + P(lambda x: s(x) * c(c(x)), lambda x: -s(c(x))),
    'kozep-10': P(lambda x: 1 / (x * (1 + ln(x))), lambda x: ln(abs(1 + ln(x))), 1)
    + P(lambda x: (2 - ln(x)) / x, lambda x: 2 * ln(x) - ln(x) ** 2 / 2, 2, 2, 2)
    + P(lambda x: sq(1 + ln(x)) / x, lambda x: 2 * (1 + ln(x)) * sq(1 + ln(x)) / 3, 2, 1, 1, 3)
    + P(lambda x: 1 / (x * ln(x) ** 2), lambda x: -1 / ln(x), 1),
    'nehez-1': P(lambda x: x ** 3 * sq(x ** 4 + 1), lambda x: (x ** 4 + 1) * sq(x ** 4 + 1) / 6, 4, 1, 4, 1, 6, 4, 1, 4, 3)
    + P(lambda x: x * sq(x - 1), lambda x: 2 * (x - 1) ** 2 * sq(x - 1) / 5 + 2 * (x - 1) * sq(x - 1) / 3,
        2, 1, 2, 1, 5, 2, 1, 1, 3, -1, 1, 1)
    + P(lambda x: s(2 * x) / (1 + s(x) ** 2), lambda x: ln(1 + s(x) ** 2), 1, 2, 1, 2, 2, 2)
    + P(lambda x: x / sq(x + 1), lambda x: 2 * (x + 1) * sq(x + 1) / 3 - 2 * sq(x + 1), 2, 1, 1, 3, 2, 1, 1, -1, -1),
    'nehez-2': P(lambda x: s(x) ** 3, lambda x: -c(x) + c(x) ** 3 / 3, 3, 3)
    + P(lambda x: c(x) ** 5, lambda x: s(x) - 2 * s(x) ** 3 / 3 + s(x) ** 5 / 5, 2, 3, 3, 5, 5)
    + P(lambda x: s(2 * x) / c(x) ** 3, lambda x: 2 / c(x), 2)
    + P(lambda x: tg(x) ** 3, lambda x: tg(x) ** 2 / 2 + ln(abs(c(x))), 2, 2),
    'joker': P(lambda x: x * e(-x ** 2), lambda x: -e(-x ** 2) / 2, 2, F(-1, 2), 2, 2, -2, -2, 2),
}
