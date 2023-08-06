from ... import TALSTATEMENTS as TS
from ... import ChameleonTemplate as CT


def get_list_of_items(
    items=(), ordered=False, list_attribs=None, list_items_attribs=None
):
    """Return list of items in HTML."""
    list_attribs = dict() if list_attribs is None else list_attribs
    list_items_attribs = dict() if list_items_attribs is None else list_items_attribs
    list_tag = "ol" if ordered is True else "ul"
    list_items = CT("li", (TS.STRUCCONTENT, TS.ATTRIBS, TS.REPEAT)).render(
        items=items, attributes=list_items_attribs
    )
    return CT(list_tag, (TS.STRUCCONTENT, TS.ATTRIBS)).render(
        content=list_items, attributes=list_attribs
    )
