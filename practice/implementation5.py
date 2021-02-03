# # p327 사과먹는 뱀
# N = int(input()) # 보드의 크기
# K = int(input()) # 사과의 개수
# MAP = [[0] * N for _ in range(N)]  # 맵 공간 다 0으로 초기화
# for i in range(K): # 사과의 개수만큼 사과의 위치를 맵 공간에 5로 지정
#     apple = list(map(int, input().split()))
#     MAP[apple[0]][apple[1]] = 5
# snake_body = [] # 현재 뱀의 몸통 좌표
# turn_cnt = int(input())  # 총 방향전환 횟수
# turn = []  # 몇초에 어디로 방향전환 할지 나타내는 리스트
# for i in range(turn_cnt):
#     turn.append(input().split())
#
# cur_row = 0  # 현재 위치 (행)
# cur_col = 0  # 현재 위치 (열)
# snake_body.append((cur_row, cur_col))
# direction_type = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
# direction = 0
# time = 0
# turn_next = 0 # 다음에 수행할 방향전환
# turn_time = int(turn[turn_next][0])  # 방향전환 할 시간
#
#
# def check(row, col, size):
#     if row < 0 or size <= row or col < 0 or size <= col:
#         print("범위초과.. 현재 위치:", row, col)
#         return 1
#     temp = []
#     for i in snake_body:
#         if i not in temp:
#             temp.append(i)
#     if temp != snake_body:  # 뱀 몸통 리스트에 중복된 원소가 있다면, 자기 자신의 몸과 부딪힌 것이므로 종료
#         print("몸통 부딪힘.. 현재 위치:", row, col)
#         return 1
#
#
# while True:
#     print(snake_body, "  시간:", time)
#     if turn_time == time:  # 방향을 바꿔줌
#         print("회전!")
#         if turn[turn_next][1] == 'D':
#             direction = (direction + 1) % 4
#         else:
#             direction = (direction - 1) % 4
#
#         turn_next += 1
#         if turn_next < turn_cnt: # 현재 방향전환한 횟수가 총 방향전환의 횟수보다 작다면, 다음 방향전환 저장
#             turn_time = int(turn[turn_next][0])
#
#     next_row = cur_row + direction_type.get(direction)[0]
#     next_col = cur_col + direction_type.get(direction)[1]
#     snake_body.append((next_row, next_col))
#     if check(next_row, next_col, N):  # if 위치가 범위를 벗어나거나 뱀의 몸통과 닿아있다면 break
#         time += 1
#         break
#     if MAP[next_row][next_col] != 5:  # 다음에 이동할 위치에 사과가 아니라면 맨 앞 요소 pop
#         snake_body.pop(0)
#
#     cur_row = next_row
#     cur_col = next_col
#     time += 1
#
# print(time)


N = 10  # 보드 크기
K = 5  # 사과 개수
K_position = [[1, 2], [1, 3], [1, 6], [1, 5], [1, 7]]  # 사과 위치
L = 4  # 뱀의 방향 전환 횟수
L_order = [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L'], [15, 'L'], [16, 'L'], [17, 'L']]  # 뱀 방향전환 순서  ex) 3초후 D(오른쪽)으로 90도 회전

game_map = [[0] * N for _ in range(N)]
# 맵에서 사과는 1로 표시
for i in K_position:
    game_map[i[0]][i[1]] = 1

body = [(0, 0)]  # 현재 뱀의 위치
cur = (0, 0)
move_time = 0

dx = (0, 1, 0, -1)  # R D L U
dy = (1, 0, -1, 0)  # R D L U 순서
d = 0  # 현재 뱀의 이동 방향

change_time = L_order.pop(0)
while 1:
    # 방향 전환 시간에 맞춰서 방향을 틀어줌
    if change_time[0] == move_time:
        if change_time[1] == 'D':
            d = (d + 1) % 4
        elif change_time[1] == 'L':
            d = (d - 1 + 4) % 4
        if len(L_order) != 0:
            change_time = L_order.pop(0)

    next_x = cur[0] + dx[d]
    next_y = cur[1] + dy[d]
    move_time += 1
    if (next_x, next_y) in body:  # 자기 몸이랑 부딪히면 끝
        break

    if 0 <= next_x < N and 0 <= next_y < N:
        cur = (next_x, next_y)
        # 이동했는데 사과가 없으면 다음 칸으로 가
        if game_map[next_x][next_y] == 0:
            body.pop(0)
            body.append(cur)
        # 이동했는데 사과가 있으면 몸집이 커져
        elif game_map[next_x][next_y] == 1:
            body.append(cur)

    else:  # 맵을 벗어남! 게임 끝!!!
        break

print(move_time)
