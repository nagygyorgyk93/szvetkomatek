---
name: matek-abra
description: >
  **Matematikai ábrák** a Szvetkó matek oldalra, inline SVG-ként, a vizuális kánon
  szerint (sötét tinta világos „tervrajz-lapon", `role="img"` + `aria-label`, `viewBox`,
  a stílus a `theme.css`-ből). Kész generátorok: **számegyenes** (intervallumok nyílt/zárt
  végponttal, egyenlőtlenség, megoldáshalmaz), **háromszög** (feliratozott csúcsok és
  oldalak, szögjelölés, derékszög, magasság talpponttal), **Venn-diagram** (2–3 halmaz,
  a tartományt halmazművelet-kóddal adod meg: `"AB"`, `"A"`, `"-"`), valamint a már
  meglévő **függvénygrafikon** és **trigonometrikus kör**. **Használd, amikor a
  weboldalra ábra, grafikon, diagram, számegyenes, halmazábra vagy geometriai vázlat
  kell, vagy amikor egy tananyag-egységhez vizuális reprezentáció kellene** — a
  didaktika elve szerint minden új fogalom legalább két reprezentációban jelenjen meg.
  Triggerszavak: „ábra", „SVG", „grafikon", „diagram", „számegyenes", „Venn",
  „halmazábra", „háromszög", „vázlat", „egységkör", „reprezentáció", „szemléltetés".
---

<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): .claude/skills/matek-abra/SKILL.md · tükrözve: 2026-09-27 · _tools/docs_tukor.py -->

# Matematikai ábrák — inline SVG

## Miért generátor, és miért nem kép

Az ábra a weboldalon **inline SVG**, nem PNG: élesen skálázódik, a szövegkeresés
megtalálja, nyomtatásban is jó, és a `theme.css` tudja stílusozni. Kézzel rajzolt SVG
viszont hamar elcsúszik a kánonhoz képest (világos lap, sötét tinta, `aria-label`), ezért
a visszatérő ábratípusokra generátor van — a builder így azt írja le, **mit** ábrázol, nem
azt, hogy melyik köríves útvonalat kell kirajzolni.

## Hol laknak

| Generátor | Modul | Mire |
|---|---|---|
| `svg_szamegyenes` | `web/_tools/builders/abra_common.py` | intervallum, egyenlőtlenség, megoldáshalmaz, abszolút érték |
| `svg_haromszog` | `abra_common.py` | síkgeometria: oldal-/szögfeliratok, derékszög, magasság |
| `svg_venn` | `abra_common.py` | halmazműveletek 2–3 halmazon |
| `svg_fuggvenyek` | `tananyag_common.py` | függvénygrafikonok koordináta-rendszerben |
| `svg_egysegkor` | `tananyag_common.py` | trigonometrikus kör, szögek, negyedek |

A két utolsó **történelmi okból** a `tananyag_common.py`-ban van (40 oldal használja) —
nem költöztettem át, hogy a meglévő builderek ne törjenek el. Mindkét modul ugyanazt a
kánont követi.

## Használat

```python
from abra_common import svg_szamegyenes, svg_haromszog, svg_venn
from tananyag_common import abra, svg_fuggvenyek, svg_egysegkor

# 1) megoldáshalmaz: −1 ≤ x < 3, és külön egy félegyenes
ki.append(abra(svg_szamegyenes(
    xr=(-4, 5),
    intervallumok=[(-1, 3, "zart", "nyilt"),
                   (3.5, 5, "nyilt", "nyil", "#ef4444")],
    pontok=[(-2, "−2", "#8b5cf6")]),
    "A megoldáshalmaz a számegyenesen"))

# 2) háromszög magassággal és két szögjelöléssel
ki.append(abra(svg_haromszog(csucsok=[(0,0), (4,0), (1.2,2.6)],
                             cimkek=("A","B","C"), oldalcimkek=("c","a","b"),
                             szogek=(0,1), magassag=2),
               "A C csúcsból húzott magasság"))

# 3) halmazművelet — a KÓD mondja meg, mit ábrázolunk
svg_venn(("A","B"), arnyekolt=("AB",))                 # metszet
svg_venn(("A","B"), arnyekolt=("A","B","AB"))          # unió
svg_venn(("A","B"), arnyekolt=("A",))                  # A ∖ B
svg_venn(("A","B"), arnyekolt=("-",))                  # komplementer
svg_venn(("A","B","C"), arnyekolt=("A","B","C"))       # csak-egyikben
svg_venn(("A","B","C"), arnyekolt=("AB",))             # A ∩ B, de nem C
```

A Venn-kód azt sorolja fel, **mely halmazokban van benne** a tartomány; a `-` az
alaphalmaz maradéka. Így a builderben olvasható, hogy melyik halmazműveletet mutatjuk.

## Kánon, amit be kell tartani

- **Sötét tinta, világos lap.** Az oldal sötét témájú, de az ábra „tervrajz-lapja"
  világos (`.svgcard`, `.venn .vbox`, `.svgwrap>svg`). Új SVG-t is így tervezz —
  világos háttéren sötét vonallal.
- **`role="img"` + `aria-label`** minden ábrán (a generátorok adják).
- **`viewBox`**, hogy mobilon is skálázódjon; fix `width`/`height` csak alapméretként.
- **Színek a design-rendszerből:** definíció-zöld `#047857`, tétel-kék `#3b82f6`,
  példa-borostyán `#f59e0b`, csapda-piros `#ef4444`, érdekesség-lila `#8b5cf6`;
  tinta `#0f172a`, halvány rács `#cbd5e1`.
- **Tipográfiai mínusz** (`−`, U+2212) a feliratokban, nem ASCII kötőjel.
- Az ábrát a `tananyag_common.abra(svg, felirat)` csomagolja `.svgcard`-ba képaláírással.

## Ha új ábratípus kell

1. Nézd meg, nem oldható-e meg a meglévő ötből (pl. sok geometriai vázlat
   `svg_haromszog`-gal + `extra` nyers SVG-vel).
2. Ha új generátor kell, az `abra_common.py`-ba írd, ugyanazzal a mintával:
   `_fej()` a fejléc, matematikai koordináták → képernyő-koordináta függvény, a színek a
   modul konstansaiból.
3. **Nézd meg a kimenetet.** Az SVG jól formált XML-sége nem jelenti, hogy jól is
   néz ki — a Venn-diagram árnyékolása két különböző hibás megoldáson ment át, amíg
   ránézésre ki nem derült, hogy nem azt a tartományt takarja, amit kell:

```bash
python3 -c "
import cairosvg, sys; sys.path.insert(0,'web/_tools/builders')
from abra_common import svg_venn
cairosvg.svg2png(bytestring=svg_venn(('A','B','C'), arnyekolt=('A','B','C')).encode(),
                 write_to='/tmp/abra.png', scale=2)"
```

majd a PNG-t **Read-del nyisd meg és nézd meg**. (Telepítés, ha kell:
`pip install cairosvg --break-system-packages`.)

4. **Egy körnél az even-odd kilyukasztás helyes, kettőnél nem** — két átfedő kör
   even-odd punchánál a metszetük visszatöltődik. Több halmaz kizárásához **halmazonként
   külön clipPath-ot** ágyazz egymásba (így működik a `svg_venn`). Maszkkal is
   megoldható lenne, de a renderelők egy része nem alkalmazza `clip-path` alatti
   csoportra.

## Kapcsolódó

- **`tananyag-narrativa`** — a narratíva-terv „Ábra" mezője mondja meg, milyen ábra kell
  egy egységhez, és hogy elég-e a meglévő generátor.
- **`didaktika`** 7. pont — minden új fogalom legalább két reprezentációban, és legyen
  legalább egy reprezentáció-váltó kérés.
- **`web-verifikacio`** — a generált oldal ellenőrzése (az SVG jól formáltságát is nézi).
- **`_WEBOLDAL_workflow.md`** 4c. — a vizuális réteg teljes kánonja.
