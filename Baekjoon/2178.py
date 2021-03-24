def bfs(start):
    q = deque([start])

    while q:
        now_r, now_c = q.popleft()

        for d in range(4):
            next_r = dr[d] + now_r
            next_c = dc[d] + now_c
            if 0 <= next_r < N and 0 <= next_c < M and data[next_r][next_c] == 1:
                q.append((next_r, next_c))
                data[next_r][next_c] = data[now_r][now_c] + 1


from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input())))

bfs((0, 0))
print(data[N - 1][M - 1])
