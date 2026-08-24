import math
import random


# tehtävä 1

nimi = input('Anna nimesi: ')
print(f'Terve, {nimi}!')

# tehtävä 2

r = float(input('Anna säde niin lasken ympyrän pinta-alan: '))
# r = float(r)
# ympyrän pinta-ala: A = pi * r^2
A = math.pi * r ** 2
print(f'Ympyrän pinta-ala on {A:.2f} yksikköä')


# tehtävä 3

a = float(input('Anna suorakulmion kanta: '))
b = float(input('Anna suorakulmion korkeus: '))

p = 2 * (a + b)
# p2 = 2 * a + 2 * b
A = a * b

print(f'Suorakulmion piiri on: {p:.2f} ja pinta-ala {A:.2f}')
print(f'Suorakulmion piiri on: {p:.2f} ja pinta-ala {(a*b):.2f}')

# tehtävä 6

luku = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)
print(f'{luku} {luku2} {luku3}')
print(f'{random.randint(0,9)} {random.randint(0,9)} {random.randint(0,9)}')