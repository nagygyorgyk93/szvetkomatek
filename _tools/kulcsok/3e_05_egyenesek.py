# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — egyenesek (2. gyűjtemény).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül.
Egyenes általános alakja: a nem ±1 együtthatók és a nem nulla konstans számként, sorrendben."""
from fractions import Fraction as F
from math import gcd
from sympy import Matrix, sqrt, Rational, symbols, solve, Abs, atan, pi, acos, nsimplify

FAJL = '3e/05-analitikus-geometria/feladatok-egyenesek.html'
x, y, c = symbols('x y c', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def P(a, b):
    return Matrix([Rational(a), Rational(b)])


def norm(a, b, c0):
    """egesz, relativ prim egyutthatok, a > 0 (vagy a = 0 es b > 0)"""
    a, b, c0 = Rational(a), Rational(b), Rational(c0)
    lk = 1
    for q in (a.q, b.q, c0.q):
        lk = lk * q // gcd(lk, q)
    a, b, c0 = int(a * lk), int(b * lk), int(c0 * lk)
    g = gcd(gcd(abs(a), abs(b)), abs(c0)) or 1
    a, b, c0 = a // g, b // g, c0 // g
    if a < 0 or (a == 0 and b < 0):
        a, b, c0 = -a, -b, -c0
    return a, b, c0


def L(a, b, c0):
    """az ax+by+c=0 alak számai, ahogy a kulcs szövegében megjelennek"""
    a, b, c0 = norm(a, b, c0)
    ki = []
    if a not in (0, 1):
        ki.append(('', a))
    if b not in (0, 1, -1):
        ki.append(('', b))
    if c0 != 0:
        ki.append(('', c0))
    return ki


def ket_pont(p, q):
    return (q[1] - p[1], p[0] - q[0], -(q[1] - p[1]) * p[0] - (p[0] - q[0]) * p[1])


def adott_normal(nx, ny, p):
    return (nx, ny, -(nx * p[0] + ny * p[1]))


def metsz(l1, l2):
    s = solve([l1[0] * x + l1[1] * y + l1[2], l2[0] * x + l2[1] * y + l2[2]], [x, y])
    return P(s[x], s[y])


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def pe(l, p):
    return Abs(l[0] * p[0] + l[1] * p[1] + l[2]) / sqrt(l[0]**2 + l[1]**2)


def tav(p, q):
    return sqrt((p - q).dot(p - q))


def terulet(a, b, c0):
    return Abs((b - a)[0] * (c0 - a)[1] - (b - a)[1] * (c0 - a)[0]) / 2


A40, B40, C40 = P(-5, -4), P(9, -2), P(4, 8)
A39, B39, C39 = P(4, 6), P(-4, 0), P(-1, 4)
l28 = ket_pont(P(4, -1), metsz((2, -1, -4), (1, 1, -5)))
l27 = ket_pont(P(4, 3), metsz((3, -5, -11), (4, 1, -7)))
M33 = metsz((2, 1, -11), (1, 1, -8))
M34 = metsz((4, -3, -8), (1, 2, -13))
M35 = metsz((1, 3, -3), (1, -2, -2))
V41 = [metsz((1, -3, 14), (7, 2, 6)), metsz((7, 2, 6), (8, -1, -3)), metsz((1, -3, 14), (8, -1, -3))]
V16 = [metsz((3, -2, -19), (2, 1, 6)), metsz((2, 1, 6), (1, -3, 10)), metsz((1, -3, 10), (3, -2, -19))]
Mt = metsz((1, -2, 3), (2, 1, -9))
Bk = P(7, -3)
Psz = metsz(ket_pont(P(1, 5), Bk), (0, 1, 0))

TESZT = {
    'alap-2': [('', fr(solve(3 * (-1) + 2 * y + 11, y)[0]))],
    'alap-3': [('', fr(solve(5 * x - 12 - 13, x)[0]))],
    'alap-5': [('', fr(solve(4 * x + 10, x)[0])), ('', 0), ('', 0), ('', fr(solve(-5 * y + 10, y)[0]))],
    'alap-8': L(*ket_pont(P(1, 5), P(-3, 4))) + L(*ket_pont(P(-2, -3), P(0, 1)))
              + L(*ket_pont(P(Rational(1, 2), 5), P(5, 0))) + L(*ket_pont(P(-3, 1), P(-2, -4))),
    'alap-10': L(2, 3, -6) + pt(metsz((2, 3, -6), (0, 1, 0))) + pt(metsz((2, 3, -6), (1, 0, 0)))
               + L(1, -2, 4) + pt(metsz((1, -2, 4), (0, 1, 0))) + pt(metsz((1, -2, 4), (1, 0, 0)))
               + pt(metsz((2, 3, -6), (1, -2, 4))),
    'alap-11': pt(metsz((1, 2, -2), (3, -1, -13))) + pt(metsz((1, -3, 17), (3, 7, -29)))
               + pt(metsz((4, 3, 5), (2, 1, 2))),
    'alap-12': [('', 'egybeesnek'), ('', 'parhuzamosak')] + pt(metsz((1, 2, -4), (3, -1, -5)))
               + pt(metsz((1, 1, -4), (-2, 1, 5))),
    'alap-14': L(*adott_normal(2, -3, P(4, -3))) + L(*adott_normal(2, -5, P(-4, 3))) + L(*adott_normal(1, -4, P(-2, 1))),
    'alap-15': L(*adott_normal(3, 5, P(-3, 2))) + L(*adott_normal(3, 2, P(2, -3))) + L(*adott_normal(7, 1, P(-2, 5))),
    'alap-17': L(*adott_normal(1, -1, (P(1, -2) + P(3, -4)) / 2)) + L(*adott_normal(10, 4, (P(-7, 1) + P(3, 5)) / 2)),
    'alap-18': [kerek(atan(Rational(1, 2)) * 180 / pi, 1), ('', 90), ('', 30)],
    'alap-19': [('', fr(pe((12, -5, -27), P(4, -1)))), ('', fr(pe((3, -4, 15), P(3, 2)))),
                kerek(pe((1, -2, 7), P(-1, -2))), kerek(pe((2, -3, 0), P(7, -4)))],
    'alap-20': [('', fr(pe((5, -12, 26), P(Rational(13, 5), 0)))), ('', 2), ('', 10), kerek(pe((3, 1, 17), P(0, 3)))],
    'alap-21': [('', fr(pe((3, 4, -20), P(0, 0)))), kerek(pe((1, -1, 2), P(0, 0)))],
    'alap-22': [('', 'igen'), ('', fr(pe((3, -4, 10), P(1, 2))))],
    'alap-23': [('', 3), ('', -4), ('', 0), ('', fr(pe((3, -4, 0), P(1, -3)))), ('', fr(tav(P(0, 0), P(4, 3)))),
                ('', fr(terulet(P(0, 0), P(4, 3), P(1, -3))))],
    'alap-24': [('', -1), kerek(pe((3, -1, 1), P(1, 2)))],
    'kozep-1': pt(P(-1, -1)) + pt(P(2, 5)) + [('', fr((5 - (-1)) / Rational(2 - (-1)))), ('', 1)],
    'kozep-2': pt(metsz((2, -1, -4), (1, 1, -5))) + L(*l28),
    'kozep-3': pt(metsz((3, -5, -11), (4, 1, -7))) + [('', fr(-l27[0] / l27[1])), ('', fr(-l27[2] / l27[1]))],
    'kozep-4': [('', 4), ('', 6), ('', fr(Rational(4 * 6, 2)))],
    'kozep-5': [('', 80), ('', 200), ('', 80 * 12 + 200)],
    'kozep-6': [('', -6), ('', -2), ('', 3)],
    'kozep-7': pt(M33) + L(*adott_normal(5, 3, M33)),
    'kozep-8': pt(M34) + L(*adott_normal(1, -3, M34)),
    'kozep-9': pt(M35) + L(*adott_normal(2, 1, M35)),
    'kozep-11': [('', fr(solve(-x / 2 - Rational(1, 2), x)[0])), ('', fr(solve(-x / 2 * Rational(1, 2) + 1, x)[0]))],
    'kozep-12': pt(metsz((2, -1, 1), (1, 2, -12))) + [('', 90)],
    'kozep-13': L(*ket_pont(A39, B39)) + L(*ket_pont(A39, C39)) + L(*ket_pont(B39, C39))
                + L(*adott_normal(-(B39 - A39)[0], -(B39 - A39)[1], C39))
                + [('', fr(tav(A39, B39))), ('', fr(pe(ket_pont(A39, B39), C39))), ('', fr(terulet(A39, B39, C39)))],
    'kozep-14': [('', fr(terulet(A40, B40, C40)))] + L(*ket_pont(A40, B40)) + L(*ket_pont(A40, C40))
                + L(*ket_pont(B40, C40)) + L(*ket_pont(C40, (A40 + B40) / 2))
                + L(*adott_normal((C40 - B40)[0], (C40 - B40)[1], A40)),
    'kozep-15': pt(V41[0]) + pt(V41[1]) + pt(V41[2]) + [('', fr(terulet(*V41)))],
    'kozep-16': pt(V16[0]) + pt(V16[1]) + pt(V16[2]) + [('', fr(terulet(*V16)))],
    'kozep-17': [('', fr(r)) for r in sorted(solve(Abs(c) / 5 - 2, c), reverse=True)],
    'kozep-18': [kerek(pe((1, -1, 1), P(4, 1)))] + pt(metsz((1, -1, 1), (1, 1, -5))),
    'nehez-1': [kerek(tav(A40, B40)), kerek(tav(B40, (A40 + C40) / 2)), kerek(pe(ket_pont(A40, B40), C40)),
                ('', fr(acos((B40 - A40).dot(C40 - A40) / (tav(A40, B40) * tav(A40, C40))) * 180 / pi))],
    'nehez-2': pt(P(-2, -1) + P(5, 4) - P(4, 1))
               + [('', fr(2 * terulet(P(-2, -1), P(4, 1), P(5, 4))))] + pt((P(-2, -1) + P(5, 4)) / 2)
               + L(*ket_pont(P(4, 1), P(-2, -1) + P(5, 4) - P(4, 1))),
    'nehez-3': pt((P(1, 1) + P(5, 3)) / 2 + Matrix([-1, 2])) + pt((P(1, 1) + P(5, 3)) / 2 - Matrix([-1, 2])),
    'nehez-4': L(2, 1, -9) + pt(Mt) + pt(2 * Mt - P(5, -1)),
    'nehez-5': pt(Psz) + [('', fr(tav(P(1, 5), Bk))), ('', fr(tav(P(1, 5), Bk) * 100))],
    'joker': [('', 6), ('', 5), ('', 17), ('', 30), ('', 2)],
}
