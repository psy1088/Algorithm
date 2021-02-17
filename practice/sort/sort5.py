# p363 카드 정렬하기

# 1번 풀이
# N = 4  # 숫자 카드 개수
# card = [1, 2, 4, 5]  # 카드 묶음 각각의 카드 수
#
# card.sort()
# temp = card[0]
# result = 0
#
# for i in range(1, len(card)):
#     temp += card[i]
#     result += temp
#
# print(result)


# 2번 풀이
import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap):
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_val = one + two
    result += sum_val
    heapq.heappush(heap, sum_val)

print(result)
