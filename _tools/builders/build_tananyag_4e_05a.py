# -*- coding: utf-8 -*-
"""4e/05 — A blokk: a szorzasi es az osszeadasi szabaly (A1), permutaciok (A2), variaciok (A3), kombinaciok (A4).
Mentor: Nyalka Vili (Ved Vilmos kommental, Nagol tisztaz). Kuldetes: Multiverzum Lotto.
Specifikacio: projektek/4e/munkafajlok/narrativa_05-kombinatorika.md
Tiltott adatok: a 25/26-os es 26/27-es 4. ellenorzo (tiltott_4e_05.py) — lent ellenorizve."""
import sys, os
from itertools import permutations, product, combinations
from math import comb, perm, factorial as fakt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
import tiltott
TILT = tiltott.modul("tiltott_4e_05")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)

T = dict(tagozat="4e", mappa="05-kombinatorika", temakor="Kombinatorika")
KUL = "Multiverzum Lottó"
FA = "feladatok-kombinatorika.html"
TINTA, HALV, KEK, KEKH, ZOLD, PIROS = "#0f172a", "#94a3b8", "#1d4ed8", "#dbeafe", "#047857", "#b91c1c"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(FA + k_h, k_c, FA + n_h, n_c, tagozat="4e")


def NEHEZ(n, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FA}#nehez-{n}">Zsoldos-lista, nehéz {n}</a>.</p>')


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{h}</th>" for h in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    return f'<div class="tblwrap"><table class="tt-table">{"<tr>" + th + "</tr>" if any(fejlec) else ""}{tr}</table></div>'


# ---------------------------------------------------------------- önteszt: képlet = teljes felsorolás
E = []


def chk(nev, kepletes, felsorolt):
    if kepletes != felsorolt:
        E.append((nev, kepletes, felsorolt))


def szamok(jegyek, k, ism, felt=lambda p: True):
    it = product(jegyek, repeat=k) if ism else permutations(jegyek, k)
    return sum(1 for p in it if p[0] != 0 and felt(p))


D = range(10)
# A1
chk("A1 szett", 3 * 2, len(list(product(range(3), range(2)))))
chk("A1 ing", 4 * 3, len(list(product(range(4), range(3)))))
chk("A1 azonosito", 26 * 26 * 1000, 676000)
chk("A1 kod", 5 ** 2 + 5 ** 3, len(list(product(range(5), repeat=2))) + len(list(product(range(5), repeat=3))))
chk("A1 haromjegyu", 900, szamok(D, 3, True))
chk("A1 kulonbozo", 9 * 9 * 8, szamok(D, 3, False))
chk("A1 legalabb0", 900 - 9 ** 3, szamok(D, 3, True, lambda p: 0 in p))
chk("A1 ketjegyu", 81, szamok(D, 2, False))
# A2
chk("A2 3", fakt(3), len(list(permutations("ABC"))))
chk("A2 4", fakt(4), len(list(permutations("ABCD"))))
chk("A2 Vili elol", fakt(4), sum(1 for p in permutations("VABCD") if p[0] == "V"))
chk("A2 blokk", 2 * fakt(4), sum(1 for p in permutations("EMABC") if abs(p.index("E") - p.index("M")) == 1))
chk("A2 0123", 18, szamok([0, 1, 2, 3], 4, False))
chk("A2 ANNA", fakt(4) // (fakt(2) * fakt(2)), len(set(permutations("ANNA"))))
chk("A2 MISSISSIPPI", fakt(11) // (fakt(4) * fakt(4) * fakt(2)), 34650)
chk("A2 golyo", fakt(7) // (fakt(4) * fakt(2)), len(set(permutations("PPPPKKF"))))
chk("A2 111223", fakt(6) // (fakt(3) * fakt(2)), len({p for p in permutations([1, 1, 1, 2, 2, 3])}))
chk("A2 0012", 6, len({p for p in permutations([0, 0, 1, 2]) if p[0] != 0}))
chk("A2 ARAD", fakt(4), len(set(permutations("ÁRAD"))))
chk("A2 10!", fakt(10), 3628800)
# A3
chk("A3 dobogo", perm(10, 3), len(list(permutations(range(10), 3))))
chk("A3 kviz dobogo", perm(8, 3), 336)
chk("A3 PIN", 10 ** 4, len(list(product(D, repeat=4))))
chk("A3 Morse", sum(2 ** k for k in range(1, 5)), sum(len(list(product("·-", repeat=k))) for k in range(1, 5)))
chk("A3 kodzar", 10 ** 3, len(list(product(D, repeat=3))))
chk("A3 2458a", perm(4, 3), szamok([2, 4, 5, 8], 3, False))
chk("A3 2458b", 4 ** 3, szamok([2, 4, 5, 8], 3, True))
chk("A3 paros", 12 + 18, szamok([0, 1, 2, 3, 4], 3, False, lambda p: p[-1] % 2 == 0))
# A4
chk("A4 43", perm(4, 3) // fakt(3), len(list(combinations("ABCD", 3))))
chk("A4 10 alatt 3", comb(10, 3), 120)
chk("A4 kezfogas", comb(10, 2), len(list(combinations(range(10), 2))))
chk("A4 koccintas", comb(6, 2), 15)
chk("A4 20 alatt 3", comb(20, 3), 1140)
chk("A4 V20 3", perm(20, 3), 6840)
csapat = [("L", i) for i in range(10)] + [("F", i) for i in range(8)]
chk("A4 pontosan2", comb(10, 2) * comb(8, 2), sum(1 for c in combinations(csapat, 4) if sum(t == "L" for t, _ in c) == 2))
chk("A4 legalabb1", comb(18, 4) - comb(8, 4), sum(1 for c in combinations(csapat, 4) if any(t == "L" for t, _ in c)))
chk("A4 szimmetria", comb(18, 16), comb(18, 2))
chk("A4 28 meccs", [n for n in range(2, 40) if comb(n, 2) == 28], [8])
chk("A4 lotto", comb(39, 7), 15380937)
chk("A4 otoslotto", comb(90, 5), 43949268)

WEB = [("perm", 3), ("perm", 4), ("szamjegy", {0, 1, 2, 3}), ("szamjegy", {2, 4, 5, 8}), ("szamjegy", {0, 1, 2, 3, 4}),
       ("szo", "ANNA"), ("szo", "MISSISSIPPI"), ("szo", "ÁRAD"), ("ismvar", (5, 2)), ("ismvar", (5, 3)),
       ("ismvar", (10, 4)), ("ismvar", (10, 3)), ("ismvar", (4, 3)), ("ismvar", (2, 4)), ("valaszt2", 10),
       ("valaszt2", 6), ("komb", (10, 2)), ("komb", (6, 2)), ("komb", (20, 3)), ("komb", (4, 3)), ("komb", (10, 3)),
       ("komb", (18, 4)), ("komb", (39, 7)), ("komb", (90, 5))]
E += TILT.ellenoriz(WEB)
assert not E, E
print("önteszt: OK")


# ---------------------------------------------------------------- ábrák (sötét tinta, világos tervrajz-lap)
def _svg(w, h, leiras, belso):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, system-ui, sans-serif">\n' + "\n".join(belso)
            + "\n</svg>")


def _szoveg(x, y, t, meret=12.5, szin=TINTA, horgony="start", vastag=False):
    fw = ' font-weight="600"' if vastag else ""
    return f'  <text x="{x:.1f}" y="{y:.1f}" font-size="{meret}" fill="{szin}" text-anchor="{horgony}"{fw}>{t}</text>'


def svg_fa():
    """Fadiagram: 3 zakó × 2 nadrág = 6 szett (A1)."""
    zako = ["fekete zakó", "kék zakó", "bordó zakó"]
    nadrag = ["csíkos nadrág", "sima nadrág"]
    w, h = 470, 262
    ki, gy = [], (60, 238)
    ki.append(f'  <circle cx="34" cy="131" r="6" fill="{TINTA}"/>')
    ki.append(_szoveg(34, 112, "Vili", 12, TINTA, "middle", True))
    level = 0
    for i, z in enumerate(zako):
        yz = 51 + i * 80
        ki.append(f'  <line x1="40" y1="131" x2="140" y2="{yz}" stroke="{TINTA}" stroke-width="1.6"/>')
        ki.append(f'  <circle cx="146" cy="{yz}" r="5" fill="{KEK}"/>')
        ki.append(_szoveg(146, yz - 11, z, 12, KEK, "middle", True))
        for j, n in enumerate(nadrag):
            yn = yz - 17 + j * 34
            level += 1
            ki.append(f'  <line x1="151" y1="{yz}" x2="262" y2="{yn}" stroke="{TINTA}" stroke-width="1.3"/>')
            ki.append(f'  <circle cx="267" cy="{yn}" r="4.5" fill="{ZOLD}"/>')
            ki.append(_szoveg(277, yn + 4, f"{level}. {z.split()[0]} + {n.split()[0]}", 12, TINTA))
    ki.append(_szoveg(146, 256, "1. döntés: 3 lehetőség", 11, "#475569", "middle"))
    ki.append(_szoveg(330, 256, "2. döntés: 2 lehetőség → 3 · 2 = 6", 11, "#475569", "middle"))
    return _svg(w, h, "Fadiagram: Vili 3 zakója közül mindegyikhez 2 nadrág választható, összesen 6 szett", ki)


def svg_sorrend():
    """4 elemből 3: a 24 rendezett hármas 4 oszlopban (A4)."""
    w, h = 440, 232
    ki = []
    for i, cs in enumerate(combinations("ABCD", 3)):
        x = 60 + i * 107
        ki.append(f'  <rect x="{x - 44}" y="10" width="88" height="26" rx="6" fill="{KEKH}" stroke="{KEK}"/>')
        ki.append(_szoveg(x, 28, "{" + ", ".join(cs) + "}", 13, KEK, "middle", True))
        for j, p in enumerate(permutations(cs)):
            ki.append(_szoveg(x, 60 + j * 25, "".join(p), 13.5, TINTA, "middle"))
        if i:
            ki.append(f'  <line x1="{x - 53.5}" y1="44" x2="{x - 53.5}" y2="200" stroke="{HALV}" stroke-dasharray="3 3"/>')
    ki.append(_szoveg(220, 222, "24 rendezett hármas = 4 csapat × 3! sorrend", 12, "#475569", "middle"))
    return _svg(w, h, "A négy elemből képezhető 24 rendezett hármas négy oszlopba csoportosítva; minden oszlop egy "
                      "háromelemű csapat hat sorrendje", ki)


def svg_dontes():
    """Döntési fa: számít a sorrend? → kombináció / minden elem? → permutáció / variáció (A4)."""
    w, h = 480, 262
    ki = []

    def kerdes(x, y, t):
        ki.append(f'  <rect x="{x - 105}" y="{y - 17}" width="210" height="34" rx="17" fill="#fff7ed" stroke="#c2410c" '
                  f'stroke-width="1.4"/>')
        ki.append(_szoveg(x, y + 4.5, t, 12.5, "#9a3412", "middle", True))

    def valasz(x, y, cim, kepl, meg):
        ki.append(f'  <rect x="{x - 72}" y="{y - 22}" width="144" height="62" rx="8" fill="{KEKH}" stroke="{KEK}" '
                  f'stroke-width="1.4"/>')
        ki.append(_szoveg(x, y - 4, cim, 12.5, KEK, "middle", True))
        ki.append(_szoveg(x, y + 14, kepl, 12.5, TINTA, "middle"))
        ki.append(_szoveg(x, y + 31, meg, 10.5, "#475569", "middle"))

    def nyil(x1, y1, x2, y2, t, tx, ty):
        ki.append(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{TINTA}" stroke-width="1.5" '
                  f'marker-end="url(#nyh)"/>')
        ki.append(_szoveg(tx, ty, t, 11.5, TINTA, "middle", True))

    ki.append(f'  <defs><marker id="nyh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
              f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{TINTA}"/></marker></defs>')
    kerdes(240, 26, "Számít a sorrend?")
    nyil(170, 43, 92, 104, "nem", 118, 70)
    nyil(310, 43, 340, 92, "igen", 346, 64)
    valasz(84, 132, "KOMBINÁCIÓ", "n! / (k! (n − k)!)", "csapat, pár, lottó")
    kerdes(340, 110, "Minden elemet sorba rakunk?")
    nyil(292, 127, 262, 184, "igen", 262, 152)
    nyil(390, 127, 410, 184, "nem, csak k-t", 426, 152)
    valasz(250, 212, "PERMUTÁCIÓ", "n!", "egyformák: n! / (k₁! k₂! …)")
    valasz(404, 212, "VARIÁCIÓ", "n! / (n − k)!", "ismétlődhet: nᵏ")
    return _svg(w, h, "Döntési fa: ha a sorrend nem számít, kombináció; ha számít és minden elemet sorba rakunk, "
                      "permutáció; ha csak k elemet, variáció", ki)


SVG_FA, SVG_SORREND, SVG_DONTES = svg_fa(), svg_sorrend(), svg_dontes()

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nyalka Vili:</b> Üdv a <i>Multiverzum Lottón</i>! Az I.V.H. ma sorsolja ki, melyik Vilmos-variáns marad '
         'meg a törölt idővonalon — és én nem akarok rosszul öltözve kiesni. Három zakót hoztam és két nadrágot. '
         'Hányféle szettben léphetek színpadra? <b>Véd Vilmos:</b> 🌮 <i>Burek-matek:</i> három meg kettő, az öt. '
         '<b>Nagol:</b> Minden zakóhoz mindkét nadrág felvehető. Az hat. <b>SZVETI:</b> Végre egy Vilmos, akinek van '
         'ízlése. A másikat, kérem, ne számoltassátok.'),
 ]),
 ("Egymás utáni döntések", [
   '<p class="lead">Nyalka Vili két lépésben dönt: <b>először</b> zakót választ (3 lehetőség), <b>utána</b> nadrágot '
   '(2 lehetőség). Rajzoljuk le a döntéseket egy <b>fadiagramon</b>: minden zakóból két ág indul.</p>',
   abra(SVG_FA, "Fadiagram: 3 zakó, mindegyikhez 2 nadrág — a végén $3\\cdot2=6$ szett."),
   doboz("tetel", "A szorzási szabály",
         r'<p>Ha egy választás egymás után következő lépésekből áll, és az első lépésben $n_1$, a másodikban $n_2$, …, '
         r'a $k$-adikban $n_k$ lehetőség van (és ezek <i>száma</i> nem függ attól, mit választottunk korábban), akkor az '
         r'összes lehetőség száma $$n_1\cdot n_2\cdot\ldots\cdot n_k.$$ Röviden: <b>ÉS → szorzás</b>.</p>',
         hid="tetel-szorzasi-szabaly"),
   doboz("pelda", "I.V.H. Akták — az azonosító",
         r'<p>Az I.V.H. minden variánsnak azonosítót ad: két betű (a 26 betűs angol ábécéből), utána három számjegy, '
         r'például <span class="kbd">VV-042</span>. Hány azonosító osztható ki?</p>'
         r'<p>Öt egymás utáni választás, és a betűk meg a számjegyek ismétlődhetnek: '
         r'$$26\cdot26\cdot10\cdot10\cdot10=676\,000.$$</p>', hid="pelda-azonosito"),
 ]),
 ("Egymást kizáró esetek", [
   r'<p class="lead">Nyalka Vili megéhezett. A büfében <b>vagy</b> burekot kér (4 féle van), <b>vagy</b> pizzaszeletet '
   r'(5 féle) — a kettő közül csak az egyiket. Itt nincs második lépés: a lehetőségek <b>kizárják egymást</b>, ezért '
   r'összeadjuk őket: $4+5=9$.</p>',
   doboz("tetel", "Az összeadási szabály",
         r'<p>Ha a választás egymást kizáró esetekre bomlik, és az egyes esetekben $n_1$, $n_2$, …, $n_k$ lehetőség van, '
         r'akkor az összes lehetőség száma $$n_1+n_2+\ldots+n_k.$$ Röviden: <b>VAGY → összeadás</b>.</p>',
         hid="tetel-osszeadasi-szabaly"),
   doboz("pelda", "I.V.H. Akták — rövid kódok",
         r'<p>Egy tárolórekesz kódja kétjegyű <b>vagy</b> háromjegyű, és csak az 1, 2, 3, 4, 5 számjegyeket használja '
         r'(ezek ismétlődhetnek). Hány kód lehetséges?</p>'
         r'<p>Két eset, és mindkettőn belül a szorzási szabály: kétjegyű kódból $5\cdot5=25$, háromjegyűből '
         r'$5\cdot5\cdot5=125$ van. Összesen $25+125=150$.</p>', hid="pelda-rovid-kod"),
   doboz("csapda", "Véd Vilmos csapda — ÉS vagy VAGY?",
         r'<p>Vilmos szerint 3 zakó és 2 nadrág 5 szett. Nem: a zakó <b>és</b> a nadrág két egymás utáni döntés, tehát '
         r'szorzunk. Fordítva is lehet hibázni: ha <b>vagy</b> burek, <b>vagy</b> pizza, akkor nincs „burek és pizza” '
         r'pár, tehát nem szorzunk. Kérdezd meg magadtól: <i>egymás után</i> döntök, vagy <i>egymás helyett</i>?</p>'),
   kviz('Nyalka Vilinek 4 inge és 3 nyakkendője van. Hányféleképpen választhat egy inget és egy nyakkendőt?',
        ['$12$', '$7$', '$4^3=64$', '$3^4=81$'], 0,
        jo="✔ Két egymás utáni döntés: $4\\cdot3=12$.",
        nem="✘ Az ing ÉS a nyakkendő két egymás utáni döntés: szorzás, $4\\cdot3=12$. Összeadni csak egymást kizáró "
            "eseteket szabad."),
 ]),
 ("Ha az első hely korlátoz", [
   r'<p class="lead">Hány háromjegyű szám van? A számjegy tízféle lehet, de az <b>első helyen nem állhat 0</b> (a 042 '
   r'nem háromjegyű). Az első helyre 9, a másodikra és a harmadikra 10–10 lehetőség jut: $9\cdot10\cdot10=900$.</p>',
   doboz("pelda", "I.V.H. Akták — különböző számjegyekkel",
         r'<p>Hány olyan háromjegyű szám van, amelynek a számjegyei különbözők?</p>'
         r'<p>A <b>korlátozott hellyel kezdünk</b>: az első jegy 9-féle (nem 0). A második bármi lehet, ami még nem '
         r'szerepelt — a 0 is —, ez 9-féle; a harmadik 8-féle. Összesen $9\cdot9\cdot8=648$.</p>'
         r'<p>Hogy konkrétan melyik jegy került az első helyre, az a második helyen a lehetőségek <i>számán</i> nem '
         r'változtat — ezért működik a szorzási szabály.</p>', hid="pelda-harmjegyu"),
   doboz("csapda", "Véd Vilmos csapda — a nulla előre tolakszik",
         r'<p>Vilmos így számolt: „a jegyek különbözők, tehát $10\cdot9\cdot8=720$.” Ebbe beleszámolta a 012-t, a '
         r'098-at és a társaikat is, amelyek nem háromjegyűek. A helyes sorrend: <b>előbb a korlátozott hely</b> (itt az '
         r'első), utána a többi.</p>'),
   kviz('Hány olyan kétjegyű szám van, amelynek a két számjegye különböző?',
        ['$81$', '$90$', '$100$', '$72$'], 0,
        jo="✔ Az első jegy 9-féle (nem 0), a második 9-féle (a 0 már állhat itt, csak az első jegy nem ismétlődhet): "
           "$9\\cdot9=81$.",
        nem="✘ Az első helyen nem lehet 0 (9 lehetőség), a másodikon bármi, ami különbözik az elsőtől (9 lehetőség): "
            "$9\\cdot9=81$."),
 ]),
 ("Összes mínusz rossz", [
   r'<p class="lead">Hány olyan háromjegyű szám van, amelyben <b>legalább egy</b> 0 számjegy szerepel? Közvetlenül sok '
   r'eset van (egy 0-s, két 0-s, és az is számít, hol állnak). Egyszerűbb a <b>fordított</b> kérdés: hány háromjegyű '
   r'számban <b>nincs</b> 0?</p>',
   doboz("pelda", "I.V.H. Akták — legalább egy nulla",
         r'<p>Háromjegyű szám, amelyben nincs 0: mindhárom jegy 9-féle (1-től 9-ig), tehát $9^3=729$ ilyen szám van. '
         r'Az összes háromjegyű szám 900, így legalább egy 0 $$900-729=171$$ számban szerepel.</p>',
         hid="pelda-legalabb"),
   doboz("erdekesseg", "Miért jó a komplementer?",
         r'<p>A „legalább egy” kérdésnél a rossz eset (<i>egy sem</i>) egyetlen, egyszerű eset, a jók viszont sokfélék. '
         r'A valószínűségszámításban (06) ugyanez a trükk jön vissza: $P(\text{legalább egy})=1-P(\text{egy sem})$.</p>'),
   GY("#alap-1", "alap 1–3", "#kozep-1", "közép 1–2"),
   brief('<b>Nyalka Vili:</b> A ruhatár rendben. Most sorba kell állnunk a Multiverzum-tablóhoz — és ott az a kérdés, '
         '<i>ki hányadik</i>. <b>Nagol:</b> Ugyanaz a szorzási szabály, csak kap egy új jelet: a felkiáltójelet.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nyalka Vili:</b> A lottó előtt minden variáns fotót kap a Multiverzum-tablóra — egy sorban, egymás mellett. '
         'Nálam a sorrend szent. <b>Véd Vilmos:</b> Minek számolni, úgyis mind egyformák vagyunk. <b>Nagol:</b> Épp '
         'ezért kell számolni. Ha két Vilmos egyforma, a helycseréjük nem ad új képet — ezt is figyelembe vesszük.'),
 ]),
 ("Hányféle sorrend?", [
   '<p class="lead">Három variáns — <b>A</b>, <b>B</b> és <b>C</b> — áll fel a tablóhoz. Soroljuk fel a lehetséges '
   'sorrendeket <b>rendszerezetten</b>: előbb azokat, amelyekben A áll elöl, aztán amelyekben B, végül C.</p>',
   TABLA(["ki áll elöl?", "sorrendek"], [["A", "ABC, ACB"], ["B", "BAC, BCA"], ["C", "CAB, CBA"]]),
   r'<p>A szorzási szabállyal: az első helyre 3, a másodikra 2, a harmadikra 1 variáns jut: $3\cdot2\cdot1=6$. Négy '
   r'variánsnál $4\cdot3\cdot2\cdot1=24$.</p>',
   doboz("definicio", "Faktoriális",
         r'<p>$n!$ (olvasd: <i>n faktoriális</i>) az első $n$ pozitív egész szám szorzata: '
         r'$$n!=n\cdot(n-1)\cdot\ldots\cdot2\cdot1.$$ Megállapodás szerint $0!=1$, és $1!=1$.</p>', hid="def-faktorialis"),
   doboz("definicio", "Permutáció",
         r'<p>$n$ különböző elem egy sorba rendezését az elemek egy <b>permutációjának</b> nevezzük.</p>',
         hid="def-permutacio"),
   doboz("tetel", "A permutációk száma",
         r'<p>$n$ különböző elem permutációinak száma $$P_n=n!$$ Indoklás: az első helyre $n$, a másodikra $n-1$, …, '
         r'az utolsóra 1 elem jut (szorzási szabály).</p>', hid="tetel-permutacio"),
   TABLA(["$n$", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
         [["$n!$", "1", "2", "6", "24", "120", "720", "5040", "40&#8239;320", "362&#8239;880", "3&#8239;628&#8239;800"]]),
   doboz("erdekesseg", "Milyen gyorsan nő?",
         r'<p>$10!=3\,628\,800$: tíz embert több mint hárommillió sorrendben lehet egy padra leültetni. Ha másodpercenként '
         r'egy új sorrendet próbálnánk ki, 42 napig tartana.</p>'),
   kviz('Hányféle sorrendben állhat fel 4 variáns egy sorban?', ['$24$', '$16$', '$12$', '$10$'], 0,
        jo="✔ $4!=4\\cdot3\\cdot2\\cdot1=24$.",
        nem="✘ Az első helyre 4, a másodikra 3, a harmadikra 2, az utolsóra 1 variáns jut: $4!=24$. A $4^2=16$ és a "
            "$4\\cdot3=12$ nem veszi figyelembe az összes helyet."),
 ]),
 ("Feltételes sorrendek", [
   '<p class="lead">A feladatok ritkán kérik az összes sorrendet; gyakoribb, hogy egy <b>feltétel</b> szűkíti őket. A '
   'módszer mindig ugyanaz: előbb a feltételt teljesítjük, a többi hely utána jön.</p>',
   doboz("pelda", "I.V.H. Akták — három feltétel",
         r'<ol class="reszfeladatok"><li>Öt variáns áll a tablóhoz, Nyalka Vili mindenképp az első helyen. A maradék '
         r'négy a többi négy helyen: $4!=24$ sorrend.</li>'
         r'<li>Öt variáns áll sorba, és Véd-eb meg Mini-Vili ragaszkodik hozzá, hogy <b>egymás mellett</b> álljanak. '
         r'Kössük össze őket egy <b>blokká</b>: így 4 egységet rendezünk sorba ($4!$ módon), a blokkon belül pedig a két '
         r'tag kétféle sorrendben állhat ($2!$). Összesen $2!\cdot4!=48$.</li>'
         r'<li>Hány négyjegyű szám írható fel a 0, 1, 2, 3 számjegyekből, ha mindegyiket pontosan egyszer használjuk? A '
         r'$4!=24$ sorrendből azok rosszak, amelyek 0-val kezdődnek — ilyenből $3!=6$ van. Tehát $24-6=18$. (Másként: '
         r'az első jegy 3-féle, a többi $3!$ módon: $3\cdot3!=18$.)</li></ol>', hid="pelda-blokk"),
   doboz("csapda", "Véd Vilmos csapda — a blokk belseje",
         r'<p>Vilmos a blokkos feladatra $4!=24$-et mondott. Elfelejtette, hogy a blokk belsejében is van sorrend: '
         r'Véd-eb állhat Mini-Vili bal <i>és</i> jobb oldalán is. A helyes eredmény $2\cdot24=48$.</p>'),
   NEHEZ(1, "hányadik lesz egy szó, ha a betűinek összes sorrendjét ábécérendbe szedjük"),
 ]),
 ("Ha vannak egyforma elemek", [
   r'<p class="lead">Hányféle betűsort rakhatunk ki az <b>ANNA</b> szó betűiből? Ha a négy betű különböző volna, '
   r'$4!=24$ sorrend lenne. A két A és a két N azonban egyforma: ha felcseréljük őket, ugyanazt a betűsort kapjuk.</p>',
   r'<p>Az összes különböző betűsor: <span class="kbd">AANN</span> <span class="kbd">ANAN</span> '
   r'<span class="kbd">ANNA</span> <span class="kbd">NAAN</span> <span class="kbd">NANA</span> '
   r'<span class="kbd">NNAA</span> — hat darab. Mindegyiket $2!\cdot2!=4$-szer számoltuk volna (a két A két '
   r'sorrendje, a két N két sorrendje), ezért $$\frac{4!}{2!\cdot2!}=\frac{24}{4}=6.$$</p>',
   doboz("tetel", "Ismétléses permutáció",
         r'<p>Ha $n$ elem között az egyes fajtákból $k_1$, $k_2$, …, $k_r$ darab egyforma van ($k_1+k_2+\ldots+k_r=n$), '
         r'akkor az elemek különböző sorrendjeinek — <b>ismétléses permutációinak</b> — száma '
         r'$$P_n^{k_1,k_2,\ldots,k_r}=\frac{n!}{k_1!\cdot k_2!\cdot\ldots\cdot k_r!}.$$ Az egyszer előforduló elemek '
         r'$1!=1$-gyel szerepelnek, ezeket nem kell kiírni.</p>', hid="tetel-ismetleses-permutacio"),
   doboz("pelda", "I.V.H. Akták — MISSISSIPPI és a golyók",
         r'<p>A MISSISSIPPI szó 11 betűjében az I négyszer, az S négyszer, a P kétszer, az M egyszer fordul elő: '
         r'$$\frac{11!}{4!\cdot4!\cdot2!}=34\,650\ \text{betűsor}.$$</p>'
         r'<p>Négy piros, két kék és egy fehér golyó egy sorban (az egyforma színűeket nem különböztetjük meg): '
         r'$$\frac{7!}{4!\cdot2!}=\frac{5040}{48}=105\ \text{sorrend}.$$</p>', hid="pelda-ismetleses"),
   doboz("csapda", "Véd Vilmos csapda — csak az egyik ismétlődést vette észre",
         r'<p>Vilmos az ANNA-nál csak a két A miatt osztott: $\frac{24}{2}=12$. <b>Minden</b> ismétlődő betűfajta '
         r'faktoriálisával osztani kell, itt $2!\cdot2!$-sal.</p>'),
   doboz("erdekesseg", "Az ékezet is betű",
         r'<p>A magyar ábécében az A és az Á két külön betű, ugyanígy az O és az Ó, az E és az É. Az ÁRAD szó betűi '
         r'tehát mind különbözők: $4!=24$ betűsor, nem $\frac{4!}{2!}=12$. Ha egy feladat ékezetes szót ad, és nem '
         r'mondja, hogy az ékezetet figyelmen kívül hagyjuk, az ékezetes betű külön betű.</p>'),
   kviz('Hány különböző betűsor rakható ki az ANNA szó betűiből?', ['$6$', '$12$', '$24$', '$4$'], 0,
        jo="✔ $\\frac{4!}{2!\\cdot2!}=6$ — felsorolva: AANN, ANAN, ANNA, NAAN, NANA, NNAA.",
        nem="✘ Mindkét ismétlődő betűfajtával osztani kell: $\\frac{4!}{2!\\cdot2!}=6$."),
 ]),
 ("Számjegyek és a nulla", [
   doboz("pelda", "I.V.H. Akták — ismétlődő számjegyek",
         r'<p>Hány hatjegyű szám írható fel az 1, 1, 1, 2, 2, 3 számjegyek mindegyikének felhasználásával?</p>'
         r'<p>Ismétléses permutáció: $\dfrac{6!}{3!\cdot2!}=\dfrac{720}{12}=60$. (Nincs 0 a jegyek között, az első '
         r'helyre nem kell figyelni.)</p>'
         r'<p>Ha a jegyek között 0 is van — például 0, 0, 1, 2 —, előbb az összes sorrendet számoljuk ki '
         r'($\frac{4!}{2!}=12$), majd levonjuk a 0-val kezdődőket (a maradék 0, 1, 2 sorrendjei: $3!=6$). Tehát '
         r'$12-6=6$ négyjegyű szám van: 1002, 1020, 1200, 2001, 2010, 2100.</p>', hid="pelda-szamjegy-ismetles"),
   GY("#alap-4", "alap 4–6", "#kozep-3", "közép 3–5"),
   brief('<b>Nyalka Vili:</b> A tabló kész. A díjátadón viszont csak három hely van a dobogón — nem áll fel mindenki. '
         '<b>Nagol:</b> Akkor nem mindenkit rakunk sorba, csak kiválasztunk néhányat, sorrendben. Ez a variáció.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- A3
A3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nyalka Vili:</b> A Multiverzum Lottó díjátadóján dobogó áll: arany, ezüst, bronz. Tíz variáns versenyez, '
         'és a szmokingomhoz csak az arany illik. <b>Véd Vilmos:</b> A nyeremény egy I.V.H.-széfben van, négyjegyű '
         'PIN-kóddal. Kitaláljuk? <b>Nagol:</b> Előbb számoljuk ki, hány próbálkozás kellene. A két kérdés rokon: '
         'kiválasztunk néhány elemet, és <i>számít a sorrend</i>.'),
 ]),
 ("Kiválasztás, ahol számít a sorrend", [
   r'<p class="lead">A tíz variánsból hányféleképpen alakulhat a dobogó? Az aranyérmes 10-féle lehet, az ezüstérmes a '
   r'maradék 9 közül, a bronzérmes a maradék 8 közül kerül ki: $10\cdot9\cdot8=720$. Nem rakjuk sorba mind a tízet — '
   r'csak hármat választunk ki, <b>sorrendben</b>.</p>',
   doboz("definicio", "Variáció",
         r'<p>Ha $n$ különböző elemből kiválasztunk $k$ darabot ($k\le n$), és a kiválasztott elemek <b>sorrendje is '
         r'számít</b>, akkor az $n$ elem egy $k$-adosztályú (ismétlés nélküli) <b>variációját</b> kapjuk.</p>',
         hid="def-variacio"),
   doboz("tetel", "Az ismétlés nélküli variációk száma",
         r'<p>$$V_n^k=n\cdot(n-1)\cdot\ldots\cdot(n-k+1)=\frac{n!}{(n-k)!}.$$ A szorzatnak $k$ tényezője van. Ha $k=n$, '
         r'minden elemet sorba rakunk: $V_n^n=n!=P_n$ — a permutáció a variáció speciális esete.</p>',
         hid="tetel-variacio"),
   doboz("erdekesseg", "Jelölés a szerb tankönyvben",
         r'<p>A szerb tankönyvek és feladatgyűjtemények fordítva írják az indexeket: $V_k^n$ (felül az elemek száma, alul '
         r'a kiválasztottaké). A jelentés ugyanaz — csak olvasd el figyelmesen, melyik szám melyik.</p>'),
   kviz('Egy 8 fős döntőből hányféle lehet az érmesek (arany, ezüst, bronz) sorrendje?',
        ['$8\\cdot7\\cdot6=336$', '$\\binom83=56$', '$8^3=512$', '$3!=6$'], 0,
        jo="✔ Hármat választunk ki, és számít, ki hányadik: $V_8^3=336$.",
        nem="✘ A dobogón számít a sorrend, és egy versenyző csak egy érmet kaphat: $V_8^3=8\\cdot7\\cdot6=336$."),
 ]),
 ("Ha egy elem többször is választható", [
   r'<p class="lead">A széf PIN-kódja négy számjegyből áll, és a számjegyek <b>ismétlődhetnek</b> (az 1111 is jó kód). '
   r'Most minden helyre mind a tíz számjegy kerülhet: $10\cdot10\cdot10\cdot10=10^4=10\,000$ kód.</p>',
   doboz("tetel", "Az ismétléses variációk száma",
         r'<p>Ha $n$ különböző elemből $k$-szor választunk úgy, hogy egy elem <b>többször is</b> választható, és a '
         r'sorrend számít, akkor ezek — az <b>ismétléses variációk</b> — száma $$V_n^{k,i}=n^k.$$ Itt $k$ nagyobb is lehet '
         r'$n$-nél.</p>', hid="tetel-ismetleses-variacio"),
   doboz("pelda", "I.V.H. Akták — Morse-jelek",
         r'<p>A Morse-ábécé két alapjelből, pontból és vonásból áll. Hány különböző jel rakható össze <b>legfeljebb '
         r'négy</b> alapjelből?</p>'
         r'<p>Esetek szerint (összeadási szabály), mindegyikben ismétléses variáció: '
         r'$$2^1+2^2+2^3+2^4=2+4+8+16=30.$$</p>', hid="pelda-morse"),
   doboz("csapda", "Véd Vilmos csapda — ismétlődhet vagy nem?",
         r'<p>Vilmos a PIN-kódra $10\cdot9\cdot8\cdot7=5040$-et mondott, mintha egy számjegy csak egyszer szerepelhetne. '
         r'Olvasd el a feltételt: <i>ismétlődhet</i> → $n^k$; <i>nem ismétlődhet</i> (különböző jegyek, különböző '
         r'emberek) → $V_n^k$.</p>'),
   kviz('Egy kódzár három tárcsáján egyenként a 0, 1, …, 9 számjegyek állnak. Hány beállítás lehetséges?',
        ['$1000$', '$720$', '$999$', '$30$'], 0,
        jo="✔ Minden tárcsa 10-féle, és ugyanaz a jegy többször is szerepelhet: $10^3=1000$.",
        nem="✘ A tárcsákon ugyanaz a jegy többször is állhat (a 777 is beállítás): ismétléses variáció, $10^3=1000$."),
 ]),
 ("Számjegyes feladatok", [
   doboz("pelda", "I.V.H. Akták — a 2, 4, 5, 8 számjegyekből",
         r'<p>Hány háromjegyű szám írható fel a 2, 4, 5, 8 számjegyekből, ha a jegyek a) nem ismétlődhetnek; '
         r'b) ismétlődhetnek?</p><p>a) $V_4^3=4\cdot3\cdot2=24$; b) $V_4^{3,i}=4^3=64$. Nincs 0 a jegyek között, így az '
         r'első helyre nem kell külön figyelni.</p>', hid="pelda-negy-jegy"),
   doboz("pelda", "I.V.H. Akták — páros számok a nullával",
         r'<p>Hány páros háromjegyű szám írható fel a 0, 1, 2, 3, 4 számjegyekből, ha a jegyek nem ismétlődhetnek?</p>'
         r'<p>A páros szám <b>utolsó</b> jegye 0, 2 vagy 4 — és a 0 az első helyre sem kerülhet. Két korlátozott hely, '
         r'ezért <b>esetekre bontunk</b> (összeadási szabály):</p>'
         r'<ul class="clean"><li>utolsó jegy 0: az első 4-féle, a középső 3-féle → $4\cdot3=12$;</li>'
         r'<li>utolsó jegy 2 vagy 4 (2 eset): az első 3-féle (nem 0 és nem az utolsó), a középső 3-féle → '
         r'$2\cdot3\cdot3=18$.</li></ul><p>Összesen $12+18=30$.</p>', hid="pelda-paros"),
   doboz("csapda", "Véd Vilmos csapda — egyben számolni",
         r'<p>Vilmos így számolt: „az utolsó jegy 3-féle, az első 4-féle, a középső 3-féle: $3\cdot4\cdot3=36$.” Csakhogy '
         r'ha az utolsó jegy 0, az első jegy 4-féle lehet, ha viszont 2 vagy 4, csak 3-féle — a lehetőségek száma függ a '
         r'korábbi döntéstől. Ilyenkor esetekre bontunk.</p>'),
   NEHEZ(2, "esetszétválasztás, amikor a 0 és a párosság egyszerre korlátoz"),
   GY("#alap-7", "alap 7–9", "#kozep-6", "közép 6–7"),
   brief('<b>Nyalka Vili:</b> Az érmesek megvannak. Az I.V.H. szerint viszont a túlélő csapatban nincs arany és bronz — '
         'csak <i>csapat</i> van. <b>Nagol:</b> Ha a sorrend nem számít, a variációkat össze kell vonni. Ez a '
         'kombináció.', outro=True),
 ]),
]

# ---------------------------------------------------------------- A4
A4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nyalka Vili:</b> Az I.V.H. csak egy háromfős csapatot enged át a törölt idővonalról. Egy csapatban nincs '
         'első és utolsó: Véd-eb, Mini-Vili és én ugyanaz a csapat, akárhogy állunk. <b>Véd Vilmos:</b> És a '
         'lottószelvény? Ott is mindegy, milyen sorrendben húzzák ki a számokat? <b>Nagol:</b> Mindegy. Ezért kevesebb '
         'a lehetőség, mint a dobogón — pontosan annyiszor kevesebb, ahányféleképpen a kiválasztottak sorba állhatnak.'),
 ]),
 ("Amikor a sorrend nem számít", [
   r'<p class="lead">Négy variánsból — A, B, C, D — hármat választunk ki. Ha számítana a sorrend, $V_4^3=24$ lehetőség '
   r'volna. Csoportosítsuk a 24 rendezett hármast aszerint, <b>kik</b> vannak benne: minden csoport egy háromfős csapat, '
   r'és egy csapat $3!=6$ sorrendben fordul elő.</p>',
   abra(SVG_SORREND, "A 24 rendezett hármas 4 oszlopban: egy oszlop egy csapat, 6 sorrenddel. Csapatból "
                     "$\\frac{24}{3!}=4$ van."),
   doboz("definicio", "Kombináció",
         r'<p>Ha $n$ különböző elemből kiválasztunk $k$ darabot, és a kiválasztott elemek <b>sorrendje nem számít</b>, '
         r'akkor az $n$ elem egy $k$-adosztályú (ismétlés nélküli) <b>kombinációját</b> kapjuk. Egy kombináció tehát '
         r'egy $k$ elemű részhalmaz.</p>', hid="def-kombinacio"),
   doboz("tetel", "A kombinációk száma",
         r'<p>$$C_n^k=\binom nk=\frac{V_n^k}{k!}=\frac{n!}{k!\,(n-k)!}.$$ A $\binom nk$ olvasása: „$n$ alatt a $k$”. '
         r'Számoláshoz a középső alak a legkényelmesebb: $\binom{10}{3}=\frac{10\cdot9\cdot8}{3\cdot2\cdot1}=120$.</p>',
         hid="tetel-kombinacio"),
   doboz("pelda", "I.V.H. Akták — kézfogás",
         r'<p>A lottó előtt tíz variáns mindegyike kezet fog mindegyikkel. Hány kézfogás történik?</p>'
         r'<p>Egy kézfogás egy <b>pár</b>: A–B ugyanaz, mint B–A. Tehát $\binom{10}{2}=\frac{10\cdot9}{2}=45$. Aki '
         r'$10\cdot9=90$-et mond, minden kézfogást kétszer számolt.</p>', hid="pelda-kezfogas"),
   kviz('Egy hatfős társaságban mindenki mindenkivel egyszer koccint. Hány koccintás hallatszik?',
        ['$15$', '$30$', '$36$', '$6$'], 0,
        jo="✔ Egy koccintás egy pár, a sorrend nem számít: $\\binom62=\\frac{6\\cdot5}{2}=15$.",
        nem="✘ Az A–B és a B–A koccintás ugyanaz: $\\binom62=\\frac{6\\cdot5}{2}=15$ (a $6\\cdot5=30$ mindegyiket "
            "kétszer számolja)."),
 ]),
 ("Számít-e a sorrend?", [
   abra(SVG_DONTES, "Döntési fa: két kérdés dönti el, melyik eszköz kell."),
   TABLA(["helyzet", "számít a sorrend?", "ismétlődhet?", "eszköz", "példa"], [
       ["mindenkit sorba állítunk", "igen", "nem", "permutáció, $n!$", "tabló: $4!=24$"],
       ["néhányat kiválasztunk, helyezéssel", "igen", "nem", "variáció, $V_n^k$", "dobogó: $V_{10}^3=720$"],
       ["minden helyre bármelyik jöhet", "igen", "igen", "ismétléses variáció, $n^k$", "PIN: $10^4$"],
       ["néhányat kiválasztunk, csoportba", "nem", "nem", "kombináció, $\\binom nk$",
        "kézfogás: $\\binom{10}2=45$"]]),
   doboz("csapda", "Véd Vilmos csapda — a „kiválaszt” szó csal",
         r'<p>Vilmos minden feladatra, amelyben szerepel a <i>kiválaszt</i> szó, kombinációt számol. De ha a kiválasztottak '
         r'<b>különböző szerepet</b> kapnak (elnök és titkár, arany és ezüst), a sorrend számít: variáció. És fordítva: ha '
         r'„sorsolunk”, de csak egy csoportot kapunk (lottó), a sorrend nem számít. A kérdés mindig ez: <i>ha a '
         r'kiválasztottak helyet cserélnek, más lesz-e az eredmény?</i></p>'),
   kviz('Egy 20 fős osztályból 3 tanulót küldenek el egy versenyre, egyenrangú csapattagként. Hányféleképpen tehetik '
        'meg?', ['$\\binom{20}{3}=1140$', '$V_{20}^3=6840$', '$20^3=8000$', '$3^{20}$'], 0,
        jo="✔ Csapat, szerepek nélkül: a sorrend nem számít, $\\binom{20}{3}=\\frac{20\\cdot19\\cdot18}{6}=1140$.",
        nem="✘ A csapattagok egyenrangúak, a helycsere nem ad új csapatot: kombináció, $\\binom{20}3=1140$."),
 ]),
 ("Két csoportból — pontosan és legalább", [
   '<p class="lead">A Szvetkó-kampusz 10 lány és 8 fiú kadétja közül négyfős csapatot küld a Multiverzum Lottó '
   'döntőjébe. Hogy a sorrend nem számít, az biztos. A kérdés: hogyan kezeljük a feltételeket?</p>',
   doboz("pelda", "I.V.H. Akták — pontosan kettő",
         r'<p>Hányféleképpen állítható össze a csapat, ha <b>pontosan 2 lány</b> legyen benne?</p>'
         r'<p>Két egymás utáni döntés (szorzási szabály): a 2 lányt a 10 közül, a 2 fiút a 8 közül választjuk: '
         r'$$\binom{10}{2}\cdot\binom82=45\cdot28=1260.$$</p>', hid="pelda-ket-csoport"),
   doboz("pelda", "I.V.H. Akták — legalább egy",
         r'<p>Hányféleképpen, ha <b>legalább egy lány</b> legyen a csapatban?</p>'
         r'<p>Összes mínusz rossz (lásd <a href="tananyag-szorzasi-szabaly.html#pelda-legalabb">A1</a>): az összes '
         r'csapat $\binom{18}{4}=3060$, a lány nélküli (csak fiú) csapat $\binom84=70$. Tehát $3060-70=2990$.</p>',
         hid="pelda-legalabb-egy"),
   doboz("csapda", "Véd Vilmos csapda — a fiúkról megfeledkezett",
         r'<p>Vilmos a „pontosan 2 lány” feladatra $\binom{10}2=45$-öt mondott. Csakhogy a csapat négyfős: a maradék két '
         r'helyet fiúkkal kell kitölteni, és ezt $\binom82$-féleképpen tehetjük meg. A két döntés egymás után jön, tehát '
         r'szorzunk.</p>'),
   doboz("tetel", "Kiválasztani ugyanaz, mint kihagyni",
         r'<p>$$\binom nk=\binom n{n-k}.$$ Ha $n$ elemből kiválasztunk $k$-t, azzal egyúttal kiválasztottuk a kimaradó '
         r'$n-k$-t is. Számolásnál ez rövidít: $\binom{18}{16}=\binom{18}{2}=153$.</p>', hid="tetel-szimmetria"),
 ]),
 ("Visszafelé — és a lottó", [
   doboz("pelda", "I.V.H. Akták — hány csapat indult?",
         r'<p>Egy bajnokságon mindenki mindenkivel egyszer játszott, összesen 28 mérkőzés volt. Hány csapat indult?</p>'
         r'<p>Egy mérkőzés egy pár: $\binom n2=\frac{n(n-1)}{2}=28$, azaz $n(n-1)=56$. Két szomszédos egész szám szorzata '
         r'56: $8\cdot7$, tehát $n=8$ csapat indult.</p>', hid="pelda-visszafele"),
   doboz("erdekesseg", "A lottó",
         r'<p>A hazai Loto 7/39-ben 39 számból 7-et húznak ki, és a sorrend nem számít. A lehetséges húzások száma '
         r'$$\binom{39}{7}=15\,380\,937.$$ A magyar ötöslottóban (90-ből 5): $\binom{90}{5}=43\,949\,268$. Ha egy '
         r'szelvényt töltesz ki, mekkora esélyed van a telitalálatra? Erre a következő fejezet, a valószínűségszámítás '
         r'felel.</p>', hid="erdekesseg-lotto"),
   NEHEZ(3, "rácsút — hányféleképpen olvasható ki egy szó egy betűtáblázatból"),
   GY("#alap-10", "alap 10–12", "#kozep-8", "közép 8–10"),
   brief('<b>Nyalka Vili:</b> Összeállt a csapat. Az I.V.H.-archívumban viszont találtam egy különös háromszöget, tele '
         'ezekkel a számokkal. <b>Nagol:</b> A Pascal-háromszög. A kombinációk száma benne van — és a hatványozást is '
         'elvégzi helyettünk.', outro=True),
 ]),
]

# ---------------------------------------------------------------- oldalak
lapok = [
 lap(**T, fajl="tananyag-szorzasi-szabaly.html",
     cim="ÉS vagy VAGY — a szorzási és az összeadási szabály",
     alcim="Fadiagram, egymás utáni és egymást kizáró döntések, a korlátozott hely és a komplementer: összes mínusz rossz.",
     chip=KUL + " · 1/5", szakaszok=A1,
     elozo=("index.html", "Kombinatorika — áttekintés"),
     kovetkezo=("tananyag-permutaciok.html", "Permutációk")),
 lap(**T, fajl="tananyag-permutaciok.html",
     cim="Sorba állítva — permutációk",
     alcim="A faktoriális, a permutációk száma, feltételes sorrendek (blokk, nulla elöl) és az ismétléses permutáció.",
     chip=KUL + " · 2/5", szakaszok=A2,
     elozo=("tananyag-szorzasi-szabaly.html", "A szorzási és az összeadási szabály"),
     kovetkezo=("tananyag-variaciok.html", "Variációk")),
 lap(**T, fajl="tananyag-variaciok.html",
     cim="Dobogó és PIN-kód — variációk",
     alcim="Ismétlés nélküli és ismétléses variáció, számjegyes feladatok és az esetszétválasztás.",
     chip=KUL + " · 3/5", szakaszok=A3,
     elozo=("tananyag-permutaciok.html", "Permutációk"),
     kovetkezo=("tananyag-kombinaciok.html", "Kombinációk")),
 lap(**T, fajl="tananyag-kombinaciok.html",
     cim="Csapat, nem sorrend — kombinációk",
     alcim="Amikor a sorrend nem számít: $\\binom nk$, a döntési fa, pontosan és legalább, visszafelé számolás és a lottó.",
     chip=KUL + " · 4/5", szakaszok=A4,
     elozo=("tananyag-variaciok.html", "Variációk"),
     kovetkezo=("tananyag-binomialis-tetel.html", "A binomiális tétel")),
]
for u in lapok:
    print("✓", os.path.relpath(u))
