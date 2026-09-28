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
| `4e/05-kombinatorika/` | helyben készül (F3–F6), a builderei aktívan változnak | amíg ez a sor itt áll |
| `4im/` | még nem indult; új témakör csak helyben (privát források kellenek) | — |
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
| ☐ | ☐ | ☐ | ☐ |

| 1e | 2e | 3e | 4e (01–04) |
|---|---|---|---|
| ☐ | ☐ | ☐ | ☐ |

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
