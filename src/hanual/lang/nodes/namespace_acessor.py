from __future__ import annotations

from abc import ABC

from typing import List, Any, Dict, Union, TYPE_CHECKING
from typing_extensions import Self
from .base_node import BaseNode

if TYPE_CHECKING:
    from hanual.compile import Assembler
    from hanual.lang.builtin_lexer import Token


class NamespaceAccessor(BaseNode, ABC):
    def __init__(self: BaseNode, first: Token) -> None:
        self._path: List[Token] = [first]

    def add_child(self, child: Union[Token, NamespaceAccessor]) -> Self:
        if isinstance(child, NamespaceAccessor):
            self._path.extend(child.path)

        else:
            self._path.append(child)
        return self

    @property
    def path(self):
        return self._path

    def compile(self, global_state: Assembler) -> Any:
        # we don't need to load any moduls because they are packed with the final runnable
        global_state.add_file_dep(self._path)

    def as_dict(self) -> Dict[str, Any]:
        return {"lib-path": self._path}
