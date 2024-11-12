import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import settings


class ModelReport:
    def __init__(self, directory: str) -> None:
        self._directory = directory

    def nested_clusters(self, data: np.ndarray) -> None:
        plt.scatter(data[:, 0], data[:, 1])
        path = settings.reports.model_report_path / f'{self._directory}' / "tsne-cluster.png"
        plt.savefig(path)
        plt.show()

    def error(self, error: list[float]) -> None:
        sns.lineplot(x=range(1, 21), y=error)
        sns.scatterplot(x=range(1, 21), y=error)
        path = settings.reports.model_report_path / f'{self._directory}' / "k-means error.png"
        plt.savefig(path)
        plt.show()

    def segment(self, tsne: np.ndarray, segments: np.ndarray) -> None:
        df = pd.DataFrame(
            {
                'x': tsne[:, 0],
                'y': tsne[:, 1],
                'segments': segments
            }
        )
        sns.scatterplot(
            x='x',
            y='y',
            hue='segments',
            data=df
        )
        path = settings.reports.model_report_path / f'{self._directory}' / "clusters-segments.png"
        plt.savefig(path)
        plt.show()
