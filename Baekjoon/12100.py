def cal_max_value(arr): # 최댓값 구함
    global max_val
    for i in range(N):
        for j in range(N):
            max_val = max(max_val, arr[i][j])


def rotate90(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]
    return new_arr


def covert(line):
    temp = []
    for i in line:
        if i != 0:
            temp.append(i)

    if temp:
        new_temp = [0] * len(line)
        index = 0
        for val in temp:
            if new_temp[index] == 0:
                new_temp[index] = val
            else:
                if new_temp[index] == val:
                    new_temp[index] *= 2
                    index += 1
                else:
                    index += 1
                    new_temp[index] = val
        return new_temp
    else:
        return [0] * N


def dfs(cnt, data):
    if cnt == 5:
        cal_max_value(data)
        return

    for _ in range(4):
        temp = []
        for line in data:
            temp.append(covert(line))
        dfs(cnt+1, temp)
        data = rotate90(data)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
dfs(0, data)
print(max_val)
