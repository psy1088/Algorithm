N = int(input()) # 수열의 크기
A = list(map(int, input().split()))

d = [1 for _ in range(N)]
for i in range(1, N):
    temp = []
    for j in range(0, i):
        if A[j] < A[i]:
            temp.append(d[j])
    if temp:
        d[i] = max(temp) + 1
print(max(d))
