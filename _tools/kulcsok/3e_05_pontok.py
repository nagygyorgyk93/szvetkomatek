# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — pontok a síkban (1. gyűjtemény).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import Matrix, sqrt, Rational, symbols, solve, Abs

FAJL = '3e/05-analitikus-geometria/feladatok-pontok.html'
x, y, t = symbols('x y t', real=True)


def fr(c):
    c = Rational(c)
    return F(int(c.p), int(c.q))


def P(a, b):
    return Matrix([a, b])


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def tav(a, b):
    return sqrt((a - b).dot(a - b))


def det(a, b, c):
    return (b - a)[0] * (c - a)[1] - (b - a)[1] * (c - a)[0]


def cipo(pp):
    n = len(pp)
    return abs(sum(pp[i][0] * pp[(i + 1) % n][1] - pp[(i + 1) % n][0] * pp[i][1] for i in range(n))) / F(2)


TESZT = {
    'alap-2': pt((4, 3)) + pt((-4, -3)) + pt((-4, 3)) + pt((-2, -5)) + pt((2, 5)) + pt((2, -5)),
    'alap-3': [('', fr(tav(P(7, 10), P(-5, 5)))), ('', fr(tav(P(6, -5), P(-2, 1)))),
               kerek(tav(P(6, 1), P(2, -1))), kerek(tav(P(3, -2), P(4, Rational(5, 3)))),
               kerek(tav(P(1, -4), P(-6, 3)))],
    'alap-4': [('', fr(tav(P(6, -8), P(0, 0)))), ('', fr(tav(P(-5, 12), P(0, 0)))), kerek(sqrt(18))],
    'alap-5': pt((P(-6, 4) + P(4, -10)) / 2) + pt((P(8, 9) + P(-6, -3)) / 2)
              + pt((P(-5, 7) + P(3, -2)) / 2) + pt((P(4, 8) + P(-10, 14)) / 2),
    'alap-6': pt((P(4, 2) + P(-7, -2) + P(6, -9)) / 3) + pt((P(3, 4) + P(-5, 2) + P(-1, -6)) / 3),
    'alap-7': pt(P(-4, 1) + (P(8, 7) - P(-4, 1)) / 3) + pt(P(-4, 1) + 2 * (P(8, 7) - P(-4, 1)) / 3)
              + [('', 5), ('', F('5.5'))],
    'alap-8': pt(P(-3, -1) + P(5, -1) - P(3, -4)),
    'alap-9': [('', fr(tav(P(-1, 1), P(5, 1) ) + 2 * tav(P(5, 1), P(2, 5)))), ('', 'egyenlo szaru')],
    'alap-10': [('', fr(Abs(det(P(-2, 1), P(6, -1), P(5, 4))) / 2)),
                ('', fr(Abs(det(P(-3, -2), P(5, -1), P(-2, 6))) / 2)),
                ('', fr(Abs(det(P(-4, 9), P(7, 3), P(-2, 1))) / 2))],
    'alap-11': [('', cipo([(3, -1), (6, 5), (-3, 6), (-2, -3)])), ('', cipo([(4, 7), (-1, 4), (-2, -2), (3, 0)]))],
    'alap-12': [('', 'igen'), ('', fr(det(P(0, 1), P(2, 4), P(5, 8))))],
    'alap-13': [('', cipo([(-3, -2), (3, -2), (4, 1), (0, 4), (-3, 2)])),
                ('', cipo([(-3, -2), (3, -2), (4, 1), (0, 4), (-3, 2)]) * 100)],
    'alap-14': [('', fr(Abs(det(P(0, 0), P(6, 1), P(2, 5))) / 2))],
    'alap-15': [('', 'derekszogu'), ('', 6), ('', fr(tav(P(1, 1), P(5, 4))))],
    'alap-16': [('', 'negativ'), ('', fr(Abs(det(P(0, 0), P(2, 6), P(6, 6))) / 2))],
    'kozep-1': [('', fr(solve((x - 7)**2 + 16 - (x - 1)**2 - 4, x)[0])), ('', 0)],
    'kozep-2': [('', fr(r)) for r in sorted(solve((x + 4)**2 + 25 - 169, x), reverse=True)],
    'kozep-3': pt(2 * P(1, 1) - P(-3, 5)) + pt(2 * P(1, 1) - P(1, 7)),
    'kozep-4': [kerek(tav(P(-7, -3), (P(1, -5) + P(9, 5)) / 2)),
                ('', fr(tav(P(1, -5), (P(-7, -3) + P(9, 5)) / 2))),
                ('', fr(tav(P(9, 5), (P(-7, -3) + P(1, -5)) / 2)))],
    'kozep-5': [('', fr(tav(P(2, 6), P(1, -1))**2)), ('', 'nincs igaza')] + pt((P(1, -1) + P(-5, 7)) / 2),
    'kozep-6': sum((pt((-3, r)) for r in sorted(solve(Abs(det(P(-4, -2), P(2, 4), P(-3, y))) - 42, y),
                                               reverse=True)), []),
    'kozep-7': sum((pt((0, r)) for r in sorted(solve(Abs(det(P(-4, 1), P(2, 5), P(0, y))) - 28, y))), []),
    'kozep-8': pt((-1, [r for r in solve(Abs(det(P(-4, 1), P(5, -2), P(-1, y))) - 27, y) if r < 0][0])),
    'kozep-9': pt(([r for r in solve(Abs(det(P(1, -3), P(-6, 4), P(x, -1))) - 21, x) if r > 0][0], -1)),
    'kozep-10': [('', fr(solve(det(P(1, 2), P(3, 6), P(x, 10)), x)[0]))],
    'nehez-1': pt(list(solve([tav(P(x, y), P(-1, -3))**2 - tav(P(x, y), P(-4, 6))**2,
                              tav(P(x, y), P(-1, -3))**2 - tav(P(x, y), P(3, -1))**2], [x, y]).values()))
               + [('', fr(tav(P(-1, 2), P(3, -1))))],
    'nehez-2': [kerek(tav(P(-1, -2), P(-2, 6)))] + pt((P(-1, -2) + P(5, 2)) / 2)
               + [kerek(tav((P(-1, -2) + P(5, 2)) / 2, P(-2, 6))),
                  ('', fr(Abs(det(P(-1, -2), P(-2, 6), P(5, 2))) / 2))]
               + pt((P(-1, -2) + P(-2, 6) + P(5, 2)) / 3),
    'nehez-3': pt((P(-3, -1) + P(4, 3)) / 2) + [('', cipo([(-3, -1), (2, -2), (4, 3), (-1, 4)]))],
    'nehez-4': [('', fr(r)) for r in sorted(solve(Abs(det(P(0, 0), P(6, 0), P(t, t))) - 30, t), reverse=True)]
               + [('', fr(solve(tav(P(t, t), P(0, 0))**2 - tav(P(t, t), P(6, 0))**2, t)[0])),
                  ('', fr(Abs(det(P(0, 0), P(6, 0), P(3, 3))) / 2))],
    'joker': [('', F(49, 2)), ('', 21), ('', 15)],
}
