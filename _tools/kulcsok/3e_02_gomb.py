# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/02 — a gömb és az összetett testek.

A harness a KaTeX-parancsokat (így a `\\pi`-t is) kidobja, ezért a π-s
végeredményeknél az EGYÜTTHATÓ a várt érték ($288\\pi$ → 288). A kivonás
második tagját a harness NEGATÍV számként olvassa ($225-81$ → 225 és −81),
ezért az ilyen köztes értékeket nem várjuk el külön.
"""
from sympy import Rational as R, sqrt, pi, N, symbols, solve, Eq

FAJL = '3e/02-forgastestek/feladatok-gomb.html'
x = symbols('x', positive=True)


def k(v, jegy=2):
    return round(float(N(v, 15)), jegy)


Fg = lambda Rr: 4*Rr**2
Vg = lambda Rr: R(4, 3)*Rr**3
Vh = lambda r, H: r**2*H
Vk = lambda r, H: R(1, 3)*r**2*H
Mh = lambda r, H: 2*r*H

a15 = (Fg(11), k(Fg(11)*pi))
a16 = (Vg(10), k(Vg(10)*pi/1000))
k10 = (Vg(3), k(Vg(3)*pi), k(Vg(3)*pi*R(785, 100)))
k17 = (Vg(3), k(Vg(3)*pi), k(216 - Vg(3)*pi), k((216 - Vg(3)*pi)/216*100))
n2 = solve(Eq(Vh(5, x), Vg(3)), x)[0]
n4 = (Vg(4), k(Vg(4)*pi), round(float(N(Vg(4)*pi*1000))))

TESZT = {
    'alap-1':  [('', 9)],
    'alap-2':  [('', 6), ('', 10), ('', 10), ('', 12)],
    'alap-4':  [('', 7), ('', 49)],
    'alap-7':  [('', int(Fg(6))), ('', 864), ('', int(Vg(6)))],
    'alap-8':  [('', 36), ('', 36)],
    'alap-9':  [('', 100), ('', 125), ('', 500)],
    'alap-10': [('', 6), ('', 216), ('', 288)],
    'alap-11': [('', 64), ('', 16), ('', 4)],
    'alap-12': [('', 196), ('', 49), ('', 7)],
    'alap-13': [('', 36), ('', 27), ('', 3)],
    'alap-14': [('', 972), ('', 729), ('', 9)],
    'alap-15': [('', 11), ('', 121), ('', int(a15[0])), ('', a15[1])],
    'alap-16': [('', 4000), ('', 4188.79), ('', 4.19)],
    'alap-17': [('', 36), ('', 27), ('', 18), ('', 54)],
    'alap-18': [('', 160), ('', 70)],
    'alap-19': [('', 54), ('', 12), ('', 66)],
    'alap-20': [('', 120), ('', 25), ('', 50), ('', 170)],
    'alap-21': [('', 360), ('', 320)],
    'alap-22': [('', 40), ('', 44)],
    'kozep-2': [('', 13), ('', 13)],
    'kozep-5': [('', 4), ('', 9), ('', 8), ('', 27)],
    'kozep-8': [('', 2)],
    'kozep-9': [('', 12), ('', 432), ('', 288)],
    'kozep-10': [('', 27), ('', int(k10[0])), ('', k10[1]), ('', k10[2])],
    'kozep-11': [('', 3)],
    'kozep-12': [('', 360), ('', 216), ('', 144), ('', 504)],
    'kozep-13': [('', 120), ('', 36), ('', 72), ('', 192)],
    'kozep-14': [('', 110), ('', 22), ('', 120), ('', 100), ('', 242)],
    'kozep-15': [('', 8), ('', 96), ('', 8), ('', 104)],
    'kozep-16': [('', 27), ('', 36), ('', 16)],
    'kozep-17': [('', 3), ('', int(k17[0])), ('', k17[1]), ('', 216), ('', k17[3])],
    'nehez-2': [('', 36), ('', 25), ('', float(n2))],
    'nehez-3': [('', 1.25), ('', 1.5625), ('', 56.25), ('', 1.953125), ('', 95.31)],
    'nehez-4': [('', 4), ('', 64), ('', 256), ('', n4[1]), ('', n4[2])],
}
