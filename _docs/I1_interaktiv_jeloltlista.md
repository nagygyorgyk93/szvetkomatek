# I1 — Interaktív ábrák jelöltlistája

## Állapot — 2026-10-10

**A négy évfolyam jelöltlistája helyben elkészült.** Kiindulás: `c4059b2`, tiszta
helyi `main`, az `origin/main` helyi referenciájával azonos; távoli frissítés nem történt.
A tanár az I1-listát választotta. A megvalósítás a következő tanári választás után indul.

A 161 tananyaglap ábráinak és médiáinak leltárából **16 jelöltet** választottam,
évfolyamonként négyet. **P1:** elsőként érdemes megvalósítani; **P2:** későbbi,
önállóan is hasznos bővítés. Ez fejlesztési sorrend. A szabványkódban az O/S betű
a tartalom hivatalos szintjét jelöli; a weboldali feladatnehézségről nem hoz új döntést.

## Mi alapján választottam?

- A vezérlő egy meglévő fogalom megértését segítse: arány, előjel, közös pont, megoldáshalmaz vagy közelítés.
- Legyen világos, mit érdemes megfigyelni a mozgatás közben.
- Kis képernyőn kevés, feliratozott vezérlővel legyen kezelhető; csúszka vagy gomb is megfelel.
- A meglévő GeoGebra és saját interaktív ábra szerepét is figyelembe vettem.
- A kimenetek és a szabványok az alapok. A helyi tanári döntések érvényesek: 1e-ben hegyesszögek; a megőrzött 2e-kiegészítések; indukcióhoz csak tananyag és szemléltetés; a 4e kombinatorikai és konvexitási feladatszintek korábbi besorolása.

**Helyi források:** a `svetko-math` matematika-1e/2e/3e/4e skillje és témaköri
referenciái, a szabvanyok skill beolvasott alap- és középszintű kimenetei,
a matek-abra skill; továbbá a jelenlegi HTML, az `interaktiv.js`, a médiaeszköz és
mind a négy médiakatalógus. A listán szereplő konkrét szakaszok szövegét is ellenőriztem.

## Leltár

Csak a tananyaglapok matematikai, `role="img"` jelölésű SVG-it számoltam.
A 286 SVG-ből 8 saját interaktív ábra kezdőképe, 278 állókép. A JPEG-eket
külön átnéztem: a kilenc korábbi kép többnyire mém vagy összefoglaló illusztráció,
a mostani jelöltek meglévő SVG-khez kötődnek.

| Évfolyam | Tananyaglap | Matematikai SVG | Saját interaktív ábra | Aktív GeoGebra | Jelölt |
|---|---:|---:|---:|---:|---:|
| 1e | 38 | 62 | 0 | 10 | 4 |
| 2e | 35 | 31 | 0 | 4 | 4 |
| 3e | 50 | 129 | 0 | 5 | 4 |
| 4e | 38 | 64 | 8 | 5 | 4 |

A GeoGebra-szám az aktív katalógusbejegyzéseket és a helyi HTML-be ágyazott elemeket
jelenti. Az appletek mostani külső működését ebben a dokumentációs adagban nem próbáltam újra.

## Jelöltek évfolyamonként

A link az ábra tényleges tananyagszakaszára vezet. A javasolt vezérlő és a kijelzett
értékek tervként szerepelnek; az új viselkedés még nincs megvalósítva vagy kipróbálva.

### 1e

| Azonosító · sorrend | Lap és meglévő ábra | Mit állítana a vezérlő? | Tanulási haszon | Kimenet |
|---|---|---|---|---|
| **I1-01 · P2** | [A függvény fogalma és megadása](../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggveny-fogalma.html#s1) — Függvény és nem függvény nyíldiagramja | Bemenet és a meglévő két példa kiválasztása; a hozzá tartozó nyilak és képek kiemelése. | Megkülönbözteti a „mindenhez tartozik” és a „pontosan egy tartozik” feltételt. | `MAT.F.SO.O.1.8 (8.1)` |
| **I1-02 · P2** | [Egybevágósági transzformációk](../1e/05-geometria/tananyag-transzformaciok.html#s1) — Eltolt háromszög; később a tükrözés és forgatás ábrája is | Az eltolásvektor két komponense; a többi transzformáció külön nézetben. | Látszik, hogy a hely változik, az oldalak és szögek megmaradnak. | `MAT.G.SO.O.1.5 (5.3)` |
| **I1-03 · P2** | [Lineáris egyenlőtlenségek](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-egyenlotlensegek.html#s2) — Nyílt/zárt határpont és félegyenes | Határpont mozgatása; <, ≤, >, ≥ közötti választás. | Összeköti az egyenlőtlenséget, a számegyenest és az intervallumjelölést. | `MAT.A.SO.O.1.2 (2.2–2.3)` |
| **I1-04 · P1** | [Homotécia és hasonlóság](../1e/08-hasonlosag/tananyag-homotecia-es-hasonlosag.html#s1) — Az O középpontú homotécia | A k arány állítása; megfelelő csúcspárok és sugarak kiemelése. | Együtt követhető a hossz- és kerületarány, valamint a területarány. | `MAT.G.SO.O.1.5 (5.2); MAT.G.SO.S.1.6 (6.2)` |

### 2e

| Azonosító · sorrend | Lap és meglévő ábra | Mit állítana a vezérlő? | Tanulási haszon | Kimenet |
|---|---|---|---|---|
| **I1-05 · P2** | [A komplex szám fogalma](../2e/01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-komplex-szam-fogalma.html#s3) — Komplex szám, konjugált és modulusz a Gauss-síkon | Valós és képzetes rész állítása; a pont és a konjugált együtt mozog. | A szám algebrai alakja, koordinátái, tükrözése és modulusza összekapcsolódik. | `MAT.A.SO.S.1.1 (1.1, 1.5)` |
| **I1-06 · P1** | [Az exponenciális függvény](../2e/03-exponencialis-es-logaritmus-fuggveny/tananyag-exponencialis-fuggveny.html#s2) — Növekvő és csökkenő exponenciális alapgrafikon | Az a alap változtatása a megengedett két tartományban. | Megmutatja a monotonitás különbségét és a közös tengelymetszetet. | `MAT.F.SO.O.1.8 (8.2, 8.4)` |
| **I1-07 · P2** | [Másodfokú és lineáris egyenletből álló rendszer](../2e/02-masodfoku-egyenletek-es-fuggvenyek/tananyag-masodfoku-linearis-rendszer.html#s1) — Parabola és egyenes metszéspontjai | A meglévő parabola mellett az egyenes eltolása; később a meredeksége is. | A rendszer megoldáspárjai közös pontként jelennek meg; látszik a nulla/egy/két megoldás. | `MAT.A.SO.S.1.2 (2.9)` |
| **I1-08 · P1** | [Trigonometrikus egyenletek és egyenlőtlenségek](../2e/04-trigonometrikus-fuggvenyek/tananyag-trigonometrikus-egyenletek.html#s1) — Szinuszgörbe és vízszintes egyenes | A sin x = b egyenlet b értéke; a [0; 2π] intervallum megoldásai kiemelve. | A két gyök, az érintési határeset és a megoldás nélküli eset közvetlenül összevethető. | `MAT.A.SO.S.1.2 (2.4)` |

### 3e

| Azonosító · sorrend | Lap és meglévő ábra | Mit állítana a vezérlő? | Tanulási haszon | Kimenet |
|---|---|---|---|---|
| **I1-09 · P1** | [A gúla és elemei — a három derékszögű háromszög](../3e/01-poliederek/tananyag-gula.html#s2) — Szabályos négyoldalú gúla jelölt szakaszai | Gombokkal külön kiemelhető a három derékszögű háromszög. | Segít megkülönböztetni H, h, s, r és R szerepét, és kiválasztani a megfelelő Pitagorasz-összefüggést. | `MAT.G.SO.S.1.6 (6.2)` |
| **I1-10 · P2** | [Vektorok a síkban — felidézés és szög](../3e/04-vektorok/tananyag-vektorok-sikban.html#s3) — Vektor és számszorosai | A λ szorzó állítása, az eredeti vektor rögzítve. | A hossz és az irányítás változása együtt látható; a λ = 0 eset is értelmezhető. | `MAT.G.SO.O.1.5 (5.1)` |
| **I1-11 · P1** | [Pont és egyenes távolsága — háromszögek koordinátákkal](../3e/05-analitikus-geometria/tananyag-pont-es-egyenes-tavolsaga.html#s1) — Pont, egyenes és merőleges talppont | A pont két koordinátájának állítása; az egyenes és a talppont jelölése követhető. | A képlet értéke és a legrövidebb szakasz ugyanazt a távolságot mutatja. | `MAT.G.SO.S.1.5 (5.3)` |
| **I1-12 · P1** | [A kör és az egyenes — metszéspont és érintő](../3e/05-analitikus-geometria/tananyag-kor-es-egyenes.html#s1) — Szelő, érintő és a kört elkerülő egyenes | Az egyenes eltolása a rögzített kör mellett. | A középpont távolsága és a sugár összehasonlítása összekapcsolódik a közös pontok számával. | `MAT.G.SO.S.1.5 (5.4–5.5)` |

### 4e

| Azonosító · sorrend | Lap és meglévő ábra | Mit állítana a vezérlő? | Tanulási haszon | Kimenet |
|---|---|---|---|---|
| **I1-13 · P1** | [A sorozat határértéke](../4e/01-sorozatok-hatarerteke/tananyag-hatarertek-fogalma.html#s2) — A határértékhez közelítő sorozat pontjai és a körülötte lévő sáv | A sáv ε fél-szélessége és a látható tagok száma. | Látszik, hogyan kerülnek egy indextől kezdve a tagok a szűkebb sávba is. | `MAT.F.SO.S.1.7 (7.3)` |
| **I1-14 · P1** | [A függvény határértéke](../4e/02-fuggvenyek/tananyag-fuggveny-hatarerteke.html#s4) — Eltérő határérték és pontbeli érték: üres/teli pont | Közelítés a megjelölt ponthoz balról vagy jobbról; a pontbeli érték külön jelölve marad. | Elválasztja a közelítés eredményét a függvény adott pontban felvett értékétől. | `MAT.F.SO.S.1.8 (8.1)` |
| **I1-15 · P1** | [A Void kivágása — síkidomok területe](../4e/04-integral/tananyag-terulet.html#s2) — Előjelet váltó görbe alatti két területrész | A jobb integrálási határ állítása; előjeles integrál és geometriai terület egymás mellett. | Megmutatja, miért kell a zérushelynél külön számolni a területet. | `MAT.F.SO.S.1.9 (9.2–9.3)` |
| **I1-16 · P2** | [Adatokból kép — sokaság, minta, gyakoriság, diagram](../4e/06-valoszinuseg-statisztika/tananyag-adatok.html#s4) — Ugyanaz a népességadat normál és levágott tengelyű oszlopdiagramon | Váltás a meglévő két tengelybeállítás között; az adatok és a százalékos változás rögzítve. | A tanuló elkülöníti a valódi változást a megjelenítés okozta benyomástól. | `MAT.V.SO.O.1.9 (9.4); MAT.SO.O.3.4` |

## Javasolt első adag

**I1-04 — homotécia; I1-06 — exponenciális alap; I1-13 — sorozat és ε-sáv.**
Mindhárom egyetlen fő paraméter változását teszi érthetővé, és az adott lapon
nincs ugyanilyen meglévő interaktív modell. A már bevált világos SVG-kártyákhoz
és feliratozott vezérlőkhöz illeszthetők. A homotéciánál a nagyság és az arány,
az exponenciális függvénynél a monotonitás, a sorozatnál a közelítés a lényeg.

A 3e-ből az **I1-09 — gúla három derékszögű háromszöge** jó alternatíva:
gombos kiemelés is elég lehet, teljes térbeli forgatómotor nélkül. Különösen hasznos
ott, ahol a tanuló H, h és s között bizonytalan.

## Meglévő modellekhez kötődő cserejavaslatok

Ezeket külön kell mérlegelni, mert azonos célt szolgáló GeoGebra már van a lapon.
Ha saját változat készül, a tanár választ a két megoldás között.

| Téma | Meglévő hely | Mikor indokolt a saját változat? |
|---|---|---|
| Lineáris függvény: meredekség és tengelymetszet | [1e lineáris függvény](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-linearis-fuggveny.html#s1) | Egységes k/n jelölés, gyors magyar vezérlés és külső betöltés nélküli használat a cél. |
| Másodfokú függvény együtthatói | [2e másodfokú függvény](../2e/02-masodfoku-egyenletek-es-fuggvenyek/tananyag-masodfoku-fuggveny.html#s2) | A csúcspont és a zérushelyek közvetlen jelölése segítene; az a = 0 határesetet külön kell kezelni. |
| Hegyesszög szögfüggvényei | [1e szögfüggvények](../1e/02-trigonometria/tananyag-szogfuggvenyek.html#s2) | Magyar oldalnevek és mind a négy arány — sin, cos, tg, ctg — egyetlen kompakt ábrán. A szög végig hegyesszög. |
| Vektorösszeadás | [1e vektorok](../1e/05-geometria/tananyag-vektorok.html#s2), [3e vektorok](../3e/04-vektorok/tananyag-vektorok-sikban.html#s2) | Ugyanaz a magyar modul mindkét évfolyamon, képernyőolvasóval is követhető koordinátákkal és eredővel. |

Az I1-10 a **skalárral szorzásra**, az I1-05 a **konjugálásra** irányul;
a vektor- és komplexszám-összeadási appletek más műveletet mutatnak.
Az I1-15 az **előjeles integrál és a geometriai terület eltérését** mutatná;
a meglévő pozitív görbe alatti téglalapos közelítés más kérdést szemléltet.

## Ami már saját interaktív ábra

A 4e-ben a szelő/derivált, monotonitás/érintő, konvexitás, primitív függvénysereg,
téglalapos integrálközelítés, Pascal-háromszög, érme- és kockaszimulátor, valamint
adatlabor már működő saját modell. A két érintős ábra azonos módra épül:
**nyolc ábra, hét működési mód**. A jelöltlista ezeket meglévő lefedettségként kezeli.

A szinusz/koszinusz egységkörből való kirajzolása, az ellipszis és a parabola
mértani helye, valamint a láncszabály és a felhalmozási függvény meglévő GeoGebra-modellje
szintén figyelembe véve. Az indukciónál a tanári korlát továbbra is csak tananyag
és szemléltető példa; új gyakorló vagy pontozott feladat nem része a listának.

## Megvalósításkor ellenőrizendő

- **Minden jelölt:** a meglévő SVG az értelmes kezdőállapot JS nélkül; világos kártya, sötét tinta, a kánon jelölései. Billentyűzetről és érintéssel is működő, feliratozott vezérlők; a számértékek szövegesen is elérhetők.
- **I1-03:** a határpont nyitottsága és az intervallumjelölés egyezzen; a végtelen mindig nyílt végpont.
- **I1-04:** k = 0 nem homotécia. Negatív k esetén a szakaszhosszak aránya |k|, a területarány k²; a pontok az O másik oldalára kerülnek. A lecke már tárgyalja a negatív esetet.
- **I1-06:** a > 0, a ≠ 1; a két oldalt jól megkülönböztető vezérlés, érvénytelen alap nélkül. Az alapgrafikon az első cél.
- **I1-07/I1-12:** érintésnél egy közös pont legyen; a számítás és a rajz egyformán kezelje a nulla/egy/két metszéspontot. Függőleges egyenes támogatásánál se legyen nullával osztás.
- **I1-08:** a [0; 2π] két végpontját következetesen kezelje; a határesetben összeeső gyökök ne szerepeljenek kétszer. Az intervallum az x értékeire vonatkozik. Elsőként az alap sin x = b ábra készülhet; a cos, az ax és az egyenlőtlenség külön bővítés.
- **I1-10/I1-11:** a nullvektor és a pont egyenesre kerülése is értelmes állapot legyen. A pont–egyenes távolságot a szabvány kéri; a normálalak tanítását nem igényli.
- **I1-13:** ε > 0; a sáv határán álló pont ne számítson belső pontnak. A kijelzett indextől valóban minden további tag a sávban legyen. Ez szemléltetés, definíció szerinti bizonyítási feladatsor nélkül.
- **I1-14:** az üres és teli pont végig külön jelentést hordozzon; a pontbeli érték ne változzon a közelítés közben.
- **I1-15:** a terület nemnegatív; az előjeles integrál kioltása és a részek területe legyen külön látható és megnevezett.
- **I1-16:** a forrásadatok és a számított százalék végig azonos; a tengely kezdőértéke mindig látszik, a levágást szöveges magyarázat kíséri.

A builderben vagy az oldal saját forrásában történő megvalósítás után a szokásos
kép/média/háttér, kánon/render, link/sáv és mobil/nyomtatási ellenőrzés szükséges.
Új feladatszámadat csak a privát ütközésellenőrzés mellett készülhet.
A közös modul számítása és a kijelzett értékek független matematikai kontrollt kapjanak.

## Ellenőrzés és korlát

Ez dokumentációs adag: a weboldal működése és tanulói tartalma megmaradt.
A 16 célhelyhez létező tananyag, szakaszhorgony és állókép tartozik; mindegyiknél
összevetettem a saját interaktív ábrát és az aktív médiakatalógust.
A kimenetkódok a beolvasott szabványreferenciákból származnak.
A dokumentáció 21 belső linkje és horgonya hibátlan; 12 különböző kimenetkód
és a hivatkozott al-pontok ellenőrizve. 639 korábbi követett fájl változatlan,
köztük mind a 310 weboldali HTML byte szerint azonos. A zárolt első 23 backlog-sor megmaradt.

Az új modellek mobilos és billentyűzetes viselkedése, matematikai szélső esetei,
külső appletek jelenlegi működése és a képernyőolvasós eredmény a megvalósításkor,
illetve a célzott próba során lesz ellenőrizhető.

**Tanári döntés kell:** melyik 2–3 jelölt induljon elsőként? Javaslat: I1-04, I1-06,
I1-13. A meglévő GeoGebra cseréjéről külön választás szükséges, ha ilyen tétel kerül sorra.
Helyi `main`, új ág és push nélkül.
