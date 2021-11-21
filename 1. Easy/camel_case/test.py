import unittest

from camel_case import camel_case

class TestCases(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(camel_case(["Go", "nasa"]), "goNasa")
        self.assertEqual(camel_case(["java", "beans"]), "javaBeans")
        self.assertEqual(camel_case(["Trudy"]), "trudy")
        self.assertEqual(camel_case(["Marge", "milhouse", "lisa", "bart"]), "margeMilhouseLisaBart")
        self.assertEqual(camel_case(["GRYFFINDOR", "SLYTHERIN", "HUFFLEPUFF", "RAVENCLAW"]), "gryffindorSlytherinHufflepuffRavenclaw")


if __name__ == "__main__":
    unittest.main(verbosity=2)