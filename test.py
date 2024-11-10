import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\andre\TyuiuClusterModel\data\raw\tyuiu-students-2019-2024.csv')
print(df.columns)
from src.visualization.data.report import DataReport

report = DataReport(df=df)
# report.labels_bar(column='Формирующее подр.')

print(df['Олимпиады'].value_counts())
df = df.drop('Зачислен', axis=1)
print(df.columns)
print(df['Результаты ЕГЭ'].isna().sum())
print(df['Результаты вступ. испытаний'][21207])

pattern = r'(?P<subject>.*?) - (?P<score>\d+) \(.*\)'
extracted_data = df['Результаты вступ. испытаний'].str.extractall(pattern)
subjects = extracted_data['subject'].unique()
scores = extracted_data['score'].astype(int)
result = extracted_data.reset_index(level=1)[['subject', 'score']]
result_pivot = result.pivot(columns='subject', values='score').reset_index(drop=True)

final_df = pd.concat([df, result_pivot], axis=1)
print(final_df['Информатика (профессиональная)'].isna().sum())
print(final_df.columns)


informatics_columns = [
    'Информатика (профессиональная)',
    'Информатика ВО',
    'Информатика и ИКТ (Профессиональная)',
    'Информатика и информационно–коммуникационные технологии (ИКТ)',
    'Информатика и основы программирования'
]


for col in informatics_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Информатика'] = pd.NA
for col in informatics_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Информатика'] = 1


math_columns = [
    'Математика',
    'Математика (профессиональная)',
    'Математика ВО',
    'Математика и начала математического анализа'
]
print(final_df['Информатика'].value_counts())


for col in math_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Математика 1'] = pd.NA
for col in math_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Математика 1'] = 1


print(final_df['Математика 1'].value_counts())
print(final_df['Математика и начала математического анализа'].value_counts())
print(final_df['Результаты вступ. испытаний'].isna().sum())

history_columns = ['История', 'История (профессиональная)', 'История ВО', 'Мировая и отечественная история']
for col in history_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['История 1'] = pd.NA
for col in history_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'История 1'] = 1
print(final_df['История 1'].value_counts())


physic_columns = ['Инженерная физика', 'Физика', 'Физика (профессиональная)', 'Физика ВО']
for col in physic_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Физика 1'] = pd.NA
for col in physic_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Физика 1'] = 1
print(final_df['Физика 1'].value_counts())


chem_columns = ['Инженерная химия', 'Химия', 'Химия (профессиональная)', 'Химия ВО']
for col in chem_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Химия 1'] = pd.NA
for col in chem_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Химия 1'] = 1
print(final_df['Химия 1'].value_counts())


russ_columns = ['Русский язык', 'Русский язык ВО']
for col in russ_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Русский язык 1'] = pd.NA
for col in russ_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Русский язык 1'] = 1
print(final_df['Русский язык 1'].value_counts())

o_columns = ['Обществознание', 'Обществознание (профессиональное)', 'Основы обществознания и социальной коммуникации']
for col in o_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Обществознание 1'] = pd.NA
for col in o_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Обществознание 1'] = 1
print(final_df['Обществознание 1'].value_counts())

comp_columns = ['Цветографическая композиция', 'Графическая композиция', 'Композиция', 'Композиция архитектура', 'Композиция дизайн']
for col in comp_columns:
    print(final_df.shape)
    for i in range(final_df.shape[0]):
        try:
            if col in final_df.loc[i, 'Результаты вступ. испытаний']:
                final_df.loc[i, col] = 1
            else:
                final_df.loc[i, col] = 0
        except Exception as _ex:
            final_df.loc[i, col] = 0

final_df['Композиция 1'] = pd.NA
for col in comp_columns:
    for i in range(final_df.shape[0]):
        if final_df.loc[i, col] == 1:
            final_df.loc[i, 'Композиция 1'] = 1
print(final_df['Композиция 1'].value_counts())

final_df = final_df.drop(informatics_columns, axis=1)
final_df = final_df.drop(math_columns, axis=1)
final_df = final_df.drop(history_columns, axis=1)
final_df = final_df.drop(physic_columns, axis=1)
final_df = final_df.drop(chem_columns, axis=1)
final_df = final_df.drop(russ_columns, axis=1)
final_df = final_df.drop(o_columns, axis=1)
final_df = final_df.drop(comp_columns, axis=1)
print(final_df.shape)
print(final_df.columns)
final_df.to_csv('tyuiu-interim-students.csv')