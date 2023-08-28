from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, Tuple, TypeVar, Union

from hanual.lang.builtin_lexer import Token

if TYPE_CHECKING:
    from hanual.compile.constants.constant import BaseConstant


T = TypeVar("T")
N = TypeVar("N", bound="BaseNode")


class BaseNode(ABC):
    @abstractmethod
    def __init__(self: BaseNode, *nodes: Tuple[T]) -> None:
        """
        This method should take n amount of arguments,
        these are either more nodes, or raw tokens.
        """
        raise NotImplementedError

    @abstractmethod
    def compile(self, **kwargs):
        """
        This method is called if the node needs to be
        compiled, this should return a stream of bytes,
        that corresponds to valid hanual bytecode.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def get_names(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def get_constants(self) -> list[BaseConstant]:
        raise NotImplementedError

    @abstractmethod
    def find_priority(self) -> list[BaseNode]:
        raise NotImplementedError

    @staticmethod
    def get_repr(o: T) -> Union[Dict, Token]:
        # Just a convenience function that will call as_dict if it exists
        return o.as_dict() if hasattr(o, "as_dict") else o
