# # p110 상하좌우
# def direction(x):
#     return {'L': -1, 'R': 1, 'U': -1, 'D': 1}[x]
#
#
# N = int(input())
# move = input().split()
# x, y = 1, 1
#
# for i in move:
#     m = direction(i)
#     if i == 'L' or i == 'R':
#         if 1 <= y + m <= N:
#             y += m
#     else:
#         if 1 <= x + m <= N:
#             x += m
# print(x, y)


# # p113 시각
# N = int(input())
# cnt = 0
#
# for i in range(N+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1
# print(cnt)


# p115 왕실의 나이트
# 범위 x : 1~8  /  y : a~h

##1
# start = input()
# s_x = ord(start[0])
# s_y = int(start[1])
# cnt = 8  # 처음에 가운데 위치한다고 할 때, 경우의 수 8개라고 잡고 상황에 따라 감소시켜주자
#
# l_space, r_space = s_x - ord('a'), ord('h') - s_x
# u_space, d_space = s_y - 1, 8 - s_y
#
# if l_space == 0 or r_space == 0:
#     cnt -= 4
#     if u_space == 0 or d_space == 0:
#         cnt -= 2
#     elif u_space == 1 or d_space == 1:
#         cnt -= 1
#     else:
#         pass
#
# elif l_space == 1 or r_space == 1:
#     cnt -= 2
#     if u_space == 0 or d_space == 0:
#         cnt -= 3
#     elif u_space == 1 or d_space == 1:
#         cnt -= 2
#     else:
#         pass
#
# else:
#     if u_space == 0 or d_space == 0:
#         cnt -= 4
#     elif u_space == 1 or d_space == 1:
#         cnt -= 2
#     else: pass

##2
# now = input()
# x, y = int(now[1]), ord(now[0])
# total_cnt = 0
# num_a, num_h = ord('a'), ord('h')
# steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
#
# for i in steps:
#     next_x = x + i[0]
#     next_y = y + i[1]
#
#     if 1 <= next_x <= 8 and num_a <= next_y <= num_h:
#         total_cnt += 1
#
# print(total_cnt)


# p118 게임 개발

# N, M = map(int, input().split())
# x, y, d = map(int, input().split())

# game_map = []
# for i in range(N):
#     game_map.append(list(map(int, input().split())))

N, M = 4, 4
x, y, d = 1, 1, 0
game_map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

game_map[x][y] = 1
cnt = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turn_cnt = 0


def turn():
    global d, turn_cnt
    d = (d - 1 + 4) % 4  # 왼쪽방향으로 돌아
    turn_cnt += 1


while True:
    turn()
    next_x = x + dx[d]
    next_y = y + dy[d]

    if game_map[next_x][next_y] == 0:  # 이동가능한 공간이면~
        x, y = next_x, next_y
        game_map[x][y] = 1
        cnt += 1
        turn_cnt = 0
        continue

    if turn_cnt == 4:  # 이동불가능 한 공간인데, 4번 회전한 상태라면~
        next_x = x - dx[d]
        next_y = y - dy[d]
        if game_map[next_x][next_y] == 0:  # 한 칸 후진
            x, y = next_x, next_y
            cnt += 1
            turn_cnt = 0
        else:  # 후진한 공간이 이동불가능 공간이면 종료
            break

print(cnt)
