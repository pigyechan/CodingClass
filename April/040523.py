'''
# 복습
N = int(input())
met = [[0 for i in range(N)] for j in range(N)]
x, y, cnt = 0, 0, 1
direct = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while cnt < N**2+1:
    if x != -1 and x != N and y != -1 and y != N and met[x][y] == 0:  # met[x][y]가 초기화 되어 있는 곳만.
        met[x][y] = cnt
        x += direction[direct % 4][0]  # %를 쓰는 이유: direction 길이가 4인데 이것을 초과해 버리면 범위 초과 에러가 남.
        y += direction[direct % 4][1]
        cnt += 1
    else:
        x -= direction[direct % 4][0]
        y -= direction[direct % 4][1]  # 이미 한 칸을 가서 범위 밖의 곳을 헤매고 있기 때문에 원래 대로 되 돌려서 잡아 줘야 함.
        direct += 1
        x += direction[direct % 4][0]
        y += direction[direct % 4][1]

for i in range(N):
    for j in range(N):
        print(f"{met[i][j]}", end = ' ')
    print()

# 백준 13458
test_room = int(input())
stud = list(map(int, input().split()))
head, second = map(int, input().split())

cnt = test_room

for i in stud:
    a = 0
    i -= head
    if i >= 0:
        a = int(i / second)
        if i % second != 0:
            cnt += (1 + a)
        else:
            cnt += a

print(cnt)


'''
import sys
sys.stdin = open("input.txt", "r")

import itertools
from collections import Counter
from collections import deque
from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    num, test = map(int, input().split(" "))
    num = list(str(num))
    num = [int(i) for i in num]
    num_sort = sorted(num, reverse=True)

    for i in range(test):
        max_idx = 0
        ch_idx = 0
        min_idx = 0
        a = []
        for m in range(len(num)):
            if num[m] != num_sort[m]:
                ch_idx = m
                a = [num[i] for i in range(ch_idx, len(num))]
                break

        for j in range(len(a)-1, -1, -1):
            if a[j] == max(a):
                max_idx = j
                break

        if len(a) != 0 and  1:
            a[max_idx], a[0] = a[0], a[max_idx]
            for n in range(len(a)):
                num[n+ch_idx] = a[n]

        else:
            b = Counter(num)
            ch = []
            nn = []
            for k, v in b.items():
                if v >= 2:
                    ch.append(k)
                    break
            if len(ch) == 0:
                num[len(num)-1], num[len(num)-2] = num[len(num)-2], num[len(num)-1]
            else:
                for s in range(len(num)):
                    if num[s] == ch[0]:
                        nn.append(s)

                num[nn[0]], num[nn[1]] = num[nn[1]], num[nn[0]]

    num = [str(i) for i in num]

    print(f"#{test_case} {''.join(num)}")
