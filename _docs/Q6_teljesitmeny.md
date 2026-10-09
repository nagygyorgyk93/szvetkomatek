# Q6 — Teljesítménymérés és betöltés

## Állapot — 2026-10-09

**Az első gyorsítási adag helyben elkészült.** Kiindulás: `940ad04`, tiszta `main`,
az `origin/main` helyi referenciájával azonos; távoli frissítés nem történt.
Új ág és push nélkül. A Q6 részben kész marad: az első megjelenés és a betűcsere
okozta elmozdulások további finomítást igényelnek.

## Hibatábla és változtatások

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

## Mérés

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

## Ellenőrzés

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

## Hátra és korlát

- Első megjelenés és fontcsere okozta elmozdulás finomítása; különösen a hosszú morzsasor/cím és az integrálos lap CLS-e.
- Az 1e/01 halmazfogalom képletbe tett idézőjeleinek tipográfiai ellenőrzése.
- Élő GitHub Pages, valódi telefon, más böngésző és képernyőolvasó nem futott. Az axe nem teljes WCAG-minősítés, a nyomtatási próba nem teljes PDF-tördelés; külső lejátszás/applet új ellenőrzése nincs.

**Tanári döntés kell:** az elkészült gyorsításhoz nincs. Q6 első adag helyben kész,
első megjelenés/CLS még finomítandó; következő nagyobb tétel előtt választás kell.

## Technikai források

Szkriptbetöltés: [MDN — script](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script).
Fonttervezés: [web.dev — betűkészletek](https://web.dev/learn/performance/optimize-web-fonts),
[web.dev — kritikus erőforrások előtöltése](https://web.dev/articles/preload-critical-assets).
A beállításokat a fenti helyi mérés alapján választottam.
