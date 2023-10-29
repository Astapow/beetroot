def fibonnacci(n):
    if n <= 1:
        return n

    first_list = [1, 1]

# 0, 1, 1, 2, 3, 5...

    while len(first_list) < n:  # [0, 1, 2, 3...]
        first_list.append(first_list[-1] + first_list[-2])
        print(first_list)

    return first_list[-1]

print(fibonnacci(10))
my_tuple = (1, 2, 3)
print(type(my_tuple))
