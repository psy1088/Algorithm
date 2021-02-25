# # 피보나치 수열 (메모이제이션 기법) 탑다운
# d = [0] * 100
#
# def fibo(x):
#     print(x)
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:  # 이미 계산한 적 있는 문제라면 그냥 반환
#         return d[x]
#
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
#
# print(fibo(9))
#
# # 피보나치 수열 바텀업
# d = [0] * 100
# d[1], d[2] = 1, 1
# n = 99
#
# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])


# # p217 1로 만들기
# x = int(input())
# d = [0] * 30001
#
# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5]+1)
#
# print(d[x])


# # p220 개미 전사
# n = int(input())  # 식량창고 개수
# k = list(map(int, input().split()))
#
# d = [0] * n
#
# d[0] = k[0]
# d[1] = max(k[0], k[1])
# for i in range(2, n):
#     d[i] = max(d[i-2]+k[i], d[i-1])
#
# print(d[n-1])


# # p223 바닥 공사
# n = int(input())
#
# d = [0] * n
# d[0] = 1
# d[1] = 3
# for i in range(2, n):
#     d[i] = (d[i-1] + d[i-2] * 2) % 796796
#
# print(d[n-1])


# p226 효율적인 화폐구성
n, m = 3, 4  # n=화폐개수, m=만들 돈의 합
coin = [3, 5, 7]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], d[j - coin[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])








