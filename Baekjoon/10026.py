# def bfs(start, visit_Arr, now_color):
#     q = deque([start])
#     visit_Arr[start[0]][start[1]] = 0
#
#     while q:
#         now_r, now_c = q.popleft()
#
#         for d in range(4):
#             next_r = now_r + dr[d]
#             next_c = now_c + dc[d]
#             if 0 <= next_r < N and 0 <= next_c < N:
#                 if data[next_r][next_c] in now_color and not visit_Arr[next_r][next_c]:
#                     q.append((next_r, next_c))
#                     visit_Arr[next_r][next_c] = 1
#
#
# from collections import deque
#
# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]
#
# N = int(input())
# data = []
# for _ in range(N):
#     data.append(list(input()))
#
# visited1 = [[0] * N for _ in range(N)]
# visited2 = [[0] * N for _ in range(N)]
#
# cnt1, cnt2 = 0, 0
# for i in range(N):
#     for j in range(N):
#         if data[i][j] == 'R':
#             color1, color2 = ['R'], ['R', 'G']
#         elif data[i][j] == 'G':
#             color1, color2 = ['G'], ['R', 'G']
#         else:
#             color1, color2 = ['B'], ['B']
#
#         if not visited1[i][j]:
#             bfs((i, j), visited1, color1)
#             cnt1 += 1
#         if not visited2[i][j]:
#             bfs((i, j), visited2, color2)
#             cnt2 += 1
#
# print(cnt1, cnt2)



def bfs(start, visit_Arr, data_Arr):
    q = deque([start])
    now_color = data_Arr[start[0]][start[1]]
    visit_Arr[start[0]][start[1]] = 0

    while q:
        now_r, now_c = q.popleft()

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N:
                if data_Arr[next_r][next_c] in now_color and not visit_Arr[next_r][next_c]:
                    q.append((next_r, next_c))
                    visit_Arr[next_r][next_c] = 1


from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())
data1, data2 = [], []
for _ in range(N):
    line = list(input().rstrip())
    data1.append(line)

    line2 = line.copy()
    for i in range(N):
        if line2[i] == 'G':
            line2[i] = 'R'
    data2.append(line2)

visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs((i, j), visited1, data1)
            cnt1 += 1
        if not visited2[i][j]:
            bfs((i, j), visited2, data2)
            cnt2 += 1

print(cnt1, cnt2)
