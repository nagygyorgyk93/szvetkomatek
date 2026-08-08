# -*- coding: utf-8 -*-
"""2e/04 — D altema: szinusz- es koszinusztetel (D1), haromszog megoldasa es
alkalmazasok (D2). Mentor: Szürke Janka."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra

T = dict(tagozat="2e", mappa="04-trigonometrikus-fuggvenyek",
         temakor="Trigonometrikus függvények")
FGY = "feladatok-haromszogek.html"

# ---------------------------------------------------------------- önteszt
from sympy import Rational as R, pi, sqrt, sin, cos, acos, asin, rad, deg, N, simplify
E = []
def chk(n, g, w, tol=1e-3):
    if abs(float(g) - w) > tol:
        E.append((n, float(g), w))
# ASA: α=40°, β=75°, a=12
A, B = rad(40), rad(75); G = pi - A - B
chk("ASA-g", deg(G), 65.0)
chk("ASA-b", 12*sin(B)/sin(A), 18.03257)
chk("ASA-c", 12*sin(G)/sin(A), 16.91958)
# SAS: b=7, c=10, α=60°
aa = sqrt(7**2 + 10**2 - 2*7*10*cos(rad(60)))
chk("SAS-a", aa, 8.888194)
chk("SAS-b", deg(asin(7*sin(rad(60))/aa)), 43.004)
# SSS: a=6, b=7, c=9
chk("SSS-cg", R(6**2 + 7**2 - 9**2, 2*6*7), 0.0476190)
chk("SSS-g", deg(acos(R(6**2 + 7**2 - 9**2, 2*6*7))), 87.271)
chk("SSS-a", deg(acos(R(7**2 + 9**2 - 6**2, 2*7*9))), 41.752)
# terület
chk("T", R(1, 2)*8*11*sin(rad(35)), 25.23736)
# torony
ATB = pi - rad(32) - (pi - rad(48))
chk("torony-sz", deg(ATB), 16.0)
chk("torony-BT", 50*sin(rad(32))/sin(ATB), 96.12617)
chk("torony-h", 50*sin(rad(32))/sin(ATB)*sin(rad(48)), 71.43567)
# navigáció
chk("nav", sqrt(30**2 + 40**2 - 2*30*40*cos(rad(65))), 38.54499)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák


def svg_haromszog(cimkek=("A", "B", "C"), oldalak=("c", "a", "b"), szogek=("α", "β", "γ"),
                  P=((60, 200), (330, 200), (230, 55)), w=400, h=250,
                  leiras="Háromszög jelölései", magassag=None):
    (ax, ay), (bx, by), (cx, cy) = P
    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}">']
    if magassag:
        ki.append(f'  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{ay}" stroke="#94a3b8" '
                  'stroke-width="1.4" stroke-dasharray="5 4"/>')
        ki.append(f'  <rect x="{cx}" y="{ay - 11}" width="11" height="11" fill="none" '
                  'stroke="#94a3b8" stroke-width="1"/>')
        ki.append(f'  <text x="{cx + 8}" y="{(cy + ay)/2:.0f}" font-size="11" '
                  f'fill="#64748b">{magassag}</text>')
    ki.append(f'  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#f1f5f9" '
              'stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>')
    for (x, y), t, dx, dy in ((P[0], cimkek[0], -14, 6), (P[1], cimkek[1], 10, 6),
                              (P[2], cimkek[2], 0, -12)):
        ki.append(f'  <text x="{x + dx}" y="{y + dy}" font-size="14" font-weight="700" '
                  f'fill="#0f172a" text-anchor="middle">{t}</text>')
    kozep = (((ax + bx)/2, (ay + by)/2 + 17), ((bx + cx)/2 + 16, (by + cy)/2),
             ((ax + cx)/2 - 16, (ay + cy)/2))
    for (x, y), t in zip(kozep, oldalak):
        ki.append(f'  <text x="{x:.0f}" y="{y:.0f}" font-size="13" font-style="italic" '
                  f'fill="#047857" text-anchor="middle">{t}</text>')
    belso = ((ax + 26, ay - 8), (bx - 28, by - 8), (cx + 2, cy + 26))
    for (x, y), t in zip(belso, szogek):
        ki.append(f'  <text x="{x:.0f}" y="{y:.0f}" font-size="12" fill="#3b82f6" '
                  f'text-anchor="middle">{t}</text>')
    ki.append('</svg>')
    return "\n".join(ki)


SVG_HSZ = svg_haromszog(leiras="A háromszög szokásos jelölései: az oldal a vele "
                               "szemközti szög betűjét kapja")
SVG_TER = svg_haromszog(leiras="A háromszög területe két oldalból és a közbezárt szögből",
                        magassag="m")
SVG_TORONY = ('<svg viewBox="0 0 460 240" width="460" height="240" role="img" '
              'aria-label="Toronymagasság meghatározása két mérési pontból">\n'
              '  <line x1="30" y1="200" x2="430" y2="200" stroke="#0f172a" stroke-width="1.8"/>\n'
              '  <line x1="360" y1="200" x2="360" y2="60" stroke="#0f172a" stroke-width="2.4"/>\n'
              '  <rect x="360" y="60" width="11" height="11" fill="none" stroke="#94a3b8"/>\n'
              '  <line x1="70" y1="200" x2="360" y2="60" stroke="#3b82f6" stroke-width="1.6"/>\n'
              '  <line x1="215" y1="200" x2="360" y2="60" stroke="#ef4444" stroke-width="1.6"/>\n'
              '  <circle cx="70" cy="200" r="4" fill="#3b82f6"/>\n'
              '  <circle cx="215" cy="200" r="4" fill="#ef4444"/>\n'
              '  <text x="70" y="218" font-size="12" fill="#3b82f6" text-anchor="middle">A</text>\n'
              '  <text x="215" y="218" font-size="12" fill="#ef4444" text-anchor="middle">B</text>\n'
              '  <text x="360" y="218" font-size="12" fill="#0f172a" text-anchor="middle">T</text>\n'
              '  <text x="142" y="218" font-size="11" fill="#475569" text-anchor="middle">'
              '50 m</text>\n'
              '  <text x="98" y="194" font-size="11" fill="#3b82f6">32°</text>\n'
              '  <text x="240" y="194" font-size="11" fill="#ef4444">48°</text>\n'
              '  <text x="374" y="135" font-size="12" font-style="italic" fill="#047857">'
              'h</text>\n'
              '</svg>')

# ===================================================================== D1

D1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> Bemérés. Ez a legrégibb és legpraktikusabb feladat: '
         'ismerek <b>néhány</b> adatot egy háromszögből, és tudni akarom a többit. '
         'Nem kell derékszög, nem kell hozzáférnem a célponthoz — elég két mérési pont '
         'és egy szögmérő. Két tétel visz el idáig, és mindegyiknek pontosan megvan '
         'a maga helyzete.'),
   abra(SVG_HSZ, "A megszokott jelölés: az $a$ oldal az $\\alpha$ szöggel <b>szemközt</b> "
                 "van, a $b$ a $\\beta$-val, a $c$ a $\\gamma$-val."),
 ]),

 ("A szinusztétel", [
   doboz("tetel", "Szinusztétel",
         '<p>Bármely háromszögben</p>'
         '$$\\frac{a}{\\sin\\alpha}=\\frac{b}{\\sin\\beta}=\\frac{c}{\\sin\\gamma}=2R,$$'
         '<p>ahol $R$ a háromszög <b>köré írt</b> körének sugara.</p>'
         '<p>Szavakban: <b>az oldalak úgy aránylanak egymáshoz, mint a velük szemközti '
         'szögek szinuszai</b>. Külön tény — bár nem közvetlenül ebből következik —, hogy a '
         'leghosszabb oldallal szemben van a legnagyobb szög.</p>',
         hid="tetel-szinusztetel",
         lenyilo=("Miért igaz?",
                  '<p>Húzzuk be a $C$ csúcsból az $m$ magasságot az $AB$ oldalra. Az így '
                  'keletkező két derékszögű háromszögből</p>'
                  '$$m=b\\sin\\alpha\\quad\\text{és}\\quad m=a\\sin\\beta,$$'
                  '<p>tehát $b\\sin\\alpha=a\\sin\\beta$, ami átrendezve épp '
                  '$\\dfrac{a}{\\sin\\alpha}=\\dfrac{b}{\\sin\\beta}$.</p>')),
   doboz("tetel", "Mikor használjuk?",
         '<p>Akkor, ha van egy <b>teljes oldal–szög pár</b> (egy oldal és a vele '
         'szemközti szög):</p>'
         '<ul>'
         '<li><b>ASA / AAS</b> (a betűk angolul: S = <i>side</i> = oldal, A = <i>angle</i> = szög — vigyázz, ez épp fordítva van, mint az elsős egybevágósági tételek magyar OSO/SOS jelölésében) — két szög és egy oldal. A harmadik szög a '
         '$180^\\circ$-ból jön, a hiányzó oldalak a szinusztételből.</li>'
         '<li><b>SSA</b> — két oldal és az egyikkel szemközti szög. ⚠️ Ez a '
         '<b>kétértelmű</b> eset.</li>'
         '</ul>',
         hid="tetel-mikor-szinusz"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg a háromszöget: $\\alpha=40^\\circ$, $\\beta=75^\\circ$, $a=12$. '
         '(A szögfüggvényeket öt, az oldalakat két tizedesre kerekítsd.)</p>',
         hid="pelda-szinusztetel",
         lenyilo=("Megoldás",
                  '<p>A harmadik szög: $\\gamma=180^\\circ-40^\\circ-75^\\circ=65^\\circ$.</p>'
                  '$$b=\\frac{a\\sin\\beta}{\\sin\\alpha}=\\frac{12\\cdot 0{,}96593}'
                  '{0{,}64279}\\approx\\boxed{18{,}03}$$'
                  '$$c=\\frac{a\\sin\\gamma}{\\sin\\alpha}=\\frac{12\\cdot 0{,}90631}'
                  '{0{,}64279}\\approx\\boxed{16{,}92}$$'
                  '<p><b>Ellenőrzés:</b> a legnagyobb szög $\\beta=75^\\circ$, és valóban '
                  'a $b$ a leghosszabb oldal ✔</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>A kétértelmű (SSA) eset.</b> Ha két oldalt és a <b>kisebbikkel</b> '
         'szemközti szöget ismerjük, két különböző háromszög is illeszkedhet az adatokra — '
         'mert $\\sin\\varphi=\\sin(180^\\circ-\\varphi)$.</p>'
         '<p><b>Mikor egyértelmű, és mikor nem?</b> Ha a megadott szög a <b>hosszabbik</b> oldallal szemközt van, a másik szög biztosan hegyes — a megoldás egyértelmű. Ha viszont a megadott szög a <b>rövidebbik</b> oldallal szemközti (legyen $\\alpha$ az $a$-val szemközt, és $b&gt;a$), akkor a $C$ csúcsból az $AB$-re állított magasság $m=b\\sin\\alpha$, és <b>három</b> eset van:</p>'
         '<ul>'
         '<li>$a&lt;b\\sin\\alpha$ → <b>nincs</b> ilyen háromszög (a számolásban $\\sin\\beta&gt;1$ jönne ki),</li>'
         '<li>$a=b\\sin\\alpha$ → <b>pontosan egy</b>, és az derékszögű ($\\beta=90^\\circ$),</li>'
         '<li>$b\\sin\\alpha&lt;a&lt;b$ → <b>két</b> különböző háromszög.</li>'
         '</ul>'
         '<p>A gyakorlati ellenőrzés egyszerű: ha $\\sin\\beta&gt;1$ adódik, nincs megoldás; ha két $\\beta$ is szóba jön, azt tartsd meg, amelyre $\\alpha+\\beta&lt;180^\\circ$ — csak akkor marad pozitív érték a harmadik szögnek. Ha mindkettőre teljesül, valóban két háromszög létezik.</p>'
         '<p><b>Példa.</b> Legyen $a=6$, $b=8$ és $\\alpha=40^\\circ$ (a megadott szög a rövidebb oldallal szemközt). A szinusztételből $\\sin\\beta=\\dfrac{8\\sin 40^\\circ}{6}\\approx 0{,}857$, ahonnan $\\beta\\approx 59^\\circ$ <b>vagy</b> $\\beta\\approx 121^\\circ$. Mindkettő működik: $40+59=99&lt;180$ és $40+121=161&lt;180$ — tehát <b>két</b> különböző háromszög is illeszkedik az adatokra.</p>'),
 ]),

 ("A koszinusztétel", [
   doboz("tetel", "Koszinusztétel",
         '$$a^{2}=b^{2}+c^{2}-2bc\\cos\\alpha$$'
         '$$b^{2}=a^{2}+c^{2}-2ac\\cos\\beta,\\qquad c^{2}=a^{2}+b^{2}-2ab\\cos\\gamma$$'
         '<p>Ez a <b>Pitagorasz-tétel általánosítása</b>: ha $\\alpha=90^\\circ$, akkor '
         '$\\cos\\alpha=0$, és marad $a^{2}=b^{2}+c^{2}$.</p>'
         '<p>Átrendezve a szög is kifejezhető:</p>'
         '$$\\cos\\alpha=\\frac{b^{2}+c^{2}-a^{2}}{2bc}.$$',
         hid="tetel-koszinusztetel"),
   doboz("tetel", "Mikor használjuk?",
         '<p>Akkor, ha <b>nincs</b> teljes oldal–szög pár:</p>'
         '<ul>'
         '<li><b>SAS</b> — két oldal és a <b>közbezárt</b> szög → a harmadik oldal.</li>'
         '<li><b>SSS</b> — mindhárom oldal → bármelyik szög.</li>'
         '</ul>'
         '<p>Utána már van teljes pár, tehát a többit a szinusztétellel is folytathatod — de <b>mindig a kisebbik oldal szögére</b> alkalmazd, mert az biztosan hegyesszög, tehát ott nincs kétértelműség. A harmadik szög $180^\\circ$-ból jön.</p>',
         hid="tetel-mikor-koszinusz"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p><b>a)</b> $b=7$, $c=10$, $\\alpha=60^\\circ$ — mekkora $a$?<br>'
         '<b>b)</b> $a=6$, $b=7$, $c=9$ — mekkora $\\gamma$?</p>',
         hid="pelda-koszinusztetel",
         lenyilo=("Megoldás",
                  '<p><b>a)</b> $a^{2}=49+100-2\\cdot 7\\cdot 10\\cdot 0{,}5=149-70=79$, '
                  'tehát $a=\\sqrt{79}\\approx\\boxed{8{,}89}$.</p>'
                  '<p><b>b)</b> A $\\gamma$ a $c=9$ oldallal szemközt van:</p>'
                  '$$\\cos\\gamma=\\frac{36+49-81}{2\\cdot 6\\cdot 7}=\\frac{4}{84}'
                  '\\approx 0{,}04762\\ \\Longrightarrow\\ \\gamma\\approx\\boxed{87{,}27^\\circ}$$'
                  '<p>A $\\cos\\gamma$ <b>pozitív</b>, tehát a szög hegyesszög — épp csak.</p>')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Az oldal és a szög nem cserélhető fel!</b> A bal oldalon álló oldal mindig azzal a '
         'szöggel van párban, amely a jobb oldalon a koszinuszban szerepel. A '
         '$-2bc\\cos\\alpha$ tagban a $b$ és a $c$ épp a <b>másik két</b> oldal — ők '
         'egymással nyugodtan felcserélhetők, a szorzatuk ugyanaz.</p>'
         '<p>És ha a $\\cos$ eredménye <b>negatív</b>, az nem hiba: azt jelenti, hogy a '
         'szög <b>tompaszög</b>. Ilyenkor a számológép helyesen ad $90^\\circ$ fölötti '
         'értéket.</p>'),
   kviz('Melyik tétel kell, ha $a=5$, $b=8$ és $\\gamma=40^\\circ$ ismert?',
        ['Koszinusztétel', 'Szinusztétel', 'Pitagorasz-tétel'], 0,
        jo="✔ Két oldal és a közbezárt szög (SAS) → koszinusztétel.",
        nem="✘ Nincs teljes oldal–szög pár, viszont a szög a két oldal KÖZÖTT van → koszinusztétel."),
   gyakorolj(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Szürke Janka:</b> A két tétel a kezedben van. Már csak azt kell eldöntened, <b>melyiket mikor</b> vedd elő — és ha ez megy, a terepen bármilyen háromszöget be tudsz mérni: tornyot, hegyoldalt, folyószélességet.', outro=True),
 ]),
]

# ===================================================================== D2

D2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Szürke Janka:</b> Utolsó bevetés. Most már mindkét tétel a kezedben van — '
         'a kérdés csak az, <b>melyiket mikor</b>. Van rá egy egyszerű recept, és ha '
         'követed, bármelyik háromszög megoldható. Utána pedig jön a legjobb rész: '
         'ezzel a tudással megmérhető egy torony magassága anélkül, hogy '
         'hozzáérnél.'),
 ]),

 ("A háromszög megoldása — a döntési recept", [
   doboz("tetel", "Melyik tétel kell?",
         '<div class="tblwrap"><table>'
         '<tr><th>Ismert adatok</th><th>Első lépés</th><th>Folytatás</th></tr>'
         '<tr><td><b>ASA / AAS</b><br>két szög + egy oldal</td>'
         '<td>a harmadik szög $180^\\circ$-ból</td><td>szinusztétel a két oldalra</td></tr>'
         '<tr><td><b>SAS</b><br>két oldal + közbezárt szög</td>'
         '<td>koszinusztétel a harmadik oldalra</td>'
         '<td>szinusztétel a <b>kisebbik</b> oldal szögére, a harmadik $180^\\circ$-ból</td></tr>'
         '<tr><td><b>SSS</b><br>három oldal</td><td>koszinusztétel a <b>legnagyobb</b> '
         'oldal szögére</td><td>szinusztétel a másodikra, a harmadik $180^\\circ$-ból</td></tr>'
         '<tr><td><b>SSA</b><br>két oldal + nem közbezárt szög</td>'
         '<td>szinusztétel</td><td>⚠️ ellenőrizd, van-e <b>két</b> megoldás</td></tr>'
         '</table></div>'
         '<p>A háromszög akkor és csak akkor létezik, ha a szögek összege '
         '$180^\\circ$, és teljesül a <b>háromszög-egyenlőtlenség</b>: bármely két oldal '
         'összege nagyobb a harmadiknál.</p>',
         hid="tetel-recept"),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p><b>Miért a legnagyobb oldal szögével kezdünk SSS-nél?</b> Mert az lehet '
         'tompaszög — és a koszinusztétel a tompaszöget is helyesen adja vissza '
         '(negatív koszinusszal). Ha utána a szinusztételt már csak <b>kisebb</b> '
         'oldalakra használod, azok biztosan hegyesszögek, tehát nincs kétértelműség.</p>'
         '<p>És a kerekítés: a <b>szögfüggvényértékeket</b> öt tizedesre, az '
         '<b>oldalhosszakat</b> két tizedesre — ha a köztes értékeket túl korán kerekíted, '
         'a végeredmény több tizedessel is elcsúszhat.</p>'),
 ]),

 ("A háromszög területe", [
   abra(SVG_TER, "A $T=\\tfrac{a\\cdot m}{2}$ képletben a magasság kifejezhető: "
                 "$m=b\\sin\\gamma$ — innen jön a trigonometrikus területképlet."),
   doboz("tetel", "Terület két oldalból és a közbezárt szögből",
         '$$T=\\frac{1}{2}ab\\sin\\gamma=\\frac{1}{2}bc\\sin\\alpha=\\frac{1}{2}ac\\sin\\beta$$'
         '<p>A szögnek mindig a <b>két megadott oldal közötti</b> szögnek kell lennie.</p>',
         hid="tetel-terulet"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Mekkora annak a háromszögnek a területe, amelyben $a=8$, $b=11$ és a '
         'közbezárt szög $\\gamma=35^\\circ$?</p>',
         hid="pelda-terulet",
         lenyilo=("Megoldás",
                  '$$T=\\frac12\\cdot 8\\cdot 11\\cdot\\sin 35^\\circ=44\\cdot 0{,}57358'
                  '\\approx\\boxed{25{,}24}$$'
                  '<p>(területegység)</p>')),
   kviz('Melyik adatokból számolható a háromszög területe a $T=\\tfrac12ab\\sin\\gamma$ képlettel?',
        ['Két oldal és a KÖZBEZÁRT szög', 'Két oldal és bármelyik szög',
         'Három oldal'], 0,
        jo="✔ A szögnek a két megadott oldal KÖZÖTT kell lennie — a képletben a gamma "
           "épp az a és b által bezárt szög.",
        nem="✘ A képlet csak a két oldal ÁLTAL BEZÁRT szöggel működik. Ha a szög máshol "
            "van, előbb a szinusztétellel kell a hiányzó adatot megkeresni."),
 ]),

 ("Alkalmazások: bemérés a terepen", [
   doboz("pelda", "Vészterem-szimuláció — a torony magassága",
         '<p>Egy torony tövéhez nem tudunk odajutni. Az $A$ pontból a torony '
         'csúcsát $32^\\circ$-os emelkedési szögben látjuk; $50$ métert közelebb menve, '
         'a $B$ pontból már $48^\\circ$-osban. Milyen magas a torony?</p>',
         hid="pelda-torony",
         lenyilo=("Megoldás",
                  '<p>Nézzük az $ABT$ háromszöget ($T$ a torony csúcsa). Az $A$-nál lévő '
                  'szög $32^\\circ$. A $B$-nél lévő <b>belső</b> szög a $48^\\circ$ '
                  'mellékszöge: $180^\\circ-48^\\circ=132^\\circ$. Ezért</p>'
                  '$$\\angle ATB=180^\\circ-32^\\circ-132^\\circ=16^\\circ.$$'
                  '<p>Szinusztétel az $ABT$ háromszögben:</p>'
                  '$$BT=\\frac{AB\\cdot\\sin 32^\\circ}{\\sin 16^\\circ}='
                  '\\frac{50\\cdot 0{,}52992}{0{,}27564}\\approx 96{,}13\\ \\text{m}$$'
                  '<p>Végül a $BT$ szakaszból a derékszögű háromszögben:</p>'
                  '$$h=BT\\cdot\\sin 48^\\circ\\approx 96{,}13\\cdot 0{,}74314'
                  '\\approx\\boxed{71{,}44\\ \\text{m}}$$')),
   abra(SVG_TORONY, "A két mérési pont és a torony egyetlen háromszöget alkot — "
                    "a $16^\\circ$-os csúcsszög a két emelkedési szög <b>különbsége</b>."),
   doboz("pelda", "Vészterem-szimuláció — navigáció",
         '<p>Egy hajó a kikötőből $30$ km-t halad egyenesen, majd $115^\\circ$-kal '
         'elfordul, és további $40$ km-t tesz meg. Milyen messze van a kikötőtől?</p>',
         hid="pelda-navigacio",
         lenyilo=("Megoldás",
                  '<p>A két útszakasz és a keresett távolság háromszöget alkot. A '
                  '<b>belső</b> szög nem $115^\\circ$, hanem a mellékszöge: '
                  '$180^\\circ-115^\\circ=65^\\circ$.</p>'
                  '$$d^{2}=30^{2}+40^{2}-2\\cdot 30\\cdot 40\\cdot\\cos 65^\\circ'
                  '=2500-2400\\cdot 0{,}42262\\approx 1485{,}7$$'
                  '$$d\\approx\\boxed{38{,}54\\ \\text{km}}$$'
                  '<p>⚠️ Az „elfordul $115^\\circ$-kal” az <b>iránytól</b> való eltérés — '
                  'a háromszög belső szöge ennek a mellékszöge. Ez a leggyakoribb hiba a '
                  'navigációs feladatokban.</p>')),
   doboz("erdekesseg", "Így mérték meg a Földet",
         '<p>A <b>háromszögelés</b> évszázadokig a térképészet alapmódszere volt: '
         'kijelöltek egy pontosan lemért alapvonalat, majd szögméréssel, '
         'szinusztétellel terjeszkedtek tovább, háromszögről háromszögre. Így készült '
         'a Nagy Trigonometriai Felmérés Indiában is, amely a Mount Everest magasságát '
         'megadta — $8840$ méternek, alig $8$ méterrel a mai értéktől.</p>'),
   kviz('Egy háromszögben $a=6$, $b=9$, $\\gamma=30^\\circ$. Mekkora a területe?',
        ['$13{,}5$', '$27$', '$54$'], 0,
        jo="✔ T = ½ · 6 · 9 · sin 30° = 27 · 0,5 = 13,5.",
        nem="✘ T = ½ab sin γ = ½ · 6 · 9 · 0,5 = 13,5."),
   gyakorolj(FGY + "#alap-6", "A 6–14", FGY + "#kozep-5", "K 5–13"),
   brief('<b>Szürke Janka:</b> A Fázisugrás teljesítve, kadétok — és ezzel a második évad '
         'is a végéhez ért. Ez az anyag a <b>4. írásbeli dolgozat</b> teljes terjedelme. '
         'Nézd át a taktikai memóriakártyát, aztán jöhet a terepküldetés: '
         'egy valódi jelet kell megfejtened, és be kell mérned egy bázist.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

KI = [
 lap(**T, fajl="tananyag-szinusz-es-koszinusztetel.html",
     cim="Szinusz- és koszinusztétel", cim_tiszta="Szinusz- és koszinusztétel",
     alcim="A két tétel, a bizonyítás gondolata, és a legfontosabb kérdés: "
           "melyiket mikor kell használni.",
     chip="A Fázisugrás · 10/11", szakaszok=D1,
     elozo=("feladatok-trig-fuggvenyek-egyenletek.html", "Feladatok — függvények és egyenletek"),
     kovetkezo=("tananyag-haromszog-megoldasa.html", "Háromszög megoldása és alkalmazások")),
 lap(**T, fajl="tananyag-haromszog-megoldasa.html",
     cim="Háromszög megoldása és alkalmazások",
     cim_tiszta="Háromszög megoldása és alkalmazások",
     alcim="A négy alapeset döntési receptje, a trigonometrikus területképlet, "
           "valamint magasság- és távolságmérés a terepen.",
     chip="A Fázisugrás · 11/11", szakaszok=D2,
     elozo=("tananyag-szinusz-es-koszinusztetel.html", "Szinusz- és koszinusztétel"),
     kovetkezo=(FGY, "Feladatok — háromszögek")),
]
for u in KI:
    print("✓", os.path.basename(u))
