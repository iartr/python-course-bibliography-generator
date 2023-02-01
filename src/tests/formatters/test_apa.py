"""
Тестирование функций оформления списка источников по APA
"""

from src.formatters.models import (
    ArticlesCollectionModel,
    AutoReportModel,
    BookModel,
    DissertationModel,
    InternetResourceModel,
    JournalArticleModel,
    RegulationActModel,
)
from src.formatters.styles.apa import (
    APAAutoReport,
    APABook,
    APACitationFormatter,
    APACollectionArticle,
    APADissertation,
    APAInternetResource,
    APAJournalArticle,
    APARegulationAct,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство (3-е изд. – ) СПб.: Просвещение, 999 p."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости (01.01.2021) Наука как искусство https://www.vedomosti.ru"
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство, Сборник научных трудов СПб.: АСТ, 25-30 p."
        )

    def test_citation_formatter(  # pylint: disable=too-many-arguments
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_fixture: DissertationModel,
        auto_report_fixture: AutoReportModel,
        journal_article_fixture: JournalArticleModel,
        regulation_act_fixture: RegulationActModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :param AutoReportModel auto_report_fixture: Фикстура модели автореферата
        :param JournalArticleModel journal_article_fixture: Фикстура модели статьи журнала
        :param RegulationActModel regulation_act_fixture: Фикстура модели нормативного акта

        :return:
        """

        models = [
            regulation_act_fixture,
            articles_collection_model_fixture,
            auto_report_fixture,
            journal_article_fixture,
            internet_resource_model_fixture,
            dissertation_fixture,
            book_model_fixture,
        ]
        results = APACitationFormatter(models).format()
        expected = [
            APARegulationAct(regulation_act_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APAAutoReport(auto_report_fixture),
            APADissertation(dissertation_fixture),
            APABook(book_model_fixture),
            APACollectionArticle(articles_collection_model_fixture),
            APAJournalArticle(journal_article_fixture),
        ]
        # тестирование сортировки списка источников
        for result, exp in zip(results, expected):
            assert result.substitute() == exp.substitute()

    def test_dissertation(self, dissertation_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертации.

        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertation(dissertation_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2020) Наука как искусство, дис. [д-р. / канд. экон. 01.01.01] СПб., 999 p."
        )

    def test_auto_report(self, auto_report_fixture: AutoReportModel) -> None:
        """
        Тестирование форматирования автореферата.

        :param AutoReportModel auto_report_fixture: Фикстура модели автореферата
        :return:
        """

        model = APAAutoReport(auto_report_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2020) Наука как искусство, автореф. дис. [д-р. / канд. экон. 01.01.01] СПб., 999 p."
        )

    def test_journal_article(
        self, journal_article_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования статьи журнала.

        :param JournalArticleModel journal_article_fixture: Фикстура модели статьи журнала
        :return:
        """

        model = APAJournalArticle(journal_article_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство. Научный журнал, 1 25-30 p."
        )

    def test_regulation_act(self, regulation_act_fixture: RegulationActModel) -> None:
        """
        Тестирование форматирования нормативного акта.

        :param RegulationActModel regulation_act_fixture: Фикстура модели нормативного акта
        :return:
        """

        model = APARegulationAct(regulation_act_fixture)

        assert (
            model.formatted
            == "(2020) Наука как искусство, Федеральный закон, Научный журнал, 123, edited 01.01.2021"
        )
