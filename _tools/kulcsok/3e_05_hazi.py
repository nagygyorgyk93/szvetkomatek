# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — Vészterem I. (pontok és egyenesek).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import sqrt, Rational, symbols, solve, atan, pi, nsimplify, Abs

FAJL = '3e/05-analitikus-geometria/feladatok-hazi.html'
x, y, a = symbols('x y a', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def tav(p, q):
    return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


def terulet(A, B, C):
    return Abs((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) / 2


def pe(l, p):
    return Abs(l[0] * p[0] + l[1] * p[1] + l[2]) / sqrt(l[0]**2 + l[1]**2)


s8 = solve([2*x + y - 7, x - y - 2], [x, y])
s10 = solve([(x - 1)**2 + y**2 - (x - 5)**2 - (y - 2)**2, y - x - 1], [x, y])
P10 = (s10[x], s10[y])

TESZT = {
    'alap-1': [('', fr(tav((-4, 3), (2, -5))))] + pt(((-4 + 2) / Rational(2), (3 - 5) / Rational(2))),
    'alap-2': pt(((0 + 6 + 2) / Rational(3), (-2 + 1 + 4) / Rational(3))) + [('', fr(terulet((0, -2), (6, 1), (2, 4))))],
    'alap-3': [('', 2), ('', -2), ('', 1), ('', 2)] + pt((1, 0)) + pt((0, 2)),
    'alap-4': [('', 5), ('', -2), ('', 5 * 3 + 2 * 2), ('', 2), ('', 5), ('', -(2 * -3 + 5 * 2))],
    'alap-5': [('', fr(pe((4, -3, 5), (1, -2))))],
    'kozep-1': [('', 7), kerek(atan(Abs((Rational(-1, 2) - 3) / (1 + 3 * Rational(-1, 2)))) * 180 / pi, 1)],
    'kozep-2': [('', -3), ('', 2), kerek(pe((1, -3, 2), (3, 7))), ('', fr(terulet((1, 1), (7, 3), (3, 7))))],
    'kozep-3': pt((s8[x], s8[y])) + [('', -4)],
    'kozep-4': [('', fr(solve(-a / 4 * 2 + 1, a)[0])), ('', fr(solve(-a / 4 - 2, a)[0]))],
    'nehez-1': pt(P10) + [('', fr(terulet((1, 0), (5, 2), P10)))],
    'nehez-2': [('', 3), ('', 4), ('', fr(max(solve(Abs(a + 2) / 5 - 2, a)))), ('', 3), ('', 4), ('', fr(min(solve(Abs(a + 2) / 5 - 2, a))))],
}
