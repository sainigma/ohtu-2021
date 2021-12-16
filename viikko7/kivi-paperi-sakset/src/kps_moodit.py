from games.kps_modes.kaksinpeli import Kaksinpeli
from games.kps_modes.yksinpeli_helppo import YksinpeliHelppo
from games.kps_modes.yksinpeli_vaikea import YksinpeliVaikea
from games.kps_modes.demo import Demo

def hae_moodi(moodi):
    if moodi == 'a':
        return Kaksinpeli()
    if moodi == 'b':
        return YksinpeliHelppo()
    if moodi == 'c':
        return YksinpeliVaikea()
    if moodi == 'd':
        return Demo()
    return None