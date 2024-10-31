import unittest
from varasto import Varasto
sepra

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

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
    
    def test_virheellinen_t_nollataan(self):
        self.varasto = Varasto(-5)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
     
    def test_virheellinen_s_nollataan(self):
        self.varasto = Varasto(10, -7)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_virheellinen_lisays(self):
        self.varasto.lisaa_varastoon(-4)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_virheellinen_otto(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.ota_varastosta(-4), 0)
    
    def test_liian_suuri_otto(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_tulostus(self):
        teksti = f"saldo = {0}, vielä tilaa {10}"
        self.assertEqual(str(self.varasto), teksti)