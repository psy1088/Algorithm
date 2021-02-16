# # p339 특정거리의 도시 찾기
from collections import deque


# ### 입력
# # N=도시 개수, M=도로 개수, K=거리정보, X=출발도시의 번호
# N, M, K, X = map(int, input().split())
# graph = [[] for _ in range(N + 1)]  # 1부터~N까지이므로 N+1개만큼 리스트
# for _ in range(M):
#     r, c = map(int, input().split())
#     graph[r].append(c)

N, M, K, X = 4, 4, 1, 1  # 도시개수 / 도로 개수 / 최단거리 / 출발번호
data = [(1, 2), (1, 3), (2, 3), (2, 4)]
graph = [[] for _ in range(N+1)]
for i in range(M):
    r, c = data[i][0], data[i][1]
    graph[r].append(c)

visited = [-1 for _ in range(N+1)]
result = []
q = deque()


def bfs(X):
    dist = 0
    q.append(X)
    visited[X] = dist

    while q:
        v = q.popleft()
        # visited리스트에 방문표시 겸 출발점으로부터의 거리를 저장
        dist = visited[v] + 1
        # 해당 도시와 연결된 도시 중에 방문하지 않은 곳 삽입
        for city in graph[v]:
            if visited[city] == -1:
                q.append(city)
                visited[city] = dist
                if dist == K:
                    result.append(city)


bfs(X)
result.sort()

if not result:
    print(-1)
else:
    for i in result:
        print(i)
