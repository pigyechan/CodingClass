'''
A = []
B = set([i for i in range(1, 31)])

for j in range(28):
    a = int(input())
    A.append(a)
A = set(A)
B = list(B - A)
print(min(B))
print(max(B))

#연속된 수가 있을 경우 1차이로 구하는 해법은 통하지 않음.
'''
N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]
copy = []

for m in range(M):
    i, j = map(int, input().split())
    copy = [basket[i] for i in range(N-1, 0, -1)]
    for ii in range(i - 1, j):
        basket[ii] = copy[ii]

print(b for b in basket)