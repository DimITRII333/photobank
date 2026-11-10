class Photo:
    """Фотография (или иллюстрация) в фотобанке."""

    def __init__(self, id, kind, title, author, tags, date, size_mb,
                 downloads, base_price, width=0, height=0, license='',
                 fmt=''):
        self.id = id
        self.kind = kind
        self.title = title
        self.author = author
        self.tags = tags
        self.date = date
        self.size_mb = size_mb
        self.downloads = downloads
        self.base_price = base_price
        self.width = width
        self.height = height
        self.license = license
        self.fmt = fmt

    def get_price(self):
        if self.kind == 'stock':
            return self.base_price
        elif self.kind == 'premium':
            if self.license == 'extended':
                return self.base_price * 3
            else:
                return self.base_price * 2
        elif self.kind == 'illustration':
            return self.base_price * 1.5
        else:
            return self.base_price

    def get_info(self):
        if self.kind == 'illustration':
            return 'вектор, ' + self.fmt
        else:
            mp = self.width * self.height / 1000000
            return str(round(mp, 1)) + ' Мп'
