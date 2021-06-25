#def solution(n,a,b):
#     team_a = (a-1) // 2
#     team_b = (b-1) // 2
    
#     exp = 0
#     while True: # 2^n으로 각 팀번호를 나누었을 때, 같은 영역이라면 break
#         num = 1
#         for i in range(exp):
#             num *= 2
            
#         if team_a//num == team_b//num:
#             break
            
#         exp += 1
    
#     return (exp+1)


def solution(n,a,b):
    cnt = 0
    while a != b:
        cnt += 1
        a = (a+1)//2
        b = (b+1)//2
    
    return cnt
    

