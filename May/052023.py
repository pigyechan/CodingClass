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