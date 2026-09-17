# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — Vészterem II. (kör, ellipszis, hiperbola, parabola).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import sqrt, Rational, symbols, solve, nsimplify, expand

FAJL = '3e/05-analitikus-geometria/feladatok-hazi-2.html'
x, y, A, B, n = symbols('x y A B n', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, k=2):
    return ('', F(str(round(float(v), k))))


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def met(g, l):
    s = solve([g, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s if r[x].is_real], key=lambda u: (float(u[0]), float(u[1])))


def kozep(e):
    e = expand(e)
    s = solve([e.diff(x), e.diff(y)], [x, y])
    return s[x], s[y], -e.subs({x: s[x], y: s[y]})


K1 = kozep(x**2 + y**2 + 8*x - 2*y - 8)
el = solve([36*A + B - 1, 4*A + 9*B - 1], [A, B])
M9 = met(x**2 + y**2 - 25, x + y - 1)
n12 = sorted(solve((2 * (-1) - 2 + n)**2 - 20 * (1 + 4), n))
n13 = sorted(solve(9 * 4 - 27 - n**2, n))          # 3x^2 - y^2 = 27: a^2 = 9, b^2 = 27, k = 2

TESZT = {
    'alap-1': pt(K1[:2]) + [('', fr(sqrt(K1[2])))],
    'alap-2': [('', -2), ('', 2), ('', -2), ('', 2), ('', fr((sqrt(6**2 + 8**2) / 2)**2))],
    'alap-3': [('', fr(sqrt(Rational(100, 4)))), ('', fr(sqrt(Rational(100, 25)))), ('', 21), kerek(sqrt(25 - 4)), ('', 21)],
    'alap-4': [('', fr(sqrt(Rational(100, 25)))), ('', fr(sqrt(Rational(100, 4)))), ('', 29), ('', 29), ('', F(5, 2))],
    'alap-5': [('', 3), ('', F(-3, 2)), ('', 0), ('', F(3, 2)), ('', 'balra')],
    'alap-6': [('', 'igen')] + pt(met((x - 2)**2 + (y - 2)**2 - 25, 3*x + 4*y - 39)[0]),
    'alap-7': [('', 3), ('', 10), ('', -25)],
    'kozep-1': [('', 2), ('', fr(1 / el[A])), ('', 2), ('', fr(1 / el[B])), ('', 1)],
    'kozep-2': pt(M9[1]) + pt(M9[0]) + [kerek(sqrt((M9[0][0] - M9[1][0])**2 + (M9[0][1] - M9[1][1])**2))],
    'kozep-3': [('', 'egy')] + pt(met(x**2 - y**2 - 9, y - x + 1)[0]) + [('', 'nem')],
    'kozep-4': pt(met(y**2 - 8*x, 2*x - 3*y + 8)[0]) + pt(met(y**2 - 8*x, 2*x - 3*y + 8)[1])
               + [('', 2), ('', -2), ('', 8)],
    'nehez-1': [('', 2), ('', fr(n12[1])), ('', fr(n12[0])), ('', 2), ('', fr(n12[1])), ('', 2), ('', fr(n12[0]))],
    'nehez-2': [('', 2), ('', fr(n13[1]))] + pt(met(3*x**2 - y**2 - 27, y - 2*x - n13[1])[0])
               + [('', 2), ('', fr(n13[0]))] + pt(met(3*x**2 - y**2 - 27, y - 2*x - n13[0])[0]),
}
