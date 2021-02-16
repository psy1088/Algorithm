### p92 큰수의 법칙
# N, M, K = list(map(int, input().split())) # 배열 크기
# data = list(map(int, input().split()))
#
# data.sort()
# res = 0

# # 1번 방법 - 단순
# for i in range(M):
#     if i % (K+1) == K:
#         res += data[N-2]
#     else:
#         res += data[N-1]
#
# print(res)

# # 2번 방법
# cnt = (M // (K+1) * K) + (M % (K+1))
# res += cnt * data[N-1]
# res += (M - cnt) * data[N-2]
#
# print(res)



### p96 숫자 카드 게임
# N, M = map(int, input().split())
#
# Min = []
#
# for i in range(N):
#     data = list(map(int, input().split()))
#     Min.append(min(data))
#
# print(max(Min))



### p99 1이 될 때까지지
# N, K = map(int, input().split())
# cnt = 0
#
# while N >= K:
#     while N % K != 0:
#         N -= 1
#         cnt += 1
#     N //= K
#     cnt += 1
#
# while N > 1:
#     N -= 1
#     cnt += 1
#
# print("cnt=",cnt)














