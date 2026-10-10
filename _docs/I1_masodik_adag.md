# I1 — Három interaktív geometriai ábra a 3e-ben

## Állapot — 2026-10-10

**I1-09, I1-11 és I1-12 helyben elkészült.** A tanár folytatási kérésére
a 3e három fennmaradó P1-jelöltjét vettem elő. Kiindulás: `8978f23`, tiszta
helyi `main`, azonos tárolt `origin/main`; távoli frissítés nem történt.
Új ág és push nincs. Az I1-listából összesen **6/16 modell kész, 10 terv maradt**.

| Jelölt | Tananyag és vezérlés | Mit figyelhet meg a tanuló? |
|---|---|---|
| I1-09 | [A gúla három derékszögű háromszöge](../3e/01-poliederek/tananyag-gula.html#s2): EOM, EOB, EMB vagy összes jelölés kiválasztása. | A befogók és az átfogó szerepe, H/h/s/r/R megkülönböztetése és a megfelelő Pitagorasz-összefüggés. |
| I1-11 | [Pont és egyenes távolsága](../3e/05-analitikus-geometria/tananyag-pont-es-egyenes-tavolsaga.html#pelda-riasztas): a próbapont x és y koordinátája 0–7 között, negyedegységes lépéssel; az eredeti egyenes rögzített. | A merőleges talppont és a távolság együtt változik. Az egyenesre kerülés és a pontosan 3 egységes határ külön is megfigyelhető. |
| I1-12 | [Kör és egyenes](../3e/05-analitikus-geometria/tananyag-kor-es-egyenes.html#s1): a 3x + 4y = c egyenes párhuzamos eltolása, c = −35–35 egész értékei. | A rögzített, 5 sugarú kör mellett két, egy vagy nulla közös pont; a középpont távolsága és a sugár kapcsolata. |

A cél a `matematika-3e` skill és a középszintű kimenetek alapján:
`MAT.G.SO.S.1.6 (6.2)`, `MAT.G.SO.S.1.5 (5.3, 5.4–5.5)`.
Új normálalak-levezetés vagy gyakorlófeladat nem került be. A kezdőképek a
meglévő ábrákhoz és példákhoz kötődnek; a szöveges feladatok számai megmaradtak.

Mindhárom modell a közös, világos kártyát, címkézett natív vezérlőt,
**Kezdőállapot** gombot és élő szöveges állapotjelzést használja.
JS nélkül a statikus kezdőkép, leírás és állapot olvasható. Nyomtatáskor a
vezérlők rejtve vannak, az ábra és a kijelzett állapot megmarad.
Külső könyvtár nem került a tanulói oldalra.

### Matematikai határesetek

- **Gúla:** EOM derékszöge O-nál, EOB-é O-nál, EMB-é M-nél van. H² + r² = h²; H² + R² = s²; h² + (a/2)² = s². A vetítés az eredeti négyzetes gúláé; a képaláírás jelzi, hogy a térbeli derékszög a vetületen torzulhat. A kiválasztott háromszög körvonala és szövege is megkülönbözteti az esetet.
- **Távolság:** a kezdőpont K(2;3), az egyenes 4x + 3y − 27 = 0, a talppont T(3,6;4,2), a távolság 2. A vezérlők csak a próbapontot mozgatják; a magyarázat egyértelműen a kezdőállapotra vonatkoztatja a meglévő példát és megoldását. Nulla távolságnál egy jelölt pont és „K = T” felirat van. A 3 egységnél közelebbi feltétel szigorú; a pontos határ nem számít belsőnek. A döntés egész számos bemenettel történik.
- **Kör:** x² + y² = 25, C(0;0) és r = 5 rögzített. A távolság |c|/5; c = ±25 esetén egyetlen közös pont szerepel, c = 0-nál a talppont a középponttal esik egybe. Az egész számos érintési döntés nem kerekítésből születik. A kijelző a szelő metszéspontjainak koordinátáit közelítőként nevezi meg.

## Lektori és megjelenítési javítások

A kontextus nélküli lektor csak a három tanulói szöveget kapta. Újraszámolta
a példákat; számolási hibát nem talált. A tanárnak bemutatott hibatábla után:

| Hol | Mi javult? | Forrás |
|---|---|---|
| Gúla: oldalél/oldallapmagasság csapdadoboza | A hibás „két különböző háromszögben él” mondat helyett az EMB félháromszögben h befogó, s átfogó. | Saját builder. |
| Távolság: gyorsismétlő | Az osztási arány jelentése AC:CB = m:n; a két pont által meghatározott egyenes mondata rövidebb és természetesebb. | Saját builder. |
| Kör: képaláírás | Egyetlen egyenes önmagával párhuzamos eltolását nevezi meg. | Közös tananyagsegéd. |
| Mozgó pontok és fix egyenletek | A fix egyenletfeliratok a rajz alatti, jobbra igazított szabad sávba kerültek. Az első alsó középre igazítás a kör y-tengelyének −8 feliratával ütközött; a végleges helyen mind a 912 állás ütközésmentes. | Közös ábragenerátor. |

A lektor a három javított szöveget visszaellenőrizte: új biztos hibát nem talált.
A kivonatban széteső törtekből nem következtettünk HTML-hibára; a valódi
képletrender és a kvízek külön ellenőrzése sikeres.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | A három 3e-builder → képek → média → háttér → naplótérkép → keresőindex; minden lépés sikeres. 334 média 139 lapon megmaradt. |
| Kánon, belső link, gyakorlósáv | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalás-jelzés megmaradt. |
| Végleges jsdom-render | Három módosult lap, 272 képlet, 6/6 kvíz, 0 hiba. |
| Kulcs és regresszió | 4499 kulcsellenőrzés, 0 eltérés; 4499/4499 érzékenység, 100%. A SymPy a repón kívüli környezetből futott. |
| Mobil és asztal | Edge 154.0.4258.62, a projekt elrendezésmérésével: három modell × 360/390/1280 px × kezdő/szélső állapot = 18 nézet, 0 túlcsordulás. A végleges igazítás után is sikeres. |
| Kezelés | 12 billentyűzetes próba, mindhárom kezdőállapot-visszaállítás; 3 tényleges érintéses csúszkapróba. A natív választó érintéssel nyílt, kiválasztása billentyűzettel is működött. A 11 korábbi saját ábra működéspróbája sikeres. |
| Akadálymentesség, JS nélkül, nyomtatás | Három teljes lap axe-próbája: 0 automatikusan jelzett eltérés. Mindhárom statikus kezdőkép olvasható; 6 nyomtatási eset JS be/ki sikeres, a végleges képek is ellenőrizve. |
| Független matematika | A gúla 3 háromszögének térbeli merőlegessége és Pitagorasz-azonossága, 4 választóállás; 841 ponthelyzet pontos törtekkel, ebből 8 egyenesre eső és 8 pontosan 3 egységes; 71 kör–egyenes helyzet független SymPy-egyenletrendszerrel: 49 szelő, 2 érintő, 20 elkerülő. Koordináták, távolságok, feliratok és vetítés helyesek. |
| Végleges feliratpróba | Mind a 841 ponthelyzetben és 71 egyenesállásban a fix egyenletfelirat ütközésmentes. Nincs JS-, helyi betöltési vagy KaTeX-hiba. |

A kezdő-, érintési, egybeesési, szélső, nyomtatási és JS nélküli képeket
szemrevételeztem. Új teljesítménymérés nem indult.

### Megőrzés

**307 HTML és 631 korábbi követett fájl byte szerint változatlan.** A három
módosult oldal az új ábrákon/feliratokon és a két jelzett tananyagi mondaton kívül
azonos DOM-ot ad. A 6 kvíz és 43 korábbi, SVG-n kívüli oldalhorgony megmaradt;
a feladatok, megoldások, médiák és többi ábra változatlanok.
A 308 bejegyzéses keresőindexben csak a három érintett URL változott.
A naplótérkép, médiakatalógusok, tükrök és első 23 zárolt backlog-sor azonosak.
Nyers próbák és függőségek a repón kívül maradtak.

## Korlát és következő lépés

Élő publikált oldal, valódi telefon/képernyőolvasó, más böngésző, teljes
PDF-tördelés és külső média új lejátszása ebben az adagban nincs ellenőrizve.
A mobilpróba helyi Edge emuláció; az axe nem teljes WCAG-minősítés.

**Tanári döntés kell:** az elkészült három modellhez nincs.
A további 10 jelölt a [jelöltlistán](I1_interaktiv_jeloltlista.md) maradt.
Az összes saját interaktív ábra száma 14: 1e 1, 2e 1, 3e 3, 4e 9.
Helyi `main`, új ág és push nélkül.
