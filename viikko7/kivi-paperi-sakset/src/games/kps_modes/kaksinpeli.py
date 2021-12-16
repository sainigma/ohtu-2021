from games.kps import KPS
from players.ihmispelaaja import Ihmispelaaja

class Kaksinpeli(KPS):
    def __init__(self):
        self.players = [Ihmispelaaja(), Ihmispelaaja()]