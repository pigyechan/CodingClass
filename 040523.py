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

