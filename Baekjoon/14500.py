# def dfs(x, y, cnt, num):
#     global result
#     if cnt == 4:
#         result = max(result, num)
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
#             visit[nx][ny] = 1
#             dfs(nx, ny, cnt + 1, num + s[nx][ny])
#             visit[nx][ny] = 0
#
#
# def middlefinger(x, y):
#     global result
#     for i in mfinger:
#         try:
#             num = s[x][y] + s[x + i[0][0]][y + i[0][1]] + s[x + i[1][0]][y + i[1][1]] + s[x + i[2][0]][y + i[2][1]]
#         except:
#             num = 0
#         result = max(result, num)
#
#
# import sys
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]],
# [[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]
# n, m = map(int, input().split())
# s = []
# visit = [[0] * m for i in range(n)]
# result = 0
#
# for i in range(n):
#     s.append(list(map(int, input().split())))
# result = 0
# for i in range(n):
#     for j in range(m):
#         visit[i][j] = 1
#         dfs(i, j, 1, s[i][j])
#         visit[i][j] = 0
#         middlefinger(i, j)
# print(result)


def exception(r, c): # dfs로는 ㅏ,ㅓ,ㅗ,ㅜ모양을 구할 수 없으므로, 따로 구해줌
    global total
    shape = [[(1, 0), (0, -1), (0, 1)], [(-1, 0), (0, -1), (0, 1)], [(0, 1), (-1, 0), (1, 0)], [(0, -1), (-1, 0), (1, 0)]]

    for s in shape: # i = [(0, 1), (-1, 0), (1, 0)] 등등..
        res = data[r][c]
        for j in s: # 해당 경우로 놓여있는 4곳이 다 범위 안에 있다면
            nr = r + j[0]
            nc = c + j[1]
            if 0 <= nr < N and 0 <= nc < M:
                res += data[nr][nc]
            else:
                res = data[r][c]
                break
        total = max(total, res)


def dfs(cnt, res, r, c): # 현재위치에서 붙어있는 4개로 만들 수 있는 최댓값 구함
    global total

    res += data[r][c]
    if cnt == 4:
        total = max(total, res)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(cnt+1, res, nr, nc)
            visited[nr][nc] = 0


import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N=행, M=열
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

total, cnt = 0, 1
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(cnt, 0, i, j)
        visited[i][j] = 0
        exception(i, j)

print(total)
