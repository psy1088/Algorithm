# p386 정확한 순위
import sys


def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


input = sys.stdin.readline
N, M = map(int, input().split())  # N=학생 수, M=성적 비교 횟수

INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 대각선 부분 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

floyd()  # 플로이드워셜 알고리즘 수행

result, cnt = 0, 0
# 해당 학생과 연결된 학생의 수를 파악 (= 이 수만큼 상하 관계 비교가 가능함)
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:  # 각 학생이 자신을 제외한 나머지 학생과 연결되어 있다면 정확한 순위 산출 가능!
        result += 1

print(result)
