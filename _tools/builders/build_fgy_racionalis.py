# -*- coding: utf-8 -*-
"""1e/06 — Racionális algebrai kifejezések KÖZÖS feladatgyűjtemény (Shuri & Iron Man, „A Hatalom Nyelve").
Egy drill-deck a teljes témakörre. Végeredmény = KIZÁRÓLAG a végső válasz, levezetés nélkül."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, w

DEST = glob.glob("/sessions/*/mnt/Claude/web/1e/06-racionalis-algebrai-kifejezesek")[0]

# ===================== numerikus / szimbolikus önellenőrzés =====================
import sympy as sp
from sympy import symbols, expand, factor, cancel, div, sqrt
x,y,z,a,b,c,m,n,p,q,r,t,u,v = symbols('x y z a b c m n p q r t u v')

def eq(lhs, rhs): assert sp.simplify(lhs-rhs)==0, f"HIBA: {lhs} != {rhs}"
# Alap
eq(expand((x+4)**2), x**2+8*x+16); eq(expand((a-3)**2), a**2-6*a+9)
eq(expand((2*x+1)**2), 4*x**2+4*x+1); eq(expand((x-5)*(x+5)), x**2-25)
eq(expand((x+1)**3), x**3+3*x**2+3*x+1); eq(expand((a-2)**3), a**3-6*a**2+12*a-8)
eq(expand((x+3)*(x+5)), x**2+8*x+15); eq(expand((x-2)*(x+7)), x**2+5*x-14); eq(expand((2*x-1)*(x+4)), 2*x**2+7*x-4)
eq(expand((x+2)**2-(x-1)*(x+1)), 4*x+5); eq(expand(3*x-(2*x**2-x+4)+2*x**2), 4*x-4)
eq(factor(6*x+9), 3*(2*x+3)); eq(factor(4*a**2-8*a), 4*a*(a-2)); eq(factor(15*x**3-10*x**2), 5*x**2*(3*x-2))
eq(factor(x**2-9), (x-3)*(x+3)); eq(factor(4*x**2-25), (2*x-5)*(2*x+5)); eq(factor(49-y**2), (7-y)*(7+y))
eq(factor(x**2+6*x+9),(x+3)**2); eq(factor(x**2-10*x+25),(x-5)**2); eq(factor(4*x**2+4*x+1),(2*x+1)**2)
eq(cancel((6*x**2)/(3*x)), 2*x); eq(cancel((x**2-x)/x), x-1); eq(cancel((5*a+10)/5), a+2)
# Közép
eq(expand((2*a-3*b)**2), 4*a**2-12*a*b+9*b**2); eq(expand((x**2+1)**2), x**4+2*x**2+1)
eq(expand((x-2)**3+(x+2)**3), 2*x**3+24*x); eq(expand((2*x-1)**2-(x+3)*(x-3)), 3*x**2-4*x+10)
Qk,Rk=div(x**3-2*x**2+3*x-5, x-1, x); eq(Qk, x**2-x+2); assert Rk==-3
assert (x**3+2*x**2-x+4).subs(x,2)==18 and (2*x**3-3*x+1).subs(x,-1)==2
eq(factor(x**3-8), (x-2)*(x**2+2*x+4)); eq(factor(a**3+27), (a+3)*(a**2-3*a+9)); eq(factor(8*x**3-1),(2*x-1)*(4*x**2+2*x+1))
eq(factor(x**3+x**2+x+1),(x+1)*(x**2+1)); eq(factor(a*x+a*y+b*x+b*y),(a+b)*(x+y)); eq(factor(2*x**3-x**2+2*x-1),(2*x-1)*(x**2+1))
eq(cancel((x**2-9)/(x-3)), x+3); eq(cancel((x**2-4)/(x**2+4*x+4)), (x-2)/(x+2)); eq(cancel((a**2-a*b)/(a**2-b**2)), a/(a+b))
eq(cancel(1/x+1/(x+1)), (2*x+1)/(x*(x+1))); eq(cancel(2/(a-1)-3/(a+1)), (5-a)/(a**2-1)); eq(cancel(1/(x-2)+x/(x**2-4)), (2*x+2)/(x**2-4))
eq(cancel((x**2-1)/x*(x/(x+1))), x-1); eq(cancel(((a**2-b**2)/(a+b))/((a-b)/2)), 2)
# Nehéz
eq(cancel(((x**2-y**2)/(x**2+2*x*y+y**2))*((x+y)/(x-y))), 1)
eq(cancel(1/(a-1)-1/(a+1)+2/(a**2-1)), 4/(a**2-1))
eq(cancel((1/(x-y)+1/(x+y))*((x**2-y**2)/2)), x)
eq(factor(x**4-16), (x-2)*(x+2)*(x**2+4)); eq(factor(x**4-1),(x-1)*(x+1)*(x**2+1)); eq(factor(a**3-a), a*(a-1)*(a+1))
assert sp.solve((x**3+m*x**2-4).subs(x,2), m)==[-1]
eq(cancel((x/y-y/x)/(1/y+1/x)), x-y)
eq(expand((a+b)**2-(a-b)**2), 4*a*b); eq(expand((a+b)**2+(a-b)**2), 2*a**2+2*b**2)
# LKO/LKT: A=x²−x=x(x−1), B=x²−1=(x−1)(x+1) -> LKO=(x−1), LKT=x(x−1)(x+1)
eq(sp.gcd(x**2-x, x**2-1), x-1); eq(sp.lcm(x**2-x, x**2-1), x*(x-1)*(x+1))
# Joker
eq(cancel((x**2+x)/(x+1)), x)
# Gyakorló ellenőrző
eq(expand((2*x-1)**2-(x-3)*(x+2)), 3*x**2-3*x+7)
eq(factor(x**3-27),(x-3)*(x**2+3*x+9)); eq(factor(a*x-a*y+b*x-b*y),(a+b)*(x-y))
assert (x**3-2*x**2+4*x-3).subs(x,1)==0
eq(cancel((x**2-25)/(x+5)), x-5); eq(cancel(1/(x-1)+1/(x+1)), 2*x/(x**2-1))
eq(cancel((a**2-b**2)/a*(a/(a-b))), a+b)
Qg,Rg=div(x**3+3*x**2-4, x+2, x); eq(Qg, x**2+x-2); assert Rg==0
eq(cancel((x**2-4)/(x-2)), x+2); assert (x+2).subs(x,3)==5
# Gyakorló otthoni
eq(expand((a+5)**2), a**2+10*a+25); eq(expand((3*x-2)*(3*x+2)), 9*x**2-4); eq(expand(2*x*(x**2-3*x+1)),2*x**3-6*x**2+2*x)
eq(factor(12*a**2-18*a), 6*a*(2*a-3)); eq(factor(4*x**2-9),(2*x-3)*(2*x+3)); eq(factor(x**2-12*x+36),(x-6)**2)
eq(expand((x+3)**2+(x-3)**2), 2*x**2+18); assert (2*x**3+x-5).subs(x,1)==-2
eq(cancel((a**2-a*b)/(a**2-b**2)), a/(a+b)); eq(cancel(3/x-1/(x+2)), (2*x+6)/(x*(x+2)))
print("MINDEN ASSERT OK")

# =============================== ALAP (12) ===============================
ALAP = [
 ("Vonj össze (egynemű tagok)!",
  ["$5a+8a-3a$","$7x^2-2x^2+x^2$","$4ab+9ab-ab$","$2y^3+5y^3-4y^3$"],
  "a) $10a$; b) $6x^2$; c) $12ab$; d) $3y^3$.", True),
 ("Végezd el a szorzást (egytag $\\cdot$ polinom)!",
  ["$3x(2x-5)$","$-2a(a+4)$","$4(3x^2-2x+1)$","$x^2(x-7)$"],
  "a) $6x^2-15x$; b) $-2a^2-8a$; c) $12x^2-8x+4$; d) $x^3-7x^2$.", True),
 ("Alkalmazd a nevezetes azonosságot!",
  ["$(x+4)^2$","$(a-3)^2$","$(2x+1)^2$","$(x-5)(x+5)$"],
  "a) $x^2+8x+16$; b) $a^2-6a+9$; c) $4x^2+4x+1$; d) $x^2-25$.", True),
 ("Számítsd ki a köböt!",
  ["$(x+1)^3$","$(a-2)^3$"],
  ["$x^3+3x^2+3x+1$","$a^3-6a^2+12a-8$"]),
 ("Szorozd össze a polinomokat!",
  ["$(x+3)(x+5)$","$(x-2)(x+7)$","$(2x-1)(x+4)$"],
  ["$x^2+8x+15$","$x^2+5x-14$","$2x^2+7x-4$"]),
 ("Írd fel kanonikus (rendezett) alakban!",
  ["$(x+2)^2-(x-1)(x+1)$","$3x-(2x^2-x+4)+2x^2$"],
  ["$4x+5$","$4x-4$"]),
 ("Emeld ki a közös tényezőt!",
  ["$6x+9$","$4a^2-8a$","$15x^3-10x^2$","$3ab+6a$"],
  "a) $3(2x+3)$; b) $4a(a-2)$; c) $5x^2(3x-2)$; d) $3a(b+2)$.", True),
 ("Bontsd tényezőkre (négyzetek különbsége)!",
  ["$x^2-9$","$4x^2-25$","$a^2-1$","$49-y^2$"],
  "a) $(x-3)(x+3)$; b) $(2x-5)(2x+5)$; c) $(a-1)(a+1)$; d) $(7-y)(7+y)$.", True),
 ("Ismerd fel a teljes négyzetet, és bontsd fel!",
  ["$x^2+6x+9$","$x^2-10x+25$","$4x^2+4x+1$"],
  "a) $(x+3)^2$; b) $(x-5)^2$; c) $(2x+1)^2$.", True),
 ("Egyszerűsítsd a törtet!",
  ["$\\dfrac{6x^2}{3x}$","$\\dfrac{x^2-x}{x}$","$\\dfrac{5a+10}{5}$"],
  ["$2x$","$x-1$","$a+2$"]),
 ("Mely értékekre értelmezett a kifejezés (nevező $\\neq 0$)?",
  ["$\\dfrac{1}{x}$","$\\dfrac{1}{x-3}$","$\\dfrac{5}{x+2}$","$\\dfrac{x}{(x-1)(x+4)}$"],
  "a) $x\\neq 0$; b) $x\\neq 3$; c) $x\\neq -2$; d) $x\\neq 1$ és $x\\neq -4$.", True),
 ("Végezd el a törtek szorzását, osztását!",
  ["$\\dfrac{2}{x}\\cdot\\dfrac{x}{5}$","$\\dfrac{a}{b}\\cdot\\dfrac{b}{a}$","$\\dfrac{3}{x}:\\dfrac{6}{x^2}$","$\\dfrac{x}{2}:\\dfrac{x}{4}$"],
  "a) $\\dfrac{2}{5}$; b) $1$; c) $\\dfrac{x}{2}$; d) $2$.", True),
]

# =============================== KÖZÉP (9) ===============================
KOZEP = [
 ("Alkalmazd a nevezetes azonosságokat!",
  ["$(2a-3b)^2$","$(x^2+1)^2$","$(3-x)(3+x)$"],
  ["$4a^2-12ab+9b^2$","$x^4+2x^2+1$","$9-x^2$"]),
 ("Írd fel kanonikus alakban!",
  ["$(x-2)^3+(x+2)^3$","$(2x-1)^2-(x+3)(x-3)$"],
  ["$2x^3+24x$","$3x^2-4x+10$"]),
 ("Végezd el a polinomosztást (add meg a hányadost és a maradékot)!",
  None, "$(x^3-2x^2+3x-5):(x-1)=x^2-x+2$, a maradék $-3$."),
 ("A Bézout-tétellel add meg az osztási maradékot!",
  ["$P(x)=x^3+2x^2-x+4$, osztó $x-2$","$P(x)=2x^3-3x+1$, osztó $x+1$"],
  ["$18$","$2$"]),
 ("Bontsd tényezőkre (köbök összege/különbsége)!",
  ["$x^3-8$","$a^3+27$","$8x^3-1$"],
  ["$(x-2)(x^2+2x+4)$","$(a+3)(a^2-3a+9)$","$(2x-1)(4x^2+2x+1)$"]),
 ("Bontsd tényezőkre csoportosítással!",
  ["$x^3+x^2+x+1$","$ax+ay+bx+by$","$2x^3-x^2+2x-1$"],
  ["$(x+1)(x^2+1)$","$(a+b)(x+y)$","$(2x-1)(x^2+1)$"]),
 ("Egyszerűsítsd a törtet, és add meg az értelmezési tartományát!",
  ["$\\dfrac{x^2-9}{x-3}$","$\\dfrac{x^2-4}{x^2+4x+4}$","$\\dfrac{a^2-ab}{a^2-b^2}$"],
  ["$x+3$, ÉT: $x\\neq 3$","$\\dfrac{x-2}{x+2}$, ÉT: $x\\neq -2$","$\\dfrac{a}{a+b}$, ÉT: $a\\neq \\pm b$"]),
 ("Add össze, illetve vond ki a törteket!",
  ["$\\dfrac{1}{x}+\\dfrac{1}{x+1}$","$\\dfrac{2}{a-1}-\\dfrac{3}{a+1}$","$\\dfrac{1}{x-2}+\\dfrac{x}{x^2-4}$"],
  ["$\\dfrac{2x+1}{x(x+1)}$","$\\dfrac{5-a}{a^2-1}$","$\\dfrac{2x+2}{x^2-4}$"]),
 ("Végezd el a törtek szorzását, osztását (egyszerűsíts)!",
  ["$\\dfrac{x^2-1}{x}\\cdot\\dfrac{x}{x+1}$","$\\dfrac{a^2-b^2}{a+b}:\\dfrac{a-b}{2}$"],
  ["$x-1$","$2$"]),
]

# =============================== NEHÉZ (8) ===============================
NEHEZ = [
 ("Egyszerűsítsd az összetett kifejezést!",
  None, "$\\dfrac{x^2-y^2}{x^2+2xy+y^2}\\cdot\\dfrac{x+y}{x-y}=1$."),
 ("Vond össze egyetlen törtté!",
  None, "$\\dfrac{1}{a-1}-\\dfrac{1}{a+1}+\\dfrac{2}{a^2-1}=\\dfrac{4}{a^2-1}$."),
 ("Egyszerűsítsd!",
  None, "$\\left(\\dfrac{1}{x-y}+\\dfrac{1}{x+y}\\right)\\cdot\\dfrac{x^2-y^2}{2}=x$."),
 ("Bontsd a lehető legtöbb tényezőre!",
  ["$x^4-16$","$x^4-1$","$a^3-a$"],
  ["$(x-2)(x+2)(x^2+4)$","$(x-1)(x+1)(x^2+1)$","$a(a-1)(a+1)$"]),
 ("Határozd meg az $m$ paramétert úgy, hogy $P(x)=x^3+mx^2-4$ osztható legyen $x-2$-vel!",
  None, "$m=-1$."),
 ("Egyszerűsítsd az emeletes törtet!",
  None, "$\\dfrac{\\dfrac{x}{y}-\\dfrac{y}{x}}{\\dfrac{1}{y}+\\dfrac{1}{x}}=x-y$."),
 ("Add meg a két polinom legnagyobb közös osztóját (LKO) és legkisebb közös többszörösét (LKT)!",
  None, "$A=x^2-x=x(x-1)$, $B=x^2-1=(x-1)(x+1)$; LKO $=x-1$, LKT $=x(x-1)(x+1)$."),
 ("Igazold az azonosságokat (alakítsd át mindkét oldalt)!",
  ["$(a+b)^2-(a-b)^2=4ab$","$(a+b)^2+(a-b)^2=2(a^2+b^2)$"],
  "Mindkettő azonosság: a bal oldalt kibontva a jobb oldalt kapjuk.", True),
]

JOKER = ("<b>Kang csapdája.</b> Kang egy „egyszerűsített” képletet injektált a rendszerbe: "
  "$\\dfrac{x^2+x}{x+1}=x^2$ — kihúzta a $+x$-et és a $+1$-et. Hol a hiba, és mi a helyes eredmény? "
  "(Emlékezz: <b>csak közös tényezővel</b> egyszerűsíthetünk, taggal nem!)",
  "A hiba: tagot húzott ki, nem tényezőt. Helyesen $\\dfrac{x^2+x}{x+1}=\\dfrac{x(x+1)}{x+1}=x$ (ÉT: $x\\neq -1$).")

# ===================== GYAKORLÓ ELLENŐRZŐ (🏫 órai + 🏠 otthoni) =====================
GYE_ORAI = [
 ("Végezd el a műveleteket!",
  ["$6x^3+2x^3-5x^3$","$5a(3-2a)$","$(x+2)^2$","$(x-4)(x+4)$"],
  "a) $3x^3$; b) $15a-10a^2$; c) $x^2+4x+4$; d) $x^2-16$.", True),
 ("Írd fel kanonikus alakban: $(2x-1)^2-(x-3)(x+2)$.",
  None, "$3x^2-3x+7$."),
 ("Bontsd tényezőkre!",
  ["$8x-12$","$x^2-16$","$x^2+8x+16$"],
  "a) $4(2x-3)$; b) $(x-4)(x+4)$; c) $(x+4)^2$.", True),
 ("Bontsd tényezőkre (köb, csoportosítás)!",
  ["$x^3-27$","$ax-ay+bx-by$"],
  ["$(x-3)(x^2+3x+9)$","$(a+b)(x-y)$"]),
 ("A Bézout-tétellel add meg a maradékot: $P(x)=x^3-2x^2+4x-3$ osztva $x-1$-gyel.",
  None, "$0$ (tehát osztható)."),
 ("Egyszerűsítsd, és add meg az értelmezési tartományt: $\\dfrac{x^2-25}{x+5}$.",
  None, "$x-5$, ÉT: $x\\neq -5$."),
 ("Add össze: $\\dfrac{1}{x-1}+\\dfrac{1}{x+1}$.",
  None, "$\\dfrac{2x}{x^2-1}$."),
 ("Végezd el: $\\dfrac{a^2-b^2}{a}\\cdot\\dfrac{a}{a-b}$.",
  None, "$a+b$."),
 ("Végezd el a polinomosztást: $(x^3+3x^2-4):(x+2)$.",
  None, "$x^2+x-2$ (a maradék $0$)."),
 ("Egyszerűsítsd a $\\dfrac{x^2-4}{x-2}$ törtet, majd számítsd ki az értékét $x=3$ esetén!",
  None, "$x+2$; értéke $5$."),
]
GYE_OTTHONI = [
 ("Végezd el a műveleteket!",
  ["$(a+5)^2$","$(3x-2)(3x+2)$","$2x(x^2-3x+1)$"],
  "a) $a^2+10a+25$; b) $9x^2-4$; c) $2x^3-6x^2+2x$.", True),
 ("Bontsd tényezőkre!",
  ["$12a^2-18a$","$4x^2-9$","$x^2-12x+36$"],
  "a) $6a(2a-3)$; b) $(2x-3)(2x+3)$; c) $(x-6)^2$.", True),
 ("Írd fel kanonikus alakban: $(x+3)^2+(x-3)^2$.",
  None, "$2x^2+18$."),
 ("A Bézout-tétellel add meg a maradékot: $P(x)=2x^3+x-5$ osztva $x-1$-gyel.",
  None, "$-2$."),
 ("Egyszerűsítsd, és add meg az értelmezési tartományt: $\\dfrac{a^2-ab}{a^2-b^2}$.",
  None, "$\\dfrac{a}{a+b}$, ÉT: $a\\neq \\pm b$."),
 ("Vond ki a törteket: $\\dfrac{3}{x}-\\dfrac{1}{x+2}$.",
  None, "$\\dfrac{2x+6}{x(x+2)}$."),
]

# =============================== OLDAL ===============================
body = []
body.append('    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(ALAP, "alap", "alap"))
body.append('    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(KOZEP, "kozep", "kozep"))
body.append('    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"))
body.append('    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]))

diszk = ('<p class="diszklemer">⚠️ Ez <b>gyakorló</b> anyag: nincs garancia, hogy az éles ellenőrzőn pontosan '
 'ennyi vagy pont ilyen feladat lesz. A cél a biztos rutin — a valódi feladatok ettől eltérhetnek.</p>')

body.append('    <h2 id="gyak-ellenorzo">🏫 Gyakorló ellenőrző</h2>\n    ' + diszk +
  '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYE_ORAI, "gye") +
  '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYE_OTTHONI, "gyeh"))

sections = "\n".join(body)

alcim = ("Közös kiképzési adattár a teljes racionális-kifejezés szektorhoz: haladj a szinteken, vagy ugorj a "
 "szükséges témára. A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!")

html = f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Racionális algebrai kifejezések — feladatok | 1e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="1e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">√</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">1e</span></a> ›
  <a href="index.html">Racionális algebrai kifejezések</a> ›
  <span class="itt">Feladatok</span>
</nav>
<div class="hero">
  <h1>Racionális algebrai kifejezések — feladatgyűjtemény</h1>
  <p class="alcim">{w(alcim)}</p>
  <div class="meta-sor">
    <span class="chip alap">Alap</span><span class="chip kozep">Közép</span>
    <span class="chip nehez">Nehéz</span><span class="chip joker">Joker</span>
  </div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
{sections}
    <div class="gyakorolj">
      <span class="ikon">📖</span>
      <p>Elakadtál? Nézd át a <a href="index.html">témakör tananyagait</a> vagy a <a href="osszefoglalo.html">tömör összefoglalót</a>.</p>
    </div>
    <div class="lapozo">
      <a class="elozo" href="tananyag-algebrai-tortek.html"><span class="irany">← Előző</span><span class="hova">Algebrai törtek</span></a>
      <a class="kov" href="osszefoglalo.html"><span class="irany">Következő →</span><span class="hova">Tömör összefoglaló</span></a>
    </div>
  </div>
  <nav class="toc" id="toc" aria-label="Tartalomjegyzék"></nav>
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
  renderMathInElement(document.body, {{delimiters:[
    {{left:'\\\\(', right:'\\\\)', display:false}},
    {{left:'\\\\[', right:'\\\\]', display:true}}
  ]}});
</script>
<script src="../../assets/js/ui.js"></script>
<script src="../../assets/js/quiz.js"></script>
</body>
</html>
'''
open(os.path.join(DEST, "feladatok-racionalis-algebrai-kifejezesek.html"), "w", encoding="utf-8").write(html)
print("feladatok-racionalis-algebrai-kifejezesek.html kész: Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "| gyak.ell.", len(GYE_ORAI)+len(GYE_OTTHONI))
