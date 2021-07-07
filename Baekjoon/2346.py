import sys
input = sys.stdin.readline

n = int(input())
q = list(map(int, input().split()))
q = list(enumerate(q))

now = 0
move = 0
while q:
    if move > 0:
        now = (now + move - 1) % len(q)
    elif move < 0:
        now = (now + move) % len(q)

    print(q[now][0]+1, end=' ')
    move = q[now][1]
    q.pop(now)
