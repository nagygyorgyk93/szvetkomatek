# -*- coding: utf-8 -*-
"""Vészterem — témakörönként EGY, teljes témakört lefedő házi feladatsor.
FONTOS: a Végeredmény KIZÁRÓLAG a végső választ tartalmazza, levezetés/indoklás NÉLKÜL."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, w

def dr_page(dest, topic_link, topic_name, fname, title, alcim, brief, sections, prev, prevc, nxt, nxtc, help_html):
    html = f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | 1e | Szvetkó matek</title>
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
  <a href="{topic_link}">{topic_name}</a> ›
  <span class="itt">Vészterem — házi</span>
</nav>
<div class="hero">
  <h1>{title}</h1>
  <p class="alcim">{w(alcim)}</p>
  <div class="meta-sor">
    <span class="chip alap">Alap</span><span class="chip kozep">Közép</span><span class="chip nehez">Nehéz</span>
  </div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
    <div class="brief"><p>{brief}</p></div>
{sections}
    <div class="gyakorolj">
      <span class="ikon">📖</span>
      <p>{help_html}</p>
    </div>
    <div class="lapozo">
      <a class="elozo" href="{prev}"><span class="irany">← Előző</span><span class="hova">{prevc}</span></a>
      <a class="kov" href="{nxt}"><span class="irany">Következő →</span><span class="hova">{nxtc}</span></a>
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
    open(os.path.join(dest, fname), "w", encoding="utf-8").write(html)
    return fname

def sect(alap, kozep, nehez):
    return (f'    <h2 id="alap">🟢 Alapszint</h2>\n{cards(alap,"alap","alap")}\n'
            f'    <h2 id="kozep">🟡 Középszint</h2>\n{cards(kozep,"kozep","kozep")}\n'
            f'    <h2 id="nehez">🔴 Nehéz (emelt)</h2>\n{cards(nehez,"nehez","nehez")}\n')


# ==================================================================
# STK2 / reprezentáció-váltó pótlások (2026-08 audit)
# A didaktika 4. pontja: STK1 fölötti feladat az ALAP és a KÖZÉP sávban is
# kell; a 7. pont témakörönként legalább egy reprezentáció-váltó kérést kér.
# ==================================================================
# --- 01 Logika, halmazok, függvények ---
A01_UJ = [
 ("Döntsd el, igaz vagy hamis, és <b>minden állításnál indokold egy mondattal</b>!",
  ["Ha egy implikáció igaz, akkor a megfordítása is igaz.",
   "Két halmaz metszete mindig részhalmaza az uniójuknak.",
   "Ha $A\\subseteq B$ és $B\\subseteq A$, akkor $A=B$."],
  ["Hamis. Például „ha esik, akkor vizes az út” igaz lehet, de a megfordítása nem — "
   "az út mástól is lehet vizes.",
   "Igaz. A metszet minden eleme mindkét halmazban benne van, tehát az unióban is.",
   "Igaz — pontosan ez a halmazok egyenlőségének a definíciója."]),
]
K01_UJ = [
 ("Egy függvény néhány helyettesítési értéke:"
  "<div class=\"tblwrap\"><table><thead><tr><th>$x$</th><td>$1$</td><td>$2$</td><td>$3$</td>"
  "<td>$4$</td></tr></thead><tbody><tr><th>$f(x)$</th><td>$5$</td><td>$8$</td><td>$11$</td>"
  "<td>$14$</td></tr></tbody></table></div>",
  ["Lehet-e $f$ lineáris? Honnan látod a <b>táblázatból</b>?",
   "Ha igen, add meg a hozzárendelési szabályt.",
   "Írj olyan négyelemű táblázatot, amelyik <b>biztosan nem</b> lehet lineáris függvényé, "
   "és indokold, miért nem."],
  ["Lehet: az $x$ egyesével nő, és az $f(x)$ mindig ugyanannyival, $3$-mal — állandó "
   "növekedés, ez a lineáris függvény ismertetőjegye.",
   "$f(x)=3x+2$.",
   "Például $1,2,3,4\\mapsto 1,4,9,16$: itt a különbségek $3,5,7$ — nem állandók, "
   "tehát a hozzárendelés nem lineáris."]),
]

# --- 02 Trigonometria ---
A02_UJ = [
 ("Egy kadét ezt írta a füzetébe: <i>„$\\sin\\alpha$ a szemközti befogó és a szomszédos "
  "befogó hányadosa.”</i> Melyik szögfüggvény definícióját keverte ide, és hogyan hangzik "
  "helyesen a szinuszé?",
  None,
  "A tangensét keverte oda: $\\operatorname{tg}\\alpha=\\dfrac{\\text{szemközti befogó}}"
  "{\\text{szomszédos befogó}}$. A szinusz helyesen: $\\sin\\alpha="
  "\\dfrac{\\text{szemközti befogó}}{\\text{átfogó}}$."),
]
K02_UJ = [
 ("Egy derékszögű háromszögről csak annyit tudsz, hogy $\\operatorname{tg}\\alpha=\\tfrac{5}{12}$.",
  ["Milyen oldalhosszakkal rajzolhatsz ilyen háromszöget? Add meg mindhárom oldalt!",
   "Olvasd le a rajzodról $\\sin\\alpha$-t és $\\cos\\alpha$-t <b>pontosan</b>.",
   "Változna-e a három szögfüggvény értéke, ha minden oldalt megkétszereznél? Indokold!"],
  ["Például $a=5$, $b=12$, és ekkor $c=\\sqrt{25+144}=13$.",
   "$\\sin\\alpha=\\tfrac{5}{13}$, $\\cos\\alpha=\\tfrac{12}{13}$.",
   "Nem változna: a szögfüggvények <b>arányok</b>, a hasonló háromszögekben pedig az "
   "oldalak aránya ugyanaz."]),
]

# --- 03 Egész és valós számok ---
A03_UJ = [
 ("Döntsd el, igaz vagy hamis, és <b>ha hamis, adj ellenpéldát</b>!",
  ["Minden racionális szám felírható véges tizedes tört alakban.",
   "Minden végtelen tizedes tört irracionális.",
   "Két irracionális szám összege mindig irracionális.",
   "$\\sqrt{9}$ irracionális."],
  ["Hamis: $\\tfrac13=0{,}333\\ldots$ végtelen.",
   "Hamis: $0{,}333\\ldots=\\tfrac13$ végtelen, mégis racionális — a szakaszos "
   "végtelen tizedes törtek racionálisak.",
   "Hamis: $\\sqrt2+(-\\sqrt2)=0$.",
   "Hamis: $\\sqrt9=3$, ami egész szám."]),
]
K03_UJ = [
 ("Egy mérőműszer $3{,}47$-et mutat, és a leírás szerint a mérés hibája legfeljebb $0{,}02$.",
  ["Mely valós számok jöhetnek szóba valódi értékként? Add meg intervallummal!",
   "Elmondható-e biztosan, hogy a valódi érték nagyobb $3{,}4$-nél? És hogy nagyobb $3{,}46$-nál?",
   "A műszer leolvasását $3{,}5$-re kerekítjük. Mekkora lesz így a legnagyobb lehetséges eltérés "
   "a valódi értéktől?"],
  ["$[3{,}45;\\ 3{,}49]$.",
   "$3{,}4$-nél biztosan nagyobb, mert a legkisebb lehetséges érték $3{,}45$. "
   "$3{,}46$-nál viszont nem biztos: a valódi érték lehet $3{,}45$ is.",
   "A legtávolabbi lehetséges valódi érték $3{,}45$, tehát az eltérés legfeljebb $0{,}05$."]),
]

# --- 04 Arányosság ---
A04_UJ = [
 ("Egy bolt februárban $20\\%$-kal <b>megemeli</b> egy termék árát, majd márciusban ugyanennek a "
  "terméknek az árát $20\\%$-kal <b>csökkenti</b>.",
  ["Visszakapjuk-e az eredeti árat? Számolj $2000$ dináros kiinduló árral!",
   "Miért nem esik egybe a két $20\\%$? Fogalmazd meg egy mondatban!",
   "Hány százalékkal kellene márciusban csökkenteni, hogy pontosan az eredeti árat kapjuk vissza? "
   "(Kerekíts egy tizedesre.)"],
  ["Nem: $2000\\to 2400\\to 1920$ dinár, tehát $80$ dinárral olcsóbb lett.",
   "Mert a két százalékot <b>különböző alapra</b> számoljuk: az emelést az eredeti árra, "
   "a csökkentést a már megemelt árra.",
   "$2400\\cdot x=2000$, ahonnan a szorzó $0{,}8\\overline{3}$, tehát kb. $16{,}7\\%$-kal."]),
]
K04_UJ = [
 ("Két táblázat, két különböző kapcsolat:"
  "<div class=\"tblwrap\"><table><thead><tr><th>$x$</th><td>$2$</td><td>$4$</td><td>$6$</td>"
  "<td>$12$</td></tr></thead><tbody><tr><th>$A$</th><td>$5$</td><td>$10$</td><td>$15$</td>"
  "<td>$30$</td></tr><tr><th>$B$</th><td>$30$</td><td>$15$</td><td>$10$</td><td>$5$</td>"
  "</tr></tbody></table></div>",
  ["Melyik sor mutat egyenes, és melyik fordított arányosságot? Mi árulja el?",
   "Írd fel mindkettőhöz a szabályt képlettel.",
   "Mennyi lenne $A$ és $B$ értéke $x=3$-nál?"],
  ["Az $A$ egyenes arányosság: az $A/x$ hányados végig $2{,}5$. A $B$ fordított: "
   "az $x\\cdot B$ szorzat végig $60$.",
   "$A=2{,}5x$, illetve $B=\\dfrac{60}{x}$.",
   "$A=7{,}5$ és $B=20$."]),
]

# --- 05 Geometria ---
A05_UJ = [
 ("Döntsd el, igaz vagy hamis, és <b>ha hamis, adj ellenpéldát</b> (elég leírni, milyen alakzat)!",
  ["Ha egy négyszög átlói merőlegesek egymásra, akkor rombusz.",
   "Minden négyzet rombusz.",
   "Ha egy háromszögnek két szöge egyenlő, akkor egyenlő szárú.",
   "Van olyan háromszög, amelynek két tompaszöge van."],
  ["Hamis: a deltoid átlói is merőlegesek, mégsem rombusz.",
   "Igaz: a négyzet minden oldala egyenlő, ez pedig a rombusz definíciója.",
   "Igaz — ez az egyenlő szárú háromszög alaptételének a megfordítása.",
   "Hamis: két tompaszög összege már meghaladná a $180^\\circ$-ot."]),
]

# --- 06 Racionális algebrai kifejezések ---
A06_UJ = [
 ("Az alábbi „levezetésekben” egy-egy tipikus hiba van. Keresd meg, hol csúszik el, és "
  "javítsd ki!",
  ["$(a+b)^2=a^2+b^2$",
   "$\\dfrac{a+b}{a}=b$",
   "$\\dfrac{x^2-4}{x-2}=x-2$"],
  ["Hiányzik a kétszeres szorzat: $(a+b)^2=a^2+2ab+b^2$. Az $a=b=1$ eset azonnal cáfol: "
   "$4\\neq 2$.",
   "Összegből nem lehet „kiegyszerűsíteni” egy tagot: $\\dfrac{a+b}{a}=1+\\dfrac{b}{a}$.",
   "A számláló $ (x-2)(x+2)$, ezért az eredmény $x+2$ — és ki kell kötni, hogy $x\\neq 2$."]),
]
K06_UJ = [
 ("Adott a $\\dfrac{x^2-9}{x^2-5x+6}$ kifejezés.",
  ["Mely $x$ értékekre nincs értelmezve? Miért éppen azokra?",
   "Egyszerűsítsd a kifejezést!",
   "Az egyszerűsítés után a $x=3$ behelyettesíthetőnek <b>látszik</b>. Behelyettesíthető-e "
   "valójában? Indokold!"],
  ["A nevező $x^2-5x+6=(x-2)(x-3)$, tehát $x\\neq 2$ és $x\\neq 3$ — nullával nem osztunk.",
   "$\\dfrac{(x-3)(x+3)}{(x-2)(x-3)}=\\dfrac{x+3}{x-2}$.",
   "Nem. Az értelmezési tartományt az <b>eredeti</b> kifejezés szabja meg, és azt az "
   "egyszerűsítés nem bővíti ki. $x=3$-nál az eredeti kifejezésnek nincs értéke."]),
]

# --- 07 Lineáris egyenletek, egyenlőtlenségek, rendszerek ---
A07_UJ = [
 ("Egy kadét így oldotta meg a $3x=6x$ egyenletet: <i>„Elosztom mindkét oldalt $x$-szel, "
  "így $3=6$, ami lehetetlen — tehát az egyenletnek nincs megoldása.”</i>",
  ["Hol a hiba a gondolatmenetben?",
   "Oldd meg helyesen az egyenletet!",
   "Milyen szabályt érdemes megjegyezni ebből?"],
  ["Ismeretlennel osztott, holott az $x$ lehet $0$ is — nullával pedig nem szabad osztani. "
   "Ezzel épp az egyetlen megoldást veszítette el.",
   "$3x=6x \\Rightarrow 3x-6x=0 \\Rightarrow -3x=0 \\Rightarrow x=0$.",
   "Egyenletet ismeretlent tartalmazó kifejezéssel osztani csak akkor szabad, ha külön "
   "megvizsgáljuk azt az esetet is, amikor az a kifejezés nulla. Rendezés és szorzattá "
   "alakítás helyette mindig biztonságos."]),
]
K07_UJ = [
 ("Egy egyenletrendszer két egyenlete egy-egy egyenest ad a koordináta-rendszerben. "
  "Az egyenesekről csak ennyit tudsz:",
  ["Az első meredeksége $2$, a másodiké $-1$. Hány megoldása van a rendszernek? Miért?",
   "Mindkettő meredeksége $2$, de a tengelymetszetük különböző. Hány megoldás van?",
   "Mindkettő meredeksége $2$, és a tengelymetszetük is ugyanaz. Hány megoldás van?"],
  ["Pontosan egy: különböző meredekségű egyenesek egyetlen pontban metszik egymást.",
   "Egy sem: párhuzamosak, de nem esnek egybe — nincs közös pontjuk.",
   "Végtelen sok: a két egyenes egybeesik, minden pontja közös megoldás."]),
]


# =========================================================== 01
DEST01 = glob.glob("/sessions/*/mnt/Claude/web/1e/01-logika-halmazok-fuggvenyek")[0]

A01 = [
 ("Döntsd el, melyik <b>kijelentés</b>, és ha az, mi az igazságértéke!",
  ["„A 7 prímszám.”","„$x+2=5$.”","„Minden négyzet téglalap.”","„Hány óra van?”","„A 12 osztható 5-tel.”"],
  "a) kijelentés, igaz; b) nem kijelentés; c) kijelentés, igaz; d) nem kijelentés; e) kijelentés, hamis.", True),
 ("Legyen $p$ igaz, $q$ hamis. Add meg az alábbiak igazságértékét!",
  ["$\\neg p$","$p\\land q$","$p\\lor q$","$p\\Rightarrow q$","$q\\Rightarrow p$","$p\\Leftrightarrow q$"],
  "a) hamis; b) hamis; c) igaz; d) hamis; e) igaz; f) hamis.", True),
 ("Írd fel a <b>tagadását</b>!",
  ["„Minden diák szereti a matekot.”","„Van olyan szám, amely páros.”","„$x>3$.”"],
  ["„Van olyan diák, aki nem szereti a matekot.”","„Egyetlen szám sem páros.”","$x\\le 3$."]),
 ("Legyen $A=\\{1,2,3,4,5\\}$, $B=\\{2,4,6,8\\}$. Add meg:",
  ["$A\\cup B$","$A\\cap B$","$A\\setminus B$","$B\\setminus A$"],
  ["$\\{1,2,3,4,5,6,8\\}$","$\\{2,4\\}$","$\\{1,3,5\\}$","$\\{6,8\\}$"], True),
 ("Az alaphalmaz $U=\\{1,2,\\dots,10\\}$, és $A=\\{2,3,5,7\\}$. Add meg $A$ komplementerét ($A^{c}$) és elemszámát, $|A|$-t!",
  None, "$A^{c}=\\{1,4,6,8,9,10\\}$; $|A|=4$."),
 ("Sorold fel a $\\{a,b,c\\}$ halmaz <b>összes részhalmazát</b>! Hány van?",
  None, "$\\varnothing,\\ \\{a\\},\\{b\\},\\{c\\},\\ \\{a,b\\},\\{a,c\\},\\{b,c\\},\\ \\{a,b,c\\}$; összesen $8$."),
 ("<b>Menü.</b> Egy étterem 3-féle levest és 4-féle főételt kínál. Hányféle (leves + főétel) menü állítható össze? (szorzási szabály)",
  None, "$12$ menü."),
 ("<b>Nyelvórák.</b> Egy 30 fős osztályban 18-an tanulnak angolt, 12-en németet, 5-en mindkettőt. Rajzolj Venn-diagramot, és számold ki: hányan tanulnak legalább egy nyelvet, és hányan egyet sem?",
  None, "Legalább egy: $25$; egyik sem: $5$."),
 ("$f(x)=3x-4$. Számítsd ki:",
  ["$f(0)$","$f(2)$","$f(-1)$","$f\\!\\left(\\tfrac13\\right)$"],
  "a) $-4$; b) $2$; c) $-7$; d) $-3$.", True),
 ("Az $A=\\{1,2,3,4\\}$ halmazon $f=\\{(1,3),(2,5),(3,3),(4,7)\\}$. Add meg az értelmezési tartományt ($D_f$) és az értékkészletet ($R_f$)! Injektív-e?",
  None, "$D_f=\\{1,2,3,4\\}$, $R_f=\\{3,5,7\\}$; nem injektív."),
 ("$f(x)=2x+1$, $g(x)=x-3$. Határozd meg a kompozíciókat!",
  ["$(f\\circ g)(x)$","$(g\\circ f)(x)$"],
  ["$2x-5$","$2x-2$"]),
]
A01 = A01 + A01_UJ
K01 = [
 ("Igazságtáblázattal döntsd el, <b>tautológia-e</b>: $(p\\land q)\\Rightarrow p$.",
  None, "Igen, tautológia."),
 ("Írd fel kvantoros alakban, majd <b>tagadd</b> (és döntsd el, igaz-e az eredeti)!",
  ["„Minden valós $x$-re $x^2\\ge 0$.”","„Van olyan természetes szám, amely osztható 3-mal.”"],
  ["$\\forall x\\in\\mathbb{R}\\,(x^2\\ge 0)$ — igaz; tagadása $\\exists x\\in\\mathbb{R}\\,(x^2<0)$.",
   "$\\exists x\\in\\mathbb{N}\\,(3\\mid x)$ — igaz; tagadása $\\forall x\\in\\mathbb{N}\\,(3\\nmid x)$."]),
 ("Adott $A=\\{x\\in\\mathbb{Z}\\mid -2\\le x<3\\}$ és $B=\\{x\\in\\mathbb{Z}\\mid 0&lt;x\\le 5\\}$. Sorold fel a halmazokat, majd add meg $A\\cup B$-t, $A\\cap B$-t és $A\\setminus B$-t!",
  None, "$A=\\{-2,-1,0,1,2\\}$, $B=\\{1,2,3,4,5\\}$; $A\\cup B=\\{-2,-1,0,1,2,3,4,5\\}$, $A\\cap B=\\{1,2\\}$, $A\\setminus B=\\{-2,-1,0\\}$."),
 ("<b>De Morgan.</b> $U=\\{1,2,\\dots,8\\}$, $A=\\{1,2,3,4\\}$, $B=\\{3,4,5,6\\}$. Számold ki mindkét oldalt, és ellenőrizd: $(A\\cup B)^{c}=A^{c}\\cap B^{c}$.",
  None, "$(A\\cup B)^{c}=\\{7,8\\}$ és $A^{c}\\cap B^{c}=\\{7,8\\}$ — egyenlők."),
 ("$f(x)=2x-6$. Add meg az <b>inverzét</b>, $f^{-1}(x)$-et, és számítsd ki $f^{-1}(4)$-et!",
  None, "$f^{-1}(x)=\\dfrac{x+6}{2}$; $f^{-1}(4)=5$."),
 ("Az $f(x)=ax+b$ lineáris függvényről tudjuk: $f(1)=5$ és $f(3)=11$. Határozd meg $a$-t, $b$-t, majd írd fel $f(x)$-et!",
  None, "$a=3$, $b=2$; $f(x)=3x+2$."),
 ("<b>Jelszó.</b> Egy kód 2 betűből (az $A,B,C,D$ közül) és 2 számjegyből ($0$–$9$) áll, az ismétlés megengedett. Hány különböző kód lehetséges?",
  None, "$1600$."),
]
K01 = K01 + K01_UJ
N01 = [
 ("<b>Sziget-akták.</b> A lovag mindig igazat mond, a lókötő mindig hazudik. $A$ azt mondja: „$B$ lókötő.”, $B$ azt mondja: „$A$ és én azonos típusúak vagyunk.” Ki micsoda? Indokolj!",
  None, "$A$ lovag, $B$ lókötő."),
 ("<b>Fordított szita.</b> Egy 40 fős csoportban 25-en sportolnak ($S$), 20-an zenélnek ($Z$), 8-an egyiket sem. Rajzolj Venn-diagramot, és számold ki, hányan csinálják <b>mindkettőt</b>!",
  None, "Mindkettőt: $13$."),
 ("$f(x)=2x+1$, $g(x)=x^2$. Add meg $(f\\circ g)(x)$-et és $(g\\circ f)(x)$-et — egyenlők-e? Számítsd ki mindkettőt $x=3$-ra!",
  None, "$(f\\circ g)(x)=2x^2+1$, $(g\\circ f)(x)=4x^2+4x+1$; nem egyenlők. $(f\\circ g)(3)=19$, $(g\\circ f)(3)=49$."),
]
brief01 = ("🕹️ <b>SZVETI:</b> Üdv a <b>Vészteremben</b>, kadét! Ez a <b>Vészterem</b> — a kampusz "
 "szimulációs edzőterme (a technológiát az X. Károly Intézet Mutáns Osztagától licenceltük). Itt otthon, a saját "
 "tempódban gyakorolsz két küldetés között. A szimuláció a <b>teljes témakört</b> lefedi: logika, halmazok, "
 "függvények. Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden "
 "feladatnál lenyithatod — de előbb küzdd le magad!")
dr_page(DEST01, "index.html", "Logika, halmazok, függvények", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: logika, halmazok és függvények. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief01, sect(A01, K01, N01),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("01 Vészterem kész: Alap", len(A01), "Közép", len(K01), "Nehéz", len(N01))

# =========================================================== 02
DEST02 = glob.glob("/sessions/*/mnt/Claude/web/1e/02-trigonometria")[0]
A02 = [
 ("Egy derékszögű háromszögben a befogók $a=6$, $b=8$, az átfogó $c=10$. Írd fel az $a$-val szemközti $\\alpha$ hegyesszög mind a négy szögfüggvényét!",
  None, "$\\sin\\alpha=\\tfrac35$, $\\cos\\alpha=\\tfrac45$, $\\operatorname{tg}\\alpha=\\tfrac34$, $\\operatorname{ctg}\\alpha=\\tfrac43$."),
 ("Add meg <b>fejből, pontosan</b>!",
  ["$\\sin 30^\\circ$","$\\cos 30^\\circ$","$\\operatorname{tg}45^\\circ$","$\\sin 60^\\circ$","$\\cos 45^\\circ$","$\\operatorname{tg}30^\\circ$"],
  "a) $\\tfrac12$; b) $\\tfrac{\\sqrt3}{2}$; c) $1$; d) $\\tfrac{\\sqrt3}{2}$; e) $\\tfrac{\\sqrt2}{2}$; f) $\\tfrac{\\sqrt3}{3}$.", True),
 ("Számológéppel, <b>öt tizedesre</b> (DEG mód)!",
  ["$\\sin 37^\\circ$","$\\cos 52^\\circ$","$\\operatorname{tg}19^\\circ$","$\\operatorname{ctg}64^\\circ$"],
  "a) $0{,}60182$; b) $0{,}61566$; c) $0{,}34433$; d) $0{,}48773$.", True),
 ("Számítsd ki <b>pontosan</b> (nevezetes szögek)!",
  ["$\\sin 30^\\circ+\\cos 60^\\circ$","$\\operatorname{tg}45^\\circ\\cdot\\cos 45^\\circ$"],
  ["$1$","$\\tfrac{\\sqrt2}{2}$"]),
]
A02 = A02 + A02_UJ
K02 = [
 ("Egy $\\alpha$ hegyesszögre $\\sin\\alpha=0{,}6$. Számítsd ki <b>pontosan</b> $\\cos\\alpha$-t, $\\operatorname{tg}\\alpha$-t és $\\operatorname{ctg}\\alpha$-t!",
  None, "$\\cos\\alpha=\\tfrac45$, $\\operatorname{tg}\\alpha=\\tfrac34$, $\\operatorname{ctg}\\alpha=\\tfrac43$."),
 ("Oldd meg a derékszögű háromszöget: az átfogó $c=12\\,\\text{cm}$, az egyik hegyesszög $\\alpha=35^\\circ$ (az $a$-val szemközti). Számítsd ki a másik hegyesszöget és a két befogót (2 tizedesre)!",
  None, "$\\beta=55^\\circ$; $a\\approx 6{,}88\\,\\text{cm}$; $b\\approx 9{,}83\\,\\text{cm}$."),
 ("Számold ki <b>számológép nélkül</b> (pótszög + alapazonosság)!",
  ["$\\sin^2 25^\\circ+\\cos^2 25^\\circ$","$\\sin 40^\\circ-\\cos 50^\\circ$"],
  ["$1$","$0$"]),
]
K02 = K02 + K02_UJ
N02 = [
 ("<b>Terep-alkalmazás.</b> Egy fa árnyéka $12\\,\\text{m}$ hosszú, amikor a napsugarak $40^\\circ$-os emelkedési szöget zárnak be a vízszintessel. Milyen magas a fa? Rajzolj, és számolj 2 tizedesre!",
  None, "$m\\approx 10{,}07\\,\\text{m}$."),
]
brief02 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, célzó modul. Ez a <b>Vészterem</b> otthoni "
 "edzésváltozata — itt gyakorolsz a terepküldetés előtt és után. A szimuláció a <b>teljes trigonometria-témakört</b> "
 "lefedi: szögfüggvények, nevezetes szögek, a derékszögű háromszög megoldása és valós mérések. Tartsd a "
 "<b>kerekítési szabályt</b> (szögfüggvény-érték 5 tizedes, hossz és szög 2 tizedes). Fokozatok: zöld → sárga → piros.")
dr_page(DEST02, "index.html", "Trigonometria", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes trigonometria-témakört lefedő házi feladatsor. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief02, sect(A02, K02, N02),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("02 Vészterem kész: Alap", len(A02), "Közép", len(K02), "Nehéz", len(N02))

# =========================================================== 03
from math import gcd as _gcd
def _lcm(a,b): return a*b//_gcd(a,b)
def _tob(n,b):
    if n==0: return "0"
    d=""
    while n: d="0123456789ABCDEF"[n%b]+d; n//=b
    return d
assert 84==2**2*3*7 and 250==2*5**3 and _gcd(84,250)==2
assert [n for n in [1080,2358,4526,7200] if n%4==0]==[1080,7200]
assert [n for n in [1080,2358,4526,7200] if n%9==0]==[1080,2358,7200]
assert int("231",4)==45 and int("10110",2)==22 and _tob(50,2)=="110010" and _tob(200,8)=="310"
assert _lcm(_lcm(8,12),20)==120
assert [x for x in range(10) if (470+x)%3==0]==[1,4,7]
assert [x for x in range(10) if (5800+x*10)%8==0]==[0,4,8]
assert 600==2**3*3*5**2 and 600*45==30**3 and round(7.64983,2)==7.65
DEST03 = glob.glob("/sessions/*/mnt/Claude/web/1e/03-egesz-es-valos-szamok")[0]
A03 = [
 ("Írd fel a $84$ és $250$ kanonikus (prímtényezős) alakját, majd add meg $\\text{LKO}(84,250)$-et!",
  None, "$84=2^2\\cdot 3\\cdot 7$, $250=2\\cdot 5^3$; $\\text{LKO}=2$."),
 ("A megadott számok közül melyek oszthatók? $1080,\\ 2358,\\ 4526,\\ 7200$.",
  ["$4$-gyel","$9$-cel"], ["$1080,\\ 7200$","$1080,\\ 2358,\\ 7200$"]),
 ("Számrendszer-váltás.",
  ["$231_4$ tízesbe","$10110_2$ tízesbe","$50$ kettesbe","$200$ nyolcasba"],
  ["$45$","$22$","$110010_2$","$310_8$"]),
 ("Sorold be mindegyik számot a legszűkebb számhalmazba ($\\mathbb{N},\\mathbb{Z},\\mathbb{Q},\\mathbb{R}$)!",
  ["$-7$","$\\tfrac{5}{2}$","$\\sqrt{49}$","$\\sqrt{3}$","$0{,}2$","$\\sqrt{10}$"],
  "$-7\\in\\mathbb{Z}$; $\\tfrac52\\in\\mathbb{Q}$; $\\sqrt{49}=7\\in\\mathbb{N}$; $\\sqrt3\\in\\mathbb{R}$; $0{,}2\\in\\mathbb{Q}$; $\\sqrt{10}\\in\\mathbb{R}$.", True),
 ("Töltsd ki a hiányzó alakokat!",
  ["$\\tfrac14$ tizedes törtként és százalékként","$0{,}45$ törtként és százalékként","$30\\%$ törtként és tizedes törtként"],
  ["$0{,}25$; $25\\%$","$\\tfrac{9}{20}$; $45\\%$","$\\tfrac{3}{10}$; $0{,}3$"]),
 ("Oldd meg, illetve írd fel normál alakban!",
  ["$|x|=15$","$|x-2|=6$","$73\\,000\\,000$","$0{,}0004$"],
  ["$x=\\pm 15$","$x=8$ vagy $x=-4$","$7{,}3\\cdot 10^{7}$","$4\\cdot 10^{-4}$"]),
]
A03 = A03 + A03_UJ
K03 = [
 ("Három jelzőfény $8$, $12$ és $20$ másodpercenként villan; most együtt villantak. Hány másodperc múlva villannak legközelebb megint mind együtt? (Prímtényezős alak, majd LKT.)",
  None, "$\\text{LKT}(8,12,20)=120$ másodperc."),
 ("Határozd meg a hiányzó számjegyet — add meg az összes megoldást!",
  ["$\\overline{47x}$ osztható $3$-mal","$\\overline{58x0}$ osztható $8$-cal"],
  ["$x\\in\\{1,4,7\\}$","$x\\in\\{0,4,8\\}$"]),
 ("Az $x=7{,}64983$ értéket kerekítsd 2 tizedesre, add meg az abszolút hibát; majd számold ki normál alakban: $(4\\cdot 10^{6})\\cdot(2{,}5\\cdot 10^{-3})$.",
  None, "$x^{*}=7{,}65$; $\\Delta=0{,}00017$; a szorzat $1\\cdot 10^{4}$."),
]
K03 = K03 + K03_UJ
N03 = [
 ("Bizonyítsd be, hogy $n^3-n$ osztható $6$-tal minden egész $n$-re!",
  None, "$n^3-n=(n-1)\\,n\\,(n+1)$ — három egymást követő egész szorzata, ezért osztható $6$-tal."),
 ("Melyik a legkisebb pozitív egész szám, amivel a $600$-at szorozva köbszámot kapunk? (Kanonikus alak.)",
  None, "$45$."),
]
brief03 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, kódtörő + kalibráló modul. Ez a <b>Vészterem</b> "
 "otthoni edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: "
 "számelmélet és számrendszerek (Iruhs szektora), valamint a valós számok, a közelítés és a normál alak (Banner "
 "szektora). Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál "
 "lenyithatod — de előbb küzdd le magad!")
dr_page(DEST03, "index.html", "Egész és valós számok", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: számelmélet, számrendszerek, számhalmazok, közelítés. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief03, sect(A03, K03, N03),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("03 Vészterem kész: Alap", len(A03), "Közép", len(K03), "Nehéz", len(N03))

# =========================================================== 04
assert 8*12/3==32 and 3*(6+4)==5*6 and 7*20000==140000
assert 5400//9==600 and 6*9//9==6 and 520/4*7==910
assert 2400*35/100==840 and 180/720==0.25 and 40/0.08==500
assert 30*3+70*7==58*10 and 96000/0.8==120000
assert 154000//7==22000 and 50000*1.2*0.9==54000 and 13*7==91
assert 120000*9*8/1200==7200 and 2000*36000/(200000*60)==6
assert 400000*(100+10*2)//100==480000 and 400000*109*109//10000==475240
DEST04 = glob.glob("/sessions/*/mnt/Claude/web/1e/04-aranyossag")[0]
A04 = [
 ("Aránypár és méretarány.",
  ["$8:x=3:12$","$(x+4):5=x:3$","Egy $1:20\\,000$ méretarányú térképen a táv $7$ cm — mennyi a valóságban?"],
  ["$x=32$","$x=6$","$1{,}4$ km"], True),
 ("Elosztás és arányosság.",
  ["Ossz szét $5400$ dinárt $4:5$ arányban.","$6$ pumpa $9$ óra alatt tölt fel egy tartályt — hány óra kell $9$ pumpának?","$4$ kg alma $520$ din — mennyibe kerül $7$ kg?"],
  ["$2400$ és $3000$ din","$6$ óra","$910$ din"]),
 ("Százalék — a három alaptípus.",
  ["$2400$ $35\\%$-a","$180$ hány $\\%$-a a $720$-nak?","Egy szám $8\\%$-a $40$ — mennyi a szám?"],
  ["$840$","$25\\%$","$500$"], True),
 ("Keverék és fordított százalék.",
  ["$30\\%$-os és $70\\%$-os oldatból $10$ l $58\\%$-osat kell keverni — hány liter kell mindkettőből?","$20\\%$ engedmény után egy termék $96\\,000$ din — mennyi volt az eredeti ára?"],
  ["$3$ l ($30\\%$) és $7$ l ($70\\%$)","$120\\,000$ din"]),
]
A04 = A04 + A04_UJ
K04 = [
 ("Összetett arány és munkaidő-elosztás.",
  ["$x:y=2:5$ és $y:z=3:4$ — add meg $x:y:z$-t","$154\\,000$ din: egyik $10$ napot napi $8$ órával, másik $12$ napot napi $5$ órával dolgozott — mennyit kap fejenként?"],
  ["$6:15:20$","$88\\,000$ és $66\\,000$ din"]),
 ("Egymás utáni százalékváltozás.",
  ["$50\\,000$ din-t előbb $20\\%$-kal emelnek, majd $10\\%$-kal csökkentenek — mennyi a végső ár?","Egy téglalap szélessége $+30\\%$, hossza $-30\\%$ — hány $\\%$-kal változik a terület?"],
  ["$54\\,000$ din","$9\\%$-kal csökken"]),
 ("Kamatszámítás.",
  ["$120\\,000$ din $9\\%$-os kamatlábbal $8$ hónap alatt mennyi kamatot hoz?","Mekkora kamatláb hoz $200\\,000$ din után $60$ nap alatt $2000$ din kamatot?"],
  ["$7200$ din","$6\\%$"]),
]
K04 = K04 + K04_UJ
N04 = [
 ("A Henrik Tech $400\\,000$ dinárt fektet be $2$ évre. Az <b>A</b> bank $10\\%$ egyszerű kamatot, a <b>B</b> bank $9\\%$ kamatos kamatot kínál. Melyiknél lesz több pénz $2$ év múlva, és mennyivel?",
  None, "$A$: $480\\,000$, $B$: $475\\,240$ → az $A$ a jobb, $4760$ dinárral."),
]
brief04 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, Zsugor-protokoll modul. Ez a <b>Vészterem</b> otthoni "
 "edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: arány és arányos "
 "osztás, egyenes és fordított arányosság, méretarány, keverék, százalék, ezrelék és kamat. Haladj a fokozatokon: "
 "zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál lenyithatod — de előbb küzdd le magad!")
dr_page(DEST04, "index.html", "Arányosság", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: arány, arányos osztás, egyenes és fordított arányosság, méretarány, keverék, százalék és kamat. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief04, sect(A04, K04, N04),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("04 Vészterem kész: Alap", len(A04), "Közép", len(K04), "Nehéz", len(N04))

# =========================================================== 05 (Geometria)
# A házi a TESZTELT magot fedi (szögek, alakzatok, egybevágóság, vektorok) —
# izometria és szerkesztés NEM (felhasználói döntés).
assert 90-34==56 and 180-34==146 and 180-72==108 and 180-118==62
assert 180-(55+80)==45 and (5+7>11) and not (3+4>8) and (6+6>6)
assert 360-(100+90+85)==85 and 10+14-8==16 and 360//15==24 and 180-24==156 and 130//2==65
assert 4*20==80 and 5*20==100 and 3*20+15==75 and 5*20-25==75
assert 2*15==30 and 3*15==45 and 7*15==105 and 180-105==75
assert (8-2)*180==1080 and 8*5//2==20
assert 180-95==85 and 180-70==110 and 90+76//2==128
DEST05 = glob.glob("/sessions/*/mnt/Claude/web/1e/05-geometria")[0]
A05 = [
 ("Add meg a $34^\\circ$-os szög pótszögét és kiegészítő szögét!",
  None, "pótszög $56^\\circ$; kiegészítő $146^\\circ$."),
 ("Két egyenes metszéspontjánál az egyik szög $72^\\circ$. Mekkora a csúcsszöge és a mellékszöge?",
  None, "csúcsszög $72^\\circ$; mellékszög $108^\\circ$."),
 ("Az $a\\parallel b$ egyeneseket transzverzális metszi; az egyik szög $118^\\circ$. Add meg az egyállású, a váltó- és a társszögét!",
  None, "egyállású $118^\\circ$; váltószög $118^\\circ$; társszög $62^\\circ$."),
 ("Egy háromszög két belső szöge $55^\\circ$ és $80^\\circ$. Mekkora a harmadik?",
  None, "$45^\\circ$."),
 ("Melyik szakaszhármasból szerkeszthető háromszög?",
  ["$5,\\ 7,\\ 11$","$3,\\ 4,\\ 8$","$6,\\ 6,\\ 6$"],
  "a) igen; b) nem; c) igen.", True),
 ("Párosítsd a vonalhármast a metszéspontjával!",
  ["szögfelezők","oldalfelező merőlegesek","súlyvonalak","magasságvonalak"],
  ["beírt kör közép","körülírt kör közép","súlypont","magasságpont"], True),
 ("Egy négyszög három belső szöge $100^\\circ$, $90^\\circ$ és $85^\\circ$. Mekkora a negyedik?",
  None, "$85^\\circ$."),
 ("Egy érintőnégyszög oldalai (sorban) $AB=10$, $BC=8$, $CD=14$. Mekkora az $AD$?",
  None, "$AD=16$."),
 ("A szabályos $15$-szögről.",
  ["Mekkora egy külső szöge?","Mekkora egy belső szöge?"],
  ["$24^\\circ$","$156^\\circ$"]),
 ("Egy ívhez $130^\\circ$-os középponti szög tartozik. Mekkora a kerületi szög ugyanezen az íven?",
  None, "$65^\\circ$."),
 ("Egészítsd ki!",
  ["$\\overrightarrow{AB}+\\overrightarrow{BC}+\\overrightarrow{CA}$","$\\overrightarrow{AB}+\\overrightarrow{BA}$"],
  ["$\\vec{0}$ (nullvektor)","$\\vec{0}$ (nullvektor)"]),
]
A05 = A05 + A05_UJ
K05 = [
 ("Két szög egymás kiegészítő szöge, és úgy aránylanak, mint $4:5$. Mekkorák?",
  None, "$80^\\circ$ és $100^\\circ$."),
 ("Az $a\\parallel b$ egyeneseket transzverzális metszi; a váltószögpár tagjai $(3x+15)^\\circ$ és $(5x-25)^\\circ$. Mekkorák ezek a szögek?",
  None, "$75^\\circ$ (mindkettő)."),
 ("Egy háromszög belső szögei úgy aránylanak, mint $2:3:7$. Mekkorák, és mekkora a legnagyobb szög külső szöge?",
  None, "$30^\\circ,\\ 45^\\circ,\\ 105^\\circ$; a legnagyobb külső szöge $75^\\circ$."),
 ("Egy derékszögű trapéz egyik (nem derékszögű) szöge $68^\\circ$. Add meg mind a négy belső szöget!",
  None, "$90^\\circ,\\ 90^\\circ,\\ 68^\\circ,\\ 112^\\circ$."),
 ("Egy sokszög belső szögeinek összege $1080^\\circ$. Hány oldala van, és hány átlója?",
  None, "$8$ oldal; $20$ átló."),
 ("Egy húrnégyszög két szomszédos szöge $95^\\circ$ és $70^\\circ$. Add meg mind a négy szöget!",
  None, "$95^\\circ,\\ 70^\\circ,\\ 85^\\circ,\\ 110^\\circ$."),
 ("Az $ABCD$ paralelogramma átlóinak metszéspontja $S$, $\\overrightarrow{SA}=\\vec{m}$, $\\overrightarrow{SB}=\\vec{n}$. Fejezd ki $\\overrightarrow{AB}$-t és $\\overrightarrow{BC}$-t!",
  None, "$\\overrightarrow{AB}=\\vec{n}-\\vec{m}$; $\\overrightarrow{BC}=-\\vec{m}-\\vec{n}$."),
]
N05 = [
 ("Egy háromszög két belső szögének belső szögfelezői $128^\\circ$-os szöget zárnak be. Mekkora a harmadik belső szög?",
  None, "$76^\\circ$."),
 ("Egy húrnégyszög két szemközti szöge úgy aránylik, mint $4:5$. Mekkorák?",
  None, "$80^\\circ$ és $100^\\circ$."),
 ("Bizonyítsd be, hogy a paralelogramma szemközti oldalai egyenlők!",
  None, "Egy átló a paralelogrammát két egybevágó háromszögre bontja (SOS: a váltószögek egyenlők, az átló közös), ezért a szemközti oldalak egyenlők."),
]
brief05 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, geometriai modul. Ez a <b>Vészterem</b> otthoni "
 "edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a témakör <b>vizsgára menő magját</b> fedi le: "
 "szögek és szögpárok, háromszögek és egybevágóság, nevezetes pontok, négyszögek, sokszögek, a kör kerületi szöge és "
 "a vektorok. Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál "
 "lenyithatod — de előbb küzdd le magad!")
dr_page(DEST05, "index.html", "Geometria", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a témakör vizsgára menő magját lefedő házi feladatsor: szögek, háromszögek, egybevágóság, négyszögek, sokszögek, kör és vektorok. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief05, sect(A05, K05, N05),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("05 Vészterem kész: Alap", len(A05), "Közép", len(K05), "Nehéz", len(N05))

# =========================================================== 06 (Racionális algebrai kifejezések)
# A teljes témakört fedi (ishod 20): polinomműveletek, azonosságok, osztás+Bézout, bontás, törtek.
# Ishod 21 (x²≥0 / AM–GM) NEM kerül ide (felhasználói döntés) — csak a tananyagban, Kán-csapdaként.
assert (1-2+1+1)==1 and (8-12+2+2)==0  # Bézout ellenőrzők (A5: P(1)=1; N3: m=1 -> P(2)=0)
DEST06 = glob.glob("/sessions/*/mnt/Claude/web/1e/06-racionalis-algebrai-kifejezesek")[0]
A06 = [
 ("Végezd el a műveleteket!",
  ["$3a^2+5a^2-a^2$","$2x(3x-4)$","$(x+6)^2$","$(a-3)(a+3)$"],
  "a) $7a^2$; b) $6x^2-8x$; c) $x^2+12x+36$; d) $a^2-9$.", True),
 ("Írd fel kanonikus alakban: $(x+4)^2-(x^2+3x)$.",
  None, "$5x+16$."),
 ("Bontsd tényezőkre!",
  ["$10x+15$","$x^2-49$","$x^2+10x+25$"],
  "a) $5(2x+3)$; b) $(x-7)(x+7)$; c) $(x+5)^2$.", True),
 ("Bontsd tényezőkre!",
  ["$6a^2-9a$","$9x^2-16$"],
  ["$3a(2a-3)$","$(3x-4)(3x+4)$"]),
 ("A Bézout-tétellel add meg a maradékot: $P(x)=x^3-2x^2+x+1$ osztva $x-1$-gyel.",
  None, "$1$."),
 ("Mely értékekre értelmezett?",
  ["$\\dfrac{1}{x+5}$","$\\dfrac{3}{x^2-9}$"],
  ["$x\\neq -5$","$x\\neq \\pm 3$"]),
 ("Egyszerűsítsd, és add meg az értelmezési tartományt: $\\dfrac{x^2-1}{x+1}$.",
  None, "$x-1$, ÉT: $x\\neq -1$."),
 ("Végezd el a törtek műveleteit!",
  ["$\\dfrac{1}{x}+\\dfrac{2}{x}$","$\\dfrac{a}{2}\\cdot\\dfrac{4}{a}$"],
  ["$\\dfrac{3}{x}$","$2$"]),
]
A06 = A06 + A06_UJ
K06 = [
 ("Írd fel kanonikus alakban: $(2x+1)^2-(x-1)(x+2)$.",
  None, "$3x^2+3x+3$."),
 ("Végezd el a polinomosztást: $(x^3+2x^2-5x+1):(x-1)$.",
  None, "$x^2+3x-2$, a maradék $-1$."),
 ("Bontsd tényezőkre!",
  ["$x^3+64$","$x^3-x$"],
  ["$(x+4)(x^2-4x+16)$","$x(x-1)(x+1)$"]),
 ("Egyszerűsítsd, és add meg az értelmezési tartományt: $\\dfrac{x^2+5x+6}{x^2-4}$.",
  None, "$\\dfrac{x+3}{x-2}$, ÉT: $x\\neq \\pm 2$."),
 ("Add össze: $\\dfrac{1}{x-3}+\\dfrac{1}{x+3}$.",
  None, "$\\dfrac{2x}{x^2-9}$."),
]
K06 = K06 + K06_UJ
N06 = [
 ("Egyszerűsítsd az emeletes törtet: $\\dfrac{\\dfrac{1}{x}-\\dfrac{1}{y}}{\\dfrac{1}{x}+\\dfrac{1}{y}}$.",
  None, "$\\dfrac{y-x}{y+x}$."),
 ("Vond egyetlen törtté: $\\dfrac{1}{a-2}-\\dfrac{1}{a+2}+\\dfrac{4}{a^2-4}$.",
  None, "$\\dfrac{8}{a^2-4}$."),
 ("Határozd meg az $m$ paramétert úgy, hogy $P(x)=x^3-3x^2+mx+2$ osztható legyen $x-2$-vel!",
  None, "$m=1$."),
]
brief06 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, A Hatalom Nyelve modul. Ez a <b>Vészterem</b> otthoni "
 "edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: polinomműveletek "
 "és nevezetes azonosságok, polinomosztás és a Bézout-tétel, tényezőkre bontás, valamint az algebrai törtek "
 "(értelmezési tartomány, egyszerűsítés, alapműveletek). Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros "
 "(nehéz). A végeredményt minden feladatnál lenyithatod — de előbb küzdd le magad!")
dr_page(DEST06, "index.html", "Racionális algebrai kifejezések", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: polinomok, nevezetes azonosságok, tényezőkre bontás, Bézout-tétel és algebrai törtek. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief06, sect(A06, K06, N06),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("06 Vészterem kész: Alap", len(A06), "Közép", len(K06), "Nehéz", len(N06))

# =========================================================== 07 (Lineáris egyenletek, egyenlőtlenségek, rendszerek)
# A teljes témakört fedi (ishod 22-25): egyenletek, egyenlőtlenségek, függvény, 2×2 rendszerek, szöveges feladatok.
# Gauss (3×3) NEM kerül ide (felhasználói döntés) — csak a tananyagban és max 1 feladat a feladatgyűjteményben.
assert 40==4*10 and 5*8+20==60  # sanity
DEST07 = glob.glob("/sessions/*/mnt/Claude/web/1e/07-linearis-egyenletek-es-rendszerek")[0]
A07 = [
 ("Oldd meg az egyenleteket!",
  ["$4x-5=11$","$3(x-2)=x+2$","$\\dfrac{x}{4}+1=3$"],
  "a) $x=4$; b) $x=4$; c) $x=8$.", True),
 ("Oldd meg az egyenlőtlenségeket!",
  ["$2x+1>7$","$-x\\le 4$","$3x-1<2x+5$"],
  "a) $x>3$; b) $x\\ge -4$; c) $x<6$.", True),
 ("Adott az $f(x)=-2x+6$ függvény.",
  ["$f(0)$","$f(3)$","a nullahelye"],
  "a) $6$; b) $0$; c) $x=3$.", True),
 ("Add meg a megoldáshalmazt intervallummal!",
  ["$x\\ge 5$","$x<0$"],
  ["$[5,\\infty)$","$(-\\infty,0)$"]),
 ("Oldd meg a rendszert: $x+y=7$, $x-y=3$.",
  None, "$x=5,\\ y=2$."),
 ("Oldd meg a rendszert: $2x+y=8$, $x+y=5$.",
  None, "$x=3,\\ y=2$."),
 ("Oldd meg a törtes egyenletet: $\\dfrac{x-1}{2}=x-4$.",
  None, "$x=7$."),
 ("Melyik szám a megoldás?",
  ["$5x=35$","$x+9=4$","$2x-6=0$"],
  "a) $7$; b) $-5$; c) $3$.", True),
]
A07 = A07 + A07_UJ
K07 = [
 ("Oldd meg a törtes egyenletet: $\\dfrac{2x+1}{3}-\\dfrac{x-1}{2}=2$.",
  None, "$x=7$."),
 ("Oldd meg a kibontással: $(x-2)(x+3)-(x+1)(x-1)=-1$.",
  None, "$x=4$."),
 ("Oldd meg a rendszert: $3x-2y=5$, $x+2y=7$.",
  None, "$x=3,\\ y=2$."),
 ("Egy szám és a nála $12$-vel nagyobb szám összege $50$. Melyik ez a két szám?",
  None, "$19$ és $31$."),
 ("Egy teljes árú jegy $500$ Ft, egy diákjegy $300$ Ft. Összesen $15$ jegyet vettek $5900$ Ft-ért. Hány teljes árú és hány diákjegyet?",
  None, "$7$ teljes árú és $8$ diákjegy."),
]
K07 = K07 + K07_UJ
N07 = [
 ("Az anya most négyszer annyi idős, mint a lánya; $5$ év múlva már csak háromszor annyi. Hány évesek most?",
  None, "az anya $40$, a lánya $10$ éves."),
 ("Egy medencét az egyik csap egyedül $6$ óra, a másik egyedül $12$ óra alatt tölt meg. Mennyi idő alatt telik meg együtt?",
  None, "$4$ óra."),
 ("Milyen $k$ esetén van a rendszernek végtelen sok megoldása: $3x+y=5$, $6x+2y=k$?",
  None, "$k=10$ (ekkor a két egyenlet egybeesik); ha $k\\neq 10$, nincs megoldás."),
]
brief07 = ("🕹️ <b>SZVETI:</b> <b>Vészterem</b>-szimuláció, A Végső Egyenlet modul. Ez a <b>Vészterem</b> otthoni "
 "edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: lineáris "
 "egyenletek és egyenlőtlenségek, a lineáris függvény, a kétismeretlenes rendszerek és a szöveges feladatok. Haladj "
 "a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál lenyithatod — de "
 "előbb küzdd le magad!")
dr_page(DEST07, "index.html", "Lineáris egyenletek és rendszerek", "feladatok-hazi.html",
 "🕹️ Vészterem — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: egyenletek, egyenlőtlenségek, lineáris függvény, rendszerek és szöveges feladatok. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief07, sect(A07, K07, N07),
 "index.html", "Témakör Főhadiszállása", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("07 Vészterem kész: Alap", len(A07), "Közép", len(K07), "Nehéz", len(N07))
