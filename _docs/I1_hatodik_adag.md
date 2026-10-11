# I1 — Vektor számszorosa és oszlopdiagram tengelyváltása

## Állapot — 2026-10-11

**I1-10 és I1-16 elkészült és ellenőrizve van. Az I1 jelöltlista 16/16 tétele teljesült.**
Kiindulás: `d6807d8`, tiszta, frissen ellenőrzött helyi `main`, az `origin/main`
ágával azonos. Be nem olvasztott ág nincs. A tanár engedélyével az ellenőrzött
adagot feltöltjük; a tényleges commit és Pages-publikálás az élő állapotnaplóba kerül.

| Jelölt | Lap és vezérlés | Tanulási cél és kimenet |
|---|---|---|
| I1-10 | [Vektor számszorosa](../3e/04-vektorok/tananyag-vektorok-sikban.html#s3): λ = −3…3, negyedegységes lépések; az eredeti vektor rögzített. | A számszoros koordinátái, intenzitása és irányítása együtt változik; a nullvektor is értelmezhető. `MAT.G.SO.O.1.5 (5.1)`. |
| I1-16 | [A diagram függőleges tengelye](../4e/06-valoszinuseg-statisztika/tananyag-adatok.html#s4): választás az eredeti levágott és a nulláról induló oszlopdiagram között. | Azonos adatok eltérő megjelenítésének felismerése; végig látható a tengely kezdete és a valódi százalékos változás. `MAT.V.SO.O.1.9 (9.4)`, kapcsolódó `MAT.SO.O.3.4`. |

A `matematika-3e` és `matematika-4e` skill, valamint a kimenetek az alapok.
A meglévő builderekben csak a kijelölt ábrakártyák változtak; közös SVG- és
tananyagsegéd, két JS-mód, címkézett natív vezérlő, **Kezdőállapot** és élő
szöveges kijelzés készült. Új gyakorlófeladat vagy feladatszámadat nincs.

## Mit mutatnak az ábrák?

- **Vektor:** az eredeti a = (2; 1) végig változatlan; a szaggatott nyíl λa = (2λ; λ). A két nyíl külön kezdőpontból indul, így λ = 1-nél is mindkettő látszik. Rögzített négyzetrács és egységjelölés segít összevetni a hosszakat. A korábbi 2a és −1,5a beállítható. Pozitív szorzónál azonos, negatívnál ellentétes az irányítás; az intenzitás |λ|-szoros. λ = 0-nál a nyíl eltűnik, kör jelöli a nullvektort; a szöveg jelzi, hogy nincs iránya és irányítása.
- **Oszlopdiagram:** a két eredeti SVG és képaláírás megmaradt. Az adatok ugyanabból a meglévő, ellenőrzött forrásból származnak: 141 554 → 123 952; 17 602 fő, 12,4% csökkenés. A levágott tengelynél a látható második oszlopmagasság az első 18,3%-a, miközben a lakosság a 2011-es érték 87,6%-ára csökkent. A nulláról induló tengelynél a magasságarány is 87,6%. A tengelytartomány és a magyarázat minden nézetben látszik. JS nélkül mindkét eredeti diagram olvasható, JS-sel a választott nézet jelenik meg.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | Két builder → képek → média → háttér → naplótérkép → keresőindex; minden lépés sikeres. 334 média 139 lapon. Az ismételt teljes lánc mind a 648 korábbi követett fájlnál bájtazonos. |
| Kánon, linkek, gyakorlósáv | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalásjelzés változatlan. |
| Végleges jsdom | 2 lap, 172 képlet, 4/4 kvíz, 0 hiba. |
| Kulcs és regresszió | 4499 ellenőrzés, 0 eltérés; 4499/4499, 100% érzékenység. SymPy a privát környezetből. |
| Elrendezés | Edge 155.0.4283.45; 360/390/1280 px, kezdő és szélső állapot: 12 nézet, 0 túlcsordulás. A `layout_teszt.py` azonos kiértékelése Node/Edge környezetben; a Python Playwright nincs telepítve. |
| Kezelés | 6 billentyűzetes vezérlőpróba, kezdőállapot-visszaállítások. Mobil emulációban 1 tényleges csúszkatap; a választó érintéses megnyitása és billentyűzetes kiválasztás. |
| Korábbi modellek | Mind a 22 korábbi saját interaktív ábra működéspróbája sikeres. |
| Akadálymentesség | 2 teljes lap axe-próbája: 0 automatikusan jelzett eltérés; nincs JS-, KaTeX-, helyi betöltési hiba vagy konzolfigyelmeztetés. |
| JS nélkül / nyomtatás | A vektor kezdőképe és mindkét eredeti oszlopdiagram látszik; 4 nyomtatási eset JS be/ki. A vezérlők rejtve, az ábrák és állapotuk olvasható. |
| Független matematika | Mind a 25 vektorállapot koordinátái, hossza, előjele, nullvektora és kijelzése; szimbolikus normanégyzet-azonosság SymPy-val. Mindkét tengelybeállítás, mind a 4 oszlop geometriája, adatai és százalékai pontos törtekkel/Decimal-kerekítéssel. 0 eltérés. |
| Szemrevételezés | Mobilos kezdő/szélső ábrák, negatív szorzó és nullvektor, mindkét oszlopdiagram, JS nélküli és nyomtatási mintaképek. |

A kontextus nélküli lektor csak az új ábrák tanulói szövegét kapta;
matematikai hibát nem talált. Két nyelvi pontosítást beépítettem:
„a szaggatott nyíl a λa vektort jelöli”, illetve „a lakosság viszont
a 2011-es érték 87,6%-ára csökkent”. A végleges próbák ezek után futottak.

## Megőrzés és lezárás

308 HTML és 638 korábbi követett fájl bájt szerint változatlan.
32 régi oldalhorgony, 4 kvíz, 5 médiablokk és 5 lenyíló megoldás megmaradt.
A két lap DOM-ja a kijelölt ábrakártyán és hozzá tartozó szkripten kívül azonos.
A 308 nem üres indexbejegyzés közül csak e két URL változott.
Naplótérkép, médiakatalógusok, tükrök és az első 23 zárolt backlog-sor azonos.
A tesztek és függőségek a repón kívül maradtak.

Összesen **24 saját interaktív ábra, 23 működési mód** van
(1e: 4, 2e: 4, 3e: 4, 4e: 12). A matematikai SVG-k száma változatlanul 285:
az oszlopdiagram választója mindkét régi SVG-t megőrzi.
Az **I1 16 jelöltje elkészült**; a négy további GeoGebra-cserejavaslat külön terv.

## Korlátok és tanári döntések

Valódi telefon, képernyőolvasó, más böngésző és teljes PDF-tördelés nem volt
ellenőrizve; külső média új lejátszása nem történt. Az axe nem teljes
akadálymentességi minősítés. A JS nélküli képaláírás képletei TeX-jelöléssel
látszanak, az SVG és a szöveges állapot olvasható. A mobilos választó teljes,
kizárólag érintéses kezelését valódi telefonon nem próbáltam. Új sebességmérés nincs.

**Tanári döntés kell:** nincs az elkészült két modellhez.
