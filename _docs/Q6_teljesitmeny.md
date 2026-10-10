# Q6 — Teljesítménymérés és betöltés

## Állapot — 2026-10-10

**A második adag helyben elkészült; a Q6 részben kész.** A betűcsere okozta
elmozdulás a hét mintalap mobilos mediánjában csökkent. Az első megjelenés és a
betöltési idő több helyen kedvezőtlenebb lett, ezért további gyorsítás szükséges.
Kiindulás: `27b5de2`, tiszta `main`, az `origin/main` helyi referenciájával azonos;
távoli frissítés nem történt. Új ág és push nélkül.

## Második adag — betűcsere és mobilfejléc, 2026-10-09–10

### Hibatábla és végleges változtatások

A hibatábla javítás előtt bemutatva; a mérési próbák után csak az igazolt,
közös CSS-módosítás maradt meg.

| Hol | Hiba vagy hiány | Súlyosság | Javítás módja |
|---|---|---|---|
| Fejléc, morzsasor, cím és bevezető | A tartalék és a végleges betűk eltérő mérete miatt a sorok betöltés közben újratördelődtek. | közepes | Öt helyi Arial-tartalék a közös CSS-ben, az Inter 400/600/700 és a Space Grotesk 500/700 méreteihez igazítva. |
| Telefonos fejléc | A logó egysoros állapota a fontcsere és a naplójelző környékén két sorra törhetett; a rövid osztályoldalon ez jól látszott. | közepes | Legfeljebb 520 px-en a logónév eleve két sorra foglal helyet; nincs oldalankénti kivétel. |
| Betöltés | Az előtöltés és az első megjelenés korábbi kedvezőtlen mutatói nem oldódtak meg minden lapon. | közepes, nyitott | Összehasonlító mérés; az általános javulást nem igazoló előtöltés-módosítások visszavonva. |

A `size-adjust` és a sormagasságot meghatározó metrikák a tartalék betű megjelenését közelítik
a webfontéhoz. A beállítás csak a `.fejlec`, `.morzsa` és `.hero` területre terjed ki.
A `font-display:swap` megtartja a betűcsere lehetőségét. Technikai alap:
[MDN — size-adjust](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust),
[MDN — font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display).

Az öt tartalék 56 186 karakter meglévő cím- és bevezetőszövegének Canvas-mérése
alapján készült. Helyi betűforrás, új letöltés nincs. Ha az Arial nem érhető el,
a meglévő rendszerbetűs tartalék marad; ennek telefonos viselkedése nincs megmérve.
A teljes folyószövegre kiterjesztett tartalék és a hat helyett négy márkafont-előtöltés
próbája visszavonva. **A végleges változás kizárólag a közös CSS-ben van.**
A betűfájlok, a hat márkafont- és a két KaTeX-előtöltés, a betöltési generátor és a
szkriptek változatlanok. KaTeX-lusta renderelés nem került be.

### Végleges összehasonlító mérés

Edge 154.0.4258.62, valódi helyi HTTP/gzip, 600 másodperces gyorsítótár;
a teljesítménymérésben nincs Playwright-kérésátirányítás. Mobil: 390 × 900 px,
1-es pixelsűrűség, négyszeres CPU-lassítás, 150 ms késleltetés, 200 000 byte/s.
Hét minta, három üres/meleg gyorsítótáras kör változatonként; asztal: 1280 × 900 px,
lassítás nélkül egy kör mintánként. Régi/új sorrend körönként váltva.
**49 + 49 = 98 futás, 0 betöltési, JS- vagy KaTeX-renderhiba.**
Az alábbi „előtte” az első adag lezárt `27b5de2` forrása, az „utána” a mostani CSS;
a 310 HTML byte szerint azonos.

Mobil, üres gyorsítótár, három futás mediánja. Az első megjelenés FCP;
a „betöltés + napló” a load esemény és az elérhető naplómodul együtt, nem a teljes
felület használhatóságának mérése. A CLS a felhasználói beavatkozás nélküli
elmozdulások legnagyobb munkameneti összege; mértékegység nélküli.

| Minta | Első megjelenés, s: előtte → utána | Betöltés + napló, s: előtte → utána | CLS: előtte → utána |
|---|---|---|---|
| Főoldal | 2,08 → 2,26 | 3,74 → 3,93 | 0,1475 → 0,0373 |
| 3e osztályoldal | 1,14 → 1,37 | 2,76 → 2,91 | 0,0254 → 0,0002 |
| 1e: tautológiák, következtetések, kvantorok | 3,25 → 3,21 | 7,15 → 5,79 | 0,2645 → 0,0267 |
| 2e: hatványfüggvény | 2,40 → 2,94 | 5,93 → 7,03 | 0,0051 → 0,0032 |
| 4e: határozott integrál feladatgyűjtemény | 2,42 → 2,38 | 9,02 → 7,52 | 0,1896 → 0,0842 |
| 4e: binomiális valószínűség | 2,76 → 2,80 | 5,44 → 5,99 | 0,1254 → 0,0604 |
| Kereső: „derivált” | 1,01 → 1,06 | 2,80 → 2,90 | 0,0008 → 0,0005 |

Az 1e hosszú című lapján a CLS-medián körülbelül **90%-kal**, a főoldalon 75%-kal,
az integrálos feladatlapnál 56%-kal csökkent. Nem minden egyedi futás lett kedvezőbb.
Meleg gyorsítótárral a betöltés + napló mediánja hat mintán javult; az integrálos
lap 5,81 → 4,38 s, a 2e hatványfüggvény viszont 2,70 → 2,79 s.

**A 2e hatványfüggvény hideg betöltése és első megjelenése lassabb lett a mérésben.**
Más minták első megjelenése is vegyes. A futások szórása jelentős: az 1e mintán
az FCP előtte 2,22–3,86 s, utána 1,88–4,03 s volt. A hét mintából nem állapítható
meg minden oldalra érvényes gyorsulás. Ez helyi összehasonlítás, nem terepi
Core Web Vitals-minősítés. A főoldali videó folyamatban lévő adatátviteléből nem
számoltam teljes hálózati forgalmat.

### Végleges ellenőrzés és megőrzés

| Próba | Eredmény |
|---|---|
| Háttér/betöltési generátor | Dry run: 0 háttér- és betöltésijelzés-változás; 310 oldal idempotens. |
| Kánon, belső link, gyakorlósáv | 310/0 hiba, sáv tiszta; két korábbi heurisztikus visszautalás-figyelmeztetés. |
| Teljes oldalkészlet, Edge 390 px | 310 oldal, 0 túlcsordulás, KaTeX-render-, JS- vagy helyi fájlhiba; naplójelző, kvízek, interaktív ábrák, tartalomjegyzék-horgonyok ellenőrizve. |
| Mobil/asztali megjelenés | 15 mintalap × 360/390/1280 px = 45 nézet/0; nyitott válaszok és fókuszolható széles képletek is. |
| Kezelés | 82 általános + 13 célzott sikeres próba, hét interaktív mód. |
| Késleltetett fejléc | 360 és 390 px-en a naplójelző betöltése előtti/utáni fejlécmagasság azonos; a napló megelőzi a látványmodult. |
| Képek és JS nélkül | Kilenc kép betöltve, natív méret/alternatív szöveg azonos; két tananyag képe JS nélkül és nyomtatásban is látható. |
| Médiafelület | Indítás, bezárás és fókusz-visszaadás sikeres, helyi próbakerettel; külső lejátszás nem vizsgálva. |
| Akadálymentesség és nyomtatás | 5 axe-próba/0 jelzés; 15 nyomtatási nézet JS-sel, 2 JS nélkül sikeres. |
| Megőrzés | 736 további forrásfájl változatlan, köztük mind a 310 HTML; a zárolt első 23 backlog-sor azonos. CSS-változás pontosan az öt tartalék, a három felső terület és a mobil logó. |

A végleges főoldali és 3e-fejléc 390 px-es képe szemrevételezve: a kétsoros logó,
a naplójelző és a keresőgomb elfér. A túlcsorduláspróba a `layout_teszt.py` aktuális,
forrásból ellenőrzött kifejezését használja. A mérési források hash-e a teljes
böngészőpróba és a célzott ellenőrzés után is egyezik.

A halmazfogalom lapon 8 korábbi KaTeX-konzolfigyelmeztetés maradt a képletbe tett
magyar idézőjel miatt; nincs képletrajzolási hibajelző. A két kánonfigyelmeztetés
az exponenciális függvény és a radián tananyagának korábbi visszautalása.
Új ilyen figyelmeztetés nincs. A nyers eredmények és a visszavont próbák privátak.

Tanulói szöveg, feladat, számadat, végeredmény, SVG, kvíz, kép, média,
naplókód/térkép, keresőindex, builder és tükör nem változott. Újraépítés,
matematikai kulcs/regresszió és új szöveglektor ehhez a CSS-adaghoz nem kellett;
a működést valódi böngészővel ellenőriztem.

### Hátra és korlát

- Első megjelenés és a betöltés CPU-költségének következő vizsgálata; különösen a 2e hatványfüggvény kedvezőtlen mutatói.
- Az 1e/01 halmazfogalom idézőjeleinek korábbi KaTeX-figyelmeztetése.
- Élő GitHub Pages, valódi telefon, más böngésző és képernyőolvasó nincs ellenőrizve. Az Arial nélküli telefonos betűcsere külön mérendő.
- Az axe nem teljes WCAG-minősítés, a nyomtatási próba nem teljes PDF-tördelés; külső videó/applet lejátszási és tartalmi próbája nem történt.

**Tanári döntés kell:** az elkészült CSS-adaghoz nincs. Helyi `main`, push nélkül;
a Q6 további gyorsítást igényel.

## Első adag — 2026-10-09 (korábbi, lezárt mérési állapot)

Az alábbi táblázat az első adag előtti és utáni forrásokat hasonlítja össze;
a második adag eredményei a fenti szakaszban szerepelnek.

### Állapot — 2026-10-09

**Az első gyorsítási adag helyben elkészült.** Kiindulás: `940ad04`, tiszta `main`,
az `origin/main` helyi referenciájával azonos; távoli frissítés nem történt.
Új ág és push nélkül. A Q6 részben kész marad: az első megjelenés és a betűcsere
okozta elmozdulások további finomítást igényelnek.

### Hibatábla és változtatások

| Hol | Hiba vagy hiány | Súlyosság | Javítás módja |
|---|---|---|---|
| Közös felület, hosszú feladatlapok | Méretolvasás és attribútumírás keveredett; a zárt válaszok belsejének mérése is új elrendezést kényszerített ki. | közepes | `ui.js`: előbb olvasás, utána jelölés; események összevonása képkockánként; rejtett tartalom csak megnyitáskor mérve. |
| 1e/01 hét régi tananyaga | Kilenc JPEG közvetlenül a HTML-ben, képméret nélkül szerepelt. | közepes | Változatlan képfájlok, valódi szélesség/magasság, lazy betöltés, async dekódolás. Ezek kézzel migrált lapok, megfelelő builder nincs. |
| Betűkészletek | A két latin fájl előtöltése a magyar karakterek későbbi cseréjét és a sorrendet nem rendezte. | közepes | Mérési próba alapján Inter 400/700 és Space Grotesk 700 alap és ékezetes készlete együtt; KaTeX-stílusú lapon Main Regular és Math Italic is. |
| Rövid kereső/listaoldalak | Az előtöltés késleltette az első megjelenést. | alacsony | Ezeken nincs külön font-előtöltés; a meglévő `font-display:swap` dolgozik. |
| Kezelőszkriptek | A HTML feldolgozását blokkolták; a dinamikus modulok sorrendjét a korábbi defer nem biztosította. | alacsony | Biztonságos helyi szkriptlista és defer, KaTeX/inline render változatlan. A napló, látvány és média dinamikus moduljai sorrendben indulnak. |

A `_tools/betoltes.py` csak a saját jelölt fejlécblokkját és az ismert szkriptek
attribútumát kezeli. A `set_hatter.py` az újraépítési láncban ezt is meghívja.
Újrafuttatva 0 változás. A `CLAUDE.md` eszköz- és láncleírása frissült.
295 KaTeX-stílusú lap és a főoldal kap font-előtöltést; 14 rövid oldal külön blokk nélkül.
Összesen 585 szkript kapott új defer jelzést, a korábbi egy megmaradt.

A kilenc JPEG 350 969 byte, tartalma és alternatív szövege változatlan.
A base64 kivétele önmagában 467 160 byte-tal rövidítette a hét HTML-t;
az új fejlécjelzésekkel együtt a nettó csökkenés **459 712 byte**.
Érintett tananyagok: Descartes-szorzat/relációk, függvénytulajdonságok,
halmazfogalom, halmazműveletek, kompozíció/inverz, következtetések/kvantorok,
logikai műveletek. A fájlok az `assets/img/tananyag/1e01/` mappában vannak.

### Mérés

Playwright, Edge 154.0.4258.62, valódi helyi HTTP, gzip, 600 másodperces gyorsítótár.
Mobil: 390 × 900 px, 1-es pixelsűrűség, négyszeres CPU-lassítás, 150 ms hálózati
késleltetés, 200 000 byte/s. Hét mintalap, három külön böngészőkörnyezetben először
üres, majd meleg gyorsítótár. Asztal: 1280 × 900 px, lassítás nélkül, egy futás/minta.
**Előtte 49 és a végleges forrásokon utána 49 futás, 0 betöltési/JS/KaTeX-renderhiba.**

Mobilos mediánok három futásból. Az első megjelenés a böngésző FCP-je.
A „betöltés + napló” pontnál a betöltési esemény lefutott és a közös naplómodul elérhető.
A CLS a felhasználói beavatkozás nélküli elmozdulások legnagyobb munkameneti összege.
Ez helyi összehasonlítás, nem terepi Core Web Vitals-minősítés.

| Minta | Első megjelenés, s: előtte → utána | Betöltés + napló, s: előtte → utána | CLS: előtte → utána |
|---|---|---|---|
| Főoldal | 1,80 → 2,27 | 4,51 → 3,83 | 0,400 → 0,148 |
| 3e osztályoldal | 1,09 → 1,23 | 2,51 → 2,77 | 0,026 → 0,026 |
| 1e: tautológiák, következtetések, kvantorok | 2,92 → 3,28 | 10,21 → 6,18 | 0,264 → 0,264 |
| 2e: hatványfüggvény | 2,22 → 2,61 | 10,32 → 6,74 | 0,012 → 0,005 |
| 4e: határozott integrál feladatgyűjtemény | 1,66 → 2,34 | 16,89 → 7,87 | 0,159 → 0,190 |
| 4e: binomiális valószínűség | 2,18 → 2,83 | 9,08 → 6,16 | 0,335 → 0,125 |
| Kereső: „derivált” | 0,98 → 1,10 | 2,76 → 2,87 | 0,001 → 0,001 |

A nagy integrálos feladatlap kész pontja **53%-kal korábbi**.
Meleg gyorsítótárral 11,61 s → 4,75 s.
Külön CPU-profilban az elrendezésszámítások száma 64 → 9; a javulás főleg
a zárt válaszok felesleges méréseinek kihagyásából származik.

**Az első megjelenés több tananyaglapnál későbbi lett**, miközben a szkriptek és a napló
hamarabb elkészülnek. A főoldal és a binomiális lap elmozdulása csökkent, más lapon
megmaradt vagy nőtt. A késleltetett naplópróba nem igazolta a fejlécmagasság növekedését;
a kipróbált logó-CSS visszavonva. A fennmaradó elmozdulások a betűcserével összefüggő
tördelésnél jelentkeznek. A kedvezőtlen mutatók további Q6-finomítások.

A főoldali, még folyamatban lévő videóátvitel nem szerepel teljes egészében a befejezett
kérések byte-számában; abból teljes adatforgalmat nem állapítottam meg.

### Ellenőrzés

| Próba | Eredmény |
|---|---|
| Kép → média → háttér/betöltési jelzések | Sikeres; 334 médiaelem 139 lapon; végül 0 háttér- és betöltésijelzés-változás. |
| Kánon, belső link, gyakorlósáv | 310/0; sáv tiszta. Két korábbi heurisztikus visszautalás-figyelmeztetés megmaradt. |
| Teljes oldalkészlet, Edge 390 px | 310/0 túlcsordulás, KaTeX-render-, JS- vagy helyi fájlhiba; naplóchip, minden kvíz, interaktív ábra, tartalomjegyzék-horgony ellenőrizve. |
| Végleges megjelenés | 15 mintalap × 360/390/1280 px: 45 nézet/0, nyitott válaszok széles képletei fókuszolhatók; a logó-CSS visszavonása után megismételve. |
| Képek | 9/9 betöltve, natív méret és alternatív szöveg egyezik; két tananyag JS nélkül és nyomtatásban is látható képpel. |
| Kezelés | 82 + 10 sikeres próba: menü/fókusz, kereső, legutóbbi lap, naplókód, hét interaktív mód, késleltetett modulsorrend; média nyit/zár helyi próbakerettel. |
| Képletrender és kvíz | 37 oldal, 3644 képlet, 52 sikeres kvízpróba, 0 hiba. |
| Akadálymentesség | 5 végleges axe-próba, 0 jelzés. |
| Nyomtatási nézet | 15/15 JS-sel, 2/2 JS nélkül; tartalom látható, menü rejtett. |
| Megőrzés és generátor | 310 kizárólag engedélyezett HTML-átalakítás, 9 byte szerint azonos kép, 228 további változatlan asset/eszköz/forrás/tükör; 310 idempotens oldal és külön generátorhatárok. |

Az 1e/01 halmazfogalom lapjának képletbe tett magyar idézőjeleiről a teljes készletben
8 korábbi KaTeX-konzolfigyelmeztetés érkezett; nincs képletrajzolási hibajelző.
Ez külön tipográfiai ellenőrzésre vár. Használatlan font-előtöltésről nem jött jelzés.

A túlcsorduláspróba a `layout_teszt.py` aktuális, forrásból ellenőrzött kifejezését használja.
Tanulói szöveg, feladat, számadat és végeredmény változatlan: builder-, kulcs-, regressziós
és új matematikai lektori futás nem kellett. Naplókód, térkép, keresőindex, tükrök és a
backlog zárolt első 23 sora megmaradtak. A nyers mérések a privát munkamappában vannak.

### Hátra és korlát

- Első megjelenés és fontcsere okozta elmozdulás finomítása; különösen a hosszú morzsasor/cím és az integrálos lap CLS-e.
- Az 1e/01 halmazfogalom képletbe tett idézőjeleinek tipográfiai ellenőrzése.
- Élő GitHub Pages, valódi telefon, más böngésző és képernyőolvasó nem futott. Az axe nem teljes WCAG-minősítés, a nyomtatási próba nem teljes PDF-tördelés; külső lejátszás/applet új ellenőrzése nincs.

**Tanári döntés kell:** az elkészült gyorsításhoz nincs. Q6 első adag helyben kész,
első megjelenés/CLS még finomítandó; következő nagyobb tétel előtt választás kell.

### Technikai források

Szkriptbetöltés: [MDN — script](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script).
Fonttervezés: [web.dev — betűkészletek](https://web.dev/learn/performance/optimize-web-fonts),
[web.dev — kritikus erőforrások előtöltése](https://web.dev/articles/preload-critical-assets).
A beállításokat a fenti helyi mérés alapján választottam.
