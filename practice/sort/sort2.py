# p360 안테나

N = 4  # 집의 수
house = [5, 1, 7, 9]  # 집의 위치

# 집의 수가 4일때, 중간값인 h[1]과 h[2]의 2가지 경우는 값이 똑같을 수밖에 없음
house.sort()
mid = N // 2 - 1
print(house[mid])
