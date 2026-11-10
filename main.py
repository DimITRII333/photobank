import argparse

from photobank.analytics.search import SearchCriteria
from photobank.console.console_view import ConsoleView
from photobank.datasource.constant_source import ConstantDataSource
from photobank.datasource.csv_source import CsvDataSource
from photobank.datasource.sqlite_source import SqliteDataSource
from photobank.presenter.presenter import Presenter


def create_source(name):
    if name == 'mock':
        return ConstantDataSource()
    csv_source = CsvDataSource('data/photos.csv')
    if name == 'db':
        db = SqliteDataSource('data/photos.db')
        if db.is_empty():
            db.import_rows(csv_source.read_rows())
        return db
    return csv_source


def main():
    parser = argparse.ArgumentParser(description='Фотобанк')
    parser.add_argument('--source', choices=['csv', 'db', 'mock'],
                        default='csv', help='источник данных')
    args = parser.parse_args()

    presenter = Presenter(ConsoleView(), create_source(args.source))
    while True:
        text = input('\nПоиск по названию или тегу (Enter - все, q - выход): ')
        if text.strip().lower() == 'q':
            break
        presenter.show_report(SearchCriteria(text=text.strip() or None))


if __name__ == '__main__':
    main()
