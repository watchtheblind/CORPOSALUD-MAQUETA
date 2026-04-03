from typing import List
from src.core.base_extractor import BaseExtractor
from src.models.worker_record import WorkerRecord

class MockExtractor(BaseExtractor):
    """
    A fake extractor that returns hardcoded data.
    Used to test the Processor and ExcelHelper without OCR overhead.
    """
    def extract_data(self, file_path: str) -> List[WorkerRecord]:
        # Simulates finding one worker in the "PDF"
        return [
            WorkerRecord(
                employee_id="V12345678",
                full_names="MOCK USER",
                entry_date="01/01/2020",
                base_salary=5000.0,
                working_place="TEST CLINIC",
                job_charge="TESTER",
                source_file=file_path
            )
        ]