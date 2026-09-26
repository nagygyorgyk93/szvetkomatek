# -*- coding: utf-8 -*-
"""4e/04 — ket feladatgyujtemeny: Zsoldos-lista I. (hatarozatlan integral) es II. (hatarozott integral, terulet).
Feladat-terkep: projektek/4e/munkafajlok/terkep_fgy_04-integral.md (jovahagyva 2026-09-26).
Forrasok (a terkep szerint): Feladatok - Hatarozatlan integralok (HI), vegyes gyakorlas (VG), Hatarozott_integralok-
Feladatok (HF), Sikidomok teruletenek kiszamitasa (SF), Vene 4.1-4.2, 4.5-4.6 + sajat feladatok; a felmerok adatai
(tiltott_4e_04) es a tananyag kidolgozott peldai kiserve.
Minden vegeredmeny sympybol: a primitiv fuggvenyeket derivaljuk, a hatarozott integralokat es a terueleteket
numerikusan (mpmath) is ujraszamoljuk. A terulet-feladatok kulcsa: vegeredmeny + abra (felhasznaloi dontes)."""
import sys, os, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal, w
from tananyag_common import svg_fuggvenyek
import tiltott_4e_04 as TILT
import sympy
import mpmath as mp
from sympy import Rational as Q, symbols, latex, sympify, diff, solve, nsimplify
from sympy.parsing.sympy_parser import parse_expr

x, t = symbols("x t", real=True)
LD = {"x": x, "t": t, "Rational": Q, "sqrt": sympy.sqrt, "root": sympy.root, "log": sympy.log, "exp": sympy.exp,
      "sin": sympy.sin, "cos": sympy.cos, "tan": sympy.tan, "cot": sympy.cot, "pi": sympy.pi, "E": sympy.E,
      "Abs": sympy.Abs}
LDT = dict(LD, x=symbols("x"), t=symbols("t"))
T = dict(tagozat="4e", mappa="04-integral", temakor="Integrál")
KEK, PIROS, ZOLD, BORO, SOT, SZURKE = "#3b82f6", "#ef4444", "#047857", "#f59e0b", "#0f172a", "#64748b"
E = []                  # önteszt-hibák
INTEGRANDUSOK = []      # tiltott-ellenőrzéshez
FUGGVENYEK = []         # primitív függvények, terület-függvények (szintén ellenőrizve)
PAROK = []              # két görbe


def Ex(s):
    return s if isinstance(s, sympy.Basic) else sympify(s, locals=LD)


_FN = {"sin": r"\sin", "cos": r"\cos", "tan": r"\operatorname{tg}", "cot": r"\operatorname{ctg}", "log": r"\ln"}


def _fn(m):
    nev, kit, arg = _FN[m.group(1)], m.group(2) or "", m.group(3).strip()
    if re.fullmatch(r"(\d+ )?[xt]|\\frac\{1\}\{x\}|\\sqrt\{x\}|\\left\|\{?x\}?\\right\||\d+", arg):
        return f"{nev}{kit} {arg.replace(' ', '')} "
    return f"{nev}{kit}\\left({arg}\\right)"


_FNRE = re.compile(r"\\(sin|cos|tan|cot|log)(\^\{\d+\})?\{\\left\(((?:(?!\\(?:sin|cos|tan|cot|log)\{\\left\().)*?) "
                   r"\\right\)\}")


def _minusz_tort(t_):
    """\\dfrac{- A}{B} → -\\dfrac{A}{B}, ha a számláló egyetlen (előjeles) szorzat."""
    ki, i = "", 0
    while True:
        m_ = re.compile(r"\\dfrac\{- ?").search(t_, i)
        if not m_:
            return ki + t_[i:]
        j = m_.start()
        k, mely = j + len(r"\dfrac{"), 1
        while mely:
            mely += {"{": 1, "}": -1}.get(t_[k], 0); k += 1
        szaml = t_[m_.end():k - 1]
        d, ok = 0, True
        for m in re.finditer(r"\\left[(|]|\\right[)|]|[{}]| [+-] ", szaml):
            g = m.group(0)
            d += 1 if g in ("{", r"\left(", r"\left|") else -1 if g in ("}", r"\right)", r"\right|") else 0
            if g.strip() in "+-" and d == 0:
                ok = False
        ki += t_[i:j] + ((r"-\dfrac{" + szaml + "}") if ok else t_[j:k])
        i = k


def TX(s):
    """sympy-szintaxisú string → TeX a leírt alakban (evaluate=False)."""
    t_ = latex(parse_expr(s, local_dict=LDT, evaluate=False), order="none") if isinstance(s, str) else latex(s)
    t_ = re.sub(r"\\log\{\\left\(((?:(?!\\log).)*?) \\right\)\}\^\{(\d+)\}", r"\\log^{\2}{\\left(\1 \\right)}", t_)
    for _ in range(4):
        t_ = _FNRE.sub(_fn, t_)
    t_ = re.sub(r"\\ln\\left\(\\left\|(.*?)\\right\|\\right\)", r"\\ln\\left|\1\\right|", t_)
    t_ = re.sub(r"\\left\|\{(.*?)\}\\right\|", r"\\left|\1\\right|", t_)
    t_ = re.sub(r"\\ln\^\{(\d+)\} ([^ ]+) ", r"\\left(\\ln \2\\right)^{\1} ", t_)
    t_ = re.sub(r"(?<![\d.}])1 \\frac", r"\\frac", t_)
    t_ = t_.replace(r"\left(-1\right) ", "-")
    t_ = t_.replace(r"\frac", r"\dfrac")
    t_ = re.sub(r"\^\{\\dfrac", r"^{\\frac", t_)
    t_ = t_.replace(r"\ln e", "1")
    t_ = _minusz_tort(re.sub(r"\s+", " ", t_))
    return re.sub(r"\s+", " ", t_).strip()


def _zar(s):
    """integrandus TeX-je: összeg/különbség zárójelbe."""
    e = parse_expr(s, local_dict=LDT, evaluate=False)
    tx = TX(s)
    return r"\left(" + tx + r"\right)" if isinstance(e, sympy.Add) else tx


def INT(f, a=None, b=None, v="x"):
    hat = "" if a is None else f"_{{{TX(a).replace(chr(92) + 'dfrac', chr(92) + 'frac')}}}^{{{TX(b).replace(chr(92) + 'dfrac', chr(92) + 'frac')}}}"
    return rf"\displaystyle\int{hat} {_zar(f)}\,d{v}"


# ---------------------------------------------------------------- ellenőrzés
_PTS = [Q(7, 10), Q(13, 10), Q(21, 10), Q(37, 10), Q(-7, 10), Q(-17, 10), Q(1, 10), Q(-31, 10), Q(47, 10), Q(1, 3),
        Q(-1, 3), Q(11, 2)]


def _pontok(f1, f2, v):
    ki = []
    for p in _PTS:
        try:
            a, b = complex(f1.subs(v, p).evalf(30)), complex(f2.subs(v, p).evalf(30))
        except (TypeError, ZeroDivisionError, ValueError):
            continue
        if abs(a.imag) > 1e-12 or abs(b.imag) > 1e-12 or not (math.isfinite(a.real) and math.isfinite(b.real)):
            continue
        ki.append((a.real, b.real))
    return ki


def egyenlo(nev, a, b, v=x):
    pts = _pontok(a, b, v)
    if len(pts) < 2 or any(abs(p - q) > 1e-8 * max(1, abs(p)) for p, q in pts):
        E.append((nev, a, b, len(pts)))


def primitiv_e(f, F, v=x, nev=""):
    egyenlo(nev or str(f), diff(Ex(F), v), Ex(f), v)


def HI(intro, tetelek, v="x", rovid=False):
    """tetelek = [(integrandus, primitív[, TeX-kijelzés])] — a primitív deriváltja = integrandus."""
    subs, ans = [], []
    for tt in tetelek:
        f, F = tt[0], tt[1]
        vv = t if t in Ex(f).free_symbols else x
        primitiv_e(f, F, vv, f"{intro[:18]}… {f}")
        INTEGRANDUSOK.append(f); FUGGVENYEK.append(F)
        subs.append(f"${INT(f, v=str(vv))}$")
        ans.append(f"${tt[2] if len(tt) > 2 and tt[2] else TX(F)}+C$" + (f" ({tt[3]})" if len(tt) > 3 else ""))
    return (intro, subs, ans, rovid) if rovid else (intro, subs, ans)


def _num(f, a, b, tores=()):
    g = sympy.lambdify(x, Ex(f), "mpmath")
    mp.mp.dps = 30
    pts = [mp.mpf(sympy.N(a, 40))] + [mp.mpf(sympy.N(c, 40)) for c in tores] + [mp.mpf(sympy.N(b, 40))]
    return mp.quad(g, pts)


def hatarozott(f, a, b, ertek, nev=""):
    kap = _num(f, Ex(a), Ex(b))
    if abs(kap - mp.mpf(sympy.N(Ex(ertek), 40))) > mp.mpf(10) ** -18:
        E.append(("határozott", nev, f, a, b, ertek, kap))
    # szimbolikusan is
    try:
        s = sympy.simplify(sympy.integrate(Ex(f), (x, Ex(a), Ex(b))) - Ex(ertek))
        if s != 0 and abs(sympy.N(s, 30)) > 1e-20:
            E.append(("határozott-sympy", nev, f, s))
    except Exception:
        pass


def HA(intro, tetelek, rovid=False):
    """tetelek = [(integrandus, a, b, érték[, TeX-kijelzés])]."""
    subs, ans = [], []
    for tt in tetelek:
        f, a, b, e = tt[:4]
        hatarozott(f, a, b, e, intro[:18])
        INTEGRANDUSOK.append(f)
        subs.append(f"${INT(f, a, b)}$")
        ans.append(f"${tt[4] if len(tt) > 4 else TX(e)}$")
    return (intro, subs, ans, rovid) if rovid else (intro, subs, ans)


def svgwrap(svg):
    return f'<div class="svgwrap">{svg}</div>'


def _gyokok(h, lo, hi):
    return sorted([r for r in solve(Ex(h), x) if r.is_real and Ex(lo) < r < Ex(hi)], key=float)


def terulet(f, lo, hi, g=None):
    """(T, [(a, b, előjeles integrál)]) — f és g (vagy az x tengely) közötti terület a [lo; hi]-n."""
    h = Ex(f) - (Ex(g) if g is not None else 0)
    hat = [Ex(lo)] + _gyokok(h, lo, hi) + [Ex(hi)]
    reszek = [(hat[i], hat[i + 1], sympy.simplify(sympy.integrate(h, (x, hat[i], hat[i + 1]))))
              for i in range(len(hat) - 1)]
    T_ = sympy.simplify(sum(sympy.Abs(r[2]) for r in reszek))
    num = sum(abs(_num(h, a, b)) for a, b, _ in reszek)
    if abs(num - mp.mpf(sympy.N(T_, 40))) > mp.mpf(10) ** -18:
        E.append(("terület-num", f, g, lo, hi, T_, num))
    return T_, reszek


def _szoveg(e):
    return str(Ex(e)).replace("**", "^").replace("*", "·").replace("exp(", "e^(").replace("log(", "ln(")


def ABRA(f, lo, hi, g=None, xr=None, yr=None, w_=320, h_=220, leiras="", pontok=None, feliratok=("f", "g"),
         szak=None):
    """Terület-ábra: f (és g) grafikonja, az árnyékolt tartomány; a tengely alatti rész pirossal."""
    F = sympy.lambdify(x, Ex(f), "math")
    G = sympy.lambdify(x, Ex(g), "math") if g is not None else None
    lo_, hi_ = float(Ex(lo)), float(Ex(hi))
    if xr is None:
        sz = max(1.0, (hi_ - lo_) * 0.18)
        xr = (min(lo_ - sz, -0.6), max(hi_ + sz, 0.6))
    xs = [xr[0] + (xr[1] - xr[0]) * i / 200 for i in range(201)]
    if yr is None:
        bent = [v for v in xs if lo_ - 1e-9 <= v <= hi_ + 1e-9] or xs
        ys = [F(v) for v in bent] + ([G(v) for v in bent] if G else []) + [0.0]
        a_, b_ = min(ys), max(ys)
        pad = max(0.8, (b_ - a_) * 0.15)
        yr = (a_ - pad if a_ < 0 else -0.7, max(b_ + pad, 2.2))
    gorbek = [(F, SOT, feliratok[0], szak or [(xr[0] + 0.05, xr[1] - 0.05)])]
    if G:
        gorbek.append((G, KEK, feliratok[1], [(xr[0] + 0.05, xr[1] - 0.05)]))
    h = Ex(f) - (Ex(g) if g is not None else 0)
    hat = [lo_] + [float(r) for r in _gyokok(h, lo, hi)] + [hi_]
    ter = []
    for i in range(len(hat) - 1):
        m = (hat[i] + hat[i + 1]) / 2
        if G:
            ter.append((G, F, hat[i], hat[i + 1], ZOLD, 0.3) if F(m) >= G(m) else (F, G, hat[i], hat[i + 1], ZOLD, 0.3))
        else:
            ter.append((F, None, hat[i], hat[i + 1], ZOLD if F(m) >= 0 else PIROS, 0.35))
    pts = pontok if pontok is not None else [(v, 0.0, "", SOT) for v in hat if not G] + (
        [(v, F(v), "", SOT) for v in hat] if G else [])
    jel = f" (az ábrán fekete: ${feliratok[0]}$, kék: ${feliratok[1]}$)" if G else ""
    return jel + svgwrap(svg_fuggvenyek(gorbek, xr=xr, yr=yr, w=w_, h=h_, jelmagyarazat=False, terulet=ter,
                                        pontok=pts, egyseg=("1", "1"),
                                        leiras=leiras or (f"Az y = {_szoveg(f)}" + (f" és az y = {_szoveg(g)}" if G else "")
                                                          + f" grafikonja; árnyékolva a síkidom a [{_szoveg(lo)}; "
                                                          f"{_szoveg(hi)}] intervallumon")))


def Tsz(T_):
    return TX(T_) if not isinstance(T_, str) else T_


# ================================================================ ZSOLDOS-LISTA I. — HATÁROZATLAN INTEGRÁL
A_I = [
 HI("Határozd meg a primitív függvényeket (olyan $F$-et keresünk, amelynek a deriváltja az adott függvény), és "
    "ellenőrizd deriválással!", [("4*x", "2*x**2"), ("x**4", "x**5/5"), ("-4*t**3", "-t**4"), ("-5*sin(x)", "5*cos(x)"),
                                 ("2*exp(x)", "2*exp(x)")], rovid=True),
 ("Döntsd el deriválással, hogy az $F$ primitív függvénye-e az $f$ függvénynek! Ha nem, javítsd ki $F$-et!",
  [r"$f(x)=3x^2-4x+1$, $F(x)=x^3-2x^2+x-5$", r"$f(x)=\dfrac{1}{x^2}$, $F(x)=7-\dfrac1x$",
   r"$f(x)=(3x+2)^3$, $F(x)=\dfrac{(3x+2)^4}{4}$"],
  [r"igen: $F'(x)=3x^2-4x+1=f(x)$", r"igen: $F'(x)=\dfrac{1}{x^2}=f(x)$",
   r"nem: $F'(x)=\dfrac{4(3x+2)^3\cdot 3}{4}=3(3x+2)^3\ne f(x)$ — a belső függvény deriváltja miatt még "
   r"$3$‑mal osztani kell; helyesen például $F(x)=\dfrac{(3x+2)^4}{12}$"]),
 ("Határozd meg az $f$ függvény azon $F$ primitív függvényét, amelynek grafikonja átmegy az $M$ ponton!",
  [r"$f(x)=3x^2-6x$, $M(2;\,1)$", r"$f(x)=2x-4x^3$, $M(1;\,3)$", r"$f(x)=2x-\dfrac{2}{x^3}$, $M(1;\,2)$"],
  [r"$F(x)=x^3-3x^2+C$, $F(2)=-4+C=1$, így $C=5$: $F(x)=x^3-3x^2+5$",
   r"$F(x)=x^2-x^4+C$, $F(1)=C=3$: $F(x)=x^2-x^4+3$",
   r"$F(x)=x^2+\dfrac{1}{x^2}+C$, $F(1)=2+C=2$, így $C=0$: $F(x)=x^2+\dfrac{1}{x^2}$"]),
 HI("Írd át a törteket és a gyököket hatvánnyá, majd integrálj!",
    [("1/x**3", "-1/(2*x**2)"), ("4/x**5", "-1/x**4"), ("x*sqrt(x)", "Rational(2,5)*x**2*sqrt(x)"),
     ("root(x**2,3)", "Rational(3,5)*x*root(x**2,3)"), ("3/root(x,4)", "4*root(x**3,4)")], rovid=True),
 HI("Integráld tagonként a polinomokat!",
    [("5*x**3-4*x**2-3*x+5", "Rational(5,4)*x**4-Rational(4,3)*x**3-Rational(3,2)*x**2+5*x"),
     ("x**3-2*x**2+2*x-1", "x**4/4-Rational(2,3)*x**3+x**2-x"),
     ("2*x**2-3*x+4", "Rational(2,3)*x**3-Rational(3,2)*x**2+4*x"),
     ("9*x**8-6*x**5+x-7", "x**9-x**6+x**2/2-7*x")]),
 HI("Számítsd ki az integrálokat a táblázat segítségével!",
    [("3*exp(x)-2*sin(x)", "3*exp(x)+2*cos(x)"), ("4*cos(x)+1/cos(x)**2", "4*sin(x)+tan(x)"),
     ("2**x+1/sin(x)**2", "2**x/log(2)-cot(x)", r"\dfrac{2^{x}}{\ln 2}-\operatorname{ctg} x"),
     ("5*exp(x)-3/x", "5*exp(x)-3*log(Abs(x))")]),
 HI("Írd át a gyököket törtkitevős hatvánnyá, és integrálj!",
    [("x**4-sqrt(x)+x*root(x,3)+1/x**2", "x**5/5-Rational(2,3)*x*sqrt(x)+Rational(3,7)*x**2*root(x,3)-1/x"),
     ("4*sqrt(x**3)+2/sqrt(x)", "Rational(8,5)*x**2*sqrt(x)+4*sqrt(x)"),
     ("root(x,3)-1/root(x**2,3)", "Rational(3,4)*x*root(x,3)-3*root(x,3)")]),
 HI("Bontsd fel a törtet tagokra, és integrálj!",
    [("(x-2)/x**3", "-1/x+1/x**2"), ("(10*x**8+3)/x**4", "2*x**5-1/x**3"),
     ("(3*x**3+1)/(5*x)", "x**3/5+log(Abs(x))/5", r"\dfrac{x^{3}}{5}+\dfrac{1}{5}\ln\left|x\right|"),
     ("(6+2*x+x**2)/x**4", "-2/x**3-1/x**2-1/x")]),
 HI("Lineáris belső függvény: integrálj, és ellenőrizd deriválással!",
    [("(3*x+1)**4", "(3*x+1)**5/15"), ("(5-2*x)**9", "-(5-2*x)**10/20"), ("(x/2+1)**3", "(x/2+1)**4/2"),
     ("root(4*x+3,3)", "Rational(3,16)*(4*x+3)*root(4*x+3,3)")]),
 HI("Lineáris belső függvény — gyök és tört:",
    [("sqrt(3*x+1)", "Rational(2,9)*(3*x+1)*sqrt(3*x+1)"), ("1/sqrt(4*x-1)", "sqrt(4*x-1)/2"),
     ("1/(5*x+2)", "log(Abs(5*x+2))/5", r"\dfrac{1}{5}\ln\left|5x+2\right|"),
     ("3/(2-x)", "-3*log(Abs(2-x))", r"-3\ln\left|2-x\right|"), ("1/(2*x+1)**2", "-1/(2*(2*x+1))")]),
 HI("Lineáris belső függvény — exponenciális és trigonometrikus:",
    [("exp(5*x)", "exp(5*x)/5"), ("exp(1-x)", "-exp(1-x)"), ("sin(3*x+2)", "-cos(3*x+2)/3"),
     ("cos(x/2)", "2*sin(x/2)"), ("1/cos(3*x)**2", "tan(3*x)/3")]),
 ("Véd Vilmos házi feladatában ez áll: $\\displaystyle\\int(4x-1)^5\\,dx=\\dfrac{(4x-1)^6}{6}+C$. Ellenőrizd "
  "deriválással, és mondd meg, mit rontott el! Utána számítsd ki a másik két integrált is — deriválással ellenőrizve.",
  [r"Mi a hiba Véd Vilmos eredményében?", r"$\displaystyle\int e^{-4x}\,dx$", r"$\displaystyle\int\dfrac{2}{3x-1}\,dx$"],
  [r"hibás: $\left(\dfrac{(4x-1)^6}{6}\right)'=4(4x-1)^5$ — elfelejtett a belső függvény deriváltjával "
   r"($4$‑gyel) osztani; helyesen $\dfrac{(4x-1)^6}{24}+C$",
   r"$-\dfrac{e^{-4x}}{4}+C$", r"$\dfrac{2}{3}\ln\left|3x-1\right|+C$"]),
]
# a kézi kulcsú feladatok ellenőrzése
for f, F in (("3*x**2-4*x+1", "x**3-2*x**2+x-5"), ("1/x**2", "7-1/x"), ("(3*x+2)**3", "(3*x+2)**4/12"),
             ("3*x**2-6*x", "x**3-3*x**2+5"), ("2*x-4*x**3", "x**2-x**4+3"), ("2*x-2/x**3", "x**2+1/x**2"),
             ("(4*x-1)**5", "(4*x-1)**6/24"), ("exp(-4*x)", "-exp(-4*x)/4"), ("2/(3*x-1)", "2*log(Abs(3*x-1))/3")):
    primitiv_e(f, F, nev="kézi " + f)
    INTEGRANDUSOK.append(f); FUGGVENYEK.append(F)
if diff(Ex("(3*x+2)**4/4"), x).equals(Ex("(3*x+2)**3")) or diff(Ex("(4*x-1)**6/6"), x).equals(Ex("(4*x-1)**5")):
    E.append("hamis párok")
if [Ex("x**3-3*x**2+5").subs(x, 2), Ex("x**2-x**4+3").subs(x, 1), Ex("x**2+1/x**2").subs(x, 1)] != [1, 3, 2]:
    E.append("ponton átmenő")

K_I = [
 ("Határozd meg az $f$ függvénynek azt az $F$ primitív függvényét, amelynek grafikonja átmegy az $M$ ponton!",
  [r"$f(x)=e^x+2x$, $M(0;\,-1)$", r"$f(x)=\sin x+\cos x$, $M\left(\dfrac{\pi}{2};\,2\right)$",
   r"$f(x)=\dfrac{1}{\cos^2x}-\dfrac{1}{\sin^2x}$, $M\left(\dfrac{\pi}{4};\,2\right)$",
   r"$f(x)=\dfrac{3}{x^2}-\dfrac{2}{x^3}$, $M(1;\,4)$"],
  [r"$F(x)=e^x+x^2+C$, $F(0)=1+C=-1$: $F(x)=e^x+x^2-2$",
   r"$F(x)=-\cos x+\sin x+C$, $F\left(\dfrac{\pi}{2}\right)=1+C=2$: $F(x)=\sin x-\cos x+1$",
   r"$F(x)=\operatorname{tg}x+\operatorname{ctg}x+C$, $F\left(\dfrac{\pi}{4}\right)=2+C=2$: "
   r"$F(x)=\operatorname{tg}x+\operatorname{ctg}x$",
   r"$F(x)=-\dfrac{3}{x}+\dfrac{1}{x^2}+C$, $F(1)=-2+C=4$: $F(x)=-\dfrac{3}{x}+\dfrac{1}{x^2}+6$"]),
 ("Határozd meg az $f$ függvényt, ha ismert a második deriváltja és a grafikonjának két pontja! (Kétszer "
  "integrálj: két állandó lesz, a két pont két egyenletet ad.)",
  [r"$f''(x)=e^x$, $M(0;\,-1)$, $N(2;\,e^2)$", r"$f''(x)=6x-4$, $M(1;\,0)$, $N(2;\,2)$"],
  [r"$f'(x)=e^x+C_1$, $f(x)=e^x+C_1x+C_2$; $1+C_2=-1$, $e^2+2C_1+C_2=e^2$, így $C_2=-2$, $C_1=1$: "
   r"$f(x)=e^x+x-2$",
   r"$f(x)=x^3-2x^2+C_1x+C_2$; $C_1+C_2=1$, $2C_1+C_2=2$, így $C_1=1$, $C_2=0$: $f(x)=x^3-2x^2+x$"]),
 HI("Szorozz be vagy alakítsd át, és csak utána integrálj!",
    [("(x+1)*(x**2-3)/(3*x**2)", "x**2/6+x/3-log(Abs(x))+1/x",
      r"\dfrac{x^{2}}{6}+\dfrac{x}{3}-\ln\left|x\right|+\dfrac{1}{x}"),
     ("(sqrt(x)+1)*(x-sqrt(x)+1)", "Rational(2,5)*x**2*sqrt(x)+x"),
     ("(x**2+1)**2", "x**5/5+Rational(2,3)*x**3+x"),
     ("(1-sqrt(x))**2/x", "log(Abs(x))-4*sqrt(x)+x", r"\ln\left|x\right|-4\sqrt{x}+x")]),
 HI("Bontsd fel a gyökös törtet tagokra, és integrálj!",
    [("(x-sqrt(x))*(1+sqrt(x))/sqrt(x)", "x**2/2-x"),
     ("(x**4+sqrt(x**3)+sqrt(x)+3)/(x*sqrt(x))", "Rational(2,7)*x**3*sqrt(x)+x+log(Abs(x))-6/sqrt(x)",
      r"\dfrac{2}{7}x^{3}\sqrt{x}+x+\ln\left|x\right|-\dfrac{6}{\sqrt{x}}"),
     ("(x**2+sqrt(x**3)+3)/sqrt(x)", "Rational(2,5)*x**2*sqrt(x)+x**2/2+6*sqrt(x)")]),
 HI("Alakítsd át azonossággal (vagy a hatványozás azonosságaival), és integrálj!",
    [("(exp(x)+1)/exp(x)", "x-exp(-x)"), ("tan(x)**2", "tan(x)-x"),
     ("(2*cos(x)**2+1)/cos(x)**2", "2*x+tan(x)"),
     ("cos(2*x)/(sin(x)**2*cos(x)**2)", "-cot(x)-tan(x)"),
     ("(1-sin(x)**3)/sin(x)**2", "-cot(x)+cos(x)")]),
 HI(r"Az $\displaystyle\int\dfrac{f'(x)}{f(x)}\,dx=\ln\left|f(x)\right|+C$ minta — ha kell, igazítsd a szorzót!",
    [("(2*x+1)/(x**2+x-3)", "log(Abs(x**2+x-3))", r"\ln\left|x^{2}+x-3\right|"),
     ("x**2/(x**3+1)", "log(Abs(x**3+1))/3", r"\dfrac{1}{3}\ln\left|x^{3}+1\right|"),
     ("exp(x)/(exp(x)+1)", "log(exp(x)+1)", r"\ln\left(e^{x}+1\right)"),
     ("cot(x)", "log(Abs(sin(x)))", r"\ln\left|\sin x\right|"),
     ("cos(x)/(1+2*sin(x))", "log(Abs(1+2*sin(x)))/2", r"\dfrac{1}{2}\ln\left|1+2\sin x\right|"),
     ("1/(x*log(x))", "log(Abs(log(x)))", r"\ln\left|\ln x\right|")]),
 HI(r"Az $\displaystyle\int\bigl[f(x)\bigr]^n\cdot f'(x)\,dx=\dfrac{\bigl[f(x)\bigr]^{n+1}}{n+1}+C$ ($n\ne-1$) minta:",
    [("x*(x**2-1)**4", "(x**2-1)**5/10"), ("x/(x**2+1)**2", "-1/(2*(x**2+1))"),
     ("sin(x)**2*cos(x)", "sin(x)**3/3"), ("sin(x)/cos(x)**3", "1/(2*cos(x)**2)"),
     ("x**2/sqrt(1+x**3)", "Rational(2,3)*sqrt(1+x**3)")]),
 HI("Exponenciális függvény nemlineáris belső függvénnyel — keresd meg a belső függvény deriváltját!",
    [("x**2*exp(x**3)", "exp(x**3)/3"), ("exp(sin(x))*cos(x)", "exp(sin(x))"),
     ("exp(1/x)/x**2", "-exp(1/x)"), ("3**(x**2)*x", "3**(x**2)/(2*log(3))", r"\dfrac{3^{x^{2}}}{2\ln 3}")]),
 HI("Trigonometrikus függvény nemlineáris belső függvénnyel:",
    [("x*cos(x**2+1)", "sin(x**2+1)/2"), ("sin(sqrt(x))/sqrt(x)", "-2*cos(sqrt(x))"),
     ("x**2/cos(x**3)**2", "tan(x**3)/3"), ("sin(x)*cos(cos(x))", "-sin(cos(x))")]),
 HI(r"A belső függvény $\ln x$ — a szorzó $\dfrac1x$ éppen a deriváltja:",
    [("1/(x*(1+log(x)))", "log(Abs(1+log(x)))", r"\ln\left|1+\ln x\right|"),
     ("(2-log(x))/x", "2*log(x)-log(x)**2/2", r"2\ln x-\dfrac{(\ln x)^{2}}{2}"),
     ("sqrt(1+log(x))/x", "Rational(2,3)*(1+log(x))*sqrt(1+log(x))"),
     ("1/(x*log(x)**2)", "-1/log(x)")]),
]
if [Ex("exp(x)+x**2-2").subs(x, 0), sympy.simplify(Ex("sin(x)-cos(x)+1").subs(x, sympy.pi / 2)),
        sympy.simplify(Ex("tan(x)+cot(x)").subs(x, sympy.pi / 4)), Ex("-3/x+1/x**2+6").subs(x, 1)] != [-1, 2, 2, 4]:
    E.append("közép-1 pontok")
for f, F in (("exp(x)+2*x", "exp(x)+x**2-2"), ("sin(x)+cos(x)", "sin(x)-cos(x)+1"),
             ("1/cos(x)**2-1/sin(x)**2", "tan(x)+cot(x)"), ("3/x**2-2/x**3", "-3/x+1/x**2+6")):
    primitiv_e(f, F, nev="közép-1"); INTEGRANDUSOK.append(f); FUGGVENYEK.append(F)
for f2, F, pts in (("exp(x)", "exp(x)+x-2", ((0, -1), (2, sympy.E ** 2))), ("6*x-4", "x**3-2*x**2+x", ((1, 0), (2, 2)))):
    egyenlo("közép-2", diff(Ex(F), x, 2), Ex(f2))
    if any(sympy.simplify(Ex(F).subs(x, a) - b) != 0 for a, b in pts):
        E.append(("közép-2 pont", F))
    FUGGVENYEK.append(F)

N_I = [
 HI("Keresd meg a jó helyettesítést ($t=g(x)$), írd át az integrált $t$-re (ha kell, $x$-et is fejezd ki $t$-vel), "
    "integrálj, és helyettesíts vissza!",
    [("x**3*sqrt(x**4+1)", "(x**4+1)*sqrt(x**4+1)/6", None, r"$t=x^4+1$, $dt=4x^3\,dx$"),
     ("x*sqrt(x-1)", "Rational(2,5)*(x-1)**2*sqrt(x-1)+Rational(2,3)*(x-1)*sqrt(x-1)", None,
      r"$t=x-1$, $x=t+1$, $dx=dt$: $\displaystyle\int(t+1)\sqrt t\,dt$"),
     ("sin(2*x)/(1+sin(x)**2)", "log(1+sin(x)**2)", r"\ln\left(1+\sin^{2}x\right)",
      r"$t=1+\sin^2x$, $dt=2\sin x\cos x\,dx=\sin2x\,dx$"),
     ("x/sqrt(x+1)", "Rational(2,3)*(x+1)*sqrt(x+1)-2*sqrt(x+1)", None,
      r"$t=x+1$, $x=t-1$, $dx=dt$: $\displaystyle\int\dfrac{t-1}{\sqrt t}\,dt$")]),
 HI("Alakítsd át trigonometrikus azonossággal, és utána helyettesíts!",
    [("sin(x)**3", "-cos(x)+cos(x)**3/3"), ("cos(x)**5", "sin(x)-Rational(2,3)*sin(x)**3+sin(x)**5/5"),
     ("sin(2*x)/cos(x)**3", "2/cos(x)"),
     ("tan(x)**3", "tan(x)**2/2+log(Abs(cos(x)))", r"\dfrac{\operatorname{tg}^{2}x}{2}+\ln\left|\cos x\right|")]),
]
JOKER_I = (r"Az $e^{-x^2}$ függvény primitív függvénye nem írható fel elemi függvényekkel — az "
           r"$\displaystyle\int x\,e^{-x^2}\,dx$ viszont könnyen kiszámolható. Számítsd ki, és magyarázd meg a különbséget!",
           r"$\displaystyle\int x\,e^{-x^2}\,dx=-\dfrac{1}{2}e^{-x^2}+C$ ($t=-x^2$, $dt=-2x\,dx$). Itt az $x$ szorzó "
           r"(egy $-2$-es szorzótól eltekintve) éppen a belső függvény deriváltja, ezért működik a helyettesítés. Az "
           r"$\int e^{-x^2}dx$-ből ez a szorzó hiányzik; a primitív függvény létezik, de nem írható fel véges sok elemi "
           r"függvénnyel (lásd a "
           '<a href="tananyag-helyettesites.html#erdekesseg-gauss">Gauss-görbét</a>).', None)
primitiv_e("x*exp(-x**2)", "-exp(-x**2)/2", nev="joker I")


# ================================================================ ZSOLDOS-LISTA II. — HATÁROZOTT INTEGRÁL
# ---- ábrák
def _tv(v):                      # alap-2: törtvonal
    pts = [(0, 0), (1, 3), (2, 0), (3, -2), (4, -2), (5, 0), (6, 2)]
    for (a, fa), (b, fb) in zip(pts, pts[1:]):
        if a <= v <= b:
            return fa + (fb - fa) * (v - a) / (b - a)
    return 0.0 if v < 0 else 2 + 2 * (v - 6)


SVG_A2 = svgwrap(svg_fuggvenyek(
    [(_tv, SOT, "f", [(0, 6)])], xr=(-0.6, 6.8), yr=(-3.0, 3.8), w=360, h=230, jelmagyarazat=False,
    terulet=[(_tv, None, 0, 2, ZOLD, 0.3), (_tv, None, 2, 5, PIROS, 0.3), (_tv, None, 5, 6, ZOLD, 0.3)],
    pontok=[(1, 3, "", SOT), (3, -2, "", SOT), (4, -2, "", SOT), (6, 2, "", SOT)],
    leiras="Egy törtvonal-grafikon: a [0; 2]-n 3 magas háromszög az x tengely fölött, a [2; 5]-ön trapéz a tengely "
           "alatt (mélysége 2), az [5; 6]-on 2 magas háromszög a tengely fölött"))
_f8 = "x**2-2*x+3"
SVG_A8 = ABRA(_f8, 0, 3, leiras="Az f(x) = x² − 2x + 3 parabola; a [0; 3] fölötti terület árnyékolva")
_f12 = "x**2-4*x+3"
SVG_K12 = ABRA(_f12, 0, 4, leiras="Az f(x) = x² − 4x + 3 grafikonja a [0; 4]-en; a görbe és az x tengely közötti "
                                 "részek árnyékolva (az [1; 3]-on a tengely alatt)")
_fk1 = lambda v: 4 - v * v / 4
SVG_K1 = svgwrap(svg_fuggvenyek([(_fk1, SOT, "f", [(-0.3, 4.3)])], xr=(-0.6, 4.8), yr=(-0.8, 4.8), w=320, h=220,
                                jelmagyarazat=False, terulet=[(_fk1, None, 0, 4, KEK, 0.25)],
                                leiras="Az f(x) = 4 − x²/4 csökkenő a [0; 4]-en; a görbe alatti terület árnyékolva"))


def TER(f, lo, hi, g=None, **kw):
    """Terület-kulcs: érték + ábra."""
    T_, reszek = terulet(f, lo, hi, g)
    FUGGVENYEK.append(f)
    if g is not None:
        PAROK.append((f, g)); FUGGVENYEK.append(g)
    return T_, reszek, ABRA(f, lo, hi, g, **kw)


# alap-8, alap-9, alap-10
T8, _, _ = TER(_f8, 0, 3)
T9 = [TER("x**3+1", 0, 2), TER("4-x**2", -1, 1), TER("sqrt(x)+1", 1, 4)]
T10 = [TER("-x**2+2*x", 0, 2), TER("6-x-x**2", -3, 2)]
if [T8] + [a[0] for a in T9] + [a[0] for a in T10] != [9, 6, Q(22, 3), Q(23, 3), Q(4, 3), Q(125, 6)]:
    E.append(("alap 8–10", T8, [a[0] for a in T9], [a[0] for a in T10]))

A_II = [
 ("Tekintsük az $f(x)=x^2$ függvényt a $[0;\\,2]$ intervallumon. Oszd fel az intervallumot $n=4$ egyenlő részre, és számítsd "
  "ki az alsó ($s_4$) és a felső ($S_4$) közelítő összeget! Hasonlítsd össze a pontos értékkel: "
  "$\\displaystyle\\int_0^2x^2\\,dx=\\dfrac{8}{3}$.",
  None,
  r"$\Delta x=0{,}5$; $s_4=0{,}5\cdot(0+0{,}25+1+2{,}25)=1{,}75$, $S_4=0{,}5\cdot(0{,}25+1+2{,}25+4)=3{,}75$; "
  r"valóban $1{,}75\lt\dfrac{8}{3}\approx2{,}67\lt3{,}75$"),
 ("Az ábrán az $f$ függvény grafikonja: törtvonal (a rács egysége $1$). A háromszögek és a trapéz területéből "
  "határozd meg a következőket!" + SVG_A2,
  [r"$\displaystyle\int_0^2f(x)\,dx$", r"$\displaystyle\int_2^5f(x)\,dx$", r"$\displaystyle\int_0^6f(x)\,dx$",
   r"a grafikon és az $x$ tengely közötti teljes terület a $[0;\,6]$-on"],
  [r"$3$ (háromszög: $\dfrac{2\cdot3}{2}$)", r"$-4$ (trapéz: $\dfrac{3+1}{2}\cdot2=4$, a tengely alatt)",
   r"$3-4+1=0$", r"$T=3+4+1=8$ — nulla csak az előjeles integrál, a terület nem!"]),
 HA("Számítsd ki a Newton–Leibniz-formulával!",
    [("x**3", 1, 3, 20), ("1-2*x+3*x**2", -1, 3, 24), ("x**3-2*x**2+5", -1, 3, Q(64, 3)), ("x**2+2*x", -2, 1, 0)]),
 HA("Írd át a gyököket hatvánnyá, és számolj!",
    [("root(x**2,3)", 1, 8, Q(93, 5)), ("1/root(x**2,3)", 1, 8, 3), ("(x-1)/sqrt(x)", 1, 9, Q(40, 3)),
     ("sqrt(x)-1/sqrt(x)", 1, 4, Q(8, 3))]),
 HA("Exponenciális függvény és $\\dfrac1x$:",
    [("exp(x)", -1, 1, "E-1/E"), ("1/x", 1, "E**3", 3), ("2*exp(x)", 0, "log(5)", 8, "8"),
     ("1/x+x", 1, 2, "log(2)+Rational(3,2)", r"\ln 2+\dfrac{3}{2}")]),
 HA("Trigonometrikus függvények:",
    [("cos(x)-sin(x)", "-pi/2", "pi/2", 2), ("1/sin(x)**2", "pi/4", "pi/3", "1-sqrt(3)/3"),
     ("1/cos(x)**2-sin(x)", "-pi/4", "pi/4", 2),
     ("cos(x)+1/sin(x)**2", "pi/6", "pi/2", "Rational(1,2)+sqrt(3)", r"\dfrac{1}{2}+\sqrt{3}")]),
 ("Tudjuk, hogy $\\displaystyle\\int_0^3f(x)\\,dx=7$, $\\displaystyle\\int_0^5f(x)\\,dx=4$ és "
  "$\\displaystyle\\int_0^3g(x)\\,dx=-2$. Számítsd ki a határozott integrál tulajdonságaival!",
  [r"$\displaystyle\int_3^0f(x)\,dx$", r"$\displaystyle\int_3^5f(x)\,dx$",
   r"$\displaystyle\int_0^3\bigl(2f(x)-3g(x)\bigr)\,dx$", r"$\displaystyle\int_0^3\bigl(f(x)+1\bigr)\,dx$",
   r"$\displaystyle\int_5^5f(x)\,dx$"],
  [r"$-7$ (a határok felcserélésekor az integrál előjelet vált)", r"$4-7=-3$ (additivitás)", r"$2\cdot7-3\cdot(-2)=20$",
   r"$7+3=10$", r"$0$"], True),
 ("Az ábrán az $f(x)=x^2-2x+3$ függvény grafikonja látható. Számítsd ki az árnyékolt síkidom területét!" + SVG_A8,
  None, r"$T=\displaystyle\int_0^3\left(x^2-2x+3\right)dx=\left[\dfrac{x^3}{3}-x^2+3x\right]_0^3=9$"),
 ("Számítsd ki a függvény grafikonja és az $x$ tengely közötti síkidom területét az adott intervallumon! "
  "(Előbb győződj meg róla, hogy a függvény ott nem negatív.)",
  [r"$f(x)=x^3+1$, $[0;\,2]$", r"$f(x)=4-x^2$, $[-1;\,1]$", r"$f(x)=\sqrt x+1$, $[1;\,4]$"],
  [f"$T={Tsz(a[0])}$" + a[2] for a in T9]),
 ("Számítsd ki a parabola és az $x$ tengely által határolt síkidom területét! (A határokat a zérushelyek adják.)",
  [r"$y=-x^2+2x$", r"$y=6-x-x^2$"],
  [r"zérushelyek: $0$ és $2$; $T=\dfrac{4}{3}$" + T10[0][2],
   r"zérushelyek: $-3$ és $2$; $T=\dfrac{125}{6}$" + T10[1][2]]),
]
for f, a, b, e in (("x**2", 0, 2, Q(8, 3)), (_f8, 0, 3, 9), ("x**3+1", 0, 2, 6), ("4-x**2", -1, 1, Q(22, 3)),
                   ("sqrt(x)+1", 1, 4, Q(23, 3))):
    hatarozott(f, a, b, e, "alap-kézi")
INTEGRANDUSOK += [_f8, "x**3+1", "4-x**2", "sqrt(x)+1", "-x**2+2*x", "6-x-x**2"]
_s = [v * v for v in (0, 0.5, 1, 1.5, 2)]
if abs(0.5 * sum(_s[:4]) - 1.75) > 1e-12 or abs(0.5 * sum(_s[1:]) - 3.75) > 1e-12:
    E.append("alap-1 összegek")

# közép
T6 = [TER("x**2-6*x+5", 1, 5), TER("x**3-8", 0, 2)]
T7 = TER("x*(x-1)*(x-2)", 0, 2)
T8k = TER("x**2-3*x", 0, 4)
T9k = [TER("sin(2*x)", 0, "pi/2", xr=(-0.4, 2.0), yr=(-0.5, 1.5)),
       TER("3*cos(x)", "-pi/2", "pi/2", xr=(-2.2, 2.2), yr=(-0.8, 3.6)),
       TER("2*sin(x)", 0, "2*pi", xr=(-0.6, 6.9), yr=(-2.6, 2.6))]
T10k = [TER("exp(x/2)", 0, "2*log(3)", xr=(-0.8, 2.8)), TER("exp(x)+exp(-x)", "-log(2)", "log(2)", xr=(-1.4, 1.4))]
T11 = TER("x**2-x-2", 0, 3)
T12 = terulet(_f12, 0, 4)
if ([a[0] for a in T6], T7[0], T8k[0], [a[0] for a in T9k], [a[0] for a in T10k], T11[0], T12[0]) != \
        ([Q(32, 3), 12], Q(1, 2), Q(19, 3), [1, 6, 8], [4, 3], Q(31, 6), 4):
    E.append(("közép-területek", [a[0] for a in T6], T7[0], T8k[0], [a[0] for a in T9k], [a[0] for a in T10k],
              T11[0], T12[0]))
for f, a, b, e in (("x**2-3*x", 0, 4, Q(-8, 3)), ("2*sin(x)", 0, "2*pi", 0), ("x**2-x-2", 0, 3, Q(-3, 2)),
                   (_f12, 0, 1, Q(4, 3)), (_f12, 1, 3, Q(-4, 3)), (_f12, 3, 4, Q(4, 3)), (_f12, 0, 4, Q(4, 3)),
                   ("4-x**2/4", 0, 4, Q(32, 3))):
    hatarozott(f, a, b, e, "közép-kézi")
_k1 = [4 - v * v / 4 for v in range(5)]
if (sum(_k1[:4]), sum(_k1[1:])) != (12.5, 8.5):
    E.append("közép-1 összegek")
INTEGRANDUSOK += ["x**2-6*x+5", "x**3-8", "x*(x-1)*(x-2)", "x**2-3*x", "sin(2*x)", "3*cos(x)", "2*sin(x)",
                  "exp(x/2)", "exp(x)+exp(-x)", "x**2-x-2", _f12, "4-x**2/4"]


def _resz(reszek):
    return ", ".join(f"$\\displaystyle\\int_{{{TX(a)}}}^{{{TX(b)}}}f\\,dx={TX(r)}$" for a, b, r in reszek)


K_II = [
 ("Az ábrán az $f(x)=4-\\dfrac{x^2}{4}$ függvény grafikonja: a $[0;\\,4]$-en csökkenő. Oszd fel az intervallumot "
  "$n=4$ egyenlő részre! Melyik közelítő összeget adják a részintervallumok bal, illetve jobb végpontjához tartozó "
  "téglalapok? Miért? Számítsd ki mindkettőt, és becsüld meg a területet!" + SVG_K1,
  None,
  r"Csökkenő függvénynél a részintervallum bal végpontjában van a legnagyobb érték, ezért a bal végpontos téglalapok "
  r"adják a felső összeget: $\Delta x=1$, így $S_4=1\cdot(4+3{,}75+3+1{,}75)=12{,}5$; a jobb végpontosak az alsót: "
  r"$s_4=1\cdot(3{,}75+3+1{,}75+0)=8{,}5$. A kettő átlaga $10{,}5$ — a pontos érték $\dfrac{32}{3}\approx10{,}67$."),
 HA("Lineáris belső függvény a határozott integrálban:",
    [("(2*x-1)**3", 2, 3, 68), ("exp(3*x)", 0, 1, "(E**3-1)/3", r"\dfrac{e^{3}-1}{3}"),
     ("1/(11+5*x)**3", -2, -1, Q(7, 72)), ("cos(2*x)", 0, "pi/4", Q(1, 2))]),
 ("Helyettesítéssel számolj, és írd át a határokat is az új változóra!",
  [f"${INT('(2*x**3+1)**4*x**2', 0, 1)}$", f"${INT('x**2/(1+x**3)', 0, 1)}$",
   f"${INT('sin(x)*cos(x)**2', 0, 'pi/2')}$", f"${INT('x/sqrt(x**2+1)', 0, 'sqrt(3)')}$"],
  [r"$t=2x^3+1$, $1\le t\le3$: $\dfrac{1}{6}\displaystyle\int_1^3t^4\,dt=\dfrac{121}{15}$",
   r"$t=1+x^3$, $1\le t\le2$: $\dfrac{1}{3}\displaystyle\int_1^2\dfrac{dt}{t}=\dfrac{\ln 2}{3}$",
   r"$t=\cos x$, $dt=-\sin x\,dx$, a határok $1$ és $0$: $-\displaystyle\int_1^0t^2\,dt=\int_0^1t^2\,dt=\dfrac{1}{3}$",
   r"$t=x^2+1$, $1\le t\le4$: $\dfrac12\displaystyle\int_1^4\dfrac{dt}{\sqrt t}=1$"]),
 HA("Alakítsd át az integrandust, és számolj!",
    [("(3*x**2-4)/x", 1, 9, "120-8*log(3)", r"120-8\ln 3"), ("x**2+1/x**4", 1, 2, Q(21, 8)),
     ("(x+sqrt(x))/x", 1, 4, 5), ("(x+1)**2/x**2", 1, 2, "Rational(3,2)+2*log(2)", r"\dfrac{3}{2}+2\ln 2")]),
 HA("Trigonometrikus integrálok — ha kell, használj azonosságot!",
    [("1/cos(x)**2+1/sin(x)**2", "pi/6", "pi/3", "4*sqrt(3)/3", r"\dfrac{4\sqrt{3}}{3}"),
     ("cot(x)**2", "pi/4", "pi/2", "1-pi/4", r"1-\dfrac{\pi}{4}"),
     ("(sin(x)+cos(x))**2", 0, "pi/4", "pi/4+Rational(1,2)", r"\dfrac{\pi}{4}+\dfrac{1}{2}"),
     ("sin(2*x)*cos(x)", 0, "pi/2", Q(2, 3))]),
 ("A függvény grafikonja az adott intervallumon az $x$ tengely alatt halad. Számítsd ki a grafikon és az $x$ tengely "
  "közötti síkidom területét!",
  [r"$f(x)=x^2-6x+5$ a két zérushelye között", r"$f(x)=x^3-8$, $[0;\,2]$"],
  [r"zérushelyek: $1$ és $5$; $\displaystyle\int_1^5f\,dx=-\dfrac{32}{3}$, így $T=\dfrac{32}{3}$" + T6[0][2],
   r"$\displaystyle\int_0^2f\,dx=-12$, így $T=12$" + T6[1][2]]),
 ("Számítsd ki az $y=x(x-1)(x-2)$ görbe és az $x$ tengely által határolt síkidom területét!", None,
  r"zérushelyek: $0$, $1$, $2$; " + _resz(T7[1]) + r"; $T=\dfrac{1}{4}+\dfrac{1}{4}=\dfrac{1}{2}$" + T7[2]),
 ("Az $f(x)=x^2-3x$ függvény a $[0;\\,4]$ intervallumon előjelet vált. Számítsd ki a grafikon és az $x$ tengely "
  "közötti síkidom területét, és hasonlítsd össze a $\\displaystyle\\int_0^4f(x)\\,dx$ értékével!", None,
  r"zérushelyek: $0$ (végpont) és $3$ — bontani csak a $3$-nál kell; " + _resz(T8k[1]) + r"; $T=\dfrac{9}{2}+\dfrac{11}{6}=\dfrac{19}{3}$, míg "
  r"$\displaystyle\int_0^4f\,dx=-\dfrac{8}{3}$" + T8k[2]),
 ("Számítsd ki a grafikon és az $x$ tengely közötti síkidom területét!",
  [r"$y=\sin 2x$, $\left[0;\,\dfrac{\pi}{2}\right]$", r"$y=3\cos x$, $\left[-\dfrac{\pi}{2};\,\dfrac{\pi}{2}\right]$",
   r"$y=2\sin x$, $[0;\,2\pi]$ — mennyi itt a határozott integrál?"],
  [r"$T=1$" + T9k[0][2], r"$T=6$" + T9k[1][2],
   r"$T=4+4=8$, de $\displaystyle\int_0^{2\pi}2\sin x\,dx=0$" + T9k[2][2]]),
 ("Számítsd ki a grafikon és az $x$ tengely közötti síkidom területét!",
  [r"$y=e^{\frac{x}{2}}$, $[0;\,2\ln 3]$", r"$y=e^x+e^{-x}$, $[-\ln 2;\,\ln 2]$"],
  [r"$\left[2e^{\frac{x}{2}}\right]_0^{2\ln3}=2\cdot3-2=4$" + T10k[0][2],
   r"$\left[e^x-e^{-x}\right]_{-\ln2}^{\ln2}=\dfrac{3}{2}-\left(-\dfrac{3}{2}\right)=3$" + T10k[1][2]]),
 ("Véd Vilmos az $f(x)=x^2-x-2$ grafikonja és az $x$ tengely közötti területet a $[0;\\,3]$-on így számolta: "
  "$T=\\left|\\displaystyle\\int_0^3\\left(x^2-x-2\\right)dx\\right|=\\left|-\\dfrac{3}{2}\\right|=\\dfrac{3}{2}$. "
  "Mit rontott el? Mennyi a helyes terület?", None,
  r"Nem bontott a zérushelynél: $f$ a $2$-ben előjelet vált, és a tengely alatti és fölötti rész részben kioltja "
  r"egymást. "
  r"Helyesen: " + _resz(T11[1]) + r", így $T=\dfrac{10}{3}+\dfrac{11}{6}=\dfrac{31}{6}$" + T11[2]),
 ("Az ábrán az $f(x)=x^2-4x+3$ grafikonja és az $x$ tengely közötti síkidom árnyékolva látható. Melyik kifejezés "
  "adja a területét? Számítsd ki!" + SVG_K12,
  [r"$\displaystyle\int_0^4f(x)\,dx$", r"$\left|\displaystyle\int_0^4f(x)\,dx\right|$",
   r"$\displaystyle\int_0^1f\,dx-\int_1^3f\,dx+\int_3^4f\,dx$", r"$\displaystyle\int_0^1f\,dx+\int_1^3f\,dx+\int_3^4f\,dx$"],
  r"A c) kifejezés: $T=\dfrac{4}{3}-\left(-\dfrac{4}{3}\right)+\dfrac{4}{3}=4$. Az a), b) és d) mind "
  r"$\dfrac{4}{3}$-ot ad: bennük az $[1;\,3]$-on vett $-\dfrac{4}{3}$ hozzáadódik, vagyis a tengely alatti rész "
  r"területe levonódik ahelyett, hogy hozzáadódna."),
]

# nehéz
N1 = [TER("x+8", -4, 2, "x**2/2+2*x+4", feliratok=("y=x+8", r"y=\frac{x^2}{2}+2x+4")),
      TER("x+4", -4, 1, "x**2+4*x", feliratok=("y=x+4", "y=x^2+4x"))]
N2 = [TER("x**2+10", -3, 3, "2*x**2+1", feliratok=("y=x^2+10", "y=2x^2+1")),
      TER("-2*x**2+18", 0, Q(8, 3), "x**2-8*x+18", feliratok=("y=-2x^2+18", "y=x^2-8x+18"))]
N3 = [TER("(x-2)**2", 0, 2), TER("4-exp(x)", 0, "log(4)"), TER("sqrt(4-x)", 0, 4, szak=[(-0.5, 4)])]
N4 = [TER("x**2-5*x+4", 0, 1, xr=(-0.8, 4.8), yr=(-2.8, 4.8)), TER("1-x", 0, 3, "x**2-4*x+1", feliratok=("y=1-x", "y=x^2-4x+1")), TER("8-x**3", 0, 2)]
if ([a[0] for a in N1], [a[0] for a in N2], [a[0] for a in N3], [a[0] for a in N4]) != \
        ([18, Q(125, 6)], [36, Q(256, 27)], [Q(8, 3), sympy.simplify(8 * sympy.log(2) - 3), Q(16, 3)],
         [Q(11, 6), Q(9, 2), 12]):
    E.append(("nehéz-területek", [a[0] for a in N1], [a[0] for a in N2], [a[0] for a in N3], [a[0] for a in N4]))
for f, g, xs in (("x+8", "x**2/2+2*x+4", [-4, 2]), ("x+4", "x**2+4*x", [-4, 1]), ("x**2+10", "2*x**2+1", [-3, 3]),
                 ("-2*x**2+18", "x**2-8*x+18", [0, Q(8, 3)]), ("1-x", "x**2-4*x+1", [0, 3])):
    if sorted(solve(Ex(f) - Ex(g), x)) != xs:
        E.append(("metszéspont", f, g))

N_II = [
 ("Számítsd ki a parabola és az egyenes által határolt síkidom területét! (Először a metszéspontokat.)",
  [r"$y=\dfrac{1}{2}x^2+2x+4$ és $y=x+8$", r"$y=x^2+4x$ és $y=x+4$"],
  [r"metszéspontok: $x=-4$ és $x=2$; $T=\displaystyle\int_{-4}^{2}\left(-\dfrac{x^2}{2}-x+4\right)dx=18$" + N1[0][2],
   r"metszéspontok: $x=-4$ és $x=1$; $T=\displaystyle\int_{-4}^{1}\left(-x^2-3x+4\right)dx=\dfrac{125}{6}$" + N1[1][2]]),
 ("Számítsd ki a két parabola által határolt síkidom területét!",
  [r"$y=2x^2+1$ és $y=x^2+10$", r"$y=x^2-8x+18$ és $y=-2x^2+18$"],
  [r"metszéspontok: $x=-3$ és $x=3$; $T=\displaystyle\int_{-3}^{3}\left(9-x^2\right)dx=36$" + N2[0][2],
   r"metszéspontok: $x=0$ és $x=\dfrac{8}{3}$; $T=\displaystyle\int_0^{\frac83}\left(8x-3x^2\right)dx=\dfrac{256}{27}$"
   + N2[1][2]]),
 ("Számítsd ki a görbe és a két koordinátatengely által határolt síkidom területét (az első síknegyedben)!",
  [r"$y=(x-2)^2$", r"$y=4-e^x$", r"$y=\sqrt{4-x}$"],
  [r"zérushely: $2$; $T=\displaystyle\int_0^2(x-2)^2\,dx=\dfrac{8}{3}$" + N3[0][2],
   r"zérushely: $\ln 4$; $T=\left[4x-e^x\right]_0^{\ln4}=4\ln4-3=8\ln 2-3\approx2{,}55$" + N3[1][2],
   r"zérushely: $4$; $T=\left[-\dfrac{2}{3}(4-x)\sqrt{4-x}\right]_0^4=\dfrac{16}{3}$" + N3[2][2]]),
 ("Ábra nélkül: határozd meg a határokat, készíts vázlatot, és számítsd ki a síkidom területét!",
  [r"az $y=x^2-5x+4$ parabola és a két koordinátatengely", r"az $y=x^2-4x+1$ parabola és az $y=1-x$ egyenes",
   r"az $y=8-x^3$ görbe és a két koordinátatengely"],
  [r"zérushelyek: $1$ és $4$, de a két tengellyel csak a $[0;\,1]$-en zár közre síkidomot; "
   r"$T=\displaystyle\int_0^1\left(x^2-5x+4\right)dx=\dfrac{11}{6}$" + N4[0][2],
   r"metszéspontok: $x=0$ és $x=3$; a síkidom egy része az $x$ tengely alatt van, de a "
   r"$\int(\text{felső}-\text{alsó})$ képlet ettől függetlenül érvényes: "
   r"$T=\displaystyle\int_0^3\left(3x-x^2\right)dx=\dfrac{9}{2}$" + N4[1][2],
   r"zérushely: $2$; $T=\displaystyle\int_0^2\left(8-x^3\right)dx=12$" + N4[2][2]]),
]
JOKER_II = (r"Arkhimédész tétele: a parabolaszelet területe a beírt háromszög területének $\dfrac{4}{3}$-a, ha a "
            r"háromszög harmadik csúcsa ott van, ahol a parabola érintője párhuzamos a húrral. Ellenőrizd az $y=x^2$ "
            r"parabola és az $y=4$ egyenes esetén! (Itt a beírt háromszög csúcsai: a két metszéspont és a parabola "
            r"csúcsa.)",
            r"metszéspontok: $(-2;\,4)$ és $(2;\,4)$; a parabolaszelet: "
            r"$T=\displaystyle\int_{-2}^{2}\left(4-x^2\right)dx=\dfrac{32}{3}$; a háromszög: $t=\dfrac{4\cdot4}{2}=8$, "
            r"és valóban $\dfrac{4}{3}\cdot8=\dfrac{32}{3}$. Arkhimédész ezt integrál nélkül, a kimerítés módszerével "
            r"látta be, kb. Kr. e. 250-ben." + ABRA("4", -2, 2, "x**2", feliratok=("y=4", "y=x^2"),
                                                     xr=(-3.2, 3.2), yr=(-0.8, 5.2)), None)
if terulet("4", -2, 2, "x**2")[0] != Q(32, 3):
    E.append("joker II")
PAROK.append(("4", "x**2"))

# ================================================================ ÖNELLENŐRZÉS
# tiltott adatok (a felmérők) és a tananyag kidolgozott példái
E += TILT.ellenoriz(INTEGRANDUSOK + FUGGVENYEK, PAROK)
TANANYAG = ["x**2-1", "4*x**3-2*x", "6*x**2+2", "2*x+3", "6*x**2-4*x+5", "3*sin(x)+2*exp(x)", "2/x**3", "x**(-1/3)",
            "(x**2+3*x-2)/x", "(2*x-1)**2", "(1+sqrt(x))*sqrt(x)", "(x**3+1)/x", "(5*x+2)**4", "exp(3*x)",
            "cos(2*x-1)", "1/(3*x-4)", "sin(4*x)", "2*x/(x**2+4)", "x/(x**2-9)", "2*x*(x**2+1)**3", "sin(x)*cos(x)**3",
            "log(x)/x", "x**2*sqrt(x**3+1)", "exp(sqrt(x))/sqrt(x)", "tan(x)", "x**2/3+1", "x**2-4*x", "3*x**2-2*x",
            "1/sqrt(x)", "(2*x+1)**3", "2*x/(x**2+1)", "x**2/2+2", "8-2*x**2", "x**3/3-x", "x**4-x**2+3"]
_P = (0.37, 1.91, 2.63, 3.3)
xp = symbols("x", positive=True)


def _az(u, r_):
    try:
        a, b = Ex(u).subs(x, xp), sympify(r_, locals=dict(LD, x=xp))
        return all(abs(complex(a.subs(xp, v)) - complex(b.subs(xp, v))) < 1e-9 for v in _P)
    except Exception:
        return False


# a tananyag exp(3x)-e a [0;1]-es határozott integrálban (közép-2) szándékosan más feladat: csak a határozatlanra nézzük
_HATAROZOTT = {"exp(3*x)"}
for u in set(INTEGRANDUSOK + FUGGVENYEK) - _HATAROZOTT:
    for r_ in TANANYAG:
        if _az(u, r_):
            E.append(("tananyag-példa", u, r_))
for f, g in PAROK:
    if (_az(f, "x+2") and _az(g, "x**2")) or _az(f"({f})-({g})", "x+2-x**2"):
        E.append(("tananyag-pár", f, g))
assert not E, E
print("sympy önteszt: OK |", len(INTEGRANDUSOK), "integrandus,", len(PAROK), "görbepár")


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


if __name__ == "__main__":
    u1 = oldal(**T, fajl="feladatok-hatarozatlan-integral.html", cim="Zsoldos-lista I. — Határozatlan integrál",
               h1="Integrál — Zsoldos-lista I.: határozatlan integrál", itt="Zsoldos-lista I. — Határozatlan integrál",
               alcim="Primitív függvény, integráltáblázat, átalakítások, lineáris belső függvény, az $\\frac{f'}{f}$ és "
                     "az $f^n\\cdot f'$ minta, helyettesítés. A végeredmény minden feladatnál lenyitható — előbb "
                     "számolj, és ellenőrizz deriválással!",
               sections_html=lista(_prim(A_I), _prim(K_I), _prim(N_I), JOKER_I), ossz_nev="Csalópapírt",
               prev="tananyag-terulet.html", prevc="A Void kivágása — síkidomok területe",
               nxt="feladatok-hatarozott-integral.html", nxtc="Zsoldos-lista II. — Határozott integrál")
    u2 = oldal(**T, fajl="feladatok-hatarozott-integral.html", cim="Zsoldos-lista II. — Határozott integrál",
               h1="Integrál — Zsoldos-lista II.: határozott integrál és terület",
               itt="Zsoldos-lista II. — Határozott integrál",
               alcim="Közelítő összegek, Newton–Leibniz-formula, tulajdonságok, helyettesítés a határok átírásával, "
                     "területszámítás: görbe alatt, a tengely alatt, előjelváltáskor, két görbe között. A "
                     "területfeladatok végeredménye ábrával!",
               sections_html=lista(_prim(A_II), _prim(K_II), _prim(N_II), JOKER_II), ossz_nev="Csalópapírt",
               prev="feladatok-hatarozatlan-integral.html", prevc="Zsoldos-lista I. — Határozatlan integrál",
               nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
    print("✓", os.path.basename(u1), "| I.", len(A_I), len(K_I), len(N_I), "+ Joker")
    print("✓", os.path.basename(u2), "| II.", len(A_II), len(K_II), len(N_II), "+ Joker")
