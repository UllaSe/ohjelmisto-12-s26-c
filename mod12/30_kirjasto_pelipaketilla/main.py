# Tämä on ohjelman päätiedosto

from kirjasto import Kirja, Kirjasto, Lukija, Apufunktioluokka

# Luodaan kirjat
kirja1 = Kirja("Muumipappa ja meri", "Tove Jansson")
kirja2 = Kirja("Seitsemän veljestä", "Aleksis Kivi")
kirja3 = Kirja("Tuntematon sotilas", "Väinö Linna")
kirja4 = Kirja("Sinuhe egyptiläinen", "Mika Waltari")
kirja5 = Kirja("Muumipeikko ja Pyrstötähti", "Tove Jansson")

# Luodaan kirjastot
keskustakirjasto = Kirjasto("Keskustakirjasto")
kampuskirjasto = Kirjasto("Kampuskirjasto")
lahikirjasto = Kirjasto("Lähikirjasto")

# Lisätään kirjoja kirjastoihin
keskustakirjasto.lisaa_kirja(kirja1)
keskustakirjasto.lisaa_kirja(kirja2)
kampuskirjasto.lisaa_kirja(kirja3)
kampuskirjasto.lisaa_kirja(kirja4)
lahikirjasto.lisaa_kirja(kirja5)

kirjastot = [keskustakirjasto, kampuskirjasto, lahikirjasto]

print("Tervetuloa kirjastosimulaattoriin!")
nimi = input("Anna lukijan nimi kirjastokorttia varten: ")

lukija = Lukija(nimi, keskustakirjasto)

print(f"Hei {lukija.nimi}!")
print(f"Aloitat kirjastosta: {lukija.sijainti.nimi}")

jatketaan = True

while jatketaan:
    Apufunktioluokka.tulosta_valikko()
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        print(f"Olet nyt kirjastossa: {lukija.sijainti.nimi}")

    elif valinta == "2":
        lukija.sijainti.tulosta_kirjat()

    elif valinta == "3":
        uusi_kirjasto = Apufunktioluokka.valitse_kirjasto(kirjastot)

        if uusi_kirjasto is not None:
            lukija.siirry(uusi_kirjasto)

    elif valinta == "4":
        kirja = Apufunktioluokka.valitse_kirja(lukija.sijainti)

        if kirja is not None:
            lukija.lainaa_kirja(kirja)

    elif valinta == "5":
        lukija.tulosta_lainatut_kirjat()

    elif valinta == "6":
        Apufunktioluokka.tulosta_kirjastot(kirjastot)

    elif valinta == "7":
        print("Voit siirtyä kirjastosta toiseen ja lainata")
        print("siellä olevia kirjoja. Lainattu kirja poistuu")
        print("kirjaston hyllystä ja siirtyy omiin lainoihisi.")

    elif valinta == "0":
        jatketaan = False

    else:
        print("Tuntematon valinta.")

print()
print("Kiitos osallistumiesta kirjastokierrokseen!")
print("Lopulliset lainasi:")
lukija.tulosta_lainatut_kirjat()
