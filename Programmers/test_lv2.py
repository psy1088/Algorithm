def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    for i in range(k):  # 최댓값을 저장했는데, k가 남았다면 그만큼 제거해줌
        stack.pop()

    return ''.join(stack)
