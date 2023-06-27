from __future__ import annotations


from typing import Any, Dict, TYPE_CHECKING, Union
from hanual.compile.constant import Constant

from hanual.compile.instruction import *
from hanual.compile.label import Label
from hanual.lang.errors import Error
from hanual.lang.lexer import Token
from .dot_chain import DotChain
from .base_node import BaseNode

if TYPE_CHECKING:
    from hanual.runtime import RuntimeEnvironment, ExecStatus
    from hanual.lang.errors import Error
    from .arguments import Arguments


class FunctionCall(BaseNode):
    def __init__(self: BaseNode, name: Token, arguments: Arguments) -> None:
        self._name: Union[Token, DotChain] = name
        self._args: Arguments = arguments

    @property
    def name(self) -> Token:
        return self._name

    @property
    def args(self) -> Arguments:
        return self._args

    def compile(self) -> None:
        instructions = []

        ret_lbl = Label("RETURL-LBL", mangle=True)
        fnc_reg = new_reg()

        instructions.extend(self._args.compile())

        instructions.append(MOV["O", ret_lbl])
        instructions.append(MOV[fnc_reg, self._name.value])
        instructions.append(MOV["F", fnc_reg])
        instructions.append(CALL[None])

        instructions.append(ret_lbl)

        return instructions

    def execute(self):
        raise NotImplementedError

    def get_constants(self) -> list[Constant]:
        return self._args.get_constants()

    def get_names(self) -> list[str]:
        lst = []

        lst.append(self._name.value)
        lst.extend(self._args.get_names())

        return lst

    def find_priority(self) -> list[BaseNode]:
        return []

    def as_dict(self) -> Dict[str, Any]:
        return {"args": self._args.as_dict(), "name": self._name}
