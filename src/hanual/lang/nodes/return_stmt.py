from __future__ import annotations

from typing import TYPE_CHECKING, Generator

from .base_node import BaseNode
from hanual.util import Reply, Request

if TYPE_CHECKING:
    from hanual.lang.util.line_range import LineRange
    from hanual.lang.lexer import Token


class ReturnStatement[V: (Token, BaseNode)](BaseNode):
    __slots__ = (
        "_value",
        "_lines",
        "_line_range",
    )

    def __init__(self, value: V, lines: str, line_range: LineRange) -> None:
        self._value: V = value

        self._line_range = line_range
        self._lines = lines

    @property
    def value(self) -> V:
        return self._value

    def gen_code(self):
        raise NotImplementedError

    def prepare(self) -> Generator[Request, Reply, None]:
        raise NotImplementedError
