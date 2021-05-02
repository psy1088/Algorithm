### 1번 풀이
# def parsing(s):
#     s = s[2:-2] # 제일 바깥 괄호를 제거
#     s = s.split('},{')
#     arr = []
#     for x in s:
#         temp = []
#         for i in x.split(','):
#             temp.append(int(i))
#         arr.append(temp)
    
#     return arr
                
    
# def solution(s):
#     s = parsing(s)
#     s.sort(key=lambda x:len(x))
    
#     result = []
#     temp_set = set()
#     for i in s:
#         x = set(i) - temp_set
#         temp_set = temp_set | x
#         result.append(x.pop())

#     return result



### 2번 풀이
dict = {}
def parsing(s):
    s = s[2:-2] # 제일 바깥 괄호를 제거
    s = s.split('},{')

    arr = []
    for x in s:
        for i in x.split(','):
            arr.append(int(i))
    
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    
def solution(s):
    parsing(s)
    return sorted(dict, key=lambda x:-dict[x])
