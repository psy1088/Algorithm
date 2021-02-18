# p197 부품 찾기
import sys

# # 이진탐색 풀이
# N = int(sys.stdin.readline())  # 보유중인 물건 개수
# stack = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())  # 찾는 물건 개수
# find = list(map(int, sys.stdin.readline().split()))
#
#
# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < f:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False
#
#
# stack.sort()
# find.sort()
#
# cnt = 0
# for f in find:
#     if binary_search(stack, f, 0, N - 1):
#         print("Yes", end=' ')
#     else:
#         print("No", end=' ')

# # 계수정렬 풀이
# N = int(sys.stdin.readline())
# arr = [0 for _ in range(1000001)]
#
# for i in sys.stdin.readline().split():  # 보관중인 물품
#     arr[int(i)] += 1
#
# M = int(sys.stdin.readline())
# for i in sys.stdin.readline().split():  # 찾을 물품
#     if arr[int(i)] != 0:
#         print("Yes", end=' ')
#     else:
#         print("No", end=' ')



# p201 떡볶이 떡 만들기
N, M = 4, 6  # N=떡의개수, M=손님이 요청한 길이
food_height = [19, 14, 10, 17]  # 각 떡의 높이

start = 0
end = max(food_height)

result = 0
while start <= end:
    cut_height = (start + end) // 2
    remain = 0
    for food in food_height:
        if cut_height < food:
            remain += (food - cut_height)

    if remain < M:  # 남은 떡이 손님의 요구보다 더 짧으면, end를 낮춰
        end = cut_height - 1
    elif remain > M:  # 남은 떡이 손님의 요구보다 더 길면, start 높여
        start = cut_height + 1
        result = cut_height  # 딱 맞는 경우가 없을수도 있으므로, 떡이 더 많이 남았을 때를 저장해놔
    else:  # 남은 떡이 손님의 요구와 같다면 리턴~
        result = cut_height
        break

print(result)
















