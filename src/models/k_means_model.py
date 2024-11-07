import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from typing import List, Any

from src.visualization.model.report import ModelReport


class KMeansModel:
    def __init__(self) -> None:
        self.model: KMeans | None = None
        self.error: List[Any] = []

    def fit(self, data: pd.DataFrame) -> None:
        for n_clusters in range(1, 21):
            model = KMeans(
                init='k-means++',
                n_clusters=n_clusters,
                max_iter=500,
                random_state=22
            )
            model.fit(data)
            self.error.append(model.inertia_)
        report: ModelReport = ModelReport()
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
