# Tämä luokka sisältää staattisia apufuktioita

class Apufunktioluokka:
    @staticmethod
    def tulosta_valikko():
        print()
        print("Mitä haluat tehdä?")
        print("1. Näytä nykyinen kirjasto")
        print("2. Näytä nykyisen kirjaston kirjat")
        print("3. Siirry toiseen kirjastoon")
        print("4. Lainaa kirja")
        print("5. Näytä lainaamani kirjat")
        print("6. Näytä kaikki kirjastot")
        print("7. Näytä ohje")
        print("0. Lopeta")


    @staticmethod
    def tulosta_kirjastot(kirjastot):
        print("Kirjastot:")
        for numero in range(len(kirjastot)):
            kirjasto = kirjastot[numero]
            print(f"{numero + 1}. {kirjasto.nimi}")


    @staticmethod
    def valitse_kirjasto(kirjastot):
        Apufunktioluokka.tulosta_kirjastot(kirjastot)
        valinta = input("Anna kirjaston numero: ")

        if valinta.isdigit():
            numero = int(valinta)

            if numero >= 1 and numero <= len(kirjastot):
                return kirjastot[numero - 1]

        print("Virheellinen valinta.")
        return None

    @staticmethod
    def valitse_kirja(kirjasto):
        if len(kirjasto.kirjat) == 0:
            print("Tässä kirjastossa ei ole lainattavia kirjoja.")
            return None

        kirjasto.tulosta_kirjat()
        valinta = input("Anna lainattavan kirjan numero: ")

        if valinta.isdigit():
            numero = int(valinta)

            if numero >= 1 and numero <= len(kirjasto.kirjat):
                return kirjasto.kirjat[numero - 1]

        print("Virheellinen valinta.")
        return None
