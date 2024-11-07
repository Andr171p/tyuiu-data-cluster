import pandas as pd
from sklearn.manifold import TSNE


class TSNEModel:
    def __init__(self) -> None:
        self.model: TSNE = TSNE(
            n_components=2,
            random_state=0
        )

    def ...