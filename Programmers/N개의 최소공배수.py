def lcm(x, y):
    min_val = min(x,y)
    for i in range(min_val, 0, -1):
        if x % i == 0 and y % i == 0:
            return x * y // i
            
            
def solution(arr):
    while len(arr) > 1:
        x, y = arr.pop(), arr.pop()
        arr.append(lcm(x, y))
        
    return arr[0]
