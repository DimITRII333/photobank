from photobank.datasource.csv_source import CsvDataSource
from photobank.datasource.sqlite_source import SqliteDataSource


def test_csv_source_reads_all_photos():
    photos = CsvDataSource('data/photos.csv').get_photos()
    assert len(photos) == 40


def test_sqlite_import_and_read(tmp_path):
    db = SqliteDataSource(str(tmp_path / 'test.db'))
    assert db.is_empty()
    db.import_rows(CsvDataSource('data/photos.csv').read_rows()[:5])
    photos = db.get_photos()
    assert len(photos) == 5
    assert photos[0].title == 'Закат над Волгой'
