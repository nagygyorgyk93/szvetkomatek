# Q3 — A legutóbbi tanulási oldal folytatása

## Állapot — 2026-10-09

**Helyben elkészült és ellenőrizve.** A változtatás a `main` ágon készült,
új ág és push nélkül. Kiindulás: `b85ce6e`, tiszta munkafa; a `main` és az
`origin/main` helyi referenciája azonos volt. Távoli frissítés nem történt. Munka közben az aktuális mainre bekerült a
`40b007c` adatvédelmi hook-commit; a Q3 fájljait nem érinti. Az új ellenőrzést
átolvastuk, a helyi Q3-mentés ezt a commitot követi.

## Mit kap a tanuló?

| Hol? | Hová vezet a folytatás? |
|---|---|
| Főoldal | A legutóbb megnyitott tanulási oldalra, osztálytól függetlenül. |
| 1e, 2e, 3e és 4e nyitóoldala | Az adott osztály legutóbb megnyitott tanulási oldalára. |

- A tananyag, feladatgyűjtemény, házi, összefoglaló és terepküldetés is megjegyezhető.
- Az indexek, a kereső és a küldetésnapló nem írják felül a tanulási előzményt.
- A kártyán **„Legutóbb megnyitott oldal”**, a konkrét cím, az osztály és az oldaltípus,
  valamint **„Folytatás →”** szerepel. A teljes kártya hivatkozás, billentyűzettel is elérhető.
- Előzmény nélkül nincs üres kártya. Hibás, idegen vagy a címjegyzékből törölt célhoz nincs hivatkozás.
- Másik böngészőfülből érkező változáskor frissül; a rajta lévő billentyűzetfókusz megmarad.
  A böngésző vissza gombjával, gyorsítótárból visszatérő lapot is megjegyzi.
- A **Napló törlése** a folytatási előzményt is törli. A kártya nyomtatásban rejtett.

Az előzmény ebben a böngészőben marad. A folytatás az oldal elejére vezet;
nem ment görgetési helyet vagy feladaton belüli állapotot. A naplókód továbbra is
a teljesítéseket és beállításokat viszi át, a helyi látogatási előzményt nem.

## Mi változott?

| Fájl | Módosítás |
|---|---|
| `assets/js/naplo.js` | Külön helyi folytatási tároló, osztályonkénti cél, a meglévő címjegyzékből ellenőrzött hivatkozás, törlés/frissítés/visszalépés. |
| `assets/css/theme.css` | Közös sötét kártya, tördelődő cím, látható fókusz és megfelelő érintési felület. |
| `assets/css/print.css` | A navigációs kártya elrejtése nyomtatásban. |

A pontozás adatszerkezete változatlan. A meglévő naplótérképet használjuk:
279 tanulási cél szerepel benne, új címjegyzék és új külső függőség nem kellett.
A kártya és a haladásgyűrűk együtt is csak egyszer kérik le a térképet.

Javítva a korábbi gyökérútvonal-felismerés is: a mappacímként megnyitott főoldalon
és osztályoldalon a haladásgyűrűk helyesek a GitHub Pages projekt-előtaggal is.
A két, változót tartalmazó cím szöveges megnevezéssel jelenik meg az indexeken.

## Ellenőrzés

| Próba | Eredmény |
|---|---|
| Kánon és belső hivatkozások | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalás-figyelmeztetés megmaradt. |
| Képletrender és kvízek | 310 oldal, 28319 képlet, 335 sikeres kvízpróba; képlet- és kvízhiba nincs. |
| Böngészőben végzett működéspróbák | 122 sikeres ellenőrzés: osztályok, oldaltípusok, navigáció, újratöltés, hibás/letiltott tároló, törlés, naplókód és változatlan pontozás. |
| Végleges címke, fókusz és visszalépés | 16 sikeres célzott ellenőrzés; két tényleges gyorsítótári visszatérés megfigyelve, projekt-előtaggal is. |
| Főoldali videó, kereső és házi | 7 sikeres valódi böngészőpróba. |
| Mobil és asztal | Főoldal + négy osztályoldal, 360/390/1280 px: 15 nézet, 0 túlcsordulás. |
| Automatikus akadálymentesség | 15 axe-futtatás, 0 jelzés; Tab-fókusz és legalább 44 px-es érintési felület. |
| Nyomtatás és JS nélkül | 15 nyomtatási nézetben rejtett kártya és látható tartalom; mind az öt nyitóoldal JS nélkül olvasható. |
| Szövegkontraszt | Böngészőből kiolvasott színek: legalább 10,53:1; az új kártya minden szövege teljesíti a 7:1 küszöböt. |
| Friss szemű szöveglektor | Projektkontextus nélkül ellenőrizte; a görgetési helyet sugalló címke pontosítva, végleges szöveg jóváhagyva. |
| Megőrzés | Mind a 310 HTML, a naplótérkép és a keresőindex byte szerint változatlan; zárolt backlog-rész és tükrök megmaradtak. |

**A jsdom két környezeti korlátját külön kezeltük:** a főoldali videó `play()`
művelete nincs megvalósítva benne; a keresőnek szükséges `fetch` sincs jelen.
A teljes futás nyers jelentése ezt a két jelzést tartalmazza. Valódi Edge-ben a videó
lejátszása/szüneteltetése/folytatása, a kereső adatbetöltése, találata és navigációja
hibátlan. Ezeket nem számítjuk a honlap hibájának, és a két jelzést nem hallgatjuk el.

A böngészőmérés Node Playwrighttal és a gépen lévő Edge-dzsel készült;
a túlcsordulás kifejezése a projekt `layout_teszt.py` eszközéből változtatás nélkül származik.
A változás nem érint buildert, HTML-t, feladatot vagy számadatot: újraépítés,
médiavisszaillesztés és új matematikai kulcs/regressziófuttatás nem volt szükséges.
A meglévő teljesítési gomb, kvízpont, feladatpipa és projektpont működését közvetlenül próbáltuk.

## Korlátok és tanári döntés

- Élő publikált oldal, más böngésző, valódi telefon és képernyőolvasó nem volt újra ellenőrizve.
- Az axe eredménye nem teljes WCAG-minősítés. A külső videók/GeoGebra-felületek nem részei ennek az adagnak.
- Letiltott tároló esetén az előzmény nem marad meg, de az oldal tovább használható.

**Tanári döntés kell:** nincs nyitott kérdés a Q3-hoz.
Következő javasolt nagyobb tétel: Q4, mobil tartalomjegyzék; indítás előtt választás.
