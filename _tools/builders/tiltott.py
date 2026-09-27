# -*- coding: utf-8 -*-
"""Tiltott (felmérő-) adatok betöltése a repón KÍVÜLRŐL.

A felmérők adatai nem kerülhetnek a publikus repóba (és így a GitHub Pages-re sem). A builderek tiltott-listái
ezért a Claude-gyökér `projektek/szvetkomatek/tiltott/` mappájában élnek (`tiltott_<osztály>_<NN>.py`), és ez a
modul tölti be őket. Keresési sorrend:
  1. a SZVETKO_TILTOTT környezeti változó (mappa; a "0" érték kikapcsolja a betöltést),
  2. <repó>/../projektek/szvetkomatek/tiltott  (a helyi klón és a Cowork-mount),
  3. /sessions/*/mnt/Claude/projektek/szvetkomatek/tiltott, majd a Windows-útvonal.
Ha a mappa nem érhető el (pl. felhős Claude Code munkamenetben, ahol csak a repó van meg), a builder figyelmeztetéssel
fut tovább, a felmérő-ütközés ellenőrzése nélkül — ilyenkor a kész oldalt a tiltott-lista birtokában újra kell építeni,
mielőtt kikerül."""
import glob
import importlib.util
import os
import sys

_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
_JELOLTEK = [os.path.join(_REPO, "..", "projektek", "szvetkomatek", "tiltott"),
             *glob.glob("/sessions/*/mnt/Claude/projektek/szvetkomatek/tiltott"),
             r"C:\Users\nagyg\OneDrive\Dokumentumok\Oktatás\Claude\projektek\szvetkomatek\tiltott"]
_szolt = set()


def mappa():
    kornyezet = os.environ.get("SZVETKO_TILTOTT")
    if kornyezet == "0":
        return None
    for j in ([kornyezet] if kornyezet else []) + _JELOLTEK:
        if j and os.path.isdir(j):
            return os.path.abspath(j)
    return None


def _figyelmeztet(nev):
    if nev not in _szolt:
        _szolt.add(nev)
        print(f"⚠ A tiltott-lista ({nev}) nem érhető el — a felmérő-ütközés ellenőrzése kimarad. "
              f"Kikerülés előtt építsd újra ott, ahol a projektek/szvetkomatek/tiltott mappa megvan.", file=sys.stderr)


class _Ures:
    """Hiányzó tiltott-modul helyett: az ellenőrzés üres eredményt ad."""

    def ellenoriz(self, *args, **kwargs):
        return []


def modul(nev):
    """A `nev` (pl. "tiltott_4e_04") privát modul — vagy egy üres helyettesítő, ha nem érhető el."""
    m = mappa()
    ut = os.path.join(m, nev + ".py") if m else None
    if not ut or not os.path.isfile(ut):
        _figyelmeztet(nev)
        return _Ures()
    spec = importlib.util.spec_from_file_location(nev, ut)
    mod = importlib.util.module_from_spec(spec)
    regi, sys.dont_write_bytecode = sys.dont_write_bytecode, True      # ne keletkezzen __pycache__ a privát mappában
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = regi
    return mod


def lista(nev, valtozo):
    """A `nev` modul `valtozo` listája — vagy üres lista, ha a modul nem érhető el."""
    mod = modul(nev)
    return list(getattr(mod, valtozo, []))
