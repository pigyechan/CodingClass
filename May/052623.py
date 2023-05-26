#2563
num = int(input())
paper = [[0 for i in range(100)] for j in range(100)]
cnt = 0
for i in range(num):
    m, n = map(int, input().split())
    for j in range(10):
        for l in range(10):
            if paper[m+j][n+l] == 0:
                paper[m+j][n+l] = 1

for m in range(100):
    for n in range(100):
        if paper[m][n] == 1:
            cnt+=1
print(cnt)

'''
생각의 사고를 넓혀준 문제

전체 넓이에서 겹치는 부분을 빼는 것이 최선이라고 생각했었음.

리스트의 특성을 사용해서 1로 채워주고 아님 지나치고를 반복한 뒤,
1의 숫자를 세어주는 방법... 똑똑하다
'''