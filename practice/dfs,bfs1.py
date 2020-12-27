# p339 특정거리의 도시 찾기

from collections import deque

### 입력
# N=도시 개수, M=도로 개수, K=거리정보, X=출발도시의 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 1부터~N까지이므로 N+1개만큼 리스트
for _ in range(M):
    r, c = map(int, input().split())
    graph[r].append(c)

visited = [0] * (N + 1)  # 인덱스 1부터 시작이므로 N+1개만큼
visited[X] = True
q = deque([X])
result = []
dist = 0  # 출발점으로부터 거리

while q:
    v = q.popleft()
    dist += 1
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = dist  # visited 리스트에 거리 값을 저장
            if dist == K:  # 거리값이 찾으려는 값과 일치하면 result리스트에 추가
                result.append(i)

result.sort()
if not result:
    print(-1)
else:
    for i in result:
        print(i)
