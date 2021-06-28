from itertools import permutations
import copy

num, oper = [], []

def cal(p):
    temp_num = copy.deepcopy(num)
    temp_oper = copy.deepcopy(oper)
    
    for o in p:
        i = 0
        while i < len(temp_oper):
            if temp_oper[i] == o:
                if o == '*':
                    temp_num[i] *= temp_num[i+1]
                elif o == '+':
                    temp_num[i] += temp_num[i+1]
                elif o == '-':
                    temp_num[i] -= temp_num[i+1]
                temp_num.pop(i+1)
                temp_oper.pop(i)
            
            else:
                i += 1
    
    return abs(temp_num[0])
    

def solution(expression):
    max_val = 0
    
    temp = ''
    for e in expression:
        if e.isdigit():
            temp += e
        else: # 연산자
            oper.append(e)
            num.append(int(temp))
            temp = ''
    num.append(int(temp))
    
    for p in permutations(['*', '+', '-'], 3):
        max_val = max(max_val, cal(p))
    
    return max_val
