# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/02 — a kúp, a síkmetszetek és a csonkakúp.

A harness a KaTeX-parancsokat (így a `\\pi`-t is) kidobja, ezért a π-s
végeredményeknél az EGYÜTTHATÓ a várt érték ($96\\pi$ → 96).
"""
from sympy import Rational as R, sqrt, pi, N, symbols, solve, Eq

FAJL = '3e/02-forgastestek/feladatok-kup.html'
x = symbols('x', positive=True)


def k(v, jegy=2):
    return round(float(N(v, 15)), jegy)


S = lambda r, H: sqrt(r**2 + H**2)
M = lambda r, s: r*s
F = lambda r, s: r**2 + r*s
V = lambda r, H: R(1, 3)*r**2*H
Scs = lambda RR, r, H: sqrt(H**2 + (RR - r)**2)
Mcs = lambda RR, r, s: (RR + r)*s
Vcs = lambda RR, r, H: R(1, 3)*H*(RR**2 + RR*r + r**2)

a7 = (M(6, 10), F(6, 10))
a8 = (S(5, 12), F(5, 13), V(5, 12))
a13 = solve(Eq(M(5, x), 65), x)[0]
a14 = solve(Eq(V(6, x), 96), x)[0]
a15 = solve(Eq(V(x, 12), 100), x)[0]
a16 = (V(2, R(15, 10)), k(V(2, R(15, 10))*pi))
a26 = Vcs(6, 3, 4)
a27 = Vcs(5, 2, 6)
a28 = (Vcs(10, 7, 12), k(Vcs(10, 7, 12)*pi), k(Vcs(10, 7, 12)*pi/1000))
k4 = (solve(Eq(F(6, x), 96), x)[0], sqrt(10**2 - 6**2))
k5 = solve(Eq(F(x, 5), 24), x)[0]
k6 = (solve(Eq(x**2*sqrt(3)/4, 9*sqrt(3)), x)[0], V(3, 3*sqrt(3)))
k8 = solve(Eq(V(x, 3*x), 27), x)[0]
k10 = (sqrt(25**2 - 24**2), F(7, 25), V(7, 24))
k12 = (solve(Eq(7*x, 84), x)[0], V(7, 12))
k15 = (solve(Eq(2*x + 20, 32), x)[0], V(6, 8))
k17 = solve(Eq(Vcs(5, 3, x), 196), x)[0]
k18 = solve(Eq(Scs(10, x, 12), 13), x)[0]
n1 = (solve(Eq(F(x, 10), 144), x)[0], V(8, 6))
n5 = V(6, 6)

TESZT = {
    'alap-1':  [('', 25), ('', 144), ('', 169), ('', 13)],
    'alap-2':  [('', 225), ('', 144), ('', 12)],
    'alap-3':  [('', 289), ('', 225), ('', 15)],
    'alap-4':  [('', 10), ('', 5)],
    'alap-5':  [('', 10), ('', 216)],
    'alap-7':  [('', int(a7[0])), ('', int(a7[1]))],
    'alap-8':  [('', int(a8[0])), ('', int(a8[1])), ('', int(a8[2]))],
    'alap-9':  [('', 12)],
    'alap-10': [('', 324)],
    'alap-11': [('', 8), ('', 96)],
    'alap-12': [('', 6), ('', 27)],
    'alap-13': [('', int(a13))],
    'alap-14': [('', int(a14))],
    'alap-15': [('', 4), ('', 100), ('', int(a15))],
    'alap-16': [('', int(a16[0])), ('', a16[1])],
    'alap-17': [('', 12), ('', 10), ('', 120)],
    'alap-18': [('', 60), ('', 13), ('', 36)],
    'alap-19': [('', 4), ('', 16)],
    'alap-20': [('', 49)],
    'alap-21': [('', 3), ('', 9)],
    'alap-22': [('', 5)],
    'alap-23': [('', 100), ('', 36), ('', 8)],
    'alap-24': [('', 45)],
    'alap-25': [('', 90)],
    'alap-26': [('', 63), ('', int(a26))],
    'alap-27': [('', 39), ('', int(a27))],
    'alap-28': [('', 219), ('', int(a28[0])), ('', a28[1]), ('', a28[2])],
    'kozep-1': [('', 16), ('', 8), ('', 17), ('', 15)],
    'kozep-2': [('', 4), ('', 12)],
    'kozep-3': [('', 6), ('', 12)],
    'kozep-4': [('', int(k4[0])), ('', int(k4[1]))],
    'kozep-5': [('', int(k5))],
    'kozep-6': [('', 36), ('', int(k6[0])), ('', 3), ('', 6)],
    'kozep-8': [('', int(k8)), ('', 9)],
    'kozep-9': [('', 144), ('', 48), ('', 96)],
    'kozep-10': [('', int(k10[0])), ('', int(k10[1])), ('', int(k10[2]))],
    'kozep-11': [('', 135), ('', 12)],
    'kozep-12': [('', int(k12[0])), ('', int(k12[1]))],
    'kozep-13': [('', 8), ('', 4), ('', 8), ('', 128)],
    'kozep-14': [('', 4), ('', 12)],
    'kozep-15': [('', 6), ('', 8), ('', 96)],
    'kozep-16': [('', 13), ('', 169), ('', 266)],
    'kozep-17': [('', int(k17))],
    'kozep-18': [('', int(k18))],
    'kozep-19': [('', 9)],
    'kozep-20': [('', 256), ('', 32), ('', 224)],
    'kozep-21': [('', 549), ('', 14372.79), ('', 14.37)],
    'nehez-1': [('', 26), ('', int(n1[0])), ('', 6), ('', int(n1[1]))],
    'nehez-3': [('', 9)],
    'nehez-5': [('', 6), ('', int(n5))],
}
