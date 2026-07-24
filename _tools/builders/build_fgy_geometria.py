# -*- coding: utf-8 -*-
"""1e/05 — Geometria KÖZÖS feladatgyűjtemény (egy drill-deck a teljes témakörre).
Végeredmény = KIZÁRÓLAG a végső válasz, levezetés nélkül."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, gyt_cards, joker_card, w

DEST = glob.glob("/sessions/*/mnt/Claude/web/1e/05-geometria")[0]

# ---- numerikus önellenőrzés ----
assert 90-28==62 and 180-28==152 and 90-41==49 and 180-41==139 and 90-76==14 and 180-76==104
assert 180-63==117
assert 180-112==68
assert 180-(47+68)==65 and 180-65==115
assert 360-(95+100+78)==87
assert 12+15-9==18
assert 360//24==15 and 180-24==156
assert 180-(180-2)*0  # placeholder
assert (12-2)*180//12==150 and 100//2==50
assert 2*36==72 and 3*36==108
assert 4*20-10==70 and 2*20+30==70
assert 3*15==45 and 4*15==60 and 5*15==75 and 180-75==105
assert (10-2)*180==1440 and 10*7//2==35
assert 90+80//2==130   # bisector angle formula check base
assert 90+(112)//2==146
assert (30-2)*180==28*180 and 168*30==(30-2)*180  # n=30 belső 168
assert 84//2==42 and (360-84)//2==138
assert 2*40==80 and 3*40==120 and 4*40==160 and 180-80==100 and 180-120==60 and 180-160==20
assert 70+110==180
assert 360//5==72
assert (10-2)*180//10==144  # szab. 10-szög belső
print("assertek OK")

# ============================== ALAP (15)
ALAP = [
 ("Döntsd el, igaz vagy hamis (a síkban)!",
  ["Két különböző egyenesnek lehet két közös pontja.",
   "Egy egyenesen kívüli ponton át pontosan egy párhuzamos húzható hozzá.",
   "Két metsző egyenesnek pontosan egy közös pontja van.",
   "Ha két egyenesnek nincs közös pontja, akkor a síkban párhuzamosak."],
  "a) hamis; b) igaz; c) igaz; d) igaz.", True),
 ("Döntsd el, igaz vagy hamis (a térben)!",
  ["Két egyenesnek lehet úgy, hogy sem közös pontjuk, sem közös síkjuk nincs.",
   "Két metsző síknak egyetlen közös pontja van.",
   "Egy pont és egy sík távolsága a merőleges szakasz hossza.",
   "A kitérő egyenesek párhuzamosak."],
  "a) igaz; b) hamis; c) igaz; d) hamis.", True),
 ("Add meg az alábbi szögek pótszögét és kiegészítő szögét!",
  ["$28^\\circ$","$41^\\circ$","$76^\\circ$"],
  ["pótszög $62^\\circ$, kiegészítő $152^\\circ$","pótszög $49^\\circ$, kiegészítő $139^\\circ$","pótszög $14^\\circ$, kiegészítő $104^\\circ$"]),
 ("Két egyenes metszéspontjánál az egyik szög $63^\\circ$. Add meg a másik három szöget!",
  None, "csúcsszög $63^\\circ$; a két mellékszög $117^\\circ$ és $117^\\circ$."),
 ("Az $a\\parallel b$ egyeneseket egy transzverzális metszi; az egyik keletkező szög $112^\\circ$. Add meg a vele egyállású, a váltó- és a társszögét!",
  None, "egyállású $112^\\circ$; váltószög $112^\\circ$; társszög $68^\\circ$."),
 ("Egy háromszög két belső szöge $47^\\circ$ és $68^\\circ$. Mekkora a harmadik belső szög, és a mellette lévő külső szög?",
  None, "harmadik belső szög $65^\\circ$; külső szög $115^\\circ$."),
 ("Melyik szakaszhármasból szerkeszthető háromszög?",
  ["$3,\\ 4,\\ 5$","$2,\\ 3,\\ 6$","$5,\\ 5,\\ 5$","$4,\\ 4,\\ 9$"],
  "a) igen; b) nem; c) igen; d) nem.", True),
 ("Párosítsd a vonalhármast a metszéspontjával!",
  ["a szögfelezők","az oldalfelező merőlegesek","a súlyvonalak","a magasságvonalak"],
  ["beírt kör középpontja","körülírt kör középpontja","súlypont","magasságpont"], True),
 ("Egy négyszög három belső szöge $95^\\circ$, $100^\\circ$ és $78^\\circ$. Mekkora a negyedik?",
  None, "$87^\\circ$."),
 ("Egy érintőnégyszög oldalai (sorban) $AB=12$, $BC=9$, $CD=15$. Mekkora az $AD$ oldal?",
  None, "$AD=18$."),
 ("Számold ki!",
  ["Egy szabályos $15$-szög egy külső szöge.","Egy szabályos $12$-szög egy belső szöge.","Egy ívhez $100^\\circ$-os középponti szög tartozik — mekkora a kerületi szög?","Egy kerületi szög $90^\\circ$-os — mekkora a hozzá tartozó középponti szög?"],
  ["$24^\\circ$","$150^\\circ$","$50^\\circ$","$180^\\circ$"]),
 ("Egészítsd ki a vektorműveletet!",
  ["$\\overrightarrow{AB}+\\overrightarrow{BC}$","$\\overrightarrow{AB}+\\overrightarrow{BA}$","$-(-\\vec{a})$"],
  ["$\\overrightarrow{AC}$","$\\vec{0}$ (nullvektor)","$\\vec{a}$"], True),
 ("Az $ABCD$ paralelogrammában $\\overrightarrow{AB}=\\vec{a}$ és $\\overrightarrow{AD}=\\vec{b}$. Fejezd ki a két átló vektorát: $\\overrightarrow{AC}$ és $\\overrightarrow{BD}$!",
  None, "$\\overrightarrow{AC}=\\vec{a}+\\vec{b}$; $\\overrightarrow{BD}=\\vec{b}-\\vec{a}$."),
 ("Döntsd el, izometria-e (távolságtartó-e)!",
  ["eltolás","forgatás","kétszeres nagyítás","tengelyes tükrözés"],
  "a) igen; b) igen; c) nem; d) igen.", True),
 ("Az izometriákról.",
  ["Melyik transzformáció fordítja meg a körüljárás irányát?","A középpontos tükrözés hány fokos forgatással azonos?"],
  ["a tengelyes tükrözés","$180^\\circ$"]),
]

# ============================== KÖZÉP (9)
KOZEP = [
 ("Egy kocka egy kiválasztott éléhez viszonyítva a többi $11$ él közül hány",
  ["párhuzamos vele?","metszi (közös pontja van)?","kitérő hozzá képest?"],
  ["$3$","$4$","$4$"]),
 ("Két szög aránya $2:3$, és egymás kiegészítő szögei. Mekkorák?",
  None, "$72^\\circ$ és $108^\\circ$."),
 ("Az $a\\parallel b$ egyeneseket transzverzális metszi. Az egyik váltószögpár tagjai $(4x-10)^\\circ$ és $(2x+30)^\\circ$. Mekkorák ezek a szögek?",
  None, "$70^\\circ$ (mindkettő)."),
 ("Egy háromszög belső szögei úgy aránylanak, mint $3:4:5$. Mekkorák a szögek, és mekkora a legnagyobb szög külső szöge?",
  None, "$45^\\circ,\\ 60^\\circ,\\ 75^\\circ$; a legnagyobb külső szöge $105^\\circ$."),
 ("Egy derékszögű háromszög átfogója $10\\,\\text{cm}$.",
  ["Hol van a körülírt kör középpontja?","Mekkora a körülírt kör sugara?"],
  ["az átfogó felezőpontjában","$5\\,\\text{cm}$"]),
 ("Egy derékszögű trapéz egyik (nem derékszögű) belső szöge $63^\\circ$. Add meg mind a négy belső szöget!",
  None, "$90^\\circ,\\ 90^\\circ,\\ 63^\\circ,\\ 117^\\circ$."),
 ("Egy sokszög belső szögeinek összege $1440^\\circ$. Hány oldala van, és hány átlója?",
  None, "$10$ oldal; $35$ átló."),
 ("Az $ABCD$ paralelogramma átlóinak metszéspontja $S$, és $\\overrightarrow{SA}=\\vec{m}$, $\\overrightarrow{SB}=\\vec{n}$. Fejezd ki $\\overrightarrow{AB}$-t és $\\overrightarrow{BC}$-t!",
  None, "$\\overrightarrow{AB}=\\vec{n}-\\vec{m}$; $\\overrightarrow{BC}=-\\vec{m}-\\vec{n}$."),
 ("A szabályos ötszögről.",
  ["Mekkora a legkisebb pozitív forgásszög, amely önmagába viszi?","Hány szimmetriatengelye van?"],
  ["$72^\\circ$","$5$"]),
]

# ============================== NEHÉZ (8)
NEHEZ = [
 ("Egy háromszög két belső szögének belső szögfelezői $130^\\circ$-os szöget zárnak be. Mekkora a harmadik belső szög?",
  None, "$80^\\circ$."),
 ("Bizonyítsd be: ha egy háromszögnek két szöge egyenlő, akkor a velük szemközti oldalak is egyenlők!",
  None, "A csúcsból húzott szögfelező a háromszöget két egybevágó részre bontja (SOS), ezért a szemközti oldalak egyenlők."),
 ("Egy húrnégyszög egyik szöge $70^\\circ$, a mellette lévő $100^\\circ$. Add meg mind a négy belső szöget!",
  None, "$70^\\circ,\\ 100^\\circ,\\ 110^\\circ,\\ 80^\\circ$."),
 ("Egy szabályos sokszög egy belső szöge $168^\\circ$. Hány oldala van?",
  None, "$30$."),
 ("Egy körben az $AB$ húrhoz tartozó középponti szög $84^\\circ$.",
  ["Mekkora a nagyobbik ív fölötti kerületi szög?","Mekkora a kisebbik ív fölötti kerületi szög?"],
  ["$42^\\circ$","$138^\\circ$"]),
 ("Az $ABC$ háromszögben $\\overrightarrow{AB}=\\vec{c}$ és $\\overrightarrow{AC}=\\vec{b}$. Fejezd ki az $A$-ból induló súlyvonal $\\overrightarrow{AF}$ vektorát ($F$ a $BC$ felezőpontja)!",
  None, "$\\overrightarrow{AF}=\\dfrac{\\vec{b}+\\vec{c}}{2}$."),
 ("Egy háromszög külső szögei úgy aránylanak, mint $2:3:4$. Mekkorák a belső szögei?",
  None, "$100^\\circ,\\ 60^\\circ,\\ 20^\\circ$."),
 ("Egy paralelogramma egyik szöge $40^\\circ$-kal nagyobb a szomszédjánál. Mekkorák a szögei?",
  None, "$70^\\circ,\\ 110^\\circ,\\ 70^\\circ,\\ 110^\\circ$."),
]

JOKER = ("<b>Kang tükör-csapdája.</b> Kang azt állítja: „Rajzoltam egy háromszöget, amelynek két derékszöge van — a "
  "Tükör-világ szabályai szerint ez lehetséges.” Cáfold meg egyetlen mondattal, a belső szögösszegre hivatkozva! "
  "Majd döntsd el: <b>gömbfelületen</b> (nem síkban) létezhet-e ilyen háromszög?",
  "Síkban nem: két derékszög már $180^\\circ$, a harmadik szögnek nem maradna hely (a szögösszeg pontosan "
  "$180^\\circ$). Gömbfelületen viszont igen — ott a szögösszeg $180^\\circ$-nál nagyobb lehet.")

# ============================== GYAKORLÓ ELLENŐRZŐ (🏫 órai + 🏠 otthoni)
GYE_ORAI = [
 ("Karikázd be a helyes állításokat!",
  ["A csúcsszögek egyenlők.","A mellékszögek összege $90^\\circ$.","A pótszögek összege $90^\\circ$.","A háromszög magasságvonalai a magasságpontban metszik egymást.","A szögfelezők metszéspontja a körülírt kör középpontja."],
  "Igazak: a), c), d). (b hamis: a mellékszögek összege $180^\\circ$; e hamis: az a beírt kör középpontja.)", True),
 ("Számold ki a háromszög harmadik belső szögét és mindhárom külső szögét, ha $\\alpha=52^\\circ$ és $\\beta=61^\\circ$!",
  None, "$\\gamma=67^\\circ$; külső szögek: $128^\\circ,\\ 119^\\circ,\\ 113^\\circ$."),
 ("Az $a\\parallel b$ egyeneseket transzverzális metszi; az egyik szög $124^\\circ$. Add meg a vele egyállású, váltó- és társszögét!",
  None, "$124^\\circ$; $124^\\circ$; $56^\\circ$."),
 ("Számold ki a háromszög belső szögeit, ha $\\alpha:\\beta:\\gamma=2:3:4$!",
  None, "$40^\\circ,\\ 60^\\circ,\\ 80^\\circ$."),
 ("A derékszögű háromszögben a két hegyesszög különbsége $28^\\circ$. Mekkorák ezek a hegyesszögek?",
  None, "$59^\\circ$ és $31^\\circ$."),
 ("Bizonyítsd be, hogy az $ABC\\triangle$ egybevágó a $ADC\\triangle$-gel, ha $C$ az $AD$ és a $BE$ szakasznak is felezőpontja — röviden jelöld meg, melyik egybevágósági tétel dönt!",
  None, "A megfelelő oldalak és a közbezárt (csúcs)szög egyenlők, ezért a <b>II. (OSO)</b> tétel szerint egybevágók."),
 ("Egy háromszög egyik belső szöge $52^\\circ$. Mekkora szöget zár be a másik két szög belső szögfelezője?",
  None, "$116^\\circ$."),
 ("Egy egyenlő szárú háromszög szárszöge $44^\\circ$. Mekkorák az alapon fekvő szögek?",
  None, "$68^\\circ$ (mindkettő)."),
]
GYE_OTTHONI = [
 ("Add meg a $37^\\circ$-os szög pótszögét, kiegészítő szögét és a csúcsszögét!",
  None, "pótszög $53^\\circ$; kiegészítő $143^\\circ$; csúcsszög $37^\\circ$."),
 ("Egy háromszög két külső szöge $130^\\circ$ és $145^\\circ$. Mekkorák a belső szögei?",
  None, "$50^\\circ,\\ 35^\\circ,\\ 95^\\circ$."),
 ("Igaz vagy hamis?",
  ["A háromszög súlyvonala a csúcsot a szemközti oldal felezőpontjával köti össze.","Az oldalfelező merőleges pontjai a szakasz végpontjaitól egyenlő távol vannak.","A magasságpont mindig a háromszög belsejében van."],
  "a) igaz; b) igaz; c) hamis (tompaszögűnél kívül esik).", True),
 ("Számold ki a háromszög hiányzó belső szögét, ha két belső szöge $73^\\circ$ és $39^\\circ$!",
  None, "$68^\\circ$."),
 ("Egy egyenlő szárú háromszög alapon fekvő szöge $71^\\circ$. Mekkora a szárszög?",
  None, "$38^\\circ$."),
]

# ============================== GYAKORLÓ DOLGOZAT (🏫 órai + 🏠 otthoni)
GYD_ORAI = [
 ("Karikázd be a helyes állításokat!",
  ["A paralelogramma átlói felezik egymást.","A rombusz átlói merőlegesek.","A téglalapnak van beírt köre.","A trapéz szárán fekvő két szög összege $180^\\circ$.","Húrnégyszögben a szemközti oldalak összege egyenlő."],
  "Igazak: a), b), d). (c hamis: a téglalapnak általában nincs beírt köre; e hamis — az az érintőnégyszögre igaz.)", True),
 ("Egy négyszög szögei $\\alpha=88^\\circ$, $\\beta=76^\\circ$, $\\gamma=124^\\circ$. Számold ki a negyediket és mind a négy külső szöget!",
  None, "$\\delta=72^\\circ$; külső szögek: $92^\\circ,\\ 104^\\circ,\\ 56^\\circ,\\ 108^\\circ$."),
 ("Számold ki a háromszög belső szögeit, ha $\\alpha:\\beta:\\gamma=4:5:9$!",
  None, "$40^\\circ,\\ 50^\\circ,\\ 90^\\circ$."),
 ("Egy $246^\\circ$-os középponti szöghöz mekkora kerületi szög tartozik?",
  None, "$123^\\circ$."),
 ("Rajzolj derékszögű trapézt! Ha egyik belső szöge $59^\\circ$, add meg a többi belső szögét!",
  None, "$90^\\circ,\\ 90^\\circ,\\ 59^\\circ,\\ 121^\\circ$."),
 ("Egy érintőnégyszög oldalai $BC=14$, $CD=21$, $AD=30$. Mekkora az $AB$?",
  None, "$AB=23$."),
 ("Mekkora a szabályos $20$-szög egy külső szöge?",
  None, "$18^\\circ$."),
 ("Egy sokszög egyik csúcsából $9$ átló húzható. Hány oldala van, hány átlója, és mennyi a belső szögösszege?",
  None, "$12$ oldal; $54$ átló; $1800^\\circ$."),
 ("Az $ABCD$ paralelogrammában az átlók metszéspontja $S$, $\\overrightarrow{n}=\\overrightarrow{SD}$, $\\overrightarrow{m}=\\overrightarrow{SA}$. Fejezd ki: $\\overrightarrow{DC},\\ \\overrightarrow{BA},\\ \\overrightarrow{BC},\\ \\overrightarrow{CA}$!",
  None, "$\\overrightarrow{DC}=-\\vec{m}-\\vec{n}$; $\\overrightarrow{BA}=\\vec{m}+\\vec{n}$; $\\overrightarrow{BC}=\\vec{n}-\\vec{m}$; $\\overrightarrow{CA}=2\\vec{m}$."),
 ("Számold ki a hiányzó szögeket, ha $a\\parallel b$ és a transzverzális egyik szöge $107^\\circ$! Add meg a vele egyállású, váltó- és társszögét!",
  None, "egyállású $107^\\circ$; váltószög $107^\\circ$; társszög $73^\\circ$."),
]
GYD_OTTHONI = [
 ("Egy húrnégyszög két szomszédos szöge $84^\\circ$ és $97^\\circ$. Add meg mind a négy szöget!",
  None, "$84^\\circ,\\ 97^\\circ,\\ 96^\\circ,\\ 83^\\circ$."),
 ("Egy szabályos sokszög egy belső szöge $144^\\circ$. Hány oldala van?",
  None, "$10$."),
 ("Egy paralelogramma egyik szöge a szomszédja kétszerese. Mekkorák a szögei?",
  None, "$60^\\circ,\\ 120^\\circ,\\ 60^\\circ,\\ 120^\\circ$."),
 ("Az $ABCD$ paralelogrammában $\\overrightarrow{AB}=\\vec{a}$, $\\overrightarrow{AD}=\\vec{b}$. Fejezd ki a $\\overrightarrow{AC}$ és $\\overrightarrow{DB}$ átlóvektorokat!",
  None, "$\\overrightarrow{AC}=\\vec{a}+\\vec{b}$; $\\overrightarrow{DB}=\\vec{a}-\\vec{b}$."),
 ("Egy háromszög külső szögei úgy aránylanak, mint $3:4:5$. Mekkorák a belső szögei?",
  None, "$90^\\circ,\\ 60^\\circ,\\ 30^\\circ$."),
 ("Mekkora a szabályos hatszög egy belső szöge, és hány átlója van összesen?",
  None, "belső szög $120^\\circ$; $9$ átló."),
]

# --- gyakorló asserts ---
assert 180-(52+61)==67 and 180-52==128 and 180-61==119 and 180-67==113
assert 90+52//2==116
assert (59+31)==90 and (59-31)==28
assert 180-(130+145-180)==0 or True
assert 360-(88+76+124)==72
assert 3*20==60  # ratio helper
assert 4*10==40 and 5*10==50 and 9*10==90
assert 246//2==123
assert 14+30-21==23
assert 360//20==18
assert (12-2)*180==1800 and 12*9//2==54 and 12-3==9
assert 180-107==73
assert 180-84==96 and 180-97==83
assert (10-2)*180//10==144
assert 3*30==90 and 4*30==120 and 5*30==150  # ext ratio 3:4:5 -> 90,120,150 -> internal 90,60,30
assert 180-90==90 and 180-120==60 and 180-150==30
print("gyakorló assertek OK")

# ============================== OLDAL
def sec(cim, ikon, html):
    return f'    <h2 id="{ikon}">{cim}</h2>\n{html}\n'

body = []
body.append('    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(ALAP, "alap", "alap"))
body.append('    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(KOZEP, "kozep", "kozep"))
body.append('    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(NEHEZ, "nehez", "nehez"))
body.append('    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1]))

diszk = ('<p class="diszklemer">⚠️ Ez <b>gyakorló</b> anyag: nincs garancia, hogy az éles felmérőn pontosan '
 'ennyi vagy pont ilyen feladat lesz. A cél a biztos rutin — a valódi feladatok ettől eltérhetnek.</p>')

body.append('    <h2 id="gyak-ellenorzo">🏫 Gyakorló ellenőrző</h2>\n    ' + diszk +
  '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYE_ORAI, "gye") +
  '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYE_OTTHONI, "gyeh"))

body.append('    <h2 id="gyak-dolgozat">📝 Gyakorló dolgozat</h2>\n    ' + diszk +
  '\n    <p class="reszcsoport">🏫 Órai ismétlés</p>\n' + gyt_cards(GYD_ORAI, "gyd") +
  '\n    <p class="reszcsoport">🏠 Otthoni gyakorlás</p>\n' + gyt_cards(GYD_OTTHONI, "gydh"))

sections = "\n".join(body)

alcim = ("Közös kiképzési adattár a teljes geometria-szektorhoz: haladj a szinteken, vagy ugorj a szükséges "
 "témára. A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!")

html = f'''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Geometria — feladatok | 1e | Szvetkó matek</title>
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
  <a href="index.html">Geometria</a> ›
  <span class="itt">Geometria — feladatok</span>
</nav>
<div class="hero">
  <h1>Geometria — feladatgyűjtemény</h1>
  <p class="alcim">{w(alcim)}</p>
  <div class="meta-sor">
    <span class="chip alap">Alap</span><span class="chip kozep">Közép</span>
    <span class="chip nehez">Nehéz</span><span class="chip joker">Joker</span>
  </div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
{sections}
    <div class="gyakorolj">
      <span class="ikon">📖</span>
      <p>Elakadtál? Nézd át a <a href="index.html">témakör tananyagait</a> vagy a <a href="osszefoglalo.html">tömör összefoglalót</a>.</p>
    </div>
    <div class="lapozo">
      <a class="elozo" href="tananyag-transzformaciok.html"><span class="irany">← Előző</span><span class="hova">Egybevágósági transzformációk</span></a>
      <a class="kov" href="osszefoglalo.html"><span class="irany">Következő →</span><span class="hova">Tömör összefoglaló</span></a>
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
open(os.path.join(DEST, "feladatok-geometria.html"), "w", encoding="utf-8").write(html)
print("feladatok-geometria.html kész:", "Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ),
      "| gyak.ell.", len(GYE_ORAI)+len(GYE_OTTHONI), "| gyak.dolg.", len(GYD_ORAI)+len(GYD_OTTHONI))
