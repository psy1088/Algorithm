# p 385 플로이드
import sys
n = 5  # 도시의 개수
m = 14  # 버스의 개수

input = sys.stdin.readline
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):  # 출발지 == 도착지의 경우 0으로 초기화
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):  # 입력 받은 값들을 그래프 리스트에 저장
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


def floyd():  # 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd()
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] < INF:
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()

