# -*- coding: utf-8 -*-
"""2e/04 — B altema feladatgyujtemeny: azonossagok (alap, addicios, ketszeres,
felszog, szorzatta alakitas)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as R, sqrt, sin, cos, tan, cot, rad, simplify, N
E = []
def chk(n, g, w, tol=None):
    ok = abs(float(g) - w) < tol if tol is not None else simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
# alapazonosság-párok (pitagoraszi hármasok)
for nev, s, c in [("35", R(3, 5), R(4, 5)), ("513", R(5, 13), R(12, 13)),
                  ("817", R(8, 17), R(15, 17)), ("941", R(9, 41), R(40, 41)),
                  ("2029", R(20, 29), R(21, 29)), ("725", R(7, 25), R(24, 25))]:
    chk("pit" + nev, s**2 + c**2, 1)
# addíciós
chk("a15", sin(rad(15)), (sqrt(6) - sqrt(2))/4)
chk("a75s", sin(rad(75)), (sqrt(6) + sqrt(2))/4)
chk("a75c", cos(rad(75)), (sqrt(6) - sqrt(2))/4)
chk("a105c", cos(rad(105)), (sqrt(2) - sqrt(6))/4)
chk("a165s", sin(rad(165)), (sqrt(6) - sqrt(2))/4)
chk("a195c", cos(rad(195)), -(sqrt(6) + sqrt(2))/4)
chk("felism1", sin(rad(40))*cos(rad(20)) + cos(rad(40))*sin(rad(20)) - sqrt(3)/2, 0, 1e-25)
chk("felism2", cos(rad(80))*cos(rad(20)) + sin(rad(80))*sin(rad(20)) - R(1, 2), 0, 1e-25)
chk("felism3", sin(rad(70))*cos(rad(10)) - cos(rad(70))*sin(rad(10)) - sqrt(3)/2, 0, 1e-25)
chk("felism4", (tan(rad(25)) + tan(rad(20)))/(1 - tan(rad(25))*tan(rad(20))) - 1, 0, 1e-25)
# összeg
chk("ossz-s", R(3, 5)*R(5, 13) + R(4, 5)*R(12, 13), R(63, 65))
chk("ossz-c", R(4, 5)*R(5, 13) - R(3, 5)*R(12, 13), R(-16, 65))
chk("kul-s", R(8, 17)*R(4, 5) - R(15, 17)*R(3, 5), R(-13, 85))
chk("kul-c", R(15, 17)*R(3, 5) + R(8, 17)*R(4, 5), R(77, 85))
# kétszeres
for nev, s, c, s2, c2 in [("A", R(4, 5), R(3, 5), R(24, 25), R(-7, 25)),
                          ("B", R(5, 13), R(12, 13), R(120, 169), R(119, 169)),
                          ("C", R(8, 17), R(15, 17), R(240, 289), R(161, 289)),
                          ("D", R(24, 25), R(7, 25), R(336, 625), R(-527, 625))]:
    chk("k2s" + nev, 2*s*c, s2); chk("k2c" + nev, c**2 - s**2, c2)
chk("k2-13", 2*R(1, 3)**2 - 1, R(-7, 9))
chk("k2-tg", 2*R(1, 2)/(1 - R(1, 4)), R(4, 3))
# félszög
chk("f725", sqrt((1 - R(7, 25))/2), R(3, 5))
chk("f725c", sqrt((1 + R(7, 25))/2), R(4, 5))
chk("f2229", sqrt((1 - R(-7, 25))/2), R(4, 5))
chk("f225", sin(rad(R(45, 2))) - sqrt(2 - sqrt(2))/2, 0, 1e-25)
chk("f15c", cos(rad(15)) - sqrt(2 + sqrt(3))/2, 0, 1e-25)
# szorzattá
chk("sz1", sin(rad(75)) + sin(rad(15)) - sqrt(6)/2, 0, 1e-25)
chk("sz2", sin(rad(70)) + sin(rad(10)) - sqrt(3)*sin(rad(40)), 0, 1e-25)
chk("sz3", cos(rad(40)) + cos(rad(20)) - sqrt(3)*cos(rad(10)), 0, 1e-25)
chk("sz4", cos(rad(15)) - cos(rad(75)) - sqrt(2)/2, 0, 1e-25)
chk("sz5", sin(rad(105)) - sin(rad(15)) - sqrt(2)/2, 0, 1e-25)
chk("sz6", (sin(rad(50)) + sin(rad(10)))/(cos(rad(50)) + cos(rad(10))) - tan(rad(30)),
    0, 1e-25)
chk("sz7", sin(rad(80)) - sin(rad(20)) - cos(rad(50)), 0, 1e-25)
# nehéz
chk("N1", (1 - cos(rad(60))**2)/sin(rad(60))**2 - 1, 0, 1e-25)
chk("N4", sin(rad(15))*cos(rad(15)) - R(1, 4), 0, 1e-25)
chk("N5", cos(rad(20))*cos(rad(40))*cos(rad(80)) - R(1, 8), 0, 1e-20)
chk("J", 4*sin(rad(15))*cos(rad(15))*cos(rad(30)) - sqrt(3)/2, 0, 1e-25)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================

ALAP = [
 ("Írd fel az öt alapazonosságot fejből, majd ellenőrizd a tananyagban!", None,
  "$\\sin^{2}\\alpha+\\cos^{2}\\alpha=1$; &nbsp; "
  "$\\operatorname{tg}\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}$; &nbsp; "
  "$\\operatorname{ctg}\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha}$; &nbsp; "
  "$\\operatorname{tg}\\alpha\\operatorname{ctg}\\alpha=1$; &nbsp; "
  "$1+\\operatorname{tg}^{2}\\alpha=\\dfrac{1}{\\cos^{2}\\alpha}$."),
 ("Számold ki a másik három szögfüggvény pontos értékét! "
  "$\\sin\\alpha=\\tfrac35$ és $\\alpha$ hegyesszög.", None,
  "$\\cos\\alpha=\\tfrac45$, $\\operatorname{tg}\\alpha=\\tfrac34$, "
  "$\\operatorname{ctg}\\alpha=\\tfrac43$."),
 ("Számold ki a másik három értéket! $\\cos\\alpha=\\tfrac{12}{13}$ és "
  "$\\sin\\alpha&lt;0$.", None,
  "IV. negyed: $\\sin\\alpha=-\\tfrac{5}{13}$, "
  "$\\operatorname{tg}\\alpha=-\\tfrac{5}{12}$, "
  "$\\operatorname{ctg}\\alpha=-\\tfrac{12}{5}$."),
 ("Számold ki a másik három értéket! $\\sin\\alpha=\\tfrac{8}{17}$ és "
  "$\\cos\\alpha&lt;0$.", None,
  "II. negyed: $\\cos\\alpha=-\\tfrac{15}{17}$, "
  "$\\operatorname{tg}\\alpha=-\\tfrac{8}{15}$, "
  "$\\operatorname{ctg}\\alpha=-\\tfrac{15}{8}$."),
 ("Számold ki a másik három értéket! $\\cos\\alpha=-\\tfrac{20}{29}$ és "
  "$\\operatorname{tg}\\alpha&lt;0$.", None,
  "A koszinusz negatív, a tangens negatív → II. negyed: $\\sin\\alpha=\\tfrac{21}{29}$, "
  "$\\operatorname{tg}\\alpha=-\\tfrac{21}{20}$, "
  "$\\operatorname{ctg}\\alpha=-\\tfrac{20}{21}$."),
 ("Melyik negyedben van a szög?",
  ["$\\sin\\alpha&gt;0$, $\\cos\\alpha&lt;0$", "$\\operatorname{tg}\\alpha&gt;0$, "
   "$\\sin\\alpha&lt;0$", "$\\cos\\alpha&gt;0$, $\\operatorname{ctg}\\alpha&lt;0$"],
  ["II.", "III.", "IV."], True),
 ("Számold ki addíciós képlettel!",
  ["$\\sin 75^\\circ$", "$\\cos 75^\\circ$"],
  ["$\\sin(45^\\circ+30^\\circ)=\\dfrac{\\sqrt6+\\sqrt2}{4}$",
   "$\\cos(45^\\circ+30^\\circ)=\\dfrac{\\sqrt6-\\sqrt2}{4}$"], True),
 ("Számold ki addíciós képlettel!",
  ["$\\sin 15^\\circ$", "$\\cos 105^\\circ$"],
  ["$\\sin(45^\\circ-30^\\circ)=\\dfrac{\\sqrt6-\\sqrt2}{4}$",
   "$\\cos(60^\\circ+45^\\circ)=\\dfrac{\\sqrt2-\\sqrt6}{4}$"], True),
 ("Ismerd fel a képletet, és add meg az értéket!",
  ["$\\sin 40^\\circ\\cos 20^\\circ+\\cos 40^\\circ\\sin 20^\\circ$",
   "$\\cos 80^\\circ\\cos 20^\\circ+\\sin 80^\\circ\\sin 20^\\circ$"],
  ["$\\sin 60^\\circ=\\dfrac{\\sqrt3}{2}$", "$\\cos 60^\\circ=\\dfrac12$"], True),
 ("Ismerd fel a képletet, és add meg az értéket!",
  ["$\\sin 70^\\circ\\cos 10^\\circ-\\cos 70^\\circ\\sin 10^\\circ$",
   "$\\dfrac{\\operatorname{tg}25^\\circ+\\operatorname{tg}20^\\circ}"
   "{1-\\operatorname{tg}25^\\circ\\operatorname{tg}20^\\circ}$"],
  ["$\\sin 60^\\circ=\\dfrac{\\sqrt3}{2}$", "$\\operatorname{tg}45^\\circ=1$"], True),
 ("Számold ki $\\sin 2\\alpha$ és $\\cos 2\\alpha$ pontos értékét! "
  "$\\sin\\alpha=\\tfrac45$, $\\alpha$ hegyesszög.", None,
  "$\\cos\\alpha=\\tfrac35$; $\\sin 2\\alpha=\\tfrac{24}{25}$, "
  "$\\cos 2\\alpha=\\tfrac{9-16}{25}=-\\tfrac{7}{25}$."),
 ("Számold ki $\\sin 2\\alpha$ és $\\cos 2\\alpha$ pontos értékét! "
  "$\\cos\\alpha=\\tfrac{12}{13}$, $\\alpha$ hegyesszög.", None,
  "$\\sin\\alpha=\\tfrac{5}{13}$; $\\sin 2\\alpha=\\tfrac{120}{169}$, "
  "$\\cos 2\\alpha=\\tfrac{144-25}{169}=\\tfrac{119}{169}$."),
 ("Számold ki!",
  ["$\\cos 2\\alpha$, ha $\\cos\\alpha=\\tfrac13$",
   "$\\operatorname{tg}2\\alpha$, ha $\\operatorname{tg}\\alpha=\\tfrac12$"],
  ["$2\\cos^{2}\\alpha-1=\\tfrac29-1=-\\tfrac79$",
   "$\\dfrac{2\\cdot\\tfrac12}{1-\\tfrac14}=\\dfrac{1}{\\tfrac34}=\\tfrac43$"], True),
 ("Számold ki $\\sin\\tfrac{\\alpha}{2}$ és $\\cos\\tfrac{\\alpha}{2}$ pontos értékét! "
  "$\\cos\\alpha=\\tfrac{7}{25}$ és $\\alpha\\in\\left(0;\\tfrac{\\pi}{2}\\right)$.", None,
  "$\\tfrac{\\alpha}{2}$ az I. negyedben van, minden pozitív: "
  "$\\sin\\tfrac{\\alpha}{2}=\\sqrt{\\tfrac{18}{50}}=\\tfrac35$, "
  "$\\cos\\tfrac{\\alpha}{2}=\\sqrt{\\tfrac{32}{50}}=\\tfrac45$."),
 ("Alakítsd szorzattá, majd egyszerűsítsd!",
  ["$\\sin 75^\\circ+\\sin 15^\\circ$", "$\\cos 40^\\circ+\\cos 20^\\circ$"],
  ["$2\\sin 45^\\circ\\cos 30^\\circ=\\dfrac{\\sqrt6}{2}$",
   "$2\\cos 30^\\circ\\cos 10^\\circ=\\sqrt3\\cos 10^\\circ$"], True),
 ("Alakítsd szorzattá, majd egyszerűsítsd!",
  ["$\\sin 70^\\circ+\\sin 10^\\circ$", "$\\cos 15^\\circ-\\cos 75^\\circ$"],
  ["$2\\sin 40^\\circ\\cos 30^\\circ=\\sqrt3\\sin 40^\\circ$",
   "$-2\\sin 45^\\circ\\sin(-30^\\circ)=\\dfrac{\\sqrt2}{2}$"], True),
 ("Alakítsd szorzattá, majd egyszerűsítsd!",
  ["$\\sin 105^\\circ-\\sin 15^\\circ$", "$\\sin 80^\\circ-\\sin 20^\\circ$"],
  ["$2\\cos 60^\\circ\\sin 45^\\circ=\\dfrac{\\sqrt2}{2}$",
   "$2\\cos 50^\\circ\\sin 30^\\circ=\\cos 50^\\circ$"], True),
 ("Igaz vagy hamis? Indokold!",
  ["$\\sin(\\alpha+\\beta)=\\sin\\alpha+\\sin\\beta$",
   "$\\cos 2\\alpha=2\\cos\\alpha$", "$\\sin^{2}\\alpha+\\cos^{2}\\alpha=1$"],
  ["<b>Hamis</b> — próbáld $30^\\circ+60^\\circ$-kal: $1\\neq 1{,}37$.",
   "<b>Hamis</b> — a $2$ a szögre vonatkozik; $\\cos 2\\alpha=2\\cos^{2}\\alpha-1$.",
   "<b>Igaz</b> — ez az alapazonosság, minden $\\alpha$-ra."], True),
]

# ============================== KÖZÉPSZINT ==============================

KOZEP = [
 ("Számold ki a másik három értéket! $\\operatorname{tg}\\alpha=\\tfrac{3}{4}$ és "
  "$\\alpha$ a III. negyedben van.", None,
  "$1+\\operatorname{tg}^{2}\\alpha=\\tfrac{1}{\\cos^{2}\\alpha}$, tehát "
  "$\\cos^{2}\\alpha=\\tfrac{16}{25}$; a III. negyedben $\\cos\\alpha=-\\tfrac45$ és "
  "$\\sin\\alpha=-\\tfrac35$. $\\operatorname{ctg}\\alpha=\\tfrac43$."),
 ("Egyszerűsítsd! $\\dfrac{1-\\cos^{2}\\alpha}{\\sin^{2}\\alpha}$", None,
  "A számláló $\\sin^{2}\\alpha$, tehát az egész $1$ (ha $\\sin\\alpha\\neq 0$)."),
 ("Egyszerűsítsd! $\\sin\\alpha\\operatorname{ctg}\\alpha$", None,
  "$\\sin\\alpha\\cdot\\dfrac{\\cos\\alpha}{\\sin\\alpha}=\\cos\\alpha$"),
 ("Számold ki $\\sin(\\alpha+\\beta)$ és $\\cos(\\alpha+\\beta)$ pontos értékét, ha "
  "$\\sin\\alpha=\\tfrac35$, $\\cos\\beta=\\tfrac{5}{13}$, és mindkét szög hegyesszög!",
  None, "$\\cos\\alpha=\\tfrac45$, $\\sin\\beta=\\tfrac{12}{13}$. "
        "$\\sin(\\alpha+\\beta)=\\tfrac{15+48}{65}=\\tfrac{63}{65}$; "
        "$\\cos(\\alpha+\\beta)=\\tfrac{20-36}{65}=-\\tfrac{16}{65}$."),
 ("Számold ki $\\sin(\\alpha-\\beta)$ és $\\cos(\\alpha-\\beta)$ pontos értékét, ha "
  "$\\sin\\alpha=\\tfrac{8}{17}$, $\\cos\\beta=\\tfrac35$, és mindkét szög hegyesszög!",
  None, "$\\cos\\alpha=\\tfrac{15}{17}$, $\\sin\\beta=\\tfrac45$. "
        "$\\sin(\\alpha-\\beta)=\\tfrac{8}{17}\\cdot\\tfrac35-\\tfrac{15}{17}\\cdot\\tfrac45="
        "-\\tfrac{13}{85}$; $\\cos(\\alpha-\\beta)=\\tfrac{15}{17}\\cdot\\tfrac35+"
        "\\tfrac{8}{17}\\cdot\\tfrac45=\\tfrac{77}{85}$."),
 ("Számold ki addíciós képlettel! $\\sin 165^\\circ$ és $\\cos 195^\\circ$", None,
  "$\\sin 165^\\circ=\\sin(180^\\circ-15^\\circ)=\\sin 15^\\circ="
  "\\dfrac{\\sqrt6-\\sqrt2}{4}$; &nbsp; "
  "$\\cos 195^\\circ=-\\cos 15^\\circ=-\\dfrac{\\sqrt6+\\sqrt2}{4}$."),
 ("Számold ki $\\sin 2\\alpha$, $\\cos 2\\alpha$ és $\\operatorname{tg}2\\alpha$ értékét, "
  "ha $\\sin\\alpha=\\tfrac{24}{25}$ és $\\alpha$ hegyesszög!", None,
  "$\\cos\\alpha=\\tfrac{7}{25}$; $\\sin 2\\alpha=\\tfrac{336}{625}$, "
  "$\\cos 2\\alpha=\\tfrac{49-576}{625}=-\\tfrac{527}{625}$, "
  "$\\operatorname{tg}2\\alpha=-\\tfrac{336}{527}$. "
  "(A $2\\alpha$ már a II. negyedben van!)"),
 ("Számold ki $\\sin\\tfrac{\\alpha}{2}$, $\\cos\\tfrac{\\alpha}{2}$ és "
  "$\\operatorname{tg}\\tfrac{\\alpha}{2}$ értékét, ha $\\cos\\alpha=-\\tfrac{7}{25}$ és "
  "$\\alpha\\in\\left(\\tfrac{\\pi}{2};\\pi\\right)$!", None,
  "$\\tfrac{\\alpha}{2}\\in\\left(\\tfrac{\\pi}{4};\\tfrac{\\pi}{2}\\right)$ — "
  "az I. negyedben, minden pozitív. "
  "$\\sin\\tfrac{\\alpha}{2}=\\sqrt{\\tfrac{32}{50}}=\\tfrac45$, "
  "$\\cos\\tfrac{\\alpha}{2}=\\sqrt{\\tfrac{18}{50}}=\\tfrac35$, "
  "$\\operatorname{tg}\\tfrac{\\alpha}{2}=\\tfrac43$."),
 ("Számold ki pontosan! $\\sin 22^\\circ30'$ és $\\cos 15^\\circ$ (félszög-képlettel).",
  None, "$\\sin 22^\\circ30'=\\sqrt{\\dfrac{1-\\tfrac{\\sqrt2}{2}}{2}}="
        "\\dfrac{\\sqrt{2-\\sqrt2}}{2}\\approx 0{,}38268$; &nbsp; "
        "$\\cos 15^\\circ=\\sqrt{\\dfrac{1+\\tfrac{\\sqrt3}{2}}{2}}="
        "\\dfrac{\\sqrt{2+\\sqrt3}}{2}\\approx 0{,}96593$."),
 ("Igazold! $\\sin(60^\\circ+\\alpha)+\\sin(60^\\circ-\\alpha)=\\sqrt3\\cos\\alpha$",
  None, "A bal oldal a $\\sin u+\\sin v$ képlettel: félösszeg $60^\\circ$, "
        "félkülönbség $\\alpha$, tehát $2\\sin 60^\\circ\\cos\\alpha="
        "2\\cdot\\tfrac{\\sqrt3}{2}\\cos\\alpha=\\sqrt3\\cos\\alpha$ ✔ "
        "(Az addíciós képletekkel kibontva is ugyanez jön ki.)"),
 ("Igazold! $\\cos\\left(\\tfrac{\\pi}{6}+\\alpha\\right)-"
  "\\cos\\left(\\tfrac{\\pi}{6}-\\alpha\\right)=-\\sin\\alpha$", None,
  "A $\\cos u-\\cos v$ képlettel: $-2\\sin\\tfrac{\\pi}{6}\\sin\\alpha="
  "-2\\cdot\\tfrac12\\sin\\alpha=-\\sin\\alpha$ ✔"),
 ("Egyszerűsítsd! $\\dfrac{\\sin 50^\\circ+\\sin 10^\\circ}"
  "{\\cos 50^\\circ+\\cos 10^\\circ}$", None,
  "Számláló: $2\\sin 30^\\circ\\cos 20^\\circ$; nevező: "
  "$2\\cos 30^\\circ\\cos 20^\\circ$. A $2\\cos 20^\\circ$ kiesik, marad "
  "$\\dfrac{\\sin 30^\\circ}{\\cos 30^\\circ}=\\operatorname{tg}30^\\circ="
  "\\dfrac{\\sqrt3}{3}$."),
 ("Számold ki! $\\sin 15^\\circ\\cos 15^\\circ$", None,
  "A kétszeres szög képlete visszafelé: $\\sin\\alpha\\cos\\alpha="
  "\\tfrac12\\sin 2\\alpha$, tehát $\\tfrac12\\sin 30^\\circ=\\dfrac14$."),
 ("Fejezd ki $\\operatorname{tg}\\alpha$ segítségével! "
  "$\\dfrac{\\sin\\alpha+\\cos\\alpha}{\\cos\\alpha}$", None,
  "Tagonként osztva: $\\operatorname{tg}\\alpha+1$."),
]

# ============================== NEHÉZ SZINT ==============================

NEHEZ = [
 ("Igazold! $\\dfrac{1-\\cos 2\\alpha}{\\sin 2\\alpha}=\\operatorname{tg}\\alpha$", None,
  "$1-\\cos 2\\alpha=1-(1-2\\sin^{2}\\alpha)=2\\sin^{2}\\alpha$, és "
  "$\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha$. A hányados "
  "$\\dfrac{2\\sin^{2}\\alpha}{2\\sin\\alpha\\cos\\alpha}="
  "\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\operatorname{tg}\\alpha$ ✔"),
 ("Igazold! $\\sin^{4}\\alpha-\\cos^{4}\\alpha=-\\cos 2\\alpha$", None,
  "A bal oldal két négyzet különbsége: "
  "$\\left(\\sin^{2}\\alpha-\\cos^{2}\\alpha\\right)"
  "\\left(\\sin^{2}\\alpha+\\cos^{2}\\alpha\\right)=\\sin^{2}\\alpha-\\cos^{2}\\alpha"
  "=-\\cos 2\\alpha$ ✔"),
 ("Számold ki! $\\cos 20^\\circ\\cos 40^\\circ\\cos 80^\\circ$", None,
  "Szorozzuk és osszuk $2\\sin 20^\\circ$-kal, és használjuk háromszor a "
  "$2\\sin u\\cos u=\\sin 2u$ azonosságot: "
  "$\\dfrac{\\sin 160^\\circ}{8\\sin 20^\\circ}=\\dfrac{\\sin 20^\\circ}"
  "{8\\sin 20^\\circ}=\\dfrac18$."),
 ("Számold ki pontosan! $\\operatorname{tg}75^\\circ$", None,
  "$\\operatorname{tg}(45^\\circ+30^\\circ)="
  "\\dfrac{1+\\tfrac{\\sqrt3}{3}}{1-\\tfrac{\\sqrt3}{3}}=2+\\sqrt3\\approx 3{,}73205$."),
 ("Egyszerűsítsd! $\\dfrac{\\sin 3\\alpha}{\\sin\\alpha}-"
  "\\dfrac{\\cos 3\\alpha}{\\cos\\alpha}$", None,
  "Közös nevezőre hozva a számláló "
  "$\\sin 3\\alpha\\cos\\alpha-\\cos 3\\alpha\\sin\\alpha=\\sin 2\\alpha$, a nevező "
  "$\\sin\\alpha\\cos\\alpha=\\tfrac12\\sin 2\\alpha$. A hányados $2$."),
 ("Egy szög szinusza és koszinusza összege $\\tfrac{7}{5}$. Mennyi "
  "$\\sin\\alpha\\cos\\alpha$?", None,
  "Négyzetre emelve: $(\\sin\\alpha+\\cos\\alpha)^{2}=1+2\\sin\\alpha\\cos\\alpha="
  "\\tfrac{49}{25}$, tehát $2\\sin\\alpha\\cos\\alpha=\\tfrac{24}{25}$ és "
  "$\\sin\\alpha\\cos\\alpha=\\tfrac{12}{25}$."),
]

JOKER = ("Számold ki pontosan! "
         "$4\\sin 15^\\circ\\cos 15^\\circ\\cos 30^\\circ$",
         "Használjuk kétszer a $2\\sin u\\cos u=\\sin 2u$ azonosságot:"
         "$$4\\sin 15^\\circ\\cos 15^\\circ\\cos 30^\\circ="
         "2\\cdot\\big(2\\sin 15^\\circ\\cos 15^\\circ\\big)\\cos 30^\\circ="
         "2\\sin 30^\\circ\\cos 30^\\circ=\\sin 60^\\circ.$$"
         "A végeredmény tehát $\\boxed{\\dfrac{\\sqrt3}{2}}\\approx 0{,}86603$.")

# ============================== OLDAL ==============================

body = [
 '    <h2 id="alap">🟢 Alapszint — Kék Csapat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Arany Csapat</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]),
]

ut = oldal(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
           fajl="feladatok-azonossagok.html", cim="Azonosságok",
           temakor="Trigonometrikus függvények",
           alcim="Alapazonosságok negyed-információval, addíciós képletek oda-vissza, "
                 "kétszeres és félszög, valamint szorzattá alakítás. "
                 "A végeredmény minden feladatnál lenyitható!",
           sections_html="\n".join(body),
           prev="tananyag-felszog-es-szorzatta-alakitas.html",
           prevc="Félszög és szorzattá alakítás",
           nxt="tananyag-trig-fuggvenyek-grafikonja.html",
           nxtc="A trigonometrikus függvények grafikonja")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "+ Joker")
