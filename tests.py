import unittest
from juuso import jaa_pelaajat_kahteen_lohkoon
from utils.runtu import play_runtu_beeps


class TestSplitToTwoRandomGroups(unittest.TestCase):
    current_result = None

    def tearDown(self):
        failures = self.current_result.failures
        if len(failures) > 0:
            play_runtu_beeps(1)

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
        self.assertEqual(1, 2)

    def test_split_counts_even(self):
        player_names = [str(x) for x in range(1000)]
        groups = jaa_pelaajat_kahteen_lohkoon(player_names)
        self.assertEqual(len(groups["Lohko A"]), len(groups["Lohko B"]))

    def test_split_counts_odd(self):
        player_names = [str(x) for x in range(999)]
        groups = jaa_pelaajat_kahteen_lohkoon(player_names)
        self.assertEqual(abs(len(groups["Lohko A"]) - len(groups["Lohko B"])), 1)



if __name__ == '__main__':
    unittest.main()
