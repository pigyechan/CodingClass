cnt = 1
a = int(input())
num = [1, 1]
direction = [[0, 1], [1, -1], [1, 0], [-1, 1]]
while a > 1:
    a -= 1
    cnt += 1
    for i in direction:
        if sum(i):
            num[0] += i[0]
            num[1] += i[1]
            a -= 1
        else:
            num[0] += i[0] * cnt
            num[1] += i[1] * cnt
            a -= cnt

print(f"{num[0]}/{num[1]}")