# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/02 — Zsoldos-lista I. (tulajdonságok).

Független forrás: a helyettesítési értékeket itt, törtekkel számoljuk; az értelmezési tartomány, a zérushely,
az előjel és a paritás várt értékei a 0_Feladatok kulcsából jönnek (a 10. i) javításával), a paritást
pedig numerikusan (f(−x) ↔ ±f(x) véletlen pontokban) is ellenőrizzük — a builder sympy-számolásától függetlenül."""
import math
import random
from fractions import Fraction as F

FAJL = '4e/02-fuggvenyek/feladatok-tulajdonsagok.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


def paritas(f, pontok=None):
    random.seed(7)
    pontok = pontok or [random.uniform(0.3, 2.7) for _ in range(12)]
    paros = all(abs(f(-t) - f(t)) < 1e-9 for t in pontok)
    paratlan = all(abs(f(-t) + f(t)) < 1e-9 for t in pontok)
    return 'páros' if paros else 'páratlan' if paratlan else 'egyik sem'


def P(*fk, pontok=None):
    """A paritás-szavak sorrendje egyben (a kulcs szövegében így követik egymást)."""
    return [('', ' '.join(paritas(f, pontok) for f in fk))]


fA = lambda a: (3 * F(a) - 8) / 2
gA = lambda a: (5 * F(a) - 1) / (F(a) ** 2 + 1)
hA = lambda a: F(a) - 1 if F(a) >= 1 else -F(a) ** 2 + 1
AK = [2, 1, 0, -2, F(-4, 3)]
S3 = [1.2, 1.7, 2.3, 2.9]           # |x| ≥ 1 kell a √(x²−1)-hez

TESZT = {
    'alap-1': v(*[fA(a) for a in AK], *[gA(a) for a in AK], *[hA(a) for a in AK]),
    'alap-2': v(fA(F(-2, 3)) * gA(-1), F(14, 3) * fA(F(2, 7)) - F(5, 6) * gA(F(1, 2))),
    'alap-3': v(-1, 1),                                   # a cos x értékkészlete
    'alap-4': v(F(1, 3), 4),
    'alap-5': v(2, 2, 0, F(7, 3), -3, F(1, 3), -1),       # 9. a) R∖{±√2}, b) 0; 7/3, c) −3; 1/3, d) −1
    'alap-6': v(3, -4, 5, F(-7, 2)),                      # 6−2x≥0, 3x+12≥0, 5−x>0, 2x+7>0
    'alap-7': v(-2, 0, 2, 1, -1, 0, 5, 3),
    'alap-8': v(-2, -1, -1, -2, -2, -1, 1, 4, 1, 1, 4, 4),                 # 10. a), b)
    'alap-9': v(0, 2, F(-2, 3), 0, 2, F(-2, 3), 0, 2, 2, 5, 1, 2, 5, 1, 2, 5),   # 10. d), e)
    'alap-10': P(lambda x: 4*x + 4/x, lambda x: x*(x - 1)**2, lambda x: x**3 - 2*x/3, lambda x: 7*x**5 - 3/x),
    'alap-11': P(lambda x: 4*abs(x) - x**4, lambda x: 3*x**3 - x*abs(x), lambda x: 7**(-x) + 7**x, lambda x: 5**x - 5**(-x)),
    'alap-12': v(-4, 4, -2, 4, -3, -1, 3),
    'kozep-1': v(F(3, 2), 9),
    'kozep-2': v(0, 0, -4, 0),
    'kozep-3': v(-1, F(1, 5), -2, 5),                     # 9. f), g)
    'kozep-4': v(-1, F(4, 3), -7, 1),                     # 9. j), k)
    'kozep-5': v(F(-7, 2), 2, 2, F(-1, 2), 2, F(-2, 3), 4),   # 9. e), h), l)
    # 10. c) ±√5 (a kulcsban „5”-ként olvasható), f), g), h), i) javítva, j) ±√2
    'kozep-6': v(5, 1, 5, 5, 1, 5, 5, 1, 5, -3, -1, -3, -3, -1, -2, 2, -2, -1, 1, 2, -2, -1, 1, 2,
                 1, 4, 1, 4, 5, 1, 4, 5, 0, F(3, 2), 0, F(3, 2), 0, F(3, 2), 2, 2, 2, 2, 2, 2),
    'kozep-7': P(lambda x: math.sqrt(x*x + 1) + math.sqrt(x*x - 1), lambda x: math.sin(x) + math.cos(x),
                 lambda x: x*math.sin(x) + math.cos(x), lambda x: x**3*math.tan(x),
                 lambda x: (x*x + 1)/(x*x + x + 1), lambda x: x*math.sin(x)**2 - x**3, lambda x: 2**(1 - x*x),
                 lambda x: math.sin(x)/x - 1, pontok=S3),
    'kozep-8': v(4, 0),
    'nehez-1': v(-3, -1, 3, -3, 0, 2, 3, -4, -1, -1, 1, 1, 4),   # 9. i), m), n)
    'nehez-2': v(-1, 1, -2, 3, -2, -1, 1, 3, -2, -1, 1, 3, 0, 6),
    'joker': v(0),
}
