from itertools import combinations
import math

def prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    arr = combinations(nums, 3)
    for num in arr:
        if prime_num(sum(num)):
            answer += 1
    
    return answer
