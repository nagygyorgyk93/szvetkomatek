# -*- coding: utf-8 -*-
"""4e/03 — C blokk: monotonitas es szelsoertek (C1), konvexitas es inflexio (C2), a teljes fuggvenyvizsgalat (C3).
Mentor: Ved Vilmos & Nagol. Kuldetes: A Pillanatnyi Kaosz.
Specifikacio: projektek/4e/munkafajlok/narrativa_03-derivalt.md (C-blokk)
A C3 lepessora a tanar kidolgozott peldaibol (munkafajlok/3_Derivalas/Fuggvenykivizsgalas/): ET -> zerushely, elojel ->
paritas -> aszimptotak -> monotonitas, szelsoertek -> konvexitas, inflexio -> grafikon.
Tiltott adatok: a 26/27-es 2. es 3. dolgozat kifejezesei (build_felmero_4e_03.py) — lent ellenorizve."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek, svg_interaktiv

T = dict(tagozat="4e", mappa="03-derivalt", temakor="A függvény deriváltja")
KUL = "A Pillanatnyi Káosz"
FV = "feladatok-fuggvenyvizsgalat.html"
E402 = "../02-fuggvenyek/"
KEK, BORO, ZOLD, PIROS, LILA, SOT, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#7c3aed", "#0f172a", "#64748b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FV}#nehez-{tol}">Zsoldos-lista II., nehéz {tol}–{ig}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table">{"<tr>" + th + "</tr>" if fejlec else ""}{tr}</table></div>'


def ELOJEL(oszlopok, sorok):
    """Előjeltáblázat: `oszlopok` = az x sor cellái, `sorok` = [(címke, [cellák]), …]."""
    th = "<th>$x$</th>" + "".join(f"<th>{c}</th>" for c in oszlopok)
    tr = "".join(f"<tr><th>{c}</th>" + "".join(f"<td>{v}</td>" for v in cs) + "</tr>" for c, cs in sorok)
    return f'<div class="tblwrap"><table class="tt-table elojel"><tr>{th}</tr>{tr}</table></div>'


# ---------------------------------------------------------------- önteszt
from sympy import symbols, diff, simplify, sympify, solve, limit, oo, factor, fraction, together, Rational as R
E = []
x = symbols("x", real=True)
S = lambda s: sympify(s, locals={"x": x})


def _egyezik(a, b):
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        return (isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)) and len(a) == len(b)
                and all(_egyezik(p, q) for p, q in zip(a, b)))
    if a == b:
        return True
    if str(a) in "+-" or str(b) in "+-":
        return False
    return simplify(S(str(a)) - S(str(b))) == 0


def chk(nev, kapott, vart):
    if not _egyezik(kapott, vart):
        E.append((nev, kapott, vart))


def krit(s):
    f = S(s); d = diff(f, x)
    return [(c, f.subs(x, c)) for c in sorted(solve(fraction(together(d))[0], x))]


def jel(s, rend, pont):
    return "+" if diff(S(s), x, rend).subs(x, pont) > 0 else "-"


# C1
W3 = "x**3-3*x**2+1"                                      # az interaktív ábra polinomja (C1, C2)
chk("C1-widget", [krit(W3), solve(diff(S(W3), x, 2), x), S(W3).subs(x, 1)], [[(0, 1), (2, -3)], [1], -1])
P1 = "x**3-6*x**2+9*x-2"
chk("C1-pol", [factor(diff(S(P1), x)), krit(P1)], ["3*(x-1)*(x-3)", [(1, 2), (3, -2)]])
chk("C1-pol-jel", [jel(P1, 1, v) for v in (0, 2, 4)], ["+", "-", "+"])
T1 = "(x**2+5)/(x-2)"
chk("C1-tort", [factor(diff(S(T1), x)), krit(T1)], ["(x-5)*(x+1)/(x-2)**2", [(-1, -2), (5, 10)]])
chk("C1-tort-jel", [jel(T1, 1, v) for v in (-2, 0, 3, 6)], ["+", "-", "-", "+"])
chk("C1-x3", [diff(S("x**3"), x).subs(x, 0), jel("x**3", 1, -1), jel("x**3", 1, 1)], [0, "+", "+"])
# C2
chk("C2-pol", [diff(S(P1), x, 2), solve(diff(S(P1), x, 2), x), S(P1).subs(x, 2), jel(P1, 2, 0), jel(P1, 2, 3)],
    ["6*x-12", [2], 0, "-", "+"])
chk("C2-x4", [diff(S("x**4"), x, 2), jel("x**4", 2, -1), jel("x**4", 2, 1)], ["12*x**2", "+", "+"])
chk("C2-tort", [factor(diff(S(T1), x, 2)), jel(T1, 2, 0), jel(T1, 2, 3)], ["18/(x-2)**3", "-", "+"])
chk("C2-1x", [factor(diff(S("1/(x-1)"), x, 2))], ["2/(x-1)**3"])
# C3 — polinom
P3 = "x**3-3*x**2"
chk("C3-pol", [factor(S(P3)), krit(P3), solve(diff(S(P3), x, 2), x), S(P3).subs(x, 1),
               [S(P3).subs(x, v) for v in (-1, 1)], limit(S(P3), x, oo), limit(S(P3).subs(x, -x), x, oo)],
    ["x**2*(x-3)", [(0, 0), (2, -4)], [1], -2, [-4, -2], oo, -oo])
# C3 — tört
T3 = "(x**2+3*x)/(x-1)"
f3 = S(T3)
chk("C3-tort", [factor(S(T3)), krit(T3), factor(diff(f3, x)), factor(diff(f3, x, 2)),
                limit(f3, x, 1, "-"), limit(f3, x, 1, "+"), limit(f3 / x, x, oo), limit(f3 - x, x, oo),
                f3.subs(x, 0)],
    ["x*(x+3)/(x-1)", [(-1, 1), (3, 9)], "(x-3)*(x+1)/(x-1)**2", "8/(x-1)**3", -oo, oo, 1, 4, 0])
chk("C3-tort-elojel", [("+" if f3.subs(x, v) > 0 else "-") for v in (-4, -1, R(1, 2), 2)], ["-", "+", "-", "+"])
chk("C3-kviz", [jel(T3, 1, 2), jel(T3, 2, 2)], ["-", "+"])

TILTOTT = ["x**3-3*x**2-9*x+5", "-x**3+3*x**2+9*x-2", "x**3+3*x**2-9*x-4", "(x**2-3*x)/(x+1)",
           "(x**2-7*x+10)/(x-1)", "(x**2-3*x)/(x-4)", "x**3-2*x**2+3", "x**3+3*x**2-2", "x**3-3*x+1",
           # a 0_Feladatok 29–32. (a gyűjtemény forrása) — a tananyag ne vegye el előre
           "x**3-2*x**2+x-2", "(x**2-5*x+7)/(x-2)", "x**3+3*x**2-4", "-x**3+3*x+2", "-x**3+9*x**2-15*x+3",
           "2*x**3+3*x**2-12*x+1", "(x**2-2*x+1)/(x-2)", "(x**2-6*x+9)/(x-1)", "(x**2-8)/(x+3)", "(x**2-3)/(x+2)",
           "(x**2+x-2)/(x+3)", "(x**2-x-2)/(x-3)", "(x**2-4)/(x**2+1)", "(3-x**2)/(x**2+1)"]
_PONT = (0.37, 1.91, 2.63, 3.3)


def _azonos(u, r_):
    try:
        return all(abs(complex(S(u).subs(x, v)) - complex(S(r_).subs(x, v))) < 1e-9 for v in _PONT)
    except (TypeError, ZeroDivisionError):
        return False


for p in (W3, P1, T1, P3, T3, "x**3", "x**4", "1/(x-1)"):
    for r_ in TILTOTT:
        if _azonos(p, r_):
            E.append(("tiltott", p, r_))
assert not E, E
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
W, H = 360, 250


def fugg_vonal(svg, x0, xr, w=W, h=H, szin=SZURKE):
    """Függőleges szaggatott egyenes (aszimptota) a svg_fuggvenyek() koordinátáiban."""
    bal, jobb, fent, lent = 26, 12, 14, 22
    X = bal + (x0 - xr[0]) / (xr[1] - xr[0]) * (w - bal - jobb)
    vonal = (f'  <line x1="{X:.1f}" y1="{fent}" x2="{X:.1f}" y2="{h - lent}" stroke="{szin}" '
             'stroke-width="1.6" stroke-dasharray="6 4"/>')
    i = svg.find("  </g>") + len("  </g>")
    return svg[:i] + "\n" + vonal + svg[i:]


fW3 = lambda v: v ** 3 - 3 * v ** 2 + 1
IV_C1 = svg_interaktiv(
    "erinto", [1, 0, -3, 1], xr=(-1.3, 3.3), yr=(-5.4, 3.8), csuszka=(-1.1, 3.1, 0.01, -0.6), w=W, h=H,
    felirat="Mozgasd a csúszkát! Ahol az érintő <b>zöld</b>, ott $f'(x_0)\\gt0$ és a függvény nő; ahol "
            "<b>piros</b>, ott $f'(x_0)\\lt0$ és csökken. A szürke, vízszintes érintő a fordulópontokban jelenik meg.",
    leiras="Interaktív ábra: az f(x) = x³ − 3x² + 1 grafikonja, rajta egy csúszkával mozgatható pont és az ottani "
           "érintő, amelynek színe a derivált előjelét mutatja")
IV_C2 = svg_interaktiv(
    "erinto", [1, 0, -3, 1], xr=(-1.3, 3.3), yr=(-5.4, 3.8), csuszka=(-1.1, 3.1, 0.01, 0.2), w=W, h=H, f2=True,
    felirat="Figyeld, hol van a görbe az érintőhöz képest! Az $x_0=1$-től balra a görbe az érintő <b>alatt</b> "
            "halad (konkáv, $f''\\lt0$), jobbra <b>fölötte</b> (konvex, $f''\\gt0$). Az $x_0=1$ az inflexiós hely.",
    leiras="Interaktív ábra: az f(x) = x³ − 3x² + 1 grafikonja mozgatható érintővel; a kijelző az első és a második "
           "derivált előjelét is mutatja")
SVG_C1_POL = svg_fuggvenyek(
    [(lambda v: v ** 3 - 6 * v ** 2 + 9 * v - 2, KEK, "f(x) = x³ − 6x² + 9x − 2", [(-0.3, 4.3)])],
    xr=(-0.8, 4.8), yr=(-3.2, 3.4), w=W, h=H,
    pontok=[(1, 2, "max (1; 2)", ZOLD, -18, -9), (3, -2, "min (3; −2)", PIROS, -20, 18)],
    leiras="Az f(x) = x³ − 6x² + 9x − 2 grafikonja: lokális maximum az (1; 2), lokális minimum a (3; −2) pontban")
_T1 = lambda v: (v * v + 5) / (v - 2)
SVG_C1_TORT = fugg_vonal(svg_fuggvenyek(
    [(_T1, KEK, "f(x) = (x² + 5)/(x − 2)", [(-5.8, 1.93), (2.07, 9.8)]),
     (lambda v: v + 2, SZURKE, "ferde aszimptota: y = x + 2", [(-5.8, 9.8)], "szaggatott")],
    xr=(-6, 10), yr=(-9, 16), w=W, h=H,
    pontok=[(-1, -2, "max (−1; −2)", ZOLD, -30, -9), (5, 10, "min (5; 10)", PIROS, -12, 18)],
    leiras="Az f(x) = (x² + 5)/(x − 2) grafikonja: két ág az x = 2 függőleges aszimptota két oldalán, lokális "
           "maximum a (−1; −2), lokális minimum az (5; 10) pontban, ferde aszimptota y = x + 2"), 2, (-6, 10))
SVG_C2_IVEK = svg_fuggvenyek(
    [(lambda v: 0.6 + 0.9 * (v - 0.3) ** 2, KEK, "nő, konvex (∪)", [(0.3, 1.9)]),
     (lambda v: 3.0 - 0.9 * (v - 3.9) ** 2, BORO, "nő, konkáv (∩)", [(2.3, 3.9)]),
     (lambda v: 0.6 + 0.9 * (v - 5.9) ** 2, ZOLD, "csökken, konvex (∪)", [(4.3, 5.9)]),
     (lambda v: 3.0 - 0.9 * (v - 6.3) ** 2, PIROS, "csökken, konkáv (∩)", [(6.3, 7.9)])],
    xr=(-0.2, 8.2), yr=(-0.3, 5.9), w=W, h=H,
    leiras="Négy görbedarab: növekvő és konvex, növekvő és konkáv, csökkenő és konvex, csökkenő és konkáv — "
           "a monotonitás és a görbülés egymástól független")
SVG_C3_POL = svg_fuggvenyek(
    [(lambda v: v ** 3 - 3 * v ** 2, KEK, "f(x) = x³ − 3x²", [(-1.25, 3.35)])],
    xr=(-1.6, 3.8), yr=(-5, 2.6), w=W, h=H,
    pontok=[(0, 0, "max (0; 0)", ZOLD, 6, -8), (2, -4, "min (2; −4)", PIROS, -22, 18),
            (1, -2, "inflexió (1; −2)", LILA, 8, 4), (3, 0, "(3; 0)", SOT, -8, -9)],
    leiras="Az f(x) = x³ − 3x² grafikonja: zérushelyek 0 és 3, lokális maximum (0; 0), lokális minimum (2; −4), "
           "inflexiós pont (1; −2)")
_T3 = lambda v: (v * v + 3 * v) / (v - 1)
SVG_C3_TORT = fugg_vonal(svg_fuggvenyek(
    [(_T3, KEK, "f(x) = (x² + 3x)/(x − 1)", [(-8.8, 0.95), (1.05, 8.8)]),
     (lambda v: v + 4, SZURKE, "ferde aszimptota: y = x + 4", [(-8.8, 8.8)], "szaggatott")],
    xr=(-9, 9), yr=(-12, 18), w=W, h=H,
    pontok=[(-1, 1, "max (−1; 1)", ZOLD, -32, -8), (3, 9, "min (3; 9)", PIROS, 6, 16),
            (-3, 0, "", SOT), (0, 0, "", SOT)],
    leiras="Az f(x) = (x² + 3x)/(x − 1) grafikonja: zérushelyek −3 és 0, függőleges aszimptota x = 1, ferde "
           "aszimptota y = x + 4, lokális maximum (−1; 1), lokális minimum (3; 9)"), 1, (-9, 9))

NO, CS, MX, MN = "↗ nő", "↘ csökken", "max", "min"

# ---------------------------------------------------------------- C1
C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Hegyek és völgyek! A legmagasabb pont, a legmélyebb pont — ott történik minden. '
         '<b>Nagol:</b> És ott vízszintes az érintő. Ennyi a titok — <i>majdnem</i>. A 02. témakörben a '
         'monotonitást még csak ránéztük a grafikonra '
         '(<a href="' + E402 + 'tananyag-fuggvenytulajdonsagok.html#def-monoton-fv">a monoton függvény</a>); '
         'most a derivált előjeléből <b>kiszámoljuk</b>. Ez a harmadik dolgozat gerince.'),
 ]),

 ("A derivált előjele és a monotonitás", [
   r'<p class="lead">Ha az érintő minden pontban emelkedik, a görbe is emelkedik. A derivált előjele tehát '
   r'megmondja, merre halad a függvény.</p>',
   doboz("tetel", "A monotonitás és a derivált",
         r'<p>Legyen $f$ deriválható az $I$ intervallumon.</p>'
         r'<ul><li>Ha $f\'(x)\gt0$ minden $x\in I$-re, akkor $f$ az $I$-n <b>szigorúan monoton növekvő</b>.</li>'
         r'<li>Ha $f\'(x)\lt0$ minden $x\in I$-re, akkor $f$ az $I$-n <b>szigorúan monoton csökkenő</b>.</li></ul>',
         hid="tetel-monotonitas"),
   IV_C1,
   kviz(r'Egy függvényre $f\'(x)\gt0$ teljesül a $(2;\,5)$ intervallumon. Mit tudunk biztosan?',
        [r'$f$ szigorúan nő a $(2;\,5)$ intervallumon',
         r'$f(x)\gt0$ a $(2;\,5)$ intervallumon',
         r'$f$-nek van szélsőértéke a $(2;\,5)$ intervallumban',
         r'$f$ konvex a $(2;\,5)$ intervallumon'], 0,
        jo="✔ A derivált előjele a monotonitást adja. Hogy f pozitív-e, arról f′ nem szól: egy növekvő függvény "
           "lehet végig negatív is.",
        nem="✘ Az f′ > 0 a MERedekségről szól: f ott nő. Az f előjeléről (pozitív-e) vagy a görbüléséről "
            "(konvex-e) ebből semmi nem következik."),
 ]),

 ("Stacionárius pont és lokális szélsőérték", [
   doboz("definicio", "Lokális szélsőérték",
         r'<p>Az $f$ függvénynek az $x_0$ helyen <b>lokális maximuma</b> van, ha $x_0$ egy környezetében minden '
         r'$x$-re $f(x)\le f(x_0)$; <b>lokális minimuma</b>, ha $f(x)\ge f(x_0)$. A szélsőérték <b>helye</b> az '
         r'$x_0$, <b>értéke</b> az $f(x_0)$. Ahol $f\'(x_0)=0$, azt a helyet <b>stacionárius</b> helynek hívjuk.</p>',
         hid="def-lokalis-szelsoertek"),
   doboz("tetel", "A szélsőérték feltételei",
         r'<ul><li><b>Szükséges feltétel:</b> ha $f$ deriválható $x_0$-ban, és ott lokális szélsőértéke van, '
         r'akkor $f\'(x_0)=0$.</li>'
         r'<li><b>Elégséges feltétel:</b> ha $f\'(x_0)=0$, és $f\'$ az $x_0$-ban <b>előjelet vált</b>, akkor ott '
         r'szélsőérték van: ha $+$-ból $-$-ba vált, <b>maximum</b>; ha $-$-ból $+$-ba, <b>minimum</b>.</li></ul>',
         hid="tetel-szelsoertek-feltetel"),
   kviz(r'Döntsd el: az $f(x)=x^3$ függvénynél $f\'(0)=0$. Van-e szélsőértéke a $0$-ban?',
        [r'nincs: $f\'(0)=0$, de $f\'$ a $0$-ban nem vált előjelet',
         r'van, lokális minimum, mert $f\'(0)=0$',
         r'van, lokális maximum, mert $f\'(0)=0$',
         r'a kérdés értelmetlen, mert $x^3$ a $0$-ban nem deriválható'], 0,
        jo="✔ f′(x) = 3x² ≥ 0 mindkét oldalon: a függvény végig nő, a 0-ban csak „megpihen”. A nulla derivált "
           "szükséges, de nem elégséges.",
        nem="✘ Az f′(x₀) = 0 csak szükséges feltétel. Az x³-nál f′(x) = 3x² a 0 két oldalán is pozitív, tehát "
            "nincs előjelváltás — a függvény végig nő, szélsőérték nincs."),
 ]),

 ("Az előjeltáblázat", [
   r'<p class="lead">A módszer mindig ugyanaz: <b>1.</b> $f\'(x)$ kiszámítása, szorzattá alakítva · <b>2.</b> '
   r'$f\'(x)=0$ megoldása (és a pólusok, ahol $f$ nincs értelmezve) · <b>3.</b> ezek az <b>osztópontok</b>: '
   r'közöttük $f\'$ előjele állandó, egy-egy próbaszámmal eldönthető · <b>4.</b> nő/csökken, és ahol előjelet '
   r'vált: maximum vagy minimum · <b>5.</b> a szélsőérték <b>értéke</b>: behelyettesítés $f$-be.</p>',
   doboz("pelda", "I.V.H. Akták — harmadfokú polinom",
         r'<p>$f(x)=x^3-6x^2+9x-2$. Ekkor $f\'(x)=3x^2-12x+9=3(x-1)(x-3)$, a stacionárius helyek $x=1$ és '
         r'$x=3$.</p>'
         + ELOJEL(["$(-\\infty;\\,1)$", "$1$", "$(1;\\,3)$", "$3$", "$(3;\\,\\infty)$"],
                  [("$f'(x)$", ["$+$", "$0$", "$-$", "$0$", "$+$"]),
                   ("$f(x)$", [NO, f"{MX} $2$", CS, f"{MN} $-2$", NO])]) +
         r'<p>$f(1)=1-6+9-2=2$ és $f(3)=27-54+27-2=-2$. Tehát $f$ nő a $(-\infty;\,1)$ és a $(3;\,\infty)$ '
         r'intervallumon, csökken az $(1;\,3)$-on; <b>lokális maximum</b> az $(1;\,2)$, <b>lokális minimum</b> a '
         r'$(3;\,-2)$ pontban.</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a próbaszám: $f\'(0)=9\gt0$, $f\'(2)=-3\lt0$, $f\'(4)=9\gt0$. '
         r'Három behelyettesítés, és kész a tábla.”</p>', hid="pelda-harmadfoku"),
   abra(SVG_C1_POL, 'A táblázat a grafikonon: nő — maximum — csökken — minimum — nő.'),
   kviz(r'Az előjeltáblázat szerint $f\'$ az $x=3$-ban $-$-ból $+$-ba vált, és $f(3)=-2$. Mi a helyes válasz?',
        [r'lokális minimum van a $(3;\,-2)$ pontban, értéke $-2$',
         r'lokális minimum, értéke $3$',
         r'lokális maximum, értéke $-2$',
         r'a minimum értéke $0$, mert $f\'(3)=0$'], 0,
        jo="✔ − → + előjelváltás: minimum. A helye x = 3, az értéke f(3) = −2.",
        nem="✘ A szélsőérték értéke nem a hely (3) és nem a derivált (0), hanem a függvényérték: f(3) = −2. "
            "A − → + váltás minimumot jelez."),
 ]),

 ("Racionális törtfüggvény", [
   r'<p class="lead">Törtfüggvénynél a módszer ugyanaz, két kiegészítéssel: a <b>pólus</b> (ahol a nevező $0$) is '
   r'osztópont, de ott a függvény nincs értelmezve; és a derivált nevezője egy <b>négyzet</b>, ami mindig '
   r'pozitív — az előjelet a számláló dönti el.</p>',
   doboz("pelda", "I.V.H. Akták — törtfüggvény monotonitása",
         r'<p>$f(x)=\dfrac{x^2+5}{x-2}$, $D_f=\mathbb R\setminus\{2\}$. A hányadosszabállyal</p>'
         r'$$f\'(x)=\frac{2x(x-2)-(x^2+5)}{(x-2)^2}=\frac{x^2-4x-5}{(x-2)^2}=\frac{(x+1)(x-5)}{(x-2)^2}.$$'
         + ELOJEL(["$(-\\infty;\\,-1)$", "$-1$", "$(-1;\\,2)$", "$2$", "$(2;\\,5)$", "$5$", "$(5;\\,\\infty)$"],
                  [("$f'(x)$", ["$+$", "$0$", "$-$", "—", "$-$", "$0$", "$+$"]),
                   ("$f(x)$", [NO, f"{MX} $-2$", CS, "nincs értelmezve", CS, f"{MN} $10$", NO])]) +
         r'<p>$f(-1)=\frac{6}{-3}=-2$ és $f(5)=\frac{30}{3}=10$: lokális maximum a $(-1;\,-2)$, lokális minimum az '
         r'$(5;\,10)$ pontban.</p>', hid="pelda-tort-monoton"),
   abra(SVG_C1_TORT, 'Két ág a pólus két oldalán: a maximum a bal, a minimum a jobb ágon.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos kihagyja a pólust a táblázatból, és azt írja: „a függvény a $(-1;\,5)$ intervallumon '
         r'csökken”. <b>Nem intervallum</b>, hiszen a $2$-ben nincs értelmezve: két külön intervallumon, a '
         r'$(-1;\,2)$-n és a $(2;\,5)$-ön csökken. A pólus nem is szélsőérték — ott nincs függvényérték.</p>'
         r'<p>És ne zavarjon, hogy a maximum ($-2$) kisebb a minimumnál ($10$): <b>lokális</b> szélsőértékek, '
         r'csak a saját környezetükben a legnagyobbak, illetve a legkisebbek.</p>'),
 ]),

 ("Nem minden nulla hely szélsőérték", [
   r'<p class="lead">Két tanulság a szélsőérték-keresés széléről:</p>'
   r'<ul><li><b>$f\'(x_0)=0$, mégsincs szélsőérték:</b> az $x^3$-nál a $0$-ban vízszintes az érintő, de a '
   r'függvény mindkét oldalon nő. Ezért kell az előjeltábla, nem elég az egyenlet.</li>'
   r'<li><b>Szélsőérték, pedig nincs vízszintes érintő:</b> lásd a 💡-dobozt.</li></ul>',
   doboz("erdekesseg", "Töréspont",
         r'<p>Az $f(x)=|x|$ függvénynek a $0$-ban minimuma van, pedig ott <b>nem deriválható</b>: balról $-1$, '
         r'jobbról $1$ a meredekség, a grafikonnak „csúcsa” van. Az ilyen helyet <b>töréspontnak</b> hívjuk. A mi '
         r'függvényeink (polinomok, racionális törtek) mindenhol deriválhatók, ahol értelmezve vannak — '
         r'nálunk töréspont nem fordul elő.</p>'),
   GY(FV + "#alap-1", "A 1–6", FV + "#kozep-1", "K 1–4"),
   brief('<b>Nagol:</b> Tudjuk, merre megy a görbe. Most azt nézzük meg, <b>hogyan hajlik</b> — ehhez kell a '
         'második derivált. <b>Véd Vilmos:</b> Az ütéseid íve? <b>Nagol:</b> Pontosan.', outro=True),
 ]),
]

# ---------------------------------------------------------------- C2
C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol</b> a saját ütései ívét elemzi a lassított felvételen: Felfelé nyíló ív — <b>konvex</b>. '
         'Lefelé nyíló — <b>konkáv</b>. Ahol vált, ott a legnagyobb a lendület. <b>Véd Vilmos:</b> Én mindig '
         'konkáv vagyok. Főleg hétfőn. <b>Nagol:</b> Ezt most ki is számoljuk — a második deriválttal.'),
 ]),

 ("Konvex és konkáv", [
   doboz("definicio", "Konvex és konkáv függvény",
         r'<p>Legyen $f$ deriválható az $I$ intervallumon. $f$ az $I$-n <b>konvex</b> (∪), ha grafikonja minden '
         r'ottani érintője <b>fölött</b> halad; <b>konkáv</b> (nem konvex, ∩), ha minden érintője <b>alatt</b>. '
         r'(Ekvivalens megfogalmazás: konvexnél bármely két pontját összekötő húr a grafikon fölött van.)</p>',
         hid="def-konvex"),
   IV_C2,
   abra(SVG_C2_IVEK, 'A monotonitás és a görbülés független: mind a négy párosítás előfordul.'),
   kviz(r'Melyik állítás igaz?',
        [r'egy függvény lehet egyszerre csökkenő és konvex',
         r'a konvex függvény mindig növekvő',
         r'a konkáv függvény értékei mindig negatívak',
         r'ha $f\'\gt0$, akkor $f$ konvex'], 0,
        jo="✔ A görbülés (konvex/konkáv) és a monotonitás (nő/csökken) két különböző tulajdonság — az ábra zöld "
           "íve csökkenő és konvex.",
        nem="✘ A konvex a HAJLÁST írja le, nem az irányt: az ábra zöld íve csökken, mégis felfelé nyílik "
            "(konvex). Az előjelhez és a monotonitáshoz a konvexitásnak nincs köze."),
 ]),

 ("A második derivált előjele", [
   doboz("tetel", "A konvexitás és a második derivált",
         r'<p>Legyen $f$ kétszer deriválható az $I$ intervallumon.</p>'
         r'<ul><li>Ha $f\'\'(x)\gt0$ minden $x\in I$-re, akkor $f$ az $I$-n <b>konvex</b>.</li>'
         r'<li>Ha $f\'\'(x)\lt0$ minden $x\in I$-re, akkor $f$ az $I$-n <b>konkáv</b>.</li></ul>'
         r'<p>Szemléletesen: $f\'\'\gt0$ esetén az érintő meredeksége nő — a görbe „felfelé kanyarodik”.</p>',
         hid="tetel-konvexitas"),
   doboz("pelda", "I.V.H. Akták — egy polinom görbülése",
         r'<p>A C1-es példa: $f(x)=x^3-6x^2+9x-2$, $f\'(x)=3x^2-12x+9$, tehát $f\'\'(x)=6x-12$, ami a $2$-ben $0$.</p>'
         + ELOJEL(["$(-\\infty;\\,2)$", "$2$", "$(2;\\,\\infty)$"],
                  [("$f''(x)$", ["$-$", "$0$", "$+$"]),
                   ("$f(x)$", ["∩ konkáv", "inflexió $0$", "∪ konvex"])]) +
         r'<p>$f(2)=8-24+18-2=0$, így az <b>inflexiós pont</b> a $(2;\,0)$ — éppen a maximum $(1;\,2)$ és a '
         r'minimum $(3;\,-2)$ között félúton.</p>', hid="pelda-konvex-polinom"),
 ]),

 ("Inflexiós pont", [
   doboz("definicio", "Inflexiós pont",
         r'<p>Az $x_0$ az $f$ <b>inflexiós helye</b> (az $\big(x_0;\,f(x_0)\big)$ pont az inflexiós pont), ha ott a '
         r'függvény konvexből konkávba vagy konkávból konvexbe vált. Kétszer deriválható függvénynél: '
         r'$f\'\'(x_0)=0$, és $f\'\'$ az $x_0$-ban <b>előjelet vált</b>.</p>', hid="def-inflexio"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „ahol $f\'\'(x_0)=0$, ott inflexiós pont van”. Az $f(x)=x^4$ lebuktatja: '
         r'$f\'\'(x)=12x^2$, ez a $0$-ban $0$ — de mindkét oldalon <b>pozitív</b>, tehát a függvény végig konvex, '
         r'inflexió nincs. Ugyanaz a hiba, mint a szélsőértéknél: <b>a nulla hely csak jelölt, az előjelváltás '
         r'dönt</b>. Rokon hiba a „konvex” és a „konkáv” felcserélése — jegyezd meg: konvex ∪, mint egy tál.</p>'),
   doboz("erdekesseg", "A leggyorsabb változás pontja",
         r'<p>Az inflexiós pontban a derivált (a meredekség) szélsőértéket vesz fel: ott a leggyorsabb a növekedés '
         r'vagy a csökkenés. Egy járvány „inflexiós pontja” az a nap, amikor a legtöbb új eset jelentkezik — '
         r'utána lassul a terjedés.</p>'),
   kviz(r'Az $f(x)=x^4$ függvényre $f\'\'(0)=0$. Van-e inflexiós pontja a $0$-ban?',
        [r'nincs, mert $f\'\'$ a $0$ két oldalán is pozitív', r'van, mert $f\'\'(0)=0$',
         r'van, mert $f\'(0)=0$', r'nincs, mert $f(0)=0$'], 0,
        jo="✔ f″(x) = 12x² ≥ 0 — nincs előjelváltás, a függvény végig konvex.",
        nem="✘ A nulla második derivált csak jelölt. Az x⁴-nél f″(x) = 12x² a 0 két oldalán is pozitív, a "
            "görbülés nem vált — inflexió nincs."),
 ]),

 ("Törtfüggvénynél", [
   r'<p class="lead">A törtfüggvény görbülése a pólus két oldalán különbözhet — de a pólus <b>nem</b> inflexiós '
   r'pont, mert ott a függvény nincs értelmezve.</p>'
   r'<p>A C1-es $f(x)=\dfrac{x^2+5}{x-2}$ függvény második deriváltja $f\'\'(x)=\dfrac{18}{(x-2)^3}$. A '
   r'számláló pozitív, az előjelet a nevező adja:</p>'
   + ELOJEL(["$(-\\infty;\\,2)$", "$2$", "$(2;\\,\\infty)$"],
            [("$f''(x)$", ["$-$", "—", "$+$"]), ("$f(x)$", ["∩ konkáv", "nincs értelmezve", "∪ konvex"])]) +
   r'<p>A bal ág tehát konkáv, a jobb ág konvex (nézd meg a C1-es grafikonon!), inflexiós pont nincs. '
   r'Hasonlóan az $\dfrac1{x-1}$-nél: $f\'\'(x)=\dfrac{2}{(x-1)^3}$.</p>',
   NEHEZ(1, 2, "törtfüggvény teljes görbülés-vizsgálata"),
   GY(FV + "#alap-7", "A 7–8", FV + "#kozep-5", "K 5–8"),
   brief('<b>Nagol:</b> Minden eszköz megvan: értelmezési tartomány, zérushely, aszimptota a 02-ből; '
         'monotonitás és görbülés a deriváltakból. <b>Véd Vilmos:</b> Akkor rakjuk össze a teljes profilt! '
         '<b>Nagol:</b> Hét lépésben.', outro=True),
 ]),
]

# ---------------------------------------------------------------- C3
C3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos</b> és <b>Nagol</b> egy ismeretlen függvény profilját rajzolják fel az I.V.H. '
         'aktájába. Minden lépés egy nyom: hol él, hol metszi a tengelyt, merre szökik a végtelenbe, hol fordul, '
         'hogyan hajlik. <b>Véd Vilmos:</b> Hé, aki most a pad alatt a telefonját nyomkodja: <b>a harmadik '
         'dolgozat pontosan ez lesz.</b>'),
 ]),

 ("A hét lépés", [
   doboz("tetel", "A teljes függvényvizsgálat lépései",
         r'<ol><li><b>Értelmezési tartomány</b> — hol van értelme a képletnek; a kizárt helyek a későbbi '
         r'táblázatok osztópontjai (<a href="' + E402 + r'tananyag-ertelmezesi-tartomany.html">02: értelmezési '
         r'tartomány</a>).</li>'
         r'<li><b>Zérushelyek és előjel</b> — $f(x)=0$ megoldása, az $y$ tengely metszéspontja $f(0)$, és hol '
         r'pozitív, hol negatív a függvény.</li>'
         r'<li><b>Paritás</b> — páros, páratlan vagy egyik sem (<a href="' + E402 +
         r'tananyag-fuggvenytulajdonsagok.html#def-paros-paratlan">02: paritás</a>).</li>'
         r'<li><b>Aszimptoták</b> — függőleges, vízszintes vagy ferde (<a href="' + E402 +
         r'tananyag-aszimptotak.html#def-aszimptota">02: aszimptoták</a>); polinomnak nincs.</li>'
         r'<li><b>Monotonitás és szélsőérték</b> — $f\'$, előjeltáblázat (C1).</li>'
         r'<li><b>Konvexitás és inflexió</b> — $f\'\'$, előjeltáblázat (C2).</li>'
         r'<li><b>Grafikon</b> — a pontok, az aszimptoták és a táblázatok alapján.</li></ol>'
         r'<p>A tanterv (M2) szerint <b>polinomot és racionális törtfüggvényt</b> vizsgálunk.</p>',
         hid="tetel-het-lepes"),
   kviz(r'Miért az értelmezési tartomány a vizsgálat <b>első</b> lépése?',
        [r'mert a kizárt helyek (pólusok) osztópontok minden táblázatban, és ott keressük a függőleges aszimptotát',
         r'mert így szokás, a sorrend valójában mindegy',
         r'mert az értelmezési tartományból kiszámolható a derivált',
         r'mert az értelmezési tartomány mindig $\mathbb R$'], 0,
        jo="✔ Minden további lépés rá épül: a pólus osztópont az előjel-, a monotonitás- és a konvexitás-"
           "táblázatban is, és ott lehet függőleges aszimptota.",
        nem="✘ A sorrend nem mindegy: a kizárt helyek nélkül rossz lenne minden táblázat (a pólusnál is válthat "
            "előjelet a függvény), és a függőleges aszimptotát sem találnánk meg."),
 ]),

 ("Polinomfüggvény", [
   doboz("pelda", "I.V.H. Akták — $f(x)=x^3-3x^2$",
         r'<ol><li>$D_f=\mathbb R$.</li>'
         r'<li>$f(x)=x^2(x-3)$: zérushelyek $x=0$ (kétszeres) és $x=3$; $f(0)=0$. Mivel $x^2\ge0$, az előjelet '
         r'az $x-3$ adja: $f(x)\lt0$, ha $x\lt3$ ($x\ne0$), és $f(x)\gt0$, ha $x\gt3$.</li>'
         r'<li>$f(-1)=-4$, $f(1)=-2$: nem páros és nem páratlan.</li>'
         r'<li>Aszimptota nincs; $\lim\limits_{x\to\infty}f(x)=\infty$, $\lim\limits_{x\to-\infty}f(x)=-\infty$.</li>'
         r'<li>$f\'(x)=3x^2-6x=3x(x-2)$: nő, ha $x\lt0$ vagy $x\gt2$; csökken a $(0;\,2)$-n; <b>maximum</b> '
         r'$(0;\,0)$, <b>minimum</b> $(2;\,-4)$.</li>'
         r'<li>$f\'\'(x)=6x-6$: konkáv, ha $x\lt1$; konvex, ha $x\gt1$; <b>inflexiós pont</b> $(1;\,-2)$.</li></ol>'
         + ELOJEL(["$(-\\infty;\\,0)$", "$0$", "$(0;\\,1)$", "$1$", "$(1;\\,2)$", "$2$", "$(2;\\,\\infty)$"],
                  [("$f'(x)$", ["$+$", "$0$", "$-$", "$-$", "$-$", "$0$", "$+$"]),
                   ("$f''(x)$", ["$-$", "$-$", "$-$", "$0$", "$+$", "$+$", "$+$"]),
                   ("$f(x)$", ["↗ ∩", "max $0$", "↘ ∩", "infl. $-2$", "↘ ∪", "min $-4$", "↗ ∪"])]) +
         r'<p>7. A grafikon az ábrán.</p>', hid="pelda-polinom-vizsgalat"),
   abra(SVG_C3_POL, 'Az $x^3-3x^2$ grafikonja: a $0$-ban érinti az $x$ tengelyt (kétszeres gyök), a $3$-ban metszi.'),
 ]),

 ("Racionális törtfüggvény", [
   doboz("pelda", "I.V.H. Akták — $f(x)=\\dfrac{x^2+3x}{x-1}$",
         r'<ol><li>$D_f=\mathbb R\setminus\{1\}$.</li>'
         r'<li>$f(x)=\dfrac{x(x+3)}{x-1}$: zérushelyek $x=-3$ és $x=0$, $f(0)=0$. Előjel (a három tényező '
         r'előjeléből): $f\lt0$ a $(-\infty;\,-3)$ és a $(0;\,1)$ intervallumon, $f\gt0$ a $(-3;\,0)$ és az '
         r'$(1;\,\infty)$ intervallumon.</li>'
         r'<li>Az értelmezési tartomány nem szimmetrikus a $0$-ra: nem páros és nem páratlan.</li>'
         r'<li>Függőleges aszimptota: $x=1$ (a számláló ott $4\ne0$); $\lim\limits_{x\to1-0}f(x)=-\infty$, '
         r'$\lim\limits_{x\to1+0}f(x)=+\infty$. Ferde aszimptota: $k=\lim\limits_{x\to\infty}\frac{f(x)}{x}=1$, '
         r'$n=\lim\limits_{x\to\infty}\big(f(x)-x\big)=\lim\limits_{x\to\infty}\frac{4x}{x-1}=4$, tehát $y=x+4$.</li>'
         r'<li>$f\'(x)=\dfrac{(2x+3)(x-1)-(x^2+3x)}{(x-1)^2}=\dfrac{x^2-2x-3}{(x-1)^2}=\dfrac{(x+1)(x-3)}{(x-1)^2}$: '
         r'<b>maximum</b> $(-1;\,1)$, <b>minimum</b> $(3;\,9)$.</li>'
         r'<li>$f\'\'(x)=\dfrac{8}{(x-1)^3}$: konkáv, ha $x\lt1$; konvex, ha $x\gt1$; inflexió nincs.</li></ol>'
         + ELOJEL(["$(-\\infty;\\,-1)$", "$-1$", "$(-1;\\,1)$", "$1$", "$(1;\\,3)$", "$3$", "$(3;\\,\\infty)$"],
                  [("$f'(x)$", ["$+$", "$0$", "$-$", "—", "$-$", "$0$", "$+$"]),
                   ("$f''(x)$", ["$-$", "$-$", "$-$", "—", "$+$", "$+$", "$+$"]),
                   ("$f(x)$", ["↗ ∩", "max $1$", "↘ ∩", "nincs ért.", "↘ ∪", "min $9$", "↗ ∪"])]) +
         r'<p>7. A grafikon az ábrán.</p>', hid="pelda-tort-vizsgalat"),
   abra(SVG_C3_TORT, 'A két ág az $x=1$ aszimptota két oldalán; mindkettő a ferde aszimptotához simul.'),
   NEHEZ(3, 4, "racionális törtfüggvény teljes vizsgálata"),
 ]),

 ("Összesítő táblázat és grafikon", [
   r'<p class="lead">A grafikont a táblázatokból rajzoljuk: <b>1.</b> berajzoljuk az aszimptotákat '
   r'(szaggatottan) · <b>2.</b> a kitüntetett pontokat (zérushelyek, $y$-metszet, szélsőértékek, inflexió) · '
   r'<b>3.</b> összekötjük őket a táblázat szerinti ívekkel · <b>4.</b> a széleken az aszimptotákhoz, illetve a '
   r'végtelenbe simítjuk. A végén <b>ellenőrizzük</b>: minden pont és ív egyezik-e a táblázattal?</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos grafikonja „szép folytonos”: a pólusnál összeköti a két ágat, a maximumot a minimum fölé '
         r'rajzolja, mert „a maximum csak nagyobb lehet”, és a görbe a ferde aszimptotát újra meg újra metszi.</p>'
         r'<p><b>A grafikon nem lehet ellentmondásban a táblázattal.</b> A pólusnál a görbe szétszakad; a lokális '
         r'maximum lehet a minimum alatt (a fenti törtnél $1\lt9$); az aszimptotához a görbe a táblázat szerinti '
         r'oldalról simul.</p>'),
   doboz("erdekesseg", "Nem elég a GeoGebra?",
         r'<p>A számítógép is csak pontokat köt össze — ha rossz ablakot választasz, elbújik a szélsőérték, és a '
         r'pólusnál függőleges vonalat húz. A vizsgálat mondja meg, <b>hova kell nézni</b>. A kettő együtt a '
         r'legjobb: számolj, aztán ellenőrizd a géppel.</p>'),
   kviz(r'Az összesítő táblázat szerint az $(1;\,3)$ intervallumon $f\'\lt0$ és $f\'\'\gt0$. Milyen ott a görbe?',
        [r'csökken, és felfelé nyíló (∪) ívben hajlik', r'csökken, és lefelé nyíló (∩) ívben hajlik',
         r'nő, és felfelé nyíló (∪) ívben hajlik', r'nő, és lefelé nyíló (∩) ívben hajlik'], 0,
        jo="✔ f′ < 0 → csökken; f″ > 0 → konvex (∪). Pont így megy le a törtfüggvény jobb ága a minimumba.",
        nem="✘ A két előjelet külön kell olvasni: f′ < 0 → csökken, f″ > 0 → konvex, azaz felfelé nyíló ív."),
   GY(FV + "#alap-9", "A 9–10", FV + "#kozep-9", "K 9–12"),
 ]),

 ("🧾 Gyorsismétlő", [
   TABLA(["", ""], [
       ["<b>derivált</b>", "$f'(x_0)=\\lim\\limits_{\\Delta x\\to0}\\dfrac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x}$ — az érintő "
                           "meredeksége, a pillanatnyi változási sebesség"],
       ["<b>táblázat</b>", "$(x^n)'=nx^{n-1}$, $(\\sin x)'=\\cos x$, $(\\cos x)'=-\\sin x$, $(e^x)'=e^x$, "
                           "$(\\ln x)'=\\frac1x$ — a teljes táblázat: "
                           "<a href=\"tananyag-derivalasi-szabalyok.html#tetel-derivalt-tablazat\">A2</a>"],
       ["<b>szabályok</b>", "$(f\\pm g)'=f'\\pm g'$, $(fg)'=f'g+fg'$, $\\left(\\frac fg\\right)'=\\frac{f'g-fg'}{g^2}$, "
                            "$\\big(f(g(x))\\big)'=f'(g(x))\\,g'(x)$"],
       ["<b>érintő</b>", "$y-f(x_0)=f'(x_0)(x-x_0)$; normális: meredeksége $-\\frac1{f'(x_0)}$"],
       ["<b>monotonitás</b>", "$f'\\gt0$ → nő, $f'\\lt0$ → csökken; szélsőérték: $f'=0$ <b>és</b> előjelváltás"],
       ["<b>görbülés</b>", "$f''\\gt0$ → konvex ∪, $f''\\lt0$ → konkáv ∩; inflexió: $f''=0$ <b>és</b> előjelváltás"],
       ["<b>vizsgálat</b>", "ÉT → zérushely, előjel → paritás → aszimptoták → $f'$ → $f''$ → grafikon"]]),
   brief('<b>Nagol:</b> A deriválttal szétszedtük a függvényt: meredekség, fordulópont, hajlás. A következő '
         'fejezetben visszafelé megyünk — a darabokból rakjuk össze az egészet. <b>SZVETI</b> már vár a '
         '<i>Valóság Összefoltozásával</i>. <b>Véd Vilmos:</b> Integrál? Az meg mi? <b>Nagol:</b> A derivált '
         'fordítottja. És ne felejtsd el a $+C$-t.', outro=True),
 ]),
]


# ---------------------------------------------------------------- oldalak
def _prim(szakaszok):
    """A nyers stringekben a \\' (KaTeX-ben ékezet!) helyett sima vessző-prím: f\\'(x) → f'(x)."""
    return [(h2, [b.replace("\\'", "'") for b in blokkok]) for h2, blokkok in szakaszok]


C1, C2, C3 = (_prim(z) for z in (C1, C2, C3))
lapok = [
 lap(**T, fajl="tananyag-monotonitas-szelsoertek.html",
     cim="Hegyek és völgyek — monotonitás és szélsőérték",
     alcim="A derivált előjele és a monotonitás, a lokális szélsőérték feltételei, előjeltáblázat polinomra és "
           "törtfüggvényre.",
     chip=KUL + " · 6/8", szakaszok=C1,
     elozo=("tananyag-masodik-derivalt.html", "A második derivált"),
     kovetkezo=("tananyag-konvexitas-inflexio.html", "Konvexitás és inflexiós pont")),
 lap(**T, fajl="tananyag-konvexitas-inflexio.html",
     cim="Hogyan hajlik a görbe? — konvexitás és inflexiós pont",
     alcim="Konvex és konkáv függvény, a második derivált előjele, az inflexiós pont és a törtfüggvények görbülése.",
     chip=KUL + " · 7/8", szakaszok=C2,
     elozo=("tananyag-monotonitas-szelsoertek.html", "Monotonitás és szélsőérték"),
     kovetkezo=("tananyag-fuggvenyvizsgalat.html", "A teljes függvényvizsgálat")),
 lap(**T, fajl="tananyag-fuggvenyvizsgalat.html",
     cim="A teljes függvényvizsgálat — hét lépés a grafikonig",
     alcim="A vizsgálat lépései, egy polinom és egy racionális törtfüggvény teljes vizsgálata, az összesítő "
           "táblázat és a grafikon.",
     chip=KUL + " · 8/8", szakaszok=C3,
     elozo=("tananyag-konvexitas-inflexio.html", "Konvexitás és inflexiós pont"),
     kovetkezo=("feladatok-derivalas.html", "Zsoldos-lista I. — deriválás")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
