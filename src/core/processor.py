import os
from typing import List
from src.models.worker_record import WorkerRecord
from src.core.base_extractor import BaseExtractor
from src.utils.config_loader import ConfigLoader

class Processor:
    """
    Orchestrate the data flow between the Extractor and the Model.
    This class is agnostic to the specific OCR engine used.
    """
    def __init__(self, extractor: BaseExtractor, config: ConfigLoader):
        self.extractor = extractor
        self.config = config
        self.mapping = ConfigLoader("config/mapping.json")

    def process_all_files(self, file_list: List[str]) -> List[WorkerRecord]:
        """
        Loops through files and collects records.
        """
        all_records = []
        for file_path in file_list:
            records = self.extractor.extract_data(file_path)
            all_records.extend(records)
        return all_records