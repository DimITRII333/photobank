from photobank.analytics.search import SearchCriteria, search
from photobank.analytics.statistics import PhotoStatistics
from photobank.presenter.adapter import PhotoViewAdapter


class Presenter:
    def __init__(self, view, source):
        self.view = view
        self.source = source

    def set_source(self, source):
        self.source = source

    def show_report(self, criteria=None):
        criteria = criteria or SearchCriteria()
        found = search(self.source.get_photos(), criteria)
        if not found:
            self.view.show_message('По запросу ничего не найдено')
        self.view.show_photos([PhotoViewAdapter.to_view(p) for p in found])
        statistics = PhotoStatistics(found)
        self.view.show_statistics(statistics.summary(), statistics.by_kind())

    def add_photo(self, row):
        try:
            self.source.add_photo(row)
        except (KeyError, ValueError) as error:
            self.view.show_message(f'Ошибка добавления: {error}')
            return False
        self.view.show_message('Изображение добавлено')
        return True
