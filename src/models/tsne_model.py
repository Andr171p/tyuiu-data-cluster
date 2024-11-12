import numpy as np
import pandas as pd
from sklearn.manifold import TSNE

from src.visualization.model.report import ModelReport


class TSNEModel:
    def __init__(self) -> None:
        self.model: TSNE = TSNE(
            n_components=2,
            random_state=0
        )

    def fit(self, data: pd.DataFrame, report_dir: str) -> np.ndarray:
        tsne_data = self.model.fit_transform(data)
        report: ModelReport = ModelReport(directory=report_dir)
        report.nested_clusters(tsne_data)
        print(tsne_data.shape)
        return tsne_data