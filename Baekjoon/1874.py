import sys
input = sys.stdin.readline


def check(num):
    while stack:
        temp = stack.pop()
        res.append('-')
        if num == temp:
            return True
    return False


arr = []
stack = []
res = []

n = int(input())
for _ in range(n):
    arr.append(int(input()))

flag = True
top = 0
for num in arr:
    if top < num:
        for i in range(top+1, num+1):
            stack.append(i)
            res.append('+')
        stack.pop()
        res.append('-')
        top = num

    else:
        if not check(num):
            flag = False
            break

if flag:
    for i in res:
        print(i)
else:
    print("NO")
