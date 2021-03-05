# p393 여행 계획

#그래프로 나타내어서 루트가 같으면 여행 가능한거지
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


def check():
    for i in range(M-1):
        if find_parent(parent, travel_route[i]) != find_parent(parent, travel_route[i+1]):
            return False
    return True


N, M = map(int, input().split())  # N=여행지 수, M=여행 계획중인 도시의 수

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

travel_route = list(map(int, input().split()))

if check():
    print("YES")
else:
    print("NO")
