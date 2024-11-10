from pydantic import BaseModel

from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class DataSettings(BaseModel):
    raw_path: Path = BASE_DIR / "data" / "raw"
    raw_years_path: Path = BASE_DIR / "data" / "raw" / "years"
    raw_all_path: Path = BASE_DIR / "data" / "raw"
    interim_data_path: Path = BASE_DIR / "data" / "interim"
    processed_data_path: Path = BASE_DIR / "data" / "processed" / "tyuiu-dataset-model.csv"
    clustered_data_path: Path = BASE_DIR / "data" / "clustered" / "tyuiu-dataset-clustered.csv"
    clustered_groups_data_path: Path = BASE_DIR / "data" / "clustered" / "groups"


class ModelSettings(BaseModel):
    standard_scaler_path: Path = BASE_DIR / "models" / "standard-scaler.pkl"


class ReportSettings(BaseModel):
    data_report_path: Path = BASE_DIR / "reports" / "data"
    model_report_path: Path = BASE_DIR / "reports" / "model"


class Settings(BaseModel):
    data: DataSettings = DataSettings()
    models: ModelSettings = ModelSettings()
    reports: ReportSettings = ReportSettings()


settings = Settings()
