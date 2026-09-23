# -*- coding: utf-8 -*-
"""4e/01 — B es C blokk (2. resz): az e szam (B3), a vegtelen mertani sor (C).
Mentor: Ved Vilmos (Nagol javit). Kuldetes: A Vegtelenbe es... Ne Tovabb!
Specifikacio: projektek/4e/munkafajlok/narrativa_01-sorozatok-hatarerteke.md"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="4e", mappa="01-sorozatok-hatarerteke", temakor="Sorozatok határértéke")
FGY = "feladatok-hatarertek.html"
KUL = "A Végtelenbe és… Ne Tovább!"
E306 = "../../3e/06-indukcio-sorozatok/"
ZOLD, BORO = "#047857", "#f59e0b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FGY}#nehez-{tol}">Zsoldos-lista, nehéz {tol}–{ig}</a>.</p>')


# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, symbols, limit, oo, exp, E as EE, simplify, N
HIBA = []


def chk(nev, kapott, vart, tol=None):
    if tol is not None:
        ok = all(abs(float(a) - b) < tol for a, b in zip(kapott, vart))
    elif isinstance(kapott, (list, tuple)):
        ok = len(kapott) == len(vart) and all(a == b or simplify(a - b) == 0 for a, b in zip(kapott, vart))
    else:
        ok = kapott == vart or simplify(kapott - vart) == 0
    if not ok:
        HIBA.append((nev, kapott, vart))


n = symbols("n", positive=True, integer=True)
L = lambda e: limit(e, n, oo)
e_n = lambda k: (1 + R(1, k))**k
chk("B3-burek-bank", [e_n(k) for k in (1, 2, 4, 12, 365, 10000)],
    [2, 2.25, 2.4414, 2.6130, 2.7146, 2.7181], tol=6e-5)
chk("B3-pontok", [e_n(k) for k in range(1, 9)],
    [2, 2.25, 2.3704, 2.4414, 2.4883, 2.5216, 2.5465, 2.5658], tol=6e-5)
chk("B3-e", L((1 + 1/n)**n), EE)
chk("B3-e-kozelito", [N(EE, 6)], [2.71828], tol=1e-5)
chk("B3-alap-pelda", L((1 + 2/n)**(4*n)), exp(8))
chk("B3-kozep-pelda-b", L((1 - 3/n)**(2*n)), exp(-6))
chk("B3-kozep-pelda-c", L((1 + 4/n)**(n/2)), exp(2))
chk("B3-kviz-2", L((1 + 3/n)**(2*n)), exp(6))
chk("B3-eltolt", L((1 + 4/(n + 3))**(3*n)), exp(12))
chk("B3-eltolt-kitevo", L(12*n/(n + 3)), 12)
chk("B3-hanyados-atiras", simplify((2*n + 5)/(2*n - 1) - (1 + 6/(2*n - 1))), 0)
chk("B3-hanyados", L(((2*n + 5)/(2*n - 1))**n), exp(3))
chk("B3-hanyados-kitevo", L(6*n/(2*n - 1)), 3)
chk("B3-nem-1-vegtelen", L(((5*n + 1)/(2*n))**n), oo)
chk("B3-nem-1-nulla", L((n/(3*n + 1))**n), 0)
chk("B3-nem-1-egy", L((1 + n/(n + 1))**(1/n)), 1)
chk("B3-kviz-3", L((1 + n/(n + 1))**n), oo)
# C
S = lambda b1, q, k: sum(b1 * q**j for j in range(k))
chk("C-motor", [S(1, R(1, 2), k) for k in range(1, 6)], [1, R(3, 2), R(7, 4), R(15, 8), R(31, 16)])
chk("C-motor-S", 1 / (1 - R(1, 2)), 2)
chk("C-kettes-formalis", 1 / (1 - 2), -1)
chk("C-kviz-2", 8 / (1 - R(-3, 4)), R(32, 7))
chk("C-inga-tagok", [64 * R(3, 4)**j for j in range(4)], [64, 48, 36, 27])
chk("C-inga-S", 64 / (1 - R(3, 4)), 256)
chk("C-szakaszos-4", R(4, 10) / (1 - R(1, 10)), R(4, 9))
chk("C-szakaszos-27", R(27, 100) / (1 - R(1, 100)), R(3, 11))
chk("C-szakaszos-9", R(9, 10) / (1 - R(1, 10)), 1)
chk("C-negyzet", S(R(1, 2), R(1, 2), 6), R(63, 64))
assert not HIBA, HIBA
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_E = svg_fuggvenyek(
    [(lambda x: 2.718281828, ZOLD, "", [(0, 9)])], xr=(0, 9), yr=(0, 3.3), w=380, h=240,
    jelmagyarazat=False, tengely=("n", "aₙ"),
    leiras="Az (1 + 1/n)ⁿ sorozat első nyolc tagja pontokként, alulról egyre közelebb az "
           "y = e ≈ 2,718 vízszintes egyeneshez, de egyik sem éri el",
    pontok=[(k, float(e_n(k)), "", BORO) for k in range(1, 9)])
SVG_E = SVG_E.replace("</svg>", '  <text x="364" y="45" font-size="11" fill="#047857" '
                      'text-anchor="end">e ≈ 2,718</text>\n</svg>')


def svg_negyzet():
    """Az egységnégyzet felezése: 1/2 + 1/4 + 1/8 + … = 1 (sötét vonal, világos lap)."""
    s, x0, y0 = 220, 12, 12
    szinek = ["#d1fae5", "#a7f3d0", "#6ee7b7", "#34d399", "#10b981", "#059669"]
    cimkek = ["1/2", "1/4", "1/8", "1/16", "", ""]
    x, y, w, h = 0.0, 0.0, 1.0, 1.0
    ki = [f'<svg viewBox="0 0 {s + 2 * x0} {s + 2 * y0}" width="{s + 2 * x0}" height="{s + 2 * y0}" '
          'role="img" aria-label="Egy egységnyi négyzetet ismételten megfelezünk: a darabok területe '
          '1/2, 1/4, 1/8, 1/16 és így tovább, együtt kitöltik az egész négyzetet">']
    for i in range(6):
        if i % 2 == 0:      # függőleges vágás: a bal fél
            rx, ry, rw, rh = x, y, w / 2, h
            x, w = x + w / 2, w / 2
        else:               # vízszintes vágás: a felső fél
            rx, ry, rw, rh = x, y, w, h / 2
            y, h = y + h / 2, h / 2
        ki.append(f'  <rect x="{x0 + rx * s:.1f}" y="{y0 + ry * s:.1f}" width="{rw * s:.1f}" '
                  f'height="{rh * s:.1f}" fill="{szinek[i]}" stroke="#0f172a" stroke-width="1.2"/>')
        if cimkek[i]:
            fs = 20 - 3 * i
            ki.append(f'  <text x="{x0 + (rx + rw / 2) * s:.1f}" y="{y0 + (ry + rh / 2) * s + fs / 3:.1f}" '
                      f'font-size="{fs}" fill="#0f172a" text-anchor="middle">{cimkek[i]}</text>')
    ki.append(f'  <rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="none" stroke="#0f172a" '
              'stroke-width="1.8"/>')
    ki.append('</svg>')
    return "\n".join(ki)


SVG_NEGYZET = svg_negyzet()

# ---------------------------------------------------------------- B3
B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Megnyitottam a Burek-bankot. Aki betesz 1 dinárt, egy év múlva '
         '100% kamatot kap, vagyis 2 dinárja lesz. 🌮 <i>Burek-matek:</i> „ha a kamatot kétszer '
         'írom jóvá, félévente 50%-ot, még többet ér — ha pedig végtelen sokszor, végtelen gazdag '
         'leszek!” <b>Nagol:</b> Többet ér, az igaz. Végtelen gazdag viszont senki sem lesz: az '
         'összeg egy nevezetes számhoz tart, amelyet ma megismerünk.'),
 ]),

 ("$\\left(1+\\frac1n\\right)^n$ — táblázatból", [
   r'<p class="lead">A Burek-bank számlája $n$ jóváírás után $\left(1+\frac1n\right)^n$ dinár: '
   r'minden alkalommal $\frac1n$-ed résznyi kamat jár (lásd a '
   r'<a href="' + E306 + r'tananyag-mertani-sorozat.html#tetel-kamatos-kamat">kamatos kamat képletét</a>).</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>jóváírás</th><td>évente</td><td>félévente</td><td>negyedévente</td><td>havonta</td>'
   r'<td>naponta</td><td>$10\,000$-szer</td></tr>'
   r'<tr><th>$n$</th><td>1</td><td>2</td><td>4</td><td>12</td><td>365</td><td>$10\,000$</td></tr>'
   r'<tr><th>$\left(1+\frac1n\right)^n$</th><td>$2$</td><td>$2{,}25$</td><td>$\approx2{,}4414$</td>'
   r'<td>$\approx2{,}6130$</td><td>$\approx2{,}7146$</td><td>$\approx2{,}7181$</td></tr></table></div>'
   r'<p>Az összeg nő, de egyre lassabban, és egy $2{,}718$ körüli értéknél „megtorpan”.</p>',
   abra(SVG_E, 'Az $\\left(1+\\frac1n\\right)^n$ sorozat első nyolc tagja alulról közelít az $e$ '
        'szintjéhez (zöld vonal), de egyik tag sem éri el.'),
   doboz("definicio", "Az $e$ szám",
         r'$$e=\lim_{n\to\infty}\left(1+\frac1n\right)^n\approx2{,}71828 .$$'
         r'<p>Az $e$ irracionális szám, ugyanolyan fontos, mint a $\pi$. A tanterv szerint a határérték '
         r'létezését nem bizonyítjuk — a táblázat és a grafikon szemlélteti.</p>', hid="def-e"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„Az alap $1$-hez tart, és $1$ akárhányadik hatványa $1$. Tehát a határérték $1$” — '
         r'érvel Véd Vilmos.</p>'
         r'<p>Csakhogy az alap <b>soha nem pontosan 1</b>, közben pedig a kitevő a végtelenbe nő. Két '
         r'folyamat húz ellentétes irányba, és ebből nem $1$, hanem $e$ jön ki. Az $1^\infty$ '
         r'<b>határozatlan alak</b>.</p>'),
   kviz(r'Mihez tart az $\left(1+\frac1n\right)^n$ sorozat?',
        [r'az $e\approx2{,}718$ számhoz', r'az $1$-hez, mert $1^\infty=1$',
         r'a $+\infty$-hez, mert a kitevő a végtelenbe tart', r'a $2$-höz, mert az első tagja $2$'], 0,
        jo="✔ Ez az e szám definíciója: a tagok (2; 2,25; 2,37; 2,44; …) egyre közelebb kerülnek a "
           "2,718…-hoz, de el nem érik.",
        nem="✘ A táblázat mutatja: 2; 2,25; 2,37; 2,44; … ≈ 2,718. Az 1^∞ nem „1”, hanem határozatlan alak — "
            "itt az eredménye e."),
 ]),

 ("Az általánosítás", [
   r'<p class="lead">A gyakorlatban ritkán áll ott pontosan $\left(1+\frac1n\right)^n$. Ha a törtben '
   r'$\frac kn$ szerepel, a kitevőben pedig $mn$, a határérték szintén $e$ valamelyik hatványa.</p>',
   doboz("tetel", "Az $e$-típusú határérték",
         r'<p>Bármely $k\ne0$ és $m$ valós számra</p>'
         r'$$\lim_{n\to\infty}\left(1+\frac kn\right)^{mn}=e^{km} .$$'
         r'<p>(Negatív $k$ esetén elég nagy $n$-re, $n\gt\lvert k\rvert$-ra az alap pozitív.) Szemléletesen: $\left(1+\frac kn\right)^{mn}=\left[\left(1+\frac{1}{n/k}\right)^{n/k}\right]^{km}$, '
         r'és a szögletes zárójelben álló kifejezés $e$-hez tart.</p>', hid="tetel-e-altalanos"),
   doboz("pelda", "I.V.H. Akták — egyenesen a képletből",
         r'<p><b>a)</b> $\lim\left(1+\dfrac2n\right)^{4n}=e^{2\cdot4}=e^8$. Ennyi az egész: a két számot '
         r'összeszorozzuk — akkor is, ha $k$ negatív vagy $m$ tört, ahogy a b) és a c) mutatja.</p>'
         r'<p><b>b)</b> $\lim\left(1-\dfrac3n\right)^{2n}$: itt $k=-3$ és $m=2$, így a határérték '
         r'$e^{-3\cdot2}=e^{-6}$.</p>'
         r'<p><b>c)</b> $\lim\left(1+\dfrac4n\right)^{n/2}$: itt $k=4$ és $m=\frac12$, így a határérték '
         r'$e^{4\cdot\frac12}=e^{2}$.</p>', hid="pelda-e-kozep"),
   kviz(r'Mennyi a $\lim\limits_{n\to\infty}\left(1+\frac3n\right)^{2n}$ határérték?',
        [r'$e^6$', r'$e^3$', r'$e^{3/2}$', r'$1$'], 0,
        jo="✔ A kitevő a két szám szorzata, azaz 6: a határérték e a hatodikon.",
        nem="✘ A képlet (1 + k/n)^(mn) → e^(km): itt k = 3 és m = 2, a kitevő szorzat, e⁶."),
 ]),

 ("Eltolt nevező és hányados-alap", [
   r'<p class="lead"><b>Ez a rész az ötösért van.</b> Ha a nevezőben nem $n$, hanem például $n+3$ áll, vagy az alap egyetlen tört, a '
   r'képlet nem használható közvetlenül. Ilyenkor az alapot $1+\frac{1}{\square}$ alakra hozzuk, és '
   r'a kitevőt úgy „javítjuk”, hogy megjelenjen benne ugyanez a $\square$.</p>',
   doboz("pelda", "I.V.H. Akták — eltolt nevező",
         r'<p>Számítsuk ki: $\lim\limits_{n\to\infty}\left(1+\dfrac{4}{n+3}\right)^{3n}$.</p>'
         r'<p>Az alap $1+\dfrac{1}{\frac{n+3}{4}}$. A kitevőt beszorozzuk és el is osztjuk '
         r'$\frac{n+3}{4}$-del:</p>'
         r'$$\left[\left(1+\frac{1}{\frac{n+3}{4}}\right)^{\frac{n+3}{4}}\right]^{\frac{4}{n+3}\cdot3n}'
         r'\ \longrightarrow\ e^{\lim\frac{12n}{n+3}}=e^{12} .$$'
         r'<p>A szögletes zárójel $e$-hez tart, a kitevő határértéke a fokszám-szabállyal $12$.</p>',
         hid="pelda-e-eltolt"),
   doboz("pelda", "I.V.H. Akták — hányados az alapban",
         r'<p>Számítsuk ki: $\lim\limits_{n\to\infty}\left(\dfrac{2n+5}{2n-1}\right)^{n}$.</p>'
         r'<p>Az alapból leválasztjuk az $1$-et: $\dfrac{2n+5}{2n-1}=\dfrac{(2n-1)+6}{2n-1}=1+\dfrac{6}{2n-1}$. '
         r'Innen ugyanúgy haladunk, mint az előbb:</p>'
         r'$$\left(1+\frac{1}{\frac{2n-1}{6}}\right)^{n}=\left[\left(1+\frac{1}{\frac{2n-1}{6}}\right)^{\frac{2n-1}{6}}\right]^{\frac{6}{2n-1}\cdot n}'
         r'\ \longrightarrow\ e^{\lim\frac{6n}{2n-1}}=e^{3} .$$',
         hid="pelda-e-hanyados"),
   NEHEZ(4, 6, "eltolt nevezős és hányados-alapú $e$-típusok"),
 ]),

 ("Nem minden hatvány $1^\\infty$", [
   r'<p class="lead">Az $e$-es módszer csak akkor jön szóba, ha az alap $1$-hez tart. Ha a kitevő a '
   r'végtelenbe tart, az alap pedig nem $1$-hez, a hatvány egyszerűen viselkedik: $1$-nél nagyobb '
   r'számhoz tartó alap a végtelenbe visz, $0$ és $1$ közötti számhoz tartó a $0$-hoz. (Ha a kitevő nem '
   r'tart a végtelenbe, mint a c)-ben, egyszerűen behelyettesítünk.)</p>',
   doboz("pelda", "I.V.H. Akták — először az alapot nézzük",
         r'<p><b>a)</b> $\lim\left(\dfrac{5n+1}{2n}\right)^{n}$: az alap $\frac52$-hez tart, és '
         r'$\left(\frac52\right)^n\to+\infty$. A határérték $+\infty$.</p>'
         r'<p><b>b)</b> $\lim\left(\dfrac{n}{3n+1}\right)^{n}$: az alap $\frac13$-hoz tart, a határérték $0$.</p>'
         r'<p><b>c)</b> $\lim\left(1+\dfrac{n}{n+1}\right)^{1/n}$: az alap $2$-höz, a kitevő $0$-hoz tart — '
         r'ez nem határozatlan alak, a határérték $2^0=1$.</p>', hid="pelda-nem-e"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos minden hatványra $e$-t ír: az a) feladatra „$e^{5/2}$”-t (mert az alap $\frac52$-höz '
         r'tart), a c)-re „$e^0$”-t. A c)-nél a végeredmény véletlenül stimmel, a gondolatmenet azonban '
         r'mindkettőnél hibás.</p>'
         r'<p><b>Az első lépés mindig: mihez tart az alap?</b> Csak ha $1$-hez, akkor van szükség az $e$-re.</p>'),
   kviz(r'Mihez tart az $\left(1+\frac{n}{n+1}\right)^{n}$ sorozat?',
        [r'a $+\infty$-hez, mert az alap $2$-höz tart',
         r'az $e$-hez, mert $\left(1+\frac1n\right)^n$-re hasonlít',
         r'az $e^{n}$-hez', r'az $1$-hez'], 0,
        jo="✔ Az n/(n + 1) tört 1-hez tart, így az alap 2-höz. Egy 1-nél nagyobb számhoz tartó alap "
           "n-edik hatványa +∞-hez tart. Ez nem 1^∞ alak.",
        nem="✘ Először az alapot nézzük meg: 1 + n/(n + 1) → 2, nem 1. Egy 2-höz tartó alap n-edik "
            "hatványa a végtelenbe tart."),
   GY(FGY + "#alap-17", "A 17–18", FGY + "#kozep-12", "K 12–15"),
   brief('<b>Véd Vilmos:</b> A kismotoros utam még mindig bánt. Végtelen sok lépés, és mégsem '
         'jutok végtelen messzire? <b>Nagol:</b> Most már ki is számoljuk, pontosan meddig jutsz: '
         'a végtelen mértani sor összege következik.', outro=True),
 ]),
]

# ---------------------------------------------------------------- C
C = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Visszaültem a kismotorra: $1$ km, aztán fél, aztán negyed… '
         '🌮 <i>Burek-matek:</i> „végtelen sok pozitív szám összege mindig végtelen”, tehát végtelen '
         'messzire jutok. <b>Nagol:</b> Tévedés, és ma ki is számoljuk: a megtett út pontosan $2$ km-hez '
         'tart. Kell hozzá a tavalyi összegképlet és a $q^n$ határértéke.'),
 ]),

 ("Az első $n$ tag összegétől a végtelen összegig", [
   r'<p class="lead">A mértani sorozat első $n$ tagjának összege '
   r'(<a href="' + E306 + r'tananyag-mertani-sorozat.html#tetel-mertani-sn">tavaly tanultuk</a>)</p>'
   r'$$S_n=b_1\cdot\frac{1-q^n}{1-q}\qquad(q\ne1).$$'
   r'<p>Ha $\lvert q\rvert\lt1$, akkor $q^n\to0$ (lásd a '
   r'<a href="tananyag-hatarertek-fogalma.html#tetel-nevezetes">nevezetes határértékeket</a>), így az '
   r'összegek sorozata a $\dfrac{b_1}{1-q}$ számhoz tart. A kismotor útjára ($b_1=1$, $q=\frac12$):</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>$n$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>'
   r'<tr><th>$S_n$</th><td>$1$</td><td>$1{,}5$</td><td>$1{,}75$</td><td>$1{,}875$</td><td>$1{,}9375$</td></tr>'
   r'</table></div><p>Az összeg a $2$-höz közelít, hiszen $\dfrac{1}{1-\frac12}=2$.</p>',
   abra(SVG_NEGYZET, 'Az egységnégyzet felezése: $\\frac12+\\frac14+\\frac18+\\frac1{16}+\\dots$ — '
        'a darabok együtt kitöltik az egész négyzetet, tehát az összeg $1$. A kismotor útja ennél $1$ km-rel '
        'több: $1+\\left(\\frac12+\\frac14+\\dots\\right)=1+1=2$ km.'),
 ]),

 ("$S=\\dfrac{b_1}{1-q}$ — és a feltétele", [
   doboz("tetel", "A végtelen mértani sor összege",
         r'<p>A végtelen mértani sor <b>összegén</b> az első $n$ tag $S_n$ összegeinek határértékét értjük: '
         r'$S=\lim\limits_{n\to\infty}S_n$.</p>'
         r'<p>Ha a mértani sorozat hányadosára $\lvert q\rvert\lt1$, akkor a tagjainak végtelen összege '
         r'(a <b>végtelen mértani sor</b> összege)</p>'
         r'$$S=b_1+b_1q+b_1q^2+\dots=\frac{b_1}{1-q} .$$'
         r'<p>Ha $\lvert q\rvert\ge1$ (és $b_1\ne0$), a sornak <b>nincs</b> véges összege.</p>',
         hid="tetel-vegtelen-mertani-sor"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a képletet mindenre ráhúzza: „$1+2+4+8+\dots=\dfrac{1}{1-2}=-1$”.</p>'
         r'<p>Pozitív számok összege nem lehet negatív. Itt $q=2$, a feltétel ($\lvert q\rvert\lt1$) nem '
         r'teljesül, az összegek sorozata a végtelenbe nő — a képlet ilyenkor <b>nem alkalmazható</b>. '
         r'A feltételt mindig előbb ellenőrizzük.</p>'),
   kviz(r'Igaz-e, hogy végtelen sok pozitív szám összege mindig végtelen?',
        [r'nem — például $\frac12+\frac14+\frac18+\dots=1$',
         r'igaz, mert minden újabb tag növeli az összeget',
         r'igaz, mert a tagok soha nem érik el a $0$-t',
         r'nem lehet eldönteni, mert a végtelenig nem tudunk összeadni'], 0,
        jo="✔ Az összeg nő, de korlátos marad: a négyzet-ábra mutatja, hogy a darabok együtt "
           "pontosan 1-et adnak.",
        nem="✘ Az összeg valóban nő, de nem feltétlenül minden határon túl: 1/2 + 1/4 + 1/8 + … "
            "a négyzet-ábrán sem lép ki az egységnégyzetből. Az összeg 1."),
   kviz(r'Melyik végtelen mértani sornak van véges összege?',
        [r'$b_1=8$, $q=-\frac34$', r'$b_1=8$, $q=\frac54$', r'$b_1=8$, $q=-1$', r'$b_1=8$, $q=1$'], 0,
        jo="✔ Csak itt teljesül |q| < 1; az összeg 8/(1 + 3/4) = 32/7.",
        nem="✘ A feltétel |q| < 1. Az 5/4, a −1 és az 1 hányadosnál a tagok nem tartanak 0-hoz, "
            "így véges összeg sincs."),
 ]),

 ("Valós helyzetek", [
   r'<p class="lead">Minden olyan folyamat, amelyben minden lépés az előzőnek <b>ugyanannyiszorosa</b> (ugyanakkora hányada), '
   r'mértani sorozatot ad. Ha a lépések végtelen sokáig folytatódnak, a teljes mennyiség a sor összege.</p>',
   doboz("pelda", "I.V.H. Akták — a lengő inga",
         r'<p>Egy inga az első lengése során $64$ cm-es ívet fut be, és minden további lengése az előző '
         r'$\frac34$-e. Mekkora az első négy lengés íve, és mekkora utat tesz meg az inga összesen, ha '
         r'(elméletben) végtelen sokáig leng?</p>'
         r'<p>A lengések: $64,\ 48,\ 36,\ 27$ cm. Itt $b_1=64$ és $q=\frac34$, $\lvert q\rvert\lt1$, így</p>'
         r'$$S=\frac{64}{1-\frac34}=\frac{64}{\frac14}=256\ \text{cm}.$$'
         r'<p>A valóságban az inga véges sok lengés után megáll — a $256$ cm az a felső határ, amelyet '
         r'a megtett út soha nem lép át.</p>', hid="pelda-valos-sor"),
 ]),

 ("Szakaszos tizedes törtek", [
   r'<p class="lead">A tisztán szakaszos tizedes tört (például $0{,}\dot4$) egy végtelen mértani sor '
   r'összege, a vegyes szakaszos (például $0{,}1\dot6=0{,}1+0{,}06+0{,}006+\dots$) egy véges tizedes tört és '
   r'egy mértani sor összege. Így bármelyiket közönséges törtté írhatjuk.</p>',
   doboz("pelda", "I.V.H. Akták — tizedes törtből tört",
         r'<p><b>a)</b> $0{,}\dot4=0{,}4+0{,}04+0{,}004+\dots$, ahol $b_1=\frac4{10}$ és $q=\frac1{10}$:</p>'
         r'$$0{,}\dot4=\frac{\frac4{10}}{1-\frac1{10}}=\frac{4}{9} .$$'
         r'<p><b>b)</b> $0{,}\dot2\dot7=0{,}27+0{,}0027+\dots$, ahol $b_1=\frac{27}{100}$ és '
         r'$q=\frac1{100}$:</p>'
         r'$$0{,}\dot2\dot7=\frac{\frac{27}{100}}{1-\frac1{100}}=\frac{27}{99}=\frac3{11} .$$',
         hid="pelda-szakaszos"),
   kviz(r'Mennyi a $0{,}999\ldots=0{,}\dot9$ végtelen szakaszos tizedes tört értéke?',
        [r'pontosan $1$', r'egy kicsit kevesebb $1$-nél', r'$0{,}9$', r'nem lehet kiszámolni'], 0,
        jo="✔ b₁ = 9/10, q = 1/10, tehát az összeg (9/10)/(9/10) = 1. A 0,999… és az 1 ugyanaz a szám.",
        nem="✘ A 0,999… nem „majdnem 1”: végtelen mértani sorként (9/10)/(1 − 1/10) = 1. "
            "Nincs olyan szám, amely a kettő közé esne."),
 ]),

 ("🧾 Gyorsismétlő", [
   r'<p>A témakör öt számolási típusa egy táblázatban.</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>típus</th><th>a módszer</th><th>példa</th></tr>'
   r'<tr><td>racionális tört</td><td>kiemelés, fokszám-szabály</td><td>$\frac{6n^2-5n+1}{3n^2+4}\to2$</td></tr>'
   r'<tr><td>$\infty-\infty$</td><td>közös nevező, utána kiemelés</td><td>$\frac{n^2}{n+1}-n\to-1$</td></tr>'
   r'<tr><td>gyökös</td><td>kiemelés a gyökjel alól: $\sqrt{an^2}=\sqrt a\,n$</td><td>$\frac{\sqrt{16n^2+5n-2}}{3n+1}\to\frac43$</td></tr>'
   r'<tr><td>$1^\infty$</td><td>$\left(1+\frac kn\right)^{mn}\to e^{km}$; előbb: az alap $1$-hez tart?</td><td>$\left(1+\frac2n\right)^{4n}\to e^8$</td></tr>'
   r'<tr><td>végtelen mértani sor</td><td>$S=\frac{b_1}{1-q}$, csak ha $\lvert q\rvert\lt1$</td><td>$0{,}\dot4=\frac49$</td></tr>'
   r'</table></div>',
   NEHEZ(7, 8, "összetettebb mértani sorok"),
   GY(FGY + "#alap-19", "A 19–26", FGY + "#kozep-16", "K 16–20"),
   brief('<b>Nagol:</b> A sorozatoknál $n$ egyik egész számról a másikra ugrált. A következő '
         'küldetésben $x$ folyamatosan fut, és a határérték <b>falakat</b> rajzol a függvények köré — '
         'az aszimptotákat. <b>Véd Vilmos:</b> Falak? Azokon én mindig átmegyek. '
         '<b>Nagol:</b> Ezeken nem fogsz.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-az-e-szam.html",
     cim="Az $e$ szám",
     cim_tiszta="Az e szám",
     alcim="Az $\\left(1+\\frac1n\\right)^n$ sorozat határértéke, az $e$-típusú határértékek számolása, "
           "és mikor nem jön szóba az $e$.",
     chip=KUL + " · 4/5", szakaszok=B3,
     elozo=("tananyag-gyokos-kifejezesek.html", "Gyökös kifejezések határértéke"),
     kovetkezo=("tananyag-vegtelen-mertani-sor.html", "A végtelen mértani sor")),
 lap(**T, fajl="tananyag-vegtelen-mertani-sor.html",
     cim="A végtelen mértani sor",
     alcim="Végtelen sok tag véges összege: az $S=\\frac{b_1}{1-q}$ képlet és a feltétele, valós "
           "helyzetek és a szakaszos tizedes törtek.",
     chip=KUL + " · 5/5", szakaszok=C,
     elozo=("tananyag-az-e-szam.html", "Az e szám"),
     kovetkezo=(FGY, "Zsoldos-lista — feladatgyűjtemény")),
]
for u in KI:
    print("✓", os.path.basename(u))
