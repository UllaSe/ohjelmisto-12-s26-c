## mod 10 teht 1->

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros 
        self.ylin = ylin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        pass

    def kerros_ylos(self):
        pass

    def kerros_alas(self):
        pass


    

hissi1 = Hissi(1, 12)
hissi2 = Hissi(5, 20)
#print(hissi1.nykyinen_kerros)
#print(hissi2.nykyinen_kerros)
hissi1.siirry_kerrokseen(6)