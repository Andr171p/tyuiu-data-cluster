import numpy as np
import pandas as pd

from src.config import settings
from src.models.tsne_model import TSNEModel
from src.models.k_means_model import KMeansModel
from src.visualization.model.report import ModelReport


df = pd.read_csv(settings.data.processed_data_path)

tsne = TSNEModel()
tsne_array = tsne.fit(data=df)

k_means = KMeansModel()
k_means.fit(data=df)
segments = k_means.fit_predict(
    data=df,
    n_clusters=5
)
report = ModelReport()
report.segment(
    tsne=tsne_array,
    segments=segments
)
labels = k_means.labels()
k_means.cluster(
    data=df,
    labels=labels
)
