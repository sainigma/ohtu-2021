from tuomari import Tuomari

class KPS:
    def __init__(self):
        self.players = []

    def pelaa(self):
        tuomari = Tuomari()
        prompts = ["Ensimmäisen pelaajan siirto: ", "Toisen pelaajan siirto: "]

        ok = True
        while ok:
            siirrot = []
            for i, player in enumerate(self.players):
                siirto = player.hae_siirto(prompts[i])
                siirrot.append(siirto)
                if not self._onko_ok_siirto(siirto):
                    ok = False
                    break
                elif i == 1:
                    tuomari.kirjaa_siirto(siirrot[0], siirrot[1])
                    self.players[0].aseta_siirto(siirrot[1])
                    self.players[1].aseta_siirto(siirrot[0])
            if ok:
                print(tuomari)
        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ['k','p','s']