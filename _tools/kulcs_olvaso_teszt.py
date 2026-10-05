# -*- coding: utf-8 -*-
"""A kulcsolvasó elkülöníti az adattáblát és a Végeredményt. Csak szerkezeti minta."""
import pathlib
import tempfile
import unittest

from kulcs_teszt import vegeredmenyek


class KulcsOlvasoTeszt(unittest.TestCase):
    def olvas(self, belso):
        with tempfile.TemporaryDirectory() as mappa:
            ut = pathlib.Path(mappa) / 'minta.html'
            ut.write_text('<article class="feladat alap" id="alap-1">' + belso + '</article>', encoding='utf-8')
            return vegeredmenyek(str(ut))

    def test_eredeti_szerkezet(self):
        self.assertEqual(self.olvas('<details class="vegeredmeny"><summary>Végeredmény</summary>'
                                   '<div class="bel">Válasz.</div></details>'), {'alap-1': 'Válasz.'})

    def test_adattabla_elotte_es_utanna(self):
        adat = '<details class="abra-adatok"><summary>Adatok</summary><div class="bel">Adat.</div></details>'
        kulcs = '<details class="vegeredmeny"><summary>Végeredmény</summary><div class="bel">Válasz.</div></details>'
        self.assertEqual(self.olvas(adat + kulcs + adat), {'alap-1': 'Válasz.'})

    def test_tobb_osztaly_es_idezojel(self):
        self.assertEqual(self.olvas("<details open class='egyeb vegeredmeny masik'><summary>Végeredmény</summary>"
                                   '<div class="bel">Válasz.</div></details>'), {'alap-1': 'Válasz.'})

    def test_hasonlo_osztalynev_nem_kulcs(self):
        self.assertEqual(self.olvas('<details class="nem-vegeredmeny"><summary>Adatok</summary>Adat.</details>'), {})

    def test_hianyzo_kulcsot_nem_potol_adat(self):
        self.assertEqual(self.olvas('<details class="abra-adatok"><summary>Adatok</summary>Adat.</details>'), {})


if __name__ == '__main__':
    unittest.main()
