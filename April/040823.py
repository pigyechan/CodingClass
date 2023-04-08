#백준 10434
T = int(input())
for test_case in range(1, T + 1):
    P, M = map(int, input().split())
    lst = []    # 처음에 들어온 숫자가 소수인지 확인하기 위한 리스트
    yes_no = ["YES", "NO"]
    cnt = 0

    lst = [j for j in range(1, M+1) if M % j == 0] # 나눠지는 수가 있으면 들어감. 소수이면 1만 들어감.
    num_list = [str(M)]  # 처음에 들어온 숫자를 string으로 만들고 리스트에 넣음.

    if len(lst) > 2:
        print(f"{P} {M} {yes_no[1]}") # 1이거나 소수이면 len(lst) > 1이므로 여기서 프린트 해 버리고 종료

    else:
        while num_list[len(num_list) - 1] != '1':   # 최종 합이 1이 아닐 때까지 반복
            a = 0
            happy = list(num_list[len(num_list) - 1])  # 가장 마지막 숫자. but string 상태.
            for i in range(len(happy)):
                a += int(happy[i]) * int(happy[i])
            num_list.append(str(a))

            for j in range(len(num_list)-1):
                if str(a) == num_list[j]:
                    num_list.append('1')

        if num_list[len(num_list) - 1] == '1' and num_list[len(num_list) - 2] not in num_list[:len(num_list) - 3]:
            print(f"{P} {M} {yes_no[0]}")  # 최종 합이 1이면 yes 출력
        else:
            print(f"{P} {M} {yes_no[1]}")