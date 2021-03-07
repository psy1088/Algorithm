# p398 행성 터널
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
    total_cost = 0

    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            arr.append((a, b))
    return total_cost


N = int(input())  # N=행성의 개수
arr = []
edges = []
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

x, y, z = [], [], []
for i in range(1, N+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
edges.sort()

print(kruskal())
