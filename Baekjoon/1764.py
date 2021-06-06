import sys
from collections import defaultdict
input = sys.stdin.readline

dict = defaultdict(int)

n, m = map(int, input().split())
for _ in range(n+m):
    dict[input().rstrip()] += 1

cnt = 0
result = []
for i in dict:
    if dict[i] == 2:
        cnt += 1
        result.append(i)

print(cnt)
print('\n'.join(sorted(result)))
