from peli import Pelaaja

pelaaja1 = Pelaaja(nimimerkki="Glizler", palvelin="Spineshatter")
pelaaja2 = Pelaaja(nimimerkki="DrGlue", palvelin="Spineshatter")

pelaaja1.viestittele("Mis mennää?")
pelaaja2.viestittele("Kuudes pulli Illidanis meneillää :skull:")
