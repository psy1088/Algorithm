from collections import deque

def solution(s):
    q = deque(list(s))
    num = []
    while q:
        value = ''
        while q[0].isdigit():
            value += q.popleft()
        
        num.append(int(value))
        bonus = q.popleft()
        if bonus == 'D':
            num[-1] **= 2
        elif bonus == 'T':
            num[-1] **= 3
        
        if q and not q[0].isdigit():
            option = q.popleft()
            if option == '#':
                num[-1] *= -1
            elif option == '*':
                num[-1] *= 2
                if len(num) >= 2:
                    num[-2] *= 2
                    
    return sum(num)
