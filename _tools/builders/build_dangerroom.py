# -*- coding: utf-8 -*-
"""Danger Room (Veszélyterem) — témakörönként EGY, teljes témakört lefedő házi feladatsor.
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
  <a href="../../index.html">Főoldal</a> ›
  <a href="../index.html"><span class="tagozat-jel">1e</span></a> ›
  <a href="{topic_link}">{topic_name}</a> ›
  <span class="itt">Danger Room — házi</span>
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
K01 = [
 ("Igazságtáblázattal döntsd el, <b>tautológia-e</b>: $(p\\land q)\\Rightarrow p$.",
  None, "Igen, tautológia."),
 ("Írd fel kvantoros alakban, majd <b>tagadd</b> (és döntsd el, igaz-e az eredeti)!",
  ["„Minden valós $x$-re $x^2\\ge 0$.”","„Van olyan természetes szám, amely osztható 3-mal.”"],
  ["$\\forall x\\in\\mathbb{R}\\,(x^2\\ge 0)$ — igaz; tagadása $\\exists x\\in\\mathbb{R}\\,(x^2<0)$.",
   "$\\exists x\\in\\mathbb{N}\\,(3\\mid x)$ — igaz; tagadása $\\forall x\\in\\mathbb{N}\\,(3\\nmid x)$."]),
 ("Adott $A=\\{x\\in\\mathbb{Z}\\mid -2\\le x<3\\}$ és $B=\\{x\\in\\mathbb{Z}\\mid 0<x\\le 5\\}$. Sorold fel a halmazokat, majd add meg $A\\cup B$-t, $A\\cap B$-t és $A\\setminus B$-t!",
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
N01 = [
 ("<b>Sziget-akták.</b> A lovag mindig igazat mond, a lókötő mindig hazudik. $A$ azt mondja: „$B$ lókötő.”, $B$ azt mondja: „$A$ és én azonos típusúak vagyunk.” Ki micsoda? Indokolj!",
  None, "$A$ lovag, $B$ lókötő."),
 ("<b>Fordított szita.</b> Egy 40 fős csoportban 25-en sportolnak ($S$), 20-an zenélnek ($Z$), 8-an egyiket sem. Rajzolj Venn-diagramot, és számold ki, hányan csinálják <b>mindkettőt</b>!",
  None, "Mindkettőt: $13$."),
 ("$f(x)=2x+1$, $g(x)=x^2$. Add meg $(f\\circ g)(x)$-et és $(g\\circ f)(x)$-et — egyenlők-e? Számítsd ki mindkettőt $x=3$-ra!",
  None, "$(f\\circ g)(x)=2x^2+1$, $(g\\circ f)(x)=4x^2+4x+1$; nem egyenlők. $(f\\circ g)(3)=19$, $(g\\circ f)(3)=49$."),
]
brief01 = ("🕹️ <b>SZVETI:</b> Üdv a <b>Veszélyteremben</b>, kadét! Ez a <b>Danger Room</b> — a kampusz "
 "szimulációs edzőterme (a technológiát a Xavier-intézet X-Menjeitől licenceltük). Itt otthon, a saját "
 "tempódban gyakorolsz két küldetés között. A szimuláció a <b>teljes témakört</b> lefedi: logika, halmazok, "
 "függvények. Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden "
 "feladatnál lenyithatod — de előbb küzdd le magad!")
dr_page(DEST01, "index.html", "Logika, halmazok, függvények", "feladatok-hazi.html",
 "🕹️ Danger Room — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: logika, halmazok és függvények. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief01, sect(A01, K01, N01),
 "index.html", "Témakör főoldala", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("01 Danger Room kész: Alap", len(A01), "Közép", len(K01), "Nehéz", len(N01))

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
K02 = [
 ("Egy $\\alpha$ hegyesszögre $\\sin\\alpha=0{,}6$. Számítsd ki <b>pontosan</b> $\\cos\\alpha$-t, $\\operatorname{tg}\\alpha$-t és $\\operatorname{ctg}\\alpha$-t!",
  None, "$\\cos\\alpha=\\tfrac45$, $\\operatorname{tg}\\alpha=\\tfrac34$, $\\operatorname{ctg}\\alpha=\\tfrac43$."),
 ("Oldd meg a derékszögű háromszöget: az átfogó $c=12\\,\\text{cm}$, az egyik hegyesszög $\\alpha=35^\\circ$ (az $a$-val szemközti). Számítsd ki a másik hegyesszöget és a két befogót (2 tizedesre)!",
  None, "$\\beta=55^\\circ$; $a\\approx 6{,}88\\,\\text{cm}$; $b\\approx 9{,}83\\,\\text{cm}$."),
 ("Számold ki <b>számológép nélkül</b> (pótszög + alapazonosság)!",
  ["$\\sin^2 25^\\circ+\\cos^2 25^\\circ$","$\\sin 40^\\circ-\\cos 50^\\circ$"],
  ["$1$","$0$"]),
]
N02 = [
 ("<b>Terep-alkalmazás.</b> Egy fa árnyéka $12\\,\\text{m}$ hosszú, amikor a napsugarak $40^\\circ$-os emelkedési szöget zárnak be a vízszintessel. Milyen magas a fa? Rajzolj, és számolj 2 tizedesre!",
  None, "$m\\approx 10{,}07\\,\\text{m}$."),
]
brief02 = ("🕹️ <b>SZVETI:</b> <b>Veszélyterem</b>-szimuláció, célzó modul. Ez a <b>Danger Room</b> otthoni "
 "edzésváltozata — itt gyakorolsz a terepküldetés előtt és után. A szimuláció a <b>teljes trigonometria-témakört</b> "
 "lefedi: szögfüggvények, nevezetes szögek, a derékszögű háromszög megoldása és valós mérések. Tartsd a "
 "<b>kerekítési szabályt</b> (szögfüggvény-érték 5 tizedes, hossz és szög 2 tizedes). Fokozatok: zöld → sárga → piros.")
dr_page(DEST02, "index.html", "Trigonometria", "feladatok-hazi.html",
 "🕹️ Danger Room — házi feladatgyűjtemény",
 "Egyetlen, a teljes trigonometria-témakört lefedő házi feladatsor. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief02, sect(A02, K02, N02),
 "index.html", "Témakör főoldala", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("02 Danger Room kész: Alap", len(A02), "Közép", len(K02), "Nehéz", len(N02))

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
K03 = [
 ("Három jelzőfény $8$, $12$ és $20$ másodpercenként villan; most együtt villantak. Hány másodperc múlva villannak legközelebb megint mind együtt? (Prímtényezős alak, majd LKT.)",
  None, "$\\text{LKT}(8,12,20)=120$ másodperc."),
 ("Határozd meg a hiányzó számjegyet — add meg az összes megoldást!",
  ["$\\overline{47x}$ osztható $3$-mal","$\\overline{58x0}$ osztható $8$-cal"],
  ["$x\\in\\{1,4,7\\}$","$x\\in\\{0,4,8\\}$"]),
 ("Az $x=7{,}64983$ értéket kerekítsd 2 tizedesre, add meg az abszolút hibát; majd számold ki normál alakban: $(4\\cdot 10^{6})\\cdot(2{,}5\\cdot 10^{-3})$.",
  None, "$x^{*}=7{,}65$; $\\Delta=0{,}00017$; a szorzat $1\\cdot 10^{4}$."),
]
N03 = [
 ("Bizonyítsd be, hogy $n^3-n$ osztható $6$-tal minden egész $n$-re!",
  None, "$n^3-n=(n-1)\\,n\\,(n+1)$ — három egymást követő egész szorzata, ezért osztható $6$-tal."),
 ("Melyik a legkisebb pozitív egész szám, amivel a $600$-at szorozva köbszámot kapunk? (Kanonikus alak.)",
  None, "$45$."),
]
brief03 = ("🕹️ <b>SZVETI:</b> <b>Veszélyterem</b>-szimuláció, kódtörő + kalibráló modul. Ez a <b>Danger Room</b> "
 "otthoni edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: "
 "számelmélet és számrendszerek (Shuri szektora), valamint a valós számok, a közelítés és a normál alak (Banner "
 "szektora). Haladj a fokozatokon: zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál "
 "lenyithatod — de előbb küzdd le magad!")
dr_page(DEST03, "index.html", "Egész és valós számok", "feladatok-hazi.html",
 "🕹️ Danger Room — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: számelmélet, számrendszerek, számhalmazok, közelítés. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief03, sect(A03, K03, N03),
 "index.html", "Témakör főoldala", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("03 Danger Room kész: Alap", len(A03), "Közép", len(K03), "Nehéz", len(N03))

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
N04 = [
 ("A Pym Tech $400\\,000$ dinárt fektet be $2$ évre. Az <b>A</b> bank $10\\%$ egyszerű kamatot, a <b>B</b> bank $9\\%$ kamatos kamatot kínál. Melyiknél lesz több pénz $2$ év múlva, és mennyivel?",
  None, "$A$: $480\\,000$, $B$: $475\\,240$ → az $A$ a jobb, $4760$ dinárral."),
]
brief04 = ("🕹️ <b>SZVETI:</b> <b>Veszélyterem</b>-szimuláció, Pym-protokoll modul. Ez a <b>Danger Room</b> otthoni "
 "edzésváltozata — itt gyakorolsz a saját tempódban. A szimuláció a <b>teljes témakört</b> lefedi: arány és arányos "
 "osztás, egyenes és fordított arányosság, méretarány, keverék, százalék, ezrelék és kamat. Haladj a fokozatokon: "
 "zöld (alap) → sárga (közép) → piros (nehéz). A végeredményt minden feladatnál lenyithatod — de előbb küzdd le magad!")
dr_page(DEST04, "index.html", "Arányosság", "feladatok-hazi.html",
 "🕹️ Danger Room — házi feladatgyűjtemény",
 "Egyetlen, a teljes témakört lefedő házi feladatsor: arány, arányos osztás, egyenes és fordított arányosság, méretarány, keverék, százalék és kamat. Minden feladatnál lenyitható végeredmény — előbb számolj, csak utána nézd meg!",
 brief04, sect(A04, K04, N04),
 "index.html", "Témakör főoldala", "osszefoglalo.html", "Tömör összefoglaló",
 "Elakadtál? Nézd át a <a href=\"index.html\">témakör tananyagait</a> vagy a <a href=\"osszefoglalo.html\">tömör összefoglalót</a>.")
print("04 Danger Room kész: Alap", len(A04), "Közép", len(K04), "Nehéz", len(N04))
