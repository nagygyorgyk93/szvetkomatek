# -*- coding: utf-8 -*-
"""2e/04 — A altema: szogmeres es radian (A1), a trigonometrikus kor (A2),
I. negyedre valo visszavezetes (A3). Mentor: Nightcrawler."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import (lap, doboz, brief, kviz, gyakorolj, abra,
                             svg_egysegkor, svg_fuggvenyek)

T = dict(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
         temakor="Trigonometrikus függvények")
FGY = "feladatok-trigonometrikus-kor.html"

# ---------------------------------------------------------------- önteszt
from sympy import (Rational as R, pi, sqrt, sin, cos, tan, cot, rad, deg,
                   nsimplify, simplify)
E = []
def chk(n, g, w):
    ok = (list(g) == list(w)) if isinstance(w, (list, tuple)) else (simplify(g - w) == 0)
    if not ok:
        E.append((n, g, w))
def negy(A): return [simplify(f(rad(A))) for f in (sin, cos, tan, cot)]
for a, w in [(180, 1), (90, R(1, 2)), (60, R(1, 3)), (45, R(1, 4)), (30, R(1, 6)),
             (270, R(3, 2)), (120, R(2, 3)), (135, R(3, 4)), (150, R(5, 6)), (315, R(7, 4))]:
    chk(f"rad{a}", nsimplify(rad(a))/pi, w)
chk("d30", negy(30), [R(1, 2), sqrt(3)/2, sqrt(3)/3, sqrt(3)])
chk("d45", negy(45), [sqrt(2)/2, sqrt(2)/2, 1, 1])
chk("d60", negy(60), [sqrt(3)/2, R(1, 2), sqrt(3), sqrt(3)/3])
chk("d120", negy(120), [sqrt(3)/2, R(-1, 2), -sqrt(3), -sqrt(3)/3])
chk("d135", negy(135), [sqrt(2)/2, -sqrt(2)/2, -1, -1])
chk("d150", negy(150), [R(1, 2), -sqrt(3)/2, -sqrt(3)/3, -sqrt(3)])
chk("d210", negy(210), [R(-1, 2), -sqrt(3)/2, sqrt(3)/3, sqrt(3)])
chk("d225", negy(225), [-sqrt(2)/2, -sqrt(2)/2, 1, 1])
chk("d240", negy(240), [-sqrt(3)/2, R(-1, 2), sqrt(3), sqrt(3)/3])
chk("d300", negy(300), [-sqrt(3)/2, R(1, 2), -sqrt(3), -sqrt(3)/3])
chk("d315", negy(315), [-sqrt(2)/2, sqrt(2)/2, -1, -1])
chk("d330", negy(330), [R(-1, 2), sqrt(3)/2, -sqrt(3)/3, -sqrt(3)])
chk("d0", [sin(0), cos(0)], [0, 1])
chk("d90", [sin(pi/2), cos(pi/2)], [1, 0])
chk("v1", sin(rad(150)) - sin(rad(30)), 0)
chk("v2", cos(rad(210)) + cos(rad(30)), 0)
chk("v3", tan(rad(300)) + tan(rad(60)), 0)
chk("v4", sin(rad(1000) - 2*pi) - sin(rad(280)), 0)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_RAD = svg_egysegkor(
    szogek=[(57.2958, "α = 1 rad ≈ 57,3°", "#047857")], w=340, h=300,
    leiras="Egy radián: az a középponti szög, amelyhez a sugárral egyenlő ívhossz tartozik",
    sugar_cimke="r")

SVG_NEGYED = svg_egysegkor(
    szogek=[(35, "P", "#047857")], w=340, h=320, negyedek=True,
    leiras="A trigonometrikus kör négy negyede és egy pont az első negyedben",
    sugar_cimke="r = 1")

SVG_JELL = svg_egysegkor(
    szogek=[(30, "30°", "#047857"), (45, "45°", "#3b82f6"), (60, "60°", "#8b5cf6"),
            (120, "120°", "#ef4444"), (135, "135°", "#f59e0b"), (150, "150°", "#0ea5e9")],
    w=380, h=380, leiras="Jellegzetes szögek a trigonometrikus körön az első két negyedben")

SVG_VISSZA = svg_egysegkor(
    szogek=[(40, "α", "#047857"), (140, "180° − α", "#ef4444"),
            (220, "180° + α", "#3b82f6"), (320, "360° − α", "#8b5cf6")],
    w=380, h=360, negyedek=False,
    leiras="Ugyanaz az alapszög a négy negyedben: a négy társszög")

# ===================================================================== A1

A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nightcrawler:</b> <i>Bamf!</i> — és már itt sem vagyok. Amikor teleportálok, '
         'nem távolságot adok meg, hanem <b>irányt</b>: egy szöget. És ha elég sokat ugrom '
         'körbe, egyszer csak ugyanoda érkezem, ahonnan indultam. Ez a trigonometria '
         'egész titka: <b>a szög körbeér</b>. Ehhez viszont előbb ki kell tágítanunk a '
         'szög fogalmát — mert $370^\\circ$-os szög a háromszögben nincs, a körön viszont '
         'nagyon is van.'),
   'Az <a href="../../1e/02-trigonometria/index.html">1e trigonometriájában</a> a szögfüggvényeket '
   '<b>derékszögű háromszögben</b> értelmeztük, ezért csak $0^\\circ$ és $90^\\circ$ közötti '
   'szögekről lehetett szó. Ez a témakör ezt a korlátot bontja le.',
 ]),

 ("A szög fogalmának általánosítása", [
   doboz("definicio", "Forgásszög",
         '<p>A szöget mostantól <b>forgatásként</b> értelmezzük: egy félegyenest az origó '
         'körül elforgatunk. A forgatás</p>'
         '<ul>'
         '<li><b>pozitív</b>, ha az óramutató járásával <b>ellentétes</b> (matematikai irány),</li>'
         '<li><b>negatív</b>, ha az óramutató járásával <b>megegyező</b>.</li>'
         '</ul>'
         '<p>Így minden valós szám szöget jelöl: $-90^\\circ$, $370^\\circ$, $1000^\\circ$ '
         'mind értelmes.</p>',
         hid="def-forgasszog"),
   doboz("tetel", "Társszögek — a teljes fordulat nem számít",
         '<p>Ha két szög <b>teljes fordulatokban</b> tér el egymástól, ugyanoda mutat:</p>'
         '$$\\alpha \\text{ és } \\alpha+k\\cdot 360^\\circ\\quad(k\\in\\mathbb{Z})$$'
         '<p>ugyanaz az irány, ezért <b>minden szögfüggvényük megegyezik</b>. Radiánban: '
         '$\\alpha$ és $\\alpha+2k\\pi$.</p>'
         '<p>Ezért minden szöget vissza tudunk vinni a $[0^\\circ;360^\\circ)$ tartományba: '
         'oszd el $360$-nal, és a <b>maradék</b> érdekel.</p>',
         hid="tetel-tarsszogek"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Melyik $[0^\\circ;360^\\circ)$ közötti szöggel egyezik meg? '
         '<b>a)</b> $420^\\circ$; <b>b)</b> $1000^\\circ$; <b>c)</b> $-50^\\circ$.</p>',
         hid="pelda-tarsszog",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $420-360=60$, tehát $\\boxed{60^\\circ}$.</p>'
                  '<p><b>b)</b> $1000=2\\cdot 360+280$, tehát $\\boxed{280^\\circ}$.</p>'
                  '<p><b>c)</b> $-50+360=310$, tehát $\\boxed{310^\\circ}$ — negatív szögnél '
                  '<b>hozzá</b>adunk teljes fordulatot.</p>')),
 ]),

 ("Szögmérés radiánban", [
   'A fok önkényes egység: valaki egyszer eldöntötte, hogy a teljes fordulat $360$ rész. '
   'Létezik azonban egy <b>természetes</b> szögmérték is, amely magából a körből adódik.',
   doboz("definicio", "Radián",
         '<p><b>Egy radián</b> annak a középponti szögnek a mértéke, amelyhez tartozó '
         '<b>ívhossz egyenlő a kör sugarával</b>.</p>'
         '<p>Mivel a teljes körív hossza $2r\\pi$, a teljes fordulat $2\\pi$ radián:</p>'
         '$$360^\\circ=2\\pi\\ \\text{rad},\\qquad 180^\\circ=\\pi\\ \\text{rad}.$$',
         hid="def-radian"),
   abra(SVG_RAD, "Egy radián $\\approx 57{,}3^\\circ$ — az a szög, amelyhez épp "
                 "egy sugárnyi ívhossz tartozik."),
   doboz("tetel", "Az átváltás",
         '<p>A $180^\\circ=\\pi$ arányból minden átváltás egyetlen szorzás:</p>'
         '$$\\text{fok}\\to\\text{radián}:\\ \\alpha_{\\text{rad}}=\\alpha^\\circ\\cdot'
         '\\frac{\\pi}{180},\\qquad'
         '\\text{radián}\\to\\text{fok}:\\ \\alpha^\\circ=\\alpha_{\\text{rad}}\\cdot'
         '\\frac{180}{\\pi}.$$'
         '<p>Gyakorlati fogás: <b>fokból radiánba</b> oszd el $180$-nal és írj mellé $\\pi$-t; '
         '<b>radiánból fokba</b> helyettesíts a $\\pi$ helyére $180^\\circ$-ot.</p>',
         hid="tetel-atvaltas"),
   doboz("tetel", "Amit érdemes fejből tudni",
         '<div class="tblwrap"><table>'
         '<tr><th>fok</th><td>$30^\\circ$</td><td>$45^\\circ$</td><td>$60^\\circ$</td>'
         '<td>$90^\\circ$</td><td>$180^\\circ$</td><td>$270^\\circ$</td><td>$360^\\circ$</td></tr>'
         '<tr><th>radián</th><td>$\\tfrac{\\pi}{6}$</td><td>$\\tfrac{\\pi}{4}$</td>'
         '<td>$\\tfrac{\\pi}{3}$</td><td>$\\tfrac{\\pi}{2}$</td><td>$\\pi$</td>'
         '<td>$\\tfrac{3\\pi}{2}$</td><td>$2\\pi$</td></tr>'
         '</table></div>'
         '<p>Figyeld meg a logikát: minél <b>nagyobb</b> a nevező, annál <b>kisebb</b> a szög.</p>',
         hid="tetel-radian-tabla"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p><b>a)</b> Váltsd radiánba: $120^\\circ$, $315^\\circ$.<br>'
         '<b>b)</b> Váltsd fokba: $\\tfrac{5\\pi}{6}$, $\\tfrac{7\\pi}{4}$.</p>',
         hid="pelda-atvaltas",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $120\\cdot\\dfrac{\\pi}{180}=\\dfrac{120\\pi}{180}='
                  '\\boxed{\\dfrac{2\\pi}{3}}$; &nbsp; '
                  '$315\\cdot\\dfrac{\\pi}{180}=\\dfrac{315\\pi}{180}=\\boxed{\\dfrac{7\\pi}{4}}$.</p>'
                  '<p><b>b)</b> $\\dfrac{5\\pi}{6}=\\dfrac{5\\cdot 180^\\circ}{6}=\\boxed{150^\\circ}$; '
                  '&nbsp; $\\dfrac{7\\pi}{4}=\\dfrac{7\\cdot 180^\\circ}{4}=\\boxed{315^\\circ}$.</p>')),
   doboz("csapda", "Sinister vírus-kódja",
         '<p><b>A számológép módja!</b> Ha a gép <b>RAD</b> módban van, a $\\sin 30$ nem '
         '$0{,}5$-öt ad, hanem $\\sin(30\\ \\text{rad})\\approx -0{,}988$. Fokos feladatnál '
         'mindig <b>DEG</b> módban dolgozz — érdemes a $\\sin 30=0{,}5$ próbával ellenőrizni.</p>'
         '<p>És ne feledd: a $\\pi$ a radiánban <b>egység</b>, nem szorzó — a '
         '$\\tfrac{5\\pi}{6}$ nem „ötször pí per hat fok”, hanem egy szög: $150^\\circ$.</p>'),
   kviz('Hány radián $270^\\circ$?',
        ['$\\tfrac{3\\pi}{2}$', '$\\tfrac{2\\pi}{3}$', '$270\\pi$'], 0,
        jo="✔ 270/180 = 3/2, tehát 3π/2.",
        nem="✘ Oszd el 180-nal: 270/180 = 3/2 → 3π/2."),
   gyakorolj(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–2"),
 ]),
]

# ===================================================================== A2

A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nightcrawler:</b> Most jön a trükk, ami mindent megold. Rajzolj egy '
         '<b>egységsugarú</b> kört az origó köré, és forgasd rá a szöget. Ahová a szög '
         'szára metszi a kört, ott van egy pont — és ennek a pontnak a <b>koordinátái '
         'maguk a szögfüggvények</b>. Nem kell háromszög, nem kell hegyesszög: ez a '
         'definíció <b>minden</b> szögre működik.'),
 ]),

 ("A trigonometrikus kör", [
   doboz("definicio", "Trigonometrikus kör és a négy függvény",
         '<p>A <b>trigonometrikus kör</b> (egységkör) az origó középpontú, $1$ sugarú kör. '
         'Forgassuk el a pozitív $x$-tengelyt $\\alpha$ szöggel; a szár a kört a '
         '$P(x_{P};y_{P})$ pontban metszi. Ekkor</p>'
         '$$\\cos\\alpha=x_{P},\\qquad \\sin\\alpha=y_{P},$$'
         '$$\\operatorname{tg}\\alpha=\\frac{\\sin\\alpha}{\\cos\\alpha}\\ (\\cos\\alpha\\neq 0),'
         '\\qquad \\operatorname{ctg}\\alpha=\\frac{\\cos\\alpha}{\\sin\\alpha}\\ '
         '(\\sin\\alpha\\neq 0).$$',
         hid="def-trigonometrikus-kor"),
   abra(SVG_NEGYED, "A kör négy <b>negyede</b>. A $P$ pont <b>első</b> koordinátája a "
                    "koszinusz, a <b>második</b> a szinusz — ebben a sorrendben, mint minden "
                    "koordinátánál."),
   doboz("tetel", "Két azonnali következmény",
         '<p><b>1.</b> Mivel $P$ rajta van az egységkörön, $x_{P}^{2}+y_{P}^{2}=1$, azaz</p>'
         '$$\\sin^{2}\\alpha+\\cos^{2}\\alpha=1.$$'
         '<p>Ez a <b>trigonometriai alapazonosság</b> — a Pitagorasz-tétel az egységkörön.</p>'
         '<p><b>2.</b> A koordináták $-1$ és $1$ közé esnek, tehát minden $\\alpha$-ra</p>'
         '$$-1\\le\\sin\\alpha\\le 1,\\qquad -1\\le\\cos\\alpha\\le 1.$$'
         '<p>Ezért a $\\sin x=2$ egyenletnek <b>nincs</b> megoldása.</p>',
         hid="tetel-kovetkezmenyek"),
   doboz("csapda", "Sinister vírus-kódja",
         '<p>A leggyakoribb kezdő hiba: <b>felcserélni a koordinátákat</b>. A pont '
         '$P(\\cos\\alpha;\\sin\\alpha)$ — előbb a koszinusz. Jó emlékeztető: a '
         '<b>c</b>oszinusz „vízszintes”, mint a <b>c</b> betű nyitott oldala; a '
         '<b>s</b>zinusz „függőleges”.</p>'
         '<p>A másik: $\\sin^{2}\\alpha$ azt jelenti, hogy $(\\sin\\alpha)^{2}$ — '
         '<b>nem</b> $\\sin(\\alpha^{2})$.</p>'),
 ]),

 ("Előjelek negyedenként", [
   'Mivel a szinusz az $y$-, a koszinusz az $x$-koordináta, az előjelüket egyszerűen '
   'a negyed helyzete adja meg.',
   doboz("tetel", "Az előjeltáblázat",
         '<div class="tblwrap"><table>'
         '<tr><th>Negyed</th><th>$\\sin$</th><th>$\\cos$</th><th>$\\operatorname{tg}$</th>'
         '<th>$\\operatorname{ctg}$</th></tr>'
         '<tr><td><b>I.</b> ($0^\\circ$–$90^\\circ$)</td><td>+</td><td>+</td><td>+</td><td>+</td></tr>'
         '<tr><td><b>II.</b> ($90^\\circ$–$180^\\circ$)</td><td>+</td><td>−</td><td>−</td><td>−</td></tr>'
         '<tr><td><b>III.</b> ($180^\\circ$–$270^\\circ$)</td><td>−</td><td>−</td><td>+</td><td>+</td></tr>'
         '<tr><td><b>IV.</b> ($270^\\circ$–$360^\\circ$)</td><td>−</td><td>+</td><td>−</td><td>−</td></tr>'
         '</table></div>'
         '<p>Nem kell bemagolni: a $\\sin$ ott pozitív, ahol a pont a tengely <b>fölött</b> '
         'van (I–II.), a $\\cos$ ott, ahol <b>jobbra</b> (I. és IV.). A $\\operatorname{tg}$ és a '
         '$\\operatorname{ctg}$ hányados, tehát ott pozitív, ahol a kettő <b>azonos előjelű</b> '
         '(I. és III.).</p>',
         hid="tetel-eljelek"),
   kviz('Milyen előjelű $\\cos 200^\\circ$?',
        ['Negatív', 'Pozitív', 'Nulla'], 0,
        jo="✔ 200° a III. negyedben van, ott a koszinusz (az x-koordináta) negatív.",
        nem="✘ A 200° a III. negyedben van — ott mind a sin, mind a cos negatív."),
 ]),

 ("Jellegzetes szögek pontos értékei", [
   abra(SVG_JELL, "A $30^\\circ$, $45^\\circ$, $60^\\circ$ és a hozzájuk tartozó "
                  "második negyedbeli szögek. Minden érték ugyanabból a három "
                  "alapszögből származik."),
   doboz("tetel", "A három alapszög",
         '<div class="tblwrap"><table>'
         '<tr><th></th><th>$0^\\circ$</th><th>$30^\\circ$</th><th>$45^\\circ$</th>'
         '<th>$60^\\circ$</th><th>$90^\\circ$</th></tr>'
         '<tr><th>$\\sin$</th><td>$0$</td><td>$\\tfrac12$</td><td>$\\tfrac{\\sqrt2}{2}$</td>'
         '<td>$\\tfrac{\\sqrt3}{2}$</td><td>$1$</td></tr>'
         '<tr><th>$\\cos$</th><td>$1$</td><td>$\\tfrac{\\sqrt3}{2}$</td>'
         '<td>$\\tfrac{\\sqrt2}{2}$</td><td>$\\tfrac12$</td><td>$0$</td></tr>'
         '<tr><th>$\\operatorname{tg}$</th><td>$0$</td><td>$\\tfrac{\\sqrt3}{3}$</td>'
         '<td>$1$</td><td>$\\sqrt3$</td><td>—</td></tr>'
         '<tr><th>$\\operatorname{ctg}$</th><td>—</td><td>$\\sqrt3$</td><td>$1$</td>'
         '<td>$\\tfrac{\\sqrt3}{3}$</td><td>$0$</td></tr>'
         '</table></div>'
         '<p><b>Memóriafogás:</b> a szinusz sora $\\tfrac{\\sqrt0}{2},\\tfrac{\\sqrt1}{2},'
         '\\tfrac{\\sqrt2}{2},\\tfrac{\\sqrt3}{2},\\tfrac{\\sqrt4}{2}$ — a gyök alatt '
         '$0,1,2,3,4$. A koszinusz ugyanez <b>visszafelé</b>.</p>'
         '<p>A $\\operatorname{tg}90^\\circ$ és a $\\operatorname{ctg}0^\\circ$ <b>nem '
         'létezik</b>: nullával kellene osztani.</p>',
         hid="tetel-jellegzetes"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Add meg mind a négy függvény pontos értékét! '
         '<b>a)</b> $135^\\circ$; <b>b)</b> $\\tfrac{4\\pi}{3}$.</p>',
         hid="pelda-jellegzetes",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $135^\\circ$ a <b>II.</b> negyedben van, az alapszöge '
                  '$180^\\circ-135^\\circ=45^\\circ$. A II. negyedben csak a szinusz pozitív:</p>'
                  '<p>$\\sin=\\tfrac{\\sqrt2}{2}$, &nbsp; $\\cos=-\\tfrac{\\sqrt2}{2}$, &nbsp; '
                  '$\\operatorname{tg}=-1$, &nbsp; $\\operatorname{ctg}=-1$.</p>'
                  '<p><b>b)</b> $\\tfrac{4\\pi}{3}=240^\\circ$, a <b>III.</b> negyedben; '
                  'alapszöge $240^\\circ-180^\\circ=60^\\circ$. Ott a $\\sin$ és a $\\cos$ '
                  'negatív, a $\\operatorname{tg}$ és a $\\operatorname{ctg}$ pozitív:</p>'
                  '<p>$\\sin=-\\tfrac{\\sqrt3}{2}$, &nbsp; $\\cos=-\\tfrac12$, &nbsp; '
                  '$\\operatorname{tg}=\\sqrt3$, &nbsp; $\\operatorname{ctg}=\\tfrac{\\sqrt3}{3}$.</p>')),
   doboz("erdekesseg", "Miért pont ez a három szög?",
         '<p>A $45^\\circ$ az egyenlő szárú derékszögű háromszögből jön (befogók $1$, '
         'átfogó $\\sqrt2$), a $30^\\circ$ és a $60^\\circ$ pedig a <b>félbevágott '
         'szabályos háromszögből</b> (oldalak $1$, $\\sqrt3$, $2$). Ez a két háromszög '
         'adja a teljes táblázatot — érdemes lerajzolni a füzet szélére.</p>'),
   gyakorolj(FGY + "#alap-6", "A 6–12", FGY + "#kozep-3", "K 3–7"),
 ]),
]

# ===================================================================== A3

A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nightcrawler:</b> Ne ijedj meg a $217^\\circ$-tól. Minden szögnek van egy '
         '<b>alapszöge</b> az első negyedben — az, amennyire a legközelebbi vízszintes '
         'tengelytől eltér. A függvényérték <b>nagysága</b> ugyanaz, mint az alapszögé; '
         'már csak az <b>előjelet</b> kell hozzátenni. Két lépés, és bármelyik szöget '
         'visszahoztad ismerős terepre.'),
 ]),

 ("A módszer", [
   abra(SVG_VISSZA, "Ugyanaz az $\\alpha$ alapszög négy különböző szöget ad meg: "
                    "$\\alpha$, $180^\\circ-\\alpha$, $180^\\circ+\\alpha$ és "
                    "$360^\\circ-\\alpha$. A négy pont a tengelyekre tükrös."),
   doboz("tetel", "Visszavezetés az első negyedre",
         '<p><b>1. lépés:</b> ha a szög nincs $[0^\\circ;360^\\circ)$-ban, vidd oda '
         'teljes fordulatokkal.</p>'
         '<p><b>2. lépés:</b> keresd meg az <b>alapszöget</b> $\\alpha$:</p>'
         '<div class="tblwrap"><table>'
         '<tr><th>Negyed</th><th>A szög alakja</th><th>Alapszög</th></tr>'
         '<tr><td>I.</td><td>$\\alpha$</td><td>maga a szög</td></tr>'
         '<tr><td>II.</td><td>$180^\\circ-\\alpha$</td><td>$180^\\circ-$ szög</td></tr>'
         '<tr><td>III.</td><td>$180^\\circ+\\alpha$</td><td>szög $-180^\\circ$</td></tr>'
         '<tr><td>IV.</td><td>$360^\\circ-\\alpha$</td><td>$360^\\circ-$ szög</td></tr>'
         '</table></div>'
         '<p><b>3. lépés:</b> a függvényérték <b>abszolút értéke</b> az alapszögé, '
         'az <b>előjelet</b> az előjeltáblázat adja.</p>',
         hid="tetel-visszavezetes"),
   doboz("tetel", "A négy összefüggés képlettel",
         '$$\\sin(180^\\circ-\\alpha)=\\sin\\alpha,\\qquad \\cos(180^\\circ-\\alpha)=-\\cos\\alpha,$$'
         '$$\\sin(180^\\circ+\\alpha)=-\\sin\\alpha,\\qquad \\cos(180^\\circ+\\alpha)=-\\cos\\alpha,$$'
         '$$\\sin(360^\\circ-\\alpha)=-\\sin\\alpha,\\qquad \\cos(360^\\circ-\\alpha)=\\cos\\alpha.$$'
         '<p>Speciálisan $\\sin(-\\alpha)=-\\sin\\alpha$ (a szinusz <b>páratlan</b>) és '
         '$\\cos(-\\alpha)=\\cos\\alpha$ (a koszinusz <b>páros</b>) — ezt a grafikonon is '
         'látni fogod.</p>',
         hid="tetel-kepletek"),
   doboz("pelda", "Veszélyterem-szimuláció",
         '<p>Vezesd vissza az első negyedre, és add meg a pontos értéket! '
         '<b>a)</b> $\\sin 150^\\circ$; <b>b)</b> $\\cos 210^\\circ$; '
         '<b>c)</b> $\\operatorname{tg}300^\\circ$; <b>d)</b> $\\sin 1000^\\circ$.</p>',
         hid="pelda-visszavezetes",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $150^\\circ$ a II. negyedben, alapszöge $30^\\circ$; ott a '
                  'szinusz <b>pozitív</b>: $\\sin 150^\\circ=\\sin 30^\\circ=\\boxed{\\tfrac12}$.</p>'
                  '<p><b>b)</b> $210^\\circ$ a III. negyedben, alapszöge $30^\\circ$; ott a '
                  'koszinusz <b>negatív</b>: $\\cos 210^\\circ=-\\cos 30^\\circ='
                  '\\boxed{-\\tfrac{\\sqrt3}{2}}$.</p>'
                  '<p><b>c)</b> $300^\\circ$ a IV. negyedben, alapszöge $60^\\circ$; ott a '
                  'tangens <b>negatív</b>: $\\operatorname{tg}300^\\circ=-\\operatorname{tg}60^\\circ='
                  '\\boxed{-\\sqrt3}$.</p>'
                  '<p><b>d)</b> Előbb a fordulatok: $1000-2\\cdot 360=280$. A $280^\\circ$ a IV. '
                  'negyedben van, alapszöge $360-280=80^\\circ$, és ott a szinusz negatív: '
                  '$\\sin 1000^\\circ=-\\sin 80^\\circ\\approx\\boxed{-0{,}98481}$.</p>')),
   doboz("csapda", "Sinister vírus-kódja",
         '<p><b>Az előjelet a SZÖG negyede dönti el, nem a végeredmény „érzése”.</b> '
         'Sokan a $\\cos 210^\\circ$-nál helyesen megtalálják a $30^\\circ$-ot, aztán '
         'elfelejtik a mínuszt. Írd fel <b>előbb</b> az előjelet, csak utána az értéket:</p>'
         '<p>$\\cos 210^\\circ = -\\;\\cos 30^\\circ = -\\tfrac{\\sqrt3}{2}$</p>'
         '<p>És vigyázz: a $180^\\circ+\\alpha$ alaknál az <b>alapszög</b> $\\alpha$, nem '
         '$180^\\circ+\\alpha$ — a $217^\\circ$ alapszöge $37^\\circ$.</p>'),
   kviz('Mennyi $\\cos 330^\\circ$?',
        ['$\\tfrac{\\sqrt3}{2}$', '$-\\tfrac{\\sqrt3}{2}$', '$\\tfrac12$'], 0,
        jo="✔ 330° a IV. negyedben van (alapszög 30°), ott a koszinusz pozitív.",
        nem="✘ 330° a IV. negyedben van — ott a koszinusz POZITÍV, az alapszög pedig 30°."),
   gyakorolj(FGY + "#alap-13", "A 13–18", FGY + "#kozep-8", "K 8–12"),
   brief('<b>Nightcrawler:</b> Ezzel a kör a kezedben van: bármelyik szöget vissza tudod '
         'vinni ismerős terepre. A következő blokkban viszont már nem <b>egy</b> szöggel '
         'dolgozunk, hanem kettővel — mert ha a $75^\\circ$-ot fel tudod bontani '
         '$45^\\circ+30^\\circ$-ra, akkor a pontos értékét is ki tudod számolni. '
         'Jönnek az <b>azonosságok</b>.', outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-szogmeres-es-radian.html",
     cim="Szögmérés és a szög általánosítása",
     cim_tiszta="Szögmérés és a szög általánosítása",
     alcim="A forgásszög, a társszögek, a radián fogalma és a fok–radián átváltás.",
     chip="A Fázisugrás · 1/11", szakaszok=A1,
     elozo=("index.html", "Trigonometrikus függvények"),
     kovetkezo=("tananyag-trigonometrikus-kor.html", "A trigonometrikus kör")),
 lap(**T, fajl="tananyag-trigonometrikus-kor.html",
     cim="A trigonometrikus kör", cim_tiszta="A trigonometrikus kör",
     alcim="A négy szögfüggvény definíciója az egységkörön, az előjelek negyedenként "
           "és a jellegzetes szögek pontos értékei.",
     chip="A Fázisugrás · 2/11", szakaszok=A2,
     elozo=("tananyag-szogmeres-es-radian.html", "Szögmérés és a szög általánosítása"),
     kovetkezo=("tananyag-visszavezetes.html", "Visszavezetés az első negyedre")),
 lap(**T, fajl="tananyag-visszavezetes.html",
     cim="Visszavezetés az első negyedre", cim_tiszta="Visszavezetés az első negyedre",
     alcim="Az alapszög megkeresése, a négy társszög és az előjelek — bármely szög "
           "pontos értéke két lépésben.",
     chip="A Fázisugrás · 3/11", szakaszok=A3,
     elozo=("tananyag-trigonometrikus-kor.html", "A trigonometrikus kör"),
     kovetkezo=(FGY, "Feladatok — a trigonometrikus kör")),
]
for u in KI:
    print("✓", os.path.basename(u))
