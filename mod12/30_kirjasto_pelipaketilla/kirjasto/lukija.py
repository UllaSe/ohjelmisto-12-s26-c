# Tämä luokka riippuu luokista Kirja ja Kirjasto

class Lukija:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.lainatut_kirjat = []

    def siirry(self, kirjasto):
        self.sijainti = kirjasto
        print(f"Siirryit kirjastoon: {kirjasto.nimi}")

    def lainaa_kirja(self, kirja):
        self.lainatut_kirjat.append(kirja)
        self.sijainti.kirjat.remove(kirja)
        print(f"Lainasit kirjan: {kirja.nimi}")

    def tulosta_lainatut_kirjat(self):
        if len(self.lainatut_kirjat) == 0:
            print("Sinulla ei ole vielä lainattuja kirjoja.")
        else:
            print("Lainaamasi kirjat:")
            for kirja in self.lainatut_kirjat:
                print(f"- {kirja.nimi} - {kirja.kirjoittaja}")
