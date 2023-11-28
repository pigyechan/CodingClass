'''
#2745
a, b = map(list, input().split())
a.reverse()
b = int(''.join(b))
result = 0

lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(a)):
    result += lists.index(a[i]) * (b ** a.index(a[i]))
    a[i] = "none"

print(result)

lists 안에 있던 숫자들도 문자처리를 해줘야 되는데 당연히 숫자로 처리했던 것이 문제.
숫자가 포함된 수를 집어넣으니 바로 valueerror가 뜸

a, b = map(int, input().split())
arr = []
c = 0

while (a >= b):
    c = a % b
    a = a // b
    arr.append(c)
arr.append(a)

lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

arr.reverse()

for i in range(len(arr)):
    arr[i] = lists[arr[i]]

print(''.join(arr))

a, b, v = map(int, input().split())
v1 = v - a
cnt = v1 // (a-b)
na = v1 % (a-b)

if na == 0:
    print(cnt + 1)
elif na > 0:
    print(cnt + 2)

T = int(input())
coin = [25, 10, 5, 1]

for i in range(T):
    result = []
    a = int(input())
    for j in coin:
        rest = a // j
        a = a % j
        result.append(rest)

    for m in result:
        print(m, end = " ")


a = int(input())
cho = 2
for i in range(a):
    num = 2 * cho -1
    cho = num
print(num**2)
'''
num = int(input()) - 1
cnt = 1
a = 6

while num > 0:
    num -= a
    cnt += 1
    a = 6 * cnt

print(cnt)