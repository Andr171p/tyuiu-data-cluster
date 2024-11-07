import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import settings
from src.visualization.utils import save_txt


class DataVisualization:
    def __init__(
            self,
            data: pd.DataFrame,
            report: bool = False
    ) -> None:
        self.data = data
        self.report = report

    def info(self) -> None:
        self.data.info(
            verbose=True,
            buf=None
        )
        if self.report:
            path = settings.reports.data_report_path / "info.txt"
            save_txt(
                file_path=path,
                text=str(self.data.info())
            )