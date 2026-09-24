# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/02 — Zsoldos-lista II. (határérték és aszimptoták).

Független számolás: a határértékek NUMERIKUSAN (mpmath, 80 jegy; véges pontban a ± 10^-30 eltolással,
a végtelenben 10^20-nál), az aszimptoták a forrás (0_Feladatok, 15.) kulcsából és kézi levezetésből —
a builder sympy-szimbolikus számolásától függetlenül."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/02-fuggvenyek/feladatok-hatarertek-aszimptota.html'
PV, MV = 'pluszvegtelen', 'minuszvegtelen'
mp.mp.dps = 80
sq, ln = mp.sqrt, mp.log
H = mp.mpf(10) ** -30
NAGY = mp.mpf(10) ** 20


def _racio(b):
    x = F(mp.nstr(b, 50, min_fixed=-mp.inf, max_fixed=mp.inf))
    r = x.limit_denominator(1000)
    assert abs(x - r) < F(1, 10 ** 8), (x, r)
    return r


def _ertek(b, a_):
    if abs(b) > 10 ** 12:
        return PV if b > 0 else MV
    if abs(b) < mp.mpf(10) ** -30:
        return F(0)
    return _racio(b)


def lim(f, a, oldal=None):
    """oldal: None (kétoldali, a két oldal egyezzen), '+' vagy '-'."""
    if a in (PV, MV):
        s = 1 if a == PV else -1
        b1, b2 = f(s * NAGY), f(s * NAGY * 10)
        if abs(b2) > 10 ** 12 and abs(b2) > abs(b1):
            return PV if b2 > 0 else MV
        return _ertek(b2, a)
    a = mp.mpf(a)
    if oldal == '+':
        b = f(a + H)
        return PV if b > 10 ** 12 else MV if b < -10 ** 12 else _racio(b)
    if oldal == '-':
        b = f(a - H)
        return PV if b > 10 ** 12 else MV if b < -10 ** 12 else _racio(b)
    bal, jobb = f(a - H), f(a + H)
    assert abs(bal - jobb) < mp.mpf(10) ** -20, ("a két oldal különbözik", bal, jobb)
    return _racio(jobb)


def v(*ertekek):
    return [('', e) for e in ertekek]


def L(*t):
    return [lim(*x) for x in t]


TESZT = {
    # --- B1: grafikon, táblázat
    'alap-1': v(2, 1, 3, 2),
    'alap-2': v(1, 2, 2),
    'alap-3': v(*[F(str(t)) ** 2 / (F(str(t)) - 1) + 2 * F(str(t)) / (F(str(t)) - 1) - 3 / (F(str(t)) - 1)
                  for t in ('0.9', '0.99', '1.01', '1.1')],
                lim(lambda x: (x**2 + 2*x - 3) / (x - 1), 1)),
    'alap-4': v(0, 1, 1, 3, -1, 1),
    # --- B2: behelyettesítés, 0/0
    'alap-5': v(*L((lambda x: (x**2 + 4*x - 5) / (x**2 - 1), 2), (lambda x: (x**2 + 4*x - 5) / (x**2 - 1), -5),
                   (lambda x: (x**3 + 2*x) / (x**2 + 4), -1), (lambda x: sq(x) + ln(x) / ln(2), 4))),
    'alap-6': v(*L((lambda x: (x**2 - 49) / (x**2 - 7*x), 7), (lambda x: (x**2 - 4*x) / (3*x**2 - 48), 4),
                   (lambda x: (7*x**2 + 8*x + 1) / (x + 1), -1))),
    'alap-7': v(*L((lambda x: (x**2 + 3*x - 10) / (x**2 - x - 2), 2), (lambda x: (x**2 + 6*x - 7) / (x**2 - 5*x + 4), 1),
                   (lambda x: (x**2 + 3*x) / (x**2 - 9), -3))),
    'alap-8': v(*L((lambda x: (x**2 - 6*x + 5) / (x**2 - 8*x + 15), 5), (lambda x: (x + 2) / (3*x**2 + 5*x - 2), -2),
                   (lambda x: (x**2 - 16) / (x + 4), -4))),
    'alap-9': v(*L((lambda x: (x**2 + 5*x) / (x**2 - 25), -5), (lambda x: (2*x**2 - 3*x - 2) / (x - 2), 2),
                   (lambda x: (x**2 - x - 12) / (x**2 - 16), 4))),
    'alap-10': v(*L((lambda x: (3*x**2 + 5*x - 2) / (x + 2), -2), (lambda x: (x**2 - 7*x + 12) / (9 - x**2), 3),
                    (lambda x: (x**2 - 2*x) / (x**2 - 4), 2))),
    # --- B3: végtelenben
    'alap-11': v(*L((lambda x: (x**2 + 4*x - 5) / (x**2 - 1), PV), (lambda x: (5*x**2 - 7*x) / (2*x**2 + 3), PV),
                    (lambda x: (5*x**2 - 7*x) / (2*x**4 + 3), PV), (lambda x: (5*x**5 - 7*x) / (2*x**4 + 3), PV))),
    'alap-12': v(*L((lambda x: (3*x**2 - x + 1) / (6*x**2 + 3*x + 2), MV), (lambda x: (-4*x**3 + x**2 - 1) / (x**2 + x - 1), PV),
                    (lambda x: (2*x + 1) / (x**2 - x - 2), MV), (lambda x: (x**5 - 3*x**2 + 2) / (1 + 7*x - 3*x**2), PV))),
    'alap-13': v(*L((lambda x: (x + 3) / (x - 2), PV), (lambda x: (x - 2) / (x + 1), MV), (lambda x: (7 - 2*x) / (4*x + 1), PV),
                    (lambda x: (3*x**2 - 1) / (2 - x**2), MV))),
    'alap-14': v(PV, F(0), PV, PV, F(0)),        # 2^x, (1/3)^x → 0, (1/3)^x a −∞-ben, log₂x, 5/x³ — a grafikonokból
    # --- C1: aszimptoták (0_F 15. a, l, d, e + saját)
    'alap-15': v(3, 2, 1, 0),
    'alap-16': v(-1, 1),
    'alap-17': v(-2, 3, 2, F(-1, 2)),
    'alap-18': v(-3, 3, 0, -2, 2, 1),
    # === KÖZÉP ===
    'kozep-1': v(2, 4),
    'kozep-2': v(5 - 2, 4 - 1),                 # 2 + a = 3·2 − 1 ; b·1² = 4 − 1
    'kozep-3': v(*L((lambda x: (sq(x - 2) - 2) / (x - 6), 6), (lambda x: (sq(1 + x) - sq(1 - x)) / (4*x), 0),
                    (lambda x: (sq(x**2 + x + 1) - 1) / x, 0))),
    'kozep-4': v(*L((lambda x: (x - 5) / (sq(5*x) - 5), 5), (lambda x: (x - 3) / (sq(x + 1) - 2), 3),
                    (lambda x: x / (sq(1 + 3*x) - 1), 0), (lambda x: (5 - x) / (3 - sq(x + 4)), 5))),
    'kozep-5': v(*L((lambda x: (sq(x + 12) - 4) / (x - 4), 4), (lambda x: (x - 9) / (sq(x) - 3), 9),
                    (lambda x: (sq(x + 1) - 2) / (x**2 - 9), 3))),
    'kozep-6': v(*L((lambda x: (x + 3) / (x - 2), 2, '+'), (lambda x: (x + 3) / (x - 2), 2, '-'),
                    (lambda x: (x - 2) / (x + 1), -1, '+'), (lambda x: (x - 2) / (x + 1), -1, '-'))),
    'kozep-7': v(lim(lambda x: (x**2 - 4) / (x + 2), -2), lim(lambda x: (x + 1) / (x - 3), 3, '+'),
                 lim(lambda x: (2 - x) / (x - 1), 1, '-')),
    'kozep-8': v(*L((lambda x: (x**3 - 2) / (x + 5), MV), (lambda x: (2*x**4 + 1) / (x - 3), MV),
                    (lambda x: (x - 4*x**3) / (x**2 + 1), MV), (lambda x: (x**2 + 5) / (3 - x), MV))),
    'kozep-9': v(lim(lambda x: x**3 / (x**2 + 1), MV), lim(lambda x: x**3 / (x**2 + 1), PV),
                 lim(lambda x: 2*x**2 / (x**2 + 1), PV), lim(lambda x: (1 - x**4) / (x**2 + 3), PV)),
    'kozep-10': v(2, lim(lambda x: (x**2 - 5*x + 6) / (x - 2), 2), -1, lim(lambda x: (x + 1) / (x**2 - 1), -1), 1, 4),
    'kozep-11': v(-1, 1, -2, 2, -1, 1, 2, 2, F(-8, -1)),
    'kozep-12': v(1, F(1, 2), 2),
    # === NEHÉZ (0_F 15. b, c, g · f, h, j, k · i + saját) ===
    'nehez-1': v(-2, 2, -3, -3, -3, -2),
    'nehez-2': v(3, 2, -1, 6, 5),
    'nehez-3': v(0, F(2, 3), 1, -1, -1, F(-3, 2)),
    'nehez-4': v(2, 3, -1),
    'joker': v(1, -1),
}
