'''
**질문
1. 우선순위 큐
heappush(heap, 3)
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 5)
heappush(heap, 6)
heappush(heap, 9)
print(heap)

[1, 4, 3, 5, 6, 9]

                  1
               ↙     ↘
            4           3
         ↙    ↘        ↙
       5       6     9

이거 맞는지...?

2. lambda을 어떻게 쓰는지 잘 모르겠음...

lst = [i for i in range(10,0,-1)]
lst.sort(key = lambda x:x)

lst2 = [[1, 'abc'], [2, 'bcd'], [3, 'cde']]
lst.sort(key = lambda x:x[1], reverse = True)

print(lst)
'''


#m행 n열 초기화
m = 3
n = 2
lst = [[0 for i in range(n)] for j in range(m)]
print(lst)

'''
T = int(input())
for test_case in range(1, T + 1):
   N = int(input())
   lst = [[0 for i in range(N)] for j in range(N)]
   num = 1
   direct = 'r'
   x = 0
   y = 0

   while num <= N**2:
       if direct == 'r':
           lst[x][y] = num
           y += 1
           num += 1
           if y == N or lst[x][y] != 0: #아래로
               direct = 'd'
               y -= 1
               x += 1

       elif direct == 'd':
           lst[x][y] = num
           x += 1
           num += 1
           if x == N or lst[x][y] != 0: #왼쪽으로
               direct = 'l'
               x -= 1
               y -= 1

       elif direct == 'l':
           lst[x][y] = num
           y -= 1
           num += 1
           if y < 0 or lst[x][y] != 0: #위로
               direct = 'u'
               y += 1
               x -= 1
       else:
           lst[x][y] = num
           x -= 1
           num += 1
           if x < 0 or lst[x][y] != 0: #오른쪽으로
               direct = 'r'
               x += 1
               y += 1

   print(f"#{test_case}")
   for i in range(N):
       for j in range(N):
           print(lst[i][j], end = ' ')
       print()'
'''
'''
N = int(input())
lst = [[0 for i in range(N)] for j in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direct = 0
num = 1
x, y = 0, 0
while num <= N ** 2:
    lst[x][y] = num
    x += direction[direct%4][0]
    y += direction[direct%4][1]
    num += 1
    if x < 0 or x == N or y < 0 or y == N or lst[x][y] != 0:
        x -= direction[direct % 4][0]
        y -= direction[direct % 4][1]
        direct += 1
        x += direction[direct % 4][0]
        y += direction[direct % 4][1]

for i in range(N):
    for j in range(N):
        print(lst[i][j], end=' ')
    print()

# x, y = y, x 스왑 방법
'''

import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    #딕셔너리는 정렬이 안 됨.

    a = list(Counter(scores).items())
    a.sort(key = lambda x: x[1], reverse= True)
    print(f"#{test_case} {a[0][0]}")