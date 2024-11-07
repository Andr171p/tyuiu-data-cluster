import pandas as pd

from src.config import settings
from src.features.build_features import FEATURES
from src.preprocessing.standardization import standard_scaler


class Dataset:
    dataset: pd.DataFrame = None

    @classmethod
    def load(
            cls,
            csv_path: str = settings.data.interim_data_path
    ) -> None:
        cls.dataset = pd.read_csv(csv_path)
        cls.dataset = cls.dataset.drop(
            labels=['Unnamed: 0.2', 'Unnamed: 0', 'ФИО', 'Unnamed: 0.1'],
            axis=1
        )

    @classmethod
    def save(
            cls,
            csv_path: str = settings.data.processed_data_path
    ) -> None:
        cls.dataset.to_csv(csv_path)

    @classmethod
    def features(cls) -> pd.Index:
        return cls.dataset.columns

    @classmethod
    def standard(cls) -> pd.DataFrame | None:
        standard_scaler.fit(cls.dataset)
        standard_scaler.save()
        cls.dataset = standard_scaler.transform(cls.dataset)
        cls.dataset = pd.DataFrame(
            data=cls.dataset,
            columns=FEATURES[1::]
        )
        return cls.dataset

    @classmethod
    def shape(cls) -> tuple[int, int]:
        return cls.dataset.shape

