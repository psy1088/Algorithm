def solution(n):
    arr = [1,2,4]
    res = ''
    while n > 0:
        res = str(arr[(n-1) % 3]) + res
        n = (n-1) // 3
    
    return res
