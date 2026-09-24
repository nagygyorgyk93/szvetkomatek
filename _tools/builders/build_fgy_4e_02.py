# -*- coding: utf-8 -*-
"""4e/02 — ket feladatgyujtemeny: Zsoldos-lista I. (tulajdonsagok) es II. (hatarertek, aszimptotak).
Feladat-terkep: projektek/4e/munkafajlok/terkep_fgy_02-fuggvenyek.md (jovahagyva 2026-09-24).
Forras: 0_Feladatok - Fuggvenyek.pdf (0_F; a 10 i, 13 f [x->5], 13 g, 15 i kulcsa javitva) + sajat.
Minden vegeredmeny sympybol (x -> -oo eseten x -> -x helyettesitessel: a sympy 1.14 limit(2**x, x, -oo)-ra oo-t ad)."""
import sys, os, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from tananyag_common import svg_fuggvenyek
import sympy
from sympy import (Rational as Q, symbols, limit, oo, latex, sympify, S, solveset, simplify, fraction, together,
                   solve, Interval, Union, FiniteSet, Complement)
from sympy.calculus.util import continuous_domain
from sympy.parsing.sympy_parser import parse_expr

x = symbols("x", real=True)
LD = {"x": x, "Rational": Q, "sqrt": sympy.sqrt, "log": sympy.log, "exp": sympy.exp, "sin": sympy.sin,
      "cos": sympy.cos, "tan": sympy.tan, "Abs": sympy.Abs, "E": sympy.E}
T = dict(tagozat="4e", mappa="02-fuggvenyek", temakor="Függvények")
KEK, PIROS, ZOLD, BORO, SOT = "#3b82f6", "#ef4444", "#047857", "#f59e0b", "#0f172a"


def Ex(s):
    return sympify(s, locals=LD)


def TX(s):
    t = latex(parse_expr(s, local_dict=LD, evaluate=False), order="none")
    t = re.sub(r"(?<![\d.}])1 \\frac", r"\\frac", t)
    t = t.replace(r"\frac", r"\dfrac")
    t = re.sub(r"\^\{\\dfrac", r"^{\\frac", t)
    t = t.replace(r"\log{\left(", r"\ln{\left(")
    for fv, nev in ((r"\sin", r"\sin"), (r"\cos", r"\cos"), (r"\tan", r"\operatorname{tg}")):
        t = t.replace(fv + r"{\left(x \right)}", nev + " x").replace(fv + r"^{2}{\left(x \right)}", nev + "^2x")
    return t


TEXMAP = {"log(5-x, 2)": r"\log_2(5-x)", "log(3*x**2-x-4, 2)": r"\log_2\left(3x^2-x-4\right)",
          "log(7-6*x-x**2, Rational(1,2))": r"\log_{0{,}5}\left(7-6x-x^2\right)",
          "log((4-x)/(3*x+2), 3)": r"\log_3\dfrac{4-x}{3x+2}", "x/(x**2-1)+log(16-x**2, 7)": r"\dfrac{x}{x^2-1}+\log_7\left(16-x^2\right)",
          "x**3*tan(x)": r"x^3\operatorname{tg}x", "log(x, 2)": r"\log_2x", "-x**3/(x**2+3)": r"-\dfrac{x^3}{x^2+3}"}


def TXM(e):
    return TEXMAP.get(e) or TX(e)


def _zar(e, t):
    return r"\left(" + t + r"\right)" if parse_expr(e, local_dict=LD, evaluate=False).is_Add else t


def LIM(s, a, d=None):
    f = Ex(s)
    if a == -oo:
        return limit(f.subs(x, -x), x, oo)
    if a == oo:
        return limit(f, x, oo)
    return limit(f, x, a, d) if d else limit(f, x, a, "+-")


def V(v):
    v = simplify(v)
    if v == oo:
        return r"+\infty"
    if v == -oo:
        return r"-\infty"
    return latex(v)


def HAT(a, d=None):
    if a == oo:
        return r"x\to+\infty"
    if a == -oo:
        return r"x\to-\infty"
    return r"x\to " + latex(a) + ("-0" if d == "-" else "+0" if d == "+" else "")


def LIMS(intro, tetelek, tex=None):
    """tetelek = [(kifejezés, pont[, irány]), …] → határérték-kártya."""
    tex = tex or {}
    subs, ans = [], []
    for t in tetelek:
        e, a = t[0], t[1]
        d = t[2] if len(t) > 2 else None
        subs.append(r"$\lim\limits_{" + HAT(a, d) + "}" + (tex.get(e) or TEXMAP.get(e) or _zar(e, TX(e))) + "$")
        ans.append("$" + V(LIM(e, a, d)) + "$")
    return (intro, subs, ans)


# ---------------------------------------------------------------- halmazok írása
def _szam(v):
    return latex(v)


def _int(I):
    a, b = I.start, I.end
    bal = "(" if (I.left_open or a == -oo) else "["
    jobb = ")" if (I.right_open or b == oo) else "]"
    return bal + (r"-\infty" if a == -oo else _szam(a)) + r";\," + (r"+\infty" if b == oo else _szam(b)) + jobb


def HALMAZ(Sx):
    """sympy-halmaz → TeX: ℝ∖{…}, intervallumok uniója, véges halmaz."""
    if Sx == S.Reals:
        return r"\mathbb R"
    ki = S.Reals - Sx
    if isinstance(ki, FiniteSet) and len(ki) > 0:
        return r"\mathbb R\setminus\{" + r";\,".join(_szam(v) for v in sorted(ki, key=float)) + r"\}"
    if isinstance(Sx, Interval):
        return _int(Sx)
    if isinstance(Sx, Union):
        return r"\cup".join(_int(I) if isinstance(I, Interval) else HALMAZ(I) for I in
                            sorted(Sx.args, key=lambda I: float(I.inf)))
    if isinstance(Sx, FiniteSet):
        return r"\{" + r";\,".join(_szam(v) for v in sorted(Sx, key=float)) + r"\}"
    return latex(Sx)


def DOM(s):
    return continuous_domain(Ex(s), x, S.Reals)


def DOMS(intro, exprs):
    return (intro, ["$f(x)=" + TXM(e) + "$" for e in exprs], ["$D_f=" + HALMAZ(DOM(e)) + "$" for e in exprs])


def ELOJEL(s):
    f = Ex(s)
    D = DOM(s)
    z = sorted(solveset(f, x, D), key=float)
    poz = solveset(f > 0, x, S.Reals).intersect(D)
    neg = solveset(f < 0, x, S.Reals).intersect(D)
    zs = "nincs" if not z else r"$" + r";\ ".join(_szam(v) for v in z) + "$"
    return (f"zérushely: {zs}; $y\\gt0$, ha $x\\in {HALMAZ(poz)}$; $y\\lt0$, ha $x\\in {HALMAZ(neg)}$")


def ELOJELS(intro, exprs):
    return (intro, ["$y=" + TXM(e) + "$" for e in exprs], [ELOJEL(e) for e in exprs])


def PARITAS(s):
    f = Ex(s)
    g = f.subs(x, -x)
    if simplify(g - f) == 0:
        return "páros"
    if simplify(g + f) == 0:
        return "páratlan"
    return "egyik sem"


def PARS(intro, exprs):
    return (intro, ["$f(x)=" + TXM(e) + "$" for e in exprs], [PARITAS(e) for e in exprs])


def ASZ(s):
    f = Ex(s)
    sz, nv = fraction(together(f))
    fu = sorted((r for r in solve(nv, x) if r.is_real and LIM(s, r, "+") in (oo, -oo)), key=float)
    h = LIM(s, oo)
    k = LIM(f"({s})/x", oo)
    fe = (k, LIM(f"({s})-({k})*x", oo)) if h in (oo, -oo) and k not in (oo, -oo, 0) else None
    return fu, (None if h in (oo, -oo) else h), fe


def EGYENES(k, n):
    """y = kx + n olvasható alakban: előbb az x-es tag (−x + 2, nem 2 − x)."""
    kx = "x" if k == 1 else "-x" if k == -1 else latex(k) + "x"
    if n == 0:
        return kx
    return kx + ("+" if n > 0 else "-") + latex(abs(n))


def ASZ_SZOVEG(s):
    fu, vi, fe = ASZ(s)
    r = []
    r.append("függőleges: " + (", ".join(f"$x={_szam(v)}$" for v in fu) if fu else "nincs"))
    r.append("vízszintes: " + (f"$y={_szam(vi)}$" if vi is not None else "nincs"))
    if fe:
        k, n = fe
        r.append("ferde: $y=" + EGYENES(k, n) + "$")
    return "; ".join(r)


def ASZS(intro, exprs):
    return (intro, ["$f(x)=" + TXM(e) + "$" for e in exprs], [ASZ_SZOVEG(e) for e in exprs])


def svgwrap(svg):
    return f'<div class="svgwrap">{svg}</div>'


# ================================================================ ÖNTESZT (forrás-kulcs és kézi értékek)
E = []


def chk(nev, g, w):
    if not (g == w or (not isinstance(g, (list, tuple)) and simplify(sympify(g) - sympify(w)) == 0)):
        E.append((nev, g, w))


chk("13f-x5", LIM("(x**2-6*x+5)/(x**2-8*x+15)", 5), 2)
chk("13g", LIM("(x+2)/(3*x**2+5*x-2)", -2), Q(-1, 7))
chk("15i", ASZ("2*x/3+3/(2*x)"), ([0], None, (Q(2, 3), 0)))
chk("13q", LIM("(3*x**2-x+1)/(6*x**2+3*x+2)", -oo), Q(1, 2))
chk("2^x a -oo-ben", LIM("2**x", -oo), 0)
chk("10i poz", solveset(Ex("(2*x**2-3*x)*exp(x)") > 0, x, S.Reals), Union(Interval.open(-oo, 0), Interval.open(Q(3, 2), oo)))
chk("joker2", ASZ("(x**2-3*x+3)/(x-2)"), ([2], None, (1, -1)))
chk("nehez3-lyuk", ASZ("(x**3+1)/(x**2-1)"), ([1], None, (1, 0)))
chk("kozep12", solve(Ex("(x**2+2*x)/(x**2+1)") - 1, x), [Q(1, 2)])
chk("kozep11", ASZ("(2*x**2-8)/(x**2-1)"), ([-1, 1], 2, None))
assert not E, E

# ================================================================ ÁBRÁK
W, H = 360, 240
PT_I = [(-4, 2), (-2, -2), (1, 4), (4, -2)]


def tv(t, P):
    for (a, b), (c, d) in zip(P, P[1:]):
        if a <= t <= c:
            return b + (d - b) * (t - a) / (c - a)
    raise ValueError


SVG_I_PAROSITAS = svg_fuggvenyek(
    [(lambda t: (1 / 3) ** t, KEK, "A", [(-1.9, 3.3)]), (lambda t: t ** 4, PIROS, "B", [(-1.4, 1.4)]),
     (lambda t: math.log(t, 0.5), ZOLD, "C", [(0.06, 4.2)]), (lambda t: 1 / t ** 2, BORO, "D", [(-3.3, -0.45), (0.45, 3.3)])],
    xr=(-3.4, 4.4), yr=(-2.6, 4.4), w=380, h=260,
    leiras="Négy grafikon A, B, C, D betűvel: az A a (0; 1) ponton megy át és jobbra a 0-hoz simul; a B az origón "
           "megy át, y tengelyre szimmetrikus és sosem negatív; a C az (1; 0) ponton megy át és csökken; a D a 0-ban "
           "nincs értelmezve és mindenhol pozitív")
SVG_I_EXPLOG = svg_fuggvenyek(
    [(lambda t: 1.5 ** t, KEK, "P", [(-3.2, 3.6)]), (lambda t: math.log(t, 3), PIROS, "Q", [(0.05, 5.2)])],
    xr=(-3.4, 5.4), yr=(-2.6, 4.4), w=380, h=250,
    pontok=[(3, 1, "", SOT)],
    leiras="Két görbe: a P minden x-re értelmezett, a (0; 1) ponton megy át és nő; a Q csak pozitív x-re létezik, "
           "az (1; 0) és a (3; 1) ponton megy át")
SVG_I_ELEMZES = svg_fuggvenyek(
    [(lambda t: tv(t, PT_I), SOT, "f", [(-4, 4)])], xr=(-4.6, 4.6), yr=(-2.8, 4.8), w=380, h=260,
    jelmagyarazat=False, pontok=[(-4, 2, "", SOT), (4, -2, "", SOT)],
    leiras="Az f függvény grafikonja a [−4; 4] intervallumon: a (−4; 2), (−2; −2), (1; 4), (4; −2) pontokat összekötő töröttvonal")
SVG_I_PARITAS = svg_fuggvenyek(
    [(lambda t: t ** 4 - 2 * t ** 2, KEK, "f", [(-1.75, 1.75)]), (lambda t: t ** 3 - 3 * t, PIROS, "g", [(-2.2, 2.2)]),
     (lambda t: 0.5 * t ** 2 + t, ZOLD, "h", [(-3.2, 1.6)])],
    xr=(-3.4, 3.4), yr=(-2.8, 3.4), w=380, h=260,
    leiras="Három grafikon: az f az y tengelyre szimmetrikus, a g az origóra szimmetrikus, a h egyikre sem")
SVG_II_1 = svg_fuggvenyek(
    [(lambda t: 0.5 * t + 2, KEK, "f", [(-3.6, 4.4)])], xr=(-4, 4.8), yr=(-0.8, 4.6), w=W, h=H, jelmagyarazat=False,
    pontok=[(2, 3, "", "o:" + SOT), (2, 1, "", SOT)],
    leiras="Az f grafikonja: az y = x/2 + 2 egyenes (átmegy a (0; 2) ponton), a (2; 3) pontban üres kör, alatta a (2; 1) pontban teli pont")
SVG_II_2 = svg_fuggvenyek(
    [(lambda t: -t, KEK, "g", [(-3.6, -1)]), (lambda t: t + 3, KEK, "", [(-1, 1.4)])],
    xr=(-4, 2.2), yr=(-0.8, 4.6), w=W, h=H, jelmagyarazat=False,
    pontok=[(-1, 1, "", "o:" + SOT), (-1, 2, "", SOT)],
    leiras="A g grafikonja: balról egy csökkenő félegyenes a (−1; 1) üres pont felé, jobbról egy emelkedő félegyenes a "
           "(−1; 2) teli pontból indulva")
SVG_II_4 = svg_fuggvenyek(
    [(lambda t: t * t, KEK, "h", [(-2, 1)]), (lambda t: 2 - t, KEK, "", [(1, 3)]), (lambda t: 1, KEK, "", [(3, 4.6)])],
    xr=(-2.4, 5), yr=(-1.6, 4.4), w=W, h=H, jelmagyarazat=False,
    pontok=[(1, 1, "", SOT), (3, -1, "", "o:" + SOT), (3, 1, "", SOT)],
    leiras="A h grafikonja: a parabola-ív az (1; 1) pontba fut, onnan egy csökkenő szakasz a (3; −1) üres pontig, és a "
           "(3; 1) teli pontból vízszintes félegyenes indul")

# ================================================================ ZSOLDOS-LISTA I. — TULAJDONSÁGOK
A_I = [
 (r"Adottak az $f(x)=\dfrac{3x-8}{2}$, a $g(x)=\dfrac{5x-1}{x^2+1}$ és a "
  r"$h(x)=\begin{cases}x-1, & \text{ha } x\ge1\\ -x^2+1, & \text{ha } x\lt1\end{cases}$ függvények. Számítsd ki "
  r"az $f(a)$, $g(a)$ és $h(a)$ értékeket, ha $a\in\left\{2;\,1;\,0;\,-2;\,-\frac43\right\}$!", None,
  r"$f$: $-1;\ -\frac52;\ -4;\ -7;\ -6$ · $g$: $\frac95;\ 2;\ -1;\ -\frac{11}{5};\ -\frac{69}{25}$ · "
  r"$h$: $1;\ 0;\ 1;\ -3;\ -\frac79$"),
 (r"Az előző feladat $f$ és $g$ függvényével számítsd ki a kifejezések értékét!",
  [r"$f\left(-\frac23\right)\cdot g(-1)$", r"$\frac{14}{3}\cdot f\left(\frac27\right)-\frac56\cdot g\left(\frac12\right)$"],
  [r"$(-5)\cdot(-3)=15$", r"$-\frac{50}{3}-1=-\frac{53}{3}$"]),
 ("Add meg az elemi függvény értelmezési tartományát ($D_f$) és értékkészletét ($R_f$)!",
  [r"$f(x)=x^4$", r"$f(x)=\sqrt x$", r"$f(x)=\dfrac{1}{x^2}$", r"$f(x)=3^x$", r"$f(x)=\log_5x$", r"$f(x)=\cos x$"],
  [r"$D_f=\mathbb R$, $R_f=[0;\,+\infty)$", r"$D_f=[0;\,+\infty)$, $R_f=[0;\,+\infty)$",
   r"$D_f=\mathbb R\setminus\{0\}$, $R_f=(0;\,+\infty)$", r"$D_f=\mathbb R$, $R_f=(0;\,+\infty)$",
   r"$D_f=(0;\,+\infty)$, $R_f=\mathbb R$", r"$D_f=\mathbb R$, $R_f=[-1;\,1]$"]),
 (r"Párosítsd a grafikonokat a képletekkel: $y=x^4$, $y=\left(\frac13\right)^x$, $y=\log_{\frac12}x$, $y=\dfrac1{x^2}$! "
  r"Minden döntést egy jellegzetességgel indokolj!" + svgwrap(SVG_I_PAROSITAS), None,
  r"A: $y=\left(\frac13\right)^x$ (a $(0;1)$ ponton megy át, csökken, pozitív) · B: $y=x^4$ (páros, az origón megy át) · "
  r"C: $y=\log_{\frac12}x$ (az $(1;0)$ ponton megy át, csak pozitív $x$-re létezik) · D: $y=\frac1{x^2}$ (a $0$-ban nincs "
  r"értelmezve, mindenhol pozitív)"),
 DOMS("Határozd meg a függvények értelmezési tartományát!",
      ["(x-1)/(x**2-2)", "1/(7*x-3*x**2)", "7*x/(3*x**2+8*x-3)", "(x-3)/(x**2+2*x+1)"]),
 DOMS("Határozd meg a függvények értelmezési tartományát!",
      ["sqrt(6-2*x)", "sqrt(3*x+12)", "log(5-x, 2)", "log(2*x+7)"]),
 (r"Határozd meg a függvények zérushelyeit! Előbb nézd meg, hol vannak értelmezve.",
  [r"$f(x)=x^3-4x$", r"$g(x)=\dfrac{x^2-1}{x+1}$", r"$h(x)=\dfrac{x^2-5x}{x-5}$", r"$k(x)=2^x-8$"],
  [r"$-2;\ 0;\ 2$", r"csak $1$ (a $-1$ nincs benne $D_g$-ben)", r"csak $0$ (az $5$ nincs benne $D_h$-ban)", r"$3$"]),
 ELOJELS("Határozd meg a függvények zérushelyeit és előjelét!", ["(x+1)*(x+2)**2", "(1-x)*(x-4)**2"]),
 ELOJELS("Határozd meg a függvények zérushelyeit és előjelét!", ["(x**2-2*x)/(3*x+2)", "(x**2-7*x+10)/(x-1)"]),
 PARS("Döntsd el, hogy a függvény páros, páratlan vagy egyik sem!", ["4*x+4/x", "x*(x-1)**2", "x**3-Rational(2,3)*x", "7*x**5-3/x"]),
 PARS("Döntsd el, hogy a függvény páros, páratlan vagy egyik sem!", ["4*Abs(x)-x**4", "3*x**3-x*Abs(x)", "7**(-x)+7**x", "5**x-5**(-x)"]),
 (r"Az ábrán az $f$ függvény grafikonja látható (a töröttvonal végpontjai a grafikon részei). Olvasd le!"
  + svgwrap(SVG_I_ELEMZES),
  ["az értelmezési tartományt és az értékkészletet", "a zérushelyeket", "hol pozitív és hol negatív a függvény",
   "hol nő és hol csökken", "a legnagyobb és a legkisebb értéket (és hol veszi fel)"],
  [r"$D_f=[-4;\,4]$, $R_f=[-2;\,4]$", r"$-3;\ -1;\ 3$",
   r"$f(x)\gt0$, ha $x\in[-4;\,-3)\cup(-1;\,3)$; $f(x)\lt0$, ha $x\in(-3;\,-1)\cup(3;\,4]$",
   r"nő a $[-2;\,1]$, csökken a $[-4;\,-2]$ és az $[1;\,4]$ intervallumon",
   r"legnagyobb: $4$ (az $x=1$ helyen); legkisebb: $-2$ (az $x=-2$ és az $x=4$ helyen)"]),
]
K_I = [
 (r"Az ábrán a $P$ és a $Q$ görbe látható; az egyik az $y=\left(\frac32\right)^x$, a másik az $y=\log_3x$ grafikonja."
  + svgwrap(SVG_I_EXPLOG),
  ["Melyik görbe melyik függvényé? Indokold két jellegzetességgel!", "Hol veszi fel a $Q$ görbéhez tartozó függvény a $2$ értéket?",
   "Van-e a $P$ görbének zérushelye?"],
  [r"$P$: $y=\left(\frac32\right)^x$ (minden $x$-re értelmezett, a $(0;1)$ ponton megy át); $Q$: $y=\log_3x$ (csak "
   r"pozitív $x$-re, az $(1;0)$ ponton megy át)", r"az $x=9$ helyen, mert $\log_39=2$", r"nincs: $\left(\frac32\right)^x\gt0$ minden $x$-re"]),
 ("Véd Vilmos négy állítást írt fel. Mit rontott el? Add meg a helyes választ!",
  [r"„Az $y=\log_3x$ függvény értelmezési tartománya $[0;\,+\infty)$.”", r"„Az $y=\sqrt x$ függvény értékkészlete $\mathbb R$.”",
   r"„Az $y=\dfrac{1}{x+4}$ függvény értelmezési tartománya $\mathbb R\setminus\{0\}$.”", r"„Az $y=2^x$ függvény értékkészlete $[0;\,+\infty)$.”"],
  [r"a $0$ nincs benne: $(0;\,+\infty)$", r"a négyzetgyök nem negatív: $[0;\,+\infty)$",
   r"a nevező $x+4$: $\mathbb R\setminus\{-4\}$", r"a $0$-t sosem veszi fel: $(0;\,+\infty)$"]),
 DOMS("Határozd meg a függvények értelmezési tartományát!", ["sqrt(5*x**2+4*x-1)", "sqrt(10+3*x-x**2)"]),
 DOMS("Határozd meg a függvények értelmezési tartományát!", ["log(3*x**2-x-4, 2)", "log(7-6*x-x**2, Rational(1,2))"]),
 DOMS("Határozd meg a függvények értelmezési tartományát!", ["sqrt(2*x+7)+4/(x-2)", "sqrt((2-x)/(2*x+1))", "log((4-x)/(3*x+2), 3)"]),
 ELOJELS("Határozd meg a függvények zérushelyeit és előjelét!",
         ["Rational(1,2)*(x**2-5)*(1-x)", "(x**2+6*x+9)/(x+1)", "(x**2-4)/(1-x**2)", "(x**2-5*x+4)/(x-5)",
          "(2*x**2-3*x)*exp(x)", "(x**2-2)*exp(2*x)"]),
 PARS("Döntsd el, hogy a függvény páros, páratlan vagy egyik sem! (Előbb nézd meg az értelmezési tartományt: szimmetrikus-e?)",
      ["sqrt(x**2+1)+sqrt(x**2-1)", "sin(x)+cos(x)", "x*sin(x)+cos(x)", "x**3*tan(x)", "(x**2+1)/(x**2+x+1)",
       "x*sin(x)**2-x**3", "2**(1-x**2)", "sin(x)/x-1"]),
 (r"Az ábrán az $f$, a $g$ és a $h$ függvény grafikonja látható." + svgwrap(SVG_I_PARITAS),
  ["Melyik páros, melyik páratlan, melyik egyik sem? Mit látsz a grafikonon?",
   r"A képletek: $f(x)=x^4-2x^2$, $g(x)=x^3-3x$, $h(x)=\frac12x^2+x$. Igazold számolással a döntéseidet!",
   r"Egyetlen konkrét $x$ helyettesítésével mutasd meg, hogy $h$ se nem páros, se nem páratlan!"],
  ["$f$ páros (az $y$ tengelyre szimmetrikus), $g$ páratlan (az origóra szimmetrikus), $h$ egyik sem",
   r"$f(-x)=x^4-2x^2=f(x)$; $g(-x)=-x^3+3x=-g(x)$; $h(-x)=\frac12x^2-x$, ez sem $h(x)$, sem $-h(x)$",
   r"pl. $h(2)=4$, de $h(-2)=0$: ez sem $h(2)=4$, sem $-h(2)=-4$"]),
]
N_I = [
 DOMS("Határozd meg a függvények értelmezési tartományát!",
      ["sqrt((x**2-9)/(x+1))", "sqrt(x**2-2*x)-log(9-x**2)", "x/(x**2-1)+log(16-x**2, 7)"]),
 (r"Vizsgáld meg az $f(x)=\dfrac{x^2-x-6}{x^2-1}$ függvényt!",
  ["Határozd meg az értelmezési tartományát!", "Határozd meg a zérushelyeit!", "Készíts előjeltáblázatot!",
   "Számítsd ki $f(0)$-t, és az előjeltáblázat alapján vázold a grafikont!"],
  [r"$D_f=\mathbb R\setminus\{-1;\,1\}$", r"$-2$ és $3$",
   r"$f(x)\gt0$, ha $x\in(-\infty;\,-2)\cup(-1;\,1)\cup(3;\,+\infty)$; $f(x)\lt0$, ha $x\in(-2;\,-1)\cup(1;\,3)$",
   r"$f(0)=6$; a grafikon az $x$ tengely fölött van, ha $x\lt-2$, $-1\lt x\lt1$ vagy $x\gt3$, alatta, ha $-2\lt x\lt-1$ vagy $1\lt x\lt3$"]),
]
JOKER_I = ("Véd Vilmos olyan „tükörfüggvényt” keres, amely egyszerre páros <b>és</b> páratlan. Létezik ilyen? "
           "Ha igen, melyik (értelmezési tartománya legyen $\\mathbb R$)?",
           [r"Ha $f$ páros és páratlan is, akkor $f(-x)=f(x)$ és $f(-x)=-f(x)$, tehát $f(x)=-f(x)$, vagyis $f(x)=0$ "
            r"minden $x$-re.", r"Egyetlen ilyen van: az $f(x)=0$ konstans függvény."],
           ["Írd fel a két feltételt egyszerre!", "Melyik függvény teljesíti?"])
# a Joker-tuple sorrendje: (intro, ans, subs) — mint a 4e/01-ben

# ================================================================ ZSOLDOS-LISTA II. — HATÁRÉRTÉK ÉS ASZIMPTOTÁK
A_II = [
 (r"Az ábrán az $f$ függvény grafikonja látható. A teli pont a függvény értékét jelöli, az üres pont azt, hogy ott "
  r"a grafikonnak nincs pontja." + svgwrap(SVG_II_1),
  [r"Olvasd le az $f(2)$ értéket!", r"Mennyi a $\lim\limits_{x\to2}f(x)$ határérték?",
   r"Mennyi az $f(0)$ és a $\lim\limits_{x\to0}f(x)$?"],
  [r"$f(2)=1$", r"$3$ (ahová a görbe tart)", r"mindkettő $2$ — itt a függvény folytonos"]),
 (r"Az ábrán a $g$ függvény grafikonja látható." + svgwrap(SVG_II_2),
  [r"Mennyi a $\lim\limits_{x\to-1-0}g(x)$ és a $\lim\limits_{x\to-1+0}g(x)$?", r"Mennyi $g(-1)$?",
   r"Létezik-e a $\lim\limits_{x\to-1}g(x)$ határérték?"],
  [r"$1$, illetve $2$", r"$2$", r"nem, mert a két egyoldali határérték különbözik"]),
 (r"Az $f(x)=\dfrac{x^2+2x-3}{x-1}$ függvény az $x=1$ helyen nincs értelmezve.",
  [r"Számítsd ki $f(0{,}9)$, $f(0{,}99)$, $f(1{,}01)$ és $f(1{,}1)$ értékét!", r"Mit sejtesz a $\lim\limits_{x\to1}f(x)$ határértékről?",
   r"Igazold a sejtést egyszerűsítéssel!"],
  [r"$3{,}9$; $3{,}99$; $4{,}01$; $4{,}1$", r"$4$", r"$\dfrac{(x+3)(x-1)}{x-1}=x+3\to4$"]),
 (r"Az ábrán a $h$ függvény grafikonja látható. Folytonos-e a függvény az $x=0$, az $x=1$ és az $x=3$ helyen? "
  r"Indokold!" + svgwrap(SVG_II_4), None,
  r"$x=0$: igen, a parabola-ív itt megszakítás nélkül halad ($\lim\limits_{x\to0}h(x)=h(0)=0$); $x=1$: igen — a grafikon itt megtörik, de nem szakad meg ($\lim\limits_{x\to1}h(x)=h(1)=1$); "
  r"$x=3$: nem, mert a bal oldali határérték $-1$, a jobb oldali $1$"),
 LIMS("Számítsd ki a határértékeket behelyettesítéssel!",
      [("(x**2+4*x-5)/(x**2-1)", 2), ("(x**2+4*x-5)/(x**2-1)", -5), ("(x**3+2*x)/(x**2+4)", -1), ("sqrt(x)+log(x, 2)", 4)],
      tex={"sqrt(x)+log(x, 2)": r"\left(\sqrt x+\log_2x\right)"}),
 LIMS("Számítsd ki a határértékeket!", [("(x**2-49)/(x**2-7*x)", 7), ("(x**2-4*x)/(3*x**2-48)", 4), ("(7*x**2+8*x+1)/(x+1)", -1)]),
 LIMS("Számítsd ki a határértékeket!", [("(x**2+3*x-10)/(x**2-x-2)", 2), ("(x**2+6*x-7)/(x**2-5*x+4)", 1), ("(x**2+3*x)/(x**2-9)", -3)]),
 LIMS("Számítsd ki a határértékeket!", [("(x**2-6*x+5)/(x**2-8*x+15)", 5), ("(x+2)/(3*x**2+5*x-2)", -2), ("(x**2-16)/(x+4)", -4)]),
 LIMS("Számítsd ki a határértékeket!", [("(x**2+5*x)/(x**2-25)", -5), ("(2*x**2-3*x-2)/(x-2)", 2), ("(x**2-x-12)/(x**2-16)", 4)]),
 LIMS("Számítsd ki a határértékeket!", [("(3*x**2+5*x-2)/(x+2)", -2), ("(x**2-7*x+12)/(9-x**2)", 3), ("(x**2-2*x)/(x**2-4)", 2)]),
 LIMS("Számítsd ki a határértékeket!",
      [("(x**2+4*x-5)/(x**2-1)", oo), ("(5*x**2-7*x)/(2*x**2+3)", oo), ("(5*x**2-7*x)/(2*x**4+3)", oo), ("(5*x**5-7*x)/(2*x**4+3)", oo)]),
 LIMS("Számítsd ki a határértékeket!",
      [("(3*x**2-x+1)/(6*x**2+3*x+2)", -oo), ("(-4*x**3+x**2-1)/(x**2+x-1)", oo), ("(2*x+1)/(x**2-x-2)", -oo),
       ("(x**5-3*x**2+2)/(1+7*x-3*x**2)", oo)]),
 LIMS("Számítsd ki a határértékeket!",
      [("(x+3)/(x-2)", oo), ("(x-2)/(x+1)", -oo), ("(7-2*x)/(4*x+1)", oo), ("(3*x**2-1)/(2-x**2)", -oo)]),
 LIMS("Számítsd ki a határértékeket! (Gondolj a grafikonokra.)",
      [("2**x", oo), ("(Rational(1,3))**x", oo), ("(Rational(1,3))**x", -oo), ("log(x, 2)", oo), ("5/x**3", -oo)],
      tex={"(Rational(1,3))**x": r"\left(\frac13\right)^x", "log(x, 2)": r"\log_2x"}),
 ASZS("Határozd meg a függvények aszimptotáit!", ["(2*x+2)/(x-3)", "6*x/(x-1)**2"]),
 ASZS("Határozd meg a függvények aszimptotáit!", ["(4-x**2)/(x**2+1)", "(x**2-3)/(x**2+1)"]),
 ASZS("Határozd meg a függvények aszimptotáit!", ["(3*x-1)/(x+2)", "(5-x)/(2*x-4)"]),
 ASZS("Határozd meg a függvények aszimptotáit!", ["4*x/(x**2-9)", "(x**2+1)/(x**2-4)"]),
]
K_II = [
 ("Mit mondhatsz a $\\lim\\limits_{x\\to a}f(x)$ határértékről és az $a$-beli folytonosságról?",
  [r"$\lim\limits_{x\to a-0}f(x)=2$, $\lim\limits_{x\to a+0}f(x)=2$, $f(a)=5$",
   r"$\lim\limits_{x\to a-0}f(x)=1$, $\lim\limits_{x\to a+0}f(x)=3$, $f(a)=3$",
   r"$\lim\limits_{x\to a-0}f(x)=4$, $\lim\limits_{x\to a+0}f(x)=4$, $f(a)=4$"],
  ["a határérték $2$; nem folytonos, mert $f(a)\\ne2$", "nincs határérték (a két oldal különbözik); nem folytonos",
   "a határérték $4=f(a)$; folytonos"]),
 ("Milyen paraméterérték mellett lesz a függvény folytonos a megadott helyen?",
  [r"$f(x)=\begin{cases}x+a, & x\lt2\\ 3x-1, & x\ge2\end{cases}$, az $x=2$ helyen",
   r"$g(x)=\begin{cases}bx^2, & x\lt1\\ 4-x, & x\ge1\end{cases}$, az $x=1$ helyen"],
  ["$2+a=5$, tehát $a=3$", r"$b\cdot1^2=4-1$, tehát $b=3$"]),
 LIMS("Számítsd ki a határértékeket! (Bővíts a konjugálttal.)",
      [("(sqrt(x-2)-2)/(x-6)", 6), ("(sqrt(1+x)-sqrt(1-x))/(4*x)", 0), ("(sqrt(x**2+x+1)-1)/x", 0)]),
 LIMS("Számítsd ki a határértékeket! (Itt a gyök a nevezőben van.)",
      [("(x-5)/(sqrt(5*x)-5)", 5), ("(x-3)/(sqrt(x+1)-2)", 3), ("x/(sqrt(1+3*x)-1)", 0), ("(5-x)/(3-sqrt(x+4))", 5)]),
 LIMS("Számítsd ki a határértékeket!", [("(sqrt(x+12)-4)/(x-4)", 4), ("(x-9)/(sqrt(x)-3)", 9), ("(sqrt(x+1)-2)/(x**2-9)", 3)]),
 LIMS("Számítsd ki az egyoldali határértékeket!",
      [("(x+3)/(x-2)", 2, "+"), ("(x+3)/(x-2)", 2, "-"), ("(x-2)/(x+1)", -1, "+"), ("(x-2)/(x+1)", -1, "-")]),
 ("Véd Vilmos ezeket írta a füzetébe. Mit rontott el? Mennyi a helyes határérték?",
  [r"$\lim\limits_{x\to-2}\dfrac{x^2-4}{x+2}=\dfrac00=1$", r"$\lim\limits_{x\to3+0}\dfrac{x+1}{x-3}=\dfrac40=0$",
   r"$\lim\limits_{x\to1-0}\dfrac{2-x}{x-1}=+\infty$"],
  [r"a $\frac00$ határozatlan; egyszerűsítve $x-2\to-4$", r"$\frac40$ alakú (nem $\frac00$): a nevező jobbról pozitív, tehát $+\infty$",
   r"balról a nevező negatív, a számláló $1$-hez tart: $-\infty$"]),
 LIMS("Számítsd ki a határértékeket! Figyelj az előjelre!",
      [("(x**3-2)/(x+5)", -oo), ("(2*x**4+1)/(x-3)", -oo), ("(x-4*x**3)/(x**2+1)", -oo), ("(x**2+5)/(3-x)", -oo)]),
 ("Merre tart a függvény a grafikon két szélén? Add meg a $-\\infty$-beli és a $+\\infty$-beli határértéket!",
  [r"$f(x)=\dfrac{x^3}{x^2+1}$", r"$g(x)=\dfrac{2x^2}{x^2+1}$", r"$h(x)=\dfrac{1-x^4}{x^2+3}$"],
  ["$-\\infty$ és $+\\infty$ (bal szélen le, jobb szélen fel)", "mindkét irányban $2$",
   "mindkét irányban $-\\infty$"]),
 ("Lyuk vagy függőleges aszimptota? Egyszerűsíts, és döntsd el!",
  [r"$f(x)=\dfrac{x^2-5x+6}{x-2}$", r"$g(x)=\dfrac{x+1}{x^2-1}$", r"$h(x)=\dfrac{x^2-16}{(x-4)^2}$"],
  [r"az $x=2$ helyen lyuk ($f\to-1$), függőleges aszimptota nincs", r"az $x=-1$ helyen lyuk ($g\to-\frac12$), az $x=1$ függőleges aszimptota",
   r"$h(x)=\frac{x+4}{x-4}$: az $x=4$ függőleges aszimptota (egyszerűsítés után is a nevezőben marad)"]),
 (r"Vizsgáld meg az $f(x)=\dfrac{2x^2-8}{x^2-1}$ függvényt!",
  ["Határozd meg az értelmezési tartományát és a zérushelyeit!", "Határozd meg az aszimptotáit!",
   "Vázold a grafikont az aszimptoták és a zérushelyek alapján!"],
  [r"$D_f=\mathbb R\setminus\{-1;\,1\}$; zérushelyek: $-2$ és $2$", r"függőleges: $x=-1$ és $x=1$; vízszintes: $y=2$",
   r"a görbe a két szélén az $y=2$-höz simul; $x\to-1-0$: $-\infty$, $x\to-1+0$: $+\infty$, $x\to1-0$: $+\infty$, $x\to1+0$: $-\infty$; $f(0)=8$"]),
 ("Metszi-e a grafikon a vízszintes aszimptotáját? Ha igen, hol?",
  [r"$f(x)=\dfrac{x^2+2x}{x^2+1}$", r"$g(x)=\dfrac{2x-1}{x+3}$"],
  [r"a vízszintes aszimptota $y=1$; $\frac{x^2+2x}{x^2+1}=1$ ⇔ $x=\frac12$: a $\left(\frac12;\,1\right)$ pontban",
   r"a vízszintes aszimptota $y=2$; $\frac{2x-1}{x+3}=2$-ből $-1=6$ adódna, ez ellentmondás: a grafikon nem metszi az aszimptotát"]),
]
N_II = [
 ASZS("Határozd meg a függvények aszimptotáit!", ["(3-x**2)/(x+2)", "(x**2-8)/(x+3)", "(x**2+x-2)/(x+3)"]),
 ASZS("Határozd meg a függvények aszimptotáit!", ["-x**3/(x**2+3)", "(x**2-x-2)/(x-3)", "(x**2+7*x+10)/(x+1)", "(x**2-5*x+4)/(x-5)"]),
 ASZS("Határozd meg a függvények aszimptotáit! A második függvénynél figyelj a számlálóra is!", ["2*x/3+3/(2*x)", "(x**3+1)/(x**2-1)"]),
 (r"Határozd meg a $b$ értékét úgy, hogy az $f(x)=\dfrac{2x^2+bx}{x+1}$ függvény ferde aszimptotája az $y=2x+1$ egyenes legyen!",
  None, r"$k=2$; $n=\lim\limits_{x\to+\infty}\dfrac{(b-2)x}{x+1}=b-2=1$, tehát $b=3$ (a függőleges aszimptota $x=-1$)"),
]
N_II[2] = (N_II[2][0], N_II[2][1],
           [N_II[2][2][0], N_II[2][2][1] + r" — az $x=-1$ helyen lyuk van (a $\left(-1;\,-\frac32\right)$ pontban), mert ott a számláló is $0$"])
JOKER_II = ("Véd Vilmos saját falat akar építeni: olyan racionális függvényt keres, amelynek függőleges aszimptotája "
            "az $x=2$, ferde aszimptotája az $y=x-1$ egyenes.",
            [r"Például $f(x)=x-1+\dfrac{1}{x-2}=\dfrac{x^2-3x+3}{x-2}$ (a tört a végtelenben $0$-hoz tart, a $2$-ben végtelenbe szakad).",
             r"$k=\lim\limits_{x\to+\infty}\frac{f(x)}{x}=1$, $n=\lim\limits_{x\to+\infty}\big(f(x)-x\big)=-1$, és $x=2$-ben a számláló $1\ne0$."],
            ["Adj meg egy ilyen függvényt!", "Ellenőrizd, hogy $k=1$, $n=-1$, és hogy az $x=2$ valóban függőleges aszimptota!"])

# ================================================================ ÖNELLENŐRZÉS
assert (len(A_I), len(K_I), len(N_I)) == (12, 8, 2), (len(A_I), len(K_I), len(N_I))
assert (len(A_II), len(K_II), len(N_II)) == (18, 12, 4), (len(A_II), len(K_II), len(N_II))
# kézzel írt végeredmények ellenőrzése
chk("I-1", [Ex("(3*x-8)/2").subs(x, a) for a in (2, 1, 0, -2, Q(-4, 3))], [-1, Q(-5, 2), -4, -7, -6])
chk("I-1g", [Ex("(5*x-1)/(x**2+1)").subs(x, a) for a in (2, 1, 0, -2, Q(-4, 3))], [Q(9, 5), 2, -1, Q(-11, 5), Q(-69, 25)])
chk("I-1h", [(a - 1 if a >= 1 else -a ** 2 + 1) for a in (2, 1, 0, -2, Q(-4, 3))], [1, 0, 1, -3, Q(-7, 9)])
f1, g1 = Ex("(3*x-8)/2"), Ex("(5*x-1)/(x**2+1)")
chk("I-2", [f1.subs(x, Q(-2, 3)) * g1.subs(x, -1), Q(14, 3) * f1.subs(x, Q(2, 7)) - Q(5, 6) * g1.subs(x, Q(1, 2))], [15, Q(-53, 3)])
chk("I-7", [sorted(solveset(Ex("x**3-4*x"), x, S.Reals)), list(solveset(Ex("(x**2-1)/(x+1)"), x, DOM("(x**2-1)/(x+1)"))),
            list(solveset(Ex("(x**2-5*x)/(x-5)"), x, DOM("(x**2-5*x)/(x-5)"))), list(solveset(Ex("2**x-8"), x, S.Reals))],
    [[-2, 0, 2], [1], [0], [3]])
chk("I-12", [min(p[1] for p in PT_I), max(p[1] for p in PT_I), tv(-3, PT_I), tv(-1, PT_I), tv(3, PT_I)], [-2, 4, 0, 0, 0])
chk("I-K1", math.log(3, 3), 1)
chk("I-K8", [PARITAS("x**4-2*x**2"), PARITAS("x**3-3*x"), PARITAS("x**2/2+x"), Ex("x**2/2+x").subs(x, 2),
             Ex("x**2/2+x").subs(x, -2)], ["páros", "páratlan", "egyik sem", 4, 0])
chk("I-N2", ELOJEL("(x**2-x-6)/(x**2-1)").count("cup"), 3)
chk("II-3", [round(float(Ex("(x**2+2*x-3)/(x-1)").subs(x, t)), 2) for t in (0.9, 0.99, 1.01, 1.1)], [3.9, 3.99, 4.01, 4.1])
chk("II-K2", [solve(Ex("2") + symbols("a") - 5)[0], solve(symbols("b") * 1 - 3)[0]], [3, 3])
chk("II-K7", [LIM("(x**2-4)/(x+2)", -2), LIM("(x+1)/(x-3)", 3, "+"), LIM("(2-x)/(x-1)", 1, "-")], [-4, oo, -oo])
chk("II-K9", [LIM("x**3/(x**2+1)", -oo), LIM("x**3/(x**2+1)", oo), LIM("2*x**2/(x**2+1)", -oo), LIM("(1-x**4)/(x**2+3)", -oo),
              LIM("(1-x**4)/(x**2+3)", oo)], [-oo, oo, 2, -oo, -oo])
chk("II-K10", [LIM("(x**2-5*x+6)/(x-2)", 2), LIM("(x+1)/(x**2-1)", -1), ASZ("(x+1)/(x**2-1)")[0], ASZ("(x**2-16)/(x-4)**2")[0]],
    [-1, Q(-1, 2), [1], [4]])
chk("II-K11", [sorted(solveset(Ex("2*x**2-8"), x, S.Reals)), Ex("(2*x**2-8)/(x**2-1)").subs(x, 0)], [[-2, 2], 8])
chk("II-N4", ASZ("(2*x**2+3*x)/(x+1)"), ([-1], None, (2, 1)))
assert not E, E

# tiltott adatok: a régi és az idei felmérők, valamint a tananyag kidolgozott példái szó szerint nem szerepelhetnek
TILTOTT = ["(3*x+14)/(2*x**2-5*x-28)", "(x+5)/(x**2+4*x-5)", "(x**2-144)/(x-12)", "(sqrt(x+9)-1)/(x+8)", "(5*x-15)/(x-6)",
           "(x-13)/(sqrt(x-4)-3)", "(x**2-3*x-10)/(x-5)", "(x-3)/(x+2)", "(x-3)/(x**2+4*x-21)", "(x**2-49)/(x+7)",
           "(sqrt(x+5)-4)/(x-11)", "(2*x+25)/(x+8)", "(x-4)/(x**2-x-12)", "(5*x-8)/(3*x+3)", "(x**2-121)/(x-11)",
           "(sqrt(x-3)-1)/(x-4)", "(5*x-18)/(x-5)", "(x+2)/(x**2-x-6)", "(3*x+1)/(2*x-2)", "(x-4)/(x**2-16)", "(x-5)/(x**2-25)",
           "(3*x+2)/(x-5)", "(2*x-3)/(12*x+24)", "(x**2-3)/(x+5)", "(2*x**2-3)/(x+5)", "(3*x+5)/(4*x-8)", "(x**2+x)/(x-2)",
           "(x+6)/(4*x-12)", "(2*x**2-5)/(x-2)", "(x-1)/(x+2)", "(2*x**2+1)/(2*x-5)", "(x+1)/(x-2)", "(2*x**2-1)/(2*x+8)",
           "(x**2-3)/(x+1)", "(2*x+1)/(2*x-12)", "(6*x+1)/(2*x-1)", "(2*x**2+1)/(2*x+4)", "(6*x**2+1)/(3*x-6)", "(x**2+1)/(3*x+9)",
           "(3*x**2-x+4)/(x+3)", "(x+4)/(x**2+7*x+12)", "(x**2-x-6)/(x**2-9)", "(sqrt(3*x+7)-4)/(x-3)", "(2*x+1)/(x-4)",
           "(6*x**3-4*x+1)/(3*x**3+2*x**2-5)", "(4*x-3)/(2*x+6)", "(x**2+3*x-2)/(x-1)", "(2*x**2+5*x-1)/(x-3)",
           "(x-5)/(x**2-2*x-15)", "(x**2+5*x+6)/(x**2-4)", "(sqrt(2*x+5)-3)/(x-2)", "(3*x-2)/(x+5)", "(4*x**2-7*x+2)/(5-2*x**2)",
           "(9*x+2)/(3*x-6)", "(x**2-2*x+5)/(x+2)", "(x**2+3*x+2)/(x+2)", "(x**2+4*x-5)/(2*x**2-2)", "(x-4)/(sqrt(2*x+1)-3)",
           "(x+3)/(4-2*x)", "(3*x**2+x)/(x**2-5*x+1)", "(8-2*x)/(x+3)", "(2*x**2+x-1)/(x+3)",
           # tananyag-példák (4e/02)
           "(x**2-1)/(x-1)", "(x**2+1)/(x+3)", "(x**2+x-6)/(x+3)", "(x**2-4)/(x**2-3*x+2)", "(sqrt(x)-2)/(x-4)",
           "x/(sqrt(x+1)-1)", "(x+2)/(x-1)", "(x**2-9)/(x-3)", "1/(x-2)", "(2*x**2-x)/(x**2+3)", "(5*x+1)/(x**2+4)",
           "(x**3+x)/(2*x**2-1)", "(x**4+1)/(x**2+x)", "(1-x**3)/(x**2+2)", "(2*x+1)/(x-3)", "(x**2-4)/(x-2)", "x/(x**2+1)",
           "(x**2+1)/(x-1)", "(2*x**2+x)/(x-1)", "(x**2-25)/(x+5)", "(x**2-3*x)/(x-3)", "sqrt(x+3)/(x-2)", "(x+1)*(x-3)/(x-1)",
           "x**4-3*x**2", "x**3+2*x", "x**2+x", "x*sin(x)", "x**3+1"]
HASZNALT = re.findall(r'"([^"]*x[^"]*)"', open(__file__, encoding="utf-8").read().split("# ================================================================ ZSOLDOS-LISTA I.")[1]
                      .split("# ================================================================ ÖNELLENŐRZÉS")[0])


def _alak(s):
    try:
        a, b = Ex(s).as_numer_denom()
        return (sympy.expand(a), sympy.expand(b))
    except Exception:
        return None


TA = {_alak(t) for t in TILTOTT}
for h in HASZNALT:
    ah = _alak(h)
    if ah is not None and ah in TA:
        E.append(("tiltott", h))
assert not E, E
print("sympy önteszt: OK")

# ================================================================ OLDALAK
def lista(A, K, N, J):
    return "\n".join([
        '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(A, "alap", "alap"),
        '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(K, "kozep", "kozep"),
        '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(N, "nehez", "nehez"),
        '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(J[0], J[1], J[2])])


u1 = oldal(**T, fajl="feladatok-tulajdonsagok.html", cim="Zsoldos-lista I. — Tulajdonságok",
           h1="Függvények — Zsoldos-lista I.: tulajdonságok", itt="Zsoldos-lista I. — Tulajdonságok",
           alcim="Helyettesítési érték, elemi függvények, értelmezési tartomány, zérushely és előjel, paritás, "
                 "grafikonelemzés. A végeredmény minden feladatnál lenyitható — előbb számolj!",
           sections_html=lista(A_I, K_I, N_I, JOKER_I), ossz_nev="Csalópapírt",
           prev="tananyag-aszimptotak.html", prevc="Aszimptoták",
           nxt="feladatok-hatarertek-aszimptota.html", nxtc="Zsoldos-lista II. — Határérték és aszimptoták")
u2 = oldal(**T, fajl="feladatok-hatarertek-aszimptota.html", cim="Zsoldos-lista II. — Határérték és aszimptoták",
           h1="Függvények — Zsoldos-lista II.: határérték és aszimptoták", itt="Zsoldos-lista II. — Határérték és aszimptoták",
           alcim="Határérték grafikonról, behelyettesítés, 0/0 szorzattá alakítással és konjugálttal, egyoldali határérték, "
                 "határérték a végtelenben, aszimptoták. A végeredmény minden feladatnál lenyitható!",
           sections_html=lista(A_II, K_II, N_II, JOKER_II), ossz_nev="Csalópapírt",
           prev="feladatok-tulajdonsagok.html", prevc="Zsoldos-lista I. — Tulajdonságok",
           nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
print("✓", os.path.basename(u1), "| I.", len(A_I), len(K_I), len(N_I), "+ Joker")
print("✓", os.path.basename(u2), "| II.", len(A_II), len(K_II), len(N_II), "+ Joker")
