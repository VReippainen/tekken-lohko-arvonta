import random
from typing import Dict, List, Tuple

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
    tiimi_1_koko = int(len(pelaajat) / 2)
    tiimi_1_set = set(random.sample(pelaajat, tiimi_1_koko))
    tiimi_2_set = set(pelaajat) - tiimi_1_set
    tiimi_1 = list(tiimi_1_set)
    tiimi_2 = list(tiimi_2_set)
    lohkot = {
        "Lohko A": tiimi_1,
        "Lohko B": tiimi_2
    }
    return lohkot


# Osa 2, "No-brainer": Laske otteluparit lohkoille.
#   - 'players_in_group' on lista yhden lohkon pelaajista.
#   - Otteluparit muodostetaan siten, että lohkon jokainen pelaaja pelaa lohkon jokaista muuta pelaajaa vastaan kerran.
# Esimerkki output funktiosta:
# otteluparit = [("Juuso", "Luukas"), ("Juuso", "Nosse"), ("Luukas", "Nosse")]
def laske_otteluparit(pelaajat_lohkossa: List[str]) -> List[Tuple[str]]:
    otteluparit = [(pelaaja_a, pelaaja_b) for indeksi, pelaaja_a in enumerate(pelaajat_lohkossa) for pelaaja_b in pelaajat_lohkossa[indeksi + 1:]]
    return otteluparit
