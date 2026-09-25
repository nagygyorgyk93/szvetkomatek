# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/03 — I.V.H. Kihallgató Terem (házi).

Független számolás: minden derivált-kulcsot itt, kézzel írt alakban ellenőrzünk numerikus deriválással (mpmath)
több pontban; az érintőket, a szélsőértékeket és az inflexiós pontokat a másodfokú megoldóképletből és
behelyettesítéssel — a builder sympy-számolásától függetlenül. A sympy-latex a mínuszjel után szóközt tesz,
ezért a kifejezés-kulcsoknál az együtthatók abszolút értékét (sorrendben) nézzük."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/03-derivalt/feladatok-hazi.html'
mp.mp.dps = 40
PONTOK = (mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('2.9'), mp.mpf('4.1'))


def v(*ertekek):
    return [('', e) for e in ertekek]


def derivalt(f, g):
    """g valóban f deriváltja? (numerikus deriválás több pontban)"""
    for p in PONTOK:
        assert abs(mp.diff(f, p) - g(p)) < mp.mpf(10) ** -20, (p, mp.diff(f, p), g(p))


def M(t):
    return mp.mpf(t.numerator) / t.denominator if isinstance(t, F) else mp.mpf(t)


def racio(b):
    if isinstance(b, (int, F)):
        return F(b)
    r = F(mp.nstr(b, 30, min_fixed=-mp.inf, max_fixed=mp.inf)).limit_denominator(1000)
    assert abs(b - mp.mpf(r.numerator) / r.denominator) < mp.mpf(10) ** -15
    return r


def masodfoku(a, b, c):
    d = mp.sqrt(b * b - 4 * a * c)
    return sorted(racio((-b + s * d) / (2 * a)) for s in (-1, 1))


def pont(f, t):
    y = racio(f(M(t)))
    return f"({'−' if t < 0 else ''}{abs(t)}; {'−' if y < 0 else ''}{abs(y)})"


# alap 1–3 és közép 1: a kulcs kézzel írt alakjai
derivalt(lambda t: 3*t**4 - 5*t**3 + 2*t - 8, lambda t: 12*t**3 - 15*t**2 + 2)
derivalt(lambda t: 4*mp.sqrt(t) - 2/t, lambda t: 2/mp.sqrt(t) + 2/t**2)
derivalt(lambda t: (2*t + 1)*mp.e**t, lambda t: (2*t + 3)*mp.e**t)
derivalt(lambda t: t**2*mp.cos(t), lambda t: 2*t*mp.cos(t) - t**2*mp.sin(t))
derivalt(lambda t: t**3*mp.log(t), lambda t: t**2*(3*mp.log(t) + 1))
derivalt(lambda t: (3*t - 2)**5, lambda t: 15*(3*t - 2)**4)
derivalt(lambda t: mp.sqrt(t**2 + 9), lambda t: t/mp.sqrt(t**2 + 9))
derivalt(lambda t: mp.sin(4*t), lambda t: 4*mp.cos(4*t))
derivalt(lambda t: mp.e**(t**2), lambda t: 2*t*mp.e**(t**2))
derivalt(lambda t: (t + 4)/(t - 3), lambda t: -7/(t - 3)**2)
derivalt(lambda t: mp.log(t**2 + 4), lambda t: 2*t/(t**2 + 4))
derivalt(lambda t: mp.e**(-2*t)*mp.cos(t), lambda t: -mp.e**(-2*t)*(2*mp.cos(t) + mp.sin(t)))
derivalt(lambda t: t*mp.sqrt(2*t + 3), lambda t: 3*(t + 1)/mp.sqrt(2*t + 3))


# alap 4: érintő
def erinto(f, x0):
    y0, m = racio(f(M(x0))), racio(mp.diff(f, M(x0)))
    return y0, m, y0 - m*x0


fa4 = lambda t: t**2 - 4*t + 1
E3, E0 = erinto(fa4, 3), erinto(fa4, 0)
assert E3 == (-2, 2, -8) and E0 == (1, -4, 1)

# alap 5: f' = 3x² − 6x − 24
fa5 = lambda t: t**3 - 3*t**2 - 24*t + 2
KA5 = masodfoku(3, -6, -24)
assert KA5 == [-2, 4] and mp.diff(fa5, -3) > 0 > mp.diff(fa5, 0) and mp.diff(fa5, 5) > 0

# közép 2: f'(x) = 3x² − 6 = 6
fk2 = lambda t: t**3 - 6*t + 1
KK2 = masodfoku(3, 0, -12)
EK2 = [erinto(fk2, t) for t in KK2]

# közép 3: f'' = 12x² − 36x + 24
fk3 = lambda t: t**4 - 6*t**3 + 12*t**2 - 5
KK3 = masodfoku(12, -36, 24)
d2 = lambda t: mp.diff(fk3, t, 2)
assert KK3 == [1, 2] and d2(0) > 0 > d2(1.5) and d2(3) > 0

# nehéz 1: f(x) = (x² + 8)/(x − 1); f' számlálója x² − 2x − 8, f'' = 18/(x − 1)³
fn1 = lambda t: (t**2 + 8)/(t - 1)
KN1 = masodfoku(1, -2, -8)
assert KN1 == [-2, 4] and racio(fn1(mp.mpf(0))) == -8
assert mp.diff(fn1, -3) > 0 > mp.diff(fn1, 0) and mp.diff(fn1, 2) < 0 < mp.diff(fn1, 5)
with mp.workdps(120):                     # ferde aszimptota: k = lim f(x)/x, n = lim (f(x) − kx)
    X = mp.mpf(10) ** 40
    k = racio(fn1(X) / X)
    n = racio(fn1(X) - k * X)
assert (k, n) == (1, 1)
derivalt(fn1, lambda t: (t**2 - 2*t - 8)/(t - 1)**2)
assert mp.diff(fn1, 3, 2) > 0 > mp.diff(fn1, -1, 2)

# nehéz 2: a) D = (2a)² − 4·3·3 ; b) f'(2) = 12 + 4a = 0, f(2) = 8 + 4a + b = −1
A_HATAR = masodfoku(4, 0, -36)
A2 = F(-12, 4)
B2 = -1 - 8 - 4*A2
assert A_HATAR == [-3, 3] and (A2, B2) == (-3, 3)

TESZT = {
    'alap-1': v(12, 3, 15, 2, 2, 2, 2, 2),
    'alap-2': v(2, 3, 2, 2, 2, 3, 1),
    'alap-3': v(15, 3, 2, 4, 2, 9, 4, 4, 2, 2),
    'alap-4': v(3, E3[0], 3, E3[1], abs(E3[1]), abs(E3[2]), 0, E0[0], 0, E0[1], abs(E0[1]), E0[2]),
    'alap-5': v(KA5[0], KA5[1], KA5[0], KA5[1], KA5[0], racio(fa5(M(KA5[0]))), KA5[1], racio(fa5(M(KA5[1])))),
    'kozep-1': v(7, 3, 2, 2, 2, 4, 2, 2, 3, 1, 2, 3),
    'kozep-2': v(6, KK2[0], EK2[0][0], 6, abs(EK2[0][2]), KK2[1], EK2[1][0], 6, abs(EK2[1][2])),
    'kozep-3': v(KK3[0], KK3[1], KK3[0], KK3[1], KK3[0], racio(fk3(M(KK3[0]))), KK3[1], racio(fk3(M(KK3[1])))),
    'nehez-1': v('D_f=R\\{1\\}', 'zérushely: nincs', f'f(0)={racio(fn1(mp.mpf(0)))}', 'x=1 (függőleges',
                 f'y=x+{n} (ferde)', 'csökken: (−2; 1) és (1; 4)',
                 'lokális maximum: ' + pont(fn1, KN1[0]), 'lokális minimum: ' + pont(fn1, KN1[1]),
                 'konvex: (1; pluszvegtelen)', 'inflexiós pont nincs'),
    'nehez-2': v('D=4a^2-36', f'a<{A_HATAR[0]} vagy a>{A_HATAR[1]}', f'így a={A2}', f'így b={B2}'),
}
