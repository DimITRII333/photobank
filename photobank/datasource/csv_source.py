import csv

from photobank.datasource.base import DataSource

FIELDS = ['id', 'kind', 'title', 'author', 'tags', 'date', 'size_mb',
          'downloads', 'base_price', 'width', 'height', 'license', 'format']


class CsvDataSource(DataSource):
    """Данные хранятся в CSV-файле."""

    def __init__(self, path, factory=None):
        super().__init__(factory)
        self.path = path

    def read_rows(self):
        with open(self.path, encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def get_photos(self):
        return [self.factory.create(row) for row in self.read_rows()]

    def add_photo(self, row):
        self.factory.create(row)  # проверяем, что строка корректна
        with open(self.path, 'a', encoding='utf-8', newline='') as f:
            csv.DictWriter(f, fieldnames=FIELDS).writerow(
                {key: row.get(key, '') for key in FIELDS})
