import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


df = pd.read_csv(r'C:\Users\andre\TyuiuClusterModel\data\raw\inputs.csv')

'''kmeans = KMeans(n_clusters=59, random_state=42)
kmeans.fit(df)

labels = kmeans.labels_
print(labels)

silhouette_avg = silhouette_score(df, labels)
print(f'Средний коэффициент силуэта: {silhouette_avg:.2f}')'''

from src.visualization.data.report import DataReport

df = df.drop('ФИО', axis=1)

from src.models.tsne_model import TSNEModel
from src.models.k_means_model import KMeansModel
from src.visualization.model.report import ModelReport

model = TSNEModel()
tsne = model.fit(df)

k_model = KMeansModel()
segments = k_model.fit_predict(df)

report = ModelReport()
report.segment(tsne=tsne, segments=segments)