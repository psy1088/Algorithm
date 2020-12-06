# 316p 다음 먹을 음식 순서
# def solution(food_times, k):
#     List = food_times
#     l = len(List);
#     deletion = 0
#     sorted_ind = sorted(range(l), key=lambda i: List[i])
#     print("sort=", sorted_ind)
#     for i in range(l):
#         if i == 0:
#             diff = List[sorted_ind[0]]
#             print("1. diff", diff)
#         else:
#             diff = List[sorted_ind[i]] - List[sorted_ind[i - 1]]
#             print("2. diff", diff)
#         tempValue = (l - i) * diff
#
#         if k < deletion + tempValue:
#             count = (k - deletion) % (l - i)
#             a = sorted(sorted_ind[i:])[count]
#             return a + 1
#         deletion += tempValue
#
#     return -1

# import heapq
#
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1))
#
#     sum_value = 0
#     previous = 0
#     length = len(food_times)
#
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
#
#     result = sorted(q, key =lambda x: x[1])
#     return result[(k-sum_value) % length][1]

# food_times = list(map(int, input().split()))
# k = int(input())
# print(solution(food_times, k))