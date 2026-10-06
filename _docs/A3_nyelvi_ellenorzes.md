# A3 — magyar megfogalmazás és a hétköznapi példák ellenőrzése

## Hatókör és állapot

**Jelenlegi összesítés:** az 1e mind a 38 tananyaglapjának teljes nyelvi és
példahitelességi ellenőrzése elkészült tizenegy adagban. A tizenkettedik adagban
az 1e/01 hét további lapja is átnézve és javítva: nyitóoldal, összefoglaló,
terepküldetés és négy feladatgyűjtemény. Az 1e/02–08 további lapfajtáinak,
valamint a 2e–4e osztályok teljes A3-auditja hátra van. Az adagok alábbi
adatai az egyes munkamenetek eredményei; a legfrissebb bejegyzés a végén található.

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

A teljes webhely nyelvi ellenőrzése hátra van. Az első adag három függvényes
tananyagát az alábbi második adag hat logikai és halmazos tananyaga követi.
Valódi képernyőolvasót, más böngészőt és a külső videók szövegét nem ellenőriztük.

**Tanári döntés kell: nincs új kérdés.**


## Második adag — 1e/01 logika és halmazok (2026-10-05)

### Hatókör és a bemutatott hibák

A `44658f7` revízióból, tiszta helyi `main` ágról indultunk. A helyi main és
origin/main referencia megegyezett; távoli frissítést és push-t nem végeztünk.
Hat tananyag teljes szövege, táblázatai, példái, kvízei és összefoglalói kerültek sorra:
kijelentések; logikai műveletek; következtetések és kvantorok; halmaz fogalma;
halmazműveletek; Descartes-szorzat és relációk. Ezekhez sincs aktuális builder;
a CLAUDE.md szerinti örökölt HTML-javítás készült.

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Bevezetők és átvezetők | Túlzó ígéretek és erőltetett mondatok: „soha ne lehessen becsapni”, „hat szuperképesség”, „igazi erő”, „a műveleteket bírod” | Nyelvi / fogalmi | HTML: konkrét tanulási célok, természetesebb átvezetés; a szereplők megmaradtak |
| Kijelentések | Az ismeretlen igazságértéket a nyitott mondattal összekeverhető magyarázat; a „csak behelyettesítéssel” kizárta a kvantoros lezárást | Közepes, fogalmi | HTML: egyértelmű igazságérték és a változó értékének megadása külön szerepel; a kizáró szó elhagyva |
| Logikai műveletek | „Öt művelet van” túl általános; „hamis feltételből bármi következik” félreérthető; a nullaszorzat feltétel nélküli | Közepes, fogalmi | HTML: öt itt vizsgált alapművelet; az implikáció igazságából az utótag igazsága nem következik; valós számok kimondva |
| Következtetések és kvantorok | A kvantor nem mondja meg pontosan, „hány x-re” igaz a mondat; a halmazok átvezetése tévesen jövő félévet említett | Közepes, tartalmi | HTML: minden elem / legalább egy elem; következő téma; modus ponens zárójelezése és a páratlan szám paraméterének halmaza kiírva |
| Halmaz fogalma | A szolgáltatói ajánlók és SQL túl általános példája; a rendszertani példában nem volt világos, mi az elem | Közepes, példa és fogalom | HTML: filmválogatás és meghívólista; az egyedek halmazainak részhalmazkapcsolata; elem és részhalmaz példája pontosítva |
| Halmazműveletek | A számos analógia „sosem igaz” mondata hibás; 25 focizó vagy úszó helyett 25 sportolót állított a szöveg; szitaképletek végessége hiányzott | Közepes, tartalmi | HTML: idempotencia, focizó vagy úszó tanulók, véges halmazok; konkrét példa szemléltetésként, nem általános bizonyításként |
| Relációk | Az oszthatóság rendezési példájából hiányzott a számhalmaz; a borbély helyi lakó volta kimaradt; az ekvivalenciaosztály neve magyarázat nélkül állt | Közepes, feltételhiány | HTML: pozitív egész számok, a faluban élő borbély és lehetetlenség, az osztály jelentése |
| Relációk, gyorsismétlő | A komplementer és a két De Morgan-azonosság `ov` osztályához nincs megjelenítési szabály; a felülvonások a böngészőben is hiányoztak | Magas, hibásan látszó matematika | HTML: három KaTeX-képlet, a hét felülvonás látható és a MathML-ben is szerepel |
| Nyelv és tipográfia | „Dr. Bizarr-re”, „a halmazok témakör után”, hibás záró idézőjelek | Alacsony, nyelvi | HTML: „Dr. Bizarrhoz”, „témaköre után”, magyar záró idézőjelek |

A kizáró/megengedő „vagy” példája pontosabb lett: egyetlen dolgozat jegyéről
szól. A sajtból álló Hold feltételes példája szándékos logikai szemléltetés,
megmaradt. A műveleti sorrendet az itt használt megegyezésként írjuk le,
egyenrangú műveleteknél zárójelezéssel.

Új feladat, feladat-számadat, külső adat, média és oldalankénti CSS nem készült.
A hat Venn-ábra már meglévő neve megfelelően leírja a színezett tartományt;
az ábrák és neveik változatlanok. Az `ov` jelölés teljes HTML-keresése csak
az érintett relációs lapot találta meg.

### Független lektor és matematikai kontroll

A web-verifikacio szerint a kontextus nélküli lektor kizárólag a hat tananyag
látható szövegét kapta, válaszindexek és lenyíló megoldások nélkül. **12/12**
kvízre önállóan helyes választ adott, és a lovag–lókötő példát is megoldotta:
Anna és Bea lovag. A filmválogatás, meghívólista, rendszertan és sportpélda
hiteles; a családi ebéd és az esős út megadott logikai feltételként megfelelő.
A játékos keretet nem minősítette hibának.

A biztos nyelvi és feltételpontosításai beépültek. Az újraolvasás a megváltozott
mondatokban nem talált további biztos hibát. A kivonat először elvesztette a
CSS-sel rajzolt felülvonásokat és egy sortörést; a kivonatot helyreállítottuk.
Ezután a valódi böngésző is megerősítette, hogy az `ov` felülvonásai a lapon
hiányoznak. A végső KaTeX-cserét renderpróba és képi ellenőrzés igazolta.

Független számolási kontroll: **9 teljes igazságtáblázat**, minden adatcellával;
**512 végeshalmaz-hármas** disztributivitásra, De Morganra és elemszámra;
**64 halmazpár** a Descartes-szorzat elemszámára és felcserélhetőségére.
A kilencelemű abszolútérték-reláció, a hatelemű szorzat, a hatványhalmaz és
a 25 focizó/úszó, illetve 5 egyik sportot sem űző tanuló eredménye egyezik.
Ezek kontrollok; véges példák ellenőrzését nem nevezzük általános bizonyításnak.

### Végleges ellenőrzések

- **Megőrzés 54/54:** képek, linkek, média, kvízopciók, válaszindexek,
  SVG-k, szkriptek, stílusok és horgonyok azonosak a kiinduló hat lapon.
  A backlog zárolt fejléce változatlan.
- **Böngésző:** 6 lap × 360/390/1280 px × zárt/nyitott lenyílók = **36 nézet**,
  0 oldalszintű túlcsordulás, képlethiba és JS-kivétel.
- **Axe: 36/0 szabályjelzés.** A képes hátterek kézi kontrasztvizsgálata nem
  teljes; nem állítunk teljes WCAG-megfelelőséget.
- **Venn-ábrák:** mind a hat név szerepel az Edge hozzáférhetőségi fájában.
  A mobilos Venn-komponens és a nyomtatási képe szemrevételezve.
- **Felülvonások:** a komplementerjel és a két De Morgan-képlet hét vonása
  megjelenik; a javított jelöléstáblázat és képletcsoport szemrevételezve.
- **JS nélkül:** mind a hat lap bevezető bekezdései láthatók. A képletek
  TeX alakban maradnak, nem teljes képernyőolvasós megoldás.
- **Nyomtatás:** 6 lap × JS be/ki = **12 nézet**, a vizsgált bekezdések és
  SVG-k láthatók. Teljes PDF-oldaltördelést nem vizsgáltunk.
- **Kánon és belső linkek: 310/310, 0 hiba;** a gyakorlósávok tiszták.
  Végleges jsdom: **6 lap, 256 képlet, 12/12 kvíz, 0 hiba**.
- **Kulcsteszt: 4499/4499**, a korábban telepített SymPy-val. Feladat,
  végeredmény és kulcsmodul nem változott, a regressziós érzékenységvizsgálat
  most nem ismétlődött.
- **Helyreállítás:** kép/média/háttér 0 módosítás; 334 médiaelem 139 lapon.
  Naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP. A keresőindex
  308 nem üres bejegyzéséből pontosan a hat érintett tananyag változott.

### Korlátok és folytatás

Az 1e/01 kilenc tananyaga A3 szerint átnézve; a többi 1e-tananyag és
a feladatgyűjtemények, nyitóoldalak, összefoglalók, terepküldetések hátra vannak.
Valódi képernyőolvasót, más böngészőt és a külső videók szövegét nem ellenőriztük.
Következő lehetséges adag: 1e/02 bevezetői és tananyagszövegei.

**Tanári döntés kell: nincs új kérdés.** Helyi main-commit; új ág és push nélkül.


## Harmadik adag — 1e/02 trigonometria (2026-10-05)

### Hatókör és javítások

A `4eabf6f` revízióból, tiszta helyi `main` ágról indultunk; az origin/main
helyi referenciája azonos volt. Távoli frissítés nem történt. Mindhárom tananyag
teljes szövege, lenyíló bizonyításai és megoldásai, példái és kvízei átnézve:
[szögfüggvények](../1e/02-trigonometria/tananyag-szogfuggvenyek.html),
[nevezetes szögek](../1e/02-trigonometria/tananyag-nevezetes-szogek.html),
[háromszög megoldása](../1e/02-trigonometria/tananyag-haromszog-megoldasa.html).
Ezek kézzel karbantartott 1e-lapok; a CLAUDE.md szerint közvetlenül javíthatók.

Az 1e matematika-skill kimenetei szerint hegyesszögek szögfüggvényeivel és
derékszögű háromszögek számológépes megoldásával dolgozunk. A karakterek és a
játékos keret megmaradtak. Javítás előtt a hibák táblázata bemutatva:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Bevezetők és átvezetők | Túl általános mérési ígéretek, erőltetett fordulatok; a következő szektor tévesen „hamarosan nyílik” | Nyelvi / fogalmi | HTML: konkrét célok és mérési feltételek, természetesebb átvezetők |
| Nevezetes szögek | A memóriafogás 0° és 90° szögfüggvényeit is bevezette | Tananyagi | HTML: csak 30°, 45° és 60° szerepel a fogásban; a derékszög mint geometriai fogalom megmarad |
| Nevezetes szögek | A levezetési blokkban kimaradt a 30° és 60° kotangense; a származtatott értékek definícióként szerepeltek | Fogalmi | HTML: a táblázat meglévő kotangensértékei a blokkban is szerepelnek; a két doboz tételként jelölve |
| Számológép | A negatív kitevőről és az inverz gombról szóló magyarázat félreérthető; a kerekítés köztes eredményekre is vonatkozhatott | Fogalmi | HTML: a gomb felirata, a reciprok és a teljes pontosságú köztes számolás külön szerepel |
| Magasságmérés | Téves állítás: a szemmagasság figyelembevételével nem használható derékszögű háromszög | Közepes, tartalmi | HTML: a számolt magasságkülönbséghez megfelelő feltételekkel hozzáadjuk a szemmagasságot |
| Két ábra | A szögív végpontja nem illeszkedett a szög szárára | Közepes, ábrahiba | HTML/SVG: a tényleges csúcsokból számolt végpontok és a megfelelő ívirány |
| Négy ábra | A rövid feliratból nem volt minden oldal és geometriai viszony kiolvasható | Hozzáférési hiány | Látható, kapcsolt ábraleírás; az SVG neve változatlan |

A Nap emelkedési szögének kvíze külön kéri az egész fokra kerekített választ;
az opciók és a helyes válasz indexe változatlan. A méretfüggetlenség bizonyításában
azonos nagyságú hegyesszögről beszélünk, és mind a négy oldalarány szerepel.

A történeti érdekességekből a túlzó általánosítások kikerültek. Hipparkhosznál
húrtáblázatok szerepelnek: [Otero saját oktatási feldolgozása](https://digitalcommons.ursinus.edu/triumphs_precalc/10/).
Az Everest korábbi évszámai megmaradtak; a trigonometriai felmérés történetéhez
[Mishra és munkatársai kutatása](https://insa.nic.in/writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art07.pdf)
ad kontrollt. A térképezést nem állítjuk egyetlen eljárásból álló folyamatnak.
Új feladat vagy feladat-számadat, média, CSS és JavaScript nem készült.

### Független lektor és számolás

A kontextus nélküli lektor kizárólag a három tananyag látható szövegét kapta,
lenyíló megoldások és válaszindexek nélkül. Mind a hat kvíz helyes válaszát és
az összes számos példa eredményét önállóan megerősítette. A torony- és fapéldák
a kimondott egyszerűsítésekkel odaillők. Két hiányt jelzett: a harmadik lap
önálló olvasásához a jelölések és oldalarányok emlékeztetője, illetve a kétlépéses
világítótorony-példa magassági referenciaszintje kellett. Mindkettő javítva;
az újraolvasás ezekben nem talált új biztos hibát. A szemléltető megoldások
szövege és a feladatgyűjtemény változatlan.

SymPy-kontroll: a tényleges értéktáblázat **12 cellája**, **10 azonosság**,
a 3–4–5 háromszög arányai, három pótszögpélda és a 7/2 értékű kifejezés;
**10 közelítő érték** független, `ROUND_HALF_UP` kerekítéssel.
A két szögív sugarát és végpontját a tényleges SVG-csúcsokból ellenőriztük.

### Végleges ellenőrzések

- **Megőrzés 30/30:** a képek, linkek, média, kvízopciók, válaszindexek,
  megoldások, szkriptek és stílusok változatlanok. Minden régi horgony megmaradt;
  négy egyedi ábraleírás-horgony került hozzá. Az SVG-kben csak a leíráskapcsolat
  és a két bemutatott szögív változott. A zárolt backlog-fejléc azonos.
- **Böngésző:** három lap × 360/390/1280 px × zárt/nyitott lenyílók =
  **18 végleges nézet**, 0 oldaltúlcsordulás, képlethiba és JS-kivétel.
  A lektori javítás után a harmadik lap mind a hat nézete újramérve.
- **Axe: 18/0 szabályjelzés.** A képes hátterek teljes kézi kontrasztvizsgálata
  továbbra is hátra van; ez nem teljes WCAG-igazolás.
- Mind a négy SVG neve és teljes leírása szerepel az Edge hozzáférhetőségi fájában.
  A négy mobilos ábra és a magasságmérés nyomtatási képe szemrevételezve.
- **JS nélkül:** mindhárom lap bevezetői és mind a négy ábraleírás látható.
  **Nyomtatás: 6/6** JS be/ki nézet, a vizsgált szövegek és SVG-k láthatók.
- **jsdom: három lap, 184 képlet, 6/6 kvíz, 0 hiba.**
  Teljes kánon és belső linkek **310/310, 0 hiba**; a gyakorlósávok tiszták.
- Kép/média/háttér: **0 módosítás**; változatlan 334 médiaelem 139 lapon.
  A naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP. A keresőindex
  308 nem üres bejegyzéséből pontosan e három tananyag változott.
- Feladatgyűjtemény, Végeredmény és kulcsmodul nem változott; a kulcstesztet és
  a regressziós érzékenységvizsgálatot ebben az adagban nem ismételtük.

### Korlátok és folytatás

Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés és a külső videók
szövege nem ellenőrizve. JS nélkül a képletek TeX alakban maradnak.
Az 1e/01 kilenc és az 1e/02 három tananyaga A3 szerint átnézve; a többi tananyag,
feladatgyűjtemény, nyitóoldal, összefoglaló és terepküldetés teljes A3-auditja hátra van.
Következő lehetséges adag: az 1e/03 egész és valós számok tananyagai.
**Tanári döntés kell: nincs új kérdés.** Helyi main-commit; új ág és push nélkül.


## Negyedik adag — 1e/03 egész és valós számok (2026-10-05)

### Hatókör és javítások

A `de24021` revízióból, tiszta helyi `main` ágról indultunk, egy committal az
origin/main helyi referenciája előtt; erről a tanárt tájékoztattuk. Távoli
frissítés nem történt. A négy tananyag teljes szövege, lenyíló megoldásai,
bizonyításai, példái, ábrái és kvízei átnézve:
[számhalmazok](../1e/03-egesz-es-valos-szamok/tananyag-szamhalmazok.html),
[oszthatóság](../1e/03-egesz-es-valos-szamok/tananyag-oszthatosag.html),
[számrendszerek](../1e/03-egesz-es-valos-szamok/tananyag-szamrendszerek.html),
[közelítés](../1e/03-egesz-es-valos-szamok/tananyag-kozelites.html).
Ezek kézzel karbantartott 1e-lapok; a CLAUDE.md szerint közvetlenül javíthatók.
Az 1e matematika-skill egész és valós számokról szóló kimenetei és módszertani
útmutatói adták a tantárgyi alapot. A szereplők és a játékos keret megmaradtak.

A javítás előtti hibatábla bemutatva; a lektori feltételpótlás is külön jelezve:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Számhalmaz-ábra | A −3 és 0 az N-ben, a törtek a Z-ben, az irracionális példák a Q-ban látszottak | Magas, matematikai | HTML/SVG: három felirat áthelyezése a helyes tartományba |
| Számhalmazok | Pontatlan állítások a mérésről és a számkörökben maradásról; az irracionális szám definíciója és az abszolútértékes összefüggések feltétele hiányos | Fogalmi / nyelvi | HTML: pontos állítások, valós számokra korlátozott definíció, x valós és a ≥ 0 feltétel, ekvivalenciák |
| Két tananyag | A √2 irracionalitásának és a prímek végtelenségének rövid bizonyítása hiányzott | Tartalmi hiány | HTML: a már kimondott tételekhez lenyíló bizonyítás, az 1e útmutatója szerint |
| Maradékos osztás | Nem szerepelt q és r egész volta, így a kimondott egyértelműség feltétel nélkül hamis | Közepes, matematikai | HTML: egész hányados és egész maradék; a doboz tételként jelölve |
| Prímtényezős felbontás és LKO | Az osztási eljárás nem nevezte meg a megfelelő prímosztót; az 5² hatványt kitevőnek nevezte a megoldás | Közepes, fogalmi | HTML: mindig a legkisebb prímosztóval osztunk; a megoldásban 2 a kitevő |
| Számrendszerek | Túl általános áramköri és jogosultsági állítások; a hibás számjegy és a hexadecimális jelek leírása kétértelmű | Fogalmi / nyelvi | HTML: bináris kód, konkrét RGB- és jogosultságpélda, a számjegy jele és értéke külön |
| Közelítés | A „majd” egymás utáni kerekítésre utalhatott; a páros felé kerekítés és az eltérés szerepe pontatlan | Közepes, fogalmi | HTML: külön kerekítési kérések, a két szabály elkülönítése, pontos hibafogalom |
| Oszthatóság utolsó kvíze | A kvíz a gyakorlósáv dobozába került | Megjelenési | HTML: lezáró dobozhatárok javítása |
| Három SVG | A rövid feliratból nem volt minden adat és viszony kiolvasható | Hozzáférési hiány | Látható ábraleírás és aria-describedby kapcsolat |

A százalékos átváltás szabálya a megoldás lenyitása nélkül is olvasható.
Egy téves kvízopció pontos megfogalmazást kapott: az egész és racionális számok
halmazának azonosságát állítja, az előző „A kettő ugyanaz” helyett. A helyes
válasz és az opciók sorrendje változatlan. A rövid számok oszthatósági vizsgálata,
a 0 és a negatív számok számrendszeres alakja, illetve a kvízben szereplő két
egész szám pozitív volta kiírva. A közös időpontban induló periodikus események,
a hosszúságmérés és a tudományos jelölés példái konkrétabbak. Új feladat vagy
feladat-számadat nem készült; a meglévő példák számai megmaradtak.

### Forráskontroll a hétköznapi példákhoz

A számítógépes állítások pontosításához az RGB színkódot az
[MDN hexadecimális színdokumentációja](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color),
a jogosultsági jelölést a
[GNU numerikus módokról szóló kézikönyve](https://www.gnu.org/s/coreutils/manual/html_node/Numeric-Modes.html)
támasztja alá. A kriptográfiai általánosítást egy konkrét eljárásra szűkítettük:
az [RSA szabványa](https://datatracker.ietf.org/doc/rfc8017/) különböző páratlan
prímek szorzatával adja meg a modulust. A páros felé kerekítés egyes számítási
eljárások lehetőségeként szerepel; ezt például a
[Python Decimal dokumentációja](https://docs.python.org/3/library/decimal.html)
is leírja. Az oldal példái az 5-ösnél felkerekítő szabályt követik.

A Föld–Nap távolság meglévő száma **átlagos távolságként** szerepel, a
[NASA földi adatlapjával](https://science.nasa.gov/earth/facts/) összhangban.
A vízmolekula mérete **jellemző közelítésként** szerepel: a meglévő adat
megegyezik a [membrántranszport-kutatásban közölt molekulaátmérővel](https://pmc.ncbi.nlm.nih.gov/articles/PMC9640652/).
A molekula méretének értelmezése modellfüggő, ezért a szöveg nem állít egyetlen
pontos, minden helyzetre érvényes méretet.

### Független lektor és számolás

A kontextus nélküli lektor kizárólag a négy tananyag szövegét kapta, a két új
bizonyítással, de a példák megoldásai és a válaszindexek nélkül. Mind a **kilenc
kvíz** helyes válaszát és az összes számos példa eredményét önállóan
megerősítette. A két bizonyítás helyes: a √2-nél a páratlan négyzet tulajdonsága
és az egyszerűsíthetetlenség adja az ellentmondást; a prímeknél a szorzat + 1
számnak egy új prímosztója van. Utóbbi érvelés nem állítja, hogy maga a szám
prím. A lektor a q és r egész voltára vonatkozó hiányzó feltételt és hat
megfogalmazási hibát jelzett. Mind a hét javítva; a javított kivonat újraolvasása
nem talált biztos új hibát. A százalékos átváltás és a rövid számok vizsgálatának
kiegészítését is megerősítette.

Független pontos számolás és SymPy-kontroll: tört/tizedes/százalék alakok,
gyökértékek és abszolútértékes egyenlet, maradékos osztás, prímtényezős alakok,
prím/összetett listák, LKO/LKT-példák; **501 egész szám** oszthatósági szabályai
és **900 pozitív számpár** LKO–LKT azonossága; **hat számrendszeres átváltás**
és a két ismételt osztási sor. A kerekítések Decimal-számolással,
ROUND_HALF_UP, illetve a megnevezett külön példák ROUND_HALF_EVEN szerint
ellenőrizve; a hiba és a normálalakok pontosan újraszámolva. A bizonyítások
algebrájának gépi kontrollját teljes logikai kézi és lektori olvasás egészíti ki.

### Végleges ellenőrzések

- **Megőrzés 40/40:** képek, linkek, média, válaszindexek, szkriptek és stílusok
  változatlanok. A kvízopciókban csak a bemutatott téves mondat, a meglévő
  megoldásokban csak az LKO-példa kitevőről szóló magyarázata változott.
  Minden régi horgony megmaradt; három ábraleírás és egy tétel új horgonya egyedi.
  Az SVG-kben csak három felirat koordinátája és a leíráskapcsolat változott.
  A zárolt backlog-fejléc azonos.
- **Böngésző:** négy lap × 360/390/1280 px × zárt/nyitott lenyílók =
  **24 végleges nézet**, 0 oldaltúlcsordulás, képlethiba és JS-kivétel.
  A lektori módosítások után mind a négy lap újramérve. A számhalmaz-ábra
  feliratainak tényleges teljes befoglaló téglalapja mindhárom szélességen a
  megfelelő tartományban van, és nem metszi a kizárandó belső halmazt.
- **Axe: 24/0 szabályjelzés.** A képes hátterek teljes kézi kontrasztvizsgálata
  továbbra is hátra van; ez nem teljes WCAG-igazolás.
- Mindhárom SVG neve és teljes leírása szerepel az Edge hozzáférhetőségi fájában.
  A három mobilos ábra és a számhalmaz-ábra nyomtatási képe szemrevételezve.
- **JS nélkül:** mind a négy lap bevezetői és mindhárom ábraleírás látható.
  **Nyomtatás: 8/8** JS be/ki nézet, a vizsgált szövegek és SVG-k láthatók.
- **jsdom: négy lap, 246 képlet, 9/9 kvíz, 0 hiba.**
  Teljes kánon és belső linkek **310/310, 0 hiba**; a gyakorlósávok tiszták.
- Kép/média/háttér: **0 módosítás**; változatlan 334 médiaelem 139 lapon.
  A naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP. A keresőindex
  308 nem üres bejegyzéséből pontosan e négy tananyag változott.
- Feladatgyűjtemény, Végeredmény és kulcsmodul nem változott; a kulcstesztet és
  a regressziós érzékenységvizsgálatot ebben az adagban nem ismételtük.

### Korlátok és folytatás

Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés és a külső videók
szövege nem ellenőrizve. JS nélkül a képletek TeX alakban maradnak.
Az 1e/01 kilenc, az 1e/02 három és az 1e/03 négy tananyaga A3 szerint átnézve;
a többi tananyag, feladatgyűjtemény, nyitóoldal, összefoglaló és terepküldetés
teljes A3-auditja hátra van. Következő lehetséges adag: az 1e/04 arányosság
három tananyaga. **Tanári döntés kell: nincs új kérdés.**
Helyi main-commit; új ág és push nélkül.


## Ötödik adag — 1e/04 arányosság (2026-10-06)

### Hatókör és javítások

A munka október 5-én indult a `9918338` revízióból, tiszta helyi `main` ágon,
két committal az origin/main helyi referenciája előtt; erről a tanárt
tájékoztattuk. A lezárás október 6-án történt. Távoli frissítés nem volt.
A három tananyag teljes szövege, lenyíló megoldásai, példái és kvízei átnézve:
[arány és arányosság](../1e/04-aranyossag/tananyag-arany-es-aranyossag.html),
[százalék és keverék](../1e/04-aranyossag/tananyag-szazalek-es-keverek.html),
[kamatszámítás](../1e/04-aranyossag/tananyag-kamatszamitas.html).
Ezek kézzel karbantartott 1e-lapok; builder nem tartozik hozzájuk, a CLAUDE.md
szerint közvetlenül javíthatók. Az 1e matematika-skill kimenetei és az
arányosság módszertani útmutatója adta a tantárgyi alapot. A kimenetek az
egyszerű kamatra helyezik a hangsúlyt; a meglévő kamatoskamat-rész és kvíze
megmaradt, de kiegészítő anyagként szerepel.

A javítás előtt bemutatott hibatábla:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Egymás utáni százalékváltozás | A +50%, majd −40% után drágább árat állított | Magas, hibás következtetés | HTML: az 1,5 · 0,6 = 0,9 szorzó szerint az ár alacsonyabb |
| Fogyásos példa | Az eredmény helyes, de az indoklás rossz alapértékre hivatkozott; az „eredményesség” célja nem egyértelmű | Közepes | HTML: műhelyi készletváltozás, ugyanazokkal a számokkal; a második százalék alapja a csökkent készlet |
| Arányossági próba | A fordított arányosságnál is állandó hányadost keresett | Közepes, fogalmi | HTML: egyenesnél hányados, fordítottnál szorzat |
| Aránypár, arányos osztás | Hiányzó feltételek; arányszámot tényleges értéknek nevezett | Fogalmi | HTML: nem nulla nevezők, pozitív osztandó és arányszámok; közös számú arányrész |
| Munkavégzés, tapéta, keverés | A modellek feltételei hiányosak | Fogalmi | HTML: egyenlő teljesítmény, felosztható munka, azonos tekercsméret; térfogat- és hőmérsékletmodell feltételei |
| Kamatszámítás | Az éves kamatláb, a futamidő és a tőkésítés kapcsolata hiányos | Fogalmi | HTML: közvetlen év/hónap/nap képletek, állandó éves kamatláb és év végi tőkésítés |
| Kamatos kamat | Nem volt világosan jelölt kiegészítés az 1e kimeneteihez képest | Tananyagi | HTML: a meglévő rész és kvíz kiegészítő jelölése |
| Bevezetők, átvezetők | Túlzó ígéretek és erőltetett fordulatok | Nyelvi | HTML: konkrétabb, természetesebb magyarázat |

Hangya Henrik és Darázs Dorka, illetve a játékos keret megmaradt.
A térképes példa légvonalbeli távolságot számol. A pénzváltás rögzített
árfolyamú, díjmentes modell; a töltéses példa független, egyenletes munkát és
elegendő töltőt feltételez. A testsúlyos helyzet helyett készletváltozás
szerepel: a meglévő 72 kg, 8%, 10% és 72,864 kg változatlan. Minden meglévő
feladat-számadat és helyes kvízválasz megmaradt. Új feladat nem készült.
Az éves, havi és napi kamatképlet egymás alatt jelenik meg, hogy mindhárom
telefonon is rögtön látható legyen; oldalankénti CSS-kivétel nincs.

### Forráskontroll és a modellek határai

A hitelajánlatok összevetésénél a díjak és az EKS szerepének rövid megnevezése
a [Szerb Nemzeti Bank fogyasztói tájékoztatójával](https://tvojnovac.nbs.rs/sr-Latn-RS/finansijski_proizvodi/krediti)
összhangban szerepel: a névleges kamatláb önmagában nem adja meg a hitel
teljes költségét. A példák díj- és adómentes, állandó kamatlábú számítási
modellek; a 360 napos számítási év választott modell, valódi ajánlatnál a
megadott napszámolást is ellenőrizni kell. A megtartott H0, 1:87 modellvasút-
példa méretarányát a [Märklin termékútmutatója](https://static.maerklin.de/damcontent/1d/0b/1d0bb9033af154bb5c58fa8989c7bff11655100549.pdf)
is megadja.

Az alkohololdatoknál térfogatszázalék és ideális térfogat-összeadódás szerepel.
A vízkeverés azonos sűrűséget és fajhőt, elhanyagolt hőveszteséget és
térfogatváltozást feltételez. Ezek kimondott modellek, nem a tényleges
folyadékkeverés feltétel nélküli állításai. Az általános keverési szabály
nemnegatív részmennyiségeket és pozitív összmennyiséget kér; eltérő
összetevőjellemzőknél egyértelmű a felbontás. Két pozitív mennyiségnél az
eredmény szigorúan a két jellemző közé esik. Azonos jellemzőkből az arány
nem határozható meg, más céljellemző pedig nem érhető el.

### Független lektor és számolás

A web-verifikacio skill szerint kontextus nélküli lektor csak a három lap
szövegét kapta, a példák lenyíló megoldásai és válaszindexek nélkül.
Mind a **nyolc kvíz** helyes válaszát és minden számos példát önállóan
megerősített; a kvízek a saját lapjuk alapján megválaszolhatók.
Négy biztos pontosítása beépítve: a keverési szabály feltételei, az egyenes
arányosság nem nulla szorzója a megadott tartományban, az „a G : P” névelő,
illetve a századrész/ezredrész írásmód. A fordított százalékos mondat is
egyértelműbb. A javított részek újraolvasásakor nem talált biztos hibát.

A független pontos és SymPy-számolás ellenőrizte az aránypárt, a két
összekapcsolt arányt, az arányos osztást, térképet, tapétát, munkavégzést,
töltést; a százalék- és ezrelékszámítást, eredeti árakat, egymás utáni
változásokat, területváltozást és mindkét keverést. Az egyszerű kamat
év/hónap/nap képlete és a kamatos kamat példái is helyesek.
A két hibás magyarázat javult: +50%, majd −40% → 0,9-szeres ár;
72 · 0,92 · 1,10 = 72,864 kg → a kezdetinél több készlet.

### Végleges ellenőrzések

- **Megőrzés 30/30:** képek, linkek, média, kvízopciók, válaszindexek,
  szkriptek, stílusok és minden régi horgony változatlan. A meglévő
  megoldásszövegekben kizárólag a bemutatott arányrész-magyarázat és a
  készletpélda változott. E három lapon nincs SVG.
- **Böngésző:** három lap × 360/390/1280 px × zárt/nyitott lenyílók =
  **18 végleges nézet**, 0 oldaltúlcsordulás, képlethiba és JS-kivétel.
  A három futamidőképlet mindhárom szélességen gördítés nélkül elfér.
- **Axe: 18/0 szabályjelzés.** A képes hátterek teljes kézi kontrasztvizsgálata
  hátra van; ez nem teljes WCAG-igazolás.
- **JS nélkül:** három lap bevezető szövege látható. **Nyomtatás: 6/6**
  JS be/ki nézetben a vizsgált szövegek és lenyíló tartalmak láthatók;
  a kvízek a kánon szerint rejtettek. A készletpélda és az árváltozás mobilos
  képe, a végleges kamatképlet-kártya és a készletpélda nyomtatási képe
  szemrevételezve.
- **jsdom: három lap, 273 képlet, 8/8 kvíz, 0 hiba.**
  Teljes kánon és belső linkek **310/310, 0 hiba**; a gyakorlósávok tiszták.
- Kép → média → háttér: **0 módosítás**; 334 aktív médiaelem 139 lapon.
  Naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP.
  A keresőindex 308 nem üres bejegyzéséből pontosan e három tananyag változott.
  A backlog zárolt fejléce változatlan, a diff-ellenőrzés tiszta.
- Feladatgyűjtemény, Végeredmény és kulcsmodul nem változott; a CLAUDE.md
  feltételes előírása szerint a kulcsteszt és a regressziós érzékenységvizsgálat
  ebben az adagban nem ismétlődött.

### Korlátok és folytatás

Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés és a külső videók
szövege nem ellenőrizve. JS nélkül a képletek TeX alakban maradnak.
Az 1e/01–04 összesen 19 tananyaga A3 szerint átnézve. A többi tananyag,
feladatgyűjtemény, nyitóoldal, összefoglaló és terepküldetés teljes A3-auditja
hátra van. Következő lehetséges adag: az 1e/05 síkgeometria tananyagai,
először az alapfogalmak, a háromszögek és a nevezetes vonalak.
**Tanári döntés kell: nincs új kérdés.** Helyi main-commit; új ág és push nélkül.


## Hatodik adag — 1e/05 geometria, első három lap (2026-10-06)

### Hatókör és javítások

Kiindulás: `cd0b66d`, tiszta helyi main, három committal az origin/main helyi
referenciája előtt; a tanár tájékoztatva. Távoli frissítés nem történt.
A három kijelölt tananyag teljes szövege, példái, bizonyítása, kvízei és ábrái
átnézve: [alapfogalmak](../1e/05-geometria/tananyag-alapfogalmak.html),
[háromszögek](../1e/05-geometria/tananyag-haromszogek.html),
[nevezetes pontok](../1e/05-geometria/tananyag-nevezetes-pontok.html).
Ezek kézzel karbantartott 1e-lapok; builder nem tartozik hozzájuk, a CLAUDE.md
szerint közvetlenül javíthatók. Az 1e matematika-skill bevezető geometriai és
egybevágósági kimenetei adták az alapot: pontos geometriai nyelv, kölcsönös
helyzetek, háromszögtulajdonságok és egyszerű bizonyítások.

Javítás előtt bemutatott hibák, valamint a később jelzett lektori pontosítások:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Háromszögfajták SVG-je | A „szabályos” háromszög oldalai eltérő hosszúak voltak | Közepes, ábrahiba | HTML/SVG: a felső csúcs magassága a megtartott alapból pontosan számolva |
| Külső szög SVG-je | A szögív nem a megfelelő szárak között futott; az α felirat a belső szögön kívül volt | Magas, ábrahiba | HTML/SVG: az ív végpontja a ferde oldalon, a teljes α-felirat a háromszög belsejében |
| Alapfogalmak | Összemosta a definíciót és a bizonyítást; a szakasz végpontjainak szerepe hiányos | Fogalmi / nyelvi | HTML: fogalom–állítás és definíció–axióma–tétel különbség; mindkét végpont a szakasz része |
| Hétköznapi példák | Feltétel nélküli „sosem billeg”, illetve „legerősebb alakzat” állítások | Fogalmi | HTML: merev lábú állvány és sík talaj; rögzített hosszú rudakból álló háromszög |
| Háromszögek | A külső szög mellékszög-kapcsolata és a transzformációk összetétele hiányzott | Közepes | HTML: közös 180°-os összeg; eltolás/forgatás/tükrözés egymás utáni alkalmazása |
| Bevezetők és lezárások | Erőltetett „rejtett pont”, „stabilizálás” és „minden titok” fordulatok | Nyelvi / fogalmi | HTML: konkrét tanulási cél és következő lépés |
| 11 ábra | A rövid névből/feliratból nem minden elrendezés és kapcsolat derült ki | Hozzáférési hiány | Látható, aria-describedby kapcsolatú teljesebb leírás; két leírás közös világos kártyán |
| Nevezetes pontok első kvíze | A szükséges fogalmak és a helyzettáblázat előtt szerepelt | Közepes, didaktikai | HTML: a kvíz a magyarázat után került |
| Lektori nyelvi jelzések | Végpontok száma/utalása, választott szögtartomány, „nagyobbik” viszonyítása és „belső” szögfelezők | Fogalmi / nyelvi | HTML: egyértelmű mondatok; egy kvízopcióban is „belső” szerepel |

A szereplők és a játékos keret megmaradtak. A háromszög leírása három nem
kollineáris csúcsból indul ki; a négy nevezetes pont nem feltétlenül különböző,
szabályos háromszögben egybeesnek. A magasságvonal egyenes, a magasságszakasz
a csúcs és a talppont közötti szakasz. A körközéppontokról szóló táblázat
szövege teljesebb. A derékszögű ábra leírása a derékszöggel szemközti oldalt
nevezi átfogónak. Új feladat vagy feladat-számadat nem készült; a példák
számai, eredményei és a meglévő bizonyítás változatlanok.

### Példahitelesség, független lektor és számolás

A rácsos szerkezetes példa a háromszög geometriai merevségét mondja ki,
a rudak változatlan hosszát feltételezve. Hidak és daruk példáit, valamint a
merev háromszögelemek modelljét az
[Albertai Egyetem statikai tananyaga](https://engcourses-uofa.ca/books/statics/structural-analysis/analysis-of-trusses/)
is bemutatja. A tananyag nem állít általános teherbírási rangsort.
Az állványpélda három pont síkmeghatározására épül, kimondott geometriai
feltételekkel; a „sosem” általánosítás és a kvíz ilyen visszajelzése eltűnt.

A web-verifikacio skill szerint kontextus nélküli lektor kizárólag a három
tananyag szövegét kapta, példamegoldások és válaszindexek nélkül.
Mind a **hat kvíz**, a két számos példa és az egyenlő szárú háromszög
alapszögeinek állítása helyes. A lektor utóbbit önálló OOO-bizonyítással
igazolta; a meglévő OSO-bizonyítás kézi olvasással és algebrai kontrollal
helyes. A kvíz előreolvasási hibája és a biztos nyelvi pontosítások beépítve.
Újraolvasáskor a sorrendet és a javított részeket megfelelőnek találta;
utolsó „velük szemközti” jelzése is javítva a javasolt átfogóleírásra.

Független pontos/SymPy-kontroll: 2:3:4 szögarány → 40°, 60°, 80°;
120° külső szög mellé 60°; az eredeti három oldalhármas és a 4–5–10 cm-es
szerkeszthetőségi példa; a súlypont és a beírt kör középpontja belül,
a körülírt kör középpontja és a magasságpont helyzete mindhárom szögtípusnál.
A szabályos háromszögben mind a négy pont egybeesése is ellenőrizve.

A 11 SVG tényleges koordinátái ellenőrizve: egyenlő szárak, szabályos oldalak,
merőleges befogók, szögösszeg, külső ív végpontja, két egyenes metszése és
párhuzamossága; a körök egyenlő csúcstávolságai/oldaltávolságai és középpontjai,
oldalfelező merőlegesek, súlyvonalak felezőpontjai és 2:1 osztása. A régi
kör- és súlypontkoordináták eltérése 0,1 SVG-egységen belül van; a szabályos
háromszög oldalhosszai egymilliomod egységen belül egyenlők.
A SymPy körsugarának pontsorrendtől függő előjelét az ellenőrzés kezeli.

### Végleges ellenőrzések

- **Megőrzés 33/33:** képek, linkek, média, helyes válaszindexek, szkriptek,
  stílusok, példamegoldások és a bizonyítás változatlan. Egy kvízopcióban
  „belső” szögfelezők szerepelnek; sorrend és helyes válasz változatlan.
  Két kvíz visszajelzésében a bemutatott feltétel/megnevezés pontosult.
  Minden régi horgony megmaradt, 11 új ábraleírás-horgony egyedi.
  Az SVG-kben csak a két bemutatott geometriai javítás és leíráskapcsolatok változtak.
- **Böngésző:** három lap × 360/390/1280 px × zárt/nyitott lenyílók =
  **18 végleges nézet**, 0 oldaltúlcsordulás, képlethiba és JS-kivétel.
  A külső ív teljes útvonala a megfelelő középpontú köríven fut;
  végpontja a ferde oldalon, az α-felirat teljes téglalapja belül van.
  Minden SVG-felirat a saját viewBox-ában elfér.
- **Axe: 18/0 szabályjelzés.** A képes hátterek teljes kézi kontrasztvizsgálata
  hátra van; ez nem teljes WCAG-igazolás.
- A 11 ábra neve és leírása az Edge hozzáférhetőségi fájában szerepel.
  A képletes leírások összevetése a MathML szövegét használja, nem a KaTeX
  rejtett és látható rétegeinek összevont, többszörös DOM-szövegét.
  A 11 mobilos ábra és három nyomtatási ábraminta szemrevételezve.
  A világos kártyák leírásszövegének mért legkisebb kontrasztja **9,20:1**.
- **JS nélkül:** három lap bevezetője és mind a 11 ábraleírás látható.
  **Nyomtatás 6/6** JS be/ki nézet: a vizsgált szövegek, lenyíló tartalmak,
  SVG-k és leírások láthatók; a kvízek a kánon szerint rejtettek.
- **jsdom: három lap, 135 képlet, 6/6 kvíz, 0 hiba.**
  Teljes kánon és belső linkek **310/310, 0 hiba**; gyakorlósávok tiszták.
- Kép → média → háttér: **0 módosítás**, 334 médiaelem 139 lapon.
  Naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP.
  A keresőindex 308 nem üres bejegyzéséből pontosan e három tananyag változott.
  A backlog zárolt fejléce azonos, a diff-ellenőrzés tiszta.
- Feladatgyűjtemény, Végeredmény és kulcsmodul nem változott; a CLAUDE.md
  feltételes előírása szerint kulcsteszt és regressziós érzékenységvizsgálat
  ebben az adagban nem ismétlődött.

### Korlátok és folytatás

Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés és a külső videók
szövege nem ellenőrizve. JS nélkül a képletek TeX alakban maradnak.
Az 1e/01–04 19 tananyaga és az 1e/05 első három lapja A3 szerint átnézve;
az 1e/05 további hat tananyaga és a többi lapfajta külön A3-auditja hátra van.
Következő lehetséges adag: tér és távolság, szögek, négyszögek.
**Tanári döntés kell: nincs új kérdés.** Helyi main-commit; új ág és push nélkül.


## Hetedik adag — 1e/05 tér, szögek és négyszögek (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `e4ca92e`, tiszta helyi main, az origin/main helyi referenciájával
egyező állapot. Távoli frissítés nem történt. Három kézzel karbantartott lap teljes
szövege, példái, hat kvíze és 13 SVG-je átnézve:
[tér és távolság](../1e/05-geometria/tananyag-ter-es-tavolsag.html),
[szögek](../1e/05-geometria/tananyag-szogek.html),
[négyszögek](../1e/05-geometria/tananyag-negyszogek.html).
Builder nem tartozik hozzájuk; a CLAUDE.md szerint közvetlenül javíthatók.
Az 1e matematika-skill geometriai kimenetei adták az alapot: kölcsönös helyzetek,
pontos geometriai nyelv, négyszögek tulajdonságai és alkalmazásuk valós helyzetben.

Javítás előtt bemutatott hibák, valamint az utólagos biztos lektori jelzések:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Térbeli távolság | A rajz kitérő éleinek összekötő normálisát lapátló irányúnak nevezte; szakaszt mondott távolságnak és közös normálisnak | Magas, fogalmi | HTML: az összekötő él, a szakaszhossz és a normális egyenes megkülönböztetve |
| Egyenes és sík | Nem volt egyértelmű, mely ponton átmenő egyenesekre kell merőlegesnek lennie | Fogalmi | HTML: a döféspont és az ott átmenő síkbeli egyenesek kimondva |
| Metsző síkok ábrája | Egy sarok a viewBox-on kívülre esett | Közepes, ábrahiba | SVG: a keret 160 helyett 180 egység magas; geometria változatlan |
| Hegyes- és tompaszög ábrája | Az ív nem a megfelelő szárra érkezett, és nem pontosan a szög csúcsa körül futott | Közepes, ábrahiba | SVG: a megtartott csúcs, szár és sugár alapján számolt végpontok |
| Szögek | A csúcsszöget kizárta a kiegészítő szögek közül; a nyolc transzverzális szögre mindig kétféle nagyságot állított | Magas, fogalmi | HTML: a derékszögű eset is szerepel |
| Szögkapcsolatok, lektori jelzés | A merőleges szárú szögek síkbeli feltétele és a váltószögek két különböző metszéspontja hiányzott | Magas, feltételhiány | HTML: közös sík és eltérő metszéspontok kimondva |
| Transzverzálisos példa | Társszöget kért egy tetszőleges keletkező szögre, miközben a definíció belső szögekről szól | Közepes, feltételhiány | HTML: az eredeti 112° egy belső szög, számadat és eredmény változatlan |
| Négyszögek | „Egyetlen adatból az összes többit” hamis általánosítás; a vizsgált konvex eset nem volt kimondva | Fogalmi / nyelvi | HTML: tulajdonságokból hiányzó adatok keresése, konvex eset és csúcssorrend |
| Trapéz, lektori jelzés | A befoglaló definíció mellett az egyenlő szár és a tengelyes szimmetria nem ekvivalens | Magas, feltételhiány | HTML: szimmetrikus trapéz tengely szerinti meghatározása; a ferde paralelogramma kivétele |
| Trapéz ábrája | Az alapok a és c jelűek voltak a jelöléskánon a és b jelölése helyett | Jelölési | SVG és leírás: a, b alapok; az érintőnégyszög külön meghatározott körbejárási jelölése megmaradt |
| Bevezetők és példák | Túlzó stabilitási és „minden eldől” állítások, mérőrudas fordulat, eltérő mentor-nevek | Nyelvi / példahitelességi | HTML: konkrét tanulási célok; doboz, fordulás, ablak/képernyő és belmagasság |
| 13 ábra | Rövid feliratokból nem állt össze a teljes kapcsolat | Hozzáférési hiány | Látható, kapcsolt részletes ábraleírások |

A szereplők és a játékos keret megmaradtak; a térlecke lezárásában is Vanda és
Fürge Pjotr szerepel. A radarpélda helyett egy téglatest alakú szoba belmagassága
szemlélteti a párhuzamos síkok távolságát, kimondott vízszintes padlóval és
párhuzamos mennyezettel. A ferde testátló ettől eltérő hosszúság. A belső kör
az oldalszakaszokat érinti; a deltoid szimmetriaátlója a megadott csúcsjelöléshez
kötve szerepel. Új feladat és új feladat-számadat nem készült.

### Független lektor és matematika

A kontextus nélküli lektor csak a három tananyag szövegét és ábraleírásait kapta,
példamegoldások és válaszindexek nélkül. A hat kvíz válaszát önállóan megerősítette:
nem feltétlenül párhuzamosak; kitérők; 63°; 50°; minden négyzet rombusz; 70°.
A négy példát újraszámolta: 53° és 143°; 112°, 112°, 68°; 75°; AB = 23.
A belmagasság, doboz, ablak és képernyő példáját megfelelőnek találta.
Négy biztos feltételpontosítás és két biztos nyelvi javítás beépítve.
A javított bekezdések újraolvasásakor nem talált biztos hibát vagy új félreértést.

A húrnégyszög és az érintőnégyszög megfordítása konvex négyszögre helyes,
ezek megmaradtak. Elsődleges kontroll:
[A. F. Beardon: Pitot’s theorem, dynamic geometry and conics, The Mathematical Gazette](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/pitots-theorem-dynamic-geometry-and-conics/3E40A70B857EEEAAC5A6FDBAB4BF419B).

Pontos/SymPy-kontroll: mind a négy számos példa; a téglatest háromdimenziós modellje
és a tényleges SVG-vetülete, kitérő élek és közös normális; merőleges távolság
minimuma; szögfajták, két ív végpontja és sugara; metsző egyenesek és két
transzverzális metszéspont; paralelogramma átlófelezése, párhuzamos oldalai;
trapézalapok és alapjelölések; rombusz/deltoid tulajdonságok szimbolikusan.
A régi húrkör csúcs-sugártávolságainak kerekítési hibája 0,5 SVG-egységen,
az érintőkör oldal-távolságainak hibája 0,1 egységen belüli, a vonalvastagságnál
kisebb; ezek a rajzok nem módosultak. A húrkör szemközti szögösszege és a
Pitot-összeg az eredeti kerekítéseknek megfelelően ellenőrizve.

### Végleges ellenőrzések

- **Megőrzés 33/33:** képek, linkek, média, kvízopciók, válaszindexek,
  szkriptek, stílusok, példamegoldások és kvízvisszajelzések változatlanok.
  Minden régi horgony megmaradt, 13 új leíráshorgony egyedi.
  Az SVG-kben csak két ív, egy rajzkeret, egy alapjel és leíráskapcsolatok változtak.
- **Böngésző:** három lap × 360/390/1280 px × nyitott/zárt lenyílók =
  **18 nézet**, 0 oldaltúlcsordulás, képlethiba és JS-kivétel.
  Minden SVG-felirat a rajzkeretén belül van. A síkábra csúcsai is elférnek.
  A két szögív tényleges útvonala a megfelelő szögtartományban fut, végpontja
  a száron van. Az analitikus sugár/végpont hibája egymilliomod egység alatti.
  Az Edge útvonal-lekérdezésének numerikus közelítése külön, 0,002 SVG-egységes
  tűréssel ellenőrzött; a kezdeti 0,001-es jelzés mérési közelítésből adódott,
  nem új ábrahibából.
- **Axe 18/0:** nincs jelzett szabályhiba. Ez nem teljes WCAG-igazolás.
  Mind a 13 ábra neve és teljes leírása az Edge hozzáférhetőségi fájában szerepel.
  A képletes leírások összevetése a MathML szövegét használja a KaTeX rejtett
  rétegeivel megsokszorozott DOM-szöveg helyett.
- Mind a **13 mobilos ábra** és három nyomtatási ábraminta szemrevételezve.
  A világos ábrakártyák leírásszövegének legkisebb mért kontrasztja 9,20:1.
- **JS nélkül:** három bevezető és 13 leírás látható.
  **Nyomtatás 6/6**, JS be/ki: a vizsgált szövegek, lenyílók, SVG-k és leírások
  láthatók; a kvízek a kánon szerint rejtettek.
- **jsdom:** három lap, **121 képlet, 6/6 kvíz, 0 hiba**.
  Teljes kánon és belső linkek **310/310, 0 hiba**; gyakorlósávok tiszták.
- Kép → média → háttér: 0 módosítás; 334 médiaelem 139 lapon.
  Naplótérkép változatlan: 184 oldal, 2294 feladat, 12315 XP.
  A keresőindex 308 nem üres bejegyzéséből pontosan e három tananyag változott.
  Backlog zárolt fejléce azonos; diff-ellenőrzés tiszta.
- Feladatgyűjtemény, Végeredmény és kulcsmodul változatlan: a CLAUDE.md
  feltételes előírása szerint kulcsteszt és regressziós érzékenységvizsgálat
  ebben az adagban nem ismétlődött.

### Korlátok és folytatás

Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés, a képes hátterek
teljes kézi kontrasztja és külső videók szövege nem ellenőrizve.
JS nélkül a képletek TeX alakban maradnak.
Az 1e/01–04 19 tananyaga és az 1e/05 első hat lapja, összesen 25 tananyag A3
szerint átnézve. Az 1e/05 további három tananyaga és a többi lapfajta külön
A3-ellenőrzése hátra van. Következő adag: sokszögek és kör, transzformációk, vektorok.
**Tanári döntés kell: nincs új kérdés.** Helyi main-commit; új ág és push nélkül.


## Nyolcadik adag — 1e/05 sokszögek és kör, transzformációk, vektorok (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `6e19421`, tiszta helyi main, az origin/main helyi referenciájával
egyező állapot. Távoli frissítés nem történt. Három kézzel karbantartott tananyag
teljes szövege, négy példája, hét kvíze és kilenc SVG-je átnézve:
[sokszögek és a kör](../1e/05-geometria/tananyag-sokszogek-es-kor.html),
[egybevágósági transzformációk](../1e/05-geometria/tananyag-transzformaciok.html),
[vektorok](../1e/05-geometria/tananyag-vektorok.html).
A builderkeresés csak hivatkozásokat talált; a CLAUDE.md szerint a kézi lapok
közvetlenül javíthatók. Az 1e matematika-skill egybevágósági kimenetei az alap:
körök és sokszögek tulajdonságai, síkbeli izometriák, lineáris vektorműveletek,
pontos matematikai nyelv és valós alkalmazás.

Javítás előtt bemutatott hibák és az utólagos biztos lektori feltételpontosítás:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Kör, első kvíz | A kerületi szög tételét a tananyag még nem tanította, amikor rákérdezett | Közepes, sorrendi | HTML: a kvíz a tétel és a hozzá tartozó példa után került |
| Kör, ív és szög | Az „ugyanezen az íven” összekeverhette a szög csúcsának helyét az átfogott ívvel; a bevezető nem nevezte meg, mit látunk szög alatt | Közepes, fogalmi | HTML: ugyanazt az ívet átfogó szögek; húr és a húr egyik oldalán mozgó körvonalpont |
| Kör és sokszög alapfogalmai | Az átló, körlap, érintő egyenes, kerületi szög szára és a külsőszögszámolás feltétele hiányos | Fogalmi | HTML: meghatározások, különböző végpontok, sugárnyi távolság és konvex eset, csúcsonként egy külső szög |
| Thalész-ábra | A forgatott téglalap nem illeszkedett a két szögszárra | Közepes, ábrahiba | SVG: a meglévő körvonalpont pontosítása, a két szárból számított derékszögjel |
| Forgatás ábrája | A csúcs útját jelző ív sugara nem felelt meg a csúcs középponttól mért távolságának, az ív középpontja eltért O-tól | Magas, szemléltetési | SVG: az eredeti forgatás megtartása, pontos képcsúcsok és O középpontú körív |
| Tükrözés és forgatás | A felezőmerőleges/forgatási szög a tengelyen vagy a középpontban lévő pontra is megfogalmazódott; ismétlődő és nehézkes forgatásmagyarázat | Közepes, feltételbeli / nyelvi | HTML: a rögzített pont külön esete, irányított szög, pozitív és negatív forgatási irány |
| Szimmetriák | Az egyenlő szárú háromszögre egy tengelyt, minden téglalapra/rombuszra kettőt mondott, a szabályos és négyzetes kivétel nélkül | Magas, fogalmi | HTML: nem szabályos háromszög 1, szabályos 3; négyzettől különböző téglalap/rombusz 2, négyzet 4 tengely |
| Szabályos sokszög forgatása, lektori jelzés | A forgatási középpont nem szerepelt | Feltételhiány | HTML: a csúcsokon átmenő kör középpontja; az ötszögkérdésben is megnevezve |
| Vektor | Egy konkrét irányított szakasszal azonosította a vektort; több irányállítás a nullvektort sem zárta ki | Fogalmi | HTML: irányított szakaszos ábrázolás, helytől független vektor, nemnulla feltételek; nullvektor ellentettje önmaga |
| Paralelogramma-szabály | A nem egy egyenesbe esés a vektorok helyétől függő feltételnek volt olvasható | Közepes, félreértés | HTML: előbb közös kezdőpont, majd az ábrázoló szakaszokra mondott feltétel |
| Bevezetők, alkalmazások | Túlzó „tökéletes szimmetria”, „teljes mozgás”, a videojáték sosem torzul és a navigáció csak utat összegez állítás | Nyelvi / példahitelességi | HTML: konkrét célok, csempeminta, feltételes logópélda, papírsablon, indulópontba visszatérő séta |
| Kilenc ábra | Rövid feliratok nem írták le az összes geometriai kapcsolatot | Hozzáférési hiány | Látható részletes leírás és aria-describedby kapcsolat |

A játékos keret, Vanda és Fürge Pjotr megmaradtak. Az elmozdulás és a megtett
út megkülönböztetése konkrét kezdő-/végpontra vonatkozik. Az identitás jelentése
ki van írva; a k valós szám külön mondatban szerepel. A körszögek tétele
a félkörnél hosszabb ívhez tartozó középponti szöget is pontosan kezeli.
Új feladat és új feladat-számadat nem készült; a példák számai és eredményei
változatlanok. A geometriai rajzkoordináták javítása a meglévő ábrákhoz kötött.

### Független lektor és matematika

A kontextus nélküli lektor csak a három tananyag látható szövegét és leírásait kapta,
példamegoldások és válaszindexek nélkül. A hét kvíz önálló válasza: 40°, 60°,
nem nulla eltolásnál nincs fix pont, tengelyes tükrözés, 72°, azonos hossz és irány,
AB = −BA. Mind megoldható a tananyagból. A négy példa önálló eredménye:
13 oldal / 65 átló / 1980°; 20°; 62°; DC = −m−n, BA = m+n, BC = n−m, CA = 2m.
A csempeminta, szimmetrikus logó, papírsablon és körbesétálás helyénvaló.
A középpont megnevezése, paralelogrammafeltétel és biztos nyelvi pontosítások
beépítve. Újraolvasáskor a lektor nem talált biztos hibát vagy új félreértést.

Független SymPy/pontos kontroll:

- Átlók nem szomszédos csúcspárok szerinti leszámlálása n = 3–18 esetén;
  a három számos példa, kvízszámolások és a paralelogramma négy vektorának helyvektoros levezetése.
- Nullvektor ellentettje és skalárszorosa, számszoros hosszának négyzete,
  ellentettek összege; a két összeadásábra tényleges nyilai.
- Eltolás és tükrözés képcsúcsai, oldaltávolságok és körüljárás; a forgatás
  három képcsúcsa és O-tól mért távolsága egymilliomod SVG-egységen belül pontos.
- A körív két lehetséges középpontja a végpontokból és sugárból számolva:
  a megfelelő középpont O, az analitikus eltérés egymilliomod egység alatti.
- Thalész-körvonalpont és merőlegesség, a két szár egységvektorából számított
  derékszögjel. A megtartott hatszög és középponti/kerületi ábra korábbi
  koordinátakerekítése vonalvastagságnál jóval kisebb eltérésű.
- Szimmetriatengelyek és középponti szimmetria pontos ponttükrözéssel:
  nem szabályos egyenlő szárú / szabályos háromszög, nem négyzet téglalap /
  rombusz, négyzet, ferde paralelogramma.

Megőrzési ellenőrzés **33/33**: képek, linkek, médiablokkok, kvízopciók és
válaszindexek, szkriptek, stílusok, példamegoldások és régi horgonyok megmaradtak.
Négy kvízvisszajelzés megfogalmazása a fent dokumentált ív-/vektorpontosítással
változott. Kilenc új leíráshorgony egyedi. Hét SVG geometriai tartalma változatlan,
csak a Thalész- és forgatásábra alakzata/jelölése változott.

### Végleges ellenőrzés

| Réteg | Eredmény |
|---|---|
| Kép → média → háttér | 0 módosítás; 334 aktív médiaelem 139 lapon |
| Naplótérkép | Változatlan: 184 oldal, 2294 feladat, 12315 XP |
| Keresőindex | 308 nem üres bejegyzés; pontosan a három tananyag változott |
| Teljes kánon | 310 oldal, 0 hiba |
| Belső linkek és horgonyok | 310 oldal, 0 hiba |
| Gyakorlósávok | 0 hiba |
| jsdom, három módosított lap | 152 képlet, 7/7 kvíz, 0 render-/JS-hiba |
| Edge, 360/390/1280 px, zárt/nyitott lenyílók | 18 nézet, 0 oldaltúlcsordulás, képlethiba vagy JS-kivétel |
| axe, ugyanez a 18 állapot | 0 jelzett szabálysértés |
| Hozzáférhetőségi fa | Mind a 9 ábranév és teljes, MathML-től helyesen kivont leírás szerepel |
| JS nélkül | Három bevezető és mind a 9 leírás olvasható |
| Nyomtatási stílus, JS be/ki | 6/6; szövegek, lenyílók, ábrák és leírások láthatók; kvízek rejtettek |
| Szemrevételezés | Kilenc mobilos ábrakártya és három nyomtatási ábraminta rendben |

A leírások a közös világos ábrakártyákban vannak; minimum mért kontraszt
**9,20:1**. A tényleges forgatási körív 21 mintapontja, kezdő-/végpontja
és szögtartománya mindhárom szélességen ellenőrzött. Az Edge numerikus
getPointAtLength közelítésének első jelzését 101 pontos diagnosztika tisztázta:
0,002477 SVG-egység maximális sugáreltérés, dokumentált 0,003-as mérési tűrés.
Az SVG-körív analitikus középpontja és végpontjai ettől függetlenül pontosak;
a diagnosztika miatt nem változtattuk meg a geometriai tartalmat.

Feladatgyűjtemény és Végeredmény nem változott. A CLAUDE.md feltételes előírása
szerint a kulcs- és regressziós teszt ebben az adagban nem ismétlődött.
Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés, képes hátterek
teljes kézi kontrasztja és külső videók/appletek tartalma nem ellenőrizve.
JS nélkül a képletek TeX alakban maradnak. A gépi axe-próba és hozzáférhetőségi
fa nem jelent teljes WCAG-minősítést vagy felolvasási próbát.

**Állapot:** az 1e/05 mind a 9 tananyaga teljes A3-audit szerint átnézve;
az 1e/01–05 összesen 28 tananyaglapja kész. Következő tananyag-adag az
1e/06 három racionális algebrai leckéje. A többi lapfajta külön A3-auditja hátra van.
**Tanári döntés kell: nincs új kérdés.** Helyi main; új ág és push nem készült.


## Kilencedik adag — 1e/06 racionális algebrai kifejezések (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `12e4b52`, tiszta helyi main, az origin/main helyi referenciájával
egyező állapot. Távoli frissítés nem történt. Három kézzel karbantartott tananyag
teljes szövege, 15 kidolgozott példakártyája és 9 kvíze átnézve:
[polinomok](../1e/06-racionalis-algebrai-kifejezesek/tananyag-polinomok.html),
[szorzattá alakítás](../1e/06-racionalis-algebrai-kifejezesek/tananyag-szorzatta-alakitas.html),
[algebrai törtek](../1e/06-racionalis-algebrai-kifejezesek/tananyag-algebrai-tortek.html).
A builderkeresés csak hivatkozásokat talált; a CLAUDE.md alapján a kézi 1e lapok
közvetlenül javíthatók. Egyik lapon sincs saját SVG-ábra. Az 1e matematika-skill
racionális kifejezésekre vonatkozó kimenetei adták az alapot: algebrai átalakítások,
a négyzet nemnegativitása és a számtani–mértani közép kapcsolata.

Javítás előtt bemutatott hibák és a későbbi biztos lektori pontosítás:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Polinom, fokszám | A rendezett alak csak sorrendként szerepelt; a nulla együtthatójú tagok elhagyása és a fokszám előtti összevonás hiányzott | Közepes, fogalmi | HTML: összevonás, nulla tagok elhagyása, nemnulla polinom/egytag feltétele; nemnegatív egész kitevők |
| Polinomosztás | A nemnulla osztó feltétele és az egyváltozós kör nem szerepelt | Közepes, feltételhiány | HTML: mindkét feltétel kimondva, a kivonási lépés is megnevezve |
| Bézout | Az x−a osztót mindig binomnak nevezte, az a=0 esetet is | Enyhe, fogalmi | HTML: elsőfokú polinom; a maradéktétel tartalma megmaradt |
| Szorzattá alakítás, csapda és kvíz | Minden négyzetösszeg felbonthatatlanságát állította | Közepes, hibás általánosítás | HTML és két visszajelzés: a különbségazonosság alkalmazási köre; konkrétan x²+9 nem bontható valós együtthatós, elsőfokú tényezőkre |
| Kiemelés, LKO és LKT | Minden együtthatóra számbeli LKO-t mondott; a konstans szorzó és a főegyüttható választása nem szerepelt | Fogalmi | HTML: egész együtthatóknál számbeli LKO; egyváltozós nemnulla polinomok, az LKO/LKT 1 főegyütthatóval megadva |
| Törtek, bevezető | A nemnulla nevező feltételét nevezte értelmezési tartománynak; a lefagyást általános következménynek állította | Közepes, fogalmi / példahitelességi | HTML: valós változóértékek halmaza; út/idő átlagsebesség-példa pozitív időtartammal |
| Egyszerűsítési képlet | Az ac/bc=a/b mellől hiányzott b≠0 | Közepes, feltételhiány | HTML: b≠0 és c≠0; az eredetileg kizárt értékek megmaradásának szabálya |
| Összeadás | Minden közös nevezőt az LKT-vel azonosított, miközben a képlet a nevezők szorzatát használta | Közepes, fogalmi | HTML: a nevezők szorzata is megfelel; az LKT gyakran egyszerűbb választás |
| Emeletes tört, utolsó mondat | Az „ezeken a helyeken nincs értelmezve” az előző nemegyenlőségekre is utalhatott | Közepes, kétértelmű | HTML: az x−y csak a fenti kikötésekkel az eredeti tört egyszerűsített alakja |
| Kitekintés | A számtani–mértani közép kapcsolatát csak említette, képlet nélkül | Kisebb kimeneti hiány | HTML: a meglévő kitekintésben a nemnegatív feltétel, két közép képlete, rövid négyzetes indoklás és egyenlőségeset |
| Bevezetők, átvezetők, összefoglaló | „Bármilyen bonyolult”, „legegyszerűbb”, „egyetlen szabály mindenre”, tisztogatás és legmagasabb szint túlzásai | Enyhe–közepes, nyelvi | HTML: konkrét tanulási célok, rendezett és szorzatalak eltérő használata; rövidebb magyar mondatok |

Krats Ynot, Iruhs, Kán és a játékos keret megmaradtak. A szorzatalak megnevezése
egybeírva szerepel. Az összeg négyzetének téves képlete és a betűk törlése
azonosságként hibás, a szöveg nem állít minden helyettesítési értékre egyenlőtlenséget.
A kitekintés címe nem keveredik a törtek bővítésének műveletével. A korábbi
emelt/nem kötelező besorolás és az ellenőrzőre vonatkozó közlés megmaradt;
a középegyenlőtlenséghez nem készült gyakorlófeladat vagy új számpélda.

### Független lektor és matematikai kontroll

A kontextus nélküli lektor csak a három lap tanulói szövegét kapta, a kidolgozott
példák megoldásai, a válaszindexek és a kvíz-visszajelzések nélkül. Önállóan
megoldotta mind a 15 példakártyát és a 9 kvízt; minden eredmény egyezik a lappal.
Egyik feladathoz sem kellett találgatnia. A nyelvet követhetőnek ítélte.
Két feltételt kért kimondani: a maradékos osztás és az LKO/LKT egyváltozós
polinomokra vonatkozik. Mindkét biztos pontosítás beépítve.

Független SymPy-kontroll:

- A polinom helyettesítési értéke, fokszáma, főegyütthatója és az összes
  kidolgozott összevonás, szorzás, hatványozás, rendezés és maradékos osztás.
- Az összes tényezőkre bontás, LKO/LKT, nevezetes azonosság mindkét iránya,
  csoportosítás; az x²+9 valós gyökhalmaza üres.
- A törtek kizárt nevezőértékei, a kivonás/szorzás/osztás/összeadás képletei,
  az összetett tört belső nevezői és teljes nevezőjének x+y számlálója.
- A nem egyszerűsíthető törtek polinom-LKO-ja 1; a hibás törlési képlet nem azonosság.
- a²+b²−2ab=(a−b)²; nemnegatív a,b esetén a+b−2√(ab)=(√a−√b)²;
  a két közép kapcsolatának egyenlőségesete.
- Mind a kilenc kvíz matematikai eredménye; a megmaradt válaszindexek helyesek.

Megőrzési ellenőrzés **30/30**: képek, linkek, média, válaszopciók/indexek,
szkriptek, stílusok és az összes régi horgony változatlan. A 15 példakártya
számadatai, képletei, eredményei és kikötései változatlanok; csak az emeletes
tört utolsó prózamondatának dokumentált pontosítása tér el. Két kvíz-visszajelzés
a négyzetek különbségére vonatkozó magyarázattal pontosult. Új feladat,
feladat-számadat, oldalankénti CSS vagy médiablokk nem készült.

### Végleges ellenőrzés

| Réteg | Eredmény |
|---|---|
| Kép → média → háttér | 0 módosítás; 334 aktív médiaelem 139 lapon |
| Naplótérkép | Változatlan: 184 oldal, 2294 feladat, 12315 XP |
| Keresőindex | 308 nem üres bejegyzés; pontosan a három tananyag változott; a késői közép- és kikötésszöveg is bekerült |
| Teljes kánon | 310 oldal, 0 hiba |
| Belső linkek és horgonyok | 310 oldal, 0 hiba |
| Gyakorlósávok | 0 hiba |
| jsdom, három módosított lap | 185 képlet, 9/9 kvíz, 0 render-/JS-hiba |
| Edge, 360/390/1280 px, zárt/nyitott lenyílók | 18 nézet, 0 oldaltúlcsordulás, képlethiba, JS-kivétel, saját konzolhiba vagy helyi 404 |
| axe, ugyanez a 18 állapot | 0 jelzett szabálysértés |
| JS nélkül | Három lecke bevezetői és törzsszövege olvasható |
| Nyomtatási stílus, JS be/ki | 6/6; törzsszöveg, bevezetők és megoldáslenyílók láthatók; kvízek rejtettek |
| Szemrevételezés | Három mobilos bevezető és három nyomtatási dobozminta rendben |

Feladatgyűjtemény és Végeredmény nem változott; a CLAUDE.md feltételes szabálya
szerint a teljes kulcs- és regressziós teszt ebben az adagban nem ismétlődött.
A tananyag példáit és kvízeit a fenti két független matematikai kontroll vizsgálta.
Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés, képes hátterek
teljes kézi kontrasztja és külső videók/appletek tartalma nem ellenőrizve.
JS nélkül a képletek TeX alakban maradnak. Az axe-próba nem teljes WCAG-minősítés.

**Állapot:** az 1e/06 mindhárom tananyaga teljes A3-audit szerint átnézve;
az 1e/01–06 összesen 31/38 tananyaglapja kész. Következő tananyag-adag az
1e/07 négy lineáris leckéje. A többi lapfajta és osztály külön A3-auditja hátra van.
**Tanári döntés kell: nincs új kérdés.** Helyi main; új ág és push nem készült.


## Tizedik adag — 1e/07 lineáris függvények, egyenletek és rendszerek (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `4e0478f`, tiszta helyi main, az origin/main helyi
referenciájával egyező állapot. Távoli frissítés nem történt. Az 1e/07 mind a négy
kézzel karbantartott tananyaglapjának teljes szövege, 13 példakártyája,
10 kvíze és öt SVG-je átnézve:
[lineáris függvények](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-linearis-fuggveny.html),
[lineáris egyenletek](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-linearis-egyenletek.html),
[egyenlőtlenségek](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-egyenlotlensegek.html),
[egyenletrendszerek](../1e/07-linearis-egyenletek-es-rendszerek/tananyag-egyenletrendszerek.html).
Az egyik példakártya két nyíltan kidolgozott rendszert tartalmaz.
A builderkeresés csak hivatkozásokat talált; a CLAUDE.md szerint a kézi
tananyagok közvetlenül javíthatók. A két számegyenes hiányzó nyílfejét
előállító közös `_tools/builders/abra_common.py` is javult.

Az 1e matematika-skill kimenetei az alap: lineáris egyenletek és paraméteres
eseteik, egyenlőtlenségek, lineáris függvények ábrázolása/elemzése,
szöveges feladatok modellezése és értelmezése legfeljebb három ismeretlennel.
A háromismeretlenes részt lépésenkénti kiküszöbölésként nevezzük meg;
a Gauss-elnevezés és a korábbi példa megmaradt, mátrixos anyag nem került be.

Javítás előtt bemutatott hibák és a későbbi biztos lektori pontosítások:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Egyenlet, ekvivalens átalakítás | Tetszőleges kifejezés hozzáadásához nem szerepelt értelmezhetőségi feltétel | Közepes, feltételhiány | HTML: az eredeti értelmezési tartomány minden pontján értelmezett kifejezés; a kizárt értékek megmaradása |
| Egyenlőtlenség | A negatív közös nevezőt LKT-nek nevezte; néhány előjel- és értelmezési feltétel hiányzott | Közepes, fogalmi | HTML: pozitív közös nevező; a nemszigorú relációk, nulla és ismeretlenes osztó külön feltételei |
| Lineáris függvény | Az ábrázolási pontválasztás és a paraméter egyértelmű meghatározása túl általános volt | Közepes, fogalmi | HTML: két különböző pont; tengelymetszetek és paraméter feltételes használata |
| Rendszerek, modellezés | A kiküszöbölés mindig egy ismeretlent ígért; minden szöveges feltételt egyenletté tett | Közepes, túláltalánosítás | HTML: egyetlen megoldású rendszer feltétele a kvízben is; a megmaradó egyenlet és további modellkorlátok szerepe |
| Két korlátlan megoldásrész | A zöld félegyenesek végéről hiányzott a nyílfej | Közepes, ábra | Eszköz és HTML: közös generátor javítása, a két meglévő SVG újragenerálása azonos adatokkal |
| Öt ábra | A rövid leírások nem közölték mindenütt a grafikont és a határpontok szerepét; egy koordinátajelölés nem a kánont követte | Közepes, hozzáférhetőség / enyhe jelölés | HTML: látható, kapcsolt leírások; pontosvesszős koordináták |
| Bevezetők és lezárások | Túlzó, körülményes vagy a módszereket elmosó megfogalmazások | Enyhe, nyelvi | HTML: rövidebb mondatok, konkrét tanulási cél és következő lépés |
| Megoldásszám csapdadoboza | A 0=13 ellentmondás előjele eltért a feltüntetett −2-szerezésből és összeadásból kapott 0=−13-tól | Enyhe, következetlenség | HTML: az előjel egyezik a kidolgozott példával; a nincs megoldás következtetés helyes marad |
| Számegyenes prózája | A határpontot a karikával azonosította | Enyhe, nyelvi | HTML: a határpontot karika jelöli; nyitott/zárt végpont szerepe világos |

A játékos keret és szereplők megmaradtak. A panziópélda életszerű:
14 szoba és 34 férőhely mellett 6 háromágyas és 8 kétágyas szoba adódik.
A kérdés a két szobatípus számára kérdez rá; a számadatok változatlanok,
a nemnegatív egész darabszám feltétele kimondva. Nincs új feladat vagy új
feladat-számadat. Az egyenesgrafikon két tengelyén eltérő az egység hossza;
a leírás ezért a koordinátákból való meredekségolvasásra figyelmeztet.

### Független lektor és matematikai kontroll

A kontextus nélküli lektor csak a tanulói szöveget és ábraleírásokat kapta,
a példák kidolgozása, kvíz-válaszindexek és visszajelzések nélkül. A nyíltan
kidolgozott két rendszerből is csak az egyenleteket látta. Mind a 13 példakártyát
és a 10 kvízt önállóan helyesen megoldotta; az öt ábraleírás állításai helyesek,
a panziópélda reális. Lényegi hibát nem talált. A fenti két biztos lektori
pontosítás beépítve; a végleges négy lap utána újra ellenőrizve.

SymPy-kontroll: minden lineáris és törtes példaszámítás, paraméter,
intervallum, két- és háromismeretlenes rendszer, panziómodell, két elfajuló
rendszer megoldásszáma, valamint mind a 10 kvíz. Az öt SVG tényleges
koordinátái visszaszámolva: egyenesek képletei, metszéspontok, határpontok,
nyitott/zárt karikák és nyílirányok. A függvénygrafikon eredeti egytizedes
SVG-kerekítésének legnagyobb eltérése 0,10 SVG-egység, a 0,20-as tűrésen belül.
A közös számegyenes-generátor hat esete ellenőrzött: bal/jobb végtelen,
kétirányú folytatás, véges nyitott/zárt intervallum és a nyíl végponttípus.

Megőrzési kontroll **44/44**: képek, linkek, média, válaszopciók/indexek,
szkriptek, stílusok és minden régi horgony megmaradt. Öt új, egyedi leíráshorgony.
A példamegoldások változatlanok az egy számhármas pontosvesszős jelölésén kívül;
egy Gauss-kvíz hibás válaszának magyarázata a feltétellel pontosult.
Az SVG-koordináták változatlanok: csak két nyílfej, leíráskapcsolatok és egy
koordinátajelölés módosult. Oldalankénti CSS-kivétel nem készült.

### Végleges ellenőrzés

| Réteg | Eredmény |
|---|---|
| Kép → média → háttér | 0 módosítás; 334 aktív médiaelem 139 lapon |
| Naplótérkép | Változatlan: 184 oldal, 2294 feladat, 12315 XP |
| Keresőindex | 308 nem üres bejegyzés; pontosan a négy lecke változott; mind a négy lezárás késői szövege indexelve |
| Teljes kánon és belső linkek | Mindkettő 310 oldal, 0 hiba |
| Gyakorlósávok | 0 hiba |
| jsdom, négy lecke | 217 képlet, 10/10 kvíz, 0 render-/JS-hiba |
| Edge, 360/390/1280 px, zárt/nyitott lenyílók | 24 nézet, 0 túlcsordulás, képlethiba, JS-kivétel, saját konzolhiba vagy helyi 404 |
| axe, ugyanez a 24 állapot | 0 jelzett szabálysértés |
| Ábraleírások | Öt teljes név és leírás az Edge hozzáférhetőségi fájában; látható mindhárom szélességen, minimum kontraszt 9,20:1 |
| JS nélkül | Négy lecke bevezetői, törzsszövege és mind az öt ábraleírás olvasható |
| Nyomtatási stílus, JS be/ki | 8/8; szöveg, megoldáslenyílók, öt ábra és leírás látható; kvízek rejtettek |
| Szemrevételezés | Öt mobilos ábrakártya, egy mobilos bevezető és négy nyomtatási minta rendben |
| Teljes kulcsteszt | 4499/4499, 0 eltérés |
| Regressziós érzékenység | 4499/4499, 100% |

A tízlépéses lánc hibátlan; a két lektori prózapontosítás után a kulcsok
előtti nyolc lépés, az önálló matematikai és az összes böngészős próba
ismét lefutott. A kulcs- és regressziós próba azonos feladatgyűjteményeken
futott; ezek, a Végeredmények és a kulcsmodul nem változtak.

A közös generátor javítása a később készülő számegyenesekre is érvényes.
Más témák korábban generált SVG-jeit ebben az adagban nem építettük újra;
ezek nyílfejeinek célzott vizsgálata Q2-folytatás. Valódi képernyőolvasó,
más böngésző, teljes PDF-oldaltördelés, képes hátterek teljes kézi kontrasztja
és külső média tartalma nem ellenőrizve. JS nélkül a képletek TeX alakban
maradnak; az axe-próba nem teljes WCAG-minősítés.

**Állapot:** az 1e/07 4/4 tananyaga teljes A3-audit szerint átnézve;
az 1e/01–07 összesen 35/38 tananyaglapja kész. Következő adag:
az 1e/08 három hasonlósági leckéje. A többi lapfajta és osztály külön
A3-auditja hátra van. **Tanári döntés kell: nincs új kérdés.**
Helyi main; új ág és push nem készült.


## Tizenegyedik adag — 1e/08 hasonlóság; az 1e tananyagok lezárása (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `7a76885`, tiszta helyi main, az origin/main helyi referenciájával
egyező állapot. Távoli frissítés nem történt. Három kézzel karbantartott tananyag
teljes szövege, három példakártyája, hat kvíze és három SVG-je átnézve:
[arányos szakaszok](../1e/08-hasonlosag/tananyag-aranyos-szakaszok.html),
[homotécia és hasonlóság](../1e/08-hasonlosag/tananyag-homotecia-es-hasonlosag.html),
[háromszögek hasonlósága](../1e/08-hasonlosag/tananyag-haromszogek-hasonlosaga.html).
A builderkeresés csak más leckék hivatkozásait találta; a CLAUDE.md szerint
ezek a kézi 1e lapok közvetlenül javíthatók. Builder nem futott újra.

Az 1e matematika-skill kimenete az alap: a hasonlóság és a középpontos hasonlóság
alkalmazása a síkban. A párhuzamos szelők és a háromszög-hasonlóság, a mérési
alkalmazás és a derékszögű háromszög tételei ehhez kapcsolódnak.
A meglévő térfogati és ponthatvány-kitekintés megmaradt, gyakorlófeladat nélkül.

Javítás előtt bemutatott hibák, majd a böngészős és lektori pontosítások:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Párhuzamos szelők ábrája | A négy metszéspont nem illeszkedett a szárakra, a szelők nem voltak pontosan párhuzamosak | Közepes, matematikai ábra | HTML: a megtartott csúcsból és szárakból számolt metszéspontok, hozzáigazított feliratok |
| Thalész-tétel és megfordítás | A pontok sorrendje hiányzott; teljes metsző egyenesekre is irányítás nélküli hosszarányokat mondott | Közepes, feltételhiány | HTML: egy szög két szárán a pontsorrend és a párhuzamos összekötők megnevezése; megfordítás ugyanebben az elrendezésben |
| Arány és szerkesztések | A pozitív hossz / nemnulla osztó nem szerepelt; a párhuzamosok meghúzásának lépései hiányosak voltak | Fogalmi / didaktikai | HTML: feltételek és végrehajtható szerkesztési lépések; negyedik arányosnál az a=b eset is |
| Hasonlósági kvízek | Az arány iránya kétértelmű, a kisebbikről a nagyobbikra mondott 2:5 arány a lecke k-konvenciójával ellentétes | Közepes, jelölés | HTML: képhossz/eredeti hossz; a másik kérdésben kisebb:nagyobb oldalhányados; helyes válaszok/indexek maradtak |
| Árnyékos mérés | A függőlegesség, vízszintes talaj és az árnyék megfelelő végpontja nem szerepelt | Közepes, modellhiány | HTML: egyidejű mérés, párhuzamos napsugarak, függőleges szakaszként modellezett fa, a csúcspont árnyéka |
| Kapcsolódás az egybevágósághoz | A két szög egyezését is az egybevágósági esetekkel mosta össze | Közepes, fogalmi | HTML: OOO/OSzO összevetés; két szög önmagában csak hasonlóságot biztosít |
| Homotéciás lecke első kvíze | Hiányzó záró div; a s3 rész és a második kvíz az első kvízbe ágyazódott | Magas, szerkezet/működés | HTML: doboz lezárása; két önálló háromopciós kvíz, a további lecke nyomtatásban látható |
| Homotécia megfogalmazása | A nagyítás/kicsinyítés nem foglalta magába a méretmegőrző eseteket | Enyhe–közepes, fogalmi | HTML: k=1 és k=−1, valós nemnulla arány; negatív aránynál irány és abszolútérték szerinti távolság |
| Bevezetők és hétköznapi kapcsolatok | „Bármit”, „minden hiányzó adat”, „mind a Thalész-elven”; körülményes túlzások | Enyhe–közepes, nyelvi | HTML: konkrét tanulási célok, méretarányos alaprajz, a mérés és a tételek feltételei |
| Három ábra | Rövid leírások; a B₁-felirat szűken fért el; a hosszú Thalész-képlet megszakadt az Edge hozzáférhetőségi leírásában | Közepes, hozzáférhetőség / enyhe tördelés | HTML: három teljes, kapcsolt leírás, B₁ igazítása; Thalész-arányok szavakkal |

A szereplők és a játékos keret megmaradtak. Az Euklideszi tételekhez a már
szereplő a,b,c,h,p,q jelölésekkel rövid hasonlósági arányok kerültek, amelyekből
a három képlet keresztbeszorzással következik. A befogóhoz tartozó szelet a
merőleges vetület hossza. A pont hatványa körön kívüli pontra, a szelő
közelebbi/távolabbi metszéspontjaival egyértelmű. Új feladat és új
feladat-számadat nem készült; a három példakártya adatai és megoldásai maradtak.

### Független lektor és matematikai kontroll

A projektkontextus nélküli lektor csak a három tanulói szöveget és leírást kapta,
példamegoldások, kvízindexek és visszajelzések nélkül. Önálló eredményei:
SB₁=9; a fa magassága 8 m; c=25, h=12, a=15, b=20. Mind a hat kvíz helyes
opciója egyezik az oldallal. A feltételezett modellben az árnyékos adatok
életszerűek; az ábraleírások állításai helyesek. A homotécia méretmegőrző
eseteiről, a negyedik arányos szerkesztéséről és a korona miatt szükséges
szakaszmodellről szóló biztos pontosításai beépítve. Az újraolvasás a
szerkesztést a<b, a>b és a=b esetben is végrehajthatónak találta;
a negatív arány mondatának k=−1-re adott utolsó javítása is beépült.

Független SymPy-kontroll minden példára, kvízre és skálázási számolásra.
A negyedik arányos általános képlete és a szerkesztés vektoros
párhuzamossága ellenőrizve, az a=b eset is. A befogó-, magasság- és
Pitagorasz-tétel arányai pozitív p,q változókkal; a külső pont szelőjének
metszési egyenletében a két távolság szorzata d²−r².

Tényleges SVG-koordinátákból, pontos racionális számolással:

- A Thalész-ábrán mind a négy pont a megfelelő száron van; a két szelő
  párhuzamos, és a három megadott hosszarány egyenlő.
- A homotécia mindhárom képcsúcsának középpontból vett vektora kétszeres;
  az oldalhosszak kétszeresek, a terület négyszeres.
- A két másik háromszög 3/2-szeres nagyítással és eltolással kapcsolódik;
  minden megfelelő oldalhányados 3/2, a területarány 9/4.

Megőrzés **33/33**: képek, linkek, médiablokkok, válaszopciók/indexek,
szkriptek, stílusok és minden régi horgony maradt. A három példamegoldás
változatlan. Három visszajelzés az arány irányával pontosult. Az SVG-kben
csak a Thalész-pontok és felirataik, egy szöveghorgony, valamint a három
leíráskapcsolat változott. A leírások a közös világos kártyákon vannak;
oldalankénti CSS-kivétel nem készült.

### Végleges ellenőrzés

| Réteg | Eredmény |
|---|---|
| Kép → média → háttér | 0 módosítás; 334 aktív médiaelem 139 lapon |
| Naplótérkép | Változatlan: 184 oldal, 2294 feladat, 12315 XP |
| Keresőindex | 308 nem üres bejegyzés; pontosan a három lecke változott; mindhárom lezárás késői szövege indexelve |
| Teljes kánon és belső linkek | Mindkettő 310 oldal, 0 hiba |
| Gyakorlósávok | 0 hiba |
| jsdom, három végleges lecke | 171 képlet, 6/6 kvíz, 0 render-/JS-hiba |
| Edge, 360/390/1280 px, zárt/nyitott lenyílók | 18 végleges nézet, 0 túlcsordulás, képlethiba, JS-kivétel, saját konzolhiba vagy helyi 404 |
| axe, ugyanez a 18 állapot | 0 jelzett szabálysértés |
| Kvízszerkezet | Nincs beágyazott kvíz vagy kvízbe került címsor; oldalanként két önálló háromopciós kérdés |
| Ábraleírások | Három teljes név és leírás az Edge hozzáférhetőségi fájában; minimum kontraszt 9,20:1 |
| JS nélkül | Három lecke szövege és mindhárom ábraleírás olvasható |
| Nyomtatási stílus, JS be/ki | 6/6; szöveg, címsorok, megoldáslenyílók, ábrák és leírások láthatók; kvízek rejtettek |
| Szemrevételezés | Három mobilos ábrakártya és három nyomtatási minta rendben |

A kiinduló homotéciás HTML valódi böngészős próbájában egy beágyazott kvíz
volt, a s3 címsor és kerület–terület doboz nyomtatáskor rejtett.
A javított HTML-ben ez megszűnt. A Thalész-képletes hosszú leírás Edge-ben
megszakadt; a szavakkal megadott változat teljes. Az első jsdom-próba
elavult segédmappa-útvonal miatt nem töltött lapot; az útvonal javítása után
mindhárom végleges lap lefutott. A homotécia legutolsó prózapontosítása után
a lecke hat böngészős/axe-nézete és két nyomtatási módja külön újramérve.

Feladatgyűjtemény, Végeredmény és kulcsmodul nem változott; a CLAUDE.md
feltételes előírása szerint a teljes kulcs- és regressziós próba nem ismétlődött.
A tananyag számításait a fenti két független kontroll ellenőrizte.
Valódi képernyőolvasó, más böngésző, teljes PDF-oldaltördelés, képes hátterek
teljes kézi kontrasztja és külső média tartalma nem ellenőrizve.
JS nélkül a képletek TeX alakban maradnak; az axe nem teljes WCAG-minősítés.

**Állapot:** az 1e/08 3/3 tananyaga kész; az 1e mind a **38/38 tananyaglapja**
teljes A3-audit szerint átnézve. A feladatgyűjtemények, nyitóoldalak,
összefoglalók, terepküldetések és a 2e–4e külön A3-auditja hátra van.
**Tanári döntés kell:** új tartalmi kérdés nincs; a következő nagyobb adag
sorrendjéről egyeztetés indult. Helyi main; új ág és push nem készült.


## Tizenkettedik adag — 1e/01 további lapfajták (2026-10-06)

### Hatókör és javítások

Kiinduló revízió: `4ba162c`, tiszta helyi main, egy committal az origin/main
helyi referenciája előtt. Távoli frissítés nem történt. A logika–halmazok–függvények
témakör hét, tananyagon kívüli lapja teljes szöveggel átnézve:
[nyitóoldal](../1e/01-logika-halmazok-fuggvenyek/index.html),
[összefoglaló](../1e/01-logika-halmazok-fuggvenyek/osszefoglalo.html),
[terepküldetés](../1e/01-logika-halmazok-fuggvenyek/terepkuldetes.html),
[logika](../1e/01-logika-halmazok-fuggvenyek/feladatok-logika.html),
[halmazok](../1e/01-logika-halmazok-fuggvenyek/feladatok-halmazok.html),
[függvények](../1e/01-logika-halmazok-fuggvenyek/feladatok-fuggvenyek.html),
[házi feladatsor](../1e/01-logika-halmazok-fuggvenyek/feladatok-hazi.html).
Összesen 132 feladatkártya: 125 gyakorlókártya és a projekt hét kártyája.
A részfeladatok ettől külön számolandók. SVG és kvíz nincs e hét lapon.

Az 1e matematika-skill 01. témakörének kimenetei az alap: pontos matematikai
nyelv, logikai és halmazműveletek, relációk, függvények, valamint az összeadási
és szorzási számlálási szabály. Új tantervi követelmény nem keletkezett.
Hat lap kézzel karbantartott; a builderkeresés nem talált hozzájuk generátort.
A házit a `build_dangerroom.py` írja: csak az első témakör forrásrésze futott
újra, a többi témakör kimenete nem változott. Utána az előírt lánc visszatette
az avatart és a hátteret. Kézzel nem illesztettünk be médiát.

Javítás előtt bemutatott hibatábla, a lektori kiegészítésekkel:

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| Nyitóoldal | A halmazos alapfeladatok és a házi szintdarabszámok elavultak; a projektkártya megoldókulcsot ígért | Enyhe | HTML: tényleges darabszámok, saját felmérést említő leírás |
| Összefoglaló | Az üres halmaz valódi részhalmazként szerepelt minden A-ra; a függvény képletében z nem volt kvantálva, a kvantorok hatóköre bizonytalan | Közepes, matematikai | HTML: részhalmazjel, külön létezési és egyértelműségi feltétel |
| Összefoglaló nyelve és jelölése | Eldönthetőség összemosása az igazságértékkel; nyitott mondatnál kötött változó is beleérthető; pontatlan Descartes-mondat, idegen idézőjelek | Közepes / enyhe | HTML: szabad változó, értelmezés, magyar idézőjel, szabályos komplementer és világos zárójelek |
| Logika alap 2, 6 és 9 | Felesleges p,q-feltétel; részben téves közös utasítás; a leves/saláta és a vezetői „vagy” kétféleképpen olvasható | Közepes, utasítás | HTML: pontos részfeladat-tartományok és konkrét választási feltételek |
| Logika alap 3, 10 és 11 | A kért magyar fordítás vagy a p,q,r jelentése hiányzott a válaszból; −3 formalizálásánál mást írt a kulcs | Közepes, hiányos válasz | HTML: a kért végső mondatok és jelölések, levezetés nélkül |
| Logika közép 10 és Joker | „Mindenkinek” önmagát is jelentette; a Joker „vagy”-ától kétféle megoldás függött | Közepes, többértelműség | HTML: minden másik hős; megengedő vagy kimondása |
| Halmazok közép 5 | Egy reláció alaphalmaza hiányzott; a kért rendezett párok nem szerepeltek a válaszban, a tulajdonságlista részleges volt | Közepes, feltétel és válasz | HTML: alaphalmaz, kilenc pár és teljes tulajdonságlista; a hosszú lista több sorba tördelve |
| Halmazos szöveges feladatok | A páronkénti létszámokról nem mondta ki, hogy tartalmazzák a hármas metszetet; a kézfogások ismétléséről nem nyilatkozott | Közepes, modell | HTML: az inkluzív létszám és a pontosan egyszeri kézfogás kimondása |
| Függvények alap 1 | Az e)–f) más halmazai is az a)–d) közös A→B kérdésébe kerültek | Közepes, típus | HTML: külön a)–d) relációk és saját halmazokon megadott e)–f) függvények |
| Függvényes modellek | Hiányzott a képletes alapértelmezés és több alkalmazás tartománya; a mobilszámla díjfajtái nem voltak kimondva | Közepes, feltétel | HTML: R→R alapértelmezés, külön alkalmazási korlátozások, egyszerű díjmodellek és az inverzek tartománya |
| Házi közép 7 és bevezető | A kód karakterfajtáinak helye nem volt rögzítve; a bevezető ismétlődött és magyartalan volt | Közepes / enyhe | Builder: két betű után két számjegy; rövidebb, természetes szöveg |
| Terepküldetés | U lehetett az egész osztály vagy csak a válaszadók; önmagára képezést kizáró hasonlat; az elitmondat számjegyek és függvényértékek összegét keverte | Közepes | HTML: válaszadók alaphalmaza, függvény pontos képfeltételei, függvényértékek összege |

Természetesebb lett a terepküldetés és a Vészterem felvezetése; a játékos
keret megmaradt. A felmérő konkrét összeállításáról szóló ellenőrizhetetlen
ígéret helyére gyakorlási útmutató került. Új gyakorlófeladat vagy új
feladat-számadat nem készült. A megtartott díjak egyszerű modellek,
nem aktuális szolgáltatói ajánlatok. A példák adatai és számszerű válaszai
megmaradtak; a hiányzó végső válaszrészek az eredeti feladatból számolva készültek.
A korábban tanári döntéssel megtartott rövid bizonyításindoklásokat ez az
A3-adag nem törölte. Terepküldetés-megoldókulcs nem került a publikus repóba.

### Független lektor és tanári pontosítás

Két projektkontextus nélküli lektor csak tanulói szöveget kapott. Az egyik
önállóan megoldotta a 31 logikai kártyát, válaszok nélkül. A másik az
összefoglaló definícióit és a projektfeladatokat vizsgálta. Az első kivonatból
kimaradt fejléc miatt jelzett N-konvenció az oldalon már szerepelt; a teljes
fejléccel megismételt kivonatban a lektor ezt igazolta. Biztos pontosításaik
beépültek; az újraolvasás nem talált új biztos matematikai hibát. A kizáró vagy
jelét az összefoglaló és a korábbi tananyag definiálja.

Az alap 1/k filmcíméről a tanár pontosított: az átnevezés szándékos.
Az átnevezett cím megmaradt; ennél a részfeladatnál csak a kijelentésként
besorolás a kérdés, az igazságértékét nem kell megadni. A válasz ehhez igazodik.
A lektor ezt önállóan megoldhatónak találta. Új tanári döntés nincs nyitva.

Független kontroll: a függvény két feltétele 31 kis véges reláción, üres
tartományokat is beleértve, pontosan az egyértékű teljes hozzárendelést adja.
A tényleges HTML-ből kiolvasott kilenc relációpár megegyezik az abszolútérték
szerint önállóan képzett párokkal; tulajdonságai ellenőrizve. SymPy igazolta a
két alkalmazási inverz képletét, a tartományhatárokat és a nemnegatív idő/út
kapcsolatát. A kódok darabszáma önálló felsorolással, a háromhalmazos
létszámok és a projekt saját számolással ellenőrizve. Projekt-eredmények csak
a repón kívüli bizonyítékban vannak. 28/28 megőrzési ellenőrzés: horgonyok,
linkek, média és kártyalisták; a 132 kártya megmaradt.

### Ellenőrzések és korlátok

| Ellenőrzés | Eredmény |
|---|---|
| Teljes kánon és belső linkek | 310 oldal, 0 hiba |
| Gyakorlósávok | Minden kártyát felad valamelyik egység |
| Teljes kulcsteszt és regresszió | 4499/4499, 0 eltérés; 100% hibafelismerés |
| Utolsó pontosítások utáni érintett kulcs és regresszió | Logika, halmazok, függvények: 145/145, 100%; a tesztelt logikai válaszblokkok változatlanok |
| jsdom / képletrender | 7 lap, 1133 képlet, 0 render- vagy JS-hiba; nincs kvíz |
| Edge mobil és asztali | Hét lap × 360/390/1280 px × zárt/nyitott válaszok: 42 végleges nézet, 0 hiba |
| axe | 42 végleges nézet, 0 jelzés; nem teljes WCAG-minősítés |
| Nyomtatás JS be/ki | 14/14: címsorok, feladatszövegek és 125 végeredmény látható; a projektnek nincs publikus lenyílókulcsa |
| JavaScript nélkül | 7/7 lap szövege olvasható; a képletek TeX alakban maradnak |
| Keresőindex | 308 nem üres bejegyzés, pontosan a hét lap változott; öt 3000. karakter utáni új részlet is benne van |
| Naplótérkép | Változatlan: 184 egység, 2294 feladat, összesen 12315 XP |
| Kép, média és háttér | A házi egy avatart és hátteret kapott vissza; 334 médiaelem/139 lap, médiaváltozás nélkül |

A lektori és tanári pontosítások után az érintett lapok célzottan újramérve;
a végleges nézetszám a legutolsó, megfelelő lapverziók összevonása. Négy
mobilos feladatkártya szemrevételezve. A relációlista öt sorban olvasható,
oldalankénti CSS-kivétel nélkül. Valódi képernyőolvasó, más böngésző,
teljes PDF-oldaltördelés, háttérképek minden pontjára végzett kézi kontrasztmérés
és külső média tartalmi ellenőrzése nem történt. A PDF-renderelő modul ebben
a futtatókörnyezetben nem volt elérhető; a nyomtatási CSS és a tartalom
láthatósága valódi Edge-ben ellenőrizve.

**Állapot:** az 1e/01 kilenc tananyaga mellé most a hét további lap A3-auditja
is elkészült. Az 1e/02–08 további lapfajtái és a 2e–4e teljes A3-auditja hátra
van. **Tanári döntés kell: nincs nyitott kérdés.** Helyi main; új ág és push
nem készült. Következő javasolt adag: az 1e/02 trigonometria további lapjai.
