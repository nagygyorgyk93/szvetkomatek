# -*- coding: utf-8 -*-
"""2e / 01 — „C" altéma: komplex szám fogalma (C1), műveletek (C2),
i hatványai és egyenletek (C3). Mentor: X. Károly professzor."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra

T = dict(tagozat="2e", mappa="01-hatvanyozas-gyokvonas-komplex-szamok",
         temakor="Hatványozás, gyökvonás, komplex számok")
FGY = "feladatok-komplex-szamok.html"

# ------------------------------------------------------------- Gauss-sík SVG

def gauss_sik():
    ox, oy, e = 148, 132, 34          # origó és egységnyi hossz
    zx, zy = ox + 3 * e, oy - 2 * e   # z = 3 + 2i
    kx, ky = ox + 3 * e, oy + 2 * e   # konjugált
    r = []
    r.append('<svg viewBox="0 0 360 262" width="360" height="262" role="img" '
             'aria-label="A z = 3 + 2i komplex szám és konjugáltja a Gauss-síkon, '
             'a modulussal mint helyvektor-hosszal">')
    r.append('  <defs><marker id="ny2" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" '
             'markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker>'
             '<marker id="ny3" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
             'markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#047857"/></marker></defs>')
    r.append('  <g stroke="#cbd5e1" stroke-width=".6">')
    for k in range(-3, 6):
        if k:
            r.append(f'    <line x1="{ox + k * e}" y1="18" x2="{ox + k * e}" y2="246"/>')
    for k in range(-3, 4):
        if k:
            r.append(f'    <line x1="16" y1="{oy + k * e}" x2="344" y2="{oy + k * e}"/>')
    r.append('  </g>')
    r.append(f'  <line x1="16" y1="{oy}" x2="344" y2="{oy}" stroke="#0f172a" stroke-width="1.4" '
             'marker-end="url(#ny2)"/>')
    r.append(f'  <line x1="{ox}" y1="246" x2="{ox}" y2="18" stroke="#0f172a" stroke-width="1.4" '
             'marker-end="url(#ny2)"/>')
    r.append(f'  <text x="338" y="{oy + 16}" font-size="11" fill="#0f172a" text-anchor="end">Re</text>')
    r.append(f'  <text x="{ox - 8}" y="28" font-size="11" fill="#0f172a" text-anchor="end">Im</text>')
    for k in (1, 2, 3, 4):
        r.append(f'  <text x="{ox + k * e}" y="{oy + 14}" font-size="10" fill="#475569" '
                 f'text-anchor="middle">{k}</text>')
    for k, cim in ((1, "1"), (2, "2"), (-2, "−2")):
        r.append(f'  <text x="{ox - 6}" y="{oy - k * e + 4}" font-size="10" fill="#475569" '
                 f'text-anchor="end">{cim}</text>')
    # segédvonalak
    r.append(f'  <line x1="{zx}" y1="{zy}" x2="{zx}" y2="{oy}" stroke="#94a3b8" stroke-width="1" '
             'stroke-dasharray="4 3"/>')
    r.append(f'  <line x1="{zx}" y1="{zy}" x2="{ox}" y2="{zy}" stroke="#94a3b8" stroke-width="1" '
             'stroke-dasharray="4 3"/>')
    r.append(f'  <line x1="{zx}" y1="{zy}" x2="{kx}" y2="{ky}" stroke="#f59e0b" stroke-width="1.2" '
             'stroke-dasharray="3 3"/>')
    # helyvektor
    r.append(f'  <line x1="{ox}" y1="{oy}" x2="{zx}" y2="{zy}" stroke="#047857" stroke-width="2.2" '
             'marker-end="url(#ny3)"/>')
    r.append(f'  <circle cx="{zx}" cy="{zy}" r="4" fill="#047857"/>')
    r.append(f'  <circle cx="{kx}" cy="{ky}" r="4" fill="#0f172a" fill-opacity=".55"/>')
    r.append(f'  <text x="{zx + 9}" y="{zy - 6}" font-size="12" fill="#047857" '
             'font-weight="600">z = 3 + 2i</text>')
    r.append(f'  <text x="{kx + 9}" y="{ky + 16}" font-size="12" fill="#334155">z̄ = 3 − 2i</text>')
    r.append(f'  <text x="{ox + 34}" y="{oy - 40}" font-size="12" fill="#047857" '
             'font-style="italic">|z| = √13</text>')
    r.append('</svg>')
    return "\n".join(r)


# =====================================================================  C1

C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>X. Károly professzor:</b> Kadét, üljön le. Amit most mondok, az kezdetben '
         'képtelenségnek fog hangzani — pontosan úgy, ahogy a negatív számok hangzottak '
         'képtelenségnek, amíg valaki ki nem mondta, hogy „tartozás". '
         'Az $x^{2}=-1$ egyenletnek <b>nincs</b> valós megoldása. Ez nem a mi hibánk, és nem is az '
         'egyenleté: a valós számok halmaza egyszerűen <b>kicsi</b> hozzá. '
         'Dr. Baljós már régen kilépett belőle. Most mi is kilépünk.'),
   'A matematika története bővítések sorozata: valahányszor felírtunk egy egyenletet, '
   'amit az addig ismert számokkal nem lehetett megoldani, <b>kibővítettük a számhalmazt</b>. '
   'A komplex számok ennek a sornak az utolsó — és legmeglepőbb — lépése.',
 ]),

 ("Miért kell bővíteni a számhalmazt?", [
   'Nézd meg a mintát: minden lépésben egy „megoldhatatlan" egyenlet kényszerít ki '
   'egy új számfajtát.',
   doboz("erdekesseg", "A számhalmazok építkezése",
         '<div class="tblwrap"><table>'
         '<tr><th>Egyenlet</th><th>Megoldhatatlan itt…</th><th>…ezért bővítünk ide</th></tr>'
         '<tr><td>$x+3=1$</td><td>$\\mathbb{N}$ — természetes számok</td>'
         '<td>$\\mathbb{Z}$ — negatív számok</td></tr>'
         '<tr><td>$2x=1$</td><td>$\\mathbb{Z}$ — egész számok</td>'
         '<td>$\\mathbb{Q}$ — törtek</td></tr>'
         '<tr><td>$x^{2}=2$</td><td>$\\mathbb{Q}$ — racionális számok</td>'
         '<td>$\\mathbb{R}$ — irracionális számok</td></tr>'
         '<tr><td>$x^{2}=-1$</td><td>$\\mathbb{R}$ — valós számok</td>'
         '<td>$\\mathbb{C}$ — <b>komplex számok</b></td></tr>'
         '</table></div>'
         '<p>Miért nincs valós megoldása az utolsónak? Mert minden valós $x$-re $x^{2}\\ge 0$ — '
         'ezt épp az előző egységben láttuk a hatványfüggvény grafikonján.</p>'),
   'A bővítés módja mindig ugyanaz: <b>bevezetünk</b> egy új objektumot, kimondjuk róla, '
   'mit tud, és megköveteljük, hogy a régi számolási szabályok érvényben maradjanak.',
 ]),

 ("A képzetes egység és az algebrai alak", [
   doboz("definicio", "A képzetes egység",
         '<p>Vezessük be azt az $i$-vel jelölt <b>képzetes egységet</b>, amelyre</p>'
         '$$i^{2}=-1.$$'
         '<p>Ezzel az $x^{2}=-1$ egyenlet megoldásai $x_{1}=i$ és $x_{2}=-i$, '
         'az $x^{2}=-9$ egyenletéi pedig $x_{1,2}=\\pm 3i$, hiszen $(3i)^{2}=9i^{2}=-9$.</p>',
         hid="def-kepzetes-egyseg"),
   doboz("definicio", "Komplex szám, algebrai alak",
         '<p><b>Komplex számnak</b> nevezzük az $z=x+yi$ alakú kifejezéseket, ahol '
         '$x,y\\in\\mathbb{R}$. A komplex számok halmaza:</p>'
         '$$\\mathbb{C}=\\left\\{\\,x+yi \\mid x,y\\in\\mathbb{R}\\ \\wedge\\ i^{2}=-1\\,\\right\\}.$$'
         '<p>Itt $x=\\operatorname{Re}(z)$ a $z$ <b>valós része</b>, $y=\\operatorname{Im}(z)$ '
         'pedig a <b>képzetes (imaginárius) része</b>. Figyelem: a képzetes rész is '
         '<b>valós szám</b> — nem tartozik hozzá az $i$!</p>',
         hid="def-komplex-szam"),
   doboz("tetel", "Két komplex szám egyenlősége",
         '<p>Ha $z_{1}=x_{1}+y_{1}i$ és $z_{2}=x_{2}+y_{2}i$, akkor</p>'
         '$$z_{1}=z_{2}\\iff x_{1}=x_{2}\\ \\wedge\\ y_{1}=y_{2}.$$'
         '<p>Vagyis <b>egy</b> komplex egyenlőség <b>két</b> valós egyenletet jelent — '
         'ez lesz a fegyverünk a $z$-t és $\\bar z$-t egyszerre tartalmazó egyenleteknél.</p>',
         hid="tetel-komplex-egyenloseg"),
   doboz("erdekesseg", "Minden valós szám komplex is",
         '<p>Ha $y=0$, akkor $z=x$ — közönséges valós szám. Ha viszont $x=0$ és $y\\neq0$, '
         'akkor $z=yi$ <b>tisztán képzetes</b>. Tehát $\\mathbb{R}\\subset\\mathbb{C}$: '
         'nem elvesztettük a régi számokat, hanem <b>beágyaztuk</b> őket egy nagyobb világba.</p>'),
   kviz('Mennyi az $z=-4+7i$ szám valós és képzetes része?',
        ['$\\operatorname{Re}(z)=-4$, $\\operatorname{Im}(z)=7$',
         '$\\operatorname{Re}(z)=-4$, $\\operatorname{Im}(z)=7i$',
         '$\\operatorname{Re}(z)=4$, $\\operatorname{Im}(z)=7$'], 0,
        jo="✔ A képzetes rész az i EGYÜTTHATÓJA — maga is valós szám.",
        nem="✘ Re(z) az i nélküli tag (−4), Im(z) pedig az i együtthatója (7), i nélkül."),
 ]),

 ("A komplex számsík", [
   'Egy komplex számot <b>két</b> valós adat határoz meg: a valós és a képzetes része. '
   'Két adat pedig természetes módon egy <b>pontot</b> jelöl ki a síkon. Ezt a szemléltetést '
   '<b>Gauss-síknak</b> vagy komplex számsíknak hívjuk: a vízszintes tengelyen a valós rész, '
   'a függőlegesen a képzetes rész.',
   abra(gauss_sik(),
        "A $z=3+2i$ szám a $(3;2)$ pontnak felel meg. A helyvektor hossza a <b>modulusz</b>, "
        "a valós tengelyre vett tükörkép pedig a <b>konjugált</b>."),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Hol helyezkednek el a Gauss-síkon a $z_{1}=2$, $z_{2}=-3i$ és $z_{3}=-1+i$ számok?</p>',
         lenyilo=("Megoldás",
                  '<p>$z_{1}=2$ valós szám → a valós tengelyen, a $(2;0)$ pontban. '
                  '$z_{2}=-3i$ tisztán képzetes → a képzetes tengelyen, a $(0;-3)$ pontban. '
                  '$z_{3}=-1+i$ → a $(-1;1)$ pontban, a második síknegyedben.</p>')),
 ]),

 ("Konjugált és modulusz", [
   doboz("definicio", "Konjugált komplex pár és modulusz",
         '<p>A $z=x+yi$ komplex szám</p>'
         '<ul>'
         '<li><b>konjugáltja</b>: $\\overline{z}=x-yi$ — a Gauss-síkon a valós tengelyre '
         'vett <b>tükörképe</b>;</li>'
         '<li><b>modulusza</b> (abszolút értéke): $|z|=\\sqrt{x^{2}+y^{2}}$ — a helyvektor '
         '<b>hossza</b>, vagyis a pont origótól mért távolsága.</li>'
         '</ul>'
         '<p>A modulusz mindig <b>nemnegatív valós</b> szám. A Pitagorasz-tétel adja: '
         'a befogók $|x|$ és $|y|$, az átfogó $|z|$.</p>',
         hid="def-konjugalt-modulusz"),
   doboz("tetel", "A legfontosabb összefüggés",
         '<p>Bármely $z=x+yi$ komplex számra</p>'
         '$$z\\cdot\\overline{z}=x^{2}+y^{2}=|z|^{2}.$$'
         '<p>Vagyis egy komplex szám és a konjugáltja szorzata <b>mindig valós</b> — sőt '
         'nemnegatív. Ez a tulajdonság teszi majd lehetővé a komplex számokkal való osztást, '
         'pontosan úgy, ahogy a $\\left(\\sqrt a+\\sqrt b\\right)\\left(\\sqrt a-\\sqrt b\\right)=a-b$ '
         'tette lehetővé a gyöktelenítést.</p>',
         hid="tetel-z-zkonj",
         lenyilo=("Levezetés",
                  '<p>$(x+yi)(x-yi)=x^{2}-xyi+xyi-y^{2}i^{2}=x^{2}-y^{2}\\cdot(-1)=x^{2}+y^{2}$. '
                  'A középső két tag kiesik — ez a négyzetek különbsége azonosság.</p>')),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Add meg $z=5-12i$ konjugáltját és moduluszát!</p>',
         hid="pelda-konjugalt",
         lenyilo=("Megoldás",
                  '<p>$\\overline{z}=5+12i$, és</p>'
                  '$$|z|=\\sqrt{5^{2}+(-12)^{2}}=\\sqrt{25+144}=\\sqrt{169}=13.$$'
                  '<p>Ellenőrzés: $z\\cdot\\overline z=(5-12i)(5+12i)=25+144=169=13^{2}$. ✔</p>')),
   kviz('Mennyi $|3-4i|$?',
        ['$5$', '$7$', '$\\sqrt{7}$'], 0,
        jo="✔ √(9 + 16) = √25 = 5.",
        nem="✘ A modulusz √(x² + y²) = √(9 + 16) = 5 — nem a részek összege."),
 ]),

 ("Egy jelölés, amivel vigyázni kell", [
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>A mutálódott kódban ez a „bizonyítás" szerepel:</p>'
         '$$-1=i^{2}=\\sqrt{-1}\\cdot\\sqrt{-1}\\overset{?}{=}\\sqrt{(-1)\\cdot(-1)}=\\sqrt{1}=1.$$'
         '<p>Tehát $-1=1$? Nyilván nem. A hiba a harmadik lépésben van: a '
         '$\\sqrt{a}\\cdot\\sqrt{b}=\\sqrt{ab}$ azonosság <b>csak $a,b\\ge 0$ esetén</b> érvényes — '
         'épp ezt a kikötést tettük a gyökvonás azonosságainál.</p>'
         '<p><b>Tanulság:</b> negatív szám négyzetgyökét ne írjuk $\\sqrt{-9}$ alakban. '
         'Helyette mondjuk azt, hogy az $x^{2}=-9$ egyenlet megoldásai $x_{1,2}=\\pm 3i$, '
         'vagy egyszerűen írjuk fel közvetlenül: $3i$. A gyökjel a komplex számok között '
         'nem egyértelmű — <b>két</b> szám négyzete is $-9$.</p>'),
   gyakorolj(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
   brief('<b>X. Károly professzor:</b> Megvan az új világ térképe. Most meg kell tanulnod <b>mozogni</b> '
         'benne: összeadni, szorozni, osztani. Meg fog lepni, mennyire ismerős lesz — '
         'úgy számolunk, mint a betűs kifejezésekkel, egyetlen extra szabállyal: '
         'ahol $i^{2}$-t látsz, oda $-1$-et írsz.',
         outro=True),
 ]),
]

# =====================================================================  C2

C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>X. Károly professzor:</b> A jó hír, kadét: nem kell új algebrát tanulnia. '
         'A komplex számokkal <b>pontosan úgy</b> számolunk, mint az $a+bx$ alakú kéttagú '
         'kifejezésekkel — összevonunk, kibontunk, nevezetes azonosságokat használunk. '
         'Egyetlen extra szabály van: valahányszor $i^{2}$ keletkezik, azonnal '
         'helyettesítse be, hogy $i^{2}=-1$. Ettől lesz a szorzat mindig ugyanolyan '
         '$x+yi$ alakú, mint amiből indultunk.'),
 ]),

 ("Összeadás és kivonás", [
   doboz("tetel", "Tagonként",
         '<p>Ha $z_{1}=x_{1}+y_{1}i$ és $z_{2}=x_{2}+y_{2}i$, akkor</p>'
         '$$z_{1}\\pm z_{2}=\\left(x_{1}\\pm x_{2}\\right)+\\left(y_{1}\\pm y_{2}\\right)i.$$'
         '<p>A valós részek a valós részekkel, a képzetesek a képzetesekkel — mint a '
         'hasonló tagok összevonása.</p>',
         hid="tetel-komplex-osszeadas"),
   doboz("erdekesseg", "Geometriai jelentés",
         '<p>A Gauss-síkon a komplex számok <b>helyvektorok</b>, és az összeadásuk pontosan '
         'a vektorok összeadása: a paralelogramma-szabály. Ezért viselkedik a komplex '
         'összeadás olyan „jól" — geometriailag eltolás.</p>'),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Legyen $z_{1}=5+3i$ és $z_{2}=2-7i$. Számítsd ki $z_{1}+z_{2}$ és $z_{1}-z_{2}$ értékét!</p>',
         lenyilo=("Megoldás",
                  '<p>$z_{1}+z_{2}=(5+2)+(3-7)i=7-4i$.</p>'
                  '<p>$z_{1}-z_{2}=(5-2)+\\left(3-(-7)\\right)i=3+10i$ — figyelj a '
                  'kivonásnál a <b>második</b> tag előjelére!</p>')),
 ]),

 ("Szorzás", [
   'Bontsuk ki a szorzatot úgy, ahogy két kéttagú kifejezést szoktunk, majd használjuk '
   'az $i^{2}=-1$ helyettesítést.',
   doboz("tetel", "A szorzás szabálya",
         '$$\\left(x_{1}+y_{1}i\\right)\\left(x_{2}+y_{2}i\\right)'
         '=\\left(x_{1}x_{2}-y_{1}y_{2}\\right)+\\left(x_{1}y_{2}+x_{2}y_{1}\\right)i$$'
         '<p>Nem érdemes bemagolni — elég kibontani és $i^{2}$ helyére $-1$-et írni. '
         'A képlet csak azt mutatja, hogy az eredmény <b>mindig</b> $x+yi$ alakú marad.</p>',
         hid="tetel-komplex-szorzas"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki: $(4+3i)(2-5i)$.</p>',
         hid="pelda-szorzas",
         lenyilo=("Megoldás",
                  '<p>Kibontva: $8-20i+6i-15i^{2}$. Mivel $i^{2}=-1$, a $-15i^{2}=+15$, tehát</p>'
                  '$$8+15+(-20+6)i=23-14i.$$')),
   doboz("csapda", "Dr. Baljós vírus-kódja",
         '<p>„$(2i)^{2}=2i^{2}=-2$." — <b>Hamis.</b> A négyzetre emelés a <b>teljes</b> '
         'tényezőre vonatkozik: $(2i)^{2}=2^{2}\\cdot i^{2}=4\\cdot(-1)=-4$. '
         'Ugyanez a hiba a $-15i^{2}$ kezelésénél: az eredmény $+15$, nem $-15$.</p>'),
   kviz('Mennyi $(1+i)^{2}$?',
        ['$2i$', '$1+i^{2}$', '$2+2i$'], 0,
        jo="✔ 1 + 2i + i² = 1 + 2i − 1 = 2i.",
        nem="✘ Bontsd ki: 1 + 2i + i², és i² = −1, tehát az eredmény 2i."),
 ]),

 ("Osztás — bővítés a konjugálttal", [
   'Mit jelent az, hogy $\\dfrac{5+i}{2-3i}$? A cél mindig ugyanaz: hozzuk az eredményt '
   '$x+yi$ alakra. Ehhez a <b>nevezőből el kell tüntetni az $i$-t</b> — és pontosan erre '
   'való a $z\\cdot\\overline z=|z|^{2}$ összefüggés.',
   doboz("tetel", "Az osztás algoritmusa",
         '<p>Bővítsük a törtet a <b>nevező konjugáltjával</b>:</p>'
         '$$\\frac{z_{1}}{z_{2}}=\\frac{z_{1}\\cdot\\overline{z_{2}}}'
         '{z_{2}\\cdot\\overline{z_{2}}}=\\frac{z_{1}\\cdot\\overline{z_{2}}}{\\left|z_{2}\\right|^{2}}.$$'
         '<p>A nevező így <b>valós</b> szám lesz, a számlálót pedig már csak ki kell bontani. '
         'Ez szó szerint ugyanaz a fogás, mint a gyöktelenítés a kéttagú nevezőnél.</p>',
         hid="tetel-komplex-osztas"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki: $\\dfrac{5+i}{2-3i}$.</p>',
         hid="pelda-osztas",
         lenyilo=("Megoldás",
                  '<p>A nevező konjugáltja $2+3i$, és $|2-3i|^{2}=4+9=13$. Bővítve:</p>'
                  '$$\\frac{(5+i)(2+3i)}{13}=\\frac{10+15i+2i+3i^{2}}{13}'
                  '=\\frac{10-3+17i}{13}=\\frac{7+17i}{13}.$$'
                  '<p>Végalak: $\\dfrac{7}{13}+\\dfrac{17}{13}i$.</p>')),
   doboz("erdekesseg", "Ugyanaz a trükk, kétszer",
         '<p>Vesd össze a két lépést:</p>'
         '$$\\frac{4}{\\sqrt7-\\sqrt3}\\cdot\\frac{\\sqrt7+\\sqrt3}{\\sqrt7+\\sqrt3},'
         '\\qquad\\qquad \\frac{5+i}{2-3i}\\cdot\\frac{2+3i}{2+3i}$$'
         '<p>Mindkettőben a „konjugálttal" bővítünk, hogy a nevező <b>racionális</b>, '
         'illetve <b>valós</b> legyen. A matematika ugyanazt a jó ötletet szereti '
         'többször is elsütni.</p>'),
 ]),

 ("A konjugálás és a modulusz tulajdonságai", [
   doboz("tetel", "Számolási szabályok",
         '<p>Bármely $z,w\\in\\mathbb{C}$ esetén:</p>'
         '$$\\overline{z+w}=\\overline{z}+\\overline{w},\\qquad '
         '\\overline{z\\cdot w}=\\overline{z}\\cdot\\overline{w},\\qquad '
         '\\overline{\\overline{z}}=z$$'
         '$$z+\\overline{z}=2\\operatorname{Re}(z),\\qquad '
         'z-\\overline{z}=2\\operatorname{Im}(z)\\cdot i,\\qquad '
         '\\left|z\\cdot w\\right|=|z|\\cdot|w|$$'
         '<p>A negyedik és ötödik különösen hasznos: velük egy komplex szám valós és '
         'képzetes része <b>kiszámolható</b>, ha ismerjük $z$-t és $\\overline z$-t.</p>',
         hid="tetel-konjugalas-tulajdonsagok"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Legyen $z=6-2i$. Mennyi $z+\\overline{z}$ és $z\\cdot\\overline{z}$?</p>',
         lenyilo=("Megoldás",
                  '<p>$\\overline z=6+2i$, ezért $z+\\overline z=12=2\\cdot 6=2\\operatorname{Re}(z)$ ✔, '
                  'és $z\\cdot\\overline z=36+4=40=|z|^{2}$ (valóban '
                  '$|z|=\\sqrt{36+4}=\\sqrt{40}$). Mindkét eredmény <b>valós</b>.</p>')),
   gyakorolj(FGY + "#alap-7", "A 7–12", FGY + "#kozep-5", "K 5–9"),
   brief('<b>X. Károly professzor:</b> Van még egy dolog, amit Dr. Baljós kihasznál: az $i$ hatványai '
         '<b>ismétlődnek</b>. Négyes ciklusban. Aki ezt észreveszi, másodpercek alatt '
         'kiszámolja $i^{2026}$ értékét — aki nem, az órákig szorozgat. '
         'Az utolsó kiképzési egység erről szól, és arról, hogyan oldunk meg egyenletet '
         'ebben az új világban.',
         outro=True),
 ]),
]

# =====================================================================  C3

C3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>X. Károly professzor:</b> Az utolsó lecke a fejezetben: a <b>minta</b> felismerése. '
         'Dr. Baljós kódjai hatalmas kitevőket használnak, hogy elrejtsék az egyszerű '
         'szerkezetet. De az $i$ hatványai négyesével ismétlődnek — ez a ciklus a kulcs '
         'az egész titkosításhoz. Aztán megoldunk pár egyenletet, és a fejezet lezárul.'),
 ]),

 ("A képzetes egység hatványai", [
   'Számoljuk ki sorban: $i^{1}=i$, $i^{2}=-1$, $i^{3}=i^{2}\\cdot i=-i$, '
   '$i^{4}=i^{2}\\cdot i^{2}=(-1)(-1)=1$. És innentől minden ismétlődik, hiszen '
   '$i^{5}=i^{4}\\cdot i=1\\cdot i=i$.',
   doboz("tetel", "Négyes ciklus",
         '$$i^{1}=i,\\qquad i^{2}=-1,\\qquad i^{3}=-i,\\qquad i^{4}=1$$'
         '<p>Általánosan: $i^{n}$ értéke csak attól függ, hogy $n$ <b>4-gyel osztva</b> '
         'mennyi maradékot ad:</p>'
         '$$i^{4k}=1,\\qquad i^{4k+1}=i,\\qquad i^{4k+2}=-1,\\qquad i^{4k+3}=-i.$$',
         hid="tetel-i-hatvanyai"),
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Mennyi $i^{27}$, $i^{100}$ és $i^{2026}$?</p>',
         hid="pelda-i-hatvany",
         lenyilo=("Megoldás",
                  '<p>$27=4\\cdot 6+3$, tehát $i^{27}=i^{3}=-i$.</p>'
                  '<p>$100=4\\cdot 25+0$, tehát $i^{100}=i^{0}=1$.</p>'
                  '<p>$2026=4\\cdot 506+2$, tehát $i^{2026}=i^{2}=-1$. '
                  '<b>Gyorsteszt:</b> elég az utolsó <b>két</b> jegyet nézni, mert $100$ osztható '
                  '$4$-gyel — itt $26$, aminek a 4-es maradéka $2$.</p>')),
   kviz('Mennyi $i^{35}$?',
        ['$-i$', '$i$', '$-1$'], 0,
        jo="✔ 35 = 4·8 + 3, tehát i³ = −i.",
        nem="✘ Oszd 35-öt 4-gyel: a maradék 3, és i³ = −i."),
 ]),

 ("Összetett kifejezések kiszámítása", [
   'A recept: minden $i$-hatványt visszavezetünk a négyes ciklussal, majd összevonjuk '
   'a valós és a képzetes tagokat.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Számítsd ki: $2i^{5}-3i^{11}+i^{22}$.</p>',
         hid="pelda-osszetett-i",
         lenyilo=("Megoldás",
                  '<p>$5=4+1\\Rightarrow i^{5}=i$ · $11=4\\cdot2+3\\Rightarrow i^{11}=-i$ · '
                  '$22=4\\cdot5+2\\Rightarrow i^{22}=-1$. Behelyettesítve:</p>'
                  '$$2i-3\\cdot(-i)+(-1)=2i+3i-1=-1+5i.$$')),
 ]),

 ("Lineáris egyenletek a komplex számok halmazán", [
   'Az $a\\cdot z=b$ alakú egyenletet ugyanúgy oldjuk meg, mint a valós számoknál: '
   'osztunk $a$-val. Az osztást pedig már ismerjük — bővítés a konjugálttal.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg a komplex számok halmazán: $(2-i)z=5+5i$.</p>',
         hid="pelda-linearis-egyenlet",
         lenyilo=("Megoldás",
                  '<p>$z=\\dfrac{5+5i}{2-i}$. A nevező konjugáltja $2+i$, '
                  '$|2-i|^{2}=4+1=5$:</p>'
                  '$$z=\\frac{(5+5i)(2+i)}{5}=\\frac{10+5i+10i+5i^{2}}{5}'
                  '=\\frac{10-5+15i}{5}=\\frac{5+15i}{5}=1+3i.$$'
                  '<p><b>Ellenőrzés:</b> $(2-i)(1+3i)=2+6i-i+3=5+5i$ ✔</p>')),
 ]),

 ("Ha $z$ és $\\overline{z}$ is szerepel", [
   'Itt nem lehet egyszerűen „átosztani": $z$ és $\\overline z$ két különböző dolog. '
   'A megoldás kulcsa az egyenlőség tétele — <b>egy</b> komplex egyenlet <b>két</b> '
   'valós egyenletet jelent.',
   doboz("pelda", "Vészterem-szimuláció",
         '<p>Oldd meg: $2z+3\\overline{z}=10-4i$.</p>',
         hid="pelda-z-es-konjugalt",
         lenyilo=("Megoldás",
                  '<p>Legyen $z=x+yi$, ekkor $\\overline z=x-yi$. Behelyettesítve:</p>'
                  '$$2(x+yi)+3(x-yi)=5x-yi.$$'
                  '<p>Ez akkor egyenlő $10-4i$-vel, ha a valós és a képzetes részek is '
                  'megegyeznek:</p>'
                  '$$5x=10\\ \\Rightarrow\\ x=2,\\qquad -y=-4\\ \\Rightarrow\\ y=4.$$'
                  '<p>Tehát $z=2+4i$. <b>Ellenőrzés:</b> '
                  '$2(2+4i)+3(2-4i)=4+8i+6-12i=10-4i$ ✔</p>')),
   kviz('Hány valós egyenletre bomlik szét egyetlen komplex egyenlőség?',
        ['Kettőre — a valós és a képzetes részekre.',
         'Egyre, csak komplex számokkal.',
         'Négyre.'], 0,
        jo="✔ Két komplex szám akkor egyenlő, ha a valós ÉS a képzetes részük is egyenlő.",
        nem="✘ Kettőre: külön a valós, külön a képzetes részek egyenlősége."),
   gyakorolj(FGY + "#alap-13", "A 13–18", FGY + "#kozep-10", "K 10–14"),
   brief('<b>X. Károly professzor:</b> Kadét, a fejezet lezárult. Kibővítette a valóságát, és '
         'megtanult mozogni benne. De figyeljen: az $x^{2}=-1$ csak a kezdet volt. '
         'A következő küldetésben olyan egyenletekkel találkozik, amelyeknek <b>néha</b> '
         'van valós megoldásuk, néha nincs — és ez a „néha" egyetlen számon fog múlni. '
         'Nagol és Küklopsz már várja a Vészteremben. Az M-Faktor küldetés indul.',
         outro=True),
 ]),
]

# ===================================================================== futtatás

ki = []
ki.append(lap(**T, fajl="tananyag-komplex-szam-fogalma.html",
              cim="A komplex szám fogalma", cim_tiszta="A komplex szám fogalma",
              alcim="A számhalmaz bővítése, a képzetes egység és az algebrai alak, a Gauss-sík, "
                    "valamint a konjugált és a modulusz.",
              chip="A Képzelet Határa · 6/8", szakaszok=C1,
              elozo=("feladatok-gyokvonas.html", "Feladatok — gyökvonás"),
              kovetkezo=("tananyag-muveletek-komplex-szamokkal.html",
                         "Műveletek a komplex számokkal")))
ki.append(lap(**T, fajl="tananyag-muveletek-komplex-szamokkal.html",
              cim="Műveletek a komplex számokkal", cim_tiszta="Műveletek a komplex számokkal",
              alcim="Összeadás, kivonás, szorzás, valamint osztás a nevező konjugáltjával való "
                    "bővítéssel — és a konjugálás számolási szabályai.",
              chip="A Képzelet Határa · 7/8", szakaszok=C2,
              elozo=("tananyag-komplex-szam-fogalma.html", "A komplex szám fogalma"),
              kovetkezo=("tananyag-i-hatvanyai-es-egyenletek.html",
                         "Az $i$ hatványai és egyenletek")))
ki.append(lap(**T, fajl="tananyag-i-hatvanyai-es-egyenletek.html",
              cim="Az $i$ hatványai és egyenletek $\\mathbb{C}$-ben",
              cim_tiszta="Az i hatványai és egyenletek",
              alcim="A képzetes egység hatványainak négyes ciklusa, összetett kifejezések "
                    "kiszámítása, lineáris egyenletek, valamint a $z$ és $\\overline{z}$ "
                    "együttes előfordulása.",
              chip="A Képzelet Határa · 8/8", szakaszok=C3,
              elozo=("tananyag-muveletek-komplex-szamokkal.html", "Műveletek a komplex számokkal"),
              kovetkezo=("feladatok-komplex-szamok.html", "Feladatok — komplex számok")))

for u in ki:
    print("✓", os.path.basename(u))
