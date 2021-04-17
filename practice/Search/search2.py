# p368 고정점 찾기
N = 7  # 리스트의 개수
data = [-15, -4, 2, 8, 9, 13, 15]


# def fix_point(arr, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if mid == arr[mid]:
#             return mid
#         elif mid < data[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1

def fix_point(arr, start, end):
    for val, index in enumerate(data):
        if val == index:
            return val
    return -1


print(fix_point(data, 0, N-1))
