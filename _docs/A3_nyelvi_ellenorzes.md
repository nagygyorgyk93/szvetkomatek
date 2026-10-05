# A3 — magyar megfogalmazás és a hétköznapi példák ellenőrzése

## Hatókör és állapot

**Jelenlegi összesítés:** az 1e/01 kilenc és az 1e/02 három tananyaglapjának
teljes nyelvi és példahitelességi ellenőrzése elkészült három adagban. A
feladatgyűjtemények, nyitóoldalak, összefoglalók és terepküldetések külön
A3-ellenőrzése, valamint a többi témakör átnézése hátra van. Az adagok alábbi
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
