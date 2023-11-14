from homework_24.stack import Stack


def check_brackets(string_brackets):
    list_brackets = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for item in string_brackets:
        if item in brackets:
            list_brackets.push(item)

        elif item in brackets.values():
            if list_brackets.is_empty() or brackets[list_brackets.pop()] != item:
                return False

    return list_brackets.is_empty()


assert check_brackets("{}}{}{{}{{") is False
assert check_brackets("")
assert check_brackets("[") is False
assert check_brackets("]") is False
assert check_brackets("((){}[])")
assert check_brackets("[][{}][()]")
assert check_brackets("{}})((){") is False
assert check_brackets("{}}{}{{}{{") is False
