from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class WorkerRecord:
    """
    Represents the specific structure of the worker report.
    This is the data contract for the entire automation flow.
    """
    employee_id: str          # Cédula
    full_names: str           # Nombres y Apellidos
    entry_date: str           # Fecha de ingreso
    base_salary: float        # Sueldo base
    working_place: str        # Centro de salud / Ubicación
    job_charge: str           # Cargo o función
    source_file: str          # PDF filename for traceability

    def to_dict(self) -> dict:
        """Converts the record to a dictionary for Excel/Pandas export."""
        return asdict(self)