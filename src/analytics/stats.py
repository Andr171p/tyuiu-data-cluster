import scipy
import pandas as pd

from typing import Any


class Statistics:
    ALPHA = 0.05

    def __init__(self, df: pd.DataFrame) -> None:
        self._df = df.describe()
        print(self._df)

    def shapiro(self, column: str) -> bool:
        stat, p = scipy.stats.shapiro(self._df[column])
        print('Statistics=%.3f, p-value=%.3f' % (stat, p))
        return True if p > self.ALPHA else False

    def normal_test(self, column: str) -> bool:
        stat, p = scipy.stats.normaltest(self._df[column])
        print('Statistics=%.3f, p-value=%.3f' % (stat, p))
        return True if p > self.ALPHA else False

    def t_test(self, column: str) -> Any:
        half = len(self._df[column]) / 2
        sam1 = self._df.loc[:half, column]
        sam2 = self._df.loc[half:, column]
        return scipy.stats.ttest_ind(sam2, sam1)


df = pd.read_csv(r'C:\Users\andre\TyuiuClusterModel\data\processed\tyuiu-processed.csv')
s = Statistics(df)
print(s.shapiro('Сумма баллов'))
print(s.normal_test('Сумма баллов'))
print(s.t_test('Сумма баллов'))