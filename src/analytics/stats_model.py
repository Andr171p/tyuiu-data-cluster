import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.iolib.summary import Summary

from typing import Any


class StatsModel:
    _history: Any = None

    def __init__(
            self,
            data: pd.DataFrame,
            feature_1: str,
            feature_2: str
    ) -> None:
        self._model = smf.ols(
            formula=f'{feature_1} ~ {feature_2}',
            data=data
        )

    def fit(self) -> Any | None:
        self._history = self._model.fit()
        return self._history

    def summary(self) -> Summary:
        if self._history is not None:
            summary: Summary = self._history.summary()
            return summary
