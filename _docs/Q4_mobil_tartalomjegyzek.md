# Q4 — Mobil tartalomjegyzék

## Állapot — 2026-10-09

**Helyben elkészült és ellenőrizve.** Kiindulás `269ae63`, tiszta `main`,
az `origin/main` helyi referenciájával azonos. Távoli frissítés nem történt.
Új ág és push nélkül; a publikált oldal külön ellenőrzése nem része ennek az adagnak.

## Mit kap a tanuló?

959 px-ig a bal alsó **Tartalom** gomb megnyitja az oldal tartalomjegyzékét.
A 279 tanulási oldal meglévő 1306 szakaszcímét és alcímét használja;
a címre kattintva az adott részhez ugrik. Asztalon a meglévő oldalsó lista marad.

- A hosszú lista külön gördül, a **Bezárás** gomb elérhető marad.
- Billentyűzettel is kezelhető; Escape vagy a sötét háttérre kattintás bezárja.
- A fókusz bezáráskor a Tartalom gombra, szakaszválasztáskor a célcímre kerül.
- Újranyitáskor a listában kijelölt rész kap fókuszt. Nyitott menü mellett
  az alapoldal és a kereső gyorsbillentyűje nem szakítja meg a választást.
- A Tartalom gomb és a jobb alsó, a lap tetejére ugró gomb külön helyen van.
  A lap végén a lábléc a gomb fölött marad olvasható.
- Nyomtatás előtt a lista bezárul; a gomb és az ablak nem kerül papírra.
- JavaScript vagy a natív párbeszédablak támogatása nélkül a tartalom olvasható,
  hibás vezérlő nem jelenik meg.

## Feltárt hibák és javításuk

| Hol? | Hiba vagy hiány | Súlyosság | Javítás módja |
|---|---|---|---|
| Közös mobilos felület | A keskeny kijelzőn elrejtett oldalsó tartalomjegyzéknek nem volt megfelelője. | közepes | Közös JavaScript és CSS: lebegő gomb, natív párbeszédablak. |
| Új menü szakaszra ugrása | A billentyűzetfókuszt a választott címsorra kell vinni. | közepes | Közös JavaScript: címfókusz, bezárás és fókusz-visszaadás. |
| Új menü, billentyűzet | A lista elején a natív Shift+Tab a böngésző kezelősávjára vitte a fókuszt. | alacsony | Tab/Shift+Tab körbejárás a két végén. |
| Közös tartalomjegyzék, 20 képletes cím | A sima szövegmásolás a KaTeX több rétegét összefűzte, a képletet többször és nyers jelöléssel írta ki. | alacsony | A megjelenített képlet másolása, egyértelmű matematikai felolvasási név; a névelő igazítása. |
| Ékezetes szakaszcímek | A címazonosító és az URL-kódolt horgony összevetése miatt elmaradt az aktív rész jelölése. | alacsony | A hivatkozás eredeti horgonyának összevetése; asztali és mobilos ellenpróba. |

Csak `assets/js/ui.js`, `assets/css/theme.css` és `assets/css/print.css`
funkcionális változása készült. Közös stílus, oldalankénti kivétel és új függőség nélkül.
Az eredeti szakaszhorgonyok megmaradtak.

## Ellenőrzés

| Próba | Eredmény |
|---|---|
| Kánon és belső linkek | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalás-figyelmeztetés megmaradt. |
| Teljes oldalkészlet valódi Edge-ben, 390 px | 310 oldal, 0 túlcsordulás/KaTeX/JS/saját konzol/helyi 404 hiba; 279 menü teljes címjegyzéke és utolsó szakaszra ugrása sikeres. |
| Célzott mobil/asztali nézet | Négy mintalap 360/390/1280 px-en, zárt/nyitott állapot: 20 nézet, 0 hiba. További hat szemrevételezett nézet, 0 túlcsordulás. |
| Automatikus akadálymentesség | 20 axe-futtatás, 0 jelzés. |
| Kezelés és szélső helyzetek | 78 fő és 15 célzott sikeres próba: látható fókusz, fókuszcsapda, ≥44 px linkek, Escape/bezárógomb/háttér, háttérgörgetés, rakéta/lábléc, 390×320 px, 959/960 px, átméretezés, projekt-előtag és visszalépés. |
| Nyomtatási nézet | 12/12: a tartalom látható, a menü és a gomb rejtett; a nyitott menü bezárul. |
| Képletrender és kvízek | 29 kiválasztott oldal, 3058 képlet és 38 kvízpróba, 0 hiba. Minden képletes szakaszcímet tartalmazó oldal szerepel a mintában. |
| Képletes címek végleges próbája | 15 oldal, 20 cím, 23 képlet, 31 sikeres név- és elrendezéspróba. |
| Szövegkontraszt | Böngészőből kiolvasott új menüszínek: minimum 9,457:1; minden vizsgált szövegpár ≥7:1. |
| JS nélkül és párbeszédablak-támogatás nélkül | Mindkét esetben olvasható tananyag, hibás gomb nélkül. |
| Friss szemű felületszöveg-lektor | Projektkontextus nélkül, csak a tanulói címkékkel; érthetőségi/nyelvi hiba nélkül. |
| Megőrzés | 310 HTML, naplókód, naplótérkép és keresőindex byte szerint azonos. A backlog zárolt első 23 sora és a tükrök megmaradtak. |

A böngészőmérés Node Playwrighttal és a gépen lévő Edge-dzsel készült;
a túlcsordulásvizsgálat a projekt `layout_teszt.py` aktuális kifejezését használja.
A tartalom nem változott: builder-újrafuttatás, média-visszaillesztés,
indexújraépítés és új matematikai kulcs/regressziós futás nem volt szükséges.

## Korlátok és tanári döntés

- Valódi telefon, más böngésző, képernyőolvasó és élő publikált oldal nem volt ellenőrizve.
- Az axe nem teljes WCAG-minősítés; a nyomtatási próba láthatóságot ellenőrzött,
  teljes PDF-oldaltördelést nem. A külső videók és appletek nem részei ennek az adagnak.
- A képletek felolvasási neve kód szerint ellenőrizve; tényleges képernyőolvasós próba még szükséges.

**Tanári döntés kell:** ehhez az adaghoz nincs. Q4 helyben kész;
a következő nagyobb tételhez választás szükséges. Javaslat: Q6 teljesítménymérés.
