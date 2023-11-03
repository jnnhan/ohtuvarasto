import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinen_varasto = Varasto(-1, -2)
        self.taysi_varasto = Varasto(3, 5)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_tilavuus_negatiivinen_nollaa_tilavuuden(self):
        self.assertAlmostEqual(self.virheellinen_varasto.tilavuus, 0)

    def test_varaston_alkusaldo_negatiivinen_nollaa_saldon(self):
        self.assertAlmostEqual(self.virheellinen_varasto.saldo, 0)

    def test_varaston_alkusaldo_suurempi_kuin_tilavuus_tasaa_tilanteen(self):
        self.assertAlmostEqual(self.taysi_varasto.saldo, 3)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_enemman_kuin_mahtuu_saldo_sama_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(8)

        # Varastossa tilaa vielä 2, mutta lisätään 3
        self.varasto.lisaa_varastoon(3)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(2)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_otetaan_varastosta_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_paljonko_mahtuu(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")