import pytest

from photobank.model.factory import PhotoFactory
from photobank.model.photo import Illustration, PremiumPhoto, StockPhoto


def make_stock():
    return StockPhoto(1, 'Лес', 'Иван', ['лес'], '2025-01-01', 5.0, 10, 200,
                      6000, 4000)


def test_stock_price():
    assert make_stock().get_price() == 200


def test_premium_price_depends_on_license():
    standard = PremiumPhoto(2, 'Горы', 'Анна', [], '2025-01-01', 9.0, 5, 300,
                            6000, 4000, 'standard')
    extended = PremiumPhoto(3, 'Горы', 'Анна', [], '2025-01-01', 9.0, 5, 300,
                            6000, 4000, 'extended')
    assert standard.get_price() == 600
    assert extended.get_price() == 900


def test_illustration_price_and_info():
    picture = Illustration(4, 'Иконки', 'Олег', [], '2025-01-01', 1.0, 0, 200,
                           'svg')
    assert picture.get_price() == 300
    assert picture.get_info() == 'вектор, svg'


def test_raster_info_in_megapixels():
    assert make_stock().get_info() == '24.0 Мп'


def test_factory_creates_right_class():
    row = {'id': '1', 'kind': 'premium', 'title': 'Т', 'author': 'А',
           'tags': 'а;б', 'date': '2025-01-01', 'size_mb': '2.5',
           'downloads': '3', 'base_price': '100', 'width': '10',
           'height': '10', 'license': 'standard', 'format': ''}
    photo = PhotoFactory().create(row)
    assert isinstance(photo, PremiumPhoto)
    assert photo.tags == ['а', 'б']


def test_factory_unknown_kind():
    with pytest.raises(ValueError):
        PhotoFactory().create({'kind': 'video'})
