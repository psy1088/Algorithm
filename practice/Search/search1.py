# p367 정렬된 배열에서 특정 수의 개수 구하기
n, x = 7, 2  # n = 수열의 원소 수,  x = 개수를 구하려는 수
data = [1, 1, 2, 2, 2, 2, 3]


# def binary_search(arr, target, start, end):
#     # 이진탐색으로 target과 같은 값을 갖는 원소 찾고, 그것을 기준으로 앞뒤로 while문 돌리면서 하나씩 검사
#     # 리스트 안에 target의 개수가 적다면 효율적일듯
#     cnt, mid = 0, 0
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == x:
#             cnt += 1
#             break
#         elif arr[mid] > x:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     if cnt > 0:
#         for i in [-1, 1]:
#             index = mid
#             while True:
#                 index += i
#                 if arr[index] == x:
#                     cnt += 1
#                 else:
#                     break
#         return cnt
#     else:
#         return -1


# 2번 풀이
def binary_search(arr, target):
    len_arr = len(arr)

    first_index = first(arr, x, 0, len_arr - 1)

    if first_index is None:
        return -1

    last_index = last(arr, x, 0, len_arr - 1)

    return last_index - first_index + 1


def first(arr, target, start, end):

    while start <= end:
        print(start, end)
        mid = (start + end) // 2
        # mid인덱스의 값이 target과 같은데 (mid가 0이거나, mid-1인덱스의 값은 target보다 작으면) => mid가 제일 앞에 있는 target!!
        if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
            print("시작값", mid)
            return mid
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1


def last(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == (end-1) or target < arr[mid+1]) and arr[mid] == target:
            # mid인덱스의 값이 target과 같은데 (mid가 제일 끝 인덱스이거나, mid+1인덱스의 값은 target보다 크면) => mid가 제일 뒤에 있는 target!!
            print("끝값", mid)
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


print(binary_search(data, x))
