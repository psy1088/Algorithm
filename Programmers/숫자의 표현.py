# def calcul(start, end):
#     return (start+end) * (end-start+1) // 2

# def solution(n):
#     res = 1 # 자기자신은 무조건 포함되므로 1로 초기화
#     for start in range(1, n//2+1):
#         for end in range(start+1, n//2+2):
#             val = calcul(start, end)
#             if val > n:
#                 break
#             elif val == n:
#                 res += 1
#                 break
#     return res

def solution(n):
    res = 1
    for start in range(1, n//2+1):
        val = start
        while val < n:
            start += 1
            val += start
            if val == n:
                res += 1
                break

    return res
    
    
