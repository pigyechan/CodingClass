import itertools
from collections import Counter
from collections import deque
from collections import defaultdict

T = int(input())

def find(ano_num, len_num):
    result = []
    idx = [i for i in range(len_num)]
    idx_com = itertools.combinations(idx, 2)

    for i in idx_com:
        ano_num[i[0]], ano_num[i[1]] = ano_num[i[1]], ano_num[i[0]]
        ano_num = [str(i) for i in ano_num]
        result.append(int(''.join(ano_num)))

    return result

for test_case in range(1, T + 1):
    num, test = map(int, input().split(" "))
    num = list(str(num))
    len_num = len(num)
    num = [int(i) for i in num]
    result = []
    a = 0

    for i in range(test):
        if i != test:
            for j in
                ano_num = num
                num = find(ano_num, len_num)
        else:
            break
