# p375 금광
T = 2  # 테스트 케이스
n, m = 4, 4
data = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]

d = [[0] * m for _ in range(n)]
for i in range(n):
    d[i][0] = data[i * m + 0]

# 오른쪽위, 오른쪽아래, 오른쪽 중 최댓값과 더하면서 계속 저장
for c in range(1, m):
    for r in range(n):
        left_up = d[r-1][c-1] if r-1 >= 0 else 0
        left_down = d[r+1][c-1] if r+1 < n else 0
        d[r][c] = data[r * m + c] + max(d[r][c-1], left_up, left_down)

# 구해진 dp리스트에서 최댓값 구함
max_val = d[0][m-1]
for i in range(1, n):
    max_val = max(max_val, d[i][m-1])

print(max_val)
