def solution(arr):
    result = []
    for s in arr:
        if [s] != result[-1:]:
            result.append(s)
            
    return result
