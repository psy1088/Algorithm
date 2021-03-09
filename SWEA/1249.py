def init_graph():
    for i in range(n):
        for j in range(n):
            for d in range(2):
                next_r, next_c = i + dr[d], j + dc[d]
                if next_r < n and next_c < n:
                    graph[i][j].append((next_r, next_c))
                    graph[next_r][next_c].append((i, j))


def dijkstra(start_r, start_c):
    q = []
    heapq.heappush(q, (0, start_r, start_c))
    dist[start_r][start_c] = 0

    while q:
        val, now_r, now_c = heapq.heappop(q)
        if dist[now_r][now_c] < val:
            continue

        for r, c in graph[now_r][now_c]:
            cost = val + data[r][c]
            if cost < dist[r][c]:
                dist[r][c] = cost
                heapq.heappush(q, (cost, r, c))


import heapq

INF = int(1e9)
dr = [1, 0, -1, 0]  # 아래, 오른쪽, 위, 왼쪽
dc = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())  # 맵의 크기
    data = []
    for i in range(n):  # 맵 정보 입력받기
        str = input()
        num_str = []
        for j in range(n):
            num_str.append(int(str[j]))
        data.append(num_str)

    graph = [[[] for _ in range(n)] for _ in range(n)]
    init_graph()  # 각 좌표별로 연결된 노드 저장

    dist = [[INF] * n for _ in range(n)]
    dijkstra(0, 0)  # 다익스트라 실행

    print("#", end='')
    print(test_case, dist[n - 1][n - 1])
