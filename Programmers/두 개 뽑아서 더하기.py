def solution(numbers):
    dict = {}
    len_arr = len(numbers)

    for i in range(len_arr):
        for j in range(i+1, len_arr):
            dict[numbers[i]+numbers[j]] = 0

    return sorted(dict)
