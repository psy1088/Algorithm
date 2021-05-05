def solution(number, k):
    stack = [number[0]]
    
    for num in number[1:]:
        while stack and (stack[-1] < num) and (0 < k):
            stack.pop()
            k -= 1    
        stack.append(num)
        
    for _ in range(k):
        stack.pop()
    
    return ''.join(stack)
    
