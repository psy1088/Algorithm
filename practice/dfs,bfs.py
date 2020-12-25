# # p151 음료수 얼려먹기
# N, M = map(int, input().split())  # N=행의 수, M=열의 수
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))
#
#
# def dfs(row, col):
#     if row <= -1 or N <= row or col <= -1 or M <= col:  # 얼음틀의 범위를 초과했으면 리턴 False
#         return False
#     if graph[row][col] == 0:  # 방문 안되어있으면 방문처리하고, 상하좌우 확인
#         graph[row][col] = 1
#         dfs(row + 1, col)
#         dfs(row, col + 1)
#         dfs(row - 1, col)
#         dfs(row, col - 1)
#         return True
#     else:
#         return False  # 방문했으면 리턴 false
#
#
# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j):
#             result += 1
#
# print(result)


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
