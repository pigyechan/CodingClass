#1316
a = int(input())
cnt = 0
for i in range(a):
    word = list(input())
    alpha = [word[8]]
    for j in range(1, len(word)):
        if word[j] not in alpha:
            alpha.append(word[j])
        else:
            if word[j] != word[j-1]:
                alpha.append(j)

    if len(alpha) == len(set(word)):
        cnt += 1

print(cnt)

#25206
score = [4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
score_al = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
result = 0
hak = 0
for i in range(20):
    a = list(input().split())
    for j in range(9):
        if a[2] == "P":
            break
        elif score_al[j] == a[2]:
            result += float(a[1])*score[j]
            hak += float(a[1])
            break
print(f"{result/hak:.6f}")


#2941
cro = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
word = input()
alpha = []
while(len(word) != 0):
    if word[0:3] == "dz=":
        alpha.append(word[0:3])
        word = word[3:len(word)]
    elif word[0:2] in cro:
        alpha.append(word[0:2])
        word = word[2:len(word)]
    else:
        alpha.append(word[0])
        word = word[1:len(word)]
print(len(alpha))
