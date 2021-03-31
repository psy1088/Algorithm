def bfs(start):
    q = deque([start])
    visited[start] = 1
    cnt = 0

    while q:
        now = q.popleft()
        for v in graph[now]:
            if not visited[v]:
                q.append(v)
                visited[v] = 1
                cnt += 1
    return cnt

# 가장 적은 종류의 비행기 타기
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # N=국가 수, M=비행기 종류
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(bfs(1))
