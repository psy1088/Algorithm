from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    line = list(input().split())
    if line[0] == '0':
        break
    for i in combinations(line[1:], 6):
        print(" ".join(i))
    print()
