import pytesseract
from pdf2image import convert_from_path
from src.core.base_extractor import BaseExtractor
from src.models.worker_record import WorkerRecord
from src.utils.data_normalizer import DataNormalizer

class TesseractHandler(BaseExtractor):
    """
        Converts PDF to images and extract text using OCR.
    """
    def __init__(self, config, mapping, normalizer: DataNormalizer):
        self.config = config
        self.mapping = mapping
        self.normalizer = normalizer
        pytesseract.pytesseract.tesseract_cmd = self.config.get("ocr.tesseract_path")

    def extract_data(self, file_path: str) -> list[WorkerRecord]:
        """
            Orchestrates the conversion from PDF to Text.
            Note: For now, we return an empty list or raw objects to focus on the OCR connection.
        """
        #Convert PDF to PIL images
        # We use a lower DPI (150-200) to save RAM on low-end PCs
        pages = convert_from_path(file_path, 200)
        all_workers = []
        for page in pages:
            raw_text = pytesseract.image_to_string(page, lang=self.config.get("ocr.lang"))
            record = self._parse_worker_text(raw_text, file_path)
            if record:
                all_workers.append(record)
        return all_workers