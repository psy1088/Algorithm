def dfs(cnt, p, r, c):
    global simple_prob

    if visited[r][c] == 1:
        simple_prob += p
        return
    if cnt == 0:
        return

    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if prob[d]:
            dfs(cnt-1, p*prob[d], nr, nc)
    visited[r][c] = 0


import sys
input = sys.stdin.readline
line = list(map(int, input().split()))
N = line[0]
prob = line[1:]  # 동서남북 확률
for i in range(4):
    prob[i] /= 100

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

simple_prob = 0
visited = [[0] * 29 for _ in range(29)]
dfs(N, 1, 14, 14)
print("%.10lf" % (1 - simple_prob))
