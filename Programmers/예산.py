def solution(d, budget):
    cnt = 0
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        else:
            cnt += 1
    
    return cnt
