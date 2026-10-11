# Főoldal — tömörebb fogadás és két videóikon

## Állapot — 2026-10-11

**A tanár kért főoldali változtatása elkészült és ellenőrizve van.**
Kiindulás: `6f7bc32`; frissen ellenőrzött, tiszta `main`, azonos `origin/main`,
be nem olvasztott ág nélkül. A korábbi engedély szerint a lezárt adagot publikáljuk;
a tényleges commit és Pages-eredmény az élő állapotnaplóban szerepel.

## Mi változott?

| Korábbi megoldás | Új megoldás |
|---|---|
| A magas videó alatt kezdődött az osztályválasztó, a köszöntő alatt nagy üres résszel. | Asztalon balra a köszöntő és közvetlenül alatta a négy osztálykártya; jobbra külön, keskeny videóoszlop. 900 px-ig a videó az osztályválasztó után kerül. |
| Három szöveges gomb: Hang be, Videó folytatása/szüneteltetése, Magyar felirat. | Pontosan két ikon a videó alján: hang ki/be és lejátszás/szünet. Az ikon és magyar felolvasási neve a tényleges médiaállapotot követi. |
| A hanggomb újraindította a videót, egyszeri hangos lejátszásra. | A hang külön kapcsolható; nem módosítja az időpozíciót és nem indítja el a szüneteltetett felvételt. A választott hangállapot a lejátszás végén is megmarad. |
| Időzített felirat és külön „A köszöntővideó szövege” lenyíló. | A külön lenyíló megszűnt. A tanár által jóváhagyott teljes köszöntőszöveg mindig olvasható közvetlenül a videó alatt; nem igényel gombot. |

Az ikon 20×20 px; a kattintási/érintési terület 44×44 px. Natív gomb,
magyar név és súgó, látható billentyűzetes fókusz. A néma automatikus lejátszás
megmaradt; mozgáscsökkentő beállításnál a videó felhasználói indításra vár.
Blokkolt automatikus indításnál is a helyes lejátszásikon jelenik meg.
JS nélkül a videó natív vezérlői és magyar feliratsávja használható, az alatta
lévő teljes szöveg is olvasható. Nyomtatásban nincs üres videóoszlop.

Az asztali, 1280 px-es nézetben a köszöntő és az osztályválasztó címe közötti
távolság **633 → 35 px**, a 390 px-es mobilnézetben
**732 → 35 px**. Ez elrendezési összevetés, nem sebességmérés.

## Ellenőrzés

| Réteg | Eredmény |
|---|---|
| Elrendezés | Edge 155.0.4283.45; 360/390/640/768/960/1280 px, 6 nézet, 0 túlcsordulás és osztálycím-ütközés. Asztalon külön oszlop, kisebb képernyőn a választó után a videó. |
| Videó állapota | 30 ellenőrzött állapot: hang ki/be szünet és lejátszás alatt, időpozíció megőrzése, nulla hangerő helyreállítása, szünet/folytatás, befejezés/újrakezdés hangállapot-megőrzéssel, néma automatikus indítás, mozgáscsökkentés. |
| Billentyűzet és érintés | Mindkét gomb Space/Enter billentyűvel és látható fókusszal; 7 tényleges tap mobil emulációban. A két név az Edge hozzáférhetőségi fájában is megjelenik. |
| Akadálymentesség | Teljes főoldal axe-próbája 390 és 1280 px-en: 0 automatikusan jelzett eltérés. 44×44 px célterület; ikon és név megfelel a tényleges hang/lejátszás állapotának. |
| JS nélkül és nyomtatás | 2 JS nélküli nézet, natív vezérlés és olvasható felirat; 8 nyomtatási eset JS be/ki, videóoszlop nélkül. |
| Automatikus indítás visszautasítása | Külön szimulált első play-visszautasítás után a kézi indítás valódi médialejátszással sikeres. |
| Közös kezelőfelület | A tananyag mobil tartalomjegyzéke és kvíze, a főoldali tanulásfolytató kártya és az asztali kereső működéspróbája sikeres. |
| Kánon, linkek és gyakorlósáv | 310 oldal, 0 hiba; a sávellenőrzés tiszta. Célzott jsdom a főoldalra és egy tananyagra. A jsdom nem szimulál médialejátszást, ezért a play() jelzése nem helyettesíti a valódi Edge-próbát. |
| Naplótérkép és keresőindex | A naplótérkép változatlan. 308 nem üres indexbejegyzés; csak az index.html bejegyzése változott. |
| Szemrevételezés | Asztali és mobil főoldal, a két ikon és felirat, valamint a világos nyomtatási nézet átnézve. |

Nincs böngészős JS-, KaTeX- vagy helyi betöltési hiba, sem konzolfigyelmeztetés.
A főoldal kézzel szerkesztett; builder és matematikai tartalom nem változott,
ezért feladatkulcsok újraszámolása nem indokolt ebben az adagban.

## Megőrzés és korlátok

309 HTML változatlan. A köszöntő, a négy osztálykártya és a főoldal többi
szakaszának DOM-ja azonos; a videó forrásai, posztere és magyar feliratsávja
megmaradtak. A közös ui.js a videókezelő szakaszon kívül bájtazonos.
Médiakatalógus, tananyag, feladat, végeredmény, tükrözött dokumentum és
az első 23 zárolt backlog-sor változatlan. A próbák a repón kívül maradtak.

Valódi telefon, fizikai hangkimenet és képernyőolvasó nem volt kipróbálva;
az Edge hozzáférhetőségi fáját ellenőriztem. Más böngésző és teljes PDF-oldaltördelés
nincs minősítve. Az axe-próba nem teljes WCAG-minősítés. Új sebességmérés nincs.

**Tanári döntés kell:** nincs a kért főoldali változtatáshoz.

## Tanári pontosítás — 2026-10-11

A tanár kérésére a videó alatti „Kiképzőtiszti fogadás” cím megszűnt.
A jóváhagyott köszöntőszöveg, az ikonok és az elrendezés változatlan.
A keresőindex újraépült: 308 bejegyzés, csak a főoldali változott;
a naplótérkép azonos. Kánon és linkek: 310 oldal, 0 hiba.
A főoldali forrásban pontosan a kért cím törlődött; új böngészős
és matematikai próba ehhez az egyszerű törléshez nem futott.
Tanári döntés kell: nincs. A publikálás eredménye az élő állapotnaplóban.
