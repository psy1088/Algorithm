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
dp = [0] * (n+1)
dp[1] = 1

next2, next3, next5 = 2, 3, 5

for i in range(2, n+1):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        next2 += 2
    if dp[i] == next3:
        next3 += 3
    if dp[i] == next5:
        next5 += 5

print(dp[n])









