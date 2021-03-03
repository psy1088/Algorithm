# p388 화성 탐사
import sys
import heapq

input = sys.stdin.readline
N = 3  # 탐사 공간의 크기
graph = [[5, 5, 4], [3, 9, 1], [3, 2, 7]]

INF = int(1e9)
distance = [[INF] * N for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dijkstra(r, c):
    q = []
    distance[r][c] = graph[r][c]
    heapq.heappush(q, (distance[r][c], r, c))

    while q:
        dist, now_r, now_c = heapq.heappop(q)
        if distance[now_r][now_c] < dist:  # 시작점에서 now노드로 가는 비용 < 다른 노드를 거쳐서 now노드로 가는 비용이면 검사할 필요가 없지
            continue

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N:
                cost = dist + graph[next_r][next_c]
                if cost < distance[next_r][next_c]:
                    distance[next_r][next_c] = cost
                    heapq.heappush(q, (distance[next_r][next_c], next_r, next_c))


dijkstra(0, 0)
print(distance[N-1][N-1])
