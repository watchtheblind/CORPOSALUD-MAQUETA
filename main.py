import os
from src.utils.config_loader import ConfigLoader
from src.utils.data_normalizer import DataNormalizer
from src.extractors.tesseract_handler import TesseractHandler
from src.core.processor import Processor
from src.utils.excel_writer import ExcelWriter

def main():
    print("--- Iniciando Procesamiento de Nómina Corposalud ---")

    # 1. Cargar configuraciones
    config = ConfigLoader("config/settings.json")
    mapping = ConfigLoader("config/mapping.json")
    
    # 2. Inicializar componentes
    normalizer = DataNormalizer(mapping)
    extractor = TesseractHandler(config) # El OCR
    processor = Processor(extractor, normalizer)
    writer = ExcelWriter("data/output/reporte_nomina.xlsx")

    # 3. Obtener lista de archivos PDF en la carpeta de entrada
    input_dir = "data/input"
    files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".pdf")]

    if not files:
        print("❌ No se encontraron archivos PDF en data/input.")
        return

    # 4. Ejecutar el flujo
    print(f"📂 Procesando {len(files)} archivos...")
    all_workers = processor.process_all_files(files)

    # 5. Guardar resultados
    writer.save_records(all_workers)
    print("--- Proceso Finalizado ---")

if __name__ == "__main__":
    main()