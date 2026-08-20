# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/01 — a gúla, a metszetek és a csonkagúla.

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől
függetlenül; a harness veti össze őket a Végeredmény-lenyíló szövegével.
"""
from sympy import Rational as R, sqrt, N, symbols, solve, Eq

FAJL = '3e/01-poliederek/feladatok-gula.html'
x = symbols('x', positive=True)


def k(v, jegy=2):
    return round(float(N(v, 15)), jegy)


def B(n, a):
    return {3: a**2*sqrt(3)/4, 4: a**2, 6: 6*a**2*sqrt(3)/4}[n]


def rho(n, a):
    return {3: a*sqrt(3)/6, 4: R(1, 2)*a, 6: a*sqrt(3)/2}[n]


def mo(n, a, m):
    return sqrt(m**2 + rho(n, a)**2)


def M(n, a, mo_):
    return n*a*mo_/2


def V(n, a, m):
    return B(n, a)*m/3


# ── független számolások ────────────────────────────────────────────────
a3_rho, a3_mo = rho(4, 8), mo(4, 8, 3)
a4_b = sqrt(4**2 + 3**2)
a8_F = B(3, 6) + M(3, 6, 8)
a9_F = B(6, 4) + M(6, 4, 6)
a11_m = solve(Eq(25*x/3, 100), x)[0]
a13 = (rho(4, 10), mo(4, 10, 12), M(4, 10, 13), B(4, 10) + M(4, 10, 13), V(4, 10, 12))
a14_F = B(3, 8) + M(3, 8, 10)
a15_V = 6**2*5 + R(6**2*4, 3)
a17 = (R(1, 3)**2*81, R(1, 3)**3*54)
a21 = (8**2, 4**2, 4*(8 + 4)/2*6, 8**2 + 4**2 + 4*(8 + 4)/2*6)
a22_m = sqrt(5**2 - 3**2)
a22_F = 144 + 36 + 4*(12 + 6)/2*5
a22_V = R(4, 3)*(144 + 36 + sqrt(144*36))
a23_m = solve(Eq(x/3*(25 + 9 + 15), 98), x)[0]
a24_T = R((8 + 5)*4, 2)
a24_M = 6*a24_T
a25_V = R(12, 3)*(100 + 256 + sqrt(100*256))

k1_a = 2*solve(Eq(sqrt(5**2 - 4**2), x), x)[0]
k2_m = solve(Eq(V(4, 6, x), 60), x)[0]
k3 = (mo(4, 16, 6), M(4, 16, 10), B(4, 16) + M(4, 16, 10))
k4_a = solve(Eq(B(4, x)*9/3, 300), x)[0]
k5 = (mo(6, 4, 2), B(6, 4) + M(6, 4, 4), V(6, 4, 2))
k6 = (B(3, 12), V(3, 12, 5))
k7_a = solve(Eq(4*x*13/2, 260), x)[0]
k9 = (sqrt(12**2 + 5**2), 2*5)
k13_alsó = 100 - R(1, 8)*100
k14_m = sqrt(13**2 - 5**2)
k15 = (4*(14 + 8)/2*8, 14**2 + 8**2 + 4*(14 + 8)/2*8)
k16_m = sqrt(10**2 - 6**2)
k16_V = R(8, 3)*(400 + 64 + sqrt(400*64))
k11_V = R(1, 8)*216
k17_a1 = solve(Eq(4*(x + 10)/2*6, 216), x)[0]
k18_V = R(6, 3)*(49 + 25 + sqrt(49*25))
k19 = (R(9*4, 3), 9*4)
k20 = (rho(6, 8), mo(6, 8, 8))
k21_V = R(12, 3)*(64 + 16 + sqrt(64*16))
n1_m = sqrt(10**2 - 6**2)
n1_F = B(4, 12) + M(4, 12, 10)
n3_m = sqrt((8*sqrt(2))**2 - (4*sqrt(2))**2)
n5_m = solve(Eq(x/3*(100 + 36 + sqrt(100*36)), 392), x)[0]
j_F = 12**2 + 4*(12*6*sqrt(2))/2

TESZT = {
    'alap-3':  [('', int(a3_rho)), ('', int(a3_mo))],
    'alap-4':  [('', int(a4_b))],
    'alap-6':  [('', 36), ('', 60), ('', 96)],
    'alap-7':  [('', 48)],
    'alap-8':  [('', k(a8_F))],
    'alap-9':  [('', k(a9_F))],
    'alap-10': [('', 144)],
    'alap-11': [('', int(a11_m))],
    'alap-12': [('', 'háromszoros')],
    'alap-13': [('', int(a13[0])), ('', int(a13[1])), ('', int(a13[2])),
                ('', int(a13[3])), ('', int(a13[4]))],
    'alap-14': [('', k(a14_F))],
    'alap-15': [('', int(a15_V))],
    'alap-16': [('', 16)],
    'alap-17': [('', int(a17[0])), ('', int(a17[1]))],
    'alap-21': [('', int(a21[0])), ('', int(a21[1])), ('', int(a21[2])), ('', int(a21[3]))],
    'alap-22': [('', int(a22_m)), ('', int(a22_F)), ('', int(a22_V))],
    'alap-23': [('', int(a23_m))],
    'alap-24': [('', int(a24_T)), ('', int(a24_M))],
    'alap-25': [('', int(a25_V))],
    'kozep-1': [('', int(k1_a))],
    'kozep-2': [('', int(k2_m))],
    'kozep-3': [('', int(k3[0])), ('', int(k3[1])), ('', int(k3[2]))],
    'kozep-4': [('', int(k4_a))],
    'kozep-5': [('', int(k5[0])), ('', k(k5[1])), ('', k(k5[2]))],
    'kozep-6': [('', k(k6[0])), ('', k(k6[1]))],
    'kozep-7': [('', int(k7_a))],
    'kozep-9': [('', int(k9[0])), ('', int(k9[1]))],
    'kozep-11': [('', int(k11_V))],
    'kozep-13': [('', float(k13_alsó))],
    'kozep-14': [('', int(k14_m))],
    'kozep-15': [('', int(k15[0])), ('', int(k15[1]))],
    'kozep-16': [('', int(k16_m)), ('', int(k16_V))],
    'kozep-17': [('', int(k17_a1))],
    'kozep-18': [('', int(k18_V))],
    'kozep-19': [('', int(k19[0])), ('', int(k19[1]))],
    'kozep-20': [('', k(k20[0])), ('', k(k20[1]))],
    'kozep-21': [('', int(k21_V))],
    'nehez-1': [('', int(n1_m)), ('', int(n1_F))],
    'nehez-2': [('', 2)],
    'nehez-3': [('', k(n3_m))],
    'nehez-5': [('', int(n5_m))],
    'joker':   [('', k(j_F))],
}
