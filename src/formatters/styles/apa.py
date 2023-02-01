from string import Template

from src.formatters.base import BaseCitationFormatter
from src.formatters.models import (
    ArticlesCollectionModel,
    AutoReportModel,
    BookModel,
    CiteModel,
    DissertationModel,
    InternetResourceModel,
    JournalArticleModel,
    RegulationActModel,
)
from src.formatters.styles.base import BaseCitationStyle
from src.logger import get_logger

logger = get_logger(__name__)

class APABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year) $title ($edition) $city: $publishing_house, $pages p.")

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)
        values = self.data.dict()
        values["edition"] = self.get_edition()
        return self.template.substitute(values)

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template("$website ($access_date) $article $link")

    def substitute(self) -> str:
        logger.info('Форматирование из интернета "%s" ...', self.data.article)
        return self.template.substitute(self.data.dict())


class APACollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year) $article_title, $collection_title $city: $publishing_house, $pages p."
        )

    def substitute(self) -> str:
        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(self.data.dict())


class APADissertation(BaseCitationStyle):
    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author ($year) $title, дис. [$author_title $speciality_field $speciality_code] $city, $pages p."
        )

    def substitute(self) -> str:
        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APAAutoReport(BaseCitationStyle):
    data: AutoReportModel

    @property
    def template(self) -> Template:
        return Template(
            "$author ($year) $title, автореф. дис. [$author_title $speciality_field $speciality_code] $city, $pages p."
        )

    def substitute(self) -> str:
        logger.info('Форматирование автореферата "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APAJournalArticle(BaseCitationStyle):
    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year) $title. $journal, $volume $pages p.")

    def substitute(self) -> str:
        logger.info('Форматирование статьи "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APARegulationAct(BaseCitationStyle):
    data: RegulationActModel

    @property
    def template(self) -> Template:
        return Template(
            "($publication_year) $title, $act_type, $official_source, $act_number, edited $edition"
        )

    def substitute(self) -> str:
        logger.info('Форматирование законодательного акта "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APACitationFormatter(BaseCitationFormatter):
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map: dict[type[CiteModel], type[BaseCitationStyle]] = {
        BookModel: APABook,
        InternetResourceModel: APAInternetResource,
        ArticlesCollectionModel: APACollectionArticle,
        DissertationModel: APADissertation,
        AutoReportModel: APAAutoReport,
        JournalArticleModel: APAJournalArticle,
        RegulationActModel: APARegulationAct,
    }
