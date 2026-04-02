import unittest
import sys

class TestEnv(unittest.TestCase):
    def test_python_version(self):
        """makes sure we are using python 3.10"""
        self.assertGreaterEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 10)

    def test_imports(self):
        """Verify that critical libs are installed"""
        import pandas
        import pytesseract
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
