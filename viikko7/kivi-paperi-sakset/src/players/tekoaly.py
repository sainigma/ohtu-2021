from players.pelaaja import Pelaaja

class Tekoaly(Pelaaja):
    def __init__(self):
        super().__init__()
        self._siirto = 0
        self._siirrot = {
          0:'k', 1:'p', 2:'s'
        }
        self.prompt = "Tietokone valitsi: "

    def _tulosta_siirto(self, siirto):
        print(f'{self.prompt}{siirto}')
        return siirto

    def hae_siirto(self, prompt):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        valinta = self._siirrot[self._siirto]
        return self._tulosta_siirto(valinta)
