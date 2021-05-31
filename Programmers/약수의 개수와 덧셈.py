def solution(left, right):
    result = 0
    
    for n in range(left, right+1):
        sq = n ** 0.5
        if sq == int(sq): # 약수 개수가 홀수인경우는, 자연수의 제곱인 수밖에 없으므로
            result -= n
        else:
            result += n
            
    return result
