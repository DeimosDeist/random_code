class Moebel:
    """
    Möbel object that saves the Price and the discount. Can also return if a discount exists, as well as the discounted price.
    """

    def __init__(self, preis: float, rabatt: float):
        self.__preis = preis
        self.__rabatt = rabatt

    @property
    def preis(self):
        return self.__preis

    @property
    def rabatt(self):
        return self.__rabatt

    def existiert_rabatt(self) -> bool:
        if self.__rabatt > 0:
            return True
        else:
            return False

    def berechne_finalen_preis(self):
        return self.__preis * (1 - self.__rabatt / 100)


class Schrank(Moebel):

    def __init__(self, anzahl_fuesse: int, preis, rabatt):
        super(Schrank, self).__init__(preis, rabatt)
        self.__anzahl_fuesse = anzahl_fuesse
        if anzahl_fuesse <= 0:
            self.ist_haengeschrank = True
        else:
            self.ist_haengeschrank = False


class Stuhl(Moebel):
    counter = 0

    def __init__(self, polster: bool, preis, rabatt):
        super(Stuhl, self).__init__(preis, rabatt)
        self.__polster = polster
        Stuhl.counter += 1

    def get_anzahl_stuehle(self):
        return Stuhl.counter


def get_anzahl_stuehle_global():
    return Stuhl.counter
