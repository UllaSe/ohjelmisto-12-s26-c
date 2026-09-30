# Tämä on ohjelmamme käyttämä keskeinen objektityyppi
# Katso: "domain-olio" (domain object)

class Kirja:
    def __init__(self, nimi, kirjoittaja):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi} - {self.kirjoittaja}")
