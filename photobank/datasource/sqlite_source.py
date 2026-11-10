import sqlite3

from photobank.datasource.base import DataSource
from photobank.datasource.csv_source import FIELDS

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    tags TEXT,
    date TEXT,
    size_mb REAL,
    downloads INTEGER,
    base_price INTEGER,
    width TEXT,
    height TEXT,
    license TEXT,
    format TEXT
)'''


class SqliteDataSource(DataSource):
    """Данные хранятся в базе SQLite."""

    def __init__(self, path, factory=None):
        super().__init__(factory)
        self.path = path
        with self._connect() as conn:
            conn.execute(CREATE_TABLE)

    def _connect(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_photos(self):
        with self._connect() as conn:
            rows = conn.execute('SELECT * FROM photos ORDER BY id').fetchall()
        return [self.factory.create(self._to_dict(row)) for row in rows]

    def add_photo(self, row):
        self.factory.create(row)
        values = [row.get(key, '') for key in FIELDS]
        if not row.get('id'):
            values[0] = None  # id назначит база данных
        with self._connect() as conn:
            conn.execute(f'INSERT INTO photos ({", ".join(FIELDS)}) '
                         f'VALUES ({", ".join("?" * len(FIELDS))})', values)

    def is_empty(self):
        with self._connect() as conn:
            return conn.execute('SELECT COUNT(*) FROM photos').fetchone()[0] == 0

    def import_rows(self, rows):
        """Заполнение базы, например из CSV-файла."""
        for row in rows:
            self.add_photo(row)

    @staticmethod
    def _to_dict(row):
        return {key: ('' if row[key] is None else str(row[key]))
                for key in row.keys()}
