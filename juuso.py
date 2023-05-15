import random
from typing import Dict, List, Tuple

# Säännöt:
#   - Tehtäväsi on kirjoittaa seuraavat kaksi funktiota siten, että vaatimukset täyttyvät ja testit menevät läpi.
#   - Et saa käyttää internetiä ongelman ratkaisemiseen.
#   - Saat lukea VAIN juuso.py ja tekken_arvonta.py -tiedostoja.
#   - Saat editoida VAIN juuso.py -tiedostoa.
#   - Saat ajaa .odinvenv -ympäristön python -tulkkia komennolla "python"
# Suoritat ohjelman ajamalla tekken_arvonta.py -tiedostoa. Esim. python tekken_arvonta.py -p Juuso Ragnar Leif Thor
# Testit voit ajaa ajamalla odinin_tuomio.py -tiedostoa.

# Osa 1, "Triviaali": Jaa pelaajat satunnaisesti kahteen lohkoon.
#   - 'pelaajat' on lista pelaajista, jotka pitää asettaa lohkoihin.
#   - Pelaajat on asetettava lohkoihin satunnaisesti.
#   - Pelaajat on aseteltava lohkoihin "LOHKO A" ja "LOHKO B" siten, että lohkot ovat yhtä suuret, tai niin lähellä sitä kuin mahdollista.
# Esimerkki funktion outputista:
# lohkot = {
#     "LOHKO A": ["Juuso", "Luukas", "Nosse"],
#     "LOHKO B": ["Piispanen", "Jukka", "Ville", "Ilmari"]
# }

# &é"'(§è!çà)^$µùm:;=<>/.+M%£*¨¨_°³

def jaa_pelaajat_kahteen_lohkoon(pelaajat: List[str]) -> Dict[str, List[str]]:
    random.shuffle(pelaajat)
    print(pelaajat[:int(len(pelaajat)/2)])
    lohkot = {
        "LOHKO A":pelaajat[:int(len(pelaajat)/2)],
        "LOHKO B":pelaajat[int(len(pelaajat)/2):]
    }
    return lohkot


# Osa 2, "No-brainer": Laske otteluparit lohkoille.
#   - 'pelaajat_lohkossa' on lista yhden lohkon pelaajista.
#   - Otteluparit muodostetaan siten, että lohkon jokainen pelaaja pelaa lohkon jokaista muuta pelaajaa vastaan kerran.
# Esimerkki output funktiosta:
# otteluparit = [("Juuso", "Luukas"), ("Juuso", "Nosse"), ("Luukas", "Nosse")]
def laske_otteluparit(pelaajat_lohkossa: List[str]) -> List[Tuple[str]]:
    otteluparit = []
    pelaajat = set(pelaajat_lohkossa)
    try:
        while i := pelaajat.pop():
            for j in pelaajat:
                otteluparit.append((i,j))
    except KeyError:
        pass
    random.shuffle(otteluparit)
    return otteluparit
