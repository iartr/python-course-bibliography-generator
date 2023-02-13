"""
Функции чтения исходного файла.
"""

from abc import ABC, abstractmethod

from openpyxl.workbook import Workbook

from formatters.models import CiteModel
from logger import get_logger

logger = get_logger(__name__)


class BaseReader(ABC):
    """
    Базовый класс читателя исходного файла.
    """

    def __init__(self, workbook: Workbook) -> None:
        """
        Конструктор.

        :param workbook: Рабочая книга Excel.
        """

        self.workbook = workbook

    @property
    @abstractmethod
    def model(self) -> type[CiteModel]:
        """
        Получение модели объекта (строки).

        :return: Модель объекта (строки).
        """

    @property
    @abstractmethod
    def sheet(self) -> str:
        """
        Получение наименования листа рабочей книги.

        :return: Наименование листа рабочей книги.
        """

    @property
    @abstractmethod
    def attributes(self) -> dict:
        """
        Получение списка наименований атрибутов с информацией об индексе столбца и типе данных.

        .. code-block::

            {
                "authors": 0,
                "title": 1,
                "edition": 2,
                "city": 3,
                "publishing_house": 4,
                "year": 5,
                "pages": 6,
            }

        :return: Атрибуты с информацией об индексе столбца и типе данных
        """

    def read(self) -> list[CiteModel]:
        """
        Чтение исходного файла.

        :return: Список моделей строк в виде DTO (Data Transfer Objects).
        """

        models = []
        # чтение со второй строки таблицы (первая строка содержит заголовок)
        for row in self.workbook[self.sheet].iter_rows(min_row=2):
            # обработка строки идет только, если заполнены обязательные столбцы
            if not row[0].value:
                continue
            # обработка заданных в методе `attributes()` атрибутов
            attrs = {attr: row[index].value for attr, index in self.attributes.items()}

            # добавление считанной и обработанной строки в список моделей
            models.append(self.model(**attrs))

        return models
