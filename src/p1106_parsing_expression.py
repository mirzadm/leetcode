"""Problem 1106: Parsing a boolean expression."""

from typing import List


def parse_boolean_expr(expression: str) -> bool:
    """Parses and calculates a boolean expression.

    Assumes expression is correctly formatted (operators, operators, balanced
    parentheses).

    Args:
        `expression`: String boolean expression. Supported operators: !, &, |.
            Supported operands: f, t.
    Returns:
        Boolean value of `expression`.
    """
    stack = []
    items_to_skip = (" ", ",", "(", ")")
    operators = ("!", "&", "|")
    for item in expression:
        if item not in items_to_skip:
            stack.append(item)
        if item == ")":
            operands = []
            prev_item = stack.pop()
            while prev_item not in operators:
                operands.append(prev_item)
                prev_item = stack.pop()
            new_item = calculate_boolean_operation(prev_item, operands)
            stack.append(new_item)
    result = stack.pop()
    return result == "t"


def calculate_boolean_operation(operator: str, operands: List[str]) -> str:
    """Calculates result of `operator` applied on `operands`.

    Args:
        `expression`: String boolean expression.
            Supported operators: !, &, |
            Supported operands: f, t
    Returns:
        Corresponding character for boolean result: "f" or "t"
    """
    if operator == "!":
        result = "t"
        if operands[0] == "t":
            result = "f"
    elif operator == "&":
        result = "t"
        for item in operands:
            if item == "f":
                result = "f"
                break
    elif operator == "|":
        result = "f"
        for item in operands:
            if item == "t":
                result = "t"
                break
    return result
