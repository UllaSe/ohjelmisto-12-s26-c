
k1_rotu = 'Mastiffi'
k1_nimi = 'Wuffe'
k1_syntymävuosi = 2022

k2_rotu = 'Bokseri'
k2_nimi = 'Lissu'
k2_syntymävuosi = 2025

k3_rotu = 'Labradori'
k3_nimi = 'Sisu'
k3_syntymävuosi = 2020

'''
class Koira:
        pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö

koira = Koira()
koira2 = Koira()

koira.nimi = "Wuffe"
koira.rotu = "Mastiffi"

koira2.nimi = "Lissu"
koira2.rotu = "Bokseri"

print('Ensimmäisen koiran nimi:', koira.nimi)
print('Ensimmäisen koiran rotu:', koira.rotu)

print('Toisen koiran nimi:', koira2.nimi)
print('TOoisen koiran rotu:', koira2.rotu)

'''

# teimme juuri luokan Koira ilman ominaisuuksia
# tämän jälkeen määrittelimme ominaisuudet yksi kerrallaa == työlästä!!!!

# Näin teemme oikeasti:
# Oliossa määritellään ns. tieto ja toiminta

# Koira:

# Koiran ominaisuudet
# - nimi
# - rotu
# - syntymävuosi

# Koiran toiminnot
# - Hauku
# - Syö
# - Nuku

class Koira:

    # Luokkamuuttuja
    tehty = 0
    
    def __init__(self, nimi, rotu, syntymävuosi, haukahdus='Viuviu'):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = 'nisäkäs'
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f'{self.nimi} tervehtii sinua')
        for i in range(kerrat):
            print(self.haukahdus)


koira = Koira("Lissu", "Bokseri", 2022, "Hau Hau")
koira2 = Koira("Wuffe", "Mastiffi", 2025, "Woof Woof")
koira3 = Koira("Fifi", "Puudeli", 2015)

print(f"Koiria on nyt {Koira.tehty}.")

koira.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(1)


print(f'1. koiran nimi on {koira.nimi} ja rotu {koira.rotu}, vuosi {koira.syntymävuosi}')
print(f'2. koiran nimi on {koira2.nimi} ja rotu {koira2.rotu}')

# print(koira) - viittaus olioon, ei muuttuja

# players = [
#     {
#         "name": "Player 1",
#         "skill_level": 10,
#         "inventory": {"map", "knife"}
#     },
#     {
#         "name": "Player 2",
#         "skill_level": 20,
#         "inventory": {"axe"}
#     }
# ]

# for player in players:
#     print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
#     for item in player["inventory"]:
#         print(f"- {item}")

### Miten tämä edellinen voitaisiin kuvata luokkana
### Esim. PELAAJA

