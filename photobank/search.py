from dataclasses import dataclass


@dataclass
class SearchCriteria:
    """Условия поиска. Пустое поле означает «не фильтровать по нему»."""
    text: str = None
    author: str = None
    kind: str = None
    min_price: float = None
    max_price: float = None

    def matches(self, photo):
        return (self._matches_text(photo)
                and (not self.author or photo.author == self.author)
                and (not self.kind or photo.kind == self.kind)
                and self._matches_price(photo.get_price()))

    def _matches_text(self, photo):
        if not self.text:
            return True
        text = self.text.lower()
        return (text in photo.title.lower()
                or text in [tag.lower() for tag in photo.tags])

    def _matches_price(self, price):
        if self.min_price is not None and price < self.min_price:
            return False
        if self.max_price is not None and price > self.max_price:
            return False
        return True


def search(photos, criteria):
    return [p for p in photos if criteria.matches(p)]


def statistics(photos):
    if len(photos) == 0:
        return {'count': 0, 'avg_price': 0, 'max_price': 0, 'downloads': 0}
    s = 0
    m = 0
    d = 0
    for p in photos:
        s += p.get_price()
        if p.get_price() > m:
            m = p.get_price()
        d += p.downloads
    return {'count': len(photos), 'avg_price': s / len(photos),
            'max_price': m, 'downloads': d}
