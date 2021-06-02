from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) >= 2:
    q.popleft()
    q.append(q.popleft())

print(q[0])
