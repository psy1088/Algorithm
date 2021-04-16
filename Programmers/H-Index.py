def solution(array):
    array.sort(reverse=True)
    for start in range(array[0], -1, -1):
        cnt = 0
        for i in range(len(array)):
            if start <= array[i]:
                cnt += 1
            else:
                break
        if start <= cnt:
            return start
