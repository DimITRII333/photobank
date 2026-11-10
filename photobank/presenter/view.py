from abc import ABC, abstractmethod


class IView(ABC):
    """Интерфейс вида. Презентер управляет видом только через эти методы,
    поэтому один и тот же презентер работает и с консолью, и с веб-API."""

    @abstractmethod
    def show_photos(self, photos):
        """photos - список словарей от PhotoViewAdapter."""

    @abstractmethod
    def show_statistics(self, summary, by_kind):
        """summary - общая статистика, by_kind - статистика по типам."""

    @abstractmethod
    def show_message(self, message):
        pass
