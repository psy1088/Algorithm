# p344 경쟁적 전염
n, k = 3, 3  # n = 맵 크기,  k = 바이러스 종류 수
data_map = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
s, x, y = 2, 3, 2  # s = 초, x,y = 좌표

virus = [[] for _ in range(k + 1)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

empty, time = 0, 0  # 빈 공간의 좌표 저장, 시간 저장
for i in range(n):  # 바이러스 종류별로 리스트에 좌표를 저장
    for j in range(n):
        val = data_map[i][j]
        if val != 0:
            virus[val].append((i, j))
        else:
            empty += 1

# 빈 공간이 0이 될 때까지 반복
while 0 < empty:
    time += 1
    for i in range(1, k + 1):  # 바이러스 숫자 작은수부터 먼저 증식
        v = virus[i]
        for l_v in range(len(v)):  # 바이러스i의 개수만큼 반복
            for d in range(4):  # 상하좌우 증식
                n_r = v[l_v][0] + dr[d]
                n_c = v[l_v][1] + dc[d]
                # 상하좌우 값중에, 범위 안에 있고 빈 공간이면 증식
                if 0 <= n_r < n and 0 <= n_c < n and data_map[n_r][n_c] == 0:
                    data_map[n_r][n_c] = i
                    virus[i].append((n_r, n_c))
                    empty -= 1
    print(data_map)
    if time == s:  # s초 후 break
        break

print(data_map[x - 1][y - 1])
