#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A megoldókulcs-önteszt érzékenységmérője.

A `kulcs_teszt.py` azt mondja meg, hogy a kulcsok jók-e. Ez a szkript arra
válaszol, hogy az önteszt **egyáltalán képes-e** hibát találni: sorra elrontja
az összes várt értéket (egyszerre mindig csak egyet), és megnézi, hogy a
harness elkapja-e. Ami elkapatlan marad, ott a kulcs szövegében véletlenül
szerepel az elrontott érték is — ilyenkor a modulban érdemes több várt értéket
felsorolni, hogy a sorrend megkösse az illesztést.

Futtatás a `_tools` mappából:  python3 kulcs_regresszio.py
"""
import glob
import importlib.util
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kulcs_teszt as KT  # noqa: E402


def ront(v):
    """Az érték típusához illő, biztosan hibás változat."""
    if isinstance(v, bool):
        return not v
    if isinstance(v, set):
        return v ^ {9999}
    if isinstance(v, (int, float, Fraction)):
        return Fraction(v) + 7
    if isinstance(v, str):
        return v + ' ZZQX'
    return v


def main() -> int:
    mappa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kulcsok')
    ossz = elkapva = 0
    for m in sorted(glob.glob(os.path.join(mappa, '*.py'))):
        nev = os.path.basename(m)[:-3]
        spec = importlib.util.spec_from_file_location(nev, m)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        eredeti = {k: list(v) for k, v in mod.TESZT.items()}
        nem = []
        for azon, lista in eredeti.items():
            for i, (betu, _) in enumerate(lista):
                mod.TESZT[azon] = [(b, ront(v) if j == i else v)
                                   for j, (b, v) in enumerate(lista)]
                ossz += 1
                if KT.ellenoriz(mod):
                    elkapva += 1
                else:
                    nem.append(f'{azon} {betu})')
                mod.TESZT[azon] = list(lista)
        print(f'── {nev:28s} {len(eredeti):3d} kártya, elkapatlan: {len(nem)}'
              + (('  → ' + ', '.join(nem)) if nem else ''))
    print(f'\nÉrzékenység: {elkapva}/{ossz} = {100 * elkapva / ossz:.1f}%')
    return 0 if elkapva == ossz else 1


if __name__ == '__main__':
    sys.exit(main())
