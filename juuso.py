import random
from typing import Dict, List, Tuple

# Säännöt:
#   - Tehtäväsi on kirjoittaa seuraavat kaksi funktiota siten, että vaatimukset täyttyvät ja testit menevät läpi.
#   - Et saa käyttää internetiä ongelman ratkaisemiseen.
#   - Saat lukea VAIN juuso.py ja tekken_arvonta.py -tiedostoja.
#   - Saat editoida VAIN juuso.py -tiedostoa.
#   - Saat ajaa .odinvenv -ympäristön python -tulkkia komennolla "python"
# Suoritat ohjelman ajamalla tekken_arvonta.py -tiedostoa. Testit voit ajaa ajamalla odinin_tuomio.py -tiedostoa.

# Osa 1, "Triviaali": Jaa pelaajat satunnaisesti kahteen lohkoon.
#   - 'players' on lista pelaajista, jotka pitää asettaa lohkoihin.
#   - Pelaajat on asetettava lohkoihin satunnaisesti.
#   - Pelaajat on aseteltava lohkoihin "Lohko A" ja "Lohko B" siten, että lohkot ovat yhtä suuret, tai niin lähellä sitä kuin mahdollista.
# Esimerkki funktion outputista:
# lohkot = {
#     "Lohko A": ["Juuso", "Luukas", "Nosse"],
#     "Lohko B": ["Piispanen", "Jukka", "Ville", "Ilmari"]
# }
def jaa_pelaajat_kahteen_lohkoon(pelaajat: List[str]) -> Dict[str, List[str]]:
    lohkot = {}
    return lohkot


# Osa 2, "No-brainer": Laske otteluparit lohkoille.
#   - 'players_in_group' on lista yhden lohkon pelaajista.
#   - Otteluparit muodostetaan siten, että lohkon jokainen pelaaja pelaa lohkon jokaista muuta pelaajaa vastaan kerran.
# Esimerkki output funktiosta:
# otteluparit = [("Juuso", "Luukas"), ("Juuso", "Nosse"), ("Luukas", "Nosse")]
def laske_otteluparit(pelaajat_lohkossa: List[str]) -> List[Tuple[str]]:
    otteluparit = []
    return otteluparit
