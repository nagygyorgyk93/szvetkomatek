# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/04 — vektorok a síkban és a térben (A blokk).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import Matrix, sqrt, Rational, symbols, solve

FAJL = '3e/04-vektorok/feladatok-vektorok.html'
t = symbols('t')


def fr(c):
    c = Rational(c)
    return F(int(c.p), int(c.q))


def vk(*k):
    """Vektor-koordináták sorrendben."""
    return [('', fr(x)) for x in k]


def M(*k):
    return Matrix(k)


def kerek(x, n=2):
    return ('', F(str(round(float(x), n))))


a, b, c, d = M(-3, 2, 4), M(-2, 1, -2), M(3, -4, 5), M(8, -5, 7)
p, q = M(4, -3, 1), M(5, -2, -3)
K, KA, KB = M(2, -3, 5), M(1, -3, 6) - M(2, -3, 5), M(1, -2, 5) - M(2, -3, 5)
X, Y, Z = M(1, 2, 0), M(4, 3, 1), M(2, -1, 3)

TESZT = {
    'alap-5': [('', 7), ('', 1), ('', 5)],
    'alap-6': [('', 60), ('', 120), ('', 120), ('', 180)],
    'alap-7': [('', 4), kerek(-4 * sqrt(3)), ('', 0), kerek(8 * 0.30901699437)],
    'alap-8': [('', 'igaz'), ('', 'hamis'), ('', 'igaz'), ('', 'igaz')],
    'alap-9': [('', 'y tengely'), ('', 'xz sik'), ('', 'z tengely'), ('', 'xy sik')],
    'alap-10': vk(2, -3, 1) + vk(0, 4, -1) + [('', 5), ('', -3)],
    'alap-11': vk(*(M(3, -1, 5) - M(1, 0, -2))) + vk(*(M(1, 0, -2) - M(3, -1, 5))),
    'alap-12': vk(*(2*a - 4*c + 6*d)) + vk(*(c + 3*b - 7*a)),
    'alap-13': [('', 26), kerek(p.norm()), kerek((p + q).norm()), ('', 18), kerek((p - q).norm())],
    'alap-14': [('', 54), kerek((M(3, -1, 5) - M(1, 0, -2)).norm()), ('', 49),
                ('', fr((M(-4, 1, 4) - M(2, 3, 1)).norm()))],
    'alap-15': vk(*(M(1, -2, 3) + M(6, 4, 4) - M(3, 2, 1))),
    'alap-16': vk(*((M(-7, 2, 8) + M(6, 4, 5)) / 2)),
    'alap-17': [('', -3), ('', 'nem parhuzamos'), ('', F(1, 2))],
    'alap-1': [('', 'AO'), ('', 'OD'), ('', 'FE'), ('', 'CB'), ('', 'EF'), ('', 'AD')],
    'alap-18': [('', fr(M(6, -2, 3).norm()))] + vk(*(M(6, -2, 3) / 7)) + vk(*(-M(6, -2, 3) / 7)),
    'kozep-3': [('', 34), kerek(sqrt(34)), ('', 109), kerek(sqrt(109)), ('', 61), kerek(sqrt(61))],
    'kozep-4': [('', fr(sqrt(12**2 + 5**2))), ('', F('22.6'))],
    'kozep-5': [('', 'nullvektor'), ('', 0)],
    'kozep-6': [('', fr(r)) for r in sorted(solve(5 + t**2 - (5*t**2 + 4), t), reverse=True)],
    'kozep-7': vk(*(2*M(Rational(1, 2), 1, -1) - M(1, 0, -2))) + vk(*(2*M(Rational(1, 2), 1, -1) - M(3, -1, 5))),
    'kozep-8': vk(*(2*M(1, 4, 1) - M(5, -2, 3))) + vk(*(2*M(7, 1, 4) - M(5, -2, 3))),
    'kozep-9': vk(*(2*M(6, 4, 5) - M(-7, 2, 8))),
    'kozep-10': vk(*(M(2, -1, 4) + (M(2, 2, 10) - M(2, -1, 4)) / 3)),
    'kozep-11': [('', 17), ('', 77), kerek(sqrt(17) + sqrt(77) + sqrt(72)), ('', 'hegyesszogu')],
    'kozep-12': [('', 3), ('', 3), ('', 18), ('', 'derekszog')],
    'nehez-1': vk(*(K + KB - KA)) + vk(*(K - KA)) + vk(*(K - KB)) + vk(*(K + KA - KB)),
    'nehez-3': vk(*(Y + Z - X)) + vk(*(X + Z - Y)) + vk(*(X + Y - Z)),
    'nehez-4': [('', fr(r)) for r in sorted(solve(4 + (t - 2)**2 + 16 - 24, t), reverse=True)]
               + [('', 'szabalyos'), ('', 8), ('', 'egyenlo szaru')],
    'joker': [('', 24), ('', 5), ('', 3)],
}
