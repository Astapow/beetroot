user_intput = input("Enter name file.txt: ")
name = user_intput + ".txt"


def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        char = file.read()
        return len(char)


def test(name):
    try:
        lines = count_lines(name)
        chars = count_chars(name)

        print(f"Lines: {lines}")
        print(f"Characters: {chars}")

    except FileNotFoundError:
        print(f"File '{name}' not found.")

    except Exception as exc:
        print(f"An error occurred: {exc}")


test(name)
