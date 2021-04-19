def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    start = 5 # 1월1일은 금요일= day[5]
    
    for i in range(1, a):
        start += month[i] % 7
    
    answer = (b - 1) % 7
    return day[(start + answer) % 7]
