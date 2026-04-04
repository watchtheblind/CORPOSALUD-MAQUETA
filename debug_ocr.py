from src.extractors.tesseract_handler import TesseractHandler
from src.utils.config_loader import ConfigLoader


def test_real_ocr():
    config = ConfigLoader("config/settings.json")
    handler = TesseractHandler(config)

    # Busca un PDF real de una maqueta que tengas a mano
    path = "data/input/punto.pdf"

    try:
        handler.extract_data(path)
        print("\n✅ OCR linked successfully!")
    except Exception as e:
        print(f"\n❌ Error linking OCR: {e}")


if __name__ == "__main__":
    test_real_ocr()