from __future__ import annotations

from typing import TYPE_CHECKING

from .base_node import BaseNode

if TYPE_CHECKING:
    from hanual.lang.lexer import Token
    from hanual.lang.util.line_range import LineRange

    from .block import CodeBlock
    from .parameters import Parameters


class FunctionDefinition(BaseNode):
    __slots__ = (
        "_name",
        "_parameters",
        "_inner",
        "_lines",
        "_line_range",
    )

    def __init__(
            self,
            name: Token,
            params: Parameters,
            inner: CodeBlock,
            lines: str,
            line_range: LineRange,
    ) -> None:
        self._name: Token = name
        self._parameters = params
        self._inner = inner

        self._line_range = line_range
        self._lines = lines

    @property
    def name(self) -> Token:
        return self._name

    @property
    def arguments(self) -> Parameters:
        return self._parameters

    @property
    def inner(self) -> CodeBlock:
        return self._inner

    def compile(self):
        raise NotImplementedError
