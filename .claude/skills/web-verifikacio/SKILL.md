---
name: web-verifikacio
description: >
  A **Szvetkó matek** weboldal kimenetének ellenőrzése négy rétegben, mielőtt a diák elé
  kerül: (1) belső linkek és horgonyok — `check_links.py`; (2) **kánon + render** —
  `verify_web.py`: s0-cím, „🎯 Gyors kérdés", doboz-ikonok, `data-hatter`, szakasz-id-k,
  **nyers `$` a címekben**, feladatkártyák id/szint/végeredmény hármasa, `data-answer`
  index-érvényesség, majd jsdom-mal KaTeX-render, kvíz-klikk, konzolhiba; (3) **friss
  szemű teszt** — kontextus nélküli agent olvassa el vagy oldja meg az oldalt, és
  jelezze, hol kellett találgatnia; (4) böngésző-réteg (mobil-túlcsordulás, nyomtatás,
  kontraszt). **Használd MINDIG, amikor a weboldalra oldal készül vagy módosul, témakört
  zárunk (F5), builder újrafut, vagy push előtt állunk** — a verifikáció az, ami sürgős
  helyzetben kimarad, és épp akkor kellene. Triggerszavak: „verifikáció", „ellenőrzés",
  „check_links", „verify_web", „KaTeX", „link-check", „push", „F5", „publikálás",
  „friss szemű", „lektorálás", „weboldal", „szvetkomatek".
---

<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): .claude/skills/web-verifikacio/SKILL.md · tükrözve: 2026-09-27 · _tools/docs_tukor.py -->

# Webes kimenet verifikációja

Négy réteg, növekvő költséggel. A cél nem az, hogy mindig mind a négy lefusson, hanem
hogy tudd, melyik mit fog meg — és hogy a legdrágább hibafajta (a **félreérthető
szöveg**) ne csak reményből legyen kizárva.

Minden szkript a repo gyökeréből fut (`Claude\web\`).

---

## 1. réteg — linkek és horgonyok

```bash
python _tools/check_links.py
```

Minden belső `href`/`src`-t és `#horgonyt` ellenőriz. Előre-hivatkozásnál (a tananyag már
a még el nem készült feladatgyűjteményre mutat) a hiányzók listája **teendő, nem hiba**.

## 2. réteg — kánon + render

```bash
python _tools/verify_web.py                        # minden oldal (~40 s)
python _tools/verify_web.py 2e/04-*/               # egy témakör (gyors)
python _tools/verify_web.py --csak-kanon           # jsdom-réteg nélkül
python _tools/verify_web.py --json                 # gépi kimenet
```

**Kánon-rész** (pure Python, mindig fut) — a 4b/4c kánon és a világ-biblia 5a. FIX
szerkezete: `s0` = „📡 Küldetés-eligazítás", kvízcím „🎯 Gyors kérdés", a doboz-ikonok
típushoz kötése (📗📘✏️⚠️💡), `data-tagozat`/`data-hatter`, a `h2` id-k folytonossága,
kézi számozás és emoji tilalma tananyag-címben, **nyers `$` a címekben** (ha a `mat()`
kimaradt, a diák dollárjeleket lát), feladatkártyák id-egyediség / szint-osztály /
`.vegeredmeny` hármasa, `data-answer` **index**-érvényesség, `.sav.henrik` + `.sav.bruno`,
és hogy a `naplo.js` fájlnév-mintái felismerik-e az oldalt (különben nem ad XP-t).

**Render-rész** (`verify_jsdom.mjs`) — lefuttatja az oldal saját JS-ét: KaTeX renderel-e
hibátlanul, marad-e nyers `$` a **renderelt** szövegben (a TOC-ban is!), reagálnak-e a
kvízgombok a `data-answer` indexre, van-e konzolhiba.

Ha a render kimarad, a szkript kiírja, miért. jsdom telepítése:
`npm install jsdom --prefix /tmp/vw` (a szkript a `JSDOM_DIR`, `/tmp/vw/node_modules`,
`_tools/node_modules` helyeken keresi).

**A `set_hatter.py` NEM része ennek** — azt minden új oldal után külön kell futtatni,
különben a `verify_web.py` hiányzó `data-hatter`-t jelez. Ugyanígy a builder újrafuttatása
**törli a külső média-blokkokat** (videó, GeoGebra) — azokat a `media.py` teszi vissza a
katalógusból. A builder utáni sorrend:

```bash
python _tools/kepek.py . --apply
python _tools/media.py . --apply        # _tools/media/*.json → figure.media blokkok
python _tools/set_hatter.py
```

## 3. réteg — friss szemű teszt

Ez a réteg olyat fog meg, amit a másik három nem tud: **a szöveg félreérthetőségét.**

A sympy-assertek azt igazolják, hogy *a szerző által gondolt* matematika helyes. A friss
szemű teszt azt vizsgálja, hogy *amit a lapon leírtunk*, az ugyanazt jelenti-e. A kettő
pontosan a többértelműségnél válik el — és ez a legdrágább hibafajta, mert egy
feladatgyűjteményben vagy felmérőn egyszerre harminc tanulót érint.

### Az eljárás

Szedd ki azt, amit a diák lát, és add oda egy **kontextus nélküli** agentnek:

```bash
# tananyag-egység szövege
python _tools/verify_web.py --szoveg 2e/04-*/tananyag-visszavezetes.html

# feladatlap végeredmények NÉLKÜL (a kulcsok a kimenet végén, külön — azokat NE add át)
python _tools/verify_web.py --szoveg --kulcs-nelkul 2e/04-*/feladatok-trigonometrikus-kor.html
```

Aztán indíts egy subagentet, **projektkontextus nélkül** — se köntös, se workflow, se
tanterv. Ez nem formalitás: ha az agent ismeri a hátteret, kitölti a hiányokat abból,
ami a diáknak nincs meg, és pont a keresett hibát nézi el.

**Tananyag-mód — a prompt kb. így:**

```
Alább egy középiskolai matematika tananyag szövege. Nem ismered a tárgyat előzőleg,
és nincs más forrásod. Három dolgot kérek:
1. Foglald össze 5-6 pontban, mit tanultál meg belőle.
2. Sorold fel MINDEN pontot, ahol találgatnod kellett: nem definiált fogalom,
   hivatkozás olyanra, ami nincs a lapon, kihagyott lépés, kétértelmű megfogalmazás.
3. Válaszolj a lapon szereplő „🎯 Gyors kérdés" kérdéseire — kizárólag a lap alapján.
Ne legyél jóindulatú: ha valamit ki kellett találnod, azt írd le hibaként, ne told el
azzal, hogy „valószínűleg azt jelenti".
```

Amit a válaszból ki kell olvasni: ha a 3. pontban **nem tudja megválaszolni a lap saját
kvízét**, akkor a lap nem tanítja azt, amit kérdez. Ez a legerősebb jelzés.

**Feladat-mód — a prompt kb. így:**

```
Alább matematikai feladatok szövege, megoldások nélkül. Oldd meg őket, és minden
feladatnál jelezd, ha a szöveg többféleképpen értelmezhető, vagy ha hiányzik hozzá
adat/feltétel. Ha egy feladatot kétféleképpen is meg lehet oldani más eredménnyel,
írd le mindkettőt.
```

Ezután **vesd össze a végeredményekkel**. Eltérés két dolgot jelenthet: hibás kulcs, vagy
félreérthető feladatszöveg — mindkettő javítandó, és a második a gyakoribb.

### Mennyit fusson

Minden oldalra nem érdemes. Egy témakör zárásakor **egy tananyag-egység** (a
legsűrűbb/legnehezebb) és **egy feladatgyűjtemény** elég ahhoz, hogy a rendszerszintű
gondok kiderüljenek — mert a builderek miatt a hibák jellemzően nem egyediek, hanem
mintázatosak.

## 4. réteg — böngésző

Amit **egyik automata réteg sem lát**, mert nincs layout-számítás:

- **mobil-túlcsordulás** (a diákok többsége telefonon nézi) — 390 px szélességen ne
  legyen vízszintes gördítés; a hosszú képletek és a táblázatok a `.tblwrap`-ben;
- **nyomtatási nézet** — a sötét téma miatt a `print.css` teljes világos visszaállítást
  végez; új komponensnél ezt ellenőrizni kell;
- **kontraszt** — új háttérképnél a világos szöveg a kép legvilágosabb pontján is
  WCAG AAA (≥7:1);
- **valódi konzol és a `naplo.js` injektálása** — megjelenik-e a fejléc-chip, az
  „✅ Egység teljesítve" gomb, a „megoldva" pipa a feladatkártyákon.

**Gépi rész (2026-09-27 óta):** `python _tools/layout_teszt.py [minta]` — Playwright + fej
nélküli Chromium, 360/390/1280 px: vízszintes túlcsordulás a túllógó elemekkel (ami saját
gördíthető dobozban lóg ki, pl. `.tblwrap`, `.katex-display`, az nem hiba), JS-kivétel,
konzolhiba, hiányzó fájl (404), KaTeX-hiba; `--kepek` képernyőképet ment a `_layout/`-ba
(gitignore), `--nyomtatas` a nyomtatási nézetét is. Ahol fut: a felhős Claude Code-munkamenet
(a SessionStart-hook telepíti a playwrightot), és minden környezet, ahol van Chromium.
A kontrasztot és a naplo.js-injektálás látványát ez sem ítéli meg — azt képernyőképről vagy
a **Claude in Chrome** eszközökkel nézd. Ha egyik sincs, **mondd meg, hogy ez a réteg
kimaradt** — ne úgy zárd a témakört, mintha megnézted volna.

---

## Mikor melyik réteg

| Helyzet | Rétegek |
|---|---|
| Egy oldal elkészült / builder újrafutott | `set_hatter.py` → 2. réteg az adott témakörre |
| Témakör zárása (F5) | 1. + 2. réteg mindenre, 3. réteg egy tananyagra és egy feladatgyűjteményre |
| Push előtt | 1. + 2. réteg (gyorsan, `--csak-kanon` is elég, ha nem volt tartalmi változás) |
| Új komponens, design- vagy háttérkép-változás | 4. réteg is (`layout_teszt.py`, képekkel) |
| Külső média (videó, GeoGebra) került a lapra | `media.py --online` + 2. réteg + `layout_teszt.py --szelessegek 390` |
| Régi builder újrafuttatása után | ⚠️ `data-hatter` letörölhet → `set_hatter.py`, majd 2. réteg |

---

## Ismert csapdák

- **A builder felülírja a HTML-t.** Kézi HTML-javítás után a buildert is javítani kell,
  különben a következő futás visszaírja a hibát. A `verify_web.py` jelzése a **builderre**
  is szól, nem csak a fájlra.
- **Régi builder újrafuttatása letörli a `data-hatter`-t** (azt a `set_hatter.py` írja ki
  utólag). Az F5-ben úgyis lefut, de közben zajt okoz.
- **A jsdom nem ismer `IntersectionObserver`-t** (az `effekt.js` használja) — a
  `verify_jsdom.mjs` stubolja, ezért ez nem jelzés. Ha új böngésző-API-t vezetsz be, azt
  is stubolni kell, különben minden oldalra hamis konzolhibát kapsz.
- **A `data-answer` INDEX, nem szöveg** (0-alapú, a `quiz.js` így értelmezi). Ez az egyik
  legkönnyebben elrontható dolog, és a 2. réteg statikusan is ellenőrzi.
- **Zajos ellenőrzőt nem olvas senki.** Ha egy jelzés rendszeresen hamis pozitív (pl. a
  `terepkuldetes.html` kártyáin szándékosan nincs `.vegeredmeny`, mert a megoldás privát
  DOCX-ben van), akkor a szkriptet kell kivételre tanítani, nem a jelzést megszokni.

## Kapcsolódó

- **`_WEBOLDAL_workflow.md`** 7. pont (Minőség / verifikáció) és 4b/4c kánon.
- **`_WEBOLDAL_prompt_sablon.md`** 5. pont — a fázisonkénti verifikáció.
- **`tananyag-narrativa`** — a tervezési oldal; ez a skill a kimeneti oldal.
- **`_WEBOLDAL_allapot.md`** — a talált, de még nem javított hibák ide kerülnek teendőként.
