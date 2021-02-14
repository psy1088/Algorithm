from collections import deque

# N, L, R = 3, 5, 10  # N=맵크기, 국경선 오픈조건= L <= x <= R
# game_map = [[10, 15, 20], [20, 30, 25], [40, 22, 10]]
N, L, R = 4, 10, 50  # N=맵크기, 국경선 오픈조건= L <= x <= R
game_map = [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
visited = [[0] * N for _ in range(N)]
move_cnt = 0
q = deque()
group = deque()


def bfs(i, j):
    q.append((i, j))
    group.append((i, j))  # 연합을 이루는 그룹
    visited[i][j] = 1
    total = game_map[i][j]  # 인구수 합

    while q:
        r, c = q.popleft()
        for d in range(4):  # 상하좌우 방향 검사
            n_r = r + dr[d]
            n_c = c + dc[d]
            if 0 <= n_r < N and 0 <= n_c < N and visited[n_r][n_c] == 0:
                diff = abs(game_map[r][c] - game_map[n_r][n_c])
                if L <= diff <= R:  # 인접 국가의 차이가 L이상 R이하라면, 해당 국가 체크
                    visited[n_r][n_c] = 1
                    q.append((n_r, n_c))
                    group.append((n_r, n_c))
                    total += game_map[n_r][n_c]

    average = total // len(group)
    for r, c in group:  # 국경선을 공유하는 국가들의 평균 값 저장
        game_map[r][c] = average
    print(game_map)
# # def bfs() 끝 # #


while True:
    visited = [[0] * N for _ in range(N)]
    index = 0  # 국경선을 공유한 국가가 있는지 알아보기 위함

    for i in range(N):
        for j in range(N):
            group.clear()
            if visited[i][j] == 0:
                bfs(i, j)
                index += 1
    if index == N * N:  # 국경선을 공유한 국가가 하나도 없는 경우 break
        break
    move_cnt += 1

print(move_cnt)

