from typing import List, Tuple


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []  # O(1)
    for el_first_list in first_list:  # O(n)
        if el_first_list in second_list:  # O(1)
            res.append(el_first_list)  # O(n)
    return res  # res = 1 + n + 1 + n = 2 + 2n = 2n = O(n)


def question2(n: int) -> int:
    for _ in range(10):  # O(1)
        n **= 3  # O(1)
    return n  # res = O(1)


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:  # O(n)
        flag = False  # 1
        for check in temp:  # O(n)
            if el_second_list == check:  # 1
                flag = True  # 1
                break
        if not flag:  # 1
            temp.append(second_list)  # 1
    return temp  # res = (n + 1) * (n + 1) = n * n = O(n^2)


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:  # O(n)
        if el > res:  # 1
            res = el
    return res  # O(n)


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            res.append((i, j))  # 1
    return res  # n * n + 1 = O(n^2)


def question6(n: int) -> int:
    while n > 1:  # O(n)
        n /= 2  # 1
    return n  # O(n)
