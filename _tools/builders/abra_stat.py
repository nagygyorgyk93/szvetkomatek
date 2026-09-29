# -*- coding: utf-8 -*-
"""Statisztikai és valószínűségi ábrák a Szvetkó matek oldalhoz (4e/06, 2026-09-29) — inline SVG.

KÁNON (workflow 4c.): sötét tinta világos „tervrajz-lapon" (`.svgcard`), `role="img"` + `aria-label`, `viewBox`.
A szín sosem egyedüli jelentéshordozó: minden oszlop, cikk és doboz felirattal is azonosítható.

Statikus ábrák: svg_oszlop · svg_hisztogram · svg_kor · svg_vonal · svg_doboz · svg_mozaik · svg_bernoulli_fa
Interaktív (az `assets/js/interaktiv.js` kelti életre; JS nélkül a statikus kép az első képkocka):
  svg_szimulacio (data-mod="szimulacio") · svg_adatlabor (data-mod="adatlabor")
A leíró statisztikai mutatókat (`mutatok`) UGYANÍGY számolja az interaktiv.js — a kvartilis az alsó és a felső fél
mediánja, páratlan elemszámnál a medián egyik félbe sem tartozik; a szórásnégyzet 1/n-es (populációs).
"""
from __future__ import annotations

import math
import random
from html import escape

from tananyag_common import _IV_SZAMLALO, _fmt

TINTA, SZURKE, HALV, RACS = "#0f172a", "#475569", "#94a3b8", "#cbd5e1"
KEK, KEKH, ZOLD, ZOLDH, PIROS, BOR = "#1d4ed8", "#dbeafe", "#047857", "#d1fae5", "#b91c1c", "#b45309"
KOR_SZINEK = ["#1d4ed8", "#0ea5e9", "#f59e0b", "#94a3b8", "#047857", "#b91c1c"]
NBSP = " "


# ------------------------------------------------------------------ számformázás
def ezres(n) -> str:
    """Egész szám ezres tagolással (nem törő szóköz): 15380937 → „15 380 937"."""
    s = f"{int(round(n)):,}".replace(",", NBSP)
    return s.replace("-", "−")


def tized(v: float, j: int = 1) -> str:
    """Tizedesvesszős kerekítés rögzített jegyszámmal: tized(0.4855, 3) → „0,486"."""
    return f"{v:.{j}f}".replace(".", ",").replace("-", "−")


# ------------------------------------------------------------------ leíró statisztika (= interaktiv.js)
def _median(s):
    n, f = len(s), len(s) // 2
    return s[f] if n % 2 else (s[f - 1] + s[f]) / 2


def mutatok(adat):
    s = sorted(adat)
    n = len(s)
    atl = sum(s) / n
    h = n // 2
    also, felso = s[:h], s[h + 1:] if n % 2 else s[h:]
    q1 = _median(also) if also else s[0]
    q3 = _median(felso) if felso else s[-1]
    aae = sum(abs(v - atl) for v in s) / n
    var = sum((v - atl) ** 2 for v in s) / n
    gy = {}
    for v in s:
        gy[v] = gy.get(v, 0) + 1
    maxgy = max(gy.values())
    mod = sorted(v for v, c in gy.items() if c == maxgy) if maxgy > 1 else []
    return dict(n=n, s=s, atlag=atl, median=_median(s), q1=q1, q3=q3, min=s[0], max=s[-1], aae=aae,
                var=var, sz=math.sqrt(var), mod=mod, modgy=maxgy)


def modusz_szoveg(m):
    if not m["mod"]:
        return "nincs (minden érték egyszer fordul elő)"
    return "; ".join(_fmt(v) for v in m["mod"]) + f" ({m['modgy']}-szer)"


# ------------------------------------------------------------------ közös segédek
def _svg(w, h, leiras, belso, extra_attr=""):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{escape(leiras, True)}" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, system-ui, sans-serif"{extra_attr}>\n'
            + "\n".join(belso) + "\n</svg>")


def _t(x, y, szoveg, meret=11.5, szin=TINTA, horgony="middle", vastag=False, extra=""):
    fw = ' font-weight="600"' if vastag else ""
    return (f'  <text x="{x:.1f}" y="{y:.1f}" font-size="{meret}" fill="{szin}" text-anchor="{horgony}"{fw}{extra}>'
            f'{szoveg}</text>')


def _szep_lepes(tart, db=5):
    nyers = tart / db if tart > 0 else 1
    mag = 10 ** math.floor(math.log10(nyers))
    for m in (1, 2, 5, 10):
        if m * mag >= nyers:
            return m * mag
    return 10 * mag


def _szamcimke(v, lepes):
    if abs(v) < 1e-12:
        return "0"
    if abs(v - round(v)) < 1e-9 and lepes >= 1:
        return ezres(v)
    j = max(0, -int(math.floor(math.log10(lepes)))) if lepes < 1 else 1
    return tized(v, j)


def _yskala(bal, jobb, fent, lent, w, h, ymin, ymax, lepes, felirat, ki, szazalek=False):
    py = h - fent - lent

    def Y(v):
        return fent + (ymax - v) / (ymax - ymin) * py
    v = ymin
    while v <= ymax + 1e-9:
        ki.append(f'  <line x1="{bal}" y1="{Y(v):.1f}" x2="{w - jobb}" y2="{Y(v):.1f}" stroke="{RACS}" '
                  f'stroke-width=".7"/>')
        c = _szamcimke(v, lepes) + ("%" if szazalek else "")
        ki.append(_t(bal - 5, Y(v) + 3.8, c, 10.5, SZURKE, "end"))
        v += lepes
    ki.append(f'  <line x1="{bal}" y1="{fent}" x2="{bal}" y2="{h - lent}" stroke="{TINTA}" stroke-width="1.2"/>')
    ki.append(f'  <line x1="{bal}" y1="{h - lent}" x2="{w - jobb}" y2="{h - lent}" stroke="{TINTA}" '
              f'stroke-width="1.2"/>')
    if felirat:
        ki.append(_t(bal - 2, fent - 5, felirat, 10.5, SZURKE, "start", extra=' font-style="italic"'))
    return Y


# ------------------------------------------------------------------ oszlopdiagram
def svg_oszlop(cimkek, ertekek, *, ymax, lepes, ymin=0, yfelirat="", xfelirat="", ertek_cimkek=None,
               kiemel=(), w=460, h=250, leiras="Oszlopdiagram", szin=KEK, szazalek=False):
    """Függőleges oszlopdiagram kategóriákra (vagy diszkrét értékekre). `ertek_cimkek` = az oszlopok fölé írt
    szövegek (None: a számérték). `kiemel` = a kiemelt oszlopok indexei (zöld). `ymin` > 0 → levágott tengely
    (ezt csak a félrevezető ábra bemutatásához használjuk)."""
    bal, jobb, fent, lent = 52, 10, 22, 40 if xfelirat else 26
    ki = []
    Y = _yskala(bal, jobb, fent, lent, w, h, ymin, ymax, lepes, yfelirat, ki, szazalek)
    n = len(ertekek)
    hely = (w - bal - jobb) / n
    sz = hely * 0.62
    for i, (c, v) in enumerate(zip(cimkek, ertekek)):
        x = bal + hely * i + (hely - sz) / 2
        szn = ZOLD if i in kiemel else szin
        y = Y(max(v, ymin))
        ki.append(f'  <rect x="{x:.1f}" y="{y:.1f}" width="{sz:.1f}" height="{Y(ymin) - y:.1f}" fill="{szn}" '
                  f'fill-opacity=".85"/>')
        ec = ertek_cimkek[i] if ertek_cimkek else (ezres(v) if abs(v - round(v)) < 1e-9 else tized(v, 2))
        ki.append(_t(x + sz / 2, y - 4, ec, 10.5, TINTA, "middle", True))
        ki.append(_t(x + sz / 2, h - lent + 14, c, 11, TINTA))
    if xfelirat:
        ki.append(_t((bal + w - jobb) / 2, h - 7, xfelirat, 10.5, SZURKE, extra=' font-style="italic"'))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ hisztogram
def svg_hisztogram(hatarok, gyak, *, ymax, lepes, xcimkek=None, yfelirat="", xfelirat="", w=480, h=250,
                   leiras="Hisztogram", szin=KEK):
    """Egymáshoz simuló oszlopok osztályközökre. `hatarok` = n+1 osztályhatár, `gyak` = n gyakoriság.
    `xcimkek` = {határ-index: felirat} — alapértelmezés: minden határ a számértékével."""
    bal, jobb, fent, lent = 56, 12, 22, 40 if xfelirat else 26
    ki = []
    Y = _yskala(bal, jobb, fent, lent, w, h, 0, ymax, lepes, yfelirat, ki)
    x0, x1 = hatarok[0], hatarok[-1]
    px = w - bal - jobb

    def X(v):
        return bal + (v - x0) / (x1 - x0) * px
    for a, b, g in zip(hatarok, hatarok[1:], gyak):
        ki.append(f'  <rect x="{X(a):.1f}" y="{Y(g):.1f}" width="{X(b) - X(a):.1f}" height="{Y(0) - Y(g):.1f}" '
                  f'fill="{szin}" fill-opacity=".8" stroke="#ffffff" stroke-width=".8"/>')
    cimkek = xcimkek if xcimkek is not None else {i: ezres(v) for i, v in enumerate(hatarok)}
    for i, c in cimkek.items():
        xv = X(hatarok[i])
        ki.append(f'  <line x1="{xv:.1f}" y1="{h - lent}" x2="{xv:.1f}" y2="{h - lent + 4}" stroke="{TINTA}"/>')
        ki.append(_t(xv, h - lent + 15, c, 10.5, TINTA))
    if xfelirat:
        ki.append(_t((bal + w - jobb) / 2, h - 7, xfelirat, 10.5, SZURKE, extra=' font-style="italic"'))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ kördiagram
def svg_kor(cimkek, ertekek, *, szazalekok=None, szinek=None, w=440, h=220, leiras="Kördiagram"):
    """Kördiagram jelmagyarázattal; a jelmagyarázatban a darabszám és a százalék is ott áll (nem csak a szín)."""
    szinek = szinek or KOR_SZINEK
    ossz = sum(ertekek)
    cx, cy, r = 112, h / 2, min(h / 2 - 14, 96)
    ki = []
    szog = -math.pi / 2
    for i, v in enumerate(ertekek):
        d = 2 * math.pi * v / ossz
        x1, y1 = cx + r * math.cos(szog), cy + r * math.sin(szog)
        x2, y2 = cx + r * math.cos(szog + d), cy + r * math.sin(szog + d)
        nagy = 1 if d > math.pi else 0
        ki.append(f'  <path d="M{cx:.1f},{cy:.1f} L{x1:.1f},{y1:.1f} A{r},{r} 0 {nagy},1 {x2:.1f},{y2:.1f} Z" '
                  f'fill="{szinek[i % len(szinek)]}" stroke="#ffffff" stroke-width="1.5"/>')
        szog += d
    szaz = szazalekok or [tized(100 * v / ossz, 1) + "%" for v in ertekek]
    for i, (c, v) in enumerate(zip(cimkek, ertekek)):
        y = cy - (len(ertekek) - 1) * 13 + i * 26
        ki.append(f'  <rect x="{cx + r + 22}" y="{y - 9:.1f}" width="13" height="13" rx="2" '
                  f'fill="{szinek[i % len(szinek)]}"/>')
        ki.append(_t(cx + r + 42, y + 2, f"{c}: {ezres(v)} ({szaz[i]})", 11.5, TINTA, "start"))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ vonaldiagram
def svg_vonal(xek, yok, *, ymin, ymax, lepes, yfelirat="", xfelirat="", pont_cimkek=None, w=480, h=250,
              leiras="Vonaldiagram", szin=KEK):
    """Idősor vonaldiagramja; a vízszintes tengelyen az x-értékek arányos távolságra (pl. népszámlálási évek)."""
    bal, jobb, fent, lent = 60, 16, 22, 40 if xfelirat else 26
    ki = []
    Y = _yskala(bal, jobb, fent, lent, w, h, ymin, ymax, lepes, yfelirat, ki)
    x0, x1 = xek[0], xek[-1]
    px = w - bal - jobb - 12

    def X(v):
        return bal + 6 + (v - x0) / (x1 - x0) * px
    d = " ".join(("M" if i == 0 else "L") + f"{X(x):.1f},{Y(y):.1f}" for i, (x, y) in enumerate(zip(xek, yok)))
    ki.append(f'  <path d="{d}" fill="none" stroke="{szin}" stroke-width="2.2" stroke-linejoin="round"/>')
    for i, (x, y) in enumerate(zip(xek, yok)):
        ki.append(f'  <circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3.6" fill="{szin}"/>')
        ki.append(_t(X(x), h - lent + 14, str(x), 10, TINTA))
        if pont_cimkek and pont_cimkek[i]:
            horgony = "start" if i == 0 else ("end" if i == len(xek) - 1 else "middle")
            ki.append(_t(X(x) + (4 if i == 0 else -4 if i == len(xek) - 1 else 0), Y(y) - 8, pont_cimkek[i], 10,
                         TINTA, horgony, True))
    if xfelirat:
        ki.append(_t((bal + w - jobb) / 2, h - 7, xfelirat, 10.5, SZURKE, extra=' font-style="italic"'))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ dobozdiagram
def _tengely_x(lo, hi):
    if hi - lo < 1e-9:
        lo, hi = lo - 1, hi + 1
    lep = _szep_lepes(hi - lo, 6)
    a = math.floor(lo / lep) * lep
    b = math.ceil(hi / lep) * lep
    return a, b, lep


def svg_doboz(sorok, *, xfelirat="", w=480, h=None, leiras="Dobozdiagram", tengely=None):
    """Vízszintes dobozdiagramok közös tengelyen: min · Q1 · medián · Q3 · max, mögöttük az adatpontok.
    `sorok` = [(név, adatok), …]."""
    h = h or 60 + 62 * len(sorok)
    bal, jobb = 86, 16
    minden = [v for _, a in sorok for v in a]
    a, b, lep = tengely or _tengely_x(min(minden), max(minden))
    px = w - bal - jobb

    def X(v):
        return bal + (v - a) / (b - a) * px
    ki = []
    ty = h - 34
    v = a
    while v <= b + 1e-9:
        ki.append(f'  <line x1="{X(v):.1f}" y1="14" x2="{X(v):.1f}" y2="{ty}" stroke="{RACS}" stroke-width=".7"/>')
        ki.append(_t(X(v), ty + 15, _szamcimke(v, lep), 10.5, SZURKE))
        v += lep
    ki.append(f'  <line x1="{bal}" y1="{ty}" x2="{w - jobb}" y2="{ty}" stroke="{TINTA}" stroke-width="1.2"/>')
    for i, (nev, adat) in enumerate(sorok):
        m = mutatok(adat)
        cy = 40 + i * 62
        szn = [KEK, BOR, ZOLD][i % 3]
        ki.append(_t(bal - 8, cy + 4, nev, 12, TINTA, "end", True))
        for vv in adat:
            ki.append(f'  <circle cx="{X(vv):.1f}" cy="{cy - 19}" r="3" fill="{szn}" fill-opacity=".55"/>')
        ki.append(f'  <line x1="{X(m["min"]):.1f}" y1="{cy}" x2="{X(m["q1"]):.1f}" y2="{cy}" stroke="{TINTA}" '
                  f'stroke-width="1.4"/>')
        ki.append(f'  <line x1="{X(m["q3"]):.1f}" y1="{cy}" x2="{X(m["max"]):.1f}" y2="{cy}" stroke="{TINTA}" '
                  f'stroke-width="1.4"/>')
        for vv in (m["min"], m["max"]):
            ki.append(f'  <line x1="{X(vv):.1f}" y1="{cy - 7}" x2="{X(vv):.1f}" y2="{cy + 7}" stroke="{TINTA}" '
                      f'stroke-width="1.4"/>')
        ki.append(f'  <rect x="{X(m["q1"]):.1f}" y="{cy - 12}" width="{X(m["q3"]) - X(m["q1"]):.1f}" height="24" '
                  f'fill="{szn}" fill-opacity=".22" stroke="{szn}" stroke-width="1.6"/>')
        ki.append(f'  <line x1="{X(m["median"]):.1f}" y1="{cy - 12}" x2="{X(m["median"]):.1f}" y2="{cy + 12}" '
                  f'stroke="{TINTA}" stroke-width="2.4"/>')
    if xfelirat:
        ki.append(_t((bal + w - jobb) / 2, h - 5, xfelirat, 10.5, SZURKE, extra=' font-style="italic"'))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ mozaikábra (kétdimenziós táblázat)
def svg_mozaik(oszlopok, sor_nevek, *, w=460, h=250, leiras="Mozaikábra"):
    """`oszlopok` = [(név, [a, b]), …]: az oszlop szélessége a csoport méretével, a sávok magassága a csoporton belüli
    aránnyal arányos. A felső sáv (a) zöld, az alsó (b) szürke; minden sávban szám és százalék is áll."""
    bal, jobb, fent, lent = 16, 16, 26, 40
    ossz = sum(sum(v) for _, v in oszlopok)
    px, py = w - bal - jobb - 8 * (len(oszlopok) - 1), h - fent - lent
    ki = []
    x = bal
    for nev, (a, b) in oszlopok:
        cs = a + b
        sz = px * cs / ossz
        ha = py * a / cs
        ki.append(f'  <rect x="{x:.1f}" y="{fent}" width="{sz:.1f}" height="{ha:.1f}" fill="{ZOLD}" '
                  f'fill-opacity=".8"/>')
        ki.append(f'  <rect x="{x:.1f}" y="{fent + ha:.1f}" width="{sz:.1f}" height="{py - ha:.1f}" fill="{HALV}" '
                  f'fill-opacity=".55"/>')
        ki.append(_t(x + sz / 2, fent + ha / 2 + 4, f"{sor_nevek[0]}: {ezres(a)} ({tized(100 * a / cs, 1)}%)",
                     11, "#ffffff" if ha > 18 else TINTA, "middle", True))
        ki.append(_t(x + sz / 2, fent + ha + (py - ha) / 2 + 4,
                     f"{sor_nevek[1]}: {ezres(b)} ({tized(100 * b / cs, 1)}%)", 11, TINTA, "middle", True))
        ki.append(_t(x + sz / 2, h - lent + 16, f"{nev} ({ezres(cs)} fő)", 11.5, TINTA, "middle", True))
        x += sz + 8
    ki.append(_t(w / 2, 15, "az oszlop szélessége ~ a csoport mérete, a sáv magassága ~ az arány a csoporton belül",
                 10, SZURKE, extra=' font-style="italic"'))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ Bernoulli-fa
def svg_bernoulli_fa(p_jel="0,8", q_jel="0,2", siker="S", kudarc="K", kiemel_k=2, w=480, h=270,
                     leiras="Fadiagram három Bernoulli-kísérlethez"):
    """Három egymás utáni, független kísérlet fája (8 ág). A pontosan `kiemel_k` sikert tartalmazó ágak zöldek."""
    ki = []
    xs = [30, 140, 250, 360]
    levelek = []

    def ag(szint, y, ut, felso, also):
        if szint == 3:
            levelek.append((y, ut))
            return
        dy = [64, 32, 16][szint]
        for jel, pj, yy in ((siker, p_jel, y - dy), (kudarc, q_jel, y + dy)):
            uj = ut + jel
            k = uj.count(siker)
            kiem = szint == 2 and k == kiemel_k
            szin = ZOLD if kiem else TINTA
            ki.append(f'  <line x1="{xs[szint] + 5}" y1="{y:.1f}" x2="{xs[szint + 1] - 6}" y2="{yy:.1f}" '
                      f'stroke="{szin}" stroke-width="{2.2 if kiem else 1.2}"/>')
            ki.append(_t((xs[szint] + xs[szint + 1]) / 2, (y + yy) / 2 - 4 if jel == siker else (y + yy) / 2 + 11,
                         pj, 9.5, SZURKE))
            ki.append(_t(xs[szint + 1], yy + 4, jel, 11.5, ZOLD if jel == siker else PIROS, "middle", True))
            ag(szint + 1, yy, uj, felso, also)
    ki.append(f'  <circle cx="{xs[0]}" cy="{h / 2 - 8:.1f}" r="5" fill="{TINTA}"/>')
    ag(0, h / 2 - 8, "", 0, 0)
    for y, ut in levelek:
        k = ut.count(siker)
        kiem = k == kiemel_k
        tag = "·".join((p_jel if c == siker else q_jel) for c in ut)
        ki.append(_t(xs[3] + 16, y + 4, f"{ut}: {tag}", 10.5, ZOLD if kiem else TINTA, "start", kiem))
    for i, nev in enumerate(("1. dobás", "2. dobás", "3. dobás")):
        ki.append(_t(xs[i + 1], h - 6, nev, 10, SZURKE))
    return _svg(w, h, leiras, ki)


# ------------------------------------------------------------------ interaktív: érme- és kockaszimulátor
SZIM_TIPUS = {"erme": (0.5, "1/2", "fej", "Érmedobás"), "kocka": (1 / 6, "1/6", "hatos", "Kockadobás")}
_SZ_W, _SZ_H, _SZ_B, _SZ_J, _SZ_F, _SZ_L = 420, 230, 44, 14, 12, 30


def _szep_max(n):
    h = 10
    while True:
        for m in (1, 2, 5):
            if m * h >= n:
                return m * h
        h *= 10


def szim_kijelzo(tipus, n, k):
    p, jel, siker, nev = SZIM_TIPUS[tipus]
    if n == 0:
        return f"{nev}: még nincs dobás. Nyomd meg a gombokat!"
    return (f"{nev}: {ezres(n)} dobás, ebből {ezres(k)} {siker} — a relatív gyakoriság {ezres(k)}/{ezres(n)} ≈ "
            f"{tized(k / n, 3)}. A klasszikus valószínűség {jel} ≈ {tized(p, 3)}.")


def svg_szimulacio(kezdo_dobas=200, mag=2026, felirat="", leiras="Érme- és kockaszimulátor: a relatív gyakoriság a "
                   "dobások számának függvényében"):
    """Interaktív szimulátor (`data-mod="szimulacio"`). A statikus kép egy beégetett, `kezdo_dobas` hosszú
    érmedobás-sorozat (rögzített maggal) — ugyanazt rajzolja a JS is betöltéskor, és onnan folytatja."""
    _IV_SZAMLALO[0] += 1
    nn = _IV_SZAMLALO[0]
    rnd = random.Random(mag)
    sor = "".join("1" if rnd.random() < 0.5 else "0" for _ in range(kezdo_dobas))
    w, h, B, J, F, L = _SZ_W, _SZ_H, _SZ_B, _SZ_J, _SZ_F, _SZ_L
    px, py = w - B - J, h - F - L

    def Y(v):
        return F + (1 - v) * py
    n, k, rel = 0, 0, []
    for c in sor:
        n += 1
        k += c == "1"
        rel.append(k / n)
    mx = _szep_max(max(n, 10))
    m = min(n, 400)
    d = []
    for i in range(m):
        idx = (i + 1) * n // m - 1
        d.append(("L" if i else "M") + f"{B + (idx + 1) / mx * px:.1f},{Y(rel[idx]):.1f}")
    ki = []
    for v, c in ((0, "0"), (0.25, "0,25"), (0.5, "0,5"), (0.75, "0,75"), (1, "1")):
        ki.append(f'  <line x1="{B}" y1="{Y(v):.1f}" x2="{w - J}" y2="{Y(v):.1f}" stroke="{RACS}" stroke-width=".7"/>')
        ki.append(_t(B - 6, Y(v) + 3.8, c, 10.5, SZURKE, "end"))
    ki.append(f'  <line x1="{B}" y1="{F}" x2="{B}" y2="{h - L}" stroke="{TINTA}" stroke-width="1.2"/>')
    ki.append(f'  <line x1="{B}" y1="{h - L}" x2="{w - J}" y2="{h - L}" stroke="{TINTA}" stroke-width="1.2"/>')
    for i in range(5):
        xv = B + px * i / 4
        ki.append(f'  <line x1="{xv:.1f}" y1="{h - L}" x2="{xv:.1f}" y2="{h - L + 4}" stroke="{TINTA}"/>')
        ki.append(f'  <text class="iv-szim-xt" x="{xv:.1f}" y="{h - L + 15}" font-size="10.5" fill="{SZURKE}" '
                  f'text-anchor="middle">{ezres(mx * i / 4)}</text>')
    ki.append(_t(w - J, h - 3, "dobások száma", 10, SZURKE, "end", extra=' font-style="italic"'))
    ki.append(_t(w - J - 4, F + 11, "relatív gyakoriság", 10, SZURKE, "end", extra=' font-style="italic"'))
    ki.append(f'  <line class="iv-szim-cel" x1="{B}" y1="{Y(0.5):.1f}" x2="{w - J}" y2="{Y(0.5):.1f}" '
              f'stroke="{PIROS}" stroke-width="1.4" stroke-dasharray="6 4"/>')
    ki.append(f'  <text class="iv-szim-cel-cimke" x="{w - J - 4}" y="{Y(0.5) - 4:.1f}" font-size="11" fill="{PIROS}" '
              f'text-anchor="end" font-weight="600">1/2</text>')
    ki.append(f'  <path class="iv-szim-gorbe" d="{" ".join(d)}" fill="none" stroke="{KEK}" stroke-width="1.8" '
              f'stroke-linejoin="round"/>')
    svg = _svg(w, h, leiras, ki)
    gombok = "".join(f'<button type="button" data-db="{db}">+{ezres(db)}</button>' for db in (1, 10, 100, 1000))
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return (f'<div class="svgcard interaktiv" data-mod="szimulacio" data-w="{w}" data-h="{h}" data-sor="{sor}">\n'
            f'{svg}\n'
            f'<div class="iv-vezerlo iv-gombsor"><label for="iv{nn}">Kísérlet:</label>'
            f'<select id="iv{nn}" class="iv-szim-tipus"><option value="erme">érmedobás — fej</option>'
            f'<option value="kocka">kockadobás — hatos</option></select>{gombok}'
            f'<button type="button" class="iv-szim-ujra">Újra</button></div>\n'
            f'<p class="iv-kijelzo" aria-live="polite">{szim_kijelzo("erme", n, k)}</p>\n</div>{cap}\n'
            f'<script src="../../assets/js/interaktiv.js"></script>')


# ------------------------------------------------------------------ interaktív: adatlabor
_AL_W, _AL_H = 440, 150
_AL_SOROK = [("n", "elemszám (n)"), ("atlag", "átlag"), ("median", "medián"), ("modusz", "módusz"),
             ("terjedelem", "terjedelem"), ("q1", "alsó kvartilis (Q₁)"), ("q3", "felső kvartilis (Q₃)"),
             ("iqr", "interkvartilis terjedelem"), ("aae", "átlagos abszolút eltérés"),
             ("var", "szórásnégyzet (σ²)"), ("sz", "szórás (σ)")]


def _al_ertekek(m):
    return {"n": str(m["n"]), "atlag": _fmt(m["atlag"]), "median": _fmt(m["median"]), "modusz": modusz_szoveg(m),
            "terjedelem": _fmt(m["max"] - m["min"]), "q1": _fmt(m["q1"]), "q3": _fmt(m["q3"]),
            "iqr": _fmt(m["q3"] - m["q1"]), "aae": _fmt(m["aae"]), "var": _fmt(m["var"]), "sz": _fmt(m["sz"])}


def _al_rajz(adat):
    """A pontdiagram + dobozdiagram statikus képe — ugyanaz, amit az interaktiv.js `adatlabor` módja rajzol."""
    w, h, bal, jobb = _AL_W, _AL_H, 20, 20
    m = mutatok(adat)
    a, b, lep = _tengely_x(m["min"], m["max"])
    px = w - bal - jobb

    def X(v):
        return bal + (v - a) / (b - a) * px
    gy = {}
    for v in m["s"]:
        gy[v] = gy.get(v, 0) + 1
    maxst = max(gy.values())
    koz = min(8.0, 52.0 / maxst)
    pontok = []
    hanyadik = {}
    for v in m["s"]:
        j = hanyadik.get(v, 0)
        hanyadik[v] = j + 1
        pontok.append(f'<circle cx="{X(v):.1f}" cy="{66 - j * koz:.1f}" r="4" fill="{KEK}" fill-opacity=".7"/>')
    tk = []
    v = a
    while v <= b + 1e-9:
        tk.append(f'<line x1="{X(v):.1f}" y1="118" x2="{X(v):.1f}" y2="122" stroke="{TINTA}"/>'
                  f'<text x="{X(v):.1f}" y="136" font-size="10.5" fill="{SZURKE}" text-anchor="middle">'
                  f'{_fmt(v)}</text>')
        v += lep
    cy = 96
    ki = [f'  <g class="iv-al-pontok">{"".join(pontok)}</g>',
          f'  <line x1="{bal}" y1="118" x2="{w - jobb}" y2="118" stroke="{TINTA}" stroke-width="1.2"/>',
          f'  <g class="iv-al-tengely">{"".join(tk)}</g>',
          f'  <line class="iv-al-bajusz1" x1="{X(m["min"]):.1f}" y1="{cy}" x2="{X(m["q1"]):.1f}" y2="{cy}" '
          f'stroke="{TINTA}" stroke-width="1.4"/>',
          f'  <line class="iv-al-bajusz2" x1="{X(m["q3"]):.1f}" y1="{cy}" x2="{X(m["max"]):.1f}" y2="{cy}" '
          f'stroke="{TINTA}" stroke-width="1.4"/>',
          f'  <line class="iv-al-min" x1="{X(m["min"]):.1f}" y1="{cy - 7}" x2="{X(m["min"]):.1f}" y2="{cy + 7}" '
          f'stroke="{TINTA}" stroke-width="1.4"/>',
          f'  <line class="iv-al-max" x1="{X(m["max"]):.1f}" y1="{cy - 7}" x2="{X(m["max"]):.1f}" y2="{cy + 7}" '
          f'stroke="{TINTA}" stroke-width="1.4"/>',
          f'  <rect class="iv-al-doboz" x="{X(m["q1"]):.1f}" y="{cy - 11}" width="{X(m["q3"]) - X(m["q1"]):.1f}" '
          f'height="22" fill="{KEK}" fill-opacity=".2" stroke="{KEK}" stroke-width="1.6"/>',
          f'  <line class="iv-al-me" x1="{X(m["median"]):.1f}" y1="{cy - 11}" x2="{X(m["median"]):.1f}" '
          f'y2="{cy + 11}" stroke="{TINTA}" stroke-width="2.4"/>',
          f'  <line class="iv-al-atl" x1="{X(m["atlag"]):.1f}" y1="{cy - 15}" x2="{X(m["atlag"]):.1f}" '
          f'y2="{cy + 15}" stroke="{PIROS}" stroke-width="1.6" stroke-dasharray="4 3"/>']
    return ki, m


def hu_lista(adat):
    return "; ".join(_fmt(v) for v in adat)


def svg_adatlabor(adatsorok, kezdo=0, felirat="", leiras="Adatlabor: pontdiagram és dobozdiagram, élő mutatókkal"):
    """Interaktív adatlabor (`data-mod="adatlabor"`). `adatsorok` = [(név, [értékek]), …]; az utolsó opció
    „saját adatok". A statikus kép és a mutatótábla a `kezdo` adatsoré (JS nélkül is értelmes)."""
    _IV_SZAMLALO[0] += 1
    nn = _IV_SZAMLALO[0]
    nev0, adat0 = adatsorok[kezdo]
    ki, m = _al_rajz(adat0)
    svg = _svg(_AL_W, _AL_H, leiras, ki)
    opciok = "".join(
        f'<option value="{i}" data-ertekek="{",".join(repr(float(v)) for v in a)}"'
        f'{" selected" if i == kezdo else ""}>{escape(n)}</option>' for i, (n, a) in enumerate(adatsorok))
    opciok += '<option value="sajat" data-ertekek="">saját adatok</option>'
    ert = _al_ertekek(m)
    sorok = "".join(f'<tr><th scope="row">{c}</th><td data-m="{k}">{ert[k]}</td></tr>' for k, c in _AL_SOROK)
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return (f'<div class="svgcard interaktiv adatlabor" data-mod="adatlabor" data-w="{_AL_W}" data-h="{_AL_H}">\n'
            f'<div class="iv-vezerlo"><label for="iv{nn}">Adatsor:</label><select id="iv{nn}" class="iv-al-valaszt">'
            f'{opciok}</select></div>\n'
            f'<label class="iv-al-cimke" for="iva{nn}">Adatok (szóközzel vagy pontosvesszővel elválasztva; '
            f'tizedesvessző is jó):</label>\n'
            f'<textarea id="iva{nn}" class="iv-al-adat" rows="2" spellcheck="false">{hu_lista(adat0)}</textarea>\n'
            f'{svg}\n'
            f'<p class="iv-kijelzo" aria-live="polite">Kék pontok: az adatok · doboz: Q₁–Q₃, benne a medián · piros '
            f'szaggatott vonal: az átlag.</p>\n'
            f'<table class="iv-tabla"><caption>{escape(nev0)}</caption>{sorok}</table>\n</div>{cap}\n'
            f'<script src="../../assets/js/interaktiv.js"></script>')
