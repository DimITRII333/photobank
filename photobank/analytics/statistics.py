import pandas as pd


class PhotoStatistics:
    """Агрегированная статистика по списку изображений.

    Внутри используется pandas.DataFrame, но наружу он не выходит:
    остальной код получает обычные словари."""

    def __init__(self, photos):
        self.df = pd.DataFrame([{
            'kind': p.kind,
            'price': p.get_price(),
            'downloads': p.downloads,
            'size_mb': p.size_mb,
        } for p in photos], columns=['kind', 'price', 'downloads', 'size_mb'])

    def summary(self):
        if self.df.empty:
            return {'count': 0, 'avg_price': 0, 'median_price': 0,
                    'min_price': 0, 'max_price': 0, 'downloads': 0,
                    'revenue': 0, 'size_mb': 0}
        price = self.df['price']
        return {
            'count': len(self.df),
            'avg_price': round(float(price.mean()), 2),
            'median_price': float(price.median()),
            'min_price': float(price.min()),
            'max_price': float(price.max()),
            'downloads': int(self.df['downloads'].sum()),
            'revenue': round(float((price * self.df['downloads']).sum()), 2),
            'size_mb': round(float(self.df['size_mb'].sum()), 1),
        }

    def by_kind(self):
        """Количество, средняя цена и скачивания для каждого типа."""
        if self.df.empty:
            return []
        groups = self.df.groupby('kind').agg(
            count=('price', 'size'),
            avg_price=('price', 'mean'),
            downloads=('downloads', 'sum'),
        ).round(2).reset_index()
        return groups.to_dict('records')
