# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/04 arányosság, százalék, kamat.

Minden várt érték független Python-számolásból jön.
"""
from fractions import Fraction as F

FAJL = '1e/04-aranyossag/feladatok-aranyossag.html'


def aranypar(a, b, c, d):
    """Az a:b = c:d aránypárból a hiányzó tag (None helyén)."""
    if a is None:
        return F(b * c, d)
    if b is None:
        return F(a * d, c)
    if c is None:
        return F(a * d, b)
    return F(b * c, a)


def eloszt(ossz, aranyok):
    e = F(ossz, sum(aranyok))
    return [e * a for a in aranyok]


def keverek(t1, t2, ossz, cel):
    """Mennyi kell az első anyagból: x·t1 + (össz−x)·t2 = össz·cél."""
    return F(ossz * (cel - t2), t1 - t2)


def egyszeru_kamat(toke, p, ev=0, honap=0, nap=0):
    return toke * F(p, 100) * (F(ev) + F(honap, 12) + F(nap, 360))


# ── alap-1 ────────────────────────────────────────────────────────────
A1 = [aranypar(12, None, 3, 8),      # 12:x = 3:8
      aranypar(None, 15, 4, 5),      # x:15 = 4:5
      aranypar(7, 4, 21, None)]      # 7:4 = 21:x
# (x+5):4 = x:3  →  3(x+5) = 4x
A1_d = 15
# (2x-1):3 = 3:1
A1_e = F(9 + 1, 2)

# ── alap-2 ────────────────────────────────────────────────────────────
A2 = eloszt(4200, [3, 7, 5]) + eloszt(3600, [2, 3, 4]) + eloszt(999, [12, 11, 14])

# ── alap-3: 1:150 000 térkép, 6 cm ────────────────────────────────────
A3_km = F(6 * 150000, 100000)

# ── alap-4: fordított arányosság ──────────────────────────────────────
A4 = [F(3 * 14, 7), F(9 * 35, 15)]

# ── alap-5 / alap-6 ───────────────────────────────────────────────────
A5 = [F(55400 * 15, 100), F(800 * 20, 100), F(160 * 100, 800)]
A6 = F(105219, 1) / F(90, 100)

# ── alap-7 / kozep-5: keverék ─────────────────────────────────────────
A7 = keverek(F(40, 100), F(85, 100), 20, F(58, 100))
K5 = keverek(F(60, 100), F(90, 100), 100, F(795, 1000))

# ── alap-8: egyszerű kamat ────────────────────────────────────────────
A8 = [egyszeru_kamat(540000, F(15, 2), ev=4), egyszeru_kamat(108000, 8, honap=4)]

# ── kozep-1: összetett arány ──────────────────────────────────────────
# x:y = 3:6 és y:z = 2:5  →  y-t közös nevezőre
K1 = [3 * 2, 6 * 2, 6 * 5]                       # → 6:12:30 = 1:2:5
K1 = [x // 6 for x in K1]
# a:b = 2:3 és b:c = 6:7  →  b közös nevezőre (3·2 = 6)
K1b = [2 * 2, 3 * 2, 3 * 7 // 3]                 # → 4:6:7
# x:y = 3:4 és y:z = 6:5  →  y közös nevezőre (4·6 = 24)
K1c = [3 * 6, 4 * 6, 4 * 5]                      # → 18:24:20 = 9:12:10
K1c = [x // 2 for x in K1c]

# ── kozep-3: 6 munkás 5 nap; 2 nap után +3 ────────────────────────────
ossz_munka = 6 * 5
kesz = 6 * 2
K3 = 2 + F(ossz_munka - kesz, 9)

# ── kozep-4: 8% fogyás, majd 10% hízás ────────────────────────────────
K4 = 72 * F(92, 100) * F(110, 100)

# ── kozep-6: 28% profittal 3136 ───────────────────────────────────────
K6 = F(3136, 1) / F(128, 100)

# ── nehez-1 / 2 / 5 / 6 / 7 / 8 ───────────────────────────────────────
N1 = (1 - F(125, 100) * F(75, 100)) * 100        # hány %-kal csökken
N2 = 25 * 5                                       # 25 kadét, 25 perc
N5 = F(2, 1) / F(55, 100)                         # friss szőlő 2 kg mazsolához
N6 = F(132000, 1) / (1 + F(8, 100) * 4)
N7 = F(571500 * 100, 12700)
N8 = F(15, 10) / F(5, 8)                          # a hosszabb 5 rész = 1,5 m

TESZT = {
    'alap-1': [('', A1[0]), ('', A1[1]), ('', A1[2]), ('', A1_d), ('', A1_e)],
    'alap-2': [('', v) for v in A2],
    'alap-3': [('', A3_km)],
    'alap-4': [('', A4[0]), ('', A4[1])],
    'alap-5': [('', v) for v in A5],
    'alap-6': [('', A6)],
    'alap-7': [('', A7), ('', 20 - A7)],
    'alap-8': [('', A8[0]), ('', A8[1])],
    'kozep-1': [('', v) for v in K1 + K1b + K1c],
    'kozep-3': [('', K3)],
    'kozep-4': [('', K4)],
    'kozep-5': [('', K5), ('', 100 - K5)],
    'kozep-6': [('', K6)],
    'nehez-1': [('', N1)],
    'nehez-2': [('', N2)],
    'nehez-5': [('', round(float(N5), 2))],
    'nehez-6': [('', N6)],
    'nehez-7': [('', N7)],
    'nehez-8': [('', N8)],
}
