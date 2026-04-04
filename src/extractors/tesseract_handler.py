import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from typing import List
from src.core.base_extractor import BaseExtractor
from src.models.worker_record import WorkerRecord
from src.utils.config_loader import ConfigLoader

class TesseractHandler(BaseExtractor):
    """
        Convert PDF to images and extract text using OCR.
    """
    def __init__(self, config: ConfigLoader):
        self.config = config
        # Configure the Tesseract executable path from JSON
        pytesseract.pytesseract.tesseract_cmd = self.config.get("ocr.tesseract_path")

    def extract_data(self, file_path: str) -> List[WorkerRecord]:
        """
            Orchestrates the conversion from PDF to Text.
            Note: For now, we return an empty list or raw objects to focus on the OCR connection.
        """
        #Convert PDF to PIL images
        # We use a lower DPI (150-200) to save RAM on low-end PCs
        pages = convert_from_path(file_path, 200)

        raw_text = ""
        for page in pages:
            #you can put some image processing here
            #Performing OCR
            raw_text += pytesseract.image_to_string(page, lang=self.config.get("ocr.language"))

        #MOMENTARILY, we print the text to make sure it works
        print(f"--- Raw OCR Output for {file_path} ---")
        print(raw_text[:500])  # First 500 chars

        return []  # We will implement the parsing logic in the next step
