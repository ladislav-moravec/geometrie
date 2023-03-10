from tvar import Tvar


class Obdelnik(Tvar):

    sirka = 0
    vyska = 0

    def __init__(self, barva, sirka, vyska):
        super(Obdelnik, self).__init__(barva)
        self.sirka = sirka
        self.vyska = vyska

    def obsah(self):
        s = self.sirka * self.vyska
        return s
