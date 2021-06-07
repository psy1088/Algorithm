from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)

for _ in range(n):
    file = input().rstrip().split('.')
    dict[file[1]] += 1

for file in sorted(dict.items()):
    print(file[0], file[1])
