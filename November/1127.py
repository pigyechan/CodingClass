from collections import deque


def solution(pr):
    answer = []
    pr = deque(pr)

    while pr:
        a = pr.popleft()
        cnt = 0

        for i in pr:
            if i >= a:
                cnt += 1
            else:
                cnt += 1
                break

        answer.append(cnt)

    # for i in range(lent):
    #     a = pr[i]
    #     cnt = 0
    #     for j in range(i+1, lent):
    #         if a <= pr[j]:
    #             cnt += 1
    #         elif pr[j] == -1:
    #             answer.append(cnt)
    #         else:
    #             answer.append(cnt+1)
    #             break
    return answer

# deque로 접근했더니 시간초과가 뜸.