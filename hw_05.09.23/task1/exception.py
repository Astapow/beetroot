# option 1
def oops(first_num, second_num):
    res = first_num / second_num
    return res


# oops(1, 2)

# option 2

try:
    print(oops(2, "2"))
except ZeroDivisionError:
    print("You can't divide by 0")
except TypeError:
    print("Enter the number ")
except IndexError:
    print("index mistake")
