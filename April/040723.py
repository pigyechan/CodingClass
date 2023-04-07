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