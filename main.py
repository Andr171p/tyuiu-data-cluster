import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\andre\TyuiuClusterModel\data\raw\tyuiu-students-2019-2024.csv')
print(df.columns)
from src.visualization.data.report import DataReport

report = DataReport(df=df)
report.labels_bar(column='Формирующее подр.')

print(df['Олимпиады'].value_counts())

