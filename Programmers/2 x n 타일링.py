def solution(n):
    if n <= 2:
        return n
    
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        val = d[i-2] + d[i-1] 
        d[i] = val % 1000000007
        
    return d[n]
