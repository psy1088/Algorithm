def primeNum(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def palindrome(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    return True


import math
N = int(input())

while True:
    if palindrome(N) and primeNum(N):
        print(N)
        break
    N += 1
