import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    # tehdään toteutus saldo-metodille
    def varasto_saldo(self,tuote_id):
        if tuote_id == 1:
            return 10
        elif tuote_id == 2:
            return 2
        elif tuote_id == 3:
            return 0

    # tehdään toteutus hae_tuote-metodille
    def varasto_hae_tuote(self,tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        elif tuote_id == 2:
            return Tuote(2, "mehu", 15)
        elif tuote_id == 3:
            return Tuote(3, "energiajuoma", 10)

    def setUp(self):
        self.pankki_mock = Mock()
        varasto_mock = Mock()
        Viitegeneraattori_mock = Mock()
        Viitegeneraattori_mock.uusi.return_value = 42
        
        varasto_mock.saldo.side_effect = self.varasto_saldo
        varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, Viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_metodia_tilisiirto_kutsutaan_oikealla_viitteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", self.kauppa._kaupan_tili, 5)

    def test_maksu_usean_eri_tuotteen_ostoskorilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", self.kauppa._kaupan_tili, 20)

    def test_maksu_ostoskorilla_johon_lisataan_yksi_loytyva_ja_yksi_loytymaton_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", self.kauppa._kaupan_tili, 5)