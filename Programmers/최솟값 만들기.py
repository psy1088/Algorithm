def solution(A,B):
    res = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A,B):
        res += a*b
    
    return res
