"""Test HTML elements."""

from lxml import etree

from chamelboots.constants import FAKE
from chamelboots.constants import HTML_PARSER
from chamelboots.html.elements import get_list_of_items
from chamelboots.html.utils import prettify_html


def test_get_list_of_items():
    """Create an HTML list of items."""
    items_list = prettify_html(
        get_list_of_items(
            items=(FAKE.catch_phrase() for _ in range(10)),
            list_attribs=(list_attribs := {"class": "list-group"}),
            list_items_attribs=(
                list_items_attribs := {
                    "class": "list-group-item list-group-item-action"
                }
            ),
        )
    )
    print(items_list)
    assert (tree := etree.fromstring(items_list, HTML_PARSER))
    assert all(
        all(
            all((child.tag == "ul", child.attrib == list_attribs, bool(child.text,)))
            for child in element.iterchildren()
        )
        for element in (child for child in tree.xpath("//body"))
    )
    assert all(
        all(
            all(
                (
                    child.tag == "li",
                    child.attrib == list_items_attribs,
                    bool(child.text,),
                )
            )
            for child in element.iterchildren()
        )
        for element in (child for child in tree.xpath("//ul"))
    )
