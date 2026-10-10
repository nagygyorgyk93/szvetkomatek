# I1 — Az első három interaktív ábra

## Állapot — 2026-10-10

A tanár jóváhagyásával **I1-04, I1-06 és I1-13 helyben elkészült**.
Kiindulás: `a2eac5a`, tiszta helyi `main`, azonos tárolt `origin/main`;
távoli frissítés nem történt. Új ág és push nincs.

| Jelölt | Tananyag | Mit lehet kipróbálni? |
|---|---|---|
| I1-04 · 1e | [Homotécia és hasonlóság](../1e/08-hasonlosag/tananyag-homotecia-es-hasonlosag.html#s1) | Pozitív/negatív arány, nagyság 0,25–2,5; megfelelő oldalak és kerületek aránya, területarány. |
| I1-06 · 2e | [Az exponenciális függvény](../2e/03-exponencialis-es-logaritmus-fuggveny/tananyag-exponencialis-fuggveny.html#s2) | Növekvő/csökkenő eset; alap 1,01–5 vagy 0,10–0,99, százados lépéssel; közös tengelymetszet és néhány függvényérték. |
| I1-13 · 4e | [A sorozat határértéke](../4e/01-sorozatok-hatarerteke/tananyag-hatarertek-fogalma.html#s2) | A meglévő a_n = 2 + 1/n sorozat nyílt ε-sávja; ε = 0,05–0,50, látható tagok száma 12–60; az első belső tag indexe és a látható pontok besorolása. |

Mindhárom ábra címkézett natív vezérlőt, **Kezdőállapot** gombot és szöveges
állapotjelzést kapott. A gomb visszaállítja az összes vezérlőt. A kártya világos,
a tinta sötét; JavaScript nélkül a statikus kezdőkép és magyarázata olvasható.
Nyomtatásban az ábra és a kijelzett állapot megmarad, a vezérlők rejtve vannak.
Külső könyvtár nem került az oldalra.

### Matematikai határesetek

- **Homotécia:** k = 0 nem választható. Negatív aránynál a képpontok a középpont másik oldalán vannak. A hossz- és kerületarány |k|, a területarány k²; k = 1 az azonosság, k = −1 a középpontos tükrözés. Az eredeti és a kép vonaltípusa is eltér.
- **Exponenciális függvény:** az a = 0 és a = 1 alap kizárt. A két megengedett tartomány külön választható; mindkét esetben f(0) = 1. A görbe a rögzített rajzablaknál vágódik el, nem ad hamis vízszintes folytatást. A kijelző a kerekített számértékeket közelítőként nevezi meg.
- **Sorozat:** a sáv nyílt, a határon lévő tag kívül marad és külön, üres pontként is látható. A feltétel 1/n < ε; az első belső index floor(1/ε) + 1. A határeset eldöntése egész számokkal történik, kerekítési bizonytalanság nélkül. A kijelzett indextől minden további tag a sávban van. Ha a látható részben még nincs belső tag, a szöveg jelzi a tagszám növelését.

## Forrás és lektori javítás

Új, közös modellsegédek a `tananyag_common.py` és `abra_common.py` fájlban;
három új mód az `interaktiv.js`-ben; közös, a modellkártyákra korlátozott CSS.
A 2e és 4e HTML a saját builderéből készült. A kézzel migrált 1e-lap első
ábráját a közös segéd kimenete váltotta fel.

A kontextus nélküli lektor csak a három tanulói szöveget kapta. A számításokat
és a saját kvízeket helyesnek találta. Hibatábla után pontosított szövegek:

| Hol | Pontosítás |
|---|---|
| 1e hasonlóság definíciója | A „középpontos hasonlósággal” megfogalmazás az azonos méretű esetet is megengedi. |
| 2e exponenciális függvény tulajdonságai | A pozitív valós számok célhalmazával a bijektivitás helyes; az egyenletekhez szükséges injektivitás külön szerepel. |
| 4e végtelenhez tartás | A leírás nem sugallja, hogy a sorozatnak monotonnak kell lennie. |
| Modellfelirat és a 4e/01 három lapja | „félszélesség”; „Véd Vilmos csapdája”. A racionális törtek és a gyökös kifejezések lapján csak a dobozcím változott. |

A javított részek második lektori ellenőrzése rendben. Új gyakorlófeladat,
új feladatszámadat és új indukciós feladat nincs; a meglévő példák megmaradtak.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Újraépítés | 2e és 4e builder → képek → média → háttér/betöltési jelzések → naplótérkép → keresőindex; minden lépés sikeres. 334 média 139 lapon megmaradt. |
| Kánon, belső link, gyakorlósáv | 310 oldal, 0 hiba; két korábbi heurisztikus visszautalás-jelzés megmaradt. |
| Végleges jsdom-render | Mind az öt módosult tananyaglap: 411 képlet, 10/10 kvíz, 0 hiba. |
| Kulcsok és regresszió | 4499 kulcsellenőrzés, 0 eltérés; 4499/4499 érzékenység, 100%. A SymPy 1.14.0 a repón kívüli környezetben rendelkezésre áll. |
| Mobil és asztal | Edge 154.0.4258.62, a projekt túlcsordulásmérésével: három új modell × 360/390/1280 px × kezdő/szélső állapot = 18 nézet, 0 túlcsordulás, JavaScript-, KaTeX- vagy helyi betöltési hiba. |
| Kezelés | 11 billentyűzetes próba, 3 tényleges érintéses csúszkapróba, kezdőállapot-visszaállítás; 8 korábbi interaktív ábra működéspróbája sikeres. |
| Akadálymentesség, nyomtatás | Három teljes lap axe-próbája: 0 automatikusan jelzett eltérés. Hat nyomtatási eset JavaScripttel/nélküle; mindhárom kezdőkép JS nélkül is olvasható. |
| Független matematikai kontroll | Mind a 20 homotéciaállás oldala, kerülete, területe és középpontos aránya; 8 exponenciális alap 1288 görbepontja SymPy-val; 30 ε/tagszám állapot 930 sorozatpontja pontos törtekkel ellenőrizve. 490 megengedett alapnál érvényes görbe készül. 0 eltérés. |

A lektor a szöveget ellenőrizte; a rajzot és a vezérlést a független matematikai
és böngészőpróba vizsgálta. A mobilos, negatív egységarányú, sávhatáros,
nyomtatási és JS nélküli képeket szemrevételeztem. Egy ismételt képernyőkép-próba
az elem mozgására várva megszakadt; a mozgásmentes végleges kör sikeres.
Új teljesítménymérés nem indult.

### Megőrzés

305 HTML és 627 korábbi követett fájl byte szerint változatlan. Az öt módosult
lap az új ábrákon, ábrafeliratokon és a jelzett mondatokon kívül azonos DOM-ot
ad; a 10 kvíz, korábbi oldalhorgonyok, feladatok, média és egyéb ábrák megmaradtak.
A 308 bejegyzéses keresőindexben csak az öt érintett URL tartalma változott;
nincs üres szöveg/cím. A naplótérkép, médiakatalógusok, tükrözött dokumentáció
és a zárolt első 23 backlog-sor azonos. A nyers próbák a repón kívül maradnak.

## Korlát és következő lépés

Az élő publikált változat, valódi telefon és képernyőolvasó, más böngésző,
teljes PDF-tördelés és a külső média új lejátszása ebben az adagban nincs ellenőrizve.
Az axe-próba nem teljes WCAG-minősítés. A mobilpróba helyi Edge emulációban futott.

**Tanári döntés kell:** az elkészült három modellhez nincs.
A többi 13 jelölt megvalósítása a [jelöltlistából](I1_interaktiv_jeloltlista.md)
választható; a meglévő GeoGebra cseréjéről külön tanári döntés szükséges.
Helyi `main`, új ág és push nélkül.
