# 311p 모험가 길드

num = int(input()) # 인원 수 입력
data = list(map(int, input().split())) # 인원의 공포수치 입력

data.sort() # 리스트 오름차순 정렬

total_cnt = 0 # 총 그룹 수
cur_cnt = 0 # 현재 그룹 수

# 현재 그룹을 결성한 멤버의 공포도가 그 그룹의 현재 인원보다 작거나 같다면 그룹 결성
for i in data:
    cur_cnt += 1
    if cur_cnt >= i:
        total_cnt += 1
        print(cur_cnt)
        cur_cnt = 0

print("최대그룹 수 : ", total_cnt)
