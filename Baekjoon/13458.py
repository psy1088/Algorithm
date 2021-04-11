import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for student in A:
    cnt = 1
    if B < student:
        student -= B
        if student % C == 0:
            cnt += student // C
        else:
            cnt += (student // C + 1)

    result += cnt

print(result)
