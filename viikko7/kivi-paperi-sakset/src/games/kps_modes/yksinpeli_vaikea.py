from games.kps import KPS
from players.ihmispelaaja import Ihmispelaaja
from players.parempi_tekoaly import ParempiTekoaly

class YksinpeliVaikea(KPS):
    def __init__(self):
        self.players = [Ihmispelaaja(), ParempiTekoaly()]