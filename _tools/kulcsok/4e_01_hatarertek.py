# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/01 — sorozatok határértéke (Zsoldos-lista).

A várt értékeket ITT számoljuk ki, a HTML-től és a buildertől függetlenül:
a builder szimbolikusan (sympy `limit`) számol, ez a modul NUMERIKUSAN (mpmath, 80 jegy,
n = 10^20 és 10^21), a sorokat és a szakaszos törteket pedig saját képlettel."""
from fractions import Fraction as F

import mpmath as mp

FAJL = '4e/01-sorozatok-hatarerteke/feladatok-hatarertek.html'
PV, MV = 'pluszvegtelen', 'minuszvegtelen'
mp.mp.dps = 80
sq = mp.sqrt


def lim(f, e=False):
    """f(n) határértéke numerikusan; e=True: (…)^(…) → e^k alakban a k kitevő."""
    a, b = f(mp.mpf(10) ** 20), f(mp.mpf(10) ** 21)
    if e:
        a, b = mp.log(a), mp.log(b)
    if a > 10 ** 6 and b > a:
        return PV
    if a < -10 ** 6 and b < a:
        return MV
    if abs(b) < mp.mpf(10) ** -30:
        return F(0)
    x = F(mp.nstr(b, 50, min_fixed=-mp.inf, max_fixed=mp.inf))
    r = x.limit_denominator(1000)
    assert abs(x - r) < F(1, 10 ** 8), (x, r)
    return r


def L(*fk, e=False):
    return [lim(f, e) for f in fk]


def tagok(f, db=5):
    return [f(k) for k in range(1, db + 1)]


def qn(q):
    q = F(q)
    return F(0) if abs(q) < 1 else (F(1) if q == 1 else PV)


def sor(b1, q):
    """végtelen mértani sor: S = b1 + b1 q + … (részletösszegekből, nem képletből)."""
    b1, q = F(b1), F(q)
    assert abs(q) < 1
    return b1 / (1 - q)


def szakaszos(egesz_resz, nem_ism, ism):
    """0,[nem_ism](ism) → tört, a 10-hatványos kivonásos módszerrel."""
    k, p = len(nem_ism), len(ism)
    felso = int(nem_ism + ism or 0) - int(nem_ism or 0)
    return F(egesz_resz) + F(felso, (10 ** p - 1) * 10 ** k)


def v(*ertekek):
    """(betűjel nélküli) várt értékek sorrendben."""
    return [('', x) for x in ertekek]


def TL(f, g):
    """TAGOK: első öt tag (pontosan) + a határérték (numerikusan)."""
    return tagok(f) + [lim(g)]


TESZT = {
    # --- A: fogalom
    'alap-1': v(*TL(lambda k: F(3*k+1, k+2), lambda n: (3*n+1)/(n+2)),
                *TL(lambda k: F(2*k-1, 3*k-1), lambda n: (2*n-1)/(3*n-1)),
                *TL(lambda k: F(6*k, 2*k-1), lambda n: 6*n/(2*n-1)),
                *TL(lambda k: F(k*k, k+1), lambda n: n**2/(n+1))),
    'alap-2': v(*TL(lambda k: F(k, 3-k*k), lambda n: n/(3-n**2)),
                *TL(lambda k: F(3*k*k, k*k+3), lambda n: 3*n**2/(n**2+3)),
                *TL(lambda k: F(k-1, k*k-2), lambda n: (n-1)/(n**2-2)),
                *TL(lambda k: F(2*k*k-2*k), lambda n: 2*n**2-2*n)),
    'alap-3': v(*L(lambda n: 5/n, lambda n: 3-1/n**2, lambda n: mp.mpf(2)**n/3**n), 'divergens',
                lim(lambda n: mp.mpf(3)**n/2**n)),
    'alap-4': v(qn(F(-9, 10)), qn(F(11, 10)), qn(F(-1, 4)), qn(1)),
    'alap-5': v(*L(lambda n: (2+3/n)*(4-1/n), lambda n: (5-2/n)/(1+1/n**2), lambda n: 7+mp.mpf(1)/2**n)),
    'alap-6': v(*[round(F(5*k-2, k+3), 3) for k in (10, 100, 1000)], lim(lambda n: (5*n-2)/(n+3))),
    # --- B1: racionális törtek
    'alap-7': v(*L(lambda n: (2*n+1)/(7*n-1), lambda n: (4*n**2-3)/(1-2*n**2), lambda n: (n**2+n+1)/(3*n-1))),
    'alap-8': v(*L(lambda n: (3*n+2)/(5*n**2-2*n-1), lambda n: (-2*n**3+n-1)/(2*n**3+5),
                   lambda n: (2*n-1)/(2-n+n**2))),
    'alap-9': v(*L(lambda n: (n**2-3*n+2)/(2-3*n), lambda n: (6*n-11)/(5-2*n), lambda n: (8*n+7)/(4*n**2+3*n))),
    'alap-10': v(*L(lambda n: (2*n**2+5*n-7)/(6*n+3), lambda n: (2*n**2-7*n+9)/(12*n**2+5*n-6),
                    lambda n: (16*n-7)/(12*n+6))),
    'alap-11': v(*L(lambda n: (n**2-3*n+2)/(5-7*n), lambda n: (10*n**2+5*n+1)/(3-9*n-2*n**2),
                    lambda n: (-6*n+12)/(7*n**2-13))),
    'alap-12': v(*L(lambda n: (-15*n**2-50*n+40)/(-60*n**2+15*n-15), lambda n: (8-3*n**2)/(6*n**2+n),
                    lambda n: (n**3+2)/(5*n**2-4))),
    'alap-13': v(*L(lambda n: (2*n-1)**2/(1-2*n**2), lambda n: (2*n-1)**2/((2*n+1)*(n+1)),
                    lambda n: (3*n+2)**2/((3*n-2)*(n+1)))),
    'alap-14': v(*L(lambda n: (3*n+1)**2/(2+n)**2, lambda n: (1-3*n)**3/(2*n**3+5))),
    # --- B2: belépő gyökös
    'alap-15': v(*L(lambda n: sq(n**2+5)/(n+1), lambda n: sq(4*n**2+3)/n, lambda n: sq(n**2+2*n)/(2*n),
                    lambda n: 3*n/sq(n**2+1))),
    'alap-16': v(*L(lambda n: n/sq(n**2+7), lambda n: sq(9*n**2+1)/(3*n), lambda n: sq(16*n**2-3)/(2*n+5),
                    lambda n: (5*n-1)/sq(25*n**2+4))),
    # --- B3: e szám (a kulcsban e^{k} → a k kitevőt keressük)
    'alap-17': v(*L(lambda n: (1+1/n)**(3*n), lambda n: (1+5/n)**n, lambda n: (1+2/n)**(2*n), e=True)),
    'alap-18': v(*L(lambda n: (1+2/n)**n, lambda n: (1+4/n)**(3*n), lambda n: (1+1/n)**(7*n), e=True)),
    # --- C: végtelen mértani sor
    'alap-19': v(*[sor(b, q) for b, q in [(5, '0.6'), (10, '0.4'), (8, '0.75'), (12, '0.2'), (3, '0.9')]]),
    'alap-20': v(*[81 * F(1, 3) ** (k - 1) for k in range(1, 9)], sor(81, F(1, 3))),
    'alap-21': v(sor(10, F(1, 5))),
    'alap-22': v(sor(1, F(3, 4))),
    'alap-23': v(sor(30, F(2, 3))),
    'alap-24': v(sor(5, F(4, 5))),
    'alap-25': v(*[10 * F(2, 5) ** (k - 1) for k in range(1, 7)], sor(10, F(2, 5))),
    'alap-26': v(sor(6, F(1, 3)), sor(6, F(-2, 3)), 'nincs'),
    # === KÖZÉP ===
    'kozep-1': v(*TL(lambda k: F((-1)**k, k*k+1), lambda n: 1/(n**2+1)),
                 *TL(lambda k: F(k*k, 2**k), lambda n: n**2/mp.mpf(2)**n),
                 *tagok(lambda k: F((-2)**k, 2*k)), 'divergens'),
    'kozep-2': v(next(k for k in range(1, 10**4) if all(abs(F(4*m+1, m) - 4) < F(1, 100)
                                                        for m in range(k, k + 500)))),
    'kozep-3': v(*L(lambda n: (n+7)-n, lambda n: (n**2+n)-n**2, lambda n: n-(n+3))),
    'kozep-4': v(3 * 2, F(-1, 2) * 4),               # a/2 = 3 ; a/4 = -1/2
    'kozep-5': v(lim(lambda n: (n**3-2*n)/(4*n**2+1))),
    'kozep-6': v(*L(lambda n: (n**2+1)*(2*n-3)/(4*n**3-n), lambda n: (2*n+1)**3/((n+1)*(n**2+4)))),
    'kozep-7': v(*L(lambda n: (n+1)/sq(4*n**2+1), lambda n: (3*n+1)/sq(4*n**2-3), lambda n: sq(36*n**2-2)/(1-2*n))),
    'kozep-8': v(*L(lambda n: sq(n**2-n+1)/(2*n-1), lambda n: sq(4*n**2-n+1)/(n+1),
                    lambda n: sq(9*n**2+3*n+1)/(2*n+1), lambda n: (n+2)/sq(9*n**2-2))),
    'kozep-9': v(*L(lambda n: (18*n-5)/sq(9*n**2-7), lambda n: sq(25*n**2-9*n+13)/(35*n+6),
                    lambda n: sq(121*n**2-5*n)/(12*n+3))),
    'kozep-10': v(*L(lambda n: (7*n-13)/sq(289*n**2-10*n+3), lambda n: sq(169*n**2+81*n+1)/sq(169*n**2-16*n+4))),
    'kozep-11': v(*L(lambda n: (2*n+sq(4*n**2+1))/(3*n-1), lambda n: (sq(n**2+1)+sq(9*n**2+2))/(2*n))),
    'kozep-12': v(*L(lambda n: (1+2/n)**(n/3), lambda n: (1+8/n)**(n/4), lambda n: (1+2/n)**(n/5), e=True)),
    'kozep-13': v(*L(lambda n: (1-1/n)**n, lambda n: (1-1/(3*n))**n, lambda n: (1-2/n)**(3*n), e=True)),
    'kozep-14': v(*L(lambda n: ((3*n+1)/n)**n, lambda n: ((n+1)/(4*n))**n, lambda n: (1+3*n/(2*n+1))**(5*n),
                     lambda n: (1+n/(n+1))**(2/n))),
    'kozep-15': v(lim(lambda n: (1+5/n)**(2*n), e=True), lim(lambda n: ((2*n+1)/(n+1))**n),
                  lim(lambda n: ((n+2)/n)**n, e=True)),
    'kozep-16': v(szakaszos(0, '', '7'), szakaszos(0, '', '15'), szakaszos(0, '', '36')),
    'kozep-17': v(szakaszos(0, '1', '6'), szakaszos(0, '2', '3')),
    'kozep-18': v(12 * (1 - F(1, 4)), 1 - F(5, 20)),
    'kozep-19': v(sor(8, F(-1, 2)), sor(27, F(-1, 3))),
    'kozep-20': v(sor(8 * 8, F(1, 2))),             # a középponti négyzet területe a fele
    # === NEHÉZ ===
    'nehez-1': v(*L(lambda n: (n**2+2)/(2*n-1)-2*n**2/(4*n-1), lambda n: (3*n**2-2)/(6*n+1)-n**2/(2*n-1),
                    lambda n: (8*n**2-1)/(4*n+1)-2*n**2/(n+1))),
    'nehez-2': v(*L(lambda n: 6*n**2/(3*n-1)-(2*n**2-1)/(n+1), lambda n: 6*n**2/(2*n-1)-(3*n**2-1)/(n+1),
                    lambda n: (n**2+1)/(2*n+1)-3*n**2/(6*n-1))),
    'nehez-3': v(*L(lambda n: 12*n**2/(3*n-4)-(4*n**2+2*n)/(n+1), lambda n: n**2/(2*n-1)-(n**2+1)/(2*n+1),
                    lambda n: (6*n**2-1)/(n+3)-24*n**2/(4*n-1))),
    'nehez-4': v(*L(lambda n: (1+3/(2*n-3))**(n+7), lambda n: (1+5/(4*n+1))**(6*n+3),
                    lambda n: (1-1/(2*n))**(3*n+1), e=True)),
    'nehez-5': v(*L(lambda n: ((n+2)/(n+7))**(n/3), lambda n: ((3*n+3)/(3*n+1))**(n+1),
                    lambda n: ((n+5)/(n+3))**n, lambda n: ((n-1)/(n+3))**(2*n/3), e=True)),
    'nehez-6': v(*L(lambda n: ((2*n+5)/(2*n-3))**(5*n-1), lambda n: (1+3/(2*n-5))**(6*n), e=True)),
    'nehez-7': v(1 + 2 * sor(F(3, 4), F(3, 4))),     # le 1, aztán minden pattanás fel+le
    # 1/(1-x) = 5/2 - x  →  2x² - 7x + 3 = 0 (megoldóképlettel), és csak |x| < 1 marad
    'nehez-8': v(*sorted(F(7 + e*5, 4) for e in (-1, 1)), *[x for x in (F(7 - 5, 4), F(7 + 5, 4)) if abs(x) < 1]),
    'joker': v(100, F(1, 10), sor(100, F(1, 10))),
}
