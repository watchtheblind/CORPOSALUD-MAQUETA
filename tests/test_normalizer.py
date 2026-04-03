import unittest
from src.utils.data_normalizer import DataNormalizer
from src.utils.config_loader import ConfigLoader

class TestDataNormalizer(unittest.TestCase):
    def setUp(self):
        self.mapping = ConfigLoader("config/mapping.json")
        self.normalizer = DataNormalizer(self.mapping)

    def test_currency_conversion(self):
        self.assertEqual(self.normalizer.to_float("1.250,50"), 1250.50)
        self.assertEqual(self.normalizer.to_float("Bs. 0,15"), 0.15)

    def test_id_sanitization(self):
        self.assertEqual(self.normalizer.sanitize_id("V-22.333.444"), "22333444")
        self.assertEqual(self.normalizer.sanitize_id(" 12 345 678 "), "12345678")

if __name__ == '__main__':
    unittest.main()