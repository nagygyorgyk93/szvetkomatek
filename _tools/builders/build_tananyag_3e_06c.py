# -*- coding: utf-8 -*-
"""3e/06 — C blokk: hianyos es teljes indukcio (C). Mentor: Prizma es Kanrak.
Rovid, olvasmanyos egyseg: SZAMONKERES NINCS, ezert nincs .gyakorolj sav sem."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, abra

T = dict(tagozat="3e", mappa="06-indukcio-sorozatok", temakor="Matematikai indukció. Sorozatok")
KUL = "A Végtelen Mutáció"
KEK, BORO, ZOLD, PIROS, TINTA, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#0f172a", "#475569"

# ---------------------------------------------------------------- önteszt
from sympy import isprime, factorint, binomial, simplify, symbols, Rational
E = []
def chk(nev, kapott, vart):
    if kapott != vart:
        E.append((nev, kapott, vart))

n = symbols("n", positive=True)
chk("prim-0-39", all(isprime(k*k + k + 41) for k in range(40)), True)
chk("prim-40", sorted(factorint(40*40 + 40 + 41).items()), [(41, 2)])
chk("prim-41", isprime(41*41 + 41 + 41), False)
chk("korosztas", [1 + binomial(k, 2) + binomial(k, 4) for k in range(1, 7)], [1, 2, 4, 8, 16, 31])
# a "+5"-os alkeplet: a lepes hibatlan, a bazis hamis
S = lambda m: m*(m + 1)/2 + 5
chk("alkeplet-lepes", simplify(S(n + 1) - (S(n) + (n + 1))), 0)
chk("alkeplet-bazis", S(1) == 1, False)
chk("paratlan-osszeg", [sum(2*i - 1 for i in range(1, m + 1)) for m in range(1, 7)],
    [1, 4, 9, 16, 25, 36])
chk("paratlan-lepes", simplify((n**2 + (2*(n + 1) - 1)) - (n + 1)**2), 0)
chk("szamtani-S5", 5*(2*6 + 4*4)//2, 70)
chk("oszthatosag-bazis", (1**3 - 1) % 6, 0)
chk("oszthatosag-azonossag", simplify(((n + 1)**3 - (n + 1)) - ((n**3 - n) + 3*n*(n + 1))), 0)
chk("oszthatosag-minta", [(k**3 - k) % 6 for k in range(1, 8)], [0]*7)
assert not E, E
print("sympy önteszt: OK")


# ---------------------------------------------------------------- ábra
def svg_domino():
    """Dominosor: az elso dol (bazis), mindegyik magaval rantja a kovetkezot (lepes)."""
    x0, dx, alap, m, sz = 58, 62, 118, 56, 15
    ki = ['<svg viewBox="0 0 440 175" width="440" height="175" role="img" '
          'aria-label="Dominósor: az első dominó eldőlve, a többi állva; nyilak jelzik, hogy '
          'minden dominó magával rántja a következőt">',
          f'  <defs><marker id="dnyil" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="5" '
          f'markerHeight="5" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{KEK}"/></marker></defs>',
          f'  <line x1="24" y1="{alap}" x2="416" y2="{alap}" stroke="{TINTA}" stroke-width="1.4"/>']
    for i in range(6):
        x = x0 + i*dx
        if i == 0:
            ki.append(f'  <g transform="rotate(-62 {x} {alap})">'
                      f'<rect x="{x - sz/2:.0f}" y="{alap - m}" width="{sz}" height="{m}" rx="2" '
                      f'fill="#dbeafe" stroke="{KEK}" stroke-width="1.8"/></g>')
        else:
            ki.append(f'  <rect x="{x - sz/2:.0f}" y="{alap - m}" width="{sz}" height="{m}" rx="2" '
                      f'fill="#f1f5f9" stroke="{TINTA}" stroke-width="1.6"/>')
        if 0 < i < 5:
            ki.append(f'  <path d="M{x + 9:.0f},{alap - m - 8} Q{x + dx/2:.0f},'
                      f'{alap - m - 26} {x + dx - 11:.0f},{alap - m - 8}" fill="none" '
                      f'stroke="{KEK}" stroke-width="1.4" marker-end="url(#dnyil)"/>')
    ki.append(f'  <text x="{x0}" y="{alap + 20}" font-size="12" fill="{KEK}" text-anchor="middle" '
              f'font-weight="600">bázis</text>')
    ki.append(f'  <text x="{x0}" y="{alap + 34}" font-size="11" fill="{SZURKE}" '
              f'text-anchor="middle">az első eldől</text>')
    ki.append(f'  <text x="{x0 + 3.2*dx:.0f}" y="24" font-size="12" fill="{KEK}" '
              f'text-anchor="middle" font-weight="600">lépés</text>')
    ki.append(f'  <text x="{x0 + 3.2*dx:.0f}" y="38" font-size="11" fill="{SZURKE}" '
              f'text-anchor="middle">amelyik eldől, magával rántja a következőt</text>')
    ki.append(f'  <text x="416" y="{alap + 20}" font-size="12" fill="{SZURKE}" '
              f'text-anchor="end">… és így tovább, minden n-re</text>')
    ki.append('</svg>')
    return "\n".join(ki)


SVG_DOMINO = svg_domino()

# ---------------------------------------------------------------- C
C = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Prizma és Kanrak:</b> A képletek működnek — de honnan tudjuk, hogy a <b>századik</b> '
         'lépésnél is működnek? Maxi éppen erre játszik: mutat néhány jó lépést, és arra épít, hogy '
         'elhisszük, örökre így marad. Egy állítást <b>minden</b> lépésre kell igazolni — és van rá '
         'egy módszer, amivel ez két lépésben megy.'),
   doboz("erdekesseg", "Mit kell ebből tudni?",
         r'<p>Ezt az egységet <b>nem kérjük vissza</b>: nem lesz belőle sem feladat, sem házi, sem '
         r'ellenőrző. '
         r'Azért van itt, mert ez a matematika egyik legszebb gondolata, és mert enélkül a '
         r'„bizonyítás” szó üresen csengene.</p>'
         r'<p>Olvasd el nyugodtan egyszer, végig. A természettudományi-matematikai szakon ebből '
         r'önálló, huszonöt órás témakör lesz.</p>', hid="erd-mire-jo"),
 ]),

 ("Sejtés néhány esetből: a hiányos indukció", [
   r'<p class="lead">Amikor néhány megfigyelt esetből általános szabályt mondunk ki, '
   r"<b>hiányos</b> (más néven nem teljes vagy empirikus) <b>indukciót</b> végzünk.</p>",
   doboz("definicio", "Hiányos indukció",
         r'<p><b>Hiányos indukció:</b> néhány konkrét esetből következtetünk egy általános '
         r'állításra. Ez a <b>felfedezés</b> módszere — nem a bizonyításé.</p>', hid="def-hianyos-indukcio"),
   r'<p>Ez nem csalás, hanem a kutatás természetes első lépése. Így vettük észre a '
   r'<a href="tananyag-szamtani-sorozat.html#tetel-szamtani-sn">korábbi egységekben</a> is a '
   r'képleteket — például azt, hogy a páratlan számok összege gyanúsan ismerős:</p>'
   r'$$1=1,\qquad 1+3=4,\qquad 1+3+5=9,\qquad 1+3+5+7=16 .$$'
   r'<p>A jobb oldalon rendre $1^2,\ 2^2,\ 3^2,\ 4^2$ áll. Kézenfekvő a <b>sejtés</b>: az első $n$ '
   r'páratlan szám összege $n^2$. A sejtés jó — de attól, hogy négy esetben igaz, még nem '
   r'tudjuk, hogy mindig igaz.</p>',
 ]),

 ("Amikor a sejtés elromlik", [
   r'<p>Két klasszikus példa arra, hogy a „sok eset” meddig nem bizonyíték.</p>',
   r'<p><b>1. Prímeket gyártó képlet?</b> Helyettesítsd be az $n=0,1,2,\dots$ értékeket az '
   r'$n^2+n+41$ kifejezésbe: $41,\ 43,\ 47,\ 53,\ 61,\ 71,\ 83,\dots$ — csupa prímszám. És így '
   r'megy tovább <b>negyven</b> eseten át, egészen $n=39$-ig. Aztán $n=40$-nél:</p>'
   r'$$40^2+40+41=1681=41^2 ,$$'
   r'<p>ami nem prím. Negyven jó eset — és a negyvenegyedik megdönti az egészet.</p>',
   r'<p><b>2. A kör tartományai.</b> Vegyél fel a körvonalon néhány pontot <b>általános '
   r'helyzetben</b> — vagyis úgy, hogy semelyik három húr ne menjen át ugyanazon a ponton (hat '
   r'pontnál tehát ne szabályos hatszöget rajzolj) —, és kösd össze mindegyiket mindegyikkel. '
   r'Hány részre osztják a húrok a körlapot?</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>pontok száma</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td><b>6</b></td></tr>'
   r'<tr><th>tartományok</th><td>1</td><td>2</td><td>4</td><td>8</td><td>16</td><td><b>31</b></td></tr>'
   r'</table></div>'
   r'<p>Az első öt adat alapján mindenki $32$-t mond — a valódi érték $31$. A kettőzés szabálya '
   r'öt eseten át tökéletesen működik, aztán vége.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi kiszámolja a láncreakció első három lépését, mindhárom a jóslata szerint alakul, '
         r'és bejelenti: „a képletem igaz 1-re, 2-re és 3-ra, tehát minden $n$-re igaz”.</p>'
         r'<p>Ez a <b>hiányos indukció</b> csapdája. Akárhány esetet ellenőrzünk, mindig marad '
         r'végtelen sok ellenőrizetlen — és a fenti két példa mutatja, hogy a törés bármikor '
         r'bekövetkezhet. Egyetlen ellenpélda viszont elég ahhoz, hogy az állítást <b>megdöntsük</b>: '
         r'cáfolni egy eset is tud, bizonyítani egy sem.</p>'),
   kviz(r'Egy állítást ellenőriztünk $n=1,2,\dots,1000$-re, és mindig igaz volt. Mit tudunk?',
        [r'csak annyit, hogy ezer esetben igaz — általánosan még nem bizonyított',
         r'bizonyítottuk, hiszen ezer eset épp elég',
         r'bizonyítottuk, ha az ezer eset között szerepel az $n=1$',
         r'az állítás biztosan hamis valahol, csak nem találtuk meg'], 0,
        jo="✔ A sok jó eset erős sejtés, de nem bizonyítás: az n² + n + 41 képlet negyven eseten át "
           "prímet ad, a negyvenediken mégsem.",
        nem="✘ Akárhány esetet nézünk végig, végtelen sok marad ellenőrizetlen. A sok jó eset "
            "sejtést ad, nem bizonyítást — és attól még az állítás lehet igaz is."),
 ]),

 ("A teljes indukció: a dominó-elv", [
   r'<p>Képzelj el egy végtelen hosszú dominósort. Mikor dől el <b>mindegyik</b>? Ha két dolgot '
   r'tudunk: az első eldől, és bármelyik dől el, magával rántja a következőt. Ebből a kettőből már '
   r'következik, hogy az egész sor eldől — anélkül, hogy egyenként megnéznénk.</p>',
   abra(SVG_DOMINO, 'A teljes indukció két feltétele: a <b>bázis</b> (az első dominó eldől) és a '
        '<b>lépés</b> (amelyik eldől, magával rántja a következőt).'),
   doboz("definicio", "A teljes (matematikai) indukció elve",
         r'<p>Ha egy $n$ természetes számról szóló állításra igaz, hogy</p>'
         r'<ol class="reszfeladatok">'
         r'<li><b>bázis:</b> igaz $n=1$-re, és</li>'
         r'<li><b>indukciós lépés:</b> valahányszor igaz egy $k$-ra, akkor igaz $k+1$-re is,</li>'
         r'</ol>'
         r'<p>akkor az állítás <b>minden</b> $n\ge1$ egész számra igaz.</p>'
         r'<p>A két feltétel elválaszthatatlan: a bázis indítja el a sort, a lépés pedig továbbviszi.</p>',
         hid="def-teljes-indukcio"),
   doboz("csapda", "Maxi trükkje — a hiányzó bázis",
         r'<p>Maxi „bebizonyítja”, hogy az első $n$ természetes szám összege '
         r'$\frac{n(n+1)}{2}+5$. A lépést valóban hibátlanul végzi el: ha a $k$-ra igaz lenne, akkor</p>'
         r'$$\frac{k(k+1)}{2}+5+(k+1)=\frac{(k+1)(k+2)}{2}+5 ,$$'
         r'<p>vagyis a képlet öröklődne $k+1$-re. Csakhogy a <b>bázis hamis</b>: $n=1$-re a bal oldal '
         r'$1$, a képlet szerint viszont $6$ lenne.</p>'
         r'<p>A dominósor tehát tökéletesen fel van állítva — csak épp senki nem lökte meg. '
         r'<b>Bázis nélkül a lépés hamis állítást is továbbvisz.</b> Fordítva ugyanígy: pusztán a '
         r'bázisból (néhány jó esetből) sem következik semmi — az az előző szakasz csapdája volt.</p>'),
   kviz(r'Egy állításnál az indukciós lépés hibátlan, de $n=1$-re az állítás hamis. Mit mondhatunk?',
        [r'az állítás nincs bizonyítva — a bázis nélkül a lépés önmagában semmit nem igazol',
         r'az állítás bizonyított, hiszen a lépés a lényeg',
         r'az állítás minden $n\ge2$-re igaz',
         r'a lépés biztosan hibás, csak nem vettük észre'], 0,
        jo="✔ A két feltétel együtt ad bizonyítást: a bázis indítja el a dominósort, a lépés viszi "
           "tovább. Meglökés nélkül egyik dominó sem dől el.",
        nem="✘ A lépés csak azt mondja: HA igaz k-ra, AKKOR igaz k + 1-re. Ha soha nem igaz "
            "egyetlen konkrét számra sem, ebből nem következik semmi — épp ez a +5-ös álképlet esete."),
 ]),

 ("Egy teljes bizonyítás, lépésről lépésre", [
   doboz("pelda", "Az első n páratlan szám összege",
         r'<p><b>Állítás:</b> minden $n\ge1$ egész számra</p>'
         r'$$1+3+5+\dots+(2n-1)=n^2 .$$'
         r'<p><b>Bázis ($n=1$).</b> A bal oldal az első páratlan szám, azaz $1$; a jobb oldal '
         r'$1^2=1$. Igaz. ✔</p>'
         r'<p><b>Indukciós lépés.</b> Tegyük fel, hogy valamely $k$-ra igaz:</p>'
         r'$$1+3+\dots+(2k-1)=k^2 .$$'
         r'<p>Adjuk hozzá mindkét oldalhoz a következő páratlan számot, $2(k+1)-1=2k+1$-et:</p>'
         r'$$1+3+\dots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2 .$$'
         r'<p>Ez pontosan az állítás $k+1$-re. ✔</p>'
         r'<p>A két lépésből következik, hogy az állítás <b>minden</b> $n\ge1$ egész számra '
         r'igaz. ∎</p>',
         hid="pelda-paratlan-osszeg"),
   doboz("erdekesseg", "Nem csak képletekre jó",
         r'<p>Ugyanez a két lépés működik <b>oszthatóságnál</b> is. Állítás: $n^3-n$ minden $n$-re '
         r'osztható $6$-tal. A bázis: $1^3-1=0$, ami osztható. A lépés: ha $k^3-k$ osztható $6$-tal, '
         r'akkor</p>'
         r'$$(k+1)^3-(k+1)=(k^3-k)+3k(k+1) ,$$'
         r'<p>és itt az első tag a feltevés szerint osztható $6$-tal, a $3k(k+1)$ pedig azért, mert '
         r'$k$ és $k+1$ közül az egyik páros. Így az összeg is osztható $6$-tal. ∎</p>'),
   r'<p>Figyeld meg a lépés szerkezetét: a feltevést (a $k$-ra vonatkozó egyenlőséget) '
   r'<b>felhasználjuk</b>, nem bizonyítjuk — a bizonyítandó a $k+1$-re szóló állítás. Ezért '
   r'nevezzük a feltevést <i>indukciós feltevésnek</i>.</p>',
   r'<p>És innen nézve derül ki, mire volt jó az egész: a '
   r'<a href="tananyag-szamtani-sorozat.html#tetel-szamtani-sn">számtani sorozat összegképletét</a> '
   r'és a <a href="tananyag-mertani-sorozat.html#tetel-mertani-sn">mértani sorozat összegképletét</a> '
   r'ugyanígy lehet igazolni. Eddig úgy használtuk őket, hogy egy ügyes trükkel megkaptuk; az '
   r'indukció az, ami <b>garantálja</b>, hogy nemcsak az első néhány, hanem minden $n$-re '
   r'érvényesek.</p>',
   brief('<b>Kanrak:</b> A láncreakció képletét felírtuk, a bizonyítás áll — és ez az, amit Maxi nem '
         'tudott kivédeni. Nem lépésről lépésre fogtuk meg, hanem egyszerre az összesre: az '
         '$n$-edik lépésnél pontosan tudjuk, hol tart, tehát tudjuk, hol kell megállítani. '
         '<b>A Kristálypára-anomália lezárva.</b><br>'
         'Prizma: a zóna stabil, a Királyi Család visszavonul. A következő évadban már nem a tér '
         'görbül — hanem a változás sebessége lesz a tét. Addig is: a '
         '<a href="osszefoglalo.html">Taktikai memóriakártya</a> mindent egy lapon tart.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lap
KI = [
 lap(**T, fajl="tananyag-indukcio.html",
     cim="Hiányos és teljes indukció",
     alcim="Mikor sejtés és mikor bizonyítás: a hiányos indukció csapdái, a teljes indukció "
           "dominó-elve, és egy végigvezetett bizonyítás. Számonkérés nincs belőle.",
     chip=KUL + " · 5/5", szakaszok=C,
     elozo=("feladatok-hazi.html", "Kristály-kamra — Vészterem"),
     kovetkezo=("osszefoglalo.html", "Taktikai memóriakártya")),
]
for u in KI:
    print("✓", os.path.basename(u))
