from __future__ import annotations

from typing import TypeVar, Generic, Any, Dict, TYPE_CHECKING
from hanual.compile.constant import Constant
from hanual.lang.errors import Error
from hanual.lang.lexer import Token
from .base_node import BaseNode

if TYPE_CHECKING:
    from hanual.runtime.runtime import RuntimeEnvironment
    from hanual.runtime.status import ExecStatus

T = TypeVar("T", BaseNode, Token)


class AssignmentNode(BaseNode, Generic[T]):
    __slots__ = ("_target", "_value")

    def __init__(self: BaseNode, target: Token, value: T) -> None:
        self._target: Token = target
        self._value: T = value

    @property
    def target(self) -> Token:
        return self._target

    @property
    def value(self) -> T:
        return self._value

    def compile(self) -> None:
        raise NotImplementedError

    def get_constants(self) -> list[Constant]:
        # if we want to set the value to a literal then we add it as a constant
        if isinstance(self._value, Token):
            if self._value.type in ("STR", "NUM"):
                return [Constant(self._value.value)]

        return []

    def get_names(self) -> list[str]:
        return [self._target.value]

    def execute(self, rte: RuntimeEnvironment) -> ExecStatus[Error, Any]:
        return super().execute(rte)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "type": type(self).__name__,
            "name": self._target,
            "value": self._value.as_dict()
            if hasattr(self._value, "as_dict")
            else self._value,
        }
