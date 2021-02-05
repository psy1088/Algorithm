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


# p152 미로탈출
from collections import deque

N, M = map(int, input().split())  # N=행의 수, M=열의 수

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

#    동  서  남  북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    dis = 1

    while q:
        r, c = q.popleft()
        if (r, c) == (N - 1, M - 1):  # pop한 좌표가 도착점이라면 이 좌표의 값을 리턴
            return graph[N - 1][M - 1]

        for i in range(4):  # 동서남북 순으로 이동 가능한 길인지 확인
            next_r = r + dr[i]
            next_c = c + dc[i]
            # 그래프의 범위를 초과했거나, 다음 이동할 좌표가 0 이면 건너뜀
            if next_r <= -1 or N <= next_r or next_c <= -1 or M <= next_c or graph[next_r][next_c] == 0:
                continue
            elif graph[next_r][next_c] == 1:
                # 이동가능한 길이면 q에 넣고, 1 증가시킨 값을 해당 좌표에 저장해줌(시작위치로부터의 거리를 나타냄)
                q.append((next_r, next_c))
                graph[next_r][next_c] = graph[r][c] + 1


print(bfs(0, 0))



