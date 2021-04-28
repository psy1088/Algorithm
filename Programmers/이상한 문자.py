def solution(s):
# 1번 방법
    res = ''
    index = 0
    for x in s:
        if x == ' ':
            index = -1
            
        if index % 2 == 0:
            res += x.upper()
        else:
            res += x.lower()
        index += 1
    
    return res


# 2번 방법
    res = []
    s = s.split(' ')
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                res.append(s[i][j].upper())
            else:
                res.append(s[i][j].lower())
        res.append(' ')
    
    return ''.join(res[:-1])
