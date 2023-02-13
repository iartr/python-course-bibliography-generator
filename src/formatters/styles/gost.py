"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from formatters.base import BaseCitationFormatter
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
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class GOSTBook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. – $edition$city: $publishing_house, $year. – $pages с."
        )

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


class GOSTInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article // $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)
        return self.template.substitute(self.data.dict())


class GOSTCollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $collection_title. – $city: $publishing_house, $year. – С. $pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(self.data.dict())


class GOSTDissertation(BaseCitationStyle):
    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $title: дис. $author_title $speciality_field: $speciality_code $city $year. $pages c."
        )

    def substitute(self) -> str:
        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class GOSTAutoReport(BaseCitationStyle):
    data: AutoReportModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $title: автореф. дис. $author_title $speciality_field: $speciality_code $city $year. $pages c."
        )

    def substitute(self) -> str:
        logger.info('Форматирование автореферата "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class GOSTJournalArticle(BaseCitationStyle):
    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template("$authors $title // $journal. $year. № $volume. С. $pages.")

    def substitute(self) -> str:
        logger.info('Форматирование статьи "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class GOSTRegulationAct(BaseCitationStyle):
    data: RegulationActModel

    @property
    def template(self) -> Template:
        return Template(
            "$title: $act_type от $accept_date. №$act_number: в ред. от $edition // $official_source $publication_year"
        )

    def substitute(self) -> str:
        logger.info('Форматирование законодательного акта "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class GOSTCitationFormatter(BaseCitationFormatter):
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map: dict[type[CiteModel], type[BaseCitationStyle]] = {
        BookModel: GOSTBook,
        InternetResourceModel: GOSTInternetResource,
        ArticlesCollectionModel: GOSTCollectionArticle,
        DissertationModel: GOSTDissertation,
        AutoReportModel: GOSTAutoReport,
        JournalArticleModel: GOSTJournalArticle,
        RegulationActModel: GOSTRegulationAct,
    }
