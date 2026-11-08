import unittest
from dounaibao import pour_soymilk


class CupStabilityTest(unittest.TestCase):
    def test_pour_does_not_spill(self):
        for amount in [1, 100, 200, 333]:
            with self.subTest(amount=amount):
                result = pour_soymilk(amount)
                self.assertEqual(result.spilled_ml, 0)
                self.assertEqual(result.served_ml, amount)
