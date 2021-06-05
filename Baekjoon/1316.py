import sys
input = sys.stdin.readline


def check(s):
    temp = []
    cur = ''
    for i in s:
        if i == cur:
            continue
        else:
            if i in temp:
                return False
            else:
                temp.append(i)
                cur = i
    return True


arr = []
n = int(input())
for _ in range(n):
    arr.append(input().rstrip())

cnt = 0
for s in arr:
    if check(s):
        cnt += 1

print(cnt)
