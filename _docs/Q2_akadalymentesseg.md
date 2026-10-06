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
- Elrendezés — **helyesbítve 2026-10-05:** a korábban jelentett 930/0 Node-eredmény
  nem érvényes túlcsordulási mérés: a futtató nem hívta meg a kiolvasott függvényt.
  A harmadik adag alább külön rögzíti a javítást és az új teljes mérést.
  Az első Python-futás 16 lapon ténylegesen jelezte a rejtett szöveg hibáját;
  ezt a CSS-ben javítottuk. A későbbi Node-futás a betöltést és a JS-/konzolhibákat
  vizsgálta, de az elrendezést nem igazolta. A Python-csomag olvasási korlátja
  a repón kívüli futtatókörnyezet problémája volt.
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

## Harmadik adag — ábrafeliratok és saját interaktív ábrák (2026-10-05)

Kiindulás: `ce3bca1`, tiszta helyi `main`, a helyi `origin/main` követőreferenciával
azonos revízió. Új ág és push nem készült. A matek-abra, web-verifikáció és
média-beágyazás szabályai alapján dolgoztunk.

### Javítás előtt bemutatott hibák

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Több osztály ábrái | Halvány színes és szürke feliratok | közepes | Közös CSS-ben sötétebb árnyalat, a színcsalád megőrzésével |
| 1e régebbi `.abra` ábrái | Világos ábralap nélkül a sötét tinta a képes háttérre került | magas | Közös világos ábrakeret és megfelelő méretezés |
| Grafikonok, térbeli vázlatok | Élek és görbék futottak a feliratok mögött | közepes | Világos betűkörvonal; a fehér sávfelirat kivétel |
| 3e/01 hatszög alapú hasábok | A felső csúcscímke a kép széléhez ért | alacsony | Közös builderben korlátozott felső címkeeltolás |
| 4e/06 Titanic-mozaikábra | Kevés kontraszt a fehér felirat és az áttetsző zöld sáv között | közepes | Builderben tömör zöld kitöltés |
| 4e nyolc saját interaktív ábrája | JavaScript nélkül 14 látszólag működő, hatástalan vezérlő maradt | közepes | Builderes statikus tájékoztató, vezérlők csak sikeres JS-indítás után |
| Korábbi Node QA-futtató | Nem hívta meg az elrendezést mérő függvényt; az üres adatot hibátlannak tekintette | magas | Eszköz: tényleges függvényhívás, kötelező számszerű eredmény, teljes újramérés |
| 1e/01 halmazok és házi; 4e/06 valószínűség-feladatok | A nyitott végeredmény hosszú képlete mobilon a teljes oldalt szélesítette | közepes | Közös CSS és UI: a képlet saját keretében, billentyűzettel is gördíthető; a képletben nincs örökölt függő behúzás |

A leltár **379 SVG-t talált 141 oldalon**. Mindegyiknek van `role="img"`, nem üres
`aria-label` és méretezhető `viewBox`; ez a komplex ábrák teljes szöveges
egyenértékűségét önmagában nem bizonyítja. A javítás előtti színmérés két szélességen
849 jelzést adott 194 ábrában, 87 oldalon; ezek átfedő mérési jelzések, nem 849
független hiba. A gyanús minták képen is ellenőrizve lettek. A világos borostyán,
zöld és cián vonalak sötétebbek, a segédrácsok és halvány területkitöltések megmaradtak.

### Ellenőrzések

- **SVG-feliratok:** 141 oldal × 390/1280 px, 758 ábranézet, 6094 szövegrész,
  **0 fennmaradó kontrasztjelzés, 0 levágott felirat, 0 betöltési hiba**. A legkisebb
  kontraszt **5,17:1**. A zárt megoldásdobozok a méréshez nyitva voltak. A betűt
  körülvevő tömör fehér körvonal háttérként szerepel a színpárban, a fehér feliratot
  a saját sávjához mérjük. A mobilos skálázás két kezdeti hamis jelzését és 17 túl
  keskeny szövegrész pixelmintavételi hiányát az SVG-egységben megadott körvonal
  figyelembevétele rendezte; az érintett öt lap külön újramérve is hibátlan.
  A módszer a [W3C szövegkontraszt-útmutatóját](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
  követi. Ez a feliratszínek vizsgálata, nem minden vonal és kitöltés teljes
  akadálymentességi igazolása.
- **Saját interaktív ábrák:** **218/218 sikeres próba**. Tab és látható fókusz;
  csúszkák Home/End és nyílbillentyűk; szimulátorgombok Enter/Space; kockaválasztás,
  újrakezdés; üres adatsor és a meglévő adatok visszaállítása; élő visszajelzés és
  JS-kivétel ellenőrzése. A billentyűzetes mozgatás utáni 16 ábranézet 170 felirata
  megfelelő kontrasztú és nem levágott. JavaScript nélkül, illetve az interaktív
  modul sikertelen betöltésekor mind a nyolc kezdőkép és a statikus tájékoztató
  látszik; nincs hatástalan, látható vezérlő. Az adatlabor kezdő mutatótáblája megmarad.
- **Axe:** 141 oldal × két szélesség = **282 vizsgálat, 0 szabályjelzés és 0
  fennmaradó betöltési hiba**. A futtatókörnyezet átmeneti hálózati hibáit új
  böngészőkörnyezetekben, a helyi fájlok változatlan bájtjaival megismételtük.
- **Builder és lánc:** kilenc builder öntesztje sikeres; 29 oldal újraépítve,
  közülük 14 HTML-ben maradt szándékolt változás. Képek → média → háttér →
  naplótérkép → keresőindex lefutott. Média: változatlan **334 aktív elem, 139 lap**.
  Naplótérkép: **184 oldal, 2294 feladat, 12315 XP**, változatlan. Keresőindex:
  **308 nem üres cím és szöveg**; pontosan a nyolc statikus tájékoztatót kapott
  oldal bejegyzése változott.
- **Teljes kánon és jsdom:** **310/310 oldal, 0 hiba**; a főoldali lejátszás és
  a kereső `fetch` hívása a jsdom ismert korlátjaként figyelmeztetést ad.
  **Linkek 310/0**, gyakorlósáv tiszta, **kulcsteszt 4499/4499**, regressziós
  érzékenység **4499/4499 = 100%**. A SymPy 1.14.0 külön, repón kívüli példánnyal
  futott; a korlátozott környezet csomagolvasási jogosultsága miatt külön futtatás
  kellett. A matematikai algoritmusok és a megoldókulcsok nem változtak.
- **Tartalommegőrzés:** a 14 módosult HTML szövege az új kezelési tájékoztatók
  kivételével azonos; minden korábbi azonosító és link megmaradt. Öt ábraminta
  390 px-es és nyomtatási képét szemrevételeztük. Teljes nyomtatott oldaltördelést
  és a teljes webhely nyomtatási látványát ebben az adagban nem ellenőriztük.

### Helyesbítés a korábbi Node-elrendezésmérésekhez

A repón kívüli Node-futtató a Python-eszközből kiolvasott függvényt korábban nem
hívta meg; így a korábbi 930 nézetben nem keletkezett túlcsordulási mérési adat.
Az ilyen futások **nem igazolják** a korábban jelentett elrendezési eredményt.
A futtató most ténylegesen meghívja a változatlan projektfüggvényt, és hibát jelez,
ha nem kap számszerű eredményt. A teljes webhely tényleges újramérése megtörtént:
**310 oldal × 360/390/1280 px = 930 nézet**, minden nézetben zárt és kinyitott
megoldásdobozokkal. Zárt állapotban nincs jelzés; nyitott állapotban három oldalon
hat mobilos túlcsordulás maradt (360/390 px-en): halmazok +82/+52 px, házi +77/+47 px,
valószínűség +144/+114 px. Betöltési, helyi fájl-, JavaScript- és KaTeX-hiba nincs.

A három hibát a közös megoldásdoboz-stílus rendezte. A hosszú képlet saját
keretében gördül, a rövid képlet teljesen látszik; az örökölt függő behúzás a
képleten belül megszűnt. Csak a ténylegesen gördülő képlet kap Tab-fókuszt és
magyar kezelési nevet. Nyomtatáskor a gördülő keret kikapcsol, a szöveg megmarad.
Javítás után **a három érintett oldal kilenc nézete újramérve: 0 jelzés**,
zárt és nyitott megoldásokkal. A teljes 930-as alapmérés és az érintett kilenc
nézet ismétlése adja a végső lefedettséget; a javítás után nem futott újabb teljes
930-as mérés. A három lap kánon- és jsdom-próbája külön is **3/3, 0 hiba**.
A nyitott megoldások kilenc nézetén külön axe-próba is futott: **9/9, 0 jelzés**;
mind a **13 ténylegesen gördülő képlet** fókuszolható, látható fókuszt és magyar
nevet kap, és a jobb nyílbillentyű valóban gördíti. Az első célzott próbában az
örökölt negatív szövegbehúzás hamis gördülő dobozokat és levágott rövid képleteket
eredményezett; ezt a végső javítás és az ismételt próba rendezte.

### Fennmaradó ellenőrzések és tanári döntés

Q2 továbbra is részben kész. Valódi NVDA/VoiceOver-próba, a komplex ábrák szöveges
egyenértékűsége, külső beágyazások és a JS nélküli képlet-felolvasás nincs teljesen
ellenőrizve. A gépi névleltár és a böngésző hozzáférhetőségi fája nem helyettesíti
a tényleges felolvasást. **Tanári döntés kell: nincs új kérdés.**

## Negyedik adag — külső médiák saját kezelőfelülete (2026-10-05)

Kiindulás: `ada7ff5`, tiszta helyi `main`. A munka elején a helyi `origin/main`
követőreferencia egy committal korábbi volt; a munka közben `ada7ff5`-re frissült,
a helyi HEAD nem változott. Új ág és push nem készült. A média-beágyazás,
web-verifikáció és akadálymentességi ellenőrzés szabályait követtük.

### Javítás előtt bemutatott hibák

| Hol | Probléma | Súlyosság | Javítás módja |
|---|---|---|---|
| Médiaindító sávok | Hivatkozásként jelentek meg, miközben helyben nyitottak lejátszót; a szóköz nem indította őket | közepes | Közös JS: gombszerep, műveleti név, vezérelt keret és nyitott állapot; Enter és szóköz |
| Megnyitott videó vagy applet | Nem volt bezáró vezérlő | közepes | Közös JS/CSS: bezárás, iframe eltávolítása és fókusz-visszaadás ugyanarra az indítóra |
| Megnyitott YouTube-videó | A közvetlen videóhivatkozás eltűnt; a képaláírás MNT-forráslinkje megmaradt | alacsony | Közös JS: külön „Megnyitás a YouTube-on új lapon” link |

Az új vezérlősáv megnyitás után a keret fölött látszik. GeoGebránál is tartalmaz
közvetlen újlap-linket; az eredeti szerzői és licencadatok a képaláírásban megmaradnak.
Bezáráskor az eredeti sáv és forráscím tér vissza, a lejátszó iframe-je megszűnik.
A szóköz csak azon az indítón működik, amelyen lenyomták és elengedték; köztes
fókuszváltás nem indít másik médiát. A módosítóbillentyűs kattintás kezelése megmaradt.

A gombszerep és az Enter/Space kezelés a
[W3C gombmintáját](https://www.w3.org/WAI/ARIA/apg/patterns/button/) követi.
A név és a kinyitott állapot gépi elérhetőségéhez:
[W3C — Name, Role, Value](https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html);
a fókuszhoz: [W3C — Focus Order](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html).

### Ellenőrzések

- **Teljes médialeltár:** 139 oldal, **334 elem: 310 YouTube és 24 GeoGebra**.
  Mindegyik két teljes billentyűzetes megnyitás–bezárás ciklust kapott 390 px-en:
  **668/668 sikeres ciklus, 0 JS-kivétel, 0 nyitott állapotú oldaltúlcsordulás
  vagy KaTeX-hiba**. Enter és szóköz, ismételt indítás, eredeti forráscím,
  műveleti név, nyitott állapot, látható fókusz és fókusz-visszaadás ellenőrizve.
  Az új vezérlők legalább 44 px magasak; a saját tömör hátterükön a szövegkontraszt
  minimuma **14,94:1**. Ez a vezérlők színpárja, nem a teljes oldal kontrasztja.
- **Két mintalap, 360/390/1280 px:** hat megnyitott állapotban a saját felület
  axe-próbája **6/6, 0 szabályjelzés**. A szolgáltatói iframe-ek belseje kizárva;
  a képes hátterekre továbbra is maradt kézi kontrasztellenőrzési jelzés.
  A böngésző hozzáférhetőségi fájában a név és a nyitott állapot változik.
  Tab/Shift+Tab visszajutás a helyi próbakeretből és a szóköz közbeni fókuszváltás
  ellenőrizve. Két külön megnyitott keret egymástól függetlenül bezárható.
- **Tartalékmódok és nyomtatás:** a két lap JS nélkül, a médiamodul betöltési
  hibájával és blokkolt iframe-mel is használható: hat tartalékpróba sikeres.
  Indítás előtt nem volt külső kérés. JS nélkül/modulhiba esetén a sáv közvetlen
  forráslink; blokkolt keretnél megmarad a bezárás és az újlap-link. Két mobilos
  és két nyomtatási képet szemrevételeztünk. Nyomtatáskor a kezelősáv és a keret
  rejtett, a cím és a rövid forráscím olvasható. A célzott állapotpróba összesen
  **14/14 sikeres eset**; teljes nyomtatott oldaltördelést nem vizsgáltunk.
- **Új lap:** a közvetlen link külön böngészőlapot nyitott a várt célcímmel, helyi
  próbadokumentummal. Ctrl-kattintáskor is létrejött az új lap, és nem nyílt helyi
  iframe, de a céloldal betöltése ebben a futtatóban böngészőhibával végződött;
  ennek sikeres hálózati betöltését nem állítjuk.
- **Projektlánc:** képek → média → háttér: **0 fájl módosult**, a katalógus és a
  334 elem változatlan. Teljes kánon **310/310, 0 hiba**; külön, a csomagolt Node
  közvetlen indításával a jsdom **310/310** lapot ténylegesen renderelt és a
  kvízeket próbálta. Két ismert környezeti figyelmeztetés maradt: a főoldali
  `play()` és a kereső `fetch` támogatása. A Python-driver első próbájában a
  render kimaradt, majd időtúllépést adott; ezt nem tekintettük sikeres rendernek.
  Belső linkek **310/0**, gyakorlósáv tiszta, diff-ellenőrzés tiszta.
  Builder, HTML, matematikai tartalom, feladat, kulcs, médiakatalógus, keresőindex
  és naplótérkép nem változott; kulcs-/regressziós és tartalmi újraépítés nem kellett.

### Korlátok és tanári döntés

A cikluspróbák a valódi helyi oldalt és a saját médiakezelőt futtatták, a külső
iframe-ben helyi próbadokumentummal. A szolgáltatók saját lejátszója, feliratai,
átiratai és GeoGebra-vezérlői ebben az adagban nem kaptak teljes vizsgálatot.
A hozzáférhetőségi fa nem helyettesít valódi NVDA/VoiceOver-felolvasást.
Q2 továbbra is részben kész: ezen túl a komplex ábrák szöveges egyenértékűsége
és a JS nélküli képlet-felolvasás is hátravan. **Tanári döntés kell: nincs új kérdés.**

## Ötödik adag — diagramok szöveges adatai, 4e/06 (2026-10-05)

Kiinduló revízió: `2f258a4`, tiszta helyi `main`, egy committal a helyi
`origin/main` követőreferencia előtt. A hat diagram javítását előzetes hibatáblában
bemutattuk. Új ág és push ebben az adagban sem készült.

### Megállapítások és javítások

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Adatokból kép — kördiagram | A hozzáférhető név közölte a százalékokat, de a négy darabszám csak az SVG-ben szerepelt | közepes | Builder: darabszám és kerekített százalék együtt, adattáblában |
| Ugyanott — hisztogram | A 20 éves csoportok táblája nem helyettesítette a rajz 18, ötéves korcsoportját | közepes | Builder: a teljes adatsor, a nyitott 85+ csoport és a tengely leírása |
| Ugyanott — vonaldiagram | A hozzáférhető név a tendenciát, az SVG csak három pont számértékét közölte | közepes | Builder: mind a kilenc népszámlálás adatai és az arányos időtengely leírása |
| Statisztika — nehéz 1. | A születésszámok csak a rajzon voltak megadva | magas | Builder: a két adat és a meglévő tengelybeosztás |
| Házi feladatok — alap 4. | A 12 havi esősnap-szám csak a rajzról volt leolvasható | magas | Builder: havi adattábla, az esős nap és a tengely leírása |
| Terepküldetés — Jokić-ábra | A két pontátlag csak a rajzon szerepelt | magas | Builder: a két adott pontátlag és a meglévő tengelybeosztás |
| Kulcsellenőrző, az új adattáblák után | Az első tetszőleges lenyílót válasznak olvasta, így hat téves eltérést jelzett | közepes | Eszköz: kizárólag a `vegeredmeny` osztályú lenyíló olvasása; öt szerkezeti teszt |
| Nyomtatás JavaScript nélkül | A böngésző natív zárt lenyílója a régi tartalék CSS ellenére sem festette ki a táblázatot | közepes | Közös `print.css`: a natív lenyílótartalom is látható nyomtatáskor |

### Megvalósítás

- Hat diagram mellett **47 adatsor**, natív, billentyűzettel működő lenyílóban.
  Mindegyik táblázat címet, oszlopfejléceket és sorfejléceket kapott. A rövid SVG-név
  megmondja, melyik lenyíló tartalmazza az adatokat; a táblázat szerkezete megmarad.
  A megoldás a [W3C összetett ábrákhoz adott útmutatóját](https://www.w3.org/WAI/tutorials/images/complex/)
  követi: rövid név mellett mindenki számára elérhető, strukturált szöveges adatközlés.
- Az új `abra_stat.diagram_adatok` segédet a három érintett builder használja.
  A diagram és leírása natív `figure`/`figcaption` csoport; nincs új táblázatstílus.
  A feladatkártya-generátor a csoportot a bekezdésen kívül helyezi el.
  A terepküldetés listájának függő szövegbehúzását az ábracsoport nem örökli.
- Érintett lapok: `tananyag-adatok.html`, `feladatok-statisztika.html`,
  `feladatok-hazi.html`, `terepkuldetes.html`, mind a `4e/06-valoszinuseg-statisztika/`
  mappában. A keresőindexben csak e négy lap szövege változott.
  Matematikai feladat, számadat, rajzgeometria, végeredmény és horgony nem változott.
- A próbák közben az új csoport fölösleges ARIA-szerepét eltávolítottuk;
  a natív ábraszerep megmaradt. A nyomtatási hibát a kép mutatta meg:
  az elem méretének mérése önmagában nem igazolta, hogy a böngésző ki is festi.
  Az utópróbák a natív tartalom láthatóságát és a képet is ellenőrizték.

### Ellenőrzés

- **Adatok:** hat táblázat, 47 sor; mindhárom szélességen pontos egyezés a már
  meglévő nyilvános adatmodullal. A százalékokat a kontroll függetlenül,
  decimális `ROUND_HALF_UP` kerekítéssel képezte. **17/17 megőrzési vizsgálat**:
  a négy lapon az SVG-k (a hozzáférhető név kivételével), végeredmények, kvízek,
  azonosítók és a backlog zárolt fejléce változatlan. A két feladat új ábrája
  a nyers HTML-ben is a bekezdésen kívül van.
- **Böngésző:** négy oldal × 360/390/1280 px × zárt/nyitott állapot = **24 nézet**,
  0 oldaltúlcsordulás és KaTeX-hiba. Axe ugyanebben a 24 nézetben: **0 szabályjelzés**.
  A képes háttérhez az axe kézi kontrasztellenőrzést kér; ez nem teljes WCAG-igazolás.
  A listából örökölt behúzás utolsó javítása után a terepküldetés külön,
  mindhárom szélességen, zárt és nyitott állapotban is újra ellenőrizve.
- **Billentyűzet:** hat lenyíló × három szélesség × Enter/Space = **36 sikeres
  nyitás–zárás ciklus**, megmaradó fókusz. JavaScript nélkül mind a hat lenyíló
  Space-szel használható, a táblázat hozzáférhető.
- **Nyomtatás:** négy lap, JavaScripttel és nélküle = **8 sikeres eset**;
  mind a 47 adatsor látható. Két korábbi feladatlapon kontrollként JavaScript nélkül
  a 31, illetve 55 zárt Végeredmény-doboz tartalma is megjelenik nyomtatási módban.
  Mobilos komponensképek és a hisztogram nyomtatási képe szemrevételezve.
  A külön komponensképeken a lebegő fejléc/rakéta szükség esetén elrejtve, hogy ne
  takarja a vizsgált ábrát. A teljes PDF-oldaltördelést nem minősítjük.
- **Friss szemű lektor:** kizárólag az új szövegekből és a két feladatból dolgozott,
  eredmények nélkül. A független válaszok a meglévő kulcsokkal egyeznek:
  10,0%; 0,305; 0-tól induló tengely; március/július; 108 nap és 9 nap/hónap; 0,295.
  Biztos számolási vagy nyelvi hibát nem talált. A tananyag három helyes összehasonlítása
  maradt; a feladatdiagramok leírása csak adott adatot és tengelybeosztást közöl.
  A nyitott utolsó korcsoportot a képaláírás és az új leírás egyaránt megnevezi.
- **Projektlánc:** a három builder öntesztje és privát tiltott-ellenőrzése rendben;
  képek → média → háttér lefutott, a két érintett tananyaglapon a médiák visszaálltak.
  Média: változatlan 334 elem, 139 lap. Teljes kánon **310/310, 0 hiba**;
  a teljes 4e/06 témakör külön jsdom-futásban **13/13**, 0 render-/kvízhiba.
  Belső linkek **310/0**, gyakorlósáv tiszta. Kulcsellenőrzés **4499/4499**;
  regressziós érzékenység **4499/4499 = 100%**; új kulcsolvasó-tesztek **5/5**.
  Naplótérkép: változatlan 184 oldal, 2294 feladat, 12315 XP; kereső: 308 oldal.
  A diff és a zárolt fejléc ellenőrzése tiszta.

### Korlátok és tanári döntés

Valódi NVDA/VoiceOver-felolvasás, a többi összetett ábra teljes szöveges
egyenértékűsége, a külső szolgáltatók médiafelülete/felirata/leirata és a JavaScript
nélküli képlet-felolvasás továbbra is nyitott Q2-tétel. A nyomtatási tartalékot a
helyi Edge-ben próbáltuk; más böngészőkre nem állítunk teljes ellenőrzést.
**Tanári döntés kell: nincs új kérdés.**


## Hatodik adag — 1e/01 függvényábrák és magyar megfogalmazás (2026-10-05)

A `840f361` revízióból indulva a három függvényes tananyag nyolc SVG-je kapott
látható, `aria-describedby` kapcsolattal elérhető szöveges leírást. A két számozott
nyíldiagram minden nyila, a három tulajdonságdiagram összes kapcsolata,
a gépsor műveleti sorrendje és a két koordináta-grafikon jelentése olvasható.
A függvényfogalom egyenesének hibás végpontja is javult.

A tanár új kérése szerint a három lap bevezetőit, matematikai prózáját és
hétköznapi példáit is végigolvastuk és javítottuk. A részletes hibalista,
a lektor eredménye, a megőrzés és a korlátok: [A3 nyelvi ellenőrzés](A3_nyelvi_ellenorzes.md).

Végleges háromszélességes böngészőpróba, zárt és nyitott lenyílókkal:
**18/18 nézet, 0 elrendezési és axe-szabályjelzés**. Mind a nyolc leírás az Edge
hozzáférhetőségi fájában is szerepel. Három JS nélküli lap és hat JS be/ki
nyomtatási nézet megfelelő. jsdom: **200 képlet, 4/4 kvíz, 0 hiba**;
kánon/linkek **310/0**, kulcs **4499/4499**. Feladat, végeredmény és kulcsmodul
nem változott, ezért a regressziós érzékenységet most nem ismételtük.

Valódi képernyőolvasós próba, a többi összetett ábra, külső szolgáltatói felület és
JS nélküli képlet-felolvasás továbbra is hátra van. Más böngészőt és a teljes
nyomtatási oldaltördelést nem minősítjük. **Tanári döntés kell: nincs új kérdés.**


## Hetedik adag — 1e/02 trigonometriai ábrák (2026-10-05)

A három tananyag négy SVG-je teljesebb, látható leírást kapott, `aria-describedby`
kapcsolattal. A leírások megadják a csúcsok és oldalak szerepét, a nevezetes
háromszögek összes oldaladatát és szögét, valamint a magasságmérés modelljét.
A szögfüggvényes háromszög és a magasságmérés szögívének hibás végpontja javítva.

Mind a négy név és leírás ellenőrizve az Edge hozzáférhetőségi fájában.
Végleges böngésző/axe: **18 nézet, 0 elrendezési és szabályjelzés**;
nyomtatás JS be/ki **6/6**, JS nélküli szöveges leírás négy ábrához látható.
Mind a négy mobilos ábra és a magasságmérés nyomtatási képe szemrevételezve.
jsdom **184 képlet, 6/6 kvíz, 0 hiba**; teljes kánon/link **310/0**.
Részletes megőrzés, lektor és számolás: [A3 harmadik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasós próba, a többi összetett ábra, külső szolgáltatói felület,
a képes hátterek kézi kontrasztja és JS nélküli képlet-felolvasás még hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**


## Nyolcadik adag — 1e/03 számhalmazok, abszolútérték és felbontás (2026-10-05)

A négy tananyag három SVG-je teljesebb, látható leírást kapott,
`aria-describedby` kapcsolattal. A számhalmazok egymásba illeszkedése és az
összes számos példa besorolása, a két szám abszolútértéke, illetve a 120 teljes
prímtényezős osztási sora szövegesen is olvasható.

A számhalmaz-ábra három példafelirata hibás tartományba került: a −3 és 0
az N-ben, a törtek a Z-ben, az irracionális példák a Q-ban látszottak.
A feliratok áthelyezve; a tényleges teljes szövegdobozuk mindhárom vizsgált
szélességen a megfelelő halmazban van, és nem metszi a kizárt belső halmazt.
Az oszthatóság utolsó kvíze a gyakorlósáv dobozából a megfelelő helyre került.

Mindhárom név és leírás ellenőrizve az Edge hozzáférhetőségi fájában.
Végleges böngésző/axe: **24 nézet, 0 elrendezési és szabályjelzés**;
nyomtatás JS be/ki **8/8**, a három ábraleírás JS nélkül is látható.
A három mobilos ábra és a számhalmaz-ábra nyomtatási képe szemrevételezve.
jsdom **246 képlet, 9/9 kvíz, 0 hiba**; teljes kánon/link **310/0**.
A lektori javítások után mind a négy tananyag újramérve.
Részletes hibalista, megőrzés, lektor és számolás:
[A3 negyedik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasós próba, a többi összetett ábra, külső szolgáltatói felület,
a képes hátterek kézi kontrasztja és JS nélküli képlet-felolvasás még hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**


## Kilencedik adag — 1e/05 geometria, 11 ábra (2026-10-06)

Három tananyag 11 SVG-je teljesebb, látható szöveges leírást kapott,
aria-describedby kapcsolattal: illeszkedés, szög, metsző/párhuzamos egyenesek,
háromszögfajták és külső szög, körülírt és beírt kör, súlyvonalak.
A leírások a feliratokat, elrendezést és geometriai kapcsolatokat is megadják.
Két korábbi svgwrap leírása a közös világos svgcard keretbe került;
oldalankénti CSS-kivétel nincs.

A „szabályos” ábrán a három oldal nem volt egyenlő: a felső csúcs javítva.
A külső szög íve rossz tartományt jelölt: helyes körív a meghosszabbított
alap és a ferde oldal között. Az α-felirat teljes doboza a belső szögben van.
Minden felirat elfér a viewBox-ban 360/390/1280 px-en. Független geometriai
számolás és a böngésző tényleges SVG-útvonalának mérése egyezik.

Mind a 11 név és teljes leírás szerepel az Edge hozzáférhetőségi fájában.
A MathML-t a szövegellenőrzés elkülöníti a rejtett TeX/KaTeX-rétegektől.
Végleges böngésző/axe: **18 nézet, 0 elrendezési és szabályjelzés**.
Nyomtatás JS be/ki **6/6**, mind a 11 ábra/leírás látható;
a leírások JS nélkül is olvashatók. A 11 mobilos ábra és három nyomtatási
ábraminta szemrevételezve. jsdom **135 képlet, 6/6 kvíz, 0 hiba**;
teljes kánon/link **310/0**. Részletes lektor, megőrzés és számolás:
[A3 hatodik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasó, a többi összetett ábra, szolgáltatói médiafelület,
képes hátterek teljes kézi kontrasztja és JS nélküli képlet-felolvasás hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**


## Tizedik adag — 1e/05 tér, szögek és négyszögek, 13 ábra (2026-10-06)

Három tananyag 13 SVG-je teljesebb, látható leírást kapott aria-describedby
kapcsolattal. Kitérő egyenesek, merőleges egyenes/sík, síkpárok, szögfajták,
csúcs- és mellékszögek, egyállású szögek, négyszögek átlói, trapézalapok,
húr- és érintőkör szerepelnek. A közös világos ábrakártyák megmaradtak,
oldalankénti CSS-kivétel nem készült.

Két szögív pontos végpontot kapott, a metsző síkok korábban levágott sarka
most elfér a bővített viewBox-ban; a trapéz alapjelölése a/b.
Független geometriai kontroll és tényleges böngészős ívútvonal-mérés sikeres.
Mind a 13 név és teljes leírás szerepel az Edge hozzáférhetőségi fájában;
az ellenőrzés a MathML-t külön kezeli a KaTeX rejtett rétegeitől.

Végleges böngésző/axe: **18 nézet, 0 elrendezési és szabályjelzés**.
Nyomtatás JS be/ki **6/6**, 13 ábra/leírás látható; JS nélkül is olvashatók.
13 mobilos ábra és három nyomtatási minta szemrevételezve.
jsdom **121 képlet, 6/6 kvíz, 0 hiba**; teljes kánon/link **310/0**.
Részletes lektor, megőrzés, matematikai és numerikus kontroll:
[A3 hetedik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasó, a többi komplex ábra, szolgáltatói médiafelületek,
képes hátterek teljes kézi kontrasztja és JS nélküli képlet-felolvasás hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**


## Tizenegyedik adag — 1e/05 sokszögek és kör, transzformációk, vektorok, 9 ábra (2026-10-06)

Három tananyag kilenc SVG-je látható, teljesebb leírást kapott aria-describedby
kapcsolattal: hatszög átlói, középponti és kerületi szög, Thalész-tétel,
eltolás, tükrözés és forgatás, irányított szakasz és a két vektorösszeadási szabály.
A közös világos ábrakártyák maradtak; oldalankénti CSS-kivétel nem készült.

A Thalész-ábra derékszögjele most a két szárra illeszkedik. A forgatási körív
középpontja O, a megtartott csúcsok útját a megfelelő sugár írja le.
Független pontos geometriai és tényleges böngészős útvonal-kontroll sikeres;
a numerikus közelítés mért eltérése és 0,003-as SVG-egységű tűrése dokumentált.
Mind a kilenc név és leírás megjelenik az Edge hozzáférhetőségi fájában;
a MathML-szöveg külön ellenőrzött, a rejtett TeX/KaTeX-rétegeket elkülönítve.
Minimum leíráskontraszt 9,20:1.

Végleges böngésző/axe: **18 nézet, 0 elrendezési és szabályjelzés**.
Nyomtatás JS be/ki **6/6**, kilenc ábra/leírás látható; JS nélkül is olvashatók.
Kilenc mobilos ábrakártya és három nyomtatási minta szemrevételezve.
jsdom **152 képlet, 7/7 kvíz, 0 hiba**; teljes kánon/link **310/0**.
Részletes lektor, megőrzés és matematikai kontroll:
[A3 nyolcadik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasó, a többi komplex ábra, szolgáltatói médiafelületek,
képes hátterek teljes kézi kontrasztja és JS nélküli képlet-felolvasás hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**


## Tizenkettedik adag — 1e/07 lineáris tananyagok, öt ábra (2026-10-06)

A négy tananyag öt SVG-je teljesebb, látható leírást kapott aria-describedby
kapcsolattal: két lineáris függvény grafikonja, három megoldáshalmaz a
számegyenesen és egy egyenletrendszer két egyenese. A leírások a közös világos
ábrakártyákban vannak, oldalankénti CSS-kivétel nélkül. A grafikon tengelyeinek
eltérő egységhossza szerepel; a határpontok nyitott/zárt volta és a megoldásrész
iránya világos. Egy koordinátajelölés pontosvesszőre változott.

Két korlátlan zöld félegyenes végéről hiányzott a nyíl. A közös
számegyenes-generátorban a végtelen és a nyíl típusú végek most nyílfejet
kapnak; a két tananyagbeli SVG az eredeti adatokkal készült újra.
Hat generátorellenőrzés és az öt ábra tényleges koordinátáinak matematikai
kontrollja sikeres. Más témák korábban generált számegyenesei ebben az
adagban nem épültek újra; nyílfejeik vizsgálata a Q2 folytatásának része.

Mind az öt név és teljes leírás megjelenik az Edge hozzáférhetőségi fájában.
Az ellenőrzés a MathML-szöveget elkülöníti a rejtett TeX/KaTeX-rétegektől.
Minimum leíráskontraszt **9,20:1**. Végleges böngésző/axe:
**24 nézet, 0 elrendezési és szabályjelzés**. Nyomtatás JS be/ki **8/8**;
az öt ábra és leírás látható, a leírások JS nélkül is olvashatók.
Öt mobilos ábrakártya, egy bevezető és négy nyomtatási minta szemrevételezve.
jsdom **217 képlet, 10/10 kvíz, 0 hiba**; teljes kánon/link **310/0**.
Kulcs **4499/4499**, regressziós érzékenység **100%**.
Részletes lektor, megőrzés és matematikai kontroll:
[A3 tizedik adag](A3_nyelvi_ellenorzes.md).

Valódi képernyőolvasó, a többi komplex ábra, szolgáltatói médiafelületek,
képes hátterek teljes kézi kontrasztja és JS nélküli képlet-felolvasás hátra van.
Más böngészőt és teljes PDF-oldaltördelést nem minősítünk.
**Tanári döntés kell: nincs új kérdés.**
