import pandas as pd
from typing import List
from src.models.worker_record import WorkerRecord

class ExcelWriter:
    """
    Responsabilidad: Transformar la lista de registros en un archivo Excel.
    """
    def __init__(self, output_path: str):
        self.output_path = output_path

    def save_records(self, records: List[WorkerRecord]):
        if not records:
            print("⚠️ No hay datos para guardar.")
            return

        # Convertimos la lista de objetos a una lista de diccionarios
        data = [record.__dict__ for record in records]
        
        # Creamos el DataFrame (la tabla)
        df = pd.DataFrame(data)
        
        # Renombramos las columnas para que se vean profesionales
        column_mapping = {
            "employee_id": "Cédula",
            "full_names": "Nombres y Apellidos",
            "entry_date": "Fecha de Ingreso",
            "base_salary": "Sueldo Base",
            "working_place": "Ubicación",
            "job_charge": "Cargo",
            "source_file": "Archivo Origen"
        }
        df.rename(columns=column_mapping, inplace=True)
        
        # Guardamos el Excel
        df.to_excel(self.output_path, index=False)
        print(f"✅ Reporte generado con éxito en: {self.output_path}")