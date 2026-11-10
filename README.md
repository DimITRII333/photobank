# Фотобанк

Курсовая работа по дисциплине "Технологии программирования".
Тема: фотобанк с поиском данных по нему.

## Часть 1: консольное приложение

Приложение хранит список изображений трёх типов (стоковое фото, премиум-фото, иллюстрация),
ищет по названию, тегам, автору, типу и цене и считает статистику по найденным изображениям:
количество, среднюю, медианную, минимальную и максимальную цену, скачивания и выручку.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py --source csv     # данные из data/photos.csv
python main.py --source db      # данные из SQLite (data/photos.db, создаётся из CSV)
python main.py --source mock    # небольшой постоянный список в памяти

pytest                          # модульные тесты
```

## Структура

| Пакет | Содержимое |
|---|---|
| `photobank/model` | иерархия классов изображений, фабрика `PhotoFactory` |
| `photobank/analytics` | поиск (`SearchCriteria`) и статистика (`PhotoStatistics`) |
| `photobank/datasource` | интерфейс `DataSource` и источники: CSV, SQLite, мок |
| `photobank/presenter` | `Presenter`, интерфейс вида `IView`, адаптер `PhotoViewAdapter` |
| `photobank/console` | консольный вид |
