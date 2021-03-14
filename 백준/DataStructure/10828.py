import sys
input = sys.stdin.readline

N = int(input())
stack, len_stack = [], 0
for _ in range(N):  # 명령 입력받음
    command = input().rstrip().split()

    if command[0] == "push":
        stack.append(command[1])
        len_stack += 1

    elif command[0] == "pop":
        if len_stack == 0:
            print(-1)
        else:
            print(stack.pop(-1))
            len_stack -= 1

    elif command[0] == "size":
        print(len_stack)

    elif command[0] == "empty":
        print(1 if len_stack == 0 else 0)

    elif command[0] == "top":
        print(-1 if len_stack == 0 else stack[-1])
