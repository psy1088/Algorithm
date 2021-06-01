import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []

i, len_arr = 0, len(arr)
while arr:
    i = (i + k-1) % len_arr
    result.append(arr.pop(i))
    len_arr -= 1

print('<%s>' % (', '.join(map(str, result))))
