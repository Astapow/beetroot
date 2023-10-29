def min_transposition(arr: list) -> int:
    count = 0
    count_arr = arr.count(1)

    if count_arr == 0 and len(arr) == count_arr and arr == []:
        return 0

    # ones_indices = [i for i, val in enumerate(arr) if val == 1]
    # print(ones_indices)
    for _ in arr:
        pass

    return count


assert min_transposition([1, 0, 0, 1, 1, 0]) == 1
assert min_transposition([1, 0, 0, 0, 1, 0]) == 1
assert min_transposition([1, 0, 0, 1, 1, 1]) == 1
assert min_transposition([1, 1, 1, 1, 1, 1]) == 0
assert min_transposition([]) == 0
assert min_transposition([0]) == 0
assert min_transposition([1]) == 0
assert min_transposition([1, 0, 0, 1, 0, 1]) == 1
assert min_transposition([1, 0, 1, 0, 0, 1, 1, 0, 0, 0]) == 2
assert min_transposition([1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1]) == 2
assert min_transposition([1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]) == 3
цш