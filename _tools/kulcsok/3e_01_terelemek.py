# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 3e/01 — térelemek, merőlegesség, poliéderek, alaplap.

Minden várt értéket ITT számolunk ki, a HTML-től és a buildertől függetlenül
(sympy-val), és a harness veti össze a Végeredmény-lenyíló szövegével. Ha a
kulcsban elírás van, a 2. lépés bukik; ha a builder számolt rosszul, akkor a
két független számolás tér el egymástól.
"""
from sympy import Rational as R, sqrt, N, atan, acos, deg, binomial

FAJL = '3e/01-poliederek/feladatok-terelemek.html'


def k(x, jegy=2):
    """Kerekített közelítő érték — pontosan úgy, ahogy a kulcsban szerepel.

    A kerekítést PYTHON végzi (a sympy `round` bináris Floatot ad, ami 8,49 helyett
    8,490234375-öt jelentene).
    """
    return round(float(N(x, 15)), jegy)


# ── független számolások ────────────────────────────────────────────────
KOCKA_EL = 6
lapatlo6 = KOCKA_EL * sqrt(2)
testatlo6 = KOCKA_EL * sqrt(3)
teglatest_atlo = sqrt(6**2 + 8**2 + 24**2)
kocka_alap_szog = deg(atan(sqrt(2) / 2))
kocka_kozep_csucs = 8 * sqrt(3) / 2

haromszog_m = 8 * sqrt(3) / 2
haromszog_T = 8**2 * sqrt(3) / 4
negyzet_atlo = 5 * sqrt(2)
teglalap_atlo = sqrt(6**2 + 8**2)
trapez_T = R((12 + 8) * 5, 2)
rombusz_T = R(16 * 12, 2)
rombusz_oldal = sqrt(8**2 + 6**2)
hatszog_T = 6 * (6**2 * sqrt(3) / 4)
hatszog_rho = 6 * sqrt(3) / 2
h30_hosszabb = 12 * sqrt(3) / 2
h45_atfogo = 7 * sqrt(2)

elpar_ossz = binomial(12, 2)
elpar_parh = 3 * binomial(4, 2)
elpar_metszo = 8 * binomial(3, 2)
elpar_kitero = elpar_ossz - elpar_parh - elpar_metszo

teglatest_szog = deg(atan(R(12, 5)))
testatlo_oldalel_szog = deg(atan(sqrt(2)))
napsugar_szog = deg(atan(R(2, 3)))
pont_sik_tav = 10 * sqrt(3) / 2

trapez_m = sqrt(5**2 - 4**2)
trapez_egyenlo_T = R((14 + 6) * 3, 2)
h_oldal = 12
h_terulet = 12**2 * sqrt(3) / 4
rombusz2_atlo = 2 * sqrt(13**2 - 12**2)
rombusz2_T = R(24 * 10, 2)
hasab_atlo = sqrt(2 * 5**2 + 12**2)

TESZT = {
    'alap-2':  [('', 4)],
    'alap-7':  [('', k(lapatlo6)), ('', k(testatlo6))],
    'alap-8':  [('', int(teglatest_atlo))],
    'alap-9':  [('', k(kocka_alap_szog))],
    'alap-10': [('', 4), ('', k(kocka_kozep_csucs))],
    'alap-11': [('', 8), ('', 12), ('', 6),
                ('', 12), ('', 18), ('', 8),
                ('', 5), ('', 8), ('', 5),
                ('', 7), ('', 12), ('', 7)],
    'alap-16': [('', k(haromszog_m)), ('', k(haromszog_T))],
    'alap-17': [('', k(negyzet_atlo)), ('', 25), ('', int(teglalap_atlo)), ('', 48)],
    'alap-18': [('', int(trapez_T))],
    'alap-19': [('', int(rombusz_T)), ('', int(rombusz_oldal))],
    'alap-20': [('', k(hatszog_T)), ('', k(hatszog_rho))],
    'alap-21': [('', 6), ('', k(h30_hosszabb)), ('', k(h45_atfogo))],
    'alap-22': [('', 10)],
    'kozep-1': [('', int(elpar_ossz)), ('', int(elpar_parh)),
                ('', int(elpar_metszo)), ('', int(elpar_kitero))],
    'kozep-4': [('', k(teglatest_szog))],
    'kozep-5': [('', k(testatlo_oldalel_szog))],
    'kozep-6': [('', k(napsugar_szog))],
    'kozep-7': [('', k(pont_sik_tav))],
    'kozep-8': [('', 5), ('', 8), ('', 5)],
    'kozep-9': [('', 7), ('', 9)],
    'kozep-10': [('', 6), ('', 12), ('', 8)],
    'kozep-11': [('', 8)],
    'kozep-12': [('', int(trapez_m)), ('', int(trapez_egyenlo_T))],
    'kozep-13': [('', h_oldal), ('', k(h_terulet))],
    'kozep-14': [('', int(rombusz2_atlo)), ('', int(rombusz2_T))],
    'nehez-2': [('', 60)],
    'nehez-3': [('', 3), ('', 4)],
    'nehez-4': [('', k(hasab_atlo))],
}
