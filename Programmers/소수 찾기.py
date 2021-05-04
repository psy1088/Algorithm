from itertools import permutations
import math


def check_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    len_numbers = len(numbers)
    arr = [[] for _ in range(len_numbers + 1)]

    for i in range(1, len_numbers + 1):  # 모든 경우의 수 중 중복을 제외하고 저장
        arr[i] = set(permutations(numbers, i))

    for i in range(1, len_numbers + 1):
        for j in arr[i]:
            if j[0] == '0':  # 맨 앞자리가 0인 경우는 고려하지 않음
                continue
            s = ''.join(j)
            if check_prime_num(int(s)):
                answer += 1

    return answer
