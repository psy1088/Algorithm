def find_fish(): # 시작 위치, 전체 물고기의 좌표 저장
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                if graph[i][j] == 9:
                    r, c = i, j
                    graph[i][j] = 0
                else: # 물고기의 위치를 전부 저장
                    fish.append([i, j, 0])
    return r, c


def bfs(now_r, now_c): # 현재 위치에서, 모든 좌표까지의 최솟값을 구해
    q = deque([(now_r, now_c)])
    visited = [[-1] * N for _ in range(N)]
    visited[now_r][now_c] = 0

    can_move = False
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if graph[nr][nc] <= shark_size:  # 상어크기보다 작거나 같은 곳만 이동 가능
                    can_move = True
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    if not can_move:
        print(time)
        exit(0)
    else:
        return visited


def simulation(start_r, start_c):
    global time, shark_size
    eat = 0

    _exit = True
    while fish:
        dist = bfs(start_r, start_c)
        for i in range(len(fish)):  # 현재 물고기 위치까지의 거리를 전부 저장
            x, y = fish[i][0], fish[i][1]
            fish[i][2] = dist[x][y]

        fish.sort(key=lambda x: (x[2], x[0], x[1])) # 제일 가까운 순 > 위에 있는 순 > 왼쪽에 있는 순
        for f in fish:
            r, c, dist = f
            if dist != -1 and graph[r][c] < shark_size: # 방문 가능한 위치에, 상어크기보다 작은 곳으로 이동
                start_r, start_c = r, c
                time += dist
                fish.remove(f)
                eat += 1
                if eat == shark_size:
                    eat = 0
                    shark_size += 1
                _exit = True
                break
            _exit = False

        if not _exit:
            break


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())  # 맵 크기
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
time = 0
shark_size = 2
fish = []

start_r, start_c = find_fish()
simulation(start_r, start_c)
print(time)
