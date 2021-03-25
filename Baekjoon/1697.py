def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        val = q.popleft()
        if val == K:
            return visited[val]

        for x in (val*2, val+1, val-1):
            if 0 <= x <= MAX and visited[x] == -1:
                q.append(x)
                visited[x] = visited[val] + 1


from collections import deque
MAX = 100000
visited = [-1] * (MAX + 1)
N, K = map(int, input().split())  # N=수빈위치, K=동생위치
print(bfs(N))
