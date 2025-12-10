import sys

import parsy
from cicodeparser.parsy import Parser, regex, seq, string

# NOTE: Expect that everything related to the language is a capital, you may need to use parsy.string() methond [[https://parsy.readthedocs.io/en/latest/ref/primitives.html#parsy.string]]

POSSIBLE_TYPES = regex(r"INT|REAL|STRING|QUALITY|TIMESTAMP|BOOL").desc(
    "Expected a type, did not find any"
)  # List of the different cicode types with ors
singleWhiteSpace = string(" ").desc("Expected whitespace, did not find any")
OptionalSingleWhiteSpace = regex(r"\s?")
paransOpen = regex(r"\s?\(").desc("Expected opening parentheses, was not found")
paransClose = regex(r"\s?\)").desc("Expected closing parentheses, was not found")


def createFunctionNameParser(StrIn: str) -> Parser:
    functionType = regex(r"(\s|INT|REAL|STRING|QUALITY|TIMESTAMP|BOOL|VOID)").desc(
        "Expected a type, did not find any"
    )  # List of the different cicode types with ors
    functionKeyword = regex(r"\s?FUNCTION\s?").desc(
        "Expected 'FUNCTION', was not found"
    )
    functionName = regex(r"\w+").desc("Expected a function name, was not found")
    ParameterName = regex(r"\w+").desc("Parameter name not found")
    functionParameter = seq(
        OptionalSingleWhiteSpace >> POSSIBLE_TYPES, singleWhiteSpace >> ParameterName
    )  # single parameter, of form TYPE paraName
    functionParameters = functionParameter.sep_by(string(","))

    fullFunction = seq(
        functionType,
        functionType >> functionKeyword >> functionName,
        paransOpen >> functionParameters << paransClose,
    )
    print(fullFunction.parse(StrIn))


def main() -> None:
    createFunctionNameParser(sys.argv[1])
