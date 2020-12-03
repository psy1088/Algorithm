
num = int(input())
data = list(map(int, input().split()))

data.sort()

total_cnt = 0 #총 그룹 수
cur_cnt = 0 #현재 그룹 수

for i in data:
    cur_cnt += 1
    if cur_cnt >= i:
        total_cnt += 1
        cur_cnt = 0

print(total_cnt)
