from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    com = input().split()
    if com[0] == "push_front":
        q.appendleft(int(com[1]))

    elif com[0] == "push_back":
        q.append(int(com[1]))

    elif com[0] == "pop_front":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)

    elif com[0] == "pop_back":
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)

    elif com[0] == "size":
        print(len(q))

    elif com[0] == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)

    elif com[0] == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)

    elif com[0] == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
