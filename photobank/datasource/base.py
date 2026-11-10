from abc import ABC, abstractmethod

from photobank.model.factory import PhotoFactory


class DataSource(ABC):
    """Источник данных фотобанка. Конкретный источник (файл, БД, мок)
    выбирается снаружи, остальной код работает только с этим интерфейсом."""

    def __init__(self, factory=None):
        self.factory = factory or PhotoFactory()

    @abstractmethod
    def get_photos(self):
        """Возвращает список объектов Photo."""

    @abstractmethod
    def add_photo(self, row):
        """Добавляет изображение, row - словарь с полями как в CSV."""
