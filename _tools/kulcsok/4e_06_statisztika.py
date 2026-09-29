# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt: 4e/06 — Zsoldos-lista, statisztika.

A mutatókat ITT számoljuk ki, a builder `abra_stat.mutatok` függvényétől függetlenül, a nyers adatsorokból (kézzel
átírva: RZS Popis 2022, Eurostat demo_fasec, Open-Meteo ERA5 2024, NBA-statisztika). Konvenciók, ahogy a tananyag
tanítja: a kvartilis az alsó/felső fél mediánja (páratlan elemszámnál a medián nélkül), a szórásnégyzet 1/n-es.
Kerekítés: ROUND_HALF_UP a pontos törtből."""
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F

FAJL = '4e/06-valoszinuseg-statisztika/feladatok-statisztika.html'


def v(*ertekek):
    return [('', e) for e in ertekek]


def k(x, j=3):
    x = F(x) if not isinstance(x, float) else F(repr(x))
    d = Decimal(x.numerator) / Decimal(x.denominator)
    return F(str(d.quantize(Decimal(1).scaleb(-j), rounding=ROUND_HALF_UP)))


def Fl(xs):
    return [F(str(x)) for x in xs]


def atlag(xs):
    return sum(xs) / len(xs)


def med(xs):
    s, n = sorted(xs), len(xs)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def kvart(xs):
    s, n = sorted(xs), len(xs)
    return med(s[:n // 2]), med(s[(n + 1) // 2:])


def var(xs):
    a = atlag(xs)
    return sum((x - a) ** 2 for x in xs) / len(xs)


def szoras(xs):
    return F(repr(float(var(xs)) ** 0.5))


def aae(xs):
    a = atlag(xs)
    return sum(abs(x - a) for x in xs) / len(xs)


JEGY = [4, 3, 5, 2, 3, 3, 3, 4, 4, 5, 2, 2, 1, 3, 2, 4, 1, 5, 4, 3, 3, 4, 2, 1, 3, 2, 3, 4, 3, 5]
KOR10_SZABADKA = [12122, 12243, 12587, 15581, 18127, 16916, 18415, 12662, 5299]    # 0–9, …, 70–79, 80+
JOKIC_MECCS = [80, 73, 75, 80, 73, 72, 74, 69, 79, 70, 65]
JOKIC_PONT = Fl([10.0, 16.7, 18.5, 20.1, 19.9, 26.4, 27.1, 24.5, 26.4, 29.6, 27.7])
HZ_SRB = [773945, 711946, 459926, 375565, 156050, 111912]                          # 1, 2, …, 6+ tagú
SRB_FERFI, SRB_NO = (3231978, F('42.43')), (3415025, F('45.19'))
SZABADKA = Fl([2.5, 8.9, 10.3, 14.6, 18.7, 23.1, 26.4, 26.7, 19.1, 12.9, 4.6, 2.5])
SPLIT = Fl([8.0, 11.0, 12.3, 15.7, 18.9, 23.8, 28.4, 28.6, 21.4, 18.4, 11.7, 8.1])
LISSZABON = Fl([13.1, 14.2, 13.8, 16.6, 17.6, 19.6, 22.4, 22.8, 20.5, 18.6, 16.3, 12.2])
ESOS = [11, 5, 7, 6, 8, 10, 3, 3, 9, 6, 4, 7]
CSAPADEK = Fl([42.2, 21.6, 20.8, 33.7, 50.1, 80.7, 13.7, 8.7, 79.3, 44.2, 40.4, 52.7])   # Szabadka 2024, mm
JUL_MAX = Fl([30.7, 23.6, 24.6, 25.5, 28.7, 30.5, 32.7, 34.7, 35.7, 36.0, 37.3, 37.6, 36.6, 37.0, 36.5, 37.8, 35.7,
              33.7, 34.1, 29.5, 30.4, 33.0, 31.3, 30.4, 27.6, 29.3, 31.5, 35.9, 29.0, 28.4, 31.6])
SG_SRB = [5691551, 2602550, 1685824, 1376725, 26452]    # összes; ismeri, részben, nem, ismeretlen
HU_2023, HU_2024 = 87671, 78868

_jc = Counter(JEGY)
_q = kvart(SZABADKA)
_gyak = [sum(1 for t in JUL_MAX if a <= t < a + 2) for a in range(22, 38, 2)]
_leg = max(_gyak)
_pont10 = JOKIC_PONT[1:]
_eso_modszer = [F(1, 2) ** 5 * [1, 5, 10, 10, 5, 1][i] for i in range(6)]
_erme = {0: 1, 1: 4, 2: 5, 3: 6, 4: 3, 5: 1}
_z = lambda xs: (max(xs) - k(atlag(xs), 2)) / k(szoras(xs), 2)     # a feladat a kerekített átlagot, szórást adja meg
_kiugo = lambda xs: sum(1 for x in xs if abs(x - atlag(xs)) > szoras(xs))

TESZT = {
    'alap-1': v('mennyiségi folytonos mennyiségi diszkrét minőségi minőségi mennyiségi diszkrét mennyiségi diszkrét'),
    'alap-2': v('nominális ordinális intervallum nominális ordinális intervallum'),
    'alap-3': v(*[_jc[j] for j in range(1, 6)], *[k(F(100 * _jc[j], 30), 1) for j in range(1, 6)]),
    'alap-4': v('60-69', KOR10_SZABADKA[0] + KOR10_SZABADKA[1],
                k(F(100 * sum(KOR10_SZABADKA[6:]), sum(KOR10_SZABADKA)), 1)),
    'alap-5': v('oszlopdiagram vonaldiagram kördiagram hisztogram'),
    'alap-6': v(med([10, 7, 7, 6, 13, 12, 8, 14]), med([17, 31, 15, 28, 35, 30, 29, 19, 19]), 8, 'nincs',
                med(JOKIC_MECCS), *sorted(x for x, c in Counter(JOKIC_MECCS).items()
                                          if c == max(Counter(JOKIC_MECCS).values()))),
    'alap-7': v(F(25 + 2 * 50 + 3 * 15 + 4 * 5 + 5 * 2, 100),
                k(F(sum((i + 1) * f for i, f in enumerate(HZ_SRB)), sum(HZ_SRB)), 2), 'kisebb'),
    'alap-8': v(k(F(50 * 98000 + 40 * 76000, 90), 0), atlag(JEGY), med(JEGY), _jc.most_common(1)[0][0],
                k((SRB_FERFI[0] * SRB_FERFI[1] + SRB_NO[0] * SRB_NO[1]) / (SRB_FERFI[0] + SRB_NO[0]), 2)),
    'alap-9': v(min(SZABADKA), max(SZABADKA), max(SZABADKA) - min(SZABADKA), med(SZABADKA), _q[0], _q[1]),
    'alap-10': v(atlag([2, 5, 8, 11, 14]), aae([2, 5, 8, 11, 14]), var([2, 5, 8, 11, 14]),
                 atlag([2, 8, 14]), aae([2, 8, 14]), var([2, 8, 14]),
                 k(atlag(ESOS), 2), med(ESOS), max(ESOS) - min(ESOS)),
    'kozep-1': v(*[k(F(100 * x, SG_SRB[0]), 1) for x in SG_SRB[1:]], *[k(F(360 * x, SG_SRB[0]), 1) for x in SG_SRB[1:]]),
    'kozep-2': v(*_gyak, *[b for a in range(22, 38, 2) if _gyak[(a - 22) // 2] == _leg for b in (a, a + 2)],
                 sum(1 for t in JUL_MAX if t >= 34)),
    'kozep-3': v('torz megfelelő torz megfelelő'),
    'kozep-4': v(k(atlag(SZABADKA), 2), k(atlag(SPLIT), 2), med(SZABADKA), med(SPLIT),
                 k(szoras(SZABADKA), 2), k(szoras(SPLIT), 2), 'Szabadkán'),
    'kozep-5': v(k(_z(SZABADKA), 2), k(_z(LISSZABON), 2), 'a lisszaboni'),
    'kozep-6': v(k(atlag(_pont10), 2), med(_pont10), 'az átlag'),
    'kozep-7': v(F(sum(i * f for i, f in _erme.items()), sum(_erme.values())),
                 F(sum(i * f for i, f in _erme.items()), sum(_erme.values())),
                 sum(i * p for i, p in enumerate(_eso_modszer)), F(_erme[3], 20), _eso_modszer[3], _eso_modszer[3]),
    'nehez-1': v(k(F(100 * (HU_2023 - HU_2024), HU_2023), 1), k(F(HU_2024 - 75000, HU_2023 - 75000)), 0),
    'nehez-2': v(5 * F(36, 10) - 4 * F(325, 100), 'nem', 5 * 4 - 4 * F(325, 100),
                 12 * atlag(CSAPADEK) - (sum(CSAPADEK) - CSAPADEK[4])),
    'nehez-3': v(k(atlag(SZABADKA), 2), k(szoras(SZABADKA), 2), k(atlag(LISSZABON), 2), k(szoras(LISSZABON), 2),
                 _kiugo(SZABADKA), _kiugo(LISSZABON), 'Lisszabont'),
    'joker': v(3, 3, 4, 7, 8),
}

# a joker példája valóban jó-e: módusz 3, medián 4, átlag 5
assert atlag(CSAPADEK) == F('40.675')   # a feladatban megadott átlag pontos
assert Counter([3, 3, 4, 7, 8]).most_common(1)[0] == (3, 2) and med([3, 3, 4, 7, 8]) == 4 and atlag([3, 3, 4, 7, 8]) == 5
