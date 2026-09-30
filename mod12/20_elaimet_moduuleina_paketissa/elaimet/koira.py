class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        print(f"{self.nimi} haukkuu: Vuh vuh!")


if __name__ == "__main__":
    koira = Koira("TestiRekku", "Labradorin noutaja")
    koira.hauku()
