import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from src.config import settings
from src.visualization.model.report import ModelReport


class KMeansModel:
    def __init__(self) -> None:
        self.model: KMeans | None = None
        self.error: list[float] = []

    def fit(self, data: pd.DataFrame, report_dir: str) -> None:
        for n_clusters in range(1, 21):
            model = KMeans(
                init='k-means++',
                n_clusters=n_clusters,
                max_iter=500,
                random_state=22
            )
            model.fit(data)
            self.error.append(model.inertia_)
        report: ModelReport = ModelReport(directory=report_dir)
        report.error(self.error)

    def fit_predict(
            self,
            data: pd.DataFrame,
            n_clusters: int = 5
    ) -> np.ndarray:
        self.model = KMeans(
            init='k-means++',
            n_clusters=n_clusters,
            max_iter=500,
            random_state=22
        )
        segments = self.model.fit_predict(data)
        return segments

    def labels(self) -> np.ndarray:
        return self.model.labels_

    @staticmethod
    def cluster(
            data: pd.DataFrame,
            labels: np.ndarray,
            group: str,
            file_name_template: str
    ) -> None:
        data['Cluster'] = labels
        data_clusters = [group for _, group in data.groupby('Cluster')]
        for i, cluster in enumerate(data_clusters):
            path = settings.data.clustered_groups_data_path / f'{group}' / f'{file_name_template}-{i + 1}.csv'
            cluster.to_csv(path)
