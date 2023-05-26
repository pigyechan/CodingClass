'''
#
N, M = map(int, input().split())
A = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    m = list(map(int, input().split()))
    for j in range(M):
        A[i][j] += m[j]

for k in range(N):
    m = list(map(int, input().split()))
    for j in range(M):
        A[k][j] += m[j]

for n in range(N):
    for m in range(M):
        print(A[n][m], end=" ")
    print()

arr = [[0 for i in range(9)] for j in range(9)]
max_num = 0
index_max = [0, 0]
for i in range(9):
    m = list(map(int, input().split()))
    for j in range(9):
        arr[i][j] = m[j]
        if arr[i][j] >= max_num:
            max_num = arr[i][j]
            index_max = [i, j]

print(max_num)
print(index_max[0]+1, index_max[1]+1)

#
max_num = 0
arr = [[] for i in range(5)]
for i in range(5):
    m = list(input())
    if len(m) > max_num:
        max_num = len(m)
    for j in range(len(m)):
        arr[i].append(m[j])

for a in range(5):
    minus = max_num - len(arr[a])
    if minus > 0:
        for i in range(minus):
            arr[a].append("")

for b in range(max_num):
    for a in range(5):
        print(arr[a][b], end="")
'''
