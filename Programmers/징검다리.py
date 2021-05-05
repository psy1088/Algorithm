def solution(distance, rocks, n):
    rocks.sort()
    
    answer = 0
    start, end = 0, distance
    
    while start <= end:
        removed_rock = 0
        mid = (start+end) // 2
        prev = 0
        for r in rocks:
            if r - prev < mid:
                removed_rock += 1
            else:
                prev = r

        if removed_rock > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer
