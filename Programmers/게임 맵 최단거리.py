from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(maps, start):
    n, m = len(maps), len(maps[0])
    q = deque([start])
    maps[start[0]][start[1]] = 2

    while q:
        r, c = q.popleft()

        for d in range(4):
            n_r = r + dr[d]
            n_c = c + dc[d]
            if 0 <= n_r < n and 0 <= n_c < m:
                if maps[n_r][n_c] == 1:
                    q.append((n_r, n_c))
                    maps[n_r][n_c] = maps[r][c] + 1

    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1] - 1


def solution(maps):
    return bfs(maps, (0,0))
