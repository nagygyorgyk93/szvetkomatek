# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/04 — a skaláris és a vektoriális szorzat, alkalmazások (B + C blokk).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül."""
from fractions import Fraction as F
from sympy import Matrix, sqrt, acos, pi, Rational, symbols, solve, N

FAJL = '3e/04-vektorok/feladatok-szorzatok.html'
t, k, x = symbols('t k x')


def fr(c):
    c = Rational(c)
    return F(int(c.p), int(c.q))


def M(*a):
    return Matrix(a)


def vk(v):
    return [('', fr(e)) for e in v]


def kerek(v, n=2):
    return ('', F(str(round(float(N(v)), n))))


def szog(u, w, n=1):
    return kerek(acos(u.dot(w) / (u.norm() * w.norm())) * 180 / pi, n)


def ter(A, B, C):
    return (B - A).cross(C - A).norm() / 2


I, J, K = M(1, 0, 0), M(0, 1, 0), M(0, 0, 1)

TESZT = {
    'alap-1': [('', 10), ('', 0), ('', -10), ('', -20)],
    'alap-3': [('', fr(M(1, 2, 5).dot(M(-1, 3, -7)))), ('', fr(M(0, 2, 3).dot(M(-2, 1, 3)))),
               ('', fr(M(2, 3, 4).dot(M(5, 7, -1))))],
    'alap-4': [('', 'hegyesszog'), ('', 'derekszog'), ('', 'tompaszog')],
    'alap-5': [('', fr(solve(M(1, -1, 2).dot(M(5, -1, x)), x)[0]))],
    'alap-6': [szog(M(8, 2, 2), M(4, -4, 0), 0), szog(M(-1, 1, 0), M(-1, 2, -2), 0),
               ('', fr(M(1, 2, 3).dot(M(5, 4, -7)))), szog(M(1, 2, 3), M(5, 4, -7))],
    'alap-7': [('', -6), ('', 12)],
    'alap-8': [('', 'igaz'), ('', 'hamis'), ('', 'hamis'), ('', 'igaz')],
    'alap-9': [kerek(3 * sqrt(2)), ('', 6), ('', 0)],
    'alap-10': vk(M(1, 2, 1).cross(M(2, 3, -2))) + [kerek(sqrt(66))]
               + vk(M(-2, 7, -8).cross(M(1, 7, -9))) + [kerek(M(-2, 7, -8).cross(M(1, 7, -9)).norm())],
    'alap-12': vk(-M(2, -1, 4)) + vk(3 * M(2, -1, 4)) + vk(-2 * M(2, -1, 4)),
    'alap-13': vk(M(-1, -4, 3).cross(M(-2, 3, 6))) + [kerek(M(-1, -4, 3).cross(M(-2, 3, 6)).norm())],
    'alap-14': vk(M(5, 7, -9) - M(5, -3, -4)) + vk(M(3, -7, 2) - M(5, -3, -4))
               + vk((M(5, 7, -9) - M(5, -3, -4)).cross(M(3, -7, 2) - M(5, -3, -4)))
               + [kerek(ter(M(5, -3, -4), M(5, 7, -9), M(3, -7, 2)))],
    'alap-15': vk(M(1, 0, 2).cross(M(0, 1, -1))),
    'alap-16': [('', 'parhuzamos'), ('', 'nem parhuzamos')],
    'kozep-5': [kerek(5 + 5*sqrt(3) + 3*sqrt(6)), szog(M(-4, 0, -3), M(1, -7, -2))],
    'alap-18': [('', 0), kerek(ter(M(1, 0, 1), M(3, 1, 3), M(0, 2, 1)))],
    'alap-19': [('', 'teglalap'), ('', 'nem negyzet'), kerek(sqrt(45))],
    'kozep-16': [('', 'igen'), ('', 7)],
    'alap-21': vk(M(3, -2, 4) + M(1, 5, -1) + M(-2, 1, 1)) + [('', fr((M(2, 4, 4)).norm())), kerek(acos(Rational(2, 6)) * 180 / pi, 1)],
    'alap-22': [('', fr(M(2, 3, 1).dot(M(5, 0, -2))))],
    'kozep-1': [('', 13), kerek(sqrt(13)), ('', -61)],
    'kozep-2': [('', fr(r)) for r in sorted(solve(M(t, t + 1, 1).dot(M(t, 2, -5)), t), reverse=True)],
    'kozep-3': [('', fr(r)) for r in sorted(solve((M(1, 2, 3) + k*M(k, 1, -1)).dot(M(-1, 0, 1)), k), reverse=True)],
    'kozep-4': [('', -3)],
    'alap-17': [szog(M(0, 4, 0), M(0, 2, 2), 0), ('', 11), szog(M(0, 1, -4), M(-8, 3, -2))],
    'kozep-6': vk(M(1, -2, 3) + M(3, -3, 4) - M(1, -4, 4)) + [('', 0), ('', 90), ('', 'rombusz'), ('', 'nem negyzet'), ('', 5), ('', -2)],
    'kozep-7': [('', 24), ('', 60)],
    'kozep-8': vk(M(2, 1, -1).cross(M(1, -1, 2))) + vk(2 * M(2, 1, -1).cross(M(1, -1, 2)))
               + vk(4 * M(2, 1, -1).cross(M(1, -1, 2))),
    'kozep-9': [kerek(ter(M(2, -3, 4), M(5, 3, -4), M(6, -7, 2))),
                kerek(2 * ter(M(2, -3, 4), M(5, 3, -4), M(6, -7, 2)) / 6),
                szog(M(2, -3, 4) - M(6, -7, 2), M(5, 3, -4) - M(6, -7, 2))],
    'kozep-10': vk(M(3, 3, 1) + M(1, 2, 2) - M(2, 1, 0)) + [kerek(sqrt(27))],
    'kozep-11': vk(M(1, 2, 2).cross(M(2, 1, -2)) / 9),
    'kozep-12': [('', 11), ('', -22), ('', 11)],
    'kozep-13': [kerek(ter(M(2, -3, -4), M(1, 3, -4), M(6, -5, -2))),
                 kerek(2 * ter(M(2, -3, -4), M(1, 3, -4), M(6, -5, -2)) / sqrt(93)),
                 szog(M(1, -6, 0), M(5, -8, 2))],
    'kozep-14': vk(M(2, 1, -2) + M(4, 3, 2) - M(4, 0, -1)) + [('', 60), kerek(6 * sqrt(3))],
    'kozep-15': [('', 2), kerek(ter(M(1, 2, 0), M(3, 2, 1), M(0, 4, 2)))],
    'alap-20': [('', 'nem'), ('', 8)],
    'kozep-17': [kerek(ter(M(-3, 3, -4), M(-2, 3, -4), M(-1, -2, 2))),
                 kerek(1 + sqrt(62) + sqrt(65))],
    'kozep-18': [('', 'mellekszog'), ('', 7), szog(M(-2, 1, -2), M(-3, 3, 1))],
    'nehez-1': [('', -5), ('', 19), ('', 7), kerek(acos(-5 / sqrt(133)) * 180 / pi, 1)],
    'nehez-3': vk(M(6, 2, -3).cross(M(-3, 6, -2)) / 7),
    'nehez-4': [('', 3), ('', -3)],
    'joker': [('', 'nem asszociativ')],
}
