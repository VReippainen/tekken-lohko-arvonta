import unittest
from juuso import jaa_pelaajat_kahteen_lohkoon
from valhalla.odin import anna_runtua

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


class TestSplitToTwoRandomGroups(unittest.TestCase):
    current_result = None

    def tearDown(self):
        if len(self.current_result.failures) > 0:
            anna_runtua(5)

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



if __name__ == '__main__':
    setattr(unittest.TestResult, 'stopTestRun', stopTestRun)
    unittest.main()
