from collections import deque
from itertools import permutations


def solution(numbers):
    arr = []
    for i in numbers:
        a = str(i)
        arr.append(a)

    arr = list(permutations(arr, len(numbers)))
    num = []

    for j in arr:
        a = "".join(map(str, j))
        num.append(a)

    num.sort(reverse=True)

    return num[0]