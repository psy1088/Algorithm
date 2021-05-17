def solution(s):
    s = list(s.lower())
    first_word = True
    
    for i in range(len(s)):
        if s[i] == ' ':
            first_word = True
            
        elif first_word:
            s[i] = s[i].upper()
            first_word = False
    
    return ''.join(s)
