### p341 연구소
# BFS 풀이
from itertools import combinations
from collections import deque

N, M = 7, 7  # 맵의 가로, 세로
game_map = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
q = deque()
empty, virus = [], []
temp_map = [[0] * M for _ in range(N)]
max_result = 0


def bfs():
    len_empty = len(empty) - 3  # 벽을 3개 세울 것을 고려해서 3을 빼줌
    for i in range(len(virus)):
        q.append(virus[i])

    while q:
        v = q.popleft()
        for d in range(4):  # 상하좌우 검사해서 0인 공간을 2로 만들어줌
            n_r = v[0] + dr[d]
            n_c = v[1] + dc[d]
            if 0 <= n_r < N and 0 <= n_c < M:
                if temp_map[n_r][n_c] == 0:
                    temp_map[n_r][n_c] = 2
                    q.append((n_r, n_c))
                    len_empty -= 1
    return len_empty
########### bfs함수 끝 ###############


# empty = 빈 공간 좌표를 담은 리스트,  virus = 바이러스 좌표를 담은 리스트
for i in range(N):
    for j in range(M):
        if game_map[i][j] == 0:
            empty.append((i, j))
        elif game_map[i][j] == 2:
            virus.append((i, j))

all_situation = list(combinations(empty, 3))  # 모든 경우의 수
for s in all_situation:  # 모든 경우의 수를 다 해봄
    for i in range(N):  # temp_map 을 game_map 과 같이 초기화
        for j in range(M):
            temp_map[i][j] = game_map[i][j]
    for x, y in s:  # 벽을 3개 세움! 1로 체크
        temp_map[x][y] = 1

    max_result = max(max_result, bfs())

print(max_result)



# # DFS 풀이
# N, M = 7, 7  # 맵의 가로, 세로
# data = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
#
# temp = [[0] * M for _ in range(N)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# result = 0
#
#
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)
#
#
# def get_score():
#     score = 0
#     for i in range(N):
#         for j in range(M):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
#
#
# def dfs(count):
#     global result
#     if count == 3:
#         for i in range(N):
#             for j in range(M):
#                 temp[i][j] = data[i][j]
#         for i in range(N):
#             for j in range(M):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         result = max(result, get_score())
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
#
#
# dfs(0)
# print(result)
