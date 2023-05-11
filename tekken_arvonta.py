import argparse
import json
import juuso
from valhalla.odin import Runtu


def tekken_arvonta(pelaajat):
    lohkot = juuso.jaa_pelaajat_kahteen_lohkoon(pelaajat)
    print("\n")
    print("############################")
    print("Osa 1, \"Triviaali\": Jaa pelaajat satunnaisesti kahteen lohkoon.")
    print("Lohkot ovat seuraavanlaiset:")
    print("----------------------------")
    print(json.dumps(lohkot, indent=4))
    print("----------------------------")
    print("############################")
    print("\n")


    print("############################")
    print("Osa 2, \"No-brainer\": Laske otteluparit lohkoille.")
    print("Otteluparit ovat seuraavanlaiset:")
    print("----------------------------")
    for lohko in lohkot:
        otteluparit = juuso.laske_otteluparit(lohkot[lohko])
        print(f"{lohko}:")
        for ottelu in otteluparit:
            print(f"\t{ottelu[0]} vs. {ottelu[1]}")
    print("----------------------------")
    print("############################")
    print("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pelaajat', nargs='+', required=True)
    pelaajat_arg = parser.parse_args().pelaajat
    uniikit_pelaajat = list(set(pelaajat_arg))
    if len(uniikit_pelaajat) < 4:
        raise Runtu("Tarvitaan vähintään 4 uniikkia pelaajaa.")
    tekken_arvonta(pelaajat_arg)
