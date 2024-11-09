from pydantic import BaseModel

from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class DataSettings(BaseModel):
    raw_path: Path = BASE_DIR / "data" / "raw"
    raw_years_path: Path = BASE_DIR / "data" / "raw" / "years"
    raw_all_path: Path = BASE_DIR / "data" / "raw"
    interim_data_path: Path = BASE_DIR / "data" / "interim"
    processed_data_path: Path = BASE_DIR / "data" / "processed" / "tyuiu-dataset-model.csv"
    clustered_data_path: Path = BASE_DIR / "data" / "clustered" / "tyuiu-dataset-clustered.csv"
    clustered_groups_data_path: Path = BASE_DIR / "data" / "clustered" / "groups"


class ModelSettings(BaseModel):
    standard_scaler_path: Path = BASE_DIR / "models" / "standard-scaler.pkl"


class ReportSettings(BaseModel):
    data_report_path: Path = BASE_DIR / "reports" / "data"
    model_report_path: Path = BASE_DIR / "reports" / "model"


class Settings(BaseModel):
    data: DataSettings = DataSettings()
    models: ModelSettings = ModelSettings()
    reports: ReportSettings = ReportSettings()


settings = Settings()


institutes = {
    'ВШЦТ': ['09.03.02 Информационные системы и технологии', '09.03.01 Информатика и    вычислительная техника', '38.03.05 Бизнес-информатика', '01.03.02 Прикладная математика и информатика', '02.03.01 Математика и компьютерные науки'],
    'СТРОИН': ['08.03.01 Строительство', '08.05.02 Строительство, эксплуатация, восстановление и техническое прикрытие автомобильных дорог, мостов и тоннелей', '08.05.01 Строительство уникальных зданий и сооружений'],
    'ВИШ EG': ['21.03.01 Нефтегазовое дело'],
    'ИГИН': ['15.03.04 Автоматизация технологических процессов и производств', '21.05.02 Прикладная геология', '21.05.03 Технология геологической разведки', '27.03.04 Управление в технических системах', '05.03.01 Геология', '12.03.04 Биотехнические системы и технологии'],
    'ИСОУ': ['20.03.01 Техносферная безопасность', '21.03.02 Землеустройство и кадастры', '13.03.01 Теплоэнергетика и теплотехника', '38.03.06 Торговое дело', '27.03.03 Системный анализ и управление', '43.03.01 Сервис', '21.05.01 Прикладная геодезия', '37.03.02 Конфликтология', '43.03.03 Гостиничное дело'],
    'ИДДО': ['13.03.02 Электроэнергетика и электротехника', '23.03.03 Эксплуатация транспортно-технологических машин и комплексов', '18.03.01 Химическая технология', '23.03.01 Технология транспортных процессов', '42.03.01 Реклама и связи с общественностью', '27.03.02 Управление качеством', '45.03.04 Интеллектуальные системы в гуманитарной сфере'],
    'ИПТИ': ['15.03.01 Машиностроение', '19.03.04 Технология продукции и организация общественного питания', '22.03.01 Материаловедение и технологии материалов', '12.03.01 Приборостроение', '15.03.05 Конструкторско-технологическое обеспечение машиностроительных производств', '18.03.02 Энерго- и ресурсосберегающие процессы в химической технологии, нефтехимии и биотехнологии', '27.03.01 Стандартизация и метрология', '27.03.05 Инноватика'],
    'ИТ': ['23.03.02 Наземные транспортно-технологические комплексы', '23.05.01 Наземные транспортно-технологические средства'],
    'ИАД': ['07.03.01 Архитектура', '07.03.03 Дизайн архитектурной среды', '35.03.10 Ландшафтная архитектура']
}
