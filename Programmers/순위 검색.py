from itertools import combinations
from bisect import bisect_left
dict = {}

def make_cases(s):
    for cnt in range(5):
        temp = list(combinations([0,1,2,3], cnt)) # cnt개만큼의 '-'의 위치

        for t in temp:
            _info = s[0:4] # _info = 점수를 제외한 지원자 정보
            for x in t:
                _info[x] = '-'
                
            key = ''.join(_info)
            if key in dict:
                dict[key].append(int(s[-1]))
            else:
                dict[key] = [int(s[-1])]


def solution(info, query):    
    result = []

    for i in range(len(info)): # 모든 경우를 dict에 넣어줌
        info[i] = info[i].split()
        make_cases(info[i])
    
    for key in dict.keys(): # dict의 각 key 오름차순 정렬
        dict[key].sort()
    
    for q in query: # 쿼리별로 dict 탐색
        q = q.split()
        s = q[0] + q[2] + q[4] + q[6]
        
        if s not in dict:
            result.append(0)
            continue
        
        temp = dict[s]
        val = int(q[-1])
        result.append(len(temp) - bisect_left(temp, val))

    return result
