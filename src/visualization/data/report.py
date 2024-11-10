import io

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import settings
from src.visualization.utils import save_txt


class DataReport:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def info(self) -> None:
        self.df.info(
            verbose=True,
            buf=None
        )
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        text = buffer.getvalue()
        path = settings.reports.data_report_path / "info.txt"
        save_txt(
            file_path=path,
            text=text
        )

    def describe(self) -> None:
        describe: pd.DataFrame = self.df.describe()
        path = settings.reports.data_report_path / "describe.csv"
        describe.to_csv(path)

    def top_values(self, column: str) -> None:
        top_values: pd.Series = self.df[column].value_counts()
        path = settings.reports.data_report_path / f"top-{column}.csv"
        top_values.to_csv(path)

    def corr(self, corr_value: float = 0.8) -> None:
        path = settings.reports.data_report_path / "corr.png"
        sns.heatmap(
            self.df.corr() > corr_value,
            annot=True,
            cbar=False
        )
        plt.savefig(path)
        plt.show()

    def labels_bar(self, column: str) -> None:
        self.df[column].value_counts().plot(kind='bar')
        plt.savefig(settings.reports.data_report_path / f'bar_{column}.png')
        plt.xlabel(column)
        plt.ylabel('Количество студентов')
        plt.show()
