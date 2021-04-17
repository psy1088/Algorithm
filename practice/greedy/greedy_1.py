# 311p 모험가 길드

num = int(input()) # 인원 수 입력
data = list(map(int, input().split())) # 인원의 공포수치 입력

data.sort(reverse=True) # 리스트 오름차순 정렬

total_cnt = 0 # 총 그룹 수
cur_cnt = 0 # 현재 그룹 수

start = data[0]
for i in range(num):
    cur_cnt += 1
    if cur_cnt >= start:
        total_cnt += 1
        cur_cnt = 0
        if i+1 < num:
            start = data[i+1]

print("최대그룹 수 : ", total_cnt)
