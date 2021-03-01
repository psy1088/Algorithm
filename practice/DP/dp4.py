# p380 병사 배치하기
N = 7
data = [15, 11, 4, 8, 5, 2, 4]

# d[i] = data[i]를 마지막 원소로 하는 수열의 최대 원소 수
d = [1] * N
for i in range(N-2, -1, -1):  # 뒤에서 2번째 원소부터 역순으로 쭉~
    for j in range(N-1, i, -1):
        if data[i] > data[j]:
            d[i] = max(d[i], d[j] + 1)

print(N - max(d))
