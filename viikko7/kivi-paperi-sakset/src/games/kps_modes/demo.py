import time
from games.kps import KPS
from players.parempi_tekoaly import ParempiTekoaly

class Demo(KPS):
    def __init__(self):
        sekunnit = int(time.time() % 60)
        self.players = [ParempiTekoaly(60 - sekunnit + 1), ParempiTekoaly(sekunnit + 1)]
        self.kierroksia = 0
    
    def _onko_ok_siirto(self, siirto):
        time.sleep(0.017)
        self.kierroksia += 0.5
        if self.kierroksia >= 100:
            return False
        return siirto in ['k','p','s']