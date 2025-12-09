import sys

from parsy import Parser, regex

# NOTE: Expect that everything related to the language is a capital, you may need to use parsy.string() methond [[https://parsy.readthedocs.io/en/latest/ref/primitives.html#parsy.string]]

POSSIBLE_TYPES: str = r"INT|REAL|STRING|QUALITY|TIMESTAMP|BOOL|VOID"  # List of the different cicode types with ors


def createFunctionNameParser(StrIn: str) -> Parser:
    functionKeyword = regex(r"FUNCTION\s*")
    functionName = regex(r"\w+")
    functionBoth = functionKeyword >> functionName
    functionBoth.parse(StrIn)


def main() -> None:
    createFunctionNameParser(sys.argv[1])
