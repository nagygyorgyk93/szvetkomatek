# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/03 — a determináns és a Cramer-szabály (B blokk).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from itertools import permutations
from sympy import Matrix, symbols, solve, Rational

FAJL = '3e/03-linearis-rendszerek/feladatok-determinans.html'
X = symbols('X')


def fr(c):
    c = Rational(c)
    return F(int(c.p), int(c.q))


def d(*sorok):
    return ('', fr(Matrix(sorok).det()))


def cr(A, b, csak=None):
    """[D, Dx, Dy, (Dz), megoldás…] a kulcs sorrendjében."""
    A, b = Matrix(A), Matrix(b)
    ki = [('', fr(A.det()))]
    for j in range(A.shape[1]):
        if csak is None or j in csak:
            M = A.copy()
            M[:, j] = b
            ki.append(('', fr(M.det())))
    return ki


def ms(A, b, csak=None):
    s = Matrix(A).LUsolve(Matrix(b))
    return [('', fr(c)) for j, c in enumerate(s) if csak is None or j in csak]


A12 = ([[1, 1, 1], [2, 1, 3], [-1, 5, -2]], [6, 13, 3])
A13 = ([[1, 2, 3], [2, -1, 1], [3, 1, -2]], [3, 6, 3])
A15 = ([[2, 1, -1], [1, -1, 2], [3, 2, 1]], [0, 9, 7])
K5 = ([[2, 3, -1], [3, -2, 2], [4, 1, -3]], [1, -1, -11])
K6 = ([[2, 1, 1], [4, -3, 1], [6, 2, -1]], [2, 7, -1])
K7 = ([[1, 1, 1], [2, -1, 1], [1, 2, -1]], [2, 5, -3])
K9 = ([[6, 5], [1, -2]], [6, Rational(-7, 10)])
N1 = ([[3, 2, 1], [2, 1, 2], [1, 3, 2]], [330, 320, 400])
det2 = [p[0]*p[3] - p[1]*p[2] for p in permutations([1, 2, 3, 4])]

TESZT = {
    'alap-1': [d([2, 3], [-1, 5]), d([7, -3], [10, -9])],
    'alap-2': [d([4, -2], [6, -3]), d([-1, 5], [2, -3]), ('', F(3, 2))],
    'alap-3': [d([2, 3, -1], [0, 1, 4], [5, 1, 3])],
    'alap-4': [d([4, 1, 5], [-3, 2, 4], [1, 3, -5])],
    'alap-5': [('', 'elso sora'), d([2, 0, 0], [5, 3, 0], [1, 4, -1])],
    'alap-6': [('', 'masodik oszlopa'), d([1, 0, 2], [3, 0, -1], [4, 5, 6])],
    'alap-7': [('', 'csupa nulla'), ('', 'ket sora egyenlo'), ('', 'elso ketszerese'),
               d([1, 0, 0], [0, 2, 0], [0, 0, 3])],
    'alap-8': [('', -7), ('', 7), ('', 0)],
    'alap-9': cr([[3, 2], [5, -1]], [7, 3]) + ms([[3, 2], [5, -1]], [7, 3]),
    'alap-10': cr([[4, -3], [2, 5]], [1, -19]) + ms([[4, -3], [2, 5]], [1, -19]),
    'alap-12': cr(*A12) + ms(*A12),
    'alap-13': cr(*A13) + ms(*A13),
    'alap-14': [d([1, 2, -1], [2, 4, -2], [1, -1, 1]), ('', 'nem alkalmazhato'),
                d([1, 2, -1], [2, 1, -2], [1, -1, 1])],
    'alap-15': cr(*A15, csak={2}) + ms(*A15, csak={2}),
    'alap-16': [('', 'nem alkalmazhato'), ('', 'Gauss')],
    'kozep-1': [d([2, 1, 1], [-5, 1, 4], [12, 3, -4]), d([2, 1, 3], [5, 3, 2], [1, 4, 3])],
    'kozep-2': [d([3, 4, -5], [8, 7, -2], [2, -1, 8])],
    'kozep-3': [('', fr(r)) for r in sorted(solve(Matrix([[X - 2, 3, 1], [1, 5, X - 2],
                                                          [2, 1, -3]]).det(), X))],
    'kozep-4': [('', 'x^2+y^2')],
    'kozep-5': cr(*K5) + ms(*K5),
    'kozep-6': cr(*K6) + ms(*K6),
    'kozep-7': ms(*K7) + cr(*K7),
    'kozep-8': [('', 'hatarozatlan'), ('', 'ellentmondasos'), ('', -1)],
    'kozep-9': cr(*K9) + ms(*K9),
    'kozep-10': cr([[3, -2], [-1, 4]], [4, 2]) + ms([[3, -2], [-1, 4]], [4, 2]),
    'kozep-11': [('', F(24, -12)), ('', F(0, -12)), ('', F(-36, -12))],
    'nehez-1': cr(*N1, csak={2}) + ms(*N1, csak={2}),
    'nehez-2': [('', fr(r)) for r in sorted(solve(Matrix([[-1, 4, X + 1], [2, -1, X - 3],
                                                          [1, X, -1]]).det(), X))],
    'nehez-3': [('', 0), ('', 3), ('', -1), ('', 't=2: (x;y;z)=(1;1;2)'), ('', 'S_3-2S_1-S_2 után 0=1')],
    'nehez-4': [('', max(det2)), ('', min(det2))],
    'joker': [('', -1), ('', 0), ('', 24), ('', 8)],
}
