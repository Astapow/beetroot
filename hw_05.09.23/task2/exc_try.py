def input_errors():
    try:
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))

        res = first ** 2 / second
        return res

    except ValueError:
        print("Enter the number!")

    except ZeroDivisionError:
        print("You can't divide by 0")


input_errors()
