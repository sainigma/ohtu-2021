KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.ljono = []

    @staticmethod
    def alusta_listalla(ljono):
        x = IntJoukko()
        x.ljono = ljono
        return x

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        self.ljono.append(n)
        return True

    def poista(self, n):
        if n not in self.ljono:
            return False
        self.ljono.remove(n)
        return True

    def kopioi_taulukko(self, a, b):
        b = a

    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        return self.ljono

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko.alusta_listalla(a.to_int_list())
        b_taulu = b.to_int_list()

        for i in range(0,len(b_taulu)):
            x.lisaa(b_taulu[i])
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        for item in b.to_int_list():
            if item in a_taulu:
                y.lisaa(item)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko.alusta_listalla(a.to_int_list())
        b_taulu = b.to_int_list()

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    def __str__(self):
        tuotos = f'{self.ljono}'[1:-1]
        return f'{"{"}{tuotos}{"}"}'
