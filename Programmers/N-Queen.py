result = 0
def dfs(row, q, n):
    global result

    if row == n:
        result += 1
        return

    for col in range(n):
        q[row] = col
        flag = True
        for i in range(row): # 같은 행에 있는지 여부는 파악할 필요X
            if q[i] == q[row]: # 같은 열에 존재한다면 break
                flag = False
                break
            if abs(i-row) == abs(q[i]-q[row]): # 대각선에 존재한다면 break
                flag = False
                break

        if flag:
            dfs(row+1, q, n)


def solution(n):
    q = [-1] * n
    dfs(0, q, n)
    return result
