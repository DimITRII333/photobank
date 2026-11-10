KIND_NAMES = {
    'stock': 'Стоковое фото',
    'premium': 'Премиум-фото',
    'illustration': 'Иллюстрация',
}


class PhotoViewAdapter:
    """Адаптер: преобразует объект Photo в словарь, который удобно
    показывать пользователю (в консоли или в JSON-ответе)."""

    @staticmethod
    def to_view(photo):
        return {
            'id': photo.id,
            'kind': photo.kind,
            'kind_name': KIND_NAMES.get(photo.kind, photo.kind),
            'title': photo.title,
            'author': photo.author,
            'tags': ', '.join(photo.tags),
            'date': photo.date,
            'info': photo.get_info(),
            'price': photo.get_price(),
            'downloads': photo.downloads,
        }
