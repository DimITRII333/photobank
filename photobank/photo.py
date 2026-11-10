from abc import ABC, abstractmethod

PIXELS_IN_MEGAPIXEL = 1_000_000
PREMIUM_MULTIPLIER = 2
EXTENDED_LICENSE_MULTIPLIER = 3
ILLUSTRATION_MULTIPLIER = 1.5


class Photo(ABC):
    """Базовый класс для всех изображений фотобанка."""

    def __init__(self, id, title, author, tags, date, size_mb, downloads,
                 base_price):
        self.id = id
        self.title = title
        self.author = author
        self.tags = tags
        self.date = date
        self.size_mb = size_mb
        self.downloads = downloads
        self.base_price = base_price

    @property
    @abstractmethod
    def kind(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class RasterPhoto(Photo):
    """Растровая фотография: у неё есть разрешение в пикселях."""

    def __init__(self, id, title, author, tags, date, size_mb, downloads,
                 base_price, width, height):
        super().__init__(id, title, author, tags, date, size_mb, downloads,
                         base_price)
        self.width = width
        self.height = height

    def get_info(self):
        mp = self.width * self.height / PIXELS_IN_MEGAPIXEL
        return str(round(mp, 1)) + ' Мп'


class StockPhoto(RasterPhoto):
    kind = 'stock'

    def get_price(self):
        return self.base_price


class PremiumPhoto(RasterPhoto):
    kind = 'premium'

    def __init__(self, id, title, author, tags, date, size_mb, downloads,
                 base_price, width, height, license):
        super().__init__(id, title, author, tags, date, size_mb, downloads,
                         base_price, width, height)
        self.license = license

    def get_price(self):
        if self.license == 'extended':
            return self.base_price * EXTENDED_LICENSE_MULTIPLIER
        return self.base_price * PREMIUM_MULTIPLIER


class Illustration(Photo):
    kind = 'illustration'

    def __init__(self, id, title, author, tags, date, size_mb, downloads,
                 base_price, fmt):
        super().__init__(id, title, author, tags, date, size_mb, downloads,
                         base_price)
        self.fmt = fmt

    def get_price(self):
        return self.base_price * ILLUSTRATION_MULTIPLIER

    def get_info(self):
        return 'вектор, ' + self.fmt
