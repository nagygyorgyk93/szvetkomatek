<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): projektek/szvetkomatek/tortenet/_WEBOLDAL_tortenet.md · tükrözve: 2026-09-29 · _tools/docs_tukor.py -->

# Szvetkó matek — VILÁG-BIBLIA (a gamifikált köntös mesterfájlja)

> A weboldal köntöse. A **matematika mindig az úr** — ez csak a keret, amibe a tananyagot
> csomagoljuk. A köntös **moduláris**: minden fejezet önállóan is működik, és bármely
> anyagrészhez behozható illő film / sorozat / crossover.
>
> **Ez a fájl a közös alap** (világ, állandó szereplők, köntös-rétegek, vizuális rendszer).
> Az évadok részletei külön fájlokban élnek — egy munkamenetben **elég ez a mesterfájl +
> az éppen dolgozott évad fájlja**:
>
> | Évfolyam | Évad-fájl | Univerzum-ág | Fő ellenfél |
> |---|---|---|---|
> | 1e | `_WEBOLDAL_tortenet_1e.md` | Hősök Ligája | Kán, a Hódító |
> | 2e | `_WEBOLDAL_tortenet_2e.md` | Mutáns Osztag | Dr. Baljós |
> | 3e | `_WEBOLDAL_tortenet_3e.md` | A Különlegesek | Maxi, az Őrült |
> | 4e | `_WEBOLDAL_tortenet_4e.md` | Véd Vilmos & Nagol | I.V.H. / Mr. Szürreál |

---

## 1. Az alapötlet

A **Szvetkó-kampusz** a Hősök Ligája Akadémiájának európai bázisa (a valóságban: a szabadkai
Svetozar Marković Gimnázium). A tanuló itt **kadét**: minden témakör egy **küldetés**, minden
matematikai diszciplína egy **stabilizáló kulcs** a soron következő fenyegetés ellen. Az oldal
maga a kampusz belső rendszere; ahogy a kadét halad, úgy nyílnak a következő szektorok.

**Pedagógiai mag (évadtól függetlenül):** a fő ellenfél fegyvere mindig a **hamis állítás, a
torz „bizonyítás", az elhallgatott feltétel**. A kadét fegyvere a **hibakeresés, az indoklás és
a verifikáció** — pontosan az, amit a tanterv is céloz (STK2: önelemzés, indoklás). A köntös
sosem old fel szakmai pontatlanságot: ha egy hős rosszul számol, azt a diáknak kell kijavítania.

## 2. A helyszín

**a Hősök Ligájának Akadémiája — Szvetkó-kampusz** (Szabadka). Évadról évadra bővül és sérül: a 2. évben
földalatti **Vészteremmel (Vészterem)**, a 3.-ban a **Kristálypára Karantén-Zónával**, a 4.-ben
egy **„törölt" idővonallal (The Void)** és az I.V.H. szervertermeivel. A kampusz épületei a valós
iskolai tereknek felelnek meg (lásd 6. pont) — ezek adják az oldal háttérképeit is.

## 3. Az évadok íve

| Évad | Fenyegetés | A matematikai tartalom, ami legyőzi | Klimax |
|---|---|---|---|
| **1e** — *Nullpont-anomália* | Kán hamis egyenletekkel tágítja a valóság szakadását | logika, halmazok, függvények, trigonometria, számhalmazok, arányosság, geometria, algebrai kifejezések, lineáris egyenletek | „A Végső Egyenlet" (07) + epilógus (08) |
| **2e** — *M-Hullám* | Dr. Baljós erőszakolt evolúciója kaotikussá teszi az egyenleteket | hatványok/gyökök/komplex számok, másodfokú egyenletek és függvények, exponenciális–logaritmikus, trigonometrikus függvények | „A Rezonancia-hullám" (04) |
| **3e** — *Kristálypára-anomália* | Maxi kristályosítja és meggörbíti magát a teret | poliéderek, forgástestek, egyenletrendszerek, vektorok, analitikus geometria, sorozatok + indukció | „A Végtelen Mutáció" (06) |
| **4e** — *Törölt idővonal* | Az I.V.H. „megmetszené" a teljes évfolyamot | sorozatok és függvények határértéke, derivált, integrál, kombinatorika, valószínűség és statisztika | „A Túlélés Esélyei" (06) |

> Az ív mindig ugyanaz a tanulási ív: **megérteni → modellezni → kiszámítani → bizonyítani.**

## 4. Állandó szereplők (minden évadban)

| Szereplő | Szerep | Eredet |
|---|---|---|
| **SZVETI** | a kampusz MI-asszisztense (filmes MI-asszisztensekre emlékeztető), a briefingek és a gyorstesztek hangja. Arca **Svetozar Marković** 19. századi portréjának holografikus változata. Évadonként „sérül": a 2e-ben glitch-el, a 4e-ben passzív-agresszív. | **saját** |
| **Nova** | a kadét-avatar, akin keresztül a diák azonosul; vele együtt lép évfolyamot | **saját** |
| **A kiképzőtiszt** | a tanár kibernetikus avatárja (fém kar, izzó technológiai szem) — az üdvözlő videó és a kiképzőtiszt-kártya szereplője | **saját** |
| **Nikola Furić parancsnok** | az Akadémia igazgatója; a nagy, évadnyitó eligazítások hangja | saját |

Az **évad-mentorok** (fejezetenként egy-egy hős) és az évad **fő ellenfele** az évad-fájlokban.

## 5. A köntös két rétege — mi FIX és mi évadfüggő

### 5a. FIX szerkezet (a `_WEBOLDAL_workflow.md` 4b. + 8. kánonja — köntösből NEM módosítható)

| Elem | Kötelező forma |
|---|---|
| tananyag `s0` szakasz | `<h2 id="s0">📡 Küldetés-eligazítás</h2>` + `.brief` doboz |
| kvíz | `.kviz` · címe **„🎯 Gyors kérdés"** |
| doboz-ikonok | definíció 📗 · tétel 📘 · példa ✏️ · csapda ⚠️ · érdekesség 💡 |
| feladatszintek | `.feladat.alap` / `.kozep` / `.nehez` / `.joker`, horgonyok `#alap-N` … |
| differenciált sávok | `.sav.henrik` (könnyített) / `.sav.bruno` (normál) — **az osztálynév szerep-alapú, a felirat évadfüggő** |
| házi | `feladatok-hazi.html`, témakörönként EGY, óraszám-arányos |
| végeredmény | `.vegeredmeny` lenyíló = **kizárólag a végső válasz** |

### 5b. Évadfüggő elnevezések (csak a látható SZÖVEG változik)

| Oldal-elem | 1e (Hősök Ligája) | 2e (Mutáns Osztag) | 3e (A Különlegesek) | 4e (Véd Vilmos) |
|---|---|---|---|---|
| témakör-index felütés | Szektor-belépő | UMOTRON-keresés | Kristályvár Archívum | A Negyedik Fal |
| `s0` brief hangja | SZVETI + mentor | Dr. Bestia / SZVETI (Mutációs elemzés) | Kanrak / Prizma (Kristály-elemzés) | Véd Vilmos (🌮 Burek-matek) |
| kidolgozott példa | Kiképzési szimuláció | Vészterem-szimuláció | Kristály-kamra szimuláció | I.V.H. Akták |
| kvíz-szöveg | gyorsteszt a HQ-tól | Reflex-teszt | Reflex-teszt | Kardcsapás-reflex |
| csapda-doboz | **Kán csapdája** | **Dr. Baljós vírus-kódja** | **Maxi trükkje** | **Vilmos csapdája** |
| feladatgyűjtemény | kiképzési adattár | Kiképzési Adattár | Kiképzési Adattár | Zsoldos-lista |
| házi (Vészterem) | Vészterem | Vészterem | Kristály-kamra | I.V.H. Kihallgató Terem |
| könnyített sáv | 🐜 Henrik-bevetés | 🐾 Bestia-protokoll | 🐕 Tér-eb-ugrás | 🐶 Véd-eb nyomravezető |
| normál sáv | 💥 Brúnó-bevetés | 🔥 Főnix-protokoll | 👑 Királyi Gárda | ⚔️ Maximális erőbedobás |
| projekt | terepküldetés | Geno-szigeti terepküldetés | Kristályvár terepküldetés | Az Üresség tisztítása |
| összefoglaló | bevetési kártya | Taktikai memóriakártya | Taktikai memóriakártya | Csalópapír |
| felmérő (privát) | minősítő vizsga | minősítő vizsga | minősítő vizsga | I.V.H.-meghallgatás |

## 6. Vizuális rendszer — helyszínek, hátterek, média

A valós iskolai terek képregényes stílusú változatai adják az oldal **fix háttérképeit**
(`web/assets/img/`, WebP; `_1` = fekvő, `_2` = álló változat). A hozzárendelést a
`body[data-hatter]` attribútum + a `theme.css` végzi, az attribútumot a
`_tools/set_hatter.py` írja ki oldaltípus szerint:

| Helyszín | Kép | Hol jelenik meg |
|---|---|---|
| Szvetkó-kampusz **főépülete** (S.Z.V.E.T.I. Központ) | `foepulet` | főhadiszállás (landing) + témakör-indexek |
| **Díszterem** — holografikus eligazító | `diszterem` | tagozat-indexek + kereső |
| **Taktikai és Elemző Központ** (általános terem) | `altalanos` | tananyag-oldalak |
| **Tech-Labor / Páncélműhely** (digitális terem) | `digitalis` | feladatgyűjtemények + összefoglalók |
| **Vészterem** (tornaterem) | `tornaterem` | Vészterem házi feladatsorok |
| **Misztikus Művészetek Műterme** (rajzterem) | `rajzterem` | terepküldetések |

**Szabályok:** a háttér **fix** (nem gördül), `cover` méretezésű (sosem torzul; inkább lelóg
belőle egy sáv), 1:1-nél keskenyebb kijelzőn az **álló** változat jön. Fölötte sötétítő fátyol
(`--hatter-sotet`), a hosszú szöveges oldalakon enyhe lágyítással — a szövegkontraszt mindenütt
WCAG **AAA** fölött marad. Új helyszín hozzáadása: 2 kép (fekvő+álló) → 1 blokk a `theme.css`-be
→ 1 sor a `set_hatter.py` `TIPUS` szótárába.

**Karakterképek:** `web/assets/img/` — négyzetes portré (`nev.jpeg`) és ahol van, teljes alakos
fekvő változat (`nev_2.jpeg`). A weboldal **nem ezeket** hivatkozza közvetlenül, hanem a belőlük
generált, tömörített WebP-derivátumokat: `web/assets/img/kar/nev.webp` (320×320 avatar, ~25 kB)
és `web/assets/img/kar/nev_w.webp` (1200 px széles banner, ~100–200 kB). Új karakterkép
hozzáadása: 1–2 JPEG az `img/`-be → derivátum a `kar/`-ba → felvenni a `_tools/kepek.py` `KAR`
szótárába. A briefek két formája: `.brief.karakter-nagy` (az `s0` eligazítás, teljes alakos
banner) és `.brief.karakter` (minden más brief, kerek avatar).

**Egyéb média:** `svetozar.webp` (SZVETI portré, a `.brief.szveti` avatarja) · `me.webp`
(kiképzőtiszt, `.mentor-sor`) · `welcome.mp4` + poszter (üdvözlő videó a landingen: néma
automata lejátszás + „🔊 Hang be" gomb egyszeri hangos futásra). Az eredeti nagy felbontású
állományok a repón kívül: `Claude\projektek\szvetkomatek\web_forras\`.

**Tervezett bővítés:** további helyszín-képek a nagyobb változatosságért; képregényesített
matek-mémek a tananyagokba; küldetésnapló / progresszió-felület a kadét haladásához.

## 7. Hangnem és szabályok (minden évadra)

- **Matek-első:** a sztori sosem megy a szakmai pontosság rovására; a köntös elhagyható
  anélkül, hogy a feladat sérülne. Ahol nem illik ötletesen, ott **nem erőltetjük**.
- **Korosztály-skála:** 1e (≈15) lelkes és pörgős → 2e (≈16) drámaibb → 3e (≈17)
  fegyelmezettebb, „királyibb", tudományosabb → 4e (≈18) önreflexív, ironikus, de
  **iskolai keretek között** (káromkodás helyett kreatív cenzúra).
- **Nevek:** a szereplőgárda **teljes egészében saját** — magyaros és balkáni-szerb ízű nevek
  (Hangya Henrik, Dr. Bestia, Crni Grom, Véd Vilmos…), a narráció magyarul. **Jogvédett
  karakter- és márkanév nem kerülhet be** sem a szövegbe, sem osztálynévbe, sem képfájlnévbe;
  új szereplő kitalálásakor a 8. pont Névtára az irányadó.
- **Következetesség:** a visszatérő szereplők és a szektor-mentorok mindig ugyanazok maradnak,
  hogy a diák ráismerjen a világra; az interfész-elemek évadról évadra ugyanott vannak.
- **Az ellenfél hibái valódi diákhibák** (nullával osztás elrejtése, feltétel elhagyása,
  hamis megfordítás) — így a köntös maga is tananyag.
- **Semmi sötét/ijesztő túlzás**, semmi valós személyre vonatkozó gúny.

## 8. Névtár — a Szvetkó-kampusz szereplőgárdája

> A teljes gárda **saját**. Ez a táblázat a kánon: ha új oldal, feladat vagy évad készül,
> innen kell nevet venni. A „képtörzs" oszlop az `assets/img/kar/` derivátumok neve
> (`+w` = van teljes alakos fekvő banner is).

### Állandók

| Szereplő | Szerep | Képtörzs |
|---|---|---|
| **SZVETI** | a kampusz MI-asszisztense | `svetozar` |
| **Nova** | a kadét-avatar | — |
| **A kiképzőtiszt** | a tanár kibernetikus avatárja | `me.webp` |
| **Nikola Furić parancsnok** | az Akadémia igazgatója | `furic_nikola` |
| **Pajzs kapitány** | a teljes csapat vezetője a fináléban | `pajzs_kapitany` |
| **Nada** | terepfelderítő; a becslés és a korlátok mestere | `nada` |

### 1e — *A Nullpont-anomália* (Hősök Ligája)

| Szereplő | Szerep | Képtörzs |
|---|---|---|
| **Kán, a Hódító** | a fő ellenfél; hamis állításokkal támad | — |
| **Krats Ynot** | fővezető-mérnök | `krats_ynot` +w |
| **Denveri Karolina** | kiképzőtiszt, a felmérők gazdája | `denveri_karolina` |
| **Ikol** | logika — igaz vs. hamis | `ikol` +w |
| **Dr. Bizarr** | halmazok, multiverzum-térkép | `dr_bizarr` +w |
| **Petar Pauk** | függvények, hálók | `pauk_petar` +w |
| **Barton Kálmán** | trigonometria, célzás | `barton_kalman` +w |
| **Iruhs** | számrendszerek, tech | `iruhs` |
| **Banner Brúnó** | közelítés, hibabecslés | `banner_bruno` +w |
| **Hangya Henrik** | arányosság, skálázás | `hangya_henrik` |
| **Darázs Dorka** | Zsugor-protokoll | `darazs_dorka` |
| **Vanda** | geometria, tükör-világ | `vanda` |
| **Fürge Pjotr** | vektorok, mozgás | `furge_pjotr` +w |

### 2e — *Az M-Hullám* (Mutáns Osztag)

| Szereplő | Szerep | Képtörzs |
|---|---|---|
| **Dr. Baljós** | a fő ellenfél; „tökéletesített", kaotikus egyenletek | — |
| **X. Károly professzor** | az évad nagy elméje; komplex számok | `x_karoly` +w |
| **Dr. Bestia** | fővezető-tudós; exponenciális és logaritmus | `dr_bestia` |
| **Vihar Vera** | hatványok, gyökök | `vihar_vera` |
| **Nagol** (hadnagy) | másodfokú egyenletek | `nagol` +w |
| **Küklopsz** | másodfokú függvények | `kuklopsz` |
| **Magnetron** | szögek, periódus | `magnetron` +w |
| **Szürke Janka** | szinusz- és koszinusztétel | `szurke_janka` |
| **Éjjáró** | trigonometrikus kör, azonosságok | `ejjaro` |

### 3e — *A Kristálypára-anomália* (A Különlegesek)

| Szereplő | Szerep | Képtörzs |
|---|---|---|
| **Maxi, az Őrült** | a fő ellenfél; torz tér-egyenletek | — |
| **Crni Grom** | a Néma Király; vektorok | `crni_grom` |
| **Medúza** | az eligazítások hangja; forgástestek | `meduza` |
| **Kanrak** | egyenletrendszerek, analitikus geometria | `kanrak` |
| **Prizma** | térgeometria, poliéderek | `prisma` |
| **Tér-eb** | teleportáló kutya; koordináta-ugrások | `ter_eb` |

### 4e — *A Törölt Idővonal*

| Szereplő | Szerep | Képtörzs |
|---|---|---|
| **Mr. Szürreál** | a fő ellenfél; az I.V.H. bürokratája | — |
| **Véd Vilmos** | a „mentor", aki áttöri a negyedik falat | `ved_vilmos` +w |
| **Nagol** | a morcos helyettesítő; a komoly analízis | `nagol` +w |
| **Véd-eb** | variáns; nyomravezető | `ved_eb` |
| **Mini-Vili** | variáns | `baby_vili` |
| **Nyalka Vili** | variáns; kombinatorika | — |

### Szervezetek, helyszínek, fogalmak

| Elem | Név |
|---|---|
| a hősszervezet | **Hősök Ligája** |
| a mutáns-szervezet | **Mutáns Osztag** · központja az **X. Károly Intézet** |
| a 3e népe | **A Különlegesek** · városuk **Kristályvár** |
| az időrendőrség | **I.V.H.** (Idővonal Védelmi Hivatal) |
| a kampusz központi rendszere | **S.Z.V.E.T.I. Központ** |
| az elmekereső gép | **UMOTRON** |
| a szimulációs edzőterem | **Vészterem** |
| a 2e ellenfél bázisa | **Geno-sziget** |
| a 3e anomália | **Kristálypára** · karanténja a **Kristály-kamra** |
| a méretskálázó eljárás | **Zsugor-protokoll** |
| Véd Vilmos kedvenc étele | **burek** |
| a normál sáv csatakiáltása | **Maximális erőbedobás** |

## 9. Fájl-térkép

- `_WEBOLDAL_tortenet.md` — **ez a fájl**: világ, állandó szereplők, köntös-rétegek, vizuális
  rendszer, **Névtár** (a teljes szereplőgárda + a szervezet- és helyszínnevek kánonja).
- `_WEBOLDAL_tortenet_[osztály].md` — évadonként: logline, helyszín, tét, szereplők, fejezet-térkép,
  köntös-szótár, hangnem, kidolgozási jegyzetek.
- `_WEBOLDAL_workflow.md` — architektúra + a KÖTELEZŐ szerkezeti kánon (4b. tananyag, 8. feladat).
- `_WEBOLDAL_prompt_sablon.md` — a témakör-pipeline (F0–F6).
- `_WEBOLDAL_allapot.md` — élő állapot, témakörönkénti leltár.
