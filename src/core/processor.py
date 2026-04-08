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
            # El extractor ahora solo escupe TEXTO CRUDO (cumple SRP)
            raw_text_pages = self.extractor.get_raw_text(file_path)
            
            for page_text in raw_text_pages:
                record = self._build_record_from_text(page_text, file_path)
                if record:
                    all_records.append(record)
        return all_records

    def _build_record_from_text(self, text: str, filename: str) -> WorkerRecord:
        """
        Mapeo dinámico: Recorre el JSON y llena los datos sin un solo 'if'.
        """
        extracted_data = {}
        lines = text.split('\n')
        categories = self.normalizer.mapping.get("keywords").keys()

        for line in lines:
            for category in categories:
                if self.normalizer.match_category(line, category):
                    # Solo guardamos si no teníamos ya un valor, o podrías 
                    # implementar lógica para quedarte con la línea más relevante.
                    if category not in extracted_data:
                        extracted_data[category] = line.strip()

        # Usamos .get(key, "") para que si no existe la categoría en el texto, 
        # el programa no explote y devuelva un campo vacío.
        return WorkerRecord(
            employee_id=self.normalizer.sanitize_id(extracted_data.get("cedula", "")),
            full_names=self.normalizer.clean_label(extracted_data.get("nombre y apellidos", "DESCONOCIDO")),
            entry_date=self.normalizer.clean_label(extracted_data.get("fecha de ingreso", "")),
            base_salary=self.normalizer.to_float(extracted_data.get("sueldo", "0")),
            working_place=self.normalizer.clean_label(extracted_data.get("ubicación laboral", "")),
            job_charge=self.normalizer.clean_label(extracted_data.get("cargo", "")),
            source_file=filename
        )