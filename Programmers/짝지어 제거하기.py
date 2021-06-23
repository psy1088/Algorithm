def solution(s):
    if len(s) % 2 != 0: # 문자열 길이가 홀수라면, 짝지어 제거하기 불가능
        return 0

    stack = []
    for i in s:
        if not stack: 
            stack.append(i)

        elif stack[-1] == i:
            stack.pop()

        else: # 스택이 비어있지 않고, 연속된 수가 아니라면 스택에 i삽입
            stack.append(i)

    if stack:
        return 0
    else:
        return 1
