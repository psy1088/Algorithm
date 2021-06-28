from collections import defaultdict

def make_set(s):
    dict = defaultdict(int)
    s = s.lower()
    for i in range(1, len(s)):
        if (s[i-1]+s[i]).isalpha():
            dict[s[i-1]+s[i]] += 1

    return dict
    
    
def solution(str1, str2):
    d1, d2 = make_set(str1), make_set(str2)
    
    if not d1 and not d2:
        return 65536
    
    else:
        x, y = 0, 0 # 교집합 원소 수, 합집합 원소 수
        s1, s2 = set(d1), set(d2)
        inter = s1 & s2
        union = s1 | s2
        diff = union - inter
        
        for key in inter:
            x += min(d1[key], d2[key])
            y += max(d1[key], d2[key])
        
        for key in diff:
            y += d1[key] + d2[key]
            
    return int(x / y * 65536)
