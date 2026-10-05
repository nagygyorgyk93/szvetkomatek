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

## Ellenőrzési eredmények

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

## Korlátok és fennmaradó ellenőrzés

- Valódi NVDA/VoiceOver-próba nem történt. A matematikai nevek szöveges vizsgálata
  és a böngésző hozzáférhetőségi fája nem helyettesíti ezt.
- Az axe több képes/áttetsző hátterű elem kontrasztját nem tudja önállóan megítélni.
  Mind a 620 nézetnél maradt ilyen kézi ellenőrzési jelzés (`incomplete`, nem szabályhiba).
  A nyolc nézet mérése mintavétel; nem minden oldal minden görgetési helyzetének,
  ábrájának vagy állapotának kontrasztbizonyítéka.
- A főoldali köszöntővideó mindkét nézetben kézi feliratellenőrzési jelzést kapott.
  A hanghoz megfelelő felirat vagy teljes szöveges alternatíva meglétét ez az adag
  nem igazolja; ez is a Q2 fennmaradó tétele.
- A külső YouTube/GeoGebra felületek, feliratok és átiratok, illetve a teljes
  nyomtatási látvány nem kaptak új teljes ellenőrzést.
- A JavaScript nélküli statikus képletek és navigáció képernyőolvasós ellenőrzése
  külön feladat. A most hozzáadott közös kezelőfelületi nevek JavaScriptből készülnek.

**Tanári döntés kell:** nincs új tantervi vagy matematikai döntés. A valódi
képernyőolvasós próba, a további kézi kontrasztminták és a köszöntővideó feliratellenőrzése fennmaradó Q2-ellenőrzésként
szerepelnek; ezekig a backlog Q2 sora részben kész.

## A javításokhoz használt hivatalos útmutatók

Az állapotüzenetek, a kikapcsolható karakter-gyorsbillentyű és a videószünet indoka:
[W3C — Status Messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html),
[W3C — Character Key Shortcuts](https://www.w3.org/WAI/WCAG21/Understanding/character-key-shortcuts.html),
[W3C — Pause, Stop, Hide](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html).
Az automatikus eszköz forrása: [axe-core](https://github.com/dequelabs/axe-core).
