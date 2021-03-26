def bfs(r, c):
    q = deque([(r, c)])
    data[r][c] = 0

    while q:
        now_r, now_c = q.popleft()
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < M and data[next_r][next_c] == 1:
                data[next_r][next_c] = 0
                q.append((next_r, next_c))


from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # M=열, N=행, K=배추개수
    data = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        data[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)
