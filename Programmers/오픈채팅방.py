from collections import defaultdict

def solution(record):
    dict = defaultdict(str)
    result = []

    for i in range(len(record)):
        s = record[i].split()
        
        temp = [s[1]]
        if s[0][0] == 'E': # 입장
            dict[s[1]] = s[2]
            temp.append("님이 들어왔습니다.")
            
        elif s[0][0] == 'L': # 퇴장
            temp.append("님이 나갔습니다.")
        
        elif s[0][0] == 'C': # 변경
            dict[s[1]] = s[2]
            continue
            
        result.append(temp)
    
    for i in range(len(result)):
        id = result[i][0]
        result[i][0] = dict[id]
        result[i] = ''.join(result[i])
        
    return result
