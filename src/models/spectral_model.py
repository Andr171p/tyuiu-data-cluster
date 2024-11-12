import numpy as np
import pandas as pd
from sklearn.cluster import SpectralClustering


class SpectralClusterModel:
    def __init__(self) -> None:
        self.model: SpectralClustering | None = None

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        self.model = SpectralClustering(
            n_clusters=2,
            affinity='rbf',
            gamma=20.0,
            random_state=42
        )
        clusters = self.model.fit_predict(data)
        return clusters
