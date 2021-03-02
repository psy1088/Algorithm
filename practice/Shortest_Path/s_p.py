# # p259 미래 도시
#
# # 1 -> K회사 -> X회사 가는 최솟값을 구해야함
# N, M = 4, 2  # N=회사 개수, M=경로 개수
# X, K = 3, 4
#
# INF = int(1e9)
# graph = [[INF] * (N+1) for _ in range(N+1)]
#
# # 자기 자신은 0으로 초기화
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j:
#             graph[i][j] = 0
#
# # 각 간선에 대한 비용 입력 받아 초기화
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = 1  # 양방향 이동가능이므로 둘다 1로 초기화
#     graph[b][a] = 1
#
# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             #k 를 거쳐서 가는 경로
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# min_dist = graph[1][K] + graph[K][X]
# if min_dist >= INF:  # 등호 중요!! min_dist 계산할 때, 둘다 하나만 수 있잖아
#     print(-1)
# else:
#     print(min_dist)



# p262 전보
import sys
import heapq

# 다익스트라 써야할듯 => C에서의 최소거리들 구하고,
# 메시지 받는 도시 = INF가 아닌 놈들
# 총 걸리는 시간 = 최소거리들 중 최댓값
N, M, C = 3, 2, 1  # N=도시개수, M=통로 개수, C= 메시지를 보내고자 하는 시작 도시

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)  # 거리들의 최솟값을 저장할 리스트
q = []

input = sys.stdin.readline
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))  # (걸리는 시간, 도시번호)로 저장


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        time, city_num = heapq.heappop(q)

        if distance[city_num] < time:
            continue

        for t, c in graph[city_num]:
            cost = time + t
            if cost < distance[c]:
                distance[c] = cost
                heapq.heappush(q, (cost, c))


dijkstra(C)

received_city = -1
max_time = 0
for d in distance:
    if d < INF:
        max_time = max(max_time, d)
        received_city += 1

print(received_city, max_time)















