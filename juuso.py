import random
from typing import Dict, List, Tuple

# Osa 1, "Triviaali": Jaa pelaajat satunnaisesti kahteen lohkoon.
#   - 'players' on lista pelaajista, jotka pitää asettaa lohkoihin.
#   - Pelaajat on asetettava lohkoihin satunnaisesti.
#   - Pelaajat on aseteltava lohkoihin "Lohko A" ja "Lohko B" siten, että lohkot ovat yhtä suuret, tai niin lähellä sitä kuin mahdollista.
# Esimerkki funktion outputista:
# groups = {
#     "Lohko A": ["Juuso", "Luukas", "Nosse"],
#     "Lohko B": ["Piispanen", "Jukka", "Ville", "Ilmari"]
# }

def jaa_pelaajat_kahteen_lohkoon(players: List[str]) -> Dict[str, List[str]]:
    team_1_size = int(len(players) / 2)
    team_1_set = set(random.sample(players, team_1_size))
    team_2_set = set(players) - team_1_set
    team_1 = list(team_1_set)
    team_2 = list(team_2_set)
    groups = {
        "Lohko A": team_1,
        "Lohko B": team_2
    }
    return groups


# Osa 2, "No-brainer": Laske otteluparit lohkoille.
#   - 'players_in_group' on lista yhden lohkon pelaajista.
#   - Otteluparit muodostetaan siten, että lohkon jokainen pelaaja pelaa lohkon jokaista muuta pelaajaa vastaan kerran.
# Esimerkki output funktiosta:
# matches = [("Juuso", "Luukas"), ("Juuso", "Nosse"), ("Luukas", "Nosse")]
def laske_otteluparit(players_in_group: List[str]) -> List[Tuple[str]]:
    matches = [(a, b) for idx, a in enumerate(players_in_group) for b in players_in_group[idx + 1:]]
    return matches
