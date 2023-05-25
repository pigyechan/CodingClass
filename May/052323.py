'''
#
a = int(input())
for i in range(a-1, -1, -1):
    print(" "*i+"*"*(a-i))
    a += 1
a = a-1
for j in range(1, a, 1):
    print(" "*j+"*"*(a-j-1))
    a -= 1
#
from collections import Counter
a = input().upper()
b = []
for i in a:
    b.append(i)

c = Counter(b).most_common(2)
if len(c) == 1:
    print(c[0][0])
elif c[0][1] == c[1][1]:
    print("?")
else:
    print(c[0][0])

#
C = int(input())
for i in range(C):
    result = 0
    num = 0
    a = 0
    N = list(map(int, input().split()))
    b = N[0]
    M = N[1:b+2]
    result = sum(M)/b
    for m in M:
        if m > result:
            num += 1
    a = num / b * 100
    print(f"{a:.3f}"+"%")
'''