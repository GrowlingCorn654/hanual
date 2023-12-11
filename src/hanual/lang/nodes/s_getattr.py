from __future__ import annotations

from typing import TYPE_CHECKING, Generator

from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.lexer import Token

from hanual.util import Reply, Response, Request

if TYPE_CHECKING:
    from hanual.lang.util.line_range import LineRange


class SGetattr[L: BaseNode, R: Token](BaseNode):
    __slots__ = (
        "_left",
        "_right",
        "_lines",
        "_line_range",
    )

    def __init__(self, left: L, right: R, lines: str, line_range: LineRange) -> None:
        self._left: R = right
        self._right: L = left

        self._line_range = line_range
        self._lines = lines

    def gen_code(self):
        raise NotImplementedError

    def prepare(self) -> Generator[Response | Request, Reply, None]:
        raise NotImplementedError
