'''
N = int(input())
met = [[0 for i in range(N)] for j in range(N)]
x, y, m = 0, 0, 0
cnt = 1
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while N**2 >= cnt:
    if y != -1 and y != N and x != -1 and x != N and met[x][y] == 0:
        met[x][y] = cnt
        x += direction[m % 4][0]
        y += direction[m % 4][1]
        cnt += 1

    else:
        x -= direction[m % 4][0]
        y -= direction[m % 4][1]
        m += 1
        x += direction[m % 4][0]
        y += direction[m % 4][1]


for i in range(N):
    for j in range(N):
        print(met[i][j], end=' ')
    print()
'''

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    apart = list(map(int, input().split()))
    cnt = 0
    b = [-2, -1, 1, 2]

    for i in range(2, N-2):
        a = []
        for j in b:
            a.append(apart[i+j])

        if apart[i] > max(a):
            cnt += apart[i] - max(a)

    print(f"#{test_case} {cnt}")
