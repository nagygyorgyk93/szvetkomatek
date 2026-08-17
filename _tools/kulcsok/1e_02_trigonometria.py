# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/02 trigonometria.

A közelítő értékeket Python-számolás adja; a pontos (gyökös) alakokat a
szöveges egyezés ellenőrzi.
"""
import math
from fractions import Fraction as F

FAJL = '1e/02-trigonometria/feladatok-trigonometria.html'

fok = math.radians
k5 = lambda x: round(x, 5)
k2 = lambda x: round(x, 2)

# ── alap-3: számológépes értékek öt tizedesre ─────────────────────────
A3 = [k5(math.sin(fok(41))), k5(math.cos(fok(63))), k5(math.tan(fok(26)))]

# ── alap-7: rombusz területe ──────────────────────────────────────────
A7 = k2(400 * math.sin(fok(40)))

# ── alap-12: létra ────────────────────────────────────────────────────
A12 = [k2(8 * math.sin(fok(70))), k2(8 * math.cos(fok(70)))]

# ── kozep-6: derékszögű háromszög megoldása (c=14, α=24°) ─────────────
K6 = [k2(14 * math.sin(fok(24))), k2(14 * math.cos(fok(24))), 90 - 24]

# ── kozep-7 … kozep-11: alkalmazások ──────────────────────────────────
K7 = k2(28 * math.tan(fok(23)))
K8 = k2(25 * math.tan(fok(42)))
K9 = k2(60 * math.sin(fok(35)))
K10 = k2(122 * math.sin(fok(7 + F(35, 60))))
K11 = [round(math.degrees(math.atan(24 / 200)), 2), k2(math.hypot(200, 24))]

# ── nehez-2: (sin+cos)/(5cos−3sin), ha sin = 7/25 ─────────────────────
s, c = F(7, 25), F(24, 25)
N2 = (s + c) / (5 * c - 3 * s)

# ── nehez-3: rámpa ────────────────────────────────────────────────────
N3 = [k2(12 * math.sin(fok(8))), k2(12 * math.cos(fok(8)))]

# ── nehez-4: egyenlő szárú háromszög, a = 10, b = 13 ──────────────────
N4_cos = F(5, 13)

TESZT = {
    'alap-3': [('a', A3[0]), ('b', A3[1]), ('c', A3[2])],
    'alap-7': [('', A7)],
    'alap-12': [('', A12[0]), ('', A12[1])],
    'kozep-6': [('', K6[0]), ('', K6[1]), ('', K6[2])],
    'kozep-7': [('', K7)],
    'kozep-8': [('', K8)],
    'kozep-9': [('', K9)],
    'kozep-10': [('', K10)],
    'kozep-11': [('', K11[0]), ('', K11[1])],
    'nehez-2': [('', N2)],
    'nehez-3': [('', N3[0]), ('', N3[1])],
    'nehez-4': [('', N4_cos)],
}
