from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any

from .algebraic_expr import AlgebraicExpression
from .base_node import BaseNode

if TYPE_CHECKING:
    ...


class AlgebraicFunc(BaseNode, ABC):
    __slots__ = "_name", "_expr", "_lines", "_line_range",

    def __init__(self: BaseNode, name: str, expr: AlgebraicExpression, lines: str, line_range: int) -> None:
        self._name = name
        self._expr = expr

        self._line_range = line_range
        self._lines = lines

    def compile(self) -> Any:
        raise NotImplementedError
