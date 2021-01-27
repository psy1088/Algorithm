# 313p 문자열 뒤집기의 최솟값
S = input()
cur = S[0]
change_cnt = 0

# 차례로 접근하면서 숫자가 바뀌는 지점마다 cnt 증가
for i in range(1, len(S)):
    if S[i] != cur:
        change_cnt += 1
        cur = S[i]
# 바뀐 횟수가 짝수이면 cnt/2, 홀수이면 cnt+1/2
# 바뀐 횟수는 0->1 또는 1->0 일때만 카운트하는 것이므로
# cnt가 짝수라면, 0->1과 1->0이 같은 횟수로 나타날 수 밖에 없음 => cnt/2이 뒤집기의 최솟값
if change_cnt % 2 != 0:
    change_cnt += 1
result = change_cnt // 2

print(result)
