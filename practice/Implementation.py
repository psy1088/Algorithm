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











