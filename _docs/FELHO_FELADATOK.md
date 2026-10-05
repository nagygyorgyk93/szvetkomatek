# Felhős feladatlista (backlog) — Szvetkó matek

Ez a fájl **a repó része** (nem tükör): a felhős munkamenetek innen dolgoznak, és a munka
végén **ugyanabban a PR-ben** frissítik a státuszt. Jelek: ☐ nincs kezdve · ◐ folyamatban /
részben · ☑ kész (PR merge-elve) · ⛔ zárolt.

## Indítás (a tanár ezt írja a felhős munkamenet elejére)

> Olvasd el a CLAUDE.md-t és a _docs/FELHO_FELADATOK.md-t. Végezd el a(z) **M1** feladatot a
> **2e** osztályra. Egy PR-t nyiss, a végén frissítsd a státusztáblát.

Egy munkamenet = **egy feladat × egy osztály** (vagy egy témakör, ha az osztály túl nagy).

## Zárolt területek ⛔

| Mi | Miért | Meddig |
|---|---|---|
| Új feladat / új számadat bármely gyűjteményben | felmérő-ütközés felhőben nem ellenőrizhető | mindig — javaslatként a PR-be |
| `_docs/workflow.md`, `jelolesek.md`, `tortenet/`, tükrözött skillek | a tanár gépéről frissülnek | mindig |

## Helyben elvégzendő (felhőből átadva) 🖥️

Amit a felhős munkamenet zárolt terület miatt nem végezhetett el, de javasolt. Helyben (Cowork / a
tanár gépén) elvégezve töröld a sort.

Jelenleg nincs ilyen tétel. (A 4e-s pilot `meret` mezőjét a tanár engedélyével felhőben pótoltuk, 2026-09-28.)

---

## M — Média

### M1 · Oktatóvideók (MNT Távoktatás) a tananyag-egységekhez
**Cél:** témakörönként a legjobban illő magyar nyelvű videós órák beágyazása, szakaszhoz kötve.
**Hogyan:** `media-beagyazas` skill. Osztály ↔ MNT: 1e ↔ I., 2e ↔ II., 3e ↔ III., 4e ↔ IV. osztály.
**Elfogadás:** minden tananyag-egységnél megvizsgálva (akkor is, ha nem került be videó — a PR-ben
egy sor: „nincs jó találat”); `media.py --online` 0 hiba; `verify_web` + `layout_teszt` tiszta.

| 1e | 2e | 3e | 4e |
|---|---|---|---|
| ☑ 85 videó 30 lapon (mind a 38 egység megvizsgálva; 8 lap videó nélkül; egy videó csak egy helyen) — 2026-09-28 | ☑ 78 videó 32 lapon (mind a 35 egység megvizsgálva; 3 lap tanári döntéssel videó nélkül) — #1, 2026-09-27 | ☑ 80 videó 41 lapon (mind az 50 egység megvizsgálva; 9 lap videó nélkül) — 2026-09-28 | ◐ 67 videó 35 lapon; mind a 38 egység megvizsgálva, 3 lap videó nélkül; helyi commit, publikálásra vár — 2026-10-03 |

**4e/05 M1 (2026-10-03, helyi main):** a kombinatorika öt egységének videódöntése: [`M1_4e_05_attekintes.md`](M1_4e_05_attekintes.md). Tíz új IV. osztályos MNT-videó került fel a permutáció, variáció, kombináció és binomiális tétel lapjára; a binomiális pilot megmaradt. A szorzási és összeadási szabály lapjához nincs igazolt jó találat. Az ismétléses kombinációról szóló 53. óra nem illik a lapra. `media.py --online`: 278/278; kánon 10/0, linkek 310/0, sáv tiszta, kulcsteszt 4499/4499, regresszió 4499/4499 = 100%; a négy módosult lap 360/390/1280 px-en rendben. A jsdom, a nyomtatási látvány és a valódi képernyőolvasós próba nem futott; a videókat nem néztem végig.

**4e/06 M1 (2026-10-03, helyi main):** a hét valószínűségi és statisztikai egység döntési táblája: [`M1_4e_06_attekintes.md`](M1_4e_06_attekintes.md). Tizennégy új MNT-videó került fel a hét lapra; a geometriai valószínűség, a teljes valószínűség, Bayes, az eloszlásfüggvény és a Gauss-eloszlás órái M2-n kívüliek, ezért kimaradtak. `media.py --online`: 292/292; kánon 13/0, linkek 310/0, sáv tiszta, kulcsteszt 4499/4499, regresszió 4499/4499 = 100%; a hét módosult lap 360/390/1280 px-en rendben, a Venn-applet 390 px-en betöltődött. A keresőindex 308 oldalából pontosan hét változott. A jsdom és a valódi képernyőolvasó nem futott; a videókat nem néztem végig, a fej nélküli böngésző YouTube-lejátszása sikertelen volt. A tanári tartalmi pontosítás a következő bejegyzésben van; a tényleges lejátszás külön technikai próba.

**4e/06 M1 tanári pontosítás (2026-10-03, helyi main):** a 72–73. binomiális videó megfelelő, megmarad. A 76. óra statisztikai bevezető középértékekkel, ezért az adatoldal `s1` szakaszához került; a 77. a reprezentatív mintáról és a szóródásról szól, ezért a mutatók oldalának `s3` szakaszán van; a 78. főleg grafikonos, ezért az adatoldal `s3` szakaszába került. A tartalmi döntések rendezve. Utóellenőrzés: média 292/292, kánon 13/0, linkek 310/0, sáv tiszta, kulcs és regresszió 4499/4499, a két módosult lap 360/390/1280 px-en rendben, a keresőindexből csak ezek változtak. A normál böngészős lejátszás külön technikai ellenőrzés marad.

**4e/01–04 M1 helyesbítés (2026-10-03, helyi main):** az előző kör évfolyam szerinti keresése hibás lezáráshoz vezetett. A tanár pontosította, hogy az MNT más tantervi sorrendet követ: a sorozathatárérték a III. osztályos 91–97. órákban van. Hét videó került a 4e/01 négy lapjára; a gyökös határérték lapja videó nélkül maradt. Az MNT IV. osztályos 17–39. órái között deriválási és integrálási anyag is van, ezért a 4e/02–04 összes korábbi negatív döntése érvénytelen. A javított státusz és az ötegységes döntési tábla: [`M1_4e_01_04_attekintes.md`](M1_4e_01_04_attekintes.md). A 4e/01 hét videóját a tanár megtartotta. A 4e/02–04 azóta új döntést kapott; az integrálási döntési tábla: [M1_4e_04_attekintes.md](M1_4e_04_attekintes.md).

**4e/02 M1 (2026-10-03, helyi main):** a függvények hét tananyag-egységének döntési táblája: [`M1_4e_02_attekintes.md`](M1_4e_02_attekintes.md). Tizennégy MNT IV. osztályos videó került hét lapra; a 7–8. óra önálló összetett/inverz függvényes ismétlése nem illik e lapokra. Online médiaellenőrzés: 313/313; kánon 13/0, linkek 310/0, sáv tiszta, kulcsteszt 4499/4499, regresszió 4499/4499 = 100%; a hét lap 360/390/1280 px-en rendben. A videókat nem néztem végig. **Tanári döntés rendezve (2026-10-03):** a 14. óra első 16 perce végtelen/végtelen típusú feladatokat tárgyal, ezért a végtelenbeli határérték lapján marad. A későbbi végtelen mínusz végtelen rész a társadalmi tagozaton nem tananyag; ezt a kártya jelzi.

**4e/03 M1 (2026-10-03, helyi main):** a deriválás nyolc egységének döntési táblája: [`M1_4e_03_attekintes.md`](M1_4e_03_attekintes.md). A 17–30. MNT-órák közül 13 videó került fel hét lapra; a 24. függvényközelítés M2-n kívül maradt, az érintő és változási sebesség lapjához nincs önálló új videó. A 19. definíció szerinti levezetését és a 22. inverzderiválását a kártya kiegészítésként jelöli. Online média 326/326; kánon 14/0, linkek 310/0, sáv tiszta, kulcs és regresszió 4499/4499; a nyolc lap 360/390/1280 px-en rendben. A keresőindexből pontosan hét URL változott. A videókat nem néztem végig; a jsdom, a nyomtatási látvány és a valódi képernyőolvasó nem futott. Tanári döntés rendezve (2026-10-03): a 19. és 22. óra vegyes tartalommal is marad; a 27–28. óra csak az „A teljes függvényvizsgálat — hét lépés a grafikonig” lap „Polinomfüggvény” szakaszában szerepel.

**4e/04 M1 (2026-10-03, helyi main):** a hat integrálási egység döntési táblája: [M1_4e_04_attekintes.md](M1_4e_04_attekintes.md). Nyolc aktív MNT-videó szerepel hat lapon. A 34. és 39. parciális integrálás, a 42–43. forgástesttérfogat M2-n kívüli; a 41. bonyolultabb területszámítási órát a tanár kihagyta. A kikapcsolás utáni online médiaellenőrzés 334/334, kánon 12/0, linkek 310/0, sáv tiszta; az érintett lap 360/390/1280 px-en és nyomtatási nézetben rendben. A keresőindex 308 bejegyzéséből csak a területszámítási URL változott. A teljes kulcsteszt és regresszió az eredeti beillesztési adagban 4499/4499 volt; matematikai tartalom most nem változott. Az M1 mind a 38 4e-egységre döntéssel lezárva: 67 videó 35 lapon, 3 lap videó nélkül. A videókat nem néztem végig; a jsdom, a tényleges YouTube-lejátszás és a valódi képernyőolvasós próba nem futott. Tanári döntés nem maradt nyitva.

**Felhőben (2026-09-27):** a felhős környezet *Network access* beállításában engedélyezni kell a
`tavoktatas.mnt.org.rs`, a `youtube.com` és az `api.geogebra.org` tartományt (nélkülük a WebFetch és a
`media.py --online` sem működik). Bevált menet: az MNT óra-oldalán (engedélyezett, lekérdezés nélküli
URL) van a beágyazott videó, a tanár, és a „Kapcsolódó tananyag” blokkban a szomszédos órák óratípussal
(új anyag / gyakorlás / megerősítés / ismétlés) — tananyag-laphoz az új anyagot feldolgozó órát válaszd.
A YouTube videóoldalai (`/watch`) innen 429-et adnak: a videó leírása és hossza nem olvasható ki, az
oEmbed (cím + csatorna) viszont működik.
Az óra-oldal „Kapcsolódó tananyag” blokkja csak a témakörön belüli szomszédokra mutat, ezért a
bejárás témakörönként megakad. Új kiindulópontot ad a tanár profiloldala (`/tanar/<név>`, lekérdezés
nélkül engedélyezett: a legutóbbi 15 óra), végső esetben a valószínű című óra-URL (1 kérés/s). Az I.
osztályból így sem került elő a 40–42., az 50–51. és a 61. óra — valószínűleg nem készült hozzájuk
videó (tanár, 2026-09-28): ami az óra-oldalon és a YouTube-on sincs meg, azt nem kell tovább keresni.

### M2 · GeoGebra-szimulációk
**Cél:** ahol a manipulálható modell többet ér az állóképnél (függvény-transzformációk, egységkör,
geometriai transzformációk, testek, vektorok, analitikus geometria, határérték, érintő, Riemann-összeg,
kombinatorika/valószínűség), témakörönként 1–4 szimuláció.
**Hogyan:** `media-beagyazas` skill; ha van saját `interaktiv.js`-mód ugyanarra, ne duplázd.
**Elfogadás:** mint M1; minden elemnél szerző + licenc; mobilon (390 px) kipróbálva.

| 1e | 2e | 3e | 4e |
|---|---|---|---|
| ☑ 10 szimuláció 10 lapon (a 8 témakörből 5-ben: 02, 05, 06, 07, 08; a 01, 03, 04 témakörhöz nincs telefonon használható, tantervhez illő applet) — 2026-09-28 | ◐ 4 szimuláció 4 lapon; 35 egység átnézve, helyi main, publikálásra vár — 2026-10-03 | ☑ 5 szimuláció 5 lapon; 50 egység átnézve, a 02 és 06 témakörhöz nincs megfelelő mobilos modell — 2026-10-02 | ☑ 5 szimuláció 5 lapon (4 új, 1 pilot); 38 egység átnézve — #14, 2026-10-03 |

**2e M2 (2026-10-03, helyi main):** négy GeoGebra-szimuláció került be a komplex összeadás, a másodfokú függvény, az inverz függvény és az egységkörből kapott szinusz/koszinusz grafikon oldalára. A 35 egység soronkénti döntése: [`M2_2e_attekintes.md`](M2_2e_attekintes.md). A vizsgált logaritmus-alapcsúszkás jelöltek 0-t vagy 1-et is engedtek, ezért nem kerültek fel. Az egyesítés után `media.py --online`: 268/268; `media_proba.py`: 4/4 betöltés 390 px-en, képek átnézve. Kánon 65/0, linkek 310/0, sáv tiszta, kulcsteszt 4499/4499, regresszió 4499/4499 = 100%, a négy érintett lap 360/390/1280 px-en rendben. A naplótérkép változatlan, a keresőindex 308 bejegyzése közül pontosan e négy oldal szövege változott; nincs üres szöveg vagy fejezetcím. A jsdom-réteg, a nyomtatási látvány és a valódi képernyőolvasós próba nem futott.

**Felhőben (2026-09-28):** a jelöltek adatlapja és mérete az `api.geogebra.org`-ról jön, a próba
(`_tools/media_proba.py`) a `www.geogebra.org`-ot is kéri. Minden jelöltet 390 px-en és szélső
helyzetben is ki kell próbálni (media-beagyazas skill, 3. és 5. pont): az 1e-ben nyolc jelölt azért
esett ki, mert szélső helyzetben 180°-nál nagyobb szöget írt ki (a háromszög megfordításakor, ill. a
kerületi szög csúcsát a másik ívre húzva). Hibás applet akkor sem marad a lapon, ha a leírás
figyelmeztetne rá (tanári döntés, 2026-09-28) — ha nincs jobb, a lap szimuláció nélkül marad.

**3e M2 (2026-10-02, publikált main):** az 50 tananyag-egység M2-döntése egyenként a
[`M2_3e_attekintes.md`](M2_3e_attekintes.md) táblázatban van. Öt GeoGebra-modell került az 01, 03, 04
és 05 témakör öt lapjára a médiakatalóguson keresztül. A gúla térfogatának, az egyenesek három
helyzetének, a vektorösszegnek, valamint az ellipszis és a parabola fókuszos meghatározásának
szélső/köztes állását kipróbáltam; a 390 px-es használhatóságot az eredeti oldalakon is ellenőriztem.
A 02 témakör kúpos-hengeres jelöltjei mobilon túl aprók, illetve maximális sugárnál lelógnak a
képről; a 06 mértani sorozatos jelöltje a tananyagban kizárt nulla hányadost is megengedi. Ezek
nem kerültek be. A részletes ellenőrzési eredmény az állapotnaplóban szerepel.

**4e M2 (2026-10-03, publikált main):** mind a 38 tananyag-egység döntése a
[`M2_4e_attekintes.md`](M2_4e_attekintes.md) táblázatban szerepel. Négy új GeoGebra-modell került a
02, 03, 04 és 06 témakörbe; a 05 korábbi binomiális kockája megmaradt. A saját szelő–érintő,
Riemann-téglalap, primitívfüggvény, Pascal-háromszög, érme/kocka és adatlabor modellekhez nem adtam
ismétlődő beágyazást. A kiválasztott modelleket 390 px-en és szélső beállításokkal ellenőriztem;
a hibás vagy telefonon túl apró jelöltek nem kerültek fel. A lánc eredménye az állapotnaplóban van.

### M3 · Link-őr (ötlet)
Havi GitHub Action, amely `media.py --online`-t futtat, és hiba esetén issue-t nyit. ☐

---

## A — Évfolyam-audit

### Átvett hibajegyzék (2026-09-29)

| Terület | Állapot | Következő lépés |
|---|---|---|
| Keresőindex: üres szöveg és fejezetek, 3000 karakteres csonkolás | ◐ Helyi ágon javítva: 308/308 lap kereshető, 360/390/1280 px próba rendben; push nélkül | Tanári jóváhagyás után publikálás |
| Képletes fejezetcímek a tartalomjegyzékben | ☐ | Közös `ui.js` javítása és célzott ellenőrzés |
| Főoldali videó szüneteltetése; mozgáscsökkentés kezdőértéke | ☑ Helyi mainen javítva: rendszerkövető mozgás, videószünet, magyar felirat és leirat; 44/44 videópróba | Publikálásra vár; a Q2 valódi képernyőolvasós próbája külön fennmarad |
| 30 régi 1e kvízvisszajelzés élő régiója | ◐ Helyi ágon javítva 26 HTML-ben; 81 böngészőpróba hibátlan | Képernyőolvasós felolvasási próba |
| 1e/02 trigonometria: Közép 4 és Nehéz 2 szögtartománya | ◐ A tanár hegyesszögű értelmezést rögzített; a két feladat helyi ágon pontosítva, a kulcs egyezik | Publikálás tanári jóváhagyás után |
| 1e/02 Alap 11 dupla részfeladatjel; 1e/06 Bővítés címe | ◐ Helyi ágon javítva; kánonellenőrzés 310/0 | Publikálás tanári jóváhagyás után |
| 1e/02 Alap 10: `\sin 90^\circ` nem hegyesszög | ◐ Helyi ágon hegyesszögű példával javítva; privát felmérő-ütközés ellenőrizve | Publikálás tanári jóváhagyás után |
| 1e/01 halmazok Közép 5 b) és logika Nehéz 3 c): hibás matematikai végeredmény | ◐ Az 1e A2 adagban javítva; független logikai ellenőrzés megtörtént | Publikálás tanári jóváhagyás után |
| 1e/05 geometria Gyakorló dolgozat 6: elfajuló háromszög az állításban | ◐ Helyi ágon `ABC` és `DEC` háromszögre javítva; az OSO-indoklás pontosítva | Publikálás tanári jóváhagyás után |
| 1e/01 halmazok Gyakorló órai 4 és 1e/05 Vészterem Alap 12: hamis egzisztenciális állításhoz „ellenpélda” kérése | ◐ Mindkét kérés indoklásra pontosítva; a logikai feladatban `\mathbb{N}` értelmezése rögzítve | Publikálás tanári jóváhagyás után |
| 1e/02 trigonometria Nehéz 4–5: a szögfüggvények közül a kotangens hiányzik a Végeredményből | ◐ `ctg φ = 5/12`, illetve `√2` pótolva; független SymPy-számítás és új kulcstesztek | Meglévő feladatparaméterekből levezetett értékek; publikálás tanári jóváhagyás után |
| Végeredménydobozok tartalmi tisztítása | ☑ 1e: 16 lapon 110; 2e/01–04: 17 lapon 279; 3e: 23 lap átnézve, 21 lapon 287; 4e: 16 lap átnézve, 12 lapon 57 Végeredmény tisztítva | Az A2 javítások helyi ágakon vannak; a teljes A1 ellenőrzés külön feladat |
| 2e/02 tantervi határ: bikvadratikus és paraméteres feladatok az Alap és a gyakorló sávban is | ☑ A kimenetek és szabványok alapján a paraméteres esetszétválasztás és a megtartott bikvadratikus feladatok kiegészítőként jelölve; a törzsanyag gyakorlóútvonalai pontosítva (2026-10-04) | A feladatok és horgonyok megmaradtak; builder, keresőindex, kánon, link, sáv, kulcs és 360/390/1280 px ellenőrzés rendben |
| 2e/04 tantervi határ: trigonometrikus függvények, azonosságok és egyenletek | ☑ A szabványalapú besorolás a 16 témakörlapon átvezetve (2026-10-04): a törzs gyakorlóútvonalai pontosítva, az összetett transzformációk, azonosságok és általános megoldások kiegészítőként jelölve | A 2026/27-es operatív terv tanári felülvizsgálata később lehetséges; a feladatok, végeredmények és horgonyok megmaradtak |

**2e kimenet- és szabványalapú döntés (2026-10-04):** A 2e évfolyam kimenetei és a teljesítményszabványok az elsődlegesek; az M2 módszertani útmutatója segít a feladatok körének szűkítésében. A helyi operatív terv nem emeli önmagában kötelezővé a benne szereplő bővítő technikákat. A honlap „Alap/Közép/Nehéz” sávjai a feladat nehézségét jelölik, nem az O/S/N szabványszint közvetlen másolatai; az M2-követelményt ezért a sáv mellett külön kell felismerhetővé tenni.

- **2e/02:** A számszerű másodfokú egyenlet, a diszkrimináns, a Viète-képletek, a parabola értelmezése és az egyszerű másodfokú egyenlőtlenség a törzsanyag (`MAT.A.SO.O.1.2 (2.1–2.3)`, `MAT.A.SO.S.1.2 (2.5)`, `MAT.F.SO.O.1.8 (8.2–8.4)`). A paraméter szerepének és a megoldásszám eseteinek vizsgálata `MAT.A.SO.N.1.3 (3.3–3.4)`, így az Alapban vagy a gyakorlóban szereplő paraméteres feladat sem kötelező 2e-s minimum. A bikvadratikus feladatok a 2026-10-01-i tanári döntés szerint megmaradnak; a változócsere és a komplex gyökök vizsgálata emelt kitekintés (`MAT.A.SO.N.1.3 (3.2)`, illetve `MAT.A.SO.N.1.1 (1.3)`).
- **2e/04:** A szögfüggvényérték, az alapgrafikonok felvázolása és leolvasása, az addíciós tételek közvetlen alkalmazása, az egyszerű trigonometrikus egyenlet/egyenlőtlenség és a szinusz-/koszinusztétel egyszerű alkalmazása a 2e-s kimenetekhez tartozik. A szabványban a függvényérték és a grafikonolvasás `MAT.F.SO.O.1.8 (8.2, 8.4)`, a trigonometrikus kifejezés egyszerű átalakítása `MAT.A.SO.S.1.2 (2.4)`, a háromszöges számítás `MAT.G.SO.S.1.6 (6.2)`. A `MAT.F.SO.O.1.8 (8.3)` alpont **kifejezetten lineáris és másodfokú grafikonról szól**; nem szabad trigonometrikus grafikonkimenetként hivatkozni rá. Az amplitúdó–periódus–fáziseltolás teljes képletes vizsgálata, a félszög és szorzattá alakítás önálló technikaként, valamint az általános megoldáscsaládok kiegészítők. Egy egyszerű, adott grafikonról történő leolvasás vagy egylépéses azonosságalkalmazás ettől még lehet alapszintű, illetve középszintű feladat.
- **2e/02 webes átvezetés kész (2026-10-04):** A paraméteres és bikvadratikus részek, az érintett feladat- és gyakorlókártyák kiegészítő jelölést kaptak; a tananyag törzsanyaghoz vezető gyakorlósávjait pontosítottam. A feladatok, végeredmények és végleges horgonyok megmaradtak. Friss szemű lektor kérésére a gyakorlólapok szövege különválasztja a törzsanyag típusait a kiegészítőktől. Builderes újraépítés után a kánon és jsdom 15/15, a linkek 310/0, a sávellenőrzés tiszta, a kulcsteszt 4499/4499, a regresszió 100%, a 360/390/1280 px-es böngészőpróba 15 lapon hibátlan. A teljes kulcstesztben nincs 2e modul; a builderöntesztek sikeresek. Nyomtatási látvány és valódi képernyőolvasó nem volt ellenőrizve.
- **2e/04 webes átvezetés kész (2026-10-04):** A trigonometriai tananyag, öt feladatgyűjtemény, összefoglaló, terepküldetés, Vészterem és témakör-nyitólap a törzsanyag és a kiegészítő részek határát mutatja. A „Gyakorolj!” útvonalak a megfelelő feladatokra vezetnek; a csak részben kiegészítő kártyák részei külön jelöltek. A friss szemű lektor jelzéseire az $x$-intervallum, a végpont bevonása és a tangenses létezésvizsgálat pontosítva. A feladatok számai és 179 Végeredmény szövege, valamint a végleges horgonyok változatlanok. Builderönteszt, kánon és jsdom 19/19, linkek 310/0, sávellenőrzés tiszta, kulcsteszt 4499/4499, regresszió 100%, 360/390/1280 px-en 19 lap hibátlan. A teljes kulcstesztben nincs 2e modul; a nyomtatási látványt és a valódi képernyőolvasót nem ellenőriztem.
- **Következő tartalmi adag:** a következő nagyobb feladat kiválasztása tanári döntés szerint; a 2e operatív tervet a rögzített kimenetalapú besoroláshoz később hozzá lehet igazítani.

Forrás: [2e M2 program és módszertani útmutató (ZUOV, 2020)](https://zuov.gov.rs/wp-content/uploads/2020/08/pravilnik-gimnazija.pdf); [középfokú matematika-teljesítményszabványok (hivatalos jogszabálytár)](https://reg.pravno-informacioni-sistem.rs/api/viewdoc?doctype=reg&regactid=438034&uuid=f3525554-666a-40d0-8580-83ba47ad9f2f). A korábbi második hivatkozás az 1/2026-os első évfolyamos tantervre mutatott, ezért cseréltem.

### A1 · Teljes ellenőrzés osztályonként
**Cél:** a már kész anyag hibáinak felderítése és javítása — **tartalmi bővítés nélkül**.
**Lépések:** (1) teljes lánc az osztályra: `verify_web`, `check_links`, `sav_check`, `kulcs_teszt` +
`kulcs_regresszio` (érzékenység 100 %), `layout_teszt`; (2) **friss szemű teszt** (web-verifikacio
skill 3. réteg) témakörönként egy tananyag-egységen és egy feladatgyűjteményen — kontextus nélküli
subagenttel; (3) matematikai szúrópróba: definíciók, tételek pontossága, jelölés-kánon.
**Javítás:** egyértelmű hiba (elírás, rossz kulcs, törött link, kánonsértés) → javítás a builderben /
1e-ben a HTML-ben, lánc újra. Minden más (pedagógiai döntés, feladat cseréje) → „Tanári döntés kell” lista.
**Elfogadás:** a lánc tiszta; a PR-ben hibalista táblázatban (hol · mi · javítva/döntés kell).

| 1e | 2e | 3e | 4e |
|---|---|---|---|
| ☑ teljes A1: 77 lap ellenőrizve, témakörönként friss szemű tartalmi próba, 16 lap pontosítva; helyi main (2026-10-04) | ☑ teljes A1: 65 lap ellenőrizve, nyolc lap javítva, mind a négy témakörből friss szemű tananyag- és feladatpróba; helyi main (2026-10-04) | ☑ teljes A1: 92 lap ellenőrizve; hat tananyag és hat feladatlap friss szemű próbája, 293 kártya önálló újraszámolása; a záró adagban 17 lap pontosítva; helyi main (2026-10-05) | ☑ teljes A1: 73 lap böngészőpróbája, témakörönként 1 tananyag és 1 feladatgyűjtemény friss szemű lektorálása, 14 lap javítva; a tanári besorolási döntések átvezetve (2026-10-02) |

**3e A1 lezárás (2026-10-05, helyi main):** a hat témakör egy-egy tananyagát és feladatlapját kontextus nélküli lektorok vizsgálták; első körben megoldókulcs nélkül mind a 293 kijelölt kártyát és részfeladatait önállóan megoldották. A 3e összesen 771 kártyájára ez mintavételes tartalmi ellenőrzés. A feltárt feltételhiányokat, túl általános állításokat, jelölési és nyelvi hibákat 14 builderben javítottam; 17 HTML-lap változott érdemben. A részletes hibalista, a visszavont jelzések és a hatókör: [3e A1 ellenőrzési jelentés](A1_3e_ellenorzes.md).

**Záró ellenőrzés:** builderöntesztek rendben; képek → média → háttér → naplótérkép → keresőindex rendben. A 334 aktív médiaelem megmaradt; naplótérkép: 184 oldal, 2294 feladat, 12315 XP. Kánon és jsdom 92/92; linkek 310/310, gyakorlósáv tiszta; kulcsteszt 4499/4499; regressziós érzékenység 100%; 92 lap 360/390/1280 px-en hibátlan. Az utolsó szövegpontosítás után a 06-os témakör 10 lapos kánon- és jsdom-próbája és a két újraépített lap háromszélességes böngészőpróbája is sikeres, a kulcs- és regressziós teszt ismét hibátlan. A 308 nem üres keresőindex-bejegyzésből pontosan a 17 javított oldal változott, a horgonyok megmaradtak. Új feladat és új feladat-számadat nem készült. Az indukció csak szemléltető tananyag kidolgozott példákkal; önálló gyakorlat, házi és kvíz nincs. Nyomtatási látványt, valódi képernyőolvasót, az ábrák rajzi minőségét és a külső média tartalmát ez az adag nem ellenőrizte újra. **Tanári döntés kell:** nincs új kérdés. Push nem történt.

**3e A1 hibalista és részállapot (2026-10-04, helyi main):**

| Hol | Mi volt a hiba | Súlyosság | Javítás / teendő |
|---|---|---|---|
| 06, indukciós tananyag és témakör-útmutatók | Az előző audit a kimenetből tévesen önálló gyakorlási igényt vezetett le; a dokumentált tanári döntés szerint az indukció itt csak szemléltető tananyag | közepes | A tananyag- és egyéb oldalépítőkben a tanári döntés átvezetve; nincs indukciós feladatsor vagy házi |
| 06, indukciós kvíz | Két önálló kérdés maradt a szemléltető tananyagban | alacsony | Mindkét kvíz eltávolítva a tananyagépítőből; a korábbi kvízszöveg-javítás tárgytalan |
| 02, gömb és síkmetszetek | A gömbtest minden pontját a középponttól egyenlő távolságúnak mondta; több helyen a test síkmetszetét körnek nevezte körlap helyett, a szélső helyzetek feltétele nélkül | magas / közepes | Tananyag- és összefoglaló-építőkben pontosítva |
| 02, gömbfeladatok | A gömb síkmetszetével, illetve beírt/körülírt gömbbel kapcsolatos feladatok M1/M3-as bővítések, de törzsanyagként látszottak | közepes | Az érintett kártyákon és tananyagrészeken kiegészítő jelölés |
| 06, terepküldetés és tanári kulcs | A küldetés önálló magyarázatot kért a hiányos indukcióról, bár ez a rész csak tananyagként szerepelhet | közepes | A részfeladat eltávolítva; a privát tanári DOCX-kulcs újragenerálva a három megmaradó részfeladathoz |

**3e A1 ellenőrzés:** mind a hét érintett builder SymPy-öntesztje rendben. A képek, a 334 aktív médiaelem, a háttér, a naplótérkép (184 oldal, 2294 feladat, 12335 XP) és a 308 oldalas keresőindex újraépült; az indexből pontosan 12 érintett URL szövege változott. A végső kánon- és jsdom-ellenőrzés 92/92, a belső linkek 310/310, a gyakorlósáv tiszta, a kulcsteszt 4499/4499, a regressziós érzékenység 4499/4499 = 100%. A 92 lap 360/390/1280 px-es böngészőpróbája hibátlan; az utolsó két szövegpontosítás után a két érintett lap külön is hibátlan ezen a három szélességen. Nyomtatási látványt és valódi képernyőolvasót nem vizsgáltam. A témakörönkénti, kontextus nélküli friss szemű lektorálás a szolgáltatás használati korlátja miatt nem indult el; ezért az A1 **részben kész** marad. A következő lépés témakörönként egy tananyag- és egy feladatlap független lektorálása. **Tanári döntés rögzítve:** az indukcióhoz önálló feladatot később sem kell készíteni.

**3e A1 tanári korrekció (2026-10-04):** az indukciós tananyagból a két kvíz, a terepküldetésből az önálló indukciós magyarázat kikerült; a privát tanári kulcs ehhez igazodik. A két építő és a privát kulcs SymPy-öntesztje hibátlan. Az újraépítési lánc után 334 aktív médiaelem, 308 indexelt oldal, 184 naplótérkép-oldal, 2294 feladat és 12315 XP maradt. A teljes 3e kánon- és jsdom-próba 92/92, a linkek 310/310, a gyakorlósáv tiszta, a kulcsteszt 4499/4499, a regressziós érzékenység 100%; a 06-os témakör 10 lapja 360/390/1280 px-en hibátlan. A privát DOCX szerkezete ellenőrzött, de a nyomtatási látvány, a valódi képernyőolvasó és a DOCX vizuális megjelenése nincs ellenőrizve. **Tanári döntés kell:** nincs új kérdés.

**2e A1 hibalista (2026-10-04, helyi main):**

| Hol | Mi volt a hiba | Súlyosság | Státusz |
|---|---|---|---|
| 01, hatványfüggvény | Az aszimptóta meghatározása kizárta a grafikon és az aszimptóta metszését | közepes | Tananyagépítőben pontosítva |
| 01, gyöktelenítés | A nevezőben álló gyök alatti számot mindig pozitívnak mondta; páratlan gyöknél negatív is lehet | közepes | Tananyagépítőben pontosítva |
| 01, komplex osztás | A képlet mellől hiányzott a nemnulla nevező feltétele | közepes | Tananyagépítőben pótolva |
| 02, Viète-képletek | A tételben nem szerepelt az $a\neq0$ feltétel | közepes | Tananyagépítőben pótolva |
| 02, másodfokú feladatok, Közép 5 | Az $m=6$ válasznál a gyökök nem valósak, amit a kérdés nem tett egyértelművé | közepes | A feladatépítőben kimondva, hogy komplex gyökök is lehetnek |
| 03, logaritmusos feladatok | Az Alap 12–13 felbontásából hiányoztak a változók és az alap feltételei; a Közép 13 kérdése nyelvtanilag hibás volt | közepes / alacsony | Feladatépítőben javítva, az Alap 14–15 feltételei is kiírva |
| 04, trigonometrikus egyenletek | A negatív jobb oldalra közölt általános sin-, cos- és tg-képletek hibásak voltak; a $bx$-es esetből hiányzott $b\neq0$ és a periódusból $|b|$ | magas | Tananyagépítőben az előjel szerinti esetekkel és a periódusfeltételekkel javítva |
| 04, trigonometrikus feladatok, Alap 19 c) | A $\sin x\le0$ megoldásából kimaradt $0^\circ$ | magas | Feladatépítőben a kérdés és a végeredmény javítva |

**2e A1 ellenőrzés:** a nyolc érintett builder lefutott, a SymPy-s önellenőrzések rendben; `kepek.py` → `media.py` → `set_hatter.py` → `build_naplo_terkep.py` → `build_search_index.py` lefutott. A kánon és a jsdom 65/65, a linkek 310/0, a sávellenőrzés tiszta, a kulcsteszt 4499/4499, a regresszió 4499/4499 = 100%. A 65 lap 360/390/1280 px-es böngészőpróbája hibátlan, az utolsó két szövegpontosítás után az érintett lapok külön is. A 308 nem üres keresőindex-bejegyzésből pontosan a nyolc javított oldal változott. A négy témakör kijelölt tananyag- és feladatlapját kontextus nélküli lektorok nézték át. A feladatlapok első kivonatából a végeredmények is látszottak, ezért új, valóban kulcs nélküli kivonatokból külön lektorok mind a négy témakörben változatos feladatokat önállóan újraszámoltak; az egyértelműen kiolvasható példákban további eltérést nem találtak. A sima szöveggé alakítás néhol elveszíti a képletek felső indexeit és törtvonalait; ezt nem minősítettük oldalhibának. A teljes kulcstesztben nincs 2e kulcsmodul, ezért a builderöntesztek és ezek az önálló számolások adtak 2e-s számtani kontrollt. A nyomtatási látvány és a valódi képernyőolvasós próba nem futott. **Tanári döntés kell:** a 2e/02 paraméteres feladatok besorolása és a 2e/04 trigonometriahatár az M2-skill és az operatív terv között továbbra is nyitott; a bikvadratikus egyenletek a korábbi döntés szerint maradnak.

**1e A1 hibalista (2026-10-04, helyi main):**

| Hol | Mi volt a hiba | Súlyosság | Státusz |
|---|---|---|---|
| 01, relációk és logika | A párhuzamosság reflexív példaként szerepelt; a hamis egzisztenciális állítás cáfolásához ellenpéldát kért a feladat; az indirekt és kontrapozíciós eljárás keveredett | közepes | HTML-ben javítva, az egész számok és a természetes számok tartománya pontosítva |
| 02, trigonometriai feladat | A sárkány zsinórjának talajjal bezárt szögét a szöveg félreérthetően adta meg | alacsony | A zsinór szögére pontosítva; csak hegyesszögű szögfüggvény maradt |
| 03, közelítés és számfeladatok | A relatív hiba nullával oszthatott; a normálalak-szabály nem fedte le pontosan az előjelet és a határeseteket; két egyenlet közös megoldásnak is olvasható volt | közepes | HTML-ben feltételekkel és egyértelmű kérdésszöveggel javítva |
| 04, arány és százalék | Az arányhoz fölöslegesen kellett nemnulla előtag; a keresztszorzás és százalékos osztás kivételei hiányoztak | közepes | A nemnulla osztó feltételeit kimondva |
| 04, keverék, haszon, kamat | A hőmérsékleti átlag modellfeltételei, a haszon viszonyítási alapja és a kamat évszámítása nem volt egyértelmű | közepes | Az idealizált modell, a beszerzési ár és a 360 napos egyszerű kamat megadva |
| 05, geometriai tételek | A párhuzamossági axióma más geometriákra tett következménye, a külső szögek száma és az alakzatok távolsága túl általános volt | közepes | Három tananyaglap szövege pontosítva |
| 05, kör és téglalap feladatai | A „nagyobbik ív fölött” helymeghatározás félreérthető volt; a „téglalapnak van beírt köre” állítás kvantora hiányzott | közepes | A builderben a csúcs helye és a minden téglalapra vonatkozó állítás megadva |
| 07, egyenletrendszerek | Az egyenesek metszéspontja és a \(0=0\) eset általános megfogalmazása elfajuló egyenleteknél hibás következtetéshez vezethetett; az életkoros feladat szövege kétféleképpen olvasható volt | közepes | Tananyagban feltételek, builderben egyértelmű életkori arány |
| 08, hasonlóság | Az átfogóhoz tartozó magasság jelölése eltért a \(h\) jelölési kánontól | alacsony | A tételben és a példában \(h\)-ra javítva |

**1e A1 ellenőrzés:** a 05 és 07 feladatlap builderének öntesztje rendben; egyedi_id.py → kepek.py → media.py → set_hatter.py → build_naplo_terkep.py → build_search_index.py lefutott. A kánon és a jsdom 77/77, a linkek 310/0, a sávellenőrzés tiszta, a kulcsteszt 4499/4499, a regresszió 4499/4499 = 100%. A 77 lap 360/390/1280 px-es böngészőpróbája hibátlan. A 308 nem üres keresőindex-bejegyzésből pontosan a 16 módosult oldal változott. A 08 témakörben szándékosan nincs feladatgyűjtemény: lezáró tananyag. A nyomtatási látvány és a valódi képernyőolvasós próba nem futott. Tanári döntést igénylő új kérdés nincs.

**4e A1 hibalista (2026-10-02, helyi ág):**

| Hol | Mi volt a hiba | Súlyosság | Státusz |
|---|---|---|---|
| 01, végtelen mértani sor | Az aszimptota metszését kizáró mondat, a véges sorösszeg feltétele és a valós inga/modellezett út összemosása | közepes | Builderben javítva |
| 01, határérték-feladatok A 22–23 | A megtett út és az indulási magasság nélküli abszolút helyzet keveredett | közepes | Kérdések pontosítva |
| 02, függvénytulajdonságok és aszimptoták | A periódushoz nem kellett a teljes tartomány ismétlődése; a fokszám szerinti kvíz kihagyta a nagyobb különbség esetét | közepes | Builderekben javítva |
| 03, konvexitás és függvényvizsgálat | A konkáv függvény nem feltétlenül „nem konvex”; a kizárt hely nem feltétlenül pólus; a polinom- és normálisállításból hiányzott kivétel | közepes | Builderben javítva |
| 04, határozott integrál és terület | Az egymást nem finomító felosztások felső összege nem feltétlenül csökken; az $F+C$ állításhoz összefüggő intervallum kell | közepes | Builderben javítva |
| 04, határozatlan integrál A 3 és K 1 | Szakadó értelmezési tartományon a pont nem választ ki egyetlen globális primitívet | közepes | Az $M$ pontot tartalmazó intervallum megadva |
| 04, kulcsteszt A 2 | A második alpontnál hibás „nem” elvárást egy későbbi „nem” elfedett | közepes | Elvárás és sorrendi teszt javítva; célzott hibamutációt elkapja |
| 05, binomiális tétel | Az $n+1$ tag csak a formális összegre igaz | alacsony | Tétel pontosítva |
| 06, valószínűség | A feltételes valószínűség nem mindig változik; a Bernoulli-kísérlet több elemi kimenetele is két csoportba sorolható | közepes | Tananyag, összefoglaló és feladat javítva |
| 06, valós adatok és döntés | A csapadékos nap adatküszöbe és a fogadás/befektetés döntési feltétele hiányzott | közepes | Builderekben pontosítva |

**Ellenőrzés:** 11 érintett builder öntesztje rendben; `kepek.py` → `media.py` → `set_hatter.py` → `build_naplo_terkep.py` → `build_search_index.py` lefutott. A kánon és a linkek 310/0, a sávellenőrzés tiszta, a kulcsteszt 4499/4499, a regresszió 4499/4499 = 100%. A 73 4e lap 360/390/1280 px-es Node Playwright-core próbája (túlcsordulás, JS, KaTeX, helyi fájlok, első kvíz 390 px-en) hibátlan; az utolsó két szövegpontosítás után a két érintett lap külön is hibátlan. A 308 bejegyzéses keresőindexből pontosan a 14 módosult oldal változott. A jsdom, a Python Playwright, a nyomtatási látvány és a valódi képernyőolvasós próba nem futott. **Tanári döntés kell:** a `4e/03` konvexitás/inflexió Alap 7–8 és a `4e/05` kombinatorikai Alap sáv hivatalos szabványszint szerinti besorolása; a Titanic „nők és gyermekek először” történeti mondatának forrásolása vagy puhítása. Az A1 nem végzett feladatátsorolást és nem cserélt feladatot.

**Tanári döntés rendezve (2026-10-02):** a honlap sávjai a feladat tényleges nehézségét jelölik, nem a szabványkód O/S/N szintjének automatikus másolatai. A `4e/03` A 7 egyszerű grafikonfelismerésként Alap marad; az A 8 háromrészes, második deriváltas feladat középszintű átvezetés lett (a végleges `#alap-8` horgony megmaradt). A polinomos K 5–8 Közép, a törtfüggvényes N 1–2 Nehéz marad. A `4e/05` 14 alap kombinatorikai kártyája tanári döntés szerint Alap; összetettebb feladatai Közép vagy Nehéz szintűek. A Titanic történeti mondata tanári döntéssel változatlanul marad. E három besorolási kérdéshez további döntés nem kell.

**Utóellenőrzés:** a 4e/03 builder SymPy-öntesztje, a `kepek.py` → `media.py` → `set_hatter.py` → `build_naplo_terkep.py` → `build_search_index.py` lánc, a kánon 310/0, a linkek 310/0 és a sávellenőrzés tiszta. Kulcsteszt 4499/4499, regresszió 4499/4499 = 100%; az egyetlen módosult lap 360/390/1280 px-en hibátlan. A középre emelt kártya miatt az elérhető XP 12334-ről 12335-re nőtt. A jsdom, a nyomtatási látvány és a valódi képernyőolvasós próba most sem futott.
**Javítva (2026-09-28, helyben):** a `3e_05_pontok` `nehez-4` kártyájának Végeredményében levezetés állt
(„\(2t^2=(t-6)^2+t^2\), tehát …”) — a `2`-esei miatt a `kulcs_regresszio` egy mutációt nem kapott el. A levezetés
kikerült (kánon), az érzékenység most 4445/4445.

### A2 · Végeredmény-kánon: csak a végső válasz
**Kánon** (`_docs/workflow.md` 8. pont): a `.vegeredmeny` **kizárólag a végső választ** tartalmazza — levezetés,
indoklás, közbülső lépés nélkül („\(25\)”, nem „\(18+12-5=25\)”). **Lelet (2026-09-28):** 423 kártya
Végeredményében áll levezetésre utaló szó (*tehát, mert, ezért, hiszen, ugyanis, így*): 3e 217 · 2e 141 · 1e 36 · 4e 29
(kulcsszavas szűrés — lesz köztük hamis pozitív is). Javítás a builderekben (1e régi gyűjteményeinél a HTML-ben),
osztályonként egy PR; utána `kulcs_teszt` + `kulcs_regresszio` (a levezetés eltűnésével a kulcs-modul várt
értékei közül a közbülsőket is ki kell venni). Ha egy kártyánál a válasz a levezetés nélkül értelmetlen
(pl. „melyik a hibás lépés?”), az maradhat — ezeket a PR-ben listázd.

| 1e | 2e | 3e | 4e |
|---|---|---|---|
| ◐ 16 lap, 110 kártya (helyi ág, 2026-09-29) | ◐ 01–04: 17 lap, 279 Végeredmény-doboz (02 és 04 ugyanazon külön helyi ágon, 2026-10-01) | ◐ 23 lap, 771 kártya átnézve; 287 Végeredmény és 1 kérdés javítva (helyi ág, 2026-10-01) | ◐ 16 lap, 359 kártya átnézve; 12 lapon 57 Végeredmény tisztítva (helyi ág, 2026-10-02) |

| 1e | 2e | 3e | 4e (01–04) |
|---|---|---|---|
| ◐ 1e helyi ágon ellenőrizve | ◐ 2e/01–04 A2 helyi ágon ellenőrizve; teljes A1 tananyagpróba még hátra | ◐ 3e A2 helyi ágon ellenőrizve; teljes A1 tananyagpróba még hátra | ◐ 4e A2 helyi ágon ellenőrizve; a teljes A1 tartalmi próba külön helyi ágon elkészült |

**1e A2 kivételek:** bizonyítást vagy indoklást kérő kártyákban a rövid érvelés a válasz része maradt: `1e/01` függvények `nehez-2`, `nehez-7`; halmazok `nehez-2`, `nehez-4`; logika `nehez-6`, `nehez-7`; `1e/02` trigonometria `nehez-1`; `1e/03` számok `nehez-1`, `nehez-2`, `nehez-7`, Vészterem `nehez-1`; `1e/04` Vészterem `alap-5`; `1e/05` geometria `nehez-2`, `gye-6`, `joker`, Vészterem `nehez-3`. Mind a 16 kártya kifejezetten bizonyítást, cáfolatot vagy indoklást kér, így az érdemi érvelés maradt. A logika `nehez-7` fölösleges értéktáblázatos mondata kikerült, a halmazok `nehez-4` és a geometria `nehez-2` bizonyítása pontosabb lett; a `gye-6` állítása javítva.


**2e/03 A2 részállapot (2026-09-30, helyi ág):** négy feladatlap 113 Végeredmény-doboza tisztult; ekkor még a 2e/01, 02 és 04 témakörök A2 tisztítása volt hátra. A végső válaszhoz szükséges rövid érvelés vagy modell megmaradt az exponenciális lap `alap-6`, `nehez-6` kártyáján, a logaritmus lap `kozep-10` bizonyításán, a logaritmusfüggvény lap `kozep-13` fogalmi kérdésén, valamint a Vészterem `alap-10` és `kozep-7` kártyáján. A HTML-diff 113 Végeredmény-dobozra és 6 feladatszövegre korlátozódik; a kánon, a linkek, a sávok, a kulcsteszt és a háromszélességes böngészőpróba rendben. A friss szemű lektor hat feladatszöveg-pontosítást jelzett; ezek a kérdésekben is javítva vannak.

**2e/01 A2 részállapot (2026-10-01, helyi ág):** négy feladatlap 150 kártyáját átnéztük; 9 Végeredmény-doboz rövidült vagy pontosodott. A Vészterem `kozep-7` feladatszövege most saját Gauss-síkbeli ábra készítését kéri, mert a korábbi szöveg nem létező rajzra hivatkozott. A hatványozás és gyökvonás Jokerében, valamint a Vészterem `alap-10` hibakereső feladatában a kért hibaazonosítás, ellenpélda vagy javítás megmaradt. A komplex számok `kozep-4` és Joker kártyájának kért indoklása, a gyökvonás `nehez-4` azonosságának bizonyítása, valamint a Vészterem `kozep-7` képletes számítása és rövid indoka is indokolt kivétel. A friss szemű lektor a kilenc módosított feladat eredményeit megerősítette; a 2e/02 és 04 témakör hátra van.

**2e/02 A2 részállapot (2026-10-01, külön helyi ág):** négy feladatlap 147 kártyáját átnéztük; 24 Végeredmény-doboz és 5 kérdésszöveg pontosodott. A „komplex gyök” többértelműségét a „nem valós komplex” megfogalmazás oldja fel; a `kozep-12` állítása a főegyüttható és a teljes négyzet szorzatáról szól. A Vészterem `alap-10` hamis állításai konkrét ellenpéldát kaptak; `kozep-7` már nem hivatkozik hiányzó ábrára, és a kért szorzat alak is szerepel a válaszban. A hibaazonosítást és indoklást kérő Joker, illetve `kozep-12` rövid érdemi magyarázata megmaradt. A friss szemű lektor a tíz vizsgált feladat eredményeit megerősítette. A HTML-diff 24 válaszdobozra és 5 kérdésre, a keresőindex 308 bejegyzéséből pontosan erre a négy URL-re korlátozódik. A kánon 310/0, a linkellenőrzés 310/0, a sávellenőrzés tiszta, a kulcsteszt 4865/4865, a regresszió 4865/4865 = 100%, a 360/390/1280 px-es böngészőpróba mind a négy lapon hibátlan. A teljes kulcstesztnek nincs 2e modulja; a jsdom- és a valódi képernyőolvasós réteg nem futott. **Tanári döntés kell:** az M2-skill szerint a bikvadratikus és paraméteres egyenletek nem 2e-s törzsanyagok, miközben a témakörben Alap- és gyakorlófeladatok, illetve önálló tananyag is épül rájuk. A 2026/27-es operatív terv csak a tágabb „másodfokúra visszavezethető egyenletek” címet használja. Az esetleges átsorolás külön tartalmi adag legyen.

**Utólagos tanári döntés (2026-10-01):** a bikvadratikus egyenletek egyelőre maradnak. A paraméteres feladatok besorolása továbbra is nyitott.

**2e/04 A2 részállapot (2026-10-01, külön helyi ág):** öt feladatlap 179 kártyáját átnéztük; 133 Végeredmény-doboz és 5 feladatszöveg pontosodott. A rövidítésből a kért indoklás, bizonyítás, szorzat alak és hibaazonosítás megmaradt; az egyszerűsített trigonometrikus törtek értelmezési feltétele, illetve az általános megoldások egész $k$ paramétere szerepel a válaszokban. A háromszögfeladatok három kerekítési hibája javítva (`alap-14`: `13,52`; `kozep-12`: `264,28`; `kozep-13`: `48,13°` és `96,87°`). A torony, a hajóforduló és a léggömb kérdése a geometriai helyzetet egyértelműen meghatározza. A kontextus nélküli lektor a háromszöges lap 34 feladatát önállóan megoldotta. A HTML-diff csak a 133 válaszra és 5 kérdésre, a keresőindex 308 bejegyzéséből csak az öt érintett URL-re esik. Az öt builder SymPy-öntesztje, a kánon 310/0, a linkek 310/0, a sávellenőrzés, a kulcsteszt 4865/4865, a regresszió 4865/4865 = 100% és az öt lap 360/390/1280 px-es böngészőpróbája rendben; a végső szövegpontosítás után a háromszöges lap külön böngészőpróbája is hibátlan. A teljes kulcstesztben nincs 2e kulcsmodul, a jsdom-réteg és valódi képernyőolvasós próba nem futott. **Tanári döntés kell:** az M2-skill és az operatív terv trigonometriahatára eltér; a feladatok átsorolása vagy elhagyása külön tartalmi adag.

**3e A2 részállapot (2026-10-01, helyi ág):** a 23 feladatlap 771 kártyáját átnéztük; 21 lapon 287 Végeredmény-doboz rövidült, és a sorozatok `alap-10` kérdése kiegészült a négy ábrázolt sorozat képletével. Az első nyolc pont önmagában nem igazolhatta a teljes sorozat korlátosságát. A henger `alap-18` litereredménye a kért két tizedesre pontosodott (`62 831,85` liter); a sorozatok `nehez-7` válasza mindkét számsorrendet tartalmazza. A bizonyítást, rövid indoklást vagy hibaazonosítást kifejezetten kérő kártyákban az érdemi állítás és a szükséges rövid érvelés megmaradt. A 3e kulcsmodulok köztes eredményeket váró tételei a végső válaszokra álltak át, a független számítások megtartásával. A friss szemű lektor négy kiemelt feladatot önállóan újraszámolt, eltérés nélkül. A HTML-diff pontosan 287 válaszra és egy kérdésre, a keresőindex 308 bejegyzéséből pontosan 21 URL-re korlátozódik. A builderöntesztek, a kánon 310/0, a linkek 310/0, a sávellenőrzés, a kulcsteszt 4621/4621 és a regresszió 4621/4621 = 100% hibátlan. A 23 lap 360/390/1280 px-es böngészőpróbája a rendelkezésre álló Node Playwright-core-ral hibátlan. A Python Playwright, a jsdom-réteg és valódi képernyőolvasós próba nem állt rendelkezésre. **Tanári döntés kell:** a 3e A2 javításaihoz nincs új tartalmi döntés; a teljes A1 ellenőrzés és a 4e A2 külön adag.

**4e A2 részállapot (2026-10-02, helyi ág):** a 16 feladatlap 359 kártyáját átnéztük; 12 lapon 57 Végeredmény-doboz rövidült vagy pontosodott, kérdésszöveg nem változott. Az 1∞ alakok besorolása, a folytonosság indoka, a hibakeresés, a tükörfüggvény bizonyítása, a deriválást vagy helyettesítést kifejezetten kérő feladatok részeredménye, valamint a Gauss-integrál Jokerének rövid magyarázata megmaradt. A 4e/04 parabolaszelet aránya `4/3`, a 4e/03 mozgásfeladatában `a(2)=0 m/s²`; ezeket független lektor is újraszámolta. A HTML-diff kizárólag 57 válaszdobozra, a 308 bejegyzéses keresőindex változása pontosan a 12 érintett URL-re esik. A builderöntesztek, a kánon 310/0, a linkek 310/0, a sávellenőrzés és a kulcsteszt 4498/4498 hibátlan; a regresszió 4498/4498 = 100%, a 16 lap 360/390/1280 px-es böngészőpróbája hibátlan. A jsdom-réteg és valódi képernyőolvasós próba nem futott. **Tanári döntés kell:** ehhez az A2 adaghoz nincs új tartalmi döntés; a 4e teljes A1 tananyagellenőrzése külön feladat.

---

### A3 · Magyar megfogalmazás és a hétköznapi példák hitelessége

**Tanári kérés, 2026-10-05:** külön ellenőrzés a természetes magyar szövegre,
főként a bevezetőkre, matematikai magyarázatokra és a hétköznapi példákra.
Az egyértelmű javításokat beépítjük, bizonytalan esetben a szöveg marad.
A korábbi A1-ellenőrzések nem helyettesítik a teljes stilisztikai átnézést.

| 1e | 2e | 3e | 4e |
|---|---|---|---|
| ◐ 01: mind a 9 tananyag teljes szövege átnézve és javítva; a többi lap külön A3-auditja hátra (helyi main, 2026-10-05) | ☐ A3 külön audit hátra | ☐ A3 külön audit hátra | ☐ A3 külön audit hátra |

Az első adag három függvényes, a második hat logikai és halmazos tananyagot
ellenőrzött. A példák feltételei, bevezetők, átvezetők és matematikai pontatlanságok
javultak; nyolc SVG teljesebb leírást kapott. A második adagban a gyorsismétlő
hiányzó komplementerjelei is javultak: végleges böngésző/axe 36/0, nyomtatás 12/12,
képletrender 256/0, kvíz 12/12, kulcs 4499/4499. A hat Venn-ábra meglévő neve
megfelelő. Részletek: [A3 nyelvi ellenőrzés](A3_nyelvi_ellenorzes.md).
Hátra van a többi tananyag, feladatgyűjtemény, nyitóoldal, összefoglaló és terepküldetés.

---

## I — Interaktív ábrák

### I1 · Statikus ábrák → interaktív
**Cél:** a kulcsfogalmak ábráiból csúszkás/húzható változat, a meglévő `assets/js/interaktiv.js`
mintájára (új `data-mod`); a builder oldalán `tananyag_common` helper.
**Kánon** (`_docs/workflow.md` 4b): JS nélkül is értelmes kezdőállapot (a statikus SVG az első
képkocka); címkézett, billentyűzettel kezelhető vezérlő; külső könyvtár nélkül; sötét tinta világos
lapon; `verify_web` hibátlan; ha 2+ lapon kell, közös modul.
**Első lépés (külön PR):** jelöltlista osztályonként (lap · ábra · mit mutatna a csúszka · haszon),
a tanár választ belőle. Ötletek: lineáris függvény (m, b); másodfokú függvény csúcsalakja;
exponenciális/logaritmus alapváltás; egységkör → szinuszgörbe; a·sin(bx+c)+d paraméterei;
vektorösszeadás; kör és egyenes kölcsönös helyzete; sorozat ε-sávja.

| jelöltlista | 1e | 2e | 3e | 4e |
|---|---|---|---|---|
| ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Q — Kényelem, használhatóság (QOL)

| Kód | Feladat | Állapot |
|---|---|---|
| Q1 | `layout_teszt.py` az összes lapra; minden mobil-túlcsordulás javítása | ☑ 2026-09-28: mind a 293 lap hibátlan 360/390/1280 px-en (fejléc, képletes doboz-cím, táblázat-burok a builderekben, hosszú képletek tördelése, h1, kereső) |
| Q2 | Akadálymentesség: axe-core Playwrighttal (`npm i axe-core`), kontraszt, `aria`, fókusz-sorrend | ◐ 2026-10-05: közös vezérlők, matematikai nevek, fókusz, mozgás, köszöntővideó és 379 SVG feliratai javítva; 6094 feliratszínpár/0 jelzés, axe 282/0, saját interaktív ábrák 218/218. A korábbi Node-elrendezésmérés helyesbítve: 930 valódi nézet, három mobilhiba javítva, kilenc célzott utópróba/0; 13 gördülő képlet kezelhető. Negyedik adag: külső média indítása, bezárása és forráslinkje javítva; 334 elem/668 sikeres ciklus, 14 állapotpróba, saját felület axe 6/0; [részletes jelentés](Q2_akadalymentesseg.md). Ötödik adag: 4e/06 hat diagramjához 47 szöveges adatsor; axe 24/0, billentyűzet 36/36, nyomtatás 8/8, kulcs 4499/4499 és regresszió 100%; a kulcsolvasó és a JS nélküli nyomtatás javítva. Hatodik adag: 1e/01 három függvényes tananyag nyolc SVG-je látható, kapcsolt leírással; 18 végleges nézet/0 elrendezés- és axe-jelzés, nyomtatás 6/6, képletrender 200/0, kvíz 4/4. Valódi képernyőolvasó, a többi komplex ábra szöveges egyenértékűsége, szolgáltatói médiafelületek és JS nélküli képlet-felolvasás még ellenőrzendő. |
| Q3 | „Folytasd, ahol abbahagytad” — a `naplo.js` jegyezze az utolsó lapot, a főoldalon és az osztály-indexen gomb | ☐ |
| Q4 | Mobil tartalomjegyzék: lebegő „Tartalom” gomb, ha a TOC keskeny kijelzőn nem látszik | ☐ (előbb ellenőrizni) |
| Q5 | Offline mód (PWA): service worker a meglátogatott lapokra + KaTeX; frissítés-kezelés deploykor | ☐ (tanári döntés kell) |
| Q6 | Teljesítmény: képméretek, font-preload, a szkriptek `defer`-je; mérés Playwrighttal | ☐ |
| Q7 | Kompakt médiakártya: kattintásig alacsony sáv (ikon, címke, cím), lejátszáskor nyílik 16:9-re / az applet arányára (`.media-fut`) | ☑ 2026-09-28 (helyben): az 1e/07 egyenletrendszer-lapon a médiablokkok aránya asztalon 46% → 19% |

---

## Ö — Ötletek (tanári döntés után)

- **Képletgyűjtemény osztályonként** — automatikusan a 📘 tétel- és 📗 definíció-dobozokból
  (`build_kepletgyujtemeny.py` → `<osztaly>/kepletgyujtemeny.html`, nyomtatható). Érettségire is jó.
- **Csapda-gyűjtemény** — az összes ⚠️ csapda-doboz témakörönként egy lapon: dolgozat előtti gyors ismétlés.
- **Végtelen gyakorló** — paraméteres generátor néhány begyakorló típusra (pl. binomiális együttható,
  deriválási szabályok) azonnali visszajelzéssel; a számok véletlenek, tehát felmérő-ütközés nincs.
- **Videó-XP** — a naplóban kis jutalom a megnézett videóért (a `beagyazas.js` jelezheti).
