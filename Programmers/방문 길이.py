# def solution(dirs):
#     arr = [[[0 for _ in range(4)] for _ in range(11)] for _ in range(11)]
    
#     dict = {'U':0, 'L':1, 'D':2, 'R':3}
#     dr = [1, 0, -1, 0] # U L D R
#     dc = [0, -1, 0, 1] # U L D R
    
#     cnt = 0
#     now_r, now_c = 0, 0
#     for d in dirs:
#         n_r = now_r + dr[dict[d]]
#         n_c = now_c + dc[dict[d]]
#         if -5 <= n_r <= 5 and -5 <= n_c <= 5:
#             if arr[now_r][now_c][dict[d]] == 0:
#                 cnt += 1
#                 arr[now_r][now_c][dict[d]] = 1
#                 arr[n_r][n_c][(dict[d]+2) % 4] = 1
#             now_r, now_c = n_r, n_c
            
#     return cnt



def solution(dirs):
    dict = {'U':(1,0), 'L':(0,-1), 'D':(-1,0), 'R':(0,1)}
    passed = set()
    cnt = 0
    
    r, c = 0, 0
    for d in dirs:
        n_r = r + dict[d][0]
        n_c = c + dict[d][1]
        if -5 <= n_r <= 5 and -5 <= n_c <= 5:
            if (r, c, n_r, n_c) not in passed:
                cnt += 1
                passed.add((r, c, n_r, n_c))
                passed.add((n_r, n_c, r, c))
            r, c = n_r, n_c
        
    return cnt
