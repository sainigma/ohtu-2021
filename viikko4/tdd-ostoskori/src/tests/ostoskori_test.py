import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_tuotteen_lisaamisen_jalkeen_ostoskorilla_sama_hinta_kuin_tuotteella(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.assertEqual(self.kori.hinta(), 7)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(),"Maito")
        self.assertEqual(ostos.hinta(), 3)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_ostosta_joilla_sama_nimi_kuin_tuotteilla(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

        ostokset_nimet = map(lambda x: x.tuotteen_nimi(), ostokset)
        self.assertTrue("Maito" in ostokset_nimet)
        self.assertTrue("Mehu" in ostokset_nimet)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_jos_toinen_poistetaan_koriin_jaa_ostos_jossa_on_yksi_tuote(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kori_tyhjenee_jos_tuotteita_on_poiston_jalkeen_nolla(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()),0)