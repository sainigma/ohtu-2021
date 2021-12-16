from players.pelaaja import Pelaaja

class Ihmispelaaja(Pelaaja):
    def __init__(self):
        super().__init__()

    def hae_siirto(self, prompt):
        return input(prompt)