from unittest.mock import Mock

from photobank.analytics.search import SearchCriteria
from photobank.datasource.constant_source import ConstantDataSource
from photobank.presenter.presenter import Presenter
from photobank.presenter.view import IView


class MockView(IView):
    """Подставной вид: записывает вызовы в журнал (строку Log)."""

    def __init__(self):
        self.log = ''
        self.photos = []

    def show_photos(self, photos):
        self.photos = photos
        self.log += f'show_photos({len(photos)});'

    def show_statistics(self, summary, by_kind):
        self.log += f"show_statistics({summary['count']});"

    def show_message(self, message):
        self.log += f'show_message({message});'


def test_presenter_shows_photos_and_statistics():
    view = MockView()
    Presenter(view, ConstantDataSource()).show_report()
    assert view.log == 'show_photos(3);show_statistics(3);'
    assert view.photos[0]['kind_name'] == 'Стоковое фото'


def test_presenter_reports_nothing_found():
    view = MockView()
    Presenter(view, ConstantDataSource()).show_report(
        SearchCriteria(text='космос'))
    assert view.log.startswith('show_message(По запросу ничего не найдено);')


def test_presenter_add_photo_error_is_shown():
    source = Mock()
    source.add_photo.side_effect = ValueError('плохие данные')
    view = MockView()
    assert Presenter(view, source).add_photo({}) is False
    assert 'Ошибка добавления: плохие данные' in view.log
