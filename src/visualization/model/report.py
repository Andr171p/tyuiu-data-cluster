import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import settings


class ModelReport:
    @staticmethod
    def nested_clusters(data: np.ndarray) -> None:
        plt.scatter(data[:, 0], data[:, 1])
        path = settings.reports.model_report_path / "tsne-cluster.png"
        plt.savefig(path)
        plt.show()

    @staticmethod
    def error(error: list[float]) -> None:
        sns.lineplot(x=range(1, 21), y=error)
        sns.scatterplot(x=range(1, 21), y=error)
        path = settings.reports.model_report_path / "k-means error.png"
        plt.savefig(path)
        plt.show()

    @staticmethod
    def segment(tsne: np.ndarray, segments: np.ndarray) -> None:
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
        path = settings.reports.model_report_path / "clusters-segments.png"
        plt.savefig(path)
        plt.show()
