nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    result = nums.copy()
    result.sort()

    if result[0] >= 0:
        return func1(nums)
    else:
        return func2(nums)
    

print(choose_func(nums1, square_nums, remove_negatives))

print(choose_func(nums2, square_nums, remove_negatives))

