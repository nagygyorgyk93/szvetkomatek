# -*- coding: utf-8 -*-
"""4e/05 — osszefoglalo (F4, Csalopapir), terepkuldetes (F5p), I.V.H. Kihallgato Terem (F6h) es a temakor-index (F5).
Kuldetes: Multiverzum Lotto. Mentor: Nyalka Vili (Ved Vilmos kommental, Nagol tisztaz).
A terepkuldetes es a hazi adatai ujak: a felmerok (tiltott_4e_05) tipus+parameter szerint kizarva; a tananyag es a
Zsoldos-lista (build_fgy_4e_05) parameteres atfedeseit a futas kiirja, a tudatosakat indoklassal engedi.
Minden vegeredmeny ketfelekeppen: keplettel ES teljes felsorolassal (itertools) vagy sympyval."""
import sys, os
from itertools import permutations, product, combinations
from math import comb, perm, factorial as fakt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, brief, GYOKER
from fgy_common import cards, oldal, w
import build_fgy_4e_05 as FG               # a Zsoldos-lista paraméterei (WEB) és a tananyagé (TANANYAG)
import tiltott
TILT = tiltott.modul("tiltott_4e_05")      # a lista a repón kívül él (projektek/szvetkomatek/tiltott)
import sympy
from sympy import symbols, expand, Poly

x = symbols("x")
T = dict(tagozat="4e", mappa="05-kombinatorika", temakor="Kombinatorika")
KUL = "Multiverzum Lottó"
A1, A2, A3, A4 = ("tananyag-szorzasi-szabaly.html", "tananyag-permutaciok.html", "tananyag-variaciok.html",
                  "tananyag-kombinaciok.html")
B1, FA, FH = "tananyag-binomialis-tetel.html", "feladatok-kombinatorika.html", "feladatok-hazi.html"
E = []
chk, N, M, szamok, pol = FG.chk, FG.N, FG.M, FG.szamok, FG.pol


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


def TABLA(fejlec, sorok):
    th = "".join(f"<th>{c}</th>" for c in fejlec)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in s) + "</tr>" for s in sorok)
    fej = f"<tr>{th}</tr>" if any(fejlec) else ""
    return f'<div class="tblwrap"><table class="tt-table">{fej}{tr}</table></div>'


# ==================================================================== F4 — Csalópapír
# a Csalópapír példái (önteszt)
chk("CS anna", fakt(4) // (fakt(2) * fakt(2)), len(set(permutations("ANNA"))))
chk("CS dobogo", perm(10, 3), len(list(permutations(range(10), 3))))
chk("CS csapat", comb(10, 3), len(list(combinations(range(10), 3))))
chk("CS pin", 10 ** 4, len(list(product(range(10), repeat=4))))
chk("CS kezfogas", comb(8, 2), 8 * 7 // 2)
chk("CS legalabb", 9 * 10 * 10 - 9 ** 3, sum(1 for v in range(100, 1000) if "0" in str(v)))
chk("CS V=Ck!", perm(10, 3), comb(10, 3) * fakt(3))
chk("CS (x+2)^6 x^3", comb(6, 3) * 2 ** 3, Poly(expand((x + 2) ** 6), x).coeff_monomial(x ** 3))
# a Csalópapír is a weben van: a példái sem ütközhetnek a felmérőkkel (a tananyag példáit ismétli, az szándékos)
E += TILT.ellenoriz([("szo", "ANNA"), ("komb", (10, 3)), ("valaszt2", 8), ("ismvar", (10, 4)), ("binom", (2, 6)),
                     ("komb", (10, 2)), ("komb", (8, 2)), ("szamjegy", set(range(10)))])
chk("CS 2^n", sum(comb(6, k) for k in range(7)), 2 ** 6)
def svg_pascal_statikus(sorok=7):
    """A Pascal-háromszög 0–6. sora (sötét tinta a világos tervrajz-lapon)."""
    dx, dy, w_, h_ = 44, 30, 400, 30 * sorok + 16
    t = []
    for r in range(sorok):
        t.append(f'<text x="14" y="{24 + r * dy}" font-size="12" fill="#64748b" font-family="Georgia,serif">{r}.</text>')
        for k in range(r + 1):
            cx = w_ / 2 + (k - r / 2) * dx
            t.append(f'<text x="{cx:.0f}" y="{24 + r * dy}" text-anchor="middle" font-size="16" fill="#0f172a" '
                     f'font-family="Georgia,serif">{comb(r, k)}</text>')
    return (f'<div class="svgwrap"><svg viewBox="0 0 {w_} {h_}" width="{w_}" role="img" aria-label="A Pascal-háromszög '
            f'0–6. sora: 1; 1 1; 1 2 1; 1 3 3 1; 1 4 6 4 1; 1 5 10 10 5 1; 1 6 15 20 15 6 1">{"".join(t)}</svg></div>')


PASCAL = svg_pascal_statikus()

OSSZ = [
 ("🧭 Két kérdés minden feladat előtt", [
  r'<p>1. <b>Számít-e a sorrend?</b> (dobogó, tisztség, számjegy, sorba állás — igen; csapat, bizottság, lottószelvény, '
  r'kézfogás — nem) 2. <b>Ismétlődhet-e egy elem?</b> (PIN-kód, totó, érmedobás — igen; emberek, különböző tárgyak — '
  r'nem) 3. <b>Vannak-e egyforma, meg nem különböztethető elemek, és mindet felhasználjuk?</b> (ANNA, színes '
  r'zászlók — ez az ismétléses permutáció). A döntési fa a ' + h(A4, "tetel-kombinacio", "Kombinációk egységben") + r' van. '
  r'Ha a sorrend nem számít, de az ismétlés megengedett (ismétléses kombináció), az nem a mi tananyagunk.</p>',
  TABLA(["sorrend", "ismétlés", "neve", "jelölés és képlet", "példa"], [
      ["számít", "nincs; mind az $n$ elem", "permutáció " + h(A2, "def-permutacio"), "$P_n=n!$",
       "4 variáns sorban: $4!=24$"],
      ["számít", "egyforma elemek", "ismétléses permutáció " + h(A2, "tetel-ismetleses-permutacio"),
       "$P_n^{k_1,k_2,\\ldots,k_r}=\\dfrac{n!}{k_1!\\,k_2!\\cdots k_r!}$, ahol $k_1+\\ldots+k_r=n$",
       "ANNA: $\\dfrac{4!}{2!\\cdot2!}=6$"],
      ["számít", "nincs; $n$-ből $k$", "variáció " + h(A3, "def-variacio"),
       "$V_n^k=\\dfrac{n!}{(n-k)!}=n(n-1)\\cdots(n-k+1)$", '10 versenyzőből a háromhelyes dobogó: $10\\cdot9\\cdot8=720$'],
      ["számít", "megengedett", "ismétléses variáció " + h(A3, "tetel-ismetleses-variacio"), "$V_n^{k,i}=n^k$",
       "PIN-kód: $10^4$"],
      ["nem számít", "nincs; $n$-ből $k$", "kombináció " + h(A4, "def-kombinacio"),
       "$C_n^k=\\dbinom nk=\\dfrac{n!}{k!\\,(n-k)!}$", "10 főből 3 fős csapat: $\\dbinom{10}3=120$"]]),
  (
      '<p class="le halvany">Az ismétlés nélküli variációnál és kombinációnál $0\\le k\\le n$; az ismétléses '
      'variációnál $k$ nagyobb is lehet $n$-nél. A darabszámok nemnegatív egészek, és $0!=1$. A kombináció '
      'és a variáció kapcsolata: $V_n^k=\\binom nk\\cdot k!$ — minden csapat $k!$-féle sorrendben állhat a '
      'dobogón '
  ) + h(A4, "tetel-kombinacio") + '.</p>',
 ]),

 ("✖️ ÉS, ➕ VAGY — a szorzási és az összeadási szabály", [
  r'<ul><li><b>Szorzási szabály</b> ' + h(A1, "tetel-szorzasi-szabaly") + r': ha egy választás egymás utáni lépésekből '
  r'áll (<i>ÉS</i>), a lehetőségek száma a lépések lehetőségeinek szorzata — fadiagrammal is látszik. Feltétel: egy '
  r'lépés lehetőségeinek <i>száma</i> nem függhet attól, mit választottunk korábban.</li>'
  r'<li><b>Összeadási szabály</b> ' + h(A1, "tetel-osszeadasi-szabaly") + (
                                                                                 ': ha a lehetőségek egymást kizáró esetekre bomlanak (<i>VAGY</i>), az egyes esetekhez tartozó '
                                                                                 'lehetőségek számát összeadjuk.</li><li><b>Korlátozott hely először:</b> a 0 nem állhat elöl; a '
                                                                                 'páros szám utolsó jegye páros — ha a kettő ütközik (0 a végén?), a lehetőségek száma a korábbi '
                                                                                 'választástól függ — ilyenkor bonts esetekre '
                                                                             ) + h(A3, "pelda-paros") + r'.</li>'
  r'<li><b>„Legalább egy”</b> = összes − „egy sincs” ' + h(A1, "pelda-legalabb") + r': a háromjegyű számok közül '
  r'$900-9^3=171$-ben szerepel 0-s számjegy.</li></ul>',
 ]),

 ("🔢 Faktoriális és binomiális együttható", [
  TABLA(["", "képlet", "jelentés"], [
      ["$n!$", "$1\\cdot2\\cdots n$, $\\;0!=1$", "$n$ különböző elem sorrendjei " + h(A2, "def-faktorialis")],
      ["$\\dbinom nk$", "$\\dfrac{n!}{k!\\,(n-k)!}$", "$n$ elemből $k$-t választunk, a sorrend nem számít"],
      ["$\\dbinom n0=\\dbinom nn=1$", "", "egyféleképpen választunk semmit, illetve mindent"],
      ["$\\dbinom nk=\\dbinom n{n-k}$", "szimmetria " + h(A4, "tetel-szimmetria"), "a kiválasztottak helyett a "
       "kimaradókat is kiválaszthatjuk"],
      ["$\\dbinom n2=\\dfrac{n(n-1)}{2}$", "", "kézfogások, körmérkőzés " + h(A4, "pelda-kezfogas") + ": 8 fő → $28$"]]),
  r'<p><b>Pontosan</b> ' + h(A4, "pelda-ket-csoport") + (
                                                            ': ha két csoportból pontosan megadott számú elemet választunk, a két kombináció szorzata a válasz '
                                                            '(pl. 10 lány és 8 fiú közül pontosan 2 lány egy 4 fős csapatban: $\\binom{10}2\\binom82$). '
                                                            '<b>Legalább egy:</b> az egyes megfelelő esetekben adódó lehetőségek számának összege — vagy '
                                                            'egyszerűbben a komplementer segítségével: összes − „egy sincs” '
                                                        ) + h(A4, "pelda-legalabb-egy") + '.</p>',
 ]),

 ("🔺 A Pascal-háromszög és a binomiális tétel", [
  PASCAL,
  r'<p>Minden sor két szélén $1$ áll, minden belső szám a fölötte álló két szám összege; az $n$-edik sor az $\binom n0,\binom n1,'
  r'\ldots,\binom nn$ számok sora, szimmetrikus, és az összege $2^n$ ' + h(B1, "tetel-pascal") + '.</p>'
  r'<p><b>Binomiális tétel</b> ' + h(B1, "tetel-binomialis") + (
                                                                     ' (minden $n$ természetes számra): $$(a+b)^n=\\binom n0a^n+\\binom n1a^{n-1}b+\\binom '
                                                                     'n2a^{n-2}b^2+\\ldots+\\binom nnb^n.$$ A formális kifejtésnek $n+1$ tagja van (összevonás után '
                                                                     'kevesebb is maradhat); a <b>$(k+1)$-edik tag</b> $T_{k+1}=\\binom nka^{n-k}b^k$ '
                                                                 )
  + h(B1, "tetel-altalanos-tag") + r'. Az $(a-b)^n$ kifejtésében az előjelek váltakoznak.</p>'
  r'<p><b>Egy együttható</b> ' + h(B1, "pelda-egyutthato") + r': az $(x+2)^6$-ban az $x^3$-ös tag $\binom63x^3\cdot2^3=160x^3$. '
  r'A tagok együtthatóinak összege $x=1$ helyettesítéssel adódik; $(1+1)^n=2^n$ — egy $n$ elemű halmaz részhalmazainak '
  r'száma ' + h(B1, "erdekesseg-reszhalmazok") + '.</p>',
 ]),

 ("⚠️ Véd Vilmos csapdái — amelyeken a legtöbben elcsúsznak", [
  (
      '<div class="doboz csapda"><p class="cim"><span class="ikon">⚠️</span> A kilenc leggyakoribb '
      'hiba</p><ol class="reszfeladatok"><li><b>ÉS vagy VAGY:</b> 3 zakó és 2 nadrág $3\\cdot2=6$ szett, '
      'nem $5$; „vagy burek, vagy pizza” viszont összeadás.</li><li><b>A nulla előre tolakszik:</b> '
      '$9\\cdot9\\cdot8=648$ különböző jegyű háromjegyű szám van, nem '
      '$10\\cdot9\\cdot8=720$.</li><li><b>Egyben számolni ott, ahol esetek vannak:</b> ha az utolsó jegy '
      'lehet 0 is, a páros számokat két esetre bontsd.</li><li><b>A blokk belseje:</b> ha kettő egymás '
      'mellett áll, a blokkon belül is van sorrend — szorozz $2!$-sal.</li><li><b>Csak az egyik '
      'ismétlődés:</b> az ANNA-nál $2!\\cdot2!$-sal kell osztani: $6$, nem $12$.</li><li><b>Ismétlődhet '
      'vagy nem?</b> PIN-kód: $10^4$ — nem $10\\cdot9\\cdot8\\cdot7$.</li><li><b>A „kiválaszt” szó csal:</b> '
      'ha a kiválasztottak különböző szerepet kapnak (elnök és titkár), az variáció.</li><li><b>A többi '
      'hely is számít:</b> „pontosan 2 lány” egy 4 fős csapatban: $\\binom{10}2\\cdot\\binom82$, nem '
      '$\\binom{10}2$.</li><li><b>A hatvány a zárójel egészére vonatkozik:</b> szorzatnál minden tényezőre '
      'szétosztható ($(2x)^3=8x^3$, nem $2x^3$), összegnél nem osztható szét így: $(a+b)^2=a^2+2ab+b^2$ — '
      'a kifejtéshez a binomiális tétel kell.</li></ol></div>'
  ),
 ]),

 ("Mit hol találsz?", [
  r'<div class="gyakorolj"><span class="ikon">🧭</span><div>'
  r'<p><b>Tananyag:</b> <a href="' + A1 + r'">szorzási és összeadási szabály</a> · <a href="' + A2 + r'">permutációk</a> · '
  r'<a href="' + A3 + r'">variációk</a> · <a href="' + A4 + r'">kombinációk</a> · <a href="' + B1 + r'">Pascal-háromszög és '
  r'binomiális tétel</a>.</p>'
  r'<p><b>Gyakorlás:</b> <a href="' + FA + r'">Zsoldos-lista</a> · <a href="' + FH + r'">I.V.H. Kihallgató Terem</a> '
  r'(házi). A témakört a <a href="terepkuldetes.html">' + KUL + r'</a> küldetés zárja, a következő fejezetben pedig '
  r'a valószínűség jön — ott ezekkel a számokkal osztunk.</p></div></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Csalópapír — a témakör egy lapon", cim_tiszta="Csalópapír", itt="Csalópapír",
    alcim="A két döntő kérdés, a képletek, a faktoriális és a binomiális együttható, a Pascal-háromszög és a "
          "binomiális tétel egy lapon — ismétléshez, az ellenőrző előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló", szakaszok=OSSZ,
    elozo=(FH, "I.V.H. Kihallgató Terem"), kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p — terepküldetés (önteszt; a kulcs privát DOCX)
LOTTO = set(range(5))
_huzasok = list(combinations(range(30), 5))
TEREP_SZAM = {
 "I-a": chk("I-a", 5 * 4 * 6 * (3 + 1), len(list(product(range(5), range(4), range(6), range(4))))),
 "I-b": chk("I-b", 5 * 4 * 6 * 3, len(list(product(range(5), range(4), range(6), range(3))))),
 "I-c": chk("I-c", 6 ** 4 - 5 ** 4, sum(1 for p in product("ABCDEF", repeat=4) if "A" in p)),
 "II-a": chk("II-a", 2 * fakt(7), sum(1 for p in permutations(range(8)) if 0 in (p[0], p[-1]))),
 "II-b": chk("II-b", fakt(3) * fakt(6), sum(1 for p in permutations(range(8))
                                            if max(p.index(i) for i in range(3)) - min(p.index(i) for i in range(3)) == 2)),
 "II-c": chk("II-c", fakt(9) // (fakt(4) * fakt(3) * fakt(2)), len(set(permutations("PPPPZZZFF")))),
 "III-a": chk("III-a", comb(30, 5), len(_huzasok)),
 "III-b": chk("III-b", comb(5, 3) * comb(25, 2), sum(1 for c in _huzasok if len(LOTTO & set(c)) == 3)),
 "III-c": chk("III-c", comb(30, 5) - comb(25, 5), sum(1 for c in _huzasok if LOTTO & set(c))),
 "III-d": chk("III-d", perm(30, 5), comb(30, 5) * fakt(5)),
 "III-e": chk("III-e", sum(comb(5, k) for k in range(6)), 2 ** 5, len([s for k in range(6) for s in combinations(range(5), k)])),
 "III-f": chk("III-f", comb(4, 2) * 3 ** 2 * (-1) ** 2, Poly(expand((3 * x - 1) ** 4), x).coeff_monomial(x ** 2)),
 "IV-a": chk("IV-a", perm(7, 3), len(list(permutations(range(7), 3)))),
 "IV-b": chk("IV-b", 3 * fakt(3), szamok([0, 3, 6, 9], 4, False)),
 "IV-c": chk("IV-c", fakt(6) // (fakt(3) * fakt(3)), len(set(permutations("LALALA")))),
 "IV-d": chk("IV-d", comb(11, 4) - comb(5, 4),
             sum(1 for c in combinations([("L", i) for i in range(6)] + [("F", i) for i in range(5)], 4)
                 if any(t == "L" for t, _ in c))),
}
if expand((x + 5) ** 3) != x ** 3 + 15 * x ** 2 + 75 * x + 125 or comb(7, 3) != 35 or 6 * comb(10, 3) != 720:
    E.append("IV-e / Vilmos-számok")
print("F5p önteszt:", "OK" if not FG.E and not E else (FG.E, E))

TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nyalka Vili:</b> Hölgyeim és uraim, kadétok és variánsok — a Multiverzum Lottó sorsolására mindenki '
         'kiöltözik, sorba áll, szelvényt tölt ki, és <i>pontosan tudja</i>, hány lehetősége van. '
         '<b>Véd Vilmos:</b> 🌮 <i>Burek-matek:</i> „Sok. Nagyon sok. Minek számolni?” <b>Nagol:</b> Mert a „sok” '
         'nem szám. Négy fázis: Vili ruhatára és belépőkódja (szorzási és összeadási szabály), a Multiverzum-tabló (permutációk), maga a '
         'lottó (kombinációk és a binomiális tétel), végül Vilmos jegyzőkönyve, tele hibás leszámlálással.'),
   r'<p>Minden lépésnél írd le, melyik szabályt vagy képletet használtad, és <b>miért</b> (számít-e a sorrend, '
   r'ismétlődhet-e egy elem, milyen esetekre bontottál). Számológép használható. A szöveges kérdésekre két-három '
   r'mondatban válaszolj.</p>'
   r'<p>A 🔴 jelű IV. fázisban a számolás csak eszköz: ott a <b>megfogalmazott érvelés</b> ér annyit, mint máshol a '
   r'számítás. Mind a négy fázis egyformán számít.</p>'
   r'<p><i>Tervezz rá nagyjából két órát; ez beadandó munka, nem órai feladat.</i></p>',
 ]),

 ("I. fázis — Vili ruhatára és belépőkódja", [
   r'<p>Nyalka Vili gardróbjában 5 zakó, 4 nadrág, 6 nyakkendő és 3 kalap lóg (mind különböző).</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Hányféle öltözéket állíthat össze, ha zakó, nadrág és nyakkendő kötelező, kalapot pedig vagy felvesz '
   r'(egyet), vagy nem?</li>'
   r'<li>Ezek közül hány öltözékben van kalap?</li>'
   r'<li>A sorsolásra négykarakteres belépőkódot kap, amelynek minden karaktere az A, B, C, D, E, F betűk egyike (egy '
   r'betű többször is szerepelhet). Hány olyan kód van, amelyben legalább egy A szerepel? Oldd meg komplementerrel, '
   r'és írd le, miért egyszerűbb így!</li>'
   r'<li>Fogalmazd meg a saját szavaiddal: leszámláláskor mikor szorzunk, és mikor adunk össze? Mondj mindkettőre egy '
   r'saját, hétköznapi példát!</li>'
   r'</ol>',
 ]),

 ("II. fázis — A Multiverzum-tabló", [
   r'<p>A sorsolás előtt 8 különböző variáns áll egy sorba a Multiverzum-tablónál; köztük van Nyalka Vili, Véd Vilmos '
   r'és Mini-Vili.</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Hányféle sorrend lehetséges, ha Nyalka Vili a sor valamelyik szélén áll?</li>'
   r'<li>Hányféle sorrend lehetséges, ha a három Vilmos-variáns — Nyalka Vili, Véd Vilmos és Mini-Vili — egymás mellett '
   r'áll, bármilyen sorrendben?</li>'
   r'<li>A tabló fölé zászlósort tűznek ki: 4 piros, 3 zöld és 2 fehér zászlót (az egyforma színűek nem '
   r'különböztethetők meg). Hányféle színsorrend lehetséges?</li>'
   r'<li>A b) és a c) feladatban is „csoportok” vannak. Miért szorzunk a b)-ben, és miért osztunk a c)-ben? Fogalmazd '
   r'meg két-három mondatban!</li>'
   r'</ol>',
 ]),

 ("III. fázis — A lottó", [
   r'<p>A Multiverzum Lottón 30 számból 5-öt húznak ki; a szelvényen 5 számot kell megjelölni, a sorrend nem számít. '
   r'A b) és a c) részben a húzás már megtörtént: egy adott, kihúzott ötöshöz számolj!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>Hányféleképpen tölthető ki egy szelvény?</li>'
   r'<li>Hány kitöltésen lesz pontosan 3 találat?</li>'
   r'<li>Hány kitöltésen lesz legalább 1 találat?</li>'
   r'<li>A sorsoláson a kihúzott számokat húzási sorrendben is kihirdetik. A húzás előtt nézve összesen hányféle '
   r'kihirdetési sor lehetséges? Hányszorosa ez az a) eredményének, és miért?</li>'
   r'<li>Nagol szerint $\binom50+\binom51+\binom52+\binom53+\binom54+\binom55=2^5$. Igazold a binomiális tétellel, '
   r'és magyarázd meg, mit számol meg ez az összeg az 5 kihúzott szám halmazán!</li>'
   r'<li>Vili szerencseszáma a $(3x-1)^4$ kifejtésében az $x^2$ együtthatója. Mennyi ez?</li>'
   r'</ol>',
 ]),

 ("🔴 IV. fázis — Véd Vilmos jegyzőkönyve", [
   r'<p>Vilmos leadta a saját „megoldásait” az I.V.H.-nak. Mind az öt hibás. Mindegyiknél nevezd meg egy mondatban a '
   r'hibát, és add meg a helyes eredményt!</p>'
   r'<ol class="reszfeladatok">'
   r'<li>„7 csapat közül az arany-, az ezüst- és a bronzérem kiosztása (holtverseny nincs, egy csapat egy érmet kap): '
   r'$\binom73=35$-féle.”</li>'
   r'<li>„A 0, 3, 6, 9 számjegyekből, mindegyiket egyszer felhasználva $4!=24$ négyjegyű szám képezhető.”</li>'
   r'<li>„A LALALA betűinek sorrendjei: $6!=720$.”</li>'
   r'<li>„6 lány és 5 fiú közül olyan 4 fős csapat, amelyben legalább egy lány van: előbb kiválasztom a lányt '
   r'(6-féleképpen), a maradék 3 helyre bárki jöhet a többi 10 közül: $6\cdot\binom{10}3=720$.”</li>'
   r'<li>„$(x+5)^3=x^3+3x^2+3x+125$.”</li>'
   r'<li>Mi a közös a hibákban? Fogalmazd meg két-három mondatban, hogyan lehetett volna <b>ellenőrizni</b> az egyes '
   r'eredményeket (például kis esetre felsorolással, vagy $x=1$ behelyettesítésével)!</li>'
   r'</ol>',
   brief('<b>Nagol:</b> A sorsolás lezajlott, a lehetőségek megszámolva. A megoldásaidat a tanárod ellenőrzi; a kulcs '
         'nem kerül a hálózatra. <b>Nyalka Vili:</b> Több mint százezer kitöltés, és én mindegyikben elegáns vagyok. '
         '<b>Mr. Szürreál</b> (I.V.H.): Megszámolni könnyű. A kérdés az, <i>mekkora az esély</i>. '
         '<b>Véd Vilmos:</b> Azt majd meglátjuk. A következő fejezet: <i>A Túlélés Esélyei</i>.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Négy fázis: Nyalka Vili ruhatára, a Multiverzum-tabló, maga a lottó és Véd Vilmos hibás jegyzőkönyve. "
          "Beadható projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés", szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Csalópapír"), kovetkezo=("index.html", "Kombinatorika — a témakör"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h — I.V.H. Kihallgató Terem (házi)
HA_ = [
 ("Az I.V.H. büféjében 6-féle szendvics, 4-féle üdítő és 3-féle gyümölcs kapható. Hányféleképpen választhat egy kadét",
  ["egy szendvicset és egy üdítőt?", "egy szendvicset, egy üdítőt és egy gyümölcsöt?",
   "egyetlen dolgot: egy szendvicset vagy egy gyümölcsöt?"],
  [M(chk("h-alap-1a", 6 * 4, len(list(product(range(6), range(4)))))),
   M(chk("h-alap-1b", 6 * 4 * 3, len(list(product(range(6), range(4), range(3)))))),
   M(chk("h-alap-1c", 6 + 3, 9))]),
 ("Ismétléses permutáció:",
  ["Hány különböző sorrendje van a BARACK szó betűinek (értelmetlen betűsor is számít)?",
   "Hány ötjegyű szám írható fel a 2, 2, 2, 7, 7 számjegyekből (mindegyiket felhasználva)?",
   "3 piros, 1 kék és 1 zöld zászlót tűzünk ki egy sorba. Hányféle színsorrend lehetséges?"],
  [M(chk("h-alap-2a", fakt(6) // fakt(2), len(set(permutations("BARACK"))))),
   M(chk("h-alap-2b", fakt(5) // (fakt(3) * fakt(2)), len(set(permutations([2, 2, 2, 7, 7]))))),
   M(chk("h-alap-2c", fakt(5) // fakt(3), len(set(permutations("PPPKZ")))))]),
 ("Egy 13 fős szakkörben (tagja Anna is):",
  ["hányféleképpen választhatnak elnököt és titkárt (két különböző tagot)?",
   "hányféleképpen választhatnak két egyenrangú küldöttet?",
   "hány olyan választás van az a) részben, amelyben Anna az elnök?"],
  [M(chk("h-alap-3a", perm(13, 2), len(list(permutations(range(13), 2))))),
   M(chk("h-alap-3b", comb(13, 2), len(list(combinations(range(13), 2))))),
   M(chk("h-alap-3c", 12, sum(1 for p in permutations(range(13), 2) if p[0] == 0)))]),
 ("Binomiális tétel:",
  ["Fejtsd ki: $(x+4)^3$", "Számold ki: $\\binom92$ és $\\binom97$", "Hány tagja van az $(a+b)^9$ kifejtésének?"],
  [f"${pol((x + 4) ** 3)}$",
   f"${chk('h-alap-4b', comb(9, 2), 36)}$ és ${chk('h-alap-4b2', comb(9, 7), comb(9, 2))}$",
   M(chk("h-alap-4c", 9 + 1, len(Poly(expand((symbols('a') + symbols('b')) ** 9)).terms())))]),
]
HK_ = [
 ("A 0, 1, 3, 5, 7, 9 számjegyekből háromjegyű számokat képezünk; egy számjegy legfeljebb egyszer szerepelhet.",
  ["Hány ilyen szám van?", "Ezek közül hány osztható 5-tel?"],
  [M(chk("h-kozep-1a", 5 * 5 * 4, szamok([0, 1, 3, 5, 7, 9], 3, False))),
   M(chk("h-kozep-1b", perm(5, 2) + 4 * 4, szamok([0, 1, 3, 5, 7, 9], 3, False, lambda p: p[-1] in (0, 5))))]),
 ("Egy 7 lányból és 5 fiúból álló csoportból 4 fős bizottságot választanak. Hányféleképpen, ha a bizottságban",
  ["pontosan 2 fiú van?", "legalább 1 fiú van?"],
  [M(chk("h-kozep-2a", comb(5, 2) * comb(7, 2),
         sum(1 for c in combinations([("L", i) for i in range(7)] + [("F", i) for i in range(5)], 4)
             if sum(t == "F" for t, _ in c) == 2))),
   M(chk("h-kozep-2b", comb(12, 4) - comb(7, 4),
         sum(1 for c in combinations([("L", i) for i in range(7)] + [("F", i) for i in range(5)], 4)
             if any(t == "F" for t, _ in c))))]),
]
HN_ = [
 ("Hány olyan négyjegyű szám van, amelynek számjegyei balról jobbra haladva",
  ["szigorúan növekednek (pl. 1358)?", "szigorúan csökkennek (pl. 9520)?"],
  [M(chk("h-nehez-1a", comb(9, 4), sum(1 for v in range(1000, 10000) if list(str(v)) == sorted(set(str(v))) and len(set(str(v))) == 4))),
   M(chk("h-nehez-1b", comb(10, 4), sum(1 for v in range(1000, 10000)
                                          if list(str(v)) == sorted(set(str(v)), reverse=True) and len(set(str(v))) == 4)))]),
]

# ==================================================================== ÖNELLENŐRZÉS: tiltott és már használt adatok
UJ_TEREP = [("ismvar", (6, 4)), ("szo", "LALALA"), ("szamjegy", {0, 3, 6, 9}), ("komb", (30, 5)), ("komb", (25, 2)),
            ("komb", (25, 5)), ("komb", (5, 3)), ("komb", (11, 4)), ("komb", (5, 4)), ("komb", (7, 3)),
            ("binom", (5, 3))]
UJ_HAZI = [("szo", "BARACK"), ("szamjegy", {2, 7}), ("valaszt2", 13), ("binom", (4, 3)), ("komb", (9, 2)),
           ("komb", (9, 7)), ("szamjegy", {0, 1, 3, 5, 7, 9}), ("komb", (5, 2)), ("komb", (7, 2)), ("komb", (12, 4)),
           ("komb", (7, 4)), ("komb", (9, 4)), ("komb", (10, 4))]
E += TILT.ellenoriz(UJ_TEREP + UJ_HAZI)


def _k(t_, p_):
    return (t_, frozenset(p_) if isinstance(p_, set) else p_)


KORABBI = {_k(*a): "Zsoldos-lista" for a in FG.WEB} | {a: "tananyag" for a in FG.TANANYAG}
ENGEDETT = {
 ("komb", (5, 2)): "házi közép-2 a): 5 fiúból 2 (bizottság); a Zsoldos-listán a joker rácsvonalai",
 ("komb", (7, 4)): "házi közép-2 b): a komplementer (csak lányok); a Zsoldos-listán 7 labdából 4",
 ("komb", (9, 4)): "házi nehéz-1 a): növekvő számjegyek; a Zsoldos-listán vezető + 4 képviselő",
 ("komb", (5, 3)): "terep III/b: 5 találatból 3; a Zsoldos-listán nincs, a tananyagban nincs",
 ("komb", (11, 4)): "terep IV/d: 11 fő közül 4 (Vilmos hibájának javítása); a Zsoldos-listán 11 fiúból 4",
}
for a in UJ_TEREP + UJ_HAZI:
    k = _k(*a)
    if k in KORABBI and k not in ENGEDETT:
        E.append(("már használt", k, KORABBI[k]))
for a in UJ_TEREP:
    if _k(*a) in {_k(*b) for b in UJ_HAZI}:
        E.append(("terep = házi", a))
assert not E and not FG.E, (E, FG.E)
print("F6h önteszt és tiltott-ellenőrzés: OK")

body = [
 '    <h2 id="alap">🟢 Alapszint — Zöldfülű</h2>\n' + cards(HA_, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — X-Force</h2>\n' + cards(HK_, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Maximális erőbedobás</h2>\n' + cards(HN_, "nehez", "nehez"),
]
oldal(**T, fajl="feladatok-hazi.html", cim="I.V.H. Kihallgató Terem", h1="I.V.H. Kihallgató Terem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span><span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a szorzási szabálytól a binomiális tételig — házi feladatnak és az ellenőrző "
            "előtti bemelegítésnek. Az I.V.H. minden választ ellenőriz: a végeredmény lenyitható, de csak a számolás "
            "után nézd meg!",
      sections_html="\n".join(body), ossz_nev="Csalópapírt",
      prev=FA, prevc="Zsoldos-lista — Kombinatorika", nxt="osszefoglalo.html", nxtc="Csalópapír")
print("✓ feladatok-hazi.html | Alap", len(HA_), "Közép", len(HK_), "Nehéz", len(HN_))


# ==================================================================== F5 — témakör-index
def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


KT = {
 "A1": kartya(A1, "ÉS vagy VAGY — a szorzási és az összeadási szabály", 'Szorzási és összeadási szabály, fadiagram, azonosítók, „legalább egy” komplementerrel'),
 "A2": kartya(A2, "Sorba állítva — permutációk", "$n!$, ismétlés nélküli és ismétléses permutáció, blokk, a 0 nem állhat elöl"),
 "A3": kartya(A3, "Dobogó és PIN-kód — variációk", "Ismétlés nélküli és ismétléses variáció, számjegyes feladatok feltételekkel"),
 "A4": kartya(A4, "Csapat, nem sorrend — kombinációk", "$\\binom nk$, döntési fa, „pontosan” és „legalább”, kézfogás és visszafelé számolás; a lottó"),
 "B1": kartya(B1, "A Pascal-háromszög és a binomiális tétel", "Interaktív Pascal-háromszög, $(a+b)^n$ kifejtése, egy tag és egy együttható, $2^n$ részhalmaz"),
 "f": kartya(FA, "🏋️ Zsoldos-lista — Kombinatorika", "A szorzási szabálytól a binomiális tételig — 30 feladat három szinten és egy joker"),
 "hazi": kartya(FH, "🕹️ I.V.H. Kihallgató Terem — házi feladatok", "Rövid, vegyes gyakorlósor az ellenőrző előtti bemelegítéshez"),
 "tk": kartya("terepkuldetes.html", "🎯 " + KUL, "Négyfázisú záróküldetés — Vili ruhatára, a Multiverzum-tabló, a lottó és Vilmos hibás jegyzőkönyve"),
 "ossz": kartya("osszefoglalo.html", "📇 Csalópapír", "A két döntő kérdés, a képletek, a Pascal-háromszög és a binomiális tétel egy lapon"),
}


def racs(*kulcsok):
    return '    <div class="racs">\n' + "\n".join(KT[k] for k in kulcsok) + '\n    </div>\n'


INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kombinatorika | 4e | Szvetkó matek</title>
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
  <span class="itt">Kombinatorika</span>
</nav>
<div class="hero">
  <h1>Kombinatorika</h1>
  <p class="alcim">Hányféleképpen? Szorzási és összeadási szabály, permutációk, variációk és kombinációk — aztán a
  Pascal-háromszög és a binomiális tétel.</p>
  <div class="meta-sor"><span class="chip ora">9 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🎰 <b>05 — Multiverzum Lottó.</b> Mentor: <b>Nyalka Vili</b>, Véd Vilmos elegáns variánsa
  (öltönyök, nyakkendők, kalapok — a szorzási szabály ruhatára). A lottósorsolásra mindenki kiöltözik, sorba áll és
  szelvényt tölt ki — mi pedig megszámoljuk, hányféleképpen. Két kérdés vezet végig a témakörön: számít-e a sorrend, és
  ismétlődhet-e egy elem? Véd Vilmos szerint „sok”. Nagol szerint a „sok” nem szám.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>🧮 Leszámlálás — Nyalka Vili</h3>
''' + racs("A1", "A2", "A3", "A4") + '''
    <h3>🔺 A binomiális tétel — Nyalka Vili és Nagol</h3>
''' + racs("B1") + '''
    <h2>Feladatgyűjtemény</h2>
''' + racs("f", "hazi") + '''
    <h2>Terepküldetés</h2>
''' + racs("tk") + '''
    <h2>Összefoglaló</h2>
''' + racs("ossz") + '''
    <p class="le halvany"><b>Ajánlott sorrend:</b> az öt tananyag-egység sorban, közben a Zsoldos-lista megfelelő
    feladatai (az egységek végén a Gyakorolj!-sávok mutatják, melyik feladat hová tartozik), a végén az I.V.H.
    Kihallgató Terem. A témakört a negyedik ellenőrző méri. A Csalópapír az ismétlést szolgálja, a témakört pedig a
    <i>Multiverzum Lottó</i> záróküldetés zárja.</p>
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
