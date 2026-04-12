import unittest
from src.core.processor import Processor
from src.utils.data_normalizer import DataNormalizer
from src.utils.config_loader import ConfigLoader


class MockTesseract:
    @staticmethod
    def get_raw_text(self, path):
        # Simulamos lo que diría un PDF real de Corposalud
        return ["""
        GOBIERNO BOLIVARIANO - CORPOSALUD
        NOMBRE Y APELLIDOS: LUIS MONASTERIOS
        C.I: V-22.333.444
        CARGO: SYSTEMS AUTOMATION ENGINEER
        SUELDO BASE: 1.500,50
        UBICACIÓN LABORAL: SEDE CENTRAL MARACAY
        """]


class TestIntegration(unittest.TestCase):
    def test_dynamic_mapping_success(self):
        mapping = ConfigLoader("config/mapping.json")
        normalizer = DataNormalizer(mapping)
        processor = Processor(MockTesseract(), normalizer)

        results = processor.process_all_files(["fake.pdf"])
        worker = results[0]

        self.assertEqual(worker.employee_id, "22333444")
        self.assertEqual(worker.base_salary, 1500.50)
        self.assertEqual(worker.full_names, "NOMBRE Y APELLIDOS: LUIS MONASTERIOS")