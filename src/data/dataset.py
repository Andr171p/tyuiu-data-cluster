import numpy as np
import pandas as pd

from src.config import settings
from src.preprocessing.standard_scaler import standard


class Dataset:
    def __init__(
            self,
            csv_path: str = settings.data.data_path / "processed" / "tyuiu-dataset-processed.csv"
    ) -> None:
        self.df = pd.read_csv(csv_path)
        self.df = self.df.drop('Unnamed: 0', axis=1)
        self.features = self.df.columns

    def shape(self) -> tuple[int, int]:
        return self.df.shape

    def columns(self) -> pd.Index:
        return self.df.columns

    def standard(self) -> pd.DataFrame:
        standard.fit(self.df)
        standard.save()
        self.df = standard.transform(self.df)
        self.df = pd.DataFrame(
            data=self.df,
            columns=self.features
        )
        return self.df

    def save(self) -> None:
        path = settings.data.processed_data_path
        self.df.to_csv(path)
