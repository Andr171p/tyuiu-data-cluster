import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\andre\TyuiuClusterModel\data\universities\ВШЦТ.csv')

'''bins = [0, 130, 180, 210, 240, 270, 310]
labels = ['0-130', '131-180', '181-210', '211-240', '241-270', '271-310']

# Создаем новый столбец с сегментами
df['Сегмент'] = pd.cut(df['Сумма баллов'], bins=bins, labels=labels, right=False)

# Считаем количество записей в каждом сегменте
segment_counts = df['Сегмент'].value_counts()

# Строим круговую диаграмму
plt.figure(figsize=(8, 6))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%')
plt.title('Распределение суммы баллов по сегментам')
plt.show()'''

print(df.columns)

bins = [3, 3.5, 4, 4.5, 5]
labels = ['3-3.5', '3.5-4', '4-4.5', '4.5-5']

# Создаем новый столбец с сегментами
df['Сегмент'] = pd.cut(df['Ср. балл док-та об образовании'], bins=bins, labels=labels, right=False)

# Считаем количество записей в каждом сегменте
segment_counts = df['Сегмент'].value_counts()

# Строим круговую диаграмму
plt.figure(figsize=(8, 6))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%')
plt.title('Распределение суммы баллов по сегментам')
plt.show()