# -*- coding: utf-8 -*-
"""A tanár gépén élő, publikálható kánon-dokumentumok tükrözése a repóba (felhős munkához).

A felhős Claude Code-munkamenet csak a repót látja. A workflow, a jelölés-kánon, a
köntös-bibliák és két webes skill ezért TÜKÖRKÉNT a repóba kerül — a forrásuk továbbra is
a privát mappa, itt NEM szerkesztendők (a következő tükrözés felülírja).

Csak az itt felsorolt fájlok mennek át (fehérlista). Privát anyag (állapotfájl, tiltott-
listák, felmérők, munkafájlok, tanulói adat) SOHA. Kiírás előtt tartalmi szűrés is fut:
e-mail-cím, telefonszám, és ha létezik, a  projektek/szvetkomatek/tiltott/tukor_tiltas.txt
reguláris kifejezései (soronként egy) — találat esetén semmi nem íródik ki.

Futtatás a tanár gépén (Cowork), a web-gyökérből:
  python _tools/docs_tukor.py            száraz futás: mi változna
  python _tools/docs_tukor.py --apply    írás
"""
import datetime, glob, os, re, sys

WEB = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CLAUDE = os.path.abspath(os.path.join(WEB, ".."))
PROJ = os.path.join(CLAUDE, "projektek", "szvetkomatek")

# (forrás a Claude-gyökérhez képest, cél a web-gyökérhez képest)
FEHERLISTA = [
    ("projektek/szvetkomatek/_WEBOLDAL_workflow.md", "_docs/workflow.md"),
    ("_JELOLESEK.md", "_docs/jelolesek.md"),
    (".claude/skills/web-verifikacio/SKILL.md", ".claude/skills/web-verifikacio/SKILL.md"),
    (".claude/skills/matek-abra/SKILL.md", ".claude/skills/matek-abra/SKILL.md"),
]
for f in sorted(glob.glob(os.path.join(PROJ, "tortenet", "_WEBOLDAL_tortenet*.md"))):
    nev = os.path.basename(f).replace("_WEBOLDAL_", "")
    FEHERLISTA.append((os.path.relpath(f, CLAUDE).replace(os.sep, "/"), f"_docs/tortenet/{nev}"))

GYANUS = [re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), re.compile(r"\+?\d{2,3}[ /-]?\d{2,3}[ /-]\d{3}[ /-]?\d{3,4}")]
TILTAS = os.path.join(PROJ, "tiltott", "tukor_tiltas.txt")


def fejlec(forras):
    ma = datetime.date.today().isoformat()
    return (f"<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): {forras} · "
            f"tükrözve: {ma} · _tools/docs_tukor.py -->\n")


def tukrozott(forras, szoveg):
    fej = fejlec(forras)
    if szoveg.startswith("---\n"):  # SKILL.md: a frontmatter maradjon legelöl
        vege = szoveg.find("\n---\n", 4)
        if vege > 0:
            return szoveg[:vege + 5] + "\n" + fej + szoveg[vege + 5:]
    return fej + "\n" + szoveg


def torzs(s):  # a dátumos fejléc nélkül — a változás-összevetéshez
    return re.sub(r"<!-- TÜKÖR — .*? -->\n", "", s)


def main(argv):
    apply = "--apply" in argv
    minta = list(GYANUS)
    if os.path.isfile(TILTAS):
        for sor in open(TILTAS, encoding="utf-8"):
            sor = sor.strip()
            if sor and not sor.startswith("#"):
                minta.append(re.compile(sor, re.I))
    hibak, iras = [], []
    for forras, cel in FEHERLISTA:
        fut = os.path.join(CLAUDE, forras)
        if not os.path.isfile(fut):
            hibak.append(f"hiányzik a forrás: {forras}")
            continue
        szoveg = open(fut, encoding="utf-8").read()
        for m in minta:
            t = m.search(szoveg)
            if t:
                hibak.append(f"{forras}: tiltott/gyanús tartalom: {t.group(0)!r} (minta: {m.pattern})")
        celut = os.path.join(WEB, cel)
        regi = open(celut, encoding="utf-8").read() if os.path.isfile(celut) else None
        if regi is None or torzs(regi) != torzs(tukrozott(forras, szoveg)):
            iras.append((celut, tukrozott(forras, szoveg), cel))
    for h in hibak:
        print("  HIBA:", h)
    if hibak:
        print("docs_tukor: hiba miatt semmi nem íródott ki.")
        return 1
    for celut, s, cel in iras:
        print(f"  {'ír' if apply else 'változna'}: {cel}")
        if apply:
            os.makedirs(os.path.dirname(celut), exist_ok=True)
            open(celut, "w", encoding="utf-8", newline="\n").write(s)
    print(f"docs_tukor: {len(FEHERLISTA)} fájl, {len(iras)} "
          f"{'frissítve' if apply else 'változna (--apply nélkül nem ír)'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
