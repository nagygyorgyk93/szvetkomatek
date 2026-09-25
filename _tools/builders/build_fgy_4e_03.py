# -*- coding: utf-8 -*-
"""4e/03 — ket feladatgyujtemeny: Zsoldos-lista I. (derivalas) es II. (fuggvenyvizsgalat).
Feladat-terkep: projektek/4e/munkafajlok/terkep_fgy_03-derivalt.md (jovahagyva 2026-09-25).
Forras: 0_Feladatok - A fuggveny derivaltja.pdf (0_F 16-32.; a 16 b-d, 23 b, 23 e kulcsa javitva; a 26 d-ben
f'(1/2) helyett f'(2), mert a fuggveny az 1/2-ben nincs ertelmezve) + sajat feladatok.
Minden vegeredmeny sympybol; a derivalt-kulcsok a 0_F (javitott) kulcsabol, sympyvel numerikusan ellenorizve.
A 32. feladathoz (nincs forraskulcs) osszesito eredmeny + SVG-grafikon keszul (felhasznaloi dontes, 2026-09-25)."""
import sys, os, re, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal, w
from tananyag_common import svg_fuggvenyek
import sympy
from sympy import (Rational as Q, symbols, limit, oo, latex, sympify, S, simplify, fraction, together, solve, diff,
                   expand, sqrt, factor, Poly, nsimplify)
from sympy.parsing.sympy_parser import parse_expr

x = symbols("x", real=True)
LD = {"x": x, "Rational": Q, "sqrt": sympy.sqrt, "root": sympy.root, "log": sympy.log, "exp": sympy.exp,
      "sin": sympy.sin, "cos": sympy.cos, "tan": sympy.tan, "cot": sympy.cot, "pi": sympy.pi}
T = dict(tagozat="4e", mappa="03-derivalt", temakor="A függvény deriváltja")
KEK, PIROS, ZOLD, BORO, SOT, SZURKE, LILA = "#3b82f6", "#ef4444", "#047857", "#f59e0b", "#0f172a", "#64748b", "#7c3aed"
E = []


def Ex(s):
    return sympify(s, locals=LD)


_FN = {"sin": r"\sin", "cos": r"\cos", "tan": r"\operatorname{tg}", "cot": r"\operatorname{ctg}", "log": r"\ln"}


def _fn(m):
    nev, kit, arg = _FN[m.group(1)], m.group(2) or "", m.group(3).strip()
    if re.fullmatch(r"(\d+ )?x|\\frac\{1\}\{x\}", arg):
        return f"{nev}{kit} {arg.replace(' ', '')} "
    return f"{nev}{kit}\\left({arg}\\right)"


LDT = dict(LD, x=symbols("x"))          # megjelenítéshez feltevés nélküli x: a root(x**4, 3) ne legyen |x|^(4/3)


def TX(s):
    """sympy-szintaxisú string → TeX a leírt alakban (evaluate=False); sympy-kifejezés → TeX a kiértékelt alakban."""
    t = (latex(parse_expr(s, local_dict=LDT, evaluate=False), order="none") if isinstance(s, str)
         else latex(s, order="lex"))
    t = re.sub(r"\\(sin|cos|tan|cot|log)(\^\{\d+\})?\{\\left\((.*?) \\right\)\}", _fn, t)
    t = re.sub(r"(?<![\d.}])1 \\frac", r"\\frac", t)
    t = t.replace(r"\left(-1\right) ", "-")
    t = t.replace(r"\frac", r"\dfrac")
    t = re.sub(r"\^\{\\dfrac", r"^{\\frac", t)
    return re.sub(r"\s+", " ", t).strip()


def _pontok(f1, f2):
    """Legalább két olyan pont, ahol mindkét kifejezés valós és véges."""
    ki = []
    for t in (Q(7, 10), Q(13, 10), Q(21, 10), Q(37, 10), Q(-7, 10), Q(-17, 10), Q(1, 10), Q(-31, 10), Q(47, 10),
              Q(1, 3), Q(-1, 3)):
        try:
            a, b = complex(f1.subs(x, t).evalf(30)), complex(f2.subs(x, t).evalf(30))
        except (TypeError, ZeroDivisionError, ValueError):
            continue
        if abs(a.imag) > 1e-12 or abs(b.imag) > 1e-12 or not (math.isfinite(a.real) and math.isfinite(b.real)):
            continue
        ki.append((a.real, b.real))
    return ki


def egyenlo(nev, a, b):
    pts = _pontok(a, b)
    if len(pts) < 2 or any(abs(p - q) > 1e-8 * max(1, abs(p)) for p, q in pts):
        E.append((nev, a, b, len(pts)))


def DER(intro, tetelek, rend=1, jel="y"):
    """tetelek = [(függvény, derivált-kulcs), …] — a kulcs sympy-szintaxisban, szép alakban (TX rendereli);
    None = a sympy kibontott deriváltja (polinomnál)."""
    subs, ans = [], []
    vessz = "'" * rend
    for i, (e, k) in enumerate(tetelek):
        d = diff(Ex(e), x, rend)
        kk = expand(d) if k is None else Ex(k)
        egyenlo(f"{intro[:20]}…{i}", d, kk)
        subs.append(f"${jel}={TX(e)}$")
        ans.append(f"${jel}{vessz}={TX(kk if k is None else k)}$")
    return (intro, subs, ans)


def PT(a, b):
    return r"\left(" + latex(a) + r";\," + latex(b) + r"\right)"


def EGY(expr):
    """egyenes y = mx + b alakban"""
    return "y=" + latex(expand(expr), order="lex").replace(r"\frac", r"\dfrac")


def ERINTO(f, x0, y0=None):
    F = Ex(f); yy = F.subs(x, x0)
    if y0 is not None and yy != y0:
        E.append(("érintési pont", f, x0, yy, y0))
    m = diff(F, x).subs(x, x0)
    return yy, m, expand(m * (x - x0) + yy)


# ---------------------------------------------------------------- vizsgálati segédek
def polusok(F):
    return sorted([r for r in solve(fraction(together(F))[1], x) if r.is_real], key=float)


def krit(F, rend=1):
    d = together(diff(F, x, rend))
    return sorted([r for r in solve(fraction(d)[0], x) if r.is_real], key=float)


def _minta(G, a, b):
    if a == -oo:
        t = b - 1
    elif b == oo:
        t = a + 1
    else:
        t = (a + b) / 2
    return G.subs(x, t)


def _intv(a, b):
    return (r"\left(" + (r"-\infty" if a == -oo else latex(a)) + r";\," + (r"+\infty" if b == oo else latex(b))
            + r"\right)")


def _unio(L):
    """Intervallumok felsorolása „és”-sel: a függvény az egyes intervallumokon monoton, nem az uniójukon."""
    return " és ".join(f"${_intv(a, b)}$" for a, b in L) if L else "sehol"


def szakaszok(F, rend):
    G = diff(F, x, rend)
    pts = sorted(set(krit(F, rend)) | set(polusok(F)), key=float)
    hat = [-oo] + pts + [oo]
    poz, neg = [], []
    for i in range(len(hat) - 1):
        (poz if _minta(G, hat[i], hat[i + 1]) > 0 else neg).append((hat[i], hat[i + 1]))
    # szomszédos azonos előjelű szakaszok összevonása, ha a határ nem pólus
    def ossze(L):
        ki = []
        for a, b in L:
            if ki and ki[-1][1] == a and a not in polusok(F):
                ki[-1] = (ki[-1][0], b)
            else:
                ki.append((a, b))
        return ki
    return ossze(poz), ossze(neg)


def szelso(F):
    d = diff(F, x)
    mx, mn = [], []
    for c in krit(F):
        bal, jobb = d.subs(x, c - Q(1, 1000)), d.subs(x, c + Q(1, 1000))
        if bal > 0 > jobb:
            mx.append((c, simplify(F.subs(x, c))))
        elif bal < 0 < jobb:
            mn.append((c, simplify(F.subs(x, c))))
    return mx, mn


def inflexio(F):
    d2 = diff(F, x, 2)
    return [(c, simplify(F.subs(x, c))) for c in krit(F, 2)
            if d2.subs(x, c - Q(1, 1000)) * d2.subs(x, c + Q(1, 1000)) < 0]


def MONO(e):
    F = Ex(e)
    poz, neg = szakaszok(F, 1)
    mx, mn = szelso(F)
    t = f"nő: {_unio(poz)}; csökken: {_unio(neg)}"
    if mx:
        t += "; lokális maximum: " + ", ".join(f"${PT(a, b)}$" for a, b in mx)
    if mn:
        t += "; lokális minimum: " + ", ".join(f"${PT(a, b)}$" for a, b in mn)
    if not mx and not mn:
        t += "; szélsőérték nincs"
    stac = [c for c in krit(F) if c not in [a for a, _ in mx + mn]]
    if stac:
        t += ("; az " + " és az ".join(f"$x={latex(c)}$" for c in stac) + " helyen $f'=0$, de ott nincs szélsőérték "
              "($f'$ nem vált előjelet)")
    return t


def GORB(e):
    F = Ex(e)
    poz, neg = szakaszok(F, 2)
    inf = inflexio(F)
    t = f"konvex: {_unio(poz)}; konkáv: {_unio(neg)}"
    t += ("; inflexiós pont: " + ", ".join(f"${PT(a, b)}$" for a, b in inf)) if inf else "; inflexiós pont nincs"
    return t


def fugg_vonal(svg, x0, xr, w=360, h=250, szin=SZURKE):
    bal, jobb, fent, lent = 26, 12, 14, 22
    X = bal + (x0 - xr[0]) / (xr[1] - xr[0]) * (w - bal - jobb)
    vonal = (f'  <line x1="{X:.1f}" y1="{fent}" x2="{X:.1f}" y2="{h - lent}" stroke="{szin}" '
             'stroke-width="1.6" stroke-dasharray="6 4"/>')
    i = svg.find("  </g>") + len("  </g>")
    return svg[:i] + "\n" + vonal + svg[i:]


def svgwrap(svg):
    return f'<div class="svgwrap">{svg}</div>'


def GRAFIKON(e, nev):
    F = Ex(e); f = sympy.lambdify(x, F, "math")
    pol = [float(p) for p in polusok(F)]
    mx, mn = szelso(F); inf = inflexio(F)
    nul = [r for r in solve(fraction(together(F))[0], x) if r.is_real]
    kulcs = [float(a) for a, _ in mx + mn + inf] + [float(r) for r in nul] + pol + [0.0]
    x0, x1 = min(kulcs) - 1.6, max(kulcs) + 1.6
    # a függőleges tartományt a kitüntetett pontok adják (a meredek ágakat a rajz levágja)
    ys = [float(b) for _, b in mx + mn + inf] + [0.0]
    if 0 not in pol:
        ys.append(float(F.subs(x, 0)))
    lo, hi = min(ys), max(ys)
    pad = max(2.0, (hi - lo) * 0.6)
    yr = (lo - pad, hi + pad)
    szak, eleje = [], x0
    for p in pol:
        szak.append((eleje, p - 0.02)); eleje = p + 0.02
    szak.append((eleje, x1))
    gorbek = [(f, KEK, "f", szak)]
    h = limit(F, x, oo)
    if h not in (oo, -oo):
        gorbek.append((lambda t, h=float(h): h, SZURKE, f"y = {latex(h)}", [(x0, x1)], "szaggatott"))
    elif Poly(fraction(together(F))[0], x).degree() - Poly(fraction(together(F))[1], x).degree() == 1:
        k = limit(F / x, x, oo); n_ = limit(F - k * x, x, oo)
        gorbek.append((lambda t, k=float(k), n=float(n_): k * t + n, SZURKE, "ferde aszimptota", [(x0, x1)], "szaggatott"))
    pontok = ([(float(a), float(b), "max", ZOLD, -12, -8) for a, b in mx] +
              [(float(a), float(b), "min", PIROS, -10, 16) for a, b in mn] +
              [(float(a), float(b), "", LILA) for a, b in inf])
    svg = svg_fuggvenyek(gorbek, xr=(x0, x1), yr=yr, w=360, h=250, jelmagyarazat=False, pontok=pontok,
                         leiras=f"A {nev} feladat függvényének grafikonja a szélsőérték- és inflexiós pontokkal")
    for p in pol:
        svg = fugg_vonal(svg, p, (x0, x1))
    return svgwrap(svg)


def PARITAS(F):
    if simplify(F.subs(x, -x) - F) == 0:
        return "páros"
    if simplify(F.subs(x, -x) + F) == 0:
        return "páratlan"
    return "nem páros és nem páratlan"


def TELJES(e, nev):
    """A 32. feladat kulcsa: összesítő eredmény + grafikon."""
    F = Ex(e)
    pol = polusok(F)
    et = r"\mathbb R" if not pol else r"\mathbb R\setminus\{" + r";\,".join(latex(p) for p in pol) + r"\}"
    gyok = sympy.roots(Poly(fraction(together(F))[0], x))
    nul = sorted([r for r in gyok if r.is_real], key=float)
    nt = ", ".join(f"${latex(r)}$" + (" (kétszeres)" if gyok[r] == 2 else "") for r in nul)
    t = [f"$D_f={et}$", ("zérushelyek: " if len(nul) > 1 else "zérushely: ") + (nt if nul else "nincs"),
         f"$f(0)={latex(F.subs(x, 0))}$" if 0 not in pol else "", PARITAS(F)]
    hat = [-oo] + sorted(set(nul) | set(pol), key=float) + [oo]
    poz = [(hat[i], hat[i + 1]) for i in range(len(hat) - 1) if _minta(F, hat[i], hat[i + 1]) > 0]
    neg = [(hat[i], hat[i + 1]) for i in range(len(hat) - 1) if _minta(F, hat[i], hat[i + 1]) < 0]
    t.append(f"$f(x)\\gt0$: {_unio(poz)}; $f(x)\\lt0$: {_unio(neg)}")
    vl = lambda v: r"+\infty" if v == oo else r"-\infty" if v == -oo else latex(v)
    t.append(f"$\\lim\\limits_{{x\\to-\\infty}}f(x)={vl(limit(F.subs(x, -x), x, oo))}$, "
             f"$\\lim\\limits_{{x\\to+\\infty}}f(x)={vl(limit(F, x, oo))}$")
    asz = [f"$x={latex(p)}$ (függőleges; $\\lim\\limits_{{x\\to{latex(p)}-0}}f(x)={vl(limit(F, x, p, '-'))}$, "
           f"$\\lim\\limits_{{x\\to{latex(p)}+0}}f(x)={vl(limit(F, x, p, '+'))}$)" for p in pol]
    h = limit(F, x, oo)
    if h not in (oo, -oo):
        asz.append(f"$y={latex(h)}$ (vízszintes)")
    elif Poly(fraction(together(F))[0], x).degree() - Poly(fraction(together(F))[1], x).degree() == 1:
        k = limit(F / x, x, oo); n_ = limit(F - k * x, x, oo)
        asz.append(f"$y={latex(expand(k * x + n_))}$ (ferde)")
    t.append(((("aszimptoták: " if len(asz) > 1 else "aszimptota: ") + ", ".join(asz)) if asz else "aszimptota nincs"))
    t += [MONO(e), GORB(e)]
    return "; ".join(s for s in t if s) + GRAFIKON(e, nev)


def ELOJEL_TABLA(oszl, sor):
    th = "<th>$x$</th>" + "".join(f"<th>{c}</th>" for c in oszl)
    tr = "".join(f"<tr><th>{c}</th>" + "".join(f"<td>{v}</td>" for v in cs) + "</tr>" for c, cs in sor)
    return '<div class="svgwrap">' + w(f'<table class="tt-table"><tr>{th}</tr>{tr}</table>') + '</div>'


# ================================================================ ZSOLDOS-LISTA I.
# ---- ábrák
_fA2 = lambda t: (t * t - 4 * t) / 2
SVG_A2 = svg_fuggvenyek(
    [(_fA2, KEK, "f", [(-0.9, 5.2)]), (lambda t: -2 * t, ZOLD, "e₁", [(-0.7, 0.9)]),
     (lambda t: -2.0, BORO, "e₂", [(1.0, 3.0)]), (lambda t: 2 * t - 8, PIROS, "e₃", [(3.1, 4.9)])],
    xr=(-1.2, 5.6), yr=(-3.2, 3.0), w=360, h=250,
    pontok=[(0, 0, "", SOT), (2, -2, "", SOT), (4, 0, "", SOT)],
    leiras="Az f(x) = (x² − 4x)/2 parabola és három érintője: a 0-ban −2, a 2-ben 0, a 4-ben 2 meredekségű")
_fK1 = lambda t: t ** 3 / 3 - t * t - 3 * t + 2
SVG_K1 = svg_fuggvenyek([(_fK1, KEK, "f", [(-2.7, 5.2)])], xr=(-3, 5.6), yr=(-8, 6.5), w=360, h=250,
                        jelmagyarazat=False,
                        pontok=[(-1, 11 / 3, "", SOT), (3, -7, "", SOT)],
                        leiras="Egy harmadfokú függvény grafikonja: az x = −1 helyen csúcs, az x = 3 helyen völgy")

A_I = [
 ("Számítsd ki az $f$ függvény $\\Delta y$ növekményét és a $\\dfrac{\\Delta y}{\\Delta x}$ differenciahányadost! "
  "(Ahol kell, két tizedesjegyre kerekíts.)",
  [r"$f(x)=x^2$, $x_0=1$, $\Delta x=0{,}5$", r"$f(x)=x^2$, $x_0=5$, $\Delta x=0{,}5$",
   r"$f(x)=\sqrt x$, $x_0=0$, $\Delta x=0{,}6$", r"$f(x)=\sqrt x$, $x_0=5$, $\Delta x=0{,}6$"],
  [r"$\Delta y=1{,}25$, $\dfrac{\Delta y}{\Delta x}=2{,}5$", r"$\Delta y=5{,}25$, $\dfrac{\Delta y}{\Delta x}=10{,}5$",
   r"$\Delta y\approx0{,}77$, $\dfrac{\Delta y}{\Delta x}\approx1{,}29$",
   r"$\Delta y\approx0{,}13$, $\dfrac{\Delta y}{\Delta x}\approx0{,}22$"]),
 (r"Az ábrán az $f$ függvény grafikonja és három érintője látható (a rács egysége $1$). Olvasd le a derivált "
  r"értékét az érintők meredekségéből!" + svgwrap(SVG_A2),
  [r"$f'(0)$", r"$f'(2)$", r"$f'(4)$"], [r"$-2$", r"$0$ (vízszintes érintő)", r"$2$"], True),
 DER("Deriváld a függvényeket!", [("3*x**2-2*x+6", None), ("x**3+3*x**2-5*x+2", None),
     ("Rational(2,3)*x**9-x**6+2*x**3-3*x**2+6*x-1", None), ("x**8-Rational(4,3)*x**6-2*x**4-4*x**2-8*x-1", None)]),
 DER("Deriváld a függvényeket!", [("sqrt(3)/4*x**4+x**3+sqrt(2)/2*x**2+x+1", "sqrt(3)*x**3+3*x**2+sqrt(2)*x+1"),
     ("(4*x+5)/3", "Rational(4,3)"), ("5*x**3-x/2+4", None), ("x**4/2-Rational(3,4)*x**2", None)]),
 DER("Deriváld a függvényeket! (Írd át a törteket negatív kitevős hatvánnyá.)",
     [("1/(3*x**4)", "-4/(3*x**5)"), ("1/x+1/x**2+1/x**3", "-1/x**2-2/x**3-3/x**4"),
      ("x+1/x**2-1/(5*x**5)", "1-2/x**3+1/x**6")]),
 DER("Deriváld a függvényeket! (Írd át a gyököket törtkitevős hatvánnyá.)",
     [("x**3*sqrt(x)", "Rational(7,2)*sqrt(x**5)"), ("x*root(x,3)", "Rational(4,3)*root(x,3)"),
      ("x**2*root(x,3)", "Rational(7,3)*root(x**4,3)")]),
 DER("Deriváld a szorzatokat!", [("(2*x+1)*(x**2+3*x-1)", "6*x**2+14*x+1"),
     ("(2*x**2-x)*(x**3+5*x-1)", "10*x**4-4*x**3+30*x**2-14*x+1"), ("x**3*sin(x)", "3*x**2*sin(x)+x**3*cos(x)"),
     ("x*exp(x)", "(x+1)*exp(x)")]),
 DER("Deriváld a függvényeket!", [("sin(x)+tan(x)", "cos(x)+1/cos(x)**2"), ("x**2-3*log(x)", "(2*x**2-3)/x"),
     ("x*log(x)", "1+log(x)")]),
 ("Deriváld a függvényt, majd számítsd ki a derivált értékét az adott helyen!",
  [r"$f(x)=\dfrac14x^4-4x^2+16$, $f'(2)$", r"$f(x)=\dfrac32x^4+4x^3-\dfrac12x^2+5x-7$, $f'(-1)$",
   r"$f(x)=-x^3+9x^2+x-1$, $f'(-1)$"],
  [r"$f'(x)=x^3-8x$, $f'(2)=-8$", r"$f'(x)=6x^3+12x^2-x+5$, $f'(-1)=12$", r"$f'(x)=-3x^2+18x+1$, $f'(-1)=-20$"]),
 ("Írd fel az $f$ függvény grafikonjának érintőjét az adott $P$ pontban!",
  [r"$f(x)=\dfrac12x^2+2x+1$, $P(2;\,y)$", r"$f(x)=-\dfrac12x^2+2x-3$, $P(4;\,y)$"],
  [r"$P(2;\,7)$, $y=4x-1$", r"$P(4;\,-3)$, $y=-2x+5$"]),
 ("Írd fel az $f$ függvény grafikonjának érintőjét az adott $P$ pontban!",
  [r"$f(x)=\dfrac12x^2+\dfrac12x-3$, $P(1;\,-2)$", r"$f(x)=-\dfrac12x^2+\dfrac32x+2$, $P(0;\,2)$"],
  [r"$y=\dfrac32x-\dfrac72$", r"$y=\dfrac32x+2$"]),
 ("Írd fel az $f$ függvény grafikonjának érintőjét az adott $P$ pontban!",
  [r"$f(x)=-3x^3+3x^2+3x+3$, $P(-1;\,y)$", r"$f(x)=-2x^3-2x^2+2x-2$, $P(1;\,y)$"],
  [r"$P(-1;\,6)$, $y=-12x-6$", r"$P(1;\,-4)$, $y=-8x+4$"]),
 (r"Változási sebesség. Egy futó $t$ másodperc alatt $s(t)=t^2+4t$ métert tesz meg (a–c).",
  [r"Mekkora a futó átlagsebessége az első $3$ másodpercben?", r"Mekkora a pillanatnyi sebessége $t=3$ s-kor?",
   r"Mikor éri el a $14\ \tfrac{\text{m}}{\text{s}}$ sebességet?",
   r"Egy medencében a víz magassága $t$ perc múlva $h(t)=120-3t+0{,}02t^2$ cm. Milyen ütemben változik a "
   r"vízszint $t=10$ perckor?"],
  [r"$\dfrac{s(3)}{3}=\dfrac{21}{3}=7\ \tfrac{\text{m}}{\text{s}}$", r"$v(t)=s'(t)=2t+4$, $v(3)=10\ \tfrac{\text{m}}{\text{s}}$",
   r"$2t+4=14$, $t=5$ s-kor", r"$h'(t)=-3+0{,}04t$, $h'(10)=-2{,}6$: percenként $2{,}6$ cm-t csökken"]),
 DER("Deriváld az összetett függvényeket!", [("(3*x-4)**4", "12*(3*x-4)**3"), ("(x**2-x+1)**5", "(10*x-5)*(x**2-x+1)**4"),
     ("sqrt(2*x-5)", "1/sqrt(2*x-5)"), ("sqrt(1-x**2)", "-x/sqrt(1-x**2)")]),
 DER("Deriváld az összetett függvényeket!", [("2*sqrt(3*x-2)", "3/sqrt(3*x-2)"), ("Rational(3,4)*cos(4*x)", "-3*sin(4*x)"),
     ("exp(-x**2)", "-2*x*exp(-x**2)"), ("log(3*x-1)", "3/(3*x-1)")]),
 DER("Deriváld az összetett függvényeket!", [("sqrt(x**2-4*x+3)", "(x-2)/sqrt(x**2-4*x+3)"),
     ("1/sqrt(4*x-1)", "-2/sqrt((4*x-1)**3)"), ("sqrt(x**2+8*x+15)", "(x+4)/sqrt(x**2+8*x+15)")]),
 DER("Határozd meg a függvények második deriváltját!", [("x**4/2-9*x**2+x+Rational(1,2)", "6*x**2-18"),
     ("x**4/3-4*x**2+7*x-Rational(1,3)", "4*x**2-8"), ("x**4-Rational(2,3)*x**3-x**2/2+7*x+3", "12*x**2-4*x-1"),
     ("2*sin(x)-3*cos(x)", "-2*sin(x)+3*cos(x)")], rend=2),
 (r"Sebesség és gyorsulás. Egy test helyzete $t$ másodperc múlva $s(t)=t^3-6t^2+9t$ méter.",
  [r"Írd fel a $v(t)$ sebességet és az $a(t)$ gyorsulást!", r"Mikor áll meg a test (mikor $v(t)=0$)?",
   r"Mekkora a gyorsulás $t=2$ s-kor, és mit jelent ez?"],
  [r"$v(t)=3t^2-12t+9$ $\tfrac{\text{m}}{\text{s}}$, $a(t)=6t-12$ $\tfrac{\text{m}}{\text{s}^2}$",
   r"$3(t-1)(t-3)=0$: $t=1$ s-kor és $t=3$ s-kor — ott pillanatnyilag megáll és irányt vált",
   r"$a(2)=0$: ebben a pillanatban a sebesség változási üteme $0$; a sebesség itt a legkisebb, $v(2)=-3\ "
   r"\tfrac{\text{m}}{\text{s}}$ — a test ekkor halad a leggyorsabban visszafelé"]),
]

K_I = [
 (r"Az ábrán egy $f$ függvény grafikonja látható. Hol pozitív, hol negatív és hol nulla az $f'$ derivált? "
  r"Indokold a grafikon alapján!" + svgwrap(SVG_K1), None,
  r"$f'(x)=0$ az $x=-1$ és az $x=3$ helyen (vízszintes érintő); $f'(x)\gt0$, ha $x\lt-1$ vagy $x\gt3$ (ott a "
  r"görbe emelkedik); $f'(x)\lt0$ a $(-1;\,3)$ intervallumon (ott süllyed)"),
 DER("Deriváld a függvényeket!", [("x+sin(x)*cos(x)", "2*cos(x)**2"), ("x-sin(x)*cos(x)", "2*sin(x)**2"),
     ("tan(x)-cot(x)", "1/(sin(x)**2*cos(x)**2)"), ("(2*x**2-3*x)*exp(x)", "(2*x**2+x-3)*exp(x)"),
     ("log(x)/x**2", "(1-2*log(x))/x**3")]),
 DER("Deriváld a hányadosokat!", [("(x**2+x-2)/(x-2)", "(x**2-4*x)/(x-2)**2"), ("(x**2-x-2)/(x+2)", "(x**2+4*x)/(x+2)**2"),
     ("(x**2-2*x+1)/(x**2+1)", "2*(x**2-1)/(x**2+1)**2"), ("(x**2-x+1)/(x**2+1)", "(x**2-1)/(x**2+1)**2")]),
 DER("Deriváld a hányadosokat!", [("-6*x/(x**2+3)", "6*(x**2-3)/(x**2+3)**2"), ("-8*x/(x**2+4)", "8*(x**2-4)/(x**2+4)**2"),
     ("sin(x)/(1-cos(x))", "-1/(1-cos(x))"), ("cos(x)/(1+sin(x))", "-1/(1+sin(x))"),
     ("(1+sin(x))/(1+cos(x))", "(1+sin(x)+cos(x))/(1+cos(x))**2"), ("(2+log(x))/(1-log(x))", "3/(x*(1-log(x))**2)")]),
 ("Deriválj, majd számolj!",
  [r"$f(x)=\dfrac14x^3+\dfrac{\sqrt2}{2}x^2-7x+2\pi$, $f'\big(\sqrt2\big)=?$",
   r"$f(x)=x^3+\dfrac5x$, $f'(2)+f'(-2)=?$", r"$f(x)=x^2-\dfrac{1}{2x^2}$, $f'(2)-f'(-2)=?$",
   r"Mutasd meg, hogy az $f(x)=\dfrac12x^2+x+1$ függvényre $2f(x)-\big(f'(x)\big)^2=1$!"],
  [r"$f'(x)=\dfrac34x^2+\sqrt2x-7$, $f'\big(\sqrt2\big)=-\dfrac72$", r"$f'(x)=3x^2-\dfrac5{x^2}$, az összeg $\dfrac{43}{2}$",
   r"$f'(x)=2x+\dfrac1{x^3}$, a különbség $\dfrac{33}{4}$",
   r"$f'(x)=x+1$, így $x^2+2x+2-(x+1)^2=1$ ✓"]),
 ("Írd fel az érintő egyenletét az adott pontban!",
  [r"$f(x)=2x^3+\dfrac12x^2-2x+\dfrac12$, $P(-1;\,1)$", r"$f(x)=\dfrac23x^3+3x^2+3x+\dfrac13$, $P(1;\,7)$",
   r"Írd fel az a) rész $P$ pontjában a <b>normális</b> (a $P$-ben az érintőre merőleges egyenes) egyenletét is!"],
  [r"$y=3x+4$", r"$y=11x-4$", r"$m_n=-\dfrac13$: $y=-\dfrac13x+\dfrac23$"]),
 (r"Legyen $f(x)=x^3-12x+1$.",
  [r"Mely pontokban párhuzamos a grafikon érintője az $y=15x$ egyenessel? Írd fel ezeket az érintőket!",
   r"Hol vízszintes az érintő? Írd fel ezeket az érintőket is!"],
  [r"$f'(x)=3x^2-12=15$, $x=\pm3$: a $(3;\,-8)$ pontban $y=15x-53$, a $(-3;\,10)$ pontban $y=15x+55$",
   r"$3x^2-12=0$, $x=\pm2$: $y=-15$ (a $(2;\,-15)$ pontban) és $y=17$ (a $(-2;\,17)$ pontban)"]),
 ("Írd fel a törtfüggvény grafikonjának érintőjét az adott helyen!",
  [r"$f(x)=\dfrac{x+3}{x-1}$, $x_0=3$", r"$f(x)=\dfrac{x}{x^2+1}$, $x_0=0$"],
  [r"$f(3)=3$, $f'(x)=-\dfrac{4}{(x-1)^2}$, $f'(3)=-1$: $y=-x+6$",
   r"$f(0)=0$, $f'(x)=\dfrac{1-x^2}{(x^2+1)^2}$, $f'(0)=1$: $y=x$"]),
 DER("Deriváld az összetett függvényeket!", [("root(1-3*x,3)", "-1/root((1-3*x)**2,3)"),
     ("root(2*x**3-3*x**2,3)", "(2*x**2-2*x)/root((2*x**3-3*x**2)**2,3)"), ("cos(1/x)", "sin(1/x)/x**2"),
     ("cot(1/x)", "1/(x**2*sin(1/x)**2)")]),
 DER("Deriváld az összetett függvényeket!", [("tan(x)**3", "3*sin(x)**2/cos(x)**4"),
     ("sin(x)**2-cos(x)**2", "4*sin(x)*cos(x)"), ("Rational(1,2)*tan(4*x)", "2/cos(4*x)**2"),
     ("-Rational(1,3)*cot(x)**6", "2*cos(x)**5/sin(x)**7"), ("Rational(1,4)*sin(x)**4", "sin(x)**3*cos(x)")]),
 ("Deriváld az összetett függvényt, és ahol kérik, számítsd ki a derivált értékét!",
  [r"$f(x)=\left(3x^2-4\right)^4$, $f'(-1)$", r"$f(x)=\left(x^2-3x+2\right)^5$, $f'(3)$", r"$f(x)=(x-2)e^{2x}$, $f'(0)$",
   r"$f(x)=3\ln\dfrac{x-1}{x+1}$, $f'(2)$", r"$y=e^{\frac1x}$", r"$y=\ln\dfrac{1-x}{1+x}$"],
  [r"$f'(x)=24x\left(3x^2-4\right)^3$, $f'(-1)=24$", r"$f'(x)=(10x-15)\left(x^2-3x+2\right)^4$, $f'(3)=240$",
   r"$f'(x)=(2x-3)e^{2x}$, $f'(0)=-3$", r"$f'(x)=\dfrac{6}{x^2-1}$, $f'(2)=2$", r"$y'=-\dfrac{1}{x^2}e^{\frac1x}$",
   r"$y'=\dfrac{2}{x^2-1}$"]),
 DER("Határozd meg a függvények második deriváltját!", [("(1-x)/(1+x)", "4/(x+1)**3"), ("x/(x**2+4)", "(2*x**3-24*x)/(x**2+4)**3"),
     ("x**2/2+2/x**2", "(x**4+12)/x**4"), ("x**2/3+3/x**2", "(2*x**4+54)/(3*x**4)"), ("(x**2-x-2)/(x-3)", "8/(x-3)**3"),
     ("(x**2+x-2)/(x+3)", "8/(x+3)**3"), ("x**2*log(x)", "2*log(x)+3"), ("x*log(x)+2*x", "1/x")], rend=2),
]

N_I = [
 ("Igazold az egyenlőségeket!",
  [r"Legyen $f(x)=\dfrac23x^3+\dfrac12x^2-\dfrac37x$ és $g(x)=2x^3-\dfrac92x^2-2x$. Igazold, hogy "
   r"$7f'\!\left(-\dfrac12\right)+g'\!\left(-\dfrac12\right)=1$!",
   r"Igazold, hogy az $f(x)=2x^2-1$ függvényre $\left(x^2-1\right)f''(x)+xf'(x)-4f(x)=0$!"],
  [r"$f'(x)=2x^2+x-\dfrac37$, $f'\!\left(-\dfrac12\right)=-\dfrac37$; $g'(x)=6x^2-9x-2$, $g'\!\left(-\dfrac12\right)=4$; "
   r"$7\cdot\left(-\dfrac37\right)+4=1$ ✓",
   r"$f'=4x$, $f''=4$: $4x^2-4+4x^2-8x^2+4=0$ ✓"]),
 ("Igazold, hogy a függvények deriváltja a megadott kifejezés (ahol a függvény értelmezve van)!",
  [r"$f(x)=\dfrac13\operatorname{tg}^3x+\operatorname{tg}x$ esetén $f'(x)=\dfrac{1}{\cos^4x}$",
   r"$f(x)=\dfrac13\operatorname{ctg}^3x+\operatorname{ctg}x$ esetén $f'(x)=-\dfrac{1}{\sin^4x}$"],
  [r"$f'=\left(\operatorname{tg}^2x+1\right)\dfrac{1}{\cos^2x}=\dfrac{1}{\cos^2x}\cdot\dfrac{1}{\cos^2x}$ ✓",
   r"$f'=-\left(\operatorname{ctg}^2x+1\right)\dfrac{1}{\sin^2x}=-\dfrac{1}{\sin^4x}$ ✓"]),
 ("Érintő külső pontból és érintési feltétel.",
  [r"Írd fel az $f(x)=x^2-2x+4$ parabola azon érintőit, amelyek átmennek az origón!",
   r"Melyik $c$ értékre érinti az $y=3x+c$ egyenes az $f(x)=x^2+x$ grafikonját?"],
  [r"az $a$ helyen húzott érintő: $y=(2a-2)(x-a)+a^2-2a+4$; az origón átmegy, ha $4-a^2=0$, $a=\pm2$: $y=2x$ "
   r"(a $(2;\,4)$ pontban) és $y=-6x$ (a $(-2;\,12)$ pontban)",
   r"$f'(x)=2x+1=3$, $x=1$, $f(1)=2$, tehát $2=3+c$, $c=-1$"]),
]
JOKER_I = (r"🃏 <b>Véd Vilmos rejtvénye.</b> Adj meg egy olyan $f$ függvényt, amelynek a deriváltja $f'(x)=2x$, és a "
           r"grafikonja átmegy az $(1;\,5)$ ponton! Hány ilyen függvény van?",
           r"$f(x)=x^2+4$ — pontosan egy. (Az összes $f'(x)=2x$ deriváltú függvény $x^2+C$ alakú; az $(1;\,5)$ pont "
           r"$C=4$-et adja. Ez már a 04. témakör, az integrál előszele.)", None)

# ================================================================ ZSOLDOS-LISTA II.
_fA6 = lambda t: t * t - t - 2
SVG_A6 = svg_fuggvenyek([(_fA6, BORO, "f′", [(-2.4, 3.4)])], xr=(-2.8, 3.8), yr=(-3, 4.5), w=360, h=230,
                        pontok=[(-1, 0, "", SOT), (2, 0, "", SOT)],
                        leiras="Az f′ deriváltfüggvény grafikonja: felfelé nyíló parabola, zérushelyei −1 és 2")
SVG_A7 = svg_fuggvenyek(
    [(lambda t: 3.0 - 0.9 * (t - 1.9) ** 2, KEK, "A", [(0.3, 1.9)]),
     (lambda t: 0.6 + 0.9 * (t - 3.9) ** 2, BORO, "B", [(2.3, 3.9)]),
     (lambda t: 0.6 + 0.9 * (t - 4.3) ** 2, ZOLD, "C", [(4.3, 5.9)]),
     (lambda t: 3.0 - 0.9 * (t - 6.3) ** 2, PIROS, "D", [(6.3, 7.9)])],
    xr=(-0.2, 8.2), yr=(-0.3, 4.2), w=360, h=230,
    leiras="Négy görbedarab: A növekvő, lefelé nyíló; B csökkenő, felfelé nyíló; C növekvő, felfelé nyíló; D csökkenő, "
           "lefelé nyíló ív")
SVG_A10 = svg_fuggvenyek([(lambda t: t ** 3 - 3 * t, KEK, "f", [(-2.1, 2.1)])], xr=(-2.6, 2.6), yr=(-3, 3), w=360, h=230,
                         jelmagyarazat=False, pontok=[(-1, 2, "", SOT), (1, -2, "", SOT), (0, 0, "", LILA)],
                         leiras="Egy harmadfokú függvény grafikonja: a −1-ben csúcs, az 1-ben völgy, az origóban "
                                "inflexiós pont")
TABLA_A1 = ELOJEL_TABLA(["$(-\\infty;\\,-2)$", "$-2$", "$(-2;\\,1)$", "$1$", "$(1;\\,+\\infty)$"],
                        [("$f'(x)$", ["$+$", "$0$", "$-$", "$0$", "$+$"])])

A_II = [
 (r"Egy $f$ függvény deriváltjának előjeltáblázata látható; tudjuk továbbá, hogy $f(-2)=5$ és $f(1)=-4$." + TABLA_A1,
  [r"Hol nő és hol csökken $f$?", r"Hol és mekkora szélsőértéke van?"],
  [r"nő: $(-\infty;\,-2)$ és $(1;\,+\infty)$; csökken: $(-2;\,1)$",
   r"lokális maximum az $x=-2$ helyen, értéke $5$ ($+\to-$ váltás); lokális minimum az $x=1$ helyen, értéke $-4$ "
   r"($-\to+$ váltás)"]),
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=x^3-2x^2+x-2$", r"$f(x)=\dfrac23x^3-x^2-4x$"],
  [MONO("x**3-2*x**2+x-2"), MONO("Rational(2,3)*x**3-x**2-4*x")]),
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=x^3+3x^2-4$", r"$f(x)=-x^3+3x+2$"], [MONO("x**3+3*x**2-4"), MONO("-x**3+3*x+2")]),
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=-x^3+9x^2-15x+3$", r"$f(x)=2x^3+3x^2-12x+1$"], [MONO("-x**3+9*x**2-15*x+3"), MONO("2*x**3+3*x**2-12*x+1")]),
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=2x^3-6x+1$", r"$f(x)=-x^3+6x^2-9x+1$"], [MONO("2*x**3-6*x+1"), MONO("-x**3+6*x**2-9*x+1")]),
 (r"Az ábrán egy $f$ függvény <b>deriváltjának</b>, az $f'$-nek a grafikonja látható." + svgwrap(SVG_A6),
  [r"Hol nő és hol csökken az $f$ függvény?", r"Melyik helyen van $f$-nek lokális maximuma, és melyiken minimuma?"],
  [r"$f'\gt0$, ha $x\lt-1$ vagy $x\gt2$: ott $f$ nő; $f'\lt0$ a $(-1;\,2)$ intervallumon: ott csökken",
   r"maximum az $x=-1$ helyen ($f'$ ott $+$-ból $-$-ba vált), minimum az $x=2$ helyen"]),
 (r"Melyik görbedarab konvex és melyik konkáv? Figyelj: a monotonitás nem számít!" + svgwrap(SVG_A7), None,
  r"konvex (felfelé nyíló): <b>B</b> és <b>C</b>; konkáv (lefelé nyíló): <b>A</b> és <b>D</b>"),
 ("Az $f$ függvény második deriváltja adott. Hol konvex, hol konkáv $f$, és hol van inflexiós helye?",
  [r"$f''(x)=6x-18$", r"$f''(x)=12x^2-12$", r"$f''(x)=4$"],
  [r"konkáv: $(-\infty;\,3)$; konvex: $(3;\,+\infty)$; inflexiós hely: $x=3$",
   r"konvex: $(-\infty;\,-1)$ és $(1;\,+\infty)$; konkáv: $(-1;\,1)$; inflexiós helyek: $x=-1$ és $x=1$",
   r"mindenütt konvex; inflexiós hely nincs"]),
 ("A teljes vizsgálat első lépései: add meg az értelmezési tartományt, a zérushelyeket, az $f(0)$ értéket, a paritást "
  "és az előjelet!",
  [r"$f(x)=(1-x)(x+2)^2$", r"$f(x)=(x+2)(x-1)^2$"],
  [r"$D_f=\mathbb R$; zérushelyek: $1$ és $-2$ (kétszeres); $f(0)=4$; nem páros és nem páratlan; $f(x)\gt0$, ha "
   r"$x\lt1$ ($x\ne-2$), $f(x)\lt0$, ha $x\gt1$",
   r"$D_f=\mathbb R$; zérushelyek: $-2$ és $1$ (kétszeres); $f(0)=2$; nem páros és nem páratlan; $f(x)\lt0$, ha "
   r"$x\lt-2$, $f(x)\gt0$, ha $x\gt-2$ ($x\ne1$)"]),
 (r"Melyik leírás illik az ábrán látható grafikonhoz? Indokold!" + svgwrap(SVG_A10),
  [r"nő a $(-\infty;\,-1)$-en, csökken a $(-1;\,1)$-en, nő az $(1;\,+\infty)$-en; az origó inflexiós pont",
   r"csökken a $(-\infty;\,-1)$-en, nő a $(-1;\,1)$-en, csökken az $(1;\,+\infty)$-en",
   r"mindenütt nő, és konvex"],
  r"az <b>a)</b> leírás: a görbe a $-1$-ig emelkedik (csúcs), az $1$-ig süllyed (völgy), utána emelkedik; az "
  r"origóban a hajlás irányt vált"),
]

K_II = [
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=-\dfrac12x^4-2x^3-2x^2+2$", r"$f(x)=-\dfrac34x^4+5x^3-6x^2-12$"],
  [MONO("-x**4/2-2*x**3-2*x**2+2"), MONO("-Rational(3,4)*x**4+5*x**3-6*x**2-12")]),
 ("Vizsgáld a függvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=\dfrac14x^4-\dfrac52x^2+\dfrac94$", r"$f(x)=x^4+4x^3+4x^2+4$", r"$f(x)=x^5+5x^4+5x^3+5$"],
  [MONO("x**4/4-Rational(5,2)*x**2+Rational(9,4)"), MONO("x**4+4*x**3+4*x**2+4"), MONO("x**5+5*x**4+5*x**3+5")]),
 ("Vizsgáld a törtfüggvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=\dfrac{x^2-5x+7}{x-2}$", r"$f(x)=\dfrac{x^2-4x+4}{x^2+2}$", r"$f(x)=\dfrac{x^2-6x+9}{x^2+3}$"],
  [MONO("(x**2-5*x+7)/(x-2)"), MONO("(x**2-4*x+4)/(x**2+2)"), MONO("(x**2-6*x+9)/(x**2+3)")]),
 ("Vizsgáld a törtfüggvényeket monotonitás és szélsőérték szempontjából!",
  [r"$f(x)=\dfrac{x^2-2x+1}{x-2}$", r"$f(x)=\dfrac{x^2-6x+9}{x-1}$"],
  [MONO("(x**2-2*x+1)/(x-2)"), MONO("(x**2-6*x+9)/(x-1)")]),
 ("Vizsgáld a függvényeket konvexitás és inflexiós pont szempontjából!",
  [r"$f(x)=x^4-3x^2$", r"$f(x)=9x^5-10x^3$"], [GORB("x**4-3*x**2"), GORB("9*x**5-10*x**3")]),
 ("Vizsgáld a függvényeket konvexitás és inflexiós pont szempontjából! (A monotonitásukat az alapszint 3–4. "
  "feladatában már megvizsgáltad.)",
  [r"$f(x)=x^3+3x^2-4$", r"$f(x)=-x^3+3x+2$", r"$f(x)=-x^3+9x^2-15x+3$", r"$f(x)=2x^3+3x^2-12x+1$"],
  [GORB("x**3+3*x**2-4"), GORB("-x**3+3*x+2"), GORB("-x**3+9*x**2-15*x+3"), GORB("2*x**3+3*x**2-12*x+1")]),
 ("Vizsgáld a függvényeket monotonitás, szélsőérték, konvexitás és inflexiós pont szempontjából!",
  [r"$f(x)=-x^4+6x^2-8$", r"$f(x)=-x^4+2x^2+3$", r"$f(x)=\dfrac14x^4-3x^2+9$"],
  [MONO("-x**4+6*x**2-8") + "; " + GORB("-x**4+6*x**2-8"), MONO("-x**4+2*x**2+3") + "; " + GORB("-x**4+2*x**2+3"),
   MONO("x**4/4-3*x**2+9") + "; " + GORB("x**4/4-3*x**2+9")]),
 ("Ötödfokú polinom és egy elvi kérdés.",
  [r"Vizsgáld az $f(x)=\dfrac13\left(x^5-10x^3\right)$ függvényt monotonitás, szélsőérték, konvexitás és inflexió "
   r"szempontjából!",
   r"Döntsd el és indokold: ha $f''(x_0)=0$, akkor az $x_0$ biztosan inflexiós hely."],
  [MONO("(x**5-10*x**3)/3") + "; " + GORB("(x**5-10*x**3)/3"),
   r"hamis: $f(x)=x^4$-re $f''(0)=0$, de $f''(x)=12x^2$ a $0$ mindkét oldalán pozitív, nem vált előjelet, ezért a "
   r"$0$ nem inflexiós hely"]),
 ("Vizsgáld ki a függvényeket, és ábrázold a grafikonjukat!",
  [r"$f(x)=(1-x)(x+2)^2$", r"$f(x)=(x+2)(x-1)^2$"],
  [TELJES("(1-x)*(x+2)**2", "K9 a)"), TELJES("(x+2)*(x-1)**2", "K9 b)")]),
 ("Vizsgáld ki a függvényeket, és ábrázold a grafikonjukat!",
  [r"$f(x)=(x-4)(x-1)^2$", r"$f(x)=(x+1)(x+4)^2$"],
  [TELJES("(x-4)*(x-1)**2", "K10 a)"), TELJES("(x+1)*(x+4)**2", "K10 b)")]),
 ("Vizsgáld ki a páros negyedfokú függvényeket, és ábrázold a grafikonjukat!",
  [r"$f(x)=\dfrac18\left(x^4-18x^2+32\right)$", r"$f(x)=\dfrac14\left(x^4-6x^2-7\right)$",
   r"$f(x)=\dfrac1{12}\left(x^4-6x^2-27\right)$"],
  [TELJES("(x**4-18*x**2+32)/8", "K11 a)"), TELJES("(x**4-6*x**2-7)/4", "K11 b)"), TELJES("(x**4-6*x**2-27)/12", "K11 c)")]),
 (r"<b>Mit rontott el Véd Vilmos?</b> Az $f(x)=\dfrac{x^2+3}{x+1}$ vizsgálatában ezt írta: „$f'(x)="
  r"\dfrac{x^2+2x-3}{(x+1)^2}=0$, tehát $x=-3$ vagy $x=1$. $f(-3)=-6$ a <i>minimum</i>, $f(1)=2$ a <i>maximum</i>, "
  r"mert $-6\lt2$. A függvény a $(-3;\,1)$ intervallumon csökken.” Keresd meg és javítsd a hibákat!", None,
  r"két hiba: <b>1.</b> $f'$ előjele $(-\infty;\,-3)$-on $+$, $(-3;\,-1)$-en és $(-1;\,1)$-en $-$, $(1;\,+\infty)$-en "
  r"$+$: a $(-3;\,-6)$ tehát lokális <b>maximum</b>, az $(1;\,2)$ lokális <b>minimum</b> — a lokális szélsőértéket "
  r"az előjelváltás dönti el, nem az értékek nagysága (a maximum itt kisebb a minimumnál); <b>2.</b> az $x=-1$ "
  r"pólus: a függvény a $(-3;\,-1)$ és a $(-1;\,1)$ intervallumon csökken, a $(-3;\,1)$ nem intervallum az "
  r"értelmezési tartományban"),
]

N_II = [
 ("Vizsgáld a törtfüggvényeket konvexitás és inflexiós pont szempontjából!",
  [r"$f(x)=\dfrac{4}{x^2+1}$", r"$f(x)=\dfrac{x+1}{x^3}$"], [GORB("4/(x**2+1)"), GORB("(x+1)/x**3")]),
 ("Vizsgáld a törtfüggvényeket monotonitás, szélsőérték, konvexitás és inflexiós pont szempontjából!",
  [r"$f(x)=\dfrac{-x}{x^2+1}$", r"$f(x)=\dfrac{-x}{x^2+3}$", r"$f(x)=\dfrac{1-3x}{x^2}$", r"$f(x)=\dfrac{2x-1}{x^2}$"],
  [MONO(e) + "; " + GORB(e) for e in ("-x/(x**2+1)", "-x/(x**2+3)", "(1-3*x)/x**2", "(2*x-1)/x**2")]),
 ("Vizsgáld ki a törtfüggvényeket, és ábrázold a grafikonjukat!",
  [r"$f(x)=\dfrac{x^2-4}{x^2+1}$", r"$f(x)=\dfrac{3-x^2}{x^2+1}$"],
  [TELJES("(x**2-4)/(x**2+1)", "N3 a)"), TELJES("(3-x**2)/(x**2+1)", "N3 b)")]),
 ("Vizsgáld ki a törtfüggvényeket, és ábrázold a grafikonjukat!",
  [r"$f(x)=\dfrac{x^2-8}{x+3}$", r"$f(x)=\dfrac{x^2-3}{x+2}$", r"$f(x)=\dfrac{x^2+x-2}{x+3}$", r"$f(x)=\dfrac{x^2-x-2}{x-3}$"],
  [TELJES("(x**2-8)/(x+3)", "N4 a)"), TELJES("(x**2-3)/(x+2)", "N4 b)"), TELJES("(x**2+x-2)/(x+3)", "N4 c)"),
   TELJES("(x**2-x-2)/(x-3)", "N4 d)")]),
]
JOKER_II = (r"🃏 <b>Létezik-e szélsőérték nélküli harmadfokú polinom?</b> Ha igen, adj példát és indokold; ha nem, "
            r"bizonyítsd!",
            r"igen, például $f(x)=x^3+x$: $f'(x)=3x^2+1\gt0$ mindenütt, tehát szigorúan nő — nincs szélsőértéke "
            r"(inflexiós pontja viszont van: $(0;\,0)$)", None)

# ================================================================ ÖNELLENŐRZÉS
# a 0_F kulcsával egyező, kézzel is ellenőrzött értékek (29–31.) — ha a sympy mást ad, álljunk meg
def _chk(e, mx, mn, inf=None):
    F = Ex(e); a, b = szelso(F)
    if [(simplify(p), simplify(q)) for p, q in a] != [(Ex(str(p)), Ex(str(q))) for p, q in mx] or \
       [(simplify(p), simplify(q)) for p, q in b] != [(Ex(str(p)), Ex(str(q))) for p, q in mn]:
        E.append(("szélsőérték", e, a, b))
    if inf is not None and [(simplify(p), simplify(q)) for p, q in inflexio(F)] != [(Ex(str(p)), Ex(str(q))) for p, q in inf]:
        E.append(("inflexió", e, inflexio(F)))


_chk("x**3-2*x**2+x-2", [("1/3", "-50/27")], [(1, -2)])
_chk("Rational(2,3)*x**3-x**2-4*x", [(-1, "7/3")], [(2, "-20/3")])
_chk("-x**4/2-2*x**3-2*x**2+2", [(-2, 2), (0, 2)], [(-1, "3/2")])
_chk("-Rational(3,4)*x**4+5*x**3-6*x**2-12", [(0, -12), (4, 20)], [(1, "-55/4")])
_chk("(x**2-5*x+7)/(x-2)", [(1, -3)], [(3, 1)])
_chk("x**5+5*x**4+5*x**3+5", [(-3, 32)], [(-1, 4)])
_chk("x**3+3*x**2-4", [(-2, 0)], [(0, -4)], [(-1, -2)])
_chk("-x**3+9*x**2-15*x+3", [(5, 28)], [(1, -4)], [(3, 12)])
_chk("2*x**3+3*x**2-12*x+1", [(-2, 21)], [(1, -6)], [("-1/2", "15/2")])
_chk("-x/(x**2+1)", [(-1, "1/2")], [(1, "-1/2")], [("-sqrt(3)", "sqrt(3)/4"), (0, 0), ("sqrt(3)", "-sqrt(3)/4")])
_chk("(1-3*x)/x**2", [], [("2/3", "-9/4")], [(1, -2)])
_chk("(2*x-1)/x**2", [(1, 1)], [], [("3/2", "8/9")])
_chk("2*x**3-6*x+1", [(-1, 5)], [(1, -3)])
_chk("-x**3+6*x**2-9*x+1", [(3, 1)], [(1, -3)])
_chk("(x**2+3)/(x+1)", [(-3, -6)], [(1, 2)])
_chk("x**3+x", [], [], [(0, 0)])
# a saját feladatok számai
chk_ertek = [(ERINTO("x**3-12*x+1", 3), (-8, 15, 15 * x - 53)), (ERINTO("x**3-12*x+1", -3), (10, 15, 15 * x + 55)),
             (ERINTO("(x+3)/(x-1)", 3), (3, -1, -x + 6)), (ERINTO("x/(x**2+1)", 0), (0, 1, x)),
             (ERINTO("2*x**3+x**2/2-2*x+Rational(1,2)", -1, 1), (1, 3, 3 * x + 4)),
             (ERINTO("Rational(2,3)*x**3+3*x**2+3*x+Rational(1,3)", 1, 7), (7, 11, 11 * x - 4)),
             (ERINTO("x**2/2+2*x+1", 2), (7, 4, 4 * x - 1)), (ERINTO("-x**2/2+2*x-3", 4), (-3, -2, -2 * x + 5)),
             (ERINTO("x**2/2+x/2-3", 1, -2), (-2, Q(3, 2), Q(3, 2) * x - Q(7, 2))),
             (ERINTO("-x**2/2+Rational(3,2)*x+2", 0, 2), (2, Q(3, 2), Q(3, 2) * x + 2)),
             (ERINTO("-3*x**3+3*x**2+3*x+3", -1), (6, -12, -12 * x - 6)),
             (ERINTO("-2*x**3-2*x**2+2*x-2", 1), (-4, -8, -8 * x + 4))]
for kap, vart in chk_ertek:
    if tuple(simplify(a - b) for a, b in zip(kap, vart)) != (0, 0, 0):
        E.append(("érintő", kap, vart))
for e, x0, v in (("x**4/4-4*x**2+16", 2, -8), ("Rational(3,2)*x**4+4*x**3-x**2/2+5*x-7", -1, 12),
                 ("-x**3+9*x**2+x-1", -1, -20), ("x**3/4+sqrt(2)/2*x**2-7*x+2*pi", sqrt(2), Q(-7, 2)),
                 ("(3*x**2-4)**4", -1, 24), ("(x**2-3*x+2)**5", 3, 240), ("(x-2)*exp(2*x)", 0, -3),
                 ("3*log((x-1)/(x+1))", 2, 2), ("(x**2-4*x)/2", 0, -2), ("(x**2-4*x)/2", 4, 2)):
    if simplify(diff(Ex(e), x).subs(x, x0) - v) != 0:
        E.append(("f'(x0)", e, x0, v))
d5 = diff(Ex("x**3+5/x"), x); d6 = diff(Ex("x**2-1/(2*x**2)"), x)
if simplify(d5.subs(x, 2) + d5.subs(x, -2) - Q(43, 2)) != 0 or simplify(d6.subs(x, 2) - d6.subs(x, -2) - Q(33, 4)) != 0:
    E.append("19 e–f")
f20 = Ex("x**2/2+x+1")
if simplify(2 * f20 - diff(f20, x) ** 2 - 1) != 0:
    E.append("20")
f21, g21 = Ex("Rational(2,3)*x**3+x**2/2-Rational(3,7)*x"), Ex("2*x**3-Rational(9,2)*x**2-2*x")
if 7 * diff(f21, x).subs(x, Q(-1, 2)) + diff(g21, x).subs(x, Q(-1, 2)) != 1:
    E.append("21")
f24 = Ex("2*x**2-1")
if simplify((x ** 2 - 1) * diff(f24, x, 2) + x * diff(f24, x) - 4 * f24) != 0:
    E.append("24")
egyenlo("27", diff(Ex("tan(x)**3/3+tan(x)"), x), Ex("1/cos(x)**4"))
egyenlo("28", diff(Ex("cot(x)**3/3+cot(x)"), x), Ex("-1/sin(x)**4"))
# 16. a–d
for (e, x0, dx, dy, q) in (("x**2", 1, Q(1, 2), 1.25, 2.5), ("x**2", 5, Q(1, 2), 5.25, 10.5),
                           ("sqrt(x)", 0, Q(3, 5), 0.77, 1.29), ("sqrt(x)", 5, Q(3, 5), 0.13, 0.22)):
    F = Ex(e); D_ = float(F.subs(x, x0 + dx) - F.subs(x, x0))
    if round(D_, 2) != dy or round(D_ / float(dx), 2) != q:
        E.append(("16", e, x0, D_))
# saját: futó, medence, mozgás, érintő külső pontból
if [Ex("t**2+4*t").subs("t", 3) / 3, diff(Ex("x**2+4*x"), x).subs(x, 3), solve(Ex("2*x+4-14"), x),
        diff(Ex("120-3*x+x**2/50"), x).subs(x, 10)] != [7, 10, [5], Q(-13, 5)]:
    E.append("futó/medence")
s_ = Ex("x**3-6*x**2+9*x")
if [solve(diff(s_, x), x), diff(s_, x, 2).subs(x, 2), diff(s_, x).subs(x, 2)] != [[1, 3], 0, -3]:
    E.append("mozgás")
a_ = symbols("a")
if sorted(solve(expand(-(2 * a_ - 2) * a_ + a_ ** 2 - 2 * a_ + 4), a_)) != [-2, 2]:
    E.append("külső pont")
if solve(diff(Ex("x**2+x"), x) - 3, x) != [1] or Ex("x**2+x").subs(x, 1) - 3 != -1:
    E.append("c érintő")
if sorted(solve(diff(Ex("x**3-12*x+1"), x), x)) != [-2, 2] or [Ex("x**3-12*x+1").subs(x, v) for v in (2, -2)] != [-15, 17]:
    E.append("vízszintes érintő")

# tiltott adatok: a 26/27-es 2. és 3. dolgozat
TILTOTT = ["5*x**4-2*x**3+7*x-3", "-4*cos(x)", "5*log(x)", "(x**2-3*x)*cos(x)", "(2*x+3)/(x**2+1)",
           "3*x**5+4*x**3-6*x+1", "5*sin(x)", "2*exp(x)", "(x**2+4*x)*sin(x)", "(3*x-1)/(x**2+2)",
           "2*x**4-5*x**2+3*x", "7*cos(x)", "3*tan(x)", "(x**2+1)*exp(x)", "(2*x+1)/(x**2+3)",
           "x**3-2*x**2+3", "x**3+3*x**2-2", "x**3-3*x+1", "2*x**5-4*x**3+6*x-7", "x**6-3*x**4+5*x-1",
           "4*x**5-2*x**3+x-3", "x**3-3*x**2-9*x+5", "-x**3+3*x**2+9*x-2", "x**3+3*x**2-9*x-4",
           "(x**2-3*x)/(x+1)", "(x**2-7*x+10)/(x-1)", "(x**2-3*x)/(x-4)"]
HASZNALT = set(re.findall(r'(?:DER\(|MONO\(|GORB\(|TELJES\(|_chk\(|ERINTO\()?"([^"]*x[^"]*)"',
                          open(__file__, encoding="utf-8").read().split("# ================================================================ ZSOLDOS-LISTA I.")[1]
                          .split("# ================================================================ ÖNELLENŐRZÉS")[0]))
_P = (0.37, 1.91, 2.63, 3.3)


def _azonos(u, r_):
    try:
        return all(abs(complex(Ex(u).subs(x, v)) - complex(Ex(r_).subs(x, v))) < 1e-9 for v in _P)
    except Exception:
        return False


for h in HASZNALT:
    try:
        Ex(h)
    except Exception:
        continue
    for r_ in TILTOTT:
        if _azonos(h, r_):
            E.append(("tiltott", h, r_))
assert not E, E
print("sympy önteszt: OK")


# ================================================================ OLDALAK
def lista(A, K, N, J):
    return "\n".join([
        '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(A, "alap", "alap"),
        '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(K, "kozep", "kozep"),
        '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(N, "nehez", "nehez"),
        '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(J[0], J[1], J[2])])


def _prim(L):
    """A nyers stringekben a \\' (KaTeX-ben ékezet) → sima vessző-prím."""
    def p(v):
        if isinstance(v, str):
            return v.replace("\\'", "'")
        if isinstance(v, (list, tuple)):
            return type(v)(p(u) for u in v)
        return v
    return [p(it) for it in L]


u1 = oldal(**T, fajl="feladatok-derivalas.html", cim="Zsoldos-lista I. — Deriválás",
           h1="A függvény deriváltja — Zsoldos-lista I.: deriválás", itt="Zsoldos-lista I. — Deriválás",
           alcim="Növekmény és differenciahányados, deriválási szabályok, összetett függvény, második derivált, érintő és "
                 "változási sebesség. A végeredmény minden feladatnál lenyitható — előbb számolj!",
           sections_html=lista(_prim(A_I), _prim(K_I), _prim(N_I), JOKER_I), ossz_nev="Csalópapírt",
           prev="tananyag-fuggvenyvizsgalat.html", prevc="A teljes függvényvizsgálat",
           nxt="feladatok-fuggvenyvizsgalat.html", nxtc="Zsoldos-lista II. — Függvényvizsgálat")
u2 = oldal(**T, fajl="feladatok-fuggvenyvizsgalat.html", cim="Zsoldos-lista II. — Függvényvizsgálat",
           h1="A függvény deriváltja — Zsoldos-lista II.: függvényvizsgálat", itt="Zsoldos-lista II. — Függvényvizsgálat",
           alcim="Monotonitás és szélsőérték, konvexitás és inflexiós pont, teljes függvényvizsgálat grafikonnal. A "
                 "végeredmény minden feladatnál lenyitható — a 32-es típusú vizsgálatoknál ábrával!",
           sections_html=lista(_prim(A_II), _prim(K_II), _prim(N_II), JOKER_II), ossz_nev="Csalópapírt",
           prev="feladatok-derivalas.html", prevc="Zsoldos-lista I. — Deriválás",
           nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
print("✓", os.path.basename(u1), "| I.", len(A_I), len(K_I), len(N_I), "+ Joker")
print("✓", os.path.basename(u2), "| II.", len(A_II), len(K_II), len(N_II), "+ Joker")
