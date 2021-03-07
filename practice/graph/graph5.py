# p399 최종 순위
from collections import deque
import sys
input = sys.stdin.readline


def topology():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0:  # 싸이클 발생 (일관성 없는 결과)
            print("Impossible")
            return False
        if len(q) >= 2:  # 다양한 경우의 수 발생
            print("?")
            return False

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    return True


test_time = int(input())  # 테스트 케이스 수
for _ in range(test_time):
    n = int(input())  # 팀의 수
    data = list(map(int, input().split()))  # 작년등수

    graph = [[False] * (n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())  # 순위 변동 수
    for i in range(m):
        a, b = map(int, input().split())  # 순위 변동있는 애들
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1

    result = []
    if topology():
        for i in result:
            print(i, end=' ')
    print()
