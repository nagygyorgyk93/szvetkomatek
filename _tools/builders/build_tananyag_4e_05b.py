# -*- coding: utf-8 -*-
"""4e/05 — B blokk: a Pascal-haromszog es a binomialis tetel (B1) + 🧾 Gyorsismetlo.
Mentor: Nyalka Vili & Nagol (Ved Vilmos kommental). Kuldetes: Multiverzum Lotto.
Specifikacio: projektek/szvetkomatek/4e/narrativa_05-kombinatorika.md
Tiltott adatok: a 26/27-es 4. ellenorzo binomialis kifejtesei (tiltott_4e_05.py) — lent ellenorizve."""
import sys, os
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, svg_pascal, pascal_kifejtes
import tiltott
TILT = tiltott.modul("tiltott_4e_05")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)
import sympy

T = dict(tagozat="4e", mappa="05-kombinatorika", temakor="Kombinatorika")
KUL = "Multiverzum Lottó"
FA = "feladatok-kombinatorika.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(FA + k_h, k_c, FA + n_h, n_c, tagozat="4e")


def NEHEZ(n, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FA}#nehez-{n}">Zsoldos-lista, nehéz {n}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table"><tr>{th}</tr>{tr}</table></div>'


# ---------------------------------------------------------------- önteszt (sympy)
E = []
x, a, b = sympy.symbols("x a b")


def kif(kifejezes, vart):
    if sympy.expand(kifejezes - vart) != 0:
        E.append((str(kifejezes), str(vart)))


kif((a + b) ** 2, a**2 + 2*a*b + b**2)
kif((a + b) ** 3, a**3 + 3*a**2*b + 3*a*b**2 + b**3)
kif((x - 2) ** 3, x**3 - 6*x**2 + 12*x - 8)
kif((2*x + 1) ** 4, 16*x**4 + 32*x**3 + 24*x**2 + 8*x + 1)
kif((x + 1) ** 3, x**3 + 3*x**2 + 3*x + 1)
if sympy.Poly((x + 2) ** 6, x).coeff_monomial(x**3) != 160:
    E.append("x^3 (x+2)^6")
if sympy.expand(comb(5, 2) * x**3 * 3**2) != 90 * x**3 or sympy.Poly((x + 3) ** 5, x).coeff_monomial(x**3) != 90:
    E.append("T3 (x+3)^5")
if sympy.Poly((x + 2) ** 3, x).coeff_monomial(x**2) != 6:
    E.append("x^2 (x+2)^3")
if [sum(comb(n, k) for k in range(n + 1)) for n in range(8)] != [2 ** n for n in range(8)]:
    E.append("sorösszeg")
if pascal_kifejtes(3) != "a³ + 3a²b + 3ab² + b³":
    E.append("pascal_kifejtes")
if comb(5, 0) + comb(5, 1) + comb(5, 2) + comb(5, 3) + comb(5, 4) + comb(5, 5) != 32:
    E.append("32 részhalmaz")
E += TILT.ellenoriz([("binom", (-2, 3)), ("binom", (2, 6)), ("binom", (3, 5)), ("binom", (1, 3)), ("binom", (2, 3))])
assert not E, E
print("önteszt: OK")

SVG_PASCAL = svg_pascal(
    n_max=7, kezdo=4,
    felirat="Mozgasd a csúszkát! A kiemelt $n$-edik sor az $(a+b)^n$ kifejtésének együtthatói; alatta a kifejtés és a "
            "sor összege.",
    leiras="Interaktív Pascal-háromszög: a 0–7. sor; a csúszka kiemeli az n-edik sort, és kiírja az (a + b) n-edik "
           "hatványának kifejtését")

B1 = [
 ("📡 Küldetés-eligazítás", [
   brief((
             '<b>Nyalka Vili:</b> Az I.V.H.-archívumban ezt a háromszöget találtam: a két szélen 1 áll, minden '
             'belső szám a fölötte álló kettő összege. Blaise Pascal a szerencsejátékok kérdéseihez is használta; '
             'a háromszöget már jóval előtte ismerték. <b>Véd Vilmos:</b> Tudom, mire jó! 🌮 <i>Burek-matek:</i> '
             '$(a+b)^2=a^2+b^2$. <b>Nagol:</b> A középső tagot, a $2ab$-t a multiverzum nem bocsátja meg. Ez a '
             'háromszög pontosan megmondja, mi hiányzik.'
         )),
 ]),
 ("A Pascal-háromszög", [
   '<p class="lead">A háromszög csúcsán és minden sor két szélén 1 áll; minden más szám a <b>fölötte álló két szám '
   'összege</b>. Mozgasd a csúszkát: a kiemelt sor számai egy hatvány együtthatói lesznek.</p>',
   SVG_PASCAL,
   doboz("tetel", "A Pascal-háromszög és a kombinációk",
         r'<p>Az $n$-edik sor (a csúcs a 0. sor) elemei balról jobbra $$\binom n0,\ \binom n1,\ \binom n2,\ \ldots,\ '
         r'\binom nn.$$ Az építési szabály: $\binom nk+\binom n{k+1}=\binom{n+1}{k+1}$; a sorok szimmetrikusak: '
         r'$\binom nk=\binom n{n-k}$ (<a href="tananyag-kombinaciok.html#tetel-szimmetria">A4</a>).</p>',
         hid="tetel-pascal"),
   r'<p>Nézd meg a sorok összegét: $1,\ 2,\ 4,\ 8,\ 16,\ \ldots$ — minden sorban kétszer annyi, mint az előzőben, az '
   r'$n$-edik sor összege tehát $2^n$. Ezt a mintát most megfigyeltük; hogy miért igaz, azt a lap végén látjuk.</p>',
 ]),
 ("Kifejtjük: $(a+b)^n$", [
   r'<p class="lead">Szorozzuk ki: $$(a+b)^2=a^2+2ab+b^2,\qquad (a+b)^3=(a+b)^2(a+b)=a^3+3a^2b+3ab^2+b^3.$$ Az '
   r'együtthatók $1,\,2,\,1$ és $1,\,3,\,3,\,1$ — a Pascal-háromszög 2. és 3. sora. Az $a$ kitevője tagról tagra eggyel '
   r'csökken, a $b$-é eggyel nő, és minden tagban a két kitevő összege $n$.</p>',
   doboz("tetel", "A binomiális tétel",
         r'<p>Ha $n$ nemnegatív egész, akkor $$(a+b)^n=\sum_{k=0}^{n}\binom nk a^{n-k}b^k.$$ '
         r'A formális összegnek $n+1$ tagja van; összevonás után kevesebb '
         r'is maradhat. Az együtthatók a Pascal-háromszög $n$-edik sorának elemei, a <b>binomiális '
         r'együtthatók</b>. A tételt bizonyítás nélkül használjuk.</p>', hid="tetel-binomialis"),
   doboz("pelda", "I.V.H. Akták — két kifejtés",
         r'<p>$(x-2)^3$: itt $a=x$, $b=-2$, az együtthatók $1,3,3,1$: '
         r'$$(x-2)^3=x^3+3x^2(-2)+3x(-2)^2+(-2)^3=x^3-6x^2+12x-8.$$</p>'
         r'<p>$(2x+1)^4$: az együtthatók $1,4,6,4,1$, és az $a=2x$ minden hatványát ki kell számolni: '
         r'$$(2x+1)^4=(2x)^4+4(2x)^3+6(2x)^2+4\cdot2x+1=16x^4+32x^3+24x^2+8x+1.$$</p>', hid="pelda-kifejtes"),
   doboz("csapda", "Véd Vilmos csapda — ami a zárójelben van, az mind hatványra emelődik",
         r'<p>Vilmos szerint $(a+b)^2=a^2+b^2$ — elhagyta a középső tagot. Két további tipikus hiba: $(2x)^3=2x^3$ '
         r'(helyesen $8x^3$, mert a 2 is a harmadikra emelődik), és az előjel az $(a-b)^n$-nél: a $b=-2$ páratlan '
         r'kitevőn negatív, páros kitevőn pozitív, ezért az előjelek váltakoznak.</p>'),
   kviz('Hány tagja van az $(x+1)^3$ kifejtésének?', ['$4$', '$3$', '$2$', '$6$'], 0,
        jo="✔ $x^3+3x^2+3x+1$ — az $n$-edik hatványnak $n+1=4$ tagja van.",
        nem="✘ Az $n$-edik hatvány kifejtésében $n+1$ tag van: $(x+1)^3=x^3+3x^2+3x+1$."),
 ]),
 ("Egy tag, egy együttható", [
   '<p class="lead">Gyakran nem kell a teljes kifejtés, csak egyetlen tag. A binomiális tételből leolvasható:</p>',
   doboz("tetel", "A $(k+1)$-edik tag",
         r'<p>$$T_{k+1}=\binom nk\,a^{n-k}\,b^k\qquad(k=0,1,\ldots,n).$$ A $k$ a $b$ kitevője — és eggyel kevesebb, mint '
         r'a tag sorszáma.</p>', hid="tetel-altalanos-tag"),
   doboz("pelda", "I.V.H. Akták — egy együttható",
         r'<p>Mi az $x^3$ együtthatója az $(x+2)^6$ kifejtésében?</p>'
         r'<p>Az $x$ kitevője $n-k=3$, tehát $k=3$: $\binom63x^3\cdot2^3=20\cdot8\,x^3=160x^3$. Az együttható $160$.</p>'
         r'<p>Mi az $(x+3)^5$ kifejtésének 3. tagja? Itt $k=2$: $T_3=\binom52x^3\cdot3^2=10\cdot9\,x^3=90x^3$.</p>',
         hid="pelda-egyutthato"),
   kviz('Mi az $x^2$ együtthatója az $(x+2)^3$ kifejtésében?', ['$6$', '$3$', '$12$', '$8$'], 0,
        jo="✔ $\\binom31x^2\\cdot2^1=6x^2$.",
        nem="✘ A $b=2$ is hatványra emelődik: $\\binom31x^2\\cdot2=6x^2$. A 3 csak a binomiális együttható."),
   doboz("erdekesseg", "Miért $2^n$ a sor összege?",
         r'<p>Írjuk be a binomiális tételbe az $a=b=1$ értéket: $$2^n=(1+1)^n=\binom n0+\binom n1+\ldots+\binom nn.$$ A '
         r'jobb oldal megszámolja, hány 0, 1, 2, …, $n$ elemű részhalmaza van egy $n$ elemű halmaznak — vagyis egy $n$ '
         r'elemű halmaznak <b>összesen $2^n$ részhalmaza</b> van. Egy ötfős társaságból tehát $2^5=32$-féle csoport '
         r'választható, az üreset és a teljeset is beleértve.</p>', hid="erdekesseg-reszhalmazok"),
   NEHEZ(4, "a kifejtésnek az a tagja, amelyben nem szerepel $x$"),
   GY("#alap-13", "A 13–14", "#kozep-11", "K 11–12"),
 ]),
 ("🧾 Gyorsismétlő", [
   TABLA(["kérdés", "eszköz", "képlet"], [
       ["egymás utáni döntések (ÉS)", "szorzási szabály", "$n_1\\cdot n_2\\cdot\\ldots\\cdot n_k$"],
       ["egymást kizáró esetek (VAGY)", "összeadási szabály", "$n_1+n_2+\\ldots+n_k$"],
       ["„legalább egy”", "komplementer", "összes − rossz"],
       ["mind az $n$ elemet sorba", "permutáció", "$P_n=n!$"],
       ["sorba, egyforma elemekkel", "ismétléses permutáció", "$\\dfrac{n!}{k_1!\\,k_2!\\cdots k_r!}$"],
       ["$k$ elemet, sorrendben", "variáció", "$V_n^k=\\dfrac{n!}{(n-k)!}$"],
       ["$k$-szor, ismétlődhet", "ismétléses variáció", "$V_n^{k,i}=n^k$"],
       ["$k$ elemet, csoportba", "kombináció", "$\\binom nk=\\dfrac{n!}{k!\\,(n-k)!}$"],
       ["$(a+b)^n$", "binomiális tétel", "$T_{k+1}=\\binom nk a^{n-k}b^k$"]]),
   brief('<b>Nyalka Vili:</b> Megszámoltunk mindent: szetteket, sorrendeket, dobogókat, csapatokat. <b>Mr. Szürreál</b> '
         '(I.V.H.): Megszámolni könnyű. A kérdés az, <i>mekkora az esélye</i>, hogy a kadétok túlélik az érettségit. A '
         'statisztikám szerint csekély. <b>Véd Vilmos:</b> Azt majd meglátjuk. A következő fejezet: <i>A Túlélés '
         'Esélyei</i>.', outro=True),
 ]),
]

u = lap(**T, fajl="tananyag-binomialis-tetel.html",
        cim="A Pascal-háromszög és a binomiális tétel",
        alcim="A háromszög építési szabálya, az $(a+b)^n$ kifejtése, egy tag és egy együttható — és a témakör "
              "gyorsismétlője.",
        chip=KUL + " · 5/5", szakaszok=B1,
        elozo=("tananyag-kombinaciok.html", "Kombinációk"),
        kovetkezo=(FA, "Zsoldos-lista — Kombinatorika"))
print("✓", os.path.relpath(u))
