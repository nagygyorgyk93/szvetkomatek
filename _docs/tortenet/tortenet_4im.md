<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): projektek/szvetkomatek/tortenet/_WEBOLDAL_tortenet_4im.md · tükrözve: 2026-09-27 · _tools/docs_tukor.py -->

# Évad-biblia — 4im: *A Végső Patch* (Véd Vilmos & Nagol, tech-ág)

> Közös alap: `_WEBOLDAL_tortenet.md` (világ, állandó szereplők, köntös-rétegek, hátterek).
> Kötelező szerkezeti kánon: `_WEBOLDAL_workflow.md` 4b. + 8. szakasz.
> **Állapot: még nem indult.** Érettségi évfolyam, **165 óra** — a gimnázium legnehezebb
> matekja; a köntös oldja a nyomást, de a szint itt a legmagasabb (S és N kimenetek).

---

## 1. Logline

Miután Véd Vilmos felrobbantotta az I.V.H. központi szerverét és az **Időszövőszéket**, a tér és az
idő határai elmosódnak. Az **informatikus kadétoknak** a vonakodó **Nagol** és az I.V.H.
tech-zsenije, **Uroborosz** segítségével kell megírniuk a „Végső Patch-et" — mesterszintű analízissel
és numerikus approximációval —, mielőtt a szerver végleg lenullázódik.

## 2. A helyszín

**Szvetkó-kampusz — a „törölt" idővonal (The Void) és az I.V.H. szerverterme.** Az oldal néha
„glitch-el", a felület meg-megbicsaklik (direkt). A kampusz egyik fele a Void pusztaságára néz,
a másik az I.V.H. retro-futurisztikus, sárgán villogó gépterme. Véd Vilmos filctollal ír bele a
felületbe. A Vészterem itt a **I.V.H. Szerverterem**.

## 3. A tét — a fő szál

Az I.V.H. ügynökei szerint a 4im kódja hibás, ezért „megmetszenék" (prune) az évfolyamot. Az egyetlen
kiút: bizonyítani, hogy a kadétok képesek **algoritmizálni a pillanatnyi változást** (derivált),
**újra összerakni a széttört valóság 3D-s darabjait** (integrál), **kimatekozni az esélyeket a
legdurvább eloszlásokkal** (valószínűség), és ha nincs egzakt megoldás, akkor **tökéletesen
közelíteni** azt (numerikus matematika).

> **Pedagógiai mag:** a 4im anyaga már-már egyetemi szintű (L'Hôpital, Taylor, forgástestek,
> numerikus közelítés). Véd Vilmos a humor, Nagol és Uroborosz a kíméletlen szigor és a stabilitás:
> *„Ha még egyszer lehagyod a `dx`-et az integrál végéről, levágom a kezed."*

## 4. Évad-szereplők

| Szereplő | Szerep az évadban |
|---|---|
| **Véd Vilmos** | a „mentor": kommentál, gúnyolódik, áttöri a negyedik falat — most kifejezetten a kockákra, kóderekre, energiaitalra hegyezve |
| **Nagol hadnagy** | a morcos helyettesítő: ő hozza a komoly analízist; célja, hogy a diákok túléljék az érettségit és a felvételit |
| **Uroborosz** | az I.V.H. tech-zsenije: a **numerikus matematika** és az algoritmusok fő mentora |
| **Mr. Szürreál (I.V.H.)** | a bürokrata akadály: Poisson- és normális eloszlásokkal próbál elgáncsolni |

**SZVETI** sérült verzióban: passzív-agresszív, és rendszeresen kritizálja Véd Vilmos
kóder-képességeit.

## 5. Fejezet-térkép — a 4im 5 témaköre

| # | Témakör (mappa) | Küldetés-cím | Mentor | A matek → a sztoriban |
|---|---|---|---|---|
| 01 | Függvények (határérték, tulajdonságok) | **A Végtelen Glitch** | **Véd Vilmos & Uroborosz** | Függvényvizsgálat, aszimptoták, limesz: fel kell térképezni a kód „viselkedését" és a szakadási pontokat, nehogy egy aszimptota mentén lezuhanjanak az Ürességbe. |
| 02 | Differenciálszámítás | **Maximális erőbedobás (Maximális Sebesség)** | **Nagol** | Derivált, érintő, szélsőérték; külön fókusz a **L'Hôpital-szabályon** („Kórház-szabály"), a másodrendű deriválton és a Taylor–Maclaurin-közelítésen. |
| 03 | Integrálszámítás | **A Valóság Újra-fordítása (Kompilálása)** | **Nagol & SZVETI** | Helyettesítéses és parciális integrálás; **forgástestek térfogata** (Véd Vilmos megforgat egy bureket az $x$ tengely körül) és **ívhossz** (mekkora utat tesz meg a katana hegye). |
| 04 | Valószínűségszámítás és statisztika (kombinatorikával) | **A Multiverzum Rulett** | **Mr. Szürreál vs. Véd Vilmos** | Kombinatorika, Bayes-tétel, binomiális, Poisson- és normális eloszlás, adatfeldolgozás: bizonyítás az I.V.H. statisztikai hivatala előtt. |
| 05 | Numerikus matematika | **A Káosz-Approximáció** | **Uroborosz & Véd Vilmos** | **Csak a 4im-nek:** közelítő számok, abszolút/relatív hiba, Lagrange-interpoláció, egyenletek közelítő megoldása. Nincs egzakt megoldás — algoritmussal kell „elég jó" eredményt adni. **Klimax.** |

> A szál íve: **a szerverhibák feltérképezése → a változások algoritmizálása → a kód
> újraépítése → esélylatolgatás az I.V.H. ellen → a Végső Hack (közelítő futam).**

## 6. Köntös-szótár (4im)

| Oldal-elem | Köntös-név |
|---|---|
| témakör-index | **A Negyedik Fal** — Véd Vilmos üzenete az IT-s diáknak |
| tananyag `s0` | **📡 Küldetés-eligazítás** — a szövegben **🌮 Patch Notes (frissítési napló)**: miért kell ez a matek a gépnek |
| kidolgozott példa | **I.V.H. Core Logs** — hivatalos levezetés, Véd Vilmos széljegyzeteivel |
| „🎯 Gyors kérdés" | Syntax Error teszt („Fatal Error. Ezt még regenerálni is fáj.") |
| csapda-doboz | **Véd Vilmos bug** — hiányzó $+C$, rossz eloszlás, elhagyott feltétel: a diáknak debuggolnia kell |
| feladatgyűjtemény | **Zsoldos-algoritmusok** (Alap = Zöldfülű, Közép = X-Force, Nehéz = Maximális erőbedobás) |
| házi | **I.V.H. Szerverterem (Vészterem)** |
| differenciált sávok | **🐶 Véd-eb debugger** (könnyített) / **⚔️ Maximális erőbedobás** (normál) |
| projekt | **Az Üresség (The Void) tisztítása** |
| összefoglaló | **Csalópapír (Cheat Sheet)** |

## 7. Hangnem

Mint a 4e — irónia és negyedik fal —, de **tech-fókusszal**: a „tech-bro" kultúra szerethető
kifigurázása, kóder-poénok, algoritmus-metaforák. **Káromkodás nincs**, kreatív cenzúra van.
DP tudja, hogy a diák informatikus és komolyabb pályára/felvételire készül.

**Matek-első:** az analízis és a numerikus matek száraz és nehéz tud lenni. Nagol és Uroborosz a
stabilitás: ők vezetik le a Lagrange-féle interpolációs polinomot, miközben Véd Vilmos a
háttérben lángszóróval főz kávét.

## 8. Kidolgozási jegyzetek

**A 05. (numerikus matematika, 16 óra) — az évfolyam megkoronázása:**

1. **Hibaszámítás** — a valóságot nem lehet tizedesjegyre pontosan megmenteni (túlmelegednek a
   szerverek). Uroborosz elmagyarázza az abszolút és a relatív hiba különbségét.
2. **Lagrange-interpoláció** — csak néhány adatpont élte túl a robbanást; ezekre kell polinomot
   illeszteni, hogy át lehessen ugrani az Ürességen.
3. **Egyenletek közelítő megoldása (felező, húr-, érintőmódszer)** — a végső bossharc: olyan
   egyenletet kell megoldani, amit analitikusan nem lehet. Véd Vilmos kedvence a **felező
   módszer**: a katanájával vágja ketté újra és újra az $[a,b]$ intervallumot, amíg a hiba egy
   megadott $\varepsilon$ alá nem csökken.

**Megjegyzés a 4e-hez képest:** a két évad ugyanazon a Véd Vilmos–Nagol vonalon fut, de a 4im
ága **tech-központú** (Uroborosz, szerverterem, algoritmusok), és a numerikus matematika miatt eggyel
hosszabb ívű. Ha egy szöveges feladat vagy magyarázat mindkét tagozatnak jó, nyugodtan
újrahasznosítható — a **szint** viszont eltér (4im: több S/N kimenet).
