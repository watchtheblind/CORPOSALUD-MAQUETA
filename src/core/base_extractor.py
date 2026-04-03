from abc import ABC, abstractmethod
from typing import List
from src.models.worker_record import WorkerRecord

class BaseExtractor(ABC):
    """Any OCR engine must implement this method"""
    @abstractmethod
    def extract_data(self, file_path: str) -> List[WorkerRecord]:
        """extracts information from file and maps it to the model"""
        pass