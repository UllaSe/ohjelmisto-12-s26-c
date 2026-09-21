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

    def __init__(self, osoite):
        # tässä asossiaatio listan avulla
        self.koirat = []
        self.osoite = osoite

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        # pääsee nyt käsiksi koiran (olion) ominaisuuksiin
        print(koira.nimi + ' kirjattu sisään')
        # hotola pääsee myös kutsumaan koiran metodeja
        # tämäkin on assosiaatio eli hoitola "tuntee" toisen olion 
        koira.hauku(2)


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola("Mäkitie 5")
hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)

koira1.hauku(3)
koira2.hauku(2)
koira2 = koira1 # viittaus ensimmäiseen koiraan poistuu ja kummatkin muuttujaat viittavat samaan olioon
koira2.hauku(1)

# Luodaan kolmas koira ja sijoitetaan se suoraan hoitolaan
hoitola.koira_sisään(Koira("Bella", 2016))

# olion ominaisuuksiin voidaan viitata pythonissa myös suoraan
hoitola.koirat[0].hauku(2)





## Lista on myös olio ja siihen viitataan muuttujilla
"""
def muokkaa_listaa(muokattava_lista):
    muokattava_lista.append(6)

lista = [1,5,8]
print(lista)
muokkaa_listaa(lista)
print(lista)
"""