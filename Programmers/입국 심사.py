def solution(n, times):
    answer = 0
    start, end = 1, min(times)*n
    
    while start <= end:
        mid = (start+end) // 2
        cnt = n
        for time in times:
            cnt -= mid // time
            if cnt <= 0:
                answer = mid
                end = mid-1
                break
        if cnt > 0:
            start = mid+1

    return answer
