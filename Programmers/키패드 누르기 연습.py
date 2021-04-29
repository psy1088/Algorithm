def distance(n, now):
    row = abs((n-1)//3 - (now-1)//3)
    col = abs((n-1)%3 - (now-1)%3)
    return row+col
    

def solution(numbers, hand):
    res = ''
    now_l, now_r = 10, 12
    
    for n in numbers:
        if n in [1,4,7]:
            res += 'L'
            now_l = n
        elif n in [3,6,9]:
            res += 'R'
            now_r = n
        else:
            if n == 0: # 0번이면, 11로 대체
                n = 11
    
            dist_l = distance(n, now_l)
            dist_r = distance(n, now_r)
            if dist_l > dist_r:
                res += 'R'
                now_r = n
            elif dist_l < dist_r:
                res += 'L'
                now_l = n
            else:
                if hand == 'right':
                    res += 'R'
                    now_r = n
                else:
                    res += 'L'
                    now_l = n
        
    return res
