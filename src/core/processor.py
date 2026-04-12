import os
from typing import List
from src.models.worker_record import WorkerRecord
from src.core.base_extractor import BaseExtractor
from src.utils.config_loader import ConfigLoader
from src.utils.data_normalizer import DataNormalizer

class Processor:
    """
    Orchestrate the data flow between the Extractor and the Model.
    This class is agnostic to the specific OCR engine used.
    """
    def __init__(self, extractor: BaseExtractor, normalizer: DataNormalizer):
        self.extractor = extractor
        self.normalizer = normalizer

    def process_all_files(self, file_list: list[str]) -> list[WorkerRecord]:
        all_records = []
        for file_path in file_list:
            raw_text_pages = self.extractor.get_raw_text(file_path)

            for page_text in raw_text_pages:
                record = self._build_record_from_text(page_text, file_path)
                if record:
                    all_records.append(record)
        return all_records

    def _build_record_from_text(self, text: str, filename: str) -> WorkerRecord:
        extracted_data = {}
        lines = text.split('\n')
        categories = self.normalizer.mapping.get("keywords").keys()

        for line in lines:
            for category in categories:
                if self.normalizer.match_category(line, category):
                    extracted_data[category] = line

        return WorkerRecord(
            employee_id=self.normalizer.sanitize_id(extracted_data.get("cedula", "")),
            full_names=extracted_data.get("nombre y apellidos", "DESCONOCIDO"),
            entry_date=extracted_data.get("fecha de ingreso", ""),
            base_salary=self.normalizer.to_float(extracted_data.get("sueldo", "0")),
            working_place=extracted_data.get("ubicación laboral", ""),
            job_charge=extracted_data.get("cargo", ""),
            source_file=filename
        )