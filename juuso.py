import random
from typing import Dict, List, Tuple

# Osa 1: Jaa pelaajat satunnaisesti kahteen lohkoon.
#   - 'players' on lista pelaajista, jotka pitää asettaa lohkoihin.
#   - Pelaajat on asetettava lohkoihin satunnaisesti.
#   - Mikäli pelaajia on parillinen määrä, molemmat lohkot "Lohko A" ja "Lohko B" sisältävät yhtä monta pelaajaa.
#   - Mikäli pelaajia on pariton määrä, toisessa lohkossa on 1 pelaaja enemmän kuin toisessa.
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


# Osa 2: Laske otteluparit lohkoille.
#   - 'players_in_group' on yhden lohkon pelaajista.
#   - Otteluparit muodostetaan siten, että lohkon jokainen pelaaja pelaa lohkon jokaista muuta pelaajaa vastaan.
#   - Paluusanoman on oltava lista ottelupareista (tuple).
#       - Esimerkiksi: [("Ville", "Juuso"), ("Juuso", "Ilmari"), ("Ville, "Ilmari")]
def laske_otteluparit(players_in_group: List[str]) -> List[Tuple[str]]:
    matches = [(a, b) for idx, a in enumerate(players_in_group) for b in players_in_group[idx + 1:]]
    return matches
