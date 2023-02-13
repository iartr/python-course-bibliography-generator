"""
Фикстуры для моделей объектов (типов источников).
"""
from datetime import date

import pytest

from formatters.models import (
    ArticlesCollectionModel,
    AutoReportModel,
    BookModel,
    DissertationModel,
    InternetResourceModel,
    JournalArticleModel,
    RegulationActModel,
)


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date=date(2021, 1, 1),
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def dissertation_fixture() -> DissertationModel:
    """
    Фикстура модели диссертации.

    :return: DissertationModel
    """

    return DissertationModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        author_title="д-р. / канд.",
        speciality_field="экон.",
        speciality_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=999,
    )


@pytest.fixture
def auto_report_fixture() -> AutoReportModel:
    """
    Фикстура модели автореферата.

    :return: AutoReportModel
    """

    return AutoReportModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        author_title="д-р. / канд.",
        speciality_field="экон.",
        speciality_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=999,
    )


@pytest.fixture
def journal_article_fixture() -> JournalArticleModel:
    """
    Фикстура модели статьи из журнала.

    :return: JournalArticleModel
    """

    return JournalArticleModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        journal="Научный журнал",
        year=2020,
        volume=1,
        pages="25-30",
    )


@pytest.fixture
def regulation_act_fixture() -> RegulationActModel:
    """
    Фикстура модели закона.

    :return: RegulationActModel
    """

    return RegulationActModel(
        act_type="Федеральный закон",
        title="Наука как искусство",
        accept_date=date(2021, 1, 1),
        act_number="123",
        official_source="Научный журнал",
        publication_year=2020,
        version=1,
        article_number=2,
        edition=date(2021, 1, 1),
    )
