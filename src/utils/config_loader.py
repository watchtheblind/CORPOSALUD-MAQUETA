import json
import os
from typing import Any

class ConfigLoader:
    """Loading, validating and serving the systems config."""
    def __init__(self, config_path: str = "config/settings.json") -> None:
        self.config_path = config_path
        self.data = self._load_file()

    def _load_file(self) -> dict:
        """reads file and handles reading error"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuración no encontrada en: {self.config_path}")
        with open(self.config_path, "r") as file:
            return json.load(file)

    def get(self, key_path: str, default: Any = None) -> Any:
        """Navigates te JSON using dots (ex: 'ocr.language') for cleaner code"""
        keys = key_path.split(".")
        value = self.data
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

    @property
    def debug_mode(self) -> bool:
        """flags to turn detailed logs or save temporary images"""
        return self.get("flags.debug", False)