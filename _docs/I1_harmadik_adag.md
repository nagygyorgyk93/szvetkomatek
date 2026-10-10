# I1 — Határérték és előjeles terület a 4e-ben

## Állapot — 2026-10-10

**I1-14 és I1-15 helyben elkészült.** A tanár folytatási kérésére a két
fennmaradó 4e P1-modellt készítettem el. Kiindulás: `2d554dd`, tiszta helyi
`main`, azonos tárolt `origin/main`; távoli frissítés nem történt.
Új ág és push nincs. Az I1-listából **8/16 modell kész, 8 terv maradt**.

| Jelölt | Lap és vezérlés | Mit figyelhet meg a tanuló? |
|---|---|---|
| I1-14 | [A függvény határértéke](../4e/02-fuggvenyek/tananyag-fuggveny-hatarerteke.html#s4): bal/jobb oldali közelítés, az x távolsága a 2-től 1; 0,1; 0,01; 0,001. | A közelítő pont a 2 magasságú lyukhoz tart, miközben a pontbeli érték g(2) = 1 végig rögzített. |
| I1-15 | [Előjelváltó görbe és terület](../4e/04-integral/tananyag-terulet.html#s2): a jobb határ b = 0–6, negyedegységes lépéssel. | A tengely alatti és fölötti rész, az előjeles integrál, a teljes geometriai terület és az integrál abszolút értéke együtt változik. |

A `matematika-4e` skill és a középszintű kimenetek az alapok:
`MAT.F.SO.S.1.8 (8.1)` és `MAT.F.SO.S.1.9 (9.2–9.3)`.
A két modell a lapon már szereplő példát használja. Új gyakorlófeladat vagy
feladatszámadat nem került be. A pozitív görbe alatti téglalapos közelítés és
a GeoGebra más célt szolgál; ezek megmaradtak.

Közös világos SVG-kártya, címkézett natív vezérlők, **Kezdőállapot** gomb és
élő szöveges állapot készült, külső könyvtár nélkül. JS nélkül a statikus
kezdőkép és a számszerű állapot olvasható. A képletet tartalmazó caption ilyenkor
TeX-jelöléssel jelenik meg, mert a közös képletrenderhez JS szükséges.
Nyomtatáskor a vezérlők rejtve vannak, az ábra és a kijelzett állapot megmarad.

### Matematikai határesetek

- **Határérték:** g(x) = 4 − x, ha x ≠ 2; g(2) = 1. A távolság mindig pozitív, így a közelítő pont soha nem kerül a kivételes helyre. Mindkét oldali határérték 2. A rögzített lyuk a mozgó pont fölé kerül a rajzban; nagyon kis távolságnál a pontok vizuálisan összemosódhatnak. Ezt a caption kimondja, és a kijelző külön megadja a koordinátákat.
- **Terület:** f(x) = x² − 4x rögzített. A kezdő b = 5 az eredeti szöveges példa, melynek megoldása változatlan. Az állítható felső határ csak a szemléltetésé. A kijelző az egész számos bemenetből pontos, egyszerűsített törteket ad, kerekítés nélkül. A görbe a rajzablakban van vágva; a függvényérték nem lapul el a szélén.

| Jobb határ b | Előjeles integrál | Geometriai terület |
|---:|---:|---:|
| 0 | 0 | 0 |
| 4 | −32/3 | 32/3 |
| 5 | −25/3 | 13 |
| 6 | 0 | 64/3 |

Az utolsó állás jól mutatja a teljes kioltást: az integrál nulla, a két
területrész mégis egyenként 32/3, összegük 64/3. A színezés mellett szöveg is
megnevezi a részeket. A jobb határt szaggatott egyenes jelöli.

## Lektori és megjelenítési javítások

A kontextus nélküli lektor csak a két tanulói szöveget kapta. A példákat és
az öt kvízválaszt újraszámolta; minden számszerű eredmény helyes.
Hibatábla után a következő pontosítások kerültek a builderekbe:

| Hol | Mi változott? |
|---|---|
| Határérték bevezetője | A „Dehogynem” helyett „Attól még lehet határérték”. |
| Szemléletes meghatározás | Kimondja, hogy minden elég közeli, a-tól különböző x-re vonatkozik. |
| Folytonosság és pontbeli érték | Két külön mondat: a folytonossági pontokban egyenlők; más pontokban eltérhetnek. |
| Egyoldali határérték képaláírása | „Jobbról a 0-ból indul” helyett „jobbról közelítve a 0-hoz tart”. |
| Integrál ismétlője | A helyettesítési képlet mellett szerepel az a ≠ 0 feltétel. |
| Előjeles integrál csapdadoboza és kvízvisszajelzése | Részleges vagy teljes kioltás; a kvíz kérdése, válaszai és helyes opciója változatlan. |
| Új vezérlő címkéje | „Az x távolsága a 2-től”. |
| Területábra b felirata | A korábbi helyen b = 4,25-nél a végponttal, 0/4/4,25-nél a görbével ütközött. A végleges felső sávban mind a 25 állásban elkerüli a görbét, a végpontot és a többi feliratot. |

A lektor a módosításokat visszaellenőrizte; az utolsó kétértelmű mondat
szétválasztását és a szaggatott határvonal captionjét is helyesnek találta.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | Két saját builder → képek → média → háttér → naplótérkép → keresőindex, minden lépés sikeres; 334 aktív média 139 lapon. |
| Kánon, belső link, gyakorlósáv | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalás-jelzés változatlan. |
| Végleges jsdom-render | Két lap, 212 képlet, 5/5 kvíz, 0 hiba. |
| Kulcs és regresszió | 4499 kulcsellenőrzés, 0 eltérés; 4499/4499, 100% regressziós érzékenység. A SymPy a korábbi privát környezetből futott. |
| Elrendezés | Edge 154.0.4258.62; két modell × 360/390/1280 px × kezdő/szélső állapot = 12 nézet, 0 túlcsordulás. |
| Kezelés | 9 billentyűzetes próba és visszaállítások; 2 tényleges érintéses csúszkapróba. A natív választó érintéssel nyílt, kiválasztása billentyűzettel történt. Mind a 14 korábbi saját modell működéspróbája sikeres. |
| Akadálymentesség | Két teljes lap axe-próbája: 0 automatikusan jelzett eltérés. Nincs JS-, helyi betöltési vagy KaTeX-hiba, illetve konzolfigyelmeztetés. |
| JS nélkül és nyomtatás | Két statikus kezdőkép és állapot olvasható; 4 nyomtatási eset JS be/ki sikeres, a vezérlők rejtve vannak. |
| Független matematika | 8 közelítő pont, a rögzített lyuk és pontbeli érték; 25 jobbhatár-állás külön SymPy-integrálással. Minden pontkoordináta, törtkijelzés, részintegrál, terület és összehasonlítás helyes. |
| Tényleges SVG-geometria | A rögzített görbe 241 pontja és állásonként két 123 pontos területpoligon ellenőrizve. A poligon területének legnagyobb eltérése 0,00073 alatt; a kijelző pontos törteket ad. A feliratpróba 25/25 ütközésmentes. |

A SymPy közvetlen Piecewise-limitje az elszigetelt pontbeli ágat választotta.
A független kontroll ezért pozitív d távolsággal x = 2 ± d helyettesítést használ,
majd d → 0 határértéket számol. Ez a privát ellenőrzés technikai korrekciója;
a weboldali modell számítása változatlanul helyes.

Kezdő-, szélső, közeli közelítési, b = 0/4/4,25/5/6, nyomtatási és JS nélküli
képek szemrevételezve. Új teljesítménymérés nem indult.

### Megőrzés

**308 HTML és 634 korábbi követett fájl byte szerint változatlan.** A két lap
az új ábrákon és a tételesen jelzett pontosításokon kívül azonos DOM-ot ad.
A 32 korábbi, SVG-n kívüli oldalhorgony, az 5 kvíz kérdése/válasza és a
meglévő példák számszerű eredménye megmaradt. Egy kvíz sikeres visszajelzése
nyelvileg pontosabb lett. A média és a többi ábra megmaradt.
A 308 bejegyzéses keresőindexben csak a két érintett URL változott.
Naplótérkép, médiakatalógusok, tükrök és a backlog első 23 zárolt sora azonosak.
Nyers próbák és függőségek a repón kívül maradtak.

## Korlát és következő lépés

Élő publikált oldal, valódi telefon/képernyőolvasó, más böngésző,
teljes PDF-tördelés és külső média új lejátszása ebben az adagban nincs
ellenőrizve. A mobilpróba helyi Edge-emuláció; az axe nem teljes WCAG-minősítés.

**Tanári döntés kell:** az elkészült két modellhez nincs.
A további 8 jelölt a [jelöltlistán](I1_interaktiv_jeloltlista.md) maradt.
Összesen 16 saját interaktív ábra van: 1e 1, 2e 1, 3e 3, 4e 11; 15 működési mód.
Helyi `main`, új ág és push nélkül.
