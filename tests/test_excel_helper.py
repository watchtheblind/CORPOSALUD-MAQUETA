import unittest
import os
from src.models.worker_record import WorkerRecord
from src.utils.excel_helper import ExcelHelper

class TestExcelHelper(unittest.TestCase):
    def setUp(self):
        """Set up a dummy record with the corporation structure"""
        self.test_file = "tests/test_output.xlsx"
        self.dummy_record = WorkerRecord(
            employee_id="V22333444",
            full_names="LUIS MONASTERIOS",
            entry_date="15/10/2023",
            base_salary=2500.00,
            working_place="CENTRO CARDIOLOGICO MARACAY",
            job_charge="SYSTEMS ENGINEER",
            source_file="maqueta_abril.pdf"
        )
    def test_save_individual_report(self):
        """verifies Excel creation with the new file structure"""
        ExcelHelper.save_individual_report(self.dummy_record, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
    def tearDown(self):
        """clean up generated files after each test"""
        if os.path.exists(self.test_file): os.remove(self.test_file)
if __name__ == '__main__':
    unittest.main()