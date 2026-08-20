# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/01 — a hasáb (felszín, térfogat, átlók, metszetek).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől
függetlenül; a harness veti össze őket a Végeredmény-lenyíló szövegével.
"""
from sympy import Rational as R, sqrt, N, symbols, solve, Eq, tan, rad

FAJL = '3e/01-poliederek/feladatok-hasab.html'
x = symbols('x', positive=True)


def k(v, jegy=2):
    return round(float(N(v, 15)), jegy)


def B(n, a):
    """Szabályos n-szög alapú hasáb alapterülete."""
    return {3: a**2*sqrt(3)/4, 4: a**2, 6: 6*a**2*sqrt(3)/4}[n]


# ── független számolások ────────────────────────────────────────────────
kocka5 = (5*sqrt(2), 5*sqrt(3))
teglatest_atlo = sqrt(12**2 + 9**2 + 8**2)
h3_F = 2*B(3, 6) + 3*6*10
h3_V = B(3, 6)*10
h6_F = 2*B(6, 4) + 6*4*9
h6_V = B(6, 4)*9
akvarium_l = R(80*40*50, 1000)
akvarium_uveg = R(80*40 + 2*80*50 + 2*40*50, 10000)
metszet_negyzetes = 6*sqrt(2)*10
metszet_teglatest = sqrt(6**2 + 8**2)*10
metszet_hatszog = (2*4*7, 4*sqrt(3)*7)

k1_lapatlo = 12*sqrt(2)
k2_x = solve(Eq(sqrt((3*x)**2 + (4*x)**2 + (12*x)**2), 26), x)[0]
k3_m = solve(Eq(2*6**2 + x**2, 9**2), x)[0]
k4_testatlo = 6*sqrt(3)
k5_F = 2*B(3, 8) + 3*8*5
k5_V = B(3, 8)*5
k6_m = solve(Eq(2*4**2 + 4*4*x, 192), x)[0]
k7_a = solve(Eq(6*x*10, 360), x)[0]
k7_V = B(6, 6)*10
k8_a = solve(Eq(x**2*sqrt(3)/4, 49*sqrt(3)), x)[0]
k8_V = 49*sqrt(3)*14
k10_V = R((R(14, 10) + R(26, 10))*25, 2)*10
k11_V = B(6, R(3, 10))*3
k12_l = R(12, 10)*R(8, 10)*R(5, 10)*1000
k13_T = 8*sqrt(2)*6
k14_alapel = 12/sqrt(2)
k15_T = (2*6*8, 6*sqrt(3)*8)
k16_T = 6*sqrt(2)*6
n1_m = 6*sqrt(2)*tan(rad(30))
n2_x = solve(Eq(2*(2*x**2 + 3*x**2 + 6*x**2), 88), x)[0]
n3_a = solve(Eq(x**2*sqrt(2), 36*sqrt(2)), x)[0]
n4_a = solve(Eq(B(6, x)*4, 216*sqrt(3)), x)[0]
joker_T = 6*((6*sqrt(2)/2)**2*sqrt(3)/4)

TESZT = {
    'alap-3':  [('', k(kocka5[0])), ('', k(kocka5[1]))],
    'alap-4':  [('', int(teglatest_atlo))],
    'alap-5':  [('', 7), ('', 15), ('', 10)],
    'alap-6':  [('', 12), ('', 18), ('', 8)],
    'alap-7':  [('', 25), ('', 160), ('', 210), ('', 200)],
    'alap-8':  [('', k(h3_F)), ('', k(h3_V))],
    'alap-9':  [('', k(h6_F)), ('', k(h6_V))],
    'alap-10': [('', 94), ('', 60)],
    'alap-11': [('', 294), ('', 343)],
    'alap-12': [('', 20)],
    'alap-13': [('', 5), ('', 125)],
    'alap-14': [('', 10), ('', 600)],
    'alap-15': [('', 3200), ('', 4.5)],
    'alap-16': [('', int(akvarium_l)), ('', float(akvarium_uveg))],
    'alap-17': [('', k(metszet_negyzetes))],
    'alap-19': [('', int(metszet_teglatest))],
    'alap-20': [('', int(metszet_hatszog[0])), ('', k(metszet_hatszog[1]))],
    'kozep-1': [('', 12), ('', k(k1_lapatlo))],
    # az x = 2 segédértéket nem teszteljük (a „3x" jelölésben a 3 véletlenül egyezne)
    'kozep-2': [('', 6), ('', 8), ('', 24)],
    'kozep-3': [('', int(k3_m)), ('', 108)],
    'kozep-4': [('', 6), ('', k(k4_testatlo))],
    'kozep-5': [('', k(k5_F)), ('', k(k5_V))],
    'kozep-6': [('', int(k6_m))],
    'kozep-7': [('', int(k7_a)), ('', k(k7_V))],
    'kozep-8': [('', int(k8_a)), ('', k(k8_V))],
    'kozep-9': [('', 4), ('', 9), ('', 8), ('', 27)],
    'kozep-10': [('', int(k10_V))],
    'kozep-11': [('', k(k11_V))],
    'kozep-12': [('', int(k12_l))],
    'kozep-13': [('', k(k13_T))],
    'kozep-14': [('', 12), ('', k(k14_alapel))],
    'kozep-15': [('', int(k15_T[0])), ('', k(k15_T[1]))],
    'kozep-16': [('', k(k16_T))],
    'nehez-1': [('', k(n1_m))],
    'nehez-2': [('', int(n2_x)), ('', 4), ('', 6), ('', 48)],
    'nehez-3': [('', int(n3_a))],
    'nehez-4': [('', int(n4_a))],
    'joker':   [('', k(joker_T))],
}
