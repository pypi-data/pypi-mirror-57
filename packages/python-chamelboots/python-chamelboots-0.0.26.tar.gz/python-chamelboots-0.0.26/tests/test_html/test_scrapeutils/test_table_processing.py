"""Test implementation of extracting data from tables."""
import operator as op
from string import ascii_lowercase

import pytest
from lxml import etree

from chamelboots import ChameleonTemplate as CT
from chamelboots import TalStatement as TS
from chamelboots.constants import HTML_PARSER
from chamelboots.html.scrapeutils.tables import get_text_from_tr_rows
from chamelboots.html.utils import prettify_html

TAL_CONTENT = (TS(CONTENT := "content", f"structure {CONTENT}"),)
TAL_REPEAT = (TS("repeat", "item items"), TS(CONTENT, "structure item"))

TABLE, ROW, CELL = (
    CT(tag, tal)
    for tag, tal in (("table", TAL_CONTENT,), ("tr", TAL_REPEAT,), ("td", TAL_REPEAT))
)


def cells(items):
    """Items to put into the html table."""
    return (CELL.render(items=items) for _ in range(5))


@pytest.fixture
def html_table():
    """Create an html table with items in cells."""
    return TABLE.render(content=ROW.render(items=cells(ascii_lowercase)))


@pytest.fixture
def tree(html_table):
    """Create a tree for testing."""

    return etree.fromstring(html_table, HTML_PARSER)


def test_get_text_from_tr_rows(tree):
    """Process tables and extract data from cells in rows."""

    assert all(
        op.eq("".join(text), ascii_lowercase) for text in get_text_from_tr_rows(tree)
    )
    assert all(
        op.eq("".join(text), ascii_lowercase)
        for text in get_text_from_tr_rows(tree, (1, 2))
    )
