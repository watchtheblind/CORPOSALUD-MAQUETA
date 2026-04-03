import re
from src.utils.config_loader import ConfigLoader

class DataNormalizer:
    """
    Clean and format raw strings into structured data.
    Separates string manipulation logic from business orchestration.
    """
    def __init__(self, mapping: ConfigLoader):
        self.mapping = mapping
    def to_float(self, raw_value: str) -> float:
        """
        Converts currency strings to floats.
        :param raw_value:
        :return:
        """
        if not raw_value: return 0.0

        pattern = self.mapping.get("regex_patterns.monto_decimal")
        match = re.search(pattern, str(raw_value))
        if match:
            # Clean Venezuelan format: remove thousands separator, swap decimal comma
            clean_val = match.group().replace('.', '').replace(',', '.')
            try:
                return float(clean_val)
            except ValueError:
                return 0.0
        return 0.0
    def match_category(self, text: str, category: str) -> bool:
        """
            Checks if a text matches keywords for a specific mapping category.
        """
        keywords = self.mapping.get(f"keywords.{category}", [])
        clean_text = str(text).strip().lower()
        return any(keyword.lower() in clean_text for keyword in keywords)

    @staticmethod
    def sanitize_id(raw_id: str) -> str:
        """
        Removes dots, spaces and letters from ID (V-12.345.678 -> 12345678).
        """
        return re.sub(r'[^0-9]', '', str(raw_id))