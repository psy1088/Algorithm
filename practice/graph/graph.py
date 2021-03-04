# # p298 팀 결성
# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# N, M = map(int, input().split())  # N+1 = 팀개수, M= 연산 수
# parent = [0] * (N+1)  # 각 학생별 루트를 저장할 리스트
# for i in range(1, N+1):
#     parent[i] = i
#
# for _ in range(M):
#     oper, a, b = map(int, input().split())
#
#     if oper == 0:  # x=0이면, 팀 합치기
#         union(parent, a, b)
#     elif oper == 1:  # x=1이면 같은 팀 확인
#         if find_parent(parent, a) == find_parent(parent, b):
#             print("YES")
#         else:
#             print("NO")


# # p300 도시 분할 계획
# # 크루스칼로 신장트리 구하고, 최대 비용 간선 하나 빼주면 최소 비용의 마을 2개로 분리되겠지
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# def kruskal():
#     result_edge = []
#     result_cost = 0
#
#     for cost, a, b in edges:
#         if find_parent(parent, a) != find_parent(parent, b):  # 싸이클이 없을 시,
#             union_parent(parent, a, b)  # a와 b를 합치고, 결과 비용에 추가해줌
#             result_cost += cost
#             max_cost = cost
#
#     result_cost -= max_cost
#     return result_cost
#
#
# N, M = map(int, input().split())  # N=집의 수, M=길의 수
#
# edges = []
# parent = [0] * (N+1)
# for i in range(1, N+1):
#     parent[i] = i
#
# for _ in range(M):
#     a, b, cost = map(int, input().split())  # a와 b집을 연결하는 유지비 = c
#     edges.append((cost, a, b))
# edges.sort()
#
# print(kruskal())


# p303 커리큘럼
from collections import deque
import copy

def topology():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, N+1):  # 처음에 진입차수가 0인 노드를 큐에 삽입해줌
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        for i in graph[node]:
            indegree[i] -= 1
            result[i] = max(result[i], result[node] + time[i])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])


N = int(input())  # 강의의 수
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)  # 각 노드의 차수 저장
time = [0] * (N+1)  # 수강하는데 걸리는 시간을 저장

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    # graph에 자신의 선이수를 append 하고, 선이수 과목 개수만큼 indegree 증가시켜줘
    for x in data[1:-1]:  # data의 2번째 원소부터~ 마지막 원소 전까지
        graph[x].append(i)
        indegree[i] += 1

topology()







