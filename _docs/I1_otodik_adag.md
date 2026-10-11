# I1 — Az 1e három további interaktív ábrája

## Állapot — 2026-10-11

**I1-01, I1-02 és I1-03 elkészült és ellenőrizve van.** Kiindulás: `3ba00b0`,
tiszta, frissen ellenőrzött helyi `main`, az `origin/main` ágával azonos.
Be nem olvasztott ág nincs. A tanár engedélyével a lezárt, ellenőrzött adagot
feltöltjük; a tényleges commit és Pages-publikálás az élő állapotnaplóba kerül.
Az I1-listából **14/16 jelölt kész; I1-10 és I1-16 maradt**.

| Jelölt | Lap és vezérlés | Tanulási cél és kimenet |
|---|---|---|
| I1-01 | [Függvény fogalma](../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggveny-fogalma.html#s1): a két meglévő hozzárendelés és az 1/2/3 bemenet kiválasztása. | Minden bemenethez pontosan egy kép; a teljes hozzárendelés minősítése független a kiemelt elemtől. `MAT.F.SO.O.1.8 (8.1)`. |
| I1-02 | [Eltolás](../1e/05-geometria/tananyag-transzformaciok.html#s1): vízszintesen −5–5, függőlegesen −3–3 egység, 0,2-es lépéssel. | Minden pont ugyanazzal a vektorral mozdul; hossz, szög és körüljárás megmarad. `MAT.G.SO.O.1.5 (5.3)`. |
| I1-03 | [Egyenlőtlenségek](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-egyenlotlensegek.html#s2): a határpont −4–4 negyedegységgel, négy relációjel. | Az egyenlőtlenség, a félegyenes és az intervallumjelölés összekapcsolása. `MAT.A.SO.O.1.2 (2.2–2.3)`. |

A `matematika-1e` skill és a kimenetek az alapok. A három kézzel migrált
oldalon egy új, ismételhető beillesztőeszköz csak a kiválasztott ábrakártyát
cseréli. Közös SVG-generátorok és tananyagsegédek, három közös JS-mód,
címkézett natív vezérlők, **Kezdőállapot** és élő szöveges kijelzés készült.
Új gyakorlófeladat vagy feladatszámadat nincs.

## Megfigyelhető határesetek

- **Nyíldiagram:** a függvényben 1→a, 2→b, 3→b; c egyik bemenetnek sem képe. A másik hozzárendelésben 1→a és 1→b, a 2-höz semmi, 3→c. A teljes hozzárendelés ettől nem függvény akkor sem, ha a 3 bemenetet emeljük ki. A kiemelt nyilak erősebbek és folytonosak, a többi szaggatott. JS nélkül a függvény kezdőképe látszik; mindkét eset leírása olvasható. A két régi képaláírás-horgony megmaradt.
- **Eltolás:** a háromszög eredeti alakja és a jobbra/lefelé mutató kezdő eltolása megmaradt. A kitöltött eredeti és a szaggatott kép különbözik; rögzített négyzetrács és egységjelölés. A nullvektornál minden pont helyben marad, a nulla hosszú nyilak rejtve vannak. Minden beállítás a rajzkereten belül marad. A tükrözés és forgatás meglévő ábrái változatlanok.
- **Félegyenes:** x>2 a kezdőállapot. A relációjel szerint balra/jobbra fordul a nyíl, nyílt/zárt a határpont és a megfelelő véges intervallumvég. A végtelen vég mindig nyílt. A másik két eredeti számegyenes és a lenyíló megoldás változatlan; a felirat tisztázza, hogy ezek az eredeti példákra vonatkoznak.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | Beillesztőeszköz → képek → média → háttér → naplótérkép → keresőindex; minden lépés sikeres. 334 média 139 lapon. Az ismételt teljes lánc bájtazonos. |
| Kánon, linkek, gyakorlósáv | 310 oldal, 0 hiba. Két korábbi heurisztikus visszautalásjelzés változatlan. |
| Végleges jsdom | 3 lap, 151 képlet, 6/6 kvíz, 0 hiba. |
| Kulcs és regresszió | 4499 ellenőrzés, 0 eltérés; 4499/4499, 100% érzékenység. SymPy a privát környezetből. |
| Elrendezés | Edge 155.0.4283.45; 360/390/1280 px, kezdő és szélső állapot: 18 nézet, 0 túlcsordulás. A `layout_teszt.py` azonos kiértékelése Node/Edge környezetben; a Python Playwright nincs telepítve. |
| Kezelés | 18 billentyűzetes vezérlőpróba, kezdőállapot-visszaállítások; 3 tényleges érintéses csúszkatap emulált mobilnézetben. 3 választónál érintéses megnyitás és billentyűzetes választás. |
| Korábbi modellek | Mind a 19 korábbi saját interaktív ábra működéspróbája sikeres. |
| Akadálymentesség | 3 teljes lap axe-próbája: 0 automatikusan jelzett eltérés; nincs JS-, KaTeX-, helyi betöltési hiba vagy konzolfigyelmeztetés. |
| JS nélkül / nyomtatás | 3 statikus kezdőkép és állapot; 6 nyomtatási eset JS be/ki. A vezérlők rejtve, az ábra és állapot olvasható. |
| Független matematika | Mind a 6 hozzárendelés/bemenet állapot; 1581 eltolás pontos törtekkel, ponthelyzetekkel, oldalakkal és előjeles területtel; 132 egyenlőtlenség SymPy-megoldáshalmazzal, határponttal, iránnyal és kijelzéssel. 0 eltérés. |
| Szemrevételezés | Mobilos kezdő/szélső ábrák, hiányzó és kétértékű kép, nullvektor, kis és negatív eltolás, negatív nyílt/zárt határpont, JS nélküli és nyomtatási mintaképek. |

A kontextus nélküli lektor az új ábrák tanulói szövegét matematikailag
helyesnek találta. Két nyelvi pontosítást beépítettem: „c egyik bemenetnek
sem képe”, valamint a teli karika a határpont megoldásszerepét jelzi.
Az új beillesztőeszköz ismétléskor kezdetben megkettőzte a közös szkriptet,
mert az ellenőrzési lánc `defer` jelöléssel látja el. Javítva; a végleges
ismétlés minden 646 korábbi követett fájlnál bájtazonos.

## Megőrzés és folytatás

307 HTML és 637 korábbi követett fájl bájt szerint változatlan.
48 régi oldalhorgony, 6 kvíz, 9 médiablokk és 3 lenyíló megoldás megmaradt.
A három lap DOM-ja a kiválasztott ábrakártyán és hozzá tartozó szkripten
kívül azonos. A 308 nem üres indexbejegyzés közül csak e három URL változott.
Naplótérkép, médiakatalógusok, tükrök és az első 23 zárolt backlog-sor azonos.
A tesztek és függőségek a repón kívül maradtak.

Összesen **22 saját interaktív ábra, 21 működési mód** van
(1e: 4, 2e: 4, 3e: 3, 4e: 11). A matematikai SVG-k száma 286→285:
a két nyíldiagram egy választható ábrává vált, mindkét hozzárendelés megmaradt.
Hátravan **I1-10 (vektor számszorosa)** és **I1-16 (oszlopdiagram tengelye)**.
A négy további GeoGebra-cserejavaslat külön terv.

## Korlátok és tanári döntések

Valódi telefon, képernyőolvasó, más böngésző és teljes PDF-tördelés nem volt
ellenőrizve; külső média új lejátszása nem történt. Az axe nem teljes
akadálymentességi minősítés. A JS nélküli képaláírás képletei TeX-jelöléssel
látszanak, a kezdőkép és szöveges állapot olvasható. A mobilos választók
teljes érintéses kezelését valódi telefonon nem próbáltam. Új sebességmérés nincs.

**Tanári döntés kell:** nincs az elkészült három modellhez.
