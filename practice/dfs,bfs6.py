# p351 감시피하기
from itertools import combinations

# N = 5
# game_map = [['X', 'S', 'X', 'X', 'T'], ['T', 'X', 'S', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'T', 'X', 'X', 'X'],
#             ['X', 'X', 'T', 'X', 'X']]
N = 4
game_map = [['S', 'S', 'S', 'T'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['T', 'T', 'T', 'X']]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
temp_map = [[0] * N for _ in range(N)]
# 빈 공간, 선생님의 좌표 저장
empty, teacher, all_case = [], [], []
for i in range(N):
    for j in range(N):
        if game_map[i][j] == 'X':
            empty.append((i, j))
        elif game_map[i][j] == 'T':
            teacher.append((i, j))

all_case = combinations(empty, 3)  # 장애물을 3개 설치하는 모든 경우


def check():
    for tr, tc in teacher:  # 선생님 위치별로 하나씩 검토
        for d in range(4):  # 상하좌우 방향
            next_tr, next_tc = tr, tc
            while True:  # 해당 방향으로 쭉 가면서 검토
                next_tr += dr[d]
                next_tc += dc[d]
                if 0 <= next_tr < N and 0 <= next_tc < N:
                    if temp_map[next_tr][next_tc] == 'O':
                        break
                    if temp_map[next_tr][next_tc] == 'S':
                        return False
                else:
                    break
    return True


result = False
for case in all_case:  # 모든 경우들 중 하나씩 검토
    for i in range(N):  # temp_map 에 원본 맵 저장
        for j in range(N):
            temp_map[i][j] = game_map[i][j]

    for r, c in case: # 장애물 3개 설치
        print((r, c))
        temp_map[r][c] = 'O'

    result = check()
    if result:
        print("YES")
        break

if not result:
    print("NO")
