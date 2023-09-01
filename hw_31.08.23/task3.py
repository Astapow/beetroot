def make_operation(operator, *args):
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    else:
        return "Invalid operator"

    return result


res = make_operation('+', 7, 7, 2)
print(res)
