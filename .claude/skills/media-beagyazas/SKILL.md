---
name: media-beagyazas
description: >
  Oktatóvideók (elsősorban az MNT magyar nyelvű távoktatásának YouTube-órái) és GeoGebra-
  szimulációk keresése, szűrése és beágyazása a Szvetkó matek tananyag-lapjaiba a
  `_tools/media/[osztaly].json` katalógus és a `_tools/media.py` segítségével; a meglévő
  beágyazások elérhetőségének ellenőrzése. Használd, ha videót, YouTube-ot, GeoGebrát,
  appletet, szimulációt vagy más külső interaktív anyagot kell a weboldalra tenni.
---

# Külső média beágyazása (videó, GeoGebra)

A beágyazás **kattintásra töltődik** (`assets/js/beagyazas.js`): a lap megnyitásakor semmi
nem megy harmadik félhez; JS nélkül a blokk sima link a forrásra; nyomtatásban cím + rövid URL.
A blokkot **soha nem írod kézzel a HTML-be** — csak a katalógusba; a `media.py` teszi a lapra
(és a builderek újrafuttatása után vissza is teszi).

## Munkamenet egy témakörre

1. **Térkép.** A témakör tananyag-lapjainak szakaszai:
   `grep -o '<h2 id="[^"]*">[^<]*' <osztaly>/<NN-slug>/tananyag-*.html` és a doboz-azonosítók
   (`#tetel-…`, `#pelda-…`, `#def-…`). Jelöld meg, hol segítene **mozgókép** (lépésenkénti
   levezetés, más tanár magyarázata) vagy **manipulálható modell** (csúszka, húzható pont).
2. **Keresés.**
   - **MNT Távoktatás magyar nyelven** — a szerbiai magyar tannyelvű gimnáziumi tanterv
     videós órái (2020–21), a mi tantervünkhöz ez áll a legközelebb. Osztály-megfeleltetés:
     `1e → i-osztaly`, `2e → ii-osztaly`, `3e → iii-osztaly`, `4e → iv-osztaly`.
     Óra-oldal: `https://tavoktatas.mnt.org.rs/<rom>-osztaly/matematika/matematika-<rom>-osztaly-<N>-ora-<slug>`.
   - **robots.txt:** a lista- és keresőoldalak (`?class=…`, `?page=…`, `/kereses`, `/tanterv?…`)
     **tiltottak — ne kérd le és ne kerüld meg** (curl, archívum, tükör: mind tilos). Az egyedi
     óra-oldalak engedélyezettek. Felderítés: WebSearch, pl.
     `site:tavoktatas.mnt.org.rs "IV. osztály" binomiális`; az óra-oldal alján a kapcsolódó órák
     linkjein tovább lehet lépni (előző/következő óra) — de csak a témakörön belül. Új témakörhöz
     kiindulópont: a tanár profiloldala (`/tanar/<név>`, a `?page=` nélkül engedélyezett, a legutóbbi
     15 órát listázza), végső esetben a valószínű című óra-URL kipróbálása (1 kérés/s).
   - Az óra-oldalból (WebFetch) kérd ki: a YouTube `embed/<ID>` azonosítót, a tanár nevét, az óra
     számát/címét. Ellenőrzés: `https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=<ID>`
     (200 = beágyazható; a csatorna: „Távoktatas magyar nyelven”).
   - Ha teljes óralista kellene, azt a tanár a böngészőjében ki tudja másolni — kérd a PR-ben.
   - **GeoGebra:** WebSearch `geogebra.org/m <téma angolul és magyarul>`; ajánlott szerzők:
     Daniel Mentrard (`https://www.geogebra.org/u/daniel+mentrard`), a GeoGebra Team és
     tankönyvi szerzők anyagai. Adatlap: `https://api.geogebra.org/v1.0/materials/<id>?scope=extended`
     (cím, láthatóság, nyelv; `creator_id` → `/v1.0/users/<creator_id>`: a szerző neve;
     `elements[].settings.width/height`: az applet mérete). Egy **könyv** (book) nem ágyazható be
     egészben — a benne lévő tevékenység azonosítóját használd (`chapters[].pages[].id`).
3. **Szűrés — mindnek teljesülnie kell.**
   - Témában és szintben a szakaszhoz illik (ne szaladjon előre, ne legyen elemibb). A mi tantervünk
     (társadalmi szak) szűkebb az MNT-énél: pl. a be- és körülírt gömb nem tananyag, határérték csak
     4. osztályban (tanári döntés, 2026-09-28). Ha egy óra fő témája ilyen, akkor sem kerül fel, ha a
     lapon érdekességként előkerül.
   - A jelölés nem ütközik a `_docs/jelolesek.md`-vel; ha igen, a `leiras` mondja ki.
   - Videó: magyar nyelvű; beágyazható; ha hosszú, a `kezdes` a releváns résznél indítja.
   - GeoGebra: mobilon is kezelhető; kevés szöveg vagy magyar/nyelvfüggetlen; nem lövi le a
     feladatgyűjtemény megoldását. Kb. 1000 px-nél szélesebb applet 390 px-en már nehezen olvasható:
     ilyenkor legyen nagy a rajza és kevés a szövege. **Szélső helyzetben is helyes:** próbáld ki,
     mielőtt kiválasztod — húzd a háromszög egyik csúcsát át a szemközti oldalon, a kerületi szög
     csúcsát a másik ívre. Sok applet ilyenkor a szög külső oldalát méri (pl. „α + β + γ = 900°”):
     az ilyet vesd el, vagy ha nincs jobb, a `leiras` mondja meg, mire figyeljen a kadét.
   - Licenc: GeoGebra-anyag **CC BY-NC-SA 4.0** (GeoGebra ÁSZF) — a szerző neve kötelező, a
     `media.py` kiírja. YouTube: **csak beágyazás** (letöltés, újrafeltöltés, kivágás tilos).
   - Mennyiség (tanári döntés, 2026-09-27): az MNT-sorozat **minden** órája bekerül, amelynek a
     témája a lapon szerepel — az új anyagot feldolgozó óra, a folytatása („második rész”) és a
     hozzá tartozó gyakorló / megerősítő / ismétlő óra is (az óratípus az óra-oldal „Kapcsolódó
     tananyag” blokkjában látszik). A folytatás közvetlenül az előző rész után jön, a lap egészére
     vonatkozó gyakorlóóra a lap utolsó tartalmi szakaszának végére. Ha a távoktatás tanterve
     eltér a miénktől, és egy laphoz nincs óra, a lap videó nélkül marad. Szimulációból 1–2.
   - **Egy videó csak egy helyre kerül** (tanári döntés, 2026-09-28; a `media.py` hibát jelez):
     ha egy óra címe több lap témáját is lefedi, a cím fő témájának lapjára tedd (pl. „Hasáb –
     definíció, felosztás, síkmetszetek” → a hasáb lapja). Ha ez nem egyértelmű, arra a lapra, ahol
     a teljes tartalma már elhangzott, kivéve, ha ott már van videó, egy korábbi lapon pedig nincs —
     akkor oda. Ha két MNT-óra oldala ugyanazt a videót ágyazza be, csak egyszer. A legközelebbi
     órát egy videó nélküli lapra csak akkor tedd, ha témában odaillik, és máshol nem szerepel.
     Nem minden órához készült videó: ami az óra-oldalon és a YouTube-on sincs meg, azt ne keresd
     tovább.
4. **Katalógus** (`_tools/media/<osztaly>.json`, mezők: `python3 _tools/media.py --help`).
   - `azon`: `<osztaly><NN>-<rovid>`, pl. `2e04-egysegkor`.
   - `hely`: `sN` = az sN szakasz végére; `#elem-id` = az elem után (pl. `#tetel-binomialis`).
   - `leiras`: 1–2 mondat a lap hangján (tegező): **mit nézzen / mit csináljon** a kadét.
     KaTeX `\\( … \\)` mehet. Ne állíts a videóról olyat, amit nem ellenőriztél; ha csak cím és
     leírás alapján választottad, legyen óvatos, és a PR-ben jelöld („nem néztem végig”).
   - `ellenorizve`: a mai dátum. Elvetett / elhalt elem: `"allapot": "kikapcsolva"` + `megjegyzes`
     (ne töröld — így látszik, hogy már megvizsgáltuk).
   - `meret` (GeoGebra): az applet eredeti mérete, pl. `896x515` (az adatlapról; a `--online`
     szól, ha hiányzik vagy eltér). A keret ezt az arányt kapja, és a GeoGebra az **egész** appletet
     belekicsinyíti — nélküle telefonon csak az applet egy darabja látszik.
5. **Lánc.** `python3 _tools/media.py . --online` → `python3 _tools/media.py . --apply` →
   `python3 _tools/verify_web.py <osztaly>/<NN-slug>/` → `python3 _tools/layout_teszt.py <osztaly>/<NN-slug>/ --szelessegek 390`.
   GeoGebra-elemnél még: `python3 _tools/media_proba.py <osztaly>/<NN-slug>/` — 390 px-en betölti az
   appleteket, képet ment a `_layout/media/` mappába (nézd is meg!), és jelez, ha egy nem töltődött
   be. Felhőben a konténer proxyja mögött is megy: a böngésző a proxy tanúsítványát fogadja el
   pluszban, a TLS-ellenőrzés marad.
6. **PR.** A `python3 _tools/media.py . --jelentes` táblázata + elemenként egy mondat indoklás +
   „Tanárnak ellenőrizni” lista.

## Karbantartás

- `media.py --online` HIBA (törölt videó, letiltott beágyazás, privát anyag) → `kikapcsolva`,
  és keress helyette másikat.
- Több mint egy éve ellenőrzött elemre a `media.py` figyelmeztet.
