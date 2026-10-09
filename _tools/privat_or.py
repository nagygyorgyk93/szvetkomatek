#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Privát-őr: commit előtt megállítja, ami nem kerülhet a publikus repóba.

A `.githooks/pre-commit` futtatja. A commitba kerülő ÚJ sorokat és fájlneveket nézi:
  1. tiltott útvonal: `tiltott_*.py`, felmérő a fájlnévben, `.docx`, `.xlsx`
  2. a privát fájlok fejlécének jelölése (lásd PRIVAT_JEL)
  3. tanulónév, mindkét névsorrendben, latinul és cirillül
  4. visszamásolt tiltólista: `TILTOTT… = [` jellegű értékadás (a listák 2026-09-27 óta a
     repón kívül élnek, a builderek a `tiltott.modul()`-lal töltik be őket)

Az egyes tiltott kifejezéseket szándékosan NEM keressük szó szerint: a listák a tananyag
saját kidolgozott példáit is tartalmazzák (hogy a gyakorlóban ne ismétlődjenek), ezért a
tananyag-builderekben jogosan szerepelnek. Az ütközést a builderek önellenőrzése fogja.

A tanulónevek a repón KÍVÜLRŐL töltődnek be (pedagógiai füzet, versenyzői névsor),
ez a fájl egyet sem tartalmaz. Ha a privát mappa nem
érhető el, a commit megáll. Tudatos kivétel: `git commit --no-verify`.

Kézi teszt staged tartalom helyett megadott fájlokra:
    python _tools/privat_or.py --teszt FAJL [FAJL ...]
"""
import fnmatch
import json
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GYOKER = os.path.abspath(os.path.join(REPO, ".."))          # a Claude-mappa, a repó mellett
PRIVAT_JEL = "NEM kerülhet " + "a publikus repóba"           # összerakva, hogy ez a fájl ne akadjon fenn rajta
TILOS_UT = ["*tiltott_*.py", "*felmero*", "*felmérő*", "*Felmero*", "*.docx", "*.xlsx"]
SZOVEG = (".html", ".js", ".mjs", ".json", ".md", ".py", ".css", ".txt", ".yml", ".svg")


def _privat(*resz):
    ut = os.path.join(GYOKER, *resz)
    return ut if os.path.exists(ut) else None


def tanulonevek():
    """Teljes nevek mindkét sorrendben. Forrás: pedagógiai füzet + versenyzői névsor."""
    nevek = set()
    fuzet = _privat("projektek", "pedagogiai_fuzet", "adatok", "pedagogiai_fuzet.json")
    if fuzet:
        d = json.load(open(fuzet, encoding="utf-8"))
        for o in d.get("osztalyok", []):
            for t in o.get("tanevek", []):
                nevek.update(x.get("nev", "") for x in t.get("tanulok", []))
    lista = _privat("memory", "context", "tanulok.md")
    if lista:
        for sor in open(lista, encoding="utf-8"):
            cellak = [c.strip(" *") for c in sor.strip().strip("|").split("|")]
            if len(cellak) >= 4 and cellak[0].isdigit():
                nevek.update([cellak[1], cellak[3]])
    ki = set()
    for n in nevek:
        r = n.split()
        if len(r) >= 2:
            ki.add(" ".join(r))
            ki.add(" ".join(r[1:] + r[:1]))      # fordított sorrend
    return {n for n in ki if len(n) >= 7}, bool(fuzet or lista)


TILTOLISTA = re.compile(r"^\s*TILTOTT\w*\s*=\s*[\[{(]")


def staged():
    """[(útvonal, [új sorok])] a commitba kerülő változásokból."""
    nevek = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
                           cwd=REPO, capture_output=True).stdout.decode("utf-8").split("\0")
    ki = []
    for ut in filter(None, nevek):
        sorok = []
        if ut.lower().endswith(SZOVEG):
            diff = subprocess.run(["git", "diff", "--cached", "-U0", "--", ut], cwd=REPO,
                                  capture_output=True).stdout.decode("utf-8", "ignore")
            sorok = [s[1:] for s in diff.splitlines() if s.startswith("+") and not s.startswith("+++")]
        ki.append((ut, sorok))
    return ki


def ellenoriz(valtozasok):
    nevek, van_nev = tanulonevek()
    hibak = []
    if not van_nev:
        hibak.append("a privát mappa (projektek/, memory/) nem érhető el a repó mellett — "
                     "a tanulónév-ellenőrzés nem futhat")
    nev_minta = re.compile(r"(?<!\w)(" + "|".join(map(re.escape, sorted(nevek, key=len, reverse=True))) + r")(?!\w)") if nevek else None
    for ut, sorok in valtozasok:
        if ut.replace("\\", "/").endswith("_tools/privat_or.py"):
            continue
        if any(fnmatch.fnmatch(ut, m) for m in TILOS_UT):
            hibak.append(f"{ut}: tiltott fájltípus vagy -név (felmérő, tiltólista, docx, xlsx)")
        for i, s in enumerate(sorok, 1):
            if PRIVAT_JEL in s:
                hibak.append(f"{ut}: privát jelölésű tartalom")
            if nev_minta:
                m = nev_minta.search(s)
                if m:
                    hibak.append(f"{ut}: tanulónév az új sorok között („{m.group(1)}”)")
            if ut.endswith(".py") and TILTOLISTA.match(s):
                hibak.append(f"{ut}: tiltólista-definíció a repóban ({s.strip()[:40]}…) — "
                             f"a helye projektek/szvetkomatek/tiltott, betöltés: tiltott.modul()")
    return sorted(set(hibak))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--teszt":
        valtozasok = [(f, open(f, encoding="utf-8", errors="ignore").read().splitlines())
                      for f in sys.argv[2:]]
    else:
        valtozasok = staged()
    hibak = ellenoriz(valtozasok)
    if hibak:
        print("✗ Privát-őr: a commit megállt, mert a publikus repóba privát adat kerülne:", file=sys.stderr)
        for h in hibak:
            print("   • " + h, file=sys.stderr)
        print("Ha biztosan tévedés, egyszeri kivétel: git commit --no-verify", file=sys.stderr)
        return 1
    print(f"✓ Privát-őr: {len(valtozasok)} fájl rendben")
    return 0


if __name__ == "__main__":
    sys.exit(main())
