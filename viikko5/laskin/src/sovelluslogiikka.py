class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edelliset = [0]

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self, arvo):
        self.aseta_arvo(0)

    def aseta_arvo(self, arvo):
        self.edelliset.append(arvo)
        self.tulos = arvo

    def kumoa(self, arvo):
        print(self.edelliset)
        if self.edellisia():
            self.edelliset.pop()
            self.tulos = self.edelliset[-1]
        else:
            self.edelliset.append(0)
            self.tulos = 0

    def edellisia(self):
        return len(self.edelliset) > 1