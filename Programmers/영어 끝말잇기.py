from collections import defaultdict

def solution(n, words):
    dict = defaultdict(list)
    dict[words[0][0]].append(words[0])
    
    for i in range(1, len(words)):
        # 문자가 이어지지 않는 경우
        if words[i][0] != words[i-1][-1]: 
            return [(i%n)+1, (i//n)+1]
        
        # 중복인 경우
        if words[i] in dict[words[i][0]]: 
            return [(i%n)+1, (i//n)+1]
        else:
            dict[words[i][0]].append(words[i])
    
    return [0, 0]
