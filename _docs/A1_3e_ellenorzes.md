# 3e A1 — tartalmi ellenőrzés és friss szemű lektorálás

Dátum: 2026-10-05. Kiinduló revízió: `245f97b`, helyi `main`; induláskor tiszta munkafa,
a helyi és a távoli `main` megegyezett. A javítások 14 builderből készültek, kézi HTML-szerkesztés nélkül.

## Hatókör

A korábbi 92 oldalas szerkezeti ellenőrzést a teljes tananyag definícióinak, tételeinek és
jelöléseinek áttekintése, valamint témakörönként egy tananyag és egy feladatlap független
lektorálása egészítette ki. A lektorok az első körben csak az oldalak szövegét kapták meg:
projektkontextust, tantervet és megoldókulcsot nem. A matematikai képleteket megőrző
kivonatokból minden kártyát és részfeladatot megoldottak. Ezután külön körben következett
az összevetés a weboldal válaszaival; az eredeti számítások megmaradtak.

| Témakör | Tananyag | Feladatlap | Önállóan megoldott kártya |
|---|---|---|---:|
| 01 Poliéderek | Csonkagúla | Gúla és csonkagúla | 54 |
| 02 Forgástestek | Csonkakúp | Gömb és összetett testek | 44 |
| 03 Lineáris rendszerek | Megoldások száma | Egyenletrendszerek | 50 |
| 04 Vektorok | Vektoriális szorzat | Skaláris és vektoriális szorzat | 45 |
| 05 Analitikus geometria | Parabola és egyenes | Ellipszis és hiperbola | 43 |
| 06 Sorozatok | Mértani sorozat | Sorozatok | 57 |
| **Összesen** | **6 tananyag** | **6 feladatlap** | **293** |

A szándékolt, pontosított értelmezésben mind a 293 kártya számeredménye és kerekítése
egyezik a weboldal válaszaival. Az ellenőrzés mintavételes, független lektorálás; nem állítja,
hogy mind a 771 darab 3e feladatkártyát külön lektor oldotta meg.

## Javítások

| Hol | Hiba | Súlyosság | Javítás módja |
|---|---|---|---|
| 01 térelemek | Négy axióma, de „három” a címben | Enyhe | Builder: cím javítva |
| 01 gúla | A definiált oldalél `s`, a képletekben `b` | Közepes | Builder: két képlet és az Alap 4 válasz jelölése javítva |
| 01 gúla síkmetszetei | A magasság `H`, de az arány nevezője `m` | Közepes | Builder: képlet és táblázat egységesítve |
| 01 gúla, Nehéz 4 | Nincs kimondva a metszősík párhuzamossága | Közepes | Builder: az alaplappal párhuzamos sík feltétele pótolva |
| 01 gúla, Alap 1 és 5 | Túl általános szigorú egyenlőtlenség; „magasságból induló” szakaszok | Közepes | Builder: rövid igaz/hamis válasz és helyes, kért indoklás |
| 01 csonkagúla | Általános testhez közös él- és oldallapmagasság; felesleges magasságszámítás előírása | Közepes | Builder: szabályos eset és a szükséges számítás hatóköre rögzítve |
| 01 csonkagúla | Elfajuló metszési helyzetet is megengedő definíció; pontatlan hétköznapi példák | Közepes | Builder: csúcs és alaplap közötti sík, megfelelő tárgymodellek |
| 02 forgástestek | Minden pontra körpálya, minden merőleges metszetre kör; egyenlő befogók kivétele hiányzik | Közepes | Builder: tengelyen kívüli pontok, a vizsgált testek körlapmetszete, egyenlő befogók esete |
| 02 kúp | Minden palástpontot `s` távolságúnak mond a csúcstól | Súlyos | Builder: egyenlő alkotók és az alapkörből keletkező ív helyes leírása |
| 02 csonkakúp | Minden felsorolt tárgy csonkakúp; a forma feltétel nélkül merevebb és egymásba rakható | Közepes | Builder: közelítő tárgymodellek, falvastagság és méretezés szerepe |
| 02 gömb, Alap 21 / Nehéz 2 | Furatirány, illetve kifolyásmentesség nincs rögzítve | Közepes | Builder: közös tengelyű furat; a víz nem folyik túl |
| 02 gömb, Közép 11 | A felszín és térfogat számértékét mértékegység nélkül hasonlítja össze | Közepes | Builder: cm²/cm³ és a válaszban cm |
| 02 gömb, Közép 15 / kapacitásfeladatok | Egyenes kúptípus és belméret hallgatólagos | Közepes | Builder: egyenes körkúp, belső sugár/átmérő |
| 02 gömb, Közép 8 / Joker | A henger alapkörét a gömb főkörével azonosítja | Közepes | Builder: egyenlő sugarak; a területazonosság nem jelent torzításmentes ráterítést |
| 03 megoldások száma | Egy `0=0` sorból feltétel nélkül végtelen sok megoldásra következtet | Súlyos | Builder: teljes lépcsős alak, ellentmondásmentesség és a megmaradó sorok száma |
| 03 megoldások száma | Mindig egy szabad paraméter; hiányzó síkegyenlet-feltétel | Közepes | Builder: a szabad ismeretleneknek megfelelő paraméterszám; nem nulla normálvektor |
| 03 megoldások száma | Arányos bal oldalak „ugyanazok”; összeegyeztethető mérésből „igaz” adatot állít | Közepes | Builder: arányosság és konzisztencia helyes leírása |
| 03 rendszerek, Alap 7 | Nem derül ki, mi marad meg az egyenletek összeszorzása után | Közepes | Builder: az eredeti két egyenletet csak a szorzategyenlet váltja fel; általános garanciát kér |
| 03 rendszerek, Közép 14–15 | Hiányzó mozgási és keverési modellfeltételek | Közepes | Builder: változatlan állandó sebességek, azonos indulási helyek, térfogatszázalék, összeadódó térfogatok |
| 03 determináns | A tulajdonságok száma és a megfogalmazás eltér | Enyhe | Builder: számozástól független cím és „további” tulajdonság |
| 04 vektoriális szorzat | Az irányleírás a nullvektorra is vonatkozik; koordinátás feltételek hallgatólagosak | Közepes | Builder: nem nulla/nem párhuzamos tényezők, szögtartomány, jobbsodrású derékszögű bázis |
| 04 vektoriális szorzat | A nyomaték feltétel nélkül tengelyirányú | Közepes | Builder: az ajtó síkbeli modellje és a tengelyirányú összetevő szerepe |
| 05 ellipszis–hiperbola, Közép 1–2 / 9–11 | Két pont nem határoz meg általános görbét; a valós tengely iránya hiányzik | Súlyos | Builder: origó középpont és megfelelő tengelyirány rögzítve |
| 05 parabola és egyenes | A képletek paraméterfeltételei és a függőleges érintők hatóköre hiányos | Közepes | Builder: pozitív paraméterek és az iránytényezős alak hatóköre |
| 05 parabola-videó | „külcsönos” elírás | Enyhe | Médiakatalógus: „kölcsönös”; a forrás URL-je változatlan |
| 06 mértani sorozat | Nulla első tag és nulla hányados következménye összemosódik | Közepes | Builder: a két kizárt eset külön indoklása |
| 06 mértani sorozat | Negatív hányadosra is exponenciális görbét állít | Közepes | Builder: pozitív hányados, konstans és váltakozó előjelű eset külön |
| 06 mértani sorozat | A mértani közép elnevezését negatív számpárra is használja | Enyhe | Builder: pozitív szélső tagok feltétele; a négyzetazonosság általánosan megmarad |
| 06 sorozatok, Nehéz 1 | A kérdés szigorú alsó korlátot sugall, az első tag 1 | Közepes | Builder: a már helyes válasszal egyező `1 ≤ aₙ < 3` kérdés |
| 06 kamat | Névleges és effektív éves kamatláb nincs elkülönítve | Közepes | Builder: névleges éves kamatláb a negyedéves számolásnál |

Nyelvi egyértelműsítésként a gömb Közép 13 közvetlenül a festendő felületet kérdezi;
a sorozatok Alap 5 pedig egy lehetséges egyszerű szabályt kér, hiszen négy tagból a
folytatás nem egyedi. A meglévő számeredmények megmaradtak.

## Visszavont vagy kontextussal feloldott jelzések

- A gúla Közép 17 már tartalmazta a „szabályos négyoldalú” feltételt; nem volt hiba.
- A kiválasztott tananyagok Gyakorolj-sávjai másik feladatlapra is mutatnak. A kivonatok
  eltérő feladatköre nem hibás hivatkozás; a sávokat a teljes weboldalon ellenőrizzük.
- A gömb Alap 6 harmadik állítása igaz: az érintősík metszete egy pont, nem kör.
  A halmazmetszet szokásos értelmezése mellett nem kellett átírni.
- A gömb Közép 13 eredménye helyes: a festendő felület a teljes mondat alapján kizárja
  az alsó körlapot. A megfogalmazás egyértelműsítése nem eredményjavítás.
- Az apotémát a csonkagúla lecke hivatkozással kapcsolja a gúlánál tárgyalt fogalomhoz;
  ez nem hiányzó tananyag.

## Ellenőrzés

- A 14 módosított builder lefutott; a SymPy-öntesztek sikeresek.
- A képek → média → háttér → naplótérkép → keresőindex lánc lefutott. A média továbbra
  is 334 aktív elem; a naplótérkép 184 oldal, 2294 feladat és 12315 elérhető XP.
- A teljes 3e kánon- és jsdom-próbája: **92/92**, hiba nélkül.
- Belső linkek: **310/310**, hibás hivatkozás nélkül; a gyakorlósáv ellenőrzése tiszta.
- Kulcsteszt: **4499/4499**; regressziós érzékenység: **4499/4499 = 100%**.
- A teljes 3e böngészőpróbája: **92 oldal × 360/390/1280 px**, hiba nélkül.
- Az utolsó, mértani középre vonatkozó mondat javítása után a lánc, a teljes kulcs- és
  regressziós teszt, a 06-os témakör 10 lapos kánon- és jsdom-próbája, továbbá az utoljára
  újraépített két lap háromszélességes böngészőpróbája ismét sikeres.
- A 308 keresőindex-bejegyzés mindegyikében nem üres a szöveg és a fejezetlista;
  pontosan a 17 érdemben módosult HTML-lap URL-jének tartalma változott.
  Mind a 17 lap azonosítói és végleges feladathorgonyai megmaradtak.

## Korlátok és tanári döntés

A független lektorok szöveges kivonatból dolgoztak: ez nem igazolja a perspektivikus ábrák
rajzi minőségét. A nyomtatási látványt, valódi képernyőolvasót és a külső videók/appletek
tartalmát ez az adag nem ellenőrizte újra. A média változása egy meglévő cím elírásának javítása.

**Tanári döntés kell:** nincs új kérdés. Az indukció továbbra is szemléltető tananyag,
kidolgozott példákkal; önálló gyakorló- és házi feladat nem kerül hozzá. Új feladat vagy
új feladat-számadat nem készült; a végleges horgonyok megmaradtak. Push nem történt.
