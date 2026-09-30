# Tämä luokka riippuu luokasta Kirja

class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []

    def lisaa_kirja(self, kirja):
        self.kirjat.append(kirja)

    def tulosta_kirjat(self):
        if len(self.kirjat) == 0:
            print("Tässä kirjastossa ei ole tällä hetkellä lainattavia kirjoja.")
        else:
            print(f"Kirjaston {self.nimi} kirjat:")
            for numero in range(len(self.kirjat)):
                kirja = self.kirjat[numero]
                print(f"{numero + 1}. {kirja.nimi} - {kirja.kirjoittaja}")
