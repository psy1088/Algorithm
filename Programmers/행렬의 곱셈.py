def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    res = [[0] * c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            val = 0
            for x in range(c1):
                val += arr1[i][x] * arr2[x][j]
            res[i][j] = val
    
    return res
