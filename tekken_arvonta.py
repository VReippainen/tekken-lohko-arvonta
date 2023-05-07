import argparse
import json
import juuso
from utils.runtu import JuusoException


def tekken_arvonta(players):
    groups = juuso.jaa_pelaajat_kahteen_lohkoon(players)
    print(json.dumps(groups, indent=4))

    for group in groups:
        matches = juuso.laske_otteluparit(groups[group])
        print(f"{group}")
        for match in matches:
            print(f"\t{match[0]} vs. {match[1]}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--players', nargs='+', required=True)
    players_arg = parser.parse_args().players
    unique_players = list(set(players_arg))
    if len(unique_players) < 4:
        raise JuusoException("Unohditko antaa pelaajat? Tarvitaan vähintään 4 uniikkia pelaajaa.")
    tekken_arvonta(players_arg)
