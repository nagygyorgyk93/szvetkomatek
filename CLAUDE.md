# Szvetkó matek — útmutató Claude-nak (felhős és helyi munkához)

Ez a repó a **Szvetkó matek** oktatási weboldal: középiskolai matematika-tananyagok,
feladatgyűjtemények és összefoglalók gamifikált köntösben (Hősök Ligája Akadémiája,
Szvetkó-kampusz), osztályonként (`1e`, `2e`, `3e`, `4e`) és témakörönként.
GitHub Pages, **publikus**. A `main` minden pusha automatikusan élesít (`.github/workflows/pages.yml`).

**Nyelv:** magyar — válasz, PR-leírás, kódkomment. Commit-üzenet magyarul, **ékezet nélkül**.

## Abszolút szabályok

1. **A repó publikus.** Nem kerülhet bele: felmérő- vagy dolgozat-adat (feladatszöveg, szám,
   paraméter — a builderek forráskódjában sem), tanulói adat, a tanár privát munkafájljai,
   megoldókulcs-DOCX. A felmérő-ütközés tiltott-listái a repón kívül élnek; a
   `_tools/builders/tiltott.py` tölti be őket, felhőben nincsenek meg → a builder figyelmeztet
   és ellenőrzés nélkül fut. Ez rendben van **meglévő** tartalom újraépítéséhez; **új feladatot,
   új számadatot felhőben ne találj ki** (a felmérő-ütközést nem tudod kizárni) — javasold a PR-ben.
2. **Soha ne a `main`-re dolgozz, és ne pusholj oda.** Felhőben: saját ág + PR; a tanár olvassa át és merge-eli.
3. **Builder-generált HTML-t kézzel ne szerkessz.** A 2e–4e tananyag- és feladatlapjai
   jellemzően a `_tools/builders/build_*.py` kimenetei (keress rá a témakör-mappa nevére és a
   fájlnévre); ilyenkor a buildert javítsd, futtasd újra, majd a teljes láncot (lent). Az 1e lapjai
   többnyire kézzel migráltak — azokat közvetlenül lehet javítani. Kivétel mindenhol: amit a
   `kepek.py` (karakterképek), a `media.py` (videó/GeoGebra) és a `set_hatter.py` (háttér) ír —
   azt csak a saját eszköze kezelheti.
4. **Matematikai precizitás nem alku tárgya.** Jelölés: `_docs/jelolesek.md` (kötelező).
   Minden számítást gépileg ellenőrizz (sympy), a feladatkulcsokat a `_tools/kulcsok/` modulok.
5. **A feladat-horgonyok véglegesek** (`#alap-3`, `#kozep-5` …): nem számozódnak át, új elem a sor végére.
6. **Tükrözött fájlok — ne szerkeszd:** `_docs/workflow.md`, `_docs/jelolesek.md`,
   `_docs/tortenet/*`, `.claude/skills/web-verifikacio/`, `.claude/skills/matek-abra/`.
   A forrásuk a tanár gépén van (`_tools/docs_tukor.py` frissíti). Ha javítanád, írd a PR-leírásba.

## Hol mi van

| Mit | Hol |
|---|---|
| Teljes workflow, oldal-anatómia, vizuális kánon, verifikáció | `_docs/workflow.md` (4b–4d, 7–8. pont) |
| Jelölés-kánon | `_docs/jelolesek.md` |
| Köntös / világ-biblia, évadonkénti szereplők és szótár | `_docs/tortenet/tortenet.md` + `tortenet_<osztaly>.md` |
| Felhős feladatlista (backlog), zárolt területek | **`_docs/FELHO_FELADATOK.md`** |
| Közös CSS / JS | `assets/css/theme.css`, `print.css`; `assets/js/` (`ui.js` tölti be a `naplo.js`, `effekt.js`, `beagyazas.js` modult) |
| Interaktív ábrák | `assets/js/interaktiv.js` (módok: szelo, erinto, sereg, osszeg, pascal, **szimulacio**, **adatlabor**) + `tananyag_common.svg_interaktiv/svg_pascal`, `abra_stat.svg_szimulacio/svg_adatlabor` |
| Builderek és közös részeik | `_tools/builders/` (`tananyag_common.py`, `fgy_common.py`, `abra_common.py`, `abra_stat.py` — statisztikai ábrák és mutatók; valós adatok: `adat_<osztaly>_<NN>.py`) |
| Külső média katalógusa | `_tools/media/<osztaly>.json` → `_tools/media.py` (skill: `media-beagyazas`) |
| Kulcs-öntesztek | `_tools/kulcsok/*.py` → `kulcs_teszt.py`, `kulcs_regresszio.py` |

## Eszközlánc (a repó gyökeréből)

```bash
python3 _tools/builders/build_<...>.py          # ha builderes lapot módosítottál
python3 _tools/egyedi_id.py                      # csak a régi 1e-builderek után (build_fgy_geometria,
                                                 #   _linearis, _racionalis, build_dangerroom): ismétlődő SVG-id-k
python3 _tools/kepek.py . --apply                # karakterképek a .brief dobozokba
python3 _tools/media.py . --apply                # videó / GeoGebra blokkok a katalógusból
python3 _tools/set_hatter.py                     # helyszín-hátterek
python3 _tools/verify_web.py [minta]             # kánon + jsdom-render (0 hiba kell)
python3 _tools/check_links.py                    # belső linkek + horgonyok
python3 _tools/sav_check.py                      # Gyakorolj!-sávok ↔ feladatkártyák
python3 _tools/kulcs_teszt.py                    # ha feladat/végeredmény változott (+ kulcs_regresszio.py)
python3 _tools/layout_teszt.py [minta]           # böngésző-réteg: mobil-túlcsordulás, konzol, KaTeX
```

Témakör zárásakor még: `build_naplo_terkep.py` (JELVENY) + `build_search_index.py`.
A web-verifikáció rétegei és a „friss szemű” (kontextus nélküli subagent) teszt:
`.claude/skills/web-verifikacio/SKILL.md`. Ábrák: `.claude/skills/matek-abra/SKILL.md`.

## Felhős munkamenet (Claude Code on the web)

- A `.claude/settings.json` SessionStart-hookja futtatja a `_tools/felho_setup.sh`-t
  (sympy, mpmath, jsdom → `/tmp/vw`, playwright). Helyi gépen nem fut.
- **Ami felhőben NINCS meg:** a tiltott-listák, a felmérők és kulcsaik, a forrás-tankönyvek
  (PDF), a narratíva-tervek és az állapotfájl, a nagy felbontású eredeti médiák. Ezért
  **új témakör (F0–F6 pipeline) felhőben nem indítható** — az a tanár gépén megy. Felhőben:
  a `_docs/FELHO_FELADATOK.md` feladatai (média, audit, interaktív ábrák, QOL).
- **Egy PR = egy osztály × egy feladattípus** (könnyen átnézhető). A PR-leírásba: mit
  változtattál és hol; a lánc kimenete (verify_web, check_links, layout_teszt); mit **nem**
  tudtál ellenőrizni; és egy „Tanári döntés kell” lista.
- A munka végén frissítsd a `_docs/FELHO_FELADATOK.md` státusztábláját ugyanabban a PR-ben.
- Webes források: tartsd tiszteletben a robots.txt-t (a tavoktatas.mnt.org.rs listaoldalai
  tiltottak — részletek a `media-beagyazas` skillben). Ha egy lap nem kérhető le, ne kerüld meg.
- Kész tartalomhoz szöveget a köntös hangján írj (tegező, rövid, a mentor/SZVETI szólal meg),
  de a matematikai rész mindig pontos, szakszerű.
