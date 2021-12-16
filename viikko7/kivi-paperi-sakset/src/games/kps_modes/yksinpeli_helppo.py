from games.kps import KPS
from players.ihmispelaaja import Ihmispelaaja
from players.tekoaly import Tekoaly

class YksinpeliHelppo(KPS):
    def __init__(self):
        self.players = [Ihmispelaaja(), Tekoaly()]