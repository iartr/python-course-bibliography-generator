import pytest

from formatters.base import BaseCitationFormatter
from formatters.styles.apa import APACitationFormatter
from formatters.styles.gost import GOSTCitationFormatter
from main import CitationEnum, get_citation_classes
from renderer import Renderer
from readers.renderer import APARenderer, GOSTRenderer


@pytest.mark.parametrize(
    "citation, renderer, formatter",
    [
        (CitationEnum.GOST, GOSTRenderer, GOSTCitationFormatter),
        (CitationEnum.APA, APARenderer, APACitationFormatter),
        ("abacaba", GOSTRenderer, GOSTCitationFormatter),
    ],
)
def test_get_formatted(
    citation: str, renderer: Renderer, formatter: BaseCitationFormatter
) -> None:
    """
    Тестирование получения форматированной строки.

    :param citation: Стиль цитирования
    :param renderer: Класс для рендеринга
    :param formatter: Класс для форматирования

    :return: None
    """
    real_formatter, real_renderer = get_citation_classes(citation)
    assert real_renderer == renderer
    assert real_formatter == formatter
