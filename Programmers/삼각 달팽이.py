def solution(n):
    arr = [[0] * n for _ in range(n)]
    res = []
    num = 1
    r, c = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # Down
                r += 1

            elif i % 3 == 1: # Right
                c += 1

            elif i % 3 == 2: # Up
                r -= 1
                c -= 1

            arr[r][c] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                res.append(arr[i][j])

    return res
