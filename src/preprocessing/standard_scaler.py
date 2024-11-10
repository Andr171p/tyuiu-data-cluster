import pickle

import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.config import settings


class Standardization:
    _scaler: StandardScaler = None

    @classmethod
    def fit(cls, data: pd.DataFrame) -> None:
        cls._scaler = StandardScaler()
        cls._scaler.fit(data)

    @classmethod
    def transform(cls, data: pd.DataFrame) -> pd.DataFrame:
        return cls._scaler.transform(data)

    @classmethod
    def save(
            cls, file_name: str = settings.models.standard_scaler_path
    ) -> None:
        with open(
                file=file_name,
                mode='wb'
        ) as file:
            pickle.dump(cls._scaler, file)

    @classmethod
    def load(
            cls, file_name: str = settings.models.standard_scaler_path
    ) -> StandardScaler | None:
        if cls._scaler is None:
            with open(
                file=file_name,
                mode='rb'
            ) as file:
                cls._scaler = pickle.load(file)
            return cls._scaler
        return


standard = Standardization()
