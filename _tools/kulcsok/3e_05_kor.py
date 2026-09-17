# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — a kör (3. gyűjtemény).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import sqrt, Rational, symbols, solve, expand, nsimplify

FAJL = '3e/05-analitikus-geometria/feladatok-kor.html'
x, y, t, c, q = symbols('x y t c q', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def kozep(expr):
    """altalanos alak -> (p, q, r^2), teljes negyzette alakitas nelkul: gradiens nullhelye"""
    e = expand(expr)
    s = solve([e.diff(x), e.diff(y)], [x, y])
    return s[x], s[y], -e.subs({x: s[x], y: s[y]})


def C(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def metsz(kor, l):
    s = solve([kor, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s], key=lambda u: (float(u[0]), float(u[1])))


def KOR(p, q0, r2):
    """a (x-p)^2+(y-q)^2=r^2 alak szamai, ahogy a szovegben megjelennek"""
    ki = []
    for u in (p, q0):
        ki += [('', fr(-u)), ('', 2)] if u != 0 else [('', 2)]
    return ki + [('', fr(r2))]


def pontok(lst):
    ki = []
    for p in lst:
        ki += C(p)
    return ki


def erinto_n(kor, k, par):
    """y = kx + par erinto: a behelyettesitett masodfoku egyenlet diszkriminansa 0"""
    e = expand(kor.subs(y, k * x + par))
    a2, b2, c2 = e.coeff(x, 2), e.coeff(x, 1), e.coeff(x, 0)
    return sorted(solve(b2**2 - 4 * a2 * c2, par), key=float)


def tav2(p, r):
    return (p[0] - r[0])**2 + (p[1] - r[1])**2


K9 = x**2 + y**2 - 2*x + 6*y - 15
K15 = x**2 + y**2 + 4*x - 2*y - 5
K16 = x**2 + y**2 - 4*x + 6*y + 8
K10 = x**2 + y**2 - 6*x - 4*y - 12
M15 = metsz(K15, 3*x + y + 5)
M10 = metsz(K10, x - y + 4)

TESZT = {
    'alap-1': C(kozep((x - 5)**2 + (y + 2)**2)) + [('', 2), ('', 5)] + C(kozep((x + 4)**2 + y**2))
              + [('', fr(sqrt(121)))] + C((0, 0)) + [('', F(3, 2))] + C((0, 7)) + [('', 5)] + C((0, 0)) + [('', F(5, 2))],
    'alap-3': KOR((7 + 3) / Rational(2), (-4 + 2) / Rational(2), tav2((7, -4), (3, 2)) / 4)
              + KOR(0, -2, tav2((-3, 2), (3, -6)) / 4)
              + KOR((-5 + 3) / Rational(2), (7 - 1) / Rational(2), tav2((-5, 7), (3, -1)) / 4),
    'alap-4': C(kozep(x**2 + y**2 - 10*x + 2*y + 22)[:2]) + [('', fr(sqrt(kozep(x**2 + y**2 - 10*x + 2*y + 22)[2])))]
              + C(kozep(x**2 + y**2 - 2*x - 8*y - 8)[:2]) + [('', fr(sqrt(kozep(x**2 + y**2 - 2*x - 8*y - 8)[2])))]
              + C(kozep(x**2 + y**2 + 6*y + 7)[:2])
              + C(kozep(x**2 + y**2 - 3*x + 2*y + 2)[:2]) + [('', 5), ('', 2)]
              + C(kozep(x**2 + y**2 - 6*x - y + 3)[:2]) + [('', fr(sqrt(kozep(x**2 + y**2 - 6*x - y + 3)[2])))],
    'alap-5': [('', 'a koron'), ('', tav2((6, 1), (1, -2))), ('', tav2((-1, 0), (1, -2)))],
    'alap-6': [('', fr(sqrt(tav2((1, 5), (-2, 1)))))],
    'alap-7': C(kozep(x**2 + y**2 - 4*x + 6*y + 4)[:2]) + [('', fr(sqrt(kozep(x**2 + y**2 - 4*x + 6*y + 4)[2])))]
              + [('', fr(kozep(x**2 + y**2 + 2*x - 4*y + 10)[2])), ('', 2), ('', 2)]
              + C(kozep(x**2 + y**2 - 8*x)[:2]) + [('', fr(sqrt(kozep(x**2 + y**2 - 8*x)[2])))],
    'alap-8': [('', 'igen'), ('', tav2((4, 6), (2, 3))), ('', 'nem'), ('', tav2((6, 7), (2, 3)))],
    'alap-9': pontok(sorted(metsz(K9, x - 2*y - 12), key=lambda u: -u[0]))
              + [('', 'nincs')] + pontok(metsz(K9, 3*x - 4*y + 10)),
    'alap-10': pontok(metsz(x**2 + y**2 - 6*x + 4*y + 8, x + 2*y + 1)),
    'alap-11': pontok(metsz(x**2 + y**2 - 4*x + 2*y - 15, 2*x + y - 3)),
    'alap-12': [('', -3), ('', 4), ('', 25), ('', 2), ('', 3), ('', -14)],
    'alap-13': [('', 5), ('', 5), ('', 'szelo'), ('', 5), ('', 'erinto'), kerek(9 / sqrt(2)), kerek(sqrt(20))],
    'alap-14': pontok(metsz((x - 1)**2 + (y + 1)**2 - 25, y - 2)) + [('', 8)],
    'kozep-1': [('', fr(r)) for r in sorted(solve((4 + t)**2 + (-1 + 3*t)**2 - 25, t))],
    'kozep-2': [('', fr(solve((-3 + 2*t)**2 + (4 - t)**2 - 5, t)[0]))],
    'kozep-3': C(tuple(solve([2*x + y - 3, x + 4*y + 2], [x, y]).values())) + [('', 20)],
    'kozep-4': C((solve((6 - x)**2 + 4 - x**2 - 16, x)[0], 0)) + [('', 20)],
    'kozep-5': C(M15[0]) + C(M15[1]) + [('', 2), ('', 10), kerek(sqrt(tav2(*M15)))],
    'kozep-6': [('', 2), ('', 3), ('', 2), ('', 7), kerek(2 * sqrt(9 - 2))],
    'kozep-7': [('', 3), ('', 4), ('', -19)],
    'kozep-8': [('', 'nincs'), ('', tav2((4, 4), (-1, 2)))] + C((3, 5)) + [('', 4), ('', 3), ('', -27)],
    'kozep-9': pontok(list(reversed(metsz(K16, x - 2*y - 5)))) + [kerek(sqrt(tav2(*metsz(K16, x - 2*y - 5))))],
    'kozep-10': C(kozep(K10)[:2]) + [('', fr(sqrt(kozep(K10)[2])))] + pontok(M10)
                + [kerek(sqrt(tav2(*M10))), kerek(abs(3 - 2 + 4) / sqrt(2))],
    'nehez-1': [('', 5), ('', 4), ('', 2), ('', 2), ('', -2), ('', -3), ('', 2), ('', 5),
                kerek(erinto_n((x - 1)**2 + (y - 1)**2 - 4, -2, c)[0] * -1), kerek(erinto_n((x - 1)**2 + (y - 1)**2 - 4, -2, c)[1] * -1)],
    'nehez-2': [('', fr(r)) for r in sorted((-v for v in erinto_n(x**2 + y**2 - 5*x - 7*y + 6, -1, c)), reverse=True)]
               + [('', fr(r)) for r in sorted(-v for v in erinto_n(x**2 + y**2 - 8*x + 2*y + 12, 2, c))],
    'nehez-3': [('', fr(r)) for r in sorted(solve((abs(1) * (5 - 2*q + 1))**2 - 100, q))],
    'nehez-4': C(kozep(K15)[:2]) + [('', 10)] + [('', -3), ('', fr(erinto_n(K15, -3, c)[1])),
                                                  ('', -3), ('', fr(erinto_n(K15, -3, c)[0]))]
               + [('', F(1, 3)), ('', fr(erinto_n(K15, Rational(1, 3), c)[1])),
                  ('', F(1, 3)), ('', fr(erinto_n(K15, Rational(1, 3), c)[0]))],
    'nehez-5': [('', F(1, 2)), ('', fr(erinto_n(K16, Rational(1, 2), c)[1])),
                ('', F(1, 2)), ('', fr(erinto_n(K16, Rational(1, 2), c)[0])),
                ('', -2), ('', fr(erinto_n(K16, -2, c)[1])), ('', -2), ('', fr(erinto_n(K16, -2, c)[0]))],
    'joker': [('', 10), ('', -7), ('', 3), ('', F(9, 5)), ('', F(12, 5))],
}
