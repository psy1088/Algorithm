from collections import deque
from sys import stdin
input = stdin.readline


def bfs(r, c):
    visited = [[-1] * (w+2) for _ in range(h+2)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    while q:
        now_r, now_c = q.popleft()
        for d in range(4):
            nr = now_r + dr[d]
            nc = now_c + dc[d]
            if nr < 0 or (h+2) <= nr or nc < 0 or (w+2) <= nc:
                continue
            if visited[nr][nc] > -1 or data[nr][nc] == '*':
                continue
            if data[nr][nc] == '.':
                visited[nr][nc] = visited[now_r][now_c]
                q.appendleft((nr, nc))
            elif data[nr][nc] == '#':
                visited[nr][nc] = visited[now_r][now_c] + 1
                q.append((nr, nc))

    return visited


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    data = ['.' * (w+2)] # '.'을 추가해서 맵을 늘려줌
    for _ in range(h):
        line = input().rstrip()
        data.append(list('.' + line + '.'))
    data.append(list('.' * (w+2)))

    s_q = deque()
    for i in range(h+2):
        for j in range(w+2):
            if data[i][j] == '$': # 죄수의 위치를 큐에 저장하고, .으로 바꿔줌
                data[i][j] = '.'
                s_q.append((i, j))

    s_r, s_c = s_q.pop()
    res1 = bfs(s_r, s_c)
    s_r, s_c = s_q.pop()
    res2 = bfs(s_r, s_c)
    res3 = bfs(0, 0)

    min_res = 1e9
    for i in range(h+2):
        for j in range(w+2):
            if data[i][j] == '*':
                continue
            r = res1[i][j] + res2[i][j] + res3[i][j]
            if data[i][j] == '#':
                r -= 2
            min_res = min(min_res, r)

    print(min_res)
