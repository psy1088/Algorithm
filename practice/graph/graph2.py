# p395 탑승구
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


G, P = map(int, input().split())  # G= 탑승구 수, P=비행기 수

parent = [0] * (G+1)
for i in range(1, G+1):
    parent[i] = i

cnt = 0
for _ in range(P):
    data = find_parent(parent, int(input()))  # 입력받는 값의 부모를 찾고
    if data == 0:  # 부모가 0이면 종료
        break
    union_parent(parent, data, data-1)  # 부모가 0이 아니면, 바로 왼쪽 탑승구와 union
    cnt += 1

print(cnt)
