import sys
input = sys.stdin.readline

data, len_arr = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
for i in range(5):
    data[i] = input().rstrip()
    len_arr[i] = len(data[i])

res = ''
for i in range(max(len_arr)):
    for j in range(5):
        if len_arr[j] > i:
            res += data[j][i]

print(res)
