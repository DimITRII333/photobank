import pytest

from photobank.analytics.search import SearchCriteria, search
from photobank.analytics.statistics import PhotoStatistics
from photobank.datasource.constant_source import ConstantDataSource


@pytest.fixture
def photos():
    # 3 изображения: цены 200, 900 и 225
    return ConstantDataSource().get_photos()


def test_search_by_tag(photos):
    found = search(photos, SearchCriteria(text='вектор'))
    assert [p.id for p in found] == [3]


def test_search_by_title_ignores_case(photos):
    found = search(photos, SearchCriteria(text='мамаев'))
    assert [p.id for p in found] == [2]


def test_search_by_author_and_price(photos):
    criteria = SearchCriteria(author='Иван Петров', max_price=210)
    assert [p.id for p in search(photos, criteria)] == [1]


def test_empty_criteria_returns_all(photos):
    assert len(search(photos, SearchCriteria())) == 3


def test_statistics_summary(photos):
    summary = PhotoStatistics(photos).summary()
    assert summary['count'] == 3
    assert summary['avg_price'] == pytest.approx(441.67)
    assert summary['median_price'] == 225
    assert summary['max_price'] == 900
    assert summary['downloads'] == 390


def test_statistics_of_empty_list():
    assert PhotoStatistics([]).summary()['count'] == 0
    assert PhotoStatistics([]).by_kind() == []
