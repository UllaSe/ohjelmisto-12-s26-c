class Pelaaja:
    def __init__(self, nimimerkki, palvelin):
        self.nimimerkki = nimimerkki
        self.palvelin = palvelin

    def viestittele(self, viesti):
        print(f"[{self.nimimerkki}-{self.palvelin}]: {viesti}")
