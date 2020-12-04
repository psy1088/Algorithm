# 313p 문자열 뒤집기의 최솟값
import time

start = time.time()

S = input()
temp = S[0]
cnt = 0

# 차례로 접근하면서 숫자가 바뀌는 지점마다 cnt 증가
for i in range(1, len(S)):
    if S[i] != temp:
        cnt += 1
        temp = S[i]
# 바뀐 횟수가 짝수이면 cnt/2, 홀수이면 cnt+1/2
# 바뀐 횟수는 0->1 또는 1->0 일때만 카운트하는 것이므로
# cnt가 짝수라면, 0->1과 1->0이 같은 횟수로 나타날 수 밖에 없음 => cnt/2이 뒤집기의 최솟값
if cnt % 2 == 0:
    cnt = int(cnt / 2)
else:
    cnt = int((cnt + 1) / 2)

end = time.time()

print(cnt)
print(end - start)
