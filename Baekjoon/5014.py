def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()
        if now == g:
            return visited[now]
        for next in [now - d, now + u]:
            if 0 < next <= f and visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + 1

    if visited[g] == -1:
        return "use the stairs"


from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [-1 for _ in range(f+1)]
print(bfs(s))
