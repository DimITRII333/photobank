from photobank.model.photo import Illustration, PremiumPhoto, StockPhoto


class PhotoFactory:
    """Фабрика: создаёт объект нужного класса по строке данных.

    Новый тип изображения добавляется одной записью в словарь creators,
    остальной код программы при этом не меняется."""

    def __init__(self):
        self.creators = {
            'stock': self._create_stock,
            'premium': self._create_premium,
            'illustration': self._create_illustration,
        }

    def create(self, row):
        kind = row['kind']
        if kind not in self.creators:
            raise ValueError(f'Неизвестный тип изображения: {kind}')
        return self.creators[kind](row)

    @staticmethod
    def _common(row):
        return (int(row['id']), row['title'], row['author'],
                row['tags'].split(';'), row['date'], float(row['size_mb']),
                int(row['downloads']), int(row['base_price']))

    def _create_stock(self, row):
        return StockPhoto(*self._common(row), int(row['width']),
                          int(row['height']))

    def _create_premium(self, row):
        return PremiumPhoto(*self._common(row), int(row['width']),
                            int(row['height']), row['license'])

    def _create_illustration(self, row):
        return Illustration(*self._common(row), row['format'])
