# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — ellipszis és hiperbola (4. gyűjtemény).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül
(az adott irányú érintőket az érintési feltétellel, nem diszkriminánssal)."""
from fractions import Fraction as F
from math import gcd
from sympy import sqrt, Rational, symbols, solve, nsimplify

FAJL = '3e/05-analitikus-geometria/feladatok-ellipszis-hiperbola.html'
x, y, A, B = symbols('x y A B', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def L(a, b, c0):
    a, b, c0 = Rational(a), Rational(b), Rational(c0)
    lk = 1
    for q in (a.q, b.q, c0.q):
        lk = lk * q // gcd(lk, q)
    a, b, c0 = int(a * lk), int(b * lk), int(c0 * lk)
    g = gcd(gcd(abs(a), abs(b)), abs(c0)) or 1
    a, b, c0 = a // g, b // g, c0 // g
    if a < 0:
        a, b, c0 = -a, -b, -c0
    ki = [('', a)] if a not in (0, 1) else []
    ki += [('', b)] if b not in (0, 1, -1) else []
    return ki + ([('', c0)] if c0 else [])


def CAN(a2, b2):
    """x^2/a2 +- y^2/b2 = 1 szamai a szovegben"""
    return [('', 2), ('', fr(a2)), ('', 2), ('', fr(b2)), ('', 1)]


def ket_pontbol(p, q, jel):
    """A x^2 + jel * B y^2 = 1 -> (1/A, 1/B)"""
    s = solve([A * p[0]**2 + jel * B * p[1]**2 - 1, A * q[0]**2 + jel * B * q[1]**2 - 1], [A, B])
    return 1 / s[A], 1 / s[B]


def erinto_pont(a2, b2, jel, p):
    """x0x/a2 + jel*y0y/b2 = 1"""
    return (p[0] / Rational(a2), jel * p[1] / Rational(b2), -1)


def metsz(g, l):
    s = solve([g, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s if r[x].is_real], key=lambda u: (float(u[0]), float(u[1])))


def hur(pp):
    return sqrt((pp[0][0] - pp[1][0])**2 + (pp[0][1] - pp[1][1])**2)


def n_ell(a2, b2, k):
    return sqrt(Rational(a2) * k**2 + b2)


def n_hip(a2, b2, k):
    return sqrt(Rational(a2) * k**2 - b2)


K1 = ket_pontbol((2, -4), (-1, 3 * sqrt(2)), 1)
K2 = ket_pontbol((6, 4), (-8, 3), 1)
K9 = ket_pontbol((7, Rational(-3, 2)), (11, Rational(9, 2)), -1)
K10 = ket_pontbol((2, 2), (4, 5), -1)
M5 = metsz(x**2 + 3*y**2 - 12, x + y - 2)
M6 = metsz(x**2 + 4*y**2 - 40, x - 2*y + 4)
M13 = metsz(9*x**2 - y**2 - 144, x - y + 4)
M14 = metsz(3*x**2 - 4*y**2 - 8, x + 2*y - 4)
M16 = metsz(3*x**2 - 4*y**2 - 8, x - y - 1)
yM7 = -sqrt(8 * (1 - Rational(9, 18)))
xM15 = sqrt(5 * (1 + Rational(1, 4)))
yM9 = sqrt((25 - 9) / Rational(4))
yM19 = -sqrt((50 - 30) / Rational(5))

TESZT = {
    'alap-1': [('', 2), ('', 1), ('', 3), ('', 5), ('', 3), ('', fr(5 - 3)),
               ('', fr(sqrt(16))), ('', 1), ('', 15), ('', fr(sqrt(16))), ('', fr(sqrt(9))), ('', 16 - 9)],
    'alap-2': CAN(36, 4) + CAN(fr(8 + 1), 8) + CAN(20, 20 - 16),
    'alap-3': [('', fr(sqrt(289 - 225)))] + pt((8, 0)) + pt((-8, 0)),
    'alap-4': [('', 'rajta'), ('', 4 * 16 + 9 * 1), ('', 'rajta'), ('', 9 * 4)],
    'alap-5': CAN((10 / 2)**2, (4 / 2)**2),
    'alap-6': [('', 10), ('', 6)] + CAN(25, 25 - 9) + [('', 10), ('', fr(2 * sqrt(25 - 9)))],
    'alap-7': pt(metsz(x**2 + 2*y**2 - 18, x - y - 3)[1]) + pt(metsz(x**2 + 2*y**2 - 18, x - y - 3)[0])
              + [('', 'nincs')] + pt(metsz(x**2 + 2*y**2 - 18, 2*x - y + 9)[0]),
    'alap-8': L(*erinto_pont(80, 5, 1, (-8, 1))),
    'alap-9': pt((-3, yM9)) + L(*erinto_pont(25, Rational(25, 4), 1, (-3, yM9)))[:0] + [('', -3), ('', 8), ('', 25)],
    'alap-10': pt((0, 4)) + [('', 'nincs')] + pt((6, 0)) + [('', 'szelo')],
    'alap-11': [('', fr(sqrt(100))), ('', fr(sqrt(25))), ('', 5), ('', 5), ('', fr(sqrt(25))), ('', fr(sqrt(16))),
                ('', 25 + 16), ('', 2), ('', 2), ('', 2), ('', 2), ('', 2), ('', F(4, 3)), ('', 2), ('', 13), ('', 3)],
    'alap-12': CAN(4, 13 - 4) + CAN(9 - 4, 4) + CAN(10, 16 - 10),
    'alap-13': [('', F(2, 5)), ('', F(2, 3))],
    'alap-14': [('', 'igen'), ('', 25 - 16), ('', 12), ('', 'igen'), ('', 'igen')],
    'alap-15': [('', 'ellipszis'), ('', 'hiperbola'), ('', 'kor'), ('', 'parabola'), ('', 'hiperbola')],
    'alap-16': [('', fr(sqrt(36 + 64)))] + pt((10, 0)) + pt((-10, 0)) + [('', F(8, 6))],
    'alap-17': pt(metsz(4*x**2 - 5*y**2 - 20, 2*x + 5*y - 10)[0]) + pt(metsz(4*x**2 - 5*y**2 - 20, 2*x + 5*y - 10)[1])
               + [('', 'nincs')] + pt(metsz(4*x**2 - 5*y**2 - 20, 2*x + y + 4)[0]),
    'alap-18': L(*erinto_pont(4, 3, -1, (-4, 3))),
    'alap-19': pt((-5, yM19)) + L(*erinto_pont(15, 6, -1, (-5, yM19))),
    'alap-20': [('', 'egy')] + pt(metsz(x**2 - 4*y**2 - 4, 2*y - x - 4)[0]) + [('', 'nem')],
    'kozep-1': [('', 2), ('', 3), ('', fr(K1[0] * 2)), ('', 2), ('', fr(K1[0])), ('', 2), ('', fr(K1[1]))],
    'kozep-2': CAN(K2[0], K2[1]),
    'kozep-3': CAN(8**2 + 6**2, 36),
    'kozep-4': [('', 3 + 11), ('', 7), ('', 49 - 25)] + CAN(49, 24),
    'kozep-5': pt(M5[0]) + pt(M5[1]) + [kerek(hur(M5))],
    'kozep-6': pt(M6[0]) + pt(M6[1]) + [kerek(hur(M6))],
    'kozep-7': pt((3, yM7)) + L(*erinto_pont(18, 8, 1, (3, yM7))),
    'kozep-8': [kerek(hur(metsz(x**2 + 4*y**2 - 4, 2*y - x)))],
    'kozep-9': [('', 2), ('', -fr(K9[0] / K9[1])), ('', 2), ('', fr(K9[0]))] + CAN(K9[0], K9[1]),
    'kozep-10': [('', 7), ('', 2), ('', -4), ('', 2), ('', 12), ('', 2), ('', F(12, 7)), ('', 2), ('', 3)] if K10 == (Rational(12, 7), 3) else [('', 'HIBA')],
    'kozep-11': [('', 2), ('', 2), ('', fr((sqrt(2) * 1)**2))],
    'kozep-12': CAN(45 / Rational(5), 4 * 45 / Rational(5)),
    'kozep-13': pt(M13[0]) + pt(M13[1]) + [kerek(hur(M13))],
    'kozep-14': pt(M14[0]) + pt(M14[1]) + [kerek(hur(M14))],
    'kozep-15': pt((xM15, -1)) + L(*erinto_pont(5, 4, -1, (xM15, -1))),
    'kozep-16': pt(M16[0]) + pt(M16[1]) + L(*erinto_pont(Rational(8, 3), 2, -1, M16[0]))
                + L(*erinto_pont(Rational(8, 3), 2, -1, M16[1])),
    'nehez-1': [('', F(5, 3)), ('', fr(n_ell(27, 6, Rational(5, 3))**2)), ('', fr(n_ell(27, 6, Rational(5, 3)))),
                ('', F(5, 3)), ('', fr(n_ell(27, 6, Rational(5, 3)))), ('', F(5, 3)), ('', -fr(n_ell(27, 6, Rational(5, 3)))),
                ('', 5), ('', -3), ('', fr(3 * n_ell(27, 6, Rational(5, 3))))],
    'nehez-2': [('', F(-3, 2)), ('', fr(n_ell(40, 10, Rational(-3, 2)))), ('', F(-3, 2)), ('', fr(n_ell(40, 10, Rational(-3, 2)))),
                ('', F(-3, 2)), ('', -fr(n_ell(40, 10, Rational(-3, 2))))],
    'nehez-3': [('', fr((2 * n_ell(12, 6, Rational(-1, 2)))**2)), ('', fr(2 * n_ell(12, 6, Rational(-1, 2)))),
                ('', -fr(2 * n_ell(12, 6, Rational(-1, 2))))],
    'nehez-4': [('', fr(n_hip(36, 3, Rational(1, 3)))), ('', F(1, 3)), ('', fr(n_hip(36, 3, Rational(1, 3)))),
                ('', F(1, 3)), ('', -fr(n_hip(36, 3, Rational(1, 3))))],
    'nehez-5': [('', 7), ('', -8), ('', 2), ('', 14), ('', fr(n_hip(14, 7, 2))), ('', 2), ('', -fr(n_hip(14, 7, 2))), ('', 2), ('', fr(n_hip(14, 7, 2)))],
    'nehez-6': [('', 'elsofoku'), ('', -36), ('', 27), ('', 'egy')] + pt(metsz(x**2 - 9*y**2 - 9, x - 3*y + 6)[0])
               + [('', 'nincs'), ('', F(1, 3))],
    'joker': [('', fr(sqrt(20 - 4))), ('', fr(sqrt(4 + 12)))]
             + [('', 5), ('', 3), ('', 5), ('', 3), ('', 5), ('', 3), ('', 5), ('', 3)]
             + [('', 5), ('', 3), ('', 15), kerek(4 * sqrt(15))],
}
