def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    for i in range(k):  # 최댓값을 구했는데, k가 남았다면, 남은 수만큼 pop
        stack.pop()

    return ''.join(stack)
