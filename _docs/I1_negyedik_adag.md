# I1 — A 2e három új interaktív ábrája

## Állapot — 2026-10-11

**I1-05, I1-07 és I1-08 elkészült és ellenőrizve van.** Kiindulás: `2e5936a`,
tiszta helyi `main`; friss távoli lekérés után egy korábbi, ellenőrzött commit
állt feltöltésre várva. Be nem olvasztott ág nincs. A tanár minden lezárt,
ellenőrzött adag feltöltését engedélyezte; a tényleges push és Pages-publikálás
eredményét az élő állapotnapló rögzíti. Új ág nem készült.
Az I1-listából **11/16 modell kész, 5 terv maradt**.

| Jelölt | Lap és vezérlés | Tanulási cél |
|---|---|---|
| I1-05 | [Komplex szám](../2e/01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-komplex-szam-fogalma.html#s3): valós és képzetes rész −4–4, negyedegységgel. | Algebrai alak, koordináták, konjugált és modulusz összekapcsolása; tengelyen és origóban is helyes állapot. |
| I1-07 | [Másodfokú–lineáris rendszer](../2e/02-masodfoku-egyenletek-es-fuggvenyek/tananyag-masodfoku-linearis-rendszer.html#s1): az y = x + c egyenes eltolása, c = −4–2. | A megoldáspárok közös pontok: nulla, egy vagy két valós megoldás. |
| I1-08 | [Szinuszegyenlet](../2e/04-trigonometrikus-fuggvenyek/tananyag-trigonometrikus-egyenletek.html#s1): sin x = b, b = −1,5–1,5, 0,05-ös lépéssel. | A megoldáshalmaz a zárt [0;2π] intervallumon, a szélső értékekkel és végpontokkal. |

A `matematika-2e` skill és a kimenetek az alapok:
`MAT.A.SO.S.1.1 (1.1, 1.5)`, `MAT.A.SO.S.1.2 (2.9)` és
`MAT.A.SO.S.1.2 (2.4)`. A három modell a meglévő példából indul.
Új gyakorlófeladat vagy feladatszámadat nincs. A megőrzött kiegészítő tananyag
és a hét érintett médiablokk változatlan.

Világos SVG-kártyák, címkézett natív csúszkák, **Kezdőállapot** gomb és
élő szöveges állapot készült, külső könyvtár nélkül. A jelölések alakjuk és
vonalstílusuk alapján is megkülönböztethetők. JS nélkül a statikus kezdőkép és
számszerű állapot olvasható; a caption képletei ilyenkor TeX-jelöléssel jelennek
meg, mert a közös képletrenderhez JS szükséges. Nyomtatásban a vezérlők rejtve
vannak, az aktuális ábra és állapot megmarad.

## Matematikai határesetek

- **Komplex szám:** kezdő z = 3 + 2i, konjugált 3 − 2i, modulusz √13. Azonos egységnyi hossz a két tengelyen. A modulusz gyökös alakja pontos, mellette szükség esetén négy tizedesre kerekített érték látszik. Valós számnál a pontok egybeesnek; az origóban a modulusz nulla. A konjugált körvonalas, az eredeti szám teli pont. Az eredeti képaláírás horgonya megmaradt.
- **Parabola–egyenes:** y = x² − 2x rögzített, a meredekség 1. A kezdő c = −2 két pontja (1;−1), (2;0). c = −2,25-nél egy érintési pont van: (1,5;−0,75); kisebb c-nél nincs, nagyobbnál két közös pont. Az irracionális koordinátáknál ≈ jel szerepel. A görbe a rajzablakon kívül vágott, a függvényérték nem lapul el.
- **Szinuszegyenlet:** b = 0,5-nél π/6 és 5π/6; b = 0-nál három külön megoldás, 0, π, 2π. b = 1-nél π/2, b = −1-nél 3π/2 az egyetlen megoldás. Ha |b| > 1, nincs megoldás. A tengely radiános; a jellegzetes szögek pontosan, a többiek kerekített radiánértékkel jelennek meg.

## Lektori és megjelenítési pontosítások

A kontextus nélküli lektor csak a három tanulói szöveget kapta. A példák
eredményeit és mind a hét gyors kérdés válaszát helyesnek találta.
A szöveges export gyökjel-/felülvonás-vesztéseit elkülönítette az oldal
tényleges megjelenítésétől; utóbbit a render és a böngészőpróba ellenőrizte.
Hibatábla után két mondat pontosult, és a lektor visszaellenőrizte őket:

| Hol | Mi változott? |
|---|---|
| Rendszerek bevezetője | „Az első példában” megfogalmazás korlátozza a parabola említését; később körpélda is szerepel. |
| Egyenlőtlenségek menete | A periódusos eltolás radiánban +2kπ, fokban +k·360°, k egész. |
| Komplex ábra feliratai | A felülvonás tényleges szélességét is figyelembe véve elkerülik az Im és az egységjelölések helyét. A végleges 1089 állásban nincs feliratütközés. |

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | Három saját builder → képek → média → háttér → naplótérkép → keresőindex, minden lépés sikeres; 334 aktív média 139 lapon. |
| Kánon, linkek, gyakorlósáv | 310 oldal, 0 hiba; két korábbi heurisztikus jelzés változatlan. |
| Végleges jsdom-render | Három lap, 324 képlet, 7/7 kvíz, 0 hiba. |
| Kulcs és regresszió | 4499 kulcsellenőrzés, 0 eltérés; 4499/4499, 100% érzékenység. SymPy a privát környezetből. A két utolsó mondat- és feliratpontosítás után célzott render/link/sáv és böngészőpróba futott. |
| Elrendezés | Edge 154.0.4258.62; három modell × 360/390/1280 px × kezdő/szélső állapot = 18 nézet, 0 túlcsordulás. |
| Kezelés | 12 billentyűzetes próba és visszaállítások; 4 tényleges érintéses csúszkapróba emulált mobilkörnyezetben. Mind a 16 korábbi saját modell működéspróbája sikeres. |
| Akadálymentesség | Három teljes lap axe-próbája: 0 automatikusan jelzett eltérés. Nincs JS-, helyi betöltési vagy KaTeX-hiba, illetve konzolfigyelmeztetés. |
| JS nélkül és nyomtatás | Három olvasható statikus kezdőkép és állapot; 6 nyomtatási eset JS be/ki, a vezérlők rejtve vannak. |
| Független matematika | 1089 komplexszám-állás: pontos modulusz SymPy-val, pontok/tükrözés és koordinátaskála; 25 rendszer SymPy-megoldással; 61 szinuszegyenlet négy monoton negyedben végzett felezéssel, inverz szögfüggvény nélkül. Minden megoldás, számkijelzés és ponthelyzet helyes. |
| SVG-geometria | 482 tényleges görbepont és a vágás ellenőrizve; 1089 komplex feliratállás, 0 ütközés. Kezdő-, szélső-, origó-, érintési-, megoldás nélküli-, végpontos-, JS nélküli és nyomtatási képek szemrevételezve. |

### Megőrzés és hatókör

307 HTML és 633 korábbi követett fájl byte szerint változatlan.
47 régi oldalhorgony, 7 kvíz és 7 médiablokk megmaradt. A három céloldal
az új ábrák és a két jelzett mondat kivételével azonos DOM.
A 308 nem üres keresőindex-bejegyzés közül csak a három cél-URL változott.
Naplótérkép, médiakatalógusok, tükrök és az első 23 zárolt backlog-sor azonos.
A privát tesztek és függőségek a repón kívül maradtak.

**Összesen 19 saját interaktív ábra, 18 működési mód** van
(1e: 1, 2e: 4, 3e: 3, 4e: 11). Az I1-ből 11/16 kész.
Hátravan I1-01, I1-02, I1-03, I1-10 és I1-16; a meglévő GeoGebra
lecserélésére javasolt négy további ötlet külön mérlegelendő.

## Korlátok és tanári döntések

Valódi telefonon, képernyőolvasóval és más böngészővel nincs új próba;
teljes PDF-tördelés és a külső média új lejátszása sem történt.
Az axe eredménye nem teljes akadálymentességi minősítés. A JS nélküli
captionban TeX látszik; az SVG és a számszerű állapot olvasható.
Új sebességmérés nem készült.

**Tanári döntés kell:** nincs az elkészült három modellhez.
