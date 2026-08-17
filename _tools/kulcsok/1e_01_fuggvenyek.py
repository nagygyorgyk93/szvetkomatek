# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/01 függvények (kompozíció, inverz, lineáris modellek).

A gyűjtemény válaszai többségükben szimbolikusak, ezért két lépésben ellenőrzünk:

1. a `KIF(...)` a kulcsban szereplő alakot **sympy-val hitelesíti** — kiszámolja
   a kompozíciót vagy az inverzet, és megköveteli, hogy a különbség azonosan 0
   legyen (ez a matematikai ellenőrzés, teljesen független a HTML-től);
2. a harness ezután megnézi, hogy a hitelesített alak **tényleg ott áll-e** a
   Végeredmény-lenyílóban (ez a szövegellenőrzés).

Így egy elgépelt kulcs a 2. lépésen, egy hibásan kiszámolt kulcs pedig már az
1. lépésen elbukik — a modul betöltése száll el.
"""
from fractions import Fraction as F

from sympy import Eq, Rational, expand, simplify, solve, symbols, sympify

FAJL = '1e/01-logika-halmazok-fuggvenyek/feladatok-fuggvenyek.html'

x, y, a, b, n = symbols('x y a b n')


def komp(f, g):
    """(f ∘ g)(x) — előbb g, aztán f."""
    return expand(f.subs(x, g))


def inverz(f):
    """Az f(x) = y egyenletet x-re oldjuk, majd visszanevezzük."""
    meg = solve(Eq(f, y), x)
    assert len(meg) == 1, f'nem egyértelmű inverz: {f}'
    return expand(meg[0].subs(y, x))


def KIF(alak, elvart):
    """A kulcsban szereplő alak — sympy hitelesíti, hogy tényleg az elvárt függvény.

    Az `alak` Python-szintaxisú (`2*x+7`, `x**2-1`); a harness normalizálásakor a
    `*` és a `**` úgyis eltűnik, így a `2x+7`, illetve az `x^2-1` kulcsalakkal esik
    egybe. A `\\tfrac{x+5}{2}` a normalizálás után `x52` lesz — ugyanaz, mint az
    `(x+5)/2`.
    """
    kap = sympify(alak)
    if simplify(kap - elvart) != 0:
        raise AssertionError(f'a várt alak nem egyezik a számolással: '
                             f'{alak} ≠ {elvart}')
    return alak


# ── a gyűjteményben szereplő függvények ────────────────────────────────
f2 = 3 * x - 5                      # alap-2 f
g2 = x / 2 - 3                      # alap-2 g
h2 = x ** 2 - 2 * x                 # alap-2 h

f4a, g4a = 2 * x - 1, x + 4         # alap-4 a
f4b, g4b = 3 * x, x - 2             # alap-4 b
f4c, g4c, h4c = x + 1, 2 * x, x - 3  # alap-4 c

f9 = -2 * x + 6                     # alap-6/alap-9
f11 = 90 * x + 300                  # alap-11 taxi
f8 = 3 * x + 50                     # alap-8 reaktor
FF = 9 * x / 5 + 32                 # alap-7 / kozep-4 Celsius→Fahrenheit

fk1, hk1 = 2 * x - 3, x ** 2 + 1    # kozep-1
gk1 = 2 * x + 1
fk6, gk6 = 2 * x - 5, 4 - 3 * x     # kozep-6
gk8 = x + 2                         # kozep-8
fn4, gn4 = 2 - 3 * x, 3 * x - 1     # nehez-4
fn5 = -2 * x + 3                    # nehez-5


# ── alap-6 a) és alap-10: „ismeretlen belső függvény" ─────────────────
def belso(kulso, ered):
    """A (kulso ∘ f)(x) = ered egyenletből f(x)."""
    t = symbols('t')
    meg = solve(Eq(kulso.subs(x, t), ered), t)
    assert len(meg) == 1
    return expand(meg[0])


# f(x−3) = 2x+1  →  a helyettesítés u = x−3, azaz x = u+3
f_a10a = expand((2 * x + 1).subs(x, x + 3))          # alap-10 a
f_k2a = expand((3 * x - 1).subs(x, x - 2))           # kozep-2 a: f(x+2)=3x−1
f_k2b = expand((4 * x + 3).subs(x, (x + 1) / 2))     # kozep-2 b: f(2x−1)=4x+3
f_k2c = expand((x - 4).subs(x, 2 * x - 2))           # kozep-2 c: f((x+2)/2)=x−4
f_k2d = expand((4 * x ** 2 + 4 * x).subs(x, (x - 1) / 2))   # kozep-2 d
f_n1 = expand((3 * x - 2).subs(x, 2 * x + 1))        # nehez-1: f((x−1)/2)=3x−2
f_n3 = expand(((3 * x - 5) / 2).subs(x, 2 * x + 2))  # nehez-3: f((x−2)/2)=(3x−5)/2
f_n5 = expand((4 * x - 7).subs(x, (5 - x) / 2))      # nehez-5: f(5−2x)=4x−7

# kozep-7: f(1)=5, f(3)=11
k7 = solve([Eq(a * 1 + b, 5), Eq(a * 3 + b, 11)], [a, b])
f_k7 = k7[a] * x + k7[b]

# joker: f(f(x)) = 9x+8, azaz a²=9 és b(a+1)=8
joker = []
for aa in (3, -3):
    bb = solve(Eq(bb_ := b * (aa + 1), 8), b)[0]
    joker.append((aa, bb))


TESZT = {
    # ── ALAP ───────────────────────────────────────────────────────────
    'alap-2': [('a', f2.subs(x, 0)), ('b', f2.subs(x, 2)), ('c', f2.subs(x, -1)),
               ('d', f2.subs(x, Rational(1, 3))), ('e', KIF('3*a-5', f2.subs(x, a))),
               ('f', g2.subs(x, 4)), ('g', g2.subs(x, -6)),
               ('h', KIF('a-3', g2.subs(x, 2 * a))),
               ('i', KIF('b/2', expand(g2.subs(x, b + 6)))),
               ('j', h2.subs(x, 3)), ('k', h2.subs(x, -1)), ('l', h2.subs(x, 0))],

    'alap-4': [('', KIF('2*x+7', komp(f4a, g4a))), ('', KIF('2*x+3', komp(g4a, f4a))),
               ('', KIF('3*x-6', komp(f4b, g4b))), ('', KIF('3*x-2', komp(g4b, f4b))),
               ('', KIF('9*x', komp(f4b, f4b))), ('', KIF('x-4', komp(g4b, g4b))),
               ('', KIF('2*x+1', komp(f4c, g4c))), ('', KIF('2*x-6', komp(g4c, h4c))),
               ('', KIF('x-2', komp(h4c, f4c)))],

    'alap-5': [('a', KIF('x/2+3', inverz(2 * x - 6))),
               ('b', KIF('-3*x+6', inverz(-x / 3 + 2))),
               ('c', KIF('(x+2)/5', inverz(5 * x - 2))),
               ('d', KIF('x-7', inverz(x + 7))),
               ('e', KIF('2*x+3', inverz((x - 3) / 2)))],

    # f(x) az f(x)=−2x+6 tengelymetszetei, illetve a g∘f = 4x−3 belső tagja
    # a tengelymetszeteket a teljes koordinátapárral kérjük, és a keresett
    # függvényértékeket (13 és 0) is felsoroljuk — így a számsor sorrendje is köt
    'alap-6': [('', KIF('2*x-2', belso(2 * x + 1, 4 * x - 3))),
               ('', solve(Eq(f9, 0), x)[0]), ('', 0),          # x-tengely: (3, 0)
               ('', 0), ('', f9.subs(x, 0)),                   # y-tengely: (0, 6)
               ('', 13), ('', solve(Eq(5 * x - 2, 13), x)[0]),  # f(x)=13 → x=3
               ('', 0), ('', solve(Eq(5 * x - 2, 0), x)[0])],   # f(x)=0  → x=2/5

    # a kulcs a Fahrenheit-értéket F-fel jelöli, ezért az inverzet is F-ben kérjük
    'alap-7': [('', FF.subs(x, 20)),                  # 68 °F
               ('', KIF('5*(F-32)/9', inverz(FF).subs(x, symbols('F')))),
               ('', solve(Eq(FF, 95), x)[0])],        # 35 °C

    'alap-8': [('', f8.subs(x, 10)),                  # 80 MW
               ('', solve(Eq(f8, 200), x)[0]),        # 50 perc
               ('', KIF('(x-50)/3', inverz(f8)))],

    'alap-9': [('a', f9.coeff(x)), ('b', f9.subs(x, 0)),
               ('c', 'csökkenő'), ('d', f9.subs(x, 4))],

    'alap-10': [('', KIF('2*x+7', f_a10a)),
                ('', KIF('2*x+1', belso(3 * x - 1, 6 * x + 2)))],

    'alap-11': [('', f11.subs(x, 8)),                 # 1020 din
                ('', solve(Eq(f11, 1200), x)[0]),     # 10 km
                ('', KIF('(x-300)/90', inverz(f11)))],

    # ── KÖZÉP ──────────────────────────────────────────────────────────
    'kozep-1': [('', KIF('2*x**2-1', komp(fk1, hk1))),
                ('', KIF('4*x**2-12*x+10', komp(hk1, fk1))),
                ('', KIF('2*x+2', expand(komp(gk1, gk1) - gk1))),
                ('', KIF('2*x+1', belso(4 * x - 3, 8 * x + 1)))],

    'kozep-2': [('a', KIF('3*x-7', f_k2a)), ('b', KIF('2*x+5', f_k2b)),
                ('c', KIF('2*x-6', f_k2c)), ('d', KIF('x**2-1', f_k2d)),
                ('d', f_k2d.subs(x, 3))],           # f(3) = 8

    'kozep-6': [('a', KIF('-6*x+3', komp(fk6, gk6))),
                ('b', KIF('-6*x+19', komp(gk6, fk6))),
                ('c', KIF('(x+5)/2', inverz(fk6))),
                ('d', KIF('(4-x)/3', inverz(gk6)))],

    'kozep-7': [('', k7[a]), ('', k7[b]),
                ('', KIF('(x-2)/3', inverz(f_k7)))],

    'kozep-8': [('a', KIF('x+4', komp(gk8, gk8))),
                ('b', KIF('x+6', komp(gk8, komp(gk8, gk8)))),
                ('c', 'x+2n')],

    # ── NEHÉZ ──────────────────────────────────────────────────────────
    'nehez-1': [('', KIF('6*x+1', f_n1))],
    'nehez-3': [('', KIF('3*x+1/2', f_n3))],
    'nehez-4': [('', KIF('(5-x)/9', komp(inverz(fn4), inverz(gn4))))],
    'nehez-5': [('', KIF('-2*x+3', f_n5)),
                ('', KIF('4*x-3', komp(fn5, fn5)))],
    'nehez-6': [('', KIF('(x-b)/a', (x - b) / a))],

    'joker': [('', joker[0][0]), ('', joker[0][1]),      # a = 3,  b = 2
              ('', joker[1][0]), ('', joker[1][1])],     # a = −3, b = −4
}

# a harness Fraction-t és int-et vár, a sympy Integer/Rational is átmegy rajta
TESZT = {k: [(betu, F(int(v.p), int(v.q)) if hasattr(v, 'p') and hasattr(v, 'q') else v)
             for betu, v in lista]
         for k, lista in TESZT.items()}
