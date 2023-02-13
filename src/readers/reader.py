"""
Чтение исходного файла.
"""

import openpyxl
from openpyxl.workbook import Workbook

from formatters.models import (
    ArticlesCollectionModel,
    AutoReportModel,
    BookModel,
    CiteModel,
    DissertationModel,
    InternetResourceModel,
    JournalArticleModel,
    RegulationActModel,
)
from logger import get_logger
from readers.base import BaseReader

logger = get_logger(__name__)


class BookReader(BaseReader):
    """
    Чтение модели книги.
    """

    @property
    def model(self) -> type[BookModel]:
        return BookModel

    @property
    def sheet(self) -> str:
        return "Книга"

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.

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
        """
        return {
            "authors": 0,
            "title": 1,
            "edition": 2,
            "city": 3,
            "publishing_house": 4,
            "year": 5,
            "pages": 6,
        }


class InternetResourceReader(BaseReader):
    """
    Чтение модели интернет-ресурса.
    """

    @property
    def model(self) -> type[InternetResourceModel]:
        return InternetResourceModel

    @property
    def sheet(self) -> str:
        return "Интернет-ресурс"

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.

        .. code-block::

            {
                "article": 0,
                "website": 1,
                "link": 2,
                "access_date": 3,
            }
        """
        return {
            "article": 0,
            "website": 1,
            "link": 2,
            "access_date": 3,
        }


class ArticlesCollectionReader(BaseReader):
    """
    Чтение модели сборника статей.
    """

    @property
    def model(self) -> type[ArticlesCollectionModel]:
        return ArticlesCollectionModel

    @property
    def sheet(self) -> str:
        return "Статья из сборника"

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.

        .. code-block::

            {
                "authors": 0,
                "article_title": 1,
                "collection_title": 2,
                "city": 3,
                "publishing_house": 4,
                "year": 5,
                "pages": 6,
            }
        """
        return {
            "authors": 0,
            "article_title": 1,
            "collection_title": 2,
            "city": 3,
            "publishing_house": 4,
            "year": 5,
            "pages": 6,
        }


class DissertationReader(BaseReader):
    """
    Чтение модели диссертации.
    """

    @property
    def model(self) -> type[DissertationModel]:
        return DissertationModel

    @property
    def sheet(self) -> str:
        return "Диссертация"

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.

        .. code-block::

            {
                "author": 0,
                "title": 1,
                "author_title": 2,
                "speciality_field": 3,
                "speciality_code": 4,
                "city": 5,
                "year": 6,
                "pages": 7,
            }
        """
        return {
            "author": 0,
            "title": 1,
            "author_title": 2,
            "speciality_field": 3,
            "speciality_code": 4,
            "city": 5,
            "year": 6,
            "pages": 7,
        }


class AutoReportReader(DissertationReader):
    """
    Чтение модели диссертации.
    """

    @property
    def model(self) -> type[DissertationModel]:
        return AutoReportModel

    @property
    def sheet(self) -> str:
        return "Автореферат"


class JournalArticleReader(BaseReader):
    """
    Чтение модели статьи.
    """

    @property
    def model(self) -> type[JournalArticleModel]:
        return JournalArticleModel

    @property
    def sheet(self) -> str:
        return "Статья из журнала"

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.
        .. code-block::

            {
                "authors": 0,
                "title": 1,
                "journal": 2,
                "year": 3,
                "volume": 4,
                "pages": 5,
            }
        """
        return {
            "authors": 0,
            "title": 1,
            "journal": 2,
            "year": 3,
            "volume": 4,
            "pages": 5,
        }


class RegulationActReader(BaseReader):
    """
    Чтение модели нормативного акта.
    """

    @property
    def model(self) -> type[RegulationActModel]:
        return RegulationActModel

    @property
    def sheet(self) -> str:
        return " Закон, нормативный акт и т.п."

    @property
    def attributes(self) -> dict[str, int]:
        """
        Атрибуты модели.

        .. code-block::

            {
                "act_type": 0,
                "title": 1,
                "accept_date": 2,
                "act_number": 3,
                "official_source": 4,
                "publication_year": 5,
                "version": 6,
                "article_number": 7,
                "edition": 8,
            }
        """
        return {
            "act_type": 0,
            "title": 1,
            "accept_date": 2,
            "act_number": 3,
            "official_source": 4,
            "publication_year": 5,
            "version": 6,
            "article_number": 7,
            "edition": 8,
        }


class SourcesReader:
    """
    Чтение из источника данных.
    """

    # зарегистрированные читатели
    readers: list[type[BaseReader]] = [
        BookReader,
        InternetResourceReader,
        ArticlesCollectionReader,
        DissertationReader,
        AutoReportReader,
        JournalArticleReader,
        RegulationActReader,
    ]

    def __init__(self, path: str) -> None:
        """
        Конструктор.

        :param path: Путь к исходному файлу для чтения.
        """

        logger.info("Загрузка рабочей книги ...")
        self.workbook: Workbook = openpyxl.load_workbook(path)

    def read(self) -> list[CiteModel]:
        """
        Чтение исходного файла.

        :return: Список прочитанных моделей (строк).
        """

        items = []
        for reader in self.readers:
            logger.info("Чтение %s ...", reader.__name__)
            items.extend(reader(self.workbook).read())

        return items
