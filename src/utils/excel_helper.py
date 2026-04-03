import pandas as pd
import os
from openpyxl import load_workbook
from src.models.worker_record import WorkerRecord
from typing import List

class ExcelHelper:
    """
        Handles all excel output operations.
        Isolates file  writing logic from data extraction
    """
    @staticmethod
    def save_individual_report(record: WorkerRecord, output_path: str):
        """Creates a single Excel file for one specified record"""
        df = pd.DataFrame([record.to_dict()])
        df.to_excel(output_path, index=False, engine='openpyxl')
    @staticmethod
    def append_to_consolidated(records: List[WorkerRecord], consolidated_path: str):
        """Adds multiple records to a master Excel file.
            If te file doesn't exist, it creates it.
        """
        df_new = pd.DataFrame(record.to_dict() for record in records)
        if not os.path.exists(consolidated_path):
            df_new.to_excel(consolidated_path, index=False, engine='openpyxl')
            return
        else:
            with pd.ExcelWriter(consolidated_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                try:
                    # Try to load existing data to append
                    existing_df = pd.read_excel(consolidated_path)
                    combined_df = pd.concat([existing_df, df_new], ignore_index=True)
                    combined_df.to_excel(writer, index=False, sheet_name='Sheet1')
                except Exception as e:
                    print(f"Error appending to Excel: {e}")