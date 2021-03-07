# p398 어두운 길
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    min_cost, total_cost = 0, 0
    for cost, a, b in graph:
        total_cost += cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            min_cost += cost

    return total_cost - min_cost


N, M = map(int, input().split())  # N=집의 수, M=도로의 수
graph = []
parent = [0] * (N+1)
total_cost = 0

for i in range(1, N+1):  # parent를 자기 자신으로 초기화
    parent[i] = i

for i in range(M):
    a, b, cost = list(map(int, input().split()))
    graph.append((cost, a, b))
    total_cost += cost

graph.sort()

print(kruskal())



