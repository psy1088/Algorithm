import copy, sys
input = sys.stdin.readline

array = [[None] * 4 for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [line[j * 2], line[j * 2 + 1] - 1]  # 방향은 0부터시작하기 위해 -1

dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # 위부터 반시계로 45도씩
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1) % 8

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


def fish_move(array, shark_r, shark_c):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is not None:
            r, c = position[0], position[1]
            dir = array[r][c][1]  # 방향
            for j in range(8):
                n_r = r + dr[dir]
                n_c = c + dc[dir]
                if 0 <= n_r < 4 and 0 <= n_c < 4:
                    if not (shark_r == n_r and shark_c == n_c):
                        array[r][c][1] = dir
                        array[r][c], array[n_r][n_c] = array[n_r][n_c], array[r][c]
                        break
                dir = turn_left(dir)


def shark_possible_position(array, shark_r, shark_c):
    possible = []
    dir = array[shark_r][shark_c][1]
    for i in range(3):
        n_r = shark_r + dr[dir]
        n_c = shark_c + dc[dir]
        if 0 <= n_r < 4 and 0 <= n_c < 4:
            if 1 <= array[n_r][n_c][0] <= 16:
                possible.append([n_r, n_c])
        shark_r, shark_c = n_r, n_c
    return possible


def dfs(array, r, c, ate):
    global max_ate
    array = copy.deepcopy(array)
    ate += array[r][c][0]
    array[r][c][0] = -1  # 잡아먹힌 곳은 -1으로 체크

    fish_move(array, r, c)  # 물고기 이동
    possible_arr = shark_possible_position(array, r, c)  # 상어 이동가능 좌표 찾기

    max_ate = max(max_ate, ate)
    for x, y in possible_arr:
        dfs(array, x, y, ate)


max_ate = 0
dfs(array, 0, 0, 0)
print(max_ate)
