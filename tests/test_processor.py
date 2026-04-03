import unittest
from tests.mock_extractor import MockExtractor
from src.core.processor import Processor
from src.utils.config_loader import ConfigLoader

class TestProcessor(unittest.TestCase):
    def setUp(self):
        # We use our real ConfigLoader but with a fake Extractor
        self.config = ConfigLoader("config/settings.json")
        self.mock_extractor = MockExtractor()
        self.processor = Processor(self.mock_extractor, self.config)

    def test_process_files_flow(self):
        """Tests if the processor correctly collects records from the extractor."""
        files = ["dummy1.pdf", "dummy2.pdf"]
        results = self.processor.process_all_files(files)

        # We sent 2 files, MockExtractor returns 1 record per file = 2 records total
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].full_names, "MOCK USER")

if __name__ == '__main__':
    unittest.main()
