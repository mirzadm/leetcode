
def parse_boolean_expr(expr_str):
    stack = []
    items_to_skip = (",", "(", ")")
    operators = ("!", "&", "|")
    for item in expr_str:
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


def calculate_boolean_operation(operator, operands):
    if operator == "!":
        if operands[0] == "f":
            return "t"
        else:
            return "f"
    if operator == "&":
        result = "t"
        for item in operands:
            if item == "f":
                result = "f"
                break
        return result
    if operator == "|":
        result = "f"
        for item in operands:
            if item == "t":
                result = "t"
                break
        return result
