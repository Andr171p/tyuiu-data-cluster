import numpy as np
import pandas as pd

from src.config import settings


class Dataset:
    def __init__(
            self,
            csv_path: str = settings.data.raw_path / "tyuiu-students-2019-2024.csv"
    ) -> None:
        self.df = pd.read_csv(csv_path)

    def shape(self) -> tuple[int, int]:
        return self.df.shape