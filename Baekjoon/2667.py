def bfs(r, c):
    global area_num
    q = deque([(r, c)])
    data[r][c] = area_num
    cnt = 1

    while q:
        now_r, now_c = q.popleft()
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N and data[next_r][next_c] == 1:
                data[next_r][next_c] = area_num
                q.append((next_r, next_c))
                cnt += 1
    area.append(cnt)


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().rstrip())))

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
area = []

area_num = 1
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            area_num += 1
            bfs(i, j)

print(area_num - 1)
for i in sorted(area):
    print(i)
