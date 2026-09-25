# -*- coding: utf-8 -*-
"""4e/03 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p), I.V.H. Kihallgato Terem (F6h) es a temakor-index (F5).
Kuldetes: A Pillanatnyi Kaosz. Mentor: Ved Vilmos es Nagol.
Az adatok ujak: sem a felmerokben (26/27-es 2. es 3. dolgozat), sem a tananyag peldaiban, sem a ket Zsoldos-listaban
nem szerepelnek — ezt a TILTOTT/HASZNALT-ellenorzes a futaskor numerikusan igazolja.
A vizsgalati segedeket (DER, MONO, GORB, TELJES, ERINTO) a build_fgy_4e_03 adja, igy a kulcsok formaja egyezik."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, brief, GYOKER
from fgy_common import cards, oldal, w
import build_fgy_4e_03 as FG
import sympy
from sympy import (Rational as Q, symbols, limit, oo, latex, S, simplify, solve, diff, expand, factor, Poly,
                   real_roots, sqrt)

x, Ex = FG.x, FG.Ex
T = dict(tagozat="4e", mappa="03-derivalt", temakor="A függvény deriváltja")
KUL = "A Pillanatnyi Káosz"
A1, A2, A3 = "tananyag-derivalt-fogalma.html", "tananyag-derivalasi-szabalyok.html", "tananyag-erinto-es-valtozasi-sebesseg.html"
B1, B2 = "tananyag-osszetett-fuggveny.html", "tananyag-masodik-derivalt.html"
C1, C2, C3 = "tananyag-monotonitas-szelsoertek.html", "tananyag-konvexitas-inflexio.html", "tananyag-fuggvenyvizsgalat.html"
FD, FV = "feladatok-derivalas.html", "feladatok-fuggvenyvizsgalat.html"


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
 ("🎯 A derivált", [
  r'<p class="lead"><b>Differenciahányados</b> ' + h(A1, "def-differenciahanyados") + r': '
  r'$\dfrac{\Delta y}{\Delta x}=\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ — a szelő meredeksége, az átlagos '
  r'változási sebesség az $x_0$ és $x_0+\Delta x$ között ($\Delta x\ne0$).</p>'
  r'<p><b>Derivált</b> ' + h(A1, "def-derivalt") + r': $f\'(x_0)=\lim\limits_{\Delta x\to0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ '
  r'— az érintő meredeksége, a <b>pillanatnyi</b> változási sebesség. Ahol ez a határérték létezik, ott az '
  r'$x\mapsto f\'(x)$ hozzárendelés az $f\'$ <b>deriváltfüggvény</b> ' + h(A1, "def-derivaltfuggveny") + r'.</p>'
  r'<p><b>Grafikonról:</b> ahol $f\'\gt0$, ott a görbe emelkedik; ahol $f\'\lt0$, ott süllyed; a csúcsban és a '
  r'völgyben (vízszintes érintő) $f\'=0$. A meredekebb szakaszon nagyobb $\lvert f\'\rvert$. Fordítva nem mindig igaz: '
  r'az $x^3$ a $0$-ban is emelkedik, pedig ott $f\'(0)=0$.</p>',
 ]),

 ("📋 A deriválttáblázat", [
  TABLA(["$f(x)$", "$f'(x)$", "$f(x)$", "$f'(x)$"], [
      ["$c$ (állandó)", "$0$", "$\\sin x$", "$\\cos x$"],
      ["$x^n$", "$n\\,x^{n-1}$", "$\\cos x$", "$-\\sin x$"],
      ["$\\sqrt x$", "$\\dfrac{1}{2\\sqrt x}$", "$\\operatorname{tg}x$", "$\\dfrac{1}{\\cos^2x}$"],
      ["$\\dfrac1x$", "$-\\dfrac{1}{x^2}$", "$\\operatorname{ctg}x$", "$-\\dfrac{1}{\\sin^2x}$"],
      ["$e^x$", "$e^x$", "$\\ln x$", "$\\dfrac1x$"],
      ["$a^x$", "$a^x\\ln a$", "$\\log_ax$", "$\\dfrac{1}{x\\ln a}$"]]),
  r'<p>A gyököt és a törtet írd <b>hatványként</b>: $\sqrt[3]{x^2}=x^{\frac23}$, $\dfrac{3}{x^4}=3x^{-4}$ — utána az '
  r'$x^n$ sora dolgozik. A teljes táblázat megjegyzésekkel: ' + h(A2, "tetel-derivalt-tablazat", "A2") + r'.</p>',
 ]),

 ("🔧 A deriválás szabályai", [
  TABLA(["szabály", "képlet"], [
      ["konstansszoros, összeg " + h(A2, "tetel-osszeg"), "$(c\\cdot f)'=c\\cdot f'$, $\\quad(f\\pm g)'=f'\\pm g'$"],
      ["szorzat " + h(A2, "tetel-szorzat"), "$(f\\cdot g)'=f'\\cdot g+f\\cdot g'$"],
      ["hányados " + h(A2, "tetel-hanyados"), "$\\left(\\dfrac fg\\right)'=\\dfrac{f'\\cdot g-f\\cdot g'}{g^2}$"],
      ["összetett függvény (láncszabály) " + h(B1, "tetel-lancszabaly"),
       "$\\big(f(g(x))\\big)'=f'\\big(g(x)\\big)\\cdot g'(x)$ — külső derivált × belső derivált"],
      ["második derivált " + h(B2, "def-masodik-derivalt"), "$f''=(f')'$"]]),
  r'<p><b>Gyakori minták</b> ($u$ a belső függvény): $\big(u^n\big)\'=n\,u^{n-1}\cdot u\'$, '
  r'$\big(\sqrt u\big)\'=\dfrac{u\'}{2\sqrt u}$, $\big(e^u\big)\'=e^u\cdot u\'$, $\big(\ln u\big)\'=\dfrac{u\'}{u}$, '
  r'$\big(\sin u\big)\'=\cos u\cdot u\'$, $\big(\cos u\big)\'=-\sin u\cdot u\'$.</p>',
 ]),

 ("📐 Érintő, normális, változási sebesség", [
  TABLA(["", ""], [
      ["érintő az $x_0$-ban " + h(A3, "tetel-erinto"), "$y-f(x_0)=f'(x_0)\\,(x-x_0)$ — a meredekség <b>szám</b>: $f'(x_0)$"],
      ["normális " + h(A3, "def-normalis"), "az érintőre merőleges; meredeksége $-\\dfrac{1}{f'(x_0)}$ (ha $f'(x_0)\\ne0$); "
       "ha $f'(x_0)=0$, a normális az $x=x_0$ függőleges egyenes"],
      ["adott $m$ meredekségű érintő", "oldd meg az $f'(x)=m$ egyenletet; párhuzamos egyenesnek ugyanaz a meredeksége"],
      ["változási sebesség " + h(A3, "pelda-sebesseg"), "$v(t)=s'(t)$, $\\;a(t)=v'(t)=s''(t)$; mértékegység: a mennyiség "
       "egysége / az idő egysége"]]),
  r'<p>Ha $v(t)=0$, a test megáll; ha $v(t)\lt0$, visszafelé halad ' + h(B2, "pelda-mozgas") + r'.</p>',
 ]),

 ("⛰️ Monotonitás és szélsőérték", [
  r'<p class="lead">$f\'\gt0$ egy intervallumon → ott <b>nő</b>; $f\'\lt0$ → ott <b>csökken</b> '
  + h(C1, "tetel-monotonitas") + r'. Ha $f\'$ egy intervallumon csak elszigetelt pontokban $0$, máshol pozitív, '
  r'$f$ ott is szigorúan nő (például $x^3$).</p>'
  r'<ul><li><b>Szükséges feltétel</b> ' + h(C1, "tetel-szelsoertek-feltetel") + r': ha $f$-nek egy intervallum '
  r'<b>belső</b> $x_0$ pontjában lokális szélsőértéke van, és ott deriválható, akkor $f\'(x_0)=0$.</li>'
  r'<li><b>Elégséges feltétel:</b> $f\'(x_0)=0$ <b>és</b> $f\'$ előjelet vált — $+\to-$: lokális <b>maximum</b>, '
  r'$-\to+$: lokális <b>minimum</b>.</li>'
  r'<li><b>Előjeltáblázat</b> ' + h(C1, "pelda-harmadfoku") + r': osztópontok az $f\'$ zérushelyei <b>és</b> a pólusok; '
  r'minden szakaszon egy próbaérték dönt.</li>'
  r'<li>A szélsőérték <b>helye</b> $x_0$, <b>értéke</b> $f(x_0)$ — a pont $\big(x_0;\,f(x_0)\big)$.</li></ul>',
 ]),

 ("〰️ Konvexitás és inflexió", [
  r'<p class="lead">$f\'\'\gt0$ → <b>konvex</b> (∪), $f\'\'\lt0$ → <b>konkáv</b> (∩) ' + h(C2, "tetel-konvexitas") + r'.</p>'
  r'<p><b>Inflexiós pont</b> ' + h(C2, "def-inflexio") + r': ahol a görbülés irányt vált — $f\'\'(x_0)=0$ <b>és</b> '
  r'$f\'\'$ előjelet vált. Pólusnál is válthat a görbülés, de ott nincs inflexiós pont (nincs függvényérték).</p>',
 ]),

 ("🧭 A teljes vizsgálat — hét lépés", [
  TABLA(["lépés", "mit számolsz"], [
      ["1. értelmezési tartomány", "a kizárt helyek minden táblázat osztópontjai"],
      ["2. zérushely, előjel", "$f(x)=0$, $f(0)$, előjeltáblázat"],
      ["3. paritás", "$f(-x)$ kiszámolva: páros, páratlan vagy egyik sem (ha $D_f$ nem szimmetrikus a $0$-ra, egyik sem)"],
      ["4. határértékek, aszimptoták", "határérték a $\\pm\\infty$-ben és a pólusok két oldalán; függőleges, vízszintes "
       "vagy ferde aszimptota (legalább másodfokú polinomnak nincs)"],
      ["5. monotonitás, szélsőérték", "$f'$ zérushelyei, előjeltáblázat"],
      ["6. konvexitás, inflexió", "$f''$ zérushelyei, előjeltáblázat"],
      ["7. grafikon", "a kitüntetett pontok, az aszimptoták és a táblázatok alapján"]]),
  r'<p>Kidolgozva: ' + h(C3, "pelda-polinom-vizsgalat", "polinom") + r' és '
  + h(C3, "pelda-tort-vizsgalat", "racionális törtfüggvény") + r' (C3). Az aszimptotákhoz: '
  r'<a href="../02-fuggvenyek/osszefoglalo.html">a 02-es Csalópapír</a>.</p>',
 ]),

 ("⚠️ Véd Vilmos csapdái — amin a legtöbben elcsúsznak", [
  r'<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A nyolc leggyakoribb hiba</p>'
  r'<ol class="reszfeladatok">'
  r'<li><b>$(f\cdot g)\'=f\'\cdot g\'$:</b> nem! A szorzat deriváltja két tag összege: $f\'g+fg\'$.</li>'
  r'<li><b>A hányados sorrendje:</b> a számlálóban $f\'g-fg\'$ — fordított sorrendben az előjel is fordul; a '
  r'nevező $g^2$.</li>'
  r'<li><b>Elfelejtett belső derivált:</b> $\big(\sin 3x\big)\'=3\cos 3x$, nem $\cos 3x$; $\big(e^{2x}\big)\'=2e^{2x}$.</li>'
  r'<li><b>Az állandó deriváltja:</b> $(\pi^2)\'=0$, $(\ln 5)\'=0$ — ezek számok, nem függvények.</li>'
  r'<li><b>Érintő $f\'(x)$-szel:</b> az érintő meredeksége az $f\'(x_0)$ <b>szám</b>; ha $x$ marad benne, nem egyenest kapsz.</li>'
  r'<li><b>„$f\'(x_0)=0$, tehát szélsőérték”:</b> csak ha $f\'$ előjelet is vált — az $x^3$-nek a $0$-ban nincs.</li>'
  r'<li><b>„$f\'\'(x_0)=0$, tehát inflexió”:</b> az $x^4$-nél $f\'\'(0)=0$, mégis végig konvex.</li>'
  r'<li><b>Pólus a táblázatból kihagyva:</b> a pólusnál is válthat előjelet $f$, $f\'$ és $f\'\'$ — és az $\frac1x$ '
  r'a teljes értelmezési tartományán nem szigorúan monoton csökkenő, csak a $(-\infty;\,0)$ és a $(0;\,+\infty)$ '
  r'intervallumon külön-külön.</li>'
  r'</ol></div>',
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A1 + r'">a derivált fogalma</a> · <a href="' + A2 + r'">deriválási szabályok</a> · '
  r'<a href="' + A3 + r'">érintő, változási sebesség</a> · <a href="' + B1 + r'">összetett függvény</a> · '
  r'<a href="' + B2 + r'">második derivált</a> · <a href="' + C1 + r'">monotonitás, szélsőérték</a> · '
  r'<a href="' + C2 + r'">konvexitás, inflexió</a> · <a href="' + C3 + r'">teljes vizsgálat</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FD + r'">Zsoldos-lista I.</a> (deriválás) · <a href="' + FV + r'">Zsoldos-lista II.</a> '
  r'(függvényvizsgálat) · <a href="feladatok-hazi.html">I.V.H. Kihallgató Terem</a> (házi).</p>'
  r'<p><b>Ismétlés:</b> határérték és aszimptoták a <a href="../02-fuggvenyek/osszefoglalo.html">02-es Csalópapíron</a>. '
  r'A témakört <a href="terepkuldetes.html">' + KUL + r'</a> küldetés zárja.</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon", cim_tiszta="Csalópapír", itt="Csalópapír",
    alcim="A derivált fogalma, a deriválttáblázat és a szabályok, érintő és változási sebesség, monotonitás, "
          "konvexitás és a teljes függvényvizsgálat egy lapon — ismétléshez, a dolgozat előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló", szakaszok=_prim(OSSZ),
    elozo=("feladatok-hazi.html", "I.V.H. Kihallgató Terem"), kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p — terepküldetés (önteszt)
E = []


def ck(nev, g, wv):
    if not (g == wv or (not isinstance(g, (list, tuple)) and simplify(sympy.sympify(g) - sympy.sympify(wv)) == 0)):
        E.append((nev, g, wv))


t_, h_, a_, b_ = symbols("t h a b", real=True)
SP = t_**3 - 9*t_**2 + 24*t_                                    # I. az ügynök helye (m), 0 ≤ t ≤ 6 (s)
ck("I-dq", expand((SP.subs(t_, 1 + h_) - SP.subs(t_, 1)) / h_), h_**2 - 6*h_ + 9)
V_ = diff(SP, t_)
ck("I-v", factor(V_), 3*(t_ - 2)*(t_ - 4))
ck("I-ut", [SP.subs(t_, k) for k in (0, 2, 4, 6)], [0, 20, 16, 36])
ck("I-a", [expand(diff(SP, t_, 2)), solve(diff(SP, t_, 2), t_), V_.subs(t_, 3)], [6*t_ - 18, [3], -3])
RA = Ex("8-x**2/2")                                             # II. a rámpa, 0 ≤ x ≤ 4
ck("II-1", FG.ERINTO("8-x**2/2", 1), (Q(15, 2), -1, -x + Q(17, 2)))
ck("II-2", sorted(solve(RA.subs(x, a_) + diff(RA, x).subs(x, a_) * (5 - a_), a_)), [2, 8])
ck("II-2e", FG.ERINTO("8-x**2/2", 2), (6, -2, -2*x + 10))
ck("II-3", [solve(diff(RA, x) + 3, x), FG.ERINTO("8-x**2/2", 3)], [[3], (Q(7, 2), -3, -3*x + Q(25, 2))])
ck("II-4", expand(6 - (x - 2) / diff(RA, x).subs(x, 2)), x/2 + 5)
UT = "x**4-6*x**2+8*x"                                          # III. Nagol ütésének íve
ck("III-d", factor(diff(Ex(UT), x)), 4*(x - 1)**2*(x + 2))
ck("III-sz", FG.szelso(Ex(UT)), ([], [(-2, -24)]))
ck("III-inf", FG.inflexio(Ex(UT)), [(-1, -13), (1, 3)])
ck("III-zh", [len(real_roots(Poly(Ex(UT), x))), Ex(UT).subs(x, -3), Ex(UT).subs(x, -2)], [2, 3, -24])
ck("IV-1", factor(diff(Ex("x**3*exp(x)"), x)), x**2*(x + 3)*sympy.exp(x))
ck("IV-2", diff(Ex("sqrt(5*x-1)"), x), 5 / (2*sqrt(5*x - 1)))
ck("IV-3", [factor(diff(Ex("x**3-3*x**2+3*x"), x)), FG.szelso(Ex("x**3-3*x**2+3*x"))], [3*(x - 1)**2, ([], [])])
ck("IV-4", [Ex("1/x").subs(x, -1), Ex("1/x").subs(x, 1)], [-1, 1])
assert not E, E
print("F5p önteszt: OK")

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Az I.V.H. ügynökei olyan gyorsak, hogy mire lefényképezem őket, már máshol vannak. 🌮 '
         '<i>Burek-matek:</i> „ha elég rövid ideig nézem, a sebességük nulla — hiszen közben nem mozdulnak.” '
         '<b>Nagol:</b> Pont ezért találták ki a deriváltat: a nagyon rövid idő alatti elmozdulást elosztjuk a nagyon '
         'rövid idővel. Négy fázis: egy ügynök pillanatnyi sebessége, Vilmos ugrása egy rámpáról, az ütésem íve, végül '
         'Vilmos jegyzőkönyve, tele hibás deriválttal.'),
   r'<p>Minden lépésnél írd le, melyik szabályt vagy módszert használtad (definíció, deriválási szabály, láncszabály, '
   r'érintő egyenlete, előjeltáblázat). Számológép használható. A választ fogalmazd meg mondatban is.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, mint máshol a '
   r'számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — Egy I.V.H.-ügynök pillanatnyi sebessége", [
   r'<p>Egy ügynök egy egyenes folyosón mozog. Az indulás után $t$ másodperccel a kiindulási ponttól mért (előjeles) '
   r'helye $s(t)=t^3-9t^2+24t$ méter ($0\le t\le6$).</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki az átlagsebességét a $t=1$ és a $t=1+h$ időpont között ($h\ne0$), és ebből — $h\to0$ határátmenettel — a '
   r'pillanatnyi sebességét a $t=1$ s időpontban! (Most a definícióval dolgozz, ne a deriválási szabályokkal.)</li>'
   r'<li>Írd fel a $v(t)=s\'(t)$ sebességfüggvényt szorzat alakban! Mikor áll meg az ügynök, és mikor halad '
   r'visszafelé?</li>'
   r'<li>Hol van az ügynök a $t=6$ s időpontban, és mekkora utat tett meg addig összesen? Miért különbözik a kettő?</li>'
   r'<li>Írd fel a gyorsulásfüggvényt! Mikor a legkisebb a $v(t)$ értéke (vagyis mikor halad a leggyorsabban '
   r'visszafelé), és mennyi akkor? Mennyi ekkor a gyorsulás?</li>'
   r'</ol>',
 ]),

 ("II. fázis — Vilmos ugrása a rámpáról", [
   r'<p>Vilmos egy rámpán csúszik lefelé, amelynek a profilja az $f(x)=8-\dfrac{x^2}{2}$ függvény grafikonja '
   r'($0\le x\le4$, méterben; a talaj az $x$ tengely). Ahol elhagyja a rámpát, onnan (egyszerűsített modellben) az '
   r'érintő mentén egyenesen repül tovább.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Ha az $x_0=1$ helyen hagyja el a rámpát, hol ér földet?</li>'
   r'<li>A rámpa melyik pontjában kell elugrania, hogy pontosan az $(5;\,0)$ pontban érjen földet? (Tipp: írd fel az '
   r'érintőt egy ismeretlen $x_0=a$ helyen, és tedd bele az $(5;\,0)$ pontot.)</li>'
   r'<li>A rámpa melyik pontjában párhuzamos az érintő az $y=-3x$ egyenessel? Írd fel ezt az érintőt!</li>'
   r'<li>Írd fel a rámpa $(2;\,6)$ pontjához tartozó normális (az érintőre merőleges egyenes) egyenletét! Hol metszi '
   r'ez az egyenes az $y$ tengelyt?</li>'
   r'</ol>',
 ]),

 ("III. fázis — Nagol ütésének íve", [
   r'<p>Nagol egy ütésének pályáját az $f(x)=x^4-6x^2+8x$ függvény írja le.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Mutasd meg, hogy $f\'(x)=4(x-1)^2(x+2)$! Hol nő, hol csökken $f$, és hol van szélsőértéke?</li>'
   r'<li>Az $x=1$ helyen $f\'(1)=0$. Miért nincs mégis szélsőérték ezen a helyen?</li>'
   r'<li>Vizsgáld meg a konvexitást, és határozd meg az inflexiós pontokat! Mi különleges az $x=1$ helyhez tartozó '
   r'inflexiós pontban?</li>'
   r'<li>Hány zérushelye van $f$-nek? Indokold a monotonitással (a negatív zérushelyet nem kell pontosan '
   r'kiszámolnod), és adj meg egy $1$ hosszúságú intervallumot, amelyben a negatív zérushely van! (Tipp: keress két '
   r'szomszédos egész számot, ahol $f$ előjele különböző.)</li>'
   r'<li>Vázold a grafikont a kitüntetett pontokkal!</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Véd Vilmos jegyzőkönyve", [
   r'<p>Vilmos leadta a saját „megoldásait” az I.V.H.-nak. Az első négy mind hibás. Keresd meg a hibát, és add meg a '
   r'helyes eredményt vagy a helyes állítást!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>$\big(x^3e^x\big)\'=3x^2e^x$.</li>'
   r'<li>$\left(\sqrt{5x-1}\right)\'=\dfrac{1}{2\sqrt{5x-1}}$.</li>'
   r'<li>„Az $f(x)=x^3-3x^2+3x$ függvénynek az $x=1$ helyen szélsőértéke van, mert $f\'(1)=0$.”</li>'
   r'<li>„Az $f(x)=\dfrac1x$ függvény az értelmezési tartományán szigorúan monoton csökkenő, mert '
   r'$f\'(x)=-\dfrac1{x^2}\lt0$.”</li>'
   r'<li>Mi a közös a négy hibában? Fogalmazd meg két-három mondatban, mit kell <b>ellenőrizni</b>, mielőtt egy '
   r'szabályt vagy egy tételt alkalmazunk!</li>'
   r'</ol>',
   brief('<b>Nagol:</b> Az ügynök sebessége megmérve, Vilmos ugrása kiszámolva, az ütésem íve felrajzolva. A '
         'számításaidat a tanárod ellenőrzi; a kulcs nem kerül a hálózatra. <b>Véd Vilmos:</b> Szóval a káoszban is van '
         'rend — csak deriválni kell. <b>Nagol:</b> És most visszafelé: a következő fejezetben <b>SZVETI</b> a '
         'darabokból rakja össze az egészet. <i>A Valóság Összefoltozása</i> vár.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: egy I.V.H.-ügynök pillanatnyi sebessége, Vilmos ugrása a rámpáról, Nagol ütésének íve és Véd "
          "Vilmos hibás jegyzőkönyve. Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés", szakaszok=_prim(TEREP),
    elozo=("osszefoglalo.html", "Csalópapír"), kovetkezo=("index.html", "A Negyedik Fal"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — I.V.H. Kihallgató Terem (Vészterem)
def ERINTO_SZ(f, x0):
    y0, m, e = FG.ERINTO(f, x0)
    return f"$P\\left({latex(x0)};\\,{latex(y0)}\\right)$, $f'({latex(x0)})={latex(m)}$, ${FG.EGY(e)}$"


def PARHUZ(f, m):
    ki = []
    for x0 in sorted(solve(diff(Ex(f), x) - m, x), key=float):
        y0, _, e = FG.ERINTO(f, x0)
        ki.append(f"$P\\left({latex(x0)};\\,{latex(y0)}\\right)$: ${FG.EGY(e)}$")
    return f"$f'(x)={latex(m)}$ megoldásai: " + "; ".join(ki)


HA = [
 FG.DER("Deriváld a függvényeket!", [("3*x**4-5*x**3+2*x-8", None), ("4*sqrt(x)-2/x", "2/sqrt(x)+2/x**2")]),
 FG.DER("Deriváld a szorzatokat!", [("(2*x+1)*exp(x)", "(2*x+3)*exp(x)"), ("x**2*cos(x)", "2*x*cos(x)-x**2*sin(x)"),
                                    ("x**3*log(x)", "x**2*(3*log(x)+1)")]),
 FG.DER("Deriváld az összetett függvényeket!", [("(3*x-2)**5", "15*(3*x-2)**4"), ("sqrt(x**2+9)", "x/sqrt(x**2+9)"),
                                                ("sin(4*x)", "4*cos(4*x)"), ("exp(x**2)", "2*x*exp(x**2)")]),
 (r"Írd fel az $f(x)=x^2-4x+1$ függvény érintőjének egyenletét a megadott helyen!", ["$x_0=3$", "$x_0=0$"],
  [ERINTO_SZ("x**2-4*x+1", 3), ERINTO_SZ("x**2-4*x+1", 0)]),
 (r"Határozd meg az $f(x)=x^3-3x^2-24x+2$ függvény monotonitási intervallumait és szélsőértékeit!", None,
  FG.MONO("x**3-3*x**2-24*x+2")),
]
HK = [
 FG.DER("Deriváld a függvényeket!", [("(x+4)/(x-3)", "-7/(x-3)**2"), ("log(x**2+4)", "2*x/(x**2+4)"),
                                     ("exp(-2*x)*cos(x)", "-exp(-2*x)*(2*cos(x)+sin(x))"),
                                     ("x*sqrt(2*x+3)", "3*(x+1)/sqrt(2*x+3)")]),
 (r"Az $f(x)=x^3-6x+1$ görbe mely pontjaiban párhuzamos az érintő az $y=6x+2$ egyenessel? Írd fel ezeknek az "
  r"érintőknek az egyenletét!", None, PARHUZ("x**3-6*x+1", 6)),
 (r"Vizsgáld meg az $f(x)=x^4-6x^3+12x^2-5$ függvény konvexitását, és határozd meg az inflexiós pontjait!", None,
  FG.GORB("x**4-6*x**3+12*x**2-5")),
]
HN = [
 (r"Végezd el az $f(x)=\dfrac{x^2+8}{x-1}$ függvény teljes vizsgálatát, és vázold a grafikonját!", None,
  FG.TELJES("(x**2+8)/(x-1)", "nehéz 1.")),
 ("Paraméteres feladatok.",
  [r"Az $a$ valós paraméter mely értékeire van az $f(x)=x^3+ax^2+3x-1$ függvénynek két lokális szélsőértéke?",
   r"Határozd meg az $a$ és $b$ értékét úgy, hogy az $f(x)=x^3+ax^2+b$ függvénynek az $x=2$ helyen lokális minimuma "
   r"legyen, és ennek értéke $-1$ legyen!"],
  [r"$f'(x)=3x^2+2ax+3$; két szélsőérték akkor van, ha $f'$-nek két különböző zérushelye van (ott előjelet is vált): "
   r"$D=4a^2-36\gt0$, azaz $a\lt-3$ vagy $a\gt3$",
   r"$f'(2)=12+4a=0$, így $a=-3$; $f(2)=8-12+b=-1$, így $b=3$; ellenőrzés: $f'(x)=3x(x-2)$ a $2$-ben negatívból "
   r"pozitívba vált, tehát ott valóban minimum van"]),
]
# a saját számok önellenőrzése
for kap, vart in [(FG.szelso(Ex("x**3-3*x**2-24*x+2")), ([(-2, 30)], [(4, -78)])),
                  (FG.inflexio(Ex("x**4-6*x**3+12*x**2-5")), [(1, 2), (2, 11)]),
                  (FG.szelso(Ex("(x**2+8)/(x-1)")), ([(-2, -4)], [(4, 8)])),
                  (sorted(solve(diff(Ex("x**3-6*x+1"), x) - 6, x)), [-2, 2]),
                  (FG.ERINTO("x**2-4*x+1", 3), (-2, 2, 2*x - 8)),
                  (sympy.solve_univariate_inequality(sympy.discriminant(3*x**2 + 2*a_*x + 3, x) > 0, a_, relational=False),
                   sympy.Union(sympy.Interval.open(-oo, -3), sympy.Interval.open(3, oo))),
                  (solve([diff(Ex("x**3") + a_*x**2 + b_, x).subs(x, 2), (x**3 + a_*x**2 + b_).subs(x, 2) + 1], [a_, b_]),
                   {a_: -3, b_: 3})]:
    if kap != vart:
        E.append(("házi", kap, vart))

# tiltott és már használt adatok: a 26/27-es dolgozatok (FG.TILTOTT) + a tananyag, a két lista és ez a fájl
_forras = "".join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding="utf-8").read()
                  for f in ("build_fgy_4e_03.py", "build_tananyag_4e_03a.py", "build_tananyag_4e_03b.py"))
_korabbi = set(re.findall(r'"([^"]*x[^"]*)"', _forras)) | set(FG.TILTOTT)
UJ = ["x**3-9*x**2+24*x", "8-x**2/2", "x**4-6*x**2+8*x", "x**3*exp(x)", "sqrt(5*x-1)", "x**3-3*x**2+3*x",
      "3*x**4-5*x**3+2*x-8", "4*sqrt(x)-2/x", "(2*x+1)*exp(x)", "x**2*cos(x)", "x**3*log(x)", "(3*x-2)**5",
      "sqrt(x**2+9)", "sin(4*x)", "exp(x**2)", "x**2-4*x+1", "x**3-3*x**2-24*x+2", "(x+4)/(x-3)", "log(x**2+4)",
      "exp(-2*x)*cos(x)", "x*sqrt(2*x+3)", "x**3-6*x+1", "x**4-6*x**3+12*x**2-5", "(x**2+8)/(x-1)"]
for k in _korabbi:
    try:
        Ex(k)
    except Exception:
        continue
    for u in UJ:
        if FG._azonos(u, k):
            E.append(("már használt", u, k))
assert not E and not FG.E, (E, FG.E)
print("F6h önteszt és tiltott-ellenőrzés: OK")

body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(_prim(HA), "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(_prim(HK), "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(_prim(HN), "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem", h1="I.V.H. Kihallgató Terem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span><span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a deriválásból és a függvényvizsgálatból — házi feladatnak és a dolgozat előtti "
            "bemelegítésnek. Az I.V.H. minden választ ellenőriz: a végeredmény lenyitható, de csak a számolás után nézd meg!",
      sections_html="\n".join(body), ossz_nev="Csalópapírt",
      prev=FV, prevc="Zsoldos-lista II. — Függvényvizsgálat", nxt="osszefoglalo.html", nxtc="Csalópapír")
print("✓ feladatok-hazi.html | Alap", len(HA), "Közép", len(HK), "Nehéz", len(HN))


# ==================================================================== F5 — témakör-index
def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


KT = {
 "A1": kartya(A1, "A pillanat sebessége — a derivált fogalma", "Növekmény, differenciahányados, a szelőtől az érintőig — interaktív ábrával"),
 "A2": kartya(A2, "A deriválás szabályai", "A deriválttáblázat, konstansszoros, összeg, szorzat és hányados"),
 "A3": kartya(A3, "Az érintő és a változás üteme", "Az érintő és a normális egyenlete, adott meredekségű érintő, változási sebesség"),
 "B1": kartya(B1, "Függvény a függvényben — összetett függvény", "Belső és külső függvény, a láncszabály, tipikus minták"),
 "B2": kartya(B2, "A derivált deriváltja", "Második és magasabb rendű derivált, sebesség és gyorsulás"),
 "C1": kartya(C1, "Hegyek és völgyek — monotonitás és szélsőérték", "A derivált előjele, a szélsőérték feltételei, előjeltáblázat — mozgó érintővel"),
 "C2": kartya(C2, "Hogyan hajlik a görbe? — konvexitás és inflexió", "A második derivált előjele, inflexiós pont, törtfüggvények görbülése"),
 "C3": kartya(C3, "A teljes függvényvizsgálat", "Hét lépés a grafikonig: polinom és racionális törtfüggvény"),
 "f1": kartya(FD, "🏋️ Zsoldos-lista I. — Deriválás", "Differenciahányados, szabályok, összetett függvény, második derivált, érintő, változási sebesség — 33 feladat és egy joker"),
 "f2": kartya(FV, "🏋️ Zsoldos-lista II. — Függvényvizsgálat", "Monotonitás, szélsőérték, konvexitás, inflexió, teljes vizsgálat grafikonnal — 26 feladat és egy joker"),
 "hazi": kartya("feladatok-hazi.html", "🕹️ I.V.H. Kihallgató Terem — házi feladatok", "Rövid, vegyes gyakorlósor a dolgozat előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL, "Négyfázisú záróküldetés — az ügynök sebessége, Vilmos ugrása, Nagol ütésének íve és Vilmos hibás jegyzőkönyve"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír", "Deriválttáblázat, szabályok, érintő, monotonitás, konvexitás és a teljes vizsgálat egy lapon"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(KT[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>A függvény deriváltja | 4e | Szvetkó matek</title>
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
  <span class="itt">A függvény deriváltja</span>
</nav>
<div class="hero">
  <h1>A függvény deriváltja</h1>
  <p class="alcim">A pillanatnyi változás mértéke: a derivált fogalma, a deriválás szabályai, az érintő és a változási
  sebesség, az összetett függvény és a második derivált — aztán a függvényvizsgálat, amely a deriváltból rajzolja meg
  a grafikont.</p>
  <div class="meta-sor"><span class="chip ora">21 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>⚡ <b>03 — A Pillanatnyi Káosz.</b> Mentor: <b>Véd Vilmos</b> és <b>Nagol</b>. Szia, megint
  én. Az I.V.H. ügynökei olyan gyorsak, hogy a „mennyit tett meg egy óra alatt” kérdés semmit nem mond róluk — azt kell
  tudni, milyen gyorsak <i>most</i>. Ehhez kell a derivált. Nagol szerint ez a matek egyik legszebb ötlete; szerintem
  a legtöbb fejfájást okozó. Mindkettőnknek igaza van. Kezdd az elején: egy szelő, ami érintővé válik.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>📈 Deriválás — Véd Vilmos és Nagol</h3>
''' + racs("A1", "A2", "A3") + '''
    <h3>🪆 Továbblépés — Nagol</h3>
''' + racs("B1", "B2") + '''
    <h3>⛰️ Függvényvizsgálat — Véd Vilmos és Nagol</h3>
''' + racs("C1", "C2", "C3") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("f1", "f2", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> a nyolc tananyag-egység sorban, közben a két Zsoldos-lista megfelelő
    szintjei (a Deriválás és a Továbblépés egységeihez az I., a Függvényvizsgálathoz a II.), a végén az I.V.H.
    Kihallgató Terem. A Deriválás és a Továbblépés a második, a Függvényvizsgálat a harmadik dolgozat anyaga. A Csalópapír az ismétlést szolgálja, a témakört pedig <i>A Pillanatnyi
    Káosz</i> záróküldetés zárja.</p>
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
