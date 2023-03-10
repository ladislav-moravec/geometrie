from trojuhelnik import Trojuhelnik
from obdelnik import Obdelnik

obdelnik = Obdelnik("hnědá", 3, 26)
trojuhelnik = Trojuhelnik("zelená", 25, 15, 15)
obsah_stromu = obdelnik.obsah() + trojuhelnik.obsah() * 4
print("Obsah stromu je {} cm^2".format(obsah_stromu))
