import unittest

from package_versioning import package_versioning

class TestCases(unittest.TestCase):
    def test_package_versioning(self):
        self.assertEqual(package_versioning("11.1.2", "11.1.3"), True)
        self.assertEqual(package_versioning("3.1.2", "1.1.3"), False)
        self.assertEqual(package_versioning("3.1.2", "3.2.3"), True)
        self.assertEqual(package_versioning("13.1.2", "3.2.3"), False)
        self.assertEqual(package_versioning("0.0.100", "1.0.0"), True)
        self.assertEqual(package_versioning("3.1.2", "3.1.20"), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)