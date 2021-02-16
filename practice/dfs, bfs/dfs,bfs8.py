from collections import deque


def get_next_body(body, board):  # 이동할 수 있는 위치를 반환하는 함수
    next_body = []
    body = list(body)
    b_x1, b_y1, b_x2, b_y2 = body[0][0], body[0][1], body[1][0], body[1][1]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for d in range(4):  # 현재 위치에서 상하좌우를 확인해보면서 이동 가능한지 체크
        next_b_x1, next_b_y1 = b_x1 + dx[d], b_y1 + dy[d]
        next_b_x2, next_b_y2 = b_x2 + dx[d], b_y2 + dy[d]
        if board[next_b_x1][next_b_y1] == 0 and board[next_b_x2][next_b_y2] == 0:
            next_body.append({(next_b_x1, next_b_y1), (next_b_x2, next_b_y2)})

    # 회전으로 이동 가능한 부분 체크
    if b_x1 == b_x2:  # 가로로 놓여 있는 경우
        for i in [-1, 1]:  # 위, 아래가 비었는지 확인
            if board[b_x1 + i][b_y1] == 0 and board[b_x2 + i][b_y2] == 0:
                next_body.append({(b_x1, b_y1), (b_x1 + i, b_y1)})
                next_body.append({(b_x2, b_y2), (b_x2 + i, b_y2)})
    elif b_y1 == b_y2:  # 세로로 놓여 있는 경우
        for i in [-1, 1]:  # 왼쪽, 오른쪽이 비었는지 확인
            if board[b_x1][b_y1 + i] == 0 and board[b_x2][b_y2 + i] == 0:
                next_body.append({(b_x1, b_y1), (b_x1, b_y1 + i)})
                next_body.append({(b_x2, b_y2), (b_x2, b_y2 + i)})
    print(next_body)
    return next_body  # 이동 가능한 위치들 반환


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]  # 보드의 크기를 늘려서 범위를 넘어선 부분을 다 벽으로 저장해버려
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    body = {(1, 1), (1, 2)}  # 현재 로봇의 위치
    q.append((body, 0))
    visited.append(body)

    while q:
        body, dist = q.popleft()
        if (n, n) in body:  # 현재 위치에 목적지가 포함되어있으면 리턴
            return dist
        for next_body in get_next_body(body, new_board):  # 이동가능한 위치들 중 방문하지 않은 곳을 방문
            if next_body not in visited:
                visited.append(next_body)
                q.append((next_body, dist + 1))

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
