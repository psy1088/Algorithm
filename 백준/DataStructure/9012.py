import sys
input = sys.stdin.readline


def check(data):
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop(-1) != '(':
                return False

    if stack:  # 스택이 비어있으면 True
        return False
    else:
        return True


T = int(input())
for _ in range(T):
    data = input().rstrip()
    if check(data):
        print("YES")
    else:
        print("NO")
