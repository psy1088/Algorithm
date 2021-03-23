def leap_year(n):
    if N % 4 == 0:
        if N % 100 != 0 or N % 400 == 0:
            return 1
    return 0


N = int(input())
print(leap_year(N))
