# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 1e/01 logika.

Az igazságértékeket és a tautológia-döntéseket Python-kiértékelés adja
(nem a HTML-ből másolva). A kontrapozíciót is a definícióból képezzük.
"""
from itertools import product

FAJL = '1e/01-logika-halmazok-fuggvenyek/feladatok-logika.html'

IMP = lambda a, b: (not a) or b
EKV = lambda a, b: a == b
XOR = lambda a, b: a != b


def jel(b):
    return '⊤' if b else '⊥'


def sorok(f, n=2):
    """A formula igazságértékei a (⊤,⊤),(⊤,⊥),(⊥,⊤),(⊥,⊥) sorrendben."""
    return [f(*ert) for ert in product([True, False], repeat=n)]


def tautologia(f, n=2):
    return all(sorok(f, n))


T, F = True, False

# ── alap-7: konstans formulák ─────────────────────────────────────────
A7 = [IMP(T and (not F), F),
      not (F or T),
      IMP(F, F) and T,
      EKV(not T, F),
      (T or F) and IMP(T, T),
      not (T and (not T))]

# ── alap-8: a négy alapművelet igazságtáblája ─────────────────────────
A8 = [[p and q for p, q in product([T, F], repeat=2)],
      [p or q for p, q in product([T, F], repeat=2)],
      [IMP(p, q) for p, q in product([T, F], repeat=2)],
      [EKV(p, q) for p, q in product([T, F], repeat=2)]]

# ── kozep-1: összetett konstans formulák ──────────────────────────────
K1 = [IMP((not T) or F, F and T),
      (not IMP(F, T)) or EKV(T, T),
      EKV(T and (not F), IMP(T, F)),
      IMP(T, F) or IMP(F, T),
      not ((T or F) and (not T))]

# ── kozep-3: tautológia-e? ────────────────────────────────────────────
K3 = [tautologia(lambda p, q: EKV(IMP(p, q), IMP(not q, not p))),
      tautologia(lambda p, q: EKV(not (p and q), (not p) or (not q))),
      tautologia(lambda p, q: EKV(IMP(p, q), p and (not q))),
      tautologia(lambda p, q: EKV(p or q, IMP(not p, q))),
      tautologia(lambda p, q: IMP(IMP(p, q) and p, q))]

# ── nehez-2 ───────────────────────────────────────────────────────────
N2 = [tautologia(lambda p, q: IMP((p or q) and (not p), q)),
      tautologia(lambda p, q: EKV(EKV(p, q), (p and q) or ((not p) and (not q))))]

# ── nehez-4: hány sorban igaz? ────────────────────────────────────────
N4 = [sum(sorok(lambda p, q: IMP(p, q) or IMP(q, p))),
      sum(sorok(lambda p, q: XOR(p, q))),
      sum(sorok(lambda p, q: (p and (not p)) or q))]

TESZT = {
    'alap-7': [(b, jel(v)) for b, v in zip('abcdef', A7)],
    'alap-8': [(b, ', '.join(jel(x) for x in sor)) for b, sor in zip('abcd', A8)],
    'kozep-1': [(b, jel(v)) for b, v in zip('abcde', K1)],
    'kozep-3': [(b, v) for b, v in zip('abcde', K3)],
    'nehez-2': [(b, v) for b, v in zip('ab', N2)],
    'nehez-4': [('a', N4[0]), ('b', N4[1]), ('c', N4[2])],
}
