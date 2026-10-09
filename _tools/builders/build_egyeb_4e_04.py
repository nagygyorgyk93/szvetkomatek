# -*- coding: utf-8 -*-
"""4e/04 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p), I.V.H. Kihallgato Terem (F6h) es a temakor-index (F5).
Kuldetes: A Valosag Osszefoltozasa. Mentor: SZVETI es Nagol (Ved Vilmos kommental).
A terepkuldetes es a hazi adatai ujak: sem a felmerokben (tiltott_4e_04), sem a tananyag peldaiban, sem a ket
Zsoldos-listaban nem szerepelnek — ezt a futaskor numerikus azonossag-vizsgalat igazolja.
A kulcs-segedeket (HI, HA, TER, TX) a build_fgy_4e_04 adja, igy a kulcsok formaja egyezik a listakeval."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, brief, GYOKER
from fgy_common import cards, oldal, w
import build_fgy_4e_04 as FG
import tiltott
TILT = tiltott.modul("tiltott_4e_04")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)
import sympy
from sympy import Rational as Q, symbols, diff, integrate, simplify, solve, sqrt, pi, E as EE

x, Ex = FG.x, FG.Ex
T = dict(tagozat="4e", mappa="04-integral", temakor="Integrál")
KUL = "A Valóság Összefoltozása"
A1, A2, A3 = "tananyag-primitiv-fuggveny.html", "tananyag-integraltablazat.html", "tananyag-helyettesites.html"
B1, B2, B3 = "tananyag-hatarozott-integral.html", "tananyag-newton-leibniz.html", "tananyag-terulet.html"
FI, FH = "feladatok-hatarozatlan-integral.html", "feladatok-hatarozott-integral.html"


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


def _prim(v):
    """A nyers stringekben a \\' (KaTeX-ben ékezet) → sima vessző-prím."""
    if isinstance(v, str):
        return v.replace("\\'", "'")
    if isinstance(v, (list, tuple)):
        return type(v)(_prim(u) for u in v)
    return v


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{c}</th>" for c in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    fej = f"<tr>{th}</tr>" if any(fejlec) else ""
    return f'<div class="tblwrap"><table class="tt-table">{fej}{tr}</table></div>'


# ==================================================================== F4 — Csalópapír
OSSZ = [
 ("🎯 Primitív függvény és határozatlan integrál", [
  r'<p><b>Primitív függvény</b> ' + h(A1, "def-primitiv") + (
                                                                   ": $F$ az $f$ primitív függvénye egy intervallumon, ha ott $F\\'(x)=f(x)$. Ha $F$ az, akkor $F+C$ is "
                                                                   'az — ugyanezen az intervallumon minden primitív függvény ilyen alakú '
                                                               ) + h(A1, "tetel-plusz-c") + r'.</p>'
  r'<p><b>Határozatlan integrál</b> ' + h(A1, "def-hatarozatlan-integral") + r': $\displaystyle\int f(x)\,dx=F(x)+C$ '
  r'— a primitív függvények serege; $f$ az <b>integrandus</b>, $C$ az <b>integrációs konstans</b>.</p>'
  r'<ul><li><b>Ellenőrzés:</b> az eredményt deriváld vissza — az integrandust kell kapnod.</li>'
  r'<li><b>Adott ponton átmenő</b> primitív függvény ' + h(A1, "pelda-adott-pont") + r': írd fel a sereget ($F(x)=G(x)+C$, ahol $G$ egy '
  r'primitív függvény), majd a pont koordinátáit behelyettesítve $C$-re egyenletet kapsz.</li>'
  r'<li>Ha $f\'\'$ ismert: kétszer integrálsz, két állandó lesz — két feltétel kell hozzájuk.</li></ul>',
 ]),

 ("📋 Az integráltáblázat", [
  TABLA(["$f(x)$", "$\\displaystyle\\int f(x)\\,dx$", "$f(x)$", "$\\displaystyle\\int f(x)\\,dx$"], [
      ["$x^n$ $(n\\ne-1)$", "$\\dfrac{x^{n+1}}{n+1}+C$", "$\\sin x$", "$-\\cos x+C$"],
      ["$\\dfrac1x$", "$\\ln\\lvert x\\rvert+C$", "$\\cos x$", "$\\sin x+C$"],
      ["$e^x$", "$e^x+C$", "$\\dfrac{1}{\\cos^2x}$", "$\\operatorname{tg}x+C$"],
      ["$a^x$", "$\\dfrac{a^x}{\\ln a}+C$", "$\\dfrac{1}{\\sin^2x}$", "$-\\operatorname{ctg}x+C$"],
      ["$k$ (állandó)", "$kx+C$", "$\\sqrt x$", "$\\dfrac23x\\sqrt x+C$"]]),
  (
      '<p class="le halvany">Feltételek: a hatványszabály tetszőleges valós kitevővel $x>0$-ra '
      'használható; más intervallumon akkor, ha a hatványok valósak és deriválhatók. A $\\dfrac1x$-nél '
      '$x\\ne0$; $a^x$-nél $a\\gt0$, $a\\ne1$; $\\dfrac{1}{\\cos^2x}$-nél $\\cos x\\ne0$; '
      '$\\dfrac{1}{\\sin^2x}$-nél $\\sin x\\ne0$; $\\sqrt x$-nél $x\\ge0$.</p>'
  ),
  r'<p><b>Szabályok</b> ' + h(A2, "tetel-linearitas") + r': $\int c\cdot f=c\int f$, $\;\int(f\pm g)=\int f\pm\int g$. '
  r'Szorzatra és hányadosra <b>nincs</b> ilyen szabály — előbb alakíts át (beszorzás, tagokra bontás) '
  + h(A2, "pelda-atalakitas") + r'. A gyököt és a törtet írd <b>hatványként</b>: $\sqrt[3]{x^2}=x^{\frac23}$, '
  r'$\dfrac{2}{x^5}=2x^{-5}$ ' + h(A2, "pelda-gyok-hatvany") + r'. A feltételek magyarázatával: ' + h(A2, "tetel-integraltablazat", "A2")
  + r'.</p>',
 ]),

 ("🔧 Helyettesítés — a négy minta", [
  TABLA(["minta", "szabály", "példa"], [
      ["lineáris belső függvény " + h(A3, "tetel-linearis-belso"),
       "$\\displaystyle\\int f(ax+b)\\,dx=\\dfrac1a\\,F(ax+b)+C$ $(a\\ne0)$",
       "$\\displaystyle\\int(2x-5)^7dx=\\dfrac{(2x-5)^8}{16}+C$"],
      ["$\\dfrac{f'}{f}$ " + h(A3, "tetel-f-per-f"), "$\\displaystyle\\int\\dfrac{f'(x)}{f(x)}\\,dx=\\ln\\lvert f(x)\\rvert+C$, ha $f$ deriválható és nem nulla az adott intervallumon",
       "$\\displaystyle\\int\\dfrac{2x}{x^2+7}\\,dx=\\ln\\left(x^2+7\\right)+C$ ($x^2+7\\gt0$, abszolút érték nem kell)"],
      ["$f^n\\cdot f'$ " + h(A3, "tetel-f-hatvany"),
       (
           "$\\displaystyle\\int\\bigl[f(x)\\bigr]^nf'(x)\\,dx=\\dfrac{\\bigl[f(x)\\bigr]^{n+1}}{n+1}+C$ $(n\\ne-1)$; "
           '$f$ deriválható, a szereplő hatványok valósak és a láncszabály alkalmazható (valós $n$-re elegendő '
           '$f>0$)'
       ),
       "$\\displaystyle\\int\\cos x\\sin^3x\\,dx=\\dfrac{\\sin^4x}{4}+C$"],
      ["általános " + h(A3, "tetel-helyettesites"), "$t=g(x)$, $dt=g'(x)\\,dx$: "
       "$\\displaystyle\\int f\\bigl(g(x)\\bigr)g'(x)\\,dx=\\int f(t)\\,dt$ — $x$ nem maradhat benne; a végén "
       "helyettesíts vissza", "kidolgozva: " + h(A3, "pelda-helyettesites", "A3")]]),
  r'<p><b>A szorzó igazítása:</b> $\displaystyle\int\dfrac{x}{x^2+7}\,dx=\dfrac12\int\dfrac{2x}{x^2+7}\,dx='
  r'\dfrac12\ln\left(x^2+7\right)+C$ — állandó szorzót szabad kiemelni, $x$-et nem.</p>',
 ]),

 ("📏 A határozott integrál", [
  r'<p><b>Jelentés</b> ' + h(B1, "def-hatarozott-integral") + r': az alsó és a felső közelítő összeg közös '
  r'határértéke ($s_n\le\int_a^bf\le S_n$) — az <b>előjeles terület</b>: a tengely fölötti rész pozitív, az alatta lévő '
  r'negatív előjellel számít.</p>'
  r'<p><b>Newton–Leibniz-formula</b> ' + h(B2, "tetel-newton-leibniz") + r': ha $f$ folytonos az $[a;\,b]$-n, és $F$ '
  r'egy primitív függvénye, akkor $\displaystyle\int_a^bf(x)\,dx=\bigl[F(x)\bigr]_a^b=F(b)-F(a)$ — bármelyik primitív '
  r'függvény jó, a $C$ kiesik.</p>',
  TABLA(["tulajdonság " + h(B2, "tetel-hatarozott-tulajdonsagok"), "képlet"], [
      ["azonos határok", "$\\displaystyle\\int_a^af(x)\\,dx=0$"],
      ["a határok cseréje", "$\\displaystyle\\int_b^af(x)\\,dx=-\\int_a^bf(x)\\,dx$"],
      ["additivitás", "$\\displaystyle\\int_a^bf\\,dx+\\int_b^cf\\,dx=\\int_a^cf\\,dx$"],
      ["linearitás", "$\\displaystyle\\int_a^b\\bigl(c\\,f\\pm g\\bigr)\\,dx=c\\int_a^bf\\,dx\\pm\\int_a^bg\\,dx$"]]),
  r'<p><b>Helyettesítés</b> ' + h(B2, "tetel-hatar-atiras") + r': a $t=g(x)$ cserénél a határokat is írd át — az új '
  r'határok $g(a)$ és $g(b)$ —, és akkor nem kell visszahelyettesíteni.</p>',
 ]),

 ("🗺️ Terület — öt helyzet", [
  TABLA(["helyzet", "a terület"], [
      ["$f\\ge0$ az $[a;\\,b]$-n " + h(B3, "pelda-gorbe-alatti"), "$T=\\displaystyle\\int_a^bf(x)\\,dx$"],
      ["$f\\le0$ az $[a;\\,b]$-n " + h(B3, "tetel-elojelvaltas"), "$T=-\\displaystyle\\int_a^bf(x)\\,dx=\\left|\\int_a^bf(x)\\,dx\\right|$"],
      ["$f$ előjelet vált " + h(B3, "tetel-elojelvaltas"), "bonts a zérushelyeknél, és a részek abszolút értékét add össze"],
      ["görbe és a két tengely " + h(B3, "pelda-ket-tengely"), 'a határok: $0$ és a pozitív zérushely (ha az adott görbe az első síknegyedben zárt síkidomot határol a tengelyekkel)'],
      ["két görbe " + h(B3, "tetel-ket-gorbe"), (
                                                      '$T=\\displaystyle\\int_a^b\\bigl(\\text{felső}-\\text{alsó}\\bigr)\\,dx$, $a$ és $b$ a határoló '
                                                      'metszéspontok $x$-koordinátái — akkor is, ha a síkidom a tengely alá nyúlik'
                                                  )]]),
  (
      '<p><b>Menetrend:</b> 1. vázlat · 2. zérushelyek, metszéspontok · 3. melyik görbe van felül (két '
      'szomszédos metszéspont között egy próbapont dönt) · 4. integrálás · 5. a részek összege. A terület '
      '<b>sosem negatív</b>.</p>'
  ),
 ]),

 ("⚠️ Véd Vilmos csapdái — amelyeken a legtöbben elcsúsznak", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A nyolc leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>Elfelejtett $+C$:</b> a határozatlan integrálnál kötelező; a határozottnál kiesik.</li>'
  r'<li><b>Az $n=-1$ kivétel:</b> $\int\dfrac1x\,dx=\ln\lvert x\rvert+C$ (nem $\dfrac{x^0}{0}$); és '
  r'$\int\dfrac{1}{x^5}\,dx=-\dfrac{1}{4x^4}+C$, nem $\ln\lvert x^5\rvert$.</li>'
  r'<li><b>Szorzat, hányados:</b> $\int f\cdot g\ne\int f\cdot\int g$ és $\int\dfrac fg\ne\dfrac{\int f}{\int g}$ — előbb '
  r'alakíts át.</li>'
  r'<li><b>Lineáris belső függvénynél a belső derivált osztó, nem szorzó:</b> '
  r'$\int(4x+3)^3dx=\dfrac{(4x+3)^4}{16}+C$; $\int e^{\frac x2}dx=2e^{\frac x2}+C$. Nemlineáris belső függvénynél '
  r'osztani tilos: ott a belső deriváltnak szorzóként ott kell lennie ($f^n\cdot f\'$), különben előbb alakíts át.</li>'
  r'<li><b>Az $\frac{f\'}{f}$ minta</b> csak akkor működik, ha a számláló — szorzótól eltekintve — a nevező deriváltja: '
  r'az $\int\dfrac{1}{x^2+7}\,dx$-nél ez a minta nem használható.</li>'
  r'<li><b>Határozott integrál ≠ terület:</b> $\int_{-2}^2x\,dx=0$, a terület viszont $4$ — előjelváltásnál '
  r'bontani kell.</li>'
  r'<li><b>Helyettesítésnél a határok:</b> vagy átírod őket $t$-re, vagy visszahelyettesítesz — a kettőt keverni hiba.</li>'
  r'<li><b>$F(b)-F(a)$ zárójellel:</b> $\bigl[x^2-x\bigr]_{-1}^2=(4-2)-(1+1)=0$ — az $F(a)$ egészét kell kivonni.</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A1 + r'">primitív függvény</a> · <a href="' + A2 + r'">integráltáblázat</a> · '
  r'<a href="' + A3 + r'">helyettesítés</a> · <a href="' + B1 + r'">határozott integrál</a> · '
  r'<a href="' + B2 + r'">Newton–Leibniz-formula</a> · <a href="' + B3 + r'">síkidomok területe</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FI + r'">Zsoldos-lista I.</a> (határozatlan integrál) · <a href="' + FH + r'">'
  r'Zsoldos-lista II.</a> (határozott integrál, terület) · <a href="feladatok-hazi.html">I.V.H. Kihallgató Terem</a> (házi).</p>'
  r'<p><b>Ismétlés:</b> a deriválttáblázat és a deriválási szabályok a <a href="../03-derivalt/osszefoglalo.html">03-as '
  r'Csalópapíron</a> — az integrálás ennek a megfordítása. A témakört <a href="terepkuldetes.html">' + KUL
  + r'</a> küldetés zárja.</p></div></div>',
 ]),
]
# a Csalópapír példái
for f, F_ in (("(2*x-5)**7", "(2*x-5)**8/16"), ("2*x/(x**2+7)", "log(x**2+7)"), ("cos(x)*sin(x)**3", "sin(x)**4/4"),
              ("x/(x**2+7)", "log(x**2+7)/2"), ("1/x**5", "-1/(4*x**4)"), ("(4*x+3)**3", "(4*x+3)**4/16"),
              ("exp(x/2)", "2*exp(x/2)"), ("sqrt(x)", "Rational(2,3)*x*sqrt(x)")):
    FG.primitiv_e(f, F_, nev="Csalópapír " + f)
if FG.terulet("x", -2, 2)[0] != 4 or integrate(Ex("x"), (x, -2, 2)) != 0 \
        or Ex("x**2-x").subs(x, 2) - Ex("x**2-x").subs(x, -1) != 0:
    FG.E.append("Csalópapír-számok")

lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon", cim_tiszta="Csalópapír", itt="Csalópapír",
    alcim="Primitív függvény, integráltáblázat, a helyettesítés négy mintája, a határozott integrál és a "
          "területszámítás egy lapon — ismétléshez, a dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló", szakaszok=_prim(OSSZ),
    elozo=("feladatok-hazi.html", "I.V.H. Kihallgató Terem"), kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p — terepküldetés (önteszt)
E = []


def _egy(g, wv):
    if isinstance(g, (list, tuple)) and isinstance(wv, (list, tuple)):
        return len(g) == len(wv) and all(_egy(p, q) for p, q in zip(g, wv))
    return g == wv or simplify(sympy.sympify(g) - sympy.sympify(wv)) == 0


def ck(nev, g, wv):
    if not _egy(g, wv):
        E.append((nev, g, wv))


a_ = symbols("a", positive=True)
# I. SZVETI regenerációja
ck("I-1", [diff(Ex("4*x**3-3*x**2+2*x-3"), x), Ex("4*x**3-3*x**2+2*x-3").subs(x, 2)], [Ex("12*x**2-6*x+2"), 21])
ck("I-3", [diff(Ex("x**3-x**2+2*x+2"), x, 2), diff(Ex("x**3-x**2+2*x+2"), x).subs(x, 1),
           Ex("x**3-x**2+2*x+2").subs(x, 1)], [Ex("6*x-2"), 3, 4])
ck("I-4", simplify(diff(Ex("x*log(x)-x"), x) - Ex("log(x)")), 0)
# II. Nagol trükkje
for f, F_ in (("(1-3*x)**5", "-(1-3*x)**6/18"), ("(4*x**3+2*x)/(x**4+x**2+1)", "log(x**4+x**2+1)"),
              ("x**2*(x**3-1)**5", "(x**3-1)**6/18"), ("sin(x)/(2+cos(x))", "-log(2+cos(x))")):
    FG.primitiv_e(f, F_, nev="terep II " + f)
# III. A Void kivágása
ck("III-1", integrate(Ex("2*x-1/x**2"), (x, 1, 3)), Q(22, 3))
ck("III-2", integrate(Ex("x*exp(x**2)"), (x, 0, 2)), (EE**4 - 1) / 2)
ck("III-4", [FG.terulet("x**2-5*x", 0, 6)[0], integrate(Ex("x**2-5*x"), (x, 0, 6))], [Q(71, 3), -18])
ck("III-5", [sorted(solve(Ex("x**2-4*x+5") - Ex("x+1"), x)), FG.terulet("x+1", 1, 4, "x**2-4*x+5")[0]], [[1, 4], Q(9, 2)])
ck("III-6", FG.terulet("16-x**4", 0, 2)[0], Q(128, 5))
# IV. Véd Vilmos jegyzőkönyve
for f, F_ in (("(x**2-3)/x", "x**2/2-3*log(Abs(x))"), ("sin(x/3)", "-3*cos(x/3)"),
              ("(x**2-2)**2", "x**5/5-Rational(4,3)*x**3+4*x")):
    FG.primitiv_e(f, F_, nev="terep IV " + f)
ck("IV-4", [FG.terulet("2*x**3", -1, 1)[0], integrate(Ex("2*x**3"), (x, -1, 1))], [1, 0])
ck("IV-5", integrate(Ex("2*x*(x**2+3)**3"), (x, 0, 1)), Q(175, 4))
assert not E, E
print("F5p önteszt: OK")

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>SZVETI:</b> Darabokban vagyok. Szó szerint. A deriválás szétszedett, most visszafelé kell összerakni — és '
         'ehhez nem elég Vilmos lelkesedése, meg az a kockás kabát sem, amelyik minden varrásánál töréspontot mutat. '
         '<b>Véd Vilmos:</b> 🌮 <i>Burek-matek:</i> „ha elég sok darabot összeadok, a végén úgyis kijön valami.” '
         '<b>Nagol:</b> Pontosan ez az integrál — csak nem mindegy, hogyan adod össze. Négy fázis: SZVETI regenerációja '
         '(primitív függvény), a helyettesítés trükkje, a Void egy zónájának kivágása (határozott integrál, terület), végül '
         'Vilmos jegyzőkönyve, tele hibás integrállal.'),
   r'<p>Minden lépésnél írd le, melyik szabályt vagy módszert használtad (táblázat, átalakítás, helyettesítés, '
   r'Newton–Leibniz-formula, bontás a zérushelynél). Számológép használható. A területfeladatokhoz készíts vázlatot, a '
   r'választ pedig fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, mint máshol a '
   r'számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — SZVETI regenerációja", [
   r'<p>SZVETI egy darabjáról csak azt tudjuk, milyen a meredeksége: a darab görbéjének deriváltja '
   r'$f(x)=12x^2-6x+2$. A darabot a primitív függvénye adja vissza.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Írd fel az $f$ összes primitív függvényét! Melyik közülük az, amelynek grafikonja átmegy a $P(2;\,21)$ '
   r'ponton? Ellenőrizd deriválással!</li>'
   r'<li>SZVETI két darabja, $F$ és $G$, ugyanannak a valós számokon értelmezett függvénynek két primitív függvénye; $F(0)=1$ és $G(0)=-4$. Mennyi '
   r'$F(5)-G(5)$? Indokold számolás nélkül!</li>'
   r'<li>Egy másik darabnak a <b>második</b> deriváltját ismerjük: $g\'\'(x)=6x-2$, továbbá $g\'(1)=3$ és $g(1)=4$. '
   r'Határozd meg a $g$ függvényt!</li>'
   r'<li>Vilmos azt állítja, hogy az $F(x)=x\ln x-x$ függvény ($x\gt0$) az $\ln x$ primitív függvénye. Igaza van? '
   r'Döntsd el deriválással!</li>'
   r'</ol>',
 ]),

 ("II. fázis — Nagol trükkje", [
   r'<p>Nagol szerint a jó helyettesítés „a karmok helyett az eszünket koptatja”. Számítsd ki a határozatlan '
   r'integrálokat, és ellenőrizd őket deriválással!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>$\displaystyle\int(1-3x)^5\,dx$</li>'
   r'<li>$\displaystyle\int\dfrac{4x^3+2x}{x^4+x^2+1}\,dx$</li>'
   r'<li>$\displaystyle\int x^2\left(x^3-1\right)^5dx$</li>'
   r'<li>$\displaystyle\int\dfrac{\sin x}{2+\cos x}\,dx$</li>'
   r'<li>Az a)–d) feladatnál melyik helyettesítést (vagy mintát) választottad, és miért éppen azt? Mi a közös a négy '
   r'integrandusban? Fogalmazd meg két-három mondatban!</li>'
   r'</ol>',
 ]),

 ("III. fázis — A Void kivágása", [
   r'<p>A Void egy-egy zónáját görbék határolják. Hogy SZVETI darabjai kijussanak, pontosan ki kell '
   r'számolnod, mekkora területet vágunk ki.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki: $\displaystyle\int_1^3\left(2x-\dfrac{1}{x^2}\right)dx$!</li>'
   r'<li>Számítsd ki helyettesítéssel, a határokat is átírva: $\displaystyle\int_0^2x\,e^{x^2}\,dx$!</li>'
   r'<li>Tudjuk, hogy $\displaystyle\int_0^4f(x)\,dx=10$ és $\displaystyle\int_2^4f(x)\,dx=3$. Számítsd ki: '
   r'$$\int_0^2f(x)\,dx\qquad\text{és}\qquad\int_0^2\bigl(3f(x)-2\bigr)\,dx.$$</li>'
   r'<li>Az első zónát az $f(x)=x^2-5x$ függvény grafikonja és az $x$ tengely határolja a $[0;\,6]$ intervallumon. '
   r'Mekkora a területe? Miért más, mint a $\displaystyle\int_0^6f(x)\,dx$ értéke?</li>'
   r'<li>A második zónát az $y=x^2-4x+5$ parabola és az $y=x+1$ egyenes határolja. Mekkora a területe?</li>'
   r'<li>A harmadik zónát az $y=16-x^4$ görbe és a két koordinátatengely határolja az első síknegyedben. Mekkora a '
   r'területe?</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Véd Vilmos jegyzőkönyve", [
   r'<p>Vilmos leadta a saját „megoldásait” az I.V.H.-nak. Mind az öt megoldása hibás. Mindegyiknél nevezd '
   r'meg egy mondatban a hibát, és add meg a helyes eredményt!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>$\displaystyle\int\dfrac{x^2-3}{x}\,dx=\left(\dfrac{x^3}{3}-3x\right)\ln\left|x\right|+C$.</li>'
   r'<li>$\displaystyle\int\sin\dfrac x3\,dx=3\cos\dfrac x3+C$.</li>'
   r'<li>$\displaystyle\int\left(x^2-2\right)^2dx=\dfrac{\left(x^2-2\right)^3}{3}+C$.</li>'
   r'<li>„Az $y=2x^3$ görbe és az $x$ tengely közötti terület a $[-1;\,1]$ intervallumon: '
   r'$\displaystyle\int_{-1}^12x^3\,dx=\left[\dfrac{x^4}{2}\right]_{-1}^1=0$, tehát a terület $0$.”</li>'
   r'<li>„$\displaystyle\int_0^12x\left(x^2+3\right)^3dx$: legyen $t=x^2+3$, $dt=2x\,dx$, így az integrál '
   r'$\displaystyle\int_0^1t^3\,dt=\dfrac14$.”</li>'
   r'<li>Mi a közös a hibákban? Fogalmazd meg két-három mondatban, mivel lehetett volna <b>ellenőrizni</b> az egyes '
   r'eredményeket!</li>'
   r'</ol>',
   brief('<b>Nagol:</b> A darabok megvannak, a zónák kivágva. A számításaidat a tanárod ellenőrzi; a kulcs nem kerül '
         'a hálózatra. <b>SZVETI:</b> Újra egyben vagyok. Majdnem. Vilmos, a kabátod még mindig nem. '
         '<b>Véd Vilmos:</b> A következő fejezetben úgyis a véletlen dönt. <b>Nagol:</b> Arról majd <b>Nyalka Vili</b> '
         'gondoskodik: már várja a csapatot a <i>Multiverzum Lottón</i> — ott azt számoljuk meg, hányféleképpen rakhatók össze a '
         'darabok.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: SZVETI regenerációja, Nagol helyettesítéses trükkje, a Void zónáinak kivágása és Véd Vilmos "
          "hibás jegyzőkönyve. Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés", szakaszok=_prim(TEREP),
    elozo=("osszefoglalo.html", "Csalópapír"), kovetkezo=("index.html", "Integrál — a témakör"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — I.V.H. Kihallgató Terem (Vészterem)
H5 = FG.TER("3*x**2+1", 1, 2)
HK3 = FG.TER("3-3*x**2", 0, 2)
HN1 = FG.TER("5-x**2", -1, 2, "x**2-2*x+1", feliratok=("y=5-x^2", "y=x^2-2x+1"))
HN2 = FG.TER("2-x**3/4", 0, 2)
HN3 = FG.TER("x-2", 2, 5, "x**2-6*x+8", feliratok=("y=x-2", "y=x^2-6x+8"))
HA_ = [
 FG.HI("Integráld tagonként!", [("8*x**3-3*x**2+4", "2*x**4-x**3+4*x"), ("3/sqrt(x)+2*exp(x)", "6*sqrt(x)+2*exp(x)"),
                                ("5/x+2*cos(x)", "5*log(Abs(x))+2*sin(x)", r"5\ln\left|x\right|+2\sin x")]),
 FG.HI("Lineáris belső függvény:", [("(6*x+5)**3", "(6*x+5)**4/24"), ("exp(4*x-1)", "exp(4*x-1)/4"),
                                    ("sin(2*x+1)", "-cos(2*x+1)/2")]),
 (r"Határozd meg az $f(x)=4x-3$ függvénynek azt az $F$ primitív függvényét, amelynek grafikonja átmegy az $M(2;\,7)$ "
  r"ponton!", None, r"$F(x)=2x^2-3x+5$"),
 FG.HA("Számítsd ki a Newton–Leibniz-formulával!",
       [("3*x**2+2*x", 0, 2, 12), ("2/sqrt(x)", 1, 4, 4), ("sin(x)+1", 0, "pi", "2+pi", r"2+\pi")]),
 (r"Számítsd ki az $y=3x^2+1$ függvény grafikonja és az $x$ tengely közötti síkidom területét az $[1;\,2]$ "
  r"intervallumon!", None,
  r"$T=8$" + H5[2]),
]
HK_ = [
 FG.HI(r"Az $\dfrac{f'}{f}$ és az $\bigl[f(x)\bigr]^n\cdot f'(x)$ minta — ha kell, igazítsd a szorzót!",
       [("6*x**2/(x**3+5)", "2*log(Abs(x**3+5))", r"2\ln\left|x^{3}+5\right|"), ("x*(x**2+4)**3", "(x**2+4)**4/8"),
        ("cos(x)*sin(x)**4", "sin(x)**5/5")]),
 (r"Számítsd ki helyettesítéssel, a határokat is átírva: $\displaystyle\int_0^2x\left(x^2+1\right)^2dx$!", None,
  r"$t=x^2+1$, az új határok $1$ és $5$: $\dfrac12\displaystyle\int_1^5t^2\,dt=\dfrac{62}{3}$"),
 (r"Az $f(x)=3-3x^2$ függvény a $[0;\,2]$ intervallumon előjelet vált. Számítsd ki a grafikon és az $x$ tengely "
  r"közötti síkidom területét, és hasonlítsd össze a $\displaystyle\int_0^2f(x)\,dx$ értékével!", None,
  r"$T=6$, míg $\displaystyle\int_0^2f\,dx=-2$" + HK3[2]),
]
HN_ = [
 (r"Számítsd ki az $y=5-x^2$ és az $y=x^2-2x+1$ parabolák által határolt síkidom területét!", None,
  r"$T=9$" + HN1[2]),
 ("Görbe és tengelyek, görbe és egyenes.",
  [r"Számítsd ki az $y=2-\dfrac{x^3}{4}$ görbe és a két koordinátatengely által határolt síkidom területét (az első "
   r"síknegyedben)!",
   r"Számítsd ki az $y=x^2-6x+8$ parabola és az $y=x-2$ egyenes által határolt síkidom területét! (Vigyázz: a síkidom "
   r"egy része az $x$ tengely alatt van.)"],
  [r"$T=3$" + HN2[2],
   r"$T=\dfrac{9}{2}$" + HN3[2]]),
]
# a saját számok önellenőrzése
for kap, vart in [(H5[0], 8), (HK3[0], 6), (integrate(Ex("3-3*x**2"), (x, 0, 2)), -2), (HN1[0], 9), (HN2[0], 3),
                  (sorted(solve(Ex("5-x**2") - Ex("x**2-2*x+1"), x)), [-1, 2]),
                  (HN3[0], Q(9, 2)), (sorted(solve(Ex("x**2-6*x+8") - Ex("x-2"), x)), [2, 5]),
                  (integrate(Ex("x*(x**2+1)**2"), (x, 0, 2)), Q(62, 3)), (Ex("2*x**2-3*x+5").subs(x, 2), 7)]:
    if kap != vart:
        E.append(("házi", kap, vart))
FG.primitiv_e("4*x-3", "2*x**2-3*x+5", nev="házi alap-3")

# tiltott és már használt adatok: a felmérők (tiltott_4e_04) + a tananyag, a két lista és ez a fájl
_forras = "".join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding="utf-8").read()
                  for f in ("build_fgy_4e_04.py", "build_tananyag_4e_04a.py", "build_tananyag_4e_04b.py"))
_korabbi = set(re.findall(r'"([^"]*x[^"]*)"', _forras))
UJ_TEREP = ["12*x**2-6*x+2", "4*x**3-3*x**2+2*x-3", "6*x-2", "x**3-x**2+2*x+2", "x*log(x)-x", "(1-3*x)**5",
            "(4*x**3+2*x)/(x**4+x**2+1)", "x**2*(x**3-1)**5", "sin(x)/(2+cos(x))", "2*x-1/x**2", "x*exp(x**2)",
            "x**2-5*x", "16-x**4", "(x**2-3)/x", "sin(x/3)", "(x**2-2)**2", "2*x**3", "2*x*(x**2+3)**3"]
UJ_HAZI = ["8*x**3-3*x**2+4", "3/sqrt(x)+2*exp(x)", "5/x+2*cos(x)", "(6*x+5)**3", "exp(4*x-1)", "sin(2*x+1)", "4*x-3",
           "2*x**2-3*x+5", "3*x**2+2*x", "2/sqrt(x)", "sin(x)+1", "3*x**2+1", "6*x**2/(x**3+5)", "x*(x**2+4)**3",
           "cos(x)*sin(x)**4", "x*(x**2+1)**2", "3-3*x**2", "5-x**2", "x**2-2*x+1", "2-x**3/4",
           "x-2", "x**2-6*x+8"]
PAROK = [("x+1", "x**2-4*x+5"), ("5-x**2", "x**2-2*x+1"), ("x-2", "x**2-6*x+8")]
E += TILT.ellenoriz(UJ_TEREP + UJ_HAZI, PAROK)
for k in _korabbi:
    for u in UJ_TEREP + UJ_HAZI:
        if FG._az(u, k):
            E.append(("már használt", u, k))
for i, u in enumerate(UJ_TEREP):
    for v in UJ_HAZI:
        if FG._az(u, v):
            E.append(("terep = házi", u, v))
assert not E and not FG.E, (E, FG.E)
print("F6h önteszt és tiltott-ellenőrzés: OK")

body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(_prim(HA_), "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(_prim(HK_), "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(_prim(HN_), "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem", h1="I.V.H. Kihallgató Terem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span><span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a határozatlan és a határozott integrálból — házi feladatnak és a dolgozat előtti "
            "bemelegítésnek. Az I.V.H. minden választ ellenőriz: a végeredmény lenyitható, de csak a számolás után nézd meg!",
      sections_html="\n".join(body), ossz_nev="Csalópapírt",
      prev=FH, prevc="Zsoldos-lista II. — Határozott integrál", nxt="osszefoglalo.html", nxtc="Csalópapír")
print("✓ feladatok-hazi.html | Alap", len(HA_), "Közép", len(HK_), "Nehéz", len(HN_))


# ==================================================================== F5 — témakör-index
def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


KT = {
 "A1": kartya(A1, "Visszafelé — a primitív függvény", "A deriválás megfordítása, a primitív függvények serege és a $+C$, a határozatlan integrál — interaktív ábrával"),
 "A2": kartya(A2, "Csalópapír visszafelé — az integráltáblázat", "Az alapintegrálok, konstansszoros és összeg, gyök és tört hatványként, átalakítás integrálás előtt"),
 "A3": kartya(A3, "Nagol trükkje — helyettesítéses integrálás", "Lineáris belső függvény, az $\\frac{f'}{f}$ és az $f^n\\cdot f'$ minta, a $t=g(x)$ helyettesítés"),
 "B1": kartya(B1, "Bezárva [a; b]-be — a határozott integrál", "A területprobléma, alsó és felső közelítő összeg, előjeles terület — interaktív ábrával"),
 "B2": kartya(B2, "A híd — a Newton–Leibniz-formula", "A formula, a határozott integrál tulajdonságai, helyettesítés a határok átírásával"),
 "B3": kartya(B3, "A Void kivágása — síkidomok területe", "Görbe alatti terület, a tengely alatti rész, előjelváltás, görbe és a két tengely, két görbe között"),
 "f1": kartya(FI, "🏋️ Zsoldos-lista I. — Határozatlan integrál", "Primitív függvény, táblázat, átalakítás, a helyettesítés mintái — 24 feladat és egy joker"),
 "f2": kartya(FH, "🏋️ Zsoldos-lista II. — Határozott integrál", "Közelítő összegek, Newton–Leibniz, tulajdonságok, területszámítás ábrás kulccsal — 26 feladat és egy joker"),
 "hazi": kartya("feladatok-hazi.html", "🕹️ I.V.H. Kihallgató Terem — házi feladatok", "Rövid, vegyes gyakorlósor a dolgozat előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL, "Négyfázisú záróküldetés — SZVETI regenerációja, Nagol trükkje, a Void kivágása és Vilmos hibás jegyzőkönyve"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír", "Integráltáblázat, a helyettesítés mintái, Newton–Leibniz és a területszámítás egy lapon"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(KT[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Integrál | 4e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="4e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">&#8730;</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">4e</span></a> ›
  <span class="itt">Integrál</span>
</nav>
<div class="hero">
  <h1>Integrál</h1>
  <p class="alcim">A deriválás megfordítása: primitív függvény, integráltáblázat és helyettesítés — aztán a határozott
  integrál, a Newton–Leibniz-formula és a síkidomok területe.</p>
  <div class="meta-sor"><span class="chip ora">17 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧵 <b>04 — A Valóság Összefoltozása.</b> Mentor: <b>SZVETI</b> és <b>Nagol</b>. Darabokban
  vagyok — a deriválás szétszedett. Most visszafelé rakjuk össze: a deriváltból megkeressük azt a függvényt, amelyből
  lett. Aztán Nagol bezár minket egy intervallumba, és kiszámoljuk, mekkora területet kell kivágni a Voidból. Véd Vilmos
  is jön; a kabátjáról most nem mondok semmit. Majdnem semmit.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🧩 Határozatlan integrál — SZVETI</h3>
''' + racs("A1", "A2", "A3") + '''
    <h3>📏 Határozott integrál és terület — Nagol és SZVETI</h3>
''' + racs("B1", "B2", "B3") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("f1", "f2", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> a hat tananyag-egység sorban, közben a két Zsoldos-lista megfelelő
    szintjei (a határozatlan integrál egységeihez az I., a határozott integrálhoz és a területhez a II.), a végén az
    I.V.H. Kihallgató Terem. A határozatlan integrál a harmadik ellenőrző, a határozott integrál és a terület a negyedik
    dolgozat anyaga. A Csalópapír az ismétlést szolgálja, a témakört pedig <i>A Valóság Összefoltozása</i> záróküldetés
    zárja.</p>
  </div>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {delimiters:[
    {left:'\\\\(', right:'\\\\)', display:false},
    {left:'\\\\[', right:'\\\\]', display:true}
  ]});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
