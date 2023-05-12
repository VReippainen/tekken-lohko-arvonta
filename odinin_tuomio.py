import time
import unittest
from pygame import mixer
from juuso import jaa_pelaajat_kahteen_lohkoon, laske_otteluparit

def stopTestRun(run):
    failures = run.failures
    if len(failures) > 0:
        print(
            """                                                                                
                                                                                
             @@                                      @@@@           @@@,        
           @@@@@@                                    @@@@           @@@         
        @@@@    @@@@       @@@                @@     /@@%           @@@         
     ,@@@&        .@@@     @@@@@@.         @@@@@      @@(     %@@   @@@         
     @@@@          @@@@    @@@ @@@@@(   @@@&  @@      @@(      @@@@@@@@         
       *@@@@    .@@@.      @@@    /@@@@@*     @@     /@@(          @@@@         
          @@@@@@@@         @@@   %@@@ @@@@@   @@*    /@@@           @@@@@@@     
           %@@@@@*         @@@@@@@       @@@@@@@*    &@@@           @@@  @@@@   
         @@@@  @@@@@       @@@@             ,@@@*    @@@@           @@@         
      @@@@@      ,@@@@@    @                    @    @@@@           @@@         
      @@@           @@.                              @@@@           @@@,        
                                                                                
                                                                                """
        )
        print("Juuso, olet pettänyt odotukseni! Ota rangaistuksesi, kulauta juomasi ja palaa koodin ääreen viisaampana!")
        mixer.init()
        mixer.music.load("valhalla/runtu.mp3")
        mixer.music.play()
        time.sleep(18)

    elif len(failures) == 0:
        print(
            """                                                                                
                                                                                
             @@                                      @@@@           @@@,        
           @@@@@@                                    @@@@           @@@         
        @@@@    @@@@       @@@                @@     /@@%           @@@         
     ,@@@&        .@@@     @@@@@@.         @@@@@      @@(     %@@   @@@         
     @@@@          @@@@    @@@ @@@@@(   @@@&  @@      @@(      @@@@@@@@         
       *@@@@    .@@@.      @@@    /@@@@@*     @@     /@@(          @@@@         
          @@@@@@@@         @@@   %@@@ @@@@@   @@*    /@@@           @@@@@@@     
           %@@@@@*         @@@@@@@       @@@@@@@*    &@@@           @@@  @@@@   
         @@@@  @@@@@       @@@@             ,@@@*    @@@@           @@@         
      @@@@@      ,@@@@@    @                    @    @@@@           @@@         
      @@@           @@.                              @@@@           @@@,        
                                                                                
                                                                                """
        )
        print("Juuso, olet osoittanut viisauttasi ja taitoasi, joka on vertaistaan vailla. Olet ansainnut paikkasi Valhallassa, sankarien salissa. Tervetuloa, rohkea viikinki!")
        mixer.init()
        mixer.music.load("valhalla/valhalla.mp3")
        mixer.music.play()
        time.sleep(21)


class TestSplitToTwoRandomGroups(unittest.TestCase):
    current_result = None

    def run(self, result=None):
        self.current_result = result
        unittest.TestCase.run(self, result)

    def test_group_structure(self):
        groups = jaa_pelaajat_kahteen_lohkoon(["jees", "joos", "jaas", "juuso"])
        self.assertIsInstance(groups, dict)
        self.assertTrue("Lohko A" in groups)
        self.assertTrue("Lohko B" in groups)
        self.assertIsInstance(groups["Lohko A"], list)
        self.assertIsInstance(groups["Lohko B"], list)

    def test_split_counts_even(self):
        player_names = [str(x) for x in range(1000)]
        groups = jaa_pelaajat_kahteen_lohkoon(player_names)
        self.assertEqual(len(groups["Lohko A"]), len(groups["Lohko B"]))

    def test_split_counts_odd(self):
        player_names = [str(x) for x in range(999)]
        groups = jaa_pelaajat_kahteen_lohkoon(player_names)
        self.assertEqual(abs(len(groups["Lohko A"]) - len(groups["Lohko B"])), 1)

    def test_empty_list(self):
        self.assertEqual(laske_otteluparit([]), [])

    def test_single_player(self):
        self.assertEqual(laske_otteluparit(['Juuso']), [])

    def test_two_players(self):
        self.assertEqual(laske_otteluparit(['Juuso', 'Ville']), [('Juuso', 'Ville')])

    def test_three_players(self):
        self.assertEqual(laske_otteluparit(['Juuso', 'Ville', 'Luke']), [('Juuso', 'Ville'), ('Juuso', 'Luke'), ('Ville', 'Luke')])

    def test_four_players(self):
        self.assertEqual(laske_otteluparit(['Juuso', 'Ville', 'Luke', 'Piispanen']), [('Juuso', 'Ville'), ('Juuso', 'Luke'), ('Juuso', 'Piispanen'), ('Ville', 'Luke'), ('Ville', 'Piispanen'), ('Luke', 'Piispanen')])



if __name__ == '__main__':
    setattr(unittest.TestResult, 'stopTestRun', stopTestRun)
    unittest.main()
