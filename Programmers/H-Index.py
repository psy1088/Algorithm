from bisect import bisect_left

def solution(citations):
    arr = sorted(citations)
    len_arr = len(arr)
    
    for i in range(len(arr), -1, -1):
        large_cnt = len_arr - bisect_left(arr, i) # i보다 큰 수의 개수
        if i <= large_cnt:
            return i
