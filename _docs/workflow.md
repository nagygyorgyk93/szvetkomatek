<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): projektek/szvetkomatek/_WEBOLDAL_workflow.md · tükrözve: 2026-09-27 · _tools/docs_tukor.py -->

# GitHub Pages tananyag-oldal — komplett workflow (mind az 5 tagozat)

> **Jelölés-kánon:** minden matematikai jelölés a **`_JELOLESEK.md`** szerint
> ($H$, $h$, $s$, $D$, $d$, $r$, $R$, $B$, $M$) — ettől eltérni nem szabad.

**Cél:** az összes tanulói anyag (tananyag + feladatgyűjtemény + tömör összefoglaló)
egyetlen, egységes stílusú, GitHub Pages-en publikált weboldalon, tagozatonként és
témakörönként rendszerezve, sűrű kereszthivatkozásokkal.

## Rögzített döntések (2026-07-22)

> **Helyek (2026-09-27 óta):** a repó-klón `Claude\web\` (publikus); minden privát webes anyag a `Claude\projektek\szvetkomatek\` alatt (térkép: `OLVASSEL.md`) — a `_WEBOLDAL_*` fájlok, `tortenet\`, `web_forras\`, `tiltott\`, osztályonként `1e\`…`4e\` (F0, narratíva, F3-térkép, lektor, terepküldetés-kulcs). **Felmérő-adat a repóba nem kerülhet, a builderek forráskódjába sem:** a tiltott-listák a `projektek\szvetkomatek\tiltott\tiltott_<osztály>_<NN>.py` privát modulokban élnek, a builder a `_tools/builders/tiltott.py` betöltővel éri el őket (`tiltott.modul(…)`, `tiltott.lista(…)`); ha a mappa nem érhető el (felhős munkamenet), figyelmeztetéssel, ellenőrzés nélkül fut.

- **Egy közös repo** mind az 5 tagozatnak (1e, 2e, 3e, 4e, 4im), osztályonkénti almappákkal.
- **KaTeX a repóban** (nem CDN): nyomdai minőségű matek, offline klónban is működik.
- **Publikus repo** (van GitHub-fiók). **A felmérők SOHA nem kerülnek fel** — azok
  maradnak DOCX-ben, a lokális projektmappákban.
- **Feladatgyűjtemény**: teljes egészében weben (nem DOCX); minden feladatnál
  **lenyíló „Végeredmény”**.
- **Témakörön belüli sorrend:** 1) tananyagok (altémánként) → 2) feladatgyűjtemény
  (altémánként) → 3) tömör összefoglaló (a témakör legvégén, szintén HTML).
- **DOCX csak ott marad, ahol Word kell:** felmérők + megoldókulcsok
  (`feladatlap-es-dokumentum` skill, változatlanul).
- A munka az **1e-vel folytatódik**, témakörönként haladva; a többi tagozat utána,
  ugyanezzel a pipeline-nal.

## 1. Repo és publikálás

- **Repo:** 1 db, javasolt név pl. `matek` vagy `matek-tananyagok` (rövid URL-t ad:
  `https://<felhasznalo>.github.io/matek/`). Branch: `main`, Pages forrás: `main` / root.
- **Kötelező:** `.nojekyll` fájl a gyökérben (különben a Jekyll-build kihagyja a
  `_`-sal kezdődő mappákat és lassítja a deployt).
- **Lokális klón:** `Oktatás\Claude\web\` — így egy Cowork-munkamenetben a szülő
  `Oktatás\Claude` mappát csatolva egyszerre elérhető a forrás (osztálymappák) és a
  repo-klón is.
- **Publikálás (nincs Cowork GitHub-connector, ellenőrizve 2026-07-22):**
  1. **Elsődleges:** Claude a Windows-MCP PowerShellen át futtatja a `git add/commit/push`-t
     a lokális klónban (előfeltétel: Git + egyszeri GitHub-bejelentkezés, pl. GitHub
     Desktop vagy `git credential manager`). Minden push előtt megmutatja, mi megy fel.
  2. **Tartalék:** kézi push GitHub Desktopból.
- Deploy automatikus push után ~1 perc alatt.
- **Felhős munka (Claude Code on the web, 2026-09-27):** a felhő csak a repót látja. Ezért a repóban:
  `CLAUDE.md` (publikus-biztos útmutató), `_docs/` (a workflow, a jelölés-kánon és a köntös-bibliák
  **tükre** + a repó-saját `FELHO_FELADATOK.md` backlog), `.claude/settings.json` (SessionStart-hook →
  `_tools/felho_setup.sh`), `.claude/skills/` (media-beagyazas + a web-verifikacio és a matek-abra
  tükre). **Ha a kánon (ez a fájl, `_JELOLESEK.md`, `tortenet\`, a két skill) változik, futtasd:**
  `python _tools/docs_tukor.py --apply` (fehérlistás, tartalmi szűrővel). A felhő ágon + PR-rel
  dolgozik; merge után **helyben Pull** (GitHub Desktop), mielőtt Cowork folytatja. A zárolt
  területeket a `_docs/FELHO_FELADATOK.md` tartja nyilván — helyben induló témakört oda fel kell venni.

## 2. Mappa- és fájlstruktúra

```
web/                              ← repo gyökér = lokális klón
├── .nojekyll
├── index.html                    ← főoldal: tagozatválasztó
├── assets/
│   ├── css/theme.css             ← teljes design-rendszer (1 fájl)
│   ├── css/print.css             ← nyomtatási/PDF nézet
│   ├── js/ui.js                  ← TOC, scroll-progress, lenyílók, prev/next, videó
│   ├── js/quiz.js                ← mini-kvíz motor (data-answer alapú)
│   ├── katex/                    ← KaTeX js+css+fonts (repóba letöltve)
│   ├── img/                      ← helyszín-hátterek (WebP, `_1` fekvő / `_2` álló),
│   │                               portrék (svetozar, me), welcome.mp4 + poszter
│   └── img/common/               ← logó, favicon, közös dekor (SVG)
├── 1e/
│   ├── index.html                ← 1e nyitóoldal: témakörlista státusz-jelzőkkel
│   ├── 01-logika-halmazok-fuggvenyek/
│   │   ├── index.html            ← témakör-nyitó (mi van benne, ajánlott sorrend)
│   │   ├── tananyag-logika.html
│   │   ├── tananyag-halmazok.html
│   │   ├── tananyag-fuggvenyek.html
│   │   ├── feladatok-logika.html
│   │   ├── feladatok-halmazok.html
│   │   ├── feladatok-fuggvenyek.html
│   │   ├── osszefoglalo.html     ← tömör összefoglaló (a témakör végén készül)
│   │   └── img/                  ← témakör-specifikus képek (mémek is)
│   ├── 02-<kovetkezo-temakor>/ …
│   └── …
├── 2e/ …   ├── 3e/ …   ├── 4e/ …   └── 4im/ …
├── _tools/                       ← build_search_index.py, check_links.py,
│   │                               set_hatter.py, builders/ (feladatgyűjtemény-építők)
└── _sablonok/                    ← HTML-vázak (tananyag / feladatok / összefoglaló /
                                     témakör-index) — ebből indul minden új oldal
```

**A repón KÍVÜL:** `Claude\projektek\szvetkomatek\web_forras\` — az eredeti, nagy felbontású médiaállományok
(PNG-k, `welcome.mov`) és a régi történet-vázlatok archívuma. A GitHub-repóba csak a
webre optimalizált WebP/MP4 kerül.

**Konvenciók (a modularitás kulcsa):**

- Témakör-mappa: `NN-slug` (NN = sorszám az éves terv sorrendjében; slug = kisbetű,
  ékezet nélkül, kötőjellel). Új témakör/tagozat = új mappa + 1 sor az indexben.
- Fájlnevek fixek: `tananyag-<altema>.html`, `feladatok-<altema>.html`,
  `osszefoglalo.html`, `index.html`. Ettől eltérni nem szabad — a kereszthivatkozások
  kiszámíthatósága múlik rajta.
- Minden oldal csak a közös `assets/`-re támaszkodik (relatív úton); oldalba ágyazott
  egyedi CSS/JS csak **interaktív ábrához** — ez viszont **kifejezetten kívánatos**, ahol a dinamikus
  szemléltetés segít (felhasználói döntés, 2026-09-24; a részletszabály a 4b. oldal-anatómiában).

## 3. Kereszthivatkozási rendszer

Stabil horgony-ID-k mindenhol, előre kiszámítható linkekkel:

- **Feladatok:** `#alap-3`, `#kozep-5`, `#nehez-2`, `#gyt-1` (gyakorló teszt), `#joker`.
  Példa: `feladatok-logika.html#kozep-5`.
- **Tananyag:** `#def-<slug>`, `#tetel-<slug>`, `#pelda-<slug>` (pl. `#def-metszet`,
  `#tetel-de-morgan`), szekciók: `#s1`, `#s2`, …
- **Évfolyamok/témakörök között** relatív út:
  `../../1e/01-logika-halmazok-fuggvenyek/tananyag-halmazok.html#def-metszet` —
  így pl. a 2e tananyag visszamutathat az 1e definícióira.
- **Előre-hivatkozás megengedett:** mivel a fájlnevek és ID-k konvencióból adódnak, a
  tananyag már hivatkozhat a még el nem készült feladatgyűjteményre; a gyűjtemény
  elkészültekor link-checkkel validáljuk (7. pont).
- A feladat-ID-k **véglegesek**: utólagos beszúrás új számot kap a sor végén, a
  meglévők nem számozódnak át (különben a régi linkek elromlanak).

## 4. Design-rendszer — „zöld matek” téma

Fiatalos, modern, matekos; domináns zöld, ízléses kiegészítő színekkel. A meglévő 1e
tananyagok design-elemei (sticky TOC, scroll-progress, színes dobozok, mini-kvízek,
mémek) megmaradnak, közös CSS-be szervezve.

**Színtokenek (`theme.css`, CSS-változók):**

- Alap: zöld `#047857` / `#10b981` / halvány `#d1fae5`; tinta `#0f172a`;
  háttér `#f8fafc`; kártya `#fff`.
- Funkciószínek (dobozok): **definíció = zöld**, **tétel = kék** `#3b82f6`,
  **példa = borostyán** `#f59e0b`, **„vigyázz, csapda!” = piros** `#ef4444`,
  **érdekesség = lila** `#8b5cf6`.
- **Tagozat-accent** (`body[data-tagozat]`): 1e `#10b981`, 2e `#14b8a6`, 3e `#06b6d4`,
  4e `#84cc16`, 4im `#6366f1` — fejléc-sávban, morzsamenüben, chipeken jelenik meg;
  az oldal egésze zöld marad.
- Szint-chipek: Alap = zöld, Közép = borostyán, Nehéz = piros; Joker = lila.

**Tipográfia és matekos karakter:** modern betű (self-hostolt woff2, pl. cím: Space
Grotesk-jellegű, szöveg: Inter-jellegű; fallback system-ui); hero-sávban halvány
matek-szimbólum minta (SVG: ∑ π √ ∫ ∞); favicon: zöld „√” vagy „∑”.

**Komponenskészlet:** morzsamenü (tagozat → témakör → oldal) · sticky TOC ·
scroll-progress · kiemelődobozok · `<details>` lenyílók (bizonyítás, megoldás,
végeredmény) · mini-kvíz instant visszajelzéssel · feladatkártya (sorszám +
szint-chip + KaTeX szöveg + lenyíló végeredmény) · „Gyakorolj!” linkdoboz a tananyag
szekciói végén · előző/következő navigáció · print.css (TOC/kvíz elrejt, lenyílók
nyomtatásban kinyitva).

**Matek-render:** KaTeX auto-render, inline `\( \)`, kiemelt `\[ \]`. **Minden képlet
KaTeX** — Unicode-matek tilos (kivétel: táblázatcellák és SVG-feliratok szimbólumai).

### 4b. Tananyag-egység KÁNON (kötelező minden oldalra — 2026-07-22)

- **Bontás:** témakör → altémánként **2–4 egység-oldal**; egy egység 3–6 h2-szakasz
  (~1–3 tanóra anyaga, jellemzően 10–25 KB szöveg). Fájlnév `tananyag-<slug>.html`,
  **számozás nélkül** — a sorrendet a témakör-index és a lapozó-lánc adja.
- **`<body>` attribútumok:** `data-tagozat="1e"` (accent-szín) + `data-hatter="…"`
  (helyszín-háttér, lásd 4c.) — az utóbbit a `_tools/set_hatter.py` írja ki, kézzel nem kell.
- **Oldal-anatómia (fix sorrend):** `#progress` → `.fejlec` (site-logó + mini-kereső)
  → `.morzsa` (**Főhadiszállás** › tagozat › témakör › oldal) → `.hero` (h1 **emoji nélkül**;
  `.alcim` 1–2 mondat; `.meta-sor`: `tananyag` chip + többaltémás témakörnél
  `Altéma · i/n` chip) → `main.lap.toc-os` (**tartalom balra, TOC jobbra** — a TOC-ot
  az ui.js generálja a h2-kből) → `.lapozo` → `.lablec` → KaTeX + ui.js + quiz.js.
  Oldalankénti saját `<style>`/`<script>` **tilos** — kivétel az **interaktív ábra**, amely bátran
  használható (felhasználói döntés, 2026-09-24): a `<script>` csak a saját ábráját kezeli (egyedi `id`,
  IIFE, globális változó nélkül), külső könyvtár nélkül; **JS nélkül is értelmes kezdőállapot** (a statikus
  SVG maga az első képkocka); a vezérlő `<input type="range">`/gomb **címkével**, billentyűzettel is
  kezelhető; a színek a téma-változókból (világos/sötét); a `verify_web` hibátlan. Ha ugyanaz a
  widget 2+ oldalon kell, kerüljön az `assets/`-be közös modulként.
- **Szakaszok:** `h2 id=”s0”,”s1”,…` sorban; **s0 mindig „📡 Küldetés-eligazítás”**
  (a mentor/SZVETI `.brief` doboza: 2–5 mondat motiváció, valós alkalmazás — a köntös-nevet
  az évad-biblia adja). Címszövegben **kézi számozás tilos**
  (h2/h3 egyaránt); emoji címben csak s0-ban és a záró „🧾 Gyorsismétlő”-ben
  (opcionális, csak az altéma utolsó egységének végén állhat).
- **Dobozok:** `.doboz.<típus>` + `<p class="cim"><span class="ikon">I</span> Cím</p>`;
  az ikon a típushoz **rögzített**: definíció 📗 · tétel 📘 · példa ✏️ · csapda ⚠️ ·
  érdekesség 💡 (alkalmazás / megegyezés / memóriahorog is az `erdekesseg` típusba).
  A cím lehet beszédes („Hol találkozol vele?”) — az ikon akkor sem tér el.
- **Kvíz:** `.kviz[data-answer]`, címe mindig „🎯 Gyors kérdés”, 2–4 gombopció,
  egységenként legalább 1. **Gyakorolj:** `.gyakorolj` doboz, konkrét horgony-linkekkel
  (`feladatok-….html#alap-N`).
- **Lapozó-lánc (kánon):** index → altéma₁ egységei sorban → `feladatok-altéma₁` →
  altéma₂ egységei → … → utolsó `feladatok-*` → `osszefoglalo` → „Vissza →” index.
  Az első egység Előzője a témakör-index; a lánc minden oldal alján `.lapozo`.
- **Segédosztályok** (mind a theme.css-ből): `.lead` (felvezető), `.tt`/`.ff`
  (igaz/hamis szín), `table.tt-table` + `.res` (igazságtáblázat), `.tblwrap`,
  `.kbd`, `.pill`, `.clean`, `.venn`/`.vbox`, `.svgwrap`/`.svgcard`/`.cap`, `.ic`.
- **Témakör-index:** Tananyag-rács; 2+ altémánál `h3`-csoportok altémánként (a h3-on
  lehet emoji); kártyacím = egység-cím (emoji nélkül) + 1 soros leírás; alul
  Feladatgyűjtemény- és Összefoglaló-rács, végén „ajánlott sorrend” mondat.

### 4c. Vizuális réteg KÁNON — sötét téma, helyszín-hátterek, média (2026-07-31)

**Permanens sötét téma.** Az oldalnak nincs világos módja; a `theme.css` egyetlen, sötét
S.Z.V.E.T.I. Központ/UMOTRON design-rendszer (üveg-panelek `backdrop-filter`-rel, neonzöld akcentus,
tech-gördítősáv). **Világos felület csak egy helyen van:** az ábrák „tervrajz-lapja"
(`.svgcard`, `.venn .vbox`, `.svgwrap>svg`) — az inline SVG-k sötét tintával rajzolnak, ezért
a keretük világos marad. **Új SVG-t is így kell tervezni** (sötét vonal világos lapon).

**Helyszín-hátterek.** Minden oldal háttere egy fix, torzításmentes helyszínfotó:

| `data-hatter` | Helyszín | Oldaltípus |
|---|---|---|
| `foepulet` | Szvetkó-kampusz főépülete | Főhadiszállás (landing) + témakör-indexek |
| `diszterem` | holografikus eligazító | tagozat-indexek + kereső |
| `altalanos` | Taktikai és Elemző Központ | tananyag-oldalak |
| `digitalis` | Tech-Labor / Páncélműhely | feladatgyűjtemények + összefoglalók |
| `tornaterem` | Vészterem (Vészterem) | `feladatok-hazi.html` |
| `rajzterem` | Misztikus Művészetek Műterme | `terepkuldetes.html` |

- **Technika:** a kép a `body::before` fix pszeudo-elemen ül (nem `background-attachment:fixed`
  — azt a mobil böngészők rosszul kezelik), `cover` méretezéssel: **soha nem torzul**, inkább
  lelóg belőle egy sáv. **1:1-nél keskenyebb** (álló) kijelzőn az `_2` (álló), egyébként az
  `_1` (fekvő) változat jön. Fölötte sötétítő fátyol (`--hatter-sotet`), a hosszú szöveges
  oldalakon enyhe lágyítás.
- **Kontraszt-szabály:** a fátyol erőssége úgy van beállítva, hogy a világos szöveg a kép
  **legvilágosabb pontján is** WCAG **AAA** (≥7:1) kontrasztú legyen. Új háttérkép
  hozzáadásakor ezt ellenőrizni kell (a 7. pont szerinti kontraszt-teszt).
- **Kiosztás:** `python _tools/set_hatter.py` (a `TIPUS` szótár tartja a szabályt) — minden
  új oldal után lefuttatandó, idempotens.
- **Új helyszín felvétele:** 2 kép (fekvő + álló) WebP-ben az `assets/img/`-be → 1 blokk a
  `theme.css` „Oldaltípus → helyszín" listájába → szükség esetén 1 sor a `set_hatter.py`-ba.

**Média-konvenciók.**

- **Kép:** WebP, `quality 80` (háttér) / `84` (portré); a nagy felbontású eredeti a repón
  kívül, a `Claude\projektek\szvetkomatek\web_forras\` mappában marad. Háttérnél a natív felbontás elég (a fátyol
  miatt nem látszik a lágyulás), portrénál 640 px.
- **Videó (átlátszó háttérrel):** elsődleges forrás **WebM / VP9 + alfa** (`-pix_fmt yuva420p
  -auto-alt-ref 0`, Opus hang), tartalék MP4 (H.264+AAC, faststart), poszter **átlátszó WebP**.
  **Mindig az eredeti, alfás forrásból dolgozz** (a vágóprogramok — pl. CapCut — exportnál
  könnyen elvesztik az átlátszóságot; ilyenkor a vágást inkább ffmpeg végezze). Fontos: a
  WebM-alfa csak akkor marad meg, ha a **dekódolás is** `-c:v libvpx-vp9`-cel történik (a
  natív ffmpeg-dekóder eldobja az alfa-síkot). Ha a forrásban nincs alfa, a maszkot **a
  széllel összefüggő fekete régiókból** lehet építeni (scipy `label` + peremkomponensek),
  hogy a figurán belüli fekete részek — pl. mintás ing — ne lyukadjanak ki; ez azonban a
  zugokban (kar–fej között) foltokat hagyhat, ezért csak végszükség esetén. A landing videója **némán, automatikusan**
  indul és ismétlődik; a **„🔊 Hang be"** gomb egyszer, hanggal játssza le, majd visszaáll néma
  ismétlésre (a böngészők a hangos automata indítást tiltják). `prefers-reduced-motion` esetén
  nincs automata indítás. Az `ui.js` canvas-teszttel ellenőrzi, hogy a böngésző kezeli-e az
  alfát; ha nem (pl. Safari), a panel `nincs-alfa` osztályt kap → `mix-blend-mode:screen`.
- **Portrék:** `svetozar.webp` → `.brief.szveti` avatar (SZVETI), `me.webp` → `.mentor-sor`
  (kiképzőtiszt).
- **Külső média — YouTube-videó, GeoGebra-szimuláció (2026-09-27):** csak a katalógusból
  (`web/_tools/media/[osztály].json`), a `_tools/media.py . --apply` teszi a lapra
  `<!-- media:begin/end -->` jelölők közé (idempotens; a builder-láncban a `kepek.py` után).
  **Kattintásra töltődik** (`assets/js/beagyazas.js`, az `ui.js` tölti be): előtte semmi nem megy
  harmadik félhez, JS nélkül link a forrásra, nyomtatásban cím + rövid URL. YouTube a
  `youtube-nocookie.com`-ról. GeoGebra-anyag: CC BY-NC-SA 4.0, a szerző neve kötelező (a
  `media.py` kiírja). Elsődleges videóforrás: MNT Távoktatás magyar nyelven (egyedi óra-oldalak;
  a listaoldalakat a robots.txt tiltja). Szabályzat: repó-skill `web/.claude/skills/media-beagyazas`.

### 4d. Küldetésnapló + mikro-animációk (2026-07-31)

**Küldetésnapló** (`assets/js/naplo.js`, oldal: `kuldetesnaplo.html`): a kadét haladása a
böngésző `localStorage`-ában él (nincs szerver, nincs adatgyűjtés, a tanár nem látja).
Pontozás: tananyag-egység/összefoglaló **10 XP**, gyors kérdés **5 XP**, terepküldetés **30 XP**,
a feladatok pedig **nehézség szerint**: Alap **2**, Közép **3**, Nehéz **5**, Joker **5**, a
gyakorló blokkok szint nélküli kártyái **2 XP** (a szintet a kártya `class`-a adja — az `id`
nem megbízható, mert a gyakorló és a terepküldetés-kártyák beszédes horgonyt kapnak).
Rangok: Újonc → Kadét → Ügynök → Elit ügynök → Bosszúálló → Legenda
(0 / 180 / 500 / 950 / 1550 / 2200 XP; az 1e teljes anyaga 2576 XP).

- **A HTML-oldalakat nem kell módosítani:** a naplo.js JS-ből injektál mindent — fejléc-chipet,
  „✅ Egység teljesítve" gombot, „megoldva" pipát minden `article.feladat[id]` kártyára (a pipa
  mellett ott a szint pontértéke), haladás-gyűrűt az index-kártyákra. A kvízeket a `quiz.js`
  `kviz-helyes` eseményéből veszi. A naplo.js-t és az effekt.js-t az **ui.js tölti be**.
- **Automatikus jelölés:** csak tananyagnál és összefoglalónál, és csak ha a kadét a lap
  **90%-áig eljutott ÉS legalább 25 másodpercet** töltött rajta (a gomb ilyenkor is azonnal
  átvált „Teljesítve" állapotba). A **terepküldetést mindig kézzel** kell bejelölni.
- **Nevezők + jelvények:** `_tools/build_naplo_terkep.py` → `assets/naplo-terkep.json` (témakörönként
  hány tananyag-egység / kvíz / feladatkártya / terepküldetés van, plusz a **jelvény**: küldetés-cím,
  mentor, jel — a szkript `JELVENY` szótárában). **Új témakör után futtatni kell**, és a `JELVENY`-be
  is felvenni egy sort (kimaradás esetén semleges 🛡️ jel + a témakör címe jár).
- **Jelvényfal:** minden **100%-ra teljesített** témakör pajzs-jelvényt ad a napló oldalán.
- **Átvitel másik eszközre:** napló-kód (base64) másolása/beillesztése a napló oldalán.
- **Új oldaltípus felvételekor** ellenőrizd, hogy a `naplo.js` felismeri-e (a fájlnév-minta
  dönt: `tananyag-*`, `osszefoglalo.html`, `terepkuldetes.html`, `feladatok-*`).

**Mikro-animációk** (`assets/js/effekt.js` + `theme.css`): jutalom-pillanatban képregényes pukkanás
(BANG!/POW!…) + lebegő „+XP" + rangemelés-szalag; halk háttérrétegként kártya-/doboz-beúszás
görgetéskor, apró szikra az interaktív elemek kattintására, rázás a hibás kvízválaszra,
**Kán-glitch** a csapda-doboz címén és **holografikus szkennelő fénycsík** a `.brief` HQ-adáson,
amikor a képernyőre érnek. QoL az `ui.js`-ben: **„🚀 vissza a tetejére"** gomb hosszú lapokon és
**`/` gyorsbillentyű** a keresőhöz.
**Kikapcsolható** a Küldetésnaplóban. A rendszer `prefers-reduced-motion` beállítása csak
**alapértelmezés**: ha a kapcsoló be van kapcsolva, a JS `html.effekt-be` osztályt tesz ki, és a
CSS mozgáscsökkentő blokkja (`html:not(.effekt-be)`) nem fojtja el az animációkat. **Figyelem:**
ezt a két helyet (JS `enged()` + CSS `:not(.effekt-be)`) együtt kell tartani — ha csak az egyik
tiltja, az effektek némán elmaradnak.
A beúszás CSS-e csak a JS által felrakott `html.anim-be` osztály alatt él → JS nélkül is
minden látszik, és nyomtatásban is teljes a tartalom.

**Nyomtatás.** A sötét téma miatt a `print.css` **teljes világos visszaállítást** végez
(univerzális `background:transparent; color:#000` + a háttérréteg elrejtése). Bármilyen új
komponensnél ellenőrizni kell a nyomtatási nézetet is.

## 5. Fázisok

**W0 — Infrastruktúra (egyszeri):**
repo létrehozás + Pages bekapcsolás → lokális klón `Claude\web` → `assets/` felépítése
(theme.css, ui.js, quiz.js, KaTeX letöltés, print.css) → `_sablonok/` 4 HTML-váza →
főoldal + 5 tagozat-nyitóoldal (témakörlisták az éves tervekből, státusz-jelzőkkel:
kész / készül / tervezett) → első push, élő URL ellenőrzése.

**W1 — 1e migráció (a kész Logika+Halmazok+Függvények témakör):**
1. A 3 kész tananyag-HTML átemelése az új sablonra (közös CSS-re kötés, Unicode-matek
   → KaTeX konverzió, gépi ellenőrzéssel; a tartalom változatlan).
2. A 3 feladatgyűjtemény DOCX → HTML (feladatkártyák, lenyíló végeredmények a meglévő
   kulcsból; a sympy-öntesztek eredményei érvényben maradnak).
3. Tömör összefoglaló DOCX → HTML (`osszefoglalo.html`).
4. Kereszthivatkozások élesítése („Gyakorolj” → konkrét feladat-horgonyok), 1e index
   frissítés, link-check, push.

**W2+ — Témakör-pipeline (ismétlődő, bármely tagozatra):**
részletesen a `_WEBOLDAL_prompt_sablon.md`-ben. Röviden: F0 feltérképezés (tantervi
skill + roadmap + forrásleltár) → **F1n narratíva-terv** → F1 felmérő-elemzés (DOCX,
privát, csak jóváhagyás utáni átdolgozás) → F2 tananyag-HTML-ek altémánként → F3
feladatgyűjtemény-HTML-ek altémánként **+ `kulcsok/` önteszt-modul** → F4
összefoglaló-HTML → F5 integráció (index, prev/next, link-check, push, állapotfájl).

> **F1n — narratíva-terv (2026-08-17 óta a pipeline része).** A `tananyag-narrativa`
> skill szerint, az F2 ELŐTT: egységhatárok, `h2`-beat-ív, ishod-lefedettség
> szabványkóddal, ⚠️ csapdák a célzott diákhibával, 🎯 kvízek a célzott tévképzettel,
> `.gyakorolj` horgony-terv, ábra-igény, köntös-slotok. Kimenet:
> `projektek\szvetkomatek\[osztály]\narrativa_[NN-slug].md`. Nem jóváhagyási kapu —
> megírod és mész tovább; **kivéve**, ha scope-ot érintő gondot találsz (otthon nélküli
> ishod, hiányzó forrás, aránytalan egységszám). A 2026-08-as visszamenőleges
> rekonstrukció négy valódi hibát talált pusztán attól, hogy a horgonyokat és a
> csapdákat egységenként fel kellett sorolni.

**Sorrend:** 1e következő témaköre az operatív terv szerint → 1e végig → többi tagozat
(javasolt: amelyikhez épp anyag kell a tanévben). A pipeline tagozatfüggetlen.

**Köntös (kötelező olvasmány a tartalomíráshoz):** `_WEBOLDAL_tortenet.md` (világ-biblia:
állandó szereplők, a FIX szerkezet vs. évadfüggő elnevezések, vizuális rendszer) +
`_WEBOLDAL_tortenet_[osztály].md` (az adott évad fejezet-térképe, mentorai, köntös-szótára).
Egy munkamenetben elég ez a kettő.

## 6. Öröklött kötelező elvek (a korábbi workflow-ból, változatlanul)

- **Matematikai precizitás nem alku tárgya** — a fiatalos köntös sosem megy a szakmai
  helyesség rovására. Célszint a tagozat szerint (társadalmi: O+S; im: feljebb).
- **Szerb → magyar fordítás**, a matematikai jelölés változatlan.
- **Globális dedup**; a `felmérők\` tartalma tananyagi gyűjteménybe NEM kerül.
- **Konzisztencia-elv:** a felmérők feladattípusai köszönjenek vissza a tananyagban,
  a gyűjteményben és a gyakorló tesztben — de a gyakorló teszt más paraméterekkel.
- **Token-hatékonyság:** előbb `ls`/Glob, aztán célzott olvasás; nagy PDF-ből
  `pdftotext`; amit egyszer láttál, ne olvasd újra.

## 7. Minőség / verifikáció (minden fázis végén)

> **Gépi verifikáció (2026-08-04):** `python _tools/verify_web.py [minta]` — kánon-réteg
> (s0-cím, kvízcím, doboz-ikonok, `data-hatter`, szakasz-id-k, **nyers `$` a címekben**,
> feladatkártya id/szint/`.vegeredmeny`, `data-answer` index, `.sav.henrik/bruno`,
> naplo-felismerés) + jsdom-render (KaTeX, nyers `$` a renderelt szövegben, kvíz-klikk,
> konzolhiba). A `--szoveg` / `--szoveg --kulcs-nelkul` mód a **friss szemű teszthez**
> adja ki azt, amit a diák lát. A teljes eljárás és a négy réteg: **`web-verifikacio` skill**.
> A layoutot (mobil, nyomtatás, kontraszt) egyik réteg sem látja — az böngészőből megy.

> **A 2026-08-as audit után beépült ellenőrzések.** Mind gépi, tehát nem tud visszajönni:
>
> | Szkript / ellenőrzés | Mit fog meg |
> |---|---|
> | `verify_web.py` — **eltolt kvízindex** | a `data-answer` a helyes válasz melletti gombra mutat (két esetben: fedettség-különbség ≥ +2) |
> | `verify_web.py` — **ábra `<p>`-ben** | érvénytelen HTML, a böngésző szétvágja a bekezdést |
> | `verify_web.py` — **link nélküli visszautalás** | „ahogy az előző egységben láttuk" — link nélkül |
> | `verify_web.py` — **kánon-sorrend** | az utolsó `h2` → `.gyakorolj` → outro → lapozó rendje (a 🧾 Gyorsismétlő kivétel) |
> | `verify_web.py` — **hiányzó `data-outro`** | az egység nem vezet át sehová |
> | `verify_web.py` — **nyers `<` a matek-határolókon belül** | a képlet eltűnik |
> | `sav_check.py` | a `.gyakorolj` sávcímkéi nem létező kártyára mutatnak, vagy a kártya egyetlen egységből sem elérhető |
> | `kulcs_teszt.py` + `_tools/kulcsok/*.py` | a Végeredmény-lenyíló szövege ≠ a **független Python/sympy újraszámolás** |
> | `kulcs_regresszio.py` | az öntesztet magát méri: elrontja a várt értékeket, és megnézi, elkapja-e (**érzékenységnek 100 %-nak kell lennie**) |
> | `layout_teszt.py` (2026-09-27) | mobil-túlcsordulás (360/390 px) a túllógó elemmel, JS-/konzolhiba, 404, KaTeX-hiba — Playwright + Chromium |
| `media.py --online` (2026-09-27) | törölt / beágyazásból letiltott videó, eltűnt GeoGebra-anyag |
| `quiz.js` — opciókeverés | a helyes válasz ne mindig az első gomb legyen (a helyzetfüggő opciós kvízek — „egyik sem", „mindhárom" — kimaradnak a keverésből) |
>
> **Új gyűjtemény készítésekor** a `kulcsok/` modul nem opcionális: annyi baj lett volna
> nélküle, amennyi kártya van. A modul soha ne a kulcsból vegye az értéket, hanem
> **számolja ki** (sympy-val, ha szimbolikus). Utána futtasd a `kulcs_regresszio.py`-t —
> a „0 eltérés" önmagában semmit nem bizonyít, ha az önteszt eleve vak.


- Matek: definíciók/tételek/számítások gépi ellenőrzése (sympy/Wolfram, kvíz
  `data-answer`-ek végigfuttatva).
- **Link-check:** szkript a lokális klónon — minden belső link + horgony létezik-e
  (előre-hivatkozásoknál a hiányzók listája = teendő, nem hiba).
- **Háttér-kiosztás:** `python _tools/set_hatter.py` lefuttatva (minden új oldalnak van
  `data-hatter`-e). Új háttérképnél **kontraszt-teszt**: a kép legvilágosabb pontja fölött
  a `--hatter-sotet` fátyollal a világos szöveg kontrasztja ≥ 7:1 (AAA).
- KaTeX: minden képlet renderel-e (hibás TeX = piros doboz — konzolból kiszűrhető);
  HTML-tagek kiegyensúlyozottak; print-nézet átnézve.
- Reszponzivitás: mobil nézet gyors ellenőrzése (a diákok többsége telefonon nézi).
- Állapotfájl (`_WEBOLDAL_allapot.md`) frissítve; push után az élő oldal szúrópróbája.

## 8. Feladatgyűjtemény-, gyakorló- és differenciálás-kánon (2026-07-22, felhasználói visszajelzés)

**Kerekítés.** Trigonometrikus **függvényértékek: mindig 5 tizedes** (a feladatszövegben is így
kérve, pl. „öt tizedesre"); **szögek és oldalak: 2 tizedes**.

**Részfeladatok tördelése.** A részfeladatokat NEM folytatólagosan, hanem **egymás alá** írjuk:
`<ol class="reszfeladatok"><li>…</li></ol>`. Rövid részfeladatnál (igaz/hamis, érték) egymás mellé,
tágas közökkel: `class="reszfeladatok rovid"`. A jelölés **egységesen „a)"** — a stílust a
`theme.css` adja (counter + `::before`); sem natív „a.", sem kézi jelölés.

**Feladatmennyiség és differenciálás.** Bőséges, ~**duplázott** feladatszám; a **könnyű
feladatoknál** (igaz/hamis, igazságérték) **drasztikusan több részfeladat**, mert differenciáltan
dolgozunk (gyengébb tanuló a könnyebbekkel, erősebb vegyesen — plusz otthoni gyakorlás, hogy
mindenkinek jusson elég). Szöveges/önálló feladatnál a **feladatszámot** növeljük (1 helyett ~3).

**Gyakorló feladatsorok.** Felméronként **két sáv**: (1) **🏫 Órai ismétlés** — az operatív
tervben az adott felmérőre szánt **ismétlőórák számához** méretezve (2 óra → ~dupla); (2) **🏠
Otthoni gyakorlás** — a felmérő típusához méretezve. Csak az **utolsó, még a felmérőre menő
anyagrésznél** helyezzük el (ellenőrző → a halmazoknál; dolgozat → a trigonometriánál). A gyakorló
feladatok a valós felmérővel **legfeljebb 50%-ban** egyezhetnek, és **MINDENHOVA** kerül a
`.diszklemer` „nincs garancia, hogy pontosan ennyi/ilyen feladat lesz" jelzés (szépen fogalmazva).

**Differenciált „Gyakorolj" sávok** (tananyag-oldalakon): **🐜 Henrik-bevetés** (könnyített, a
2-es/3-asig — a konkrét Alap-horgonyra mutat) és **💥 Brúnó-bevetés** (normál, a teljes tudásért — a
Középszintre). Stílus: `.savok`, `.sav.henrik`, `.sav.bruno`.
A differenciálás **két kategória**: a könnyített sáv a gyengébb tanulóknak, a normál sáv (évadonként más felirattal,
pl. 4e: ⚔️ Maximális erőbedobás) **mindenki másnak**. A normál sáv ezért mutathat közép- (és nehéz-) feladatokra
egyaránt: hogy pontosan hová, azt mindig az egységhez tartozó feladatok és azok nehézsége dönti el. Ha a normál sáv
felirata egybeesik a feladatoldal nehéz szintjének nevével, az nem ellentmondás (felhasználói döntés, 2026-09-26).

**Házi feladatok — Vészterem.** Témakörönként **EGY** házi feladatsor (nem bontjuk
kisebb egységekre, mint a rendes feladatgyűjteményeket), külön oldalon (`feladatok-hazi.html`), az
index Feladatgyűjtemény-szekciójában **kártyával**. Elvárások: **minden teljesítményszabvány-kimenetet
lefed**; a **feladatszám óraszám-arányos** (pl. 26 órás témakör ~21, 10 órás ~8 feladat); az arány kb.
**50% alap / 35% közép / 15% nehéz** (irányadó, eltérhet). Köntös: a Mutáns Osztag edzőterme, ami most a
Szvetkó-kampuszé is — rövid `.brief` felütés az elején (SZVETI). A megoldás itt — mint a többi
feladatgyűjteményben — **lenyitható végeredmény** marad (ez NEM projektfeladat: ott a megoldás privát
DOCX-be megy). Építő: `web/_tools/builders/build_dangerroom.py` + `web/_tools/builders/fgy_common.py`
(session-független útvonalakkal, a Cowork-sandboxban futtatva) — a `fgy_common.cards` helper +
témakör-paraméteres oldalburok.

**Végeredmény-tartalom (MINDEN feladatgyűjteményre, rendes és Vészterem egyaránt).** A
`.vegeredmeny` lenyíló **kizárólag a végső választ** tartalmazza — **semmilyen levezetés, indoklás
vagy közbülső lépés nincs benne**, még akkor sem, ha a feladatszöveg „indokolj"-t kér (az indoklást a
tanuló végzi; a kulcs csak a választ adja). Pl. „$25$" — nem „$18+12-5=25$"; „$A$ lovag, $B$ lókötő" —
nem a végigvezetett gondolatmenet.

**Gyors kérdések.** A `quiz.js` v2 kétféle kártyát kezel: egyszerű (`.kviz[data-answer]`, visszafelé
kompatibilis) és **változatos** (`.kviz` több `.valtozat[data-answer]`-rel): `data-mod="veletlen"` →
frissítéskor / „🎲 Másik kérdés" gombra véletlen variáns; `data-mod="lanc"` → helyes válasz után a
következő. Több gyors kérdés az anyag több pontján is elhelyezhető.

**Kreatív irány.** Modern, fiatalos, **gamifikált**, képregényes ízű köntös (szöveges feladatok,
összekötő szövegek, elnevezések, esetleg tematikus projektfeladat) — de a **matematikai precizitás,
a szakszerű átadás és a pedagógiai módszertan MINDIG elsődleges**.

**CSS-osztály-elv.** Minden újrahasznosítható stílusjegy (kártya, doboz, kvíz, sáv, részfeladat,
utility) a **`theme.css`-ben** él; a HTML-ekben csak a megfelelő `class`. **Inline `style` kerülendő**
— kivétel az adatvezérelt CSS-változó (pl. `--kartya-szin`) és az SVG-attribútumok (`font-style`
stb.). Így bármely aspektus egy helyről, minden oldalon egyszerre állítható.
