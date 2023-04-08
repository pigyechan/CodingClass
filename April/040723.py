'''
def dfs(index, comb = []):
    if len(comb) == k:
        ans.append(comb)
        return

    for i in range(index, len(lst)):
        dfs(i + 1, comb + [lst[i]])

lst = [1, 2, 3, 4, 5]
ans = []
k = 2

dfs(0)
print(ans)

def is_promising(row) -> bool:
    for i in range(row):
        if col[row] == col[i] or abs(col[row] - col[i]) == abs(row - i): # 각 열이나 대각선과 겹치는지 판단
            return False
    return True

def back_tracking(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        col[row] = i    # row행 i열에 queen이 위치
        if is_promising(row):
            back_tracking(row + 1)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    col = ['' for i in range(n)] # 각 행의 열 번호
    cnt = 0
    back_tracking(0)

    print(f"#{test_case} {cnt}")
'''
#1208
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    lst = list(map(int, input().split()))
    a = 0
    b = 0

    while dump > 0:

        min_idx = lst.index(min(lst))
        max_idx = lst.index(max(lst))

        lst[min_idx] += 1
        lst[max_idx] -= 1
        dump -= 1

    print(f"#{test_case} {max(lst) - min(lst)}")