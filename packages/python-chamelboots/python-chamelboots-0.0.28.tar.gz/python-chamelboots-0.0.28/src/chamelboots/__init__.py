"""Create Chameleon compatible HTML templates."""

__version__ = "0.0.28"

from collections import namedtuple
from enum import Enum
from typing import Sequence
from uuid import uuid4

import lxml.etree
from chameleon import PageTemplate
from lxml.html import builder as E

from .constants import JoinWith

VALID_STATEMENTS = {
    "define": "tal:define",
    "switch": "tal:switch",
    "condition": "tal:condition",
    "repeat": "tal:repeat",
    "case": "tal:case",
    "content": "tal:content",
    "replace": "tal:replace",
    "omit-tag": "tal:omit-tag",
    "attributes": "tal:attributes",
    "on-error": "tal:on-error",
}

_TalStatement = namedtuple("TalStatement", "name value")


class TalStatement(_TalStatement):
    """Define a tuple that verifies its values."""

    valid_statements = VALID_STATEMENTS

    def __init__(self, name, value):
        """Verify before init of parent."""

        for message, condition in (
            (
                f'"{name}" must be one of the following: {JoinWith.COMMASPACE(self.valid_statements.keys())}',
                name not in self.valid_statements,
            ),
        ):
            if condition:
                raise ValueError(message)
        super().__init__()


class ChameleonTemplate:
    """Create a Chameleon template string."""

    valid_statements = VALID_STATEMENTS

    def __init__(
        self,
        tag: str = "div",
        tal_statements: Sequence[TalStatement] = (),
        inner_content: str = "",
    ):
        """Initialize.
        :tag: tag name
        :tal_statements: sequence of TalStatement instances
        :inner_content: The inner content of the HTML element.
        if :inner_content: is HTML it is escaped into entities.
        """
        self._set_tal_statements(tal_statements)
        self.builder = getattr(E, tag.upper())
        # issue: keys are overwritten when they are the same, e.g. "tal:define"
        unique_ids = [uuid4().hex for _ in range(len(self.tal_statements))]
        attrib = (
            {
                f"{name}{id_}": value
                for id_, (name, value) in zip(unique_ids, self.tal_statements)
            }
            if self.tal_statements
            else dict()
        )
        self.element = self.builder(**attrib)
        self.inner_content = self.element.text = inner_content
        html_string = self.tostring()
        for uid in unique_ids:
            html_string = html_string.replace(uid, "")
        self.html_string = html_string
        self.page_template = PageTemplate(html_string)

    def _verify_tal_statements(self, tal_statements):
        """Verify tal statements."""
        if not all(isinstance(item, TalStatement) for item in tal_statements):
            raise ValueError(
                f"All tal_statements must be a sequence of constants.TalStatement instances"
            )

    def _set_tal_statements(self, tal_statements):
        """Set self.tal_statements to _TalStatement instances."""
        self._verify_tal_statements(tal_statements)
        self.tal_statements = [
            _TalStatement(self.valid_statements[item.name], item.value)
            for item in tal_statements
        ]

    def tostring(self):
        return lxml.etree.tostring(self.element, method="html").decode()

    def __getattr__(self, attr):
        """Use proxy so that attributes of Chamaleon PageTemplate can be looked up."""
        # https://nedbatchelder.com/blog/201010/surprising_getattr_recursion.html
        try:
            return getattr(self.page_template, attr)
        except AttributeError:
            return super().__getattribute__(attr)

    def __str__(self):
        return self.html_string

    def __repr__(self):
        return f"<{__class__.__name__}: '{self.html_string}'>"


_CONTENT = "content"


class TALSTATEMENTS(TalStatement, Enum):
    CONTENT = TalStatement(_CONTENT, _CONTENT)
    STRUCCONTENT = TalStatement(_CONTENT, f"structure {_CONTENT}")
    REPEAT = TalStatement("repeat", f"{_CONTENT} items")
    ATTRIBS = TalStatement("attributes", "attributes")
