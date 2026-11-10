from photobank.presenter.view import IView


class ConsoleView(IView):
    def show_photos(self, photos):
        for p in photos:
            print(f"{p['id']:>3}  {p['title']:<28} {p['author']:<16} "
                  f"{p['kind_name']:<14} {p['info']:<12} {p['price']:>7} руб.")

    def show_statistics(self, summary, by_kind):
        print()
        print('Найдено изображений:', summary['count'])
        print('Средняя цена:', summary['avg_price'], 'руб.')
        print('Медианная цена:', summary['median_price'], 'руб.')
        print('Минимальная / максимальная цена:',
              summary['min_price'], '/', summary['max_price'], 'руб.')
        print('Скачиваний всего:', summary['downloads'])
        print('Выручка:', summary['revenue'], 'руб.')
        for row in by_kind:
            print(f"  {row['kind']}: {row['count']} шт., "
                  f"средняя цена {row['avg_price']} руб.")

    def show_message(self, message):
        print('>>', message)
