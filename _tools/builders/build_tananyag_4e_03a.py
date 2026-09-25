# -*- coding: utf-8 -*-
"""4e/03 — A es B blokk: a derivalt fogalma (A1), a derivalasi szabalyok (A2), az erinto es a valtozasi sebesseg (A3),
az osszetett fuggveny (B1), a masodik derivalt (B2). Mentor: Ved Vilmos & Nagol. Kuldetes: A Pillanatnyi Kaosz.
Specifikacio: projektek/4e/munkafajlok/narrativa_03-derivalt.md
Tiltott adatok: a 26/27-es 2. es 3. dolgozat kifejezesei (build_felmero_4e_03.py) — lent ellenorizve."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek, svg_interaktiv

T = dict(tagozat="4e", mappa="03-derivalt", temakor="A függvény deriváltja")
KUL = "A Pillanatnyi Káosz"
FD = "feladatok-derivalas.html"
E402 = "../02-fuggvenyek/"
E3E = "../../3e/05-analitikus-geometria/"
KEK, BORO, ZOLD, PIROS, LILA, SOT, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#7c3aed", "#0f172a", "#64748b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table"><tr>{th}</tr>{tr}</table></div>'


# ---------------------------------------------------------------- önteszt
from sympy import (symbols, diff, simplify, sympify, sin, cos, tan, exp, log, sqrt, Rational as R, expand, solve,
                   limit, oo, cbrt)
E = []
x, t = symbols("x t", real=True)
S = lambda s: sympify(s, locals={"x": x, "t": t})


def _egyezik(a, b):
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        return (isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)) and len(a) == len(b)
                and all(_egyezik(p, q) for p, q in zip(a, b)))
    return simplify(S(str(a)) - S(str(b))) == 0


def chk(nev, kapott, vart):
    if not _egyezik(kapott, vart):
        E.append((nev, kapott, vart))


def D(s, n=1, v=None):
    return diff(S(s), v or x, n)


# A1
chk("A1-tabla", [((1 + h) ** 2 - 1) / h for h in (1, R(1, 2), R(1, 10), R(1, 100))], [3, R(5, 2), R(21, 10), R(201, 100)])
chk("A1-atlag", [(S("t**2").subs(t, 3) - 1) / 2, (S("t**2").subs(t, 2) - 1) / 1], [4, 3])
chk("A1-x2-3", limit(((3 + t) ** 2 - 9) / t, t, 0), 6)
chk("A1-graf", [D("x**3/3-x").subs(x, v) for v in (-1, 0, 2)], [0, -1, 3])
# A2
chk("A2-pol", D("4*x**3-5*x**2+7*x-2"), "12*x**2-10*x+7")
chk("A2-hatv", [D("x**(R(2,3))".replace("R(2,3)", "2/3")), D("3/x**2"), D("x*sqrt(x)")],
    ["2/(3*x**(1/3))", "-6/x**3", "3*sqrt(x)/2"])
chk("A2-sz-a", D("(x**2+1)*(3*x-2)"), "9*x**2-4*x+3")
chk("A2-sz-b", D("x**2*sin(x)"), "2*x*sin(x)+x**2*cos(x)")
chk("A2-sz-c", D("(x-1)*exp(x)"), "x*exp(x)")
chk("A2-sz-d", D("x**2*log(x)"), "2*x*log(x)+x")
chk("A2-kviz2", D("x**3*cos(x)"), "3*x**2*cos(x)-x**3*sin(x)")
chk("A2-h-a", D("(2*x-1)/(x+3)"), "7/(x+3)**2")
chk("A2-h-b", D("(x**2+1)/(x-2)"), "(x**2-4*x-1)/(x-2)**2")
chk("A2-h-tg", D("sin(x)/cos(x)"), "1/cos(x)**2")
chk("A2-kviz3", D("1/(x**2+1)"), "-2*x/(x**2+1)**2")
chk("A2-helyet", [D("x**3-4*x+1").subs(x, v) for v in (2, 0, -1)], [8, -4, -1])
# A3
f3 = S("x**2-4*x+5")
chk("A3-erinto", [f3.subs(x, 3), D("x**2-4*x+5").subs(x, 3)], [2, 2])
chk("A3-kviz1", expand(D("x**3").subs(x, 1) * (x - 1) + 1), "3*x-2")
chk("A3-parh", solve(D("x**3-3*x**2") - 9, x), [-1, 3])
chk("A3-parh-p", [S("x**3-3*x**2").subs(x, v) for v in (3, -1)], [0, -4])
chk("A3-parh-e", [expand(9 * (x - 3) + 0), expand(9 * (x + 1) - 4)], ["9*x-27", "9*x+5"])
chk("A3-vizsz", [solve(D("x**3-3*x**2"), x), [S("x**3-3*x**2").subs(x, v) for v in (0, 2)]], [[0, 2], [0, -4]])
chk("A3-kviz2", solve(D("x**2-6*x+5"), x), [3])
chk("A3-seb", [D("2*t**2+3*t", v=t).subs(t, 2), S("2*t**2+3*t").subs(t, 2) / 2], [11, 7])
chk("A3-tea", D("80-4*t+t**2/20", v=t).subs(t, 10), -3)
# B1
chk("B1-lanc", D("(2*x+5)**3"), "6*(2*x+5)**2")
chk("B1-kviz", D("(4*x-1)**5"), "20*(4*x-1)**4")
chk("B1-min", [D("sqrt(x**2+4)"), D("cos(3*x)"), D("exp(2*x)"), D("log(x**2+1)"), D("sin(x)**2"), D("sin(x**2)")],
    ["x/sqrt(x**2+4)", "-3*sin(3*x)", "2*exp(2*x)", "2*x/(x**2+1)", "2*sin(x)*cos(x)", "2*x*cos(x**2)"])
chk("B1-tg3", D("tan(x)**3"), "3*tan(x)**2/cos(x)**2")
chk("B1-vegyes", D("x*exp(-2*x)"), "(1-2*x)*exp(-2*x)")
# B2
chk("B2-pol", [D("x**4-2*x**3+5*x"), D("x**4-2*x**3+5*x", 2)], ["4*x**3-6*x**2+5", "12*x**2-12*x"])
chk("B2-mas", [D("sin(x)", 2), D("1/x", 2), D("exp(3*x)", 2), D("x/(x+1)"), D("x/(x+1)", 2)],
    ["-sin(x)", "2/x**3", "9*exp(3*x)", "1/(x+1)**2", "-2/(x+1)**3"])
chk("B2-kviz1", D("x**3+2*x", 2), "6*x")
chk("B2-x4", [D("x**4", n) for n in (1, 2, 3, 4, 5)], ["4*x**3", "12*x**2", "24*x", 24, 0])
chk("B2-mozg", [D("-5*t**2+20*t", v=t), D("-5*t**2+20*t", 2, t), solve(D("-5*t**2+20*t", v=t), t),
                S("-5*t**2+20*t").subs(t, 2)], ["-10*t+20", -10, [2], 20])

# tiltott adatok: a 26/27-es dolgozatok (2d, 3d) kifejezései nem lehetnek tananyag-példák
TILTOTT = ["5*x**4-2*x**3+7*x-3", "-4*cos(x)", "5*log(x)", "(x**2-3*x)*cos(x)", "(2*x+3)/(x**2+1)",
           "3*x**5+4*x**3-6*x+1", "5*sin(x)", "2*exp(x)", "(x**2+4*x)*sin(x)", "(3*x-1)/(x**2+2)",
           "2*x**4-5*x**2+3*x", "7*cos(x)", "3*tan(x)", "(x**2+1)*exp(x)", "(2*x+1)/(x**2+3)",
           "x**3-2*x**2+3", "x**3+3*x**2-2", "x**3-3*x+1", "2*x**5-4*x**3+6*x-7", "x**6-3*x**4+5*x-1",
           "4*x**5-2*x**3+x-3", "x**3-3*x**2-9*x+5", "-x**3+3*x**2+9*x-2", "x**3+3*x**2-9*x-4",
           "(x**2-3*x)/(x+1)", "(x**2-7*x+10)/(x-1)", "(x**2-3*x)/(x-4)"]
PELDAK = ["x**3/3-x", "4*x**3-5*x**2+7*x-2", "(x**2+1)*(3*x-2)", "x**2*sin(x)", "(x-1)*exp(x)", "x**2*log(x)",
          "x**3*cos(x)", "(2*x-1)/(x+3)", "(x**2+1)/(x-2)", "1/(x**2+1)", "x**3-4*x+1", "x**2-4*x+5", "x**3",
          "x**3-3*x**2", "x**2-6*x+5", "(2*x+5)**3", "(4*x-1)**5", "sqrt(x**2+4)", "x*exp(-2*x)",
          "x**4-2*x**3+5*x", "x**3+2*x", "x/(x+1)"]
_PONT = (0.37, 1.91, 2.63, 3.3)


def _azonos(u, r_):
    try:
        return all(abs(complex(S(u).subs(x, v)) - complex(S(r_).subs(x, v))) < 1e-9 for v in _PONT)
    except (TypeError, ZeroDivisionError):
        return False


for p in PELDAK:
    for r_ in TILTOTT:
        if _azonos(p, r_):
            E.append(("tiltott", p, r_))
assert not E, E
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
W, H = 360, 250
F_A1 = lambda v: v ** 3 / 3 - v
SVG_A1_GRAF = svg_fuggvenyek(
    [(F_A1, KEK, "f", [(-2.35, 2.35)]),
     (lambda v: 2 / 3, ZOLD, "érintő, f′(−1) = 0", [(-1.9, -0.1)]),
     (lambda v: -v, BORO, "érintő, f′(0) = −1", [(-0.8, 0.8)]),
     (lambda v: 3 * (v - 2) + 2 / 3, PIROS, "érintő, f′(2) = 3", [(1.55, 2.3)])],
    xr=(-2.6, 2.8), yr=(-2.2, 2.6), w=W, h=H,
    pontok=[(-1, 2 / 3, "A", SOT, -4, -9), (0, 0, "B", SOT, 6, -6), (2, 2 / 3, "C", SOT, -16, -6)],
    leiras="Az f(x) = x³/3 − x grafikonja három érintővel: az A(−1; 2/3) pontban vízszintes, a B(0; 0) pontban "
           "−1 meredekségű, a C(2; 2/3) pontban 3 meredekségű érintő")
SVG_A1_SZELO = svg_interaktiv(
    "szelo", [0, 0, 1], xr=(-1.2, 3.4), yr=(-1.0, 9.6), x0=1, csuszka=(-1.5, 2.0, 0.01, 1.5), w=W, h=H,
    felirat="Mozgasd a csúszkát! A kék egyenes a $P(1;\\,1)$ és a $Q$ ponton átmenő <b>szelő</b>, a zöld szaggatott "
            "az <b>érintő</b>. Ahogy $\\Delta x\\to0$, a $Q$ a $P$-hez csúszik, és a szelő meredeksége $2$-höz tart.",
    leiras="Interaktív ábra: az y = x² parabola, a rögzített P(1; 1) pont, a csúszkával mozgatható Q pont és a "
           "rajtuk átmenő szelő; halványan az érintő")
SVG_A2_SINCOS = svg_fuggvenyek(
    [(math.sin, KEK, "y = sin x", [(-0.4, 6.6)]), (math.cos, BORO, "y = cos x", [(-0.4, 6.6)])],
    xr=(-0.6, 6.8), yr=(-1.6, 1.9), w=W, h=210,
    pontok=[(math.pi / 2, 1, "csúcs", KEK, -14, -8), (math.pi / 2, 0, "", BORO), (math.pi, 0, "", KEK),
            (math.pi, -1, "", BORO)],
    leiras="A szinusz- és a koszinuszgörbe: ahol a szinusz a csúcson van (x = π/2), ott a koszinusz értéke 0; "
           "ahol a szinusz a legmeredekebben csökken (x = π), ott a koszinusz −1")
SVG_A3 = svg_fuggvenyek(
    [(lambda v: v * v - 4 * v + 5, KEK, "f(x) = x² − 4x + 5", [(-0.2, 4.6)]),
     (lambda v: 2 * v - 4, ZOLD, "érintő: y = 2x − 4", [(1.2, 5.0)]),
     (lambda v: -v / 2 + 3.5, LILA, "normális: y = −x/2 + 7/2", [(0.2, 5.4)], "szaggatott")],
    xr=(-0.6, 5.6), yr=(-0.8, 6.2), w=W, h=H,
    pontok=[(3, 2, "T(3; 2)", SOT, 8, 14)],
    leiras="Az f(x) = x² − 4x + 5 parabola, a T(3; 2) pontbeli érintője (y = 2x − 4) és normálisa (y = −x/2 + 7/2)")
SVG_B1 = ('<svg viewBox="0 0 400 96" width="400" height="96" role="img" aria-label="Az összetett függvény mint két '
          'egymás után kapcsolt gép: x a belső g gépbe megy, abból u lesz, u a külső f gépbe megy, abból y lesz">'
          '<defs><marker id="nyilb" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="7" markerHeight="7" '
          'orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker></defs>'
          '<g font-family="inherit" font-size="15" fill="#0f172a" text-anchor="middle">'
          '<text x="22" y="53" font-style="italic">x</text>'
          '<line x1="36" y1="48" x2="92" y2="48" stroke="#0f172a" stroke-width="1.6" marker-end="url(#nyilb)"/>'
          '<rect x="96" y="22" width="92" height="52" rx="9" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>'
          '<text x="142" y="45">belső</text><text x="142" y="64" font-style="italic">g</text>'
          '<line x1="190" y1="48" x2="236" y2="48" stroke="#0f172a" stroke-width="1.6" marker-end="url(#nyilb)"/>'
          '<text x="213" y="40" font-style="italic">u</text>'
          '<rect x="240" y="22" width="92" height="52" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>'
          '<text x="286" y="45">külső</text><text x="286" y="64" font-style="italic">f</text>'
          '<line x1="334" y1="48" x2="372" y2="48" stroke="#0f172a" stroke-width="1.6" marker-end="url(#nyilb)"/>'
          '<text x="386" y="53" font-style="italic">y</text></g></svg>')
SVG_B2 = svg_fuggvenyek(
    [(lambda v: v * v / 2 - 0.5, KEK, "y = x²/2 − 1/2 (f″ > 0)", [(-2.4, 2.4)]),
     (lambda v: -v * v / 2 + 3, PIROS, "y = −x²/2 + 3 (f″ < 0)", [(-2.4, 2.4)])],
    xr=(-2.6, 2.6), yr=(-1.2, 3.8), w=W, h=H,
    leiras="Két parabola: a felfelé nyíló (második deriváltja pozitív) és a lefelé nyíló (második deriváltja negatív)")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Az I.V.H. traffipaxa egyetlen villanással lemérte a sebességemet a kismotoron. '
         '🌮 <i>Burek-matek:</i> két óra alatt 60 kilométert mentem, vagyis végig 30-cal, tehát ártatlan vagyok. '
         '<b>Nagol:</b> Ez az <b>átlag</b>. A traffipax a <b>pillanatot</b> méri — és egyetlen pillanat alatt nem '
         'teszel meg utat, tehát osztani sincs mit mivel. Ezt a „pillanatnyi sebességet” találta ki Newton a '
         'mozgáshoz és Leibniz a görbék érintőjéhez — ugyanazzal az eszközzel: a határértékkel. Üdv a '
         '<b>Pillanatnyi Káoszban</b>.'),
 ]),

 ("Átlagsebesség és növekmény", [
   r'<p class="lead">Véd Vilmos motorja $t$ másodperc alatt $s(t)=t^2$ métert tesz meg. Az első és a harmadik '
   r'másodperc között $s(3)-s(1)=9-1=8$ métert halad $2$ másodperc alatt, az <b>átlagsebessége</b> tehát '
   r'$\dfrac{8}{2}=4\ \tfrac{\text{m}}{\text{s}}$. Az $[1;\,2]$ szakaszon $\dfrac{4-1}{1}=3\ \tfrac{\text{m}}{\text{s}}$. '
   r'Minél rövidebb a szakasz, annál közelebb vagyunk ahhoz, amit a traffipax mér.</p>',
   doboz("definicio", "Növekmény és differenciahányados",
         r'<p>Ha az $x_0$ helyről $\Delta x$-szel továbblépünk, a függvény értéke '
         r'$\Delta y=f(x_0+\Delta x)-f(x_0)$-lal változik. $\Delta x$ a független változó <b>növekménye</b>, '
         r'$\Delta y$ a függvény <b>növekménye</b>, a hányadosuk pedig a <b>differenciahányados</b>:</p>'
         r'$$\frac{\Delta y}{\Delta x}=\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.$$'
         r'<p>Geometriailag ez a $P\big(x_0;\,f(x_0)\big)$ és a $Q\big(x_0+\Delta x;\,f(x_0+\Delta x)\big)$ pontot '
         r'összekötő <b>szelő meredeksége</b>, fizikailag az <b>átlagos változási sebesség</b>.</p>',
         hid="def-differenciahanyados"),
   r'<p>Az $f(x)=x^2$ függvénynél az $x_0=1$ helyen $\Delta y=(1+\Delta x)^2-1=2\Delta x+\Delta x^2$, így '
   r'$\dfrac{\Delta y}{\Delta x}=2+\Delta x$. Egyre kisebb lépésekkel:</p>',
   TABLA(["$\\Delta x$", "$1$", "$0{,}5$", "$0{,}1$", "$0{,}01$"],
         [["$\\dfrac{\\Delta y}{\\Delta x}$", "$3$", "$2{,}5$", "$2{,}1$", "$2{,}01$"]]),
   kviz(r'Mit ad meg az $f$ függvény $\dfrac{\Delta y}{\Delta x}$ differenciahányadosa az $x_0$ helyen, '
        r'$\Delta x\ne0$ lépéssel?',
        [r'a $P\big(x_0;f(x_0)\big)$ és a $Q\big(x_0+\Delta x;f(x_0+\Delta x)\big)$ ponton átmenő szelő meredekségét',
         r'az $x_0$ pontbeli érintő meredekségét',
         r'a $Q$ pont második koordinátáját',
         r'a függvény értékét a $\Delta x$ helyen'], 0,
        jo="✔ Két pont — egy szelő. Az érintőhöz még a Δx → 0 határátmenet kell.",
        nem="✘ A differenciahányados két pont között számol: ez a szelő meredeksége (átlagos változás). Az "
            "érintő meredeksége csak a Δx → 0 határértékben jön ki."),
 ]),

 ("A szelőtől az érintőig", [
   r'<p class="lead">Rögzítsük a $P(1;\,1)$ pontot az $y=x^2$ parabolán, és húzzuk egyre közelebb hozzá a $Q$ '
   r'pontot. A szelő a $P$ körül fordul, és egy határhelyzethez közelít: ez az <b>érintő</b>.</p>',
   SVG_A1_SZELO,
   r'<p>A táblázat és az ábra ugyanazt mondja: a $2+\Delta x$ meredekség $2$-höz tart, ha $\Delta x\to0$. Ez '
   r'a függvény határértéke, amit a 02. témakörben tanultunk (<a href="' + E402 +
   r'tananyag-fuggveny-hatarerteke.html#def-fv-hatarertek">a függvény határértéke</a>) — csak most a változó a '
   r'$\Delta x$, és a $0$-hoz tart.</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a pillanatnyi sebességet úgy számolja, hogy a differenciahányadosba rögtön '
         r'$\Delta x=0$-t ír: $\dfrac{(1+0)^2-1}{0}=\dfrac00$ — és kész is a káosz.</p>'
         r'<p><b>A $\Delta x=0$ nem behelyettesíthető</b>: két egybeeső pont nem határoz meg szelőt, a hányados '
         r'$\frac00$ alakú. Előbb egyszerűsítünk ($\frac{2\Delta x+\Delta x^2}{\Delta x}=2+\Delta x$), és csak '
         r'utána nézzük, mihez tart, ha $\Delta x\to0$. Pontosan úgy, mint a 0/0-s határértékeknél.</p>'),
 ]),

 ("A derivált definíciója", [
   doboz("definicio", "A derivált",
         r'<p>Az $f$ függvény <b>deriváltja</b> az $x_0$ helyen a differenciahányados határértéke, ha ez létezik '
         r'és véges:</p>'
         r'$$f\'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.$$'
         r'<p>Ilyenkor azt mondjuk, hogy $f$ az $x_0$ helyen <b>deriválható</b> (differenciálható). Jelölés: '
         r'$f\'(x_0)$, illetve $y\'$.</p>'
         r'<ul><li><b>Geometriai jelentés:</b> $f\'(x_0)$ az $x_0$ pontbeli <b>érintő meredeksége</b>.</li>'
         r'<li><b>Fizikai jelentés:</b> $f\'(x_0)$ a <b>pillanatnyi változási sebesség</b> (az út deriváltja a '
         r'sebesség).</li></ul>', hid="def-derivalt"),
   doboz("pelda", "I.V.H. Akták — az $x^2$ deriváltja az $x_0=3$ helyen",
         r'<p>$\Delta y=(3+\Delta x)^2-9=6\Delta x+\Delta x^2$, tehát '
         r'$\dfrac{\Delta y}{\Delta x}=6+\Delta x\ \xrightarrow{\ \Delta x\to0\ }\ 6$. Vagyis $f\'(3)=6$: a '
         r'parabola a $(3;\,9)$ pontban $6$ meredekséggel emelkedik.</p>'
         r'<p>Ugyanígy bármely $x_0$-ra $\dfrac{\Delta y}{\Delta x}=2x_0+\Delta x\to2x_0$, tehát az $x^2$ '
         r'deriváltja $2x$.</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „ezt minden függvényre végig kéne csinálni? — <b>Nem.</b> A '
         r'többit a következő leckében kész táblázatként kapod.”</p>', hid="pelda-x-negyzet"),
   doboz("erdekesseg", "Newton, Leibniz és a jelölések",
         r'<p>A differenciálszámítást egymástól függetlenül fedezte fel Isaac Newton (a mozgás felől) és '
         r'Gottfried Wilhelm Leibniz (az érintő felől) a 17. század végén; a „ki volt az első” vita évtizedekig '
         r'tartott. Leibniztől ered a $\frac{dy}{dx}$ jelölés, Newtontól a pont ($\dot s$ — a fizikában ma is '
         r'használják), a vessző ($f\'$) pedig Lagrange-tól.</p>'),
 ]),

 ("A derivált a grafikonról", [
   r'<p class="lead">Ha minden $x$-hez hozzárendeljük az ottani deriváltat, újabb függvényt kapunk: ez a '
   r'<b>deriváltfüggvény</b>. A grafikonról képletek nélkül is sokat elárul.</p>',
   doboz("definicio", "A deriváltfüggvény",
         r'<p>Ha $f$ egy intervallum minden pontjában deriválható, akkor az $x\mapsto f\'(x)$ hozzárendelés az '
         r'$f$ <b>deriváltfüggvénye</b> (röviden: deriváltja), jele $f\'$.</p>', hid="def-derivaltfuggveny"),
   abra(SVG_A1_GRAF, 'Az $f(x)=\\frac{x^3}{3}-x$ grafikonja: az érintő meredeksége a derivált értéke.'),
   r'<p>Az ábrán az <b>A</b> pontban az érintő vízszintes, tehát $f\'(-1)=0$; a <b>B</b> pontban a görbe '
   r'csökken, az érintő meredeksége $-1$; a <b>C</b> pontban meredeken emelkedik: ha az érintőn $1$-et lépünk '
   r'jobbra, $3$-at megyünk fel, tehát $f\'(2)=3$. <b>Ahol a függvény nő, ott a derivált pozitív; ahol csökken, '
   r'ott negatív; ahol „megfordul”, ott $0$.</b></p>',
   kviz(r'Egy függvény grafikonján az <b>A</b> pont a görbe csúcsa (ott a legnagyobb a függvényérték), a '
        r'<b>B</b> pontban pedig a görbe meredeken emelkedik. Hol nagyobb a derivált?',
        [r'a <b>B</b> pontban',
         r'az <b>A</b> pontban, mert ott a legnagyobb a függvényérték',
         r'egyenlők, hiszen mindkettő ugyanannak a függvénynek a pontja',
         r'a grafikonról nem lehet eldönteni'], 0,
        jo="✔ A derivált a meredekség, nem a magasság. A csúcson az érintő vízszintes (f′ = 0), B-ben pozitív.",
        nem="✘ A derivált azt méri, milyen meredek a görbe, nem azt, milyen magasan van. A csúcsban az "
            "érintő vízszintes, ott a derivált 0; a meredeken emelkedő B pontban pozitív."),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A sebességmérő a megtett út deriváltját mutatja. A járványgörbék „napi új esetek” oszlopai az '
         r'összes eset <b>változási ütemét</b> adják — vagyis egy derivált közelítését. Ugyanígy a népesség '
         r'növekedési üteme, a hőmérséklet változásának sebessége: mind derivált.</p>'),
   GY(FD + "#alap-1", "A 1–2", FD + "#kozep-1", "K 1"),
   brief('<b>Nagol:</b> Definícióból minden deriváltat ki lehetne számolni — de ez olyan, mintha minden '
         'szorzást összeadásokkal végeznél. <b>Véd Vilmos:</b> Van rövidítés? <b>Nagol:</b> Egy táblázat és '
         'négy szabály. A következő leckében megkapod.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
_TABLA = TABLA(["$f(x)$", "$f'(x)$", "megjegyzés"], [
    ["$c$ (állandó)", "$0$", "a vízszintes egyenes meredeksége $0$"],
    ["$x^n$", "$n\\,x^{n-1}$", "bármely valós $n$-re (ahol értelmezett)"],
    ["$\\sqrt x$", "$\\dfrac{1}{2\\sqrt x}$", "$x\\gt0$; ez az $n=\\frac12$ eset"],
    ["$\\dfrac1x$", "$-\\dfrac{1}{x^2}$", "$x\\ne0$; ez az $n=-1$ eset"],
    ["$\\sin x$", "$\\cos x$", ""],
    ["$\\cos x$", "$-\\sin x$", "vigyázz az előjelre!"],
    ["$\\operatorname{tg} x$", "$\\dfrac{1}{\\cos^2 x}$", "$\\cos x\\ne0$"],
    ["$\\operatorname{ctg} x$", "$-\\dfrac{1}{\\sin^2 x}$", "$\\sin x\\ne0$"],
    ["$e^x$", "$e^x$", "önmaga deriváltja"],
    ["$a^x$", "$a^x\\ln a$", "$a\\gt0$, $a\\ne1$"],
    ["$\\ln x$", "$\\dfrac1x$", "$x\\gt0$"],
    ["$\\log_a x$", "$\\dfrac{1}{x\\ln a}$", "$x\\gt0$"]])

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Minden deriváltat definícióból számolok. A harmadiknál elfogyott a papír, a '
         'negyediknél a türelmem. <b>Nagol</b> elővesz egy gyűrött lapot: Ez a <b>Csalópapír</b>. Newton óta '
         'mindenki ezt használja — a vizsgán is. Egy táblázat az alapfüggvényekről, és négy szabály arra, '
         'hogyan kell összerakni őket.'),
 ]),

 ("Az elemi függvények deriváltjai", [
   doboz("tetel", "A deriválttáblázat", _TABLA, hid="tetel-derivalt-tablazat"),
   r'<p>A táblázat sorait a definícióból lehet igazolni, mint az $x^2$-nél; a tanterv szerint ezt nem '
   r'gyakoroljuk, a táblázatot kész szabályként használjuk.</p>',
   abra(SVG_A2_SINCOS, 'Ahol a szinusz a csúcson van, ott a koszinusz $0$ — mert a csúcsban az érintő vízszintes.'),
   doboz("erdekesseg", "Miért éppen $e^x$?",
         r'<p>Az $e^x$ az egyetlen (nem nulla) függvény, amely <b>önmaga deriváltja</b>: minden pontban '
         r'pontosan olyan gyorsan nő, amekkora az értéke. Ezért jelenik meg mindenütt, ahol a növekedés üteme '
         r'a pillanatnyi mennyiséggel arányos — baktériumoknál, kamatos kamatnál, radioaktív bomlásnál.</p>'),
 ]),

 ("Konstansszoros, összeg, különbség", [
   doboz("tetel", "Konstansszoros és összeg deriváltja",
         r'<p>Ha $f$ és $g$ deriválható, $c$ állandó, akkor</p>'
         r'$$\big(c\cdot f(x)\big)\'=c\cdot f\'(x),\qquad \big(f(x)\pm g(x)\big)\'=f\'(x)\pm g\'(x).$$'
         r'<p>A polinomokat tehát tagonként deriváljuk.</p>', hid="tetel-osszeg"),
   r'<p><b>Polinom:</b> $\big(4x^3-5x^2+7x-2\big)\'=12x^2-10x+7$ — a konstans $-2$ eltűnik.</p>'
   r'<p><b>Gyök és tört hatványként:</b> ha a gyököt vagy a törtet hatványként írjuk, az $x^n$ sora '
   r'elvégzi a munkát:</p>'
   r'<ul><li>$\sqrt[3]{x^2}=x^{\frac23}$, így $\big(\sqrt[3]{x^2}\big)\'=\frac23x^{-\frac13}=\dfrac{2}{3\sqrt[3]x}$;</li>'
   r'<li>$\dfrac{3}{x^2}=3x^{-2}$, így $\left(\dfrac3{x^2}\right)\'=-6x^{-3}=-\dfrac{6}{x^3}$;</li>'
   r'<li>$x\sqrt x=x^{\frac32}$, így $\big(x\sqrt x\big)\'=\frac32x^{\frac12}=\frac32\sqrt x$.</li></ul>',
   kviz(r'Mennyi az $f(x)=x^2+5$ függvény deriváltja?',
        [r'$2x$', r'$2x+5$', r'$2x+1$', r'$x^2$'], 0,
        jo="✔ Az állandó deriváltja 0: a +5 csak feljebb tolja a parabolát, a meredekségén nem változtat.",
        nem="✘ Az állandó tag deriváltja 0 (a vízszintes egyenes nem emelkedik). Tehát (x² + 5)′ = 2x."),
 ]),

 ("A szorzat deriváltja", [
   doboz("tetel", "A szorzat deriválási szabálya",
         r'$$\big(f(x)\cdot g(x)\big)\'=f\'(x)\cdot g(x)+f(x)\cdot g\'(x)$$'
         r'<p>Szóban: az első deriváltja szorozva a másodikkal, <b>plusz</b> az első szorozva a második '
         r'deriváltjával.</p>', hid="tetel-szorzat"),
   doboz("pelda", "I.V.H. Akták — szorzatok",
         r'<ul><li>$\big((x^2+1)(3x-2)\big)\'=2x(3x-2)+(x^2+1)\cdot3=9x^2-4x+3$. (Ellenőrzés: beszorozva '
         r'$3x^3-2x^2+3x-2$, ennek deriváltja ugyanez.)</li>'
         r'<li>$\big(x^2\sin x\big)\'=2x\sin x+x^2\cos x$</li>'
         r'<li>$\big((x-1)e^x\big)\'=1\cdot e^x+(x-1)e^x=x\,e^x$</li>'
         r'<li>$\big(x^2\ln x\big)\'=2x\ln x+x^2\cdot\dfrac1x=2x\ln x+x$</li></ul>', hid="pelda-szorzat"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „a szorzat deriváltja a deriváltak szorzata”: $(f\cdot g)\'=f\'\cdot g\'$.</p>'
         r'<p><b>Nem az.</b> Már az $x\cdot x$ is lebuktatja: $f\'\cdot g\'=1\cdot1=1$, pedig '
         r'$(x\cdot x)\'=(x^2)\'=2x$. A szorzatszabály két tagja közül egyik sem maradhat el.</p>'),
   kviz(r'Mennyi az $x^3\cos x$ deriváltja?',
        [r'$3x^2\cos x-x^3\sin x$', r'$3x^2\cdot(-\sin x)$', r'$3x^2\cos x+x^3\sin x$', r'$-3x^2\sin x$'], 0,
        jo="✔ (x³)′·cos x + x³·(cos x)′ = 3x²cos x + x³·(−sin x).",
        nem="✘ Szorzatszabály: az első deriváltja × a második + az első × a második deriváltja, és "
            "(cos x)′ = −sin x. Így 3x²cos x − x³sin x."),
 ]),

 ("A hányados deriváltja", [
   doboz("tetel", "A hányados deriválási szabálya",
         r'$$\left(\frac{f(x)}{g(x)}\right)\'=\frac{f\'(x)\cdot g(x)-f(x)\cdot g\'(x)}{g^2(x)},\qquad g(x)\ne0.$$'
         r'<p>A számlálóban <b>a sorrend számít</b> (a kivonás miatt): előbb a számláló deriváltja szorozva a '
         r'nevezővel.</p>', hid="tetel-hanyados"),
   doboz("pelda", "I.V.H. Akták — hányadosok",
         r'<ul><li>$\left(\dfrac{2x-1}{x+3}\right)\'=\dfrac{2(x+3)-(2x-1)\cdot1}{(x+3)^2}=\dfrac{7}{(x+3)^2}$</li>'
         r'<li>$\left(\dfrac{x^2+1}{x-2}\right)\'=\dfrac{2x(x-2)-(x^2+1)\cdot1}{(x-2)^2}=\dfrac{x^2-4x-1}{(x-2)^2}$</li>'
         r'<li>A táblázat $\operatorname{tg}$-sora is így jön ki: $\left(\dfrac{\sin x}{\cos x}\right)\'='
         r'\dfrac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\dfrac{\cos^2x+\sin^2x}{\cos^2x}=\dfrac1{\cos^2x}$.</li></ul>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a nevezőt NEM bontom ki — $(x-2)^2$ így marad, a számlálót '
         r'viszont összevonom.”</p>', hid="pelda-hanyados"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a számlálóban megcseréli a sorrendet: $f\cdot g\'-f\'\cdot g$. Az eredmény pont az '
         r'ellenkező előjelű lesz — a monotonitásnál később ez fordított „nő–csökken” választ ad. Mondd '
         r'magadnak: <b>„számláló deriváltja × nevező — mínusz — számláló × nevező deriváltja”</b>.</p>'),
   kviz(r'Mennyi az $\dfrac{1}{x^2+1}$ deriváltja?',
        [r'$-\dfrac{2x}{(x^2+1)^2}$', r'$\dfrac{1}{2x}$', r'$-\dfrac{1}{(x^2+1)^2}$', r'$\dfrac{2x}{(x^2+1)^2}$'], 0,
        jo="✔ A számláló deriváltja 0, így marad a −1·2x a számlálóban és a (x² + 1)² a nevezőben.",
        nem="✘ Hányadosszabály: (0·(x² + 1) − 1·2x)/(x² + 1)² = −2x/(x² + 1)². A nevező négyzete nem maradhat el, "
            "és a számlálóban a mínusz sem."),
 ]),

 ("Helyettesítési érték: $f'(x_0)$", [
   r'<p class="lead">Az $f\'(x_0)$ kiszámítása két lépés: <b>előbb deriválunk, aztán helyettesítünk</b>.</p>'
   r'<p>Ha $f(x)=x^3-4x+1$, akkor $f\'(x)=3x^2-4$, így $f\'(2)=3\cdot4-4=8$, $f\'(0)=-4$ és $f\'(-1)=3-4=-1$.</p>'
   r'<p>Fordított sorrendben nem megy: $f(2)=1$ egy <b>szám</b>, és egy szám deriváltja $0$ — ami semmit sem '
   r'mond a görbe meredekségéről.</p>',
   GY(FD + "#alap-3", "A 3–9", FD + "#kozep-2", "K 2–5"),
   brief('<b>Nagol:</b> Most már bármely polinom meredekségét tudod bármely pontban. <b>Véd Vilmos:</b> És mire '
         'jó a meredekség, ha nem vagyok síugró? <b>Nagol:</b> Megmondja, merre repül tovább a dobócsillag, amit '
         'elengedsz. A következő leckében: az érintő egyenlete.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol</b> egy görbe pályán pörgeti a dobócsillagot: Merre repül tovább, ha elengedem? '
         '<b>Az érintő mentén.</b> <b>Véd Vilmos:</b> Én mindig merőlegesen dobok. <b>Nagol:</b> Az a '
         '<b>normális</b> — azt is felírjuk. A kulcs mindkettőhöz ugyanaz: a derivált az érintő meredeksége.'),
 ]),

 ("Az érintő egyenlete", [
   r'<p class="lead">Egy egyenest egy pontja és a meredeksége meghatároz: $y-y_1=m(x-x_1)$ (3e: '
   r'<a href="' + E3E + r'tananyag-egyenes-egyenlete.html#def-iranytenyezo">az egyenes egyenlete</a>). Az érintőnél '
   r'a pont az érintési pont, a meredekség a derivált.</p>',
   doboz("tetel", "Az érintő egyenlete",
         r'<p>Az $f$ függvény grafikonjának $T\big(x_0;\,y_0\big)$ pontjába húzott érintője, ahol $y_0=f(x_0)$:</p>'
         r'$$y-y_0=f\'(x_0)\,(x-x_0).$$'
         r'<p>A lépések: <b>1.</b> $y_0=f(x_0)$ · <b>2.</b> $f\'(x)$ · <b>3.</b> $m=f\'(x_0)$ · <b>4.</b> az '
         r'egyenlet, rendezve $y=mx+b$ alakra.</p>', hid="tetel-erinto"),
   doboz("pelda", "I.V.H. Akták — érintő a $T(3;\\,y)$ pontban",
         r'<p>Legyen $f(x)=x^2-4x+5$ és $x_0=3$.</p>'
         r'<ol><li>$y_0=f(3)=9-12+5=2$, tehát $T(3;\,2)$.</li>'
         r'<li>$f\'(x)=2x-4$.</li><li>$m=f\'(3)=2$.</li>'
         r'<li>$y-2=2(x-3)$, vagyis $y=2x-4$.</li></ol>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „ha a pont második koordinátája $y$ — azt nekem kell kiszámolni. '
         r'Az első lépés, nem az utolsó.”</p>', hid="pelda-erinto"),
   abra(SVG_A3, 'A parabola, az érintője és a normálisa a $T(3;\\,2)$ pontban.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos az $f\'(x_0)$ szám helyére a derivált <b>képletét</b> írja: $y-2=(2x-4)(x-3)$. Ez '
         r'másodfokú — nem egyenes, tehát nem is érintő.</p>'
         r'<p><b>A meredekség egyetlen szám</b>: a deriváltat előbb az $x_0$ helyen ki kell számolni. Gyakori '
         r'rokon hiba: $y_0$ helyére $f\'(x_0)$ kerül.</p>'),
   kviz(r'Mi az $f(x)=x^3$ grafikonjának $T(1;\,1)$ pontjába húzott érintő egyenlete?',
        [r'$y=3x-2$', r'$y=3x^2$', r'$y=3x$', r'$y=3x^2-2$'], 0,
        jo="✔ f′(x) = 3x², f′(1) = 3, így y − 1 = 3(x − 1), azaz y = 3x − 2.",
        nem="✘ Az érintő egyenes: a meredeksége a szám f′(1) = 3 (nem a 3x² képlet), és át kell mennie a (1; 1) "
            "ponton. y − 1 = 3(x − 1) → y = 3x − 2."),
 ]),

 ("A normális", [
   doboz("definicio", "A normális",
         r'<p>A grafikon $T(x_0;\,y_0)$ pontbeli <b>normálisa</b> az a $T$-n átmenő egyenes, amely az ottani '
         r'érintőre merőleges. Merőleges egyenesek meredekségének szorzata $-1$ '
         r'(<a href="' + E3E + r'tananyag-ket-egyenes.html#tetel-parhuzamos-meroleges">két egyenes helyzete</a>), '
         r'ezért ha $f\'(x_0)\ne0$:</p>'
         r'$$y-y_0=-\frac{1}{f\'(x_0)}\,(x-x_0).$$'
         r'<p>Ha $f\'(x_0)=0$, az érintő vízszintes ($y=y_0$), a normális függőleges ($x=x_0$).</p>',
         hid="def-normalis"),
   r'<p>Az előző példában $m=2$, így a normális meredeksége $-\frac12$: $y-2=-\frac12(x-3)$, vagyis '
   r'$y=-\frac12x+\frac72$ (az ábrán szaggatott vonal).</p>',
 ]),

 ("Adott meredekségű érintő", [
   r'<p class="lead">Néha fordítva kérdezünk: <b>hol</b> lesz az érintő meredeksége egy adott szám? Ehhez az '
   r'$f\'(x)=m$ <b>egyenletet</b> kell megoldani.</p>'
   r'<p><b>Párhuzamos egy egyenessel.</b> Hol párhuzamos az $f(x)=x^3-3x^2$ grafikonjának érintője az '
   r'$y=9x$ egyenessel? A párhuzamos egyenesek meredeksége egyenlő, tehát $f\'(x)=3x^2-6x=9$, azaz '
   r'$x^2-2x-3=0$, ahonnan $x=3$ vagy $x=-1$. Az érintési pontok $(3;\,0)$ és $(-1;\,-4)$, az érintők '
   r'$y=9x-27$ és $y=9x+5$.</p>'
   r'<p><b>Vízszintes érintő.</b> Ekkor $m=0$: $3x^2-6x=0$, tehát $x=0$ vagy $x=2$ — a $(0;\,0)$ és a '
   r'$(2;\,-4)$ pontban. Ezek a helyek a függvényvizsgálatban kulcsszerepet kapnak (szélsőérték-gyanús '
   r'helyek).</p>',
   kviz(r'Hol vízszintes az $f(x)=x^2-6x+5$ grafikonjának érintője?',
        [r'az $x=3$ helyen', r'az $x=1$ és az $x=5$ helyen', r'az $x=0$ helyen', r'sehol'], 0,
        jo="✔ Vízszintes érintő: f′(x) = 2x − 6 = 0, tehát x = 3 — a parabola csúcsában.",
        nem="✘ Az 1 és az 5 a zérushelyek (ahol f(x) = 0) — ott a görbe metszi az x tengelyt, de ferdén. A "
            "vízszintes érintőhöz a DERIVÁLT kell nullának lennie: 2x − 6 = 0, x = 3."),
 ]),

 ("A derivált mint változási sebesség", [
   r'<p class="lead">Ha egy mennyiség az időtől függ, a deriváltja megmondja, <b>milyen gyorsan változik</b> '
   r'abban a pillanatban. A mértékegysége: a mennyiség egysége osztva az idő egységével.</p>',
   doboz("pelda", "I.V.H. Akták — pillanatnyi sebesség és hűlési ütem",
         r'<p><b>Út–idő.</b> Egy ügynök $t$ másodperc alatt $s(t)=2t^2+3t$ métert fut. A sebessége '
         r'$v(t)=s\'(t)=4t+3$, így a $t=2$ s-kor $v(2)=11\ \tfrac{\text{m}}{\text{s}}$. (Az első két másodperc '
         r'<b>átlagsebessége</b> csak $\frac{s(2)}{2}=\frac{14}{2}=7\ \tfrac{\text{m}}{\text{s}}$.)</p>'
         r'<p><b>Hőmérséklet.</b> Egy bögre tea hőmérséklete $t$ perc után $T(t)=80-4t+0{,}05t^2$ °C '
         r'($0\le t\le40$). $T\'(t)=-4+0{,}1t$, így $T\'(10)=-3$: a $t=10$ perckor a tea percenként kb. 3 fokot '
         r'hűl. A negatív előjel a csökkenést jelzi.</p>', hid="pelda-sebesseg"),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Az autó sebességmérője és a „pillanatnyi fogyasztás” kijelzője egyaránt deriváltat mutat. '
         r'Grafikonról is le lehet olvasni: az idő–mennyiség görbe érintőjének meredeksége a változás üteme az '
         r'adott pillanatban.</p>'),
   GY(FD + "#alap-10", "A 10–13", FD + "#kozep-6", "K 6–8"),
   brief('<b>Véd Vilmos:</b> Eddig csak „tisztességes” függvényeket deriváltunk. Mi van, ha egy függvény belsejében '
         'egy másik függvény lakik, mint a $\\sqrt{x^2+4}$-ben? <b>Nagol:</b> Az egy matrjoska. Szétszedjük — '
         'rétegenként.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol</b> egy I.V.H.-matrjoskát tesz az asztalra: függvény a függvényben. <b>Véd Vilmos</b> '
         'szétszedi, deriválja a külső babát — a belsőt elfelejti. <b>Nagol:</b> Kívülről befelé. '
         '<b>Minden réteg egy szorzót ad.</b> Ez a láncszabály.'),
 ]),

 ("Az összetett függvény", [
   doboz("definicio", "Az összetett függvény",
         r'<p>Ha $u=g(x)$ és $y=f(u)$, akkor az $y=f\big(g(x)\big)$ függvény az $f$ és a $g$ <b>összetett</b> '
         r'függvénye. A $g$ a <b>belső</b>, az $f$ a <b>külső</b> függvény: először $g$ „dolgozik” az $x$-en, az '
         r'eredményt ($u$) kapja meg $f$.</p>', hid="def-osszetett"),
   abra(SVG_B1, 'Két gép egymás után: a belső $g$ kimenete a külső $f$ bemenete.'),
   TABLA(["függvény", "belső: $u=g(x)$", "külső: $y=f(u)$"], [
       ["$(2x+5)^3$", "$2x+5$", "$u^3$"],
       ["$\\sqrt{x^2+4}$", "$x^2+4$", "$\\sqrt u$"],
       ["$\\cos 3x$", "$3x$", "$\\cos u$"],
       ["$e^{2x}$", "$2x$", "$e^u$"],
       ["$\\ln(x^2+1)$", "$x^2+1$", "$\\ln u$"],
       ["$\\sin^2x=(\\sin x)^2$", "$\\sin x$", "$u^2$"]]),
   r'<p><b>Hogyan ismered fel a külsőt?</b> Az a külső függvény, amelyik műveletet <b>utoljára</b> végeznéd el, '
   r'ha számológéppel kiszámolnád az értékét. A $\sqrt{x^2+4}$-nél előbb $x^2+4$-et számolsz, a gyököt '
   r'utoljára vonod — a gyök a külső.</p>',
   kviz(r'Melyik a külső függvény az $y=\sqrt{x^2+1}$ összetett függvényben?',
        [r'a gyökvonás: $y=\sqrt u$', r'az $x^2+1$', r'a négyzetre emelés', r'nincs külső függvény'], 0,
        jo="✔ Utoljára a gyököt vonod, tehát az a külső; a belső az u = x² + 1.",
        nem="✘ Nézd meg, melyik műveletet végeznéd utoljára: először x² + 1, a végén a gyökvonás. A külső a √u, "
            "a belső az x² + 1."),
 ]),

 ("A láncszabály", [
   doboz("tetel", "Az összetett függvény deriváltja (láncszabály)",
         r'$$\Big(f\big(g(x)\big)\Big)\'=f\'\big(g(x)\big)\cdot g\'(x)$$'
         r'<p>Szóban: <b>a külső függvény deriváltja</b> (a belsőt változatlanul hagyva) <b>szorozva a belső '
         r'függvény deriváltjával</b>.</p>', hid="tetel-lancszabaly"),
   doboz("pelda", "I.V.H. Akták — rétegenként",
         r'<p>$y=(2x+5)^3$. Külső: $u^3$, deriváltja $3u^2$; belső: $2x+5$, deriváltja $2$. Tehát</p>'
         r'$$y\'=3(2x+5)^2\cdot2=6(2x+5)^2.$$'
         r'<p><i>Véd Vilmos széljegyzete:</i> „ellenőriztem: beszorozva $8x^3+60x^2+150x+125$, ennek deriváltja '
         r'$24x^2+120x+150=6(2x+5)^2$. Stimmel — de a láncszabály rövidebb.”</p>', hid="pelda-lanc"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a belső deriváltat elhagyja: $\big((2x+5)^3\big)\'=3(2x+5)^2$. Ez <b>hiányzik egy '
         r'szorzóval</b> — a belső $2x+5$ is változik, kétszer olyan gyorsan, mint $x$.</p>'
         r'<p>Rokon hiba: a $\sin^2x$ és a $\sin x^2$ összekeverése. $(\sin^2x)\'=2\sin x\cos x$ (a külső a '
         r'négyzetre emelés), de $(\sin x^2)\'=\cos x^2\cdot2x$ (a külső a szinusz).</p>'),
   kviz(r'Mennyi a $(4x-1)^5$ deriváltja?',
        [r'$20(4x-1)^4$', r'$5(4x-1)^4$', r'$5(4x)^4$', r'$20x(4x-1)^4$'], 0,
        jo="✔ Külső: 5u⁴, belső deriváltja 4 → 5(4x − 1)⁴ · 4 = 20(4x − 1)⁴.",
        nem="✘ A külső deriváltja 5(4x − 1)⁴, de ezt még szorozni kell a belső (4x − 1) deriváltjával, 4-gyel: "
            "20(4x − 1)⁴."),
 ]),

 ("Tipikus minták", [
   r'<p class="lead">A leggyakoribb összetett függvények deriváltja — mindegyik a láncszabályból jön:</p>',
   TABLA(["függvény", "deriváltja", "példa"], [
       ["$(ax+b)^n$", "$n\\,a\\,(ax+b)^{n-1}$", "$\\big((2x+5)^3\\big)'=6(2x+5)^2$"],
       ["$\\sqrt{g(x)}$", "$\\dfrac{g'(x)}{2\\sqrt{g(x)}}$", "$\\big(\\sqrt{x^2+4}\\big)'=\\dfrac{x}{\\sqrt{x^2+4}}$"],
       ["$\\sin(ax)$, $\\cos(ax)$", "$a\\cos(ax)$, $-a\\sin(ax)$", "$(\\cos3x)'=-3\\sin3x$"],
       ["$e^{kx}$", "$k\\,e^{kx}$", "$(e^{2x})'=2e^{2x}$"],
       ["$\\ln g(x)$", "$\\dfrac{g'(x)}{g(x)}$", "$\\big(\\ln(x^2+1)\\big)'=\\dfrac{2x}{x^2+1}$"],
       ["$g(x)^n$", "$n\\,g(x)^{n-1}g'(x)$", "$(\\operatorname{tg}^3x)'=3\\operatorname{tg}^2x\\cdot\\dfrac1{\\cos^2x}$"]]),
 ]),

 ("Összetett függvény szorzatban", [
   r'<p class="lead">A szabályok kombinálhatók: a szorzat- vagy hányadosszabályon belül egy tényező maga is '
   r'lehet összetett.</p>'
   r'<p>$y=x\cdot e^{-2x}$: a szorzatszabály szerint $y\'=1\cdot e^{-2x}+x\cdot\big(e^{-2x}\big)\'$, és a '
   r'láncszabállyal $\big(e^{-2x}\big)\'=-2e^{-2x}$. Összesen $y\'=e^{-2x}-2x\,e^{-2x}=(1-2x)\,e^{-2x}$.</p>',
   doboz("erdekesseg", "A láncszabály Leibniz-jelöléssel",
         r'<p>Ha $y=f(u)$ és $u=g(x)$, Leibniz jelölésével $\dfrac{dy}{dx}=\dfrac{dy}{du}\cdot\dfrac{du}{dx}$ — '
         r'mintha a $du$-val „egyszerűsítenénk”. Nem valódi tört, de jól mutatja: a változások üteme '
         r'rétegenként összeszorzódik.</p>'),
   GY(FD + "#alap-14", "A 14–16", FD + "#kozep-9", "K 9–11"),
   brief('<b>Véd Vilmos:</b> És ha a deriváltat még egyszer deriválom? <b>Nagol:</b> Akkor azt kapod, milyen '
         'gyorsan változik a változás. Padlógáz — a következő leckében.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos</b> padlógázzal indul: A sebességem nő — de <b>milyen gyorsan</b> nő? <b>Nagol:</b> Az a '
         '<b>gyorsulás</b>. A sebesség az út deriváltja, a gyorsulás a sebességé — vagyis az út <b>második '
         'deriváltja</b>. És ugyanez a második derivált mondja majd meg, merre hajlik egy görbe.'),
 ]),

 ("A második derivált", [
   doboz("definicio", "A második derivált",
         r'<p>Ha az $f\'$ deriváltfüggvény is deriválható, az ő deriváltja az $f$ <b>második deriváltja</b>: '
         r'$f\'\'(x)=\big(f\'(x)\big)\'$. Jelölés: $f\'\'$, $y\'\'$.</p>', hid="def-masodik-derivalt"),
   TABLA(["$f(x)$", "$f'(x)$", "$f''(x)$"], [
       ["$x^4-2x^3+5x$", "$4x^3-6x^2+5$", "$12x^2-12x$"],
       ["$\\sin x$", "$\\cos x$", "$-\\sin x$"],
       ["$\\dfrac1x$", "$-\\dfrac1{x^2}$", "$\\dfrac2{x^3}$"],
       ["$e^{3x}$", "$3e^{3x}$", "$9e^{3x}$"],
       ["$\\dfrac{x}{x+1}$", "$\\dfrac{1}{(x+1)^2}$", "$-\\dfrac{2}{(x+1)^3}$"]]),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos a második derivált helyett a derivált <b>négyzetét</b> számolja: az $x^3$-nál '
         r'$(3x^2)^2=9x^4$. Helyesen $f\'\'=(3x^2)\'=6x$ — <b>deriválni kell még egyszer</b>, nem négyzetre '
         r'emelni.</p>'
         r'<p>Törtnél a második lépésben is kell a hányados- vagy a láncszabály: '
         r'$\left(\frac{1}{(x+1)^2}\right)\'=\big((x+1)^{-2}\big)\'=-2(x+1)^{-3}$.</p>'),
   kviz(r'Mennyi az $f(x)=x^3+2x$ függvény második deriváltja?',
        [r'$6x$', r'$(3x^2+2)^2$', r'$3x^2+2$', r'$6x+2$'], 0,
        jo="✔ f′(x) = 3x² + 2, ezt még egyszer deriválva f″(x) = 6x.",
        nem="✘ A második derivált a derivált deriváltja (nem a négyzete): f′ = 3x² + 2, így f″ = 6x — a 2 "
            "konstans deriváltja 0."),
 ]),

 ("Magasabb rendű deriváltak", [
   r'<p class="lead">A deriválás folytatható: harmadik derivált $f\'\'\'$, negyedik $f^{(4)}$, és így tovább.</p>'
   r'<ul><li>$x^4\to4x^3\to12x^2\to24x\to24\to0$: egy $n$-edfokú polinom $(n+1)$-edik deriváltja mindig $0$.</li>'
   r'<li>$\sin x\to\cos x\to-\sin x\to-\cos x\to\sin x$: négy lépés után körbeér.</li></ul>',
 ]),

 ("Sebesség és gyorsulás", [
   doboz("pelda", "I.V.H. Akták — a feldobott labda",
         r'<p>Egy labda $t$ másodperc múlva $s(t)=-5t^2+20t$ méter magasan van.</p>'
         r'<ul><li>sebessége: $v(t)=s\'(t)=-10t+20$ ($\tfrac{\text{m}}{\text{s}}$);</li>'
         r'<li>gyorsulása: $a(t)=v\'(t)=s\'\'(t)=-10$ ($\tfrac{\text{m}}{\text{s}^2}$) — ez a nehézségi '
         r'gyorsulás (kerekítve), lefelé mutat;</li>'
         r'<li>a pálya csúcsán $v(t)=0$, azaz $t=2$ s, a magasság $s(2)=20$ m.</li></ul>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a csúcson a sebesség $0$ — a gyorsulás mégsem. Ha az is $0$ '
         r'lenne, a labda ott maradna lebegni.”</p>', hid="pelda-mozgas"),
   kviz(r'A feldobott labda a pálya legmagasabb pontján egy pillanatra megáll. Mekkora ott a gyorsulása '
        r'(a fenti példában)?',
        [r'$-10\ \tfrac{\text{m}}{\text{s}^2}$', r'$0$, mert a labda áll', r'$20\ \tfrac{\text{m}}{\text{s}^2}$',
         r'nem határozható meg'], 0,
        jo="✔ a(t) = s″(t) = −10 minden pillanatban — a csúcson is. A sebesség 0, a gyorsulás nem.",
        nem="✘ Az, hogy a sebesség pillanatnyilag 0, nem jelenti, hogy nem is változik. a(t) = s″(t) = −10 "
            "állandó: a csúcson is lefelé gyorsul a labda."),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A harmadik derivált (a gyorsulás változási üteme) a <b>rántás</b>. A hullámvasutak és a liftek '
         r'tervezői erre figyelnek: a hirtelen gyorsulásváltozást érezzük „rángatásnak”, nem magát a '
         r'gyorsulást.</p>'),
 ]),

 ("Mire jó még? — előretekintés", [
   r'<p class="lead">A második derivált előjele a görbe <b>hajlását</b> mutatja. A felfelé nyíló parabolánál '
   r'$f\'\'\gt0$, a lefelé nyílónál $f\'\'\lt0$. Ezt a függvényvizsgálatban (C2) használjuk majd a '
   r'konvexitás eldöntésére.</p>',
   abra(SVG_B2, 'Pozitív második derivált: felfelé nyíló ív; negatív: lefelé nyíló ív.'),
   GY(FD + "#alap-17", "A 17–18", FD + "#kozep-12", "K 12"),
   brief('<b>Nagol:</b> A derivált előjeléből kiolvasható, hol nő és hol csökken a függvény, a második '
         'deriváltéból pedig, merre hajlik. <b>Véd Vilmos:</b> Hegyek és völgyek! Imádom a szélsőértékeket. '
         '<b>Nagol:</b> Akkor kezdjük a függvényvizsgálatot.', outro=True),
 ]),
]

# ---------------------------------------------------------------- oldalak
def _prim(szakaszok):
    """A nyers stringekben a \\' (KaTeX-ben ékezet!) helyett sima vessző-prím: f\\'(x) → f'(x)."""
    return [(h2, [b.replace("\\'", "'") for b in blokkok]) for h2, blokkok in szakaszok]


A1, A2, A3, B1, B2 = (_prim(z) for z in (A1, A2, A3, B1, B2))
lapok = [
 lap(**T, fajl="tananyag-derivalt-fogalma.html",
     cim="A pillanat sebessége — a derivált fogalma",
     alcim="Növekmény, differenciahányados, a szelőtől az érintőig; a derivált mint az érintő meredeksége és "
           "mint pillanatnyi sebesség.",
     chip=KUL + " · 1/8", szakaszok=A1,
     elozo=("index.html", "A függvény deriváltja — témakör"),
     kovetkezo=("tananyag-derivalasi-szabalyok.html", "A deriválás szabályai")),
 lap(**T, fajl="tananyag-derivalasi-szabalyok.html",
     cim="A deriválás szabályai",
     alcim="A deriválttáblázat, a konstansszoros és az összeg, a szorzat és a hányados deriváltja, "
           "helyettesítési érték.",
     chip=KUL + " · 2/8", szakaszok=A2,
     elozo=("tananyag-derivalt-fogalma.html", "A derivált fogalma"),
     kovetkezo=("tananyag-erinto-es-valtozasi-sebesseg.html", "Az érintő és a változási sebesség")),
 lap(**T, fajl="tananyag-erinto-es-valtozasi-sebesseg.html",
     cim="Az érintő és a változás üteme",
     alcim="Az érintő és a normális egyenlete, adott meredekségű érintő, a derivált mint változási sebesség.",
     chip=KUL + " · 3/8", szakaszok=A3,
     elozo=("tananyag-derivalasi-szabalyok.html", "A deriválás szabályai"),
     kovetkezo=("tananyag-osszetett-fuggveny.html", "Az összetett függvény deriváltja")),
 lap(**T, fajl="tananyag-osszetett-fuggveny.html",
     cim="Függvény a függvényben — az összetett függvény deriváltja",
     alcim="Belső és külső függvény, a láncszabály, tipikus minták és kombinált esetek.",
     chip=KUL + " · 4/8", szakaszok=B1,
     elozo=("tananyag-erinto-es-valtozasi-sebesseg.html", "Az érintő és a változási sebesség"),
     kovetkezo=("tananyag-masodik-derivalt.html", "A második derivált")),
 lap(**T, fajl="tananyag-masodik-derivalt.html",
     cim="A derivált deriváltja — második és magasabb rendű derivált",
     alcim="A második derivált kiszámítása, magasabb rendű deriváltak, sebesség és gyorsulás.",
     chip=KUL + " · 5/8", szakaszok=B2,
     elozo=("tananyag-osszetett-fuggveny.html", "Az összetett függvény deriváltja"),
     kovetkezo=("tananyag-monotonitas-szelsoertek.html", "Monotonitás és szélsőérték")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
