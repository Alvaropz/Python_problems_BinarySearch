import unittest

from validate_delivery_orders import validate_delivery_orders

class TestCases(unittest.TestCase):
    def test_validate_delivery_orders(self):
        self.assertEqual(validate_delivery_orders(["P1","P2","D2","D1"]), True)
        self.assertEqual(validate_delivery_orders(["P1","P2","P3"]), False)
        self.assertEqual(validate_delivery_orders(["D1","P1"]), False)
        self.assertEqual(validate_delivery_orders(["P1","D1","P1","D1"]), False)
        self.assertEqual(validate_delivery_orders(["P1","P2","D2","D1","P3"]), False)
        self.assertEqual(validate_delivery_orders(["P1","P2","D2","D1","P3","P4","P5","D4","D5","D3"]), True)
        self.assertEqual(validate_delivery_orders(["P2"]), False)
        self.assertEqual(validate_delivery_orders(["P2","D2"]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)