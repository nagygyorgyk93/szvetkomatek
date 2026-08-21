# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/02 — forgástestek és a henger.

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől
függetlenül. FONTOS: a harness a KaTeX-parancsokat (így a `\\pi`-t is) kidobja,
ezért a π-s végeredményeknél az EGYÜTTHATÓT kell várt értékként megadni
($104\\pi$ → 104).
"""
from sympy import Rational as R, sqrt, pi, N, symbols, solve, Eq

FAJL = '3e/02-forgastestek/feladatok-henger.html'
x = symbols('x', positive=True)


def k(v, jegy=2):
    return round(float(N(v, 15)), jegy)


def egyutt(v):
    """A π együtthatója (a harness a \\pi-t eltávolítja a szövegből)."""
    return N(v / pi)


B = lambda r: r**2
M = lambda r, H: 2*r*H
F = lambda r, H: 2*r**2 + 2*r*H
V = lambda r, H: r**2*H

a10 = (F(4, 9), V(4, 9))
a11 = (M(6, 10), F(6, 10), V(6, 10))
a12 = V(3, 5)
a13 = (F(4, 8), V(4, 8))
a14 = solve(Eq(V(7, x), 245), x)[0]
a15 = solve(Eq(V(x, 4), 100), x)[0]
a16 = solve(Eq(F(4, x), 112), x)[0]
a17 = (V(4, 10), k(V(4, 10)*pi), k(V(4, 10)*pi/100))
a18 = (V(2, 5), k(V(2, 5)*pi), round(float(N(V(2, 5)*pi*1000))))
a19 = B(3) + M(3, 8)
a20 = (M(1, 4), k(M(1, 4)*pi))
k6 = solve(Eq(F(x, 8), 96), x)[0]
k7 = solve(Eq(V(x, 2*x), 128), x)[0]
k8 = solve(Eq(F(x, 3*x), 32), x)[0]
k11 = (solve(Eq(2*x*6, 48), x)[0], V(4, 6))
k12 = (solve(Eq(2*x**2, 50), x)[0], solve(Eq(M(5, x), 60), x)[0])
k13 = round(float(N(R(72, 100)*pi*1000)))
n1 = (solve(Eq(F(x, 2*x), 54), x)[0], V(3, 6))
n3 = B(5)*3
n4 = solve(Eq(V(x, x), F(x, x)), x)[0]

TESZT = {
    'alap-2':  [('', 5), ('', 9)],
    'alap-4':  [('', 6), ('', 8), ('', 10)],
    'alap-5':  [('', 14), ('', 10)],
    'alap-6':  [('', 4)],
    'alap-7':  [('', 12)],
    'alap-8':  [('', 7)],
    'alap-9':  [('', 4), ('', 5)],
    'alap-10': [('', int(a10[0])), ('', int(a10[1]))],
    'alap-11': [('', int(a11[0])), ('', int(a11[1])), ('', int(a11[2]))],
    'alap-12': [('', int(a12))],
    'alap-13': [('', 8), ('', int(a13[0])), ('', int(a13[1]))],
    'alap-14': [('', int(a14))],
    'alap-15': [('', 25), ('', int(a15))],
    'alap-16': [('', int(a16))],
    'alap-17': [('', int(a17[0])), ('', a17[1]), ('', a17[2])],
    'alap-18': [('', int(a18[0])), ('', a18[1]), ('', a18[2])],
    'alap-19': [('', int(a19))],
    'alap-20': [('', int(a20[0])), ('', a20[1])],
    'kozep-1': [('', 6), ('', 4), ('', 144), ('', 4), ('', 6), ('', 96)],
    'kozep-2': [('', 4), ('', 3), ('', 16), ('', 3), ('', 4), ('', 12)],
    'kozep-3': [('', 12), ('', 6), ('', 7)],
    'kozep-4': [('', 100), ('', 10), ('', 5)],
    'kozep-5': [('', 30), ('', 15), ('', 5)],
    'kozep-6': [('', int(k6))],
    'kozep-7': [('', 64), ('', int(k7))],
    'kozep-8': [('', 4), ('', int(k8)), ('', 6)],
    'kozep-11': [('', int(k11[0])), ('', int(k11[1]))],
    'kozep-12': [('', 50), ('', int(k12[0])), ('', int(k12[1]))],
    'kozep-13': [('', k13)],
    'nehez-1': [('', int(n1[0])), ('', 6), ('', int(n1[1]))],
    'nehez-3': [('', int(n3))],
    'nehez-4': [('', int(n4))],
}
