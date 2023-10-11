# option 1
def oops(first_num, second_num):
    res = first_num / second_num

    return res


# oops(1, 2)

# option 2

try:
    print(oops(2, 0))  # raise ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by 0")

try:
    print(oops(2, "2"))  # raise TypeError
except TypeError:
    print("Pass numbers as parameters")

try:
    raise IndexError
except IndexError:
    print("index mistake")
