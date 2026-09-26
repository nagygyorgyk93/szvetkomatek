# -*- coding: utf-8 -*-
"""4e/04 — A blokk: a primitiv fuggveny (A1), az integraltablazat (A2), a helyettesiteses integralas (A3).
Mentor: SZVETI (Nagol, Ved Vilmos kommental). Kuldetes: A Valosag Osszefoltozasa.
Specifikacio: projektek/4e/munkafajlok/narrativa_04-integral.md
Tiltott adatok: a 25/26-os es 26/27-es integral-felmerok (tiltott_4e_04.py) — lent ellenorizve."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek, svg_interaktiv
import tiltott_4e_04 as TILT

T = dict(tagozat="4e", mappa="04-integral", temakor="Integrál")
KUL = "A Valóság Összefoltozása"
FA = "feladatok-hatarozatlan-integral.html"
E403 = "../03-derivalt/"
KEK, ZOLD, PIROS, SOT, SZURKE = "#3b82f6", "#047857", "#ef4444", "#0f172a", "#64748b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FA}#nehez-{tol}">Zsoldos-lista I., nehéz {tol}–{ig}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table">{"<tr>" + th + "</tr>" if any(fejlec) else ""}{tr}</table></div>'


# ---------------------------------------------------------------- önteszt: minden primitív függvényt deriválunk
from sympy import symbols, diff, simplify, sympify, Rational as R, log, sqrt, exp, sin, cos, tan

E = []
x = symbols("x", positive=True)
S = lambda s: sympify(s, locals={"x": x, "R": R})


def prim(f, F, nev):
    """F valóban f primitív függvénye?"""
    if simplify(diff(S(F), x) - S(f)) != 0:
        E.append((nev, f, F))


# A1
for f, F in (("2*x", "x**2"), ("cos(x)", "sin(x)"), ("3*x**2", "x**3"), ("exp(x)", "exp(x)"), ("1/x", "log(x)"),
             ("x**2-1", "x**3/3-x"), ("4*x**3-2*x", "x**4-x**2+3"), ("6*x**2+2", "2*x**3+2*x"), ("x**2", "x**3/3"),
             ("2*x+3", "x**2+3*x")):
    prim(f, F, "A1")
if S("x**4-x**2+3").subs(x, 1) != 3 or abs(float(diff(S("x**3/3-x"), x).subs(x, R(3, 2))) - 1.25) > 1e-12:
    E.append("A1-pont")
# A2
for f, F in (("x**5", "x**6/6"), ("1/x", "log(x)"), ("2**x", "2**x/log(2)"), ("sin(x)", "-cos(x)"),
             ("1/cos(x)**2", "tan(x)"), ("1/sin(x)**2", "-1/tan(x)"), ("6*x**2-4*x+5", "2*x**3-2*x**2+5*x"),
             ("3*sin(x)+2*exp(x)", "-3*cos(x)+2*exp(x)"), ("sqrt(x)", "R(2,3)*x*sqrt(x)"), ("2/x**3", "-1/x**2"),
             ("x**R(-1,3)", "R(3,2)*x**R(2,3)"), ("(x**2+3*x-2)/x", "x**2/2+3*x-2*log(x)"),
             ("(2*x-1)**2", "R(4,3)*x**3-2*x**2+x"), ("(1+sqrt(x))*sqrt(x)", "R(2,3)*x*sqrt(x)+x**2/2"),
             ("1/x**2", "-1/x"), ("(x**3+1)/x", "x**3/3+log(x)")):
    prim(f, F, "A2")
# A3
for f, F in (("(5*x+2)**4", "(5*x+2)**5/25"), ("exp(3*x)", "exp(3*x)/3"), ("cos(2*x-1)", "sin(2*x-1)/2"),
             ("1/(3*x-4)", "log(3*x-4)/3"), ("sin(4*x)", "-cos(4*x)/4"), ("cos(3*x)", "sin(3*x)/3"),
             ("2*x/(x**2+4)", "log(x**2+4)"), ("x/(x**2-9)", "log(x**2-9)/2"), ("tan(x)", "-log(cos(x))"),
             ("2*x*(x**2+1)**3", "(x**2+1)**4/4"), ("sin(x)*cos(x)**3", "-cos(x)**4/4"), ("log(x)/x", "log(x)**2/2"),
             ("x**2*sqrt(x**3+1)", "R(2,9)*(x**3+1)*sqrt(x**3+1)"), ("exp(sqrt(x))/sqrt(x)", "2*exp(sqrt(x))"),
             ("(2*x-1)**2", "(2*x-1)**3/6")):
    prim(f, F, "A3")
# a (2x−1)² kétféle primitív függvénye csak állandóban tér el
if simplify(S("R(4,3)*x**3-2*x**2+x") - S("(2*x-1)**3/6")).free_symbols:
    E.append("A2-A3 állandó")

WEB = ["x**2-1", "4*x**3-2*x", "6*x**2+2", "2*x+3", "6*x**2-4*x+5", "3*sin(x)+2*exp(x)", "2/x**3", "x**R(-1,3)",
       "(x**2+3*x-2)/x", "(2*x-1)**2", "(1+sqrt(x))*sqrt(x)", "(x**3+1)/x", "(5*x+2)**4", "exp(3*x)", "cos(2*x-1)",
       "1/(3*x-4)", "sin(4*x)", "2*x/(x**2+4)", "x/(x**2-9)", "2*x*(x**2+1)**3", "sin(x)*cos(x)**3", "log(x)/x",
       "x**2*sqrt(x**3+1)", "exp(sqrt(x))/sqrt(x)"]
E += TILT.ellenoriz(WEB)
assert not E, E
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
W, H = 360, 250
SVG_A1_SEREG = svg_interaktiv(
    "sereg", [0, -1, 0, R(1, 3)], xr=(-2.6, 2.6), yr=(-4.2, 4.2), x0=1.5, csuszka=(-3.0, 3.0, 0.1, 0.0), w=W, h=H,
    felirat="Mozgasd a csúszkát! A fekete görbe az $F(x)+C=\\frac{x^3}{3}-x+C$, a szürkék a sereg néhány másik tagja. "
            "A görbe fel-le tolódik, de az $x_0=1{,}5$ helyen az érintő meredeksége mindig $f(1{,}5)=1{,}25$.",
    leiras="Interaktív ábra: az x³/3 − x + C függvénysereg; a csúszka a C-t állítja, az érintő az x = 1,5 helyen "
           "minden görbén ugyanolyan meredek")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>SZVETI:</b> Darabokban vagyok. A regisztereimből csak a <i>sebességprofilom</i> maradt meg — a deriváltam. '
         'Ha valaki visszaszámolná belőle, ki voltam, talán összeállnék. <b>Véd Vilmos:</b> Könnyű. 🌮 <i>Burek-matek:</i> '
         'a $2x$-ből $x^2$ lesz, pont. <b>Nagol:</b> És az $x^2+5$? Meg az $x^2-7$? Mind a $2x$-et adják. <b>SZVETI:</b> '
         'Szóval a $+C$ nélkül rossz alakban raktok össze. Mint Vilmost a kabátjával.'),
 ]),

 ("A deriválás megfordítása", [
   r'<p class="lead">Eddig egy függvényből kiszámoltuk a deriváltját. Most fordított a kérdés: <b>adott a derivált — '
   r'melyik függvényé?</b></p>',
   TABLA(["$f(x)$", "melyik függvény deriváltja?", "ellenőrzés"], [
       ["$2x$", "$x^2$", "$(x^2)'=2x$"],
       ["$\\cos x$", "$\\sin x$", "$(\\sin x)'=\\cos x$"],
       ["$3x^2$", "$x^3$", "$(x^3)'=3x^2$"],
       ["$e^x$", "$e^x$", "$(e^x)'=e^x$"],
       ["$\\dfrac1x$ $(x\\gt0)$", "$\\ln x$", "$(\\ln x)'=\\dfrac1x$"]]),
   doboz("definicio", "Primitív függvény",
         r'<p>Az $F$ függvény az $f$ függvény <b>primitív függvénye</b> az $I$ intervallumon, ha $F$ deriválható, és '
         r'$$F\'(x)=f(x)\quad\text{minden } x\in I\text{-re.}$$</p>'
         r'<p>A primitív függvényt a deriválttáblázat „visszafelé olvasásával” keressük '
         r'(<a href="' + E403 + r'tananyag-derivalasi-szabalyok.html#tetel-derivalt-tablazat">03: a deriválttáblázat</a>).</p>',
         hid="def-primitiv"),
 ]),

 ("Végtelen sok primitív függvény", [
   r'<p class="lead">Az $x^2$, az $x^2+5$ és az $x^2-7$ deriváltja egyaránt $2x$, mert az állandó deriváltja $0$. '
   r'Egy függvénynek tehát nem egy, hanem <b>végtelen sok</b> primitív függvénye van.</p>',
   doboz("tetel", "A primitív függvények serege",
         r'<p>Ha $F$ az $f$ primitív függvénye az $I$ intervallumon, akkor minden $C$ valós számra $F+C$ is az; és '
         r'az $f$ <b>minden</b> primitív függvénye $F+C$ alakú.</p>'
         r'<p>A primitív függvények grafikonjai egymás függőleges eltoltjai: ugyanazon az $x$ helyen mindegyik érintője '
         r'ugyanolyan meredek — a meredekség $f(x)$.</p>', hid="tetel-plusz-c"),
   SVG_A1_SEREG,
   kviz(r'Hány primitív függvénye van az $f(x)=2x+3$ függvénynek?',
        [r'végtelen sok: $x^2+3x+C$', r'pontosan egy: $x^2+3x$', r'kettő: $x^2+3x$ és $x^2+3x+1$',
         r'egy sem, mert $f$ nem páros'], 0,
        jo="✔ Bármely állandót hozzáadhatsz: a deriválásnál eltűnik. A primitív függvények egy seregét alkotják.",
        nem="✘ Az állandó deriváltja 0, ezért az x² + 3x + C mindegyike 2x + 3-at ad — végtelen sok primitív függvény van."),
 ]),

 ("A határozatlan integrál", [
   doboz("definicio", "A határozatlan integrál",
         r'<p>Az $f$ függvény primitív függvényeinek összességét az $f$ <b>határozatlan integráljának</b> nevezzük:'
         r'$$\int f(x)\,dx=F(x)+C,\qquad\text{ahol } F\'(x)=f(x).$$</p>'
         r'<p>A $\int$ az integráljel, $f(x)$ az <b>integrandus</b>, a $dx$ jelzi, hogy az $x$ változó szerint '
         r'integrálunk, a $C$ az <b>integrációs konstans</b>. Az integrálás a deriválás fordított művelete.</p>',
         hid="def-hatarozatlan-integral"),
   r'<p>Például $\int 2x\,dx=x^2+C$, $\int\cos x\,dx=\sin x+C$, $\int 3x^2\,dx=x^3+C$.</p>',
   doboz("pelda", "I.V.H. Akták — a seregből egyetlen tag",
         r'<p><b>Feladat.</b> Az $f(x)=4x^3-2x$ primitív függvényei közül melyiknek a grafikonja megy át a '
         r'$P(1;\,3)$ ponton?</p>'
         r'<p><b>1. A sereg:</b> $\int(4x^3-2x)\,dx=x^4-x^2+C$.</p>'
         r'<p><b>2. A pont:</b> $F(1)=1-1+C=C$, és ennek $3$-nak kell lennie, tehát $C=3$.</p>'
         r'<p><b>Eredmény:</b> $F(x)=x^4-x^2+3$. <i>Véd Vilmos széljegyzete: a pont kiválasztja a sereg egyetlen '
         r'tagját — ahogy engem is csak egyféleképpen lehet jól összerakni.</i></p>', hid="pelda-adott-pont"),
 ]),

 ("Ellenőrzés deriválással", [
   r'<p class="lead">Az integrálás eredményét <b>mindig</b> ellenőrizheted: deriváld! Ha visszakapod az integrandust, '
   r'jó a primitív függvény. Röviden: $\left(\int f(x)\,dx\right)\'=f(x)$.</p>',
   r'<p>Például $\int(6x^2+2)\,dx=2x^3+2x+C$, és valóban $(2x^3+2x+C)\'=6x^2+2$.</p>',
   doboz("csapda", "Véd Vilmos csapda",
         r'<p><b>1. Az elfelejtett $C$.</b> Az „$\int2x\,dx=x^2$” csak a sereg egyetlen tagja. A határozatlan '
         r'integrál mindig $+C$-vel teljes — a dolgozatban is.</p>'
         r'<p><b>2. Deriválás integrálás helyett.</b> $\int x^2\,dx\ne2x$! A $2x$ az $x^2$ <i>deriváltja</i>. '
         r'Helyesen $\int x^2\,dx=\frac{x^3}{3}+C$ — ellenőrzés: $\left(\frac{x^3}{3}\right)\'=x^2$.</p>'),
   kviz(r'Mennyi az $\int x^2\,dx$?',
        [r'$\dfrac{x^3}{3}+C$', r'$2x+C$', r'$x^3+C$', r'$\dfrac{x^3}{3}$'], 0,
        jo="✔ Ellenőrzés deriválással: (x³/3 + C)′ = x². És a +C sem maradt le.",
        nem="✘ Deriváld a választásod! A 2x az x² deriváltja (nem az integrálja), az x³ deriváltja 3x², az x³/3-ból "
            "pedig hiányzik a +C."),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A lépésszámláló és a navigáció a pillanatnyi sebességből számolja vissza a megtett utat: ez a primitív '
         r'függvény keresése. A $C$ itt a kiindulási pont — azt külön meg kell adni.</p>'),
   GY(FA + "#alap-1", "A 1–3", FA + "#kozep-1", "K 1–2"),
   brief('<b>SZVETI:</b> Egy darab a helyén. De ha minden deriválási sort így, egyenként fordítunk vissza, a '
         'regenerációm tovább tart, mint Vilmos reggeli öltözködése. <b>Nagol:</b> Akkor fordítsuk meg az egész '
         'Csalópapírt egyszerre.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
_TABLA_INT = TABLA(["$f(x)$", "$\\int f(x)\\,dx$", "megjegyzés"], [
    ["$k$ (állandó)", "$kx+C$", ""],
    ["$x^n$", "$\\dfrac{x^{n+1}}{n+1}+C$", "$n\\ne-1$ (a gyök és a tört is: $n\\in\\mathbb R$)"],
    ["$\\dfrac1x$", "$\\ln\\lvert x\\rvert+C$", "$x\\ne0$ — ez az $n=-1$ eset"],
    ["$e^x$", "$e^x+C$", ""],
    ["$a^x$", "$\\dfrac{a^x}{\\ln a}+C$", "$a\\gt0$, $a\\ne1$"],
    ["$\\sin x$", "$-\\cos x+C$", "vigyázz az előjelre!"],
    ["$\\cos x$", "$\\sin x+C$", ""],
    ["$\\dfrac{1}{\\cos^2x}$", "$\\operatorname{tg}x+C$", "$\\cos x\\ne0$"],
    ["$\\dfrac{1}{\\sin^2x}$", "$-\\operatorname{ctg}x+C$", "$\\sin x\\ne0$"]])

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>SZVETI</b> fejjel lefelé fordítja Nagol Csalópapírját. <b>SZVETI:</b> Minden sor visszafelé olvasva '
         'integrál. Egy kivétellel: az $x^{-1}$. Vilmos, a kabátod is kivétel volt? <b>Véd Vilmos:</b> Az limitált '
         'kiadás. <b>Nagol:</b> A táblázatot tanuljátok, ne a kabátot.'),
 ]),

 ("Az alapintegrálok táblázata", [
   doboz("tetel", "Az alapintegrálok táblázata", _TABLA_INT, hid="tetel-integraltablazat"),
   r'<p>Minden sor <b>deriválással igazolható</b>: például $\left(\frac{x^{n+1}}{n+1}\right)\'=x^n$, és '
   r'$\left(\frac{a^x}{\ln a}\right)\'=\frac{a^x\ln a}{\ln a}=a^x$. Így: $\int x^5\,dx=\frac{x^6}{6}+C$, '
   r'$\int 2^x\,dx=\frac{2^x}{\ln2}+C$.</p>',
   doboz("erdekesseg", "Miért $\\ln\\lvert x\\rvert$, és nem $\\ln x$?",
         r'<p>Az $\frac1x$ a negatív számokra is értelmezett, a $\ln x$ viszont nem. Negatív $x$-re '
         r'$\big(\ln(-x)\big)\'=\frac{-1}{-x}=\frac1x$, így a két ágat egy képlet fogja össze: $\ln\lvert x\rvert$.</p>'),
   kviz(r'Mennyi az $\int\dfrac1x\,dx$?',
        [r'$\ln\lvert x\rvert+C$', r'$\dfrac{x^0}{0}+C$', r'$-\dfrac{1}{x^2}+C$', r'$\dfrac{1}{x^2}+C$'], 0,
        jo="✔ Az n = −1 kivétel: a hatványszabály itt 0-val osztana. A ln|x| deriváltja pontosan 1/x.",
        nem="✘ A hatványszabály n = −1-re nem működik (0-val osztanál), a −1/x² pedig az 1/x deriváltja. "
            "Az 1/x primitív függvénye ln|x|."),
 ]),

 ("Konstansszoros és összeg", [
   doboz("tetel", "Az integrál tulajdonságai",
         r'<p>$$\int c\cdot f(x)\,dx=c\int f(x)\,dx,\qquad \int\big(f(x)\pm g(x)\big)\,dx=\int f(x)\,dx\pm\int g(x)\,dx.$$</p>'
         r'<p>Az állandó szorzó kiemelhető, az összeget tagonként integráljuk. A tagok $C$-it egyetlen $C$-be '
         r'vonjuk össze.</p>', hid="tetel-linearitas"),
   r'<p><b>Polinom:</b> $\int(6x^2-4x+5)\,dx=2x^3-2x^2+5x+C$.</p>'
   r'<p><b>Vegyes:</b> $\int(3\sin x+2e^x)\,dx=-3\cos x+2e^x+C$.</p>',
 ]),

 ("Gyök és tört hatványként", [
   r'<p class="lead">A gyököt és a törtet <b>hatványként</b> írjuk, és utána a táblázat első sora dolgozik: '
   r'$\sqrt[3]{x^2}=x^{\frac23}$, $\;\frac1{x^3}=x^{-3}$, $\;\frac1{\sqrt x}=x^{-\frac12}$.</p>',
   doboz("pelda", "I.V.H. Akták — gyök és tört",
         r'<ol><li>$\int\sqrt x\,dx=\int x^{\frac12}dx=\frac{x^{\frac32}}{\frac32}+C=\frac23x\sqrt x+C$;</li>'
         r'<li>$\int\frac{2}{x^3}dx=\int2x^{-3}dx=2\cdot\frac{x^{-2}}{-2}+C=-\frac1{x^2}+C$;</li>'
         r'<li>$\int\frac{1}{\sqrt[3]x}dx=\int x^{-\frac13}dx=\frac{x^{\frac23}}{\frac23}+C=\frac32\sqrt[3]{x^2}+C$.</li></ol>'
         r'<p>A törtkitevővel <b>osztani</b> kell: osztani $\frac32$-del = szorozni $\frac23$-dal.</p>',
         hid="pelda-gyok-hatvany"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„$\int\frac1{x^2}dx=\ln x^2$.” — Nem! A $\ln$ csak az $x^{-1}$-nek jár. Az $\frac1{x^2}=x^{-2}$, erre a '
         r'hatványszabály érvényes: $\int x^{-2}dx=\frac{x^{-1}}{-1}+C=-\frac1x+C$.</p>'),
 ]),

 ("Átalakítás integrálás előtt", [
   r'<p class="lead">Szorzatra és hányadosra <b>nincs</b> „integrálási szabály”. Előbb alakítsd át az integrandust '
   r'összeggé: a törtet tagonként osztva, a szorzatot beszorozva.</p>',
   doboz("pelda", "I.V.H. Akták — előbb átalakítunk",
         r'<ol><li>Tört szétbontása: $\int\frac{x^2+3x-2}{x}dx=\int\left(x+3-\frac2x\right)dx=\frac{x^2}2+3x-2\ln\lvert x\rvert+C$;</li>'
         r'<li>beszorzás: $\int(2x-1)^2dx=\int(4x^2-4x+1)\,dx=\frac43x^3-2x^2+x+C$ (az A3-ban rövidebben is megy);</li>'
         r'<li>szorzat: $\int(1+\sqrt x)\sqrt x\,dx=\int\left(x^{\frac12}+x\right)dx=\frac23x\sqrt x+\frac{x^2}2+C$.</li></ol>',
         hid="pelda-atalakitas"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„A szorzat integrálja az integrálok szorzata.” — Nem! $\int x\cdot x\,dx=\frac{x^3}3+C$, de '
         r'$\int x\,dx\cdot\int x\,dx=\frac{x^2}2\cdot\frac{x^2}2=\frac{x^4}4$. A hányadosra ugyanígy: előbb átalakítás.</p>'),
   kviz(r'Mennyi az $\int\dfrac{x^3+1}{x}\,dx$?',
        [r'$\dfrac{x^3}{3}+\ln\lvert x\rvert+C$', r'$\dfrac{x^4/4+x}{x^2/2}+C$', r'$\dfrac{x^4}{4}+x+C$',
         r'$3x^2+C$'], 0,
        jo="✔ Tagonként osztva x² + 1/x, ennek integrálja x³/3 + ln|x| + C.",
        nem="✘ A hányados nem integrálható a számláló és a nevező külön integrálásával. Előbb bontsd szét: "
            "(x³ + 1)/x = x² + 1/x, és ezt integráld tagonként."),
   GY(FA + "#alap-4", "A 4–8", FA + "#kozep-3", "K 3–5"),
   brief('<b>SZVETI:</b> A táblázattal a darabjaim felét visszaraktam. A másik fele belső függvényekbe bújt: '
         '$\\cos3x$, $(5x+2)^4$, $e^{3x}$. <b>Nagol:</b> Oda kell a trükk.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Egy ügyes cserével drasztikusan egyszerűsödik a rendszer — különben csak a karmait koptatja '
         'az ember. <b>Véd Vilmos:</b> Kinek vannak karmai? <b>Nagol:</b> A helyettesítés a láncszabály visszafelé. '
         'Ha a belső függvény deriváltja ott van az integrandusban, a feladat egyetlen sorrá zsugorodik.'),
 ]),

 ("Lineáris belső függvény", [
   r'<p class="lead">A láncszabály szerint $\big(F(ax+b)\big)\'=a\cdot f(ax+b)$. Ha tehát a belső függvény '
   r'<b>lineáris</b>, a külső primitív függvényét csak el kell osztani $a$-val.</p>',
   doboz("tetel", "Lineáris belső függvény",
         r'<p>Ha $F\'=f$ és $a\ne0$, akkor $$\int f(ax+b)\,dx=\frac1a\,F(ax+b)+C.$$</p>', hid="tetel-linearis-belso"),
   doboz("pelda", "I.V.H. Akták — egy sorban",
         r'<ol><li>$\int(5x+2)^4dx=\frac15\cdot\frac{(5x+2)^5}{5}+C=\frac{(5x+2)^5}{25}+C$;</li>'
         r'<li>$\int e^{3x}dx=\frac13e^{3x}+C$;</li>'
         r'<li>$\int\cos(2x-1)\,dx=\frac12\sin(2x-1)+C$;</li>'
         r'<li>$\int\frac{1}{3x-4}dx=\frac13\ln\lvert3x-4\rvert+C$.</li></ol>'
         r'<p>Ellenőrzés az elsőre: $\left(\frac{(5x+2)^5}{25}\right)\'=\frac{5(5x+2)^4\cdot5}{25}=(5x+2)^4$. ✓ '
         r'(Az A2-es $(2x-1)^2$ így: $\frac{(2x-1)^3}{6}+C$ — a két eredmény csak állandóban tér el.)</p>'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„$\int\cos3x\,dx=\sin3x+C$.” — Deriváld: $(\sin3x)\'=3\cos3x$, ez háromszor annyi. Az $\frac1a$ '
         r'szorzó nem maradhat le: $\int\cos3x\,dx=\frac13\sin3x+C$.</p>'),
   kviz(r'Mennyi az $\int\sin4x\,dx$?',
        [r'$-\dfrac14\cos4x+C$', r'$-\cos4x+C$', r'$\dfrac14\cos4x+C$', r'$-4\cos4x+C$'], 0,
        jo="✔ A sin primitív függvénye −cos, és a belső 4x miatt osztunk 4-gyel. Deriválva: (−¼cos 4x)′ = sin 4x.",
        nem="✘ Deriváld a választásod! Kell a −cos (a sin primitív függvénye), és a belső függvény 4-es szorzója "
            "miatt ¼ is."),
 ]),

 ("Az $\\frac{f'}{f}$ minta", [
   doboz("tetel", "Ha a számláló a nevező deriváltja",
         r'<p>$$\int\frac{f\'(x)}{f(x)}\,dx=\ln\lvert f(x)\rvert+C,$$ mert $\big(\ln\lvert f(x)\rvert\big)\'=\frac{f\'(x)}{f(x)}$ '
         r'(a láncszabály).</p>', hid="tetel-f-per-f"),
   doboz("pelda", "I.V.H. Akták — felismerés és igazítás",
         r'<ol><li>$\int\frac{2x}{x^2+4}dx=\ln(x^2+4)+C$ — a számláló pontosan a nevező deriváltja (és $x^2+4\gt0$);</li>'
         r'<li>$\int\frac{x}{x^2-9}dx=\frac12\int\frac{2x}{x^2-9}dx=\frac12\ln\lvert x^2-9\rvert+C$ — a hiányzó 2-es '
         r'szorzót mi tesszük be, és kívül kiegyenlítjük;</li>'
         r'<li>$\int\operatorname{tg}x\,dx=\int\frac{\sin x}{\cos x}dx=-\int\frac{-\sin x}{\cos x}dx=-\ln\lvert\cos x\rvert+C$.</li></ol>'),
   kviz(r'Melyik integrál számolható ki az $\frac{f\'}{f}$ mintával?',
        [r'$\int\dfrac{2x}{x^2+1}\,dx$', r'$\int\dfrac{1}{x^2+1}\,dx$', r'$\int\dfrac{x^2}{x+1}\,dx$',
         r'$\int\dfrac{x^2+1}{2x}\,dx$'], 0,
        jo="✔ A számláló (2x) pontosan a nevező (x² + 1) deriváltja: az eredmény ln(x² + 1) + C.",
        nem="✘ Nem minden tört vezet ln-re: a mintához a számlálónak a nevező deriváltjának (vagy annak számszorosának) "
            "kell lennie. Ez csak a 2x/(x² + 1)-nél teljesül."),
 ]),

 ("Az $f^n\\cdot f'$ minta", [
   doboz("tetel", "Hatvány szorozva a belső deriválttal",
         r'<p>Ha $n\ne-1$, akkor $$\int f(x)^n\cdot f\'(x)\,dx=\frac{f(x)^{n+1}}{n+1}+C.$$</p>', hid="tetel-f-hatvany"),
   doboz("pelda", "I.V.H. Akták — a belső függvény deriváltja ott van",
         r'<ol><li>$\int2x(x^2+1)^3dx=\frac{(x^2+1)^4}{4}+C$ — itt $f=x^2+1$, $f\'=2x$;</li>'
         r'<li>$\int\sin x\cos^3x\,dx=-\int\cos^3x\cdot(-\sin x)\,dx=-\frac{\cos^4x}{4}+C$;</li>'
         r'<li>$\int\frac{\ln x}{x}dx=\int\ln x\cdot\frac1x\,dx=\frac{(\ln x)^2}{2}+C$.</li></ol>'),
 ]),

 ("Az általános helyettesítés", [
   doboz("tetel", "A helyettesítés lépései",
         r'<ol><li>Válaszd a belső függvényt új változónak: $t=g(x)$.</li>'
         r'<li>Írd át a $dx$-et is: $dt=g\'(x)\,dx$.</li>'
         r'<li>Írd át az egész integrált $t$-re — $x$ nem maradhat benne.</li>'
         r'<li>Integrálj $t$ szerint.</li>'
         r'<li>Helyettesíts vissza: $t=g(x)$.</li></ol>'
         r'<p>Jó választás az, amelynek a deriváltja (számszorosa) szorzótényezőként szerepel az integrandusban.</p>',
         hid="tetel-helyettesites"),
   doboz("pelda", "I.V.H. Akták — Nagol két cseréje",
         r'<p><b>a)</b> $\int x^2\sqrt{x^3+1}\,dx$. Legyen $t=x^3+1$, ekkor $dt=3x^2dx$, azaz $x^2dx=\frac13dt$:'
         r'$$\int x^2\sqrt{x^3+1}\,dx=\frac13\int\sqrt t\,dt=\frac13\cdot\frac23t^{\frac32}+C=\frac29(x^3+1)\sqrt{x^3+1}+C.$$</p>'
         r'<p><b>b)</b> $\int\frac{e^{\sqrt x}}{\sqrt x}dx$. Legyen $t=\sqrt x$, ekkor $dt=\frac{dx}{2\sqrt x}$, azaz '
         r'$\frac{dx}{\sqrt x}=2\,dt$: $$\int\frac{e^{\sqrt x}}{\sqrt x}dx=2\int e^t\,dt=2e^{\sqrt x}+C.$$</p>',
         hid="pelda-helyettesites"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p><b>1.</b> A $dx$ átírása elmarad: „$\int x^2\sqrt t\,dx$” — keverék, ilyen integrál nincs. A $t$-re '
         r'áttérve a $dx$-et is $dt$-vel kell kifejezni.</p>'
         r'<p><b>2.</b> A visszahelyettesítés elmarad: az eredmény $x$ függvénye, nem $t$-é.</p>'),
   NEHEZ(1, 2, "helyettesítés, amikor a belső függvényt magadnak kell megtalálnod"),
   doboz("erdekesseg", "Ahol a matematika megáll",
         r'<p>A deriválás mindig sikerül: minden elemi függvény deriváltja elemi. Az integrálásnál nem így van. Az '
         r'$\int e^{-x^2}dx$ primitív függvénye <b>létezik</b>, de semmilyen véges képlettel nem írható fel az elemi '
         r'függvényekből (J. Liouville bizonyította a 19. században). Pedig a $y=e^{-x^2}$ a statisztika híres '
         r'<b>Gauss-féle harang görbéje</b> — az alatta lévő területeket ezért táblázatból vagy számítógéppel kapjuk.</p>',
         hid="erdekesseg-gauss"),
   GY(FA + "#alap-9", "A 9–12", FA + "#kozep-6", "K 6–10"),
   brief('<b>SZVETI:</b> A határozatlan integrál egy egész sereget ad vissza, nem engem. <b>Nagol:</b> Mert nincs '
         'megadva, hol kezdődsz és hol végződsz. Ha egy $[a;\\,b]$ intervallumba zárnak — és az I.V.H. éppen ezt teszi —, '
         'a sereg helyett egyetlen szám marad: a határozott integrál.', outro=True),
 ]),
]


# ---------------------------------------------------------------- oldalak
def _prim(szakaszok):
    """A nyers stringekben a \\' (KaTeX-ben ékezet!) helyett sima vessző-prím: f\\'(x) → f'(x)."""
    return [(h2.replace("\\'", "'"), [b.replace("\\'", "'") for b in blokkok]) for h2, blokkok in szakaszok]


A1, A2, A3 = (_prim(z) for z in (A1, A2, A3))
lapok = [
 lap(**T, fajl="tananyag-primitiv-fuggveny.html",
     cim="Visszafelé — a primitív függvény",
     alcim="A deriválás megfordítása, a primitív függvények serege és a +C, a határozatlan integrál jelölése, "
           "ellenőrzés deriválással.",
     chip=KUL + " · 1/6", szakaszok=A1,
     elozo=("index.html", "Integrál — témakör"),
     kovetkezo=("tananyag-integraltablazat.html", "Az integráltáblázat")),
 lap(**T, fajl="tananyag-integraltablazat.html",
     cim="Csalópapír visszafelé — az integráltáblázat",
     alcim="Az alapintegrálok táblázata, a konstansszoros és az összeg integrálja, gyök és tört hatványként, "
           "átalakítás integrálás előtt.",
     chip=KUL + " · 2/6", szakaszok=A2,
     elozo=("tananyag-primitiv-fuggveny.html", "A primitív függvény"),
     kovetkezo=("tananyag-helyettesites.html", "Helyettesítéses integrálás")),
 lap(**T, fajl="tananyag-helyettesites.html",
     cim="Nagol trükkje — helyettesítéses integrálás",
     alcim="Lineáris belső függvény, az f′/f és az fⁿ·f′ minta, az általános helyettesítés lépései — és egy "
           "integrál, amely nem számolható ki.",
     chip=KUL + " · 3/6", szakaszok=A3,
     elozo=("tananyag-integraltablazat.html", "Az integráltáblázat"),
     kovetkezo=("tananyag-hatarozott-integral.html", "A határozott integrál")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
