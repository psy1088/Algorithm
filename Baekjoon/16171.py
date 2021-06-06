import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

temp = ''
for i in s:
    if i.isalpha():
        temp += i

if k in temp:
    print(1)
else:
    print(0)
