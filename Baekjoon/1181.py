import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(input().rstrip())

arr = list(set(arr))
arr.sort(key=lambda x:(len(x), x))

for i in arr:
    print(i)
