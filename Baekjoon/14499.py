import sys, copy
input = sys.stdin.readline

#n=행 m=열 x,y=주사위 위치 k=명령 개수
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
all_command = list(map(int, input().split()))

east, west, north, south = 1, 2, 3, 4
front, back, left, right, up, down = 0, 0, 0, 0, 0, 0 # 주사위의 앞 뒤 왼 오 위 아래

dr = [0, 0, 0, -1, 1] # 동 서 북 남
dc = [0, 1, -1, 0, 0]


def ewsn(command):
    global front, back, up, down, left, right

    if command == east:
        up, down, left, right = left, right, down, up
    elif command == west:
        up, down, left, right = right, left, up, down
    elif command == north:
        up, down, front, back = front, back, down, up
    elif command == south:
        up, down, front, back = back, front, up, down
    print(up)


for com in all_command:
    n_r = x + dr[com]
    n_c = y + dc[com]
    if 0 <= n_r < n and 0 <= n_c < m:
        ewsn(com) # 주사위 굴리기
        if graph[n_r][n_c] == 0:
            graph[n_r][n_c] = down
        else:
            down = graph[n_r][n_c]
            graph[n_r][n_c] = 0
        x, y = n_r, n_c
