# def solution(land):
#     length = len(land)
#     for i in range(1, length): # 현재 행
#         for j in range(4): # 현재 열
#             max_val = 0 
#             for k in range(4):
#                 if j == k: 
#                     continue
#                 max_val = max(max_val, land[i-1][k])
#             land[i][j] += max_val
        
#     return max(land[length-1])


def solution(land):
    length = len(land)
    for i in range(1, length): # 현재 행
        for j in range(4): # 현재 열
            max_val = max(land[i-1][:j] + land[i-1][j+1:])
            land[i][j] += max_val
            
    return max(land[length-1])
