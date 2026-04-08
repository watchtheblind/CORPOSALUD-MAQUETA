import pytesseract
from pdf2image import convert_from_path
from src.core.base_extractor import BaseExtractor

class TesseractHandler(BaseExtractor):
    def __init__(self, config):
        self.config = config
        pytesseract.pytesseract.tesseract_cmd = self.config.get("ocr.tesseract_path")

    def get_raw_text(self, file_path: str) -> list[str]:
        """
        Única responsabilidad: Convertir PDF a texto crudo página por página.
        """
        pages = convert_from_path(file_path, 200)
        return [pytesseract.image_to_string(page, lang=self.config.get("ocr.lang")) for page in pages]
    
    def extract_data(self, file_path: str):
        # Este método lo mantenemos por la interfaz BaseExtractor, 
        # pero ahora redirige a get_raw_text o se adapta según necesites.
        return self.get_raw_text(file_path)