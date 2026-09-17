# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/05 — a parabola (5. gyűjtemény).

A várt értékeket ITT számoljuk ki sympy-val, a HTML-től és a buildertől függetlenül
(az adott irányú érintőket a p = 2kn érintési feltétellel, nem diszkriminánssal)."""
from fractions import Fraction as F
from sympy import sqrt, Rational, symbols, solve, nsimplify

FAJL = '3e/05-analitikus-geometria/feladatok-parabola.html'
x, y = symbols('x y', real=True)


def fr(v):
    v = Rational(nsimplify(v))
    return F(int(v.p), int(v.q))


def kerek(v, n=2):
    return ('', F(str(round(float(v), n))))


def pt(p):
    return [('', fr(p[0])), ('', fr(p[1]))]


def adat(ketp):
    """y^2 = ketp*x -> p, F elso koordinataja, vezeregyenes"""
    q = Rational(ketp) / 2
    return [('', fr(abs(q))), ('', fr(q / 2)), ('', 0), ('', fr(-q / 2))]


def ponton_at(p):
    """y^2 = a x, amely atmegy p-n -> a"""
    return Rational(p[1])**2 / p[0]


def erinto_sajat(ketp, p0):
    """y0*y = p(x + x0) -> (a, b, c) az ax + by + c = 0 alakhoz"""
    q = Rational(ketp) / 2
    return (q, -p0[1], q * p0[0])


def Lsz(a, b, c0):
    from math import gcd
    a, b, c0 = Rational(a), Rational(b), Rational(c0)
    lk = 1
    for d in (a.q, b.q, c0.q):
        lk = lk * d // gcd(lk, d)
    a, b, c0 = int(a * lk), int(b * lk), int(c0 * lk)
    g = gcd(gcd(abs(a), abs(b)), abs(c0)) or 1
    a, b, c0 = a // g, b // g, c0 // g
    if a < 0:
        a, b, c0 = -a, -b, -c0
    ki = [('', a)] if a not in (0, 1) else []
    ki += [('', b)] if b not in (0, 1, -1) else []
    return ki + ([('', c0)] if c0 else [])


def metsz(g, l):
    s = solve([g, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s if r[x].is_real], key=lambda u: (float(u[0]), float(u[1])))


def n_felt(ketp, k):
    """p = 2kn -> n"""
    return Rational(ketp) / 2 / (2 * k)


M49 = metsz(y**2 - 4*x, 2*x - y - 4)
M58 = metsz(y**2 - 18*x, y - 2*x - 2)
n1, n2, n3 = n_felt(3, Rational(1, 4)), n_felt(12, 1), n_felt(8, 2)
p54 = 2 * Rational(-3, 2) * Rational(-3, 2)          # p = 2kn, y = -3/2 x - 3/2

TESZT = {
    'alap-1': adat(4) + adat(Rational(5, 2)) + adat(-8) + adat(24),
    'alap-2': [('', 2), ('', fr(ponton_at((1, -3)))), ('', 2), ('', fr(ponton_at((2, 8)))),
               ('', 2), ('', fr(ponton_at((-4, 1)))), ('', 2), ('', fr(ponton_at((-6, 4))))],
    'alap-3': [('', 0), ('', fr(Rational(8, 4))), ('', fr(-Rational(8, 4))), ('', 0), ('', fr(Rational(-12, 4))),
               ('', fr(Rational(12, 4)))],
    'alap-4': [('', 2), ('', 4), ('', fr(Rational(4, 2))), ('', 0), ('', fr(Rational(4, 4))), ('', fr(-Rational(4, 4)))],
    'alap-5': [('', 'igen'), ('', 'igen'), ('', 4**2), ('', 6 * 2), ('', 'igen')],
    'alap-6': pt(metsz(y**2 - 4*x, x - 2*y + 4)[0]) + pt(M49[0]) + pt(M49[1]) + [('', 'nincs')],
    'alap-7': Lsz(*erinto_sajat(6, (6, 6))),
    'alap-8': pt((8, -sqrt(2 * 8))) + Lsz(*erinto_sajat(2, (8, -4))),
    'alap-9': pt((Rational(9, 9), 3)) + pt((Rational(36, 9), -6)),
    'alap-10': pt((Rational(5, 2), -sqrt(25))) + Lsz(*erinto_sajat(10, (Rational(5, 2), -5))),
    'kozep-1': [('', 2), ('', 4 * 3), ('', 2), ('', -4 * 5)],
    'kozep-2': [('', 2), ('', fr(80**2 / Rational(40))), ('', fr(80**2 / Rational(40) / 4)), ('', 0),
                ('', fr(80**2 / Rational(40) / 4))],
    'kozep-3': [('', fr(Rational(12, 4))), ('', 0)],
    'kozep-4': [('', 6), ('', 4), ('', 6), ('', fr(16 / Rational(4))), ('', 0), ('', fr(6 + 16 / Rational(4)))],
    'kozep-5': pt(M49[0]) + pt(M49[1]) + [kerek(sqrt((M49[1][0] - M49[0][0])**2 + (M49[1][1] - M49[0][1])**2))],
    'kozep-6': pt(M58[0]) + pt(M58[1]) + Lsz(*erinto_sajat(18, M58[0])) + Lsz(*erinto_sajat(18, M58[1])),
    'kozep-7': pt((-1, -4)) + [('', fr(Rational(-8) / -4)), ('', fr(Rational(-8) * (-1) / -4))]   # -4y = -8(x - 1)
               + pt((solve(2*x - 2, x)[0], 0)) + pt((0, -2)),
    'kozep-8': [('', 2), ('', fr(-10**2 / Rational(5)))] + [kerek(Rational(-16, 20)), kerek(5 - Rational(16, 20))],
    'nehez-1': [('', F(1, 4)), ('', 2), ('', 8), ('', -48), ('', 16), ('', 2), ('', fr(n1))]
               + Lsz(1, -4, 4 * n1) + pt(metsz(y**2 - 3*x, y - x / 4 - n1)[0]),
    'nehez-2': [('', 2), ('', 2), ('', -12), ('', 2), ('', fr(n2)), ('', fr(n2))] + pt(metsz(y**2 - 12*x, y - x - n2)[0]),
    'nehez-3': [('', 2), ('', 4), ('', 2), ('', 4), ('', -8), ('', 2), ('', fr(n3)), ('', 2), ('', fr(n3))]
               + pt(metsz(y**2 - 8*x, y - 2*x - n3)[0]),
    'nehez-4': [('', F(9, 4)), ('', 2), ('', F(9, 2)), ('', -2), ('', F(9, 4)), ('', 0), ('', 0), ('', fr(p54)),
                ('', fr(p54)), ('', 2), ('', fr(2 * p54))] + pt(metsz(y**2 - 2 * p54 * x, 3*x + 2*y + 3)[0]),
    'joker': pt((Rational(4, 4), 0)) + pt((0, Rational(4, 4))) + pt((0, 0)) + pt((4, 4)) + [kerek(sqrt(32))],
}
