import math


def solution(brown, yellow):
    cnt = brown + yellow # 총 타일 수

    for i in range(3, int(math.sqrt(cnt)) + 1): # 3부터 총 타일수의 제곱근까지만 확인
        if cnt % i == 0:
            r, c = cnt // i, i # 제곱근까지만 확인하므로 r이 항상 c보다 크거나 같음
            if yellow == ((r-2)*(c-2)) and brown == ((r+c)*2-4):
                return [r, c]
