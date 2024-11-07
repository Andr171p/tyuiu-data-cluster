from pydantic import BaseModel

from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve() .parent.parent


class DataSettings(BaseModel):
    raw_inputs_path: Path = BASE_DIR / "data" / "raw" / "inputs.csv"
    raw_outputs_path: Path = BASE_DIR / "data" / "raw" / "outputs.csv"
    interim_data_path: Path = BASE_DIR / "data" / "interim" / "tyuiu-dataset.csv"
    processed_data_path: Path = BASE_DIR / "data" / "processed" / "tyuiu-dataset-model.csv"


class ModelSettings(BaseModel):
    standard_scaler_path: Path = BASE_DIR / "models" / "standard-scaler.pkl"


class ReportSettings(BaseModel):
    data_report_path: Path = BASE_DIR / "reports" / "data"
    model_report_path: Path = BASE_DIR / "reports" / "model"


class Settings(BaseModel):
    data: DataSettings = DataSettings()
    model: ModelSettings = ModelSettings()
    reports: ReportSettings = ReportSettings()


settings = Settings()
