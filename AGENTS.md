# AGENTS.md — Szvetkó matek

Ez a fájl a nem Claude-alapú kódoló ágenseknek (ChatGPT, Codex stb.) szól. **A teljes, kötelező útmutató a
[`CLAUDE.md`](CLAUDE.md)-ben van: olvasd el elsőként, és kövesd úgy, mintha neked szólna** — minden szabálya rád is
érvényes. Utána: `_docs/FELHO_FELADATOK.md` (backlog, zárolt területek), `_docs/workflow.md` (szerkezeti és vizuális
kánon), `_docs/jelolesek.md` (jelölés), `_docs/tortenet/` (köntös). A `.claude/skills/*/SKILL.md` fájlokat
(`media-beagyazas`, `web-verifikacio`, `matek-abra`) útmutatóként olvasd.

A legfontosabbak röviden:

- A repó **publikus**: felmérő-adat, tanulói adat, privát munkafájl, megoldókulcs nem kerülhet bele.
- **Builder-generált HTML-t kézzel ne szerkessz** — a buildert javítsd, futtasd, majd a teljes láncot
  (`kepek.py` → `media.py` → `set_hatter.py` → `verify_web.py` → `check_links.py` → `sav_check.py` → `kulcs_teszt.py`
  → `layout_teszt.py`). A builder újrafuttatása eltünteti a médiablokkokat és a háttér-attribútumot: ezeket a lánc
  teszi vissza. Utána `git diff --stat`: csak a szándékolt változás maradhat.
- **Push csak a tanár kifejezett kérésére**; felhőben/GitHubon saját ág + PR. Commit-üzenet magyarul, ékezet nélkül.
- Nyelv: magyar. A tanári döntést igénylő kérdéseket gyűjtsd egy „Tanári döntés kell” listába.
