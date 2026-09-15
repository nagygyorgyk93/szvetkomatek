# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/03 — egyenletrendszerek (A + C blokk).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül.
Szöveges (határozatlan / ellentmondásos) válasznál a döntés szavát ellenőrizzük."""
from fractions import Fraction as F
from sympy import symbols, linsolve, expand

FAJL = '3e/03-linearis-rendszerek/feladatok-rendszerek.html'
x, y, z = symbols('x y z')


def m(*eqs, v=(x, y, z)):
    s = list(linsolve([expand(e) for e in eqs], v))
    assert len(s) == 1 and all(not getattr(c, 'free_symbols', None) for c in s[0]), s
    return [('', F(int(c.p), int(c.q))) for c in s[0]]


TESZT = {
    'alap-2': m(2*x + y - 16, x - 4*y + 1, v=(x, y)),
    'alap-3': m(3*x - 4*y + 42, 2*x + y - 5, v=(x, y)),
    'alap-4': m(5*x + 3*y - 19, 5*x - 2*y - 4, v=(x, y)),
    'alap-5': m(x - y + 2, x + y - 4, v=(x, y)),
    'alap-6': [('', 'vegtelen sok'), ('', 'nincs megoldas'), ('', 'pontosan egy')],
    'alap-8': m(x + 2*y - z - 3, y + z - 5, 2*z - 6),
    'alap-9': m(x + y + z - 9, x + 2*y + 3*z - 16, x + 3*y + 4*z - 21),
    'alap-10': m(x + y - 5, y + z - 7, x + z - 6),
    'alap-11': m(x + 3*y + 2*z - 11, 2*x + 5*y + 4*z - 20, 3*x + 8*y + 9*z - 37),
    'alap-12': m(2*x + y + z + 9, x - 2*y + z + 11, x + y - 2*z - 4),
    'alap-13': m(x + 2*y + 3*z - 32, 2*x + y + 3*z - 31, 3*x + 2*y + z - 28),
    'alap-14': [('', 'y-3z=-10')] + m(x + 2*y + z - 7, 2*x + 3*y - z - 4, x - y + 2*z - 7),
    'alap-15': [('', 'hatarozatlan'), ('', 'ellentmondasos'), ('', 'hatarozott')],
    'alap-16': [('', 'nincs megoldas'), ('', 4)],
    'alap-17': [('', 'hatarozatlan'), ('', 2), ('', -3), ('', 5), ('', -3)],
    'alap-19': m(2*x + 3*y - 480, x + 2*y - 290, v=(x, y)) + [('', 190)],
    'alap-20': m(x + y - 57, x - y - 13, v=(x, y)),
    'alap-21': m(x + y - 30, 350*x + 250*y - 8400, v=(x, y)),
    'alap-22': m(x - 3*y, x + 12 - 2*(y + 12), v=(x, y)),
    'alap-24': [('', 47)],
    'kozep-1': m(x/2 + y/3 - 4, x/4 - y/6, v=(x, y)),
    'kozep-2': m((x + 4)*(y - 3) - x*y + 22, (x - 2)*(y + 2) - x*y, v=(x, y)),
    'kozep-3': m(x - y + 1, 2*x + y - 3, v=(x, y)),
    'kozep-4': m(x + 2*y - 5*z - 6, 2*x - y - 2*z + 5, 3*x - 3*y + 4*z + 8),
    'kozep-5': m(3*x - 5*y + 2*z + 5, 6*x + 2*y - 3*z - 23, 4*x - 3*y - z - 8),
    'kozep-6': m(x + 2*y - 7*z - 18, 4*x - 2*y - 3*z - 17, 2*x - 5*y + 8*z + 13),
    'kozep-7': m(x - 6*y + 8*z, 2*x + 4*y - 3*z - 26, 3*x - 4*y + 5*z - 18),
    'kozep-8': m(2*x - y + 3*z - 20, x + 2*y + 2*z - 7, 3*x + 2*y - z - 1),
    'kozep-9': [('', 6), ('', 2)] + m(x + 2*y + 3*z - 1, x + 2*y - 3*z + 1, x - 2*y - 6*z + 4),
    'kozep-10': [('', 'nincs megoldas'), ('', 1), ('', 6), ('', 5)],
    'kozep-11': [('', 'hatarozatlan'), ('', F(-4, 3)), ('', F(-5, 3))],
    'kozep-12': [('', 'a (0;0;0)'), ('', 'vegtelen sok')],
    'kozep-13': [('', 'hatarozatlan'), ('', F(1, 2)), ('', F(-1, 2))],
    'kozep-14': m(F(1, 2)*(x + y) - 60, 3*(x - y) - 60, v=(x, y)),
    'kozep-15': m(x + y - 30, F(1, 5)*x + F(1, 2)*y - 9, v=(x, y)),
    'kozep-16': m(x + 5*y - 650, x + 12*y - 1210, v=(x, y)) + [('', 1850)],
    'kozep-17': m(2*x + 3*y + z - 2300, x + 2*y + 2*z - 1900, 3*x + y + z - 2200),
    'kozep-18': [('', 165)],
    'kozep-19': m(x + y - 12, 5*x + 2*y - 39, v=(x, y)) + [('', 39), ('', 5), ('', 7)],
    'nehez-1': m(x + y + z - 2, x - y + z - 6, 4*x + 2*y + z - 3),
    'nehez-2': [('', F(1, 2)), ('', F(1, 3)), ('', 2), ('', 3)],
    'nehez-3': m(x + y + z - 500, F(11, 10)*x + F(6, 5)*y + z - 540, z - x - y) + [('', 8)],
    'nehez-4': [('', F(-2, 3)), ('', F(-1, 3)), ('', -1), ('', F(1, 3)), ('', F(2, 3)), ('', -1)],
    'nehez-5': m(x + y + z - 10, 1200*x + 1600*y + 2000*z - 15600, x - 2*z),
    'nehez-6': [('', 200), ('', 400), ('', 300)],
    'joker': m(3*x + 2*y + z - 39, 2*x + 3*y + z - 34, x + 2*y + 3*z - 26),
}
