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
# row = int(start[1])
# col = ord(start[0]) - ord('a') + 1
#
# move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
# cnt = 0
#
# for i in move:
#     next_row = row + i[0]
#     next_col = col + i[1]
#
#     if 1 <= next_row <= 8 and 1 <= next_col <= 8:
#         cnt += 1
# print(cnt)


# # p118 게임 개발
# N, M = map(int, input().split())
# cur_row, cur_col, direction = map(int, input().split())
# visited = [[0] * M for _ in range(N)] # 방문 여부
# visited[cur_row][cur_col] = 1
# d_row = [-1, 0, 1, 0]
# d_col = [0, 1, 0, -1]
# array = [] # 맵
# move_cnt = 1 # 이동횟수
# turn_cnt = 0 # 회전횟수
# for i in range(N):
#     array.append(list(map(int, input().split())))
#
#
# def turnLeft():
#     global direction
#     direction = (direction - 1 + 4) % 4
#
# while True:
#     turnLeft()
#     next_row = cur_row + d_row[direction]
#     next_col = cur_col + d_col[direction]
#
#     # 육지에 해당하는 좌표이고 && 방문하지 않았다면
#     if array[next_row][next_col] == 0 and visited[next_row][next_col] == 0:
#         visited[next_row][next_col] = 1
#         cur_row = next_row
#         cur_col = next_col
#         move_cnt += 1
#         turn_cnt = 0
#         continue
#     else:
#         turn_cnt += 1
#
#     # 제 자리에서 한바퀴 회전했다면
#     if turn_cnt == 4:
#         next_row = cur_row - d_row[direction]
#         next_col = cur_col - d_col[direction]
#
#         # 1칸 후진 할 공간이 육지라면 이동
#         if array[next_row][next_col] == 0:
#             cur_row = next_row
#             cur_col = next_col
#         else:
#             break
#         turn_cnt = 0
#
# print(move_cnt)










