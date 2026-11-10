from photobank.datasource.base import DataSource

PHOTOS = [
    {'id': '1', 'kind': 'stock', 'title': 'Закат над Волгой',
     'author': 'Иван Петров', 'tags': 'природа;закат', 'date': '2025-06-01',
     'size_mb': '7.5', 'downloads': '100', 'base_price': '200',
     'width': '6000', 'height': '4000', 'license': '', 'format': ''},
    {'id': '2', 'kind': 'premium', 'title': 'Мамаев курган',
     'author': 'Анна Смирнова', 'tags': 'город;памятник', 'date': '2025-05-09',
     'size_mb': '9.1', 'downloads': '40', 'base_price': '300',
     'width': '8256', 'height': '5504', 'license': 'extended', 'format': ''},
    {'id': '3', 'kind': 'illustration', 'title': 'Иконки погоды',
     'author': 'Иван Петров', 'tags': 'иконки;вектор', 'date': '2025-03-15',
     'size_mb': '1.2', 'downloads': '250', 'base_price': '150',
     'width': '', 'height': '', 'license': '', 'format': 'svg'},
]


class ConstantDataSource(DataSource):
    """Мок-источник: небольшой постоянный список в памяти,
    используется для отладки без файлов и базы данных."""

    def __init__(self, factory=None):
        super().__init__(factory)
        self.rows = [dict(row) for row in PHOTOS]

    def get_photos(self):
        return [self.factory.create(row) for row in self.rows]

    def add_photo(self, row):
        self.factory.create(row)
        self.rows.append(dict(row))
