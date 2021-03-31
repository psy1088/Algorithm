def check(cnt):
    for x in range(cnt):
        if row[x] == row[cnt] or (cnt - x) == abs(row[cnt] - row[x]):
            return False
    return True


def dfs(cnt): # cnt = 행이라고 생각해
    global result

    if cnt == N:
        result += 1
    else:
        for i in range(N):
            row[cnt] = i  # cnt행의 i열에 퀸을 위치시킴
            if check(cnt):
                dfs(cnt+1)


N = int(input())
row = [0 for _ in range(N)]
result = 0 # 가능한 경우의 수
dfs(0)
print(result)

