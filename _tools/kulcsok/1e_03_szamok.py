# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/03 egész és valós számok.

Minden várt érték független Python-számolásból jön.
"""
from fractions import Fraction
from math import gcd, isqrt

FAJL = '1e/03-egesz-es-valos-szamok/feladatok-egesz-es-valos-szamok.html'


def lkt(*sz):
    k = 1
    for x in sz:
        k = k * x // gcd(k, x)
    return k


def prim(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def tenyezok(n):
    ki, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            ki[d] = ki.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        ki[n] = ki.get(n, 0) + 1
    return ki


def alapba(n, b):
    """n → b alapú számjegyek füzére (A–F is)."""
    jegy = '0123456789ABCDEF'
    ki = ''
    while n:
        ki = jegy[n % b] + ki
        n //= b
    return ki or '0'


def alapbol(s, b):
    return int(s, b)


SZAMOK2 = [1236, 2430, 3820, 5049, 7128, 9315]
oszthato = lambda d: [x for x in SZAMOK2 if x % d == 0]

# ── alap-1: euklideszi maradékos osztás ───────────────────────────────
def maradekos(a, b):
    q = a // b
    return q, a - q * b


# ── kozep-3: mivel kell szorozni négyzetszámhoz ───────────────────────
paratlan_kitevo = 1
for p, k in tenyezok(52800).items():
    if k % 2:
        paratlan_kitevo *= p

# ── nehez-3: (3n+10)/(n+1) egész ──────────────────────────────────────
N3 = sorted(n for n in range(-100, 101) if n != -1 and (3 * n + 10) % (n + 1) == 0)

# ── nehez-4 / kozep-6 ─────────────────────────────────────────────────
N4 = next(n for n in range(1, 10**4)
          if n % 3 == 2 and n % 4 == 3 and n % 5 == 4 and n % 6 == 5)
K6 = next(n for n in range(2, 10**4) if n % 5 == 1 and n % 6 == 1 and n % 7 == 1)

# ── nehez-5: p, p+10, p+20 mind prím ──────────────────────────────────
N5 = [p for p in range(2, 500) if prim(p) and prim(p + 10) and prim(p + 20)]

# ── nehez-8: aba₃ = 20 ────────────────────────────────────────────────
N8 = [(a, b) for a in range(1, 3) for b in range(0, 3) if 10 * a + 3 * b == 20]

# ── kozep-9: kerekítési hiba ──────────────────────────────────────────
x9 = Fraction('4.88465009')
delta9 = x9 - Fraction('4.88')

TESZT = {
    # mind a négy osztás hányadosa ÉS maradéka — sorrendben
    'alap-1': [('', v) for par in (maradekos(38, 5), maradekos(100, 7),
                                   maradekos(-17, 5), maradekos(45, 6))
               for v in par],
    'alap-2': [('', ', '.join(str(x) for x in oszthato(4)))],
    'alap-4': [('', gcd(75, 200)), ('', lkt(75, 200))],
    'alap-5': [('', alapbol('321', 4)), ('', alapbol('1011', 2)),
               ('', alapbol('412', 5)), ('', alapbol('1111', 2))],
    'alap-6': [('', alapba(1234, 8)), ('', alapba(77, 3)),
               ('', alapba(44, 2)), ('', alapba(543, 8))],
    'kozep-1': [('', lkt(160, 200)), ('', gcd(160, 200))],
    'kozep-3': [('', paratlan_kitevo)],
    'kozep-4': [('', alapbol('A2A', 16)), ('', alapbol('351', 6)),
                ('', alapba(399, 16)), ('', alapba(100, 2))],
    'kozep-5': [('', len(alapba(100, 2))), ('', alapbol('210', 3))],
    'kozep-6': [('', K6)],
    'kozep-9': [('', float(delta9))],
    'nehez-3': [('', min(N3)), ('', max(N3))],
    'nehez-4': [('', N4)],
    'nehez-5': [('', N5[0])],
    'nehez-6': [('', lkt(160, 200, 240))],
    'nehez-8': [('', N8[0][0])],
}
