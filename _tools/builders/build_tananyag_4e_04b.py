# -*- coding: utf-8 -*-
"""4e/04 — B blokk: a hatarozott integral (B1), a Newton–Leibniz-formula (B2), a siksidomok terulete (B3) + 🧾.
Mentor: Nagol & SZVETI. Kuldetes: A Valosag Osszefoltozasa.
Specifikacio: projektek/4e/munkafajlok/narrativa_04-integral.md
Tiltott adatok: a 25/26-os es 26/27-es integral-felmerok (tiltott_4e_04.py) — lent ellenorizve."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek, svg_interaktiv, _fmt
import tiltott_4e_04 as TILT

T = dict(tagozat="4e", mappa="04-integral", temakor="Integrál")
KUL = "A Valóság Összefoltozása"
FB = "feladatok-hatarozott-integral.html"
KEK, ZOLD, PIROS, BORO, SOT, SZURKE = "#3b82f6", "#047857", "#ef4444", "#f59e0b", "#0f172a", "#64748b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FB}#nehez-{tol}">Zsoldos-lista II., nehéz {tol}–{ig}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table">{"<tr>" + th + "</tr>" if any(fejlec) else ""}{tr}</table></div>'


# ---------------------------------------------------------------- önteszt
from sympy import symbols, integrate, simplify, sympify, Rational as R, pi, E as EE, log, solve, Abs, sqrt

E_ = []
t = symbols("x", real=True)
S = lambda s: sympify(s, locals={"x": t, "e": EE, "pi": pi})


def chk(nev, kapott, vart):
    if simplify(kapott - vart) != 0:
        E_.append((nev, kapott, vart))


def I(f, a, b):
    return integrate(S(f), (t, a, b))


F1 = lambda v: v * v / 3 + 1                      # B1–B2 mintafüggvénye a [0; 3]-on


def osszegek(n, a=0.0, b=3.0):
    dx = (b - a) / n
    lo = sum(min(F1(a + i * dx), F1(a + (i + 1) * dx)) * dx for i in range(n))
    hi = sum(max(F1(a + i * dx), F1(a + (i + 1) * dx)) * dx for i in range(n))
    return lo, hi


chk("B1-pontos", I("x**2/3+1", 0, 3), 6)
lo3, hi3 = osszegek(3)
if abs(lo3 - 14 / 3) > 1e-12 or abs(hi3 - 23 / 3) > 1e-12:
    E_.append(("B1-n3", lo3, hi3))
chk("B1-elojel", I("x**2-4*x", 0, 6), 0)
chk("B1-elojel-resz", I("x**2-4*x", 0, 4), R(-32, 3))
chk("B2-a", I("3*x**2-2*x", 1, 2), 4)
chk("B2-b", I("1/sqrt(x)", 1, 4), 2)
chk("B2-c", I("cos(x)", pi / 2, pi), -1)
chk("B2-d", I("exp(x)", 0, log(2)), 1)
chk("B2-csapda", I("x**2", -1, 2), 3)
chk("B2-add", I("x**2", 0, 1) + I("x**2", 1, 3), I("x**2", 0, 3))
chk("B2-add-9", I("x**2", 0, 3), 9)
chk("B2-hely-a", I("(2*x+1)**3", 0, 1), 10)
chk("B2-hely-a2", integrate(S("x**3") / 2, (t, 1, 3)), 10)
chk("B2-hely-b", I("2*x/(x**2+1)", 0, 2), log(5))
chk("B3-trapez", I("x**2/2+2", -1, 2), R(15, 2))
if sorted(solve(S("x**2-4*x"), t)) != [0, 4] or -I("x**2-4*x", 0, 4) + I("x**2-4*x", 4, 5) != 13 \
        or I("x**2-4*x", 0, 5) != R(-25, 3):
    E_.append("B3-elojel")
if sorted(solve(S("8-2*x**2"), t)) != [-2, 2] or I("8-2*x**2", 0, 2) != R(32, 3):
    E_.append("B3-tengelyek")
if sorted(solve(S("x**2-(x+2)"), t)) != [-1, 2] or I("x+2-x**2", -1, 2) != R(9, 2):
    E_.append("B3-ket")
E_ += TILT.ellenoriz(["x**2/3+1", "x**2-4*x", "3*x**2-2*x", "1/sqrt(x)", "(2*x+1)**3", "2*x/(x**2+1)",
                      "x**2/2+2", "8-2*x**2"], [("x**2", "x+2")])
assert not E_, E_
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
W, H = 360, 250
SVG_B1_OSSZEG = svg_interaktiv(
    "osszeg", [1, 0, R(1, 3)], xr=(-0.4, 3.4), yr=(-0.5, 4.6), ab=(0, 3), csuszka=(1, 40, 1, 6), w=W, h=H,
    pontos="6",
    felirat="Mozgasd a csúszkát! A sötétkék téglalapok a görbe <b>alatt</b> maradnak (alsó összeg), a világoskékek "
            "<b>fölé</b> nyúlnak (felső összeg). Ahogy $n$ nő, mindkét összeg a görbe alatti területhez, $6$-hoz tart.",
    leiras="Interaktív ábra: az f(x) = x²/3 + 1 görbe alatti terület a [0; 3] intervallumon, n darab téglalappal "
           "közelítve; a csúszka az n-et állítja")
_f4 = lambda v: v * v - 4 * v
SVG_B1_ELOJEL = svg_fuggvenyek(
    [(_f4, SOT, "f", [(-0.5, 6.4)])], xr=(-0.8, 6.8), yr=(-5.2, 12.8), w=W, h=280, jelmagyarazat=False,
    terulet=[(_f4, None, 0, 4, PIROS, 0.35), (_f4, None, 4, 6, ZOLD, 0.35)], egyseg=("1", ""),
    leiras="Az f(x) = x² − 4x grafikonja: a [0; 4]-en a tengely alatt (piros), a [4; 6]-on fölötte (zöld); "
           "a két terület egyenlő")
SVG_B2_TERULETFV = svg_fuggvenyek(
    [(F1, SOT, "f", [(-0.3, 3.3)])], xr=(-0.5, 3.4), yr=(-0.5, 4.6), w=W, h=H, jelmagyarazat=False,
    terulet=[(F1, None, 0, 2, KEK, 0.3), (F1, None, 2, 2.4, BORO, 0.6)],
    pontok=[(0, 0, "a", SOT, 3, 14), (2, 0, "x", SOT, -4, 14), (2.4, 0, "x+Δx", BORO, 2, 14)],
    leiras="A területfüggvény: a kék terület a-tól x-ig T(x); a narancssárga keskeny sáv T(x + Δx) − T(x), "
           "közelítőleg f(x)·Δx")
_fb3a = lambda v: v * v / 2 + 2
SVG_B3_TRAPEZ = svg_fuggvenyek(
    [(_fb3a, SOT, "f", [(-1.8, 2.6)])], xr=(-2.2, 3.0), yr=(-0.6, 5.4), w=W, h=H, jelmagyarazat=False,
    terulet=[(_fb3a, None, -1, 2, KEK, 0.35)],
    leiras="Görbe vonalú trapéz: az f(x) = x²/2 + 2 grafikonja alatti terület a [−1; 2] intervallumon")
SVG_B3_ELOJEL = svg_fuggvenyek(
    [(_f4, SOT, "f", [(-0.5, 5.6)])], xr=(-0.8, 6.0), yr=(-5.2, 6.2), w=W, h=H, jelmagyarazat=False,
    terulet=[(_f4, None, 0, 4, PIROS, 0.35), (_f4, None, 4, 5, ZOLD, 0.35)],
    leiras="Az f(x) = x² − 4x a [0; 5] intervallumon: a [0; 4]-en a tengely alatt (piros), a [4; 5]-ön fölötte (zöld)")
_fb3c = lambda v: 8 - 2 * v * v
SVG_B3_TENGELYEK = svg_fuggvenyek(
    [(_fb3c, SOT, "f", [(-2.4, 2.4)])], xr=(-2.8, 3.0), yr=(-1.6, 9.0), w=W, h=H, jelmagyarazat=False,
    terulet=[(_fb3c, None, 0, 2, KEK, 0.35)], pontok=[(2, 0, "", SOT)],
    leiras="Az f(x) = 8 − 2x² grafikonja, az x és az y tengely által határolt síkidom az első síknegyedben")
_g = lambda v: v + 2
_f = lambda v: v * v
SVG_B3_KET = svg_fuggvenyek(
    [(_f, SOT, "f(x) = x²", [(-2.2, 2.6)]), (_g, KEK, "g(x) = x + 2", [(-2.6, 3.0)])],
    xr=(-2.6, 3.0), yr=(-0.8, 5.4), w=W, h=H, jelmagyarazat=False,
    terulet=[(_g, _f, -1, 2, KEK, 0.3)], pontok=[(-1, 1, "", SOT), (2, 4, "", SOT)],
    leiras="Az f(x) = x² parabola és a g(x) = x + 2 egyenes; a [−1; 2]-n a köztük lévő terület kiemelve")

# ---------------------------------------------------------------- B1
_tabla_osszeg = TABLA(["$n$", "alsó összeg", "felső összeg"],
                      [[str(n), _fmt(osszegek(n)[0]), _fmt(osszegek(n)[1])] for n in (3, 6, 12, 30)] +
                      [["$n\\to\\infty$", "$6$", "$6$"]])
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> Az I.V.H. egy $[a;\\,b]$ intervallumba zárt minket. Kijutni csak az tud, aki megmondja, '
         'mekkora terület van a görbe alatt. <b>Véd Vilmos:</b> Lemérem vonalzóval. <b>SZVETI:</b> A görbét? '
         '<b>Nagol:</b> Arkhimédész 2200 éve kis darabokkal közelítette — mi is azzal kezdjük.'),
 ]),

 ("A területprobléma", [
   r'<p class="lead">Mekkora az $f(x)=\frac{x^2}{3}+1$ grafikonja alatti terület a $[0;\,3]$ intervallumon? '
   r'Téglalapot, háromszöget ki tudunk számolni — görbe vonalú alakzatot még nem. Ezért <b>téglalapokkal '
   r'közelítünk</b>.</p>',
   r'<p>Osszuk az intervallumot $n$ egyenlő részre. Minden részre állítsunk egy téglalapot: a <b>kisebbik</b> '
   r'végpontbeli függvényérték magasságával a görbe alatt maradunk (<b>alsó összeg</b>), a <b>nagyobbikkal</b> fölé '
   r'nyúlunk (<b>felső összeg</b>). A keresett terület a kettő közé esik.</p>',
   SVG_B1_OSSZEG,
   _tabla_osszeg,
   kviz(r'Növekvő függvénynél mi történik a felső összeggel, ha a téglalapok számát, $n$-et növeljük?',
        [r'csökken, és a pontos területhez tart', r'nő, mert több téglalapot adunk össze',
         r'nem változik, hiszen ugyanaz a terület', r'$0$-hoz tart, mert a téglalapok egyre keskenyebbek'], 0,
        jo="✔ A felső összeg „túllógó” része egyre kisebb, ezért csökken; az alsó nő; mindkettő a területhez tart.",
        nem="✘ Több, de keskenyebb téglalap: a görbe fölé lógó részek csökkennek. A felső összeg ezért csökken, és a "
            "pontos területhez (itt 6) tart — nem 0-hoz."),
 ]),

 ("A határozott integrál", [
   doboz("definicio", "A határozott integrál",
         r'<p>Ha az $[a;\,b]$ intervallum egyre finomabb felosztásánál az alsó és a felső összeg ugyanahhoz a számhoz '
         r'tart, ezt a számot az $f$ függvény <b>határozott integráljának</b> nevezzük az $[a;\,b]$ intervallumon:'
         r'$$\int_a^b f(x)\,dx.$$ Az $a$ az <b>alsó</b>, a $b$ a <b>felső határ</b>. Folytonos függvényre ez a szám '
         r'mindig létezik.</p>', hid="def-hatarozott-integral"),
   r'<p>Ha $f\ge0$ az $[a;\,b]$-n, a határozott integrál a grafikon, az $x$ tengely és az $x=a$, $x=b$ egyenesek által '
   r'határolt <b>görbe vonalú trapéz</b> területe. A példánkban $\int_0^3\left(\frac{x^2}{3}+1\right)dx=6$.</p>'
   r'<p>A határozatlan integrál <b>függvénysereg</b>, a határozott integrál <b>egyetlen szám</b>. A kettőt a '
   r'következő egység köti össze.</p>',
   doboz("erdekesseg", "Arkhimédész parabolaszelete",
         r'<p>Arkhimédész (Kr. e. 3. század) a parabolaszelet területét egyre több, egyre kisebb háromszöggel töltötte '
         r'ki, és megmutatta, hogy a terület a beírt háromszög $\frac43$-a. Ez a „kimerítés módszere” — a határozott '
         r'integrál ősének tekintjük. A $\int$ jel egy megnyújtott S: a latin <i>summa</i>, összeg.</p>'),
 ]),

 ("Előjeles terület", [
   r'<p class="lead">Ha a görbe a tengely <b>alatt</b> fut, a téglalapok „magassága”, $f(x)$ negatív — a határozott '
   r'integrál ott <b>negatívan</b> számol. Általában: $$\int_a^b f(x)\,dx=(\text{a tengely fölötti terület})-'
   r'(\text{a tengely alatti terület}).$$</p>',
   abra(SVG_B1_ELOJEL, 'Az $f(x)=x^2-4x$ a $[0;\\,6]$-on: a piros és a zöld rész területe egyenlő, ezért '
                       '$\\int_0^6(x^2-4x)\\,dx=0$ — pedig a két rész együttes területe nem $0$.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„A határozott integrál terület, tehát nem lehet negatív, sem $0$.” — Nem így van: a határozott integrál '
         r'<b>előjeles</b>. Ha a görbe a tengely alá bukik, a terület kiszámításához bontani kell — ezt a B3-ban '
         r'gyakoroljuk.</p>'),
   kviz(r'Egy $f$ grafikonja a $[0;\,4]$-en részben a tengely fölött, részben alatta fut. A tengely fölötti rész '
        r'területe $5$, az alatti részé $2$. Mennyi a $\int_0^4 f(x)\,dx$?',
        [r'$3$', r'$7$', r'$-3$', r'$5$'], 0,
        jo="✔ A határozott integrál előjeles: 5 − 2 = 3. (A két rész együttes területe viszont 7.)",
        nem="✘ A tengely alatti rész negatívan számít: 5 − 2 = 3. A 7 a két rész területének összege — az nem a "
            "határozott integrál."),
   doboz("erdekesseg", "Út a sebesség–idő grafikon alatt",
         r'<p>Ha egy test sebességét az idő függvényében ábrázoljuk, a grafikon alatti terület a <b>megtett út</b>: '
         r'$s=\int_{t_1}^{t_2}v(t)\,dt$. Ha a sebesség negatív (visszafelé halad), az a rész negatívan számít — így '
         r'az integrál az elmozdulást adja.</p>'),
   GY(FB + "#alap-1", "A 1–2", FB + "#kozep-1", "K 1"),
   brief('<b>SZVETI:</b> Téglalapokkal csak közelítünk, és negyven téglalapnál már az én processzorom is melegszik. '
         '<b>Nagol:</b> Van egy híd, amely pontosan kiszámolja — és a primitív függvényen át vezet.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>SZVETI:</b> A terület és a primitív függvény ugyanannak a Void-nak két oldala. <b>Véd Vilmos:</b> Ezt '
         'kívülről megtanulom, jól hangzik. <b>Nagol:</b> Newton és Leibniz egymástól függetlenül találta meg ezt a '
         'hidat — és évtizedekig vitatkoztak, kié.'),
 ]),

 ("A formula", [
   doboz("tetel", "A Newton–Leibniz-formula",
         r'<p>Ha $f$ folytonos az $[a;\,b]$ intervallumon, és $F$ az egyik primitív függvénye, akkor '
         r'$$\int_a^b f(x)\,dx=F(b)-F(a)=\big[F(x)\big]_a^b.$$</p>'
         r'<p>A határozott integrált tehát <b>nem</b> téglalapokkal számoljuk ki: keresünk egy primitív függvényt, és '
         r'kivonjuk a két határon vett értékét.</p>', hid="tetel-newton-leibniz"),
   r'<p><b>Miért igaz? (szemléletesen)</b> Jelölje $T(x)$ a görbe alatti területet $a$-tól $x$-ig. Ha $x$-et egy '
   r'kicsit, $\Delta x$-szel növeljük, a terület egy keskeny sávval nő, amely majdnem téglalap: '
   r'$T(x+\Delta x)-T(x)\approx f(x)\cdot\Delta x$. Osztva $\Delta x$-szel és $\Delta x\to0$: $T\'(x)=f(x)$. A '
   r'területfüggvény tehát <b>primitív függvény</b>, és $T(a)=0$, így $T(b)=F(b)-F(a)$.</p>',
   abra(SVG_B2_TERULETFV, 'A kék terület $T(x)$; a narancssárga sáv $T(x+\\Delta x)-T(x)\\approx f(x)\\cdot\\Delta x$.'),
   r'<p>A B1 példája most egy sorban: $\int_0^3\left(\frac{x^2}{3}+1\right)dx=\left[\frac{x^3}{9}+x\right]_0^3='
   r'(3+3)-0=6$ — pontosan az, amihez a téglalapok tartottak.</p>',
   doboz("erdekesseg", "Newton és Leibniz vitája",
         r'<p>Isaac Newton az 1660-as években, Gottfried Wilhelm Leibniz az 1670-es években jutott el a '
         r'differenciál- és integrálszámításhoz, egymástól függetlenül. Leibniz publikált előbb (1684-ben), Newton '
         r'hívei plágiummal vádolták — a vita évtizedekig mérgezte az angol és a kontinentális matematikusok viszonyát. '
         r'Ma mindkettejüket felfedezőnek tekintjük; a $\int$ jel és a $dx$ Leibniztől származik.</p>',
         hid="erdekesseg-newton-leibniz"),
 ]),

 ("Számolás a formulával", [
   doboz("pelda", "I.V.H. Akták — négy határozott integrál",
         r'<ol><li>$\int_1^2(3x^2-2x)\,dx=\big[x^3-x^2\big]_1^2=(8-4)-(1-1)=4$;</li>'
         r'<li>$\int_1^4\frac{1}{\sqrt x}dx=\big[2\sqrt x\big]_1^4=4-2=2$;</li>'
         r'<li>$\int_{\pi/2}^{\pi}\cos x\,dx=\big[\sin x\big]_{\pi/2}^{\pi}=0-1=-1$ — negatív, mert ott a koszinusz '
         r'a tengely alatt fut;</li>'
         r'<li>$\int_0^{\ln2}e^x\,dx=\big[e^x\big]_0^{\ln2}=2-1=1$.</li></ol>'
         r'<p>Az integrációs konstans kiesik: $\big(F(b)+C\big)-\big(F(a)+C\big)=F(b)-F(a)$.</p>',
         hid="pelda-newton-leibniz"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p><b>1. Fordított sorrend.</b> A felső határon vett érték jön előre: $F(b)-F(a)$, nem $F(a)-F(b)$.</p>'
         r'<p><b>2. Az elveszett mínusz.</b> $\int_{-1}^{2}x^2dx=\left[\frac{x^3}{3}\right]_{-1}^{2}=\frac83-'
         r'\left(-\frac13\right)=3$. Zárójel nélkül könnyű $\frac83-\frac13$-ot írni — az már hibás.</p>'),
   kviz(r'Kell-e $+C$ a határozott integrál eredményéhez?',
        [r'nem, mert kivonáskor kiesik', r'igen, mindig', r'csak ha az alsó határ negatív',
         r'csak trigonometrikus függvénynél'], 0,
        jo="✔ (F(b) + C) − (F(a) + C) = F(b) − F(a): a határozott integrál egyetlen szám.",
        nem="✘ A C kiesik: (F(b) + C) − (F(a) + C) = F(b) − F(a). A határozott integrál szám, nem függvénysereg."),
 ]),

 ("A határozott integrál tulajdonságai", [
   doboz("tetel", "Tulajdonságok",
         r'<ul><li>$\int_a^a f(x)\,dx=0$;</li>'
         r'<li>a határok cseréje előjelet vált: $\int_b^a f(x)\,dx=-\int_a^b f(x)\,dx$;</li>'
         r'<li>az intervallum feldarabolható: $\int_a^b f(x)\,dx+\int_b^c f(x)\,dx=\int_a^c f(x)\,dx$;</li>'
         r'<li>$\int_a^b c\cdot f(x)\,dx=c\int_a^b f(x)\,dx$ és $\int_a^b\big(f(x)\pm g(x)\big)dx='
         r'\int_a^b f(x)\,dx\pm\int_a^b g(x)\,dx$.</li></ul>', hid="tetel-hatarozott-tulajdonsagok"),
   r'<p>Például $\int_0^3x^2dx=9$, és ugyanez két részben: $\int_0^1x^2dx+\int_1^3x^2dx=\frac13+\frac{26}{3}=9$. '
   r'A feldarabolás a B3-ban lesz fontos, amikor a görbe a tengely alá bukik.</p>',
   kviz(r'Ha $\int_1^3 f(x)\,dx=5$, mennyi a $\int_3^1 f(x)\,dx$?',
        [r'$-5$', r'$5$', r'$0$', r'$\dfrac15$'], 0,
        jo="✔ A határok cseréje előjelet vált: F(1) − F(3) = −(F(3) − F(1)) = −5.",
        nem="✘ Nézd meg a formulát: ∫₃¹ f = F(1) − F(3) = −(F(3) − F(1)) = −5."),
 ]),

 ("Helyettesítés határozott integrálban", [
   doboz("tetel", "A határok átírása",
         r'<p>Ha a $t=g(x)$ helyettesítést használjuk, a <b>határokat is átírjuk</b>: $x=a$ helyett $t=g(a)$, $x=b$ '
         r'helyett $t=g(b)$. Így nem kell visszahelyettesíteni — a $t$-beli primitív függvénybe az új határokat '
         r'írjuk.</p>', hid="tetel-hatar-atiras"),
   doboz("pelda", "I.V.H. Akták — a határok is cserélődnek",
         r'<p><b>a)</b> $\int_0^1(2x+1)^3dx$: $t=2x+1$, $dt=2\,dx$; $x=0\Rightarrow t=1$, $x=1\Rightarrow t=3$: '
         r'$$\int_0^1(2x+1)^3dx=\frac12\int_1^3t^3dt=\frac12\left[\frac{t^4}{4}\right]_1^3=\frac12\cdot\frac{81-1}{4}=10.$$</p>'
         r'<p><b>b)</b> $\int_0^2\frac{2x}{x^2+1}dx$: $t=x^2+1$, $dt=2x\,dx$; $x=0\Rightarrow t=1$, $x=2\Rightarrow t=5$: '
         r'$$\int_0^2\frac{2x}{x^2+1}dx=\int_1^5\frac{dt}{t}=\big[\ln t\big]_1^5=\ln5.$$</p>'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>A régi határok ottmaradnak az új változó mellett: „$\frac12\int_0^1t^3dt$” — hibás, mert $t$ nem $0$-tól '
         r'$1$-ig fut, hanem $1$-től $3$-ig. Vagy átírod a határokat, vagy visszahelyettesítesz — a kettő keveréke '
         r'rossz.</p>'),
   GY(FB + "#alap-3", "A 3–7", FB + "#kozep-2", "K 2–5"),
   brief('<b>SZVETI:</b> Megvan a híd. Most jöhet a Void egy zónája. <b>Nagol:</b> Vigyázat: ha a görbe a tengely '
         'alá bukik, a határozott integrál kevesebbet mutat, mint amennyit ki kell vágni.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B3
B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> A Void egy zónáját kell kivágni a valóságból — pontosan akkorát, amekkora a görbék közötti '
         'terület. SZVETI számol, Vilmos rajzol. <b>Véd Vilmos:</b> És a rajzon az is látszik, hogy ez a kabát jól '
         'áll. <b>SZVETI:</b> Nem.'),
 ]),

 ("Görbe vonalú trapéz", [
   r'<p class="lead">Ha $f\ge0$ az $[a;\,b]$-n, a grafikon, az $x$ tengely és az $x=a$, $x=b$ egyenesek által '
   r'határolt síkidom területe $$T=\int_a^b f(x)\,dx.$$</p>',
   doboz("pelda", "I.V.H. Akták — terület a görbe alatt",
         r'<p>Az $f(x)=\frac{x^2}{2}+2$ a $[-1;\,2]$-n pozitív (sőt mindenütt), ezért '
         r'$$T=\int_{-1}^{2}\left(\frac{x^2}{2}+2\right)dx=\left[\frac{x^3}{6}+2x\right]_{-1}^{2}='
         r'\left(\frac86+4\right)-\left(-\frac16-2\right)=\frac{15}{2}.$$</p>', hid="pelda-gorbe-alatti"),
   abra(SVG_B3_TRAPEZ, 'A kiemelt terület $\\frac{15}{2}=7{,}5$ egység.'),
 ]),

 ("Ha a görbe a tengely alá bukik", [
   doboz("tetel", "Terület előjelváltásnál",
         r'<p>Ha $f\le0$ az $[a;\,b]$-n, a terület $T=\left\lvert\int_a^b f(x)\,dx\right\rvert$. Ha $f$ az intervallumon '
         r'<b>előjelet vált</b>, a zérushelyeinél <b>részekre bontunk</b>, és a részintegrálok abszolút értékét adjuk '
         r'össze: $$T=\left\lvert\int_a^c f(x)\,dx\right\rvert+\left\lvert\int_c^b f(x)\,dx\right\rvert,$$ ahol $c$ a '
         r'zérushely.</p>', hid="tetel-elojelvaltas"),
   doboz("pelda", "I.V.H. Akták — bontás a zérushelynél",
         r'<p>Az $f(x)=x^2-4x=x(x-4)$ és az $x$ tengely közötti terület a $[0;\,5]$-ön. A zérushelyek $0$ és $4$: a '
         r'$[0;\,4]$-en $f\le0$, a $[4;\,5]$-ön $f\ge0$.</p>'
         r'<p>$\int_0^4(x^2-4x)\,dx=\left[\frac{x^3}{3}-2x^2\right]_0^4=\frac{64}{3}-32=-\frac{32}{3}$, '
         r'$\;\int_4^5(x^2-4x)\,dx=\left(\frac{125}{3}-50\right)-\left(-\frac{32}{3}\right)=\frac73$.</p>'
         r'<p>$$T=\frac{32}{3}+\frac73=13.$$ Ha nem bontanánk: $\int_0^5(x^2-4x)\,dx=-\frac{25}{3}$ — ez nem terület.</p>'),
   abra(SVG_B3_ELOJEL, 'Piros: a tengely alatti rész ($\\frac{32}{3}$), zöld: a fölötti ($\\frac73$).'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„Kiszámolom egyben, és veszem az abszolút értékét.” — Ha a függvény előjelet vált, a pozitív és a '
         r'negatív rész <b>kiegyenlíti</b> egymást, és kevesebbet kapsz: itt $\frac{25}{3}$-ot $13$ helyett. Először '
         r'mindig a zérushelyeket keresd meg!</p>'),
   kviz(r'Az $f$ az $[a;\,b]$ intervallumon előjelet vált. Helyes-e a $T=\left\lvert\int_a^b f(x)\,dx\right\rvert$ képlet a '
        r'grafikon és az $x$ tengely közötti területre?',
        [r'nem: a zérushelynél bontani kell, és a részek abszolút értékét összeadni', r'igen, mindig',
         r'csak akkor, ha $f$ polinom', r'igen, ha $b\gt a$'], 0,
        jo="✔ Egyben integrálva a pozitív és a negatív részek kiegyenlítik egymást — a terület ennél nagyobb.",
        nem="✘ Az abszolút érték csak a végeredményen nem segít: a részek előbb kioltják egymást. Bonts a zérushelynél!"),
 ]),

 ("Görbe és a két tengely", [
   r'<p class="lead">Ha a síkidomot a görbe, az $x$ és az $y$ tengely határolja, az egyik határ az $y$ tengely '
   r'($x=0$), a másik a görbe <b>zérushelye</b> — ezt nekünk kell kiszámolni.</p>',
   doboz("pelda", "I.V.H. Akták — a két tengely között",
         r'<p>Az $f(x)=8-2x^2$ grafikonja, az $x$ és az $y$ tengely az első síknegyedben zár be egy síkidomot. A '
         r'zérushely: $8-2x^2=0\Rightarrow x=2$ (a $-2$ a másik síknegyedben van). A $[0;\,2]$-n $f\ge0$, ezért '
         r'$$T=\int_0^2(8-2x^2)\,dx=\left[8x-\frac{2x^3}{3}\right]_0^2=16-\frac{16}{3}=\frac{32}{3}.$$</p>',
         hid="pelda-ket-tengely"),
   abra(SVG_B3_TENGELYEK, 'A kiemelt síkidomot a görbe és a két tengely határolja.'),
 ]),

 ("Két görbe közötti terület", [
   doboz("tetel", "Terület két görbe között",
         r'<p>Ha az $[a;\,b]$-n $f(x)\ge g(x)$, a két grafikon közötti síkidom területe '
         r'$$T=\int_a^b\big(f(x)-g(x)\big)\,dx\quad(\text{a felső mínusz az alsó}).$$</p>'
         r'<p><b>Lépések:</b> 1. a metszéspontok: $f(x)=g(x)$; 2. melyik van felül — egy próbapont a metszéspontok '
         r'között; 3. az integrál a metszéspontok között.</p>', hid="tetel-ket-gorbe"),
   doboz("pelda", "I.V.H. Akták — parabola és egyenes",
         r'<p>Az $f(x)=x^2$ és a $g(x)=x+2$ közötti terület.</p>'
         r'<p><b>1.</b> $x^2=x+2\Rightarrow x^2-x-2=0\Rightarrow x=-1$ vagy $x=2$.</p>'
         r'<p><b>2.</b> Próbapont: $x=0$-ban $g(0)=2\gt f(0)=0$, tehát az egyenes van felül.</p>'
         r'<p><b>3.</b> $$T=\int_{-1}^{2}\big(x+2-x^2\big)\,dx=\left[\frac{x^2}{2}+2x-\frac{x^3}{3}\right]_{-1}^{2}='
         r'\frac{10}{3}-\left(-\frac76\right)=\frac92.$$</p>', hid="pelda-ket-gorbe"),
   abra(SVG_B3_KET, 'Fekete: $f(x)=x^2$, kék: $g(x)=x+2$. A két metszéspont $(-1;\\,1)$ és $(2;\\,4)$; a köztük lévő terület $\\frac92$.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>„Mindegy, melyiket vonom ki.” — Ha az alsóból vonod ki a felsőt, negatív „területet” kapsz. Mindig a '
         r'<b>felső mínusz az alsó</b> — ha nem tudod, melyik van felül, egy próbapont eldönti.</p>'),
   kviz(r'Az $f(x)=x^2$ és a $g(x)=x+2$ közül melyik van felül a $[-1;\,2]$-n?',
        [r'a $g$, mert például $g(0)=2\gt f(0)=0$', r'az $f$, mert négyzetes függvény', r'mindegy, az integrál '
         r'úgyis ugyanaz', r'egyik sem, mert metszik egymást'], 0,
        jo="✔ Egy próbapont a metszéspontok között eldönti: 0-ban az egyenes 2, a parabola 0.",
        nem="✘ Nem a függvény típusa dönt: helyettesíts egy pontot a metszéspontok közé (például 0-t). Ott g(0) = 2, "
            "f(0) = 0, tehát g van felül."),
   NEHEZ(1, 4, "két görbe közötti és a két tengely által határolt területek"),
   doboz("erdekesseg", "Munka mint terület",
         r'<p>Állandó erő munkája erő szorozva úttal. Ha az erő változik — például egy rugó annál erősebben húz, minél '
         r'jobban megnyújtjuk —, a munka az erő–út grafikon alatti terület: $W=\int_{s_1}^{s_2}F(s)\,ds$. A rugónál '
         r'$F=D\cdot s$, és $W=\frac12Ds^2$.</p>', hid="erdekesseg-munka"),
   GY(FB + "#alap-8", "A 8–10", FB + "#kozep-6", "K 6–12"),
 ]),

 ("🧾 Gyorsismétlő", [
   TABLA(["", ""], [
       ["<b>primitív függvény</b>", "$F'=f$; minden primitív függvény $F+C$ alakú"],
       ["<b>határozatlan integrál</b>", "$\\int f(x)\\,dx=F(x)+C$ — ellenőrzés deriválással"],
       ["<b>táblázat</b>", "$\\int x^n\\,dx=\\frac{x^{n+1}}{n+1}+C$ $(n\\ne-1)$, $\\int\\frac1x\\,dx=\\ln\\lvert x\\rvert+C$, "
                           "$\\int e^x\\,dx=e^x+C$ — a teljes táblázat: "
                           "<a href=\"tananyag-integraltablazat.html#tetel-integraltablazat\">A2</a>"],
       ["<b>helyettesítés</b>", "$\\int f(ax+b)\\,dx=\\frac1aF(ax+b)+C$, $\\int\\frac{f'}{f}=\\ln\\lvert f\\rvert+C$, "
                                "$t=g(x)$, $dt=g'(x)\\,dx$"],
       ["<b>Newton–Leibniz</b>", "$\\int_a^b f(x)\\,dx=F(b)-F(a)$ — a határozott integrál előjeles szám"],
       ["<b>terület</b>", "$f\\ge0$: $\\int_a^b f$; előjelváltásnál bontás a zérushelyeken; két görbe: "
                          "$\\int_a^b(\\text{felső}-\\text{alsó})$"]]),
   brief('<b>SZVETI:</b> A zóna kivágva, a darabjaim a helyükön. Majdnem. <b>Véd Vilmos:</b> Maradt egy darab! '
         '<b>SZVETI:</b> Az a te kabátod. <b>Nagol:</b> Összeraktuk a valóságot — de a Multiverzumban nem csak egy '
         'változata létezik. A következő fejezetben <b>Nyalka Vili</b> azt számolja meg, hányféleképpen rakhatók össze '
         'a darabok: <i>Multiverzum Lottó</i>.', outro=True),
 ]),
]


# ---------------------------------------------------------------- oldalak
def _prim(szakaszok):
    """A nyers stringekben a \\' (KaTeX-ben ékezet!) helyett sima vessző-prím: f\\'(x) → f'(x)."""
    return [(h2, [b.replace("\\'", "'") for b in blokkok]) for h2, blokkok in szakaszok]


B1, B2, B3 = (_prim(z) for z in (B1, B2, B3))
lapok = [
 lap(**T, fajl="tananyag-hatarozott-integral.html",
     cim="Bezárva [a; b]-be — a határozott integrál",
     alcim="A területprobléma, alsó és felső közelítő összeg, a határozott integrál fogalma és az előjeles terület.",
     chip=KUL + " · 4/6", szakaszok=B1,
     elozo=("tananyag-helyettesites.html", "Helyettesítéses integrálás"),
     kovetkezo=("tananyag-newton-leibniz.html", "A Newton–Leibniz-formula")),
 lap(**T, fajl="tananyag-newton-leibniz.html",
     cim="A híd — a Newton–Leibniz-formula",
     alcim="A formula és szemléletes indoklása, számolás vele, a határozott integrál tulajdonságai és a helyettesítés "
           "a határok átírásával.",
     chip=KUL + " · 5/6", szakaszok=B2,
     elozo=("tananyag-hatarozott-integral.html", "A határozott integrál"),
     kovetkezo=("tananyag-terulet.html", "Síkidomok területe")),
 lap(**T, fajl="tananyag-terulet.html",
     cim="A Void kivágása — síkidomok területe",
     alcim="Görbe vonalú trapéz, a tengely alatti rész és az előjelváltás, a görbe és a két tengely, két görbe közötti "
           "terület — és a témakör gyorsismétlője.",
     chip=KUL + " · 6/6", szakaszok=B3,
     elozo=("tananyag-newton-leibniz.html", "A Newton–Leibniz-formula"),
     kovetkezo=("feladatok-hatarozatlan-integral.html", "Zsoldos-lista I. — Határozatlan integrál")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
