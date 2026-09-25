# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/03 — Zsoldos-lista II. (függvényvizsgálat).

Független forrás: a szélsőérték- és inflexiós pontok a 0_Feladatok kulcsából (29–31.) és kézi levezetésből (32. és a
saját feladatok); mindegyiket itt, numerikus deriválással (mpmath) ellenőrizzük: a szélsőérték-helyen f' = 0 és a
függvényérték egyezik, az inflexiós helyen f'' = 0 — a builder sympy-számolásától függetlenül.
Irracionális koordinátát (√) nem várunk szövegként; ott csak a racionális társkoordináta szerepel."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/03-derivalt/feladatok-fuggvenyvizsgalat.html'
mp.mp.dps = 40


def v(*ertekek):
    return [('', e) for e in ertekek]


def pont(f, x0, y0, rend=1):
    """Ellenőrzi, hogy (x0; y0) a grafikonon van, és ott f^(rend) = 0 (szélsőérték-, ill. inflexiós jelölt)."""
    x0 = mp.mpf(x0.numerator) / x0.denominator if isinstance(x0, F) else mp.mpf(x0)
    assert abs(f(x0) - (mp.mpf(y0.numerator) / y0.denominator if isinstance(y0, F) else y0)) < mp.mpf(10) ** -20, (x0, y0)
    assert abs(mp.diff(f, x0, rend)) < mp.mpf(10) ** -15, (x0, rend)
    return True


R = mp.sqrt
# 29.
assert pont(lambda t: t ** 3 - 2 * t * t + t - 2, F(1, 3), F(-50, 27)) and pont(lambda t: t ** 3 - 2 * t * t + t - 2, 1, -2)
f29b = lambda t: mp.mpf(2) / 3 * t ** 3 - t * t - 4 * t
assert pont(f29b, -1, F(7, 3)) and pont(f29b, 2, F(-20, 3))
f29c = lambda t: -t ** 4 / 2 - 2 * t ** 3 - 2 * t * t + 2
assert pont(f29c, -2, 2) and pont(f29c, 0, 2) and pont(f29c, -1, F(3, 2))
f29d = lambda t: -mp.mpf(3) / 4 * t ** 4 + 5 * t ** 3 - 6 * t * t - 12
assert pont(f29d, 0, -12) and pont(f29d, 4, 20) and pont(f29d, 1, F(-55, 4))
f29e = lambda t: t ** 4 / 4 - mp.mpf(5) / 2 * t * t + mp.mpf(9) / 4
assert pont(f29e, 0, F(9, 4)) and pont(f29e, R(5), -4)
f29f = lambda t: t ** 4 + 4 * t ** 3 + 4 * t * t + 4
assert pont(f29f, -1, 5) and pont(f29f, -2, 4) and pont(f29f, 0, 4)
f29h = lambda t: t ** 5 + 5 * t ** 4 + 5 * t ** 3 + 5
assert pont(f29h, -3, 32) and pont(f29h, -1, 4)
assert pont(lambda t: (t * t - 5 * t + 7) / (t - 2), 1, -3) and pont(lambda t: (t * t - 5 * t + 7) / (t - 2), 3, 1)
assert pont(lambda t: (t * t - 4 * t + 4) / (t * t + 2), -1, 3) and pont(lambda t: (t * t - 4 * t + 4) / (t * t + 2), 2, 0)
assert pont(lambda t: (t * t - 6 * t + 9) / (t * t + 3), -1, 4) and pont(lambda t: (t * t - 6 * t + 9) / (t * t + 3), 3, 0)
# 30.
assert pont(lambda t: t ** 4 - 3 * t * t, R(2) / 2, F(-5, 4), 2)
assert pont(lambda t: 9 * t ** 5 - 10 * t ** 3, 0, 0, 2)
assert pont(lambda t: 4 / (t * t + 1), R(3) / 3, 3, 2) and pont(lambda t: (t + 1) / t ** 3, -2, F(1, 8), 2)
# 31.
for f, pts in ((lambda t: t ** 3 + 3 * t * t - 4, [(-2, 0, 1), (0, -4, 1), (-1, -2, 2)]),
               (lambda t: -t ** 3 + 3 * t + 2, [(1, 4, 1), (-1, 0, 1), (0, 2, 2)]),
               (lambda t: -t ** 3 + 9 * t * t - 15 * t + 3, [(5, 28, 1), (1, -4, 1), (3, 12, 2)]),
               (lambda t: 2 * t ** 3 + 3 * t * t - 12 * t + 1, [(-2, 21, 1), (1, -6, 1), (F(-1, 2), F(15, 2), 2)]),
               (lambda t: -t ** 4 + 6 * t * t - 8, [(R(3), 1, 1), (0, -8, 1), (-1, -3, 2), (1, -3, 2)]),
               (lambda t: -t ** 4 + 2 * t * t + 3, [(-1, 4, 1), (1, 4, 1), (0, 3, 1), (1 / R(3), F(32, 9), 2)]),
               (lambda t: t ** 4 / 4 - 3 * t * t + 9, [(0, 9, 1), (R(6), 0, 1), (R(2), 4, 2)]),
               (lambda t: -t / (t * t + 1), [(-1, F(1, 2), 1), (1, F(-1, 2), 1), (0, 0, 2)]),
               (lambda t: -t / (t * t + 3), [(-3, F(1, 4), 2), (0, 0, 2), (3, F(-1, 4), 2)]),
               (lambda t: (t * t - 2 * t + 1) / (t - 2), [(1, 0, 1), (3, 4, 1)]),
               (lambda t: (t * t - 6 * t + 9) / (t - 1), [(-1, -8, 1), (3, 0, 1)]),
               (lambda t: (1 - 3 * t) / t ** 2, [(F(2, 3), F(-9, 4), 1), (1, -2, 2)]),
               (lambda t: (2 * t - 1) / t ** 2, [(1, 1, 1), (F(3, 2), F(8, 9), 2)])):
    for x0, y0, r in pts:
        assert pont(f, x0, y0, r)
# saját feladatok
assert pont(lambda t: 2 * t ** 3 - 6 * t + 1, -1, 5) and pont(lambda t: 2 * t ** 3 - 6 * t + 1, 1, -3)
assert pont(lambda t: -t ** 3 + 6 * t * t - 9 * t + 1, 3, 1) and pont(lambda t: -t ** 3 + 6 * t * t - 9 * t + 1, 1, -3)
assert pont(lambda t: (t * t + 3) / (t + 1), -3, -6) and pont(lambda t: (t * t + 3) / (t + 1), 1, 2)
# 32. (kézi levezetés)
T32 = {
    'a': (lambda t: (1 - t) * (t + 2) ** 2, 4, [(0, 4, 1), (-2, 0, 1), (-1, 2, 2)]),
    'b': (lambda t: (t + 2) * (t - 1) ** 2, 2, [(-1, 4, 1), (1, 0, 1), (0, 2, 2)]),
    'c': (lambda t: (t - 4) * (t - 1) ** 2, -4, [(1, 0, 1), (3, -4, 1), (2, -2, 2)]),
    'd': (lambda t: (t + 1) * (t + 4) ** 2, 16, [(-4, 0, 1), (-2, -4, 1), (-3, -2, 2)]),
    'e': (lambda t: (t ** 4 - 18 * t * t + 32) / 8, 4, [(0, 4, 1), (3, F(-49, 8), 1), (R(3), F(-13, 8), 2)]),
    'f': (lambda t: (t ** 4 - 6 * t * t - 7) / 4, F(-7, 4), [(0, F(-7, 4), 1), (R(3), -4, 1), (1, -3, 2)]),
    'g': (lambda t: (t ** 4 - 6 * t * t - 27) / 12, F(-9, 4), [(0, F(-9, 4), 1), (R(3), -3, 1), (1, F(-8, 3), 2)]),
    'h': (lambda t: (t * t - 4) / (t * t + 1), -4, [(0, -4, 1), (1 / R(3), F(-11, 4), 2)]),
    'i': (lambda t: (3 - t * t) / (t * t + 1), 3, [(0, 3, 1), (1 / R(3), 2, 2)]),
    'j': (lambda t: (t * t - 8) / (t + 3), F(-8, 3), [(-4, -8, 1), (-2, -4, 1)]),
    'k': (lambda t: (t * t - 3) / (t + 2), F(-3, 2), [(-3, -6, 1), (-1, -2, 1)]),
    'l': (lambda t: (t * t + t - 2) / (t + 3), F(-2, 3), [(-5, -9, 1), (-1, -1, 1)]),
    'm': (lambda t: (t * t - t - 2) / (t - 3), F(2, 3), [(1, 1, 1), (5, 9, 1)]),
}
for f, f0, pts in T32.values():
    f0 = F(f0)
    assert abs(f(mp.mpf(0)) - mp.mpf(f0.numerator) / f0.denominator) < mp.mpf(10) ** -20      # f(0)
    for x0, y0, r in pts:
        assert pont(f, x0, y0, r)

TESZT = {
    'alap-1': v(-2, 1, -2, 1, -2, 5, 1, -4),
    'alap-2': v(F(1, 3), F(-50, 27), 1, -2, -1, F(7, 3), 2, F(-20, 3)),
    'alap-3': v(-2, 0, 0, -4, 1, 4, -1, 0),
    'alap-4': v(5, 28, 1, -4, -2, 21, 1, -6),
    'alap-5': v(-1, 5, 1, -3, 3, 1, 1, -3),
    'alap-6': v(-1, 2, -1, 2, -1, 2),
    'alap-7': v('konvex (felfelé nyíló): B és C', 'konkáv (lefelé nyíló): A és D'),
    'alap-8': v(3, 3, 3, -1, 1, -1, 1, -1, 1, 'mindenütt konvex'),
    'alap-9': v(1, -2, 4, -2, 1, 2),
    'alap-10': v('az a) leírás'),
    'kozep-1': v(-2, 2, 0, 2, -1, F(3, 2), 0, -12, 4, 20, 1, F(-55, 4)),
    'kozep-2': v(0, F(9, 4), -4, -4, -1, 5, -2, 4, 0, 4, -3, 32, -1, 4),
    'kozep-3': v(1, -3, 3, 1, -1, 3, 2, 0, -1, 4, 3, 0),
    'kozep-4': v(1, 0, 3, 4, 'lokális maximum: (−1; −8)', 3, 0),
    'kozep-5': v(F(-5, 4), F(-5, 4), '(0; 0)'),
    'kozep-6': v(-1, -2, 0, 2, 3, 12, F(-1, 2), F(15, 2)),
    'kozep-7': v(1, 1, 'lokális minimum: (0; −8)', -1, -3, 1, -3, -1, 4, 1, 4, 0, 3, F(32, 9), F(32, 9), 0, 9, 0, 0, 4, 4),
    'kozep-8': v('(0; 0)', 'hamis', 12),
    'kozep-9': v(4, 0, 4, -2, 0, -1, 2, 2, -1, 4, 1, 0, 0, 2),
    'kozep-10': v('f(0)=−4', 1, 0, 'lokális minimum: (3; −4)', 2, -2, 16, -4, 0, -2, -4, -3, -2),
    'kozep-11': v(4, 0, 4, F(-49, 8), F(-49, 8), F(-13, 8), F(-13, 8), F(-7, 4), F(-7, 4), 'lokális minimum: (−√3; −4), (√3; −4)', -3, -3,
                  F(-9, 4), 0, F(-9, 4), -3, -3, F(-8, 3), F(-8, 3)),
    'kozep-12': v('(−3; −6) tehát lokális maximum', '(1; 2) lokális minimum', 'az x=−1 pólus'),
    'nehez-1': v(3, 3, -2, F(1, 8)),
    'nehez-2': v(-1, F(1, 2), 1, F(-1, 2), 0, 0, 'inflexiós pont: (−3; 1/4)', 0, 0, 3, F(-1, 4), F(2, 3), F(-9, 4), 1, -2,
                 1, 1, F(3, 2), F(8, 9)),
    'nehez-3': v(-4, 1, 'lokális minimum: (0; −4)', F(-11, 4), F(-11, 4), 3, -1, 0, 3, 2, 2),
    'nehez-4': v(F(-8, 3), -3, 'lokális maximum: (−4; −8)', 'lokális minimum: (−2; −4)', F(-3, 2), -2, -3, -6, -1, -2,
                 F(-2, 3), -3, 'lokális maximum: (−5; −9)', 'lokális minimum: (−1; −1)', F(2, 3), 3, 1, 1, 5, 9),
    'joker': v(3, 1, 0, 0),
}
