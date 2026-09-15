# class Hoitola:
#     def __init__(self, koiralista):
#         # syntyy assosiaatio
#         self.koirat = koiralista

# # Pääohjelma

# koira1 = Koira("Muro", 2018)
# koira2 = Koira("Rekku", 2022, "Viu viu viu")

# koiralista = [koira1, koira2]
# hoitola = Hoitola(koiralista)
# print(hoitola.koirat)
# print(hoitola.koirat[0])
# print(hoitola.koirat[0].nimi)

class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class Hoitola:

    def __init__(self):
        # tässä asossiaatio listan avulla
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        # pääsee nyt käsiksi koiran (olion) ominaisuuksiin
        print(koira.nimi + ' kirjattu sisään')
        # hotola pääsee myös kutsumaan koiran metodeja
        # tämäkin on assosiaatio eli hoitola "tuntee" toisen olion 
        print(koira.hauku(2))


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()
hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)