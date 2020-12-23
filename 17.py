
class Medium:
    def __init__(self, titel: str, prijs: float):
        self.titel = titel
        self.prijs = prijs

    def __str__(self):
        return '"{}", {:.2f}'.format(self.titel, self.prijs)

class Boek(Medium):
    def __init__(self, auteur: str, paginas: int, **kwargs):
        super().__init__(**kwargs)
        self.auteur = auteur
        self.paginas = paginas

    def __str__(self):
        return '{}, {}, {}'.format(super().__str__(), self.auteur, self.paginas)

class Strip(Boek):
    def __init__(self, tekenaar: str, **kwargs):
        super().__init__(**kwargs)
        self.tekenaar = tekenaar
    
    def __str__(self):
        return '{}, {}'.format(super().__str__(), self.tekenaar)

class Dvd(Medium):
    def __init__(self, regisseur: str, minleeftijd: int, **kwargs):
        super().__init__(**kwargs)
        self.regisseur = regisseur
        self.minleeftijd = minleeftijd

    def __str__(self):
        return '{}, {}, {}'.format(super().__str__(), self.regisseur, self.minleeftijd)

b = Strip(tekenaar="Trish", auteur="Jesse", paginas=512, titel="Mijn boek", prijs=120.0)
a = str(b)
a

film = Dvd(titel="2001, a space odyssey", prijs=17.50, regisseur="Stanley Kubrik", minleeftijd=12)
f = str(film)