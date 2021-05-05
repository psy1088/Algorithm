def solution(people, limit):
    people.sort()
    len_arr = len(people)
    
    start = 0
    end = len_arr-1
    result = 0
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        result += 1
        
    return result
