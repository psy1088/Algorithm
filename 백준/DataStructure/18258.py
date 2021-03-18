import sys
input = sys.stdin.readline

q = []
N = int(input())

start = 0
for i in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if len(q) > start:
            print(q[start])
            start += 1
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q) - start)
    elif command[0] == "empty":
        if len(q) > start:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(q) > start:
            print(q[start])
        else:
            print(-1)
    elif command[0] == "back":
        if len(q) > start:
            print(q[-1])
        else:
            print(-1)
