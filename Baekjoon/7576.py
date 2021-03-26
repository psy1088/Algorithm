def Input():
    global flag

    for r in range(N):
        line = list(map(int, input().split()))
        data.append(line)
        for c in range(M):
            if data[r][c] == 0:  # 안 익은 토마토가 있는 경우
                flag = True
                data[r][c] = MAX  # 0인 곳을 다 1e9로 바꿔줌
            if data[r][c] == 1:  # 익은 토마토의 좌표를 따로 저장
                q.append((r, c))


def bfs():
    while q:
        now_r, now_c = q.popleft()
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < M:
                if data[next_r][next_c] != -1:
                    if data[now_r][now_c] + 1 < data[next_r][next_c]:
                        data[next_r][next_c] = data[now_r][now_c] + 1
                        q.append((next_r, next_c))


def check():  # 출력값 계산
    res = 0
    for i in data:  # 리스트에 0이 있다면, 안 익은것이 있으므로 -1 리턴
        if MAX in i:
            return -1
        res = max(res, max(i))
    return res - 1


from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())  # M=열, N=행
data = []
q = deque([])  # 초기에 익은 과일의 좌표를 저장
flag = False  # 초기에 안 익은 과일이 있는지 확인
MAX = int(1e9)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

Input() # 입력 받기
bfs() # bfs 수행

if flag:  # 초기에 안 익은 과일이 있었다면~
    print(check())
else:  # 초기에 안 익은 과일이 없었다면 0 출력
    print(0)
