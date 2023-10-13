def input_errors():
    try:
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))

        result = first ** 2 / second

        print(result)
        return result

    except ZeroDivisionError:
        print("You can't divide by 0")
    except ValueError:
        print("Enter the number!")
    except IndexError:
        print("some mistake")


input_errors()
