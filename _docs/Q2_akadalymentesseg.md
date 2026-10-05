# Q2 — akadálymentességi ellenőrzés és javítások

Dátum: 2026-10-05. Kiinduló revízió: `f491b04`, tiszta helyi `main`, egy helyi
committal az `origin/main` előtt. A tanár korábbi döntése szerint a munka a `main`
ágon folyik; új ág és push nem készült.

## Hatókör

A közös kezelőfelület, a főoldal, a kereső, a Küldetésnapló, a képletes kvízgombok,
táblázatfejlécek és gördülő képletek ellenőrzése. A tananyag szövege, a feladatok,
számadatok és megoldókulcsok nem változtak. A halmazműveletek hat meglévő Venn-ábrája
szöveges nevet kapott. Az érintett HTML-lapok kézzel karbantartott lapok; builder
újraépítésére nem volt szükség. Tükrözött dokumentáció nem változott.

Az axe-core 4.13.0 a WCAG 2.1 A/AA és best-practice szabályaival futott, helyi
Playwright–Edge böngészőben. A külső kérések blokkolva voltak. Az eredmény nem teljes
WCAG-megfelelőségi tanúsítás, és nem igazolja a beágyazott külső szolgáltatásokat.

## Javítás előtt bemutatott hibalista

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Képletes kvízgombok és táblázatfejlécek | A látható KaTeX-képlet mellett hiányzott a vezérlő olvasható neve | magas | Közös `ui.js`: a MathML szerkezetéből képzett magyar név, fejlécnél rejtett szöveges alternatíva |
| Kereső és Küldetésnapló | Több másodlagos szöveg és XP-címke kontrasztja kevés volt a képes háttéren | közepes | Közös `theme.css`: világosabb szürke, sötétebb dísztermi háttér, tömör XP-címke |
| Oldal tetejére vivő rakéta | A láthatatlan gomb Tab-bal elérhető maradt | közepes | CSS-ben valódi elrejtés; aktiválás után fókusz a logóra |
| „/” gyorskereső | Mobilon rejtett mezőre próbált fókuszálni; nem volt kikapcsolható | közepes | Látható mező keresése, mobilon keresőoldal; tartós kapcsoló a naplóban |
| Mozgáscsökkentés | Friss naplónál a rendszer beállítását felülírta az alapértelmezett effektkapcsoló | közepes | Rendszerkövető alapállapot; a tanuló kifejezett kapcsolása továbbra is érvényes |
| Üdvözlő videó | Nem volt külön szüneteltető vezérlő | közepes | Billentyűzettel kezelhető folytatás/szüneteltetés; csökkentett mozgásnál nincs automatikus indítás |
| Kereső, napló, kvíz | A dinamikus visszajelzés nem volt állapotüzenetként megjelölve | közepes | `role="status"`, udvarias, teljes üzenetet közlő élő régió |
| Küldetésnapló | A számlálók címsorok voltak; a kódmezőnek nem volt látható címkéje | alacsony | Számláló-bekezdések, látható mezőcímke, közös mezőstílus |
| Főoldal és tananyaglapon fejléc | Nem volt gyors ugrás a főtartalomra; a nyitó rész nem tartozott megnevezett régióhoz | alacsony | Első Tab-állomásként főtartalom-link, címmel megnevezett nyitó régió és útvonal |
| 1e/01 halmazműveletek | Hat Venn-SVG-nek nem volt hozzáférhető neve | magas | A meglévő ábráknak a halmazműveletet leíró név |
| Túl széles képlet- és táblázatdobozok | Nem voltak minden esetben billentyűzettel gördíthetők | magas | Csak valódi túlcsordulásnál Tab-állomás; újramérés méretezéskor, lenyitáskor és betűbetöltéskor |
| jsdom-ellenőrző eszköz | Rögzített várakozás után még betöltés alatt is vizsgálhatta a kvízeket | alacsony | A `load` esemény megvárása 30 másodperces időkorláttal |
| 23 lap táblázatai | 26 szándékosan üres sarok- vagy elválasztócella fejlécnek volt jelölve | alacsony | A közös UI rendes táblázatcellára cseréli; tartalom nem kerül az üres cellákba |
| Három mobilos képlet | Egy képpontnyi, kerekítésből eredő gördülés kimaradt a korábbi tűrés miatt | közepes | Minden tényleges gördülés Tab-bal elérhető; további betűbetöltés után újramérés |
| Új matematikai felolvasási nevek | A lektor 70 névpárban hibás megnevezést vagy hatókörvesztést talált | magas | Fokjel, derivált, inverz, teljes zárójeles alap, binomiális együttható, magyar ékezet és eltérő szorzásjelek helyes kezelése |
| Rejtett fejlécszöveg a javítás közben | 16 lapon mobilos oldaltúlcsordulást okozott a rejtett szöveg statikus helyzete | közepes | Rejtett szöveg helyzete rögzítve a bal felső sarokhoz, új teljes mobilpróba |

A javítás előtti 310 oldalas, 1280 px-es axe-futásban a szabályonkénti darabszámok
átfednek; nem összegezhetők különálló hibák számaként:

| Szabály | Érintett lap | Jelzett elem |
|---|---:|---:|
| `button-name` | 117 | 543 |
| `empty-table-header` | 53 | 205 |
| `svg-img-alt` | 1 | 6 |
| `scrollable-region-focusable` | 4 | 10 |
| `heading-order` | 1 | 1 |
| `region` — best-practice | 309 | 309 |

## Ellenőrzési eredmények — első adag (`fec9760`)

- Axe: **310 oldal × 390/1280 px = 620 vizsgálat, 0 szabályjelzés és 0 betöltési
  hiba**. A legutolsó arkuszfüggvény-név pontosítása után az érintett oldal külön,
  mindkét szélességen is hibátlan; a tényleges böngészős nevek megegyeznek a lektorált
  kivonattal. A bizonytalan eredményeket az eszköz külön tárolja, nem tekinti tiszta
  kézi ellenőrzésnek.
- Elrendezés: **310 oldal × 360/390/1280 px = 930 nézet, 0 jelzés**. A végső
  futás Node Playwrighttal a `layout_teszt.py` változatlanul kiolvasott mérőfüggvényét
  használta; a helyi fájlokat, JavaScript-kivételeket, konzol- és KaTeX-hibákat is
  vizsgálta. Az első teljes Python-futás 16 lapon jelezte a rejtett szöveg hibáját;
  ezt a CSS-javítás utáni teljes futás már nem találta. Egy korábban telepített
  Python-csomag jogosultsági hibája a repón kívüli futtatókörnyezet problémája volt.
- Kánon és jsdom: **310/310 oldal, 0 hiba**, osztályonkénti futásokban és a három
  alaplapon. A főoldal médialejátszására és a kereső `fetch` hívására a jsdom
  figyelmeztet: ezeket nem valósítja meg. A valódi böngészős videó- és keresőpróba sikeres.
- Friss szemű matematikai lektor: **785 egyedi névpár**. A 70 biztos jelentésvesztés
  javítása után a teljes új kivonatban nincs biztos fennmaradó vagy új matematikai
  hiba. A 163 érintett oldal statikus forrásából újra képzett kivonat mind a 785
  korábbi képletet megőrizte. A pont- és keresztjeles szorzás neve eltér, a téves
  válaszlehetőségek eredeti állításai megmaradtak. Ez szöveges ellenőrzés, nem hangos
  felolvasási próba; a kivonat nem tartalmazott mátrixot vagy összegjelet.
- Billentyűzetes próba: **55/55 sikeres** 390 és 1280 px-en, friss naplóval és
  rendszer szerinti mozgáscsökkentéssel. Főtartalom-link, fókusz, videóvezérlés,
  kereső és kikapcsolható gyorsbillentyű, naplókapcsolók, kódmező, rakéta, kvíz,
  Enter/Space-szel kezelt végeredmény-lenyíló, nyílbillentyűvel gördített képlet,
  érme/kocka-szimulátor és ábracsúszka. Az asztali három alaplap 200%-os nagyításnál
  is túlcsordulás nélkül maradt.
- Kontrasztmérés: négy kiválasztott oldal látható szövege, 390 és 1280 px-en,
  összesen **8 nézet**. Az átmenetek lezajlása után a háttér tényleges képpontjaival
  számolva a javítás után nincs küszöb alatti mért szöveg. Javítás előtt például
  a kereső útvonala kb. 2,98:1, a napló szürke szövege 2,94–4,27:1, egy XP-címke
  3,70:1 volt. A logó mentessége miatt a márkajel nem hibaként szerepel.
- A főoldal és a napló 390/1280 px-es képeit szemrevételeztem. A gombok, mezők,
  címsorok és kontrasztjavítások az adott nézetekben rendezettek.
- A teljes belsőlink-vizsgálat: **310 oldal, 0 hiba**; gyakorlósáv-ellenőrzés: tiszta.
- A képek, médiakártyák és hátterek helyreállító eszközei lefutottak, 0 HTML-módosítással.
  A média állománya 334 aktív elem 139 lapon. A naplótérkép 184 oldal, 2294 feladat,
  12315 XP. A keresőindex újrafutott: **308 oldal**, az állománya változatlan.
- Megoldókulcs és feladat nem változott, ezért új kulcs- és regressziós futás nem kellett.
  Az előző, `f491b04`-hez tartozó adagban 4499/4499 kulcs és 100% regressziós érzékenység
  volt; ez nem jelen adagban végzett új mérés.

## Megismételhető eszköz

Az új `_tools/akadaly_teszt.cjs` minden lapot, osztályt vagy kijelölt lapot képes
ellenőrizni. A Playwright és axe-core telepítése a repón kívül marad; `NODE_PATH`
adhatja meg a csomagkönyvtárat, `CHROMIUM_PATH` a böngészőt.

```text
node _tools/akadaly_teszt.cjs --szelessegek=390,1280 --json=C:/QA/akadaly.json
node _tools/akadaly_teszt.cjs 2e/ --szelessegek=390
```

Kilépés: 0 = nincs axe-jelzés, 1 = szabályjelzés, 2 = eszköz- vagy betöltési hiba.
A JSON külön őrzi a bizonytalan, kézi ellenőrzést kérő eredményeket és a képletes
vezérlők felolvasási neveit is. A részletes helyi nyers eredmények és képek a
Codex munkamappájában maradnak, nem kerülnek a nyilvános repóba.

## Második adag — köszöntővideó és további kontrasztminták (2026-10-05)

Kiinduló revízió: `fec9760`, tiszta helyi `main`, két helyi committal az
`origin/main` előtt. Új ág és push ebben az adagban sem készült.

### Javítás előtt bemutatott hibák

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Főoldali videó | A beszédhez nem tartozott felirat vagy teljes leirat | közepes | Kézzel karbantartott főoldali HTML, VTT-fájl és közös videókezelő |
| Osztály- és témakörkártyák | Sötét sorszámok, a mintákban akár 1,46:1 | közepes | Közös CSS, világos másodlagos szövegszín |
| „Nehéz” szintcímke | Egy képes háttér előtt 3,58:1 | közepes | Közös CSS, világosabb piros szöveg |
| Összefoglaló szövegközi linkje | 3,95:1 a normál szövegre előírt 4,5:1 helyett | közepes | Közös CSS, világosabb zöld linkszín |
| Nyomtatás | A fókuszkeret és a lenyíló elválasztója zöld maradt | alacsony | Közös nyomtatási stílus |
| Videó JavaScript nélkül | Automatikusan indult, így nem alkalmazhatta a rendszer mozgáscsökkentését | közepes | HTML-ben kézi indítás; JS-sel továbbra is rendszerfüggő, néma indítás |

### Mi változott

- `assets/img/welcome-hu.vtt`: három időzített magyar felirat. A helyi
  beszédfelismerésből készült szöveget a tanár ebben a beszélgetésben pontosként
  megerősítette: „Üdv, kadét! Kezdődik a kiképzés. Húzd ki magad, és villantsd a matekot!”
- A főoldalon alapból bekapcsolt, billentyűzettel kapcsolható magyar felirat és
  külön, nyitható, nyomtatható leirat. A felirat a videó alatt, tömör, sötét
  dobozon jelenik meg, így az átlátszó videó tartalék-keverése nem rontja a
  kontrasztját. Az időzített másolat nem élő régió; a teljes szöveg a leiratban
  hozzáférhető. JS nélkül a videó saját vezérlői és natív felirata használhatók.
- A sorszámok, nehézségcímkék és szövegközi linkek közös színe világosabb.
  Nyomtatáskor nincs fókuszkeret, a lenyílók elválasztója szürke. Oldalankénti
  stíluskivétel és builder-módosítás nem kellett.
- Az akadálymentességi eszköz helyi kiszolgálója a VTT-fájlokat megfelelő
  tartalomtípussal adja vissza. A keresőindexben kizárólag a főoldal szövege változott.

### Ellenőrzés

- **Kontraszt: 16 oldal, 390/1280 px, 128 nézet, 5826 látható szövegminta,
  0 küszöb alatti érték.** Mind a hat háttértípus és négy osztály szerepelt.
  Nézetek: az oldal eleje/közepe/vége (96), lenyitott rész (12), helyes és
  téves kvízválasz (10–10). A legkisebb javított sorszámérték 10,14:1,
  „Nehéz” címkeérték 5,22:1, közös linkszínérték 5,21:1 volt a mintákban.
  A felirat tömör hátterének számított kontrasztja 14,94:1.
- A mérés a szöveg mögötti tényleges képpontokkal számolt, az átmenetek
  lezajlása után. A rögzített fejléc vagy rakéta által takart pontokat kizárta;
  azok az első mérésben hamis kontrasztjelzéseket okoztak. A logó, dekoráció,
  színes emoji és SVG nem része ennek a szövegmérésnek. A tíz áttetsző
  gyakorlósáv-címke külön, öt nézetben mérve is megfelelő: a saját átlátszó
  hátterük miatt a 0,85-ös szövegopacitás a tényleges háttérre keverhető;
  a legkisebb érték 5,35:1, küszöb alatti címke nincs.
- **Axe: 16 oldal × 390/1280 px = 32 vizsgálat, 0 szabályjelzés és betöltési hiba.**
  A videóhoz tartozó feliratjelzés eltűnt. Mind a 32 nézetben maradt kézi
  kontrasztellenőrzést kérő eredmény; a fenti mintamérés ezt külön vizsgálta.
- **Elrendezés: 16 oldal × 360/390/1280 px = 48 vizsgálat, 0 jelzés.**
  A projekt Python Playwright-eszköze futott; a túlcsordulást, helyi fájlokat,
  konzolt, JavaScript-kivételeket és KaTeX-hibákat vizsgálta.
  Az utolsó nyomtatási és JS nélküli indítási pontosítás után a főoldal
  külön, mindhárom szélességen is hibátlan.
- **Videó: 44/44 sikeres böngészős ellenőrzés.**
  A felirat mindhárom időpontban látható és túlcsordulás nélkül olvasható;
  Enter/Space-szel kapcsolható. A mozgáscsökkentés, szüneteltetés, leirat,
  nyomtatás, JS nélküli natív felirat és MP4-tartalékforrás is szerepelt.
  A WebM és MP4 hangjának helyi összevetése 7 ms eltérést és 0,998 körüli
  csúcskorrelációt mutatott. Az időzítés gépi szóidőkből készült;
  külön hangos meghallgatást nem állítunk.
- A főoldali felirat 390/1280 px-es és a leirat nyomtatási képe szemrevételezve.
  Az első videópróba ugrási hibája a helyi tesztkiszolgáló hiányzó byte-range
  támogatásából adódott; megfelelő kiszolgálás után az ugrás és a természetes
  lejátszás is működött. A jsdom feliratsáv-API-jának hiányát képességellenőrzés kezeli.
- **Kánon: 310 oldal, 0 hiba.** A három alaplap jsdom-próbája 0 hiba;
  a videólejátszás és keresőhálózat ismert jsdom-korlátai külön figyelmeztetések.
  **Belső linkek: 310 oldal, 0 hiba; gyakorlósávok: tiszta.**
- Kép/média/háttér helyreállítás: 0 módosítás. Média: 334 aktív elem 139 lapon;
  naplótérkép: 184 oldal, 2294 feladat, 12315 XP, változatlan. Kereső: 308 oldal,
  csak az `index.html` szövege módosult. Feladat és kulcs nem változott,
  kulcs- és regressziós teszt ebben az adagban nem kellett.

A nyers eredmények, képek, helyi beszédfelismerő és modell a Codex munkamappájában
maradtak, nem kerültek a repóba. A videót nem töltöttük fel külső átíró szolgáltatásba.

## Korlátok és fennmaradó ellenőrzés — aktuális állapot

- Valódi NVDA/VoiceOver-próba nem történt. A matematikai nevek szöveges vizsgálata
  és a böngésző hozzáférhetőségi fája nem helyettesíti ezt.
- Az axe több képes/áttetsző hátterű elem kontrasztját nem tudja önállóan megítélni.
  Mind a 620 nézetnél maradt ilyen kézi ellenőrzési jelzés (`incomplete`, nem szabályhiba).
  A második adag 128 nézetes mérése is mintavétel; nem minden oldal minden
  görgetési helyzetének, SVG-ábrájának vagy állapotának kontrasztbizonyítéka.
- A külső YouTube/GeoGebra felületek, feliratok és átiratok, illetve a teljes
  nyomtatási látvány nem kaptak új teljes ellenőrzést.
- A JavaScript nélküli statikus képletek és navigáció képernyőolvasós ellenőrzése
  külön feladat. A most hozzáadott közös kezelőfelületi nevek JavaScriptből készülnek.

**Tanári döntés kell:** nincs nyitott tartalmi döntés; a köszöntővideó szövegét
a tanár megerősítette. A valódi képernyőolvasós próba, a külső médiák és az ábrák
teljes hozzáférhetőségi vizsgálata még nem történt meg; a backlog Q2 sora részben kész.

## A javításokhoz használt hivatalos útmutatók

Az állapotüzenetek, a kikapcsolható karakter-gyorsbillentyű és a videószünet indoka:
[W3C — Status Messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html),
[W3C — Character Key Shortcuts](https://www.w3.org/WAI/WCAG21/Understanding/character-key-shortcuts.html),
[W3C — Pause, Stop, Hide](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html).
Az automatikus eszköz forrása: [axe-core](https://github.com/dequelabs/axe-core).
A felirathoz: [W3C — Captions (Prerecorded)](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html).
A szövegkontraszt küszöbeihez: [W3C — Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).
A helyi beszédfelismerő forrása: [faster-whisper](https://github.com/SYSTRAN/faster-whisper).
