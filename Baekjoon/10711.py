def bfs(cnt):
    while q: # q에는 모래가 없는 곳들의 좌표가 들어있음
        now_r, now_c, now_cnt = q.popleft()
        for d in range(8): # 모래 없는 곳의 주변을 -1 해주고, 0이 되면 큐에 삽입
            nr = now_r + dr[d]
            nc = now_c + dc[d]
            if 0 <= nr < H and 0 <= nc < W:
                if 0 < graph[nr][nc]:
                    graph[nr][nc] -= 1
                    if graph[nr][nc] == 0:
                        cnt = now_cnt + 1
                        q.append((nr, nc, cnt))
    return cnt


from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0, -1, -1, 1, 1]
dc = [0, -1, 0, 1, -1, 1, -1, 1]

H, W = map(int, input().split()) # H=행, W=열
graph = [[0] * W for _ in range(H)] # 전체 맵

q = deque()
cnt = 0
for i in range(H):
    line = list(input().rstrip())
    for j in range(W):
        if line[j] != '.':
            graph[i][j] = int(line[j])
        else: # '.' 인 곳은 0으로 저장하고, 큐에 삽입
            graph[i][j] = 0
            q.append((i, j, cnt))

print(bfs(cnt))
