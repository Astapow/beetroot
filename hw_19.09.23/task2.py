class Mathematician:

    def square_nums(self, nums: list[int]) -> list[int]:
        return [square ** 2 for square in nums]

    def remove_positives(self, nums: list[int]) -> list[int]:
        return [negative for negative in nums if negative < 0]

    def filter_leaps(self, nums: list[int]) -> list[int]:
        return [num for num in nums if not num % 4]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
