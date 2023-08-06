"""Get data from HTML tables."""
import itertools as it
import operator as op

from ...constants import JoinWith

head, tail = (op.itemgetter(i) for i in range(2))


def get_text_from_tr_rows(table, slice_values: tuple = ()):
    """Get header text values from a table element that does not have a head and body,
    i.e. the rows are all tr elements.

    :table: an lxml table element with tr[td] elements as children
    :slice_values: a tuple of the slice wanted from the collection of rows; if empty all are returned.
    """
    if not slice_values:
        table_iterable = iter(table.xpath("//tr"))  # keep it lazy
    else:
        start, stop = slice_values
        table_iterable = it.islice(table.xpath("//tr"), start, stop)  # keep it lazy
    return [
        [
            JoinWith.SPACES(text)
            for cell in rows.iterchildren()
            if (text := [t for item in cell.itertext() if (t := item.strip())])
        ]
        for rows in table_iterable
    ]
