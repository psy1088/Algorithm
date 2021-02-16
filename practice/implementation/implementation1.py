# p321 럭키 스트레이트
N = input()
len_N = len(N)
res = 0

for i in range(len_N // 2):
    res += int(N[i])
for i in range(len_N // 2, len_N):
    res -= int(N[i])

if res == 0:
    print("LUCKY")
else:
    print("READY")
