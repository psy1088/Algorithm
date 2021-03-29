def dfs(start):
    visited[start] = 1
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i]:
                q.append(i)
                visited[i] = 0


from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())  # N=정점 개수, M=간선 개수, V=시작 정점
graph = [[] for _ in range(N + 1)]  # 정점+1 만큼 간선을 저장하기위함

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for g in graph:
    g.sort()

visited = [0 for _ in range(N+1)]
dfs(V)
print()
bfs(V)
