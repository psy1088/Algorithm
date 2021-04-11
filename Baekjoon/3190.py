import sys
input = sys.stdin.readline

N = int(input())  # 맵 크기
graph = [[0] * N for _ in range(N)]

K = int(input())  # 사과 개수
for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1  # 사과 있는 위치 = 1

direction = []
L = int(input())
for _ in range(L):
    x, c = input().split()
    direction.append((int(x), c))

body = [(0, 0)]
dr = [0, 1, 0, -1]  # 동 남 서 북
dc = [1, 0, -1, 0]


def check(n_r, n_c):  # 몸에 닿거나, 범위를 벗어났는지 체크
    if (n_r, n_c) in body:
        return False
    if n_r < 0 or n_c < 0 or N <= n_r or N <= n_c:
        return False

    return True


def move(dir):  # 이동
    global time

    time += 1
    now_r, now_c = body[-1][0], body[-1][1]  # 현재 머리 위치
    n_r = now_r + dr[dir]
    n_c = now_c + dc[dir]

    if not check(n_r, n_c):
        return False

    body.append((n_r, n_c))
    if graph[n_r][n_c] == 1: # 사과라면, 0으로 바꿔줌
        graph[n_r][n_c] = 0
    elif graph[n_r][n_c] == 0:  # 사과가 아니면, 다시 몸길이 줄여줌
        body.pop(0)

    return True


dir = 0
time = 0
t_d = direction.pop(0)  # t_d = (시간, '방향')
while True:
    if not move(dir):
        break

    if time == t_d[0]:
        if t_d[1] == 'L':
            dir = (dir + 4 - 1) % 4
        elif t_d[1] == 'D':
            dir = (dir + 1) % 4

        if direction:
            t_d = direction.pop(0)

print(time)
