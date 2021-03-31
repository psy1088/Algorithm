from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input()) # 한변의 길이
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

dr = [0, -1, 0, 1, 0]
dc = [0, 0, -1, 0, 1]
cost_arr = [[0] * N for _ in range(N)]
flower = [] # 모든 꽃의 좌표모음
for i in range(1, N-1):
    for j in range(1, N-1):
        cost = 0
        temp = []
        for d in range(5):
            r, c = i + dr[d], j + dc[d]
            temp.append((r, c)) # temp[0]이 꽃의 가운데 좌표
            cost += data[r][c]
        flower.append(temp)
        cost_arr[i][j] = cost

min_cost = 200 * 5 * 3
for f in combinations(flower, 3):
    sum_f = f[0] + f[1] + f[2]
    c = 0
    if len(set(sum_f)) == len(sum_f): # 중복을 제거한 것과 길이가 같다면, 꽃 3개가 겹치는 곳이 없는 것이므로
        for l in f: # 꽃의 3송이의 비용을 구함
            c += cost_arr[l[0][0]][l[0][1]]
        min_cost = min(min_cost, c)

print(min_cost)
