from abc import ABC, abstractmethod
from typing import List
from src.models.worker_record import WorkerRecord

class BaseExtractor(ABC):
    """
    Abstract Base Class for all extraction engines.
    Ensures that any extractor (Tesseract, AWS, Google)
    returns a list of WorkerRecord objects.
    Any OCR engine must implement this method
    """
    @abstractmethod
    def extract_data(self, file_path: str) -> List[WorkerRecord]:
        """
        Reads a file and returns a list of processed WorkerRecords.
        :param file_path: Path to the PDF or Image file.
        :return: List of WorkerRecord entities.
        """
        pass