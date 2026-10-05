# A3 — magyar megfogalmazás és a hétköznapi példák ellenőrzése

## Hatókör és állapot

**2026-10-05, első adag:** az 1e/01 három függvényes tananyaglapjának teljes szövegét
átnéztük, a bevezetőktől az összefoglalóig. A tanár kérése szerint az egyértelműen
jobb megfogalmazásokat beépítettük. A tananyag játékos kerete megmaradt.
A munka a helyi `main` ágon indult, a `840f361` revízióból, tiszta munkafával és
két helyi committal az `origin/main` előtt. Új ág és push nem készült.

| Ellenőrzött lap | Nyelv és hétköznapi példák | Q2: ábraleírás |
|---|---|---|
| [A függvény fogalma és megadása](../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggveny-fogalma.html) | Átnézve, javítva | 3 ábra |
| [Függvénytulajdonságok](../1e/01-logika-halmazok-fuggvenyek/tananyag-fuggvenytulajdonsagok.html) | Átnézve, javítva | 3 ábra |
| [Kompozíció és inverz](../1e/01-logika-halmazok-fuggvenyek/tananyag-kompozicio-inverz.html) | Átnézve, javítva | 2 ábra |

Az új A3-audit **folyamatban van**. A többi tananyaglap, a feladatgyűjtemények,
a témakörök nyitóoldalai, összefoglalói és terepküldetései ebben az adagban nem
kaptak teljes nyelvi ellenőrzést. A korábbi A1-adagok nyelvi javításai nem jelentenek
minden mondatra kiterjedő stilisztikai ellenőrzést.

## Javítás előtt bemutatott hibák és a megoldásuk

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Függvény fogalma, grafikon | A teljes valós értelmezési tartományból folytonos grafikont következtetett a szöveg | Magas, hibás általánosítás | Kézzel karbantartott HTML: a mondat most a konkrét lineáris példát írja le |
| Ugyanott, SVG | Az egyenes egyik végpontja nem felelt meg az `f(x)=2x−1` képletnek | Magas, ábrahiba | SVG: az első végpont `y1=243.6` helyett `259.2`; a jelölt pontokon is átmegy |
| Bevezető példák | Az almaárhoz hiányzott a rögzített egységár; a személyi számos példa szükségtelen közigazgatási általánosításra épült; a programozási példa túl általános volt | Közepes, félreérthetőség | HTML: az ár feltételei kiírva, rögzített osztálynévsor az inverz példája; a programrész minden megengedett bemenethez egyértelmű kimenetet ad |
| Mindhárom lap, bevezetők és átvezetők | Erőltetett vagy túlzó mondatok: „függvény bújik meg”, „a behelyettesítés bármit tűr”, „ezen múlik minden”, „ami elront, azt az inverz helyrehozza” | Alacsony–közepes, nyelvi és fogalmi pontatlanság | HTML: rövidebb, konkrétabb magyarázat; a hálós metafora a tényleges hozzárendeléshez kapcsolódik |
| Kompozíció és inverz, grafikon | Az előző `2x−6` példától eltérő `2x−1` grafikonváltás nem volt kimondva | Közepes, félrevezető példaváltás | HTML: a két ábrázolt képlet és a példaváltás megnevezve |
| Inverz, jelölés és gyorsismétlő | Az inverz–reciprok különbséget pontonkénti kizárásként is lehetett olvasni; az inverzzel való felcserélhetőség eltérő halmazokon félrevezető volt | Közepes, matematikai pontatlanság | HTML: különböző függvényekről szóló mondat; az identikus kompozíciók halmazai külön szerepelnek |
| Betűcsere és mémek | A modern titkosításról szóló rész túl általános volt, a mémek képletes egyenlőségei nem definiáltak függvényt | Közepes, példa és szemléltetés | HTML: egyszerű, visszafejthető betűcsere; a mémek emlékeztetőként szerepelnek |
| Nyolc SVG | A rövid ábranév önmagában nem mondta el az összes nyilat, pontot vagy műveleti sorrendet | Közepes, hozzáférési hiány | Látható szöveges leírás és az SVG-ről `aria-describedby` kapcsolat |

A három laphoz nincs aktuális tananyag-builder: a repó eszközei csak hivatkoznak
rájuk. A CLAUDE.md szerint az ilyen örökölt 1e HTML közvetlenül javítható.
Oldalankénti CSS-kivétel, új feladat és új külső számadat nem készült. A meglévő
képletek, halmazok, pontok és nyilak adatait tettük pontosabbá és szövegesen
hozzáférhetővé.

## Független nyelvi és matematikai lektor

A web-verifikacio skill előírása szerint kontextus nélküli lektor csak a három lap
szövegét kapta meg: projektfájl, kánon, válaszindex és a kvíz utáni levezetés nélkül.
A természetes magyar megfogalmazást és a hétköznapi példákat megfelelőnek találta.
Az almaár, a rögzített névsor, a hőmérséklet-átváltás és a betűcsere hihető példa.
A játékos keret és a mémek maradhatnak.

A biztos pontosításait beépítettük:

- Az inverzes és kompozíciós példákban szerepelnek az érintett halmazok.
- A reciprokfüggvénynél kiírtuk a kizárt bemenetet.
- A függvényegyenlet minden valós bemenetre teljesül.
- Két függvény csak megfelelő bemenetek és kimenetek esetén kapcsolható sorba.
- A bijektív véges példában az egész kodomén minden elemének előfordulásáról szól a mondat.
- A betűcserében „különböző betűknek különböző képe” szerepel.
- Az inverz kiszámításakor a „fejtsd ki” helyett „fejezzük ki y-t” áll.

A négy kvíz önálló válasza a meglévő helyes opcióval egyezik: 4., 2., 4., 4.
A lektor újraszámolta a behelyettesítéseket, a két lineáris kompozíciót,
a véges kompozíciót és inverzt, valamint a függvényegyenletet; eltérést nem talált.
A lektorálás után pontosított mondatok külön új lektorkört nem kaptak, a végső
változatot újramértük a böngészőben és a képletrenderelővel.

## Ellenőrzések

- **Megőrzés 22/22:** a képek bájtjai, linkek, médiablokkok, kvízopciók és
  válaszindexek azonosak; a régi horgonyok megmaradtak; mind a nyolc leírás létező,
  egyedi elemhez kapcsolódik. A backlog zárolt fejléce változatlan.
- **Grafikonok:** hat végpont koordinátáját a SVG-ből, decimális aritmetikával
  számoltuk vissza; a végpontok és a jelölt pontok a megadott egyeneseken vannak.
  A véges kompozíció és inverz külön számolási kontrollja is egyezik.
- **Végleges böngészős mérés:** három lap × 360/390/1280 px × zárt/nyitott
  lenyílók = **18 nézet**, 0 túlcsordulás, képlethiba és JS-kivétel.
- **Axe:** **18 vizsgálat, 0 szabályjelzés**. A képes háttérhez maradt kézi
  kontraszt-ellenőrzési jelzés; teljes WCAG-megfelelőséget nem állítunk.
- **Ábraleírások:** mind a nyolc látható mindhárom szélességen. Az Edge
  hozzáférhetőségi fájában mind a nyolc kép rendelkezik névvel és leírással.
  Az inverz grafikonjának szövege a törtet szóban is egyértelműen leírja:
  a bemenethez egyet adunk, majd kettővel osztunk.
- **JS nélkül:** három lap, mind a nyolc leírás látható. A képletek ilyenkor
  TeX alakban maradnak; ezt nem minősítjük teljes képernyőolvasós megoldásnak.
- **Nyomtatási nézet:** három lap × JS be/ki = **6 sikeres próba**, a leírások
  láthatók. Mobilos ábrák és nyomtatási komponenskép szemrevételezve.
  Teljes PDF-oldaltördelést nem vizsgáltunk.
- **Kánon és linkek:** **310/310, 0 hiba**, a gyakorlósávok tiszták.
  A végső három lap külön jsdom-próbája: **200 képlet, 4/4 kvíz, 0 hiba**.
- **Kulcsteszt:** **4499/4499**, eltérés nélkül, a korábban telepített SymPy-val.
  A feladatok, végeredmények és kulcsmodulok nem változtak; a regressziós
  érzékenységvizsgálatot ebben az adagban nem ismételtük.
- **Helyreállítás és indexek:** kép/média/háttér 0 módosítás; változatlan 334
  médiaelem 139 lapon. Naplótérkép változatlan: 184 oldal, 2294 feladat,
  12315 XP. A 308 oldalas keresőindexből csak a három érintett URL változott.

## Korlátok és következő adag

A teljes webhely nyelvi ellenőrzése hátra van; ez három tananyaglap lezárt adaga.
Folytatásként az 1e/01 logikai és halmazos lapjain érdemes ugyanezt a nyelvi,
példahitelességi és ábraleírási ellenőrzést elvégezni.
Valódi képernyőolvasót, más böngészőt és a külső videók szövegét nem ellenőriztük.

**Tanári döntés kell: nincs új kérdés.**
