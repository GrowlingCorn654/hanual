from __future__ import annotations


from hanual.compile.instruction import Instruction
from typing import NamedTuple, List, Dict
from hanual.lang.lexer import Token
from .assembler import Assembler
from .label import Label


class DepInfo(NamedTuple):
    file_deps: List[str]
    consts: List[Token]
    refs: List[str]


class CompileInfo(NamedTuple):
    instructions: List[Instruction]
    functions: Dict[str, Label]
    deps: DepInfo


class Compiler:
    def __init__(self) -> None:
        self._assembler = Assembler()

    def get_deps(self):
        return DepInfo(
            file_deps=self._assembler.file_deps,
            consts=self._assembler.constants,
            refs=self._assembler.refs,
        )

    def compile_src(self, tree):
        tree.compile(self._assembler)
        return self._assembler.instructions

    @property
    def assembler(self):
        return self._assembler

    def compile(self, tree):
        return CompileInfo(
            instructions=self.compile_src(tree),
            deps=self.get_deps(),
            functions=self._assembler.functions,
        )
