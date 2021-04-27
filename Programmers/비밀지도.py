def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        temp = str(bin(a|b)[2:])
        
        temp = temp.replace('1', '#')
        temp = temp.zfill(n)
        temp = temp.replace('0', ' ')
        
        answer.append(temp)
    return answer
