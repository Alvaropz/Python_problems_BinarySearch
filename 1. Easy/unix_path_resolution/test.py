import unittest

from unix_path_resolution import unix_path_resolution

class TestCases(unittest.TestCase):
    def test_unix_path_resolution(self):
        self.assertEqual(unix_path_resolution(["usr", "..", "usr", ".", "local", "bin", "docker"]), ["usr", "local", "bin", "docker"])
        self.assertEqual(unix_path_resolution([".."]), [])
        self.assertEqual(unix_path_resolution(["."]), [])
        self.assertEqual(unix_path_resolution([".", "."]), [])
        self.assertEqual(unix_path_resolution([]), [])
        self.assertEqual(unix_path_resolution(["usr", "..", "usr", ".", "local", "..", "bin", "docker", "."]), ['usr', 'bin', 'docker'])
        self.assertEqual(unix_path_resolution([".", ".", "docker"]), ['docker'])
        self.assertEqual(unix_path_resolution(["docker"]), ['docker'])

if __name__ == "__main__":
    unittest.main(verbosity=2)