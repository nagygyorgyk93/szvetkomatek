# -*- coding: utf-8 -*-
"""4e/01 — feladatgyujtemeny (Zsoldos-lista): sorozatok hatarerteke.
Horgony-terv: narrativa_01-sorozatok-hatarerteke.md · feladat-terkep: terkep_fgy_01-sorozatok-hatarerteke.md
(jovahagyva 2026-09-23; a B2 belepo alap-kartyai 4-4 reszfeladatra bovitve).
Forras: 5_Feladatok-A_szamsorozat_hatarerteke.pdf (5_F, a kulcs hibai javitva), 7_Feladatok - Mertani sor.pdf (7_F),
6_Az e szam.pdf (6_), 8_Gyakorlas az ellenorzore.pdf (8_), 9_Egyeni/paros munka (9_, a 3c nevezoje n+3: igy a forras kulcsa helyes), sajat.
A hatarerteket minden kartyan sympy szamolja; a vegeredmeny-szoveg ebbol epul."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from sympy import Rational as Q, symbols, limit, oo, exp, latex, sympify, S, N, Pow, E as EE
from sympy.parsing.sympy_parser import parse_expr

n = symbols("n", positive=True, integer=True)
LD = {"n": n, "Rational": Q, "sqrt": __import__("sympy").sqrt}


def TX(s):
    t = latex(parse_expr(s, local_dict=LD, evaluate=False), order="none")
    return re.sub(r"(?<![\d.}])1 \\frac", r"\\frac", t)      # Mul(1, 1/n) → „1 \frac1n” ne legyen


def _zar(e, t):
    """Összeg/különbség a lim után zárójelbe (különben a lim csak az első tagra vonatkozna)."""
    return r"\left(" + t + r"\right)" if parse_expr(e, local_dict=LD, evaluate=False).is_Add else t


def LIM(s):
    f = sympify(s, locals=LD)
    try:
        return limit(f, n, oo)
    except NotImplementedError:
        # váltakozó előjel: |a_n| -> 0 esetén 0, különben divergens
        g = f.replace(lambda x: x.is_Pow and x.base.is_number and x.base < 0,
                      lambda x: (-x.base) ** x.exp)
        return S.Zero if limit(g, n, oo) == 0 else S.NaN


def V(v):
    """Határérték → TeX."""
    if v == oo:
        return r"+\infty"
    if v == -oo:
        return r"-\infty"
    if isinstance(v, Pow) and v.base == EE or v.func == exp:
        k = v.exp if isinstance(v, Pow) else v.args[0]
        return "e^{%s}" % latex(k)
    return latex(v)


def LIMS(intro, exprs, tex=None):
    """Határérték-kártya: minden részfeladat egy lim, a végeredmény sympyből."""
    tex = tex or {}
    subs = [r"$\lim\limits_{n\to\infty}" + (tex[e] if e in tex else _zar(e, TX(e))) + "$" for e in exprs]
    ans = ["$" + V(LIM(e)) + "$" for e in exprs]
    return (intro, subs, ans)


def TAGOK(intro, exprs, extra=None):
    """Első öt tag + sejtés a határértékre."""
    subs, ans = [], []
    for e in exprs:
        f = sympify(e, locals=LD)
        t = [f.subs(n, k) for k in range(1, 6)]
        if extra and e in extra:
            vege = extra[e]
        else:
            L = LIM(e)
            vege = "divergens" if L is S.NaN or not (L.is_finite or L in (oo, -oo)) else "$" + V(L) + "$"
        subs.append("$a_n=" + TX(e) + "$")
        ans.append("$" + r";\ ".join(latex(x) for x in t) + r"$ — a határérték: " + vege)
    return (intro, subs, ans)


def JEGYZ(k, szoveg):
    """Megjegyzés az utolsó végeredmény után."""
    return (k[0], k[1], k[2][:-1] + [k[2][-1] + szoveg])


def DEC(x):
    """Tört + tizedes alak: 25/2 = 12,5; 50/3 ≈ 16,67."""
    if x.q == 1:
        return latex(x)
    d = x.q
    for p in (2, 5):
        while d % p == 0:
            d //= p
    t = str(round(float(x), 2)).replace(".", "{,}")
    return latex(x) + ("=" if d == 1 else r"\approx") + t


def MS(b1, q):
    return Q(b1) / (1 - Q(q))


def D(x):
    """Tizedes tört vesszővel (a kerekítéshez)."""
    return str(x).replace(".", "{,}")


HAT = "Számítsd ki a határértékeket!"

# ============================== ALAP ==============================
A5 = ["(3*n+1)/(n+2)", "(2*n-1)/(3*n-1)", "6*n/(2*n-1)", "n**2/(n+1)"]
A5b = ["n/(3-n**2)", "3*n**2/(n**2+3)", "(n-1)/(n**2-2)", "2*n**2-2*n"]
tabla6 = [round(float(N(Q(5 * k - 2, k + 3))), 3) for k in (10, 100, 1000)]
assert tabla6 == [3.692, 4.835, 4.983], tabla6

ALAP = [
 TAGOK("Írd fel a sorozat első öt tagját, és a tagok alapján sejtsd meg a határértékét! Ha kell, számold ki "
       "az $a_{100}$ tagot is!", A5),
 TAGOK("Írd fel a sorozat első öt tagját, és a tagok alapján sejtsd meg a határértékét! Ha kell, számold ki "
       "az $a_{100}$ tagot is!", A5b),
 ("Döntsd el, konvergens-e a sorozat, és ha igen, mi a határértéke! Használd a nevezetes határértékeket.",
  [r"$a_n=\dfrac5n$", r"$a_n=3-\dfrac1{n^2}$", r"$a_n=\left(\dfrac23\right)^n$", r"$a_n=\left(\dfrac32\right)^n$"],
  ["konvergens, $0$", "konvergens, $3$", "konvergens, $0$", r"divergens, $+\infty$"]),
 ("Mihez tart a $q^n$ sorozat?",
  [r"$q=-\dfrac{9}{10}$", r"$q=\dfrac{11}{10}$", r"$q=-\dfrac14$", r"$q=1$"],
  ["$0$", r"$+\infty$", "$0$", "$1$"]),
 LIMS("Számítsd ki a határértékeket a műveleti szabályok segítségével!",
      ["(2+3/n)*(4-1/n)", "(5-2/n)/(1+1/n**2)", "7+(Rational(1,2))**n"],
      tex={"(5-2/n)/(1+1/n**2)": r"\dfrac{5-\frac2n}{1+\frac1{n^2}}"}),
 (r"Számítsd ki az $a_n=\dfrac{5n-2}{n+3}$ sorozat $10.$, $100.$ és $1000.$ tagját három tizedesjegyre "
  r"kerekítve, és a kapott értékek alapján sejtsd meg a sorozat határértékét!", None,
  r"$a_{10}\approx" + D(tabla6[0]) + r"$; $a_{100}\approx" + D(tabla6[1]) + r"$; $a_{1000}\approx" + D(tabla6[2])
  + r"$ — a határérték: $5$"),
 # --- B1: racionális törtek
 LIMS(HAT, ["(2*n+1)/(7*n-1)", "(4*n**2-3)/(1-2*n**2)", "(n**2+n+1)/(3*n-1)"]),
 LIMS(HAT, ["(3*n+2)/(5*n**2-2*n-1)", "(-2*n**3+n-1)/(2*n**3+5)", "(2*n-1)/(2-n+n**2)"]),
 LIMS(HAT, ["(n**2-3*n+2)/(2-3*n)", "(6*n-11)/(5-2*n)", "(8*n+7)/(4*n**2+3*n)"]),
 LIMS(HAT, ["(2*n**2+5*n-7)/(6*n+3)", "(2*n**2-7*n+9)/(12*n**2+5*n-6)", "(16*n-7)/(12*n+6)"]),
 LIMS(HAT, ["(n**2-3*n+2)/(5-7*n)", "(10*n**2+5*n+1)/(3-9*n-2*n**2)", "(-6*n+12)/(7*n**2-13)"]),
 LIMS(HAT, ["(-15*n**2-50*n+40)/(-60*n**2+15*n-15)", "(8-3*n**2)/(6*n**2+n)", "(n**3+2)/(5*n**2-4)"]),
 LIMS("Számítsd ki a határértékeket! Elég a főtagokat összeszorozni.",
      ["(2*n-1)**2/(1-2*n**2)", "(2*n-1)**2/((2*n+1)*(n+1))", "(3*n+2)**2/((3*n-2)*(n+1))"]),
 LIMS("Számítsd ki a határértékeket! Elég a főtagokat összeszorozni.",
      ["(3*n+1)**2/(2+n)**2", "(1-3*n)**3/(2*n**3+5)"]),
 # --- B2: belépő gyökös
 LIMS("Számítsd ki a határértékeket! A gyökjel alól is kiemelhetsz: $\\sqrt{n^2}=n$.",
      ["sqrt(n**2+5)/(n+1)", "sqrt(4*n**2+3)/n", "sqrt(n**2+2*n)/(2*n)", "3*n/sqrt(n**2+1)"]),
 LIMS("Számítsd ki a határértékeket! A gyökjel alól is kiemelhetsz: $\\sqrt{n^2}=n$.",
      ["n/sqrt(n**2+7)", "sqrt(9*n**2+1)/(3*n)", "sqrt(16*n**2-3)/(2*n+5)", "(5*n-1)/sqrt(25*n**2+4)"]),
 # --- B3: (1 + c/n)^(kn)
 LIMS("Számítsd ki a határértékeket! Használd az $\\left(1+\\frac kn\\right)^{mn}\\to e^{km}$ összefüggést.",
      ["(1+1/n)**(3*n)", "(1+5/n)**n", "(1+2/n)**(2*n)"]),
 LIMS("Számítsd ki a határértékeket! Használd az $\\left(1+\\frac kn\\right)^{mn}\\to e^{km}$ összefüggést.",
      ["(1+2/n)**n", "(1+4/n)**(3*n)", "(1+1/n)**(7*n)"]),
 # --- C: végtelen mértani sor
 ("Határozd meg a végtelen mértani sor összegét!",
  [r"$b_1=5$, $q=0{,}6$", r"$b_1=10$, $q=0{,}4$", r"$b_1=8$, $q=0{,}75$", r"$b_1=12$, $q=0{,}2$",
   r"$b_1=3$, $q=0{,}9$"],
  ["$" + DEC(MS(b, q)) + "$" for b, q in [(5, "3/5"), (10, "2/5"), (8, "3/4"), (12, "1/5"), (3, "9/10")]]),
 (r"Egy mértani sorozat első tagja $81$, hányadosa $\frac13$. Írd fel az első nyolc tagját! Mennyi a "
  r"sorozat tagjaiból képzett végtelen mértani sor összege?", None,
  r"$81;\ 27;\ 9;\ 3;\ 1;\ \frac13;\ \frac19;\ \frac{1}{27}$ — az összeg $S=" + latex(MS(81, "1/3")) + r"=121{,}5$"),
 (r"Egy pillangó minden repülési körében az előző kör útjának $\frac15$-ét teszi meg. Az első körben "
  r"$10$ métert repül. Hány métert tesz meg összesen, ha végtelen sok kört repül?", None,
  "$" + latex(MS(10, "1/5")) + r"=12{,}5$ m"),
 (r"Minden lépésed hossza az előző lépés hosszának $\frac34$-e. Az első lépés $1$ méter. Milyen messzire "
  r"jutsz összesen, ha végtelen sok lépést teszel?", None, "$" + latex(MS(1, "3/4")) + "$ m"),
 (r"Egy hőlégballon minden újabb emelkedéskor az előző emelkedés $\frac23$-ával jut feljebb. Az első "
  r"emelkedéskor $30$ métert emelkedik. Milyen magasra jut összesen, ha végtelen sokszor emelkedik?", None,
  "$" + latex(MS(30, "2/3")) + "$ m"),
 (r"Egy cseppkő minden évben az előző évi növekedésének $\frac45$-ével nő. Az első évben $5$ cm-t nő. "
  r"Mekkora lesz a teljes növekedése, ha végtelen sok évig nő?", None, "$" + latex(MS(5, "4/5")) + "$ cm"),
 (r"Egy cseppkő minden évben az előző évi növekedésének $\frac25$-ével nő. Az első évben $10$ cm-t nő.",
  ["Sorold fel az első hat év növekedését!", "Mekkora lesz a teljes növekedése, ha végtelen sok évig nő?"],
  [r"$10;\ 4;\ \frac85;\ \frac{16}{25};\ \frac{32}{125};\ \frac{64}{625}$ cm",
   "$" + latex(MS(10, "2/5")) + r"\approx16{,}67$ cm"]),
 (r"Van-e összege a végtelen mértani sornak, és ha igen, mennyi? Minden esetben $b_1=6$.",
  [r"$q=\dfrac13$", r"$q=-\dfrac23$", r"$q=\dfrac32$", r"$q=-1$"],
  ["$" + latex(MS(6, "1/3")) + "$", "$" + latex(MS(6, "-2/3")) + "$",
   r"nincs, mert $\lvert q\rvert\ge1$", r"nincs, mert $\lvert q\rvert\ge1$"]),
]

# ============================== KÖZÉP ==============================
KOZEP = [
 TAGOK("Írd fel a sorozat első öt tagját, és sejtsd meg, konvergens-e, és ha igen, mi a határértéke! "
       "Ha kell, számolj ki néhány nagyobb sorszámú tagot is.", ["(-1)**n/(n**2+1)", "n**2/2**n", "(-2)**n/(2*n)"],
       extra={"(-2)**n/(2*n)": "nincs, a sorozat divergens (a tagok előjele váltakozik, az abszolút értékük nő)"}),
 (r"Az $a_n=\dfrac{4n+1}{n}$ sorozat határértéke $4$. Hányadik tagtól kezdve tér el a sorozat minden tagja "
  r"$0{,}01$-nál kevesebbel a $4$-től?", None, r"a $101.$ tagtól ($\frac1n\lt\frac{1}{100}$, ha $n\gt100$)"),
 JEGYZ(LIMS("Számítsd ki a határértékeket! Mit mutatnak az eredmények a „$\\infty-\\infty$” alakról?",
      ["(n+7)-n", "(n**2+n)-n**2", "n-(n+3)"],
      tex={"(n+7)-n": r"\big((n+7)-n\big)", "(n**2+n)-n**2": r"\big((n^2+n)-n^2\big)",
           "n-(n+3)": r"\big(n-(n+3)\big)"}),
      r" — tanulság: a $\infty-\infty$ alak határozatlan, ugyanez az alak $7$-et, $+\infty$-t és "
      r"$-3$-at is adott, ezért először mindig össze kell vonni."),
 ("Határozd meg az $a$ valós paraméter értékét!",
  [r"$\lim\limits_{n\to\infty}\dfrac{an^2+3}{2n^2-n}=3$", r"$\lim\limits_{n\to\infty}\dfrac{an+1}{4n-3}=-\dfrac12$"],
  ["$a=6$", "$a=-2$"]),
 (r"Véd Vilmos szerint $\lim\limits_{n\to\infty}\dfrac{n^3-2n}{4n^2+1}=\dfrac14$, „mert a főegyütthatók "
  r"hányadosa”. Mit rontott el? Mennyi a helyes határérték?", None,
  r"a számláló harmadfokú, a nevező másodfokú, így nem a főegyütthatók hányadosa a határérték: $"
  + V(LIM("(n**3-2*n)/(4*n**2+1)")) + "$"),
 LIMS("Számítsd ki a határértékeket!", ["(n**2+1)*(2*n-3)/(4*n**3-n)", "(2*n+1)**3/((n+1)*(n**2+4))"]),
 # --- B2: gyökös
 LIMS(HAT, ["(n+1)/sqrt(4*n**2+1)", "(3*n+1)/sqrt(4*n**2-3)", "sqrt(36*n**2-2)/(1-2*n)"]),
 LIMS(HAT, ["sqrt(n**2-n+1)/(2*n-1)", "sqrt(4*n**2-n+1)/(n+1)", "sqrt(9*n**2+3*n+1)/(2*n+1)", "(n+2)/sqrt(9*n**2-2)"]),
 LIMS(HAT, ["(18*n-5)/sqrt(9*n**2-7)", "sqrt(25*n**2-9*n+13)/(35*n+6)", "sqrt(121*n**2-5*n)/(12*n+3)"]),
 LIMS(HAT, ["(7*n-13)/sqrt(289*n**2-10*n+3)", "sqrt(169*n**2+81*n+1)/sqrt(169*n**2-16*n+4)"],
      tex={"sqrt(169*n**2+81*n+1)/sqrt(169*n**2-16*n+4)": r"\dfrac{\sqrt{169n^2+81n+1}}{\sqrt{169n^2-16n+4}}"}),
 LIMS(HAT, ["(2*n+sqrt(4*n**2+1))/(3*n-1)", "(sqrt(n**2+1)+sqrt(9*n**2+2))/(2*n)"]),
 # --- B3
 LIMS(HAT, ["(1+2/n)**(n/3)", "(1+8/n)**(n/4)", "(1+2/n)**(n/5)"]),
 LIMS(HAT, ["(1-1/n)**n", "(1-1/(3*n))**n", "(1-2/n)**(3*n)"]),
 LIMS("Számítsd ki a határértékeket! Először nézd meg, mihez tart az alap.",
      ["((3*n+1)/n)**n", "((n+1)/(4*n))**n", "(1+3*n/(2*n+1))**(5*n)", "(1+n/(n+1))**(2/n)"]),
 (lambda k: (k[0], k[1], [r"$1^\infty$ alakú: " + k[2][0],
                          r"nem $1^\infty$ alakú, mert az alap $2$-höz tart: " + k[2][1],
                          r"$1^\infty$ alakú, mert $\frac{n+2}{n}=1+\frac2n$: " + k[2][2]]))(
 LIMS("Döntsd el, melyik $1^\\infty$ alakú, és számítsd ki a határértékeket!",
      ["(1+5/n)**(2*n)", "((2*n+1)/(n+1))**n", "((n+2)/n)**n"])),
 # --- C
 ("Írd fel közönséges törtként a szakaszos tizedes törtet!",
  [r"$0{,}\dot7$", r"$0{,}\dot1\dot5$", r"$0{,}\dot3\dot6$"],
  ["$" + latex(MS("7/10", "1/10")) + "$", "$" + latex(MS("15/100", "1/100")) + "$",
   "$" + latex(MS("36/100", "1/100")) + "$"]),
 ("Írd fel közönséges törtként a vegyes szakaszos tizedes törtet!",
  [r"$0{,}1\dot6$", r"$0{,}2\dot3$"],
  ["$" + latex(Q(1, 10) + MS("6/100", "1/10")) + "$", "$" + latex(Q(2, 10) + MS("3/100", "1/10")) + "$"]),
 ("Számolj visszafelé!",
  [r"Egy végtelen mértani sor összege $12$, hányadosa $\frac14$. Mennyi az első tagja?",
   r"Egy végtelen mértani sor első tagja $5$, összege $20$. Mennyi a hányadosa?"],
  ["$b_1=" + latex(12 * (1 - Q(1, 4))) + "$", "$q=" + latex(1 - Q(5, 20)) + "$"]),
 ("Számítsd ki a végtelen mértani sor összegét!",
  [r"$8-4+2-1+\dots$", r"$27-9+3-1+\dots$"],
  ["$" + latex(MS(8, "-1/2")) + "$", "$" + latex(MS(27, "-1/3")) + "$"]),
 (r"Egy $8$ cm oldalú négyzet oldalfelező pontjai egy újabb négyzetet határoznak meg, ennek oldalfelező "
  r"pontjai egy harmadikat, és így tovább, végtelen sokáig. Mennyi a négyzetek területének összege?", None,
  r"$64+32+16+\dots=" + latex(MS(64, "1/2")) + r"$ cm$^2$"),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 LIMS(HAT, ["(n**2+2)/(2*n-1)-2*n**2/(4*n-1)", "(3*n**2-2)/(6*n+1)-n**2/(2*n-1)", "(8*n**2-1)/(4*n+1)-2*n**2/(n+1)"]),
 LIMS(HAT, ["6*n**2/(3*n-1)-(2*n**2-1)/(n+1)", "6*n**2/(2*n-1)-(3*n**2-1)/(n+1)", "(n**2+1)/(2*n+1)-3*n**2/(6*n-1)"]),
 LIMS(HAT, ["12*n**2/(3*n-4)-(4*n**2+2*n)/(n+1)", "n**2/(2*n-1)-(n**2+1)/(2*n+1)", "(6*n**2-1)/(n+3)-24*n**2/(4*n-1)"]),
 LIMS(HAT, ["(1+3/(2*n-3))**(n+7)", "(1+5/(4*n+1))**(6*n+3)", "(1-1/(2*n))**(3*n+1)"]),
 LIMS(HAT, ["((n+2)/(n+7))**(n/3)", "((3*n+3)/(3*n+1))**(n+1)", "((n+5)/(n+3))**n", "((n-1)/(n+3))**(2*n/3)"]),
 LIMS(HAT, ["((2*n+5)/(2*n-3))**(5*n-1)", "(1+3/(2*n-5))**(6*n)"]),
 (r"Egy labdát $1$ m magasról leejtünk. Minden pattanás után az előző magasság $\frac34$-éig emelkedik "
  r"vissza. Mekkora utat tesz meg a labda összesen, ha (elméletben) végtelen sokszor pattan?", None,
  r"$1+2\left(\frac34+\frac{9}{16}+\dots\right)=1+2\cdot" + latex(MS("3/4", "3/4")) + "=" +
  latex(1 + 2 * MS("3/4", "3/4")) + "$ m"),
 (r"Oldd meg a valós számok halmazán: $1+x+x^2+x^3+\dots=\frac52-x$.", None,
  r"$\frac{1}{1-x}=\frac52-x$, rendezve $2x^2-7x+3=0$, ebből $x_1=\frac{1}{2}$, $x_2=3$; a sornak csak "
  r"$\lvert x\rvert\lt1$ esetén van összege, ezért a megoldás csak $x=\frac{1}{2}$"),
]

JOKER = (r"Akhilleusz tízszer olyan gyorsan fut, mint a teknős, a teknős pedig $100$ m előnnyel indul. Mire "
         r"Akhilleusz odaér, ahol a teknős volt, a teknős már $10$ m-rel előrébb jár; mire ezt a $10$ m-t is "
         r"megteszi, a teknős újabb $1$ m-rel jár előrébb, és így tovább.",
         [r"$100+10+1+0{,}1+\dots$ — végtelen mértani sor, $b_1=100$, $q=\frac{1}{10}$",
          "$" + latex(MS(100, "1/10")) + r"\approx111{,}1$ m után"],
         [r"Írd fel Akhilleusz szakaszait végtelen mértani sorként!",
          r"Hány méter megtétele után éri utol Akhilleusz a teknőst?"])

# ============================== ÖNELLENŐRZÉS ==============================
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (26, 20, 8), (len(ALAP), len(KOZEP), len(NEHEZ))
assert MS(81, "1/3") == Q(243, 2) and 1 + 2 * MS("3/4", "3/4") == 7 and MS(100, "1/10") == Q(1000, 9)
assert LIM("(6*n**2-1)/(n+3)-24*n**2/(4*n-1)") == Q(-39, 2)         # n+3 nevezővel a 9_ kulcsa (-19,5) helyes
assert LIM("(n**2-3*n+2)/(2-3*n)") == -oo                            # az 5_F kulcsa itt +inf-et írt
print("sympy önteszt: OK")

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
ut = oldal(tagozat="4e", mappa="01-sorozatok-hatarerteke", fajl="feladatok-hatarertek.html",
           cim="Sorozatok határértéke", temakor="Sorozatok határértéke",
           h1="Sorozatok határértéke — Zsoldos-lista",
           alcim="A sorozat határértéke, kiemelés, gyökös kifejezések, az $e$ szám és a végtelen mértani sor. "
                 "A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-vegtelen-mertani-sor.html", prevc="A végtelen mértani sor",
           nxt="feladatok-hazi.html", nxtc="I.V.H. Kihallgató Terem — Vészterem")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ), "+ Joker")
