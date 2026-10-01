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
| ☑ 85 videó 30 lapon (mind a 38 egység megvizsgálva; 8 lap videó nélkül; egy videó csak egy helyen) — 2026-09-28 | ☑ 78 videó 32 lapon (mind a 35 egység megvizsgálva; 3 lap tanári döntéssel videó nélkül) — #1, 2026-09-27 | ☑ 80 videó 41 lapon (mind az 50 egység megvizsgálva; 9 lap videó nélkül) — 2026-09-28 | ◐ pilot: 4e/05 binomiális tétel (1 videó) |

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
| ☑ 10 szimuláció 10 lapon (a 8 témakörből 5-ben: 02, 05, 06, 07, 08; a 01, 03, 04 témakörhöz nincs telefonon használható, tantervhez illő applet) — 2026-09-28 | ☐ | ☐ | ◐ pilot: 4e/05 (a+b)³-kocka (1 szimuláció) |

**Felhőben (2026-09-28):** a jelöltek adatlapja és mérete az `api.geogebra.org`-ról jön, a próba
(`_tools/media_proba.py`) a `www.geogebra.org`-ot is kéri. Minden jelöltet 390 px-en és szélső
helyzetben is ki kell próbálni (media-beagyazas skill, 3. és 5. pont): az 1e-ben nyolc jelölt azért
esett ki, mert szélső helyzetben 180°-nál nagyobb szöget írt ki (a háromszög megfordításakor, ill. a
kerületi szög csúcsát a másik ívre húzva). Hibás applet akkor sem marad a lapon, ha a leírás
figyelmeztetne rá (tanári döntés, 2026-09-28) — ha nincs jobb, a lap szimuláció nélkül marad.

### M3 · Link-őr (ötlet)
Havi GitHub Action, amely `media.py --online`-t futtat, és hiba esetén issue-t nyit. ☐

---

## A — Évfolyam-audit

### Átvett hibajegyzék (2026-09-29)

| Terület | Állapot | Következő lépés |
|---|---|---|
| Keresőindex: üres szöveg és fejezetek, 3000 karakteres csonkolás | ◐ Helyi ágon javítva: 308/308 lap kereshető, 360/390/1280 px próba rendben; push nélkül | Tanári jóváhagyás után publikálás |
| Képletes fejezetcímek a tartalomjegyzékben | ☐ | Közös `ui.js` javítása és célzott ellenőrzés |
| Főoldali videó szüneteltetése; mozgáscsökkentés kezdőértéke | ☐ | Közös HTML/JS/CSS akadálymentességi javítás |
| 30 régi 1e kvízvisszajelzés élő régiója | ◐ Helyi ágon javítva 26 HTML-ben; 81 böngészőpróba hibátlan | Képernyőolvasós felolvasási próba |
| 1e/02 trigonometria: Közép 4 és Nehéz 2 szögtartománya | ◐ A tanár hegyesszögű értelmezést rögzített; a két feladat helyi ágon pontosítva, a kulcs egyezik | Publikálás tanári jóváhagyás után |
| 1e/02 Alap 11 dupla részfeladatjel; 1e/06 Bővítés címe | ◐ Helyi ágon javítva; kánonellenőrzés 310/0 | Publikálás tanári jóváhagyás után |
| 1e/02 Alap 10: `\sin 90^\circ` nem hegyesszög | ◐ Helyi ágon hegyesszögű példával javítva; privát felmérő-ütközés ellenőrizve | Publikálás tanári jóváhagyás után |
| 1e/01 halmazok Közép 5 b) és logika Nehéz 3 c): hibás matematikai végeredmény | ◐ Az 1e A2 adagban javítva; független logikai ellenőrzés megtörtént | Publikálás tanári jóváhagyás után |
| 1e/05 geometria Gyakorló dolgozat 6: elfajuló háromszög az állításban | ◐ Helyi ágon `ABC` és `DEC` háromszögre javítva; az OSO-indoklás pontosítva | Publikálás tanári jóváhagyás után |
| 1e/01 halmazok Gyakorló órai 4 és 1e/05 Vészterem Alap 12: hamis egzisztenciális állításhoz „ellenpélda” kérése | ◐ Mindkét kérés indoklásra pontosítva; a logikai feladatban `\mathbb{N}` értelmezése rögzítve | Publikálás tanári jóváhagyás után |
| 1e/02 trigonometria Nehéz 4–5: a szögfüggvények közül a kotangens hiányzik a Végeredményből | ◐ `ctg φ = 5/12`, illetve `√2` pótolva; független SymPy-számítás és új kulcstesztek | Meglévő feladatparaméterekből levezetett értékek; publikálás tanári jóváhagyás után |
| Végeredménydobozok tartalmi tisztítása | ◐ 1e: 16 lapon 110; 2e/01–04: 17 lapon 279 Végeredmény tisztítva | 3e–4e hátra; a 2e/02 és 04 helyi ága még nincs pusholva |
| 2e/02 tantervi határ: bikvadratikus és paraméteres feladatok az Alap és a gyakorló sávban is | ◐ Tanári döntés (2026-10-01): a bikvadratikus egyenletek egyelőre maradnak, átsorolás nem történt | A paraméteres feladatok besorolása nyitott; az A2 adag nem cserélt feladatot |
| 2e/04 tantervi határ: trigonometrikus függvények, azonosságok és egyenletek | ⚠️ A 2e M2 skillje szűkebb, mint a 2026/27-es operatív terv (pl. a tervben `y=a sin(bx)+c` és félszög/szorzattá alakítás is van); a weben általános trigonometrikus megoldások is szerepelnek Alap sávban | Tanári döntés kell a témakör tartalmi besorolásáról; az A2 javítások nem cseréltek feladatot |

### A1 · Teljes ellenőrzés osztályonként
**Cél:** a már kész anyag hibáinak felderítése és javítása — **tartalmi bővítés nélkül**.
**Lépések:** (1) teljes lánc az osztályra: `verify_web`, `check_links`, `sav_check`, `kulcs_teszt` +
`kulcs_regresszio` (érzékenység 100 %), `layout_teszt`; (2) **friss szemű teszt** (web-verifikacio
skill 3. réteg) témakörönként egy tananyag-egységen és egy feladatgyűjteményen — kontextus nélküli
subagenttel; (3) matematikai szúrópróba: definíciók, tételek pontossága, jelölés-kánon.
**Javítás:** egyértelmű hiba (elírás, rossz kulcs, törött link, kánonsértés) → javítás a builderben /
1e-ben a HTML-ben, lánc újra. Minden más (pedagógiai döntés, feladat cseréje) → „Tanári döntés kell” lista.
**Elfogadás:** a lánc tiszta; a PR-ben hibalista táblázatban (hol · mi · javítva/döntés kell).
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
| ◐ 16 lap, 110 kártya (helyi ág, 2026-09-29) | ◐ 01–04: 17 lap, 279 Végeredmény-doboz (02 és 04 ugyanazon külön helyi ágon, 2026-10-01) | ☐ | ☐ |

| 1e | 2e | 3e | 4e (01–04) |
|---|---|---|---|
| ◐ 1e helyi ágon ellenőrizve | ◐ 2e/01–04 A2 helyi ágon ellenőrizve; teljes A1 tananyagpróba még hátra | ☐ | ☐ |

**1e A2 kivételek:** bizonyítást vagy indoklást kérő kártyákban a rövid érvelés a válasz része maradt: `1e/01` függvények `nehez-2`, `nehez-7`; halmazok `nehez-2`, `nehez-4`; logika `nehez-6`, `nehez-7`; `1e/02` trigonometria `nehez-1`; `1e/03` számok `nehez-1`, `nehez-2`, `nehez-7`, Vészterem `nehez-1`; `1e/04` Vészterem `alap-5`; `1e/05` geometria `nehez-2`, `gye-6`, `joker`, Vészterem `nehez-3`. Mind a 16 kártya kifejezetten bizonyítást, cáfolatot vagy indoklást kér, így az érdemi érvelés maradt. A logika `nehez-7` fölösleges értéktáblázatos mondata kikerült, a halmazok `nehez-4` és a geometria `nehez-2` bizonyítása pontosabb lett; a `gye-6` állítása javítva.


**2e/03 A2 részállapot (2026-09-30, helyi ág):** négy feladatlap 113 Végeredmény-doboza tisztult; ekkor még a 2e/01, 02 és 04 témakörök A2 tisztítása volt hátra. A végső válaszhoz szükséges rövid érvelés vagy modell megmaradt az exponenciális lap `alap-6`, `nehez-6` kártyáján, a logaritmus lap `kozep-10` bizonyításán, a logaritmusfüggvény lap `kozep-13` fogalmi kérdésén, valamint a Vészterem `alap-10` és `kozep-7` kártyáján. A HTML-diff 113 Végeredmény-dobozra és 6 feladatszövegre korlátozódik; a kánon, a linkek, a sávok, a kulcsteszt és a háromszélességes böngészőpróba rendben. A friss szemű lektor hat feladatszöveg-pontosítást jelzett; ezek a kérdésekben is javítva vannak.

**2e/01 A2 részállapot (2026-10-01, helyi ág):** négy feladatlap 150 kártyáját átnéztük; 9 Végeredmény-doboz rövidült vagy pontosodott. A Vészterem `kozep-7` feladatszövege most saját Gauss-síkbeli ábra készítését kéri, mert a korábbi szöveg nem létező rajzra hivatkozott. A hatványozás és gyökvonás Jokerében, valamint a Vészterem `alap-10` hibakereső feladatában a kért hibaazonosítás, ellenpélda vagy javítás megmaradt. A komplex számok `kozep-4` és Joker kártyájának kért indoklása, a gyökvonás `nehez-4` azonosságának bizonyítása, valamint a Vészterem `kozep-7` képletes számítása és rövid indoka is indokolt kivétel. A friss szemű lektor a kilenc módosított feladat eredményeit megerősítette; a 2e/02 és 04 témakör hátra van.

**2e/02 A2 részállapot (2026-10-01, külön helyi ág):** négy feladatlap 147 kártyáját átnéztük; 24 Végeredmény-doboz és 5 kérdésszöveg pontosodott. A „komplex gyök” többértelműségét a „nem valós komplex” megfogalmazás oldja fel; a `kozep-12` állítása a főegyüttható és a teljes négyzet szorzatáról szól. A Vészterem `alap-10` hamis állításai konkrét ellenpéldát kaptak; `kozep-7` már nem hivatkozik hiányzó ábrára, és a kért szorzat alak is szerepel a válaszban. A hibaazonosítást és indoklást kérő Joker, illetve `kozep-12` rövid érdemi magyarázata megmaradt. A friss szemű lektor a tíz vizsgált feladat eredményeit megerősítette. A HTML-diff 24 válaszdobozra és 5 kérdésre, a keresőindex 308 bejegyzéséből pontosan erre a négy URL-re korlátozódik. A kánon 310/0, a linkellenőrzés 310/0, a sávellenőrzés tiszta, a kulcsteszt 4865/4865, a regresszió 4865/4865 = 100%, a 360/390/1280 px-es böngészőpróba mind a négy lapon hibátlan. A teljes kulcstesztnek nincs 2e modulja; a jsdom- és a valódi képernyőolvasós réteg nem futott. **Tanári döntés kell:** az M2-skill szerint a bikvadratikus és paraméteres egyenletek nem 2e-s törzsanyagok, miközben a témakörben Alap- és gyakorlófeladatok, illetve önálló tananyag is épül rájuk. A 2026/27-es operatív terv csak a tágabb „másodfokúra visszavezethető egyenletek” címet használja. Az esetleges átsorolás külön tartalmi adag legyen.

**Utólagos tanári döntés (2026-10-01):** a bikvadratikus egyenletek egyelőre maradnak. A paraméteres feladatok besorolása továbbra is nyitott.

**2e/04 A2 részállapot (2026-10-01, külön helyi ág):** öt feladatlap 179 kártyáját átnéztük; 133 Végeredmény-doboz és 5 feladatszöveg pontosodott. A rövidítésből a kért indoklás, bizonyítás, szorzat alak és hibaazonosítás megmaradt; az egyszerűsített trigonometrikus törtek értelmezési feltétele, illetve az általános megoldások egész $k$ paramétere szerepel a válaszokban. A háromszögfeladatok három kerekítési hibája javítva (`alap-14`: `13,52`; `kozep-12`: `264,28`; `kozep-13`: `48,13°` és `96,87°`). A torony, a hajóforduló és a léggömb kérdése a geometriai helyzetet egyértelműen meghatározza. A kontextus nélküli lektor a háromszöges lap 34 feladatát önállóan megoldotta. A HTML-diff csak a 133 válaszra és 5 kérdésre, a keresőindex 308 bejegyzéséből csak az öt érintett URL-re esik. Az öt builder SymPy-öntesztje, a kánon 310/0, a linkek 310/0, a sávellenőrzés, a kulcsteszt 4865/4865, a regresszió 4865/4865 = 100% és az öt lap 360/390/1280 px-es böngészőpróbája rendben; a végső szövegpontosítás után a háromszöges lap külön böngészőpróbája is hibátlan. A teljes kulcstesztben nincs 2e kulcsmodul, a jsdom-réteg és valódi képernyőolvasós próba nem futott. **Tanári döntés kell:** az M2-skill és az operatív terv trigonometriahatára eltér; a feladatok átsorolása vagy elhagyása külön tartalmi adag.

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
| Q2 | Akadálymentesség: axe-core Playwrighttal (`npm i axe-core`), kontraszt, `aria`, fókusz-sorrend | ☐ |
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
