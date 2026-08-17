# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/01 halmazok.

Minden várt érték FÜGGETLEN Python-számolásból jön — nem a HTML-ből másolva.
A korpusz konvenciója: ℕ = {1, 2, 3, …} (a nulla nem tartozik bele).
"""
from itertools import combinations

FAJL = '1e/01-logika-halmazok-fuggvenyek/feladatok-halmazok.html'


def oszto(n):
    return {d for d in range(1, n + 1) if n % d == 0}


def hatvanyhalmaz(h):
    h = sorted(h)
    return [set(c) for r in range(len(h) + 1) for c in combinations(h, r)]


# ── alap-1 ────────────────────────────────────────────────────────────
A1 = {x for x in range(1, 100) if x <= 5}                    # x ∈ ℕ, x ≤ 5
B1 = {x for x in range(-50, 51) if -3 <= x <= 2}             # x ∈ ℤ
C1 = set('matematika')
D1 = {2 * n for n in range(1, 100) if n <= 4}
P1 = {x for x in range(-50, 51) if x * x < 10}

# ── alap-3 ────────────────────────────────────────────────────────────
A3, B3, C3 = {1, 2, 3, 4, 5}, {2, 4, 6, 8}, {1, 2, 4, 8}

# ── alap-4 ────────────────────────────────────────────────────────────
S4 = set(range(1, 11))
A4, B4 = {2, 4, 6, 8, 10}, {1, 2, 3, 4, 5}

# ── alap-9 ────────────────────────────────────────────────────────────
A9, B9, C9 = {1, 3, 5, 7, 9}, {1, 2, 3, 4, 5}, {5, 6, 7, 8, 9}

# ── kozep-1 ───────────────────────────────────────────────────────────
Ak1, Bk1 = oszto(24), oszto(36)

# ── kozep-6 ───────────────────────────────────────────────────────────
metszet_k6 = 20 + 15 - 28

# ── nehez-7 ───────────────────────────────────────────────────────────
An7, Bn7, Cn7 = oszto(12), oszto(18), oszto(8)

# ── nehez-8 ───────────────────────────────────────────────────────────
S8 = set(range(1, 9))
A8 = {x for x in S8 if x % 2 == 0}
B8 = {x for x in S8 if x % 3 == 0}
C8 = {5, 6, 7, 8}

TESZT = {
    'alap-1': [('a', A1), ('b', B1), ('c', C1), ('d', D1), ('e', P1)],
    'alap-3': [('a', A3 | B3), ('b', A3 & B3), ('c', A3 - B3), ('d', B3 - A3),
               ('e', A3 - (B3 | C3)), ('f', (A3 & B3) | C3), ('g', B3 & C3),
               ('h', (A3 - B3) - C3)],
    'alap-4': [('a', S4 - A4), ('b', S4 - B4), ('c', (S4 - A4) & (S4 - B4)),
               ('d', (S4 - A4) | (S4 - B4)), ('e', S4 - (A4 | B4))],
    'alap-6': [('b', 7), ('c', 20), ('d', 8), ('e', 32)],
    'alap-8': [('', 13)],
    'alap-9': [('a', A9 & B9 & C9), ('b', A9 | B9 | C9), ('c', A9), ('d', set())],
    'kozep-1': [('a', Ak1 & Bk1), ('b', Ak1 | Bk1), ('c', Ak1 - Bk1),
                ('d', len(Ak1 & Bk1))],
    'kozep-6': [('', metszet_k6)],
    'nehez-3': [('', 330 + 470 + 420 - 140 - 180 - 250 + 120)],
    'nehez-5': [('a', 2 ** 16), ('b', 2 ** 12)],
    'nehez-7': [('a', An7 & Bn7), ('b', An7 | Cn7), ('c', (An7 & Bn7) - Cn7)],
    'nehez-8': [('a', A8 & B8), ('b', C8 - A8), ('d', A8 ^ C8)],
}
