import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.config import settings
from src.models.tsne_model import TSNEModel
from src.models.k_means_model import KMeansModel
from src.visualization.model.report import ModelReport


def get_df(csv_path: str, feature: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df = df.drop(
        labels=['Unnamed: 0', 'Unnamed: 0.1'],
        axis=1
    )
    df = df[df[feature] == 1]
    return df


def get_clusters(data: pd.DataFrame, group: str) -> None:
    tsne_model = TSNEModel()
    tsne = tsne_model.fit(
        data=data,
        report_dir=group
    )
    k_means_model = KMeansModel()
    k_means_model.fit(
        data=data,
        report_dir=group
    )
    segments = k_means_model.fit_predict(
        data=data,
        n_clusters=6
    )
    labels = k_means_model.labels()
    report = ModelReport(directory=group)
    report.segment(
        tsne=tsne,
        segments=segments
    )
    k_means_model.cluster(
        data=data,
        labels=labels,
        group='ВШЦТ',
        file_name_template="tyuiu-hits"
    )


def main() -> None:
    df = get_df(
        csv_path=settings.data.processed_data_path / "tyuiu-dataset-processed.csv",
        feature='Формирующее подр._Высшая школа цифровых технологий'
    )
    get_clusters(
        data=df,
        group='ВШЦТ'
    )


if __name__ == "__main__":
    main()
