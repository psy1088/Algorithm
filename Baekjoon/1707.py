def bfs(start):
    q.append(start)
    color[start] = 1

    while q:
        now = q.popleft()
        for v in graph[now]:
            if color[v] == 0:
                color[v] = color[now] * -1
                q.append(v)
            elif color[v] == color[now]:
                return False
    return True


from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())  # V=정점, E=간선

    color = [0 for _ in range(V + 1)]
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    q = deque()
    flag = True
    for i in range(1, V + 1):
        if color[i] == 0:
            if not bfs(i):
                flag = False
                break

    print("YES" if flag else "NO")
