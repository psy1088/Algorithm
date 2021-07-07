from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # n=문서 개수, m=문서가 놓여있는 위치
    importance = list(map(int, input().split())) # 중요도

    q = deque(enumerate(importance))
    importance.sort(reverse=True)

    i = 0
    while True:
        val = q.popleft()
        if val[1] == importance[i]:
            i += 1
            if val[0] == m:
                break
        else:
            q.append(val)

    print(i)
