# Tuntiesimerkkejä moduulin 4

import random

## kolikonheittosimulaattori
random_number = random.randint(0,1)
print(random_number)

# if lauseen _ehto_ muodostuu AINA True tai False arvoksi
if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")

if random_number == 1:
    result = "klaava"
        
print(f"Heitit kolikkoa ja sait {result}n.")

# boolean
onko_totta = False
if onko_totta:
    print("Onhan se totta!")

