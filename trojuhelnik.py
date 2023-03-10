from tvar import Tvar


class Trojuhelnik(Tvar):

    a = 0
    b = 0
    c = 0

    def __init__(self, barva, a, b, c):
        super(Trojuhelnik, self).__init__(barva)
        self.a = a
        self.b = b
        self.c = c

    def obsah(self):
        # heronuv vzorec
        s: float = (self.a + self.b + self.c) / 2
        S: float = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** (1/2)
        return S
