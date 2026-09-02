# Tuntiesimerkkejä mod 6 - 2.9.
import random

# arvotaan satunnainen piste välillä -1,-1 ja 1,1
x = random.uniform(-1,1)
y = random.uniform(-1,1)

piste = [x, y]

print(piste)

# tulostetaan vain ensimmäisen alkion arvo (x)
print(piste[0])

# esimerkki materiaalista

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)

listan_koko = len(nimet)
print(listan_koko)

# listan arvojen tulostaminen yksittäin while-silmukalla
counter = 0
while counter < len(nimet):
    print(f"{counter+1}. nimi: {nimet[counter]}")
    counter += 1
