from __future__ import annotations

from bytecode import Instr
from typing import Generator, TYPE_CHECKING

from hanual.compile.context import Context
from hanual.lang.lexer import Token
from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.nodes.dot_chain import DotChain
from hanual.util import Reply, Request, Response


if TYPE_CHECKING:
    from .arguments import Arguments


class FunctionCall[N: (Token, DotChain)](BaseNode):
    __slots__ = (
        "_name",
        "_args",
        "_lines",
        "_line_range",
    )

    def __init__(
        self,
        name: N,
        arguments: Arguments,
    ) -> None:
        self._name: N = name
        self._args: Arguments = arguments

    @property
    def name(self) -> N:
        return self._name

    @property
    def args(self) -> Arguments:
        return self._args

    def gen_code(self) -> Generator[Response | Request, Reply, None]:
        from hanual.lang.nodes.assignment import AssignmentNode

        yield Response(Instr("PUSH_NULL", location=self.get_location()))

        if isinstance(self._name, DotChain):
            yield from self._name.gen_code()

        else:
            yield Response(
                Instr("LOAD_NAME", self._name.value, location=self._name.get_location())
            )
        yield from self._args.gen_code()

        yield Response(Instr("CALL", len(self._args), location=self.get_location()))

        ctx: Context = (yield Request[Context](Request.GET_CONTEXT)).response

        if ctx.assert_instance("parent", AssignmentNode) is False:
            yield Response(Instr("POP_TOP", location=self.get_location()))

    def prepare(self) -> Generator[Request, Reply, None]:
        yield from self._name.prepare()
        yield from self._args.prepare()
