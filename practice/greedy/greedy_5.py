# 315p 볼링공 고르기

# # 1번
# from itertools import combinations
#
# n, m = map(int, input().split()) # n = 볼링공 개수, m = 무게의 종류
# ball = list(map(int, input().split())) # 공들의 무게
#
# arr = list(combinations(ball, 2)) # 공들중에서 2개를 뽑는 경우
# for i in arr: # 같은 무게의 투플 제거
#     if i[0] == i[1]:
#         arr.remove(i)
#
# print(len(arr))



# # 2번
# n, m = map(int, input().split())
# ball = list(map(int, input().split()))
#
# cnt = 0
# len_ball = len(ball)
# for i in range(0, len_ball - 1):
#     cur = ball[i]
#     for j in range(i+1, len_ball):
#         if cur != ball[j]:
#             cnt += 1
#
# print(cnt)


# 3번
n, m = map(int, input().split())
ball = list(map(int, input().split()))

arr = [0] * (m+1) # 공 무게의 개수를 담는 배열
res = 0

for i in ball:
    arr[i] += 1

for i in range(1, m+1):
    n -= arr[i]
    res += n * arr[i]

print(res)


