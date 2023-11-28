'''

m, n = map(int, input().split())
arr = [list(input().split()) for j in range(n)]
cnt = 0
cnt2 = 0
a, b = 0, 0
arr2 = [([0]*8) for _ in range(8)]

for i in range(m-7):
    for j in range(n-7):
       if

for i in range(7):
    for j in range(7):
'''


def solution(participant, completion):
    a = 0
    dit = {}

    for i in participant:
        dit[i] = dit.get(i, 0) + 1

    for j in participant:
        if participant[j] == 1:
            return j