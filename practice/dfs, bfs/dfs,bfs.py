# # p151 음료수 얼려먹기 DFS 풀이
# N, M = map(int, input().split())  # N=행의 수, M=열의 수
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))
#
#
# def dfs(row, col):
#     # 그래프 범위 내에 있고, 칸막이 부분이 0이라면 => 1로 바꿔주고, 상하좌우 재귀탐색
#     if 0 <= row < N and 0 <= col < M and graph[row][col] == 0:
#         graph[row][col] = 1
#         dfs(row + 1, col)
#         dfs(row - 1, col)
#         dfs(row, col + 1)
#         dfs(row, col - 1)
#         return True
#     else:  # 범위 초과 or 칸막이 부분이면 False
#         return False
#
#
# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j):
#             result += 1
# print(result)


# # # p151 음료수 얼려먹기 BFS 풀이
# from collections import deque
#
# N, M = 4, 5
# data = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
#
# dr = [-1, 0, 1, 0]  # 위 오 아 왼
# dc = [0, 1, 0, -1]  # 위 오 아 왼
#
# q = deque()
# cnt = 0
# # 좌표별로 확인해가면서 0인놈이 없을때까지 반복
# for i in range(N):
#     for j in range(M):
#         if data[i][j] == 1:  # 벽이거나, 방문했으면 continue
#             continue
#
#         data[i][j] = 1
#         q.append((i, j))
#         while q:  # 큐가 빌 때까지
#             v = q.popleft()
#             row, col = v[0], v[1]
#             for k in range(4):  # 상하좌우 연결되어있으면 큐에 삽입
#                 n_r, n_c = row + dr[k], col + dc[k]
#                 if 0 <= n_r < N and 0 <= n_c < M:  # 범위를 벗어나지 않았을 때
#                     if data[n_r][n_c] == 0:  # 벽이 아닌데, 방문하지 않았다면 큐에 추가
#                         q.append((n_r, n_c))
#                         data[n_r][n_c] = 1
#         cnt += 1
#
# print(cnt)


# # p152 미로탈출
from collections import deque

N, M = 5, 6
game_map = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


def bfs(r, c):
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for d in range(4): # 상하좌우 탐색해서 범위 안에 있고, 이동 가능한 경우 큐에 추가
            n_r, n_c = r + dr[d], c + dc[d]
            if 0 <= n_r < N and 0 <= n_c < M and game_map[n_r][n_c] == 1:
                q.append((n_r, n_c))
                game_map[n_r][n_c] = game_map[r][c] + 1
                if n_r == N - 1 and n_c == M - 1:  # 도착지점이면 리턴
                    return game_map[n_r][n_c]


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
q = deque()
print(bfs(0, 0))
