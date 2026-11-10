from photobank.datasource.csv_loader import load_photos
from photobank.analytics.search import SearchCriteria, search, statistics


def main():
    photos = load_photos('data/photos.csv')
    text = input('Поиск (тег или название, Enter - все): ').strip()
    found = search(photos, SearchCriteria(text=text or None))
    for p in found:
        print(p.id, p.title, '|', p.author, '|', p.kind, '|', p.get_info(),
              '|', p.get_price(), 'руб.')
    st = statistics(found)
    print('Найдено:', st['count'])
    print('Средняя цена:', round(st['avg_price'], 2))
    print('Максимальная цена:', st['max_price'])
    print('Скачиваний всего:', st['downloads'])


if __name__ == '__main__':
    main()
