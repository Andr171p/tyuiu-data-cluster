import io

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import settings
from src.visualization.utils import save_txt


class DataReport:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def info(self) -> None:
        self.data.info(
            verbose=True,
            buf=None
        )
        buffer = io.StringIO()
        self.data.info(buf=buffer)
        text = buffer.getvalue()
        path = settings.reports.data_report_path / "info.txt"
        save_txt(
            file_path=path,
            text=text
        )

    def describe(self) -> None:
        describe: pd.DataFrame = self.data.describe()
        path = settings.reports.data_report_path / "describe.csv"
        describe.to_csv(path)

    def corr(self, corr_value: float = 0.8) -> None:
        path = settings.reports.data_report_path / "corr.png"
        sns.heatmap(
            self.data.corr() > corr_value,
            annot=True,
            cbar=False
        )
        plt.savefig(path)
        plt.show()