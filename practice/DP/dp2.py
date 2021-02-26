# p376 정수 삼각형
n = 5
data = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1, n):
    for j in range(i+1):
        up_left = data[i-1][j-1] if j-1 >= 0 else 0
        up_right = data[i-1][j] if j != i else 0
        data[i][j] = data[i][j] + max(up_left, up_right)

print(max(data[n-1]))
