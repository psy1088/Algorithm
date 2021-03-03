# p390 숨바꼭질
import sys
import heapq


def dijkstra(start):  # start = 1
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)  # dist = 시작점부터 now까지의 거리
        if distance[now] < dist:
            continue

        for i in graph[now]:  # i = (값, 노드번호)
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())  # N=노드 수, M=간선 수
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, d = map(int, input().split())
    graph[s].append((1, d))  # s에서 d까지의 거리 1
    graph[d].append((1, s))  # d에서 s까지의 거리 1   (양방향이므로 양쪽에 삽입해줌)

dijkstra(1)
print(distance)

max_val, max_index = 0, 0
result = []
for i in range(1, N + 1):
    if max_val < distance[i]:
        max_val = distance[i]
        max_index = i
        result = [max_index]
    elif max_val == distance[i]:
        result.append(i)

print(max_index, max_val, len(result))
