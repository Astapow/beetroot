def count_local_variables():
    my_list = [1, 2, 3]
    my_str = 'abc'
    my_integer = 1

    count_local = locals()
    return len(count_local)


print(count_local_variables())
