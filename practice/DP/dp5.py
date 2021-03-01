# p381 못생긴 수
n = int(input())

# # 1번 풀이 ( 완전탐색..? )
# def prime_Factor(num):
#     for i in range(2, num+1):
#         if num % i == 0:
#             if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
#                 return False
#     return True
#
#
# cnt, index = 1, 1
# while cnt < n:
#     index += 1
#     if prime_Factor(index):
#         cnt += 1
#
# print(index)

# 2번 풀이
ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):  # 못생긴 수의 *2, *3, *5 또한 못생긴 수라는 점을 이용한 dp 풀이
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly)








