def solution(arr):
    spec = ['.', '-', '_']
    new_arr = ''

    # 1단계
    arr = arr.lower()
    
    # 2단계
    for s in arr:
        if s.isalpha() or s.isdigit() or s in spec:
            new_arr += s  
    
    # 3단계
    while '..' in new_arr:
        new_arr = new_arr.replace('..', '.')
    
    # 4단계
    if new_arr[0] == '.':
        new_arr = new_arr[1:] if len(new_arr) > 1 else '.'
    if new_arr[-1] == '.':
        new_arr = new_arr[:-1]
    
    # 5단계
    if new_arr == '':
        new_arr += 'a'
    
    # 6단계
    if len(new_arr) >= 16:
        new_arr = new_arr[:15]
        if new_arr[-1] == '.':
            new_arr = new_arr[:-1]
            
    # 7단계
    while len(new_arr) < 3:
        new_arr += new_arr[-1]

    return new_arr
