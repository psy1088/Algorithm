import sys
input = sys.stdin.readline

s = input().rstrip()
result = 0
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if s[i-1] == '(':
            result += cnt
        else:
            result += 1

print(result)
